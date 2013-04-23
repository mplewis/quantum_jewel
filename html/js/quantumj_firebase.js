var firebaseUrl = 'https://quantumj.firebaseIO.com/'

var firebaseRef = new Firebase(firebaseUrl);
var testRef = firebaseRef.child('main_board');
testRef.on('value', function(dataSnap) {
	var data = dataSnap.val();
	var row;
	var gem;
	console.log('New board!');
	for (var i = 0; i < data.length; i++) {
		row = data[i]
		console.log(row);
	};
});

console.log('Ready!');