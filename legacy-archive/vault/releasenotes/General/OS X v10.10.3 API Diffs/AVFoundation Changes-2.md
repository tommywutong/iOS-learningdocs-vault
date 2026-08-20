---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/AVFoundation.html
archived_at: '2026-07-18T02:51:51.307645Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# AVFoundation Changes

## AVFoundation

Removed AVAssetReader.assetReaderWithAsset(AVAsset!, error: NSErrorPointer) -> Self! [class]Removed AVAssetReferenceRestrictions.valueRemoved AVAssetWriter.assetWriterWithURL(NSURL!, fileType: String!, error: NSErrorPointer) -> Self! [class]Removed AVAudioChannelLayout.layoutWithLayout(ConstUnsafePointer<AudioChannelLayout>) -> Self! [class]Removed AVAudioChannelLayout.layoutWithLayoutTag(AudioChannelLayoutTag) -> Self! [class]Removed AVAudioPlayerNodeBufferOptions.valueRemoved AVAudioTime.timeWithAudioTimeStamp(ConstUnsafePointer<AudioTimeStamp>, sampleRate: Double) -> Self! [class]Removed AVAudioTime.timeWithHostTime(UInt64) -> Self! [class]Removed AVAudioTime.timeWithHostTime(UInt64, sampleTime: AVAudioFramePosition, atRate: Double) -> Self! [class]Removed AVAudioTime.timeWithSampleTime(AVAudioFramePosition, atRate: Double) -> Self! [class]Removed AVURLAsset.URLAssetWithURL(NSURL!, options:[NSObject: AnyObject]!) -> AVURLAsset! [class]Removed AVMetadataFormatIcyMetadataAdded AVAssetReferenceRestrictions.init(rawValue: UInt)Added AVAudio3DAngularOrientation.init()Added AVAudio3DAngularOrientation.init(yaw: Float, pitch: Float, roll: Float)Added AVAudio3DPoint.init()Added AVAudio3DPoint.init(x: Float, y: Float, z: Float)Added AVAudio3DVectorOrientation.init()Added AVAudio3DVectorOrientation.init(forward: AVAudio3DVector, up: AVAudio3DVector)Added AVAudioPlayerNodeBufferOptions.init(rawValue: UInt)Added AVEdgeWidths.init()Added AVEdgeWidths.init(left: CGFloat, top: CGFloat, right: CGFloat, bottom: CGFloat)Added AVPixelAspectRatio.init()Added AVPixelAspectRatio.init(horizontalSpacing: Int, verticalSpacing: Int)Added AVSampleCursorChunkInfo.init()Added AVSampleCursorChunkInfo.init(chunkSampleCount: Int64, chunkHasUniformSampleSizes: ObjCBool, chunkHasUniformSampleDurations: ObjCBool, chunkHasUniformFormatDescriptions: ObjCBool)Added AVSampleCursorDependencyInfo.init()Added AVSampleCursorDependencyInfo.init(sampleIndicatesWhetherItHasDependentSamples: ObjCBool, sampleHasDependentSamples: ObjCBool, sampleIndicatesWhetherItDependsOnOthers: ObjCBool, sampleDependsOnOthers: ObjCBool, sampleIndicatesWhetherItHasRedundantCoding: ObjCBool, sampleHasRedundantCoding: ObjCBool)Added AVSampleCursorStorageRange.init()Added AVSampleCursorStorageRange.init(offset: Int64, length: Int64)Added AVSampleCursorSyncInfo.init()Added AVSampleCursorSyncInfo.init(sampleIsFullSync: ObjCBool, sampleIsPartialSync: ObjCBool, sampleIsDroppable: ObjCBool)Added NSCoder.decodeCMTimeForKey(String!) -> CMTimeAdded NSCoder.decodeCMTimeMappingForKey(String!) -> CMTimeMappingAdded NSCoder.decodeCMTimeRangeForKey(String!) -> CMTimeRangeAdded NSCoder.encodeCMTime(CMTime, forKey: String!)Added NSCoder.encodeCMTimeMapping(CMTimeMapping, forKey: String!)Added NSCoder.encodeCMTimeRange(CMTimeRange, forKey: String!)Added NSValue.init(CMTime: CMTime)Added NSValue.init(CMTimeMapping: CMTimeMapping)Added NSValue.CMTimeMappingValueAdded NSValue.init(CMTimeRange: CMTimeRange)Added NSValue.CMTimeRangeValueAdded NSValue.CMTimeValueModified AVAsset

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAsset.availableChapterLocales

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAsset.availableMediaCharacteristicsWithMediaSelectionOptions

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVAsset.chapterMetadataGroupsBestMatchingPreferredLanguages([AnyObject]!) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVAsset.chapterMetadataGroupsWithTitleLocale(NSLocale!, containingItemsWithCommonKeys:[AnyObject]!) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAsset.composable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAsset.creationDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVAsset.exportable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAsset.hasProtectedContent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAsset.mediaSelectionGroupForMediaCharacteristic(String!) -> AVMediaSelectionGroup!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVAsset.playable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAsset.readable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAsset.referenceRestrictions

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAsset.trackGroups

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetExportSession

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAssetExportSession.asset

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVAssetExportSession.init(asset: AVAsset!, presetName: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(asset asset: AVAsset!, presetName presetName: String!) ``` |
| To | ``` init!(asset asset: AVAsset!, presetName presetName: String!) ``` |

Modified AVAssetExportSession.audioMix

|  | Declaration |
| --- | --- |
| From | ``` var audioMix: AVAudioMix! ``` |
| To | ``` @NSCopying var audioMix: AVAudioMix! ``` |

Modified AVAssetExportSession.audioTimePitchAlgorithm

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetExportSession.customVideoCompositor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetExportSession.determineCompatibilityOfExportPreset(String!, withAsset: AVAsset!, outputFileType: String!, completionHandler:((Bool) -> Void)!) [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetExportSession.determineCompatibleFileTypesWithCompletionHandler((([AnyObject]!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetExportSession.directoryForTemporaryFiles

|  | Declaration |
| --- | --- |
| From | ``` var directoryForTemporaryFiles: NSURL! ``` |
| To | ``` @NSCopying var directoryForTemporaryFiles: NSURL! ``` |

Modified AVAssetExportSession.estimatedOutputFileLength

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetExportSession.metadataItemFilter

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetExportSession.outputURL

|  | Declaration |
| --- | --- |
| From | ``` var outputURL: NSURL! ``` |
| To | ``` @NSCopying var outputURL: NSURL! ``` |

Modified AVAssetExportSession.videoComposition

|  | Declaration |
| --- | --- |
| From | ``` var videoComposition: AVVideoComposition! ``` |
| To | ``` @NSCopying var videoComposition: AVVideoComposition! ``` |

Modified AVAssetImageGenerator

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAssetImageGenerator.asset

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetImageGenerator.init(asset: AVAsset!)

|  | Declaration |
| --- | --- |
| From | ``` init(asset asset: AVAsset!) ``` |
| To | ``` init!(asset asset: AVAsset!) ``` |

Modified AVAssetImageGenerator.copyCGImageAtTime(CMTime, actualTime: UnsafeMutablePointer<CMTime>, error: NSErrorPointer) -> CGImage!

|  | Declaration |
| --- | --- |
| From | ``` func copyCGImageAtTime(_ requestedTime: CMTime, actualTime actualTime: UnsafePointer<CMTime>, error outError: NSErrorPointer) -> CGImage! ``` |
| To | ``` func copyCGImageAtTime(_ requestedTime: CMTime, actualTime actualTime: UnsafeMutablePointer<CMTime>, error outError: NSErrorPointer) -> CGImage! ``` |

Modified AVAssetImageGenerator.customVideoCompositor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetImageGenerator.requestedTimeToleranceAfter

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAssetImageGenerator.requestedTimeToleranceBefore

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAssetImageGenerator.videoComposition

|  | Declaration |
| --- | --- |
| From | ``` var videoComposition: AVVideoComposition! ``` |
| To | ``` @NSCopying var videoComposition: AVVideoComposition! ``` |

Modified AVAssetReader

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAssetReader.init(asset: AVAsset!, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(asset asset: AVAsset!, error outError: NSErrorPointer) ``` |
| To | ``` init!(asset asset: AVAsset!, error outError: NSErrorPointer) ``` |

Modified AVAssetReaderAudioMixOutput

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAssetReaderAudioMixOutput.audioMix

|  | Declaration |
| --- | --- |
| From | ``` var audioMix: AVAudioMix! ``` |
| To | ``` @NSCopying var audioMix: AVAudioMix! ``` |

Modified AVAssetReaderAudioMixOutput.audioTimePitchAlgorithm

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetReaderAudioMixOutput.init(audioTracks: [AnyObject]!, audioSettings:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(audioTracks audioTracks: [AnyObject]!, audioSettings audioSettings: [NSObject : AnyObject]!) ``` |
| To | ``` init!(audioTracks audioTracks: [AnyObject]!, audioSettings audioSettings: [NSObject : AnyObject]!) ``` |

Modified AVAssetReaderOutput

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAssetReaderOutput.alwaysCopiesSampleData

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

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
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAssetReaderTrackOutput.audioTimePitchAlgorithm

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetReaderTrackOutput.init(track: AVAssetTrack!, outputSettings:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(track track: AVAssetTrack!, outputSettings outputSettings: [NSObject : AnyObject]!) ``` |
| To | ``` init!(track track: AVAssetTrack!, outputSettings outputSettings: [NSObject : AnyObject]!) ``` |

Modified AVAssetReaderVideoCompositionOutput

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAssetReaderVideoCompositionOutput.customVideoCompositor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetReaderVideoCompositionOutput.videoComposition

|  | Declaration |
| --- | --- |
| From | ``` var videoComposition: AVVideoComposition! ``` |
| To | ``` @NSCopying var videoComposition: AVVideoComposition! ``` |

Modified AVAssetReaderVideoCompositionOutput.init(videoTracks: [AnyObject]!, videoSettings:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(videoTracks videoTracks: [AnyObject]!, videoSettings videoSettings: [NSObject : AnyObject]!) ``` |
| To | ``` init!(videoTracks videoTracks: [AnyObject]!, videoSettings videoSettings: [NSObject : AnyObject]!) ``` |

Modified AVAssetReferenceRestrictions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVAssetReferenceRestrictions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var RestrictionForbidNone: AVAssetReferenceRestrictions { get }     static var RestrictionForbidRemoteReferenceToLocal: AVAssetReferenceRestrictions { get }     static var RestrictionForbidLocalReferenceToRemote: AVAssetReferenceRestrictions { get }     static var RestrictionForbidCrossSiteReference: AVAssetReferenceRestrictions { get }     static var RestrictionForbidLocalReferenceToLocal: AVAssetReferenceRestrictions { get }     static var RestrictionForbidAll: AVAssetReferenceRestrictions { get } } ``` | RawOptionSet |
| To | ``` struct AVAssetReferenceRestrictions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var RestrictionForbidNone: AVAssetReferenceRestrictions { get }     static var RestrictionForbidRemoteReferenceToLocal: AVAssetReferenceRestrictions { get }     static var RestrictionForbidLocalReferenceToRemote: AVAssetReferenceRestrictions { get }     static var RestrictionForbidCrossSiteReference: AVAssetReferenceRestrictions { get }     static var RestrictionForbidLocalReferenceToLocal: AVAssetReferenceRestrictions { get }     static var RestrictionForbidAll: AVAssetReferenceRestrictions { get } } ``` | RawOptionSetType |

Modified AVAssetReferenceRestrictions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified AVAssetResourceLoader

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetResourceLoaderDelegate.resourceLoader(AVAssetResourceLoader!, didCancelAuthenticationChallenge: NSURLAuthenticationChallenge!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified AVAssetResourceLoaderDelegate.resourceLoader(AVAssetResourceLoader!, didCancelLoadingRequest: AVAssetResourceLoadingRequest!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | yes |

Modified AVAssetResourceLoaderDelegate.resourceLoader(AVAssetResourceLoader!, shouldWaitForLoadingOfRequestedResource: AVAssetResourceLoadingRequest!) -> Bool

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | yes |

Modified AVAssetResourceLoaderDelegate.resourceLoader(AVAssetResourceLoader!, shouldWaitForRenewalOfRequestedResource: AVAssetResourceRenewalRequest!) -> Bool

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified AVAssetResourceLoaderDelegate.resourceLoader(AVAssetResourceLoader!, shouldWaitForResponseToAuthenticationChallenge: NSURLAuthenticationChallenge!) -> Bool

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified AVAssetResourceLoadingContentInformationRequest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetResourceLoadingContentInformationRequest.renewalDate

|  | Declaration |
| --- | --- |
| From | ``` var renewalDate: NSDate! ``` |
| To | ``` @NSCopying var renewalDate: NSDate! ``` |

Modified AVAssetResourceLoadingDataRequest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetResourceLoadingRequest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetResourceLoadingRequest.cancelled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetResourceLoadingRequest.contentInformationRequest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetResourceLoadingRequest.dataRequest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetResourceLoadingRequest.finishLoading()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetResourceLoadingRequest.redirect

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var redirect: NSURLRequest! ``` | OS X 10.10 |
| To | ``` @NSCopying var redirect: NSURLRequest! ``` | OS X 10.9 |

Modified AVAssetResourceLoadingRequest.response

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var response: NSURLResponse! ``` | OS X 10.10 |
| To | ``` @NSCopying var response: NSURLResponse! ``` | OS X 10.9 |

Modified AVAssetTrack

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAssetTrack.associatedTracksOfType(String!) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetTrack.availableTrackAssociationTypes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetTrack.playable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVAssetTrackGroup

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetTrackSegment

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAssetWriter

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAssetWriter.init(URL: NSURL!, fileType: String!, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(URL outputURL: NSURL!, fileType outputFileType: String!, error outError: NSErrorPointer) ``` |
| To | ``` init!(URL outputURL: NSURL!, fileType outputFileType: String!, error outError: NSErrorPointer) ``` |

Modified AVAssetWriter.addInputGroup(AVAssetWriterInputGroup!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetWriter.canAddInputGroup(AVAssetWriterInputGroup!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetWriter.directoryForTemporaryFiles

|  | Declaration |
| --- | --- |
| From | ``` var directoryForTemporaryFiles: NSURL! ``` |
| To | ``` @NSCopying var directoryForTemporaryFiles: NSURL! ``` |

Modified AVAssetWriter.finishWritingWithCompletionHandler((() -> Void)!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetWriter.inputGroups

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetWriter.movieTimeScale

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAssetWriter.outputURL

|  | Declaration |
| --- | --- |
| From | ``` var outputURL: NSURL! { get } ``` |
| To | ``` @NSCopying var outputURL: NSURL! { get } ``` |

Modified AVAssetWriterInput

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAssetWriterInput.addTrackAssociationWithTrackOfInput(AVAssetWriterInput!, type: String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetWriterInput.canAddTrackAssociationWithTrackOfInput(AVAssetWriterInput!, type: String!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetWriterInput.extendedLanguageTag

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetWriterInput.languageCode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetWriterInput.marksOutputTrackAsEnabled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetWriterInput.mediaTimeScale

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAssetWriterInput.init(mediaType: String!, outputSettings:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(mediaType mediaType: String!, outputSettings outputSettings: [NSObject : AnyObject]!) ``` |
| To | ``` init!(mediaType mediaType: String!, outputSettings outputSettings: [NSObject : AnyObject]!) ``` |

Modified AVAssetWriterInput.init(mediaType: String!, outputSettings:[NSObject: AnyObject]!, sourceFormatHint: CMFormatDescription!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(mediaType mediaType: String!, outputSettings outputSettings: [NSObject : AnyObject]!, sourceFormatHint sourceFormatHint: CMFormatDescription!) ``` | OS X 10.10 |
| To | ``` init!(mediaType mediaType: String!, outputSettings outputSettings: [NSObject : AnyObject]!, sourceFormatHint sourceFormatHint: CMFormatDescription!) ``` | OS X 10.8 |

Modified AVAssetWriterInput.naturalSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetWriterInput.preferredVolume

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAssetWriterInput.sampleReferenceBaseURL

|  | Declaration |
| --- | --- |
| From | ``` var sampleReferenceBaseURL: NSURL! ``` |
| To | ``` @NSCopying var sampleReferenceBaseURL: NSURL! ``` |

Modified AVAssetWriterInput.sourceFormatHint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVAssetWriterInputGroup

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

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
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAssetWriterInputPixelBufferAdaptor.init(assetWriterInput: AVAssetWriterInput!, sourcePixelBufferAttributes:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(assetWriterInput input: AVAssetWriterInput!, sourcePixelBufferAttributes sourcePixelBufferAttributes: [NSObject : AnyObject]!) ``` |
| To | ``` init!(assetWriterInput input: AVAssetWriterInput!, sourcePixelBufferAttributes sourcePixelBufferAttributes: [NSObject : AnyObject]!) ``` |

Modified AVAsynchronousVideoCompositionRequest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAudio3DAngularOrientation [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AVAudio3DAngularOrientation {     var yaw: Float     var pitch: Float     var roll: Float } ``` |
| To | ``` struct AVAudio3DAngularOrientation {     var yaw: Float     var pitch: Float     var roll: Float     init()     init(yaw yaw: Float, pitch pitch: Float, roll roll: Float) } ``` |

Modified AVAudio3DPoint [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AVAudio3DPoint {     var x: Float     var y: Float     var z: Float } ``` |
| To | ``` struct AVAudio3DPoint {     var x: Float     var y: Float     var z: Float     init()     init(x x: Float, y y: Float, z z: Float) } ``` |

Modified AVAudio3DVectorOrientation [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AVAudio3DVectorOrientation {     var forward: AVAudio3DVector     var up: AVAudio3DVector } ``` |
| To | ``` struct AVAudio3DVectorOrientation {     var forward: AVAudio3DVector     var up: AVAudio3DVector     init()     init(forward forward: AVAudio3DVector, up up: AVAudio3DVector) } ``` |

Modified AVAudioBuffer.audioBufferList

|  | Declaration |
| --- | --- |
| From | ``` var audioBufferList: ConstUnsafePointer<AudioBufferList> { get } ``` |
| To | ``` var audioBufferList: UnsafePointer<AudioBufferList> { get } ``` |

Modified AVAudioBuffer.mutableAudioBufferList

|  | Declaration |
| --- | --- |
| From | ``` var mutableAudioBufferList: UnsafePointer<AudioBufferList> { get } ``` |
| To | ``` var mutableAudioBufferList: UnsafeMutablePointer<AudioBufferList> { get } ``` |

Modified AVAudioChannelLayout.layout

|  | Declaration |
| --- | --- |
| From | ``` var layout: ConstUnsafePointer<AudioChannelLayout> { get } ``` |
| To | ``` var layout: UnsafePointer<AudioChannelLayout> { get } ``` |

Modified AVAudioChannelLayout.init(layout: UnsafePointer<AudioChannelLayout>)

|  | Declaration |
| --- | --- |
| From | ``` init(layout layout: ConstUnsafePointer<AudioChannelLayout>) ``` |
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

Modified AVAudioFormat.streamDescription

|  | Declaration |
| --- | --- |
| From | ``` var streamDescription: ConstUnsafePointer<AudioStreamBasicDescription> { get } ``` |
| To | ``` var streamDescription: UnsafePointer<AudioStreamBasicDescription> { get } ``` |

Modified AVAudioFormat.init(streamDescription: UnsafePointer<AudioStreamBasicDescription>)

|  | Declaration |
| --- | --- |
| From | ``` init(streamDescription asbd: ConstUnsafePointer<AudioStreamBasicDescription>) ``` |
| To | ``` init!(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>) ``` |

Modified AVAudioFormat.init(streamDescription: UnsafePointer<AudioStreamBasicDescription>, channelLayout: AVAudioChannelLayout!)

|  | Declaration |
| --- | --- |
| From | ``` init(streamDescription asbd: ConstUnsafePointer<AudioStreamBasicDescription>, channelLayout layout: AVAudioChannelLayout!) ``` |
| To | ``` init!(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>, channelLayout layout: AVAudioChannelLayout!) ``` |

Modified AVAudioMix

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAudioMixInputParameters

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAudioMixInputParameters.audioTapProcessor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVAudioMixInputParameters.getVolumeRampForTime(CMTime, startVolume: UnsafeMutablePointer<Float>, endVolume: UnsafeMutablePointer<Float>, timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func getVolumeRampForTime(_ time: CMTime, startVolume startVolume: UnsafePointer<Float>, endVolume endVolume: UnsafePointer<Float>, timeRange timeRange: UnsafePointer<CMTimeRange>) -> Bool ``` |
| To | ``` func getVolumeRampForTime(_ time: CMTime, startVolume startVolume: UnsafeMutablePointer<Float>, endVolume endVolume: UnsafeMutablePointer<Float>, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool ``` |

Modified AVAudioPCMBuffer.init(PCMFormat: AVAudioFormat!, frameCapacity: AVAudioFrameCount)

|  | Declaration |
| --- | --- |
| From | ``` init(PCMFormat format: AVAudioFormat!, frameCapacity frameCapacity: AVAudioFrameCount) ``` |
| To | ``` init!(PCMFormat format: AVAudioFormat!, frameCapacity frameCapacity: AVAudioFrameCount) ``` |

Modified AVAudioPCMBuffer.floatChannelData

|  | Declaration |
| --- | --- |
| From | ``` var floatChannelData: ConstUnsafePointer<UnsafePointer<Float>> { get } ``` |
| To | ``` var floatChannelData: UnsafePointer<UnsafeMutablePointer<Float>> { get } ``` |

Modified AVAudioPCMBuffer.int16ChannelData

|  | Declaration |
| --- | --- |
| From | ``` var int16ChannelData: ConstUnsafePointer<UnsafePointer<Int16>> { get } ``` |
| To | ``` var int16ChannelData: UnsafePointer<UnsafeMutablePointer<Int16>> { get } ``` |

Modified AVAudioPCMBuffer.int32ChannelData

|  | Declaration |
| --- | --- |
| From | ``` var int32ChannelData: ConstUnsafePointer<UnsafePointer<Int32>> { get } ``` |
| To | ``` var int32ChannelData: UnsafePointer<UnsafeMutablePointer<Int32>> { get } ``` |

Modified AVAudioPlayer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAudioPlayer.init(contentsOfURL: NSURL!, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfURL url: NSURL!, error outError: NSErrorPointer) ``` |
| To | ``` init!(contentsOfURL url: NSURL!, error outError: NSErrorPointer) ``` |

Modified AVAudioPlayer.init(contentsOfURL: NSURL!, fileTypeHint: String!, error: NSErrorPointer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(contentsOfURL url: NSURL!, fileTypeHint utiString: String!, error outError: NSErrorPointer) ``` | OS X 10.10 |
| To | ``` init!(contentsOfURL url: NSURL!, fileTypeHint utiString: String!, error outError: NSErrorPointer) ``` | OS X 10.9 |

Modified AVAudioPlayer.init(data: NSData!, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData!, error outError: NSErrorPointer) ``` |
| To | ``` init!(data data: NSData!, error outError: NSErrorPointer) ``` |

Modified AVAudioPlayer.init(data: NSData!, fileTypeHint: String!, error: NSErrorPointer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(data data: NSData!, fileTypeHint utiString: String!, error outError: NSErrorPointer) ``` | OS X 10.10 |
| To | ``` init!(data data: NSData!, fileTypeHint utiString: String!, error outError: NSErrorPointer) ``` | OS X 10.9 |

Modified AVAudioPlayer.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: AVAudioPlayerDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: AVAudioPlayerDelegate! ``` |

Modified AVAudioPlayer.deviceCurrentTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAudioPlayer.enableRate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVAudioPlayer.pan

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAudioPlayer.playAtTime(NSTimeInterval) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAudioPlayer.rate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVAudioPlayer.settings

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAudioPlayerDelegate.audioPlayerDecodeErrorDidOccur(AVAudioPlayer!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified AVAudioPlayerDelegate.audioPlayerDidFinishPlaying(AVAudioPlayer!, successfully: Bool)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified AVAudioPlayerNodeBufferOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVAudioPlayerNodeBufferOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var Loops: AVAudioPlayerNodeBufferOptions { get }     static var Interrupts: AVAudioPlayerNodeBufferOptions { get }     static var InterruptsAtLoop: AVAudioPlayerNodeBufferOptions { get } } ``` | RawOptionSet |
| To | ``` struct AVAudioPlayerNodeBufferOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Loops: AVAudioPlayerNodeBufferOptions { get }     static var Interrupts: AVAudioPlayerNodeBufferOptions { get }     static var InterruptsAtLoop: AVAudioPlayerNodeBufferOptions { get } } ``` | RawOptionSetType |

Modified AVAudioPlayerNodeBufferOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified AVAudioRecorder

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAudioRecorder.init(URL: NSURL!, settings:[NSObject: AnyObject]!, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(URL url: NSURL!, settings settings: [NSObject : AnyObject]!, error outError: NSErrorPointer) ``` |
| To | ``` init!(URL url: NSURL!, settings settings: [NSObject : AnyObject]!, error outError: NSErrorPointer) ``` |

Modified AVAudioRecorder.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: AVAudioRecorderDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: AVAudioRecorderDelegate! ``` |

Modified AVAudioRecorderDelegate.audioRecorderDidFinishRecording(AVAudioRecorder!, successfully: Bool)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified AVAudioRecorderDelegate.audioRecorderEncodeErrorDidOccur(AVAudioRecorder!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified AVAudioTime.init(audioTimeStamp: UnsafePointer<AudioTimeStamp>, sampleRate: Double)

|  | Declaration |
| --- | --- |
| From | ``` init(audioTimeStamp ts: ConstUnsafePointer<AudioTimeStamp>, sampleRate sampleRate: Double) ``` |
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

Modified AVAudioUnitComponentManager.componentsPassingTest(((AVAudioUnitComponent!, UnsafeMutablePointer<ObjCBool>) -> Bool)!) -> [AnyObject]!

|  | Declaration |
| --- | --- |
| From | ``` func componentsPassingTest(_ testHandler: ((AVAudioUnitComponent!, UnsafePointer<ObjCBool>) -> Bool)!) -> [AnyObject]! ``` |
| To | ``` func componentsPassingTest(_ testHandler: ((AVAudioUnitComponent!, UnsafeMutablePointer<ObjCBool>) -> Bool)!) -> [AnyObject]! ``` |

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

Modified AVCaptureAudioChannel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureAudioChannel.enabled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureAudioChannel.volume

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureAudioDataOutput

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureAudioDataOutput.audioSettings

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureAudioDataOutputSampleBufferDelegate.captureOutput(AVCaptureOutput!, didOutputSampleBuffer: CMSampleBuffer!, fromConnection: AVCaptureConnection!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified AVCaptureAudioFileOutput

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureAudioPreviewOutput

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureConnection

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureConnection.automaticallyAdjustsVideoMirroring

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureConnection.init(inputPort: AVCaptureInputPort!, videoPreviewLayer: AVCaptureVideoPreviewLayer!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(inputPort port: AVCaptureInputPort!, videoPreviewLayer layer: AVCaptureVideoPreviewLayer!) ``` | OS X 10.10 |
| To | ``` init!(inputPort port: AVCaptureInputPort!, videoPreviewLayer layer: AVCaptureVideoPreviewLayer!) ``` | OS X 10.7 |

Modified AVCaptureConnection.init(inputPorts: [AnyObject]!, output: AVCaptureOutput!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(inputPorts ports: [AnyObject]!, output output: AVCaptureOutput!) ``` | OS X 10.10 |
| To | ``` init!(inputPorts ports: [AnyObject]!, output output: AVCaptureOutput!) ``` | OS X 10.7 |

Modified AVCaptureConnection.supportsVideoFieldMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureConnection.supportsVideoMaxFrameDuration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVCaptureConnection.supportsVideoMinFrameDuration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureConnection.videoFieldMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureConnection.videoMaxFrameDuration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVCaptureConnection.videoMinFrameDuration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureConnection.videoPreviewLayer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureDevice

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureDevice.activeFormat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureDevice.activeInputSource

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureDevice.activeVideoMaxFrameDuration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVCaptureDevice.activeVideoMinFrameDuration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureDevice.formats

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureDevice.inUseByAnotherApplication

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureDevice.inputSources

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureDevice.linkedDevices

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureDevice.manufacturer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVCaptureDevice.setTransportControlsPlaybackMode(AVCaptureDeviceTransportControlsPlaybackMode, speed: AVCaptureDeviceTransportControlsSpeed)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureDevice.suspended

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureDevice.transportControlsPlaybackMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureDevice.transportControlsSpeed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureDevice.transportControlsSupported

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureDevice.transportType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureDevice.init(uniqueID: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(uniqueID deviceUniqueID: String!) -> AVCaptureDevice ``` |
| To | ``` init!(uniqueID deviceUniqueID: String!) -> AVCaptureDevice ``` |

Modified AVCaptureDeviceFormat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureDeviceInput

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureDeviceInput.init(device: AVCaptureDevice!, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(device device: AVCaptureDevice!, error outError: NSErrorPointer) ``` |
| To | ``` init!(device device: AVCaptureDevice!, error outError: NSErrorPointer) ``` |

Modified AVCaptureDeviceInputSource

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureDevicePosition [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureDeviceTransportControlsPlaybackMode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureExposureMode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureFileOutput

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureFileOutput.delegate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var delegate: AVCaptureFileOutputDelegate! ``` | OS X 10.10 |
| To | ``` unowned(unsafe) var delegate: AVCaptureFileOutputDelegate! ``` | OS X 10.7 |

Modified AVCaptureFileOutput.pauseRecording()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureFileOutput.recordingPaused

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureFileOutput.resumeRecording()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureFileOutputDelegate.captureOutput(AVCaptureFileOutput!, didOutputSampleBuffer: CMSampleBuffer!, fromConnection: AVCaptureConnection!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified AVCaptureFileOutputDelegate.captureOutputShouldProvideSampleAccurateRecordingStart(AVCaptureOutput!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVCaptureFileOutputRecordingDelegate.captureOutput(AVCaptureFileOutput!, didPauseRecordingToOutputFileAtURL: NSURL!, fromConnections:[AnyObject]!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified AVCaptureFileOutputRecordingDelegate.captureOutput(AVCaptureFileOutput!, didResumeRecordingToOutputFileAtURL: NSURL!, fromConnections:[AnyObject]!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified AVCaptureFileOutputRecordingDelegate.captureOutput(AVCaptureFileOutput!, didStartRecordingToOutputFileAtURL: NSURL!, fromConnections:[AnyObject]!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified AVCaptureFileOutputRecordingDelegate.captureOutput(AVCaptureFileOutput!, willFinishRecordingToOutputFileAtURL: NSURL!, fromConnections:[AnyObject]!, error: NSError!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified AVCaptureFlashMode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureFocusMode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureInput

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureInputPort

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureInputPort.clock

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVCaptureMetadataOutputObjectsDelegate.captureOutput(AVCaptureOutput!, didOutputMetadataObjects:[AnyObject]!, fromConnection: AVCaptureConnection!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified AVCaptureMovieFileOutput

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureMovieFileOutput.outputSettingsForConnection(AVCaptureConnection!) -> [NSObject: AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureMovieFileOutput.setOutputSettings([NSObject: AnyObject]!, forConnection: AVCaptureConnection!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureOutput

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureOutput.connectionWithMediaType(String!) -> AVCaptureConnection!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureScreenInput

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureScreenInput.capturesCursor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVCaptureScreenInput.init(displayID: CGDirectDisplayID)

|  | Declaration |
| --- | --- |
| From | ``` init(displayID displayID: CGDirectDisplayID) ``` |
| To | ``` init!(displayID displayID: CGDirectDisplayID) ``` |

Modified AVCaptureScreenInput.removesDuplicateFrames

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVCaptureSession

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureSession.addConnection(AVCaptureConnection!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureSession.addInputWithNoConnections(AVCaptureInput!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureSession.addOutputWithNoConnections(AVCaptureOutput!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureSession.canAddConnection(AVCaptureConnection!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureSession.masterClock

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVCaptureSession.removeConnection(AVCaptureConnection!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureStillImageOutput

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureStillImageOutput.capturingStillImage

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVCaptureTorchMode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureVideoDataOutput

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureVideoDataOutput.availableVideoCVPixelFormatTypes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureVideoDataOutput.availableVideoCodecTypes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureVideoDataOutputSampleBufferDelegate.captureOutput(AVCaptureOutput!, didDropSampleBuffer: CMSampleBuffer!, fromConnection: AVCaptureConnection!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified AVCaptureVideoDataOutputSampleBufferDelegate.captureOutput(AVCaptureOutput!, didOutputSampleBuffer: CMSampleBuffer!, fromConnection: AVCaptureConnection!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified AVCaptureVideoOrientation [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureVideoPreviewLayer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureVideoPreviewLayer.connection

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureVideoPreviewLayer.layerWithSessionWithNoConnection(AVCaptureSession!) -> AnyObject! [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureVideoPreviewLayer.init(session: AVCaptureSession!)

|  | Declaration |
| --- | --- |
| From | ``` init(session session: AVCaptureSession!) ``` |
| To | ``` init!(session session: AVCaptureSession!) ``` |

Modified AVCaptureVideoPreviewLayer.init(sessionWithNoConnection: AVCaptureSession!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(sessionWithNoConnection session: AVCaptureSession!) ``` | OS X 10.10 |
| To | ``` init!(sessionWithNoConnection session: AVCaptureSession!) ``` | OS X 10.7 |

Modified AVCaptureVideoPreviewLayer.setSessionWithNoConnection(AVCaptureSession!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCaptureWhiteBalanceMode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVComposition

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCompositionTrack

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVCompositionTrackSegment

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

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

Modified AVEdgeWidths [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AVEdgeWidths {     var left: CGFloat     var top: CGFloat     var right: CGFloat     var bottom: CGFloat } ``` |
| To | ``` struct AVEdgeWidths {     var left: CGFloat     var top: CGFloat     var right: CGFloat     var bottom: CGFloat     init()     init(left left: CGFloat, top top: CGFloat, right right: CGFloat, bottom bottom: CGFloat) } ``` |

Modified AVFragmentedMovieMinder.init(movie: AVFragmentedMovie!, mindingInterval: NSTimeInterval)

|  | Declaration |
| --- | --- |
| From | ``` init(movie movie: AVFragmentedMovie!, mindingInterval mindingInterval: NSTimeInterval) ``` |
| To | ``` init!(movie movie: AVFragmentedMovie!, mindingInterval mindingInterval: NSTimeInterval) ``` |

Modified AVFrameRateRange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

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
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVMediaSelectionGroup.mediaSelectionOptionsFromArray([AnyObject]!, filteredAndSortedAccordingToPreferredLanguages:[AnyObject]!) -> [AnyObject]! [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVMediaSelectionOption

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVMediaSelectionOption.displayName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVMediaSelectionOption.displayNameWithLocale(NSLocale!) -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVMediaSelectionOption.extendedLanguageTag

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVMetadataItem

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVMetadataItem.duration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVMetadataItem.key

|  | Declaration |
| --- | --- |
| From | ``` var key: protocol<NSCopying, NSObjectProtocol>! { get } ``` |
| To | ``` @NSCopying var key: protocol<NSCopying, NSObjectProtocol>! { get } ``` |

Modified AVMetadataItem.loadValuesAsynchronouslyForKeys([AnyObject]!, completionHandler:(() -> Void)!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVMetadataItem.locale

|  | Declaration |
| --- | --- |
| From | ``` var locale: NSLocale! { get } ``` |
| To | ``` @NSCopying var locale: NSLocale! { get } ``` |

Modified AVMetadataItem.metadataItemsFromArray([AnyObject]!, filteredAndSortedAccordingToPreferredLanguages:[AnyObject]!) -> [AnyObject]! [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVMetadataItem.metadataItemsFromArray([AnyObject]!, filteredByMetadataItemFilter: AVMetadataItemFilter!) -> [AnyObject]! [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVMetadataItem.statusOfValueForKey(String!, error: NSErrorPointer) -> AVKeyValueStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVMetadataItem.value

|  | Declaration |
| --- | --- |
| From | ``` var value: protocol<NSCopying, NSObjectProtocol>! { get } ``` |
| To | ``` @NSCopying var value: protocol<NSCopying, NSObjectProtocol>! { get } ``` |

Modified AVMetadataItemFilter

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVMovie.init(URL: NSURL!, options:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(URL URL: NSURL!, options options: [NSObject : AnyObject]!) ``` |
| To | ``` init!(URL URL: NSURL!, options options: [NSObject : AnyObject]!) ``` |

Modified AVMutableAudioMix

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVMutableAudioMixInputParameters

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVMutableAudioMixInputParameters.audioTapProcessor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVMutableAudioMixInputParameters.init(track: AVAssetTrack!)

|  | Declaration |
| --- | --- |
| From | ``` init(track track: AVAssetTrack!) -> AVMutableAudioMixInputParameters ``` |
| To | ``` init!(track track: AVAssetTrack!) -> AVMutableAudioMixInputParameters ``` |

Modified AVMutableComposition

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVMutableCompositionTrack

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVMutableCompositionTrack.insertTimeRanges([AnyObject]!, ofTracks:[AnyObject]!, atTime: CMTime, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVMutableMetadataItem

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVMutableMetadataItem.duration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVMutableMetadataItem.key

|  | Declaration |
| --- | --- |
| From | ``` var key: protocol<NSCopying, NSObjectProtocol>! ``` |
| To | ``` @NSCopying var key: protocol<NSCopying, NSObjectProtocol>! ``` |

Modified AVMutableMetadataItem.locale

|  | Declaration |
| --- | --- |
| From | ``` var locale: NSLocale! ``` |
| To | ``` @NSCopying var locale: NSLocale! ``` |

Modified AVMutableMetadataItem.value

|  | Declaration |
| --- | --- |
| From | ``` var value: protocol<NSCopying, NSObjectProtocol>! ``` |
| To | ``` @NSCopying var value: protocol<NSCopying, NSObjectProtocol>! ``` |

Modified AVMutableTimedMetadataGroup

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVMutableVideoComposition

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVMutableVideoComposition.customVideoCompositorClass

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVMutableVideoComposition.init(propertiesOfAsset: AVAsset!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(propertiesOfAsset asset: AVAsset!) -> AVMutableVideoComposition ``` | OS X 10.10 |
| To | ``` init!(propertiesOfAsset asset: AVAsset!) -> AVMutableVideoComposition ``` | OS X 10.9 |

Modified AVMutableVideoCompositionInstruction

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVMutableVideoCompositionLayerInstruction

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVMutableVideoCompositionLayerInstruction.init(assetTrack: AVAssetTrack!)

|  | Declaration |
| --- | --- |
| From | ``` init(assetTrack track: AVAssetTrack!) -> AVMutableVideoCompositionLayerInstruction ``` |
| To | ``` init!(assetTrack track: AVAssetTrack!) -> AVMutableVideoCompositionLayerInstruction ``` |

Modified AVMutableVideoCompositionLayerInstruction.setCropRectangle(CGRect, atTime: CMTime)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVMutableVideoCompositionLayerInstruction.setCropRectangleRampFromStartCropRectangle(CGRect, toEndCropRectangle: CGRect, timeRange: CMTimeRange)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVOutputSettingsAssistant

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVOutputSettingsAssistant.init(preset: String!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(preset presetIdentifier: String!) ``` |
| To | ``` convenience init!(preset presetIdentifier: String!) ``` |

Modified AVPixelAspectRatio [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AVPixelAspectRatio {     var horizontalSpacing: Int     var verticalSpacing: Int } ``` |
| To | ``` struct AVPixelAspectRatio {     var horizontalSpacing: Int     var verticalSpacing: Int     init()     init(horizontalSpacing horizontalSpacing: Int, verticalSpacing verticalSpacing: Int) } ``` |

Modified AVPlayer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayer.init(URL: NSURL!)

|  | Declaration |
| --- | --- |
| From | ``` init(URL URL: NSURL!) ``` |
| To | ``` init!(URL URL: NSURL!) ``` |

Modified AVPlayer.appliesMediaSelectionCriteriaAutomatically

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayer.audioOutputDeviceUniqueID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayer.cancelPendingPrerolls()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVPlayer.masterClock

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVPlayer.mediaSelectionCriteriaForMediaCharacteristic(String!) -> AVPlayerMediaSelectionCriteria!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayer.muted

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayer.init(playerItem: AVPlayerItem!)

|  | Declaration |
| --- | --- |
| From | ``` init(playerItem item: AVPlayerItem!) ``` |
| To | ``` init!(playerItem item: AVPlayerItem!) ``` |

Modified AVPlayer.prerollAtRate(Float, completionHandler:((Bool) -> Void)!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVPlayer.seekToDate(NSDate!, completionHandler:((Bool) -> Void)!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayer.seekToTime(CMTime, completionHandler:((Bool) -> Void)!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayer.seekToTime(CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler:((Bool) -> Void)!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayer.setMediaSelectionCriteria(AVPlayerMediaSelectionCriteria!, forMediaCharacteristic: String!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayer.setRate(Float, time: CMTime, atHostTime: CMTime)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVPlayer.volume

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayerItem

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayerItem.init(URL: NSURL!)

|  | Declaration |
| --- | --- |
| From | ``` init(URL URL: NSURL!) ``` |
| To | ``` init!(URL URL: NSURL!) ``` |

Modified AVPlayerItem.accessLog() -> AVPlayerItemAccessLog!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayerItem.addOutput(AVPlayerItemOutput!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVPlayerItem.applicationAuthorizedForPlayback

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayerItem.init(asset: AVAsset!)

|  | Declaration |
| --- | --- |
| From | ``` init(asset asset: AVAsset!) ``` |
| To | ``` init!(asset asset: AVAsset!) ``` |

Modified AVPlayerItem.init(asset: AVAsset!, automaticallyLoadedAssetKeys:[AnyObject]!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(asset asset: AVAsset!, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [AnyObject]!) ``` | OS X 10.10 |
| To | ``` init!(asset asset: AVAsset!, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [AnyObject]!) ``` | OS X 10.9 |

Modified AVPlayerItem.audioMix

|  | Declaration |
| --- | --- |
| From | ``` var audioMix: AVAudioMix! ``` |
| To | ``` @NSCopying var audioMix: AVAudioMix! ``` |

Modified AVPlayerItem.audioTimePitchAlgorithm

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayerItem.authorizationRequiredForPlayback

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayerItem.automaticallyLoadedAssetKeys

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayerItem.canPlayFastForward

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVPlayerItem.canPlayFastReverse

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVPlayerItem.canPlayReverse

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVPlayerItem.canPlaySlowForward

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVPlayerItem.canPlaySlowReverse

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVPlayerItem.canStepBackward

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVPlayerItem.canStepForward

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVPlayerItem.cancelContentAuthorizationRequest()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayerItem.cancelPendingSeeks()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayerItem.contentAuthorizationRequestStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayerItem.contentAuthorizedForPlayback

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayerItem.customVideoCompositor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayerItem.duration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayerItem.errorLog() -> AVPlayerItemErrorLog!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayerItem.outputs

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVPlayerItem.removeOutput(AVPlayerItemOutput!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVPlayerItem.requestContentAuthorizationAsynchronouslyWithTimeoutInterval(NSTimeInterval, completionHandler:(() -> Void)!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayerItem.seekToDate(NSDate!, completionHandler:((Bool) -> Void)!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayerItem.seekToTime(CMTime, completionHandler:((Bool) -> Void)!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayerItem.seekToTime(CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler:((Bool) -> Void)!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayerItem.seekingWaitsForVideoCompositionRendering

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayerItem.selectMediaOption(AVMediaSelectionOption!, inMediaSelectionGroup: AVMediaSelectionGroup!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVPlayerItem.selectMediaOptionAutomaticallyInMediaSelectionGroup(AVMediaSelectionGroup!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayerItem.selectedMediaOptionInMediaSelectionGroup(AVMediaSelectionGroup!) -> AVMediaSelectionOption!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVPlayerItem.textStyleRules

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayerItem.timebase

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVPlayerItem.videoComposition

|  | Declaration |
| --- | --- |
| From | ``` var videoComposition: AVVideoComposition! ``` |
| To | ``` @NSCopying var videoComposition: AVVideoComposition! ``` |

Modified AVPlayerItemAccessLog

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayerItemAccessLogEvent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayerItemAccessLogEvent.downloadOverdue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayerItemAccessLogEvent.mediaRequestsWWAN

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayerItemAccessLogEvent.numberOfMediaRequests

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayerItemAccessLogEvent.observedBitrateStandardDeviation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayerItemAccessLogEvent.observedMaxBitrate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayerItemAccessLogEvent.observedMinBitrate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayerItemAccessLogEvent.playbackType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayerItemAccessLogEvent.startupTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayerItemAccessLogEvent.switchBitrate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayerItemAccessLogEvent.transferDuration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayerItemErrorLog

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayerItemErrorLogEvent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayerItemLegibleOutput

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayerItemLegibleOutput.init(mediaSubtypesForNativeRepresentation: [AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(mediaSubtypesForNativeRepresentation subtypes: [AnyObject]!) ``` |
| To | ``` init!(mediaSubtypesForNativeRepresentation subtypes: [AnyObject]!) ``` |

Modified AVPlayerItemLegibleOutputPushDelegate.legibleOutput(AVPlayerItemLegibleOutput!, didOutputAttributedStrings:[AnyObject]!, nativeSampleBuffers:[AnyObject]!, forItemTime: CMTime)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | yes |

Modified AVPlayerItemMetadataOutput.init(identifiers: [AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(identifiers identifiers: [AnyObject]!) ``` |
| To | ``` init!(identifiers identifiers: [AnyObject]!) ``` |

Modified AVPlayerItemMetadataOutputPushDelegate.metadataOutput(AVPlayerItemMetadataOutput!, didOutputTimedMetadataGroups:[AnyObject]!, fromPlayerItemTrack: AVPlayerItemTrack!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified AVPlayerItemOutput

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVPlayerItemOutput.itemTimeForCVTimeStamp(CVTimeStamp) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVPlayerItemOutput.suppressesPlayerRendering

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVPlayerItemOutputPullDelegate.outputMediaDataWillChange(AVPlayerItemOutput!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | yes |

Modified AVPlayerItemOutputPullDelegate.outputSequenceWasFlushed(AVPlayerItemOutput!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | yes |

Modified AVPlayerItemOutputPushDelegate.outputSequenceWasFlushed(AVPlayerItemOutput!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified AVPlayerItemTrack

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayerItemTrack.currentVideoFrameRate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayerItemVideoOutput

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVPlayerItemVideoOutput.copyPixelBufferForItemTime(CMTime, itemTimeForDisplay: UnsafeMutablePointer<CMTime>) -> CVPixelBuffer!

|  | Declaration |
| --- | --- |
| From | ``` func copyPixelBufferForItemTime(_ itemTime: CMTime, itemTimeForDisplay outItemTimeForDisplay: UnsafePointer<CMTime>) -> CVPixelBuffer! ``` |
| To | ``` func copyPixelBufferForItemTime(_ itemTime: CMTime, itemTimeForDisplay outItemTimeForDisplay: UnsafeMutablePointer<CMTime>) -> CVPixelBuffer! ``` |

Modified AVPlayerItemVideoOutput.init(pixelBufferAttributes: [NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(pixelBufferAttributes pixelBufferAttributes: [NSObject : AnyObject]!) ``` |
| To | ``` init!(pixelBufferAttributes pixelBufferAttributes: [NSObject : AnyObject]!) ``` |

Modified AVPlayerLayer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVPlayerLayer.init(player: AVPlayer!)

|  | Declaration |
| --- | --- |
| From | ``` init(player player: AVPlayer!) -> AVPlayerLayer ``` |
| To | ``` init!(player player: AVPlayer!) -> AVPlayerLayer ``` |

Modified AVPlayerLayer.videoRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayerMediaSelectionCriteria

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVPlayerMediaSelectionCriteria.init(preferredLanguages: [AnyObject]!, preferredMediaCharacteristics:[AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(preferredLanguages preferredLanguages: [AnyObject]!, preferredMediaCharacteristics preferredMediaCharacteristics: [AnyObject]!) ``` |
| To | ``` init!(preferredLanguages preferredLanguages: [AnyObject]!, preferredMediaCharacteristics preferredMediaCharacteristics: [AnyObject]!) ``` |

Modified AVQueuePlayer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVQueuePlayer.init(items: [AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(items items: [AnyObject]!) ``` |
| To | ``` init!(items items: [AnyObject]!) ``` |

Modified AVSampleBufferDisplayLayer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVSampleBufferGenerator.init(asset: AVAsset!, timebase: CMTimebase!)

|  | Declaration |
| --- | --- |
| From | ``` init(asset asset: AVAsset!, timebase timebase: CMTimebase!) ``` |
| To | ``` init!(asset asset: AVAsset!, timebase timebase: CMTimebase!) ``` |

Modified AVSampleBufferRequest.init(startCursor: AVSampleCursor!)

|  | Declaration |
| --- | --- |
| From | ``` init(startCursor startCursor: AVSampleCursor!) ``` |
| To | ``` init!(startCursor startCursor: AVSampleCursor!) ``` |

Modified AVSampleCursor.stepByDecodeTime(CMTime, wasPinned: UnsafeMutablePointer<ObjCBool>) -> CMTime

|  | Declaration |
| --- | --- |
| From | ``` func stepByDecodeTime(_ deltaDecodeTime: CMTime, wasPinned outWasPinned: UnsafePointer<ObjCBool>) -> CMTime ``` |
| To | ``` func stepByDecodeTime(_ deltaDecodeTime: CMTime, wasPinned outWasPinned: UnsafeMutablePointer<ObjCBool>) -> CMTime ``` |

Modified AVSampleCursor.stepByPresentationTime(CMTime, wasPinned: UnsafeMutablePointer<ObjCBool>) -> CMTime

|  | Declaration |
| --- | --- |
| From | ``` func stepByPresentationTime(_ deltaPresentationTime: CMTime, wasPinned outWasPinned: UnsafePointer<ObjCBool>) -> CMTime ``` |
| To | ``` func stepByPresentationTime(_ deltaPresentationTime: CMTime, wasPinned outWasPinned: UnsafeMutablePointer<ObjCBool>) -> CMTime ``` |

Modified AVSampleCursorChunkInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AVSampleCursorChunkInfo {     var chunkSampleCount: Int64     var chunkHasUniformSampleSizes: ObjCBool     var chunkHasUniformSampleDurations: ObjCBool     var chunkHasUniformFormatDescriptions: ObjCBool } ``` |
| To | ``` struct AVSampleCursorChunkInfo {     var chunkSampleCount: Int64     var chunkHasUniformSampleSizes: ObjCBool     var chunkHasUniformSampleDurations: ObjCBool     var chunkHasUniformFormatDescriptions: ObjCBool     init()     init(chunkSampleCount chunkSampleCount: Int64, chunkHasUniformSampleSizes chunkHasUniformSampleSizes: ObjCBool, chunkHasUniformSampleDurations chunkHasUniformSampleDurations: ObjCBool, chunkHasUniformFormatDescriptions chunkHasUniformFormatDescriptions: ObjCBool) } ``` |

Modified AVSampleCursorDependencyInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AVSampleCursorDependencyInfo {     var sampleIndicatesWhetherItHasDependentSamples: ObjCBool     var sampleHasDependentSamples: ObjCBool     var sampleIndicatesWhetherItDependsOnOthers: ObjCBool     var sampleDependsOnOthers: ObjCBool     var sampleIndicatesWhetherItHasRedundantCoding: ObjCBool     var sampleHasRedundantCoding: ObjCBool } ``` |
| To | ``` struct AVSampleCursorDependencyInfo {     var sampleIndicatesWhetherItHasDependentSamples: ObjCBool     var sampleHasDependentSamples: ObjCBool     var sampleIndicatesWhetherItDependsOnOthers: ObjCBool     var sampleDependsOnOthers: ObjCBool     var sampleIndicatesWhetherItHasRedundantCoding: ObjCBool     var sampleHasRedundantCoding: ObjCBool     init()     init(sampleIndicatesWhetherItHasDependentSamples sampleIndicatesWhetherItHasDependentSamples: ObjCBool, sampleHasDependentSamples sampleHasDependentSamples: ObjCBool, sampleIndicatesWhetherItDependsOnOthers sampleIndicatesWhetherItDependsOnOthers: ObjCBool, sampleDependsOnOthers sampleDependsOnOthers: ObjCBool, sampleIndicatesWhetherItHasRedundantCoding sampleIndicatesWhetherItHasRedundantCoding: ObjCBool, sampleHasRedundantCoding sampleHasRedundantCoding: ObjCBool) } ``` |

Modified AVSampleCursorStorageRange [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AVSampleCursorStorageRange {     var offset: Int64     var length: Int64 } ``` |
| To | ``` struct AVSampleCursorStorageRange {     var offset: Int64     var length: Int64     init()     init(offset offset: Int64, length length: Int64) } ``` |

Modified AVSampleCursorSyncInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AVSampleCursorSyncInfo {     var sampleIsFullSync: ObjCBool     var sampleIsPartialSync: ObjCBool     var sampleIsDroppable: ObjCBool } ``` |
| To | ``` struct AVSampleCursorSyncInfo {     var sampleIsFullSync: ObjCBool     var sampleIsPartialSync: ObjCBool     var sampleIsDroppable: ObjCBool     init()     init(sampleIsFullSync sampleIsFullSync: ObjCBool, sampleIsPartialSync sampleIsPartialSync: ObjCBool, sampleIsDroppable sampleIsDroppable: ObjCBool) } ``` |

Modified AVSynchronizedLayer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVSynchronizedLayer.init(playerItem: AVPlayerItem!)

|  | Declaration |
| --- | --- |
| From | ``` init(playerItem playerItem: AVPlayerItem!) -> AVSynchronizedLayer ``` |
| To | ``` init!(playerItem playerItem: AVPlayerItem!) -> AVSynchronizedLayer ``` |

Modified AVTextStyleRule

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

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
| From | OS X 10.10 |
| To | OS X 10.7 |

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
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVURLAsset.URL

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL! { get } ``` |
| To | ``` @NSCopying var URL: NSURL! { get } ``` |

Modified AVURLAsset.init(URL: NSURL!, options:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(URL URL: NSURL!, options options: [NSObject : AnyObject]!) ``` |
| To | ``` init!(URL URL: NSURL!, options options: [NSObject : AnyObject]!) ``` |

Modified AVURLAsset.audiovisualMIMETypes() -> [AnyObject]! [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVURLAsset.audiovisualTypes() -> [AnyObject]! [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVURLAsset.isPlayableExtendedMIMEType(String!) -> Bool [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVURLAsset.resourceLoader

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVVideoCompositing

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVVideoCompositing.cancelAllPendingVideoCompositionRequests()

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified AVVideoComposition

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVVideoComposition.customVideoCompositorClass

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVVideoComposition.isValidForAsset(AVAsset!, timeRange: CMTimeRange, validationDelegate: AVVideoCompositionValidationHandling!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified AVVideoComposition.init(propertiesOfAsset: AVAsset!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(propertiesOfAsset asset: AVAsset!) -> AVVideoComposition ``` | OS X 10.10 |
| To | ``` init!(propertiesOfAsset asset: AVAsset!) -> AVVideoComposition ``` | OS X 10.9 |

Modified AVVideoCompositionCoreAnimationTool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

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

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(postProcessingAsVideoLayers videoLayers: [AnyObject]!, inLayer animationLayer: CALayer!) -> AVVideoCompositionCoreAnimationTool ``` | OS X 10.10 |
| To | ``` init!(postProcessingAsVideoLayers videoLayers: [AnyObject]!, inLayer animationLayer: CALayer!) -> AVVideoCompositionCoreAnimationTool ``` | OS X 10.9 |

Modified AVVideoCompositionInstruction

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVVideoCompositionInstruction.passthroughTrackID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVVideoCompositionInstruction.requiredSourceTrackIDs

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVVideoCompositionInstructionProtocol

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVVideoCompositionLayerInstruction

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVVideoCompositionLayerInstruction.getCropRectangleRampForTime(CMTime, startCropRectangle: UnsafeMutablePointer<CGRect>, endCropRectangle: UnsafeMutablePointer<CGRect>, timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func getCropRectangleRampForTime(_ time: CMTime, startCropRectangle startCropRectangle: UnsafePointer<CGRect>, endCropRectangle endCropRectangle: UnsafePointer<CGRect>, timeRange timeRange: UnsafePointer<CMTimeRange>) -> Bool ``` | OS X 10.10 |
| To | ``` func getCropRectangleRampForTime(_ time: CMTime, startCropRectangle startCropRectangle: UnsafeMutablePointer<CGRect>, endCropRectangle endCropRectangle: UnsafeMutablePointer<CGRect>, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool ``` | OS X 10.9 |

Modified AVVideoCompositionLayerInstruction.getOpacityRampForTime(CMTime, startOpacity: UnsafeMutablePointer<Float>, endOpacity: UnsafeMutablePointer<Float>, timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func getOpacityRampForTime(_ time: CMTime, startOpacity startOpacity: UnsafePointer<Float>, endOpacity endOpacity: UnsafePointer<Float>, timeRange timeRange: UnsafePointer<CMTimeRange>) -> Bool ``` |
| To | ``` func getOpacityRampForTime(_ time: CMTime, startOpacity startOpacity: UnsafeMutablePointer<Float>, endOpacity endOpacity: UnsafeMutablePointer<Float>, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool ``` |

Modified AVVideoCompositionLayerInstruction.getTransformRampForTime(CMTime, startTransform: UnsafeMutablePointer<CGAffineTransform>, endTransform: UnsafeMutablePointer<CGAffineTransform>, timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func getTransformRampForTime(_ time: CMTime, startTransform startTransform: UnsafePointer<CGAffineTransform>, endTransform endTransform: UnsafePointer<CGAffineTransform>, timeRange timeRange: UnsafePointer<CMTimeRange>) -> Bool ``` |
| To | ``` func getTransformRampForTime(_ time: CMTime, startTransform startTransform: UnsafeMutablePointer<CGAffineTransform>, endTransform endTransform: UnsafeMutablePointer<CGAffineTransform>, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool ``` |

Modified AVVideoCompositionRenderContext

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AVVideoCompositionValidationHandling.videoComposition(AVVideoComposition!, shouldContinueValidatingAfterFindingEmptyTimeRange: CMTimeRange) -> Bool

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | yes |

Modified AVVideoCompositionValidationHandling.videoComposition(AVVideoComposition!, shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction: AVVideoCompositionInstructionProtocol!) -> Bool

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | yes |

Modified AVVideoCompositionValidationHandling.videoComposition(AVVideoComposition!, shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction: AVVideoCompositionInstructionProtocol!, layerInstruction: AVVideoCompositionLayerInstruction!, asset: AVAsset!) -> Bool

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | yes |

Modified AVVideoCompositionValidationHandling.videoComposition(AVVideoComposition!, shouldContinueValidatingAfterFindingInvalidValueForKey: String!) -> Bool

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | yes |

Modified AVVideoFieldMode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVAssetExportPreset1280x720

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAssetExportPreset1280x720: NSString! ``` | OS X 10.10 |
| To | ``` let AVAssetExportPreset1280x720: String ``` | OS X 10.7 |

Modified AVAssetExportPreset1920x1080

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAssetExportPreset1920x1080: NSString! ``` | OS X 10.10 |
| To | ``` let AVAssetExportPreset1920x1080: String ``` | OS X 10.7 |

Modified AVAssetExportPreset3840x2160

|  | Declaration |
| --- | --- |
| From | ``` let AVAssetExportPreset3840x2160: NSString! ``` |
| To | ``` let AVAssetExportPreset3840x2160: String ``` |

Modified AVAssetExportPreset640x480

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAssetExportPreset640x480: NSString! ``` | OS X 10.10 |
| To | ``` let AVAssetExportPreset640x480: String ``` | OS X 10.7 |

Modified AVAssetExportPreset960x540

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAssetExportPreset960x540: NSString! ``` | OS X 10.10 |
| To | ``` let AVAssetExportPreset960x540: String ``` | OS X 10.7 |

Modified AVAssetExportPresetAppleM4A

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAssetExportPresetAppleM4A: NSString! ``` | OS X 10.10 |
| To | ``` let AVAssetExportPresetAppleM4A: String ``` | OS X 10.7 |

Modified AVAssetExportPresetAppleM4V1080pHD

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAssetExportPresetAppleM4V1080pHD: NSString! ``` | OS X 10.10 |
| To | ``` let AVAssetExportPresetAppleM4V1080pHD: String ``` | OS X 10.8 |

Modified AVAssetExportPresetAppleM4V480pSD

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAssetExportPresetAppleM4V480pSD: NSString! ``` | OS X 10.10 |
| To | ``` let AVAssetExportPresetAppleM4V480pSD: String ``` | OS X 10.7 |

Modified AVAssetExportPresetAppleM4V720pHD

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAssetExportPresetAppleM4V720pHD: NSString! ``` | OS X 10.10 |
| To | ``` let AVAssetExportPresetAppleM4V720pHD: String ``` | OS X 10.7 |

Modified AVAssetExportPresetAppleM4VAppleTV

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAssetExportPresetAppleM4VAppleTV: NSString! ``` | OS X 10.10 |
| To | ``` let AVAssetExportPresetAppleM4VAppleTV: String ``` | OS X 10.7 |

Modified AVAssetExportPresetAppleM4VCellular

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAssetExportPresetAppleM4VCellular: NSString! ``` | OS X 10.10 |
| To | ``` let AVAssetExportPresetAppleM4VCellular: String ``` | OS X 10.7 |

Modified AVAssetExportPresetAppleM4VWiFi

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAssetExportPresetAppleM4VWiFi: NSString! ``` | OS X 10.10 |
| To | ``` let AVAssetExportPresetAppleM4VWiFi: String ``` | OS X 10.7 |

Modified AVAssetExportPresetAppleM4ViPod

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAssetExportPresetAppleM4ViPod: NSString! ``` | OS X 10.10 |
| To | ``` let AVAssetExportPresetAppleM4ViPod: String ``` | OS X 10.7 |

Modified AVAssetExportPresetAppleProRes422LPCM

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAssetExportPresetAppleProRes422LPCM: NSString! ``` | OS X 10.10 |
| To | ``` let AVAssetExportPresetAppleProRes422LPCM: String ``` | OS X 10.7 |

Modified AVAssetExportPresetPassthrough

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAssetExportPresetPassthrough: NSString! ``` | OS X 10.10 |
| To | ``` let AVAssetExportPresetPassthrough: String ``` | OS X 10.7 |

Modified AVAssetImageGeneratorApertureModeCleanAperture

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAssetImageGeneratorApertureModeCleanAperture: NSString! ``` | OS X 10.10 |
| To | ``` let AVAssetImageGeneratorApertureModeCleanAperture: String ``` | OS X 10.7 |

Modified AVAssetImageGeneratorApertureModeEncodedPixels

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAssetImageGeneratorApertureModeEncodedPixels: NSString! ``` | OS X 10.10 |
| To | ``` let AVAssetImageGeneratorApertureModeEncodedPixels: String ``` | OS X 10.7 |

Modified AVAssetImageGeneratorApertureModeProductionAperture

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAssetImageGeneratorApertureModeProductionAperture: NSString! ``` | OS X 10.10 |
| To | ``` let AVAssetImageGeneratorApertureModeProductionAperture: String ``` | OS X 10.7 |

Modified AVAudioBitRateStrategy_Constant

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAudioBitRateStrategy_Constant: NSString! ``` | OS X 10.10 |
| To | ``` let AVAudioBitRateStrategy_Constant: String ``` | OS X 10.9 |

Modified AVAudioBitRateStrategy_LongTermAverage

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAudioBitRateStrategy_LongTermAverage: NSString! ``` | OS X 10.10 |
| To | ``` let AVAudioBitRateStrategy_LongTermAverage: String ``` | OS X 10.9 |

Modified AVAudioBitRateStrategy_Variable

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAudioBitRateStrategy_Variable: NSString! ``` | OS X 10.10 |
| To | ``` let AVAudioBitRateStrategy_Variable: String ``` | OS X 10.9 |

Modified AVAudioBitRateStrategy_VariableConstrained

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAudioBitRateStrategy_VariableConstrained: NSString! ``` | OS X 10.10 |
| To | ``` let AVAudioBitRateStrategy_VariableConstrained: String ``` | OS X 10.9 |

Modified AVAudioEngineConfigurationChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioEngineConfigurationChangeNotification: NSString! ``` |
| To | ``` let AVAudioEngineConfigurationChangeNotification: String ``` |

Modified AVAudioTimePitchAlgorithmSpectral

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAudioTimePitchAlgorithmSpectral: NSString! ``` | OS X 10.10 |
| To | ``` let AVAudioTimePitchAlgorithmSpectral: String ``` | OS X 10.9 |

Modified AVAudioTimePitchAlgorithmTimeDomain

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAudioTimePitchAlgorithmTimeDomain: NSString! ``` | OS X 10.10 |
| To | ``` let AVAudioTimePitchAlgorithmTimeDomain: String ``` | OS X 10.9 |

Modified AVAudioTimePitchAlgorithmVarispeed

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVAudioTimePitchAlgorithmVarispeed: NSString! ``` | OS X 10.10 |
| To | ``` let AVAudioTimePitchAlgorithmVarispeed: String ``` | OS X 10.9 |

Modified AVAudioUnitComponentTagsDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioUnitComponentTagsDidChangeNotification: NSString! ``` |
| To | ``` let AVAudioUnitComponentTagsDidChangeNotification: String ``` |

Modified AVAudioUnitManufacturerNameApple

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioUnitManufacturerNameApple: NSString! ``` |
| To | ``` let AVAudioUnitManufacturerNameApple: String ``` |

Modified AVAudioUnitTypeEffect

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioUnitTypeEffect: NSString! ``` |
| To | ``` let AVAudioUnitTypeEffect: String ``` |

Modified AVAudioUnitTypeFormatConverter

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioUnitTypeFormatConverter: NSString! ``` |
| To | ``` let AVAudioUnitTypeFormatConverter: String ``` |

Modified AVAudioUnitTypeGenerator

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioUnitTypeGenerator: NSString! ``` |
| To | ``` let AVAudioUnitTypeGenerator: String ``` |

Modified AVAudioUnitTypeMIDIProcessor

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioUnitTypeMIDIProcessor: NSString! ``` |
| To | ``` let AVAudioUnitTypeMIDIProcessor: String ``` |

Modified AVAudioUnitTypeMixer

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioUnitTypeMixer: NSString! ``` |
| To | ``` let AVAudioUnitTypeMixer: String ``` |

Modified AVAudioUnitTypeMusicDevice

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioUnitTypeMusicDevice: NSString! ``` |
| To | ``` let AVAudioUnitTypeMusicDevice: String ``` |

Modified AVAudioUnitTypeMusicEffect

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioUnitTypeMusicEffect: NSString! ``` |
| To | ``` let AVAudioUnitTypeMusicEffect: String ``` |

Modified AVAudioUnitTypeOfflineEffect

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioUnitTypeOfflineEffect: NSString! ``` |
| To | ``` let AVAudioUnitTypeOfflineEffect: String ``` |

Modified AVAudioUnitTypeOutput

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioUnitTypeOutput: NSString! ``` |
| To | ``` let AVAudioUnitTypeOutput: String ``` |

Modified AVAudioUnitTypePanner

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioUnitTypePanner: NSString! ``` |
| To | ``` let AVAudioUnitTypePanner: String ``` |

Modified AVCaptureDeviceWasConnectedNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVCaptureDeviceWasConnectedNotification: NSString! ``` | OS X 10.10 |
| To | ``` let AVCaptureDeviceWasConnectedNotification: String ``` | OS X 10.7 |

Modified AVCaptureDeviceWasDisconnectedNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVCaptureDeviceWasDisconnectedNotification: NSString! ``` | OS X 10.10 |
| To | ``` let AVCaptureDeviceWasDisconnectedNotification: String ``` | OS X 10.7 |

Modified AVCaptureInputPortFormatDescriptionDidChangeNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVCaptureInputPortFormatDescriptionDidChangeNotification: NSString! ``` | OS X 10.10 |
| To | ``` let AVCaptureInputPortFormatDescriptionDidChangeNotification: String ``` | OS X 10.7 |

Modified AVCaptureSessionDidStartRunningNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVCaptureSessionDidStartRunningNotification: NSString! ``` | OS X 10.10 |
| To | ``` let AVCaptureSessionDidStartRunningNotification: String ``` | OS X 10.7 |

Modified AVCaptureSessionDidStopRunningNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVCaptureSessionDidStopRunningNotification: NSString! ``` | OS X 10.10 |
| To | ``` let AVCaptureSessionDidStopRunningNotification: String ``` | OS X 10.7 |

Modified AVCaptureSessionErrorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVCaptureSessionErrorKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVCaptureSessionErrorKey: String ``` | OS X 10.7 |

Modified AVCaptureSessionPreset1280x720

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVCaptureSessionPreset1280x720: NSString! ``` | OS X 10.10 |
| To | ``` let AVCaptureSessionPreset1280x720: String ``` | OS X 10.7 |

Modified AVCaptureSessionPreset320x240

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVCaptureSessionPreset320x240: NSString! ``` | OS X 10.10 |
| To | ``` let AVCaptureSessionPreset320x240: String ``` | OS X 10.7 |

Modified AVCaptureSessionPreset352x288

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVCaptureSessionPreset352x288: NSString! ``` | OS X 10.10 |
| To | ``` let AVCaptureSessionPreset352x288: String ``` | OS X 10.7 |

Modified AVCaptureSessionPreset640x480

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVCaptureSessionPreset640x480: NSString! ``` | OS X 10.10 |
| To | ``` let AVCaptureSessionPreset640x480: String ``` | OS X 10.7 |

Modified AVCaptureSessionPreset960x540

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVCaptureSessionPreset960x540: NSString! ``` | OS X 10.10 |
| To | ``` let AVCaptureSessionPreset960x540: String ``` | OS X 10.7 |

Modified AVCaptureSessionPresetHigh

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVCaptureSessionPresetHigh: NSString! ``` | OS X 10.10 |
| To | ``` let AVCaptureSessionPresetHigh: String ``` | OS X 10.7 |

Modified AVCaptureSessionPresetLow

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVCaptureSessionPresetLow: NSString! ``` | OS X 10.10 |
| To | ``` let AVCaptureSessionPresetLow: String ``` | OS X 10.7 |

Modified AVCaptureSessionPresetMedium

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVCaptureSessionPresetMedium: NSString! ``` | OS X 10.10 |
| To | ``` let AVCaptureSessionPresetMedium: String ``` | OS X 10.7 |

Modified AVCaptureSessionPresetPhoto

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVCaptureSessionPresetPhoto: NSString! ``` | OS X 10.10 |
| To | ``` let AVCaptureSessionPresetPhoto: String ``` | OS X 10.7 |

Modified AVCaptureSessionPresetiFrame1280x720

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVCaptureSessionPresetiFrame1280x720: NSString! ``` | OS X 10.10 |
| To | ``` let AVCaptureSessionPresetiFrame1280x720: String ``` | OS X 10.9 |

Modified AVCaptureSessionPresetiFrame960x540

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVCaptureSessionPresetiFrame960x540: NSString! ``` | OS X 10.10 |
| To | ``` let AVCaptureSessionPresetiFrame960x540: String ``` | OS X 10.9 |

Modified AVCaptureSessionRuntimeErrorNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVCaptureSessionRuntimeErrorNotification: NSString! ``` | OS X 10.10 |
| To | ``` let AVCaptureSessionRuntimeErrorNotification: String ``` | OS X 10.7 |

Modified AVChannelLayoutKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVChannelLayoutKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVChannelLayoutKey: String ``` | OS X 10.7 |

Modified AVCoreAnimationBeginTimeAtZero

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVEncoderAudioQualityForVBRKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVEncoderAudioQualityForVBRKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVEncoderAudioQualityForVBRKey: String ``` | OS X 10.9 |

Modified AVEncoderAudioQualityKey

|  | Declaration |
| --- | --- |
| From | ``` let AVEncoderAudioQualityKey: NSString! ``` |
| To | ``` let AVEncoderAudioQualityKey: String ``` |

Modified AVEncoderBitDepthHintKey

|  | Declaration |
| --- | --- |
| From | ``` let AVEncoderBitDepthHintKey: NSString! ``` |
| To | ``` let AVEncoderBitDepthHintKey: String ``` |

Modified AVEncoderBitRateKey

|  | Declaration |
| --- | --- |
| From | ``` let AVEncoderBitRateKey: NSString! ``` |
| To | ``` let AVEncoderBitRateKey: String ``` |

Modified AVEncoderBitRatePerChannelKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVEncoderBitRatePerChannelKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVEncoderBitRatePerChannelKey: String ``` | OS X 10.7 |

Modified AVEncoderBitRateStrategyKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVEncoderBitRateStrategyKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVEncoderBitRateStrategyKey: String ``` | OS X 10.9 |

Modified AVErrorDeviceKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVErrorDeviceKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVErrorDeviceKey: String ``` | OS X 10.7 |

Modified AVErrorDiscontinuityFlagsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVErrorDiscontinuityFlagsKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVErrorDiscontinuityFlagsKey: String ``` | OS X 10.7 |

Modified AVErrorFileSizeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVErrorFileSizeKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVErrorFileSizeKey: String ``` | OS X 10.7 |

Modified AVErrorFileTypeKey

|  | Declaration |
| --- | --- |
| From | ``` let AVErrorFileTypeKey: NSString! ``` |
| To | ``` let AVErrorFileTypeKey: String ``` |

Modified AVErrorMediaSubTypeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVErrorMediaSubTypeKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVErrorMediaSubTypeKey: String ``` | OS X 10.7 |

Modified AVErrorMediaTypeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVErrorMediaTypeKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVErrorMediaTypeKey: String ``` | OS X 10.7 |

Modified AVErrorPIDKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVErrorPIDKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVErrorPIDKey: String ``` | OS X 10.7 |

Modified AVErrorPersistentTrackIDKey

|  | Declaration |
| --- | --- |
| From | ``` let AVErrorPersistentTrackIDKey: NSString! ``` |
| To | ``` let AVErrorPersistentTrackIDKey: String ``` |

Modified AVErrorPresentationTimeStampKey

|  | Declaration |
| --- | --- |
| From | ``` let AVErrorPresentationTimeStampKey: NSString! ``` |
| To | ``` let AVErrorPresentationTimeStampKey: String ``` |

Modified AVErrorRecordingSuccessfullyFinishedKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVErrorRecordingSuccessfullyFinishedKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVErrorRecordingSuccessfullyFinishedKey: String ``` | OS X 10.7 |

Modified AVErrorTimeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVErrorTimeKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVErrorTimeKey: String ``` | OS X 10.7 |

Modified AVFileTypeAC3

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVFileTypeAC3: NSString! ``` | OS X 10.10 |
| To | ``` let AVFileTypeAC3: String ``` | OS X 10.9 |

Modified AVFileTypeAIFC

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVFileTypeAIFC: NSString! ``` | OS X 10.10 |
| To | ``` let AVFileTypeAIFC: String ``` | OS X 10.7 |

Modified AVFileTypeAIFF

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVFileTypeAIFF: NSString! ``` | OS X 10.10 |
| To | ``` let AVFileTypeAIFF: String ``` | OS X 10.7 |

Modified AVFileTypeAMR

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVFileTypeAMR: NSString! ``` | OS X 10.10 |
| To | ``` let AVFileTypeAMR: String ``` | OS X 10.7 |

Modified AVFileTypeAppleM4A

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVFileTypeAppleM4A: NSString! ``` | OS X 10.10 |
| To | ``` let AVFileTypeAppleM4A: String ``` | OS X 10.7 |

Modified AVFileTypeAppleM4V

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVFileTypeAppleM4V: NSString! ``` | OS X 10.10 |
| To | ``` let AVFileTypeAppleM4V: String ``` | OS X 10.7 |

Modified AVFileTypeCoreAudioFormat

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVFileTypeCoreAudioFormat: NSString! ``` | OS X 10.10 |
| To | ``` let AVFileTypeCoreAudioFormat: String ``` | OS X 10.7 |

Modified AVFileTypeMPEG4

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVFileTypeMPEG4: NSString! ``` | OS X 10.10 |
| To | ``` let AVFileTypeMPEG4: String ``` | OS X 10.7 |

Modified AVFileTypeMPEGLayer3

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVFileTypeMPEGLayer3: NSString! ``` | OS X 10.10 |
| To | ``` let AVFileTypeMPEGLayer3: String ``` | OS X 10.9 |

Modified AVFileTypeQuickTimeMovie

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVFileTypeQuickTimeMovie: NSString! ``` | OS X 10.10 |
| To | ``` let AVFileTypeQuickTimeMovie: String ``` | OS X 10.7 |

Modified AVFileTypeSunAU

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVFileTypeSunAU: NSString! ``` | OS X 10.10 |
| To | ``` let AVFileTypeSunAU: String ``` | OS X 10.9 |

Modified AVFileTypeWAVE

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVFileTypeWAVE: NSString! ``` | OS X 10.10 |
| To | ``` let AVFileTypeWAVE: String ``` | OS X 10.7 |

Modified AVFormatIDKey

|  | Declaration |
| --- | --- |
| From | ``` let AVFormatIDKey: NSString! ``` |
| To | ``` let AVFormatIDKey: String ``` |

Modified AVFoundationErrorDomain

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVFoundationErrorDomain: NSString! ``` | OS X 10.10 |
| To | ``` let AVFoundationErrorDomain: String ``` | OS X 10.7 |

Modified AVFragmentedMovieDurationDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVFragmentedMovieDurationDidChangeNotification: NSString! ``` |
| To | ``` let AVFragmentedMovieDurationDidChangeNotification: String ``` |

Modified AVFragmentedMovieTrackSegmentsDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVFragmentedMovieTrackSegmentsDidChangeNotification: NSString! ``` |
| To | ``` let AVFragmentedMovieTrackSegmentsDidChangeNotification: String ``` |

Modified AVFragmentedMovieTrackTimeRangeDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVFragmentedMovieTrackTimeRangeDidChangeNotification: NSString! ``` |
| To | ``` let AVFragmentedMovieTrackTimeRangeDidChangeNotification: String ``` |

Modified AVFragmentedMovieTrackTotalSampleDataLengthDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVFragmentedMovieTrackTotalSampleDataLengthDidChangeNotification: NSString! ``` |
| To | ``` let AVFragmentedMovieTrackTotalSampleDataLengthDidChangeNotification: String ``` |

Modified AVFragmentedMovieWasDefragmentedNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVFragmentedMovieWasDefragmentedNotification: NSString! ``` |
| To | ``` let AVFragmentedMovieWasDefragmentedNotification: String ``` |

Modified AVLayerVideoGravityResize

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVLayerVideoGravityResize: NSString! ``` | OS X 10.10 |
| To | ``` let AVLayerVideoGravityResize: String ``` | OS X 10.7 |

Modified AVLayerVideoGravityResizeAspect

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVLayerVideoGravityResizeAspect: NSString! ``` | OS X 10.10 |
| To | ``` let AVLayerVideoGravityResizeAspect: String ``` | OS X 10.7 |

Modified AVLayerVideoGravityResizeAspectFill

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVLayerVideoGravityResizeAspectFill: NSString! ``` | OS X 10.10 |
| To | ``` let AVLayerVideoGravityResizeAspectFill: String ``` | OS X 10.7 |

Modified AVLinearPCMBitDepthKey

|  | Declaration |
| --- | --- |
| From | ``` let AVLinearPCMBitDepthKey: NSString! ``` |
| To | ``` let AVLinearPCMBitDepthKey: String ``` |

Modified AVLinearPCMIsBigEndianKey

|  | Declaration |
| --- | --- |
| From | ``` let AVLinearPCMIsBigEndianKey: NSString! ``` |
| To | ``` let AVLinearPCMIsBigEndianKey: String ``` |

Modified AVLinearPCMIsFloatKey

|  | Declaration |
| --- | --- |
| From | ``` let AVLinearPCMIsFloatKey: NSString! ``` |
| To | ``` let AVLinearPCMIsFloatKey: String ``` |

Modified AVLinearPCMIsNonInterleaved

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVLinearPCMIsNonInterleaved: NSString! ``` | OS X 10.10 |
| To | ``` let AVLinearPCMIsNonInterleaved: String ``` | OS X 10.7 |

Modified AVMakeRectWithAspectRatioInsideRect(CGSize, CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified AVMediaCharacteristicAudible

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMediaCharacteristicAudible: NSString! ``` | OS X 10.10 |
| To | ``` let AVMediaCharacteristicAudible: String ``` | OS X 10.7 |

Modified AVMediaCharacteristicContainsOnlyForcedSubtitles

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMediaCharacteristicContainsOnlyForcedSubtitles: NSString! ``` | OS X 10.10 |
| To | ``` let AVMediaCharacteristicContainsOnlyForcedSubtitles: String ``` | OS X 10.8 |

Modified AVMediaCharacteristicDescribesMusicAndSoundForAccessibility

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMediaCharacteristicDescribesMusicAndSoundForAccessibility: NSString! ``` | OS X 10.10 |
| To | ``` let AVMediaCharacteristicDescribesMusicAndSoundForAccessibility: String ``` | OS X 10.8 |

Modified AVMediaCharacteristicDescribesVideoForAccessibility

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMediaCharacteristicDescribesVideoForAccessibility: NSString! ``` | OS X 10.10 |
| To | ``` let AVMediaCharacteristicDescribesVideoForAccessibility: String ``` | OS X 10.8 |

Modified AVMediaCharacteristicEasyToRead

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMediaCharacteristicEasyToRead: NSString! ``` | OS X 10.10 |
| To | ``` let AVMediaCharacteristicEasyToRead: String ``` | OS X 10.8 |

Modified AVMediaCharacteristicFrameBased

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMediaCharacteristicFrameBased: NSString! ``` | OS X 10.10 |
| To | ``` let AVMediaCharacteristicFrameBased: String ``` | OS X 10.7 |

Modified AVMediaCharacteristicIsAuxiliaryContent

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMediaCharacteristicIsAuxiliaryContent: NSString! ``` | OS X 10.10 |
| To | ``` let AVMediaCharacteristicIsAuxiliaryContent: String ``` | OS X 10.8 |

Modified AVMediaCharacteristicIsMainProgramContent

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMediaCharacteristicIsMainProgramContent: NSString! ``` | OS X 10.10 |
| To | ``` let AVMediaCharacteristicIsMainProgramContent: String ``` | OS X 10.8 |

Modified AVMediaCharacteristicLegible

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMediaCharacteristicLegible: NSString! ``` | OS X 10.10 |
| To | ``` let AVMediaCharacteristicLegible: String ``` | OS X 10.7 |

Modified AVMediaCharacteristicTranscribesSpokenDialogForAccessibility

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMediaCharacteristicTranscribesSpokenDialogForAccessibility: NSString! ``` | OS X 10.10 |
| To | ``` let AVMediaCharacteristicTranscribesSpokenDialogForAccessibility: String ``` | OS X 10.8 |

Modified AVMediaCharacteristicVisual

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMediaCharacteristicVisual: NSString! ``` | OS X 10.10 |
| To | ``` let AVMediaCharacteristicVisual: String ``` | OS X 10.7 |

Modified AVMediaTypeAudio

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMediaTypeAudio: NSString! ``` | OS X 10.10 |
| To | ``` let AVMediaTypeAudio: String ``` | OS X 10.7 |

Modified AVMediaTypeClosedCaption

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMediaTypeClosedCaption: NSString! ``` | OS X 10.10 |
| To | ``` let AVMediaTypeClosedCaption: String ``` | OS X 10.7 |

Modified AVMediaTypeMetadata

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMediaTypeMetadata: NSString! ``` | OS X 10.10 |
| To | ``` let AVMediaTypeMetadata: String ``` | OS X 10.8 |

Modified AVMediaTypeMuxed

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMediaTypeMuxed: NSString! ``` | OS X 10.10 |
| To | ``` let AVMediaTypeMuxed: String ``` | OS X 10.7 |

Modified AVMediaTypeSubtitle

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMediaTypeSubtitle: NSString! ``` | OS X 10.10 |
| To | ``` let AVMediaTypeSubtitle: String ``` | OS X 10.7 |

Modified AVMediaTypeText

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMediaTypeText: NSString! ``` | OS X 10.10 |
| To | ``` let AVMediaTypeText: String ``` | OS X 10.7 |

Modified AVMediaTypeTimecode

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMediaTypeTimecode: NSString! ``` | OS X 10.10 |
| To | ``` let AVMediaTypeTimecode: String ``` | OS X 10.7 |

Modified AVMediaTypeVideo

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMediaTypeVideo: NSString! ``` | OS X 10.10 |
| To | ``` let AVMediaTypeVideo: String ``` | OS X 10.7 |

Modified AVMetadata3GPUserDataKeyAlbumAndTrack

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyAlbumAndTrack: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadata3GPUserDataKeyAlbumAndTrack: String ``` | OS X 10.9 |

Modified AVMetadata3GPUserDataKeyAuthor

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyAuthor: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadata3GPUserDataKeyAuthor: String ``` | OS X 10.7 |

Modified AVMetadata3GPUserDataKeyCollection

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyCollection: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadata3GPUserDataKeyCollection: String ``` | OS X 10.9 |

Modified AVMetadata3GPUserDataKeyCopyright

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyCopyright: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadata3GPUserDataKeyCopyright: String ``` | OS X 10.7 |

Modified AVMetadata3GPUserDataKeyDescription

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyDescription: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadata3GPUserDataKeyDescription: String ``` | OS X 10.7 |

Modified AVMetadata3GPUserDataKeyGenre

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyGenre: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadata3GPUserDataKeyGenre: String ``` | OS X 10.7 |

Modified AVMetadata3GPUserDataKeyKeywordList

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyKeywordList: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadata3GPUserDataKeyKeywordList: String ``` | OS X 10.9 |

Modified AVMetadata3GPUserDataKeyLocation

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyLocation: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadata3GPUserDataKeyLocation: String ``` | OS X 10.7 |

Modified AVMetadata3GPUserDataKeyMediaClassification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyMediaClassification: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadata3GPUserDataKeyMediaClassification: String ``` | OS X 10.9 |

Modified AVMetadata3GPUserDataKeyMediaRating

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyMediaRating: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadata3GPUserDataKeyMediaRating: String ``` | OS X 10.9 |

Modified AVMetadata3GPUserDataKeyPerformer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyPerformer: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadata3GPUserDataKeyPerformer: String ``` | OS X 10.7 |

Modified AVMetadata3GPUserDataKeyRecordingYear

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyRecordingYear: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadata3GPUserDataKeyRecordingYear: String ``` | OS X 10.7 |

Modified AVMetadata3GPUserDataKeyThumbnail

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyThumbnail: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadata3GPUserDataKeyThumbnail: String ``` | OS X 10.9 |

Modified AVMetadata3GPUserDataKeyTitle

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyTitle: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadata3GPUserDataKeyTitle: String ``` | OS X 10.7 |

Modified AVMetadata3GPUserDataKeyUserRating

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyUserRating: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadata3GPUserDataKeyUserRating: String ``` | OS X 10.9 |

Modified AVMetadataCommonIdentifierAlbumName

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierAlbumName: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierAlbumName: String ``` |

Modified AVMetadataCommonIdentifierArtist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierArtist: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierArtist: String ``` |

Modified AVMetadataCommonIdentifierArtwork

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierArtwork: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierArtwork: String ``` |

Modified AVMetadataCommonIdentifierAssetIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierAssetIdentifier: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierAssetIdentifier: String ``` |

Modified AVMetadataCommonIdentifierAuthor

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierAuthor: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierAuthor: String ``` |

Modified AVMetadataCommonIdentifierContributor

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierContributor: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierContributor: String ``` |

Modified AVMetadataCommonIdentifierCopyrights

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierCopyrights: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierCopyrights: String ``` |

Modified AVMetadataCommonIdentifierCreationDate

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierCreationDate: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierCreationDate: String ``` |

Modified AVMetadataCommonIdentifierCreator

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierCreator: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierCreator: String ``` |

Modified AVMetadataCommonIdentifierDescription

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierDescription: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierDescription: String ``` |

Modified AVMetadataCommonIdentifierFormat

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierFormat: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierFormat: String ``` |

Modified AVMetadataCommonIdentifierLanguage

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierLanguage: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierLanguage: String ``` |

Modified AVMetadataCommonIdentifierLastModifiedDate

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierLastModifiedDate: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierLastModifiedDate: String ``` |

Modified AVMetadataCommonIdentifierLocation

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierLocation: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierLocation: String ``` |

Modified AVMetadataCommonIdentifierMake

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierMake: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierMake: String ``` |

Modified AVMetadataCommonIdentifierModel

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierModel: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierModel: String ``` |

Modified AVMetadataCommonIdentifierPublisher

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierPublisher: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierPublisher: String ``` |

Modified AVMetadataCommonIdentifierRelation

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierRelation: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierRelation: String ``` |

Modified AVMetadataCommonIdentifierSoftware

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierSoftware: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierSoftware: String ``` |

Modified AVMetadataCommonIdentifierSource

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierSource: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierSource: String ``` |

Modified AVMetadataCommonIdentifierSubject

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierSubject: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierSubject: String ``` |

Modified AVMetadataCommonIdentifierTitle

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierTitle: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierTitle: String ``` |

Modified AVMetadataCommonIdentifierType

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonIdentifierType: NSString! ``` |
| To | ``` let AVMetadataCommonIdentifierType: String ``` |

Modified AVMetadataCommonKeyAlbumName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeyAlbumName: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeyAlbumName: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeyArtist

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeyArtist: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeyArtist: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeyArtwork

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeyArtwork: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeyArtwork: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeyAuthor

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeyAuthor: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeyAuthor: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeyContributor

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeyContributor: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeyContributor: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeyCopyrights

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeyCopyrights: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeyCopyrights: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeyCreationDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeyCreationDate: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeyCreationDate: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeyCreator

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeyCreator: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeyCreator: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeyDescription

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeyDescription: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeyDescription: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeyFormat

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeyFormat: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeyFormat: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeyIdentifier

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeyIdentifier: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeyIdentifier: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeyLanguage

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeyLanguage: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeyLanguage: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeyLastModifiedDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeyLastModifiedDate: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeyLastModifiedDate: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeyLocation

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeyLocation: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeyLocation: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeyMake

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeyMake: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeyMake: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeyModel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeyModel: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeyModel: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeyPublisher

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeyPublisher: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeyPublisher: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeyRelation

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeyRelation: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeyRelation: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeySoftware

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeySoftware: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeySoftware: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeySource

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeySource: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeySource: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeySubject

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeySubject: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeySubject: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeyTitle

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeyTitle: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeyTitle: String ``` | OS X 10.7 |

Modified AVMetadataCommonKeyType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataCommonKeyType: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataCommonKeyType: String ``` | OS X 10.7 |

Modified AVMetadataExtraAttributeBaseURIKey

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataExtraAttributeBaseURIKey: NSString! ``` |
| To | ``` let AVMetadataExtraAttributeBaseURIKey: String ``` |

Modified AVMetadataExtraAttributeValueURIKey

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataExtraAttributeValueURIKey: NSString! ``` |
| To | ``` let AVMetadataExtraAttributeValueURIKey: String ``` |

Modified AVMetadataFormatHLSMetadata

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataFormatHLSMetadata: NSString! ``` |
| To | ``` let AVMetadataFormatHLSMetadata: String ``` |

Modified AVMetadataFormatID3Metadata

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataFormatID3Metadata: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataFormatID3Metadata: String ``` | OS X 10.7 |

Modified AVMetadataFormatISOUserData

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataFormatISOUserData: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataFormatISOUserData: String ``` | OS X 10.9 |

Modified AVMetadataFormatQuickTimeMetadata

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataFormatQuickTimeMetadata: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataFormatQuickTimeMetadata: String ``` | OS X 10.7 |

Modified AVMetadataFormatQuickTimeUserData

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataFormatQuickTimeUserData: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataFormatQuickTimeUserData: String ``` | OS X 10.7 |

Modified AVMetadataFormatiTunesMetadata

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataFormatiTunesMetadata: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataFormatiTunesMetadata: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyAlbumSortOrder

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyAlbumSortOrder: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyAlbumSortOrder: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyAlbumTitle

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyAlbumTitle: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyAlbumTitle: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyAttachedPicture

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyAttachedPicture: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyAttachedPicture: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyAudioEncryption

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyAudioEncryption: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyAudioEncryption: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyAudioSeekPointIndex

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyAudioSeekPointIndex: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyAudioSeekPointIndex: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyBand

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyBand: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyBand: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyBeatsPerMinute

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyBeatsPerMinute: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyBeatsPerMinute: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyComments

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyComments: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyComments: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyCommercialInformation

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyCommercialInformation: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyCommercialInformation: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyCommerical

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyCommerical: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyCommerical: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyComposer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyComposer: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyComposer: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyConductor

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyConductor: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyConductor: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyContentGroupDescription

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyContentGroupDescription: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyContentGroupDescription: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyContentType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyContentType: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyContentType: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyCopyright

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyCopyright: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyCopyright: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyCopyrightInformation

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyCopyrightInformation: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyCopyrightInformation: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyDate: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyDate: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyEncodedBy

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyEncodedBy: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyEncodedBy: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyEncodedWith

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyEncodedWith: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyEncodedWith: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyEncodingTime

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyEncodingTime: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyEncodingTime: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyEncryption

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyEncryption: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyEncryption: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyEqualization

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyEqualization: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyEqualization: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyEqualization2

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyEqualization2: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyEqualization2: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyEventTimingCodes

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyEventTimingCodes: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyEventTimingCodes: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyFileOwner

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyFileOwner: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyFileOwner: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyFileType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyFileType: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyFileType: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyGeneralEncapsulatedObject

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyGeneralEncapsulatedObject: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyGeneralEncapsulatedObject: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyGroupIdentifier

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyGroupIdentifier: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyGroupIdentifier: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyInitialKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyInitialKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyInitialKey: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyInternationalStandardRecordingCode

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyInternationalStandardRecordingCode: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyInternationalStandardRecordingCode: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyInternetRadioStationName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyInternetRadioStationName: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyInternetRadioStationName: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyInternetRadioStationOwner

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyInternetRadioStationOwner: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyInternetRadioStationOwner: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyInvolvedPeopleList_v23

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyInvolvedPeopleList_v23: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyInvolvedPeopleList_v23: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyInvolvedPeopleList_v24

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyInvolvedPeopleList_v24: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyInvolvedPeopleList_v24: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyLanguage

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyLanguage: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyLanguage: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyLeadPerformer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyLeadPerformer: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyLeadPerformer: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyLength

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyLength: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyLength: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyLink

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyLink: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyLink: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyLyricist

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyLyricist: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyLyricist: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyMPEGLocationLookupTable

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyMPEGLocationLookupTable: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyMPEGLocationLookupTable: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyMediaType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyMediaType: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyMediaType: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyModifiedBy

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyModifiedBy: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyModifiedBy: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyMood

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyMood: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyMood: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyMusicCDIdentifier

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyMusicCDIdentifier: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyMusicCDIdentifier: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyMusicianCreditsList

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyMusicianCreditsList: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyMusicianCreditsList: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyOfficialArtistWebpage

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOfficialArtistWebpage: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyOfficialArtistWebpage: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyOfficialAudioFileWebpage

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOfficialAudioFileWebpage: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyOfficialAudioFileWebpage: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyOfficialAudioSourceWebpage

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOfficialAudioSourceWebpage: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyOfficialAudioSourceWebpage: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyOfficialInternetRadioStationHomepage

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOfficialInternetRadioStationHomepage: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyOfficialInternetRadioStationHomepage: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyOfficialPublisherWebpage

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOfficialPublisherWebpage: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyOfficialPublisherWebpage: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyOriginalAlbumTitle

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOriginalAlbumTitle: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyOriginalAlbumTitle: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyOriginalArtist

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOriginalArtist: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyOriginalArtist: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyOriginalFilename

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOriginalFilename: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyOriginalFilename: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyOriginalLyricist

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOriginalLyricist: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyOriginalLyricist: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyOriginalReleaseTime

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOriginalReleaseTime: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyOriginalReleaseTime: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyOriginalReleaseYear

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOriginalReleaseYear: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyOriginalReleaseYear: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyOwnership

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOwnership: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyOwnership: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyPartOfASet

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyPartOfASet: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyPartOfASet: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyPayment

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyPayment: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyPayment: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyPerformerSortOrder

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyPerformerSortOrder: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyPerformerSortOrder: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyPlayCounter

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyPlayCounter: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyPlayCounter: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyPlaylistDelay

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyPlaylistDelay: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyPlaylistDelay: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyPopularimeter

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyPopularimeter: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyPopularimeter: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyPositionSynchronization

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyPositionSynchronization: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyPositionSynchronization: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyPrivate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyPrivate: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyPrivate: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyProducedNotice

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyProducedNotice: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyProducedNotice: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyPublisher

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyPublisher: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyPublisher: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyRecommendedBufferSize

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyRecommendedBufferSize: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyRecommendedBufferSize: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyRecordingDates

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyRecordingDates: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyRecordingDates: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyRecordingTime

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyRecordingTime: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyRecordingTime: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyRelativeVolumeAdjustment

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyRelativeVolumeAdjustment: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyRelativeVolumeAdjustment: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyRelativeVolumeAdjustment2

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyRelativeVolumeAdjustment2: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyRelativeVolumeAdjustment2: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyReleaseTime

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyReleaseTime: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyReleaseTime: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyReverb

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyReverb: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyReverb: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeySeek

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeySeek: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeySeek: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeySetSubtitle

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeySetSubtitle: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeySetSubtitle: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeySignature

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeySignature: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeySignature: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeySize

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeySize: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeySize: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeySubTitle

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeySubTitle: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeySubTitle: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeySynchronizedLyric

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeySynchronizedLyric: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeySynchronizedLyric: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeySynchronizedTempoCodes

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeySynchronizedTempoCodes: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeySynchronizedTempoCodes: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyTaggingTime

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyTaggingTime: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyTaggingTime: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyTermsOfUse

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyTermsOfUse: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyTermsOfUse: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyTime

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyTime: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyTime: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyTitleDescription

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyTitleDescription: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyTitleDescription: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyTitleSortOrder

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyTitleSortOrder: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyTitleSortOrder: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyTrackNumber

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyTrackNumber: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyTrackNumber: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyUniqueFileIdentifier

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyUniqueFileIdentifier: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyUniqueFileIdentifier: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyUnsynchronizedLyric

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyUnsynchronizedLyric: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyUnsynchronizedLyric: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyUserText

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyUserText: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyUserText: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyUserURL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyUserURL: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyUserURL: String ``` | OS X 10.7 |

Modified AVMetadataID3MetadataKeyYear

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataID3MetadataKeyYear: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataID3MetadataKeyYear: String ``` | OS X 10.7 |

Modified AVMetadataISOUserDataKeyCopyright

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataISOUserDataKeyCopyright: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataISOUserDataKeyCopyright: String ``` | OS X 10.7 |

Modified AVMetadataISOUserDataKeyTaggedCharacteristic

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataISOUserDataKeyTaggedCharacteristic: NSString! ``` |
| To | ``` let AVMetadataISOUserDataKeyTaggedCharacteristic: String ``` |

Modified AVMetadataIcyMetadataKeyStreamTitle

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIcyMetadataKeyStreamTitle: NSString! ``` |
| To | ``` let AVMetadataIcyMetadataKeyStreamTitle: String ``` |

Modified AVMetadataIcyMetadataKeyStreamURL

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIcyMetadataKeyStreamURL: NSString! ``` |
| To | ``` let AVMetadataIcyMetadataKeyStreamURL: String ``` |

Modified AVMetadataIdentifier3GPUserDataAlbumAndTrack

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifier3GPUserDataAlbumAndTrack: NSString! ``` |
| To | ``` let AVMetadataIdentifier3GPUserDataAlbumAndTrack: String ``` |

Modified AVMetadataIdentifier3GPUserDataAuthor

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifier3GPUserDataAuthor: NSString! ``` |
| To | ``` let AVMetadataIdentifier3GPUserDataAuthor: String ``` |

Modified AVMetadataIdentifier3GPUserDataCollection

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifier3GPUserDataCollection: NSString! ``` |
| To | ``` let AVMetadataIdentifier3GPUserDataCollection: String ``` |

Modified AVMetadataIdentifier3GPUserDataCopyright

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifier3GPUserDataCopyright: NSString! ``` |
| To | ``` let AVMetadataIdentifier3GPUserDataCopyright: String ``` |

Modified AVMetadataIdentifier3GPUserDataDescription

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifier3GPUserDataDescription: NSString! ``` |
| To | ``` let AVMetadataIdentifier3GPUserDataDescription: String ``` |

Modified AVMetadataIdentifier3GPUserDataGenre

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifier3GPUserDataGenre: NSString! ``` |
| To | ``` let AVMetadataIdentifier3GPUserDataGenre: String ``` |

Modified AVMetadataIdentifier3GPUserDataKeywordList

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifier3GPUserDataKeywordList: NSString! ``` |
| To | ``` let AVMetadataIdentifier3GPUserDataKeywordList: String ``` |

Modified AVMetadataIdentifier3GPUserDataLocation

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifier3GPUserDataLocation: NSString! ``` |
| To | ``` let AVMetadataIdentifier3GPUserDataLocation: String ``` |

Modified AVMetadataIdentifier3GPUserDataMediaClassification

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifier3GPUserDataMediaClassification: NSString! ``` |
| To | ``` let AVMetadataIdentifier3GPUserDataMediaClassification: String ``` |

Modified AVMetadataIdentifier3GPUserDataMediaRating

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifier3GPUserDataMediaRating: NSString! ``` |
| To | ``` let AVMetadataIdentifier3GPUserDataMediaRating: String ``` |

Modified AVMetadataIdentifier3GPUserDataPerformer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifier3GPUserDataPerformer: NSString! ``` |
| To | ``` let AVMetadataIdentifier3GPUserDataPerformer: String ``` |

Modified AVMetadataIdentifier3GPUserDataRecordingYear

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifier3GPUserDataRecordingYear: NSString! ``` |
| To | ``` let AVMetadataIdentifier3GPUserDataRecordingYear: String ``` |

Modified AVMetadataIdentifier3GPUserDataThumbnail

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifier3GPUserDataThumbnail: NSString! ``` |
| To | ``` let AVMetadataIdentifier3GPUserDataThumbnail: String ``` |

Modified AVMetadataIdentifier3GPUserDataTitle

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifier3GPUserDataTitle: NSString! ``` |
| To | ``` let AVMetadataIdentifier3GPUserDataTitle: String ``` |

Modified AVMetadataIdentifier3GPUserDataUserRating

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifier3GPUserDataUserRating: NSString! ``` |
| To | ``` let AVMetadataIdentifier3GPUserDataUserRating: String ``` |

Modified AVMetadataIdentifierID3MetadataAlbumSortOrder

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataAlbumSortOrder: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataAlbumSortOrder: String ``` |

Modified AVMetadataIdentifierID3MetadataAlbumTitle

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataAlbumTitle: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataAlbumTitle: String ``` |

Modified AVMetadataIdentifierID3MetadataAttachedPicture

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataAttachedPicture: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataAttachedPicture: String ``` |

Modified AVMetadataIdentifierID3MetadataAudioEncryption

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataAudioEncryption: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataAudioEncryption: String ``` |

Modified AVMetadataIdentifierID3MetadataAudioSeekPointIndex

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataAudioSeekPointIndex: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataAudioSeekPointIndex: String ``` |

Modified AVMetadataIdentifierID3MetadataBand

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataBand: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataBand: String ``` |

Modified AVMetadataIdentifierID3MetadataBeatsPerMinute

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataBeatsPerMinute: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataBeatsPerMinute: String ``` |

Modified AVMetadataIdentifierID3MetadataComments

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataComments: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataComments: String ``` |

Modified AVMetadataIdentifierID3MetadataCommercialInformation

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataCommercialInformation: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataCommercialInformation: String ``` |

Modified AVMetadataIdentifierID3MetadataCommerical

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataCommerical: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataCommerical: String ``` |

Modified AVMetadataIdentifierID3MetadataComposer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataComposer: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataComposer: String ``` |

Modified AVMetadataIdentifierID3MetadataConductor

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataConductor: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataConductor: String ``` |

Modified AVMetadataIdentifierID3MetadataContentGroupDescription

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataContentGroupDescription: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataContentGroupDescription: String ``` |

Modified AVMetadataIdentifierID3MetadataContentType

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataContentType: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataContentType: String ``` |

Modified AVMetadataIdentifierID3MetadataCopyright

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataCopyright: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataCopyright: String ``` |

Modified AVMetadataIdentifierID3MetadataCopyrightInformation

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataCopyrightInformation: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataCopyrightInformation: String ``` |

Modified AVMetadataIdentifierID3MetadataDate

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataDate: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataDate: String ``` |

Modified AVMetadataIdentifierID3MetadataEncodedBy

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataEncodedBy: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataEncodedBy: String ``` |

Modified AVMetadataIdentifierID3MetadataEncodedWith

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataEncodedWith: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataEncodedWith: String ``` |

Modified AVMetadataIdentifierID3MetadataEncodingTime

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataEncodingTime: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataEncodingTime: String ``` |

Modified AVMetadataIdentifierID3MetadataEncryption

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataEncryption: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataEncryption: String ``` |

Modified AVMetadataIdentifierID3MetadataEqualization

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataEqualization: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataEqualization: String ``` |

Modified AVMetadataIdentifierID3MetadataEqualization2

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataEqualization2: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataEqualization2: String ``` |

Modified AVMetadataIdentifierID3MetadataEventTimingCodes

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataEventTimingCodes: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataEventTimingCodes: String ``` |

Modified AVMetadataIdentifierID3MetadataFileOwner

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataFileOwner: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataFileOwner: String ``` |

Modified AVMetadataIdentifierID3MetadataFileType

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataFileType: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataFileType: String ``` |

Modified AVMetadataIdentifierID3MetadataGeneralEncapsulatedObject

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataGeneralEncapsulatedObject: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataGeneralEncapsulatedObject: String ``` |

Modified AVMetadataIdentifierID3MetadataGroupIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataGroupIdentifier: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataGroupIdentifier: String ``` |

Modified AVMetadataIdentifierID3MetadataInitialKey

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataInitialKey: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataInitialKey: String ``` |

Modified AVMetadataIdentifierID3MetadataInternationalStandardRecordingCode

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataInternationalStandardRecordingCode: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataInternationalStandardRecordingCode: String ``` |

Modified AVMetadataIdentifierID3MetadataInternetRadioStationName

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataInternetRadioStationName: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataInternetRadioStationName: String ``` |

Modified AVMetadataIdentifierID3MetadataInternetRadioStationOwner

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataInternetRadioStationOwner: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataInternetRadioStationOwner: String ``` |

Modified AVMetadataIdentifierID3MetadataInvolvedPeopleList_v23

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataInvolvedPeopleList_v23: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataInvolvedPeopleList_v23: String ``` |

Modified AVMetadataIdentifierID3MetadataInvolvedPeopleList_v24

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataInvolvedPeopleList_v24: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataInvolvedPeopleList_v24: String ``` |

Modified AVMetadataIdentifierID3MetadataLanguage

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataLanguage: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataLanguage: String ``` |

Modified AVMetadataIdentifierID3MetadataLeadPerformer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataLeadPerformer: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataLeadPerformer: String ``` |

Modified AVMetadataIdentifierID3MetadataLength

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataLength: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataLength: String ``` |

Modified AVMetadataIdentifierID3MetadataLink

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataLink: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataLink: String ``` |

Modified AVMetadataIdentifierID3MetadataLyricist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataLyricist: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataLyricist: String ``` |

Modified AVMetadataIdentifierID3MetadataMPEGLocationLookupTable

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataMPEGLocationLookupTable: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataMPEGLocationLookupTable: String ``` |

Modified AVMetadataIdentifierID3MetadataMediaType

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataMediaType: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataMediaType: String ``` |

Modified AVMetadataIdentifierID3MetadataModifiedBy

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataModifiedBy: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataModifiedBy: String ``` |

Modified AVMetadataIdentifierID3MetadataMood

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataMood: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataMood: String ``` |

Modified AVMetadataIdentifierID3MetadataMusicCDIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataMusicCDIdentifier: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataMusicCDIdentifier: String ``` |

Modified AVMetadataIdentifierID3MetadataMusicianCreditsList

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataMusicianCreditsList: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataMusicianCreditsList: String ``` |

Modified AVMetadataIdentifierID3MetadataOfficialArtistWebpage

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataOfficialArtistWebpage: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataOfficialArtistWebpage: String ``` |

Modified AVMetadataIdentifierID3MetadataOfficialAudioFileWebpage

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataOfficialAudioFileWebpage: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataOfficialAudioFileWebpage: String ``` |

Modified AVMetadataIdentifierID3MetadataOfficialAudioSourceWebpage

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataOfficialAudioSourceWebpage: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataOfficialAudioSourceWebpage: String ``` |

Modified AVMetadataIdentifierID3MetadataOfficialInternetRadioStationHomepage

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataOfficialInternetRadioStationHomepage: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataOfficialInternetRadioStationHomepage: String ``` |

Modified AVMetadataIdentifierID3MetadataOfficialPublisherWebpage

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataOfficialPublisherWebpage: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataOfficialPublisherWebpage: String ``` |

Modified AVMetadataIdentifierID3MetadataOriginalAlbumTitle

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataOriginalAlbumTitle: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataOriginalAlbumTitle: String ``` |

Modified AVMetadataIdentifierID3MetadataOriginalArtist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataOriginalArtist: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataOriginalArtist: String ``` |

Modified AVMetadataIdentifierID3MetadataOriginalFilename

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataOriginalFilename: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataOriginalFilename: String ``` |

Modified AVMetadataIdentifierID3MetadataOriginalLyricist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataOriginalLyricist: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataOriginalLyricist: String ``` |

Modified AVMetadataIdentifierID3MetadataOriginalReleaseTime

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataOriginalReleaseTime: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataOriginalReleaseTime: String ``` |

Modified AVMetadataIdentifierID3MetadataOriginalReleaseYear

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataOriginalReleaseYear: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataOriginalReleaseYear: String ``` |

Modified AVMetadataIdentifierID3MetadataOwnership

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataOwnership: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataOwnership: String ``` |

Modified AVMetadataIdentifierID3MetadataPartOfASet

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataPartOfASet: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataPartOfASet: String ``` |

Modified AVMetadataIdentifierID3MetadataPayment

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataPayment: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataPayment: String ``` |

Modified AVMetadataIdentifierID3MetadataPerformerSortOrder

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataPerformerSortOrder: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataPerformerSortOrder: String ``` |

Modified AVMetadataIdentifierID3MetadataPlayCounter

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataPlayCounter: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataPlayCounter: String ``` |

Modified AVMetadataIdentifierID3MetadataPlaylistDelay

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataPlaylistDelay: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataPlaylistDelay: String ``` |

Modified AVMetadataIdentifierID3MetadataPopularimeter

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataPopularimeter: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataPopularimeter: String ``` |

Modified AVMetadataIdentifierID3MetadataPositionSynchronization

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataPositionSynchronization: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataPositionSynchronization: String ``` |

Modified AVMetadataIdentifierID3MetadataPrivate

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataPrivate: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataPrivate: String ``` |

Modified AVMetadataIdentifierID3MetadataProducedNotice

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataProducedNotice: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataProducedNotice: String ``` |

Modified AVMetadataIdentifierID3MetadataPublisher

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataPublisher: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataPublisher: String ``` |

Modified AVMetadataIdentifierID3MetadataRecommendedBufferSize

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataRecommendedBufferSize: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataRecommendedBufferSize: String ``` |

Modified AVMetadataIdentifierID3MetadataRecordingDates

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataRecordingDates: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataRecordingDates: String ``` |

Modified AVMetadataIdentifierID3MetadataRecordingTime

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataRecordingTime: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataRecordingTime: String ``` |

Modified AVMetadataIdentifierID3MetadataRelativeVolumeAdjustment

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataRelativeVolumeAdjustment: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataRelativeVolumeAdjustment: String ``` |

Modified AVMetadataIdentifierID3MetadataRelativeVolumeAdjustment2

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataRelativeVolumeAdjustment2: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataRelativeVolumeAdjustment2: String ``` |

Modified AVMetadataIdentifierID3MetadataReleaseTime

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataReleaseTime: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataReleaseTime: String ``` |

Modified AVMetadataIdentifierID3MetadataReverb

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataReverb: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataReverb: String ``` |

Modified AVMetadataIdentifierID3MetadataSeek

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataSeek: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataSeek: String ``` |

Modified AVMetadataIdentifierID3MetadataSetSubtitle

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataSetSubtitle: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataSetSubtitle: String ``` |

Modified AVMetadataIdentifierID3MetadataSignature

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataSignature: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataSignature: String ``` |

Modified AVMetadataIdentifierID3MetadataSize

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataSize: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataSize: String ``` |

Modified AVMetadataIdentifierID3MetadataSubTitle

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataSubTitle: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataSubTitle: String ``` |

Modified AVMetadataIdentifierID3MetadataSynchronizedLyric

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataSynchronizedLyric: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataSynchronizedLyric: String ``` |

Modified AVMetadataIdentifierID3MetadataSynchronizedTempoCodes

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataSynchronizedTempoCodes: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataSynchronizedTempoCodes: String ``` |

Modified AVMetadataIdentifierID3MetadataTaggingTime

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataTaggingTime: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataTaggingTime: String ``` |

Modified AVMetadataIdentifierID3MetadataTermsOfUse

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataTermsOfUse: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataTermsOfUse: String ``` |

Modified AVMetadataIdentifierID3MetadataTime

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataTime: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataTime: String ``` |

Modified AVMetadataIdentifierID3MetadataTitleDescription

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataTitleDescription: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataTitleDescription: String ``` |

Modified AVMetadataIdentifierID3MetadataTitleSortOrder

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataTitleSortOrder: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataTitleSortOrder: String ``` |

Modified AVMetadataIdentifierID3MetadataTrackNumber

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataTrackNumber: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataTrackNumber: String ``` |

Modified AVMetadataIdentifierID3MetadataUniqueFileIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataUniqueFileIdentifier: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataUniqueFileIdentifier: String ``` |

Modified AVMetadataIdentifierID3MetadataUnsynchronizedLyric

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataUnsynchronizedLyric: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataUnsynchronizedLyric: String ``` |

Modified AVMetadataIdentifierID3MetadataUserText

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataUserText: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataUserText: String ``` |

Modified AVMetadataIdentifierID3MetadataUserURL

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataUserURL: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataUserURL: String ``` |

Modified AVMetadataIdentifierID3MetadataYear

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierID3MetadataYear: NSString! ``` |
| To | ``` let AVMetadataIdentifierID3MetadataYear: String ``` |

Modified AVMetadataIdentifierISOUserDataCopyright

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierISOUserDataCopyright: NSString! ``` |
| To | ``` let AVMetadataIdentifierISOUserDataCopyright: String ``` |

Modified AVMetadataIdentifierISOUserDataTaggedCharacteristic

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierISOUserDataTaggedCharacteristic: NSString! ``` |
| To | ``` let AVMetadataIdentifierISOUserDataTaggedCharacteristic: String ``` |

Modified AVMetadataIdentifierIcyMetadataStreamTitle

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierIcyMetadataStreamTitle: NSString! ``` |
| To | ``` let AVMetadataIdentifierIcyMetadataStreamTitle: String ``` |

Modified AVMetadataIdentifierIcyMetadataStreamURL

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierIcyMetadataStreamURL: NSString! ``` |
| To | ``` let AVMetadataIdentifierIcyMetadataStreamURL: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataAlbum

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataAlbum: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataAlbum: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataArranger

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataArranger: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataArranger: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataArtist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataArtist: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataArtist: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataArtwork

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataArtwork: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataArtwork: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataAuthor

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataAuthor: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataAuthor: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataCameraFrameReadoutTime

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataCameraFrameReadoutTime: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataCameraFrameReadoutTime: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataCameraIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataCameraIdentifier: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataCameraIdentifier: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataCollectionUser

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataCollectionUser: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataCollectionUser: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataComment

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataComment: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataComment: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataComposer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataComposer: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataComposer: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataCopyright

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataCopyright: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataCopyright: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataCreationDate

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataCreationDate: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataCreationDate: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataCredits

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataCredits: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataCredits: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataDescription

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataDescription: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataDescription: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataDirectionFacing

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataDirectionFacing: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataDirectionFacing: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataDirectionMotion

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataDirectionMotion: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataDirectionMotion: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataDirector

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataDirector: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataDirector: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataDisplayName

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataDisplayName: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataDisplayName: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataEncodedBy

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataEncodedBy: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataEncodedBy: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataGenre

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataGenre: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataGenre: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataInformation

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataInformation: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataInformation: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataKeywords

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataKeywords: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataKeywords: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataLocationBody

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataLocationBody: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataLocationBody: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataLocationDate

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataLocationDate: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataLocationDate: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataLocationISO6709

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataLocationISO6709: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataLocationISO6709: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataLocationName

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataLocationName: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataLocationName: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataLocationNote

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataLocationNote: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataLocationNote: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataLocationRole

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataLocationRole: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataLocationRole: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataMake

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataMake: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataMake: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataModel

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataModel: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataModel: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataOriginalArtist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataOriginalArtist: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataOriginalArtist: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataPerformer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataPerformer: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataPerformer: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataPhonogramRights

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataPhonogramRights: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataPhonogramRights: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataPreferredAffineTransform

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataPreferredAffineTransform: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataPreferredAffineTransform: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataProducer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataProducer: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataProducer: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataPublisher

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataPublisher: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataPublisher: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataRatingUser

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataRatingUser: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataRatingUser: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataSoftware

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataSoftware: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataSoftware: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataTitle

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataTitle: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataTitle: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataYear

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataYear: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataYear: String ``` |

Modified AVMetadataIdentifierQuickTimeMetadataiXML

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeMetadataiXML: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeMetadataiXML: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataAlbum

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataAlbum: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataAlbum: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataArranger

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataArranger: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataArranger: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataArtist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataArtist: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataArtist: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataAuthor

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataAuthor: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataAuthor: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataChapter

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataChapter: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataChapter: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataComment

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataComment: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataComment: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataComposer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataComposer: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataComposer: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataCopyright

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataCopyright: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataCopyright: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataCreationDate

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataCreationDate: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataCreationDate: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataCredits

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataCredits: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataCredits: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataDescription

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataDescription: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataDescription: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataDirector

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataDirector: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataDirector: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataDisclaimer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataDisclaimer: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataDisclaimer: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataEncodedBy

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataEncodedBy: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataEncodedBy: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataFullName

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataFullName: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataFullName: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataGenre

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataGenre: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataGenre: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataHostComputer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataHostComputer: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataHostComputer: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataInformation

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataInformation: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataInformation: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataKeywords

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataKeywords: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataKeywords: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataLocationISO6709

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataLocationISO6709: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataLocationISO6709: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataMake

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataMake: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataMake: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataModel

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataModel: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataModel: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataOriginalArtist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataOriginalArtist: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataOriginalArtist: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataOriginalFormat

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataOriginalFormat: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataOriginalFormat: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataOriginalSource

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataOriginalSource: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataOriginalSource: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataPerformers

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataPerformers: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataPerformers: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataPhonogramRights

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataPhonogramRights: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataPhonogramRights: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataProducer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataProducer: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataProducer: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataProduct

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataProduct: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataProduct: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataPublisher

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataPublisher: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataPublisher: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataSoftware

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataSoftware: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataSoftware: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataSpecialPlaybackRequirements

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataSpecialPlaybackRequirements: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataSpecialPlaybackRequirements: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataTaggedCharacteristic

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataTaggedCharacteristic: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataTaggedCharacteristic: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataTrack

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataTrack: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataTrack: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataTrackName

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataTrackName: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataTrackName: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataURLLink

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataURLLink: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataURLLink: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataWarning

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataWarning: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataWarning: String ``` |

Modified AVMetadataIdentifierQuickTimeUserDataWriter

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifierQuickTimeUserDataWriter: NSString! ``` |
| To | ``` let AVMetadataIdentifierQuickTimeUserDataWriter: String ``` |

Modified AVMetadataIdentifieriTunesMetadataAccountKind

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataAccountKind: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataAccountKind: String ``` |

Modified AVMetadataIdentifieriTunesMetadataAcknowledgement

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataAcknowledgement: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataAcknowledgement: String ``` |

Modified AVMetadataIdentifieriTunesMetadataAlbum

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataAlbum: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataAlbum: String ``` |

Modified AVMetadataIdentifieriTunesMetadataAlbumArtist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataAlbumArtist: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataAlbumArtist: String ``` |

Modified AVMetadataIdentifieriTunesMetadataAppleID

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataAppleID: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataAppleID: String ``` |

Modified AVMetadataIdentifieriTunesMetadataArranger

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataArranger: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataArranger: String ``` |

Modified AVMetadataIdentifieriTunesMetadataArtDirector

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataArtDirector: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataArtDirector: String ``` |

Modified AVMetadataIdentifieriTunesMetadataArtist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataArtist: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataArtist: String ``` |

Modified AVMetadataIdentifieriTunesMetadataArtistID

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataArtistID: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataArtistID: String ``` |

Modified AVMetadataIdentifieriTunesMetadataAuthor

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataAuthor: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataAuthor: String ``` |

Modified AVMetadataIdentifieriTunesMetadataBeatsPerMin

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataBeatsPerMin: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataBeatsPerMin: String ``` |

Modified AVMetadataIdentifieriTunesMetadataComposer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataComposer: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataComposer: String ``` |

Modified AVMetadataIdentifieriTunesMetadataConductor

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataConductor: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataConductor: String ``` |

Modified AVMetadataIdentifieriTunesMetadataContentRating

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataContentRating: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataContentRating: String ``` |

Modified AVMetadataIdentifieriTunesMetadataCopyright

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataCopyright: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataCopyright: String ``` |

Modified AVMetadataIdentifieriTunesMetadataCoverArt

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataCoverArt: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataCoverArt: String ``` |

Modified AVMetadataIdentifieriTunesMetadataCredits

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataCredits: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataCredits: String ``` |

Modified AVMetadataIdentifieriTunesMetadataDescription

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataDescription: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataDescription: String ``` |

Modified AVMetadataIdentifieriTunesMetadataDirector

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataDirector: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataDirector: String ``` |

Modified AVMetadataIdentifieriTunesMetadataDiscCompilation

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataDiscCompilation: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataDiscCompilation: String ``` |

Modified AVMetadataIdentifieriTunesMetadataDiscNumber

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataDiscNumber: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataDiscNumber: String ``` |

Modified AVMetadataIdentifieriTunesMetadataEQ

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataEQ: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataEQ: String ``` |

Modified AVMetadataIdentifieriTunesMetadataEncodedBy

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataEncodedBy: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataEncodedBy: String ``` |

Modified AVMetadataIdentifieriTunesMetadataEncodingTool

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataEncodingTool: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataEncodingTool: String ``` |

Modified AVMetadataIdentifieriTunesMetadataExecProducer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataExecProducer: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataExecProducer: String ``` |

Modified AVMetadataIdentifieriTunesMetadataGenreID

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataGenreID: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataGenreID: String ``` |

Modified AVMetadataIdentifieriTunesMetadataGrouping

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataGrouping: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataGrouping: String ``` |

Modified AVMetadataIdentifieriTunesMetadataLinerNotes

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataLinerNotes: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataLinerNotes: String ``` |

Modified AVMetadataIdentifieriTunesMetadataLyrics

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataLyrics: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataLyrics: String ``` |

Modified AVMetadataIdentifieriTunesMetadataOnlineExtras

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataOnlineExtras: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataOnlineExtras: String ``` |

Modified AVMetadataIdentifieriTunesMetadataOriginalArtist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataOriginalArtist: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataOriginalArtist: String ``` |

Modified AVMetadataIdentifieriTunesMetadataPerformer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataPerformer: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataPerformer: String ``` |

Modified AVMetadataIdentifieriTunesMetadataPhonogramRights

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataPhonogramRights: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataPhonogramRights: String ``` |

Modified AVMetadataIdentifieriTunesMetadataPlaylistID

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataPlaylistID: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataPlaylistID: String ``` |

Modified AVMetadataIdentifieriTunesMetadataPredefinedGenre

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataPredefinedGenre: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataPredefinedGenre: String ``` |

Modified AVMetadataIdentifieriTunesMetadataProducer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataProducer: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataProducer: String ``` |

Modified AVMetadataIdentifieriTunesMetadataPublisher

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataPublisher: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataPublisher: String ``` |

Modified AVMetadataIdentifieriTunesMetadataRecordCompany

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataRecordCompany: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataRecordCompany: String ``` |

Modified AVMetadataIdentifieriTunesMetadataReleaseDate

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataReleaseDate: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataReleaseDate: String ``` |

Modified AVMetadataIdentifieriTunesMetadataSoloist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataSoloist: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataSoloist: String ``` |

Modified AVMetadataIdentifieriTunesMetadataSongID

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataSongID: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataSongID: String ``` |

Modified AVMetadataIdentifieriTunesMetadataSongName

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataSongName: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataSongName: String ``` |

Modified AVMetadataIdentifieriTunesMetadataSoundEngineer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataSoundEngineer: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataSoundEngineer: String ``` |

Modified AVMetadataIdentifieriTunesMetadataThanks

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataThanks: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataThanks: String ``` |

Modified AVMetadataIdentifieriTunesMetadataTrackNumber

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataTrackNumber: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataTrackNumber: String ``` |

Modified AVMetadataIdentifieriTunesMetadataTrackSubTitle

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataTrackSubTitle: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataTrackSubTitle: String ``` |

Modified AVMetadataIdentifieriTunesMetadataUserComment

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataUserComment: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataUserComment: String ``` |

Modified AVMetadataIdentifieriTunesMetadataUserGenre

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataIdentifieriTunesMetadataUserGenre: NSString! ``` |
| To | ``` let AVMetadataIdentifieriTunesMetadataUserGenre: String ``` |

Modified AVMetadataKeySpaceCommon

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataKeySpaceCommon: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataKeySpaceCommon: String ``` | OS X 10.7 |

Modified AVMetadataKeySpaceID3

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataKeySpaceID3: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataKeySpaceID3: String ``` | OS X 10.7 |

Modified AVMetadataKeySpaceISOUserData

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataKeySpaceISOUserData: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataKeySpaceISOUserData: String ``` | OS X 10.9 |

Modified AVMetadataKeySpaceIcy

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataKeySpaceIcy: NSString! ``` |
| To | ``` let AVMetadataKeySpaceIcy: String ``` |

Modified AVMetadataKeySpaceQuickTimeMetadata

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataKeySpaceQuickTimeMetadata: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataKeySpaceQuickTimeMetadata: String ``` | OS X 10.7 |

Modified AVMetadataKeySpaceQuickTimeUserData

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataKeySpaceQuickTimeUserData: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataKeySpaceQuickTimeUserData: String ``` | OS X 10.7 |

Modified AVMetadataKeySpaceiTunes

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataKeySpaceiTunes: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataKeySpaceiTunes: String ``` | OS X 10.7 |

Modified AVMetadataObjectTypeFace

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataObjectTypeFace: NSString! ``` |
| To | ``` let AVMetadataObjectTypeFace: String ``` |

Modified AVMetadataQuickTimeMetadataKeyAlbum

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyAlbum: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyAlbum: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyArranger

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyArranger: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyArranger: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyArtist

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyArtist: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyArtist: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyArtwork

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyArtwork: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyArtwork: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyAuthor

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyAuthor: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyAuthor: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyCameraFrameReadoutTime

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyCameraFrameReadoutTime: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyCameraFrameReadoutTime: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyCameraIdentifier

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyCameraIdentifier: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyCameraIdentifier: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyCollectionUser

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyCollectionUser: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyCollectionUser: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyComment

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyComment: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyComment: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyComposer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyComposer: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyComposer: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyCopyright

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyCopyright: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyCopyright: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyCreationDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyCreationDate: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyCreationDate: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyCredits

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyCredits: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyCredits: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyDescription

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyDescription: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyDescription: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyDirectionFacing

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyDirectionFacing: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyDirectionFacing: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyDirectionMotion

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyDirectionMotion: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyDirectionMotion: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyDirector

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyDirector: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyDirector: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyDisplayName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyDisplayName: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyDisplayName: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyEncodedBy

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyEncodedBy: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyEncodedBy: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyGenre

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyGenre: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyGenre: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyInformation

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyInformation: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyInformation: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyKeywords

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyKeywords: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyKeywords: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyLocationBody

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyLocationBody: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyLocationBody: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyLocationDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyLocationDate: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyLocationDate: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyLocationISO6709

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyLocationISO6709: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyLocationISO6709: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyLocationName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyLocationName: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyLocationName: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyLocationNote

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyLocationNote: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyLocationNote: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyLocationRole

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyLocationRole: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyLocationRole: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyMake

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyMake: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyMake: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyModel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyModel: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyModel: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyOriginalArtist

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyOriginalArtist: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyOriginalArtist: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyPerformer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyPerformer: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyPerformer: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyPhonogramRights

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyPhonogramRights: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyPhonogramRights: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyProducer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyProducer: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyProducer: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyPublisher

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyPublisher: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyPublisher: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyRatingUser

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyRatingUser: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyRatingUser: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeySoftware

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeySoftware: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeySoftware: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyTitle

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyTitle: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyTitle: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyYear

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyYear: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyYear: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeMetadataKeyiXML

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyiXML: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeMetadataKeyiXML: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyAlbum

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyAlbum: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyAlbum: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyArranger

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyArranger: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyArranger: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyArtist

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyArtist: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyArtist: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyAuthor

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyAuthor: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyAuthor: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyChapter

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyChapter: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyChapter: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyComment

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyComment: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyComment: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyComposer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyComposer: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyComposer: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyCopyright

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyCopyright: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyCopyright: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyCreationDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyCreationDate: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyCreationDate: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyCredits

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyCredits: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyCredits: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyDescription

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyDescription: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyDescription: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyDirector

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyDirector: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyDirector: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyDisclaimer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyDisclaimer: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyDisclaimer: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyEncodedBy

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyEncodedBy: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyEncodedBy: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyFullName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyFullName: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyFullName: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyGenre

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyGenre: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyGenre: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyHostComputer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyHostComputer: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyHostComputer: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyInformation

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyInformation: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyInformation: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyKeywords

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyKeywords: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyKeywords: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyLocationISO6709

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyLocationISO6709: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyLocationISO6709: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyMake

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyMake: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyMake: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyModel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyModel: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyModel: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyOriginalArtist

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyOriginalArtist: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyOriginalArtist: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyOriginalFormat

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyOriginalFormat: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyOriginalFormat: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyOriginalSource

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyOriginalSource: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyOriginalSource: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyPerformers

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyPerformers: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyPerformers: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyPhonogramRights

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyPhonogramRights: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyPhonogramRights: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyProducer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyProducer: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyProducer: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyProduct

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyProduct: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyProduct: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyPublisher

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyPublisher: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyPublisher: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeySoftware

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeySoftware: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeySoftware: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeySpecialPlaybackRequirements

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeySpecialPlaybackRequirements: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeySpecialPlaybackRequirements: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyTaggedCharacteristic

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyTaggedCharacteristic: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyTaggedCharacteristic: String ``` | OS X 10.8 |

Modified AVMetadataQuickTimeUserDataKeyTrack

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyTrack: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyTrack: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyTrackName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyTrackName: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyTrackName: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyURLLink

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyURLLink: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyURLLink: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyWarning

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyWarning: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyWarning: String ``` | OS X 10.7 |

Modified AVMetadataQuickTimeUserDataKeyWriter

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyWriter: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataQuickTimeUserDataKeyWriter: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyAccountKind

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyAccountKind: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyAccountKind: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyAcknowledgement

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyAcknowledgement: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyAcknowledgement: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyAlbum

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyAlbum: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyAlbum: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyAlbumArtist

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyAlbumArtist: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyAlbumArtist: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyAppleID

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyAppleID: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyAppleID: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyArranger

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyArranger: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyArranger: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyArtDirector

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyArtDirector: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyArtDirector: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyArtist

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyArtist: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyArtist: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyArtistID

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyArtistID: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyArtistID: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyAuthor

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyAuthor: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyAuthor: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyBeatsPerMin

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyBeatsPerMin: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyBeatsPerMin: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyComposer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyComposer: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyComposer: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyConductor

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyConductor: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyConductor: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyContentRating

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyContentRating: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyContentRating: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyCopyright

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyCopyright: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyCopyright: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyCoverArt

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyCoverArt: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyCoverArt: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyCredits

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyCredits: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyCredits: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyDescription

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyDescription: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyDescription: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyDirector

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyDirector: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyDirector: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyDiscCompilation

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyDiscCompilation: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyDiscCompilation: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyDiscNumber

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyDiscNumber: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyDiscNumber: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyEQ

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyEQ: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyEQ: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyEncodedBy

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyEncodedBy: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyEncodedBy: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyEncodingTool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyEncodingTool: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyEncodingTool: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyExecProducer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyExecProducer: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyExecProducer: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyGenreID

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyGenreID: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyGenreID: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyGrouping

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyGrouping: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyGrouping: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyLinerNotes

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyLinerNotes: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyLinerNotes: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyLyrics

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyLyrics: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyLyrics: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyOnlineExtras

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyOnlineExtras: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyOnlineExtras: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyOriginalArtist

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyOriginalArtist: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyOriginalArtist: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyPerformer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyPerformer: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyPerformer: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyPhonogramRights

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyPhonogramRights: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyPhonogramRights: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyPlaylistID

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyPlaylistID: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyPlaylistID: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyPredefinedGenre

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyPredefinedGenre: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyPredefinedGenre: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyProducer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyProducer: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyProducer: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyPublisher

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyPublisher: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyPublisher: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyRecordCompany

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyRecordCompany: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyRecordCompany: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyReleaseDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyReleaseDate: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyReleaseDate: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeySoloist

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeySoloist: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeySoloist: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeySongID

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeySongID: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeySongID: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeySongName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeySongName: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeySongName: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeySoundEngineer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeySoundEngineer: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeySoundEngineer: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyThanks

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyThanks: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyThanks: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyTrackNumber

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyTrackNumber: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyTrackNumber: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyTrackSubTitle

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyTrackSubTitle: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyTrackSubTitle: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyUserComment

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyUserComment: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyUserComment: String ``` | OS X 10.7 |

Modified AVMetadataiTunesMetadataKeyUserGenre

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyUserGenre: NSString! ``` | OS X 10.10 |
| To | ``` let AVMetadataiTunesMetadataKeyUserGenre: String ``` | OS X 10.7 |

Modified AVMovieReferenceRestrictionsKey

|  | Declaration |
| --- | --- |
| From | ``` let AVMovieReferenceRestrictionsKey: NSString! ``` |
| To | ``` let AVMovieReferenceRestrictionsKey: String ``` |

Modified AVNumberOfChannelsKey

|  | Declaration |
| --- | --- |
| From | ``` let AVNumberOfChannelsKey: NSString! ``` |
| To | ``` let AVNumberOfChannelsKey: String ``` |

Modified AVOutputSettingsPreset1280x720

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVOutputSettingsPreset1280x720: NSString! ``` | OS X 10.10 |
| To | ``` let AVOutputSettingsPreset1280x720: String ``` | OS X 10.9 |

Modified AVOutputSettingsPreset1920x1080

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVOutputSettingsPreset1920x1080: NSString! ``` | OS X 10.10 |
| To | ``` let AVOutputSettingsPreset1920x1080: String ``` | OS X 10.9 |

Modified AVOutputSettingsPreset3840x2160

|  | Declaration |
| --- | --- |
| From | ``` let AVOutputSettingsPreset3840x2160: NSString! ``` |
| To | ``` let AVOutputSettingsPreset3840x2160: String ``` |

Modified AVOutputSettingsPreset640x480

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVOutputSettingsPreset640x480: NSString! ``` | OS X 10.10 |
| To | ``` let AVOutputSettingsPreset640x480: String ``` | OS X 10.9 |

Modified AVOutputSettingsPreset960x540

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVOutputSettingsPreset960x540: NSString! ``` | OS X 10.10 |
| To | ``` let AVOutputSettingsPreset960x540: String ``` | OS X 10.9 |

Modified AVPlayerItemDidPlayToEndTimeNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVPlayerItemDidPlayToEndTimeNotification: NSString! ``` | OS X 10.10 |
| To | ``` let AVPlayerItemDidPlayToEndTimeNotification: String ``` | OS X 10.7 |

Modified AVPlayerItemFailedToPlayToEndTimeErrorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVPlayerItemFailedToPlayToEndTimeErrorKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVPlayerItemFailedToPlayToEndTimeErrorKey: String ``` | OS X 10.7 |

Modified AVPlayerItemFailedToPlayToEndTimeNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVPlayerItemFailedToPlayToEndTimeNotification: NSString! ``` | OS X 10.10 |
| To | ``` let AVPlayerItemFailedToPlayToEndTimeNotification: String ``` | OS X 10.7 |

Modified AVPlayerItemLegibleOutputTextStylingResolutionDefault

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVPlayerItemLegibleOutputTextStylingResolutionDefault: NSString! ``` | OS X 10.10 |
| To | ``` let AVPlayerItemLegibleOutputTextStylingResolutionDefault: String ``` | OS X 10.9 |

Modified AVPlayerItemLegibleOutputTextStylingResolutionSourceAndRulesOnly

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVPlayerItemLegibleOutputTextStylingResolutionSourceAndRulesOnly: NSString! ``` | OS X 10.10 |
| To | ``` let AVPlayerItemLegibleOutputTextStylingResolutionSourceAndRulesOnly: String ``` | OS X 10.9 |

Modified AVPlayerItemNewAccessLogEntryNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVPlayerItemNewAccessLogEntryNotification: NSString! ``` | OS X 10.10 |
| To | ``` let AVPlayerItemNewAccessLogEntryNotification: String ``` | OS X 10.9 |

Modified AVPlayerItemNewErrorLogEntryNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVPlayerItemNewErrorLogEntryNotification: NSString! ``` | OS X 10.10 |
| To | ``` let AVPlayerItemNewErrorLogEntryNotification: String ``` | OS X 10.9 |

Modified AVPlayerItemPlaybackStalledNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVPlayerItemPlaybackStalledNotification: NSString! ``` | OS X 10.10 |
| To | ``` let AVPlayerItemPlaybackStalledNotification: String ``` | OS X 10.9 |

Modified AVPlayerItemTimeJumpedNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVPlayerItemTimeJumpedNotification: NSString! ``` | OS X 10.10 |
| To | ``` let AVPlayerItemTimeJumpedNotification: String ``` | OS X 10.7 |

Modified AVPlayerItemTrackVideoFieldModeDeinterlaceFields

|  | Declaration |
| --- | --- |
| From | ``` let AVPlayerItemTrackVideoFieldModeDeinterlaceFields: NSString! ``` |
| To | ``` let AVPlayerItemTrackVideoFieldModeDeinterlaceFields: String ``` |

Modified AVSampleBufferDisplayLayerFailedToDecodeNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVSampleBufferDisplayLayerFailedToDecodeNotification: NSString! ``` |
| To | ``` let AVSampleBufferDisplayLayerFailedToDecodeNotification: String ``` |

Modified AVSampleBufferDisplayLayerFailedToDecodeNotificationErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let AVSampleBufferDisplayLayerFailedToDecodeNotificationErrorKey: NSString! ``` |
| To | ``` let AVSampleBufferDisplayLayerFailedToDecodeNotificationErrorKey: String ``` |

Modified AVSampleRateConverterAlgorithmKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVSampleRateConverterAlgorithmKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVSampleRateConverterAlgorithmKey: String ``` | OS X 10.9 |

Modified AVSampleRateConverterAlgorithm_Mastering

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVSampleRateConverterAlgorithm_Mastering: NSString! ``` | OS X 10.10 |
| To | ``` let AVSampleRateConverterAlgorithm_Mastering: String ``` | OS X 10.9 |

Modified AVSampleRateConverterAlgorithm_Normal

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVSampleRateConverterAlgorithm_Normal: NSString! ``` | OS X 10.10 |
| To | ``` let AVSampleRateConverterAlgorithm_Normal: String ``` | OS X 10.9 |

Modified AVSampleRateConverterAudioQualityKey

|  | Declaration |
| --- | --- |
| From | ``` let AVSampleRateConverterAudioQualityKey: NSString! ``` |
| To | ``` let AVSampleRateConverterAudioQualityKey: String ``` |

Modified AVSampleRateKey

|  | Declaration |
| --- | --- |
| From | ``` let AVSampleRateKey: NSString! ``` |
| To | ``` let AVSampleRateKey: String ``` |

Modified AVTrackAssociationTypeAudioFallback

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVTrackAssociationTypeAudioFallback: NSString! ``` | OS X 10.10 |
| To | ``` let AVTrackAssociationTypeAudioFallback: String ``` | OS X 10.9 |

Modified AVTrackAssociationTypeChapterList

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVTrackAssociationTypeChapterList: NSString! ``` | OS X 10.10 |
| To | ``` let AVTrackAssociationTypeChapterList: String ``` | OS X 10.9 |

Modified AVTrackAssociationTypeForcedSubtitlesOnly

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVTrackAssociationTypeForcedSubtitlesOnly: NSString! ``` | OS X 10.10 |
| To | ``` let AVTrackAssociationTypeForcedSubtitlesOnly: String ``` | OS X 10.9 |

Modified AVTrackAssociationTypeMetadataReferent

|  | Declaration |
| --- | --- |
| From | ``` let AVTrackAssociationTypeMetadataReferent: NSString! ``` |
| To | ``` let AVTrackAssociationTypeMetadataReferent: String ``` |

Modified AVTrackAssociationTypeSelectionFollower

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVTrackAssociationTypeSelectionFollower: NSString! ``` | OS X 10.10 |
| To | ``` let AVTrackAssociationTypeSelectionFollower: String ``` | OS X 10.9 |

Modified AVTrackAssociationTypeTimecode

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVTrackAssociationTypeTimecode: NSString! ``` | OS X 10.10 |
| To | ``` let AVTrackAssociationTypeTimecode: String ``` | OS X 10.9 |

Modified AVURLAssetPreferPreciseDurationAndTimingKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVURLAssetPreferPreciseDurationAndTimingKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVURLAssetPreferPreciseDurationAndTimingKey: String ``` | OS X 10.7 |

Modified AVURLAssetReferenceRestrictionsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVURLAssetReferenceRestrictionsKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVURLAssetReferenceRestrictionsKey: String ``` | OS X 10.7 |

Modified AVVideoAllowFrameReorderingKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoAllowFrameReorderingKey: NSString! ``` |
| To | ``` let AVVideoAllowFrameReorderingKey: String ``` |

Modified AVVideoAverageBitRateKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoAverageBitRateKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoAverageBitRateKey: String ``` | OS X 10.7 |

Modified AVVideoAverageNonDroppableFrameRateKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoAverageNonDroppableFrameRateKey: NSString! ``` |
| To | ``` let AVVideoAverageNonDroppableFrameRateKey: String ``` |

Modified AVVideoCleanApertureHeightKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoCleanApertureHeightKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoCleanApertureHeightKey: String ``` | OS X 10.7 |

Modified AVVideoCleanApertureHorizontalOffsetKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoCleanApertureHorizontalOffsetKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoCleanApertureHorizontalOffsetKey: String ``` | OS X 10.7 |

Modified AVVideoCleanApertureKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoCleanApertureKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoCleanApertureKey: String ``` | OS X 10.7 |

Modified AVVideoCleanApertureVerticalOffsetKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoCleanApertureVerticalOffsetKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoCleanApertureVerticalOffsetKey: String ``` | OS X 10.7 |

Modified AVVideoCleanApertureWidthKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoCleanApertureWidthKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoCleanApertureWidthKey: String ``` | OS X 10.7 |

Modified AVVideoCodecAppleProRes422

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoCodecAppleProRes422: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoCodecAppleProRes422: String ``` | OS X 10.7 |

Modified AVVideoCodecAppleProRes4444

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoCodecAppleProRes4444: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoCodecAppleProRes4444: String ``` | OS X 10.7 |

Modified AVVideoCodecH264

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoCodecH264: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoCodecH264: String ``` | OS X 10.7 |

Modified AVVideoCodecJPEG

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoCodecJPEG: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoCodecJPEG: String ``` | OS X 10.7 |

Modified AVVideoCodecKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoCodecKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoCodecKey: String ``` | OS X 10.7 |

Modified AVVideoColorPrimariesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoColorPrimariesKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoColorPrimariesKey: String ``` | OS X 10.7 |

Modified AVVideoColorPrimaries_EBU_3213

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoColorPrimaries_EBU_3213: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoColorPrimaries_EBU_3213: String ``` | OS X 10.7 |

Modified AVVideoColorPrimaries_ITU_R_709_2

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoColorPrimaries_ITU_R_709_2: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoColorPrimaries_ITU_R_709_2: String ``` | OS X 10.7 |

Modified AVVideoColorPrimaries_SMPTE_C

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoColorPrimaries_SMPTE_C: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoColorPrimaries_SMPTE_C: String ``` | OS X 10.7 |

Modified AVVideoColorPropertiesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoColorPropertiesKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoColorPropertiesKey: String ``` | OS X 10.7 |

Modified AVVideoCompressionPropertiesKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoCompressionPropertiesKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoCompressionPropertiesKey: String ``` | OS X 10.7 |

Modified AVVideoEncoderSpecificationKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoEncoderSpecificationKey: NSString! ``` |
| To | ``` let AVVideoEncoderSpecificationKey: String ``` |

Modified AVVideoExpectedSourceFrameRateKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoExpectedSourceFrameRateKey: NSString! ``` |
| To | ``` let AVVideoExpectedSourceFrameRateKey: String ``` |

Modified AVVideoH264EntropyModeCABAC

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoH264EntropyModeCABAC: NSString! ``` |
| To | ``` let AVVideoH264EntropyModeCABAC: String ``` |

Modified AVVideoH264EntropyModeCAVLC

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoH264EntropyModeCAVLC: NSString! ``` |
| To | ``` let AVVideoH264EntropyModeCAVLC: String ``` |

Modified AVVideoH264EntropyModeKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoH264EntropyModeKey: NSString! ``` |
| To | ``` let AVVideoH264EntropyModeKey: String ``` |

Modified AVVideoHeightKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoHeightKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoHeightKey: String ``` | OS X 10.7 |

Modified AVVideoMaxKeyFrameIntervalDurationKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoMaxKeyFrameIntervalDurationKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoMaxKeyFrameIntervalDurationKey: String ``` | OS X 10.9 |

Modified AVVideoMaxKeyFrameIntervalKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoMaxKeyFrameIntervalKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoMaxKeyFrameIntervalKey: String ``` | OS X 10.7 |

Modified AVVideoPixelAspectRatioHorizontalSpacingKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoPixelAspectRatioHorizontalSpacingKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoPixelAspectRatioHorizontalSpacingKey: String ``` | OS X 10.7 |

Modified AVVideoPixelAspectRatioKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoPixelAspectRatioKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoPixelAspectRatioKey: String ``` | OS X 10.7 |

Modified AVVideoPixelAspectRatioVerticalSpacingKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoPixelAspectRatioVerticalSpacingKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoPixelAspectRatioVerticalSpacingKey: String ``` | OS X 10.7 |

Modified AVVideoProfileLevelH264Baseline30

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoProfileLevelH264Baseline30: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoProfileLevelH264Baseline30: String ``` | OS X 10.8 |

Modified AVVideoProfileLevelH264Baseline31

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoProfileLevelH264Baseline31: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoProfileLevelH264Baseline31: String ``` | OS X 10.8 |

Modified AVVideoProfileLevelH264Baseline41

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoProfileLevelH264Baseline41: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoProfileLevelH264Baseline41: String ``` | OS X 10.8 |

Modified AVVideoProfileLevelH264BaselineAutoLevel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoProfileLevelH264BaselineAutoLevel: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoProfileLevelH264BaselineAutoLevel: String ``` | OS X 10.9 |

Modified AVVideoProfileLevelH264High40

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoProfileLevelH264High40: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoProfileLevelH264High40: String ``` | OS X 10.9 |

Modified AVVideoProfileLevelH264High41

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoProfileLevelH264High41: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoProfileLevelH264High41: String ``` | OS X 10.9 |

Modified AVVideoProfileLevelH264HighAutoLevel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoProfileLevelH264HighAutoLevel: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoProfileLevelH264HighAutoLevel: String ``` | OS X 10.9 |

Modified AVVideoProfileLevelH264Main30

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoProfileLevelH264Main30: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoProfileLevelH264Main30: String ``` | OS X 10.8 |

Modified AVVideoProfileLevelH264Main31

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoProfileLevelH264Main31: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoProfileLevelH264Main31: String ``` | OS X 10.8 |

Modified AVVideoProfileLevelH264Main32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoProfileLevelH264Main32: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoProfileLevelH264Main32: String ``` | OS X 10.8 |

Modified AVVideoProfileLevelH264Main41

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoProfileLevelH264Main41: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoProfileLevelH264Main41: String ``` | OS X 10.8 |

Modified AVVideoProfileLevelH264MainAutoLevel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoProfileLevelH264MainAutoLevel: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoProfileLevelH264MainAutoLevel: String ``` | OS X 10.9 |

Modified AVVideoProfileLevelKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoProfileLevelKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoProfileLevelKey: String ``` | OS X 10.8 |

Modified AVVideoQualityKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoQualityKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoQualityKey: String ``` | OS X 10.7 |

Modified AVVideoScalingModeFit

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoScalingModeFit: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoScalingModeFit: String ``` | OS X 10.7 |

Modified AVVideoScalingModeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoScalingModeKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoScalingModeKey: String ``` | OS X 10.7 |

Modified AVVideoScalingModeResize

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoScalingModeResize: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoScalingModeResize: String ``` | OS X 10.7 |

Modified AVVideoScalingModeResizeAspect

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoScalingModeResizeAspect: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoScalingModeResizeAspect: String ``` | OS X 10.7 |

Modified AVVideoScalingModeResizeAspectFill

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoScalingModeResizeAspectFill: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoScalingModeResizeAspectFill: String ``` | OS X 10.7 |

Modified AVVideoTransferFunctionKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoTransferFunctionKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoTransferFunctionKey: String ``` | OS X 10.7 |

Modified AVVideoTransferFunction_ITU_R_709_2

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoTransferFunction_ITU_R_709_2: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoTransferFunction_ITU_R_709_2: String ``` | OS X 10.7 |

Modified AVVideoTransferFunction_SMPTE_240M_1995

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoTransferFunction_SMPTE_240M_1995: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoTransferFunction_SMPTE_240M_1995: String ``` | OS X 10.7 |

Modified AVVideoWidthKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoWidthKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoWidthKey: String ``` | OS X 10.7 |

Modified AVVideoYCbCrMatrixKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoYCbCrMatrixKey: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoYCbCrMatrixKey: String ``` | OS X 10.7 |

Modified AVVideoYCbCrMatrix_ITU_R_601_4

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoYCbCrMatrix_ITU_R_601_4: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoYCbCrMatrix_ITU_R_601_4: String ``` | OS X 10.7 |

Modified AVVideoYCbCrMatrix_ITU_R_709_2

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoYCbCrMatrix_ITU_R_709_2: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoYCbCrMatrix_ITU_R_709_2: String ``` | OS X 10.7 |

Modified AVVideoYCbCrMatrix_SMPTE_240M_1995

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let AVVideoYCbCrMatrix_SMPTE_240M_1995: NSString! ``` | OS X 10.10 |
| To | ``` let AVVideoYCbCrMatrix_SMPTE_240M_1995: String ``` | OS X 10.7 |

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
