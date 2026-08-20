---
title: AV Foundation Release Notes
apple_id: TP40010717
resource_type: Release Note
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2011-10-12'
source_url: https://developer.apple.com/library/archive/releasenotes/AudioVideo/RN-AVFoundation/index.html
archived_at: '2026-07-18T02:50:21.430418Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# AV Foundation Release Notes for iOS 5

This article summarizes some of the new features and changes in functionality in AV Foundation in iOS 5.

#### Contents:

- [UTIs and MIME types](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydomjxfvbuqmjnknlte)
- [Preparing an AVAsset for playback](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydomjxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Selection of audio and subtitle media according to language and other criteria](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydomjxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Advice about subtitles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydomjxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)
- [AirPlay support in AVPlayer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydomjxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6na)
- [Determining whether fast forward and fast reverse playback are available](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydomjxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6ni)
- [Seeking and, having sought, knowing that the seeking is done](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydomjxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6nq)
- [Advice about scrubbing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydomjxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6ny)
- [Background and foreground transitions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydomjxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6oa)
- [Audio playback under the locked screen](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydomjxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mjr)
- [Receiving rotated CVPixelBuffers from AVCaptureVideoDataOutput](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydomjxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mjs)
- [Setting minimum and maximum video frame rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydomjxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mjt)
- [Discovering pixel formats supported by AVCaptureVideoDataOutput](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydomjxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mju)
- [Determining when a re-focus is necessary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydomjxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mjv)
- [Determining flash and torch availability](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydomjxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mjw)
- [Using the LED torch as a flashlight](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydomjxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mjx)
- [Finding connections with a given media type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydomjxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mjy)
- [Scaling and cropping still images](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydomjxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mjz)
- [Driving a camera shutter animation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydomjxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mrq)
- [Enhancements for streaming video applications](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydomjxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mrr)
- [Capturing movies for editing applications](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydomjxfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mrs)

### UTIs and MIME types

New class methods have been defined on AVURLAsset that provide information about file types and MIME types supported by AVFoundation.

- +audiovisualTypes provides an NSArray containing Universal Type Identifiers (UTIs) that the AVURLAsset class supports.
- +audiovisualMIMETypes provides an NSArray containing MIME types that the AVURLAsset class supports.
- +isPlayableExtendedMIMEType: can be used to determine whether a MIME type that includes the codecs parameter, as described by RFC 4281, indicates a type of resource that's playable by the current platform, device, and software revision.

Note that a definitive determination of whether a particular resource is playable or is suitable for any other purpose requires an examination of its contents; -[AVAsset isPlayable] and other methods in the category AVAssetUsability are available for that purpose.

### Preparing an AVAsset for playback

The current revision of _[AVFoundation Programming Guide](../../documentation/Audio%20Video/AVFoundation%20Programming%20Guide/About%20AVFoundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcoby)_ recommends for all file-based assets that applications load the value of the tracks property of an asset before creating an AVPlayerItem with it and associating the AVPlayerItem with an instance of AVPlayer. While this recommendation is still the best practice for all applications with a deployment target of iOS 4.0-4.3, applications with a deployment target of iOS 5.0 or later need no longer load properties of an AVAsset before creating an AVPlayerItem with it and playing the AVPlayerItem. Instead, those applications need load only the values of properties of an AVAsset that they will examine or process themselves, to display in a user interface, for configuration of playback, or for any other purpose. Starting with iOS 5.0, AVPlayer takes care of its own loading needs.

### Selection of audio and subtitle media according to language and other criteria

AVFoundation now offers features for the discovery of options that may be offered by audiovisual media resources to accommodate differing language preferences, accessibility requirements, custom application configurations, and other needs, and for selection of these options for playback. For example, a resource may contain multiple audible options, each with dialog spoken in a different language, to be selected for playback to the exclusion of the others. Similar options in multiple languages can also be provided for legible media, such as subtitles. Both file-based content and HTTP Live Streaming content can offer media options.
To obtain information about the groups of options that are offered by an instance of AVAsset:

