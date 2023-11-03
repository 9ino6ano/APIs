const express = require('express');
const app = express();
//https://expressjs.com/
app.get('/', (req, res) =>{
    res.send('Hello World');
});
//creating end points = return an array of 3 numbers
app.get('/api/courses', (req, res) =>{
    //res.send([1,2,3]);
    res.send(courses);
});

// Port
const port = process.env.PORT || 3000;
app.listen(port, () => {
    app.listen(port, () => console.log(`Listening on port - ${port}...`));
});

app.use(express.json()); //this method returns a piece of middleware, that could be used in pipline
//app.get('/api/courses/:id', (req, res) => {
//    res.send(req.params.id);
//});
const courses = [
    {id: 1, name: 'course1'},
    {id: 1, name: 'course2'},
    {id: 1, name: 'course3'},
];

app.post('/api/courses/', (req, res) => {
    const course = {
        id: courses.length + 1,
        name: req.body.name
    };
    courses.push(course);
    res.send(course);
});

app.get('/api/posts/:year/:month', (req, res) => {
    res.send(req.params.year);
});

app.get('/api/courses/:id', (req, res) => {
    //res.send(req.params.id);
    const course = courses.find(c => c.id === parseInt(req.params.id));
    if (!course) res.status(404).send('The course with the given ID was not found.')
    res.send(course);
});
app.listen(4000, () => console.log('Listening on port 4000...'));


//app.post()
//app.put()
//app.delete()
