---
title: Safari HTML5 Canvas Guide
apple_id: TP40010542
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/HTML-canvas-guide/CreatingGames/CreatingGames.html
archived_at: '2026-07-15T05:21:06.879322Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari HTML5 Canvas Guide](About%20Canvas.md)


[Next](Document%20Revision%20History.md)[Previous](Pixel%20Manipulation.md)

# Creating Games

Creating games involves all the subjects covered in this document up to this point: drawing shapes, images, and text; animation; adding touch and mouse controls; and triggering sounds. In addition, for many games you need to detect collisions, which may involve reading the canvas pixels.

There are several ways to detect collisions between objects in a game.

You can compare the x and y coordinates of the various elements—this is best for detecting collisions with walls or between rectangular objects.

If at least one of the objects is a shape, you can use the `isPointInPath(x,y)` method to see if a given point is inside the path—this is best for detecting collisions between missiles and shapes.

You can examine the canvas bitmap, to see if a target color is anywhere inside a given area—this is best when the target is a unique color.

The example in Listing 16-1 is the skeleton of an arcade game, as illustrated in Figure 16-1. It has a scrolling background, a ship that responds to touch or mouse control, missiles that fire when the mouse is clicked or the screen is tapped, and targets that follow a path. The game detects collisions between missiles and targets, and maintains a score that advances when a target is hit.

All the elements of a side-scrolling arcade game are present. With a little work, you can modify the skeleton to support any number of arcade shoot-em-ups.

__Figure 16-1__  Space arcade game

__Listing 16-1__  Space arcade game

```
<html>
<head>
    <title>Space Arcade Game</title>
    <meta name="viewport" content="width=600" />
    <script type="text/javascript">
        var can, ctx, back, xBack = 0, xIncr = 1,
            imgWidth = 1498, shipX = 10, shipY = 140,
            target = [1, 1, 1, 1, 1],
            targetX = [], targetY = [], targetSpeed = 1.5,
            phase = 0.1, targets = 4, bulletX, bulletY, score = 0;

        function init() {
            back = document.getElementById("back");
            can = document.getElementById("can");
            ctx = can.getContext("2d");
            ctx.font = "14pt Helvetica";
            newTargets();
            animate();
            can.addEventListener("mousemove",move, false);
            can.addEventListener("touchmove",tMove, false);
            can.addEventListener("mouseup",newBullet, false);
        }

        function newTargets() {
            for (i = 0; i < targets; i++) {
                target[i] = 1;
                targetX[i] = can.width + 10 + i * 50;
                targetY[i] = i * Math.PI / 2;
            }
        }

        // There is a maximum of 1 bullet
        // If user shoots again, old bullet is gone
        // If bulletX = 0, there is no bullet

        // User clicked mouse or lifted finger
        function newBullet(e) {
            bulletX = 35;
            bulletY = shipY + 10;
        }

        function animate() {
            model();
            drawBack();
            drawShip();
            drawBullet();
            drawTarget();
            drawScore();
            setTimeout(animate, 15);
        }

        function model() {
            // if there is a bullet, advance it
            if (bulletX)
                bulletX = bulletX + 2;
            // if the bullet goes off the right edge, zero it
            if (bulletX > can.width)
                 bulletX = 0;
             // move targets
            for (i = 0; i < targets; i++) {
                    targetX[i] -= targetSpeed;
                    targetY[i] += phase;
            }
            // if last target off left edge of screen,
            // generate new set
            if (targetX[targets - 1] < 0)
                newTargets();
        }

        function drawBack() {
                // pan background
                xBack -= xIncr;
                ctx.drawImage(back, xBack, 0);
                // draw new copy at right edge of old copy
                ctx.drawImage(back, xBack + imgWidth, 0);
                // if background scrolled off screen, reset
                if (xBack <= -1 * imgWidth)
                    xBack += imgWidth;
        }


        function drawTarget() {
            ctx.strokeStyle = "red";
            // for each target:
            for (i = 0; i < targets; i++) {
                // if target not yet hit:
                if (target[i]) {
                    // draw a circle
                    ctx.beginPath();
                    var tY = 150 + 25 * Math.sin(targetY[i]);
                    ctx.arc(targetX[i], tY, 10, 0, 2 * Math.PI);
                    ctx.closePath();
                    ctx.stroke();
                    // if bullet inside circle, target is hit
                    if (bulletX && ctx.isPointInPath(bulletX,bulletY)) {
                        target[i] = 0;
                        score = score + 10;
                    }
                }
            }
        }

        function drawShip() {
            ctx.fillStyle = "white";
            ctx.beginPath();
            ctx.moveTo(shipX, shipY);
            ctx.lineTo(shipX + 30, shipY + 10);
            ctx.lineTo(shipX, shipY + 20);
            ctx.closePath();
            ctx.fill();
        }

        function drawBullet() {
            if (bulletX)
                ctx.fillRect(bulletX, bulletY, 2, 1);
        }

        function drawScore() {
            var sc = "Score: " + score;
            ctx.fillText(sc, 10, 25);
        }

        // move ship in response to mouse
        function move(e)
        {
            if (!e)
                e = event;
            shipY = e.pageY;
            return false;
        }

        // move ship in response to touch
        function tMove(e)
        {
            if (!e)
                e = event;
            shipY = e.touches[0].pageY;
            return false;
        }
    </script>
</head>
<body onload="init()" style="background-color:black">
    <canvas id="can" height="300" width="500"
            style="position:absolute;top:0;left:0">
    </canvas>
    <img id="back" style="display:none" src="starback.png" />
</body>
</html>
```


