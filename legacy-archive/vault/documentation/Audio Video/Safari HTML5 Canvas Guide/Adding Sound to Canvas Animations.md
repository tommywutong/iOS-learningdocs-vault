---
title: Safari HTML5 Canvas Guide
apple_id: TP40010542
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/HTML-canvas-guide/AddingSoundtoCanvasAnimations/AddingSoundtoCanvasAnimations.html
archived_at: '2026-07-15T05:21:03.868124Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari HTML5 Canvas Guide](About%20Canvas.md)


[Next](Pixel%20Manipulation.md)[Previous](Adding%20Mouse%20and%20Touch%20Controls%20to%20Canvas.md)

# Adding Sound to Canvas Animations

Canvas provides the visual tools for creating animations, slide shows, and games, but to complete a rich media experience you typically want to add sound as well. To add sound to a canvas-based animation or game, use the HTML5 `<audio>` element, controlled by the same JavaScript that controls your canvas animation.

This section provides a brief summary of using HTML5 audio in the context of creating canvas-based rich media websites. For a more in-depth discussion of HTML5 audio and video, see _[Safari HTML5 Audio and Video Guide](../Safari%20HTML5%20Audio%20and%20Video%20Guide/About%20HTML5%20Audio%20and%20Video.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmrt)_.

Adding HTML5 audio to your canvas presentation on the desktop is simple—just include an `<audio>` tag and use the JavaScript `play()` method.

On iOS, it’s slightly more complicated. Because the user may be viewing your website over a cellular connection, paying for data by the megabyte, and because audio uses a lot of data, Safari on iOS downloads audio only as a direct result of user action. You can’t programmatically load and play audio unless the user authorizes it by clicking a button.

Currently, iOS supports playback of a single audio stream at a time when playing audio inline on a website.

Currently, the `loop` attribute for HTML5 audio is not supported on iOS.

To include audio in your canvas presentation, and have it work on the desktop and iOS, follow these steps:

- Include an “Enable sound” button to initiate playback.
- Use a single HTML5 audio element for all your sounds.
- To play different sounds, change the `src` property of the audio element.
- If your game includes background music as well as sound effects, make the background music available in iTunes or another iOS app that can play music in the background while the user plays your game, and trigger the sound effects one by one from within your game.
- If you need to have your audio track loop, listen for the `ended` event on the audio element, then call the `play()` method to restart the sound.

A soundtrack is a single audio source—such as music or a voice-over—that plays during your presentation. The audio source can loop or be timed to match the canvas presentation.

To add a soundtrack, create an `audio` element in your HTML and use the `play()` method to start it. If your presentation includes a “Start” button, the same button can initiate the presentation and play the audio, providing iOS compatibility.

The simplest way to add a soundtrack is to include the `controls` attribute in the `<audio>` tag. You can use CSS to position the audio controller on the canvas if you like. By installing an event listener on the audio element, you can use the audio controller’s start button to start your animation as well.

The amount of time between the user pressing the play button and the start of the sound varies—file size, audio format, and network speed are all factors. To synchronize your animation more closely with the start of the audio, install an event listener on the `audio` element and begin your animation when the `"playing"` event is triggered. You can also pause your animation when the audio element’s `pause` or `ended` events are triggered.

The example in Listing 14-1 uses an `<audio>` tag with the `controls` attribute to add a user-initiated soundtrack to the canvas, and animates a gradient when the music is playing, as illustrated in Figure 14-1.

__Figure 14-1__  Soundtrack

__Listing 14-1__  Adding a simple soundtrack

