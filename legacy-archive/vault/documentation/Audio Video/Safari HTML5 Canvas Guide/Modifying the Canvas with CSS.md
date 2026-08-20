---
title: Safari HTML5 Canvas Guide
apple_id: TP40010542
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/HTML-canvas-guide/ModifyingtheCanvaswithCSS/ModifyingtheCanvaswithCSS.html
archived_at: '2026-07-15T05:21:14.392876Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari HTML5 Canvas Guide](About%20Canvas.md)


[Next](Adding%20Mouse%20and%20Touch%20Controls%20to%20Canvas.md)[Previous](Animating%20the%20Canvas.md)

# Modifying the Canvas with CSS

Because the canvas is an HTML element, you can use CSS styles to modify its position, assign it a background color or image, add a border, and so on.

In Safari and other WebKit-based browsers, you can use WebKit transitions to smoothly animate changes in CSS properties.

Because the canvas can have a transparent background, you can use CSS to create animated graphics that roam freely across the webpage.

The example in Listing 12-1 uses CSS to assign a background image and a border to the canvas element, as illustrated in Figure 12-1.

A CSS background does not appear in the canvas bitmap, so it does not interfere with image processing.

The `clearRect(x,y, width,height)` method clears a section of the canvas, revealing the CSS background, allowing you to use a background image and clear small areas of the canvas quickly, without redrawing the background image.

__Figure 12-1__  CSS bulletin board

!

__Listing 12-1__  Adding a CSS background and border

```
<html>
<head>
    <title>Background Image and Border</title>
    <style>
        canvas {
            background-image: url('cork.png');
            border: 10px inset brown;
        }
    </style>
    <script type="text/javascript">
        function init() {
            var can = document.getElementById("can");
            var ctx = can.getContext("2d");
            ctx.fillStyle = "white";
            ctx.fillRect(25,25,120,100);
            ctx.font = "24pt Helvetica";
            ctx.fillStyle = "black";
            ctx.fillText("Notice:", 30, 55);
        }
    </script>
</head>
<body onload="init()">
    <canvas id="can" height="200" width="400">
    </canvas>
</body>
</html>
```


You can make the canvas element into a pop-up that responds to a hover, click, or rollover event on another webpage element.

Begin by using CSS to position the canvas element offscreen or make it transparent. When the event occurs that triggers the pop-up, use CSS to change the canvas top, left, or opacity properties to make the canvas appear at the appropriate place on the page.

If you set the position and opacity properties as `-webkit-transition` properties, any changes are automatically animated in Safari and other WebKit-based browsers. In non-WebKit-based browsers, the changes take place immediately and the canvas simply appears in the specified position.

The example in Listing 12-2 creates a canvas and uses CSS to position it offscreen and make it transparent by default. Touching or clicking and holding a particular text element on the page changes the class name of the canvas. The CSS class definition makes the canvas visible and positions it on the page. A `mouseup` event anywhere on the page changes the canvas’s class name to hide it again.

All CSS properties are set as `webkit-transition` properties for the canvas element, so the canvas fades in and out over 1 second in Safari. The canvas is given a CSS background image and a border, and animates a bouncing ball, just for fun.

__Figure 12-2__  Animating a pop-up canvas

__Listing 12-2__  Making the canvas a pop-up

```

<html>
<head>
    <title>Pop-up Canvas</title>
    <meta name="viewport" content="width=device-width" />
    <style>
        canvas {
            background-image:url('cork.png');
            border: 10px inset brown;
            position:absolute;
            top: -225;
            left: 200;
            -webkit-transition: all 1s;
        }

        .can-hide {
            top: -225;
            opacity: 0;
        }

        .can-pop {
            top: 120;
            opacity:1;
        }
    </style>
    <script type="text/javascript">
        var can, ctx,
            x = 25, y = 25;
            xdir = 1, ydir = 1;

        function init() {
            can = document.getElementById("can");
            ctx = can.getContext("2d");
            var grad = ctx.createLinearGradient(0, 10, 0, 190);
            grad.addColorStop(0, 'brown');
            grad.addColorStop(1, 'red');
            ctx.fillStyle = grad;
            animate();
        }

        function animate() {
            x += xdir;
            if (x > 375)
                xdir = -1;
            if (x < 25)
                xdir = 1;

            y += ydir;
            if (y > 175)
                ydir = -1;
            if (y < 25)
                ydir = 1;

            ctx.clearRect(0, 0, 400, 200);
            ctx.beginPath();
            ctx.arc(x, y, 25, 0, 2 * Math.PI);
            ctx.closePath();
            ctx.fill();
            setTimeout(animate, 25);
        }

        function pop() {
            can.className = "can-pop";
        }

        function unpop() {
            can.className = "can-hide";
        }
    </script>
</head>
<body onload="init()" onmouseup="unpop()">
    <canvas class="can-hide" id="can" height="200" width="400">
    </canvas>
    <h1>Click to view:<h1>
    <h1 onmousedown="pop()" ontouchstart="pop()" onclick="void()">
        &nbsp;[x] Bulletin Board</h1>
</body>
</html>
```


