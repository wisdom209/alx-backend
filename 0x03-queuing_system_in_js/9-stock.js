const express = require('express')
const redis = require('redis')
const { promisify } = require('util')
const client = redis.createClient({
	redis: {
		host: '127.0.0.1',
		port: 6379
	}
})

const listProducts = [
	{ Id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
	{ Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
	{ Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
	{ Id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
]

let listProductsInitial = listProducts.map(v => {
	v.initialAvailableQuantity = v.stock;
	v.currentQuantity = v.stock
	delete v.stock
	return v
})

const getItemById = (id) => {
	return listProductsInitial.filter(v => v.Id == id)[0]
}

const reserveStockById = (itemId, stock) => {
	client.set(itemId, stock)
}

const getCurrentReservedStockById = async (itemId) => {
	const redisAsyncGet = promisify(client.get).bind(client)
	const reserved = await redisAsyncGet(`${itemId}`)
	if (!reserved) return getItemById(itemId).currentQuantity
	return Number(reserved)

}

const app = express()

app.get('/list_products', (req, res) => {
	const returnList = listProductsInitial.map(v => {
		let {currentQuantity, ...withoutCurrentQuantity} = v
		return withoutCurrentQuantity
	})
	res.send(returnList)
})


app.get('/list_products/:itemId', async (req, res) => {
	let currentQuantity = await getCurrentReservedStockById(Number(req.params.itemId))

	let item = getItemById(req.params.itemId)

	if (!item) return res.status(404).send({ status: "Product not found" })
	
	item = { ...item, currentQuantity}
	
	res.send(item)
})


app.get('/reserve_product/:itemId', async (req, res) => {
	let item = getItemById(req.params.itemId)
	
	if (!item)
		return res.status(404).send({ status: "Product not found" })

	let currentQuantity = await getCurrentReservedStockById(req.params.itemId)

	if (currentQuantity && currentQuantity != 0){
		
		reserveStockById(req.params.itemId, item.currentQuantity - 1)
		item.currentQuantity = item.currentQuantity - 1

		return res.send({ "status": "Reservation confirmed", "itemId": Number(req.params.itemId) })
	}

	res.send({ "status": "Not enough stock available", "itemId": req.params.itemId })

})

const port = 1245

client.on('connect', () => {
	app.listen(port, 'localhost')
})

