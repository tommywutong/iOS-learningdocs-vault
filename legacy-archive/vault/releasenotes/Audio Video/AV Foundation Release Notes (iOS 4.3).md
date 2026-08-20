---
title: AV Foundation Release Notes (iOS 4.3)
apple_id: TP40011199
resource_type: Release Note
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2011-10-12'
source_url: https://developer.apple.com/library/archive/releasenotes/AudioVideo/RN-AVFoundation-Old/index.html
archived_at: '2026-07-18T02:50:21.306525Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# AV Foundation Release Notes for iOS 4.3

This article summarizes some of the new features and changes in functionality in AV Foundation in iOS 4.3.

#### Contents:

- [Determining Whether an Operation Can Be Performed on an Asset](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojzfvbuqmjnknlte)
- [Enhancements for HTTP Live Streaming](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojzfvbuqmjnknltg)
- [Duration of Timed Media Resources for Playback](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojzfvbuqmjnknlti)
- [Determining Whether an Item Has Played Successfully](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojzfvbuqmjnknltk)
- [Access to Chapter Metadata](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojzfvbuqmjnknltm)
- [Attempting to Run an AVCaptureSession in the Background](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojzfvbuqmjnknlto)

### Determining Whether an Operation Can Be Performed on an Asset

