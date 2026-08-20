---
title: AVFoundation Programming Guide
apple_id: TP40010188
resource_type: Guide
platform: tvOS|iOS|macOS
topic: null
technology: AVFoundation
published: '2015-06-30'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/AVFoundationPG/Articles/00_Introduction.html
archived_at: '2026-07-15T05:20:54.200770Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Using%20Assets.md)

# About AVFoundation

AVFoundation is one of several frameworks that you can use to play and create time-based audiovisual media. It provides an Objective-C interface you use to work on a detailed level with time-based audiovisual data. For example, you can use it to examine, create, edit, or reencode media files. You can also get input streams from devices and manipulate video during realtime capture and playback. Figure I-1 shows the architecture on iOS.

__Figure I-1__  AVFoundation stack on iOS

!

[Figure I-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcobyfvbuqmjnknltk) shows the corresponding media architecture on OS X.

__Figure I-2__  AVFoundation stack on OS X

!

You should typically use the highest-level abstraction available that allows you to perform the tasks you want.

- If you simply want to play movies, use the AVKit framework.
- On iOS, to record video when you need only minimal control over format, use the UIKit framework ([UIImagePickerController](https://developer.apple.com/documentation/uikit/uiimagepickercontroller)).

Note, however, that some of the primitive data structures that you use in AV Foundation—including time-related data structures and opaque objects to carry and describe media data—are declared in the Core Media framework.

There are two facets to the AVFoundation framework—APIs related to video and APIs related just to audio. The older audio-related classes provide easy ways to deal with audio.

- To play sound files, you can use [AVAudioPlayer](https://developer.apple.com/documentation/avfoundation/avaudioplayer).
- To record audio, you can use [AVAudioRecorder](https://developer.apple.com/documentation/avfoundation/avaudiorecorder).

You can also configure the audio behavior of your application using [AVAudioSession](https://developer.apple.com/documentation/avfoundation/avaudiosession); this is described in _[Audio Session Programming Guide](../../Audio/Audio%20Session%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzv)_.

### Representing and Using Media with AVFoundation

The primary class that the AV Foundation framework uses to represent media is [AVAsset](https://developer.apple.com/documentation/avfoundation/avasset). The design of the framework is largely guided by this representation. Understanding its structure will help you to understand how the framework works. An `AVAsset` instance is an aggregated representation of a collection of one or more pieces of media data (audio and video tracks). It provides information about the collection as a whole, such as its title, duration, natural presentation size, and so on. `AVAsset` is not tied to particular data format. `AVAsset` is the superclass of other classes used to create asset instances from media at a URL (see [Using Assets](Using%20Assets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcobyfvbuqnznknltc)) and to create new compositions (see [Editing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcobyfvbuqmjnknltc)).

Each of the individual pieces of media data in the asset is of a uniform type and called a _track_. In a typical simple case, one track represents the audio component, and another represents the video component; in a complex composition, however, there may be multiple overlapping tracks of audio and video. Assets may also have metadata.

A vital concept in AV Foundation is that initializing an asset or a track does not necessarily mean that it is ready for use. It may require some time to calculate even the duration of an item (an MP3 file, for example, may not contain summary information). Rather than blocking the current thread while a value is being calculated, you ask for values and get an answer back asynchronously through a callback that you define using a [block](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3).

#### Playback

AVFoundation allows you to manage the playback of asset in sophisticated ways. To support this, it separates the presentation state of an asset from the asset itself. This allows you to, for example, play two different segments of the same asset at the same time rendered at different resolutions. The presentation state for an asset is managed by a _player item_ object; the presentation state for each track within an asset is managed by a _player item track_ object. Using the player item and player item tracks you can, for example, set the size at which the visual portion of the item is presented by the player, set the audio mix parameters and video composition settings to be applied during playback, or disable components of the asset during playback.

You play player items using a _player_ object, and direct the output of a player to the Core Animation layer. You can use a _player queue_ to schedule playback of a collection of player items in sequence.

#### Reading, Writing, and Reencoding Assets

AVFoundation allows you to create new representations of an asset in several ways. You can simply reencode an existing asset, or—in iOS 4.1 and later—you can perform operations on the contents of an asset and save the result as a new asset.

You use an _export session_ to reencode an existing asset into a format defined by one of a small number of commonly-used presets. If you need more control over the transformation, in iOS 4.1 and later you can use an _asset reader_ and _asset writer_ object in tandem to convert an asset from one representation to another. Using these objects you can, for example, choose which of the tracks you want to be represented in the output file, specify your own output format, or modify the asset during the conversion process.

To produce a visual representation of the waveform, you use an asset reader to read the audio track of an asset.

#### Thumbnails

To create thumbnail images of video presentations, you initialize an instance of [AVAssetImageGenerator](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator) using the asset from which you want to generate thumbnails. `AVAssetImageGenerator` uses the default enabled video tracks to generate images.

#### Editing

AVFoundation uses _compositions_ to create new assets from existing pieces of media (typically, one or more video and audio tracks). You use a mutable composition to add and remove tracks, and adjust their temporal orderings. You can also set the relative volumes and ramping of audio tracks; and set the opacity, and opacity ramps, of video tracks. A composition is an assemblage of pieces of media held in memory. When you export a composition using an _export session_, it’s collapsed to a file.

You can also create an asset from media such as sample buffers or still images using an _asset writer_.

#### Still and Video Media Capture

Recording input from cameras and microphones is managed by a _capture session_. A capture session coordinates the flow of data from input devices to outputs such as a movie file. You can configure multiple inputs and outputs for a single session, even when the session is running. You send messages to the session to start and stop data flow.

In addition, you can use an instance of a _preview layer_ to show the user what a camera is recording.

### Concurrent Programming with AVFoundation

Callbacks from AVFoundation—invocations of [blocks](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3), [key-value observers](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16), and [notification](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Notification.html#//apple_ref/doc/uid/TP40008195-CH35) handlers—are not guaranteed to be made on any particular thread or queue. Instead, AVFoundation invokes these handlers on threads or queues on which it performs its internal tasks.

There are two general guidelines as far as notifications and threading:

- UI related notifications occur on the main thread.
- Classes or methods that require you create and/or specify a queue will return notifications on that queue.

Beyond those two guidelines (and there are exceptions, which are noted in the reference documentation) you should not assume that a notification will be returned on any specific thread.

If you’re writing a multithreaded application, you can use the `NSThread` method [isMainThread](https://developer.apple.com/documentation/foundation/thread/1408455-ismainthread) or `[[NSThread currentThread] isEqual:<#A stored thread reference#>]` to test whether the invocation thread is a thread you expect to perform your work on. You can redirect messages to appropriate threads using methods such as [performSelectorOnMainThread:withObject:waitUntilDone:](https://developer.apple.com/documentation/objectivec/nsobject/1414900-performselector) and [performSelector:onThread:withObject:waitUntilDone:modes:](https://developer.apple.com/documentation/objectivec/nsobject/1417922-perform). You could also use [dispatch_async](https://developer.apple.com/documentation/dispatch/1453057-dispatch_async) to “bounce” to your blocks on an appropriate queue, either the main queue for UI tasks or a queue you have up for concurrent operations. For more about concurrent operations, see _[Concurrency Programming Guide](../../General/Concurrency%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojr)_; for more about blocks, see _[Blocks Programming Topics](../../Cocoa/Blocks%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tkmbs)_. The _[AVCam-iOS: Using AVFoundation to Capture Images and Movies](https://developer.apple.com/library/archive/samplecode/AVCam/Introduction/Intro.html#//apple_ref/doc/uid/DTS40010112)_ sample code is considered the primary example for all AVFoundation functionality and can be consulted for examples of thread and queue usage with AVFoundation.

AVFoundation is an advanced Cocoa framework. To use it effectively, you must have:

- A solid understanding of fundamental Cocoa development tools and techniques
- A basic grasp of [blocks](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3)
- A basic understanding of [key-value coding](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KeyValueCoding.html#//apple_ref/doc/uid/TP40008195-CH25) and [key-value observing](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16)
- For playback, a basic understanding of Core Animation (see _[Core Animation Programming Guide](../../Cocoa/Core%20Animation%20Programming%20Guide/About%20Core%20Animation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmju)_ or, for basic playback, the _[AVKit Framework Reference](https://developer.apple.com/documentation/avkit)_.

There are several AVFoundation examples including two that are key to understanding and implementation Camera capture functionality:

- _[AVCam-iOS: Using AVFoundation to Capture Images and Movies](https://developer.apple.com/library/archive/samplecode/AVCam/Introduction/Intro.html#//apple_ref/doc/uid/DTS40010112)_ is the canonical sample code for implementing any program that uses the camera functionality. It is a complete sample, well documented, and covers the majority of the functionality showing the best practices.
- _[AVCamManual: Extending AVCam to Use Manual Capture API](../../../samplecode/AVCamManual-%20Extending%20AVCam%20to%20Use%20Manual%20Capture%20API/AVCamManual-%20Extending%20AVCam%20to%20Use%20Manual%20Capture%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dknzy)_ is the companion application to AVCam. It implements Camera functionality using the manual camera controls. It is also a complete example, well documented, and should be considered the canonical example for creating camera applications that take advantage of manual controls.
- _[RosyWriter](../../../samplecode/RosyWriter/RosyWriter.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmjrga)_ is an example that demonstrates real time frame processing and in particular how to apply filters to video content. This is a very common developer requirement and this example covers that functionality.
- _[AVLocationPlayer: Using AVFoundation Metadata Reading APIs](../../../samplecode/AVLocationPlayer-%20Using%20AVFoundation%20Metadata%20Reading%20APIs/AVLocationPlayer-%20Using%20AVFoundation%20Metadata%20Reading%20APIs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diojv)_ demonstrates using the metadata APIs.
[Next](Using%20Assets.md)

