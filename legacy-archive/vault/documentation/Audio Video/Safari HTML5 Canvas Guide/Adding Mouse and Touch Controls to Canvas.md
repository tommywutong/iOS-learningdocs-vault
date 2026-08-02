---
title: Safari HTML5 Canvas Guide
apple_id: TP40010542
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/HTML-canvas-guide/AddingMouseandTouchControlstoCanvas/AddingMouseandTouchControlstoCanvas.html
archived_at: '2026-07-15T05:21:02.723386Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari HTML5 Canvas Guide](About%20Canvas.md)


[Next](Adding%20Sound%20to%20Canvas%20Animations.md)[Previous](Modifying%20the%20Canvas%20with%20CSS.md)

# Adding Mouse and Touch Controls to Canvas

Because the `canvas` element works both on the desktop and in iOS, it can be interacted with by either mouse or touch. This section shows you how to create canvas webpages that respond equally well to both mouse and touch input.

Because the `canvas` element responds to JavaScript, you can include controls for the canvas anywhere on the page. This chapter covers four input variants.

- Control using standard HTML inputs elsewhere on the page
- Superimposing standard inputs on the canvas
- Responding to mouse and touch events on the canvas generally
- Creating custom controls on the canvas

There are a few things to bear in mind when using standard HTML inputs with canvas.

Text input fields bring up the soft keyboard on iOS-based devices, covering the lower half of the screen. Make sure the relevant parts of the canvas aren’t obscured by the keyboard, or choose a different kind of input.

Selection input fields with alternates bring up the rotary picker on iPhone and iPod touch, again covering the lower half of the screen. Make sure the relevant parts of the canvas aren’t obscured by the picker, or choose a different kind of input.

Button inputs with default settings tend to be quite small on iPhone and iPod touch. To make buttons easier to find with a finger, try setting a smaller viewport or a larger initial scale using the `<meta>` tag, or making the button font larger using the CSS `font` style.

The example in Listing 13-1 sets the viewport width to 300, the initial scale to 2, and the input font to `larger` and `bold`, resulting in large, easy-to-push buttons on iPhone and iPod touch. The desktop version is illustrated in Figure 13-1.

__Figure 13-1__  Big buttons

__Listing 13-1__  Make big buttons

```
<html>
<head>
    <title>Big Buttons</title>
    <!-- zoom in for iOS-based devices -->
    <meta name="viewport" content="width=300" />
    <meta name="viewport" content="initial-scale=2" />
    <style>
        input { font: larger bold; }
        canvas { background-color: black; }
    </style>
    <script type="text/javascript">
        var can, ctx, hun, n = 0;

        function init() {
            can = document.getElementById("can");
            ctx = can.getContext("2d");
            hun = document.getElementById("hundred");
            ctx.fillStyle = "rgb(64, 255, 64)";
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";
            ctx.font = "24pt Helvetica";
            showN();
        }

        function showN() {
            ctx.clearRect(0, 0, can.width, can.height, 99);
            ctx.fillText(n, can.width / 2, can.height / 2);
        }

        function incr() {
            n++;
            showN();
        }

        function decr() {
            n--;
            showN();
        }

        function setHundred() {
            n = hun.value;
            showN();
        }
    </script>
</head>
<body onload="init()">
    <canvas id="can" height="100" width="100">
    </canvas>
    <br />
    <input type="button" value=" + " onclick="incr()">
    <input type="button" value=" - " onclick="decr()">
    <select id="hundred" onchange="setHundred()">
        <option value=0> -- </option>
        <option value=100> 100 </option>
        <option value=-100> -100 </option>
    </select>
</body>
</html>
```


You can superimpose standard HTML inputs—or custom inputs—on the canvas simply by declaring the inputs after the `<canvas>` tag and using CSS to position the inputs on top of the canvas.

The inputs cover any graphics or animation drawn on the canvas.

The example in Listing 13-2 positions a pair of buttons and a selector on top of the canvas, as illustrated in Figure 13-2.

__Figure 13-2__  Controls on canvas

__Listing 13-2__  Putting controls on canvas

