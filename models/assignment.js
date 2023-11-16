let mongoose = require('mongoose');

let assignment = mongoose.Schema({
    Name:String,
    Due_Date:String,
    Completed:String,
    Grade: Number
},
{
    collection:"assignments"
});
module.exports = mongoose.model('Assignment', assignment);
