const express = require('express')

const app = express()

app.get('/', (request, response) => {
  response.send('<h1>Welcome to User Service v1.3</h1>')
})

app.listen(4000, '0.0.0.0', () => {
  console.log('server started on port 4000')
})