```
<html>
<head>
    <title>Controls on Canvas</title>
    <!-- fill iPhone screen with canvas -->
    <meta name="viewport" content="width=200" />
    <meta name="viewport" content="initial-scale=2" />
        <script type="text/javascript">
            var can, ctx, hun, n = 0;

            function init() {
                can = document.getElementById("can");
                ctx = can.getContext("2d");
                hun = document.getElementById("hundred");
                showN();
            }

            function showN() {
                // large, centered, bright green text
                ctx.font = "24pt Helvetica";
                ctx.textAlign = "center";
                ctx.textBaseline = "middle";
                ctx.fillStyle = "rgb(64, 255, 64)";
                ctx.clearRect(0, 0, can.width, can.height);
                // draw text at center, max length to fit on canvas
                ctx.fillText(n, can.width /2, can.height / 2, can.width - 2);
            }

            function incr() {
                n++;
                showN();
            }

            function decr() {
                n--;
                showN();
            }

            function setHundred() {
                n = hun.value;
                showN();
            }
        </script>
</head>
<body onload="init()">
    <!-- give canvas rounded corners-->
    <canvas id="can" height="200" width="200" style="background-color:black; border-radius:25px;">
    </canvas>
    <br />
    <!-- float inputs over canvas -->
    <div style="position:relative; top:-50; left:25">
        <input type="button" value=" + " onclick="incr()">
        <input type="button" value=" - " onclick="decr()">
        <select id="hundred" onchange="setHundred()">
            <option value=0> -- </option>
            <option value=100> 100 </option>
            <option value=-100> -100 </option>
        </select>
    </div>
</body>
</html>
```


For some applications, you don’t need a specific input object—just a way to respond to mouse and touch events on the canvas as a whole.

Install event listeners on the `canvas` element for `mousedown` or `click` events, and install event listeners on the `body` element for `mouseup` events, in case a mouse event begins on the canvas and ends off the canvas. Similarly, listen for `touchstart` and `touchend` events on the canvas, but listen for `touchcancel` events on the HTML body.

To obtain the mouse or touch coordinates in terms of the canvas, get the `pageX` and `pageY` properties, then subtract the canvas’s `offsetLeft` and `offsetTop` properties.

By default, dragging a finger in iOS pans the browser window. To allow touch to flow smoothly over the canvas on iOS, prevent the default panning behavior by adding `preventDefault()` to your `touchstart` event handler.

The example in Listing 13-3 tracks mouse and touch movements that originate on the canvas, displaying the canvas coordinates and whether the mouse button or finger is down. The results are displayed on the canvas, as shown in Figure 13-3.

__Figure 13-3__  Tracking events on canvas

The example listens for `mousemove` or `touchmove` events on the canvas to track the mouse or finger position on the canvas. The example also listens for `mousedown` and `mouseup`, or `touchstart` and `touchend`, to determine if the mouse button or finger is down. Note that the mouse is still tracked when the mouse button is released, but when the finger is lifted off the screen, there is no touch to track. The example then shows the current x,y position and state (up or down) of the mouse or touch, and draws a white cursor at that position on the canvas.

Only a single touch event is tracked; additional simultaneous touches are ignored. To obtain all the touch events that begin on the canvas, iterate through the event’s `targetTouches` array. See [Tracking Multiple Touches and Testing for Hits](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbsfvbuqmjufvjvonq) for details.

__Listing 13-3__  Track mouse and touch events

```
<html>
<head>
    <!-- fill iPhone screen with canvas -->
    <meta name="viewport" content="width=400" /
    <title>Tracking Mouse and Touch Events on Canvas</title>
    <script type="text/javascript">
        var can, ctx, canX, canY, mouseIsDown = 0;

        function init() {
            can = document.getElementById("can");
            ctx = can.getContext("2d");

            can.addEventListener("mousedown", mouseDown, false);
            can.addEventListener("mousemove", mouseXY, false);
            can.addEventListener("touchstart", touchDown, false);
            can.addEventListener("touchmove", touchXY, true);
            can.addEventListener("touchend", touchUp, false);

            document.body.addEventListener("mouseup", mouseUp, false);
            document.body.addEventListener("touchcancel", touchUp, false);
        }

        function mouseUp() {
            mouseIsDown = 0;
            mouseXY();
        }

        function touchUp() {
            mouseIsDown = 0;
            // no touch to track, so just show state
            showPos();
        }

        function mouseDown() {
            mouseIsDown = 1;
            mouseXY();
        }

        function touchDown() {
            mouseIsDown = 1;
            touchXY();
        }

        function mouseXY(e) {
            if (!e)
                var e = event;
            canX = e.pageX - can.offsetLeft;
            canY = e.pageY - can.offsetTop;
            showPos();
        }

        function touchXY(e) {
            if (!e)
                var e = event;
            e.preventDefault();
            canX = e.targetTouches[0].pageX - can.offsetLeft;
            canY = e.targetTouches[0].pageY - can.offsetTop;
            showPos();
        }

        function showPos() {
            // large, centered, bright green text
            ctx.font = "24pt Helvetica";
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";
            ctx.fillStyle = "rgb(64,255,64)";
            var str = canX + ", " + canY;
            if (mouseIsDown)
                str += " down";
            if (!mouseIsDown)
                str += " up";
            ctx.clearRect(0, 0, can.width, can.height);
            // draw text at center, max length to fit on canvas
            ctx.fillText(str, can.width / 2, can.height / 2, can.width - 10);
            // plot cursor
            ctx.fillStyle = "white";
            ctx.fillRect(canX -5, canY -5, 10, 10);
        }
    </script>

</head>
<body onload="init()">
    <canvas id="can" height="200" width="300" style="background-color:black">
    </canvas>
</body>
</html>
```


