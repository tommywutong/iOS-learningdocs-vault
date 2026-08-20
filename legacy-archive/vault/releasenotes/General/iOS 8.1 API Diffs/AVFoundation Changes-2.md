---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/AVFoundation.html
archived_at: '2026-07-18T02:56:03.435949Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# AVFoundation Changes

## AVFoundation

Removed AVAssetReader.assetReaderWithAsset(AVAsset!, error: NSErrorPointer) -> Self! [class]Removed AVAssetReferenceRestrictions.valueRemoved AVAssetWriter.assetWriterWithURL(NSURL!, fileType: String!, error: NSErrorPointer) -> Self! [class]Removed AVAudioChannelLayout.layoutWithLayout(UnsafePointer<AudioChannelLayout>) -> Self! [class]Removed AVAudioChannelLayout.layoutWithLayoutTag(AudioChannelLayoutTag) -> Self! [class]Removed AVAudioPlayerNodeBufferOptions.valueRemoved AVAudioSessionCategoryOptions.valueRemoved AVAudioSessionInterruptionOptions.valueRemoved AVAudioSessionRecordPermission.valueRemoved AVAudioSessionSetActiveOptions.valueRemoved AVAudioTime.timeWithAudioTimeStamp(UnsafePointer<AudioTimeStamp>, sampleRate: Double) -> Self! [class]Removed AVAudioTime.timeWithHostTime(UInt64) -> Self! [class]Removed AVAudioTime.timeWithHostTime(UInt64, sampleTime: AVAudioFramePosition, atRate: Double) -> Self! [class]Removed AVAudioTime.timeWithSampleTime(AVAudioFramePosition, atRate: Double) -> Self! [class]Removed AVURLAsset.URLAssetWithURL(NSURL!, options:[NSObject: AnyObject]!) -> AVURLAsset! [class]Added AVAssetReferenceRestrictions.init(rawValue: UInt)Added AVAudioPlayerNodeBufferOptions.init(rawValue: UInt)Added AVAudioSessionCategoryOptions.init(rawValue: UInt)Added AVAudioSessionInterruptionOptions.init(rawValue: UInt)Added AVAudioSessionRecordPermission.init(rawValue: UInt)Added AVAudioSessionSetActiveOptions.init(rawValue: UInt)Added NSCoder.decodeCMTimeForKey(String!) -> CMTimeAdded NSCoder.decodeCMTimeMappingForKey(String!) -> CMTimeMappingAdded NSCoder.decodeCMTimeRangeForKey(String!) -> CMTimeRangeAdded NSCoder.encodeCMTime(CMTime, forKey: String!)Added NSCoder.encodeCMTimeMapping(CMTimeMapping, forKey: String!)Added NSCoder.encodeCMTimeRange(CMTimeRange, forKey: String!)Added NSValue.init(CMTime: CMTime)Added NSValue.init(CMTimeMapping: CMTimeMapping)Added NSValue.CMTimeMappingValueAdded NSValue.init(CMTimeRange: CMTimeRange)Added NSValue.CMTimeRangeValueAdded NSValue.CMTimeValueAdded AVAudioSessionOrientationLeftAdded AVAudioSessionOrientationRightModified AVAsset

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAsset.availableChapterLocales

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVAsset.availableMediaCharacteristicsWithMediaSelectionOptions

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAsset.chapterMetadataGroupsBestMatchingPreferredLanguages([AnyObject]!) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAsset.chapterMetadataGroupsWithTitleLocale(NSLocale!, containingItemsWithCommonKeys:[AnyObject]!) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVAsset.compatibleWithSavedPhotosAlbum

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAsset.composable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVAsset.creationDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAsset.exportable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVAsset.hasProtectedContent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified AVAsset.mediaSelectionGroupForMediaCharacteristic(String!) -> AVMediaSelectionGroup!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAsset.playable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVAsset.readable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVAsset.referenceRestrictions

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAsset.trackGroups

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetExportSession

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAssetExportSession.asset

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAssetExportSession.init(asset: AVAsset!, presetName: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(asset asset: AVAsset!, presetName presetName: String!) ``` |
| To | ``` init!(asset asset: AVAsset!, presetName presetName: String!) ``` |

Modified AVAssetExportSession.audioTimePitchAlgorithm

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetExportSession.customVideoCompositor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetExportSession.determineCompatibilityOfExportPreset(String!, withAsset: AVAsset!, outputFileType: String!, completionHandler:((Bool) -> Void)!) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAssetExportSession.determineCompatibleFileTypesWithCompletionHandler((([AnyObject]!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAssetExportSession.estimatedOutputFileLength

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAssetExportSession.metadataItemFilter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetImageGenerator

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAssetImageGenerator.asset

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAssetImageGenerator.init(asset: AVAsset!)

|  | Declaration |
| --- | --- |
| From | ``` init(asset asset: AVAsset!) ``` |
| To | ``` init!(asset asset: AVAsset!) ``` |

Modified AVAssetImageGenerator.customVideoCompositor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetImageGenerator.requestedTimeToleranceAfter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAssetImageGenerator.requestedTimeToleranceBefore

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAssetReader

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified AVAssetReader.init(asset: AVAsset!, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(asset asset: AVAsset!, error outError: NSErrorPointer) ``` |
| To | ``` init!(asset asset: AVAsset!, error outError: NSErrorPointer) ``` |

Modified AVAssetReaderAudioMixOutput

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified AVAssetReaderAudioMixOutput.audioTimePitchAlgorithm

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetReaderAudioMixOutput.init(audioTracks: [AnyObject]!, audioSettings:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(audioTracks audioTracks: [AnyObject]!, audioSettings audioSettings: [NSObject : AnyObject]!) ``` |
| To | ``` init!(audioTracks audioTracks: [AnyObject]!, audioSettings audioSettings: [NSObject : AnyObject]!) ``` |

Modified AVAssetReaderOutput

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified AVAssetReaderOutput.alwaysCopiesSampleData

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAssetReaderOutputMetadataAdaptor.init(assetReaderTrackOutput: AVAssetReaderTrackOutput!)

|  | Declaration |
| --- | --- |
| From | ``` init(assetReaderTrackOutput trackOutput: AVAssetReaderTrackOutput!) ``` |
| To | ``` init!(assetReaderTrackOutput trackOutput: AVAssetReaderTrackOutput!) ``` |

Modified AVAssetReaderSampleReferenceOutput.init(track: AVAssetTrack!)

|  | Declaration |
| --- | --- |
| From | ``` init(track track: AVAssetTrack!) ``` |
| To | ``` init!(track track: AVAssetTrack!) ``` |

Modified AVAssetReaderTrackOutput

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified AVAssetReaderTrackOutput.audioTimePitchAlgorithm

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetReaderTrackOutput.init(track: AVAssetTrack!, outputSettings:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(track track: AVAssetTrack!, outputSettings outputSettings: [NSObject : AnyObject]!) ``` |
| To | ``` init!(track track: AVAssetTrack!, outputSettings outputSettings: [NSObject : AnyObject]!) ``` |

Modified AVAssetReaderVideoCompositionOutput

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified AVAssetReaderVideoCompositionOutput.customVideoCompositor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetReaderVideoCompositionOutput.init(videoTracks: [AnyObject]!, videoSettings:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(videoTracks videoTracks: [AnyObject]!, videoSettings videoSettings: [NSObject : AnyObject]!) ``` |
| To | ``` init!(videoTracks videoTracks: [AnyObject]!, videoSettings videoSettings: [NSObject : AnyObject]!) ``` |

Modified AVAssetReferenceRestrictions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AVAssetReferenceRestrictions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var RestrictionForbidNone: AVAssetReferenceRestrictions { get }     static var RestrictionForbidRemoteReferenceToLocal: AVAssetReferenceRestrictions { get }     static var RestrictionForbidLocalReferenceToRemote: AVAssetReferenceRestrictions { get }     static var RestrictionForbidCrossSiteReference: AVAssetReferenceRestrictions { get }     static var RestrictionForbidLocalReferenceToLocal: AVAssetReferenceRestrictions { get }     static var RestrictionForbidAll: AVAssetReferenceRestrictions { get } } ``` |
| To | ``` struct AVAssetReferenceRestrictions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var RestrictionForbidNone: AVAssetReferenceRestrictions { get }     static var RestrictionForbidRemoteReferenceToLocal: AVAssetReferenceRestrictions { get }     static var RestrictionForbidLocalReferenceToRemote: AVAssetReferenceRestrictions { get }     static var RestrictionForbidCrossSiteReference: AVAssetReferenceRestrictions { get }     static var RestrictionForbidLocalReferenceToLocal: AVAssetReferenceRestrictions { get }     static var RestrictionForbidAll: AVAssetReferenceRestrictions { get } } ``` |

Modified AVAssetReferenceRestrictions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified AVAssetResourceLoader

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAssetResourceLoaderDelegate.resourceLoader(AVAssetResourceLoader!, didCancelLoadingRequest: AVAssetResourceLoadingRequest!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetResourceLoaderDelegate.resourceLoader(AVAssetResourceLoader!, shouldWaitForLoadingOfRequestedResource: AVAssetResourceLoadingRequest!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAssetResourceLoadingContentInformationRequest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetResourceLoadingDataRequest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetResourceLoadingRequest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAssetResourceLoadingRequest.cancelled

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetResourceLoadingRequest.contentInformationRequest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetResourceLoadingRequest.dataRequest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetResourceLoadingRequest.finishLoading()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetResourceLoadingRequest.redirect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetResourceLoadingRequest.response

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetTrack

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAssetTrack.associatedTracksOfType(String!) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetTrack.availableTrackAssociationTypes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetTrack.minFrameDuration

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetTrack.playable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAssetTrackGroup

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetTrackSegment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAssetWriter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified AVAssetWriter.init(URL: NSURL!, fileType: String!, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(URL outputURL: NSURL!, fileType outputFileType: String!, error outError: NSErrorPointer) ``` |
| To | ``` init!(URL outputURL: NSURL!, fileType outputFileType: String!, error outError: NSErrorPointer) ``` |

Modified AVAssetWriter.addInputGroup(AVAssetWriterInputGroup!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetWriter.canAddInputGroup(AVAssetWriterInputGroup!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetWriter.finishWritingWithCompletionHandler((() -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAssetWriter.inputGroups

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetWriter.movieTimeScale

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVAssetWriterInput

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified AVAssetWriterInput.addTrackAssociationWithTrackOfInput(AVAssetWriterInput!, type: String!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetWriterInput.canAddTrackAssociationWithTrackOfInput(AVAssetWriterInput!, type: String!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetWriterInput.extendedLanguageTag

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetWriterInput.languageCode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetWriterInput.marksOutputTrackAsEnabled

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetWriterInput.mediaTimeScale

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVAssetWriterInput.init(mediaType: String!, outputSettings:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(mediaType mediaType: String!, outputSettings outputSettings: [NSObject : AnyObject]!) ``` |
| To | ``` init!(mediaType mediaType: String!, outputSettings outputSettings: [NSObject : AnyObject]!) ``` |

Modified AVAssetWriterInput.init(mediaType: String!, outputSettings:[NSObject: AnyObject]!, sourceFormatHint: CMFormatDescription!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(mediaType mediaType: String!, outputSettings outputSettings: [NSObject : AnyObject]!, sourceFormatHint sourceFormatHint: CMFormatDescription!) ``` | iOS 8.0 |
| To | ``` init!(mediaType mediaType: String!, outputSettings outputSettings: [NSObject : AnyObject]!, sourceFormatHint sourceFormatHint: CMFormatDescription!) ``` | iOS 6.0 |

Modified AVAssetWriterInput.naturalSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetWriterInput.preferredVolume

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetWriterInput.sourceFormatHint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAssetWriterInputGroup

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAssetWriterInputGroup.init(inputs: [AnyObject]!, defaultInput: AVAssetWriterInput!)

|  | Declaration |
| --- | --- |
| From | ``` init(inputs inputs: [AnyObject]!, defaultInput defaultInput: AVAssetWriterInput!) ``` |
| To | ``` init!(inputs inputs: [AnyObject]!, defaultInput defaultInput: AVAssetWriterInput!) ``` |

Modified AVAssetWriterInputMetadataAdaptor.init(assetWriterInput: AVAssetWriterInput!)

|  | Declaration |
| --- | --- |
| From | ``` init(assetWriterInput input: AVAssetWriterInput!) ``` |
| To | ``` init!(assetWriterInput input: AVAssetWriterInput!) ``` |

Modified AVAssetWriterInputPixelBufferAdaptor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified AVAssetWriterInputPixelBufferAdaptor.init(assetWriterInput: AVAssetWriterInput!, sourcePixelBufferAttributes:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(assetWriterInput input: AVAssetWriterInput!, sourcePixelBufferAttributes sourcePixelBufferAttributes: [NSObject : AnyObject]!) ``` |
| To | ``` init!(assetWriterInput input: AVAssetWriterInput!, sourcePixelBufferAttributes sourcePixelBufferAttributes: [NSObject : AnyObject]!) ``` |

Modified AVAsynchronousVideoCompositionRequest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioChannelLayout.init(layout: UnsafePointer<AudioChannelLayout>)

|  | Declaration |
| --- | --- |
| From | ``` init(layout layout: UnsafePointer<AudioChannelLayout>) ``` |
| To | ``` init!(layout layout: UnsafePointer<AudioChannelLayout>) ``` |

Modified AVAudioChannelLayout.init(layoutTag: AudioChannelLayoutTag)

|  | Declaration |
| --- | --- |
| From | ``` init(layoutTag layoutTag: AudioChannelLayoutTag) ``` |
| To | ``` init!(layoutTag layoutTag: AudioChannelLayoutTag) ``` |

Modified AVAudioEngine.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified AVAudioFile.init(forReading: NSURL!, commonFormat: AVAudioCommonFormat, interleaved: Bool, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(forReading fileURL: NSURL!, commonFormat format: AVAudioCommonFormat, interleaved interleaved: Bool, error outError: NSErrorPointer) ``` |
| To | ``` init!(forReading fileURL: NSURL!, commonFormat format: AVAudioCommonFormat, interleaved interleaved: Bool, error outError: NSErrorPointer) ``` |

Modified AVAudioFile.init(forReading: NSURL!, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(forReading fileURL: NSURL!, error outError: NSErrorPointer) ``` |
| To | ``` init!(forReading fileURL: NSURL!, error outError: NSErrorPointer) ``` |

Modified AVAudioFile.init(forWriting: NSURL!, settings:[NSObject: AnyObject]!, commonFormat: AVAudioCommonFormat, interleaved: Bool, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(forWriting fileURL: NSURL!, settings settings: [NSObject : AnyObject]!, commonFormat format: AVAudioCommonFormat, interleaved interleaved: Bool, error outError: NSErrorPointer) ``` |
| To | ``` init!(forWriting fileURL: NSURL!, settings settings: [NSObject : AnyObject]!, commonFormat format: AVAudioCommonFormat, interleaved interleaved: Bool, error outError: NSErrorPointer) ``` |

Modified AVAudioFile.init(forWriting: NSURL!, settings:[NSObject: AnyObject]!, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(forWriting fileURL: NSURL!, settings settings: [NSObject : AnyObject]!, error outError: NSErrorPointer) ``` |
| To | ``` init!(forWriting fileURL: NSURL!, settings settings: [NSObject : AnyObject]!, error outError: NSErrorPointer) ``` |

Modified AVAudioFormat.init(commonFormat: AVAudioCommonFormat, sampleRate: Double, channels: AVAudioChannelCount, interleaved: Bool)

|  | Declaration |
| --- | --- |
| From | ``` init(commonFormat format: AVAudioCommonFormat, sampleRate sampleRate: Double, channels channels: AVAudioChannelCount, interleaved interleaved: Bool) ``` |
| To | ``` init!(commonFormat format: AVAudioCommonFormat, sampleRate sampleRate: Double, channels channels: AVAudioChannelCount, interleaved interleaved: Bool) ``` |

Modified AVAudioFormat.init(commonFormat: AVAudioCommonFormat, sampleRate: Double, interleaved: Bool, channelLayout: AVAudioChannelLayout!)

|  | Declaration |
| --- | --- |
| From | ``` init(commonFormat format: AVAudioCommonFormat, sampleRate sampleRate: Double, interleaved interleaved: Bool, channelLayout layout: AVAudioChannelLayout!) ``` |
| To | ``` init!(commonFormat format: AVAudioCommonFormat, sampleRate sampleRate: Double, interleaved interleaved: Bool, channelLayout layout: AVAudioChannelLayout!) ``` |

Modified AVAudioFormat.init(settings: [NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(settings settings: [NSObject : AnyObject]!) ``` |
| To | ``` init!(settings settings: [NSObject : AnyObject]!) ``` |

Modified AVAudioFormat.init(standardFormatWithSampleRate: Double, channelLayout: AVAudioChannelLayout!)

|  | Declaration |
| --- | --- |
| From | ``` init(standardFormatWithSampleRate sampleRate: Double, channelLayout layout: AVAudioChannelLayout!) ``` |
| To | ``` init!(standardFormatWithSampleRate sampleRate: Double, channelLayout layout: AVAudioChannelLayout!) ``` |

Modified AVAudioFormat.init(standardFormatWithSampleRate: Double, channels: AVAudioChannelCount)

|  | Declaration |
| --- | --- |
| From | ``` init(standardFormatWithSampleRate sampleRate: Double, channels channels: AVAudioChannelCount) ``` |
| To | ``` init!(standardFormatWithSampleRate sampleRate: Double, channels channels: AVAudioChannelCount) ``` |

Modified AVAudioFormat.init(streamDescription: UnsafePointer<AudioStreamBasicDescription>)

|  | Declaration |
| --- | --- |
| From | ``` init(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>) ``` |
| To | ``` init!(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>) ``` |

Modified AVAudioFormat.init(streamDescription: UnsafePointer<AudioStreamBasicDescription>, channelLayout: AVAudioChannelLayout!)

|  | Declaration |
| --- | --- |
| From | ``` init(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>, channelLayout layout: AVAudioChannelLayout!) ``` |
| To | ``` init!(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>, channelLayout layout: AVAudioChannelLayout!) ``` |

Modified AVAudioMix

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAudioMixInputParameters

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAudioMixInputParameters.audioTapProcessor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioMixInputParameters.audioTimePitchAlgorithm

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioPCMBuffer.init(PCMFormat: AVAudioFormat!, frameCapacity: AVAudioFrameCount)

|  | Declaration |
| --- | --- |
| From | ``` init(PCMFormat format: AVAudioFormat!, frameCapacity frameCapacity: AVAudioFrameCount) ``` |
| To | ``` init!(PCMFormat format: AVAudioFormat!, frameCapacity frameCapacity: AVAudioFrameCount) ``` |

Modified AVAudioPlayer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.2 |

Modified AVAudioPlayer.channelAssignments

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioPlayer.init(contentsOfURL: NSURL!, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfURL url: NSURL!, error outError: NSErrorPointer) ``` |
| To | ``` init!(contentsOfURL url: NSURL!, error outError: NSErrorPointer) ``` |

Modified AVAudioPlayer.init(contentsOfURL: NSURL!, fileTypeHint: String!, error: NSErrorPointer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(contentsOfURL url: NSURL!, fileTypeHint utiString: String!, error outError: NSErrorPointer) ``` | iOS 8.0 |
| To | ``` init!(contentsOfURL url: NSURL!, fileTypeHint utiString: String!, error outError: NSErrorPointer) ``` | iOS 7.0 |

Modified AVAudioPlayer.init(data: NSData!, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData!, error outError: NSErrorPointer) ``` |
| To | ``` init!(data data: NSData!, error outError: NSErrorPointer) ``` |

Modified AVAudioPlayer.init(data: NSData!, fileTypeHint: String!, error: NSErrorPointer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(data data: NSData!, fileTypeHint utiString: String!, error outError: NSErrorPointer) ``` | iOS 8.0 |
| To | ``` init!(data data: NSData!, fileTypeHint utiString: String!, error outError: NSErrorPointer) ``` | iOS 7.0 |

Modified AVAudioPlayer.deviceCurrentTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAudioPlayer.enableRate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAudioPlayer.pan

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAudioPlayer.playAtTime(NSTimeInterval) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAudioPlayer.rate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAudioPlayer.settings

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAudioPlayerDelegate.audioPlayerBeginInterruption(AVAudioPlayer!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.2 | iOS 8.0 |

Modified AVAudioPlayerDelegate.audioPlayerEndInterruption(AVAudioPlayer!, withOptions: Int)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 6.0 | iOS 8.0 |

Modified AVAudioPlayerNodeBufferOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AVAudioPlayerNodeBufferOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Loops: AVAudioPlayerNodeBufferOptions { get }     static var Interrupts: AVAudioPlayerNodeBufferOptions { get }     static var InterruptsAtLoop: AVAudioPlayerNodeBufferOptions { get } } ``` |
| To | ``` struct AVAudioPlayerNodeBufferOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Loops: AVAudioPlayerNodeBufferOptions { get }     static var Interrupts: AVAudioPlayerNodeBufferOptions { get }     static var InterruptsAtLoop: AVAudioPlayerNodeBufferOptions { get } } ``` |

Modified AVAudioPlayerNodeBufferOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified AVAudioRecorder

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified AVAudioRecorder.init(URL: NSURL!, settings:[NSObject: AnyObject]!, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(URL url: NSURL!, settings settings: [NSObject : AnyObject]!, error outError: NSErrorPointer) ``` |
| To | ``` init!(URL url: NSURL!, settings settings: [NSObject : AnyObject]!, error outError: NSErrorPointer) ``` |

Modified AVAudioRecorder.channelAssignments

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioRecorder.deviceCurrentTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioRecorder.recordAtTime(NSTimeInterval) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioRecorder.recordAtTime(NSTimeInterval, forDuration: NSTimeInterval) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioRecorderDelegate.audioRecorderBeginInterruption(AVAudioRecorder!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.2 | iOS 8.0 |

Modified AVAudioRecorderDelegate.audioRecorderEndInterruption(AVAudioRecorder!, withOptions: Int)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 6.0 | iOS 8.0 |

Modified AVAudioSession

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified AVAudioSession.IOBufferDuration

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.availableInputs

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSession.categoryOptions

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.currentRoute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.inputAvailable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.inputDataSource

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.inputDataSources

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.inputGain

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.inputGainSettable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.inputLatency

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.inputNumberOfChannels

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.maximumInputNumberOfChannels

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSession.maximumOutputNumberOfChannels

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSession.mode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAudioSession.otherAudioPlaying

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.outputDataSource

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.outputDataSources

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.outputLatency

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.outputNumberOfChannels

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.outputVolume

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.overrideOutputAudioPort(AVAudioSessionPortOverride, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.preferredInput

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSession.preferredInputNumberOfChannels

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSession.preferredOutputNumberOfChannels

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSession.preferredSampleRate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.requestRecordPermission(PermissionBlock!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSession.sampleRate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.setActive(Bool, withOptions: AVAudioSessionSetActiveOptions, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.setCategory(String!, withOptions: AVAudioSessionCategoryOptions, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.setInputDataSource(AVAudioSessionDataSourceDescription!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.setInputGain(Float, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.setMode(String!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAudioSession.setOutputDataSource(AVAudioSessionDataSourceDescription!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSession.setPreferredInput(AVAudioSessionPortDescription!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSession.setPreferredInputNumberOfChannels(Int, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSession.setPreferredOutputNumberOfChannels(Int, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSession.setPreferredSampleRate(Double, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionCategoryOptions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct AVAudioSessionCategoryOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var MixWithOthers: AVAudioSessionCategoryOptions { get }     static var DuckOthers: AVAudioSessionCategoryOptions { get }     static var AllowBluetooth: AVAudioSessionCategoryOptions { get }     static var DefaultToSpeaker: AVAudioSessionCategoryOptions { get } } ``` | iOS 8.0 |
| To | ``` struct AVAudioSessionCategoryOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var MixWithOthers: AVAudioSessionCategoryOptions { get }     static var DuckOthers: AVAudioSessionCategoryOptions { get }     static var AllowBluetooth: AVAudioSessionCategoryOptions { get }     static var DefaultToSpeaker: AVAudioSessionCategoryOptions { get } } ``` | iOS 6.0 |

Modified AVAudioSessionCategoryOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified AVAudioSessionChannelDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionDataSourceDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionDataSourceDescription.location

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionDataSourceDescription.orientation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionDataSourceDescription.preferredPolarPattern

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionDataSourceDescription.selectedPolarPattern

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionDataSourceDescription.setPreferredPolarPattern(String!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionDataSourceDescription.supportedPolarPatterns

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionDelegate.endInterruptionWithFlags(Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAudioSessionErrorCode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionInterruptionOptions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct AVAudioSessionInterruptionOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var OptionShouldResume: AVAudioSessionInterruptionOptions { get } } ``` | iOS 8.0 |
| To | ``` struct AVAudioSessionInterruptionOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var OptionShouldResume: AVAudioSessionInterruptionOptions { get } } ``` | iOS 6.0 |

Modified AVAudioSessionInterruptionOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified AVAudioSessionInterruptionType [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionPortDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionPortDescription.dataSources

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionPortDescription.preferredDataSource

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionPortDescription.selectedDataSource

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionPortDescription.setPreferredDataSource(AVAudioSessionDataSourceDescription!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionPortOverride [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionRecordPermission [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AVAudioSessionRecordPermission : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Undetermined: AVAudioSessionRecordPermission { get }     static var Denied: AVAudioSessionRecordPermission { get }     static var Granted: AVAudioSessionRecordPermission { get } } ``` |
| To | ``` struct AVAudioSessionRecordPermission : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Undetermined: AVAudioSessionRecordPermission { get }     static var Denied: AVAudioSessionRecordPermission { get }     static var Granted: AVAudioSessionRecordPermission { get } } ``` |

Modified AVAudioSessionRecordPermission.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified AVAudioSessionRouteChangeReason [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionRouteDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionSetActiveOptions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct AVAudioSessionSetActiveOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var OptionNotifyOthersOnDeactivation: AVAudioSessionSetActiveOptions { get } } ``` | iOS 8.0 |
| To | ``` struct AVAudioSessionSetActiveOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var OptionNotifyOthersOnDeactivation: AVAudioSessionSetActiveOptions { get } } ``` | iOS 6.0 |

Modified AVAudioSessionSetActiveOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified AVAudioTime.init(audioTimeStamp: UnsafePointer<AudioTimeStamp>, sampleRate: Double)

|  | Declaration |
| --- | --- |
| From | ``` init(audioTimeStamp ts: UnsafePointer<AudioTimeStamp>, sampleRate sampleRate: Double) ``` |
| To | ``` init!(audioTimeStamp ts: UnsafePointer<AudioTimeStamp>, sampleRate sampleRate: Double) ``` |

Modified AVAudioTime.init(hostTime: UInt64)

|  | Declaration |
| --- | --- |
| From | ``` init(hostTime hostTime: UInt64) ``` |
| To | ``` init!(hostTime hostTime: UInt64) ``` |

Modified AVAudioTime.init(hostTime: UInt64, sampleTime: AVAudioFramePosition, atRate: Double)

|  | Declaration |
| --- | --- |
| From | ``` init(hostTime hostTime: UInt64, sampleTime sampleTime: AVAudioFramePosition, atRate sampleRate: Double) ``` |
| To | ``` init!(hostTime hostTime: UInt64, sampleTime sampleTime: AVAudioFramePosition, atRate sampleRate: Double) ``` |

Modified AVAudioTime.init(sampleTime: AVAudioFramePosition, atRate: Double)

|  | Declaration |
| --- | --- |
| From | ``` init(sampleTime sampleTime: AVAudioFramePosition, atRate sampleRate: Double) ``` |
| To | ``` init!(sampleTime sampleTime: AVAudioFramePosition, atRate sampleRate: Double) ``` |

Modified AVAudioUnitEQ.init(numberOfBands: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(numberOfBands numberOfBands: Int) ``` |
| To | ``` init!(numberOfBands numberOfBands: Int) ``` |

Modified AVAudioUnitEffect.init(audioComponentDescription: AudioComponentDescription)

|  | Declaration |
| --- | --- |
| From | ``` init(audioComponentDescription audioComponentDescription: AudioComponentDescription) ``` |
| To | ``` init!(audioComponentDescription audioComponentDescription: AudioComponentDescription) ``` |

Modified AVAudioUnitGenerator.init(audioComponentDescription: AudioComponentDescription)

|  | Declaration |
| --- | --- |
| From | ``` init(audioComponentDescription audioComponentDescription: AudioComponentDescription) ``` |
| To | ``` init!(audioComponentDescription audioComponentDescription: AudioComponentDescription) ``` |

Modified AVAudioUnitMIDIInstrument.init(audioComponentDescription: AudioComponentDescription)

|  | Declaration |
| --- | --- |
| From | ``` init(audioComponentDescription description: AudioComponentDescription) ``` |
| To | ``` init!(audioComponentDescription description: AudioComponentDescription) ``` |

Modified AVAudioUnitTimeEffect.init(audioComponentDescription: AudioComponentDescription)

|  | Declaration |
| --- | --- |
| From | ``` init(audioComponentDescription audioComponentDescription: AudioComponentDescription) ``` |
| To | ``` init!(audioComponentDescription audioComponentDescription: AudioComponentDescription) ``` |

Modified AVAuthorizationStatus [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureAudioChannel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureAudioDataOutput

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureAudioDataOutput.recommendedAudioSettingsForAssetWriterWithOutputFileType(String!) -> [NSObject: AnyObject]!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureAutoFocusRangeRestriction [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureConnection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureConnection.automaticallyAdjustsVideoMirroring

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVCaptureConnection.enablesVideoStabilizationWhenAvailable

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 6.0 | iOS 8.0 |

Modified AVCaptureConnection.init(inputPort: AVCaptureInputPort!, videoPreviewLayer: AVCaptureVideoPreviewLayer!)

|  | Declaration |
| --- | --- |
| From | ``` init(inputPort port: AVCaptureInputPort!, videoPreviewLayer layer: AVCaptureVideoPreviewLayer!) ``` |
| To | ``` init!(inputPort port: AVCaptureInputPort!, videoPreviewLayer layer: AVCaptureVideoPreviewLayer!) ``` |

Modified AVCaptureConnection.init(inputPorts: [AnyObject]!, output: AVCaptureOutput!)

|  | Declaration |
| --- | --- |
| From | ``` init(inputPorts ports: [AnyObject]!, output output: AVCaptureOutput!) ``` |
| To | ``` init!(inputPorts ports: [AnyObject]!, output output: AVCaptureOutput!) ``` |

Modified AVCaptureConnection.supportsVideoStabilization

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVCaptureConnection.videoMaxScaleAndCropFactor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVCaptureConnection.videoPreviewLayer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVCaptureConnection.videoScaleAndCropFactor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVCaptureConnection.videoStabilizationEnabled

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 6.0 | iOS 8.0 |

Modified AVCaptureDevice

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureDevice.activeFormat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureDevice.activeVideoMaxFrameDuration

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureDevice.activeVideoMinFrameDuration

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureDevice.authorizationStatusForMediaType(String!) -> AVAuthorizationStatus [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureDevice.autoFocusRangeRestriction

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureDevice.autoFocusRangeRestrictionSupported

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureDevice.automaticallyEnablesLowLightBoostWhenAvailable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVCaptureDevice.cancelVideoZoomRamp()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureDevice.flashActive

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVCaptureDevice.flashAvailable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVCaptureDevice.formats

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureDevice.lowLightBoostEnabled

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVCaptureDevice.lowLightBoostSupported

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVCaptureDevice.rampToVideoZoomFactor(CGFloat, withRate: Float)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureDevice.rampingVideoZoom

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureDevice.requestAccessForMediaType(String!, completionHandler:((Bool) -> Void)!) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureDevice.setTorchModeOnWithLevel(Float, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVCaptureDevice.smoothAutoFocusEnabled

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureDevice.smoothAutoFocusSupported

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureDevice.subjectAreaChangeMonitoringEnabled

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVCaptureDevice.torchActive

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVCaptureDevice.torchAvailable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVCaptureDevice.torchLevel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVCaptureDevice.init(uniqueID: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(uniqueID deviceUniqueID: String!) -> AVCaptureDevice ``` |
| To | ``` init!(uniqueID deviceUniqueID: String!) -> AVCaptureDevice ``` |

Modified AVCaptureDevice.videoZoomFactor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureDeviceFormat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureDeviceFormat.videoBinned

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureDeviceFormat.videoFieldOfView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureDeviceFormat.videoMaxZoomFactor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureDeviceFormat.videoStabilizationSupported

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 8.0 |

Modified AVCaptureDeviceFormat.videoZoomFactorUpscaleThreshold

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureDeviceInput

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureDeviceInput.init(device: AVCaptureDevice!, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(device device: AVCaptureDevice!, error outError: NSErrorPointer) ``` |
| To | ``` init!(device device: AVCaptureDevice!, error outError: NSErrorPointer) ``` |

Modified AVCaptureDevicePosition [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureExposureMode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureFileOutput

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureFlashMode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureFocusMode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureInput

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureInputPort

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureInputPort.clock

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureMetadataOutput

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVCaptureMetadataOutput.rectOfInterest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureMovieFileOutput

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureOutput

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureOutput.connectionWithMediaType(String!) -> AVCaptureConnection!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVCaptureOutput.metadataOutputRectOfInterestForRect(CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureOutput.rectForMetadataOutputRectOfInterest(CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureOutput.transformedMetadataObjectForMetadataObject(AVMetadataObject!, connection: AVCaptureConnection!) -> AVMetadataObject!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVCaptureSession

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureSession.automaticallyConfiguresApplicationAudioSession

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureSession.interrupted

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureSession.masterClock

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureSession.usesApplicationAudioSession

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureStillImageOutput

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureStillImageOutput.automaticallyEnablesStillImageStabilizationWhenAvailable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureStillImageOutput.capturingStillImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVCaptureStillImageOutput.stillImageStabilizationActive

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureStillImageOutput.stillImageStabilizationSupported

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureTorchMode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureVideoDataOutput

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureVideoDataOutput.availableVideoCVPixelFormatTypes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVCaptureVideoDataOutput.availableVideoCodecTypes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVCaptureVideoDataOutput.recommendedVideoSettingsForAssetWriterWithOutputFileType(String!) -> [NSObject: AnyObject]!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureVideoDataOutputSampleBufferDelegate.captureOutput(AVCaptureOutput!, didDropSampleBuffer: CMSampleBuffer!, fromConnection: AVCaptureConnection!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVCaptureVideoOrientation [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureVideoPreviewLayer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureVideoPreviewLayer.captureDevicePointOfInterestForPoint(CGPoint) -> CGPoint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVCaptureVideoPreviewLayer.connection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVCaptureVideoPreviewLayer.metadataOutputRectOfInterestForRect(CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureVideoPreviewLayer.pointForCaptureDevicePointOfInterest(CGPoint) -> CGPoint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVCaptureVideoPreviewLayer.rectForMetadataOutputRectOfInterest(CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureVideoPreviewLayer.init(session: AVCaptureSession!)

|  | Declaration |
| --- | --- |
| From | ``` init(session session: AVCaptureSession!) ``` |
| To | ``` init!(session session: AVCaptureSession!) ``` |

Modified AVCaptureVideoPreviewLayer.init(sessionWithNoConnection: AVCaptureSession!)

|  | Declaration |
| --- | --- |
| From | ``` init(sessionWithNoConnection session: AVCaptureSession!) ``` |
| To | ``` init!(sessionWithNoConnection session: AVCaptureSession!) ``` |

Modified AVCaptureVideoPreviewLayer.transformedMetadataObjectForMetadataObject(AVMetadataObject!) -> AVMetadataObject!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVCaptureWhiteBalanceMode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVComposition

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCompositionTrack

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCompositionTrackSegment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCompositionTrackSegment.init(URL: NSURL!, trackID: CMPersistentTrackID, sourceTimeRange: CMTimeRange, targetTimeRange: CMTimeRange)

|  | Declaration |
| --- | --- |
| From | ``` init(URL URL: NSURL!, trackID trackID: CMPersistentTrackID, sourceTimeRange sourceTimeRange: CMTimeRange, targetTimeRange targetTimeRange: CMTimeRange) ``` |
| To | ``` init!(URL URL: NSURL!, trackID trackID: CMPersistentTrackID, sourceTimeRange sourceTimeRange: CMTimeRange, targetTimeRange targetTimeRange: CMTimeRange) ``` |

Modified AVCompositionTrackSegment.init(timeRange: CMTimeRange)

|  | Declaration |
| --- | --- |
| From | ``` init(timeRange timeRange: CMTimeRange) ``` |
| To | ``` init!(timeRange timeRange: CMTimeRange) ``` |

Modified AVFrameRateRange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMIDIPlayer.init(contentsOfURL: NSURL!, soundBankURL: NSURL!, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfURL inURL: NSURL!, soundBankURL bankURL: NSURL!, error outError: NSErrorPointer) ``` |
| To | ``` init!(contentsOfURL inURL: NSURL!, soundBankURL bankURL: NSURL!, error outError: NSErrorPointer) ``` |

Modified AVMIDIPlayer.init(data: NSData!, soundBankURL: NSURL!, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData!, soundBankURL bankURL: NSURL!, error outError: NSErrorPointer) ``` |
| To | ``` init!(data data: NSData!, soundBankURL bankURL: NSURL!, error outError: NSErrorPointer) ``` |

Modified AVMediaSelectionGroup

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVMediaSelectionGroup.mediaSelectionOptionsFromArray([AnyObject]!, filteredAndSortedAccordingToPreferredLanguages:[AnyObject]!) -> [AnyObject]! [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVMediaSelectionOption

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVMediaSelectionOption.displayName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMediaSelectionOption.displayNameWithLocale(NSLocale!) -> String!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMediaSelectionOption.extendedLanguageTag

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadataFaceObject

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVMetadataItem

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataItem.duration

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified AVMetadataItem.loadValuesAsynchronouslyForKeys([AnyObject]!, completionHandler:(() -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified AVMetadataItem.metadataItemsFromArray([AnyObject]!, filteredAndSortedAccordingToPreferredLanguages:[AnyObject]!) -> [AnyObject]! [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVMetadataItem.metadataItemsFromArray([AnyObject]!, filteredByMetadataItemFilter: AVMetadataItemFilter!) -> [AnyObject]! [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadataItem.statusOfValueForKey(String!, error: NSErrorPointer) -> AVKeyValueStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified AVMetadataItemFilter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadataMachineReadableCodeObject

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadataObject

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVMutableAudioMix

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMutableAudioMixInputParameters

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMutableAudioMixInputParameters.audioTapProcessor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVMutableAudioMixInputParameters.audioTimePitchAlgorithm

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMutableAudioMixInputParameters.init(track: AVAssetTrack!)

|  | Declaration |
| --- | --- |
| From | ``` init(track track: AVAssetTrack!) -> AVMutableAudioMixInputParameters ``` |
| To | ``` init!(track track: AVAssetTrack!) -> AVMutableAudioMixInputParameters ``` |

Modified AVMutableComposition

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMutableCompositionTrack

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMutableCompositionTrack.insertTimeRanges([AnyObject]!, ofTracks:[AnyObject]!, atTime: CMTime, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVMutableMetadataItem

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMutableMetadataItem.duration

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified AVMutableTimedMetadataGroup

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVMutableVideoComposition

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMutableVideoComposition.customVideoCompositorClass

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMutableVideoComposition.init(propertiesOfAsset: AVAsset!)

|  | Declaration |
| --- | --- |
| From | ``` init(propertiesOfAsset asset: AVAsset!) -> AVMutableVideoComposition ``` |
| To | ``` init!(propertiesOfAsset asset: AVAsset!) -> AVMutableVideoComposition ``` |

Modified AVMutableVideoCompositionInstruction

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMutableVideoCompositionLayerInstruction

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMutableVideoCompositionLayerInstruction.init(assetTrack: AVAssetTrack!)

|  | Declaration |
| --- | --- |
| From | ``` init(assetTrack track: AVAssetTrack!) -> AVMutableVideoCompositionLayerInstruction ``` |
| To | ``` init!(assetTrack track: AVAssetTrack!) -> AVMutableVideoCompositionLayerInstruction ``` |

Modified AVMutableVideoCompositionLayerInstruction.setCropRectangle(CGRect, atTime: CMTime)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMutableVideoCompositionLayerInstruction.setCropRectangleRampFromStartCropRectangle(CGRect, toEndCropRectangle: CGRect, timeRange: CMTimeRange)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVOutputSettingsAssistant

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVOutputSettingsAssistant.availableOutputSettingsPresets() -> [AnyObject]! [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVOutputSettingsAssistant.init(preset: String!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(preset presetIdentifier: String!) ``` |
| To | ``` convenience init!(preset presetIdentifier: String!) ``` |

Modified AVOutputSettingsAssistant.sourceVideoMinFrameDuration

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVPlayer.init(URL: NSURL!)

|  | Declaration |
| --- | --- |
| From | ``` init(URL URL: NSURL!) ``` |
| To | ``` init!(URL URL: NSURL!) ``` |

Modified AVPlayer.allowsExternalPlayback

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayer.appliesMediaSelectionCriteriaAutomatically

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayer.cancelPendingPrerolls()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayer.externalPlaybackActive

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayer.externalPlaybackVideoGravity

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayer.masterClock

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayer.mediaSelectionCriteriaForMediaCharacteristic(String!) -> AVPlayerMediaSelectionCriteria!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayer.muted

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayer.outputObscuredDueToInsufficientExternalProtection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayer.init(playerItem: AVPlayerItem!)

|  | Declaration |
| --- | --- |
| From | ``` init(playerItem item: AVPlayerItem!) ``` |
| To | ``` init!(playerItem item: AVPlayerItem!) ``` |

Modified AVPlayer.prerollAtRate(Float, completionHandler:((Bool) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayer.seekToDate(NSDate!, completionHandler:((Bool) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVPlayer.seekToTime(CMTime, completionHandler:((Bool) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVPlayer.seekToTime(CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler:((Bool) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVPlayer.setMediaSelectionCriteria(AVPlayerMediaSelectionCriteria!, forMediaCharacteristic: String!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayer.setRate(Float, time: CMTime, atHostTime: CMTime)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayer.usesExternalPlaybackWhileExternalScreenIsActive

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayer.volume

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerItem

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVPlayerItem.init(URL: NSURL!)

|  | Declaration |
| --- | --- |
| From | ``` init(URL URL: NSURL!) ``` |
| To | ``` init!(URL URL: NSURL!) ``` |

Modified AVPlayerItem.accessLog() -> AVPlayerItemAccessLog!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVPlayerItem.addOutput(AVPlayerItemOutput!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayerItem.init(asset: AVAsset!)

|  | Declaration |
| --- | --- |
| From | ``` init(asset asset: AVAsset!) ``` |
| To | ``` init!(asset asset: AVAsset!) ``` |

Modified AVPlayerItem.init(asset: AVAsset!, automaticallyLoadedAssetKeys:[AnyObject]!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(asset asset: AVAsset!, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [AnyObject]!) ``` | iOS 8.0 |
| To | ``` init!(asset asset: AVAsset!, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [AnyObject]!) ``` | iOS 7.0 |

Modified AVPlayerItem.audioTimePitchAlgorithm

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerItem.automaticallyLoadedAssetKeys

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerItem.canPlayFastForward

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVPlayerItem.canPlayFastReverse

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVPlayerItem.canPlayReverse

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayerItem.canPlaySlowForward

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayerItem.canPlaySlowReverse

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayerItem.canStepBackward

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayerItem.canStepForward

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayerItem.cancelPendingSeeks()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVPlayerItem.customVideoCompositor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerItem.duration

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVPlayerItem.errorLog() -> AVPlayerItemErrorLog!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVPlayerItem.outputs

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayerItem.removeOutput(AVPlayerItemOutput!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayerItem.seekToDate(NSDate!, completionHandler:((Bool) -> Void)!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayerItem.seekToTime(CMTime, completionHandler:((Bool) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVPlayerItem.seekToTime(CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler:((Bool) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVPlayerItem.seekingWaitsForVideoCompositionRendering

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayerItem.selectMediaOption(AVMediaSelectionOption!, inMediaSelectionGroup: AVMediaSelectionGroup!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVPlayerItem.selectMediaOptionAutomaticallyInMediaSelectionGroup(AVMediaSelectionGroup!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerItem.selectedMediaOptionInMediaSelectionGroup(AVMediaSelectionGroup!) -> AVMediaSelectionOption!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVPlayerItem.textStyleRules

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayerItem.timebase

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayerItemAccessLog

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVPlayerItemAccessLogEvent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVPlayerItemAccessLogEvent.downloadOverdue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerItemAccessLogEvent.mediaRequestsWWAN

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerItemAccessLogEvent.numberOfMediaRequests

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayerItemAccessLogEvent.observedBitrateStandardDeviation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerItemAccessLogEvent.observedMaxBitrate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerItemAccessLogEvent.observedMinBitrate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerItemAccessLogEvent.playbackType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerItemAccessLogEvent.startupTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerItemAccessLogEvent.switchBitrate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerItemAccessLogEvent.transferDuration

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerItemErrorLog

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVPlayerItemErrorLogEvent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVPlayerItemLegibleOutput

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerItemLegibleOutput.init(mediaSubtypesForNativeRepresentation: [AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(mediaSubtypesForNativeRepresentation subtypes: [AnyObject]!) ``` |
| To | ``` init!(mediaSubtypesForNativeRepresentation subtypes: [AnyObject]!) ``` |

Modified AVPlayerItemLegibleOutputPushDelegate.legibleOutput(AVPlayerItemLegibleOutput!, didOutputAttributedStrings:[AnyObject]!, nativeSampleBuffers:[AnyObject]!, forItemTime: CMTime)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerItemMetadataOutput.init(identifiers: [AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(identifiers identifiers: [AnyObject]!) ``` |
| To | ``` init!(identifiers identifiers: [AnyObject]!) ``` |

Modified AVPlayerItemOutput

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayerItemOutput.suppressesPlayerRendering

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayerItemOutputPullDelegate.outputMediaDataWillChange(AVPlayerItemOutput!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayerItemOutputPullDelegate.outputSequenceWasFlushed(AVPlayerItemOutput!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayerItemTrack

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVPlayerItemTrack.currentVideoFrameRate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerItemVideoOutput

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayerItemVideoOutput.init(pixelBufferAttributes: [NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(pixelBufferAttributes pixelBufferAttributes: [NSObject : AnyObject]!) ``` |
| To | ``` init!(pixelBufferAttributes pixelBufferAttributes: [NSObject : AnyObject]!) ``` |

Modified AVPlayerLayer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVPlayerLayer.init(player: AVPlayer!)

|  | Declaration |
| --- | --- |
| From | ``` init(player player: AVPlayer!) -> AVPlayerLayer ``` |
| To | ``` init!(player player: AVPlayer!) -> AVPlayerLayer ``` |

Modified AVPlayerLayer.videoRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerMediaSelectionCriteria

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerMediaSelectionCriteria.init(preferredLanguages: [AnyObject]!, preferredMediaCharacteristics:[AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(preferredLanguages preferredLanguages: [AnyObject]!, preferredMediaCharacteristics preferredMediaCharacteristics: [AnyObject]!) ``` |
| To | ``` init!(preferredLanguages preferredLanguages: [AnyObject]!, preferredMediaCharacteristics preferredMediaCharacteristics: [AnyObject]!) ``` |

Modified AVQueuePlayer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified AVQueuePlayer.init(items: [AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(items items: [AnyObject]!) ``` |
| To | ``` init!(items items: [AnyObject]!) ``` |

Modified AVSpeechBoundary [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVSpeechSynthesisVoice

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVSpeechSynthesisVoice.init(language: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(language language: String!) -> AVSpeechSynthesisVoice ``` |
| To | ``` init!(language language: String!) -> AVSpeechSynthesisVoice ``` |

Modified AVSpeechSynthesizer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVSpeechUtterance

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVSpeechUtterance.init(string: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(string string: String!) ``` |
| To | ``` init!(string string: String!) ``` |

Modified AVSynchronizedLayer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVSynchronizedLayer.init(playerItem: AVPlayerItem!)

|  | Declaration |
| --- | --- |
| From | ``` init(playerItem playerItem: AVPlayerItem!) -> AVSynchronizedLayer ``` |
| To | ``` init!(playerItem playerItem: AVPlayerItem!) -> AVSynchronizedLayer ``` |

Modified AVTextStyleRule

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVTextStyleRule.init(textMarkupAttributes: [NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(textMarkupAttributes textMarkupAttributes: [NSObject : AnyObject]!) ``` |
| To | ``` init!(textMarkupAttributes textMarkupAttributes: [NSObject : AnyObject]!) ``` |

Modified AVTextStyleRule.init(textMarkupAttributes: [NSObject: AnyObject]!, textSelector: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(textMarkupAttributes textMarkupAttributes: [NSObject : AnyObject]!, textSelector textSelector: String!) ``` |
| To | ``` init!(textMarkupAttributes textMarkupAttributes: [NSObject : AnyObject]!, textSelector textSelector: String!) ``` |

Modified AVTimedMetadataGroup

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVTimedMetadataGroup.init(items: [AnyObject]!, timeRange: CMTimeRange)

|  | Declaration |
| --- | --- |
| From | ``` init(items items: [AnyObject]!, timeRange timeRange: CMTimeRange) ``` |
| To | ``` init!(items items: [AnyObject]!, timeRange timeRange: CMTimeRange) ``` |

Modified AVTimedMetadataGroup.init(sampleBuffer: CMSampleBuffer!)

|  | Declaration |
| --- | --- |
| From | ``` init(sampleBuffer sampleBuffer: CMSampleBuffer!) ``` |
| To | ``` init!(sampleBuffer sampleBuffer: CMSampleBuffer!) ``` |

Modified AVURLAsset

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVURLAsset.init(URL: NSURL!, options:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(URL URL: NSURL!, options options: [NSObject : AnyObject]!) ``` |
| To | ``` init!(URL URL: NSURL!, options options: [NSObject : AnyObject]!) ``` |

Modified AVURLAsset.audiovisualMIMETypes() -> [AnyObject]! [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVURLAsset.audiovisualTypes() -> [AnyObject]! [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVURLAsset.isPlayableExtendedMIMEType(String!) -> Bool [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVURLAsset.resourceLoader

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVVideoCompositing

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVVideoComposition

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoComposition.customVideoCompositorClass

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVVideoComposition.isValidForAsset(AVAsset!, timeRange: CMTimeRange, validationDelegate: AVVideoCompositionValidationHandling!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVVideoComposition.init(propertiesOfAsset: AVAsset!)

|  | Declaration |
| --- | --- |
| From | ``` init(propertiesOfAsset asset: AVAsset!) -> AVVideoComposition ``` |
| To | ``` init!(propertiesOfAsset asset: AVAsset!) -> AVVideoComposition ``` |

Modified AVVideoCompositionCoreAnimationTool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoCompositionCoreAnimationTool.init(additionalLayer: CALayer!, asTrackID: CMPersistentTrackID)

|  | Declaration |
| --- | --- |
| From | ``` init(additionalLayer layer: CALayer!, asTrackID trackID: CMPersistentTrackID) -> AVVideoCompositionCoreAnimationTool ``` |
| To | ``` init!(additionalLayer layer: CALayer!, asTrackID trackID: CMPersistentTrackID) -> AVVideoCompositionCoreAnimationTool ``` |

Modified AVVideoCompositionCoreAnimationTool.init(postProcessingAsVideoLayer: CALayer!, inLayer: CALayer!)

|  | Declaration |
| --- | --- |
| From | ``` init(postProcessingAsVideoLayer videoLayer: CALayer!, inLayer animationLayer: CALayer!) -> AVVideoCompositionCoreAnimationTool ``` |
| To | ``` init!(postProcessingAsVideoLayer videoLayer: CALayer!, inLayer animationLayer: CALayer!) -> AVVideoCompositionCoreAnimationTool ``` |

Modified AVVideoCompositionCoreAnimationTool.init(postProcessingAsVideoLayers: [AnyObject]!, inLayer: CALayer!)

|  | Declaration |
| --- | --- |
| From | ``` init(postProcessingAsVideoLayers videoLayers: [AnyObject]!, inLayer animationLayer: CALayer!) -> AVVideoCompositionCoreAnimationTool ``` |
| To | ``` init!(postProcessingAsVideoLayers videoLayers: [AnyObject]!, inLayer animationLayer: CALayer!) -> AVVideoCompositionCoreAnimationTool ``` |

Modified AVVideoCompositionInstruction

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoCompositionInstruction.passthroughTrackID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVVideoCompositionInstruction.requiredSourceTrackIDs

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVVideoCompositionInstructionProtocol

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVVideoCompositionLayerInstruction

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoCompositionLayerInstruction.getCropRectangleRampForTime(CMTime, startCropRectangle: UnsafeMutablePointer<CGRect>, endCropRectangle: UnsafeMutablePointer<CGRect>, timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVVideoCompositionRenderContext

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVVideoCompositionValidationHandling.videoComposition(AVVideoComposition!, shouldContinueValidatingAfterFindingEmptyTimeRange: CMTimeRange) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVVideoCompositionValidationHandling.videoComposition(AVVideoComposition!, shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction: AVVideoCompositionInstructionProtocol!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVVideoCompositionValidationHandling.videoComposition(AVVideoComposition!, shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction: AVVideoCompositionInstructionProtocol!, layerInstruction: AVVideoCompositionLayerInstruction!, asset: AVAsset!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVVideoCompositionValidationHandling.videoComposition(AVVideoComposition!, shouldContinueValidatingAfterFindingInvalidValueForKey: String!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAssetExportPreset1280x720

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAssetExportPreset1920x1080

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAssetExportPreset640x480

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAssetExportPreset960x540

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAssetExportPresetAppleM4A

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAssetExportPresetHighestQuality

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAssetExportPresetLowQuality

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAssetExportPresetMediumQuality

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAssetExportPresetPassthrough

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAssetImageGeneratorApertureModeCleanAperture

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAssetImageGeneratorApertureModeEncodedPixels

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAssetImageGeneratorApertureModeProductionAperture

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVAudioBitRateStrategy_Constant

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioBitRateStrategy_LongTermAverage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioBitRateStrategy_Variable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioBitRateStrategy_VariableConstrained

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionCategoryMultiRoute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionInterruptionNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionInterruptionOptionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionInterruptionTypeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionLocationLower

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionLocationUpper

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionMediaServicesWereLostNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionMediaServicesWereResetNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionModeDefault

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAudioSessionModeGameChat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAudioSessionModeMeasurement

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAudioSessionModeMoviePlayback

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionModeVideoChat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionModeVideoRecording

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAudioSessionModeVoiceChat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVAudioSessionOrientationBack

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionOrientationBottom

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionOrientationFront

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionOrientationTop

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionPolarPatternCardioid

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionPolarPatternOmnidirectional

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionPolarPatternSubcardioid

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionPortAirPlay

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionPortBluetoothA2DP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionPortBluetoothHFP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionPortBluetoothLE

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionPortBuiltInMic

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionPortBuiltInReceiver

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionPortBuiltInSpeaker

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionPortCarAudio

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioSessionPortHDMI

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionPortHeadphones

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionPortHeadsetMic

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionPortLineIn

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionPortLineOut

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionPortUSBAudio

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionRouteChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionRouteChangePreviousRouteKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioSessionRouteChangeReasonKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVAudioTimePitchAlgorithmLowQualityZeroLatency

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioTimePitchAlgorithmSpectral

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioTimePitchAlgorithmTimeDomain

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVAudioTimePitchAlgorithmVarispeed

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureDeviceSubjectAreaDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVCaptureDeviceWasConnectedNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureDeviceWasDisconnectedNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureInputPortFormatDescriptionDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureSessionDidStartRunningNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureSessionDidStopRunningNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureSessionErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureSessionInterruptionEndedNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureSessionPreset1280x720

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureSessionPreset1920x1080

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVCaptureSessionPreset352x288

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVCaptureSessionPreset640x480

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureSessionPresetHigh

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureSessionPresetInputPriority

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureSessionPresetLow

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureSessionPresetMedium

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureSessionPresetPhoto

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureSessionPresetiFrame1280x720

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVCaptureSessionPresetiFrame960x540

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVCaptureSessionRuntimeErrorNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCaptureSessionWasInterruptedNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVChannelLayoutKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVCoreAnimationBeginTimeAtZero

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVEncoderAudioQualityForVBRKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVEncoderBitRatePerChannelKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVEncoderBitRateStrategyKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVErrorDeviceKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVErrorFileSizeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVErrorMediaSubTypeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVErrorMediaTypeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVErrorPIDKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVErrorRecordingSuccessfullyFinishedKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVErrorTimeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVFileType3GPP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVFileType3GPP2

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVFileTypeAC3

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVFileTypeAIFC

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVFileTypeAIFF

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVFileTypeAMR

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVFileTypeAppleM4A

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVFileTypeAppleM4V

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVFileTypeCoreAudioFormat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVFileTypeMPEG4

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVFileTypeMPEGLayer3

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVFileTypeQuickTimeMovie

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVFileTypeSunAU

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVFileTypeWAVE

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVFoundationErrorDomain

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVLayerVideoGravityResize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVLayerVideoGravityResizeAspect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVLayerVideoGravityResizeAspectFill

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVLinearPCMIsNonInterleaved

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMakeRectWithAspectRatioInsideRect(CGSize, CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMediaCharacteristicAudible

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMediaCharacteristicContainsOnlyForcedSubtitles

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVMediaCharacteristicDescribesMusicAndSoundForAccessibility

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVMediaCharacteristicDescribesVideoForAccessibility

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVMediaCharacteristicEasyToRead

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVMediaCharacteristicFrameBased

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMediaCharacteristicIsAuxiliaryContent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVMediaCharacteristicIsMainProgramContent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVMediaCharacteristicLegible

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMediaCharacteristicTranscribesSpokenDialogForAccessibility

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVMediaCharacteristicVisual

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMediaTypeAudio

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMediaTypeClosedCaption

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMediaTypeMetadata

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVMediaTypeMuxed

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMediaTypeSubtitle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMediaTypeText

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMediaTypeTimecode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMediaTypeVideo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadata3GPUserDataKeyAlbumAndTrack

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadata3GPUserDataKeyAuthor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadata3GPUserDataKeyCollection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadata3GPUserDataKeyCopyright

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadata3GPUserDataKeyDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadata3GPUserDataKeyGenre

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadata3GPUserDataKeyKeywordList

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadata3GPUserDataKeyLocation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadata3GPUserDataKeyMediaClassification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadata3GPUserDataKeyMediaRating

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadata3GPUserDataKeyPerformer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadata3GPUserDataKeyRecordingYear

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadata3GPUserDataKeyThumbnail

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadata3GPUserDataKeyTitle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadata3GPUserDataKeyUserRating

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadataCommonKeyAlbumName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeyArtist

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeyArtwork

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeyAuthor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeyContributor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeyCopyrights

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeyCreationDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeyCreator

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeyDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeyFormat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeyIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeyLanguage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeyLastModifiedDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeyLocation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeyMake

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeyModel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeyPublisher

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeyRelation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeySoftware

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeySource

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeySubject

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeyTitle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataCommonKeyType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataFormatID3Metadata

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataFormatISOUserData

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadataFormatQuickTimeMetadata

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataFormatQuickTimeUserData

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataFormatiTunesMetadata

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyAlbumSortOrder

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyAlbumTitle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyAttachedPicture

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyAudioEncryption

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyAudioSeekPointIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyBand

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyBeatsPerMinute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyComments

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyCommercialInformation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyCommerical

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyComposer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyConductor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyContentGroupDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyContentType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyCopyright

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyCopyrightInformation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyEncodedBy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyEncodedWith

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyEncodingTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyEncryption

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyEqualization

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyEqualization2

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyEventTimingCodes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyFileOwner

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyFileType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyGeneralEncapsulatedObject

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyGroupIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyInitialKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyInternationalStandardRecordingCode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyInternetRadioStationName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyInternetRadioStationOwner

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyInvolvedPeopleList_v23

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyInvolvedPeopleList_v24

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyLanguage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyLeadPerformer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyLength

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyLink

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyLyricist

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyMPEGLocationLookupTable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyMediaType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyModifiedBy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyMood

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyMusicCDIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyMusicianCreditsList

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyOfficialArtistWebpage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyOfficialAudioFileWebpage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyOfficialAudioSourceWebpage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyOfficialInternetRadioStationHomepage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyOfficialPublisherWebpage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyOriginalAlbumTitle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyOriginalArtist

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyOriginalFilename

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyOriginalLyricist

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyOriginalReleaseTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyOriginalReleaseYear

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyOwnership

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyPartOfASet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyPayment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyPerformerSortOrder

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyPlayCounter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyPlaylistDelay

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyPopularimeter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyPositionSynchronization

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyPrivate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyProducedNotice

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyPublisher

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyRecommendedBufferSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyRecordingDates

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyRecordingTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyRelativeVolumeAdjustment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyRelativeVolumeAdjustment2

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyReleaseTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyReverb

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeySeek

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeySetSubtitle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeySignature

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeySize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeySubTitle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeySynchronizedLyric

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeySynchronizedTempoCodes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyTaggingTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyTermsOfUse

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyTitleDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyTitleSortOrder

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyTrackNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyUniqueFileIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyUnsynchronizedLyric

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyUserText

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyUserURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataID3MetadataKeyYear

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataISOUserDataKeyCopyright

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataKeySpaceCommon

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataKeySpaceID3

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataKeySpaceISOUserData

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadataKeySpaceQuickTimeMetadata

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataKeySpaceQuickTimeUserData

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataKeySpaceiTunes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataObjectTypeAztecCode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadataObjectTypeCode128Code

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadataObjectTypeCode39Code

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadataObjectTypeCode39Mod43Code

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadataObjectTypeCode93Code

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadataObjectTypeEAN13Code

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadataObjectTypeEAN8Code

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadataObjectTypeFace

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVMetadataObjectTypePDF417Code

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadataObjectTypeQRCode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadataObjectTypeUPCECode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVMetadataQuickTimeMetadataKeyAlbum

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyArranger

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyArtist

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyArtwork

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyAuthor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyCameraFrameReadoutTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyCameraIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyCollectionUser

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVMetadataQuickTimeMetadataKeyComment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyComposer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyCopyright

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyCreationDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyCredits

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyDirectionFacing

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVMetadataQuickTimeMetadataKeyDirectionMotion

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVMetadataQuickTimeMetadataKeyDirector

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyDisplayName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyEncodedBy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyGenre

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyInformation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyKeywords

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyLocationBody

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVMetadataQuickTimeMetadataKeyLocationDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVMetadataQuickTimeMetadataKeyLocationISO6709

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyLocationName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVMetadataQuickTimeMetadataKeyLocationNote

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVMetadataQuickTimeMetadataKeyLocationRole

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVMetadataQuickTimeMetadataKeyMake

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyModel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyOriginalArtist

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyPerformer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyPhonogramRights

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyProducer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyPublisher

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyRatingUser

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVMetadataQuickTimeMetadataKeySoftware

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyTitle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVMetadataQuickTimeMetadataKeyYear

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeMetadataKeyiXML

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyAlbum

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyArranger

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyArtist

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyAuthor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyChapter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyComment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyComposer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyCopyright

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyCreationDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyCredits

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyDirector

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyDisclaimer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyEncodedBy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyFullName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyGenre

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyHostComputer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyInformation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyKeywords

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyLocationISO6709

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyMake

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyModel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyOriginalArtist

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyOriginalFormat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyOriginalSource

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyPerformers

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyPhonogramRights

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyProducer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyProduct

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyPublisher

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeySoftware

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeySpecialPlaybackRequirements

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyTaggedCharacteristic

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVMetadataQuickTimeUserDataKeyTrack

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyTrackName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyURLLink

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyWarning

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataQuickTimeUserDataKeyWriter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyAccountKind

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyAcknowledgement

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyAlbum

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyAlbumArtist

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyAppleID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyArranger

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyArtDirector

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyArtist

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyArtistID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyAuthor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyBeatsPerMin

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyComposer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyConductor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyContentRating

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyCopyright

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyCoverArt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyCredits

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyDirector

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyDiscCompilation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyDiscNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyEQ

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyEncodedBy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyEncodingTool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyExecProducer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyGenreID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyGrouping

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyLinerNotes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyLyrics

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyOnlineExtras

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyOriginalArtist

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyPerformer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyPhonogramRights

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyPlaylistID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyPredefinedGenre

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyProducer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyPublisher

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyRecordCompany

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyReleaseDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeySoloist

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeySongID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeySongName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeySoundEngineer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyThanks

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyTrackNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyTrackSubTitle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyUserComment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVMetadataiTunesMetadataKeyUserGenre

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVOutputSettingsPreset1280x720

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVOutputSettingsPreset1920x1080

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVOutputSettingsPreset640x480

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVOutputSettingsPreset960x540

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerItemDidPlayToEndTimeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVPlayerItemFailedToPlayToEndTimeErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVPlayerItemFailedToPlayToEndTimeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified AVPlayerItemLegibleOutputTextStylingResolutionDefault

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerItemLegibleOutputTextStylingResolutionSourceAndRulesOnly

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVPlayerItemNewAccessLogEntryNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayerItemNewErrorLogEntryNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayerItemPlaybackStalledNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPlayerItemTimeJumpedNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVSampleRateConverterAlgorithmKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVSampleRateConverterAlgorithm_Mastering

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVSampleRateConverterAlgorithm_Normal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVTrackAssociationTypeAudioFallback

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVTrackAssociationTypeChapterList

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVTrackAssociationTypeForcedSubtitlesOnly

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVTrackAssociationTypeSelectionFollower

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVTrackAssociationTypeTimecode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVURLAssetPreferPreciseDurationAndTimingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVURLAssetReferenceRestrictionsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVVideoAllowFrameReorderingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVVideoAverageBitRateKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoAverageNonDroppableFrameRateKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVVideoCleanApertureHeightKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoCleanApertureHorizontalOffsetKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoCleanApertureKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoCleanApertureVerticalOffsetKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoCleanApertureWidthKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoCodecH264

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoCodecJPEG

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoCodecKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoCompressionPropertiesKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoExpectedSourceFrameRateKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVVideoH264EntropyModeCABAC

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVVideoH264EntropyModeCAVLC

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVVideoH264EntropyModeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVVideoHeightKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoMaxKeyFrameIntervalDurationKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVVideoMaxKeyFrameIntervalKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoPixelAspectRatioHorizontalSpacingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoPixelAspectRatioKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoPixelAspectRatioVerticalSpacingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoProfileLevelH264Baseline30

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoProfileLevelH264Baseline31

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoProfileLevelH264Baseline41

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVVideoProfileLevelH264BaselineAutoLevel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVVideoProfileLevelH264High40

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVVideoProfileLevelH264High41

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVVideoProfileLevelH264HighAutoLevel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVVideoProfileLevelH264Main30

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoProfileLevelH264Main31

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoProfileLevelH264Main32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVVideoProfileLevelH264Main41

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVVideoProfileLevelH264MainAutoLevel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVVideoProfileLevelKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified AVVideoQualityKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVVideoScalingModeFit

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVVideoScalingModeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVVideoScalingModeResize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVVideoScalingModeResizeAspect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVVideoScalingModeResizeAspectFill

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified AVVideoWidthKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

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
