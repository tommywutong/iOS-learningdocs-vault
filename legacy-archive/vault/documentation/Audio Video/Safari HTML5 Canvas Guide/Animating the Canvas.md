---
title: Safari HTML5 Canvas Guide
apple_id: TP40010542
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/HTML-canvas-guide/AnimatingtheCanvas/AnimatingtheCanvas.html
archived_at: '2026-07-15T05:21:05.473257Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari HTML5 Canvas Guide](About%20Canvas.md)


[Next](Modifying%20the%20Canvas%20with%20CSS.md)[Previous](Creating%20Charts%20and%20Graphs.md)

# Animating the Canvas

You can use canvas for animations as well as static images. Animation is a series of graphic images shown one after another, the same way that video is a series of still images. If the sequential images are similar to one another, and the time between images is short, the eye is fooled into seeing continuous motion.

You can easily use the `canvas` element to produce images that differ from each other slightly, and the canvas element is designed to support smooth, rapid changes between images.

The JavaScript methods `setTimeout()` and `setInterval()` can be used to redraw the canvas at precise repeating intervals.

Animation involves repeatedly clearing the canvas and drawing an image on it. To create smooth animations, you need to minimize the time between clearing the canvas and completing the new drawing, and you need to keep the changes relatively small from image to image.

You can use a sequence of predrawn images to change the appearance of some elements from frame to frame, substituting one image for another. You can also change the rotation, scale, or position of a predrawn image, or of a path or shape.

For smooth animation, use the following sequence:

1. Model—Calculate small changes in image substitution, position, rotation, color, or scale.
2. Clear—Clear part or all of the canvas.
3. Draw—Draw any images, using the pre-calculated values. Stroke or fill any paths, shapes, or strings.
4. Repeat steps 1-3.

If you have an opaque background image or shape that fills the canvas, or the part of the canvas you are animating, you can skip step 2. Drawing the background has the effect of “clearing” the canvas to your background.

As with static images, you should draw the elements in order, from backmost to frontmost, so your foreground images are superimposed on any background.

When using predrawn images in the foreground, use SVG images or PNG images on transparent backgrounds, to allow automatic alpha-channel compositing.

When changing the scale or rotation of an element, save the context by calling `save()`, change the scale or rotation of the canvas, translating the canvas as needed, draw the element, then restore the context by calling `restore()`.

Use `setTimeout()` for animations that repeat conditionally, and `setInterval()` for animations that repeat indefinitely.

For examples, see [A Simple Animation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbsfvbuqmjsfvjvoni) and [Intermittent Animation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbsfvbuqmjsfvjvonq).

Animation is smoothest when you make the changes between frames as incremental as possible, and the time between frames as short as possible.

Try not to move objects more than two or three pixels per frame. This means keeping incremental values such as gravity or thrust quite small, to prevent them from accumulating and resulting in jerky movement.

Try to keep changes in rotation down to 0.1 radians per frame. Less is better.

Changes in scale should be kept to 0.2 or less per frame.

If making small changes results in slow animation, you can decrease the time between cycles.

A timeout value of 40 ms results in a refresh rate of 25 fps. This is a good minimum refresh rate—the same as PAL television and a touch faster than cinema’s 24 fps. A timeout value of 20 ms yields a frame rate of 50 fps, which should be fast enough for any animation.

You can see exactly how long your animation function takes to execute on the desktop by creating a JavaScript profile. To profile your script, follow these steps.

1. Enable the Developer menu in Safari preferences.
2. Choose Develop > Show Web Inspector.
3. Click the Profiles icon and enable profiling when prompted.
4. With your website loaded and your script running, click the record button (the black circle on the lower left), wait a second, and click it again. This generates a profile.
5. Click the icon of the profile.
6. Choose Tree view, and reveal the operations to find your _animate()_ function.
7. Toggle the view from % to ms.

   You should see a profile similar to the one shown in Figure 11-1.

   __Figure 11-1__  Animation profile

   !!