- Load the value of the AVAsset key availableMediaCharacteristicsWithMediaSelectionOptions using AVAsynchronousKeyValueLoading. When loading is complete, -[AVAsset availableMediaCharacteristicsWithMediaSelectionOptions] will provide an NSArray that may contain AVMediaCharacteristicAudible, AVMediaCharacteristicLegible, or AVMediaCharacteristicVisual, or any combination of these, to indicate the availability of groups of mutually exclusive options.
- Each group of mutually exclusive options with a media characteristic of interest can be obtained via -[AVAsset mediaSelectionGroupForMediaCharacteristic:]. To obtain the audible options, pass AVMediaCharacteristicAudible, etc. Each group is represented by an instance of AVMediaSelectionGroup. Each option within a group is represented by an instance of AVMediaSelectionOption. Both of these classes are defined in AVMediaSelectionGroup.h.

To examine available options within a group and to filter them for selection for playback:

- AVMediaSelectionGroup offers methods in the category AVMediaSelectionOptionFiltering that perform common filtering operations on arrays of AVMediaSelectionOptions, according to whether the options are playable, match a desired locale, or either have or do not have special media characteristics, such as whether they offer specific features for accessibility. Media characteristics that indicate the presence of accessibility features, which can be used to filter media selection options, have been defined in AVMediaFormat.h.
- AVMediaSelectionOption offers information about options that may be used for display in a user interface that allows users to select among available options or in the implementation of client-defined filtering operations. As an example of client-defined filtering option in an application that makes use of custom media resources, options may be considered eligible for selection only if their associated metadata contains a specific value.
- To select a specific option within a group for playback, use -[AVPlayerItem selectMediaOption:inMediaSelectionGroup:]. To discover the option that's currently selected for playback, use -[AVPlayerItem selectedMediaOptionInMediaSelectionGroup:].

### Advice about subtitles

Special care should be taken when displaying options to the user among the available legible options for playback and when making a selection among the available legible options according to user preferences. Some legible content contains "forced" subtitles, meaning that according to the content author's intent the subtitles should be displayed when the user has neither indicated a preference for the display of subtitles nor made an explicit selection of a subtitle option. Forced subtitles are typically used in order to convey the meaning of spoken dialog or visible text in a language that the content provider assumes will not be commonly understood, when comprehension of the dialog or text is nevertheless considered to be essential. Be sure that your app allows them to be displayed appropriately by following the advice below.

An AVMediaSelectionGroup for the characteristic AVMediaCharacteristicLegible can provide two types of legible options: 1) for display of legible content that's considered to be elective along with content that's considered to be essential, and 2) for display of essential legible content only. Legible AVMediaSelectionOptions that include essential content only have the media characteristic AVMediaCharacteristicContainsOnlyForcedSubtitles (defined in AVMediaFormat.h). When offering legible options for display to the end user in a selection interface, or when considering subtitle options for automatic selection according to a user preference for language, legible options with the characteristic AVMediaCharacteristicContainsOnlyForcedSubtitles should be excluded. +[AVMediaSelectionOption mediaSelectionOptionsFromArray:withoutMediaCharacteristics:], specifying AVMediaCharacteristicContainsOnlyForcedSubtitles as a characteristic to exclude, can be used to obtain the legible options that are suitable to offer to the end user in a selection interface or for consideration for selection according to a user preference.

If the user indicates no preference for or makes no selection of legible content, the application should select one of the legible options for playback that has the characteristic AVMediaCharacteristicContainsOnlyForcedSubtitles, if any are present. For most resources containing legible options with forced-only subtitles, an appropriate selection among them can be made in accordance with the current audible selection. Use -[AVMediaSelectionOption associatedMediaSelectionOptionInMediaSelectionGroup:] to obtain the legible option associated with an audible option. If there is no other means available to choose among them, the first legible option with forced-only subtitles in the media selection group is an appropriate default.

### AirPlay support in AVPlayer

Routing of audio and video to another device via AirPlay does not require the intervention or knowledge AVFoundation clients. Users can choose AirPlay routing of any audio or video played by an AVPlayer either by interacting with an instance of MPVolumeView as provided within an application's playback interface or with the System AirPlay Picker that's part of the standard multitasking interface. See the MPVolumeView class reference for details on how to offer AirPlay routing to users within your application's user interface.

Whether audio and video is playing on the local device or remotely via AirPlay, existing interfaces for control of playback as defined on AVPlayer, AVQueuePlayer, and AVPlayerItem will apply.

In addition, AVPlayer now defines properties that allow AVFoundation clients to control AirPlay behaviors and to respond to AirPlay routing.