```
<html>
<head>
    <title>Animated Gradient with Sound Track</title>
    <!-- Fill the iOS screen /-->
    <meta name="viewport" content="width=400" />
    <style>
        canvas {
            position: absolute;
            top: 10px;
            left: 10px;
            border-radius: 25px;
            border: 1px solid #404040;
        }
        audio {
            position: absolute;
            top: 195px;
            left: 60px;
        }
    </style>
    <script type="text/javascript">
        var can, ctx, audio,
        var timer, angle = 0;

        function init() {
            audio = document.getElementById("audio");
            can = document.getElementById("can");
            ctx = can.getContext("2d");
            audio.addEventListener("playing", drawGradient, false);
            audio.addEventListener("pause", stop, false);
            audio.addEventListener("ended", stop, false);
        }

        function stop() {
            clearTimeout(timer);
        }

        function drawGradient() {
            // increment angle slowly from 0 to 2 PI
            angle += 0.1;
            if (angle >= 6.2)
                angle = 0;
                // create gradient that goes from bottom to top of canvas
            var grad = ctx.createLinearGradient(0,can.height, 0,0);

            // start gradient at black
            grad.addColorStop(0, 'black');

            // create changing rgb color values that go from 0 to 255
            var gAngle = angle + Math.PI / 2;
            var bAngle = gAngle + Math.PI;
            var r = parseInt(255 * Math.abs(Math.sin(angle)));
            var g = parseInt(255 * Math.abs(Math.sin(gAngle)));
            var b = parseInt(255 * Math.abs(Math.sin(bAngle)));
            var rgbCol = "rgb(" + r + "," + g + "," + b + ")";

            // add color stop with new rgb colors
            grad.addColorStop(1, rgbCol);

            // fill canvas with gradient
            ctx.save();
            ctx.fillStyle = grad;
            ctx.fillRect(0,0, can.width, can.height);
            ctx.restore();
                // repeat while audio is not paused
            if (!document.querySelector("audio").paused)
                timer = setTimeout(drawGradient, 100);
        }
    </script>
</head>
<body onload="init()">
    <canvas id="can" height="200" width="300">
    </canvas>
    <audio id="audio" src="myAudio.m4a" controls>
    </audio>
</body>
</html>
```

Note that the previous example tests whether the audio is playing at the end of the animation cycle, instead of just clearing the animation timeout in the `"pause"` and `"ended"` event handlers. The audio events can occur while the animation cycle is in mid-execution, so it’s important not to reset the timer without testing the play state.

Sometimes sound isn’t tightly-coupled to the visual display—for example, looping audio may provide ambience to your site, but not be a requirement to enjoy the visuals.

The `loop` attribute is not currently supported for inline HTML5 audio on iOS, so to make your audio loop you need to install an event listener on the `audio` element—the event listener listens for the `"ended"` event and invokes the `play()` method to immediately restart the audio at the beginning.

The example in Listing 14-2 runs the visual part of the presentation whether or not the user chooses to play the audio, but loops the audio when it is playing. Note that the audio loops only when the `"ended"` event is triggered. If the user stops playback manually, the `"pause"` event is triggered, and the audio is not automatically restarted. The example is illustrated in Figure 14-2.

__Figure 14-2__  Looping audio

__Listing 14-2__  Adding looping audio