The total time spent in your `animate()` function and all its subsidiary calls is shown in the Total column. The number of calls is shown in the Calls column. Divide the total by the number of calls to get the timing for a single call. (The Average column shows the average for the `animate()` function alone, with none of its subsidiary calls.)

If your animation function takes longer to execute than the timeout value, you have a bug. If the values are close, you may have a problem on handheld devices.

One way to avoid timing problems is to use `setTimeout()` instead of `setInterval()`, and set the timeout as the last step in your `animate()` function. This guarantees that your animation function is completed before being called again.

Using `setTimeout()` can result in uneven timing, however, especially if your modeling code has long and short branches. Using `setInterval()` guarantees the same frame rate for all code branches, on all devices, but you must allow enough time for the longest branch to execute on the slowest device.

[Listing 11-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbsfvbuqmjsfvjvomy), generates a continuous animation of a bouncing soccer ball, as shown in [Figure 11-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbsfvbuqmjsfvjvomi).

__Figure 11-2__  Animated soccer ball

The soccer ball rotates as it falls, and bounces from the bottom and sides of the canvas. The rotation direction changes when the ball bounces off the side.

The canvas has a clear background, allowing the webpage background to show through. The `canvas` element is positioned using CSS to overlap the heading in the `<h2>` tag, so the ball covers part of the heading at times.

During the `model()` step, an x-increment is added to the x position, and a y-increment is added to the y position. A `gravity` constant is added to the y-increment, so the ball realistically moves faster as it drops and moves slower as it bounces up, eventually stopping and falling again.

The `model()` step also checks for a bounce condition, and reverses the x or y increment if needed.

Because the animation is based on a model, instead of a canned series of images, it does not simply repeat—the ball follows a slightly different path each time it bounces.

During the `draw()` step, the canvas is translated to the ball’s x,y-coordinate and rotated. The ball is then drawn with its center at 0,0.

There is a -75 pixel offset from the upper-left corner of the ball image to the center of the ball. This pixel offset is stored in a variable named `centerOffset`, and the image of the ball is drawn at `centerOffset`, `centerOffset` to put the ball’s center at 0,0.

__Listing 11-1__  Creating a simple animation

```
<html>
<head>
    <title>Simple Animation</title>
    <script type="text/javascript">
        var can, ctx, ball,
            x, y, xVec, yVec,
            direc, interval,
            rot = 0,
            gravity = 1,
            left = 75,
            right = 525,
            bottom = 325,
            centerOffset = -75;

        function init() {
            ball = document.getElementById("ball");
            can = document.getElementById("can");
            ctx = can.getContext("2d");
            ctx.strokeStyle = "black";
            // initialize position, speed, spin direction
            x = 98;
            y = 75;
            xVec = 5.5;
            yVec = 0;
            direc = 1;
            // draw lines for the ball to bounce off of
            ctx.moveTo(0, bottom + 75);
            ctx.lineTo(600, bottom+ 75);
            ctx.lineTo(600, 0)
            ctx.stroke();
            // set animation to repeat every 40 ms
            interval = setInterval(animate, 40);
        }

        function animate() {
            model();
            // clear canvas except for lines at edge
            ctx.clearRect(0, 0, can.width - 1 , can.height - 1);
            draw();
        }

        function model() {
            rot += .1 * direc;
            x += xVec;
            yVec += gravity;
            y += yVec;
            bounceIf();
        }

        function bounceIf() {
            if (y >= bottom) {
                y = bottom;
                yVec = -1 * yVec - gravity
            }
            if (x >= right || x <= left) {
                xVec *= -1;
                direc *= -1;
            }
        }

        function draw() {
            ctx.save();
            ctx.translate(x, y);
            ctx.rotate(rot);
            ctx.drawImage(ball, centerOffset,centerOffset);
            ctx.restore();
        }
    </script>
</head>
<body onload="init()" style="background-color:#e0e0e0">
    <h2>Simple Animation</h2>
    <img id="ball" src="http://homepage.mac.com/qt4web/soccerball1.png" style="display:none" />
    <canvas id="can" height="400" width="600" style="position:relative;top:-50">
    </canvas>
</body>
</html>
```