The example in [Listing 16-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbsfvbuqmjxfvjvona) is a complete game, including sound effects, simulating a Lunar Excursion Module (LEM) landing on the moon. This game uses PNG images—scaled and rotated—as sprites over a fixed background. The game has two custom controls, a button and a slider, created using CSS-styled `div` elements, to control thrust and rotation. The controls respond to touch or mouse input. A very simple physics model adds gravity to the LEM at regular intervals. The game is illustrated in [Figure 16-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbsfvbuqmjxfvjvoni).

__Figure 16-2__  Lander game

__Listing 16-2__  Lander game

```
<html>
<head>
    <title>lander</title>
    <meta name="viewport" content="width=900" />
    <style>
        .myButton {
            position: absolute;
            top: 420px;
            left: 170px;
            border: 4px outset red;
            background-color: #C0C0C0;
            width: 75px;
            padding: 10px;
            text-align: center;
            border-radius: 18px;
        }
        .myButton.pressed {
            border: 4px inset red;
            background-color: #808080;
        }
        .slider {
            position: absolute;
            top: 410px;
            left: 500px;
            width: 152px;
            height: 52px;
        }
        .bar {
            position: relative;
            top: 30px;
            width: 152px;
            height: 2px;
            background-color: red;
        }
        .knob {
            position: relative;
            left: 0;
            border: 2px solid red;
            background-color: #C0C0C0;
            width: 50px;
            height: 50px;
            border-radius: 25px;
            text-align: center;
        }
    </style>
    <script type="text/javascript">
        var can, ctx, back, sprite, flames, flag, offset, slider,
            t, interval, scale, sound, thrustButton, knob, knobMid,
            x = 30, y = 30, lemH = 88, lemW = 88, gravity = 0.02,
            yVector = 0, xVector = 1.2, thrust = 0.2, fuel = 250,
            delay = 100, theta = 0, bottom = 380, mouseIsDown = 0,
            thrustIsDown = 0, gameOver = 0;

        function init() {
            can = document.getElementById("can");
            ctx = can.getContext('2d');
            back = document.getElementById("back");
            sprite = document.getElementById("sprite");
            flames = document.getElementById("flames");
            flag = document.getElementById("flag");
            sound = document.getElementById("sound");
            thrustButton = document.getElementById("thrustButton");
            slider = document.getElementById("slider");
            knob = document.getElementById("knob");
            knobMid = knob.offsetWidth / 2;
            setKnob(75);
            document.body.addEventListener("mouseup", mouseUp, true);
            x = 30;
            y = 30;
            yVector = 0;
            xVector = 1.2;
            theta=0;
            fuel = 250;
            drawAll();
            interval = setInterval("addGravity()",delay);
            update();
        }

        function restart() {
            sound.src="noise.m4a";
            sound.load();
            clearTimeout(t);
            clearInterval(interval);
            gameover = 0;
            init();
        }

        function drawAll() {
            drawBack();
            drawStatus();
            drawFuel();
            drawSprite();
        }

        function drawBack() {
            ctx.drawImage(back, 0, 0);
            ctx.fillStyle = "yellow";
            ctx.font = "36pt Helvetica";
            ctx.fillText("Loony Lander", 300, 50);
        }

        function drawStatus() {
            var dispX = parseInt(xVector * 100) / 100;
            var dispY = parseInt(yVector * 100) / 100;
            var dispRot = parseInt(theta * 100) / 100;
            var status = "Velocity X: " + dispX + "  Y: " + dispY + "  Rot: " + dispRot;
            ctx.font = "18pt Helvetica";
            ctx.fillText(status, 285, 100);
        }

        function drawFuel() {
            ctx.shadowColor = "rgba(0, 0, 0, 0)";
            ctx.font = "14pt Helvetica";
            ctx.globalAlpha = 0.5;
            ctx.fillText("Fuel:", 52, 375);
            ctx.fillRect(100, 360, fuel, 20);
            ctx.globalAlpha = 1;
        }

        function drawSprite() {
            ctx.save();
            ctx.translate(x,y);
            scale = 0.5 + (y / 600);
            offset = -1 * lemW * scale / 2
            ctx.shadowColor = "black";
            ctx.shadowOffsetX = 10;
            ctx.shadowOffsetY = -5;
            ctx.rotate(theta);
            ctx.drawImage(sprite, offset, offset, lemW * scale, lemH * scale);
            ctx.restore();
        }

        function addGravity() {
            yVector += gravity * scale;
        }

        function gameOver() {
            gameover = 1;
            clearTimeout(t);
            clearInterval(interval);
            if (y == bottom && yVector < 1 && Math.abs(xVector) < 1 && Math.abs(theta) < .1) {
                theta = 0;
                drawAll();
                ctx.drawImage(flag, x - 50, y - 120);
                ctx.font = "14pt Helvetica";
                ctx.fillStyle = "green";
                ctx.fillText("Nice landing!", x, 280);
                sound.src = "chord.m4a";
            } else {
                theta = 1.75;
                drawAll();
                ctx.font = "14pt Helvetica";
                ctx.fillStyle=  "red";
                ctx.fillText("Oops. Hard landing.", x, 280);
                sound.src = "ohno.m4a";
            }
            sound.play();
        }

        function update() {
            x += xVector;
            y += yVector;
            if (y >= bottom) {
                y = bottom;
                gameOver();
            } else {
                t = setTimeout(update, delay);
                drawAll();
             }
        }

        function burn() {
            if (fuel > 0 && y < bottom) {
                clearTimeout(t);
                yVector -= thrust * scale * Math.cos(theta);
                xVector += thrust * scale * Math.sin(theta);
                fuel -= 5;
                ctx.save();
                ctx.globalAlpha = .75;
                ctx.shadowColor="rgba(0, 0, 0, 0)";
                ctx.translate(x, y);
                ctx.rotate(theta);
                ctx.drawImage(flames, offset, offset, lemW * scale, lemH * scale);
                ctx.restore();
                t = setTimeout(update, delay);
                if (thrustIsDown) {
                    sound.play();
                    setTimeout(burn, 200);
                }
            }
        }

        function mouseDown() {
            mouseIsDown = 1;
        }

        function mouseUp() {
            mouseIsDown = 0;
        }

        function thrustDown() {
            sound.play();
            thrustIsDown = 1;
            thrustButton.className = "myButton pressed";
            burn();
        }

        function thrustUp() {
            thrustIsDown = 0;
            thrustButton.className = "myButton";
        }

        function mouseXY(e) {
            if (mouseIsDown) {
                if (!e)
                    var e = event;
                var mouseX = e.pageX - slider.offsetLeft;
                if (mouseX >= 0 && mouseX <= slider.offsetWidth ) {
                    setKnob(mouseX);
                }
            }
        }

        function touchXY(e) {
            if (!e)
                var e = event;
            // slide, don't scroll
            e.preventDefault();
            var touchX = e.touches[0].pageX - slider.offsetLeft;
            if (touchX >= 0 && touchX <= slider.offsetWidth) {
                setKnob(touchX);
            }
        }

        function setKnob(x) {
            var knobX = x - knobMid;
            knobX = Math.max(knobX, 0);
            knobX = Math.min(knobX, slider.offsetWidth - knob.offsetWidth);
            knob.style.left = knobX;
            if (!gameover) {
                theta = (x - 75) / 75;
                drawSprite();
            }
        }
    </script>
</head>
<body onload="init()">
    <img id="back" src="lunarsurface.jpg" style="display:none" />
    <img id="sprite" src="lem.png" style="display:none" />
    <img id="flames" src="flames.png" style="display:none" />
    <img id="flag" src="flag.png" style="display:none" />

    <audio id="sound" src="noise.m4a"></audio>

    <canvas id="can" height="436" width="810">
    </canvas>

    <div id="thrustButton" class="myButton"
         onmousedown="thrustDown()" onmouseup="thrustUp()"
         ontouchstart="thrustDown()" ontouchend="thrustUp()">
        Thrust
    </div>

    <div id="slider" class="slider"
         onmousedown="mouseDown()" onmousemove="mouseXY()"
         ontouchstart="touchXY()" ontouchmove="touchXY()">
        <div class="bar"></div>
        <div id="knob" class="knob">
            <br />
            Spin
        </div>
    </div>

    <br />
    <h2 style="text-align:center">
        To win, land with velocity X < 1, Y < 1, Rot < 0.1
    </h2>
    <input type="button" value="Restart" onclick="restart()" />
</body>
</html>
```

[Next](Document%20Revision%20History.md)[Previous](Pixel%20Manipulation.md)

