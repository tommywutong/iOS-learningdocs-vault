---
title: 'A history of iOS media APIs (iPhone OS 2.0 to iOS 4.3) | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2011/03/history-of-ios-media-apis-iphone-os-20.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:a1d3f4bf3fbea04e'
translated: false
---

> 原文：[A history of iOS media APIs (iPhone OS 2.0 to iOS 4.3) | Cocoa with Love](https://www.cocoawithlove.com/2011/03/history-of-ios-media-apis-iphone-os-20.html)　·　Cocoa with Love (Matt Gallagher)

After initially starting with a small set of fairly basic media APIs in iPhone OS 2.0, the APIs and the features they provide have dramatically increased in the past 2 years and provided a rapidly moving target for developers trying to remain current. In this post, I'll try to summarize all of the different APIs in iOS 4.3 for playing media, when they arrived, what their purposes are, what their limitations are and what it's been like to remain up-to-date and support new features.

## Introduction

This post has two purposes:

1. To detail the different media APIs in iOS and to explain the scenarios to which they are best suited.
2. To show how many updates have been made to the media APIs and what that has meant to any iOS developer attempting to keep their media applications compiling successfully against the latest SDKs and up-to-date with the latest media features in iOS.

Note: I'll be limiting discussion to time-based media in this post, i.e. audio and video APIs. I realize that still photos are "media" but since photos are generally handled as basic graphics, they are handled in a very different manner to audio and video which use specialized hardware processing and handling in iOS.

I was inspired to write this post while working on [StreamToMe](http://zqueue.com/streamtome/index.html) version 3.5.2 — an update to one of my applications to improve the experience of users running iOS 4.3. Nominally, iOS 4.3 only added logging features to some media classes and added an "`allowsAirPlay`" property to the `MPMoviePlayerController`. Despite these seemingly limited changes to the APIs, StreamToMe still required some significant changes to work smoothly and deliver the features that users expect in iOS 4.3.

But I'm getting ahead of myself.

## iPhone OS 2.0

### Playback APIs

The first version of iPhone OS available to developers arrived with 5 media playing APIs:

- AudioUnits/AUGraphs
- AudioQueues
- `MPMoviePlayerController`
- `AudioServicesPlaySystemSound`
- `UIWebView`

**[AudioUnits](http://developer.apple.com/library/ios/#documentation/AudioUnit/Reference/AudioUnit_Framework/_index.html%23//apple_ref/doc/uid/TP40007295)/[AUGraphs](http://developer.apple.com/library/ios/#documentation/AudioToolbox/Reference/AUGraphServicesReference/Reference/reference.html%23//apple_ref/doc/uid/TP40007289)** are the "low-level" API in both Mac OS and iOS. If you want to process audio in any way, mix more than one source of audio, want to generate your own samples or otherwise access the raw Linear-PCM values, these have always been the best option — in many cases, close to the _only_ option.

I've previously written a post showing what is probably the simplest possible AudioUnit program: [an iOS Tone Generator](https://www.cocoawithlove.com/2010/10/ios-tone-generator-introduction-to.html). Of course, most people require considerably more complexity than this. A good next step if you're trying to learn about lower level audio APIs is the [MixerHost sample project](http://developer.apple.com/library/ios/samplecode/MixerHost/Introduction/Intro.html) you'll find in the iOS documentation. Apple tend to favor C++ wrappers around these C APIs so you may also want to be familiar with the classes in AUPublic folder — you can start to see how these are used by looking at the very similar [iPhoneMultichannelMixerTest](http://developer.apple.com/library/ios/samplecode/iPhoneMultichannelMixerTest/Introduction/Intro.html).

**[AudioQueues](http://developer.apple.com/library/mac/#documentation/MusicAudio/Reference/AudioQueueReference/Reference/reference.html)** are for playing or recording buffers of data. `AudioQueueNewInput` remains a common means of capturing microphone input and `AudioQueueNewOutput` is a common way to play to the speaker. The AudioQueue API is, like AudioUnits, a pure C API still requires a fairly meticulous set up. Where AudioUnits require that you push PCM samples into buffers yourself, AudioQueues let you push the buffers and not worry about the sample format. In fact, AudioQueues generally deal with buffers of still-compressed MP3 or AAC data.

I've written a series of posts on using AudioQueues (in conjunction with AudioFileStream) to play from an HTTP stream starting with [Streaming and playing an MP3](https://www.cocoawithlove.com/2008/09/streaming-and-playing-live-mp3-stream.html) stream and ending with [Streaming MP3/AAC audio again](https://www.cocoawithlove.com/2010/03/streaming-mp3aac-audio-again.html)

**[AudioServicesPlaySystemSound](http://developer.apple.com/library/mac/#documentation/AudioToolbox/Reference/SystemSoundServicesReference/Reference/reference.html)** will play up to 30 second segments. Its purpose is really for brief UI or notification sounds played asynchronously. You create the sound using `AudioServicesCreateSystemSoundID` and then play with `AudioServicesPlaySystemSound`. Not much more to say than that.

Living out on its own in iPhone OS 2.0, was **[MPMoviePlayerController](http://developer.apple.com/library/ios/documentation/mediaplayer/reference/MPMoviePlayerController_Class/Reference/Reference.html)** — the only Objective-C class for media playback in iPhone OS 2.0. It offered no programmatic control other than `play`, no options to configure the UI or movie and no feedback about state. You gave it a URL (either file or HTTP) and it presented the interface, handled the entire experience and posted a notification when it was done. The canonical code example used to be the [MoviePlayer](http://developer.apple.com/library/ios/samplecode/MoviePlayer_iPhone/Introduction/Intro.html#//apple_ref/doc/uid/DTS40007798) sample project but this has not been updated since iOS 3.0 and since iOS 4.0 broke backwards compatibility with this class, you'll need to ensure that the `MPMoviePlayerController`'s view is inserted into the view hierarchy before this project will work.

**[UIWebView](http://developer.apple.com/library/ios/documentation/uikit/reference/UIWebView_Class/Reference/Reference.html)** offered an experience similar to `MPMoviePlayerController` but had an added advantage: it was the only way to output over the TV out dock cables until iOS 3.2 (`MPMoviePlayerController`, despite being implemented by the same internal private classes, has this functionality disabled). While playing a movie through `UIWebView` didn't break in iOS 4 like `MPMoviePlayerController` did, the ability to play to the TV went away without explanation.

### Media support APIs

- AudioFile
- AudioFileStream
- AudioSession
- OpenAL
- `MPVolumeSettingsAlertShow`
- `MPVolumeView`

**[AudioFile](http://developer.apple.com/library/ios/documentation/MusicAudio/Reference/AudioFileConvertRef/Reference/reference.html)** offers a fairly rich set of metadata and parsing functions for files that are fully saved to disk. **[AudioFileStream](http://developer.apple.com/library/mac/documentation/MusicAudio/Reference/AudioStreamReference/Reference/reference.html)** offers a limited subset of the AudioFile functionality but has the advantage that the file doesn't need to be fully saved or downloaded — it can be a continuous source or progressive source.

**[AudioSession](http://developer.apple.com/library/ios/documentation/AudioToolbox/Reference/AudioSessionServicesReference/Reference/reference.html)** is mostly for handling audio routing (is the audio going to the headphones or the speaker) and for determining how your application's audio is blended with audio that other applications may be playing. If you need to handle interruptions (like when an iPhone rings) this API will help you.

**OpenAL** is an audio standard for controlling the positioning of the audio in 3D — mostly used for games. You can look at the [oalTouch](http://developer.apple.com/library/ios/#samplecode/oalTouch/Introduction/Intro.html) sample project for an example of how to set this up in iOS.

The **[MPVolumeSettingsAlertShow](http://developer.apple.com/library/ios/documentation/mediaplayer/reference/MediaPlayerFunctionsReference/Reference/reference.html)** and related functions show a dialog so the user can change the volume. The **[MPVolumeView](http://developer.apple.com/library/ios/documentation/mediaplayer/reference/MPVolumeView_Class/Reference/Reference.html)** is a slider so that the user can change the volume.

### Code maintenance considerations

Code written using AudioUnits, AudioQueues, AudioSessions and `AudioServicesPlaySystemSound` for iPhone OS 2.0 will generally continue to work in the latest version of iOS (iOS 4.3). Despite additions to these APIs, backwards compatibility remains high. However, many new classes like `AVAudioPlayer`, `AVPlayer`, `AVAudioRecorder`, `AVAudioSession` and `AVCaptureSession` provide alternative ways of doing similar things so you may need to consider these alternatives compared to these earlier APIs.

As I mentioned, `MPMoviePlayerController` code written for iPhone OS 2.0 but linked against iOS 4.3 SDKs will likely not work since this code requires a view be inserted into the hierarchy starting with iOS 3.2.

`UIWebView` stopped outputting over TV out in iOS 3.2 so there's no longer a real reason to use a web view instead of a real movie view.

I rarely use the AudioFile APIs anymore. It's not due to compatibility issues but instead I feel it's been superceded: AudioFileStream (rather than AudioFile) is required for streaming or progressive downloads, `AVAudioPlayer` (iOS 2.2) is easier for playing files stored on the device (apparently it uses AudioFile/AudioQueue internally) and ExtAudioFile (iOS 2.1) can convert between media formats using the hardware and hence can plug into an AUGraph better.

In my experience, the `MPVolumeView` slider is more commonly used than the `MPVolumeSettingsAlertShow` dialog — with `MPVolumeView` supporting AirPlay audio in iOS 4.2 and later, the `MPVolumeView` become even more compelling. It used to infuriate me that in the simulator, the `MPVolumeView` simply didn't appear — it worked fine on the device but didn't draw itself in simulator (many hours were lost around wondering if its absence was a bug). The `MPVolumeView` still doesn't appear in the simulator (for no reason I can understand) but at least it now draws a label saying "No volume available".

## iPhone OS 2.1

Arriving just 2 months after iPhone OS 2, iPhone OS 2.1 brought audio conversion as the main addition to the SDK. The **[AudioConverter](http://developer.apple.com/library/ios/DOCUMENTATION/MusicAudio/Reference/AudioConverterServicesReference/Reference/reference.html)** functions introduced various forms of PCM conversions and conversions to and from compressed audio formats (MP3 and AAC).

The ability to convert MP3/AAC was important since it could take advantage of the audio hardware (previously decompression required software handling which consumes much more battery power).

Since the primary purpose for audio conversion is to allow a file — like an MP3 — to be opened and fed into a processing pipeline like an AUGraph, the **[ExtAudioFile](http://developer.apple.com/library/ios/documentation/MusicAudio/Reference/ExtendedAudioFileServicesReference/Reference/reference.html)** functions were also added to streamline this process.

### Code maintenance considerations

If you had code that decompressed audio in software or performed PCM conversion in anything less than an optimal manner, it was now a waste of CPU cycles relative to newer code that used these APIs.

## iPhone OS 2.2

Arriving just 2 months after iPhone OS 2.1 (now just 4 months after iPhone OS 2) the iPhone OS 2.2 update introduced the **[AVAudioPlayer](http://developer.apple.com/library/ios/DOCUMENTATION/AVFoundation/Reference/AVAudioPlayerClassReference/)** — the first Objective-C API for dedicated audio playback in iPhone OS. The `AVAudioPlayer` requires that the file be fully saved on your iOS device (so it isn't suitable for continuous streams, network streams or progressive downloads).

### Code maintenance considerations

If you had code that used AudioFile and AudioQueue, chances are that it would have been much easier to write your program using `AVAudioPlayer` instead — however, AudioFile and AudioQueue continue to work, so there was no need to update to `AVAudioPlayer`. Later on, `AVPlayer` superceded almost all of `AVAudioPlayer`'s functionality (with the exception of audio metering and playing from a non-URL buffer) so you need to consider if this is still the class you want to use.

## iPhone OS 3.0

Arriving approximately 1 year after iPhone OS 2.0, iPhone OS 3.0 brought the following media APIs:

- `AVAudioRecorder`
- `AVAudioSession`
- ,

  and

  classes

**[AVAudioRecorder](http://developer.apple.com/library/ios/documentation/AVFoundation/Reference/AVAudioRecorder_ClassReference/Reference/Reference.html)** provided the first Objective-C approach for recording sound. It offers a simple way to record sound to a file but doesn't allow processing of the sound on-the-fly (for that, `AudioQueueNewInput` is still required).

**[AVAudioSession](http://developer.apple.com/library/ios/documentation/AVFoundation/Reference/AVAudioSession_ClassReference/Reference/Reference.html)** provided an Objective-C approach for managing the application's audio session but bizarrely, it still lacks any facility for handling routing changes (i.e. a switch from the headphones to the speaker or to the dock connector). For this reason, I still generally avoid this class — the AudioSession C functions are clean an simple enough that sacrificing functionality for the improved simplicity of `AVAudioSession` doesn't seem like a great tradeoff.

The **[MPMediaQuery](http://developer.apple.com/library/ios/documentation/mediaplayer/reference/MPMediaQuery_ClassReference/Reference/Reference.html)**, **[MPMediaPickerController](http://developer.apple.com/library/ios/documentation/mediaplayer/reference/MPMediaPickerController_ClassReference/Reference/Reference.html)** classes and **[MPMusicPlayerController](http://developer.apple.com/library/ios/documentation/mediaplayer/reference/MPMusicPlayerController_ClassReference/Reference/Reference.html)** added the ability to browse, control or play music from the user's iTunes library on the device. This allows you to offer basic library browsing and playing capability. In iPhone OS 3, there was no way to apply different processing to the files — you had to use `MPMusicPlayerController`.

Arguably though, the 2 biggest media additions in iPhone OS 3 didn't require a new API: **HTTP live streaming** and video capture on the iPhone 3Gs. Video capture was added into the existing `UIImagePickerController` and the `MPMoviePlayerController` added handling of HTTP live streaming.

While `MPMoviePlayerController` has always supported opening an MP4 file over HTTP, this has three major disadvantages:

1. It is not really optimized for streaming (so the many HTTP byte range requests required can end up being slow).
2. An MP4 file can't be generated on-the-fly (so it's not suitable for continuous sources, live remuxed sources or live transcoded sources).
3. You can't dynamically change bitrate on an MP4 file (you can't handle 3G and WiFi bitrates in a single URL).

All of which were addressed by Apple's HTTP live streaming.

### Code maintenance considerations

HTTP live streaming did bring with it the following additional problems:

1. As a new protocol, the segmented MPEG-TS and M3U8 files required completely new software to generate them.
2. It was initially only supported by MPMoviePlayerController (no other interface could be used except UIWebView which was just a different way of presenting the same interface).
3. You don't have any access to the transport layer — all communication is handled by Apple's internal libraries making careful control of network access difficult or impossible.

The `MPMusicPlayerController`'s remote controlling of the iPod application is still relevant but since iOS 4.0 introduced the ability to get the URL and play the music in AVAudioPlayer or AVPlayer instead, `MPMusicPlayerController`'s playback capabilities seem limited.

Despite adding video to `UIImagePickerController`, you still were not able to get a live image from the camera or programmatically take a picture. Still image capture didn't arrive until iPhone OS 3.1. Actual movie capture didn't arrive until iOS 4.

In iPhone OS 3, you couldn't get a URL for MPMediaQuery results, meaning that you could play files from the user's iTunes library but couldn't do anything interesting. It wasn't until iOS 4 that you could finally get a URL (a weird "ipod-library" URL) that could be used to open the file in lower-level audio APIs to actually perform processing, mixing or other more interesting effects to music.

With HTTP live streaming in place, Apple introduced bitrate restrictions for media into the App Store submission guidelines. This meant that you needed to update your code to throttle streaming audio connections over 3G yourself (a tricky thing to do since `NSURLConnection` won't generally do this and you need to resort to `CFHTTPReadStream`), and all HTTP live streams over 3G needed to have a 64kbps fallback variant. If you've ever tried to squeeze video into 64kbps, you'll know how tight a restriction that is.

`AVAudioSession`'s inability to handle routing changes prevented it from properly superceding the older AudioSession functions.

## iPhone OS 3.1

**[UIVideoEditorController](http://developer.apple.com/library/ios/documentation/uikit/reference/UIVideoEditorController_ClassReference/Reference/Reference.html)** was the only significant media addition in iPhone OS 3.1. It allowed you to present the trimming/re-encoding interface for videos stored in the user's Photo Library.

## iOS 3.2

The first iPad release and the first release to be named "iOS" made two changes that were significant to for media playback: the addition of multiple screen support and a radical overhaul of the `MPMoviePlayerController`.

Prior to iOS 3.2, the only App Store legal way to output via the dock connector to a TV was to load a movie in a `UIWebView` and let the movie player in the web view connect to the TV screen and output via the dock connector. With the iPad, you could finally use **[UIScreen](http://developer.apple.com/library/ios/documentation/uikit/reference/UIScreen_Class/Reference/UIScreen.html) to find additional screens** and place your views on that screen instead of the main screen.

**MPMoviePlayerController was finally overhauled** to provide a lot of the feature it sorely needed:

- Inline (non-fullscreen) playback if desired, with smooth switching between fullscreen and non-fullscreen
- Ability to programmatically seek and get the current playback point
- Ability to set the control style (including disabling the standard user-interface entirely)
- Provided a location to actually insert a background image if desired

The "set and forget" movie player was reborn as **[MPMoviePlayerViewController](http://developer.apple.com/library/ios/documentation/mediaplayer/reference/mpmovieplayerviewcontroller_class/Reference/Reference.html)**, a `UIViewController` that handles all display and handling automatically and which handles all communication with its internal `MPMoviePlayerController` automatically.

### Code maintenance considerations

While older `MPMoviePlayerController` code linked against previous SDKs would continue to work, if you ever linked the code against a iOS 3.2 SDK or newer, it would now fail since the new `MPMoviePlayerController` requires its view be inserted into the view hierarchy or that fullscreen be set to YES.

Remember: Apple rarely allow you to link against anything except the newest SDK, so any attempt to recompile old projects with `MPMoviePlayerController` code will result in no video being shown unless you update the code. For this reason, Apple's MoviePlayer sample project continues to not work (they haven't updated since iPhone OS 3.0).

Given the size of the iPad screen, users now expect a non-fullscreen view to be possible.

The "Done" button of the `MPMoviePlayerController` (visible in fullscreen) no longer ends the movie. It just pauses it and shrinks it to the inline (non-fullscreen) view. This creates another new trait of the `MPMoviePlayerController` that you must adapt to handle.

## iOS 4.0

The biggest update since iPhone OS 2.0, iOS 4 brought a huge number of changes to media APIs.

- (and related classes)
- (and related classes)
- (and related classes)
- ,

  ,

  (and related classes)
- The ability to get the URL for an `MPMediaItem`
- and

  in
- and

  changes from iOS 3.2 brought to non-iPad devices
- Background audio
- and

The huge additions to the [AVFoundation.framework](http://developer.apple.com/library/ios/#DOCUMENTATION/AVFoundation/Reference/AVFoundationFramework/_index.html%23//apple_ref/doc/uid/TP40008072) — particularly the **[AVPlayer](http://developer.apple.com/library/ios/documentation/AVFoundation/Reference/AVPlayer_Class/Reference/Reference.html)** and **[AVComposition](http://developer.apple.com/library/ios/DOCUMENTATION/AVFoundation/Reference/AVComposition_Class/Reference/Reference.html)** class hierarchies — reflect Apple providing APIs that replace what Quicktime's API used to provide on the Mac: sophisticated media handling that could be used to implement a complete music or movie editing program if required. Ultimately, since Quicktime 7 is deprecated in favor of Quicktime X on the Mac, I expect that these APIs will probably appear in a future version of Mac OS X and represent multi-track mixing, editing and composition in Cocoa for the future.

`AVPlayer` in iOS 4.0 ultimately didn't offer any advantages over `MPMoviePlayerController` for playing regular media. `AVPlayer` is required for playing `AVCompositions` but for regular files, it was largely the same as `MPMoviePlayerController` with the user interface disabled (made possible since iOS 3.2).

The **[ALAsset](http://developer.apple.com/library/ios/documentation/AssetsLibrary/Reference/ALAsset_Class/Reference/Reference.html)** classes finally provided a way to search through the photo and video media without using the `UIImagePickerController`. It also provided a better way to handle reading and writing photo and video media to the user's photo library.

**[AVCaptureSesssion](http://developer.apple.com/library/ios/documentation/AVFoundation/Reference/AVCaptureSession_Class/Reference/Reference.html)** and the other AVCapture classes finally provided the ability to capture video data without the `UIImagePickerController` interface and perform realtime processing of video data. The classes also included the ability to handle audio capture too, providing an alternative to the `AudioQueueNewInput` function for processing audio while it is recording (remember `AVAudioRecorder` will still let you record audio direct to a file without processing).

**[Background audio](http://developer.apple.com/library/ios/documentation/iphone/conceptual/iphoneosprogrammingguide/BackgroundExecution/BackgroundExecution.html)** was largely painless — just a setting in your Info.plist — although trying to get videos to continue playing their audio in the background is a near impossibility (you need to disable the video track or if you're using HTTP live streaming, you need to restart the stream without video or iOS will forcibly pause playback when you hit the background).

### Code maintenance considerations

iOS 4.0 required updating of all `MPMoviePlayerController` code for non-iPad devices in the same way that iOS 3.2 required updating for the iPad.

`AVPlayer` has no built-in interface. You must entirely create it yourself. This remains a problem for anyone who needs to use `AVPlayer` instead of the standard `MPMoviePlayerController` because implementing video playback controls can take a long time and requires a lot of subtle features.

`UIWebView` stopped playing to the TV in iOS 4. No idea why but this functionality has not returned.

The inline (non-fullscreen) iPhone/iPod version of the `MPMoviePlayerController` user interface offers no button to return to fullscreen when playing audio. This creates an annoying difference between the iPhone/iPod and iPad versions of the `MPMoviePlayerController` which you need to handle.

## iOS 4.1

The biggest update in this version was the `AVQueuePlayer`. The iOS 4.0 headers actually hinted at being able to queue multiple items for an `AVPlayer` but obviously this functionality was held over.

**AVQueuePlayer** is an important class as it is the only player in iOS that will attempt to cache subsequent items for play to allow nearly gapless playback between items in a list. Like `AVPlayer` though, it has no user-interface so if you want to use this player, you need to write your own interface completely.

### Code maintenance considerations

`AVQueuePlayer` would be the unambiguously best player in iOS if it:

- could provide an inbuilt UI if requested
- could use AirPlay video

Until these features are brought to `AVQueuePlayer`, there are still reasons why you would need to use `MPMoviePlayerController` instead.

## iOS 4.2

The first version of iOS to merge iPad and iPhone/iPod lines. For media APIs, it added the CoreMIDI framework and AirPlay audio support.

**AirPlay audio** ended up being very simple: any existing `MPVolumeView` would allow you to select an AirPlay destination for your application's audio. Many applications required zero code changes if they already featured an `MPVolumeView`.

I have no experience with this framework but from the look of it, **[CoreMIDI](http://developer.apple.com/library/ios/documentation/MusicAudio/Reference/CACoreMIDIRef/_index.html)** appears to be for controlling MIDI devices over the network, not for actually playing/synthesizing on the iPhone/iPod/iPad so it is perhaps only tangentially related to media on an iOS device.

### Code maintenance considerations

If any `MPVolumeView`s in your program are too small, they won't be able to show the AirPlay controls, so a new minimum width requirement is effectively established.

## iOS 4.3

The biggest addition in iOS 4.3 was **AirPlay video**. In essence this only required you set the flag `allowsAirPlay` to `YES` on the `MPMoviePlayerController`.

Additionally a large set of **logging, error tracking and statistics gathering** APIs were added to the AV media classes ([AVPlayerItemAccessLog](file:///Developer/Platforms/iPhoneOS.platform/Developer/Documentation/DocSets/com.apple.adc.documentation.AppleiOS4_3.iOSLibrary.docset/Contents/Resources/Documents/documentation/AVFoundation/Reference/AVPlayerItemAccessLog_Class/Reference/Reference.html#//apple_ref/occ/cl/AVPlayerItemAccessLog), [AVPlayerItemErrorLog](file:///Developer/Platforms/iPhoneOS.platform/Developer/Documentation/DocSets/com.apple.adc.documentation.AppleiOS4_3.iOSLibrary.docset/Contents/Resources/Documents/documentation/AVFoundation/Reference/AVPlayerItemErrorLog_Class/Reference/Reference.html#//apple_ref/occ/cl/AVPlayerItemErrorLog)) and `MPMoviePlayerController` ([MPMovieAccessLog](http://developer.apple.com/library/ios/documentation/MediaPlayer/Reference/MPMovieAccessLog_Class/Reference/Reference.html), [MPMovieErrorLog](http://developer.apple.com/library/ios/documentation/MediaPlayer/Reference/MPMovieErrorLog_Class/Reference/Reference.html)).

### Code maintenance considerations

The `allowsAirPlay` flag on the `MPMoviePlayerController` carries with it an implicit requirement: that you're actually using `MPMoviePlayerController`. If you've been playing media with a different API, then you'll need to switch to `MPMoviePlayerController` to take advantage of AirPlay video. This was the biggest change that StreamToMe required for iOS 4.3 — since StreamToMe uses the `AVQueuePlayer` by default (for its superior track transitions and more detailed track and asset control) it needed to allow switching to the `MPMoviePlayerController` in the case where AirPlay video is desired. For a program as focussed on media play as StreamToMe, allowing a runtime switch between two interfaces at the core of the program was a big effort. Fortunately, StreamToMe has always had `MPMoviePlayerController` code for supported iOS prior to 4.1 but this was the first time a dynamic switch between interfaces had been needed.

The second change, much less expected since it wasn't really documented, it that iOS 4.3 no longer lets you observe the `playerItem.asset.tracks` key path of an `AVQueuePlayer`, instead you must now observe `playerItem.tracks.assetTrack` key path to get the same value. Technically while linked against iOS 4.2, you can still observe the old key path even when running on iOS 4.3 but it suddenly incurs a dramatic performance hit. Finding the exact cause of this issue was time consuming — as I said, it wasn't documented in any change notes I could find.

The final point that made compatibility difficult: if you have an `MPMoviePlayerController` with `allowsAirPlay` set to `YES` and `useApplicationAudioSession` set to `NO`, and the `MPMoviePlayerController` wants to launch straight to the Apple TV without displaying on the local device first, then the entire movie player interface disappears, never to return. This is undoubtedly a temporary bug but it provided another unexpected reason to make maintenance updates to StreamToMe.

## Conclusion

This has been a lot of classes and functions to summarize. I hope I haven't missed anything important.

Obviously, I'm closer to the media APIs than to some other traits of iOS (so I might have a skewed perspective on their prominence) but I think that the media APIs are close to the most, if not the most updated area of iOS. Attempting to keep media applications up-to-date with the latest media features available remains a busy task.

Of course despite the huge amount of work (on the part of both Apple and the 3rd party application developers) these additions have certainly improved the media experience in iOS. The original iPhone OS felt hugely limiting at the time and users were certainly crying out for the additions that have appeared. The idea that the only movie player interface used to be fullscreen, the only audio playback API was AudioQueue or raw AudioUnits, there was no programmatic camera access and no access to the iPod library in the original iPhone OS highlights how many more options are now available.

Of course, the constant changes to the API also leave me feeling embarrassed when they trip me up or otherwise get ahead of my release schedules. The StreamToMe 3.5.2 update is coming soon, I promise!
