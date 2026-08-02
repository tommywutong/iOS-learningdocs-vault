---
title: Safari HTML5 Audio and Video Guide
apple_id: TP40009523
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/Using_HTML5_Audio_Video/Device-SpecificConsiderations/Device-SpecificConsiderations.html
archived_at: '2026-07-15T05:21:32.512191Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari HTML5 Audio and Video Guide](About%20HTML5%20Audio%20and%20Video.md)


[Next](Playing%20Sounds%20with%20the%20Web%20Audio%20API.md)[Previous](Audio%20and%20Video%20HTML.md)

# iOS-Specific Considerations

There are a handful of device-specific considerations you should be aware of when embedding audio and video using HTML5.

Currently, Safari optimizes video presentation for the smaller screen on iPhone or iPod touch by playing video using the full screen—video controls appear when the screen is touched, and the video is scaled to fit the screen in portrait or landscape mode. Video is not presented within the webpage. The `height` and `width` attributes affect only the space allotted on the webpage, and the `controls` attribute is ignored. This is true only for Safari on devices with small screens. On Mac OS X, Windows, and iPad, Safari plays video inline, embedded in the webpage.

In Safari on iOS (for all devices, including iPad), where the user may be on a cellular network and be charged per data unit, preload and autoplay are disabled. No data is loaded until the user initiates it. This means the JavaScript `play()` and `load()` methods are also inactive until the user initiates playback, unless the `play()` or `load()` method is triggered by user action. In other words, a user-initiated Play button works, but an `onLoad="play()"` event does not.

__This plays the movie:__ `<input type="button" value="Play" onclick="document.myMovie.play()">`

__This does nothing on iOS:__ `<body onload="document.myMovie.play()">`

Because the native dimensions of a video are not known until the movie metadata loads, a default height and width of 150 x 300 is allocated on devices running iOS if the height or width is not specified. Currently, the default height and width do not change when the movie loads, so you should specify the preferred height and width for the best user experience on iOS, especially on iPad, where the video plays in the allocated space.

On iPhone and iPod touch, a placeholder with a play button is shown until the user initiates playback, as shown in Figure 2-1. The placeholder is translucent, so the background or any poster image shows through. The placeholder provides a way for the user to play the media. If the iOS device cannot play the specified media, there is a diagonal bar through the control, indicating that it cannot play.

__Figure 2-1__  The iPhone video placeholder

!

On the desktop and iPad, the first frame of a video displays as soon as it becomes available. There is no placeholder.

Controls are always supplied during fullscreen playback on iPhone and iPod touch, and the placeholder allows the user to initiate fullscreen playback. On the desktop or iPad, you must either include the `controls` attribute or provide playback controls using JavaScript. It is especially important to provide user controls on iPad because autoplay is disabled to prevent unsolicited cellular download.

Safari on the desktop supports any media the installed version of QuickTime can play. This includes media encoded using codecs QuickTime does not natively support, provided the codecs are installed on the user’s computer as QuickTime codec components.

Safari on iOS (including iPad) currently supports uncompressed WAV and AIF audio, MP3 audio, and AAC-LC or HE-AAC audio. HE-AAC is the preferred format.

Safari on iOS (including iPad) currently supports MPEG-4 video (Baseline profile) and QuickTime movies encoded with H.264 video (Baseline profile) and one of the supported audio types.

iPad and iPhone 3G and later support H.264 Baseline profile 3.1. Earlier versions of iPhone support H.264 Baseline profile 3.0.

Currently, all devices running iOS are limited to playback of a single audio or video stream at any time. Playing more than one video—side by side, partly overlapping, or completely overlaid—is not currently supported on iOS devices. Playing multiple simultaneous audio streams is also not supported. You can change the audio or video source dynamically, however. See [Replacing a Media Source Sequentially](Controlling%20Media%20with%20JavaScript.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmrtfvbuqmznknltk) for details.

On the desktop, you can set and read the `volume` property of an `<audio>` or `<video>` element. This allows you to set the element’s audio volume relative to the computer’s current volume setting. A value of 1 plays sound at the normal level. A value of 0 silences the audio. Values between 0 and 1 attenuate the audio.

This volume adjustment can be useful, because it allows the user to mute a game, for example, while still listening to music on the computer.

On iOS devices, the audio level is always under the user’s physical control. The `volume` property is not settable in JavaScript. Reading the `volume` property always returns 1.

You can set the audio or video `playbackRate` property to nonzero values to play media in slow motion (values >0 and <1) or fast forward (values >1) in Safari on the desktop. Setting `playbackRate` is not currently supported on iOS.

You can set the audio or video `loop` attribute in Safari on the desktop and on iOS 5.0 and later to cause media to repeat endlessly. To loop audio or video in a manner compatible with earlier versions of iOS, use JavaScript to install the `play()` method as an event listener for the `"ended"` event. This technique is illustrated in Listing 2-1.

__Listing 2-1__  Backward-compatible looping audio

```
<!doctype html>
<html>
<head>
    <title>Looping Audio</title>
    <script type="text/javascript">
        function init() {
            var myAudio = document.getElementById("audio");
            myAudio.addEventListener('ended', loopAudio, false);
        }
        function loopAudio() {
            var myAudio = document.getElementById("audio");
            myAudio.play();
        }
    </script>
</head>
<body onload="init();">
    <audio id="audio" src="myAudio.m4a" controls></audio>
</body>
</html>
```

[Next](Playing%20Sounds%20with%20the%20Web%20Audio%20API.md)[Previous](Audio%20and%20Video%20HTML.md)

