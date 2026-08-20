---
title: tvOS 9.2 API Diffs
apple_id: TP40016673
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS92APIDiffs/Swift/AVFoundation.html
archived_at: '2026-07-18T02:58:04.944766Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 9.2 API Diffs](tvOS%209.1%20to%209.2%20API%20Differences.md)


# AVFoundation Changes for Swift

### AVFoundation

Added [AVMetadataGroup.classifyingLabel](https://developer.apple.com/documentation/avfoundation/avmetadatagroup/1620087-classifyinglabel)Added [AVMetadataGroup.uniqueID](https://developer.apple.com/documentation/avfoundation/avmetadatagroup/1620088-uniqueid)Added [AVPlayerItem.addMediaDataCollector(_: AVPlayerItemMediaDataCollector)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1624164-addmediadatacollector)Added [AVPlayerItem.mediaDataCollectors](https://developer.apple.com/documentation/avfoundation/avplayeritem/1624161-mediadatacollectors)Added [AVPlayerItem.removeMediaDataCollector(_: AVPlayerItemMediaDataCollector)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1624163-remove)Added [AVPlayerItemMediaDataCollector](https://developer.apple.com/documentation/avfoundation/avplayeritemmediadatacollector)Added [AVPlayerItemMetadataCollector](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollector)Added [AVPlayerItemMetadataCollector.delegate](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollector/1617196-delegate)Added [AVPlayerItemMetadataCollector.delegateQueue](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollector/1617192-delegatequeue)Added [AVPlayerItemMetadataCollector.init(identifiers: [String]?, classifyingLabels: [String]?)](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollector/1617191-init)Added [AVPlayerItemMetadataCollector.setDelegate(_: AVPlayerItemMetadataCollectorPushDelegate?, queue: dispatch_queue_t?)](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollector/1617195-setdelegate)Added [AVPlayerItemMetadataCollectorPushDelegate](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollectorpushdelegate)Added [AVPlayerItemMetadataCollectorPushDelegate.metadataCollector(_: AVPlayerItemMetadataCollector, didCollectDateRangeMetadataGroups: [AVDateRangeMetadataGroup], indexesOfNewGroups: NSIndexSet, indexesOfModifiedGroups: NSIndexSet)](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollectorpushdelegate/1617190-metadatacollector)Added [AVMetadataKeySpaceHLSDateRange](https://developer.apple.com/documentation/avfoundation/avmetadatakeyspace/1625011-hlsdaterange)Modified [AVMetadataGroup](https://developer.apple.com/documentation/avfoundation/avmetadatagroup)

|  | Declaration |
| --- | --- |
| From | ``` class AVMetadataGroup : NSObject {     var items: [AVMetadataItem] { get } } ``` |
| To | ``` class AVMetadataGroup : NSObject {     var items: [AVMetadataItem] { get } } extension AVMetadataGroup {     var classifyingLabel: String? { get }     var uniqueID: String? { get } } ``` |

Modified [AVPlayerItem](https://developer.apple.com/documentation/avfoundation/avplayeritem)

|  | Declaration |
| --- | --- |
| From | ``` class AVPlayerItem : NSObject, NSCopying {     convenience init()      init(URL URL: NSURL)     class func playerItemWithURL(_ URL: NSURL) -> AVPlayerItem      init(asset asset: AVAsset)     class func playerItemWithAsset(_ asset: AVAsset) -> AVPlayerItem      init(asset asset: AVAsset, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [String]?)     class func playerItemWithAsset(_ asset: AVAsset, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [String]?) -> AVPlayerItem     convenience init(URL URL: NSURL)     convenience init(asset asset: AVAsset)     init(asset asset: AVAsset, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [String]?)     var status: AVPlayerItemStatus { get }     var error: NSError? { get } } extension AVPlayerItem {     var asset: AVAsset { get }     var tracks: [AVPlayerItemTrack] { get }     var duration: CMTime { get }     var presentationSize: CGSize { get }     var timedMetadata: [AVMetadataItem]? { get }     var automaticallyLoadedAssetKeys: [String] { get } } extension AVPlayerItem {     var canPlayFastForward: Bool { get }     var canPlaySlowForward: Bool { get }     var canPlayReverse: Bool { get }     var canPlaySlowReverse: Bool { get }     var canPlayFastReverse: Bool { get }     var canStepForward: Bool { get }     var canStepBackward: Bool { get } } extension AVPlayerItem {     func currentTime() -> CMTime     var forwardPlaybackEndTime: CMTime     var reversePlaybackEndTime: CMTime     var seekableTimeRanges: [NSValue] { get }     func seekToTime(_ time: CMTime)     func seekToTime(_ time: CMTime, completionHandler completionHandler: (Bool) -> Void)     func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime)     func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime, completionHandler completionHandler: (Bool) -> Void)     func cancelPendingSeeks()     func currentDate() -> NSDate?     func seekToDate(_ date: NSDate) -> Bool     func seekToDate(_ date: NSDate, completionHandler completionHandler: (Bool) -> Void) -> Bool     func stepByCount(_ stepCount: Int)     var timebase: CMTimebase? { get } } extension AVPlayerItem {     @NSCopying var videoComposition: AVVideoComposition?     var customVideoCompositor: AVVideoCompositing? { get }     var seekingWaitsForVideoCompositionRendering: Bool     var textStyleRules: [AVTextStyleRule]? } extension AVPlayerItem {     var audioTimePitchAlgorithm: String     @NSCopying var audioMix: AVAudioMix? } extension AVPlayerItem {     var loadedTimeRanges: [NSValue] { get }     var playbackLikelyToKeepUp: Bool { get }     var playbackBufferFull: Bool { get }     var playbackBufferEmpty: Bool { get }     var canUseNetworkResourcesForLiveStreamingWhilePaused: Bool } extension AVPlayerItem {     var preferredPeakBitRate: Double } extension AVPlayerItem {     func selectMediaOption(_ mediaSelectionOption: AVMediaSelectionOption?, inMediaSelectionGroup mediaSelectionGroup: AVMediaSelectionGroup)     func selectMediaOptionAutomaticallyInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup)     func selectedMediaOptionInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption?     var currentMediaSelection: AVMediaSelection { get } } extension AVPlayerItem {     func accessLog() -> AVPlayerItemAccessLog?     func errorLog() -> AVPlayerItemErrorLog? } extension AVPlayerItem {     func addOutput(_ output: AVPlayerItemOutput)     func removeOutput(_ output: AVPlayerItemOutput)     var outputs: [AVPlayerItemOutput] { get } } extension AVPlayerItem {     var navigationMarkerGroups: [AVNavigationMarkersGroup]     var externalMetadata: [AVMetadataItem]     var interstitialTimeRanges: [AVInterstitialTimeRange] } extension AVPlayerItem {     var externalSubtitleOptionLanguages: [String]     var selectedExternalSubtitleOptionLanguage: String } ``` |
| To | ``` class AVPlayerItem : NSObject, NSCopying {     convenience init()      init(URL URL: NSURL)     class func playerItemWithURL(_ URL: NSURL) -> AVPlayerItem      init(asset asset: AVAsset)     class func playerItemWithAsset(_ asset: AVAsset) -> AVPlayerItem      init(asset asset: AVAsset, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [String]?)     class func playerItemWithAsset(_ asset: AVAsset, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [String]?) -> AVPlayerItem     convenience init(URL URL: NSURL)     convenience init(asset asset: AVAsset)     init(asset asset: AVAsset, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [String]?)     var status: AVPlayerItemStatus { get }     var error: NSError? { get } } extension AVPlayerItem {     var asset: AVAsset { get }     var tracks: [AVPlayerItemTrack] { get }     var duration: CMTime { get }     var presentationSize: CGSize { get }     var timedMetadata: [AVMetadataItem]? { get }     var automaticallyLoadedAssetKeys: [String] { get } } extension AVPlayerItem {     var canPlayFastForward: Bool { get }     var canPlaySlowForward: Bool { get }     var canPlayReverse: Bool { get }     var canPlaySlowReverse: Bool { get }     var canPlayFastReverse: Bool { get }     var canStepForward: Bool { get }     var canStepBackward: Bool { get } } extension AVPlayerItem {     func currentTime() -> CMTime     var forwardPlaybackEndTime: CMTime     var reversePlaybackEndTime: CMTime     var seekableTimeRanges: [NSValue] { get }     func seekToTime(_ time: CMTime)     func seekToTime(_ time: CMTime, completionHandler completionHandler: (Bool) -> Void)     func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime)     func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime, completionHandler completionHandler: (Bool) -> Void)     func cancelPendingSeeks()     func currentDate() -> NSDate?     func seekToDate(_ date: NSDate) -> Bool     func seekToDate(_ date: NSDate, completionHandler completionHandler: (Bool) -> Void) -> Bool     func stepByCount(_ stepCount: Int)     var timebase: CMTimebase? { get } } extension AVPlayerItem {     @NSCopying var videoComposition: AVVideoComposition?     var customVideoCompositor: AVVideoCompositing? { get }     var seekingWaitsForVideoCompositionRendering: Bool     var textStyleRules: [AVTextStyleRule]? } extension AVPlayerItem {     var audioTimePitchAlgorithm: String     @NSCopying var audioMix: AVAudioMix? } extension AVPlayerItem {     var loadedTimeRanges: [NSValue] { get }     var playbackLikelyToKeepUp: Bool { get }     var playbackBufferFull: Bool { get }     var playbackBufferEmpty: Bool { get }     var canUseNetworkResourcesForLiveStreamingWhilePaused: Bool } extension AVPlayerItem {     var preferredPeakBitRate: Double } extension AVPlayerItem {     func selectMediaOption(_ mediaSelectionOption: AVMediaSelectionOption?, inMediaSelectionGroup mediaSelectionGroup: AVMediaSelectionGroup)     func selectMediaOptionAutomaticallyInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup)     func selectedMediaOptionInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption?     var currentMediaSelection: AVMediaSelection { get } } extension AVPlayerItem {     func accessLog() -> AVPlayerItemAccessLog?     func errorLog() -> AVPlayerItemErrorLog? } extension AVPlayerItem {     func addOutput(_ output: AVPlayerItemOutput)     func removeOutput(_ output: AVPlayerItemOutput)     var outputs: [AVPlayerItemOutput] { get } } extension AVPlayerItem {     func addMediaDataCollector(_ collector: AVPlayerItemMediaDataCollector)     func removeMediaDataCollector(_ collector: AVPlayerItemMediaDataCollector)     var mediaDataCollectors: [AVPlayerItemMediaDataCollector] { get } } extension AVPlayerItem {     var navigationMarkerGroups: [AVNavigationMarkersGroup]     var externalMetadata: [AVMetadataItem]     var interstitialTimeRanges: [AVInterstitialTimeRange] } extension AVPlayerItem {     var externalSubtitleOptionLanguages: [String]     var selectedExternalSubtitleOptionLanguage: String } ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
