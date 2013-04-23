var canvasWidth  = 480; // px
var canvasHeight = 480;
var numGemsX     = 8;   // gems horizontal
var numGemsY     = 8;   // gems vertical

Game = {
    // Initialize and start our game
    start: function() {
        // Start crafty and set a background color so that we can see it's working
        Crafty.init(canvasWidth, canvasHeight);
        Crafty.background('black');
    }
}

window.addEventListener('load', Game.start);