Four new properties have been defined on [AVAsset](https://developer.apple.com/documentation/avfoundation/avasset) to help you determine whether a operations supported by AV Foundation can be performed on a particular asset.

- [playable](https://developer.apple.com/documentation/avfoundation/avasset/1385974-playable) indicates whether an [AVPlayerItem](https://developer.apple.com/documentation/avfoundation/avplayeritem) initialized with asset can be played by an [AVPlayer](https://developer.apple.com/documentation/avfoundation/avplayer).
- [exportable](https://developer.apple.com/documentation/avfoundation/avasset/1389245-isexportable) indicates whether an [AVAssetExportSession](https://developer.apple.com/documentation/avfoundation/avassetexportsession) initialized with an asset can produce an output file.
- [readable](https://developer.apple.com/documentation/avfoundation/avasset/1390475-readable) indicates whether an [AVAssetReader](https://developer.apple.com/documentation/avfoundation/avassetreader) initialized with an asset can provide media derived or extracted from the asset.
- [composable](https://developer.apple.com/documentation/avfoundation/avasset/1386129-composable) indicates whether the asset or any of its [AVAssetTrack](https://developer.apple.com/documentation/avfoundation/avassettrack) objects can be inserted into an [AVMutableComposition](https://developer.apple.com/documentation/avfoundation/avmutablecomposition).

Note that the value of each of these properties is `YES` even if the associated operation is only conditionally supported. Examples:

- `playable` is `YES` even if the asset has protected content and requires authorization of both the application and the content for playback. You can determine whether an asset has protected content via [hasProtectedContent](https://developer.apple.com/documentation/avfoundation/avasset/1389223-hasprotectedcontent) (`AVAsset`).
- `exportable` is `YES` even if only some of the export presets are compatible with the asset. You can obtain an array of export presets that can be used with an asset via [exportPresetsCompatibleWithAsset:](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1390567-exportpresetscompatiblewithasset) (`AVAssetExportSession`).
- `readable` is `YES` even if only some classes of [AVAssetReaderOutput](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput) or only some configurations of settings on the outputs can be used with the asset. You can determine whether a particular instance of `AVAssetReaderOutput` with its settings can be used by invoking [canAddOutput:](https://developer.apple.com/documentation/avfoundation/avassetreader/1387485-canadd).

### Enhancements for HTTP Live Streaming

The inspection features of [AVURLAsset](https://developer.apple.com/documentation/avfoundation/avurlasset) have been enhanced to handle HTTP Live Streaming Media resources. For this reason, starting with iOS 4.3 you can prepare any asset for playback in a uniform way, according to the best practices originally outlined for file-based assets in the _[AVFoundation Programming Guide](../../documentation/Audio%20Video/AVFoundation%20Programming%20Guide/About%20AVFoundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcoby)_. Those steps are as follows:

1. Create an asset using `AVURLAsset` and load its tracks using [loadValuesAsynchronouslyForKeys:completionHandler:](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/1387321-loadvaluesasynchronouslyforkeys).
2. When the asset has loaded its tracks, create an instance of [AVPlayerItem](https://developer.apple.com/documentation/avfoundation/avplayeritem) using the asset.
3. Associate the item with an instance of [AVPlayer](https://developer.apple.com/documentation/avfoundation/avplayer).
4. Wait until the item’s status indicates that it’s ready to play.

   Typically you use key-value observing to receive a notification when the status changes.

While you can still prepare stream-based assets for playback according to the steps described specifically for them in the _[AVFoundation Programming Guide](../../documentation/Audio%20Video/AVFoundation%20Programming%20Guide/About%20AVFoundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcoby)_, starting with iOS 4.3 it’s no longer necessary to do so and therefore no longer necessary for you to determine whether a URL references HTTP Live Streaming Media.

Note that `AVURLAsset` provides information about the persistent state of a timed media resource. Because of the dynamic nature of HTTP Live Streaming Media, the duration of the media and the specifics of the tracks available can change during playback. Therefore URL assets initialized with URLs that reference HTTP Live Streaming Media may have values for their duration and tracks properties that are different from the values of the duration and tracks properties of [AVPlayerItem](https://developer.apple.com/documentation/avfoundation/avplayeritem) objects that play them. In particular, the duration reported by the URL asset for streaming-based media is typically [kCMTimeIndefinite](https://developer.apple.com/documentation/coremedia/kcmtimeindefinite), while the duration of a corresponding `AVPlayerItem` may be different and may change while it plays. Similarly, the array of [AVAssetTrack](https://developer.apple.com/documentation/avfoundation/avassettrack) objects available via the [tracks](https://developer.apple.com/documentation/avfoundation/avasset/1387953-tracks) property of an URL asset is typically empty for streaming-based media, while the array of [AVPlayerItemTrack](https://developer.apple.com/documentation/avfoundation/avplayeritemtrack) objects available via the [tracks](https://developer.apple.com/documentation/avfoundation/avplayeritem/1386361-tracks) property on the corresponding player item may have a different count and may change while it plays. If you need to, you can observe both the `duration` and `tracks` keys of `AVPlayerItem` to remain in sync with the current state of playback.

[AVPlayerItem](https://developer.apple.com/documentation/avfoundation/avplayeritem) has been enhanced to provide access and error information during HTTP Live Streaming playback. A network access log is available via [accessLog](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388499-accesslog). A log of error information is available via [errorLog](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387573-errorlog).

### Duration of Timed Media Resources for Playback

Because of the dynamic nature of HTTP Live Streaming Media our best practice for obtaining the duration of an [AVPlayerItem](https://developer.apple.com/documentation/avfoundation/avplayeritem) object has changed in iOS 4.3. Prior to iOS 4.3, you would obtain the duration of a player item by fetching the value of the duration property of its associated [AVAsset](https://developer.apple.com/documentation/avfoundation/avasset) object. As above, however, note that for HTTP Live Streaming Media the duration of a player item during any particular playback session may differ from the duration of its asset. For this reason a new key-value observable [duration](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389386-duration) property has been defined on `AVPlayerItem`.

To make your code compatible with all available revisions of AV Foundation, you can check whether the duration property of an `AVPlayerItem` instance is available and obtain the duration for playback as follows:

```
CMTime itemDuration = kCMTimeInvalid;

// Once the AVPlayerItem becomes ready to play, i.e. [playerItem status] == AVPlayerItemStatusReadyToPlay),
// its duration can be fetched from the item as follows.

if ([AVPlayerItem instancesRespondToSelector:@selector (duration)]) {

    // Fetch the duration directly from the AVPlayerItem.

    itemDuration = [playerItem duration];
}
else {
    // Reach through the AVPlayerItem to its asset to get the duration.
    itemDuration = [[playerItem asset] duration];
}
```


### Determining Whether an Item Has Played Successfully

[AVPlayerItem](https://developer.apple.com/documentation/avfoundation/avplayeritem) posts the notification [AVPlayerItemDidPlayToEndTimeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1386566-avplayeritemdidplaytoendtime) when it successfully reaches its end time during normal playback. Starting with iOS 4.3, `AVPlayerItem` will post the notification `AVPlayerItemFailedToPlayToEndTimeNotification` if playback is interrupted by an unrecoverable error. The [userInfo](https://developer.apple.com/documentation/foundation/nsnotification/1409222-userinfo) dictionary of the notification will contain an `NSError` object describing the problem, which can be obtained by using the key `AVPlayerItemFailedToPlayToEndTimeErrorKey`. For example, if the underlying timed media resource contains corrupted data associated with a particular playback time that prevents playback from proceeding beyond that time, `AVPlayerItem` will post `AVPlayerItemFailedToPlayToEndTimeNotification`.

### Access to Chapter Metadata

In iOS 4.3, [AVAsset](https://developer.apple.com/documentation/avfoundation/avasset) has been enhanced to provide metadata information associated with chapters, including chapter titles and chapter images. The class [AVTimedMetadataGroup](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup) has been defined to organize collections of metadata items by time range; each chapter of an asset will be represented by a corresponding instance of `AVTimedMetadataGroup`.

To load chapter information for an asset, request the value for the key [availableChapterLocales](https://developer.apple.com/documentation/avfoundation/avasset/1388228-availablechapterlocales) in a call to [loadValuesAsynchronouslyForKeys:completionHandler:](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/1387321-loadvaluesasynchronouslyforkeys). Once the value of `availableChapterLocales` has been successfully loaded, you can obtain the chapter information for any specific locale via [chapterMetadataGroupsWithTitleLocale:containingItemsWithCommonKeys:](https://developer.apple.com/documentation/avfoundation/avasset/1388966-chaptermetadatagroupswithtitlelo). If you wish to obtain chapter images along with chapter titles, include the metadata key [AVMetadataCommonKeyArtwork](https://developer.apple.com/documentation/avfoundation/avmetadatacommonkeyartwork) in the array of common keys that you specify. This method will return an array of instances of `AVTimedMetadataGroup`, one per chapter.

You can obtain the timeRange of a chapter via [timeRange](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/1387992-timerange). The metadata information associated with the chapter, typically including an item that has the common metadata key [AVMetadataCommonKeyTitle](https://developer.apple.com/documentation/avfoundation/avmetadatacommonkeytitle), is available via [items](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/1385928-items), which returns an array of instances of [AVMetadataItem](https://developer.apple.com/documentation/avfoundation/avmetadataitem).

Note that some metadata items included in an `AVTimedMetadataGroup` may not have a time and duration that correspond exactly with the timeRange of the group. This can occur, for example, with a QuickTime movie file that has a chapter image track with times that do not align precisely with the times of its chapter text track. So that all information for a group’s timeRange is accessible to you, all items that overlap in time with the timeRange of the group will be included in the group, and you can decide which item to use at any particular time according to the included items' times and durations.

Because of the way chapter information can be stored within timed media resources, additional I/O may be required to obtain the value of an `AVMetadataItem` included in an `AVTimedMetadataGroup`. To avoid potentially lengthy (and risky) blocking, you can load the values of `AVMetadataItem` objects asynchronously using the same [AVAsynchronousKeyValueLoading](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading) loading protocol already supported by `AVAsset` and `AVAssetTrack`. Call [loadValuesAsynchronouslyForKeys:completionHandler:](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/1387321-loadvaluesasynchronouslyforkeys)] and include the key `@"value"` in the specified array of keys to trigger the loading of a value.

### Attempting to Run an AVCaptureSession in the Background

AV Foundation does not support running an [AVCaptureSession](https://developer.apple.com/documentation/avfoundation/avcapturesession) in the background. Starting with iOS 4.3, if you attempt to run a capture session in the background, the session will post the notification [AVCaptureSessionRuntimeErrorNotification](https://developer.apple.com/documentation/avfoundation/avcapturesessionruntimeerrornotification) with a payload that contains an `NSError` object with the error [code](https://developer.apple.com/documentation/foundation/nserror/1409165-code) `AVErrorDeviceIsNotAvailableInBackground`.