```
<html>
<head>
    <title>Happy Holidays</title>
    <!-- Fill the iOS screen /-->
    <meta name="viewport" content="width=600" />
    <style>
        canvas {
            position: absolute;
            top: 10px;
            left: 10px;
            border-radius: 25px;
        }
        audio {
            position: absolute;
            top: 307px;
            left: 160px;
        }
    </style>
    <script type="text/javascript">
        var can, ctx, flake,
            x = [], y = [], xIncr = [], yIncr = [];
            rot = 0, grad, rainbow, audio;

        function init() {
            flake = document.getElementById("flake");
            audio = document.getElementById("audio");
            can = document.getElementById("can");
            ctx = can.getContext("2d");
            // create blue background gradient
            grad = ctx.createLinearGradient(0, can.height, 0, 0);
            grad.addColorStop(0, 'rgb(20,20,128)');
            grad.addColorStop(1, 'rgb(140,140,255)');
            // create rainbow gradient for letters
            rainbow = ctx.createLinearGradient(20, 0, can.width - 20, 0);
            rainbow.addColorStop(0, 'red');
            rainbow.addColorStop(1 / 6, 'orange');
            rainbow.addColorStop(2 / 6, 'yellow');
            rainbow.addColorStop(3 / 6, 'green');
            rainbow.addColorStop(4 / 6, 'aqua');
            rainbow.addColorStop(5 / 6, 'blue');
            rainbow.addColorStop(6 / 6, 'purple');
            // set font properties
            ctx.font = "140pt Papyrus bold italic";
            ctx.textAlign = "center";
            ctx.textBaseline = "bottom";
            // create snowflakes above screen
            // drifting slowly down and randomly left or right
            for (i = 1; i <= 16; i++) {
                x[i] = Math.random() * can.width;
                y[i] = Math.random() * can.height / -2;
                yIncr[i] = Math.max(Math.random() * .4, 0.15);
                xIncr[i] = Math.random() * 0.3 - 0.15;
            }
            // add listener function to loop on end
            audio.addEventListener("ended", loop, false);
            // set animation on perpetual loop
            setInterval(animate, 30);
        }

        function loop() {
            audio.play();
        }

        function animate() {
            model();
            draw();
        }

        function model() {
                // increment flakes x and y coords
            for (i = 1; i <= 16; i++) {
                y[i] += yIncr[i];
                x[i] += xIncr[i];
                // if off bottom, give new x coord and start above top
                if (y[i] > can.height + 45) {
                    y[i] = -45;
                    x[i] = Math.random() * can.width;
                    yIncr[i] = Math.max(Math.random() * .4, 0.15);
                }
            }
        }

        function draw() {
            // draw background
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, can.width, can.height);
                // rotate flakes as they fall
            rot += 0.005;
                // draw flakes offset so they rotate around center
            for (i = 1; i <= 16; i++) {
                ctx.save();
                ctx.translate(x[i], y[i]);
                ctx.rotate(rot);
                ctx.drawImage(flake, -37, -43);
                ctx.restore();
            }
                // draw word with black and white borders for depth
            ctx.fillStyle = 'black';
            ctx.fillText("Peace", can.width / 2 -2, can.height + 2);
            ctx.fillStyle = 'white';
            ctx.fillText("Peace", can.width / 2 + 2, can.height - 2);
            ctx.fillStyle = rainbow;
            ctx.fillText("Peace", can.width / 2, can.height );
        }
    </script>
</head>
<body onload="init()">
    <canvas id="can" height="300" width="500">
    </canvas>
    <br />
    <audio src="peace.mp4" id="audio" controls></audio>
    <img id="flake" src="flake.png" style="display:none" />
</body>
</html>
```


For a slideshow or a Keynote presentation, for example, you may want to add a voice-over that narrates each slide individually. It’s easiest to create and maintain such a presentation if you record a separate audio file for each slide—that way you can add, change, or rearrange your presentation on a slide-by-slide basis.

To synchronize the slides with your audio, install an event listener on the `audio` element and listen for the `"ended"` event. Respond to the event by changing the `src` property of the audio element to the audio file for the next slide, and by changing the canvas to display the next slide.

When the last slide has played, reset the audio and visual elements so that, if the user presses play again, the presentation starts from the beginning.

The example in Listing 14-3 plays a series of images exported from Keynote, synchronized to a series of voice-overs created using QuickTime Player. The example is illustrated in Figure 14-3.

__Figure 14-3__  Voice-over

__Listing 14-3__  Displaying slides with voice-overs

