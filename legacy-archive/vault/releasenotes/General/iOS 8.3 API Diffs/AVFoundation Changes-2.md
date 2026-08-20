---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/AVFoundation.html
archived_at: '2026-07-18T02:56:20.418404Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# AVFoundation Changes

## AVFoundation

Added AVAudio3DAngularOrientation.init()Added AVAudio3DAngularOrientation.init(yaw: Float, pitch: Float, roll: Float)Added AVAudio3DPoint.init()Added AVAudio3DPoint.init(x: Float, y: Float, z: Float)Added AVAudio3DVectorOrientation.init()Added AVAudio3DVectorOrientation.init(forward: AVAudio3DVector, up: AVAudio3DVector)Added AVCaptureWhiteBalanceChromaticityValues.init()Added AVCaptureWhiteBalanceChromaticityValues.init(x: Float, y: Float)Added AVCaptureWhiteBalanceGains.init()Added AVCaptureWhiteBalanceGains.init(redGain: Float, greenGain: Float, blueGain: Float)Added AVCaptureWhiteBalanceTemperatureAndTintValues.init()Added AVCaptureWhiteBalanceTemperatureAndTintValues.init(temperature: Float, tint: Float)Added AVEdgeWidths.init()Added AVEdgeWidths.init(left: CGFloat, top: CGFloat, right: CGFloat, bottom: CGFloat)Added AVError.AirPlayControllerRequiresInternetAdded AVError.AirPlayReceiverRequiresInternetAdded AVPixelAspectRatio.init()Added AVPixelAspectRatio.init(horizontalSpacing: Int, verticalSpacing: Int)Modified AVAudio3DAngularOrientation [struct]

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