You can overlay runtime-generated shapes on predrawn images. Let’s take the previous example and overlay the soccer ball with a shape, filled with a gradient. This allows you to make the ball any color you like and add a lighting effect at the same time, as shown in Figure 11-3.

__Figure 11-3__  Animation with gradient fill

The following snippet defines a radial gradient the size of the soccer ball that goes from white at 80% opacity at the center to blue at 30% opacity at the outer edge.

```
var grad;
function makeGradient() {
    grad = ctx.createRadialGradient(0, 0, 10, 0, 0, 75);
    grad.addColorStop(0, 'rgba(255, 255, 255, 0.8)');
    grad.addColorStop(1, 'rgba(0, 0, 255, 0.3)');
}
```

This next snippet redefines `draw()` to draw a circle filled with the gradient on top of the soccer ball (the radius of the circle is 73 pixels).

```
var twoPi = Math.PI * 2;
function draw() {
    ctx.save();
    ctx.translate(x, y);
    ctx.rotate(rot);
    ctx.drawImage(ball, centerOffset,centerOffset);
    ctx.fillStyle = grad;
    ctx.beginPath();
    ctx.arc(0,0, 73, 0, twoPi);
    ctx.closePath;
    ctx.fill();
    ctx.restore();
}
```

To add the gradient-filled overlay to the example in [Listing 11-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbsfvbuqmjsfvjvomy), paste in the first snippet, add a call to `makeGradient()` in the `init()` function, and replace the `draw()` function with the second snippet.

Listing 11-2 animates a butterfly whose wings flap intermittently. The animation is achieved by substituting images of a butterfly with wings in different positions. The example uses shadows and rotation to make the animation more realistic. The output is shown in Figure 11-4.

__Figure 11-4__  Flapping butterfly

Because the animation is intermittent, `setTimeout()` is used instead of `setInterval()`. A short timeout of 40 ms is used during a flap, and a longer, random interval is used between flaps.

__Listing 11-2__  Creating an intermittent animation

```

<html>
<head>
    <title>Butterfly</title>
    <script type="text/javascript">
        var can, ctx;
        var sprite = new Array();
        var counter = 0;
        var rot = 0;
        var centerX = -200;
        var centerY = -148;

        function init() {
            can = document.getElementById("can");
            ctx = can.getContext("2d");
            // get images into array
            sprite[0] = document.getElementById("b1");
            sprite[1] = document.getElementById("b2");
            sprite[2] = document.getElementById("b3");
            sprite[3] = document.getElementById("b4");
            // set shadow color, offset, blur
            ctx.shadowColor = "rgba(80,80,80,.3)";
            ctx.shadowBlur = "5";
            ctx.shadowOffsetX = "10";
            ctx.shadowYOffsetY = "20";
            // draw butterfly
            draw();
            // wait 3 sec, then begin animation
            var t = setTimeout(flap, 3000);
            }

        function flap() {
            var wait = 40;
            counter++;
            if (counter == 4) {
                counter = 0;
                wait += (Math.random() * 1500);
                rot += .01;
            }
            draw();
            setTimeout(flap, wait);
        }

        function draw() {
            ctx.clearRect(0, 0, can.width, can.height);
            ctx.save();
            ctx.translate(can.width / 2, can.height / 2);
            ctx.rotate(rot);
            ctx.drawImage(sprite[counter], centerX, centerY);
            ctx.restore();
        }
    </script>
</head>
<body onload="init()">
    <h1>Butterfly</h1>
    <p>Why are they called butterflies?</p>
    <p>Shouldnt they be flutter-bys?</p>
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
    <canvas id="can" height="450" width="450" style="position:absolute;left:0;top:225">
    </canvas>
</body>
</html>
```