```
<html>
<head>
    <title>Slides with Voice-Over</title>
    <!-- Fill the iOS screen /-->
    <meta name="viewport" content="width=600" />
    <style>
        canvas {
            position: absolute;
            top: 10px;
            left: 10px;
        }
        audio {
            position: absolute;
            top: 380px;
            left: 160px;
        }
    </style>
    <script type="text/javascript">
        var can, ctx, audio, image, maxSlides = 4,
            slide = [], voice = [], index = 0;

        function init() {
            audio = document.getElementById("audio");
            image = document.getElementById("image");
            can = document.getElementById("can");
            ctx = can.getContext("2d");
            for (i = 0; i < maxSlides; i++) {
                // get filenames into JavaScript
                slide[i] = "slides" + i + ".jpg";
                voice[i] = "slide" + i + ".mp4";
                // preload images
                image.src = slide[i];
            }
            // draw initial "splash screen" slide
            image.src = slide[0];
            ctx.drawImage(image, 0, 0, can.width, can.height);
            audio.addEventListener("playing", start, false);
            audio.addEventListener("ended", next, false);
        }

        function start() {
            // respond to playing event only if index = 0
            if (index == 0) {
                // set index to 1 and show next slide
                index = 1;
                image.src = slide[1];
                ctx.drawImage(image, 0, 0, can.width, can.height);
            }
        }

        function next() {
            // if audio for this slide ended, advance index
            index++;
            if (index < maxSlides) {
                // increment slide image src
                image.src = slide[index];
                // increment audio src
                audio.src = voice[index];
                // play new audio src
                audio.play();
                // show new slide
                ctx.drawImage(image, 0, 0, can.width, can.height);
            }
            // if last slide shown, reset index and audio src to start over
            if (index == 4) {
                index = 0;
                audio.src = voice[1];
            }
        }
    </script>
</head>
<body onload="init()">
    <canvas id="can" height="384" width="512">
    </canvas>
    <img id="image" src="slides0.jpg" style="display:none" />
    <audio id="audio" src="slide1.mp4" controls ></audio>
</body>
</html>
```


For games, you typically want to trigger different sounds in response to events in the game. To make this work on iOS as well as the desktop, load the first sound in response to a user-activated control, such as a start button; play other sounds by changing the `src` property of the audio element and calling the `play()` method.

The example in Listing 14-4 includes an `audio` element and an Enable Sounds button. When sounds are enabled, the ball makes different sounds when it bounces off the bottom or the side. The example is illustrated in Figure 14-4.

__Figure 14-4__  Animation with sound effects

__Listing 14-4__  Creating animation with sound effects

```
<html>
<head>
    <title>Animation with Sound Effects</title>
    <script type="text/javascript">
        var can, ctx, ball, x, y, xVec, yVec, direc,
            rot = 0, gravity = 1, left = 70, right = 525, bottom = 325,
            interval, centerOffset = -75, audio, sound = 0, button;

        function init() {
            audio = document.getElementById("audio");
            button = document.getElementById("button");
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
            ctx.lineTo(600, bottom + 75);
            ctx.lineTo(600, 0)
            ctx.stroke();
            // set animation to repeat every 50 msec
            interval = setInterval(animate), 50);
        }

        function animate() {
            model();
            // clear canvas except for lines at edge
            ctx.clearRect(0, 0, can.width - 1, can.height - 1);
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
                yVec = -1 * yVec - gravity;
                // set audio for bottom bounce
                audio.src = "boing.mp4";
                if (sound)
                    audio.play();
            }
            if (x >= right || x <= left) {
                xVec *= -1;
                direc *= -1;
                // set audio for side bounce
                audio.src = "bing.mp4";
                if (sound)
                    audio.play();
            }
        }

        function draw() {
            ctx.save();
            ctx.translate(x, y);
            ctx.rotate(rot);
            ctx.drawImage(ball, centerOffset, centerOffset);
            ctx.restore();
        }

        function soundToggle() {
            if (!sound) {
                audio.load();
                sound = 1;
                button.value = "Turn Sounds Off";
            } else {
                sound = 0;
                button.value = "Enable Sounds";
            }
        }
    </script>
</head>
<body onload="init()" style="background-color:#e0e0e0">
    <h2>Animation with Sound</h2>
    <img id="ball" src="soccerball1.png" style="display:none" />
    <canvas id="can" height="400" width="600" style="position:relative;top:-50">
    </canvas>
    <audio id="audio" src="boing.mp4" style="display:none"></audio>
    <input id="button" type="button" value="Enable Sounds" onclick="soundToggle()" />
</body>
</html>
```

[Next](Pixel%20Manipulation.md)[Previous](Adding%20Mouse%20and%20Touch%20Controls%20to%20Canvas.md)

