---
title: AirPlay Overview
apple_id: TP40011045
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/AirPlayGuide/Introduction/Introduction.html
archived_at: '2026-07-15T05:21:01.995625Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Preparing%20Your%20Media%20and%20Server%20for%20AirPlay.md)

# About AirPlay

If you provide audio or video content from a website, or display audio or video content within your iOS app, you should learn about AirPlay. AirPlay lets users stream your audio and video to high-definition displays and high-fidelity audio systems. Using AirPlay, users redirect audio and video from iTunes or an iOS-based device to either an Apple TV (and from there to a home theater system) or to an AirPlay-enabled sound system. AirPlay can stream media coming live from the Internet, media already stored in iTunes, or media stored on an iOS-based device. AirPlay can stream Internet-based media when it is playing in iOS apps, in the Safari browser on iOS-based devices, or in iTunes on any platform.

AirPlay is supported on iOS 4.3 or later and iTunes 10.2 or later on OS X and Windows.

Using AirPlay, users redirect audio and video to either an Apple TV or to an AirPlay-enabled sound system or remote speakers. AirPlay is user controlled. As a content provider, your primary role is to ensure that your media is AirPlay compatible and that your app or website works correctly with AirPlay. You might also want to provide high-definition video or surround-sound audio when your content is being redirected to a home theater system.

As an app developer, you can enhance the user’s AirPlay experience in several ways:

- Provide an AirPlay output device picker.
- Provide audio metadata that the AirPlay-enabled output device can display.
- Listen for and respond to remote events from the AirPlay output device, such as play/pause.
- Use the iOS-based device’s built-in display independently when a second display is active.

### Choose the Best Option for Media Playback

You can deliver AirPlay-compatible audio and video to iOS-based devices in four distinct ways:

- Embed audio or video in your website using the HTML5 `<audio>` and `<video>` tags. Media delivered this way works on iOS-based devices through the Safari browser or in apps that use a web view.
- Stream audio and video directly to your app, playing the media using AV Foundation, the [MPMoviePlayerController](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller) class, or the [UIWebView](https://developer.apple.com/documentation/uikit/uiwebview) class.
- Store the media locally on an iOS-based device.
- Make your content available through iTunes, either commercially or as a podcast.

AirPlay is compatible with media delivered by progressive downloading or HTTP Live Streaming, but HTTP Live Streaming is preferred. To prepare your media for playback through AirPlay, make sure that it’s in a supported format—for example, H.264 video and AAC or MP3 audio. No special server configuration is required, apart from associating the correct MIME types with the file extensions used to send the media. To enrich the user’s AirPlay experience, you can also provide alternative audio and video streams that take advantage of a home theater system’s capabilities.

### You Can Opt Into or Out of AirPlay for Video

AirPlay is user initiated and, generally speaking, user controlled. Audio content (other than system sounds) can always be redirected by the user to an AirPlay-enabled sound system, and so can iTunes content, whether audio or video. If you provide video from your website or display it from within your app, however, you can choose to opt into AirPlay, enabling user redirection, or opt out of AirPlay, restricting your video to the device on which it is received.

In iOS 5.0 and later (including Safari in iOS 5.0), AirPlay is enabled by default and you must explicitly opt out of AirPlay if you want to prevent users from redirecting your video to Apple TV.

### Provide a Great AirPlay User Experience in Your App

You can include an AirPlay picker in your app’s user interface, allowing the user to select an AirPlay device for output without leaving your app.

If your app’s audio or video is being redirected to an AirPlay-enabled device that has its own controls, you can provide metadata—such as a song title and album artwork—to enhance the user’s experience. In addition your app should respond to remote events, such as play/pause or next-track requests.

### Protect Your Media Using Encryption and Authentication

If you deliver your audio and video using HTTP Live Streaming, there is built-in support for encryption, with automatic generation of encryption keys and initialization vectors on a periodic basis (see _[HTTP Live Streaming Overview](../../Networking%20Internet/HTTP%20Live%20Streaming%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmzs)_ for details). If you deliver the keys over HTTPS and use authentication, however, your app is responsible for the initial authentication handshake.

- _[Multiple Display Programming Guide for iOS](../../Windows%20Views/Multiple%20Display%20Programming%20Guide%20for%20iOS/Using%20Windows%20to%20Present%20Content%20on%20Multiple%20Displays.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdknjv)_ describes how to take advantage of an external display by mirroring the content of an iOS-based device or displaying different content on each device.
- _[HTTP Live Streaming Overview](../../Networking%20Internet/HTTP%20Live%20Streaming%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmzs)_ explains how to set up and use HTTP Live Streaming to deliver live and on-demand audio and video over HTTP from an ordinary web server.
- _[Safari HTML5 Audio and Video Guide](../Safari%20HTML5%20Audio%20and%20Video%20Guide/About%20HTML5%20Audio%20and%20Video.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmrt)_ explains how to embed audio and video in websites.
- _[AVPlayer Class Reference](https://developer.apple.com/documentation/avfoundation/avplayer)_ describes the `AVPlayer` class, including AirPlay-specific properties.
- _[MPMoviePlayerController Class Reference](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller)_ describes the `MPMoviePlayerController` class, including AirPlay-specific properties.
- _[UIWebView Class Reference](https://developer.apple.com/documentation/uikit/uiwebview)_ describes the `UIWebView` class, including AirPlay-specific properties.
[Next](Preparing%20Your%20Media%20and%20Server%20for%20AirPlay.md)

