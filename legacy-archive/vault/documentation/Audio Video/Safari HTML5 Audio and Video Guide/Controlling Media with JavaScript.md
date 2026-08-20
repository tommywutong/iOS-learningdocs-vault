---
title: Safari HTML5 Audio and Video Guide
apple_id: TP40009523
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/Using_HTML5_Audio_Video/ControllingMediaWithJavaScript/ControllingMediaWithJavaScript.html
archived_at: '2026-07-15T05:21:32.487893Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari HTML5 Audio and Video Guide](About%20HTML5%20Audio%20and%20Video.md)


[Next](Adding%20CSS%20Styles.md)[Previous](Playing%20Sounds%20with%20the%20Web%20Audio%20API.md)

# Controlling Media with JavaScript

Because the `<audio>` and `<video>` elements are part of the HTML5 standard, there are JavaScript methods, properties, and DOM events associated with them.

There are methods for loading, playing, pausing, and jumping to a time. There are also properties you can set programmatically, such as the `src` URL and the height and width of a video, as well as read-only properties such as the video’s native height. Finally, there are DOM events you can listen for, such as load progress, media playing, media paused, and media done playing.

This chapter shows you how to do the following:

- Use JavaScript to create a simple controller.
- Change the size of a movie dynamically.
- Display a progress indicator while the media is loading.
- Replace one movie with another when the first finishes.
- Keep the playback of multiple media elements in perfect sync.
- Provide fallback content using JavaScript if none of the media sources is playable.
- Enter and exit full-screen mode.
- Take your custom video player and controls into full-screen mode.

