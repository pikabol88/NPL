const express = require('express');
const bodyParser = require('body-parser');
const MongoClient = require('mongodb').MongoClient



const app = express();
const port = 3000;
const connectionString = "mongodb+srv:/YOUR_USERNAME:YOUR_PASSWORD@cluster0.amhmp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"



MongoClient.connect(connectionString)
    .then(client => {
        const db = client.db('users-feedbacks')
        const feedbacksCollection = db.collection('feedbacks')

        app.set('view engine', 'ejs')

        app.use(bodyParser.urlencoded({ extended: true }))

        app.listen(port, () => {
            console.log(('listening on 3000'))
        })

        app.get('/', (req, res) => {
            db.collection('feedbacks').find().toArray()
            .then(result => {
                res.render('index.ejs', {feedbacks:result})  
            })
            .catch(error => console.log(error))        
        });

        
        app.post('/feedbacks', (req, res) => {
            feedbacksCollection.insertOne(req.body)
            .then(result => {
                res.redirect('/')                
            })
            .catch(error=>console.error(error))
        })        

    }).catch(error => console.error(error))