The example in Listing 13-4 draws an endless series of descending red bubbles on the canvas, as illustrated in Figure 13-4. Clicking the mouse on a bubble, or touching a bubble with a finger on iOS, pops the bubble.

This example tracks up to four simultaneous touch events, allowing the user to pop up to four bubbles at a time on iOS-based devices.

The example uses `isPointInPath()` to test each bubble against each touch. The length of the touches array is stored in a global variable, and the variable is updated whenever a touch starts, ends, or is canceled.

__Figure 13-4__  Bubbles

__Listing 13-4__  Track multiple touches

```
<html>
<head>
    <!-- fill iPhone screen with canvas -->
    <meta name="viewport" content="width=400" />
    <title>Pop the Bubbles</title>
    <script type="text/javascript">
        var can, ctx,
            canX = [], canY = [], bubble = [],
            mouseIsDown = 0, len = 0;

        function init() {
            can = document.getElementById("can");
            ctx = can.getContext("2d");

            can.addEventListener("mousedown", mouseDown, false);
            can.addEventListener("mousemove", mouseXY, false);
            can.addEventListener("touchstart", touchDown, false);
            can.addEventListener("touchend", touchUp, false);
            can.addEventListener("touchmove", touchXY, false);

            document.body.addEventListener("mouseup", mouseUp, false);
            document.body.addEventListener("touchcancel", touchUp, false);
            for (i = 0; i < 4; i++) {
                bubble[i] = 0;
            }
            animate();
        }

        function mouseUp() {
            mouseIsDown = 0;
            mouseXY();
        }

        function mouseDown() {
            mouseIsDown = 1;
            mouseXY();
        }

        function touchDown() {
            mouseIsDown = 1;
            touchXY();
        }

        function touchUp(e) {
            if (!e)
                e = event;
            len = e.targetTouches.length;
        }

        function mouseXY(e) {
            if (!e)
                e = event;
            canX[0] = e.pageX - can.offsetLeft;
            canY[0] = e.pageY - can.offsetTop;
            len = 1;
        }

        function touchXY(e) {
            if (!e)
                e = event;
            e.preventDefault();
            len = e.targetTouches.length;
            for (i = 0; i < len; i++) {
                canX[i] = e.targetTouches[i].pageX - can.offsetLeft;
                canY[i] = e.targetTouches[i].pageY - can.offsetTop;
            }
        }

        function animate() {
            ctx.strokeStyle = "red";
            ctx.clearRect(0,0, can.width, can.height);
            // create a path for each bubble
            for (i = 0; i < 4; i++) {
                bubble[i]++;
                if (bubble[i] >= can.height + 10)
                    bubble[i] = -10;
                var y = bubble[i];
                var x = (i + 1) * 50;
                var radius = 20;
                ctx.beginPath();
                ctx.arc(x, y, radius, 0, 2 * Math.PI);
                ctx.closePath();
                // test each extant touch to see if it is on the bubble
                for (j = 0;j < len; j++) {
                    if (ctx.isPointInPath(canX[j], canY[j]) && mouseIsDown)
                        bubble[i] = -30;
                }
                ctx.stroke();
            }
            setTimeout(animate, 40);
        }
    </script>
</head>
<body onload="init()">
    <canvas id="can" height="200" width="300" style="background-color:black">
    </canvas>
</body>
</html>
```


