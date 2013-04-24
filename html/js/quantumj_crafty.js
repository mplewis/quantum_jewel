Game = {
    // Initialize and start our game
    boardSize: {
        canvasWidth:  480, // px
        canvasHeight: 480,
        numGemsX:     8,   // gems horizontal
        numGemsY:     8,   // gems vertical
        gemWidth:     60,  // px
        gemHeight:    60
    },
    gemColors: [ // red, orange, yellow, green, blue, purple, white
        'rgb(255,   0,   0)',
        'rgb(255, 102,   0)',
        'rgb(255, 255,   0)',
        'rgb(  0, 255,   0)',
        'rgb(  0,   0, 255)',
        'rgb(128,   0, 128)',
        'rgb(255, 255, 255)',
    ],
    start: function() {
        // Start crafty and set a background color so that we can see it's working
        Crafty.init(Game.boardSize.canvasWidth, Game.boardSize.canvasHeight);
        Crafty.background('black');
    },
    drawBoard: function(liveBoard) {
        for (var y = 0; y < Game.boardSize.numGemsY; y++) {
            for (var x = 0; x < Game.boardSize.numGemsX; x++) {
                var gemColor = liveBoard[y][x];
                var gemColorRGB = Game.gemColors[gemColor];
                xDraw = x * Game.boardSize.gemWidth;
                yDraw = y * Game.boardSize.gemHeight;
                newGem = Crafty.e('2D, Canvas, Color, Mouse')
                    .attr({
                        x: xDraw,
                        y: yDraw,
                        w: Game.boardSize.gemWidth,
                        h: Game.boardSize.gemHeight
                    })
                    .color(gemColorRGB)
                    .bind('MouseDown', function() {
                        console.log(this.xCoord, this.yCoord);
                    });
                newGem.xCoord = x;
                newGem.yCoord = y;
            }
        }
    }
}

window.addEventListener('load', Game.start);