- allowsAirPlayVideo controls whether the receiver allows video to be routed to an external device via AirPlay. If your application requires that video be displayed locally, typically because the composition of the video with other content that's displayed locally is essential to the experience of your app, set the value of allowsAirPlayVideo to NO. It's also appropriate to set this property to NO for instances of AVPlayer that are used to play audio-only content. The default value is YES.
- airPlayVideoActive indicates whether video is currently being routed to another device via AirPlay. This property is key-value observable. Note that when video is routed to an external device, the AVPlayerLayer you've associated with the AVPlayer will display nothing. Under those circumstances it's appropriate to alter your display to make use of space not otherwise occupied; at a minimum, a message that video is being displayed via AirPlay can be very helpful to users.
- usesAirPlayVideoWhileAirPlayScreenIsActive indicates whether the application prefers that video be displayed via AirPlay Video while the entire screen is being routed to an external device via AirPlay. It's appropriate to set this property to YES when an application is playing video that occupies the entire screen; it allows video to be played by the external device at the highest resolution available.

### Determining whether fast forward and fast reverse playback are available

AVPlayerItem now has properties that allow applications to determine whether playback is possible at forward rates greater than 1.0 and at reverse rates less than -1.0. While such playback rates are possible with all file-based content, they are possible with HTTP Live Streaming content only when the source playlist offers media that allows it. Applications may wish to customize playback controls offered to users to accord with the values of these properties for the currently playing item.

- canPlayFastForward indicates whether rates greater than 1.0 can be set on the associated AVPlayer for forward playback
- canPlayFastReverse indicates whether rates less than -1.0 can be set on the associated AVPlayer for reverse playback

### Seeking and, having sought, knowing that the seeking is done

None of the variants of -seekToTime: as provided by AVPlayer and AVPlayerItem perform a seek operation synchronously. Therefore, without a notification of some kind, it can be difficult to tell whether the full effect of a seek operation has occurred; a determination by observing the effect of a seek on the current time is not always sufficient, because a seek to a nearby time using typical tolerances may have no effect on the current time at all. To provide an indication when a seek operation has either finished or was cancelled, AVPlayer and AVPlayerItem now define methods for seeking that accept a client-specified block to be invoked as a notification.

- -seekToTime:completionHandler: performs the same operation as -seekToTime: and, in addition, invokes the specified block when the seeking operation is either finished or cancelled. The block takes a BOOL parameter to indicate whether the operation was finished.
- -seekToTime:toleranceBefore:toleranceAfter:completionHandler: performs the same operation as -seekToTime:toleranceBefore:toleranceAfter: and, in addition, invokes the specified block when the seeking operation is either finished or cancelled. The block takes a BOOL parameter to indicate whether the operation was finished.

  Note that each successive seek operation, initiated via any of the variants of -seekToTime:, implicitly cancels a prior seek operation that has not yet finished.
- -[AVPlayerItem cancelPendingSeeks] can be used to cancel seek operations explicitly.

### Advice about scrubbing

Scrubbing is the common term for an operation in which the user jumps from time to time within an audiovisual media resource, in arbitrary increments of media time both backward and forward, at arbitrary intervals of real time, sometimes to locate a particular scene of interest and sometimes as a way of previewing the contents of the resource. Scrubbing is commonly implemented by AVFoundation clients as a succession of seek operations, in order to set the current time of an AVPlayerItem to a time indicated by the current or recent position of a UI affordance, such as a slider. As noted above, because each successive seek operation implicitly cancels a prior seek operation, it's important during scrubbing to allow at least some seek operations to finish instead of being cancelled by new ones, so that the user will be presented with a visual indication that scrubbing is in fact having an effect.

One way to ensure that a sufficient number of seek operations will finish and that the user will receive appropriate visual feedback is to chain them. Instead of initiating a new seek operation each time a UI affordance changes position, you can merely note the time that its new position indicates, and when the completion handler for a prior seek is invoked, you can seek to the time indicated by the most recent position of the UI affordance, if that time has changed since the last seek.

### Background and foreground transitions

### To the background

In iOS 4.x, the playback of any instance of AVPlayer is automatically paused as the app that created it is sent to the background whenever the AVPlayer is associated with any instance of AVPlayerLayer, whether the AVPlayerLayer is being displayed onscreen or not, and whether the currently playing item has video media or not.