You can draw any kind of control you like on the canvas, and use the techniques described in [Responding to Mouse and Touch Events on Canvas](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbsfvbuqmjufvjvomjq) to determine if the input is on your custom control, but there is a faster and better way to implement most custom controls.

If your custom control is part of the canvas itself, the control is just a graphic, not a targetable element. Consequently, you need to track all touches on the canvas, and compare the coordinates of each touch to each control you draw. It can get complicated.

A better approach is to build the control using HTML and CSS, then position the control on top of the canvas using CSS. Your control can still be a graphic image—or multiple images—alpha channels in images are automatically composited onto the underlying canvas.

By creating the control as an element in HTML, you can make the control a target for mouse and touch events. That way, Safari sorts the touches for you, and you can respond to touches on the control itself. There’s no need to compare multiple touches with multiple controls, or to track the mouse or finger coordinates at all.

To add a custom button to the canvas, create an HTML `div` or `img` element and use CSS to style the element and position it on top of the canvas.

Add a listener function for `touchstart` and `mousedown` events to detect a custom button being pressed, and add a listener function for `touchend` and `mouseup` events to detect the button being released. You might want to take an action when the button is pressed or when it is released, or both.

Add a state variable to track whether the button is pressed or released.

Add a listener function for `mouseup` events to the page as a whole, in case the user clicks your button, then moves the mouse pointer off your button before releasing the mouse button.

Similarly, add a listener function for `touchcancel` events to the page as a whole, in case the touch is canceled for some reason (such as an incoming phone call, for example).

The example in Listing 13-5 creates a `div` element, styles it as a button, and positions it on the canvas. When the button is clicked or touched, the button state changes and a different style is applied to the button. The canvas also changes, in this case to blue. When the touch ends or the mouse button is released, the button style reverts to the unpressed state and the canvas changes to black. The results are illustrated in Figure 13-5.

__Figure 13-5__  Clicking a custom button

The listener functions are added to the button and the HTML body using HTML attributes, such as `onmousedown` and `ontouchstart`.

__Listing 13-5__  Creating a custom button on canvas

```
<html>
<head>
    <title>Custom Button</title>
    <meta name="viewport" content="width=300" />
    <meta name="viewport" content="initial-scale=2" />
    <style>
        .myButton {
            position: relative;
            top: -60px;
            left: 10px;
            border: 4px outset #c0c0c0;
            background-color: #e0e0e0;
            width: 100px;
            padding: 10px;
            text-align: center;
            border-radius: 18px;
        }

        .mybutton.pressed {
            border: 4px outset black;
            background-color: #808080;
        }
    </style>
    <script type="text/javascript">
        var can, ctx, but1, but1press;

        function init() {
            but1 = document.getElementById("but1");
            can = document.getElementById("can");
            ctx = can.getContext("2d");
            but1press = 0;
        }

        function press1() {
            // change state variable
            but1press = 1;
            // change button style
            but1.className = "myButton pressed";
            // do something on the canvas
            ctx.fillStyle = "beige";
            ctx.fillRect(0, 0, can.width, can.height);
        }

        function release1() {
            // button 1 may or may not be pressed when mouse button comes up
            // or touch ends.
            // if button is pressed, release it and do something on the canvas
            if (but1press) {
                but1press = 0;
                // revert button style
                but1.className = "myButton";
                // do something on the canvas
                ctx.fillStyle = "white";
                ctx.fillRect(0, 0, can.width, can.height);
            }
        }
    </script>
</head>
<body onload="init()" onmouseup="release1()" ontouchcancel="release1()">
    <canvas id="can" height="200" width="300">
    </canvas>
    <div id="but1" class="myButton"
         onmousedown="press1()" onmouseup="release1()"
         ontouchstart="press1()" ontouchend="release1()">
        Click Me
    </div>
</body>
</html>
```


A slider is a useful control for user input having a fixed range. A slider consists of a knob and a bar for the knob to slide on. The range of the slider can be anything, but the number of dragable steps is constrained by the length of the bar. To create a slider with a range of `n1` to `n2` in 100 steps, for example, you need to create a bar at least 100 pixels long—a single pixel is the minimum finger-controllable movement of the knob.

A slider can be a graphic image, but you can also use CSS to style a set of nested `div` elements to act as a slider, using only text.

On iOS-based devices, the minimum comfortable size for the knob on a slider is 44 x 44 pixels. A circle of radius 25 meets these criteria and makes a comfortable target for a finger.