Modified AVAudioSessionRouteChangeReason.RouteConfigurationChange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified AVCaptureWhiteBalanceChromaticityValues [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AVCaptureWhiteBalanceChromaticityValues {     var x: Float     var y: Float } ``` |
| To | ``` struct AVCaptureWhiteBalanceChromaticityValues {     var x: Float     var y: Float     init()     init(x x: Float, y y: Float) } ``` |

Modified AVCaptureWhiteBalanceGains [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AVCaptureWhiteBalanceGains {     var redGain: Float     var greenGain: Float     var blueGain: Float } ``` |
| To | ``` struct AVCaptureWhiteBalanceGains {     var redGain: Float     var greenGain: Float     var blueGain: Float     init()     init(redGain redGain: Float, greenGain greenGain: Float, blueGain blueGain: Float) } ``` |

Modified AVCaptureWhiteBalanceTemperatureAndTintValues [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AVCaptureWhiteBalanceTemperatureAndTintValues {     var temperature: Float     var tint: Float } ``` |
| To | ``` struct AVCaptureWhiteBalanceTemperatureAndTintValues {     var temperature: Float     var tint: Float     init()     init(temperature temperature: Float, tint tint: Float) } ``` |

Modified AVEdgeWidths [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AVEdgeWidths {     var left: CGFloat     var top: CGFloat     var right: CGFloat     var bottom: CGFloat } ``` |
| To | ``` struct AVEdgeWidths {     var left: CGFloat     var top: CGFloat     var right: CGFloat     var bottom: CGFloat     init()     init(left left: CGFloat, top top: CGFloat, right right: CGFloat, bottom bottom: CGFloat) } ``` |

Modified AVError [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum AVError : Int {     case Unknown     case OutOfMemory     case SessionNotRunning     case DeviceAlreadyUsedByAnotherSession     case NoDataCaptured     case SessionConfigurationChanged     case DiskFull     case DeviceWasDisconnected     case MediaChanged     case MaximumDurationReached     case MaximumFileSizeReached     case MediaDiscontinuity     case MaximumNumberOfSamplesForFileFormatReached     case DeviceNotConnected     case DeviceInUseByAnotherApplication     case DeviceLockedForConfigurationByAnotherProcess     case SessionWasInterrupted     case MediaServicesWereReset     case ExportFailed     case DecodeFailed     case InvalidSourceMedia     case FileAlreadyExists     case CompositionTrackSegmentsNotContiguous     case InvalidCompositionTrackSegmentDuration     case InvalidCompositionTrackSegmentSourceStartTime     case InvalidCompositionTrackSegmentSourceDuration     case FileFormatNotRecognized     case FileFailedToParse     case MaximumStillImageCaptureRequestsExceeded     case ContentIsProtected     case NoImageAtTime     case DecoderNotFound     case EncoderNotFound     case ContentIsNotAuthorized     case ApplicationIsNotAuthorized     case DeviceIsNotAvailableInBackground     case OperationNotSupportedForAsset     case DecoderTemporarilyUnavailable     case EncoderTemporarilyUnavailable     case InvalidVideoComposition     case ReferenceForbiddenByReferencePolicy     case InvalidOutputURLPathExtension     case ScreenCaptureFailed     case DisplayWasDisabled     case TorchLevelUnavailable     case OperationInterrupted     case IncompatibleAsset     case FailedToLoadMediaData     case ServerIncorrectlyConfigured     case ApplicationIsNotAuthorizedToUseDevice     case FailedToParse     case FileTypeDoesNotSupportSampleReferences     case UndecodableMediaData } ``` |
| To | ``` enum AVError : Int {     case Unknown     case OutOfMemory     case SessionNotRunning     case DeviceAlreadyUsedByAnotherSession     case NoDataCaptured     case SessionConfigurationChanged     case DiskFull     case DeviceWasDisconnected     case MediaChanged     case MaximumDurationReached     case MaximumFileSizeReached     case MediaDiscontinuity     case MaximumNumberOfSamplesForFileFormatReached     case DeviceNotConnected     case DeviceInUseByAnotherApplication     case DeviceLockedForConfigurationByAnotherProcess     case SessionWasInterrupted     case MediaServicesWereReset     case ExportFailed     case DecodeFailed     case InvalidSourceMedia     case FileAlreadyExists     case CompositionTrackSegmentsNotContiguous     case InvalidCompositionTrackSegmentDuration     case InvalidCompositionTrackSegmentSourceStartTime     case InvalidCompositionTrackSegmentSourceDuration     case FileFormatNotRecognized     case FileFailedToParse     case MaximumStillImageCaptureRequestsExceeded     case ContentIsProtected     case NoImageAtTime     case DecoderNotFound     case EncoderNotFound     case ContentIsNotAuthorized     case ApplicationIsNotAuthorized     case DeviceIsNotAvailableInBackground     case OperationNotSupportedForAsset     case DecoderTemporarilyUnavailable     case EncoderTemporarilyUnavailable     case InvalidVideoComposition     case ReferenceForbiddenByReferencePolicy     case InvalidOutputURLPathExtension     case ScreenCaptureFailed     case DisplayWasDisabled     case TorchLevelUnavailable     case OperationInterrupted     case IncompatibleAsset     case FailedToLoadMediaData     case ServerIncorrectlyConfigured     case ApplicationIsNotAuthorizedToUseDevice     case FailedToParse     case FileTypeDoesNotSupportSampleReferences     case UndecodableMediaData     case AirPlayControllerRequiresInternet     case AirPlayReceiverRequiresInternet } ``` |

Modified AVMutableVideoComposition.init(propertiesOfAsset: AVAsset!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVPixelAspectRatio [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AVPixelAspectRatio {     var horizontalSpacing: Int     var verticalSpacing: Int } ``` |
| To | ``` struct AVPixelAspectRatio {     var horizontalSpacing: Int     var verticalSpacing: Int     init()     init(horizontalSpacing horizontalSpacing: Int, verticalSpacing verticalSpacing: Int) } ``` |

Modified AVVideoComposition.init(propertiesOfAsset: AVAsset!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified AVVideoCompositionCoreAnimationTool.init(postProcessingAsVideoLayers: [AnyObject]!, inLayer: CALayer!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSValue.init(CMTime: CMTime)

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 4.0 |

Modified NSValue.init(CMTimeMapping: CMTimeMapping)

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 4.0 |

Modified NSValue.init(CMTimeRange: CMTimeRange)

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 4.0 |

Modified AVAssetExportPreset1280x720

|  | Declaration |
| --- | --- |
| From | ``` let AVAssetExportPreset1280x720: NSString! ``` |
| To | ``` let AVAssetExportPreset1280x720: String ``` |

Modified AVAssetExportPreset1920x1080

|  | Declaration |
| --- | --- |
| From | ``` let AVAssetExportPreset1920x1080: NSString! ``` |
| To | ``` let AVAssetExportPreset1920x1080: String ``` |

Modified AVAssetExportPreset640x480

|  | Declaration |
| --- | --- |
| From | ``` let AVAssetExportPreset640x480: NSString! ``` |
| To | ``` let AVAssetExportPreset640x480: String ``` |

Modified AVAssetExportPreset960x540

|  | Declaration |
| --- | --- |
| From | ``` let AVAssetExportPreset960x540: NSString! ``` |
| To | ``` let AVAssetExportPreset960x540: String ``` |

Modified AVAssetExportPresetAppleM4A

|  | Declaration |
| --- | --- |
| From | ``` let AVAssetExportPresetAppleM4A: NSString! ``` |
| To | ``` let AVAssetExportPresetAppleM4A: String ``` |

Modified AVAssetExportPresetHighestQuality

|  | Declaration |
| --- | --- |
| From | ``` let AVAssetExportPresetHighestQuality: NSString! ``` |
| To | ``` let AVAssetExportPresetHighestQuality: String ``` |

Modified AVAssetExportPresetLowQuality

|  | Declaration |
| --- | --- |
| From | ``` let AVAssetExportPresetLowQuality: NSString! ``` |
| To | ``` let AVAssetExportPresetLowQuality: String ``` |

Modified AVAssetExportPresetMediumQuality

|  | Declaration |
| --- | --- |
| From | ``` let AVAssetExportPresetMediumQuality: NSString! ``` |
| To | ``` let AVAssetExportPresetMediumQuality: String ``` |

Modified AVAssetExportPresetPassthrough

|  | Declaration |
| --- | --- |
| From | ``` let AVAssetExportPresetPassthrough: NSString! ``` |
| To | ``` let AVAssetExportPresetPassthrough: String ``` |

Modified AVAssetImageGeneratorApertureModeCleanAperture

|  | Declaration |
| --- | --- |
| From | ``` let AVAssetImageGeneratorApertureModeCleanAperture: NSString! ``` |
| To | ``` let AVAssetImageGeneratorApertureModeCleanAperture: String ``` |

Modified AVAssetImageGeneratorApertureModeEncodedPixels

|  | Declaration |
| --- | --- |
| From | ``` let AVAssetImageGeneratorApertureModeEncodedPixels: NSString! ``` |
| To | ``` let AVAssetImageGeneratorApertureModeEncodedPixels: String ``` |

Modified AVAssetImageGeneratorApertureModeProductionAperture

|  | Declaration |
| --- | --- |
| From | ``` let AVAssetImageGeneratorApertureModeProductionAperture: NSString! ``` |
| To | ``` let AVAssetImageGeneratorApertureModeProductionAperture: String ``` |

Modified AVAudioBitRateStrategy_Constant

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioBitRateStrategy_Constant: NSString! ``` |
| To | ``` let AVAudioBitRateStrategy_Constant: String ``` |

Modified AVAudioBitRateStrategy_LongTermAverage

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioBitRateStrategy_LongTermAverage: NSString! ``` |
| To | ``` let AVAudioBitRateStrategy_LongTermAverage: String ``` |

Modified AVAudioBitRateStrategy_Variable

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioBitRateStrategy_Variable: NSString! ``` |
| To | ``` let AVAudioBitRateStrategy_Variable: String ``` |

Modified AVAudioBitRateStrategy_VariableConstrained

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioBitRateStrategy_VariableConstrained: NSString! ``` |
| To | ``` let AVAudioBitRateStrategy_VariableConstrained: String ``` |

Modified AVAudioEngineConfigurationChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioEngineConfigurationChangeNotification: NSString! ``` |
| To | ``` let AVAudioEngineConfigurationChangeNotification: String ``` |

Modified AVAudioSessionCategoryAmbient

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionCategoryAmbient: NSString! ``` |
| To | ``` let AVAudioSessionCategoryAmbient: String ``` |

Modified AVAudioSessionCategoryAudioProcessing

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionCategoryAudioProcessing: NSString! ``` |
| To | ``` let AVAudioSessionCategoryAudioProcessing: String ``` |

Modified AVAudioSessionCategoryMultiRoute

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionCategoryMultiRoute: NSString! ``` |
| To | ``` let AVAudioSessionCategoryMultiRoute: String ``` |

Modified AVAudioSessionCategoryPlayAndRecord

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionCategoryPlayAndRecord: NSString! ``` |
| To | ``` let AVAudioSessionCategoryPlayAndRecord: String ``` |

Modified AVAudioSessionCategoryPlayback

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionCategoryPlayback: NSString! ``` |
| To | ``` let AVAudioSessionCategoryPlayback: String ``` |

Modified AVAudioSessionCategoryRecord

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionCategoryRecord: NSString! ``` |
| To | ``` let AVAudioSessionCategoryRecord: String ``` |

Modified AVAudioSessionCategorySoloAmbient

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionCategorySoloAmbient: NSString! ``` |
| To | ``` let AVAudioSessionCategorySoloAmbient: String ``` |

Modified AVAudioSessionInterruptionNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionInterruptionNotification: NSString! ``` |
| To | ``` let AVAudioSessionInterruptionNotification: String ``` |

Modified AVAudioSessionInterruptionOptionKey

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionInterruptionOptionKey: NSString! ``` |
| To | ``` let AVAudioSessionInterruptionOptionKey: String ``` |

Modified AVAudioSessionInterruptionTypeKey

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionInterruptionTypeKey: NSString! ``` |
| To | ``` let AVAudioSessionInterruptionTypeKey: String ``` |

Modified AVAudioSessionLocationLower

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionLocationLower: NSString! ``` |
| To | ``` let AVAudioSessionLocationLower: String ``` |

Modified AVAudioSessionLocationUpper

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionLocationUpper: NSString! ``` |
| To | ``` let AVAudioSessionLocationUpper: String ``` |

Modified AVAudioSessionMediaServicesWereLostNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionMediaServicesWereLostNotification: NSString! ``` |
| To | ``` let AVAudioSessionMediaServicesWereLostNotification: String ``` |

Modified AVAudioSessionMediaServicesWereResetNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionMediaServicesWereResetNotification: NSString! ``` |
| To | ``` let AVAudioSessionMediaServicesWereResetNotification: String ``` |

Modified AVAudioSessionModeDefault

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionModeDefault: NSString! ``` |
| To | ``` let AVAudioSessionModeDefault: String ``` |

Modified AVAudioSessionModeGameChat

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionModeGameChat: NSString! ``` |
| To | ``` let AVAudioSessionModeGameChat: String ``` |

Modified AVAudioSessionModeMeasurement

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionModeMeasurement: NSString! ``` |
| To | ``` let AVAudioSessionModeMeasurement: String ``` |

Modified AVAudioSessionModeMoviePlayback

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionModeMoviePlayback: NSString! ``` |
| To | ``` let AVAudioSessionModeMoviePlayback: String ``` |

Modified AVAudioSessionModeVideoChat

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionModeVideoChat: NSString! ``` |
| To | ``` let AVAudioSessionModeVideoChat: String ``` |

Modified AVAudioSessionModeVideoRecording

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionModeVideoRecording: NSString! ``` |
| To | ``` let AVAudioSessionModeVideoRecording: String ``` |

Modified AVAudioSessionModeVoiceChat

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionModeVoiceChat: NSString! ``` |
| To | ``` let AVAudioSessionModeVoiceChat: String ``` |

Modified AVAudioSessionOrientationBack

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionOrientationBack: NSString! ``` |
| To | ``` let AVAudioSessionOrientationBack: String ``` |

Modified AVAudioSessionOrientationBottom

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionOrientationBottom: NSString! ``` |
| To | ``` let AVAudioSessionOrientationBottom: String ``` |

Modified AVAudioSessionOrientationFront

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionOrientationFront: NSString! ``` |
| To | ``` let AVAudioSessionOrientationFront: String ``` |

Modified AVAudioSessionOrientationLeft

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionOrientationLeft: NSString! ``` |
| To | ``` let AVAudioSessionOrientationLeft: String ``` |

Modified AVAudioSessionOrientationRight

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionOrientationRight: NSString! ``` |
| To | ``` let AVAudioSessionOrientationRight: String ``` |

Modified AVAudioSessionOrientationTop

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionOrientationTop: NSString! ``` |
| To | ``` let AVAudioSessionOrientationTop: String ``` |

Modified AVAudioSessionPolarPatternCardioid

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionPolarPatternCardioid: NSString! ``` |
| To | ``` let AVAudioSessionPolarPatternCardioid: String ``` |

Modified AVAudioSessionPolarPatternOmnidirectional

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionPolarPatternOmnidirectional: NSString! ``` |
| To | ``` let AVAudioSessionPolarPatternOmnidirectional: String ``` |

Modified AVAudioSessionPolarPatternSubcardioid

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionPolarPatternSubcardioid: NSString! ``` |
| To | ``` let AVAudioSessionPolarPatternSubcardioid: String ``` |

Modified AVAudioSessionPortAirPlay

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionPortAirPlay: NSString! ``` |
| To | ``` let AVAudioSessionPortAirPlay: String ``` |

Modified AVAudioSessionPortBluetoothA2DP

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionPortBluetoothA2DP: NSString! ``` |
| To | ``` let AVAudioSessionPortBluetoothA2DP: String ``` |

Modified AVAudioSessionPortBluetoothHFP

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionPortBluetoothHFP: NSString! ``` |
| To | ``` let AVAudioSessionPortBluetoothHFP: String ``` |

Modified AVAudioSessionPortBluetoothLE

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionPortBluetoothLE: NSString! ``` |
| To | ``` let AVAudioSessionPortBluetoothLE: String ``` |

Modified AVAudioSessionPortBuiltInMic

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionPortBuiltInMic: NSString! ``` |
| To | ``` let AVAudioSessionPortBuiltInMic: String ``` |

Modified AVAudioSessionPortBuiltInReceiver

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionPortBuiltInReceiver: NSString! ``` |
| To | ``` let AVAudioSessionPortBuiltInReceiver: String ``` |

Modified AVAudioSessionPortBuiltInSpeaker

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionPortBuiltInSpeaker: NSString! ``` |
| To | ``` let AVAudioSessionPortBuiltInSpeaker: String ``` |

Modified AVAudioSessionPortCarAudio

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionPortCarAudio: NSString! ``` |
| To | ``` let AVAudioSessionPortCarAudio: String ``` |

Modified AVAudioSessionPortHDMI

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionPortHDMI: NSString! ``` |
| To | ``` let AVAudioSessionPortHDMI: String ``` |

Modified AVAudioSessionPortHeadphones

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionPortHeadphones: NSString! ``` |
| To | ``` let AVAudioSessionPortHeadphones: String ``` |

Modified AVAudioSessionPortHeadsetMic

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionPortHeadsetMic: NSString! ``` |
| To | ``` let AVAudioSessionPortHeadsetMic: String ``` |

Modified AVAudioSessionPortLineIn

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionPortLineIn: NSString! ``` |
| To | ``` let AVAudioSessionPortLineIn: String ``` |

Modified AVAudioSessionPortLineOut

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionPortLineOut: NSString! ``` |
| To | ``` let AVAudioSessionPortLineOut: String ``` |

Modified AVAudioSessionPortUSBAudio

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionPortUSBAudio: NSString! ``` |
| To | ``` let AVAudioSessionPortUSBAudio: String ``` |

Modified AVAudioSessionRouteChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionRouteChangeNotification: NSString! ``` |
| To | ``` let AVAudioSessionRouteChangeNotification: String ``` |

Modified AVAudioSessionRouteChangePreviousRouteKey

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionRouteChangePreviousRouteKey: NSString! ``` |
| To | ``` let AVAudioSessionRouteChangePreviousRouteKey: String ``` |

Modified AVAudioSessionRouteChangeReasonKey

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionRouteChangeReasonKey: NSString! ``` |
| To | ``` let AVAudioSessionRouteChangeReasonKey: String ``` |

Modified AVAudioSessionSilenceSecondaryAudioHintNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionSilenceSecondaryAudioHintNotification: NSString! ``` |
| To | ``` let AVAudioSessionSilenceSecondaryAudioHintNotification: String ``` |

Modified AVAudioSessionSilenceSecondaryAudioHintTypeKey

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioSessionSilenceSecondaryAudioHintTypeKey: NSString! ``` |
| To | ``` let AVAudioSessionSilenceSecondaryAudioHintTypeKey: String ``` |

Modified AVAudioTimePitchAlgorithmLowQualityZeroLatency

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioTimePitchAlgorithmLowQualityZeroLatency: NSString! ``` |
| To | ``` let AVAudioTimePitchAlgorithmLowQualityZeroLatency: String ``` |

Modified AVAudioTimePitchAlgorithmSpectral

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioTimePitchAlgorithmSpectral: NSString! ``` |
| To | ``` let AVAudioTimePitchAlgorithmSpectral: String ``` |

Modified AVAudioTimePitchAlgorithmTimeDomain

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioTimePitchAlgorithmTimeDomain: NSString! ``` |
| To | ``` let AVAudioTimePitchAlgorithmTimeDomain: String ``` |

Modified AVAudioTimePitchAlgorithmVarispeed

|  | Declaration |
| --- | --- |
| From | ``` let AVAudioTimePitchAlgorithmVarispeed: NSString! ``` |
| To | ``` let AVAudioTimePitchAlgorithmVarispeed: String ``` |

Modified AVCaptureDeviceSubjectAreaDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVCaptureDeviceSubjectAreaDidChangeNotification: NSString! ``` |
| To | ``` let AVCaptureDeviceSubjectAreaDidChangeNotification: String ``` |

Modified AVCaptureDeviceWasConnectedNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVCaptureDeviceWasConnectedNotification: NSString! ``` |
| To | ``` let AVCaptureDeviceWasConnectedNotification: String ``` |

Modified AVCaptureDeviceWasDisconnectedNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVCaptureDeviceWasDisconnectedNotification: NSString! ``` |
| To | ``` let AVCaptureDeviceWasDisconnectedNotification: String ``` |

Modified AVCaptureInputPortFormatDescriptionDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVCaptureInputPortFormatDescriptionDidChangeNotification: NSString! ``` |
| To | ``` let AVCaptureInputPortFormatDescriptionDidChangeNotification: String ``` |

Modified AVCaptureSessionDidStartRunningNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVCaptureSessionDidStartRunningNotification: NSString! ``` |
| To | ``` let AVCaptureSessionDidStartRunningNotification: String ``` |

Modified AVCaptureSessionDidStopRunningNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVCaptureSessionDidStopRunningNotification: NSString! ``` |
| To | ``` let AVCaptureSessionDidStopRunningNotification: String ``` |

Modified AVCaptureSessionErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let AVCaptureSessionErrorKey: NSString! ``` |
| To | ``` let AVCaptureSessionErrorKey: String ``` |

Modified AVCaptureSessionInterruptionEndedNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVCaptureSessionInterruptionEndedNotification: NSString! ``` |
| To | ``` let AVCaptureSessionInterruptionEndedNotification: String ``` |

Modified AVCaptureSessionPreset1280x720

|  | Declaration |
| --- | --- |
| From | ``` let AVCaptureSessionPreset1280x720: NSString! ``` |
| To | ``` let AVCaptureSessionPreset1280x720: String ``` |

Modified AVCaptureSessionPreset1920x1080

|  | Declaration |
| --- | --- |
| From | ``` let AVCaptureSessionPreset1920x1080: NSString! ``` |
| To | ``` let AVCaptureSessionPreset1920x1080: String ``` |

Modified AVCaptureSessionPreset352x288

|  | Declaration |
| --- | --- |
| From | ``` let AVCaptureSessionPreset352x288: NSString! ``` |
| To | ``` let AVCaptureSessionPreset352x288: String ``` |

Modified AVCaptureSessionPreset640x480

|  | Declaration |
| --- | --- |
| From | ``` let AVCaptureSessionPreset640x480: NSString! ``` |
| To | ``` let AVCaptureSessionPreset640x480: String ``` |

Modified AVCaptureSessionPresetHigh

|  | Declaration |
| --- | --- |
| From | ``` let AVCaptureSessionPresetHigh: NSString! ``` |
| To | ``` let AVCaptureSessionPresetHigh: String ``` |

Modified AVCaptureSessionPresetInputPriority

|  | Declaration |
| --- | --- |
| From | ``` let AVCaptureSessionPresetInputPriority: NSString! ``` |
| To | ``` let AVCaptureSessionPresetInputPriority: String ``` |

Modified AVCaptureSessionPresetLow

|  | Declaration |
| --- | --- |
| From | ``` let AVCaptureSessionPresetLow: NSString! ``` |
| To | ``` let AVCaptureSessionPresetLow: String ``` |

Modified AVCaptureSessionPresetMedium

|  | Declaration |
| --- | --- |
| From | ``` let AVCaptureSessionPresetMedium: NSString! ``` |
| To | ``` let AVCaptureSessionPresetMedium: String ``` |

Modified AVCaptureSessionPresetPhoto

|  | Declaration |
| --- | --- |
| From | ``` let AVCaptureSessionPresetPhoto: NSString! ``` |
| To | ``` let AVCaptureSessionPresetPhoto: String ``` |

Modified AVCaptureSessionPresetiFrame1280x720

|  | Declaration |
| --- | --- |
| From | ``` let AVCaptureSessionPresetiFrame1280x720: NSString! ``` |
| To | ``` let AVCaptureSessionPresetiFrame1280x720: String ``` |

Modified AVCaptureSessionPresetiFrame960x540

|  | Declaration |
| --- | --- |
| From | ``` let AVCaptureSessionPresetiFrame960x540: NSString! ``` |
| To | ``` let AVCaptureSessionPresetiFrame960x540: String ``` |

Modified AVCaptureSessionRuntimeErrorNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVCaptureSessionRuntimeErrorNotification: NSString! ``` |
| To | ``` let AVCaptureSessionRuntimeErrorNotification: String ``` |

Modified AVCaptureSessionWasInterruptedNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVCaptureSessionWasInterruptedNotification: NSString! ``` |
| To | ``` let AVCaptureSessionWasInterruptedNotification: String ``` |

Modified AVChannelLayoutKey

|  | Declaration |
| --- | --- |
| From | ``` let AVChannelLayoutKey: NSString! ``` |
| To | ``` let AVChannelLayoutKey: String ``` |

Modified AVEncoderAudioQualityForVBRKey

|  | Declaration |
| --- | --- |
| From | ``` let AVEncoderAudioQualityForVBRKey: NSString! ``` |
| To | ``` let AVEncoderAudioQualityForVBRKey: String ``` |

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

|  | Declaration |
| --- | --- |
| From | ``` let AVEncoderBitRatePerChannelKey: NSString! ``` |
| To | ``` let AVEncoderBitRatePerChannelKey: String ``` |

Modified AVEncoderBitRateStrategyKey

|  | Declaration |
| --- | --- |
| From | ``` let AVEncoderBitRateStrategyKey: NSString! ``` |
| To | ``` let AVEncoderBitRateStrategyKey: String ``` |

Modified AVErrorDeviceKey

|  | Declaration |
| --- | --- |
| From | ``` let AVErrorDeviceKey: NSString! ``` |
| To | ``` let AVErrorDeviceKey: String ``` |

Modified AVErrorFileSizeKey

|  | Declaration |
| --- | --- |
| From | ``` let AVErrorFileSizeKey: NSString! ``` |
| To | ``` let AVErrorFileSizeKey: String ``` |

Modified AVErrorFileTypeKey

|  | Declaration |
| --- | --- |
| From | ``` let AVErrorFileTypeKey: NSString! ``` |
| To | ``` let AVErrorFileTypeKey: String ``` |

Modified AVErrorMediaSubTypeKey

|  | Declaration |
| --- | --- |
| From | ``` let AVErrorMediaSubTypeKey: NSString! ``` |
| To | ``` let AVErrorMediaSubTypeKey: String ``` |

Modified AVErrorMediaTypeKey

|  | Declaration |
| --- | --- |
| From | ``` let AVErrorMediaTypeKey: NSString! ``` |
| To | ``` let AVErrorMediaTypeKey: String ``` |

Modified AVErrorPIDKey

|  | Declaration |
| --- | --- |
| From | ``` let AVErrorPIDKey: NSString! ``` |
| To | ``` let AVErrorPIDKey: String ``` |

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

|  | Declaration |
| --- | --- |
| From | ``` let AVErrorRecordingSuccessfullyFinishedKey: NSString! ``` |
| To | ``` let AVErrorRecordingSuccessfullyFinishedKey: String ``` |

Modified AVErrorTimeKey

|  | Declaration |
| --- | --- |
| From | ``` let AVErrorTimeKey: NSString! ``` |
| To | ``` let AVErrorTimeKey: String ``` |

Modified AVFileType3GPP

|  | Declaration |
| --- | --- |
| From | ``` let AVFileType3GPP: NSString! ``` |
| To | ``` let AVFileType3GPP: String ``` |

Modified AVFileType3GPP2

|  | Declaration |
| --- | --- |
| From | ``` let AVFileType3GPP2: NSString! ``` |
| To | ``` let AVFileType3GPP2: String ``` |

Modified AVFileTypeAC3

|  | Declaration |
| --- | --- |
| From | ``` let AVFileTypeAC3: NSString! ``` |
| To | ``` let AVFileTypeAC3: String ``` |

Modified AVFileTypeAIFC

|  | Declaration |
| --- | --- |
| From | ``` let AVFileTypeAIFC: NSString! ``` |
| To | ``` let AVFileTypeAIFC: String ``` |

Modified AVFileTypeAIFF

|  | Declaration |
| --- | --- |
| From | ``` let AVFileTypeAIFF: NSString! ``` |
| To | ``` let AVFileTypeAIFF: String ``` |

Modified AVFileTypeAMR

|  | Declaration |
| --- | --- |
| From | ``` let AVFileTypeAMR: NSString! ``` |
| To | ``` let AVFileTypeAMR: String ``` |

Modified AVFileTypeAppleM4A

|  | Declaration |
| --- | --- |
| From | ``` let AVFileTypeAppleM4A: NSString! ``` |
| To | ``` let AVFileTypeAppleM4A: String ``` |

Modified AVFileTypeAppleM4V

|  | Declaration |
| --- | --- |
| From | ``` let AVFileTypeAppleM4V: NSString! ``` |
| To | ``` let AVFileTypeAppleM4V: String ``` |

Modified AVFileTypeCoreAudioFormat

|  | Declaration |
| --- | --- |
| From | ``` let AVFileTypeCoreAudioFormat: NSString! ``` |
| To | ``` let AVFileTypeCoreAudioFormat: String ``` |

Modified AVFileTypeMPEG4

|  | Declaration |
| --- | --- |
| From | ``` let AVFileTypeMPEG4: NSString! ``` |
| To | ``` let AVFileTypeMPEG4: String ``` |

Modified AVFileTypeMPEGLayer3

|  | Declaration |
| --- | --- |
| From | ``` let AVFileTypeMPEGLayer3: NSString! ``` |
| To | ``` let AVFileTypeMPEGLayer3: String ``` |

Modified AVFileTypeQuickTimeMovie

|  | Declaration |
| --- | --- |
| From | ``` let AVFileTypeQuickTimeMovie: NSString! ``` |
| To | ``` let AVFileTypeQuickTimeMovie: String ``` |

Modified AVFileTypeSunAU

|  | Declaration |
| --- | --- |
| From | ``` let AVFileTypeSunAU: NSString! ``` |
| To | ``` let AVFileTypeSunAU: String ``` |

Modified AVFileTypeWAVE

|  | Declaration |
| --- | --- |
| From | ``` let AVFileTypeWAVE: NSString! ``` |
| To | ``` let AVFileTypeWAVE: String ``` |

Modified AVFormatIDKey

|  | Declaration |
| --- | --- |
| From | ``` let AVFormatIDKey: NSString! ``` |
| To | ``` let AVFormatIDKey: String ``` |

Modified AVFoundationErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let AVFoundationErrorDomain: NSString! ``` |
| To | ``` let AVFoundationErrorDomain: String ``` |

Modified AVLayerVideoGravityResize

|  | Declaration |
| --- | --- |
| From | ``` let AVLayerVideoGravityResize: NSString! ``` |
| To | ``` let AVLayerVideoGravityResize: String ``` |

Modified AVLayerVideoGravityResizeAspect

|  | Declaration |
| --- | --- |
| From | ``` let AVLayerVideoGravityResizeAspect: NSString! ``` |
| To | ``` let AVLayerVideoGravityResizeAspect: String ``` |

Modified AVLayerVideoGravityResizeAspectFill

|  | Declaration |
| --- | --- |
| From | ``` let AVLayerVideoGravityResizeAspectFill: NSString! ``` |
| To | ``` let AVLayerVideoGravityResizeAspectFill: String ``` |

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

|  | Declaration |
| --- | --- |
| From | ``` let AVLinearPCMIsNonInterleaved: NSString! ``` |
| To | ``` let AVLinearPCMIsNonInterleaved: String ``` |

Modified AVMediaCharacteristicAudible

|  | Declaration |
| --- | --- |
| From | ``` let AVMediaCharacteristicAudible: NSString! ``` |
| To | ``` let AVMediaCharacteristicAudible: String ``` |

Modified AVMediaCharacteristicContainsOnlyForcedSubtitles

|  | Declaration |
| --- | --- |
| From | ``` let AVMediaCharacteristicContainsOnlyForcedSubtitles: NSString! ``` |
| To | ``` let AVMediaCharacteristicContainsOnlyForcedSubtitles: String ``` |

Modified AVMediaCharacteristicDescribesMusicAndSoundForAccessibility

|  | Declaration |
| --- | --- |
| From | ``` let AVMediaCharacteristicDescribesMusicAndSoundForAccessibility: NSString! ``` |
| To | ``` let AVMediaCharacteristicDescribesMusicAndSoundForAccessibility: String ``` |

Modified AVMediaCharacteristicDescribesVideoForAccessibility

|  | Declaration |
| --- | --- |
| From | ``` let AVMediaCharacteristicDescribesVideoForAccessibility: NSString! ``` |
| To | ``` let AVMediaCharacteristicDescribesVideoForAccessibility: String ``` |

Modified AVMediaCharacteristicEasyToRead

|  | Declaration |
| --- | --- |
| From | ``` let AVMediaCharacteristicEasyToRead: NSString! ``` |
| To | ``` let AVMediaCharacteristicEasyToRead: String ``` |

Modified AVMediaCharacteristicFrameBased

|  | Declaration |
| --- | --- |
| From | ``` let AVMediaCharacteristicFrameBased: NSString! ``` |
| To | ``` let AVMediaCharacteristicFrameBased: String ``` |

Modified AVMediaCharacteristicIsAuxiliaryContent

|  | Declaration |
| --- | --- |
| From | ``` let AVMediaCharacteristicIsAuxiliaryContent: NSString! ``` |
| To | ``` let AVMediaCharacteristicIsAuxiliaryContent: String ``` |

Modified AVMediaCharacteristicIsMainProgramContent

|  | Declaration |
| --- | --- |
| From | ``` let AVMediaCharacteristicIsMainProgramContent: NSString! ``` |
| To | ``` let AVMediaCharacteristicIsMainProgramContent: String ``` |

Modified AVMediaCharacteristicLegible

|  | Declaration |
| --- | --- |
| From | ``` let AVMediaCharacteristicLegible: NSString! ``` |
| To | ``` let AVMediaCharacteristicLegible: String ``` |

Modified AVMediaCharacteristicTranscribesSpokenDialogForAccessibility

|  | Declaration |
| --- | --- |
| From | ``` let AVMediaCharacteristicTranscribesSpokenDialogForAccessibility: NSString! ``` |
| To | ``` let AVMediaCharacteristicTranscribesSpokenDialogForAccessibility: String ``` |

Modified AVMediaCharacteristicVisual

|  | Declaration |
| --- | --- |
| From | ``` let AVMediaCharacteristicVisual: NSString! ``` |
| To | ``` let AVMediaCharacteristicVisual: String ``` |

Modified AVMediaTypeAudio

|  | Declaration |
| --- | --- |
| From | ``` let AVMediaTypeAudio: NSString! ``` |
| To | ``` let AVMediaTypeAudio: String ``` |

Modified AVMediaTypeClosedCaption

|  | Declaration |
| --- | --- |
| From | ``` let AVMediaTypeClosedCaption: NSString! ``` |
| To | ``` let AVMediaTypeClosedCaption: String ``` |

Modified AVMediaTypeMetadata

|  | Declaration |
| --- | --- |
| From | ``` let AVMediaTypeMetadata: NSString! ``` |
| To | ``` let AVMediaTypeMetadata: String ``` |

Modified AVMediaTypeMuxed

|  | Declaration |
| --- | --- |
| From | ``` let AVMediaTypeMuxed: NSString! ``` |
| To | ``` let AVMediaTypeMuxed: String ``` |

Modified AVMediaTypeSubtitle

|  | Declaration |
| --- | --- |
| From | ``` let AVMediaTypeSubtitle: NSString! ``` |
| To | ``` let AVMediaTypeSubtitle: String ``` |

Modified AVMediaTypeText

|  | Declaration |
| --- | --- |
| From | ``` let AVMediaTypeText: NSString! ``` |
| To | ``` let AVMediaTypeText: String ``` |

Modified AVMediaTypeTimecode

|  | Declaration |
| --- | --- |
| From | ``` let AVMediaTypeTimecode: NSString! ``` |
| To | ``` let AVMediaTypeTimecode: String ``` |

Modified AVMediaTypeVideo

|  | Declaration |
| --- | --- |
| From | ``` let AVMediaTypeVideo: NSString! ``` |
| To | ``` let AVMediaTypeVideo: String ``` |

Modified AVMetadata3GPUserDataKeyAlbumAndTrack

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyAlbumAndTrack: NSString! ``` |
| To | ``` let AVMetadata3GPUserDataKeyAlbumAndTrack: String ``` |

Modified AVMetadata3GPUserDataKeyAuthor

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyAuthor: NSString! ``` |
| To | ``` let AVMetadata3GPUserDataKeyAuthor: String ``` |

Modified AVMetadata3GPUserDataKeyCollection

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyCollection: NSString! ``` |
| To | ``` let AVMetadata3GPUserDataKeyCollection: String ``` |

Modified AVMetadata3GPUserDataKeyCopyright

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyCopyright: NSString! ``` |
| To | ``` let AVMetadata3GPUserDataKeyCopyright: String ``` |

Modified AVMetadata3GPUserDataKeyDescription

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyDescription: NSString! ``` |
| To | ``` let AVMetadata3GPUserDataKeyDescription: String ``` |

Modified AVMetadata3GPUserDataKeyGenre

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyGenre: NSString! ``` |
| To | ``` let AVMetadata3GPUserDataKeyGenre: String ``` |

Modified AVMetadata3GPUserDataKeyKeywordList

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyKeywordList: NSString! ``` |
| To | ``` let AVMetadata3GPUserDataKeyKeywordList: String ``` |

Modified AVMetadata3GPUserDataKeyLocation

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyLocation: NSString! ``` |
| To | ``` let AVMetadata3GPUserDataKeyLocation: String ``` |

Modified AVMetadata3GPUserDataKeyMediaClassification

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyMediaClassification: NSString! ``` |
| To | ``` let AVMetadata3GPUserDataKeyMediaClassification: String ``` |

Modified AVMetadata3GPUserDataKeyMediaRating

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyMediaRating: NSString! ``` |
| To | ``` let AVMetadata3GPUserDataKeyMediaRating: String ``` |

Modified AVMetadata3GPUserDataKeyPerformer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyPerformer: NSString! ``` |
| To | ``` let AVMetadata3GPUserDataKeyPerformer: String ``` |

Modified AVMetadata3GPUserDataKeyRecordingYear

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyRecordingYear: NSString! ``` |
| To | ``` let AVMetadata3GPUserDataKeyRecordingYear: String ``` |

Modified AVMetadata3GPUserDataKeyThumbnail

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyThumbnail: NSString! ``` |
| To | ``` let AVMetadata3GPUserDataKeyThumbnail: String ``` |

Modified AVMetadata3GPUserDataKeyTitle

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyTitle: NSString! ``` |
| To | ``` let AVMetadata3GPUserDataKeyTitle: String ``` |

Modified AVMetadata3GPUserDataKeyUserRating

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadata3GPUserDataKeyUserRating: NSString! ``` |
| To | ``` let AVMetadata3GPUserDataKeyUserRating: String ``` |

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

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeyAlbumName: NSString! ``` |
| To | ``` let AVMetadataCommonKeyAlbumName: String ``` |

Modified AVMetadataCommonKeyArtist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeyArtist: NSString! ``` |
| To | ``` let AVMetadataCommonKeyArtist: String ``` |

Modified AVMetadataCommonKeyArtwork

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeyArtwork: NSString! ``` |
| To | ``` let AVMetadataCommonKeyArtwork: String ``` |

Modified AVMetadataCommonKeyAuthor

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeyAuthor: NSString! ``` |
| To | ``` let AVMetadataCommonKeyAuthor: String ``` |

Modified AVMetadataCommonKeyContributor

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeyContributor: NSString! ``` |
| To | ``` let AVMetadataCommonKeyContributor: String ``` |

Modified AVMetadataCommonKeyCopyrights

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeyCopyrights: NSString! ``` |
| To | ``` let AVMetadataCommonKeyCopyrights: String ``` |

Modified AVMetadataCommonKeyCreationDate

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeyCreationDate: NSString! ``` |
| To | ``` let AVMetadataCommonKeyCreationDate: String ``` |

Modified AVMetadataCommonKeyCreator

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeyCreator: NSString! ``` |
| To | ``` let AVMetadataCommonKeyCreator: String ``` |

Modified AVMetadataCommonKeyDescription

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeyDescription: NSString! ``` |
| To | ``` let AVMetadataCommonKeyDescription: String ``` |

Modified AVMetadataCommonKeyFormat

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeyFormat: NSString! ``` |
| To | ``` let AVMetadataCommonKeyFormat: String ``` |

Modified AVMetadataCommonKeyIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeyIdentifier: NSString! ``` |
| To | ``` let AVMetadataCommonKeyIdentifier: String ``` |

Modified AVMetadataCommonKeyLanguage

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeyLanguage: NSString! ``` |
| To | ``` let AVMetadataCommonKeyLanguage: String ``` |

Modified AVMetadataCommonKeyLastModifiedDate

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeyLastModifiedDate: NSString! ``` |
| To | ``` let AVMetadataCommonKeyLastModifiedDate: String ``` |

Modified AVMetadataCommonKeyLocation

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeyLocation: NSString! ``` |
| To | ``` let AVMetadataCommonKeyLocation: String ``` |

Modified AVMetadataCommonKeyMake

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeyMake: NSString! ``` |
| To | ``` let AVMetadataCommonKeyMake: String ``` |

Modified AVMetadataCommonKeyModel

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeyModel: NSString! ``` |
| To | ``` let AVMetadataCommonKeyModel: String ``` |

Modified AVMetadataCommonKeyPublisher

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeyPublisher: NSString! ``` |
| To | ``` let AVMetadataCommonKeyPublisher: String ``` |

Modified AVMetadataCommonKeyRelation

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeyRelation: NSString! ``` |
| To | ``` let AVMetadataCommonKeyRelation: String ``` |

Modified AVMetadataCommonKeySoftware

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeySoftware: NSString! ``` |
| To | ``` let AVMetadataCommonKeySoftware: String ``` |

Modified AVMetadataCommonKeySource

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeySource: NSString! ``` |
| To | ``` let AVMetadataCommonKeySource: String ``` |

Modified AVMetadataCommonKeySubject

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeySubject: NSString! ``` |
| To | ``` let AVMetadataCommonKeySubject: String ``` |

Modified AVMetadataCommonKeyTitle

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeyTitle: NSString! ``` |
| To | ``` let AVMetadataCommonKeyTitle: String ``` |

Modified AVMetadataCommonKeyType

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataCommonKeyType: NSString! ``` |
| To | ``` let AVMetadataCommonKeyType: String ``` |

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

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataFormatID3Metadata: NSString! ``` |
| To | ``` let AVMetadataFormatID3Metadata: String ``` |

Modified AVMetadataFormatISOUserData

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataFormatISOUserData: NSString! ``` |
| To | ``` let AVMetadataFormatISOUserData: String ``` |

Modified AVMetadataFormatQuickTimeMetadata

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataFormatQuickTimeMetadata: NSString! ``` |
| To | ``` let AVMetadataFormatQuickTimeMetadata: String ``` |

Modified AVMetadataFormatQuickTimeUserData

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataFormatQuickTimeUserData: NSString! ``` |
| To | ``` let AVMetadataFormatQuickTimeUserData: String ``` |

Modified AVMetadataFormatiTunesMetadata

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataFormatiTunesMetadata: NSString! ``` |
| To | ``` let AVMetadataFormatiTunesMetadata: String ``` |

Modified AVMetadataID3MetadataKeyAlbumSortOrder

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyAlbumSortOrder: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyAlbumSortOrder: String ``` |

Modified AVMetadataID3MetadataKeyAlbumTitle

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyAlbumTitle: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyAlbumTitle: String ``` |

Modified AVMetadataID3MetadataKeyAttachedPicture

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyAttachedPicture: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyAttachedPicture: String ``` |

Modified AVMetadataID3MetadataKeyAudioEncryption

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyAudioEncryption: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyAudioEncryption: String ``` |

Modified AVMetadataID3MetadataKeyAudioSeekPointIndex

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyAudioSeekPointIndex: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyAudioSeekPointIndex: String ``` |

Modified AVMetadataID3MetadataKeyBand

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyBand: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyBand: String ``` |

Modified AVMetadataID3MetadataKeyBeatsPerMinute

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyBeatsPerMinute: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyBeatsPerMinute: String ``` |

Modified AVMetadataID3MetadataKeyComments

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyComments: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyComments: String ``` |

Modified AVMetadataID3MetadataKeyCommercialInformation

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyCommercialInformation: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyCommercialInformation: String ``` |

Modified AVMetadataID3MetadataKeyCommerical

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyCommerical: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyCommerical: String ``` |

Modified AVMetadataID3MetadataKeyComposer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyComposer: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyComposer: String ``` |

Modified AVMetadataID3MetadataKeyConductor

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyConductor: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyConductor: String ``` |

Modified AVMetadataID3MetadataKeyContentGroupDescription

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyContentGroupDescription: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyContentGroupDescription: String ``` |

Modified AVMetadataID3MetadataKeyContentType

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyContentType: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyContentType: String ``` |

Modified AVMetadataID3MetadataKeyCopyright

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyCopyright: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyCopyright: String ``` |

Modified AVMetadataID3MetadataKeyCopyrightInformation

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyCopyrightInformation: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyCopyrightInformation: String ``` |

Modified AVMetadataID3MetadataKeyDate

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyDate: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyDate: String ``` |

Modified AVMetadataID3MetadataKeyEncodedBy

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyEncodedBy: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyEncodedBy: String ``` |

Modified AVMetadataID3MetadataKeyEncodedWith

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyEncodedWith: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyEncodedWith: String ``` |

Modified AVMetadataID3MetadataKeyEncodingTime

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyEncodingTime: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyEncodingTime: String ``` |

Modified AVMetadataID3MetadataKeyEncryption

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyEncryption: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyEncryption: String ``` |

Modified AVMetadataID3MetadataKeyEqualization

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyEqualization: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyEqualization: String ``` |

Modified AVMetadataID3MetadataKeyEqualization2

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyEqualization2: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyEqualization2: String ``` |

Modified AVMetadataID3MetadataKeyEventTimingCodes

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyEventTimingCodes: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyEventTimingCodes: String ``` |

Modified AVMetadataID3MetadataKeyFileOwner

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyFileOwner: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyFileOwner: String ``` |

Modified AVMetadataID3MetadataKeyFileType

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyFileType: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyFileType: String ``` |

Modified AVMetadataID3MetadataKeyGeneralEncapsulatedObject

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyGeneralEncapsulatedObject: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyGeneralEncapsulatedObject: String ``` |

Modified AVMetadataID3MetadataKeyGroupIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyGroupIdentifier: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyGroupIdentifier: String ``` |

Modified AVMetadataID3MetadataKeyInitialKey

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyInitialKey: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyInitialKey: String ``` |

Modified AVMetadataID3MetadataKeyInternationalStandardRecordingCode

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyInternationalStandardRecordingCode: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyInternationalStandardRecordingCode: String ``` |

Modified AVMetadataID3MetadataKeyInternetRadioStationName

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyInternetRadioStationName: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyInternetRadioStationName: String ``` |

Modified AVMetadataID3MetadataKeyInternetRadioStationOwner

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyInternetRadioStationOwner: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyInternetRadioStationOwner: String ``` |

Modified AVMetadataID3MetadataKeyInvolvedPeopleList_v23

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyInvolvedPeopleList_v23: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyInvolvedPeopleList_v23: String ``` |

Modified AVMetadataID3MetadataKeyInvolvedPeopleList_v24

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyInvolvedPeopleList_v24: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyInvolvedPeopleList_v24: String ``` |

Modified AVMetadataID3MetadataKeyLanguage

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyLanguage: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyLanguage: String ``` |

Modified AVMetadataID3MetadataKeyLeadPerformer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyLeadPerformer: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyLeadPerformer: String ``` |

Modified AVMetadataID3MetadataKeyLength

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyLength: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyLength: String ``` |

Modified AVMetadataID3MetadataKeyLink

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyLink: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyLink: String ``` |

Modified AVMetadataID3MetadataKeyLyricist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyLyricist: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyLyricist: String ``` |

Modified AVMetadataID3MetadataKeyMPEGLocationLookupTable

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyMPEGLocationLookupTable: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyMPEGLocationLookupTable: String ``` |

Modified AVMetadataID3MetadataKeyMediaType

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyMediaType: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyMediaType: String ``` |

Modified AVMetadataID3MetadataKeyModifiedBy

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyModifiedBy: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyModifiedBy: String ``` |

Modified AVMetadataID3MetadataKeyMood

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyMood: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyMood: String ``` |

Modified AVMetadataID3MetadataKeyMusicCDIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyMusicCDIdentifier: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyMusicCDIdentifier: String ``` |

Modified AVMetadataID3MetadataKeyMusicianCreditsList

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyMusicianCreditsList: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyMusicianCreditsList: String ``` |

Modified AVMetadataID3MetadataKeyOfficialArtistWebpage

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOfficialArtistWebpage: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyOfficialArtistWebpage: String ``` |

Modified AVMetadataID3MetadataKeyOfficialAudioFileWebpage

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOfficialAudioFileWebpage: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyOfficialAudioFileWebpage: String ``` |

Modified AVMetadataID3MetadataKeyOfficialAudioSourceWebpage

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOfficialAudioSourceWebpage: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyOfficialAudioSourceWebpage: String ``` |

Modified AVMetadataID3MetadataKeyOfficialInternetRadioStationHomepage

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOfficialInternetRadioStationHomepage: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyOfficialInternetRadioStationHomepage: String ``` |

Modified AVMetadataID3MetadataKeyOfficialPublisherWebpage

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOfficialPublisherWebpage: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyOfficialPublisherWebpage: String ``` |

Modified AVMetadataID3MetadataKeyOriginalAlbumTitle

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOriginalAlbumTitle: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyOriginalAlbumTitle: String ``` |

Modified AVMetadataID3MetadataKeyOriginalArtist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOriginalArtist: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyOriginalArtist: String ``` |

Modified AVMetadataID3MetadataKeyOriginalFilename

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOriginalFilename: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyOriginalFilename: String ``` |

Modified AVMetadataID3MetadataKeyOriginalLyricist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOriginalLyricist: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyOriginalLyricist: String ``` |

Modified AVMetadataID3MetadataKeyOriginalReleaseTime

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOriginalReleaseTime: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyOriginalReleaseTime: String ``` |

Modified AVMetadataID3MetadataKeyOriginalReleaseYear

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOriginalReleaseYear: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyOriginalReleaseYear: String ``` |

Modified AVMetadataID3MetadataKeyOwnership

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyOwnership: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyOwnership: String ``` |

Modified AVMetadataID3MetadataKeyPartOfASet

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyPartOfASet: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyPartOfASet: String ``` |

Modified AVMetadataID3MetadataKeyPayment

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyPayment: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyPayment: String ``` |

Modified AVMetadataID3MetadataKeyPerformerSortOrder

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyPerformerSortOrder: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyPerformerSortOrder: String ``` |

Modified AVMetadataID3MetadataKeyPlayCounter

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyPlayCounter: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyPlayCounter: String ``` |

Modified AVMetadataID3MetadataKeyPlaylistDelay

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyPlaylistDelay: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyPlaylistDelay: String ``` |

Modified AVMetadataID3MetadataKeyPopularimeter

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyPopularimeter: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyPopularimeter: String ``` |

Modified AVMetadataID3MetadataKeyPositionSynchronization

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyPositionSynchronization: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyPositionSynchronization: String ``` |

Modified AVMetadataID3MetadataKeyPrivate

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyPrivate: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyPrivate: String ``` |

Modified AVMetadataID3MetadataKeyProducedNotice

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyProducedNotice: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyProducedNotice: String ``` |

Modified AVMetadataID3MetadataKeyPublisher

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyPublisher: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyPublisher: String ``` |

Modified AVMetadataID3MetadataKeyRecommendedBufferSize

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyRecommendedBufferSize: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyRecommendedBufferSize: String ``` |

Modified AVMetadataID3MetadataKeyRecordingDates

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyRecordingDates: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyRecordingDates: String ``` |

Modified AVMetadataID3MetadataKeyRecordingTime

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyRecordingTime: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyRecordingTime: String ``` |

Modified AVMetadataID3MetadataKeyRelativeVolumeAdjustment

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyRelativeVolumeAdjustment: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyRelativeVolumeAdjustment: String ``` |

Modified AVMetadataID3MetadataKeyRelativeVolumeAdjustment2

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyRelativeVolumeAdjustment2: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyRelativeVolumeAdjustment2: String ``` |

Modified AVMetadataID3MetadataKeyReleaseTime

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyReleaseTime: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyReleaseTime: String ``` |

Modified AVMetadataID3MetadataKeyReverb

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyReverb: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyReverb: String ``` |

Modified AVMetadataID3MetadataKeySeek

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeySeek: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeySeek: String ``` |

Modified AVMetadataID3MetadataKeySetSubtitle

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeySetSubtitle: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeySetSubtitle: String ``` |

Modified AVMetadataID3MetadataKeySignature

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeySignature: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeySignature: String ``` |

Modified AVMetadataID3MetadataKeySize

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeySize: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeySize: String ``` |

Modified AVMetadataID3MetadataKeySubTitle

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeySubTitle: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeySubTitle: String ``` |

Modified AVMetadataID3MetadataKeySynchronizedLyric

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeySynchronizedLyric: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeySynchronizedLyric: String ``` |

Modified AVMetadataID3MetadataKeySynchronizedTempoCodes

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeySynchronizedTempoCodes: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeySynchronizedTempoCodes: String ``` |

Modified AVMetadataID3MetadataKeyTaggingTime

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyTaggingTime: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyTaggingTime: String ``` |

Modified AVMetadataID3MetadataKeyTermsOfUse

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyTermsOfUse: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyTermsOfUse: String ``` |

Modified AVMetadataID3MetadataKeyTime

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyTime: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyTime: String ``` |

Modified AVMetadataID3MetadataKeyTitleDescription

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyTitleDescription: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyTitleDescription: String ``` |

Modified AVMetadataID3MetadataKeyTitleSortOrder

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyTitleSortOrder: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyTitleSortOrder: String ``` |

Modified AVMetadataID3MetadataKeyTrackNumber

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyTrackNumber: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyTrackNumber: String ``` |

Modified AVMetadataID3MetadataKeyUniqueFileIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyUniqueFileIdentifier: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyUniqueFileIdentifier: String ``` |

Modified AVMetadataID3MetadataKeyUnsynchronizedLyric

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyUnsynchronizedLyric: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyUnsynchronizedLyric: String ``` |

Modified AVMetadataID3MetadataKeyUserText

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyUserText: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyUserText: String ``` |

Modified AVMetadataID3MetadataKeyUserURL

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyUserURL: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyUserURL: String ``` |

Modified AVMetadataID3MetadataKeyYear

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataID3MetadataKeyYear: NSString! ``` |
| To | ``` let AVMetadataID3MetadataKeyYear: String ``` |

Modified AVMetadataISOUserDataKeyCopyright

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataISOUserDataKeyCopyright: NSString! ``` |
| To | ``` let AVMetadataISOUserDataKeyCopyright: String ``` |

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

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataKeySpaceCommon: NSString! ``` |
| To | ``` let AVMetadataKeySpaceCommon: String ``` |

Modified AVMetadataKeySpaceID3

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataKeySpaceID3: NSString! ``` |
| To | ``` let AVMetadataKeySpaceID3: String ``` |

Modified AVMetadataKeySpaceISOUserData

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataKeySpaceISOUserData: NSString! ``` |
| To | ``` let AVMetadataKeySpaceISOUserData: String ``` |

Modified AVMetadataKeySpaceIcy

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataKeySpaceIcy: NSString! ``` |
| To | ``` let AVMetadataKeySpaceIcy: String ``` |

Modified AVMetadataKeySpaceQuickTimeMetadata

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataKeySpaceQuickTimeMetadata: NSString! ``` |
| To | ``` let AVMetadataKeySpaceQuickTimeMetadata: String ``` |

Modified AVMetadataKeySpaceQuickTimeUserData

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataKeySpaceQuickTimeUserData: NSString! ``` |
| To | ``` let AVMetadataKeySpaceQuickTimeUserData: String ``` |

Modified AVMetadataKeySpaceiTunes

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataKeySpaceiTunes: NSString! ``` |
| To | ``` let AVMetadataKeySpaceiTunes: String ``` |

Modified AVMetadataObjectTypeAztecCode

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataObjectTypeAztecCode: NSString! ``` |
| To | ``` let AVMetadataObjectTypeAztecCode: String ``` |

Modified AVMetadataObjectTypeCode128Code

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataObjectTypeCode128Code: NSString! ``` |
| To | ``` let AVMetadataObjectTypeCode128Code: String ``` |

Modified AVMetadataObjectTypeCode39Code

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataObjectTypeCode39Code: NSString! ``` |
| To | ``` let AVMetadataObjectTypeCode39Code: String ``` |

Modified AVMetadataObjectTypeCode39Mod43Code

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataObjectTypeCode39Mod43Code: NSString! ``` |
| To | ``` let AVMetadataObjectTypeCode39Mod43Code: String ``` |

Modified AVMetadataObjectTypeCode93Code

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataObjectTypeCode93Code: NSString! ``` |
| To | ``` let AVMetadataObjectTypeCode93Code: String ``` |

Modified AVMetadataObjectTypeDataMatrixCode

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataObjectTypeDataMatrixCode: NSString! ``` |
| To | ``` let AVMetadataObjectTypeDataMatrixCode: String ``` |

Modified AVMetadataObjectTypeEAN13Code

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataObjectTypeEAN13Code: NSString! ``` |
| To | ``` let AVMetadataObjectTypeEAN13Code: String ``` |

Modified AVMetadataObjectTypeEAN8Code

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataObjectTypeEAN8Code: NSString! ``` |
| To | ``` let AVMetadataObjectTypeEAN8Code: String ``` |

Modified AVMetadataObjectTypeFace

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataObjectTypeFace: NSString! ``` |
| To | ``` let AVMetadataObjectTypeFace: String ``` |

Modified AVMetadataObjectTypeITF14Code

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataObjectTypeITF14Code: NSString! ``` |
| To | ``` let AVMetadataObjectTypeITF14Code: String ``` |

Modified AVMetadataObjectTypeInterleaved2of5Code

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataObjectTypeInterleaved2of5Code: NSString! ``` |
| To | ``` let AVMetadataObjectTypeInterleaved2of5Code: String ``` |

Modified AVMetadataObjectTypePDF417Code

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataObjectTypePDF417Code: NSString! ``` |
| To | ``` let AVMetadataObjectTypePDF417Code: String ``` |

Modified AVMetadataObjectTypeQRCode

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataObjectTypeQRCode: NSString! ``` |
| To | ``` let AVMetadataObjectTypeQRCode: String ``` |

Modified AVMetadataObjectTypeUPCECode

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataObjectTypeUPCECode: NSString! ``` |
| To | ``` let AVMetadataObjectTypeUPCECode: String ``` |

Modified AVMetadataQuickTimeMetadataKeyAlbum

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyAlbum: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyAlbum: String ``` |

Modified AVMetadataQuickTimeMetadataKeyArranger

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyArranger: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyArranger: String ``` |

Modified AVMetadataQuickTimeMetadataKeyArtist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyArtist: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyArtist: String ``` |

Modified AVMetadataQuickTimeMetadataKeyArtwork

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyArtwork: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyArtwork: String ``` |

Modified AVMetadataQuickTimeMetadataKeyAuthor

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyAuthor: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyAuthor: String ``` |

Modified AVMetadataQuickTimeMetadataKeyCameraFrameReadoutTime

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyCameraFrameReadoutTime: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyCameraFrameReadoutTime: String ``` |

Modified AVMetadataQuickTimeMetadataKeyCameraIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyCameraIdentifier: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyCameraIdentifier: String ``` |

Modified AVMetadataQuickTimeMetadataKeyCollectionUser

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyCollectionUser: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyCollectionUser: String ``` |

Modified AVMetadataQuickTimeMetadataKeyComment

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyComment: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyComment: String ``` |

Modified AVMetadataQuickTimeMetadataKeyComposer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyComposer: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyComposer: String ``` |

Modified AVMetadataQuickTimeMetadataKeyCopyright

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyCopyright: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyCopyright: String ``` |

Modified AVMetadataQuickTimeMetadataKeyCreationDate

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyCreationDate: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyCreationDate: String ``` |

Modified AVMetadataQuickTimeMetadataKeyCredits

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyCredits: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyCredits: String ``` |

Modified AVMetadataQuickTimeMetadataKeyDescription

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyDescription: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyDescription: String ``` |

Modified AVMetadataQuickTimeMetadataKeyDirectionFacing

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyDirectionFacing: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyDirectionFacing: String ``` |

Modified AVMetadataQuickTimeMetadataKeyDirectionMotion

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyDirectionMotion: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyDirectionMotion: String ``` |

Modified AVMetadataQuickTimeMetadataKeyDirector

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyDirector: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyDirector: String ``` |

Modified AVMetadataQuickTimeMetadataKeyDisplayName

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyDisplayName: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyDisplayName: String ``` |

Modified AVMetadataQuickTimeMetadataKeyEncodedBy

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyEncodedBy: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyEncodedBy: String ``` |

Modified AVMetadataQuickTimeMetadataKeyGenre

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyGenre: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyGenre: String ``` |

Modified AVMetadataQuickTimeMetadataKeyInformation

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyInformation: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyInformation: String ``` |

Modified AVMetadataQuickTimeMetadataKeyKeywords

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyKeywords: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyKeywords: String ``` |

Modified AVMetadataQuickTimeMetadataKeyLocationBody

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyLocationBody: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyLocationBody: String ``` |

Modified AVMetadataQuickTimeMetadataKeyLocationDate

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyLocationDate: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyLocationDate: String ``` |

Modified AVMetadataQuickTimeMetadataKeyLocationISO6709

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyLocationISO6709: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyLocationISO6709: String ``` |

Modified AVMetadataQuickTimeMetadataKeyLocationName

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyLocationName: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyLocationName: String ``` |

Modified AVMetadataQuickTimeMetadataKeyLocationNote

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyLocationNote: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyLocationNote: String ``` |

Modified AVMetadataQuickTimeMetadataKeyLocationRole

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyLocationRole: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyLocationRole: String ``` |

Modified AVMetadataQuickTimeMetadataKeyMake

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyMake: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyMake: String ``` |

Modified AVMetadataQuickTimeMetadataKeyModel

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyModel: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyModel: String ``` |

Modified AVMetadataQuickTimeMetadataKeyOriginalArtist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyOriginalArtist: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyOriginalArtist: String ``` |

Modified AVMetadataQuickTimeMetadataKeyPerformer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyPerformer: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyPerformer: String ``` |

Modified AVMetadataQuickTimeMetadataKeyPhonogramRights

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyPhonogramRights: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyPhonogramRights: String ``` |

Modified AVMetadataQuickTimeMetadataKeyProducer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyProducer: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyProducer: String ``` |

Modified AVMetadataQuickTimeMetadataKeyPublisher

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyPublisher: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyPublisher: String ``` |

Modified AVMetadataQuickTimeMetadataKeyRatingUser

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyRatingUser: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyRatingUser: String ``` |

Modified AVMetadataQuickTimeMetadataKeySoftware

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeySoftware: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeySoftware: String ``` |

Modified AVMetadataQuickTimeMetadataKeyTitle

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyTitle: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyTitle: String ``` |

Modified AVMetadataQuickTimeMetadataKeyYear

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyYear: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyYear: String ``` |

Modified AVMetadataQuickTimeMetadataKeyiXML

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeMetadataKeyiXML: NSString! ``` |
| To | ``` let AVMetadataQuickTimeMetadataKeyiXML: String ``` |

Modified AVMetadataQuickTimeUserDataKeyAlbum

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyAlbum: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyAlbum: String ``` |

Modified AVMetadataQuickTimeUserDataKeyArranger

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyArranger: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyArranger: String ``` |

Modified AVMetadataQuickTimeUserDataKeyArtist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyArtist: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyArtist: String ``` |

Modified AVMetadataQuickTimeUserDataKeyAuthor

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyAuthor: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyAuthor: String ``` |

Modified AVMetadataQuickTimeUserDataKeyChapter

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyChapter: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyChapter: String ``` |

Modified AVMetadataQuickTimeUserDataKeyComment

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyComment: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyComment: String ``` |

Modified AVMetadataQuickTimeUserDataKeyComposer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyComposer: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyComposer: String ``` |

Modified AVMetadataQuickTimeUserDataKeyCopyright

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyCopyright: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyCopyright: String ``` |

Modified AVMetadataQuickTimeUserDataKeyCreationDate

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyCreationDate: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyCreationDate: String ``` |

Modified AVMetadataQuickTimeUserDataKeyCredits

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyCredits: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyCredits: String ``` |

Modified AVMetadataQuickTimeUserDataKeyDescription

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyDescription: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyDescription: String ``` |

Modified AVMetadataQuickTimeUserDataKeyDirector

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyDirector: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyDirector: String ``` |

Modified AVMetadataQuickTimeUserDataKeyDisclaimer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyDisclaimer: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyDisclaimer: String ``` |

Modified AVMetadataQuickTimeUserDataKeyEncodedBy

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyEncodedBy: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyEncodedBy: String ``` |

Modified AVMetadataQuickTimeUserDataKeyFullName

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyFullName: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyFullName: String ``` |

Modified AVMetadataQuickTimeUserDataKeyGenre

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyGenre: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyGenre: String ``` |

Modified AVMetadataQuickTimeUserDataKeyHostComputer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyHostComputer: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyHostComputer: String ``` |

Modified AVMetadataQuickTimeUserDataKeyInformation

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyInformation: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyInformation: String ``` |

Modified AVMetadataQuickTimeUserDataKeyKeywords

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyKeywords: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyKeywords: String ``` |

Modified AVMetadataQuickTimeUserDataKeyLocationISO6709

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyLocationISO6709: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyLocationISO6709: String ``` |

Modified AVMetadataQuickTimeUserDataKeyMake

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyMake: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyMake: String ``` |

Modified AVMetadataQuickTimeUserDataKeyModel

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyModel: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyModel: String ``` |

Modified AVMetadataQuickTimeUserDataKeyOriginalArtist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyOriginalArtist: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyOriginalArtist: String ``` |

Modified AVMetadataQuickTimeUserDataKeyOriginalFormat

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyOriginalFormat: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyOriginalFormat: String ``` |

Modified AVMetadataQuickTimeUserDataKeyOriginalSource

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyOriginalSource: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyOriginalSource: String ``` |

Modified AVMetadataQuickTimeUserDataKeyPerformers

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyPerformers: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyPerformers: String ``` |

Modified AVMetadataQuickTimeUserDataKeyPhonogramRights

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyPhonogramRights: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyPhonogramRights: String ``` |

Modified AVMetadataQuickTimeUserDataKeyProducer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyProducer: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyProducer: String ``` |

Modified AVMetadataQuickTimeUserDataKeyProduct

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyProduct: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyProduct: String ``` |

Modified AVMetadataQuickTimeUserDataKeyPublisher

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyPublisher: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyPublisher: String ``` |

Modified AVMetadataQuickTimeUserDataKeySoftware

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeySoftware: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeySoftware: String ``` |

Modified AVMetadataQuickTimeUserDataKeySpecialPlaybackRequirements

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeySpecialPlaybackRequirements: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeySpecialPlaybackRequirements: String ``` |

Modified AVMetadataQuickTimeUserDataKeyTaggedCharacteristic

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyTaggedCharacteristic: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyTaggedCharacteristic: String ``` |

Modified AVMetadataQuickTimeUserDataKeyTrack

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyTrack: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyTrack: String ``` |

Modified AVMetadataQuickTimeUserDataKeyTrackName

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyTrackName: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyTrackName: String ``` |

Modified AVMetadataQuickTimeUserDataKeyURLLink

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyURLLink: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyURLLink: String ``` |

Modified AVMetadataQuickTimeUserDataKeyWarning

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyWarning: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyWarning: String ``` |

Modified AVMetadataQuickTimeUserDataKeyWriter

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataQuickTimeUserDataKeyWriter: NSString! ``` |
| To | ``` let AVMetadataQuickTimeUserDataKeyWriter: String ``` |

Modified AVMetadataiTunesMetadataKeyAccountKind

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyAccountKind: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyAccountKind: String ``` |

Modified AVMetadataiTunesMetadataKeyAcknowledgement

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyAcknowledgement: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyAcknowledgement: String ``` |

Modified AVMetadataiTunesMetadataKeyAlbum

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyAlbum: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyAlbum: String ``` |

Modified AVMetadataiTunesMetadataKeyAlbumArtist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyAlbumArtist: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyAlbumArtist: String ``` |

Modified AVMetadataiTunesMetadataKeyAppleID

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyAppleID: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyAppleID: String ``` |

Modified AVMetadataiTunesMetadataKeyArranger

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyArranger: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyArranger: String ``` |

Modified AVMetadataiTunesMetadataKeyArtDirector

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyArtDirector: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyArtDirector: String ``` |

Modified AVMetadataiTunesMetadataKeyArtist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyArtist: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyArtist: String ``` |

Modified AVMetadataiTunesMetadataKeyArtistID

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyArtistID: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyArtistID: String ``` |

Modified AVMetadataiTunesMetadataKeyAuthor

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyAuthor: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyAuthor: String ``` |

Modified AVMetadataiTunesMetadataKeyBeatsPerMin

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyBeatsPerMin: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyBeatsPerMin: String ``` |

Modified AVMetadataiTunesMetadataKeyComposer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyComposer: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyComposer: String ``` |

Modified AVMetadataiTunesMetadataKeyConductor

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyConductor: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyConductor: String ``` |

Modified AVMetadataiTunesMetadataKeyContentRating

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyContentRating: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyContentRating: String ``` |

Modified AVMetadataiTunesMetadataKeyCopyright

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyCopyright: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyCopyright: String ``` |

Modified AVMetadataiTunesMetadataKeyCoverArt

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyCoverArt: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyCoverArt: String ``` |

Modified AVMetadataiTunesMetadataKeyCredits

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyCredits: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyCredits: String ``` |

Modified AVMetadataiTunesMetadataKeyDescription

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyDescription: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyDescription: String ``` |

Modified AVMetadataiTunesMetadataKeyDirector

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyDirector: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyDirector: String ``` |

Modified AVMetadataiTunesMetadataKeyDiscCompilation

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyDiscCompilation: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyDiscCompilation: String ``` |

Modified AVMetadataiTunesMetadataKeyDiscNumber

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyDiscNumber: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyDiscNumber: String ``` |

Modified AVMetadataiTunesMetadataKeyEQ

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyEQ: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyEQ: String ``` |

Modified AVMetadataiTunesMetadataKeyEncodedBy

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyEncodedBy: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyEncodedBy: String ``` |

Modified AVMetadataiTunesMetadataKeyEncodingTool

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyEncodingTool: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyEncodingTool: String ``` |

Modified AVMetadataiTunesMetadataKeyExecProducer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyExecProducer: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyExecProducer: String ``` |

Modified AVMetadataiTunesMetadataKeyGenreID

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyGenreID: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyGenreID: String ``` |

Modified AVMetadataiTunesMetadataKeyGrouping

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyGrouping: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyGrouping: String ``` |

Modified AVMetadataiTunesMetadataKeyLinerNotes

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyLinerNotes: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyLinerNotes: String ``` |

Modified AVMetadataiTunesMetadataKeyLyrics

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyLyrics: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyLyrics: String ``` |

Modified AVMetadataiTunesMetadataKeyOnlineExtras

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyOnlineExtras: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyOnlineExtras: String ``` |

Modified AVMetadataiTunesMetadataKeyOriginalArtist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyOriginalArtist: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyOriginalArtist: String ``` |

Modified AVMetadataiTunesMetadataKeyPerformer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyPerformer: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyPerformer: String ``` |

Modified AVMetadataiTunesMetadataKeyPhonogramRights

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyPhonogramRights: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyPhonogramRights: String ``` |

Modified AVMetadataiTunesMetadataKeyPlaylistID

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyPlaylistID: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyPlaylistID: String ``` |

Modified AVMetadataiTunesMetadataKeyPredefinedGenre

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyPredefinedGenre: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyPredefinedGenre: String ``` |

Modified AVMetadataiTunesMetadataKeyProducer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyProducer: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyProducer: String ``` |

Modified AVMetadataiTunesMetadataKeyPublisher

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyPublisher: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyPublisher: String ``` |

Modified AVMetadataiTunesMetadataKeyRecordCompany

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyRecordCompany: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyRecordCompany: String ``` |

Modified AVMetadataiTunesMetadataKeyReleaseDate

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyReleaseDate: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyReleaseDate: String ``` |

Modified AVMetadataiTunesMetadataKeySoloist

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeySoloist: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeySoloist: String ``` |

Modified AVMetadataiTunesMetadataKeySongID

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeySongID: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeySongID: String ``` |

Modified AVMetadataiTunesMetadataKeySongName

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeySongName: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeySongName: String ``` |

Modified AVMetadataiTunesMetadataKeySoundEngineer

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeySoundEngineer: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeySoundEngineer: String ``` |

Modified AVMetadataiTunesMetadataKeyThanks

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyThanks: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyThanks: String ``` |

Modified AVMetadataiTunesMetadataKeyTrackNumber

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyTrackNumber: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyTrackNumber: String ``` |

Modified AVMetadataiTunesMetadataKeyTrackSubTitle

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyTrackSubTitle: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyTrackSubTitle: String ``` |

Modified AVMetadataiTunesMetadataKeyUserComment

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyUserComment: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyUserComment: String ``` |

Modified AVMetadataiTunesMetadataKeyUserGenre

|  | Declaration |
| --- | --- |
| From | ``` let AVMetadataiTunesMetadataKeyUserGenre: NSString! ``` |
| To | ``` let AVMetadataiTunesMetadataKeyUserGenre: String ``` |

Modified AVNumberOfChannelsKey

|  | Declaration |
| --- | --- |
| From | ``` let AVNumberOfChannelsKey: NSString! ``` |
| To | ``` let AVNumberOfChannelsKey: String ``` |

Modified AVOutputSettingsPreset1280x720

|  | Declaration |
| --- | --- |
| From | ``` let AVOutputSettingsPreset1280x720: NSString! ``` |
| To | ``` let AVOutputSettingsPreset1280x720: String ``` |

Modified AVOutputSettingsPreset1920x1080

|  | Declaration |
| --- | --- |
| From | ``` let AVOutputSettingsPreset1920x1080: NSString! ``` |
| To | ``` let AVOutputSettingsPreset1920x1080: String ``` |

Modified AVOutputSettingsPreset640x480

|  | Declaration |
| --- | --- |
| From | ``` let AVOutputSettingsPreset640x480: NSString! ``` |
| To | ``` let AVOutputSettingsPreset640x480: String ``` |

Modified AVOutputSettingsPreset960x540

|  | Declaration |
| --- | --- |
| From | ``` let AVOutputSettingsPreset960x540: NSString! ``` |
| To | ``` let AVOutputSettingsPreset960x540: String ``` |

Modified AVPlayerItemDidPlayToEndTimeNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVPlayerItemDidPlayToEndTimeNotification: NSString! ``` |
| To | ``` let AVPlayerItemDidPlayToEndTimeNotification: String ``` |

Modified AVPlayerItemFailedToPlayToEndTimeErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let AVPlayerItemFailedToPlayToEndTimeErrorKey: NSString! ``` |
| To | ``` let AVPlayerItemFailedToPlayToEndTimeErrorKey: String ``` |

Modified AVPlayerItemFailedToPlayToEndTimeNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVPlayerItemFailedToPlayToEndTimeNotification: NSString! ``` |
| To | ``` let AVPlayerItemFailedToPlayToEndTimeNotification: String ``` |

Modified AVPlayerItemLegibleOutputTextStylingResolutionDefault

|  | Declaration |
| --- | --- |
| From | ``` let AVPlayerItemLegibleOutputTextStylingResolutionDefault: NSString! ``` |
| To | ``` let AVPlayerItemLegibleOutputTextStylingResolutionDefault: String ``` |

Modified AVPlayerItemLegibleOutputTextStylingResolutionSourceAndRulesOnly

|  | Declaration |
| --- | --- |
| From | ``` let AVPlayerItemLegibleOutputTextStylingResolutionSourceAndRulesOnly: NSString! ``` |
| To | ``` let AVPlayerItemLegibleOutputTextStylingResolutionSourceAndRulesOnly: String ``` |

Modified AVPlayerItemNewAccessLogEntryNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVPlayerItemNewAccessLogEntryNotification: NSString! ``` |
| To | ``` let AVPlayerItemNewAccessLogEntryNotification: String ``` |

Modified AVPlayerItemNewErrorLogEntryNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVPlayerItemNewErrorLogEntryNotification: NSString! ``` |
| To | ``` let AVPlayerItemNewErrorLogEntryNotification: String ``` |

Modified AVPlayerItemPlaybackStalledNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVPlayerItemPlaybackStalledNotification: NSString! ``` |
| To | ``` let AVPlayerItemPlaybackStalledNotification: String ``` |

Modified AVPlayerItemTimeJumpedNotification

|  | Declaration |
| --- | --- |
| From | ``` let AVPlayerItemTimeJumpedNotification: NSString! ``` |
| To | ``` let AVPlayerItemTimeJumpedNotification: String ``` |

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

|  | Declaration |
| --- | --- |
| From | ``` let AVSampleRateConverterAlgorithmKey: NSString! ``` |
| To | ``` let AVSampleRateConverterAlgorithmKey: String ``` |

Modified AVSampleRateConverterAlgorithm_Mastering

|  | Declaration |
| --- | --- |
| From | ``` let AVSampleRateConverterAlgorithm_Mastering: NSString! ``` |
| To | ``` let AVSampleRateConverterAlgorithm_Mastering: String ``` |

Modified AVSampleRateConverterAlgorithm_Normal

|  | Declaration |
| --- | --- |
| From | ``` let AVSampleRateConverterAlgorithm_Normal: NSString! ``` |
| To | ``` let AVSampleRateConverterAlgorithm_Normal: String ``` |

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

|  | Declaration |
| --- | --- |
| From | ``` let AVTrackAssociationTypeAudioFallback: NSString! ``` |
| To | ``` let AVTrackAssociationTypeAudioFallback: String ``` |

Modified AVTrackAssociationTypeChapterList

|  | Declaration |
| --- | --- |
| From | ``` let AVTrackAssociationTypeChapterList: NSString! ``` |
| To | ``` let AVTrackAssociationTypeChapterList: String ``` |

Modified AVTrackAssociationTypeForcedSubtitlesOnly

|  | Declaration |
| --- | --- |
| From | ``` let AVTrackAssociationTypeForcedSubtitlesOnly: NSString! ``` |
| To | ``` let AVTrackAssociationTypeForcedSubtitlesOnly: String ``` |

Modified AVTrackAssociationTypeMetadataReferent

|  | Declaration |
| --- | --- |
| From | ``` let AVTrackAssociationTypeMetadataReferent: NSString! ``` |
| To | ``` let AVTrackAssociationTypeMetadataReferent: String ``` |

Modified AVTrackAssociationTypeSelectionFollower

|  | Declaration |
| --- | --- |
| From | ``` let AVTrackAssociationTypeSelectionFollower: NSString! ``` |
| To | ``` let AVTrackAssociationTypeSelectionFollower: String ``` |

Modified AVTrackAssociationTypeTimecode

|  | Declaration |
| --- | --- |
| From | ``` let AVTrackAssociationTypeTimecode: NSString! ``` |
| To | ``` let AVTrackAssociationTypeTimecode: String ``` |

Modified AVURLAssetHTTPCookiesKey

|  | Declaration |
| --- | --- |
| From | ``` let AVURLAssetHTTPCookiesKey: NSString! ``` |
| To | ``` let AVURLAssetHTTPCookiesKey: String ``` |

Modified AVURLAssetPreferPreciseDurationAndTimingKey

|  | Declaration |
| --- | --- |
| From | ``` let AVURLAssetPreferPreciseDurationAndTimingKey: NSString! ``` |
| To | ``` let AVURLAssetPreferPreciseDurationAndTimingKey: String ``` |

Modified AVURLAssetReferenceRestrictionsKey

|  | Declaration |
| --- | --- |
| From | ``` let AVURLAssetReferenceRestrictionsKey: NSString! ``` |
| To | ``` let AVURLAssetReferenceRestrictionsKey: String ``` |

Modified AVVideoAllowFrameReorderingKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoAllowFrameReorderingKey: NSString! ``` |
| To | ``` let AVVideoAllowFrameReorderingKey: String ``` |

Modified AVVideoAverageBitRateKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoAverageBitRateKey: NSString! ``` |
| To | ``` let AVVideoAverageBitRateKey: String ``` |

Modified AVVideoAverageNonDroppableFrameRateKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoAverageNonDroppableFrameRateKey: NSString! ``` |
| To | ``` let AVVideoAverageNonDroppableFrameRateKey: String ``` |

Modified AVVideoCleanApertureHeightKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoCleanApertureHeightKey: NSString! ``` |
| To | ``` let AVVideoCleanApertureHeightKey: String ``` |

Modified AVVideoCleanApertureHorizontalOffsetKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoCleanApertureHorizontalOffsetKey: NSString! ``` |
| To | ``` let AVVideoCleanApertureHorizontalOffsetKey: String ``` |

Modified AVVideoCleanApertureKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoCleanApertureKey: NSString! ``` |
| To | ``` let AVVideoCleanApertureKey: String ``` |

Modified AVVideoCleanApertureVerticalOffsetKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoCleanApertureVerticalOffsetKey: NSString! ``` |
| To | ``` let AVVideoCleanApertureVerticalOffsetKey: String ``` |

Modified AVVideoCleanApertureWidthKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoCleanApertureWidthKey: NSString! ``` |
| To | ``` let AVVideoCleanApertureWidthKey: String ``` |

Modified AVVideoCodecH264

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoCodecH264: NSString! ``` |
| To | ``` let AVVideoCodecH264: String ``` |

Modified AVVideoCodecJPEG

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoCodecJPEG: NSString! ``` |
| To | ``` let AVVideoCodecJPEG: String ``` |

Modified AVVideoCodecKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoCodecKey: NSString! ``` |
| To | ``` let AVVideoCodecKey: String ``` |

Modified AVVideoCompressionPropertiesKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoCompressionPropertiesKey: NSString! ``` |
| To | ``` let AVVideoCompressionPropertiesKey: String ``` |

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

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoHeightKey: NSString! ``` |
| To | ``` let AVVideoHeightKey: String ``` |

Modified AVVideoMaxKeyFrameIntervalDurationKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoMaxKeyFrameIntervalDurationKey: NSString! ``` |
| To | ``` let AVVideoMaxKeyFrameIntervalDurationKey: String ``` |

Modified AVVideoMaxKeyFrameIntervalKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoMaxKeyFrameIntervalKey: NSString! ``` |
| To | ``` let AVVideoMaxKeyFrameIntervalKey: String ``` |

Modified AVVideoPixelAspectRatioHorizontalSpacingKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoPixelAspectRatioHorizontalSpacingKey: NSString! ``` |
| To | ``` let AVVideoPixelAspectRatioHorizontalSpacingKey: String ``` |

Modified AVVideoPixelAspectRatioKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoPixelAspectRatioKey: NSString! ``` |
| To | ``` let AVVideoPixelAspectRatioKey: String ``` |

Modified AVVideoPixelAspectRatioVerticalSpacingKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoPixelAspectRatioVerticalSpacingKey: NSString! ``` |
| To | ``` let AVVideoPixelAspectRatioVerticalSpacingKey: String ``` |

Modified AVVideoProfileLevelH264Baseline30

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoProfileLevelH264Baseline30: NSString! ``` |
| To | ``` let AVVideoProfileLevelH264Baseline30: String ``` |

Modified AVVideoProfileLevelH264Baseline31

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoProfileLevelH264Baseline31: NSString! ``` |
| To | ``` let AVVideoProfileLevelH264Baseline31: String ``` |

Modified AVVideoProfileLevelH264Baseline41

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoProfileLevelH264Baseline41: NSString! ``` |
| To | ``` let AVVideoProfileLevelH264Baseline41: String ``` |

Modified AVVideoProfileLevelH264BaselineAutoLevel

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoProfileLevelH264BaselineAutoLevel: NSString! ``` |
| To | ``` let AVVideoProfileLevelH264BaselineAutoLevel: String ``` |

Modified AVVideoProfileLevelH264High40

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoProfileLevelH264High40: NSString! ``` |
| To | ``` let AVVideoProfileLevelH264High40: String ``` |

Modified AVVideoProfileLevelH264High41

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoProfileLevelH264High41: NSString! ``` |
| To | ``` let AVVideoProfileLevelH264High41: String ``` |

Modified AVVideoProfileLevelH264HighAutoLevel

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoProfileLevelH264HighAutoLevel: NSString! ``` |
| To | ``` let AVVideoProfileLevelH264HighAutoLevel: String ``` |

Modified AVVideoProfileLevelH264Main30

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoProfileLevelH264Main30: NSString! ``` |
| To | ``` let AVVideoProfileLevelH264Main30: String ``` |

Modified AVVideoProfileLevelH264Main31

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoProfileLevelH264Main31: NSString! ``` |
| To | ``` let AVVideoProfileLevelH264Main31: String ``` |

Modified AVVideoProfileLevelH264Main32

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoProfileLevelH264Main32: NSString! ``` |
| To | ``` let AVVideoProfileLevelH264Main32: String ``` |

Modified AVVideoProfileLevelH264Main41

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoProfileLevelH264Main41: NSString! ``` |
| To | ``` let AVVideoProfileLevelH264Main41: String ``` |

Modified AVVideoProfileLevelH264MainAutoLevel

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoProfileLevelH264MainAutoLevel: NSString! ``` |
| To | ``` let AVVideoProfileLevelH264MainAutoLevel: String ``` |

Modified AVVideoProfileLevelKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoProfileLevelKey: NSString! ``` |
| To | ``` let AVVideoProfileLevelKey: String ``` |

Modified AVVideoQualityKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoQualityKey: NSString! ``` |
| To | ``` let AVVideoQualityKey: String ``` |

Modified AVVideoScalingModeFit

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoScalingModeFit: NSString! ``` |
| To | ``` let AVVideoScalingModeFit: String ``` |

Modified AVVideoScalingModeKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoScalingModeKey: NSString! ``` |
| To | ``` let AVVideoScalingModeKey: String ``` |

Modified AVVideoScalingModeResize

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoScalingModeResize: NSString! ``` |
| To | ``` let AVVideoScalingModeResize: String ``` |

Modified AVVideoScalingModeResizeAspect

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoScalingModeResizeAspect: NSString! ``` |
| To | ``` let AVVideoScalingModeResizeAspect: String ``` |

Modified AVVideoScalingModeResizeAspectFill

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoScalingModeResizeAspectFill: NSString! ``` |
| To | ``` let AVVideoScalingModeResizeAspectFill: String ``` |

Modified AVVideoWidthKey

|  | Declaration |
| --- | --- |
| From | ``` let AVVideoWidthKey: NSString! ``` |
| To | ``` let AVVideoWidthKey: String ``` |

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