In iOS 5.0, playback of an AVPlayer is automatically paused as the app that created it is sent to the background only if the AVPlayer's current item is displaying video on the device's display.

### To the foreground

In iOS 4.x, the playback of audio in the background by other applications is automatically interrupted as an AVFoundation client comes to the foreground whenever any instance of AVPlayerLayer exists within the application. The AVPlayerLayer need not be associated with any AVPlayer.

In iOS 5.0, the above behavior continues, except for applications that have a base SDK of iOS 5.0 or later. As those applications come to the foreground, the playback of audio in the background by other applications is automatically interrupted only if they have an AVPlayer with a current item that needs to update the display of video either on the device or on a connected display. Otherwise the playback of background audio will continue until a further user action requires an interruption.

### Audio playback under the locked screen

(When the screen is locked while an app is the frontmost app.)

Applications that have a base SDK of iOS 5 or later:

- When the screen is locked, applications will run in the background. Hence, to continue playing under the locked screen, applications need to have background audio entitlement.
- Applications that configure their audio to be non-mixable must also register for remote-control events to be able to start playing under the locked screen. However, applications that use non-mixable audio but do not register for remote-control events will continue playing under the locked screen if they started playing before the screen was locked.
- Applications whose audio is mixable need only the background audio entitlement to play under the locked screen.

Applications that have a base SDK prior to iOS 5.0:

- When the screen is locked, applications will be able to play audio regardless of background audio entitlement or mixable behavior.

### Receiving rotated CVPixelBuffers from AVCaptureVideoDataOutput

Clients may now receive physically rotated CVPixelBuffers in their AVCaptureVideoDataOutput -captureOutput:didOutputSampleBuffer:fromConnection: delegate callback. In previous iOS versions, the front-facing camera would always deliver buffers in AVCaptureVideoOrientationLandscapeLeft and the back-facing camera would always deliver buffers in AVCaptureVideoOrientationLandscapeRight. All 4 AVCaptureVideoOrientations are supported, and rotation is hardware accelerated. To request buffer rotation, a client calls -setVideoOrientation: on the AVCaptureVideoDataOutput's video AVCaptureConnection. Note that physically rotating buffers does come with a performance cost, so only request rotation if it's necessary. If, for instance, you want rotated video written to a QuickTime movie file using AVAssetWriter, it is preferable to set the -transform property on the AVAssetWriterInput rather than physically rotate the buffers in AVCaptureVideoDataOutput.

### Setting minimum and maximum video frame rate

Since iOS 4.0, clients have been able to adjust the maximum frame rate of video buffers delivered to the AVCaptureVideoDataOutput -captureOutput:didOutputSampleBuffer:fromConnection: delegate callback using [AVCaptureVideoDataOutput setMinFrameDuration:]. In iOS 5, AVCaptureVideoDataOutput's minFrameDuration property has been deprecated, and a new pair of properties introduced in AVCaptureConnection.

- To adjust max frame rate, clients may now use [AVCaptureConnection setVideoMinFrameDuration:].
- New in iOS 5, to adjust min frame rate, clients may use [AVCaptureConnection setVideoMaxFrameDuration:].
- By setting max and min to the same value, clients may achieve constant frame rate capture, at the expense of some low light performance, where the camera would normally throttle the frame rate to achieve longer exposure time.
- Clients may discover whether setting max and min frame duration is supported for a particular connection by calling [AVCaptureConnection isVideoMinFrameDurationSupported] or [AVCaptureConnection isVideoMaxFrameDurationSupported].

### Discovering pixel formats supported by AVCaptureVideoDataOutput

- Clients may now query AVCaptureVideoDataOutput's availableVideoCVPixelFormatTypes property to find out what pixel formats are supported by the current device and platform.
- Compressed video data output is not supported.

### Determining when a re-focus is necessary

Clients of AVCaptureDevice may lock focus, exposure, and/or white balance if the receiver supports it, but once locked, these properties stay locked, even if the subject area changes dramatically due either to substantial movement of the iOS device, or the subjects within the capture device's field of view. A new opt-in mechanism has been added to AVCaptureDevice to allow clients to receive a notification when the subject area changes substantially.