To build a slider, listen for `mousedown`, `mousemove`, `touchbegin`, and `touchmove` events on the slider element. Listen for `mouseup` events on the `body` element and track the mouse button state.

Begin your touch event handlers with `preventDefault()` to allow the finger to drag the slider instead of scrolling the page.

Position the knob relative to the bar using CSS. The slider has a dragable range from 0 to the width of the bar, minus the width of the knob. For example, for a circular knob of radius 25, the minimum bar width is 150 pixels to allow 100 dragable steps while keeping the knob on the bar.

The knob value is the mouse or touch event’s `pageX` property, minus the slider’s `offsetLeft` property. The knob should be positioned half its width to the left of the knob value, so the mouse or finger drags the center of the knob. The knob value should be clamped at 0 and the bar width minus the knob width.

The example in Listing 13-6 creates a slider using three nested `div` elements. The outermost `div` element is the slider and is positioned absolutely. The two inner `div` elements are the bar and the knob, and are positioned relatively within the slider. The bar `div` is styled into a horizontal line and the knob `div` is styled into a circle using CSS.

The knob is 52 pixels wide, including the border, and the bar is 152 pixels wide, giving the slider a positional range of 0-100. The slider is used to scale a graphic from a size of 0.25 to 0.75 in 100 steps, to demonstrate that the value range driven by the slider is not constrained by the positional range. The result is illustrated in Figure 13-6.

__Figure 13-6__  Slider controlling image size

The knob value is displayed and the image is redrawn in an independent animation loop, so as not to overload the event handlers and make them unresponsive. The knob is repositioned using CSS, by setting the `offsetLeft` property. Safari redraws the knob automatically.

__Listing 13-6__  Adding a slider using CSS

```
<html>
<head>
    <title>Custom Slider</title>
    <!-- Fill the iOS screen /-->
    <meta name="viewport" content="width=400" />
    <style>
        canvas {
            position: absolute;
            top: 10px;
            left: 10px;
            background-color: beige;
            border-radius: 25px;
            border: 1px solid #404040;
        }
        .slider {
            position: absolute;
            top: 115px;
            left: 85px;
            width: 152px;
            height: 52px;
        }
        .bar {
            position: relative;
            top: 30px;
            width: 152px;
            height: 2px;
            background-color: #404040;
        }
        .knob {
            position: relative;
            left: 0;
            border: 1px solid #404040;
            background-color: #c0c0c0;
            width: 50px;
            height: 50px;
            border-radius: 25px;
        }
    </style>
    <script type="text/javascript">
        var can, ctx, image, slider,
            knob, mouseIsDown, knobMid;

        function init() {
            slider = document.getElementById("slider");
            knob = document.getElementById("knob");
            image = document.getElementById("image");
            can = document.getElementById("can");
            ctx = can.getContext("2d");
            mouseIsDown = 0;
            knobMid = knob.offsetWidth / 2;
            margin = can.offsetLeft - 1;
            textInit();
            showVal();
        }

        function textInit() {
            ctx.fillStyle = "blue";
            ctx.font = "24pt Helvetica";
            ctx.textAlign = "center";
            ctx.textBaseline = "bottom";
        }

        function showVal() {
            // value goes from 0 to slider-width minus knob width
            var sliderVal = knob.offsetLeft;
            ctx.save();
            ctx.clearRect(0, 0, can.width, can.height);
            var scale = .25 + sliderVal / 200;
            ctx.scale(scale, scale);
            ctx.drawImage(image, 0, 0);
            ctx.restore();
            ctx.fillText(sliderVal, can.width / 2, can.height - 5);
            setTimeout(showVal, 25);
        }

        function mouseDown() {
            mouseIsDown = 1;
            mouseXY();
        }

        function mouseUp() {
            mouseIsDown = 0;
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
        }
    </script>
</head>
<body onload="init()" onmouseup="mouseUp()">
    <canvas id="can" height="200" width="300">
    </canvas>
    <div class="slider" id="slider"
         onmousedown="mouseDown()" onmousemove="mouseXY()"
         ontouchstart="touchXY()" ontouchmove="touchXY()">
        <div class="bar"></div>
        <div id="knob" class="knob"></div>
    <div>
    <img id="image" style="display:none" src="butterfly1.png" />
</body>
</html>
```

[Next](Adding%20Sound%20to%20Canvas%20Animations.md)[Previous](Modifying%20the%20Canvas%20with%20CSS.md)

