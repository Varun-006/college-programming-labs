import express, { json } from 'express'; // Use require instead of import
const app = express();
app.use(json()); // This is required to parse JSON data

app.get('/', (req, res) => {
    res.send('Hello, World!');
});
const products = [
    {
        id: 1,
        name: "mi"
    },
    {
        id: 2,
        name: "iphone"
    },
    {
        id: 3,
        name: "oppo"
    }
]
app.get('/products', (req, res) => {
    res.send(products);
});

app.get('/products/:id', (req, res) => {
    const newData = products.filter(item => item.id.toString() === req.params.id)
    res.send(newData);
});

app.post('/addproducts', (req, res) => {
    const { id, name } = req.body;
    const newProduct = { id, name };
    products.push(newProduct);
    res.send(newProduct);
});

app.put('/updateproducts/:id', (req, res) => {
    const product = products.find(item => item.id.toString() === req.params.id);
    Object.assign(product, req.body);
    res.send(product);
});

app.delete('/deleteproducts/:id', (req, res) => {
    const index = products.findIndex(item => item.id.toString() === req.params.id);
    const deletedProduct = products.splice(index, 1);
    res.send(deletedProduct);
});

app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});
