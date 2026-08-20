---
title: iSudoku
apple_id: DTS10004395
resource_type: Sample Code
platform: Safari|iOS
topic: General
technology: null
published: '2007-10-29'
source_url: https://developer.apple.com/library/archive/samplecode/iSudoku/Listings/iSudoku_js.html
archived_at: '2026-07-18T03:29:45.538231Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iSudoku](iSudoku.md)


[Next](iSudokuChooser.html.md)[Previous](iSudoku.css.md)

# iSudoku.js

```
/*

 File: iSudoku.js 

 Abstract: JavaScript for the index.html file
           Demonstrates use of Puzzle2x2 object that implements a 2x2 Sudoku game.

 Version: <1.0>

 Disclaimer: IMPORTANT:  This Apple software is supplied to you by 
 Apple Inc. ("Apple") in consideration of your agreement to the
 following terms, and your use, installation, modification or
 redistribution of this Apple software constitutes acceptance of these
 terms.  If you do not agree with these terms, please do not use,
 install, modify or redistribute this Apple software.

 In consideration of your agreement to abide by the following terms, and
 subject to these terms, Apple grants you a personal, non-exclusive
 license, under Apple's copyrights in this original Apple software (the
 "Apple Software"), to use, reproduce, modify and redistribute the Apple
 Software, with or without modifications, in source and/or binary forms;
 provided that if you redistribute the Apple Software in its entirety and
 without modifications, you must retain this notice and the following
 text and disclaimers in all such redistributions of the Apple Software. 
 Neither the name, trademarks, service marks or logos of Apple Inc. 
 may be used to endorse or promote products derived from the Apple
 Software without specific prior written permission from Apple.  Except
 as expressly stated in this notice, no other rights or licenses, express
 or implied, are granted by Apple herein, including but not limited to
 any patent rights that may be infringed by your derivative works or by
 other works in which the Apple Software may be incorporated.

 The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
 MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
 THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS
 FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
 OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

 IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
 OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
 MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
 AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
 STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.

 Copyright (C) 2007 Apple Inc. All Rights Reserved.

 */
document.puzzle = null;

function Puzzle2x2() {
    this.badSquares = new Object();
    this.board = new Object();
    this.mask = new Object();
    this.solved = false;
    this.width = 2;
    this.height = 2;
    this.maximumValue = this.width * this.height;

    // Load board
    for (var i = 0; i < this.maximumValue; i++) {
        for (var j = 0; j < this.maximumValue; j++) {
            this.board[i+","+j] = arguments[i * this.maximumValue + j];

        }
    }

    // Load mask
    for (var i = this.maximumValue; i < arguments.length; i++) {
        this.mask[arguments[i]] = 1;
    }

}

/* Utility function for going from a tuple (2,2, e.g.) to the DOM ID */
Puzzle2x2.prototype.tupleToID = function(tuple) {
    var id = "cell" + parseInt(tuple.substring(0, tuple.indexOf(','))) + ":";
    id += parseInt(tuple.substring(tuple.indexOf(',') + 1));
    return id;
}

/* Utility function for going from a DOM ID ("cell2:2", e.g.) to a tuple */
Puzzle2x2.prototype.IDToTuple = function(id) {
    var tuple = parseInt(id.substring(4, id.indexOf(":"))) + ",";
    tuple += parseInt(id.substring(id.indexOf(":") + 1));
    return tuple;
}

/* Set up digits on the board */
Puzzle2x2.prototype.setup = function() {
   for (var i = 0; i < this.maximumValue; i++) {
        for (var j = 0; j < this.maximumValue; j++) {
            var tuple = i + "," + j;
            var element = document.getElementById(this.tupleToID(tuple));
            if (this.mask[tuple]) { 
                element.style.backgroundColor = '#dddddd';
                element.textContent = this.board[tuple];
                element.onclick = null;
            }
            else {
                element.style.backgroundColor = 'white';
                element.textContent = ' ';
                element.onclick = function() { document.puzzle.choose(this.id); };
            }
        }
    }
}

/* Displays the the content of the file associated with chooser-iframe
chooser-iframe loads iSudokuChooser.html by default */
Puzzle2x2.prototype.choose = function(id) {
    var chooser = document.getElementById('chooser-iframe');
    chooser.style.position = 'absolute';
    chooser.style.zIndex = '1';
    chooser.style.display = 'block';
    chooser.contentDocument.id = id;
}

/*Set chooser-iframe to display iSudokuSuccess.html   */
Puzzle2x2.prototype.success = function(){
    var chooser = document.getElementById('chooser-iframe');
    var lastId=chooser.contentDocument.id;

    chooser.setAttribute("src", "iSudokuSuccess.html");
    this.choose(lastId);
}

/* Displays a congratulation message if the player successfully filled out the board*/
Puzzle2x2.prototype.gameOver = function() {

    for (var i = 0; i < this.maximumValue; i++) {
        for (var j = 0; j < this.maximumValue; j++) {
            var id = this.tupleToID(i + "," + j);
            document.getElementById(id).onclick = null;
        }
    }

    this.success();

}


/*  Returns true if a player succesfully filled out the board */
Puzzle2x2.prototype.isSolved = function() {
    return this.solved;
}

/* Sets a value at a given cell of the board */  
Puzzle2x2.prototype.setValue = function(position, value) {
    document.getElementById(position).textContent = value;

    if (value) {
        var oldBadSquares = this.badSquares;
        this.badSquares = new Object();

        // Revalidate the whole board
        this.validate("0,0"); 
        this.validate("1,2"); 
        this.validate("2,1"); 
        this.validate("3,3");

        // Iterate through the previous bad squares and reset them to
        // to a normal background if they aren't in the new listing of
        // bad squares. 
        for (var tuple in oldBadSquares) {
            if (! this.badSquares[tuple]) {
                var elementID = this.tupleToID(tuple);
                document.getElementById(elementID).style.backgroundColor = 'white';
            }
        }

        // Iterate through our new bad squares and make sure that we 
        // mark any squares not previously in our bad squares as red.
        // We also adjust our bad square count for use later.
        var countBadSquares = 0;
        for (var tuple in this.badSquares) {
            countBadSquares++;
            if (! oldBadSquares[tuple]) {
                var elementID = this.tupleToID(tuple);
                document.getElementById(elementID).style.backgroundColor = 'red';
            }
        }

        // If we have no bad squares then we check to ensure that every 
        // square is filled.  If it is, then they game is done.  If not,
        // the game continues!
        if (countBadSquares == 0) {
            var isDone = true;
            for (var i = 0; i < this.maximumValue; i++) {
                for (var j = 0; j < this.maximumValue; j++) {
                    var tuple = i + "," + j;
                    if (this.board[tuple] != document.getElementById(this.tupleToID(tuple)).textContent) {
                        isDone = false;
                    }
                }
            }
            if (isDone) {
                this.solved = true;
                this.gameOver();
            }
        }
    }
}


/* Check each row and column for duplicated values */
Puzzle2x2.prototype.validate = function(tuple) {

    var box = parseInt(tuple.substring(0, tuple.indexOf(',')));
    var square = parseInt(tuple.substring(tuple.indexOf(',') + 1));

    // Validate square
    this.validateTuple(box + ",0", box + ",1", box + ",2", box + ",3");
    // Validate row;
    var rowBox = (box % 2 == 0) ? (box + 1) : (box - 1);
    var rowSquare = (square % 2 == 0) ? (square + 1) : (square - 1);
    this.validateTuple(box + "," + square, box + "," + rowSquare, rowBox + "," + square, rowBox + "," + rowSquare);

    // Validate column
    var colBox = (box % 2 == 0) ? (box + 2) % 4 : (box + 2) % 4;
    var colSquare = (square % 2 == 0) ? (square + 2) % 4 : (square + 2) % 4;
    this.validateTuple(box + "," + square, box + "," + colSquare, colBox + "," + square, colBox + "," + colSquare);
}


/* Compare two values  */
Puzzle2x2.prototype.validateTuple = function() {
    var check = new Array();
    for (var i = 0; i < arguments.length; i++) {

        var element = document.getElementById(this.tupleToID(arguments[i]));

        if (element && element.textContent && element.textContent != ' ') {
            var value = element.textContent;
            if (! check[value]) {
                check[value] = new Array();
            }

            check[value][check[value].length] = element;
        }
    }
    for (var i in check) {
        if (check[i].length > 1) {
            for (var j = 0; j < check[i].length; j++) {
                var element = check[i][j];
                var tuple = this.IDToTuple(element.id);
                if (! this.mask[tuple]) {
                    this.badSquares[tuple]++;

                }
            }
        }
    }
}


var games = new Array();
games[0] = "new Puzzle2x2(1,2,4,3,3,4,2,1,3,4,2,1,1,2,4,3,'0,0','1,2','2,1','3,3')";
games[1] = "new Puzzle2x2(2,1,3,4,4,3,1,2,4,3,1,2,2,1,3,4,'0,3','1,1','2,2','3,0')";
games[2] = "new Puzzle2x2(4,3,2,1,2,1,4,3,3,4,1,2,1,2,3,4,'1,1','0,2','2,1','3,2')";
games[3] = "new Puzzle2x2(3,4,1,2,1,2,3,4,4,3,2,1,2,1,4,3,'0,0','1,3','2,3','3,0')";
games[4] = "new Puzzle2x2(2,3,4,1,4,1,2,3,3,2,1,4,1,4,3,2,'0,1','1,2','2,3','3,0')";

var lastGameIndex = -1;

/* Used to create a board  with random numbers for the iSudoku game */
function setupPuzzle() {
    var gameIndex = Math.floor(Math.random() * games.length);
    while (gameIndex == lastGameIndex) {
         gameIndex = Math.floor(Math.random() * games.length);     
    }

    lastGameIndex = gameIndex;

    document.puzzle = eval(games[gameIndex]);
    document.puzzle.setup();
}
```

[Next](iSudokuChooser.html.md)[Previous](iSudoku.css.md)