The static webpage is a paradigm we’re all familiar with. Video, animated banners, and pop-ups notwithstanding, things are laid out in boxes, and they tend to stay in boxes.

Because the canvas element can have a transparent background, and because it supports alpha channel compositing on the fly, it offers a way to visually break the static boxes paradigm.

When the canvas itself is animated using CSS, animated images on the canvas appear to range freely about the page, covering or casting shadows on other elements.

The example in [Listing 12-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbsfvbuqmjtfvjvonq) creates a simple animated butterfly, then moves the canvas using CSS to allow the butterfly to wander across the page, as shown in Figure 12-3.

__Figure 12-3__  Butterfly

__Listing 12-3__  Making a free-roaming canvas

```
<html>
<head>
    <title>Butterfly</title>
    <script type="text/javascript">
        var can, ctx,
            sprite = [],
            counter = 0, rot = 0,
            centerX = -176, centerY = -127,
            canX = 0, canY = 225;

        function init() {
            can = document.getElementById("can");
            ctx = can.getContext("2d");
            // get images into array
            sprite[0] = document.getElementById("b1");
            sprite[1] = document.getElementById("b2");
            sprite[2] = document.getElementById("b3");
            sprite[3] = document.getElementById("b4");
            // set shadow color, offset, blur
            ctx.shadowColor = "rgba(80, 80, 80, .3)";
            ctx.shadowBlur = "5";
            ctx.shadowOffsetX = "10";
            ctx.shadowYOffsetY = "20";
            // draw butterfly
            draw();
            // wait 3 sec, then begin animation
            var t = setTimeout(flap, 3000);
        }

        function flap() {
            // flap wings four times quickly, then wait randomly up to 1.5sec
            var wait = 40;
            counter++;
            if (counter == 4) {
                counter = 0;
                wait += Math.random() * 1500;
                rot += .01;
            }
            // draw butterfly, move canvas, repeat
            draw();
            moveCan();
            setTimeout(flap, wait);
        }

        function draw() {
            // draw rotated: translate to x,y; rotate; draw at 0,0, offset to center
            ctx.clearRect(0, 0, can.width, can.height);
            ctx.save();
            ctx.translate(can.width / 2, can.height / 2);
            ctx.rotate(rot);
            ctx.drawImage(sprite[counter], centerX, centerY);
            ctx.restore();
        }

        function moveCan() {
            canX += 1;
            canY -= 2;
            if (canY < -80)
                canY = -80;
            if (canX > 400)
                canX = 400;
            // use CSS style to move canvas
            can.style.left = canX;
            can.style.top = canY;
        }
    </script>
</head>
<body onload="init()" onmousedown="moveToMouse()">
    <h1>Butterfly</h1>
    <p>Why are they called butterflies?</p>
    <p>Shouldn't they be flutter-bys?</p>
    <h2>but-ter-fly</h2>
    <p><i>--noun</i></p>
    <ol>
        <li>any of numerous diurnal insects of the order Lepidoptera, characterized by clubbed antennae, a slender body, and large, broad, often conspicuously marked wings.</li>
        <li>a person who flits aimlessly from one interest or group to another: a social butterfly.</li>
        <li>butterflies, ( used with a plural verb ) Informal . a queasy feeling, as from nervousness, excitement, etc.</li>
    </ol>
    <img id="b1" style="display:none" src="butterfly1.png" >
    <img id="b2" style="display:none" src="butterfly2.png" >
    <img id="b3" style="display:none" src="butterfly3.png" >
    <img id="b4" style="display:none" src="butterfly4.png" >
    <canvas id="can" height="380" width="380" style="position:absolute;left:0;top:225">
    </canvas>
</body>
</html>
```

[Next](Adding%20Mouse%20and%20Touch%20Controls%20to%20Canvas.md)[Previous](Animating%20the%20Canvas.md)