Sometimes you want to animate the background. To create a panning background, start by creating an image that is wider than the canvas, and whose left edge and right edge are very similar. Then follow these steps:

1. Draw the image at an ever-decreasing x-coordinate.

   This pans the image to the left.
2. When the x-coordinate is less than the image width minus the canvas width, draw a second copy of the image at x + the image width.

   This draws a new copy with the left edge flush with the old copy’s right edge.
3. When the x-coordinate is less than the negative image width, add the image width to the x-coordinate.

   The first copy has scrolled off the screen, so reset the x-coordinate and start over.

The example in Listing 11-3 creates a background image that pans smoothly across the canvas, as illustrated in Figure 11-5.

__Figure 11-5__  Panning background

__Listing 11-3__  Adding a panning background

```
<html>
<head>
    <title>Simple Panning Background</title>
    <script type="text/javascript">
        var can, ctx, back;
            x, imgWidth = 1498;

        function init() {
            back = document.getElementById("back");
            can = document.getElementById("can");
            ctx = can.getContext("2d");
            x = 0;
            animate();
        }

        function animate() {
            x--;
            drawBack();
            setTimeout(animate, 25);
        }

        function drawBack() {
            ctx.drawImage(back, x, 0);
            if (x < -1 * (imgWidth - can.width))
                ctx.drawImage(back, x + imgWidth, 0);
            if (x <= -1 * imgWidth)
                x += imgWidth;
        }
    </script>
</head>
<body onload="init()">
    <h2>Simple Panning Background</h2>
    <canvas id="can" height="500" width="500">
    </canvas>
    <img id="back" style="display:none" src="landscape.png" />
</body>
</html>
```


A simple panning background tends to have a flat look to it, because we expect nearby things to move faster when panning. The example in Listing 11-4 creates a more realistic panning background by dividing the background image into three parts—the sky, the landscape, and the guardrail in the foreground—and panning each part at a different speed.

To support three layers of background, the image, the x increment, and the x and y coordinates are made into arrays, and the background drawing function is made into a loop that cycles through all three layers.

A line of text is added to illustrate an image floating over a panning background, as shown in Figure 11-6.

__Figure 11-6__  Layered background

__Listing 11-4__  Adding a layered panning background

```
<html>
<head>
    <title>Layered Panning Background</title>
    <script type="text/javascript">
        var can, ctx;
        var back = [];
        var x = [0, 0, 0];
        var y = [ 0, -2, 376];
        var xIncr = [0.3, 1, 4];
        var imgWidth = 1498;

        function init() {
            back[0] = document.getElementById("sky");
            back[1] = document.getElementById("back");
            back[2] = document.getElementById("front");
            can = document.getElementById("can");
            ctx = can.getContext("2d");
            animate();
        }

        function animate() {
            drawBack();
            setTimeout(animate, 25);
        }

        function drawBack() {
            for (i = 0; i < 3; i++) {
                x[i] -= xIncr[i];
                ctx.drawImage(back[i], x[i], y[i]);
                if (x[i] < -1 * (imgWidth - can.width))
                    ctx.drawImage(back[i], x[i] + imgWidth, y[i]);
                if (x[i]<= -1 * imgWidth)
                    x[i] += imgWidth;
            }
        }
    </script>
</head>
<body onload="init()" >
    <canvas id="can" height="500" width="600">
    </canvas>
    <h1 style="position:relative; top:-300; left: 125; color:#ffffff">Grand Canyon Vacation</h1>
    <img id="sky" style="display:none" src="sky.png" />
    <img id="back" style="display:none" src="landscape2.png" />
    <img id="front" style="display:none" src="foreground.png" />
</body>
</html>
```

[Next](Modifying%20the%20Canvas%20with%20CSS.md)[Previous](Creating%20Charts%20and%20Graphs.md)

