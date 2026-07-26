---
title: 'What''s New in iOS SDK 4.3'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/03/whats-new-in-ios-sdk-4-3/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:64bfd63fccb4197a'
translated: false
---

> 原文：[What's New in iOS SDK 4.3](https://oleb.net/blog/2011/03/whats-new-in-ios-sdk-4-3/)　·　Ole Begemann

# What's New in iOS SDK 4.3

Now that the [final version of iOS SDK 4.3](http://developer.apple.com/devcenter/ios/) is available, let’s have a look at what is new. What follows is a detailed overview of the [What’s New in iOS 4.3](http://developer.apple.com/library/ios/releasenotes/General/WhatsNewIniPhoneOS/Articles/iOS4_3.html#//apple_ref/doc/uid/TP40010567-SW1) and [iOS 4.3 API Diffs](http://developer.apple.com/library/ios/releasenotes/General/iOS43APIDiffs/index.html#//apple_ref/doc/uid/TP40010594) documents. Compared to the [changes in iOS SDK 4.2](https://oleb.net/blog/2010/11/whats-new-in-ios-sdk-4-2/), the 4.3 update is rather small.

# No more iPhone 3G support

iOS 4.3 drops support for the iPhone 3G and second-generation iPod touch. So if you need your apps to run on these devices, be sure to not require any of the new features.

# App switching gestures on the iPad

Apple introduced [new four and five finger gestures](http://developer.apple.com/library/ios/#releasenotes/General/RN-iOSSDK-4_3/_index.html) to switch between apps on the iPad. These gestures are not yet activated for consumers, but developers can enable them in Settings. If your app uses gestures that potentially use four or more fingers, you should test it for possible interference with the new multitasking gestures and discuss your concerns in the Apple Developer Forums.

# AirPlay for everybody

After introducing AirPlay in iOS 4.2 for some of Apple’s own apps, the feature can now be used by all third-party apps that play video through [MPMoviePlayerController](http://developer.apple.com/library/ios/documentation/MediaPlayer/Reference/MPMoviePlayerController_Class/Reference/Reference.html#//apple_ref/occ/cl/MPMoviePlayerController). AirPlay is disabled by default, but all you have to do is set the [`allowsAirPlay`](http://developer.apple.com/library/ios/documentation/MediaPlayer/Reference/MPMoviePlayerController_Class/Reference/Reference.html#//apple_ref/occ/instp/MPMoviePlayerController/allowsAirPlay) to `YES` and the OS manages the display of the AirPlay button for you as soon as it detects an AirPlay device nearby.

You can also [enable AirPlay for web-based video content](http://developer.apple.com/library/ios/releasenotes/General/WhatsNewIniPhoneOS/Articles/iOS4_3.html#//apple_ref/doc/uid/TP40010567-SW1) embedded through the QuickTime Plug-in or HTML5 video element.

# Framework Changes

## AV Foundation

### Chapter information in AVAsset

`AVAsset` can now access the chapters an asset contains with the new method [`chapterMetadataGroupsWithTitleLocale:containingItemsWithCommonKeys:`](https://developer.apple.com/reference/avfoundation/avasset/1388966-chaptermetadatagroups). Each chapter is returned in the form of an `AVMetadataItem` containing the chapter’s title and time range. This looks super-useful for apps that work with podcasts or audiobooks. The new property [`availableChapterLocales`](https://developer.apple.com/reference/avfoundation/avasset/1388228-availablechapterlocales) can tell you the locales in which chapter information is available.

### AVAsset usage restrictions

Some new properties of `AVAsset` provide information on what this asset can be used for:

- `composable`

  :
- `exportable`

  :
- `playable`

  :
- `readable`

  :

### Network playback statistics

When playing a network stream, you can now track network playback statistics through two new methods on `AVPlayerItem`, [`accessLog`](https://developer.apple.com/reference/avfoundation/avplayeritem/1388499-accesslog) and [`errorLog`](https://developer.apple.com/reference/avfoundation/avplayeritem/1387573-errorlog). These methods return instances of [`AVPlayerItemAccessLog`](https://developer.apple.com/reference/avfoundation/avplayeritemaccesslog) and [`AVPlayerItemErrorLog`](https://developer.apple.com/reference/avfoundation/avplayeritemerrorlog), respectively, which in turn contain arrays of [`AVPlayerItemAccessLogEvent`](https://developer.apple.com/reference/avfoundation/avplayeritemaccesslogevent) or [`AVPlayerItemErrorLogEvent`](https://developer.apple.com/reference/avfoundation/avplayeritemerrorlogevent) instances that represent the single log events.

### Asynchronous metadata loading

The `AVMetadataItem` class can now load metadata asynchronously. Call [`loadValuesAsynchronouslyForKeys:completionHandler:`](https://developer.apple.com/reference/avfoundation/avmetadataitem/1387102-loadvaluesasynchronously) to initiate the load process and [`statusOfValueForKey:error:`](https://developer.apple.com/reference/avfoundation/avmetadataitem/1388523-statusofvalue) to check if the metadata for a key has been loaded.

### New metadata keys

In addition, Apple has defined some very interesting-looking-but-so-far-undocumented new constants for metadata keys: `AVMetadataQuickTimeMetadataKeyCollectionUser`, `AVMetadataQuickTimeMetadataKeyDirectionFacing`, `AVMetadataQuickTimeMetadataKeyDirectionMotion`, `AVMetadataQuickTimeMetadataKeyLocationBody`, `AVMetadataQuickTimeMetadataKeyLocationDate`, `AVMetadataQuickTimeMetadataKeyLocationName`, `AVMetadataQuickTimeMetadataKeyLocationNote`, `AVMetadataQuickTimeMetadataKeyLocationRole`, `AVMetadataQuickTimeMetadataKeyRatingUser`, and `AVMetadataQuickTimeMetadataKeyTitle`.

These look as if there would be metadata not only about the location of a video, but also about the direction the camera is facing and the movement of the camera over the duration of the video. It would be interesting to check if a video taken with the iPhone actually contains this metadata (I haven’t checked).

### Metadata groups

[`AVTimedMetadataGroup`](https://developer.apple.com/reference/avfoundation/avtimedmetadatagroup) is a new class to represent a collection of `AVMetadataItem`s over a specified time range. The class also has a mutable counterpart, [`AVMutableTimedMetadataGroup`](https://developer.apple.com/reference/avfoundation/avmutabletimedmetadatagroup).

## Core Audio

Let me just quote from [Apple’s What’s New document](http://developer.apple.com/library/ios/releasenotes/General/WhatsNewIniPhoneOS/Articles/iOS4_3.html#//apple_ref/doc/uid/TP40010567-SW1) here because I haven’t got anything to add:

> The Audio Unit and Audio Toolbox frameworks include the following enhancements:
> 
> - `AudioUnitParameterHistoryInfo`
> 
>   struct (in the Audio Unit framework) along with supporting audio unit properties adds the ability to track and use parameter automation history.
> - `ExtendedAudioFormatInfo`
> 
>   struct (in the Audio Toolbox framework) lets you specify which codec to use when accessing the
> 
>   `kAudioFormatProperty_FormatList`
> 
>   property.
> - `kAFInfoDictionary_SourceBitDepth`
> 
>   dictionary key and the
> 
>   `kAudioFilePropertySourceBitDepth`
> 
>   property (in the Audio Toolbox framework) provide access to the bit depth of an audio stream.
> - `kAudioConverterErr_NoHardwarePermission`
> 
>   result code (in the Audio Toolbox framework) indicates that a request to create a new audio converter object cannot be satisfied because the application does not have permission to use the requested hardware codec.

## Core Foundation

In iOS SDK 4.2, the `CFStringGetHyphenationLocationBeforeIndex()` function was added to hyphenate `CFString`s. In iOS SDK 4.3, we got another new function, `CFStringIsHyphenationAvailableForLocale()`, to ask the system if hyphenation information is available for the specified locale.

## Core Text

Apple added some new constants to the Core Text framework. They are not documented yet (besides the comments in the header files), but it seems that Core Text on iOS supports a few new font traits and formatting settings, such as line spacing in paragraphs or non-rectangular clipping paths for `CTFrame`s. The new stuff:

- (

  ;

  )
- (

  ;

  )
- and

  (

  ;

  )
- ,

  , and

  (

  ;

  )
- `kCTVerticalFormsAttributeName`

  (

  ;

  )

## iAd

In addition to small banners, iAd now also supports full-screen ads on the iPad (to be used, for instance, as full-page ads in a magazine app). Use the new [`ADInterstitialAd`](http://developer.apple.com/library/ios/#documentation/iAd/Reference/ADInterstitialAd_Ref/Introduction/Introduction.html#//apple_ref/occ/cl/ADInterstitialAd) class to display them.

iAd also got a new error state, [ADErrorApplicationInactive](http://developer.apple.com/library/ios/#documentation/UserExperience/Reference/ADBannerView_Ref/Reference/Reference.html#//apple_ref/c/econst/ADErrorApplicationInactive).

# ImageIO

Apple defined some new constants to make it easier to retrieve some frequently needed EXIF information about camera and lens model from a `CGImageSourceRef`. Namely:

- `kCGImagePropertyExifBodySerialNumber`
- `kCGImagePropertyExifCameraOwnerName`
- `kCGImagePropertyExifLensMake`
- `kCGImagePropertyExifLensModel`
- `kCGImagePropertyExifLensSerialNumber`
- `kCGImagePropertyExifLensSpecification`

Call [`CGImageSourceCopyProperties()`](https://developer.apple.com/library/ios/#documentation/GraphicsImaging/Reference/CGImageSource/Reference/reference.html) to retrieve an image’s EXIF dictionary.

## MediaPlayer

Besides AirPlay support, the `MPMoviePlayerController` class also gained new properties to track network playback statistics, analogous to the AV Foundation framework.

If the player is playing a network stream, [`accessLog`](http://developer.apple.com/library/ios/#documentation/MediaPlayer/Reference/MPMoviePlayerController_Class/Reference/Reference.html#//apple_ref/occ/instp/MPMoviePlayerController/accessLog) and [`errorLog`](http://developer.apple.com/library/ios/#documentation/MediaPlayer/Reference/MPMoviePlayerController_Class/Reference/Reference.html#//apple_ref/occ/instp/MPMoviePlayerController/errorLog) reference instances of two new classes, [`MPMovieAccessLog`](http://developer.apple.com/library/ios/#documentation/MediaPlayer/Reference/MPMovieAccessLog_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40010561) and [`MPMovieErrorLog`](http://developer.apple.com/library/ios/#documentation/MediaPlayer/Reference/MPMovieErrorLog_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40010562), each containing arrays of [`MPMovieAccessLogEvent`](http://developer.apple.com/library/ios/#documentation/MediaPlayer/Reference/MPMovieAccessLogEvent_Class/Reference/Reference.html#//apple_ref/occ/cl/MPMovieAccessLogEvent) or [`MPMovieErrorLogEvent`](http://developer.apple.com/library/ios/#documentation/MediaPlayer/Reference/MPMovieErrorLogEvent_Class/Reference/Reference.html#//apple_ref/occ/cl/MPMovieErrorLogEvent), respectively.

## UIKit

- `UIViewController` has a new method called [`disablesAutomaticKeyboardDismissal`](https://developer.apple.com/reference/uikit/uiviewcontroller/1621385-disablesautomatickeyboarddismiss), which you can override to control whether the keyboard should be dismissed automatically when the user changes from a control that uses the keyboard to one that does not. By default, this method returns `NO`, except when a view controller is presented modally with its modal presentation style set to `UIModalPresentationFormSheet`.
- To support the new [screen mirroring feature](http://www.apple.com/ipad/features/mirroring.html) in the iPad 2, a new read-only property was added to `UIScreen`: if screen mirrroring is active, [`mirroredScreen`](http://developer.apple.com/library/ios/#documentation/UIKit/Reference/UIScreen_Class/Reference/UIScreen.html#//apple_ref/occ/instp/UIScreen/mirroredScreen) will contain the screen object that is being mirrored (the device’s main screen).
- Another new `UIScreen` property: `preferredMode` (undocumented so far) is the preferred `UIScreenMode` of the screen in question. From the header file: Choosing this mode will likely produce the best results.