- subjectAreaChangeMonitoringEnabled defaults to NO. When set to YES, the AVCaptureDevice receiver sends a AVCaptureDeviceSubjectAreaDidChangeNotification whenever its subject area changes significantly.
- Clients may wish to re-focus, adjust exposure, or white-balance upon receiving this notification.

### Determining flash and torch availability

Clients of AVCaptureDevice may query whether it -hasFlash or -hasTorch and may turn the flash or torch on. Use of the LED torch generates a lot of heat. Continuous use of the torch or flash could cause the enclosing device to overheat, so, under thermal duress, the flash and torch will turn off automatically. In iOS 5 AVCaptureDevice provides three new properties exposing the current state of the flash and torch.

- flashAvailable is a key-value observable property that toggles to NO when the unit is too hot to use the flash. Clients may query this property to drive flash-related UI.
- torchAvailable is a key-value observable property that toggles to NO when the unit is too hot to use the torch. Clients may query this property to drive torch-related UI.
- torchLevel is a key-value observable property that tells clients the current strength of the torch, where 1.0 is full strength and 0.0 is off. Under thermal duress, the torch may automatically decrease in intensity. Clients may query this property to drive torch-related UI.
- flashActive is a key-value observable property that tells clients whether the flash will be used if [AVCaptureStillImageOutput captureStillImageAsynchronouslyFromConnection:completionHandler:] is called. This is useful if clients have set the flash mode to AVCaptureFlashModeAuto.

### Using the LED torch as a flashlight

Previous iOS releases require AVCaptureSession to be running before a client may turn on the LED torch. Consequently, the full capture stack is allocated and running, resulting in unnecessary power consumption for applications using the LED torch as a flashlight. In iOS 5, it is no longer necessary to run an AVCaptureSession to turn the torch on. Flashlight applications may now simply call:

```
AVCaptureDevice *backCamera = [AVCaptureDevice defaultDeviceWithMediaType:AVMediaTypeVideo];
if ( [backCamera isTorchAvailable] && [backCamera isTorchModeSupported:AVCaptureTorchModeOn]  )
{
    BOOL success = [backCamera lockForConfiguration:nil];
    if ( success )
    {
        [backCamera setTorchMode:AVCaptureTorchModeOn];
        [backCamera unlockForConfiguration];
    }
}
```


### Finding connections with a given media type

The new AVCaptureOutput utility method, -connectionWithMediaType: allows clients to find an output's first connection of a given media type without writing a function iterate through each connection's input ports.

### Scaling and cropping still images

AVCaptureStillImageOutput now supports still image scale and crop to simulate a "digital zoom" effect. To set a scale and crop factor, clients call [AVCaptureConnection setVideoScaleAndCropFactor:] on the still image output's video connection. The value must be between 1.0 (no scaling/cropping) and the result of [AVCaptureConnection videoMaxScaleAndCropFactor]. When the video scale and crop factor is set to a value higher than 1.0, AVCaptureStillImageOutput scales the captured image by the specified factor and center crops the result back to its original size using hardware acceleration.

### Driving a camera shutter animation

AVCaptureStillImageOutput provides a new key-value observable property, -capturingStillImage, whereby a client can find out when a request to [AVCaptureStillImageOutput captureStillImageAsynchronouslyFromConnection:completionHandler:] is being satisfied. -isCapturingStillImage changes to YES right before the picture is taken, and changes to NO right after it is taken. Clients may use this property to drive a camera shutter or iris animation.

### Enhancements for streaming video applications

Clients may use the new AVCaptureSessionPreset352x288 session preset to receive 352x288 (CIF) sized video buffers from the camera. This preset is supported on all devices, front and back cameras. Clients should always call [AVCaptureDevice supportsAVCaptureSessionPreset:] to ensure that the input supports their desired preset.

### Capturing movies for editing applications

AVCaptureSession provides two new session presets to aid in the creation of editable content.

- AVCaptureSessionPresetiFrame960x540 produces quarter-HD video and captures movies using AVCaptureMovieFileOutput at ~30 megabits/second using I-frame only H.264 + AAC audio.
- AVCaptureSessionPresetiFrame1280x720 produces 720p video and captures movies using AVCaptureMovieFileOutput at ~40 megabits/second using I-frame only H.264 + AAC audio.

Using either of these presets, AVCaptureMovieFileOutput captures Apple iFrame compatible movies (see http://support.apple.com/kb/HT3905) that work well in iMovie and in other editing applications.
