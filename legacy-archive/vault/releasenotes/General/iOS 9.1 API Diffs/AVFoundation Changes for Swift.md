---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/AVFoundation.html
archived_at: '2026-07-18T02:57:05.449820Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# AVFoundation Changes for Swift

### AVFoundation

Modified [AVAsset](https://developer.apple.com/documentation/avfoundation/avasset)

|  | Protocols |
| --- | --- |
| From | AVAsynchronousKeyValueLoading, AnyObject, NSCopying |
| To | AVAsynchronousKeyValueLoading, NSCopying |

Modified [AVAssetDownloadDelegate](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol AVAssetDownloadDelegate : NSURLSessionTaskDelegate, NSURLSessionDelegate, NSObjectProtocol {     optional func URLSession(_ session: NSURLSession, assetDownloadTask assetDownloadTask: AVAssetDownloadTask, didLoadTimeRange timeRange: CMTimeRange, totalTimeRangesLoaded loadedTimeRanges: [NSValue], timeRangeExpectedToLoad timeRangeExpectedToLoad: CMTimeRange)     optional func URLSession(_ session: NSURLSession, assetDownloadTask assetDownloadTask: AVAssetDownloadTask, didResolveMediaSelection resolvedMediaSelection: AVMediaSelection) } ``` | NSObjectProtocol, NSURLSessionDelegate, NSURLSessionTaskDelegate |
| To | ``` protocol AVAssetDownloadDelegate : NSURLSessionTaskDelegate {     optional func URLSession(_ session: NSURLSession, assetDownloadTask assetDownloadTask: AVAssetDownloadTask, didLoadTimeRange timeRange: CMTimeRange, totalTimeRangesLoaded loadedTimeRanges: [NSValue], timeRangeExpectedToLoad timeRangeExpectedToLoad: CMTimeRange)     optional func URLSession(_ session: NSURLSession, assetDownloadTask assetDownloadTask: AVAssetDownloadTask, didResolveMediaSelection resolvedMediaSelection: AVMediaSelection) } ``` | NSURLSessionTaskDelegate |

Modified [AVAssetDownloadTask](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetDownloadURLSession](https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetExportSession](https://developer.apple.com/documentation/avfoundation/avassetexportsession)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetExportSessionStatus [enum]](https://developer.apple.com/documentation/avfoundation/avassetexportsession/status)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVAssetImageGenerator](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetImageGeneratorResult [enum]](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/result)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVAssetReader](https://developer.apple.com/documentation/avfoundation/avassetreader)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetReaderAudioMixOutput](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetReaderOutput](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetReaderOutputMetadataAdaptor](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputmetadataadaptor)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetReaderSampleReferenceOutput](https://developer.apple.com/documentation/avfoundation/avassetreadersamplereferenceoutput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetReaderStatus [enum]](https://developer.apple.com/documentation/avfoundation/avassetreader/status)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVAssetReaderTrackOutput](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetReaderVideoCompositionOutput](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetResourceLoader](https://developer.apple.com/documentation/avfoundation/avassetresourceloader)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetResourceLoadingContentInformationRequest](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetResourceLoadingDataRequest](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetResourceLoadingRequest](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetResourceRenewalRequest](https://developer.apple.com/documentation/avfoundation/avassetresourcerenewalrequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetTrack](https://developer.apple.com/documentation/avfoundation/avassettrack)

|  | Protocols |
| --- | --- |
| From | AVAsynchronousKeyValueLoading, AnyObject, NSCopying |
| To | AVAsynchronousKeyValueLoading, NSCopying |

Modified [AVAssetTrackGroup](https://developer.apple.com/documentation/avfoundation/avassettrackgroup)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [AVAssetTrackSegment](https://developer.apple.com/documentation/avfoundation/avassettracksegment)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetWriter](https://developer.apple.com/documentation/avfoundation/avassetwriter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetWriterInput](https://developer.apple.com/documentation/avfoundation/avassetwriterinput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetWriterInputGroup](https://developer.apple.com/documentation/avfoundation/avassetwriterinputgroup)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetWriterInputMetadataAdaptor](https://developer.apple.com/documentation/avfoundation/avassetwriterinputmetadataadaptor)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetWriterInputPassDescription](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpassdescription)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetWriterInputPixelBufferAdaptor](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAssetWriterStatus [enum]](https://developer.apple.com/documentation/avfoundation/avassetwriter/status)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVAsynchronousCIImageFilteringRequest](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [AVAsynchronousVideoCompositionRequest](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [AVAudio3DMixingRenderingAlgorithm [enum]](https://developer.apple.com/documentation/avfoundation/avaudio3dmixingrenderingalgorithm)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVAudioBuffer](https://developer.apple.com/documentation/avfoundation/avaudiobuffer)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying |

Modified [AVAudioChannelLayout](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioChannelLayout : NSObject, NSSecureCoding, NSCoding {     convenience init(layoutTag layoutTag: AudioChannelLayoutTag)     init(layout layout: UnsafePointer<AudioChannelLayout>)     func isEqual(_ object: AnyObject) -> Bool     class func layoutWithLayoutTag(_ layoutTag: AudioChannelLayoutTag) -> Self     class func layoutWithLayout(_ layout: UnsafePointer<AudioChannelLayout>) -> Self     var layoutTag: AudioChannelLayoutTag { get }     var layout: UnsafePointer<AudioChannelLayout> { get }     var channelCount: AVAudioChannelCount { get } } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class AVAudioChannelLayout : NSObject, NSSecureCoding {     convenience init(layoutTag layoutTag: AudioChannelLayoutTag)     init(layout layout: UnsafePointer<AudioChannelLayout>)     func isEqual(_ object: AnyObject) -> Bool     class func layoutWithLayoutTag(_ layoutTag: AudioChannelLayoutTag) -> Self     class func layoutWithLayout(_ layout: UnsafePointer<AudioChannelLayout>) -> Self     var layoutTag: AudioChannelLayoutTag { get }     var layout: UnsafePointer<AudioChannelLayout> { get }     var channelCount: AVAudioChannelCount { get } } ``` | NSSecureCoding |

Modified [AVAudioCommonFormat [enum]](https://developer.apple.com/documentation/avfoundation/avaudiocommonformat)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVAudioCompressedBuffer](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioConnectionPoint](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioConverter](https://developer.apple.com/documentation/avfoundation/avaudioconverter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioConverterInputStatus [enum]](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVAudioConverterOutputStatus [enum]](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVAudioConverterPrimeMethod [enum]](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVAudioEngine](https://developer.apple.com/documentation/avfoundation/avaudioengine)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioEnvironmentDistanceAttenuationModel [enum]](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationmodel)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVAudioEnvironmentDistanceAttenuationParameters](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationparameters)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioEnvironmentNode](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioEnvironmentNode : AVAudioNode, AVAudioMixing, AVAudioStereoMixing, AVAudio3DMixing {     var outputVolume: Float     var nextAvailableInputBus: AVAudioNodeBus { get }     var listenerPosition: AVAudio3DPoint     var listenerVectorOrientation: AVAudio3DVectorOrientation     var listenerAngularOrientation: AVAudio3DAngularOrientation     var distanceAttenuationParameters: AVAudioEnvironmentDistanceAttenuationParameters { get }     var reverbParameters: AVAudioEnvironmentReverbParameters { get }     var applicableRenderingAlgorithms: [NSNumber] { get } } ``` | AVAudio3DMixing, AVAudioMixing, AVAudioStereoMixing, AnyObject, NSObjectProtocol |
| To | ``` class AVAudioEnvironmentNode : AVAudioNode, AVAudioMixing {     var outputVolume: Float     var nextAvailableInputBus: AVAudioNodeBus { get }     var listenerPosition: AVAudio3DPoint     var listenerVectorOrientation: AVAudio3DVectorOrientation     var listenerAngularOrientation: AVAudio3DAngularOrientation     var distanceAttenuationParameters: AVAudioEnvironmentDistanceAttenuationParameters { get }     var reverbParameters: AVAudioEnvironmentReverbParameters { get }     var applicableRenderingAlgorithms: [NSNumber] { get } } ``` | AVAudioMixing |

Modified [AVAudioEnvironmentReverbParameters](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentreverbparameters)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioFile](https://developer.apple.com/documentation/avfoundation/avaudiofile)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioFormat](https://developer.apple.com/documentation/avfoundation/avaudioformat)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioFormat : NSObject, NSSecureCoding, NSCoding {     init(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>)     init(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>, channelLayout layout: AVAudioChannelLayout?)     init(standardFormatWithSampleRate sampleRate: Double, channels channels: AVAudioChannelCount)     init(standardFormatWithSampleRate sampleRate: Double, channelLayout layout: AVAudioChannelLayout)     init(commonFormat format: AVAudioCommonFormat, sampleRate sampleRate: Double, channels channels: AVAudioChannelCount, interleaved interleaved: Bool)     init(commonFormat format: AVAudioCommonFormat, sampleRate sampleRate: Double, interleaved interleaved: Bool, channelLayout layout: AVAudioChannelLayout)     init(settings settings: [String : AnyObject])     init(CMAudioFormatDescription formatDescription: CMAudioFormatDescription)     func isEqual(_ object: AnyObject) -> Bool     var standard: Bool { get }     var commonFormat: AVAudioCommonFormat { get }     var channelCount: AVAudioChannelCount { get }     var sampleRate: Double { get }     var interleaved: Bool { get }     var streamDescription: UnsafePointer<AudioStreamBasicDescription> { get }     var channelLayout: AVAudioChannelLayout? { get }     var settings: [String : AnyObject] { get }     var formatDescription: CMAudioFormatDescription { get } } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class AVAudioFormat : NSObject, NSSecureCoding {     init(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>)     init(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>, channelLayout layout: AVAudioChannelLayout?)     init(standardFormatWithSampleRate sampleRate: Double, channels channels: AVAudioChannelCount)     init(standardFormatWithSampleRate sampleRate: Double, channelLayout layout: AVAudioChannelLayout)     init(commonFormat format: AVAudioCommonFormat, sampleRate sampleRate: Double, channels channels: AVAudioChannelCount, interleaved interleaved: Bool)     init(commonFormat format: AVAudioCommonFormat, sampleRate sampleRate: Double, interleaved interleaved: Bool, channelLayout layout: AVAudioChannelLayout)     init(settings settings: [String : AnyObject])     init(CMAudioFormatDescription formatDescription: CMAudioFormatDescription)     func isEqual(_ object: AnyObject) -> Bool     var standard: Bool { get }     var commonFormat: AVAudioCommonFormat { get }     var channelCount: AVAudioChannelCount { get }     var sampleRate: Double { get }     var interleaved: Bool { get }     var streamDescription: UnsafePointer<AudioStreamBasicDescription> { get }     var channelLayout: AVAudioChannelLayout? { get }     var settings: [String : AnyObject] { get }     var formatDescription: CMAudioFormatDescription { get } } ``` | NSSecureCoding |

Modified [AVAudioInputNode](https://developer.apple.com/documentation/avfoundation/avaudioinputnode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioInputNode : AVAudioIONode, AVAudioMixing, AVAudioStereoMixing, AVAudio3DMixing { } ``` | AVAudio3DMixing, AVAudioMixing, AVAudioStereoMixing, AnyObject, NSObjectProtocol |
| To | ``` class AVAudioInputNode : AVAudioIONode, AVAudioMixing { } ``` | AVAudioMixing |

Modified [AVAudioIONode](https://developer.apple.com/documentation/avfoundation/avaudioionode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioMix](https://developer.apple.com/documentation/avfoundation/avaudiomix)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying |

Modified [AVAudioMixerNode](https://developer.apple.com/documentation/avfoundation/avaudiomixernode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioMixerNode : AVAudioNode, AVAudioMixing, AVAudioStereoMixing, AVAudio3DMixing {     var outputVolume: Float     var nextAvailableInputBus: AVAudioNodeBus { get } } ``` | AVAudio3DMixing, AVAudioMixing, AVAudioStereoMixing, AnyObject, NSObjectProtocol |
| To | ``` class AVAudioMixerNode : AVAudioNode, AVAudioMixing {     var outputVolume: Float     var nextAvailableInputBus: AVAudioNodeBus { get } } ``` | AVAudioMixing |

Modified [AVAudioMixing](https://developer.apple.com/documentation/avfoundation/avaudiomixing)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol AVAudioMixing : AVAudioStereoMixing, NSObjectProtocol, AVAudio3DMixing {     func destinationForMixer(_ mixer: AVAudioNode, bus bus: AVAudioNodeBus) -> AVAudioMixingDestination?     var volume: Float { get set } } ``` | AVAudio3DMixing, AVAudioStereoMixing, NSObjectProtocol |
| To | ``` protocol AVAudioMixing : AVAudioStereoMixing, AVAudio3DMixing {     func destinationForMixer(_ mixer: AVAudioNode, bus bus: AVAudioNodeBus) -> AVAudioMixingDestination?     var volume: Float { get set } } ``` | AVAudio3DMixing, AVAudioStereoMixing |

Modified [AVAudioMixingDestination](https://developer.apple.com/documentation/avfoundation/avaudiomixingdestination)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioMixingDestination : NSObject, AVAudioMixing, AVAudioStereoMixing, AVAudio3DMixing {     var connectionPoint: AVAudioConnectionPoint { get } } ``` | AVAudio3DMixing, AVAudioMixing, AVAudioStereoMixing, AnyObject, NSObjectProtocol |
| To | ``` class AVAudioMixingDestination : NSObject, AVAudioMixing {     var connectionPoint: AVAudioConnectionPoint { get } } ``` | AVAudioMixing |

Modified [AVAudioMixInputParameters](https://developer.apple.com/documentation/avfoundation/avaudiomixinputparameters)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying |

Modified [AVAudioNode](https://developer.apple.com/documentation/avfoundation/avaudionode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioOutputNode](https://developer.apple.com/documentation/avfoundation/avaudiooutputnode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioPCMBuffer](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioPlayer](https://developer.apple.com/documentation/avfoundation/avaudioplayer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioPlayerNode](https://developer.apple.com/documentation/avfoundation/avaudioplayernode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioPlayerNode : AVAudioNode, AVAudioMixing, AVAudioStereoMixing, AVAudio3DMixing {     func scheduleBuffer(_ buffer: AVAudioPCMBuffer, completionHandler completionHandler: AVAudioNodeCompletionHandler?)     func scheduleBuffer(_ buffer: AVAudioPCMBuffer, atTime when: AVAudioTime?, options options: AVAudioPlayerNodeBufferOptions, completionHandler completionHandler: AVAudioNodeCompletionHandler?)     func scheduleFile(_ file: AVAudioFile, atTime when: AVAudioTime?, completionHandler completionHandler: AVAudioNodeCompletionHandler?)     func scheduleSegment(_ file: AVAudioFile, startingFrame startFrame: AVAudioFramePosition, frameCount numberFrames: AVAudioFrameCount, atTime when: AVAudioTime?, completionHandler completionHandler: AVAudioNodeCompletionHandler?)     func stop()     func prepareWithFrameCount(_ frameCount: AVAudioFrameCount)     func play()     func playAtTime(_ when: AVAudioTime?)     func pause()     func nodeTimeForPlayerTime(_ playerTime: AVAudioTime) -> AVAudioTime?     func playerTimeForNodeTime(_ nodeTime: AVAudioTime) -> AVAudioTime?     var playing: Bool { get } } ``` | AVAudio3DMixing, AVAudioMixing, AVAudioStereoMixing, AnyObject, NSObjectProtocol |
| To | ``` class AVAudioPlayerNode : AVAudioNode, AVAudioMixing {     func scheduleBuffer(_ buffer: AVAudioPCMBuffer, completionHandler completionHandler: AVAudioNodeCompletionHandler?)     func scheduleBuffer(_ buffer: AVAudioPCMBuffer, atTime when: AVAudioTime?, options options: AVAudioPlayerNodeBufferOptions, completionHandler completionHandler: AVAudioNodeCompletionHandler?)     func scheduleFile(_ file: AVAudioFile, atTime when: AVAudioTime?, completionHandler completionHandler: AVAudioNodeCompletionHandler?)     func scheduleSegment(_ file: AVAudioFile, startingFrame startFrame: AVAudioFramePosition, frameCount numberFrames: AVAudioFrameCount, atTime when: AVAudioTime?, completionHandler completionHandler: AVAudioNodeCompletionHandler?)     func stop()     func prepareWithFrameCount(_ frameCount: AVAudioFrameCount)     func play()     func playAtTime(_ when: AVAudioTime?)     func pause()     func nodeTimeForPlayerTime(_ playerTime: AVAudioTime) -> AVAudioTime?     func playerTimeForNodeTime(_ nodeTime: AVAudioTime) -> AVAudioTime?     var playing: Bool { get } } ``` | AVAudioMixing |

Modified [AVAudioQuality [enum]](https://developer.apple.com/documentation/avfoundation/avaudioquality)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVAudioRecorder](https://developer.apple.com/documentation/avfoundation/avaudiorecorder)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioSequencer](https://developer.apple.com/documentation/avfoundation/avaudiosequencer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioSession](https://developer.apple.com/documentation/avfoundation/avaudiosession)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioSessionChannelDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessionchanneldescription)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioSessionDataSourceDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioSessionErrorCode [enum]](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVAudioSessionInterruptionType [enum]](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptiontype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVAudioSessionPortDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioSessionPortOverride [enum]](https://developer.apple.com/documentation/avfoundation/avaudiosession/portoverride)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVAudioSessionRouteChangeReason [enum]](https://developer.apple.com/documentation/avfoundation/avaudiosession/routechangereason)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVAudioSessionRouteDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutedescription)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioSessionSilenceSecondaryAudioHintType [enum]](https://developer.apple.com/documentation/avfoundation/avaudiosession/silencesecondaryaudiohinttype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVAudioTime](https://developer.apple.com/documentation/avfoundation/avaudiotime)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioUnit](https://developer.apple.com/documentation/avfoundation/avaudiounit)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioUnitComponent](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioUnitComponentManager](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioUnitDelay](https://developer.apple.com/documentation/avfoundation/avaudiounitdelay)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioUnitDistortion](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortion)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioUnitDistortionPreset [enum]](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVAudioUnitEffect](https://developer.apple.com/documentation/avfoundation/avaudiouniteffect)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioUnitEQ](https://developer.apple.com/documentation/avfoundation/avaudiouniteq)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioUnitEQFilterParameters](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfilterparameters)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioUnitEQFilterType [enum]](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVAudioUnitGenerator](https://developer.apple.com/documentation/avfoundation/avaudiounitgenerator)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioUnitGenerator : AVAudioUnit, AVAudioMixing, AVAudioStereoMixing, AVAudio3DMixing {     init(audioComponentDescription audioComponentDescription: AudioComponentDescription)     var bypass: Bool } ``` | AVAudio3DMixing, AVAudioMixing, AVAudioStereoMixing, AnyObject, NSObjectProtocol |
| To | ``` class AVAudioUnitGenerator : AVAudioUnit, AVAudioMixing {     init(audioComponentDescription audioComponentDescription: AudioComponentDescription)     var bypass: Bool } ``` | AVAudioMixing |

Modified [AVAudioUnitMIDIInstrument](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioUnitMIDIInstrument : AVAudioUnit, AVAudioMixing, AVAudioStereoMixing, AVAudio3DMixing {     init(audioComponentDescription description: AudioComponentDescription)     func startNote(_ note: UInt8, withVelocity velocity: UInt8, onChannel channel: UInt8)     func stopNote(_ note: UInt8, onChannel channel: UInt8)     func sendController(_ controller: UInt8, withValue value: UInt8, onChannel channel: UInt8)     func sendPitchBend(_ pitchbend: UInt16, onChannel channel: UInt8)     func sendPressure(_ pressure: UInt8, onChannel channel: UInt8)     func sendPressureForKey(_ key: UInt8, withValue value: UInt8, onChannel channel: UInt8)     func sendProgramChange(_ program: UInt8, onChannel channel: UInt8)     func sendProgramChange(_ program: UInt8, bankMSB bankMSB: UInt8, bankLSB bankLSB: UInt8, onChannel channel: UInt8)     func sendMIDIEvent(_ midiStatus: UInt8, data1 data1: UInt8, data2 data2: UInt8)     func sendMIDIEvent(_ midiStatus: UInt8, data1 data1: UInt8)     func sendMIDISysExEvent(_ midiData: NSData) } ``` | AVAudio3DMixing, AVAudioMixing, AVAudioStereoMixing, AnyObject, NSObjectProtocol |
| To | ``` class AVAudioUnitMIDIInstrument : AVAudioUnit, AVAudioMixing {     init(audioComponentDescription description: AudioComponentDescription)     func startNote(_ note: UInt8, withVelocity velocity: UInt8, onChannel channel: UInt8)     func stopNote(_ note: UInt8, onChannel channel: UInt8)     func sendController(_ controller: UInt8, withValue value: UInt8, onChannel channel: UInt8)     func sendPitchBend(_ pitchbend: UInt16, onChannel channel: UInt8)     func sendPressure(_ pressure: UInt8, onChannel channel: UInt8)     func sendPressureForKey(_ key: UInt8, withValue value: UInt8, onChannel channel: UInt8)     func sendProgramChange(_ program: UInt8, onChannel channel: UInt8)     func sendProgramChange(_ program: UInt8, bankMSB bankMSB: UInt8, bankLSB bankLSB: UInt8, onChannel channel: UInt8)     func sendMIDIEvent(_ midiStatus: UInt8, data1 data1: UInt8, data2 data2: UInt8)     func sendMIDIEvent(_ midiStatus: UInt8, data1 data1: UInt8)     func sendMIDISysExEvent(_ midiData: NSData) } ``` | AVAudioMixing |

Modified [AVAudioUnitReverb](https://developer.apple.com/documentation/avfoundation/avaudiounitreverb)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioUnitReverbPreset [enum]](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVAudioUnitSampler](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioUnitTimeEffect](https://developer.apple.com/documentation/avfoundation/avaudiounittimeeffect)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioUnitTimePitch](https://developer.apple.com/documentation/avfoundation/avaudiounittimepitch)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAudioUnitVarispeed](https://developer.apple.com/documentation/avfoundation/avaudiounitvarispeed)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVAuthorizationStatus [enum]](https://developer.apple.com/documentation/avfoundation/avauthorizationstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVCaptureAudioChannel](https://developer.apple.com/documentation/avfoundation/avcaptureaudiochannel)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVCaptureAudioDataOutput](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVCaptureAutoExposureBracketedStillImageSettings](https://developer.apple.com/documentation/avfoundation/avcaptureautoexposurebracketedstillimagesettings)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVCaptureAutoFocusRangeRestriction [enum]](https://developer.apple.com/documentation/avfoundation/avcaptureautofocusrangerestriction)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVCaptureAutoFocusSystem [enum]](https://developer.apple.com/documentation/avfoundation/avcaptureautofocussystem)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVCaptureBracketedStillImageSettings](https://developer.apple.com/documentation/avfoundation/avcapturebracketedstillimagesettings)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVCaptureConnection](https://developer.apple.com/documentation/avfoundation/avcaptureconnection)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVCaptureDevice](https://developer.apple.com/documentation/avfoundation/avcapturedevice)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVCaptureDeviceFormat](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVCaptureDeviceInput](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVCaptureDevicePosition [enum]](https://developer.apple.com/documentation/avfoundation/avcapturedeviceposition)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVCaptureExposureMode [enum]](https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposuremode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVCaptureFileOutput](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVCaptureFlashMode [enum]](https://developer.apple.com/documentation/avfoundation/avcapturedevice/flashmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVCaptureFocusMode [enum]](https://developer.apple.com/documentation/avfoundation/avcapturedevice/focusmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVCaptureInput](https://developer.apple.com/documentation/avfoundation/avcaptureinput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVCaptureInputPort](https://developer.apple.com/documentation/avfoundation/avcaptureinputport)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVCaptureManualExposureBracketedStillImageSettings](https://developer.apple.com/documentation/avfoundation/avcapturemanualexposurebracketedstillimagesettings)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVCaptureMetadataInput](https://developer.apple.com/documentation/avfoundation/avcapturemetadatainput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVCaptureMetadataOutput](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVCaptureMovieFileOutput](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVCaptureOutput](https://developer.apple.com/documentation/avfoundation/avcaptureoutput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVCaptureSession](https://developer.apple.com/documentation/avfoundation/avcapturesession)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVCaptureSessionInterruptionReason [enum]](https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionreason)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVCaptureStillImageOutput](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVCaptureTorchMode [enum]](https://developer.apple.com/documentation/avfoundation/avcapturedevice/torchmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVCaptureVideoDataOutput](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVCaptureVideoOrientation [enum]](https://developer.apple.com/documentation/avfoundation/avcapturevideoorientation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVCaptureVideoPreviewLayer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVCaptureVideoStabilizationMode [enum]](https://developer.apple.com/documentation/avfoundation/avcapturevideostabilizationmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVCaptureWhiteBalanceMode [enum]](https://developer.apple.com/documentation/avfoundation/avcapturedevice/whitebalancemode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVComposition](https://developer.apple.com/documentation/avfoundation/avcomposition)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSMutableCopying |
| To | NSMutableCopying |

Modified [AVCompositionTrack](https://developer.apple.com/documentation/avfoundation/avcompositiontrack)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVCompositionTrackSegment](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVDateRangeMetadataGroup](https://developer.apple.com/documentation/avfoundation/avdaterangemetadatagroup)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying |

Modified [AVError [enum]](https://developer.apple.com/documentation/avfoundation/averror/code)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum AVError : Int {     case Unknown     case OutOfMemory     case SessionNotRunning     case DeviceAlreadyUsedByAnotherSession     case NoDataCaptured     case SessionConfigurationChanged     case DiskFull     case DeviceWasDisconnected     case MediaChanged     case MaximumDurationReached     case MaximumFileSizeReached     case MediaDiscontinuity     case MaximumNumberOfSamplesForFileFormatReached     case DeviceNotConnected     case DeviceInUseByAnotherApplication     case DeviceLockedForConfigurationByAnotherProcess     case SessionWasInterrupted     case MediaServicesWereReset     case ExportFailed     case DecodeFailed     case InvalidSourceMedia     case FileAlreadyExists     case CompositionTrackSegmentsNotContiguous     case InvalidCompositionTrackSegmentDuration     case InvalidCompositionTrackSegmentSourceStartTime     case InvalidCompositionTrackSegmentSourceDuration     case FileFormatNotRecognized     case FileFailedToParse     case MaximumStillImageCaptureRequestsExceeded     case ContentIsProtected     case NoImageAtTime     case DecoderNotFound     case EncoderNotFound     case ContentIsNotAuthorized     case ApplicationIsNotAuthorized     case DeviceIsNotAvailableInBackground     case OperationNotSupportedForAsset     case DecoderTemporarilyUnavailable     case EncoderTemporarilyUnavailable     case InvalidVideoComposition     case ReferenceForbiddenByReferencePolicy     case InvalidOutputURLPathExtension     case ScreenCaptureFailed     case DisplayWasDisabled     case TorchLevelUnavailable     case OperationInterrupted     case IncompatibleAsset     case FailedToLoadMediaData     case ServerIncorrectlyConfigured     case ApplicationIsNotAuthorizedToUseDevice     case FailedToParse     case FileTypeDoesNotSupportSampleReferences     case UndecodableMediaData     case AirPlayControllerRequiresInternet     case AirPlayReceiverRequiresInternet     case VideoCompositorFailed     case RecordingAlreadyInProgress } extension AVError : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension AVError : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable |
| To | ``` enum AVError : Int {     case Unknown     case OutOfMemory     case SessionNotRunning     case DeviceAlreadyUsedByAnotherSession     case NoDataCaptured     case SessionConfigurationChanged     case DiskFull     case DeviceWasDisconnected     case MediaChanged     case MaximumDurationReached     case MaximumFileSizeReached     case MediaDiscontinuity     case MaximumNumberOfSamplesForFileFormatReached     case DeviceNotConnected     case DeviceInUseByAnotherApplication     case DeviceLockedForConfigurationByAnotherProcess     case SessionWasInterrupted     case MediaServicesWereReset     case ExportFailed     case DecodeFailed     case InvalidSourceMedia     case FileAlreadyExists     case CompositionTrackSegmentsNotContiguous     case InvalidCompositionTrackSegmentDuration     case InvalidCompositionTrackSegmentSourceStartTime     case InvalidCompositionTrackSegmentSourceDuration     case FileFormatNotRecognized     case FileFailedToParse     case MaximumStillImageCaptureRequestsExceeded     case ContentIsProtected     case NoImageAtTime     case DecoderNotFound     case EncoderNotFound     case ContentIsNotAuthorized     case ApplicationIsNotAuthorized     case DeviceIsNotAvailableInBackground     case OperationNotSupportedForAsset     case DecoderTemporarilyUnavailable     case EncoderTemporarilyUnavailable     case InvalidVideoComposition     case ReferenceForbiddenByReferencePolicy     case InvalidOutputURLPathExtension     case ScreenCaptureFailed     case DisplayWasDisabled     case TorchLevelUnavailable     case OperationInterrupted     case IncompatibleAsset     case FailedToLoadMediaData     case ServerIncorrectlyConfigured     case ApplicationIsNotAuthorizedToUseDevice     case FailedToParse     case FileTypeDoesNotSupportSampleReferences     case UndecodableMediaData     case AirPlayControllerRequiresInternet     case AirPlayReceiverRequiresInternet     case VideoCompositorFailed     case RecordingAlreadyInProgress } extension AVError : _BridgedNSError { } extension AVError : _BridgedNSError { } ``` | -- |

Modified [AVFrameRateRange](https://developer.apple.com/documentation/avfoundation/avframeraterange)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVKeyValueStatus [enum]](https://developer.apple.com/documentation/avfoundation/avkeyvaluestatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVMediaSelection](https://developer.apple.com/documentation/avfoundation/avmediaselection)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying |

Modified [AVMediaSelectionGroup](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [AVMediaSelectionOption](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [AVMetadataFaceObject](https://developer.apple.com/documentation/avfoundation/avmetadatafaceobject)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [AVMetadataGroup](https://developer.apple.com/documentation/avfoundation/avmetadatagroup)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVMetadataItem](https://developer.apple.com/documentation/avfoundation/avmetadataitem)

|  | Protocols |
| --- | --- |
| From | AVAsynchronousKeyValueLoading, AnyObject, NSCopying, NSMutableCopying |
| To | AVAsynchronousKeyValueLoading, NSCopying, NSMutableCopying |

Modified [AVMetadataItemFilter](https://developer.apple.com/documentation/avfoundation/avmetadataitemfilter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVMetadataItemValueRequest](https://developer.apple.com/documentation/avfoundation/avmetadataitemvaluerequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVMetadataMachineReadableCodeObject](https://developer.apple.com/documentation/avfoundation/avmetadatamachinereadablecodeobject)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVMetadataObject](https://developer.apple.com/documentation/avfoundation/avmetadataobject)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVMIDIPlayer](https://developer.apple.com/documentation/avfoundation/avmidiplayer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVMusicTrack](https://developer.apple.com/documentation/avfoundation/avmusictrack)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVMusicTrackLoopCount [enum]](https://developer.apple.com/documentation/avfoundation/avmusictrackloopcount)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVMutableAudioMix](https://developer.apple.com/documentation/avfoundation/avmutableaudiomix)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVMutableAudioMixInputParameters](https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVMutableComposition](https://developer.apple.com/documentation/avfoundation/avmutablecomposition)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVMutableCompositionTrack](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVMutableDateRangeMetadataGroup](https://developer.apple.com/documentation/avfoundation/avmutabledaterangemetadatagroup)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVMutableMediaSelection](https://developer.apple.com/documentation/avfoundation/avmutablemediaselection)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVMutableMetadataItem](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVMutableTimedMetadataGroup](https://developer.apple.com/documentation/avfoundation/avmutabletimedmetadatagroup)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVMutableVideoComposition](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVMutableVideoCompositionInstruction](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositioninstruction)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVMutableVideoCompositionLayerInstruction](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVOutputSettingsAssistant](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVPlayer](https://developer.apple.com/documentation/avfoundation/avplayer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVPlayerActionAtItemEnd [enum]](https://developer.apple.com/documentation/avfoundation/avplayer/actionatitemend)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVPlayerItem](https://developer.apple.com/documentation/avfoundation/avplayeritem)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [AVPlayerItemAccessLog](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslog)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [AVPlayerItemAccessLogEvent](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [AVPlayerItemErrorLog](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlog)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [AVPlayerItemErrorLogEvent](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [AVPlayerItemLegibleOutput](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVPlayerItemLegibleOutputPushDelegate](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutputpushdelegate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol AVPlayerItemLegibleOutputPushDelegate : AVPlayerItemOutputPushDelegate, NSObjectProtocol {     optional func legibleOutput(_ output: AVPlayerItemLegibleOutput, didOutputAttributedStrings strings: [NSAttributedString], nativeSampleBuffers nativeSamples: [AnyObject], forItemTime itemTime: CMTime) } ``` | AVPlayerItemOutputPushDelegate, NSObjectProtocol |
| To | ``` protocol AVPlayerItemLegibleOutputPushDelegate : AVPlayerItemOutputPushDelegate {     optional func legibleOutput(_ output: AVPlayerItemLegibleOutput, didOutputAttributedStrings strings: [NSAttributedString], nativeSampleBuffers nativeSamples: [AnyObject], forItemTime itemTime: CMTime) } ``` | AVPlayerItemOutputPushDelegate |

Modified [AVPlayerItemMetadataOutput](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVPlayerItemMetadataOutputPushDelegate](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutputpushdelegate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol AVPlayerItemMetadataOutputPushDelegate : AVPlayerItemOutputPushDelegate, NSObjectProtocol {     optional func metadataOutput(_ output: AVPlayerItemMetadataOutput, didOutputTimedMetadataGroups groups: [AVTimedMetadataGroup], fromPlayerItemTrack track: AVPlayerItemTrack) } ``` | AVPlayerItemOutputPushDelegate, NSObjectProtocol |
| To | ``` protocol AVPlayerItemMetadataOutputPushDelegate : AVPlayerItemOutputPushDelegate {     optional func metadataOutput(_ output: AVPlayerItemMetadataOutput, didOutputTimedMetadataGroups groups: [AVTimedMetadataGroup], fromPlayerItemTrack track: AVPlayerItemTrack) } ``` | AVPlayerItemOutputPushDelegate |

Modified [AVPlayerItemOutput](https://developer.apple.com/documentation/avfoundation/avplayeritemoutput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVPlayerItemStatus [enum]](https://developer.apple.com/documentation/avfoundation/avplayeritem/status)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVPlayerItemTrack](https://developer.apple.com/documentation/avfoundation/avplayeritemtrack)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVPlayerItemVideoOutput](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVPlayerLayer](https://developer.apple.com/documentation/avfoundation/avplayerlayer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVPlayerMediaSelectionCriteria](https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVPlayerStatus [enum]](https://developer.apple.com/documentation/avfoundation/avplayer/status)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVQueuedSampleBufferRenderingStatus [enum]](https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrenderingstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVQueuePlayer](https://developer.apple.com/documentation/avfoundation/avqueueplayer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVSampleBufferDisplayLayer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVSpeechBoundary [enum]](https://developer.apple.com/documentation/avfoundation/avspeechboundary)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVSpeechSynthesisVoice](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVSpeechSynthesisVoice : NSObject, NSSecureCoding, NSCoding {     class func speechVoices() -> [AVSpeechSynthesisVoice]     class func currentLanguageCode() -> String      init?(language languageCode: String?)     class func voiceWithLanguage(_ languageCode: String?) -> AVSpeechSynthesisVoice?      init?(identifier identifier: String)     class func voiceWithIdentifier(_ identifier: String) -> AVSpeechSynthesisVoice?     var language: String { get }     var identifier: String { get }     var name: String { get }     var quality: AVSpeechSynthesisVoiceQuality { get } } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class AVSpeechSynthesisVoice : NSObject, NSSecureCoding {     class func speechVoices() -> [AVSpeechSynthesisVoice]     class func currentLanguageCode() -> String      init?(language languageCode: String?)     class func voiceWithLanguage(_ languageCode: String?) -> AVSpeechSynthesisVoice?      init?(identifier identifier: String)     class func voiceWithIdentifier(_ identifier: String) -> AVSpeechSynthesisVoice?     var language: String { get }     var identifier: String { get }     var name: String { get }     var quality: AVSpeechSynthesisVoiceQuality { get } } ``` | NSSecureCoding |

Modified [AVSpeechSynthesisVoiceQuality [enum]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoicequality)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [AVSpeechSynthesizer](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVSpeechUtterance](https://developer.apple.com/documentation/avfoundation/avspeechutterance)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVSpeechUtterance : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init(string string: String)     class func speechUtteranceWithString(_ string: String) -> Self     init(string string: String)     var voice: AVSpeechSynthesisVoice?     var speechString: String { get }     var rate: Float     var pitchMultiplier: Float     var volume: Float     var preUtteranceDelay: NSTimeInterval     var postUtteranceDelay: NSTimeInterval } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class AVSpeechUtterance : NSObject, NSCopying, NSSecureCoding {     convenience init(string string: String)     class func speechUtteranceWithString(_ string: String) -> Self     init(string string: String)     var voice: AVSpeechSynthesisVoice?     var speechString: String { get }     var rate: Float     var pitchMultiplier: Float     var volume: Float     var preUtteranceDelay: NSTimeInterval     var postUtteranceDelay: NSTimeInterval } ``` | NSCopying, NSSecureCoding |

Modified [AVSynchronizedLayer](https://developer.apple.com/documentation/avfoundation/avsynchronizedlayer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVTextStyleRule](https://developer.apple.com/documentation/avfoundation/avtextstylerule)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [AVTimedMetadataGroup](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying |

Modified [AVURLAsset](https://developer.apple.com/documentation/avfoundation/avurlasset)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVVideoComposition](https://developer.apple.com/documentation/avfoundation/avvideocomposition)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying |

Modified [AVVideoCompositionCoreAnimationTool](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [AVVideoCompositionInstruction](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVVideoCompositionInstruction : NSObject, NSSecureCoding, NSCoding, NSCopying, NSMutableCopying, AVVideoCompositionInstructionProtocol {     var timeRange: CMTimeRange { get }     var backgroundColor: CGColor? { get }     var layerInstructions: [AVVideoCompositionLayerInstruction] { get }     var enablePostProcessing: Bool { get }     var requiredSourceTrackIDs: [NSValue] { get }     var passthroughTrackID: CMPersistentTrackID { get } } ``` | AVVideoCompositionInstructionProtocol, AnyObject, NSCoding, NSCopying, NSMutableCopying, NSObjectProtocol, NSSecureCoding |
| To | ``` class AVVideoCompositionInstruction : NSObject, NSSecureCoding, NSCopying, NSMutableCopying, AVVideoCompositionInstructionProtocol {     var timeRange: CMTimeRange { get }     var backgroundColor: CGColor? { get }     var layerInstructions: [AVVideoCompositionLayerInstruction] { get }     var enablePostProcessing: Bool { get }     var requiredSourceTrackIDs: [NSValue] { get }     var passthroughTrackID: CMPersistentTrackID { get } } ``` | AVVideoCompositionInstructionProtocol, NSCopying, NSMutableCopying, NSSecureCoding |

Modified [AVVideoCompositionLayerInstruction](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVVideoCompositionLayerInstruction : NSObject, NSSecureCoding, NSCoding, NSCopying, NSMutableCopying {     var trackID: CMPersistentTrackID { get }     func getTransformRampForTime(_ time: CMTime, startTransform startTransform: UnsafeMutablePointer<CGAffineTransform>, endTransform endTransform: UnsafeMutablePointer<CGAffineTransform>, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool     func getOpacityRampForTime(_ time: CMTime, startOpacity startOpacity: UnsafeMutablePointer<Float>, endOpacity endOpacity: UnsafeMutablePointer<Float>, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool     func getCropRectangleRampForTime(_ time: CMTime, startCropRectangle startCropRectangle: UnsafeMutablePointer<CGRect>, endCropRectangle endCropRectangle: UnsafeMutablePointer<CGRect>, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool } ``` | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding |
| To | ``` class AVVideoCompositionLayerInstruction : NSObject, NSSecureCoding, NSCopying, NSMutableCopying {     var trackID: CMPersistentTrackID { get }     func getTransformRampForTime(_ time: CMTime, startTransform startTransform: UnsafeMutablePointer<CGAffineTransform>, endTransform endTransform: UnsafeMutablePointer<CGAffineTransform>, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool     func getOpacityRampForTime(_ time: CMTime, startOpacity startOpacity: UnsafeMutablePointer<Float>, endOpacity endOpacity: UnsafeMutablePointer<Float>, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool     func getCropRectangleRampForTime(_ time: CMTime, startCropRectangle startCropRectangle: UnsafeMutablePointer<CGRect>, endCropRectangle endCropRectangle: UnsafeMutablePointer<CGRect>, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool } ``` | NSCopying, NSMutableCopying, NSSecureCoding |

Modified [AVVideoCompositionRenderContext](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

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