For a complete description of all the methods, properties, and DOM events associated with HTML5 media, see _[Safari DOM Additions Reference](https://developer.apple.com/documentation/webkitjs)_. All the methods, properties, and DOM events associated with `HTMLMediaElement`, `HTMLAudioElement`, and `HTMLVideoElement` are exposed to JavaScript.

Listing 4-1 creates a simple play/pause movie control in JavaScript, with additional controls to toggle the video size between normal and doubled. It is intended to illustrate, in the simplest possible way, addressing a media element, reading and setting properties, and calling methods.

Any of the standard ways to address an HTML element in JavaScript can be used with `<audio>` or `<video>` elements. You can assign the element a name or an id, use the tag name, or use the element’s place in the DOM hierarchy. The example in Listing 4-1 uses the tag name. Since there is only one `<video>` element in the example, it is the 0th item in the array of elements with the “video” tag name.

__Listing 4-1__  Adding simple JavaScript controls

```
<!doctype html>
<html>
<head>
    <title>Simple JavaScript Controller</title>
    <script type="text/javascript">
        function playPause() {
            var myVideo = document.getElementsByTagName('video')[0];
            if (myVideo.paused)
                myVideo.play();
            else
                myVideo.pause();
        }
       function makeBig() {
           var myVideo = document.getElementsByTagName('video')[0];
           myVideo.height = myVideo.videoHeight * 2;
       }
       function makeNormal() {
           var myVideo = document.getElementsByTagName('video')[0];
           myVideo.height = myVideo.videoHeight;
       }
    </script>
</head>
<body>
    <div class="video-player" align="center">
        <video src="myMovie.m4v" poster="poster.jpg" ></video>
        <a href="javascript:playPause();">Play/Pause</a> |
        <a href="javascript:makeBig();">2x Size</a> |
        <a href="javascript:makeNormal();">1x Size</a>
    </div>
</body>
</html>
```

The previous example gets two read-only properties: `paused` and `videoHeight` (the native height of the video). It calls two methods: `play()` and `pause()`. And it sets one read/write property: `height`. Recall that setting only the height or width causes the video to scale up or down while retaining its native aspect ratio.

One of the common tasks for a movie controller is to display a progress indicator showing how much of the movie has loaded so far. One way to do this is to constantly poll the media element’s `buffered` property, to see how much of the movie has buffered, but this is a waste of time and energy. It wastes processor time and often battery charge, and it slows the loading process.

A much better approach is to create an event listener that is notified when the media element has something to report. Once the movie has begun to load, you can listen for `progress` events. You can read the `buffered` value when the browser reports `progress` and display it as a percentage of the movie’s `duration`.

Another useful DOM event is `canplaythrough`, a logical point to begin playing programmatically.

You can install event listeners on the media element or any of its parents, up to and including the document body.

Listing 4-2 loads a large movie from a remote server so you can see the progress changing. It installs an event listener for `progress` events and another for the `canplaythrough` event. It indicates the percentage loaded by changing the inner HTML of a paragraph element.

You can copy and paste the example into a text editor and save it as HTML to see it in action.

__Listing 4-2__  Installing DOM event listeners

```
<!doctype html>
<html>
<head>
    <title>JavaScript Progress Monitor</title>
    <script type="text/javascript">
        function getPercentProg() {
            var myVideo = document.getElementsByTagName('video')[0];
            var endBuf = myVideo.buffered.end(0);
            var soFar = parseInt(((endBuf / myVideo.duration) * 100));
            document.getElementById("loadStatus").innerHTML =  soFar + '%';
        }
       function myAutoPlay() {
           var myVideo = document.getElementsByTagName('video')[0];
           myVideo.play();
       }
       function addMyListeners(){
           var myVideo = document.getElementsByTagName('video')[0];
           myVideo.addEventListener('progress', getPercentProg, false);
           myVideo.addEventListener('canplaythrough', myAutoPlay, false);
       }
    </script>
</head>
<body onload="addMyListeners()">
    <div>
        <video controls
               src="http://homepage.mac.com/qt4web/sunrisemeditations/myMovie.m4v">
        </video>
        <p id="loadStatus">MOVIE LOADING...</p>
    </div>
</body>
</html>
```

The `buffered` property is a `TimeRanges` object, essentially an array of start and stop times, not a single value. Consider what happens if the person watching the media uses the time scrubber to jump forward to a point in the movie that hasn’t loaded yet—the movie stops loading and jumps forward to the new point in time, then starts buffering again from there. So the `buffered` property can contain an array of discontinuous ranges. The example simply seeks to the end of the array and reads the last value, so it actually shows the percentage into the movie duration for which there is data. To determine precisely what percentage of a movie has loaded, taking possible discontinuities into account, iterate through the array, summing the seekable ranges, as illustrated in Listing 4-3

__Listing 4-3__  Summing a TimeRanges object

```
var myBuffered = document.getElementsByTagName('video')[0].buffered;
var total = 0;
for (var i = 0, len = myBuffered.length; i < len; i++) {
    total += (seekable.end(i) - seekable.start(i));
}
```

The `buffered`, `played`, and `seekable` properties are all `TimeRanges` objects.

Another common task for a website programmer is to create a playlist of audio or video—to put together a radio set or to follow an advertisement with a program, for example. To do this, you can provide a function that listens for the `ended` event. The `ended` event is triggered only when the media ends (plays to its complete duration), not if it is paused.

When your listener function is triggered, it should change the media’s `src` property, then call the `load` method to load the new media and the `play` method to play it, as shown in Listing 4-4.

__Listing 4-4__  Replacing media sequentially

```
<!doctype html>
<html>
<head>
    <title>Sequential Movies</title>
    <script type="text/javascript">
        // listener function changes src
        function myNewSrc() {
            var myVideo = document.getElementsByTagName('video')[0];
            myVideo.src = "http://homepage.mac.com/qt4web/myMovie.m4v";
            myVideo.load();
            myVideo.play();
        }
        // add a listener function to the ended event
        function myAddListener(){
            var myVideo = document.getElementsByTagName('video')[0];
            myVideo.addEventListener('ended', myNewSrc, false);
        }
    </script>
</head>
<body onload="myAddListener()">
    <video controls
           src="http://homepage.mac.com/qt4web/A-chord.m4v">
    </video>
</body>
</html>
```

The previous example works on both Safari on the desktop and Safari on iOS, as the `load()` and `play()` methods are enabled even on cellular networks once the user has started playing the first media element.

Until the advent of media controllers, ensuring that two or more videos played at precisely the same time was a challenging endeavor. Media controllers let you group any number of audio and/or video elements so that they can be managed by a universal set of controls, and also so that they can be kept in perfect sync, even if a network hiccup occurs.

To create a media controller, simply add the `mediagroup` attribute to all of the elements you wish to sync together. The value you choose to assign to `mediagroup` is up to you—as long as the value is the same for each slaved element, a media controller will be created implicitly.

```
<video src="video.m4v" width="960" height="600" mediagroup="masterController"></video>
```

Most of the same functions, attributes, and events available to audio and video elements are also available to media controllers. Instead of calling `play()` or `pause()` directly on the video itself, you call them on the media controller.

```
var myVideo = document.querySelector('video');
var mediaController = myVideo.controller;
mediaController.play();
```

Accessing the controller object on any of the slaved media elements will return a controller of the grouped elements. You can also create a media controller entirely in JavaScript without needing to modify the attributes of your HTML:

```
var myVideos = document.querySelectorAll('video');
var mediaController = new MediaController();
myVideos[0].controller = mediaController;
myVideos[1].controller = mediaController;
mediaController.play();
```

If one video stalls or stutters, the other videos will automatically pause to wait for the lagging video to catch up. When the video buffers and is ready to play, the remaining videos will resume in sync.

It’s easy to provide fallback content for browsers that don’t support the `<audio>` or `<video>` tag using HTML (see [Specifying Fallback Behavior](Audio%20and%20Video%20HTML.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmrtfvbuqmrnknltcmy)). But if the browser understands the tag and can’t play any of the media you’ve specified, you need JavaScript to detect this and provide fallback content.

To test whether the browser can play any of the specified media, iterate through your source types using the `canPlayType` method.

If the method returns “no” or the empty string (“”) for all the source types, the browser knows it can’t play any of the media, and you need to supply fallback content. If the method returns “maybe” or “probably” for any of the types, it will attempt to play the media and no fallback should be needed.

The following example creates an array of types, one for each source, and iterates through them to see if the browser thinks it can play any of them. If it exhausts the array without a positive response, none of the media types are supported, and it replaces the video element using `innerHTML`. Listing 4-5 displays a text message as fallback content. You could fall back to a plug-in or redirect to another page instead.

__Listing 4-5__  Testing for playability using JavaScript

```
<!doctype html>
<html>
<head>
    <title>JavaScript Fallback</title>
    <script type="text/javascript">
        function checkPlaylist() {
            var playAny = 0;
            myTypes = new Array ("video/mp4","video/ogg","video/divx");
            var nonePlayable = "Your browser cannot play these movie types."
            var myVideo = document.getElementsByTagName('video')[0];
            for (var i = 0, len = myTypes.length; i < len; x++) {
                var canPlay = myVideo.canPlayType(myTypes[i]);
                if ((canPlay == "maybe") || (canPlay == "probably"))
                    playAny = 1;
            }
            if (playAny == 0)
                document.getElementById("video-player").innerHTML = nonePlayable;
         }
    </script>
</head>
<body onload="checkPlaylist()" >
    <div id="video-player" align=center>
        <video controls height="200" width="400">
            <source src="myMovie.m4v" type="video/mp4">
            <source src="myMovie.oga" type="video/ogg">
            <source src="myMovie.dvx" type="video/divx">
        </video>
    </div>
</body>
</html>
```


Even if a source type is playable, that’s no guarantee that the source _file_ is playable—the file may be missing, corrupted, misspelled, or the `type` attribute supplied may be incorrect. If Safari 4.0.4 or earlier attempts to play a source and cannot, it emits an `error` event. However, it still continues to iterate through the playable sources, so the `error` event may indicate only a momentary setback, not a complete failure. It’s important to check which source has failed to play.

Changes in the HTML5 specification now require the media element to emit an error only if the _last_ playable source fails, so this test is not necessary in Safari 5.0 or later.

The example in Listing 4-5 iterates through the source types to see if any are playable. It saves the filename of the last playable source. If there are no playable types, it triggers a fallback. If there are playable types, it installs an `error` event listener. The event listener checks to see if the current source contains the last playable filename before triggering a failure fallback. (The `currentSrc` property includes the full path, so the test is for inclusion, not equality.)

Notice that when adding a listener for the `error` event you need to set the `capture` property to `true`, whereas for most events you set it to `false`.

__Listing 4-6__  Testing for failure using JavaScript

```
<!doctype html>
<html>
<head>
    <title>JavaScript Fallback</title>
    <script type="text/javascript">
        var lastPlayable,
            myTypes = new Array("video/mp4", "video/ogg", "video/divx"),
            mySrc = new Array("myMovie.mp4", "myMovie.oga", "myMovie.dvx");

        function errorFallback() {
            var errorLast = "An error occurred playing ";
            var myVideo = document.getElementsByTagName('video')[0];
            if (myVideo.currentSrc.match(lastPlayable)) {
                errorLast = errorLast + lastPlayable;
                document.getElementById("video-player").innerHTML = errorLast;
            }
        }

        function checkPlaylist() {
            var noPlayableTypes = "Your browser cannot play these movie types";
            var myVideo = document.getElementsByTagName('video')[0];
            var playAny = 0;
            for (var i = 0, len = myTypes.length; i < len; i++) {
                var canPlay = myVideo.canPlayType(myTypes[i]);
                if ((canPlay == "maybe") || (canPlay == "probably")) {
                    playAny = 1;
                    lastPlayable = mySrc[i];
                }
            }
            if (playAny == 0)
                document.getElementById("video-player").innerHTML = noPlayableTypes;
            else
                myVideo.addEventListener('error', errorFallback, true);
        }
    </script>
</head>
<body onload="checkPlaylist()">
    <video controls >
        <source src="myMovie.mp4" type="video/mp4">
        <source src="myMovie.oga" type="video/ogg">
        <source src="myMovie.dvx" type="video/divx
    </video>
</body>
</html>
```


If you know the dimensions of your movie in advance, you should specify them. Specifying the dimensions is especially important for delivering the best user experience on iPad. But you may not know the dimensions when writing the webpage. For example, your source movies may not be the same size, or sequential movies may have different dimensions. If you install a listener function for the `loadedmetadata` event, you can resize the video player to the native movie size dynamically using JavaScript as soon as the native size is known. The `loadedmetadata` event fires once for each movie that loads, so a listener function is called any time you change the source. Listing 4-7 shows how.

__Listing 4-7__  Resizing movies programmatically

```
<!doctype html>
<html>
<head>
    <title>Resizing Movies</title>
    <script type="text/javascript">
        // set height and width to native values
        function naturalSize() {
            var myVideo = document.getElementsByTagName('video')[0];
            myVideo.height = myVideo.videoHeight;
            myVideo.width = myVideo.videoWidth;
        }
        // register listener function on metadata load
        function myAddListener(){
            var myVideo = document.getElementsByTagName('video')[0];
            myVideo.addEventListener('loadedmetadata', naturalSize, false);
        }
    </script>
</head>
<body onload="myAddListener()">
     <video src="http://homepage.mac.com/qt4web/myMovie.m4v" controls>
     </video>
</body>
</html>
```


Safari 5.0 and later, and iOS 3.2 and later on iPad, include a full-screen button on the video controller, allowing the user to initiate full-screen video mode.

Safari 5.0 and iOS 4.2 and later add JavaScript properties and DOM events that your scripts can use to determine when the browser has entered or exited full-screen video mode, as well as the methods to enter and exit full-screen video mode programatically. See _[HTMLMediaElement Class Reference](https://developer.apple.com/documentation/webkitjs/htmlmediaelement)_ for a full description of the full-screen DOM events, properties, and methods.

The following example, Listing 4-8, adds a button that puts Safari into full-screen video mode. The Boolean property `webkitSupportsFullscreen` is tested to verify that the current media is capable of being played in full-screen mode. Audio-only files cannot be played in full-screen mode, for example. The Full-screen button is hidden until the test is performed.

__Listing 4-8__  Using `webkitEnterFullscreen()`

```
<!doctype html>
<html>
<head>
    <title>Fullscreen Video</title>
    <script type="text/javascript">
        var vid;
        function init() {
            vid = document.getElementById("myVideo");
            vid.addEventListener("loadedmetadata", addFullscreenButton, false);
        }
        function addFullscreenButton() {
            if (vid.webkitSupportsFullscreen) {
                var fs = document.getElementById("fs");
                fs.style.visibility = "visible";
            }
        }
        function goFullscreen() {
            vid.webkitEnterFullscreen();
        }
    </script>
</head>
<body onload="init()"
    <h1>Fullscreen Video</h1>
    <video src="myMovie.m4v" id="myVideo" autoplay controls>
    </video>
    <input type="button" id="fs" value="Fullscreen" onclick="goFullscreen()" style="visibility:hidden">
</body>
</html>
```


In Safari 5.1 and later for OS X and Windows, you can not only take your video into full-screen mode, you can take _any_ HTML element into full-screen mode. If you enclose a video and custom controls inside a `div` element, for example, you can take the `div` element and all its contents into full-screen mode by calling `myDiv.webkitRequestFullscreen()`.

Use the following functions to take any element into and out of full-screen mode:

- `myElement.webkitRequestFullscreen()`
- `document.webkitExitFullscreen()`

When you enter full-screen mode programatically, it is important to remember that the user can exit full-screen mode at any time by pressing the Esc key.

OS X and iOS behave differently in terms of detecting which HTML elements can be brought full-screen. On iOS, you can take any video full-screen. On OS X, you can take any HTML element full-screen. Although they share the same `webkitRequestFullscreen` and `webkitExitFullscreen` methods, the two platforms have different event listeners:

- __OS X:__ the `webkitfullscreenchange` event fires when an element enters or exits full-screen mode.
- __iOS:__ the `webkitbeginfullscreen` and `webkitendfullscreen` events fire when a video enters and exits full-screen mode, respectively.

Listen for these events to detect changes in screen presentation. Take a look at the _[HTML5VideoEventFlow](../../../samplecode/HTML5VideoEventFlow/HTML5VideoEventFlow.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytambygu)_ sample code project to get an interactive understanding of the order in which these and other video playback events happen.

The `document.webkitFullscreenElement` property contains the element that is in full-screen mode. Check if this property is defined to determine if the user is currently in full-screen mode. The `document.fullscreenEnabled` property detects whether the browser supports the full-screen API, not whether an element is currently full-screen.

When a `video` element alone is taken into full-screen mode, the video is automatically scaled to fill the screen. When other elements are taken full screen, however, they are not necessarily resized. Instead, normal HTML rules are followed, so a `div` element and its children retain their height and width. If your video is inside an element that you take full screen, you are responsible for resizing the video when Safari enters and exits full-screen mode.

An easy way to resize video automatically is to define a full-screen `pseudo-class` in CSS for the element enclosing the video. With this `pseudo-class`, you can specify a set of CSS styles that are only applied in full-screen mode. For example, if the ID of the `div` you are taking full-screen is “video-player” this CSS snippet expands the enclosed video when the `div` element is in full-screen mode:

```
#video-player:-webkit-full-screen {
    width: 100%;
}
```

A key advantage to using CSS is that it expands the video when its parent is in full-screen mode, then returns the video to its normal size when its parent leaves full-screen mode.

It can be tricky to expand a video to use the full screen while preserving its aspect ratio. Here are some guidelines:

- If your video aspect ratio is 16 x 9, setting the width to 100% usually works best without setting the height explicitly—your video is scaled to the correct width, and the height is scaled to preserve the aspect ratio. Most displays are 4 x 3, 16 x 9, or slightly taller, so there is normally enough display height to prevent clipping.
- If your video aspect ratio is 4 x 3, setting the width to 75% gives the maximum image size for screens with 16 x 9 aspect ratios, while still using most of a 4 x 3 display. (Setting the width to 100% clips off the top and bottom of the image on widescreen displays.) Alternatively, you can use JavaScript to read the screen height and width, then set the width to 100% on 4 x 3 displays and 75% on wider displays.
- If your video is taller than it is wide, setting the height to 100% and leaving the width unset gives you the maximum image size on any landscape display.
- If your controls appear under the video, instead of floating on top of the video, reduce the width or height setting by 10% or so to leave room for the controls.

The example in Listing 4-9 creates a `div` element enclosing a video and a simple Play/Pause control. Beneath the `div` element is a full-screen control. When the full-screen control is clicked, the example takes the `div` element enclosing the video and Play/Pause control into full-screen mode.

CSS styles are used to expand the `div` element itself to 100% of the screen width and height, and to expand the enclosed video element to 100% of the `div` element’s width. Only the video’s width is specified, so that the video scales up while retaining its native aspect ratio. The example also gives the `div` element a black background when in full-screen mode.

More elaborate CSS could be used to hide the controls while in full-screen mode and reveal them when the user touches or hovers over the video. For more about styling video controllers using CSS, see [Adding CSS Styles](Adding%20CSS%20Styles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmrtfvbuqnbnknltc).

__Listing 4-9__  Full-screen video with custom controls

```
<!doctype html>
<html>
<head>
    <title>Full-screen JavaScript Controller</title>
    <style>
        #video-player:-webkit-full-screen {
            width: 100%;
            height: 100%;
            background-color: black;
        }
        #video-player:-webkit-full-screen video {
            width: 100%;
        }
    </style>
    <script type="text/javascript">
        function playPause() {
            var myVideo = document.querySelector('video');
            if (myVideo.paused)
                myVideo.play();
            else
                myVideo.pause();
         }
        function goFullscreen() {
            var myPlayer = document.getElementById('video-player');
            myPlayer.webkitRequestFullscreen();
        }
    </script>
</head>
<body>
    <div id="video-player">
        <video src="myMovie.m4v"></video>
        <p><a href="javascript:playPause();">Play/Pause</a></p>
    </div>
    <a href="javascript:goFullscreen();">Full-screen</a>
</body>
</html>
```

[Next](Adding%20CSS%20Styles.md)[Previous](Playing%20Sounds%20with%20the%20Web%20Audio%20API.md)

