---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Swift/AVFoundation.html
archived_at: '2026-07-18T02:57:28.883247Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# AVFoundation Changes for Swift

### AVFoundation

Removed [AVAssetDownloadDelegate](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate)Removed [AVAssetDownloadDelegate.URLSession(_: NSURLSession, assetDownloadTask: AVAssetDownloadTask, didLoadTimeRange: CMTimeRange, totalTimeRangesLoaded: [NSValue], timeRangeExpectedToLoad: CMTimeRange)](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/1621019-urlsession)Removed [AVAssetDownloadDelegate.URLSession(_: NSURLSession, assetDownloadTask: AVAssetDownloadTask, didResolveMediaSelection: AVMediaSelection)](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/1621023-urlsession)Removed [AVAssetDownloadTask](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask)Removed [AVAssetDownloadTask.destinationURL](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask/1621022-destinationurl)Removed [AVAssetDownloadTask.loadedTimeRanges](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask/1621026-loadedtimeranges)Removed [AVAssetDownloadTask.options](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask/1621014-options)Removed [AVAssetDownloadTask.urlAsset](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask/1621024-urlasset)Removed [AVAssetDownloadURLSession](https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession)Removed [AVAssetDownloadURLSession.init(configuration: NSURLSessionConfiguration, assetDownloadDelegate: AVAssetDownloadDelegate?, delegateQueue: NSOperationQueue?)](https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession/1621015-sessionwithconfiguration)Removed [AVAssetDownloadURLSession.assetDownloadTaskWithURLAsset(_: AVURLAsset, destinationURL: NSURL, options: [String : AnyObject]?) -> AVAssetDownloadTask?](https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession/1621018-assetdownloadtaskwithurlasset)Removed [AVAssetReferenceRestrictions.ForbidNone](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/avassetreferencerestrictionforbidnone)Removed [AVAudioInputNode](https://developer.apple.com/documentation/avfoundation/avaudioinputnode)Removed [AVMusicSequenceLoadOptions.SMF_PreserveTracks](https://developer.apple.com/documentation/avfoundation/avmusicsequenceloadoptions/avmusicsequenceloadsmf_preservetracks)Added [AVAssetCache](https://developer.apple.com/documentation/avfoundation/avassetcache)Added [AVAssetCache.isPlayableOffline](https://developer.apple.com/documentation/avfoundation/avassetcache/1823708-playableoffline)Added [AVAssetCache.mediaSelectionOptions(in: AVMediaSelectionGroup) -> [AVMediaSelectionOption]](https://developer.apple.com/documentation/avfoundation/avassetcache/1823715-mediaselectionoptions)Added [AVAssetWriter.init(url: URL, fileType: String) throws](https://developer.apple.com/documentation/avfoundation/avassetwriter/1426663-init)Added [AVAudioEnvironmentNode.init()](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1643654-init)Added [AVAudioFormat.magicCookie](https://developer.apple.com/documentation/avfoundation/avaudioformat/1639892-magiccookie)Added [AVAudioMixerNode.init()](https://developer.apple.com/documentation/avfoundation/avaudiomixernode/1643644-init)Added [AVAudioPlayer.format](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1778427-format)Added [AVAudioPlayer.setVolume(_: Float, fadeDuration: TimeInterval)](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1643591-setvolume)Added [AVAudioPlayerNode.init()](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1643624-init)Added [AVAudioSession.setCategory(_: String, mode: String, options: AVAudioSessionCategoryOptions) throws](https://developer.apple.com/documentation/avfoundation/avaudiosession/1771734-setcategory)Added [AVAudioSessionCategoryOptions.allowAirPlay](https://developer.apple.com/documentation/avfoundation/avaudiosession/categoryoptions/1771736-allowairplay)Added [AVAudioSessionCategoryOptions.allowBluetoothA2DP](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryoptions/avaudiosessioncategoryoptionallowbluetootha2dp)Added [AVAudioSessionPortDescription.hasHardwareVoiceCallProcessing](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1778338-hashardwarevoicecallprocessing)Added [AVCaptureDevice.activeColorSpace](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1648668-activecolorspace)Added [AVCaptureDevice.isLockingFocusWithCustomLensPositionSupported](https://developer.apple.com/documentation/avfoundation/avcapturedevice/2361529-lockingfocuswithcustomlenspositi)Added [AVCaptureDevice.isLockingWhiteBalanceWithCustomDeviceGainsSupported](https://developer.apple.com/documentation/avfoundation/avcapturedevice/2360576-lockingwhitebalancewithcustomdev)Added [AVError [struct]](https://developer.apple.com/documentation/avfoundation/averror)Added [AVError.airPlayControllerRequiresInternet](https://developer.apple.com/documentation/avfoundation/averror/2330554-airplaycontrollerrequiresinterne)Added [AVError.airPlayReceiverRequiresInternet](https://developer.apple.com/documentation/avfoundation/averror/2330568-airplayreceiverrequiresinternet)Added [AVError.applicationIsNotAuthorized](https://developer.apple.com/documentation/avfoundation/averror/2330550-applicationisnotauthorized)Added [AVError.applicationIsNotAuthorizedToUseDevice](https://developer.apple.com/documentation/avfoundation/averror/2330562-applicationisnotauthorizedtoused)Added [AVError.compositionTrackSegmentsNotContiguous](https://developer.apple.com/documentation/avfoundation/averror/2330587-compositiontracksegmentsnotconti)Added [AVError.contentIsNotAuthorized](https://developer.apple.com/documentation/avfoundation/averror/2330560-contentisnotauthorized)Added [AVError.contentIsProtected](https://developer.apple.com/documentation/avfoundation/averror/2330586-contentisprotected)Added [AVError.decodeFailed](https://developer.apple.com/documentation/avfoundation/averror/2330573-decodefailed)Added [AVError.decoderNotFound](https://developer.apple.com/documentation/avfoundation/averror/2330578-decodernotfound)Added [AVError.decoderTemporarilyUnavailable](https://developer.apple.com/documentation/avfoundation/averror/2330592-decodertemporarilyunavailable)Added AVError.deviceAdded [AVError.deviceAlreadyUsedByAnotherSession](https://developer.apple.com/documentation/avfoundation/averror/2330565-devicealreadyusedbyanothersessio)Added [AVError.deviceInUseByAnotherApplication](https://developer.apple.com/documentation/avfoundation/averror/2330548-deviceinusebyanotherapplication)Added [AVError.deviceIsNotAvailableInBackground](https://developer.apple.com/documentation/avfoundation/averror/2335072-deviceisnotavailableinbackground)Added [AVError.deviceLockedForConfigurationByAnotherProcess](https://developer.apple.com/documentation/avfoundation/averror/2330552-devicelockedforconfigurationbyan)Added [AVError.deviceNotConnected](https://developer.apple.com/documentation/avfoundation/averror/2330583-devicenotconnected)Added [AVError.deviceWasDisconnected](https://developer.apple.com/documentation/avfoundation/averror/2330589-devicewasdisconnected)Added [AVError.diskFull](https://developer.apple.com/documentation/avfoundation/averror/2330572-diskfull)Added [AVError.displayWasDisabled](https://developer.apple.com/documentation/avfoundation/averror/2330563-displaywasdisabled)Added [AVError.encoderNotFound](https://developer.apple.com/documentation/avfoundation/averror/2330553-encodernotfound)Added [AVError.encoderTemporarilyUnavailable](https://developer.apple.com/documentation/avfoundation/averror/2330546-encodertemporarilyunavailable)Added [AVError.exportFailed](https://developer.apple.com/documentation/avfoundation/averror/2330545-exportfailed)Added [AVError.failedToLoadMediaData](https://developer.apple.com/documentation/avfoundation/averror/2330561-failedtoloadmediadata)Added [AVError.failedToParse](https://developer.apple.com/documentation/avfoundation/averror/2330564-failedtoparse)Added [AVError.fileAlreadyExists](https://developer.apple.com/documentation/avfoundation/averror/2330594-filealreadyexists)Added [AVError.fileFailedToParse](https://developer.apple.com/documentation/avfoundation/averror/2330585-filefailedtoparse)Added [AVError.fileFormatNotRecognized](https://developer.apple.com/documentation/avfoundation/averror/2330593-fileformatnotrecognized)Added [AVError.fileSize](https://developer.apple.com/documentation/avfoundation/averror/2305304-filesize)Added [AVError.fileTypeDoesNotSupportSampleReferences](https://developer.apple.com/documentation/avfoundation/averror/2330571-filetypedoesnotsupportsamplerefe)Added [AVError.incompatibleAsset](https://developer.apple.com/documentation/avfoundation/averror/2330580-incompatibleasset)Added AVError.init(_nsError: NSError)Added [AVError.invalidCompositionTrackSegmentDuration](https://developer.apple.com/documentation/avfoundation/averror/2330556-invalidcompositiontracksegmentdu)Added [AVError.invalidCompositionTrackSegmentSourceDuration](https://developer.apple.com/documentation/avfoundation/averror/2330551-invalidcompositiontracksegmentso)Added [AVError.invalidCompositionTrackSegmentSourceStartTime](https://developer.apple.com/documentation/avfoundation/averror/2330559-invalidcompositiontracksegmentso)Added [AVError.invalidOutputURLPathExtension](https://developer.apple.com/documentation/avfoundation/averror/2330566-invalidoutputurlpathextension)Added [AVError.invalidSourceMedia](https://developer.apple.com/documentation/avfoundation/averror/2330588-invalidsourcemedia)Added [AVError.invalidVideoComposition](https://developer.apple.com/documentation/avfoundation/averror/2330581-invalidvideocomposition)Added [AVError.maximumDurationReached](https://developer.apple.com/documentation/avfoundation/averror/2330569-maximumdurationreached)Added [AVError.maximumFileSizeReached](https://developer.apple.com/documentation/avfoundation/averror/2330575-maximumfilesizereached)Added [AVError.maximumNumberOfSamplesForFileFormatReached](https://developer.apple.com/documentation/avfoundation/averror/2330590-maximumnumberofsamplesforfilefor)Added [AVError.maximumStillImageCaptureRequestsExceeded](https://developer.apple.com/documentation/avfoundation/averror/2330598-maximumstillimagecapturerequests)Added [AVError.mediaChanged](https://developer.apple.com/documentation/avfoundation/averror/2330591-mediachanged)Added [AVError.mediaDiscontinuity](https://developer.apple.com/documentation/avfoundation/averror/2330584-mediadiscontinuity)Added [AVError.mediaServicesWereReset](https://developer.apple.com/documentation/avfoundation/averror/2335075-mediaserviceswerereset)Added [AVError.mediaSubtypes](https://developer.apple.com/documentation/avfoundation/averror/2305285-mediasubtypes)Added AVError.mediaTypeAdded [AVError.noDataCaptured](https://developer.apple.com/documentation/avfoundation/averror/2330555-nodatacaptured)Added [AVError.noImageAtTime](https://developer.apple.com/documentation/avfoundation/averror/2330579-noimageattime)Added [AVError.operationInterrupted](https://developer.apple.com/documentation/avfoundation/averror/2335071-operationinterrupted)Added [AVError.operationNotAllowed](https://developer.apple.com/documentation/avfoundation/averror/2330576-operationnotallowed)Added [AVError.operationNotSupportedForAsset](https://developer.apple.com/documentation/avfoundation/averror/2330557-operationnotsupportedforasset)Added [AVError.outOfMemory](https://developer.apple.com/documentation/avfoundation/averror/2330595-outofmemory)Added [AVError.processID](https://developer.apple.com/documentation/avfoundation/averror/2305278-processid)Added [AVError.recordingAlreadyInProgress](https://developer.apple.com/documentation/avfoundation/averror/2335073-recordingalreadyinprogress)Added [AVError.recordingSuccessfullyFinished](https://developer.apple.com/documentation/avfoundation/averror/2305300-recordingsuccessfullyfinished)Added [AVError.referenceForbiddenByReferencePolicy](https://developer.apple.com/documentation/avfoundation/averror/2330567-referenceforbiddenbyreferencepol)Added [AVError.screenCaptureFailed](https://developer.apple.com/documentation/avfoundation/averror/2330549-screencapturefailed)Added [AVError.serverIncorrectlyConfigured](https://developer.apple.com/documentation/avfoundation/averror/2330596-serverincorrectlyconfigured)Added [AVError.sessionConfigurationChanged](https://developer.apple.com/documentation/avfoundation/averror/2330558-sessionconfigurationchanged)Added [AVError.sessionNotRunning](https://developer.apple.com/documentation/avfoundation/averror/2330597-sessionnotrunning)Added [AVError.sessionWasInterrupted](https://developer.apple.com/documentation/avfoundation/averror/2335074-sessionwasinterrupted)Added [AVError.time](https://developer.apple.com/documentation/avfoundation/averror/2305264-time)Added [AVError.torchLevelUnavailable](https://developer.apple.com/documentation/avfoundation/averror/2330582-torchlevelunavailable)Added [AVError.undecodableMediaData](https://developer.apple.com/documentation/avfoundation/averror/2330599-undecodablemediadata)Added [AVError.unknown](https://developer.apple.com/documentation/avfoundation/averror/2330574-unknown)Added [AVError.unsupportedOutputSettings](https://developer.apple.com/documentation/avfoundation/averror/2330570-unsupportedoutputsettings)Added [AVError.videoCompositorFailed](https://developer.apple.com/documentation/avfoundation/averror/2330577-videocompositorfailed)Added [AVError.Code.operationNotAllowed](https://developer.apple.com/documentation/avfoundation/averror/averroroperationnotallowed)Added [AVError.Code.unsupportedOutputSettings](https://developer.apple.com/documentation/avfoundation/averror/code/unsupportedoutputsettings)Added [AVMutableVideoComposition.colorPrimaries](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1643234-colorprimaries)Added [AVMutableVideoComposition.colorTransferFunction](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1643237-colortransferfunction)Added [AVMutableVideoComposition.colorYCbCrMatrix](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1643231-colorycbcrmatrix)Added [AVPlayer.automaticallyWaitsToMinimizeStalling](https://developer.apple.com/documentation/avfoundation/avplayer/1643482-automaticallywaitstominimizestal)Added [AVPlayer.playImmediately(atRate: Float)](https://developer.apple.com/documentation/avfoundation/avplayer/1643480-playimmediatelyatrate)Added [AVPlayer.reasonForWaitingToPlay](https://developer.apple.com/documentation/avfoundation/avplayer/1643486-reasonforwaitingtoplay)Added [AVPlayer.timeControlStatus](https://developer.apple.com/documentation/avfoundation/avplayer/1643485-timecontrolstatus)Added [AVPlayerItem.preferredForwardBufferDuration](https://developer.apple.com/documentation/avfoundation/avplayeritem/1643630-preferredforwardbufferduration)Added [AVPlayerItemAccessLogEvent.averageAudioBitrate](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1643590-averageaudiobitrate)Added [AVPlayerItemAccessLogEvent.averageVideoBitrate](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1643592-averagevideobitrate)Added [AVPlayerItemAccessLogEvent.indicatedAverageBitrate](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1872546-indicatedaveragebitrate)Added [AVPlayerItemVideoOutput.init(outputSettings: [String : Any]?)](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1643270-init)Added [AVPlayerLooper](https://developer.apple.com/documentation/avfoundation/avplayerlooper)Added [AVPlayerLooper.disableLooping()](https://developer.apple.com/documentation/avfoundation/avplayerlooper/1643629-disablelooping)Added [AVPlayerLooper.error](https://developer.apple.com/documentation/avfoundation/avplayerlooper/2177064-error)Added [AVPlayerLooper.init(player: AVQueuePlayer, templateItem: AVPlayerItem)](https://developer.apple.com/documentation/avfoundation/avplayerlooper/1643625-init)Added [AVPlayerLooper.init(player: AVQueuePlayer, templateItem: AVPlayerItem, timeRange: CMTimeRange)](https://developer.apple.com/documentation/avfoundation/avplayerlooper/1643626-initwithplayer)Added [AVPlayerLooper.loopCount](https://developer.apple.com/documentation/avfoundation/avplayerlooper/1643648-loopcount)Added [AVPlayerLooper.loopingPlayerItems](https://developer.apple.com/documentation/avfoundation/avplayerlooper/1643631-loopingplayeritems)Added [AVPlayerLooper.status](https://developer.apple.com/documentation/avfoundation/avplayerlooper/2177060-status)Added [AVPlayerLooperStatus [enum]](https://developer.apple.com/documentation/avfoundation/avplayerlooper/status)Added [AVPlayerLooperStatus.cancelled](https://developer.apple.com/documentation/avfoundation/avplayerlooperstatus/avplayerlooperstatuscancelled)Added [AVPlayerLooperStatus.failed](https://developer.apple.com/documentation/avfoundation/avplayerlooper/status/failed)Added [AVPlayerLooperStatus.ready](https://developer.apple.com/documentation/avfoundation/avplayerlooper/status/ready)Added [AVPlayerLooperStatus.unknown](https://developer.apple.com/documentation/avfoundation/avplayerlooperstatus/avplayerlooperstatusunknown)Added [AVPlayerTimeControlStatus [enum]](https://developer.apple.com/documentation/avfoundation/avplayertimecontrolstatus)Added [AVPlayerTimeControlStatus.paused](https://developer.apple.com/documentation/avfoundation/avplayertimecontrolstatus/avplayertimecontrolstatuspaused)Added [AVPlayerTimeControlStatus.playing](https://developer.apple.com/documentation/avfoundation/avplayer/timecontrolstatus/playing)Added [AVPlayerTimeControlStatus.waitingToPlayAtSpecifiedRate](https://developer.apple.com/documentation/avfoundation/avplayer/timecontrolstatus/waitingtoplayatspecifiedrate)Added [AVSpeechSynthesizer.outputChannels](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1648692-outputchannels)Added [AVSpeechUtterance.attributedSpeechString](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1648723-attributedspeechstring)Added [AVSpeechUtterance.init(attributedString: NSAttributedString)](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1648776-init)Added [AVURLAsset.assetCache](https://developer.apple.com/documentation/avfoundation/avurlasset/1823714-assetcache)Added [AVVideoCompositing.supportsWideColorSourceFrames](https://developer.apple.com/documentation/avfoundation/avvideocompositing/1643657-supportswidecolorsourceframes)Added [AVVideoComposition.colorPrimaries](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1643235-colorprimaries)Added [AVVideoComposition.colorTransferFunction](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1643230-colortransferfunction)Added [AVVideoComposition.colorYCbCrMatrix](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1643236-colorycbcrmatrix)Added AVAUDIOENGINE_HAVE_MUSICPLAYERAdded AVAUDIOFORMAT_HAVE_CMFORMATDESCRIPTIONAdded AVAUDIOIONODE_HAVE_AUDIOUNITAdded AVAUDIOUNIT_HAVE_AUDIOUNITAdded AVAUDIOUNITCOMPONENT_HAVE_AUDIOCOMPONENTAdded [AVMediaCharacteristicUsesWideGamutColorSpace](https://developer.apple.com/documentation/avfoundation/avmediacharacteristicuseswidegamutcolorspace)Added [AVMetadataIdentifierISOUserDataDate](https://developer.apple.com/documentation/avfoundation/avmetadataidentifier/1642209-isouserdatadate)Added [AVMetadataISOUserDataKeyDate](https://developer.apple.com/documentation/avfoundation/avmetadatakey/1643642-isouserdatakeydate)Added [AVPlayerWaitingToMinimizeStallsReason](https://developer.apple.com/documentation/avfoundation/avplayerwaitingtominimizestallsreason)Added [AVPlayerWaitingWhileEvaluatingBufferingRateReason](https://developer.apple.com/documentation/avfoundation/avplayerwaitingwhileevaluatingbufferingratereason)Added [AVPlayerWaitingWithNoItemToPlayReason](https://developer.apple.com/documentation/avfoundation/avplayerwaitingwithnoitemtoplayreason)Added [AVSampleRateConverterAlgorithm_MinimumPhase](https://developer.apple.com/documentation/avfoundation/avsamplerateconverteralgorithm_minimumphase)Added [AVSpeechSynthesisIPANotationAttribute](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisipanotationattribute)Added [AVURLAssetAllowsCellularAccessKey](https://developer.apple.com/documentation/avfoundation/avurlassetallowscellularaccesskey)Added [AVVideoAllowWideColorKey](https://developer.apple.com/documentation/avfoundation/avvideoallowwidecolorkey)Added [AVVideoColorPrimaries_ITU_R_709_2](https://developer.apple.com/documentation/avfoundation/avvideocolorprimaries_itu_r_709_2)Added [AVVideoColorPrimaries_P3_D65](https://developer.apple.com/documentation/avfoundation/avvideocolorprimaries_p3_d65)Added [AVVideoColorPrimaries_SMPTE_C](https://developer.apple.com/documentation/avfoundation/avvideocolorprimaries_smpte_c)Added [AVVideoColorPrimariesKey](https://developer.apple.com/documentation/avfoundation/avvideocolorprimarieskey)Added [AVVideoColorPropertiesKey](https://developer.apple.com/documentation/avfoundation/avvideocolorpropertieskey)Added [AVVideoTransferFunction_ITU_R_709_2](https://developer.apple.com/documentation/avfoundation/avvideotransferfunction_itu_r_709_2)Added [AVVideoTransferFunctionKey](https://developer.apple.com/documentation/avfoundation/avvideotransferfunctionkey)Added [AVVideoYCbCrMatrix_ITU_R_601_4](https://developer.apple.com/documentation/avfoundation/avvideoycbcrmatrix_itu_r_601_4)Added [AVVideoYCbCrMatrix_ITU_R_709_2](https://developer.apple.com/documentation/avfoundation/avvideoycbcrmatrix_itu_r_709_2)Added [AVVideoYCbCrMatrixKey](https://developer.apple.com/documentation/avfoundation/avvideoycbcrmatrixkey)Modified [AVAsset](https://developer.apple.com/documentation/avfoundation/avasset)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAsset : NSObject, NSCopying, AVAsynchronousKeyValueLoading {     convenience init(URL URL: NSURL)     class func assetWithURL(_ URL: NSURL) -> Self     var duration: CMTime { get }     var preferredRate: Float { get }     var preferredVolume: Float { get }     var preferredTransform: CGAffineTransform { get }     var naturalSize: CGSize { get } } extension AVAsset {     var providesPreciseDurationAndTiming: Bool { get }     func cancelLoading() } extension AVAsset {     var referenceRestrictions: AVAssetReferenceRestrictions { get } } extension AVAsset {     var tracks: [AVAssetTrack] { get }     func trackWithTrackID(_ trackID: CMPersistentTrackID) -> AVAssetTrack?     func tracksWithMediaType(_ mediaType: String) -> [AVAssetTrack]     func tracksWithMediaCharacteristic(_ mediaCharacteristic: String) -> [AVAssetTrack]     var trackGroups: [AVAssetTrackGroup] { get } } extension AVAsset {     var creationDate: AVMetadataItem? { get }     var lyrics: String? { get }     var commonMetadata: [AVMetadataItem] { get }     var metadata: [AVMetadataItem] { get }     var availableMetadataFormats: [String] { get }     func metadataForFormat(_ format: String) -> [AVMetadataItem] } extension AVAsset {     var availableChapterLocales: [NSLocale] { get }     func chapterMetadataGroupsWithTitleLocale(_ locale: NSLocale, containingItemsWithCommonKeys commonKeys: [String]?) -> [AVTimedMetadataGroup]     func chapterMetadataGroupsBestMatchingPreferredLanguages(_ preferredLanguages: [String]) -> [AVTimedMetadataGroup] } extension AVAsset {     var availableMediaCharacteristicsWithMediaSelectionOptions: [String] { get }     func mediaSelectionGroupForMediaCharacteristic(_ mediaCharacteristic: String) -> AVMediaSelectionGroup?     var preferredMediaSelection: AVMediaSelection { get } } extension AVAsset {     var hasProtectedContent: Bool { get } } extension AVAsset {     var canContainFragments: Bool { get }     var containsFragments: Bool { get } } extension AVAsset {     var playable: Bool { get }     var exportable: Bool { get }     var readable: Bool { get }     var composable: Bool { get }     var compatibleWithSavedPhotosAlbum: Bool { get }     var compatibleWithAirPlayVideo: Bool { get } } extension AVAsset {     func unusedTrackID() -> CMPersistentTrackID } ``` | AVAsynchronousKeyValueLoading, NSCopying |
| To | ``` class AVAsset : NSObject, NSCopying, AVAsynchronousKeyValueLoading {     convenience init(url URL: URL)     class func withURL(_ URL: URL) -> Self     var duration: CMTime { get }     var preferredRate: Float { get }     var preferredVolume: Float { get }     var preferredTransform: CGAffineTransform { get }     var naturalSize: CGSize { get }     func unusedTrackID() -> CMPersistentTrackID     var isPlayable: Bool { get }     var isExportable: Bool { get }     var isReadable: Bool { get }     var isComposable: Bool { get }     var isCompatibleWithSavedPhotosAlbum: Bool { get }     var isCompatibleWithAirPlayVideo: Bool { get }     var canContainFragments: Bool { get }     var containsFragments: Bool { get }     var hasProtectedContent: Bool { get }     var availableMediaCharacteristicsWithMediaSelectionOptions: [String] { get }     func mediaSelectionGroup(forMediaCharacteristic mediaCharacteristic: String) -> AVMediaSelectionGroup?     var preferredMediaSelection: AVMediaSelection { get }     var availableChapterLocales: [Locale] { get }     func chapterMetadataGroups(withTitleLocale locale: Locale, containingItemsWithCommonKeys commonKeys: [String]?) -> [AVTimedMetadataGroup]     func chapterMetadataGroups(bestMatchingPreferredLanguages preferredLanguages: [String]) -> [AVTimedMetadataGroup]     var creationDate: AVMetadataItem? { get }     var lyrics: String? { get }     var commonMetadata: [AVMetadataItem] { get }     var metadata: [AVMetadataItem] { get }     var availableMetadataFormats: [String] { get }     func metadata(forFormat format: String) -> [AVMetadataItem]     var tracks: [AVAssetTrack] { get }     func track(withTrackID trackID: CMPersistentTrackID) -> AVAssetTrack?     func tracks(withMediaType mediaType: String) -> [AVAssetTrack]     func tracks(withMediaCharacteristic mediaCharacteristic: String) -> [AVAssetTrack]     var trackGroups: [AVAssetTrackGroup] { get }     var referenceRestrictions: AVAssetReferenceRestrictions { get }     var providesPreciseDurationAndTiming: Bool { get }     func cancelLoading()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAsset : CVarArg { } extension AVAsset : Equatable, Hashable {     var hashValue: Int { get } } extension AVAsset {     var providesPreciseDurationAndTiming: Bool { get }     func cancelLoading() } extension AVAsset {     var referenceRestrictions: AVAssetReferenceRestrictions { get } } extension AVAsset {     var tracks: [AVAssetTrack] { get }     func track(withTrackID trackID: CMPersistentTrackID) -> AVAssetTrack?     func tracks(withMediaType mediaType: String) -> [AVAssetTrack]     func tracks(withMediaCharacteristic mediaCharacteristic: String) -> [AVAssetTrack]     var trackGroups: [AVAssetTrackGroup] { get } } extension AVAsset {     var creationDate: AVMetadataItem? { get }     var lyrics: String? { get }     var commonMetadata: [AVMetadataItem] { get }     var metadata: [AVMetadataItem] { get }     var availableMetadataFormats: [String] { get }     func metadata(forFormat format: String) -> [AVMetadataItem] } extension AVAsset {     var availableChapterLocales: [Locale] { get }     func chapterMetadataGroups(withTitleLocale locale: Locale, containingItemsWithCommonKeys commonKeys: [String]?) -> [AVTimedMetadataGroup]     func chapterMetadataGroups(bestMatchingPreferredLanguages preferredLanguages: [String]) -> [AVTimedMetadataGroup] } extension AVAsset {     var availableMediaCharacteristicsWithMediaSelectionOptions: [String] { get }     func mediaSelectionGroup(forMediaCharacteristic mediaCharacteristic: String) -> AVMediaSelectionGroup?     var preferredMediaSelection: AVMediaSelection { get } } extension AVAsset {     var hasProtectedContent: Bool { get } } extension AVAsset {     var canContainFragments: Bool { get }     var containsFragments: Bool { get } } extension AVAsset {     var isPlayable: Bool { get }     var isExportable: Bool { get }     var isReadable: Bool { get }     var isComposable: Bool { get }     var isCompatibleWithSavedPhotosAlbum: Bool { get }     var isCompatibleWithAirPlayVideo: Bool { get } } extension AVAsset {     func unusedTrackID() -> CMPersistentTrackID } ``` | AVAsynchronousKeyValueLoading, CVarArg, Equatable, Hashable, NSCopying |

Modified [AVAsset.availableChapterLocales](https://developer.apple.com/documentation/avfoundation/avasset/1388228-availablechapterlocales)

|  | Declaration |
| --- | --- |
| From | ``` var availableChapterLocales: [NSLocale] { get } ``` |
| To | ``` var availableChapterLocales: [Locale] { get } ``` |

Modified [AVAsset.chapterMetadataGroups(bestMatchingPreferredLanguages: [String]) -> [AVTimedMetadataGroup]](https://developer.apple.com/documentation/avfoundation/avasset/1390909-chaptermetadatagroupsbestmatchin)

|  | Declaration |
| --- | --- |
| From | ``` func chapterMetadataGroupsBestMatchingPreferredLanguages(_ preferredLanguages: [String]) -> [AVTimedMetadataGroup] ``` |
| To | ``` func chapterMetadataGroups(bestMatchingPreferredLanguages preferredLanguages: [String]) -> [AVTimedMetadataGroup] ``` |

Modified [AVAsset.chapterMetadataGroups(withTitleLocale: Locale, containingItemsWithCommonKeys: [String]?) -> [AVTimedMetadataGroup]](https://developer.apple.com/documentation/avfoundation/avasset/1388966-chaptermetadatagroupswithtitlelo)

|  | Declaration |
| --- | --- |
| From | ``` func chapterMetadataGroupsWithTitleLocale(_ locale: NSLocale, containingItemsWithCommonKeys commonKeys: [String]?) -> [AVTimedMetadataGroup] ``` |
| To | ``` func chapterMetadataGroups(withTitleLocale locale: Locale, containingItemsWithCommonKeys commonKeys: [String]?) -> [AVTimedMetadataGroup] ``` |

Modified [AVAsset.init(url: URL)](https://developer.apple.com/documentation/avfoundation/avasset/1389943-assetwithurl)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(URL URL: NSURL) ``` |
| To | ``` convenience init(url URL: URL) ``` |

Modified [AVAsset.isCompatibleWithAirPlayVideo](https://developer.apple.com/documentation/avfoundation/avasset/1390333-compatiblewithairplayvideo)

|  | Declaration |
| --- | --- |
| From | ``` var compatibleWithAirPlayVideo: Bool { get } ``` |
| To | ``` var isCompatibleWithAirPlayVideo: Bool { get } ``` |

Modified [AVAsset.isCompatibleWithSavedPhotosAlbum](https://developer.apple.com/documentation/avfoundation/avasset/1616742-iscompatiblewithsavedphotosalbum)

|  | Declaration |
| --- | --- |
| From | ``` var compatibleWithSavedPhotosAlbum: Bool { get } ``` |
| To | ``` var isCompatibleWithSavedPhotosAlbum: Bool { get } ``` |

Modified [AVAsset.isComposable](https://developer.apple.com/documentation/avfoundation/avasset/1386129-iscomposable)

|  | Declaration |
| --- | --- |
| From | ``` var composable: Bool { get } ``` |
| To | ``` var isComposable: Bool { get } ``` |

Modified [AVAsset.isExportable](https://developer.apple.com/documentation/avfoundation/avasset/1389245-isexportable)

|  | Declaration |
| --- | --- |
| From | ``` var exportable: Bool { get } ``` |
| To | ``` var isExportable: Bool { get } ``` |

Modified [AVAsset.isPlayable](https://developer.apple.com/documentation/avfoundation/avasset/1385974-playable)

|  | Declaration |
| --- | --- |
| From | ``` var playable: Bool { get } ``` |
| To | ``` var isPlayable: Bool { get } ``` |

Modified [AVAsset.isReadable](https://developer.apple.com/documentation/avfoundation/avasset/1390475-readable)

|  | Declaration |
| --- | --- |
| From | ``` var readable: Bool { get } ``` |
| To | ``` var isReadable: Bool { get } ``` |

Modified [AVAsset.mediaSelectionGroup(forMediaCharacteristic: String) -> AVMediaSelectionGroup?](https://developer.apple.com/documentation/avfoundation/avasset/1387496-mediaselectiongroupformediachara)

|  | Declaration |
| --- | --- |
| From | ``` func mediaSelectionGroupForMediaCharacteristic(_ mediaCharacteristic: String) -> AVMediaSelectionGroup? ``` |
| To | ``` func mediaSelectionGroup(forMediaCharacteristic mediaCharacteristic: String) -> AVMediaSelectionGroup? ``` |

Modified [AVAsset.metadata(forFormat: String) -> [AVMetadataItem]](https://developer.apple.com/documentation/avfoundation/avasset/1387759-metadata)

|  | Declaration |
| --- | --- |
| From | ``` func metadataForFormat(_ format: String) -> [AVMetadataItem] ``` |
| To | ``` func metadata(forFormat format: String) -> [AVMetadataItem] ``` |

Modified [AVAsset.track(withTrackID: CMPersistentTrackID) -> AVAssetTrack?](https://developer.apple.com/documentation/avfoundation/avasset/1390145-track)

|  | Declaration |
| --- | --- |
| From | ``` func trackWithTrackID(_ trackID: CMPersistentTrackID) -> AVAssetTrack? ``` |
| To | ``` func track(withTrackID trackID: CMPersistentTrackID) -> AVAssetTrack? ``` |

Modified [AVAsset.tracks(withMediaCharacteristic: String) -> [AVAssetTrack]](https://developer.apple.com/documentation/avfoundation/avasset/1389554-trackswithmediacharacteristic)

|  | Declaration |
| --- | --- |
| From | ``` func tracksWithMediaCharacteristic(_ mediaCharacteristic: String) -> [AVAssetTrack] ``` |
| To | ``` func tracks(withMediaCharacteristic mediaCharacteristic: String) -> [AVAssetTrack] ``` |

Modified [AVAsset.tracks(withMediaType: String) -> [AVAssetTrack]](https://developer.apple.com/documentation/avfoundation/avasset/1387140-trackswithmediatype)

|  | Declaration |
| --- | --- |
| From | ``` func tracksWithMediaType(_ mediaType: String) -> [AVAssetTrack] ``` |
| To | ``` func tracks(withMediaType mediaType: String) -> [AVAssetTrack] ``` |

Modified [AVAssetExportSession](https://developer.apple.com/documentation/avfoundation/avassetexportsession)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetExportSession : NSObject {     convenience init()     convenience init?(asset asset: AVAsset, presetName presetName: String)     class func exportSessionWithAsset(_ asset: AVAsset, presetName presetName: String) -> Self?     init?(asset asset: AVAsset, presetName presetName: String)     var presetName: String { get }     var asset: AVAsset { get }     var outputFileType: String?     @NSCopying var outputURL: NSURL?     var shouldOptimizeForNetworkUse: Bool     var status: AVAssetExportSessionStatus { get }     var error: NSError? { get }     func exportAsynchronouslyWithCompletionHandler(_ handler: () -> Void)     var progress: Float { get }     func cancelExport() } extension AVAssetExportSession {     class func allExportPresets() -> [String]     class func exportPresetsCompatibleWithAsset(_ asset: AVAsset) -> [String]     class func determineCompatibilityOfExportPreset(_ presetName: String, withAsset asset: AVAsset, outputFileType outputFileType: String?, completionHandler handler: (Bool) -> Void) } extension AVAssetExportSession {     var supportedFileTypes: [String] { get }     func determineCompatibleFileTypesWithCompletionHandler(_ handler: ([String]) -> Void) } extension AVAssetExportSession {     var timeRange: CMTimeRange     var maxDuration: CMTime { get }     var estimatedOutputFileLength: Int64 { get }     var fileLengthLimit: Int64 } extension AVAssetExportSession {     var metadata: [AVMetadataItem]?     var metadataItemFilter: AVMetadataItemFilter? } extension AVAssetExportSession {     var audioTimePitchAlgorithm: String     @NSCopying var audioMix: AVAudioMix?     @NSCopying var videoComposition: AVVideoComposition?     var customVideoCompositor: AVVideoCompositing? { get } } extension AVAssetExportSession {     var canPerformMultiplePassesOverSourceMediaData: Bool     @NSCopying var directoryForTemporaryFiles: NSURL? } ``` | -- |
| To | ``` class AVAssetExportSession : NSObject {     convenience init()     convenience init?(asset asset: AVAsset, presetName presetName: String)     class func withAsset(_ asset: AVAsset, presetName presetName: String) -> Self?     init?(asset asset: AVAsset, presetName presetName: String)     var presetName: String { get }     var asset: AVAsset { get }     var outputFileType: String?     var outputURL: URL?     var shouldOptimizeForNetworkUse: Bool     var status: AVAssetExportSessionStatus { get }     var error: Error? { get }     func exportAsynchronously(completionHandler handler: @escaping () -> Swift.Void)     var progress: Float { get }     func cancelExport()     var canPerformMultiplePassesOverSourceMediaData: Bool     var directoryForTemporaryFiles: URL?     var audioTimePitchAlgorithm: String     @NSCopying var audioMix: AVAudioMix?     @NSCopying var videoComposition: AVVideoComposition?     var customVideoCompositor: AVVideoCompositing? { get }     var metadata: [AVMetadataItem]?     var metadataItemFilter: AVMetadataItemFilter?     var timeRange: CMTimeRange     var maxDuration: CMTime { get }     var estimatedOutputFileLength: Int64 { get }     var fileLengthLimit: Int64     var supportedFileTypes: [String] { get }     func determineCompatibleFileTypes(completionHandler handler: @escaping ([String]) -> Swift.Void)     class func allExportPresets() -> [String]     class func exportPresets(compatibleWith asset: AVAsset) -> [String]     class func determineCompatibility(ofExportPreset presetName: String, with asset: AVAsset, outputFileType outputFileType: String?, completionHandler handler: @escaping (Bool) -> Swift.Void)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetExportSession : CVarArg { } extension AVAssetExportSession : Equatable, Hashable {     var hashValue: Int { get } } extension AVAssetExportSession {     class func allExportPresets() -> [String]     class func exportPresets(compatibleWith asset: AVAsset) -> [String]     class func determineCompatibility(ofExportPreset presetName: String, with asset: AVAsset, outputFileType outputFileType: String?, completionHandler handler: @escaping (Bool) -> Swift.Void) } extension AVAssetExportSession {     var supportedFileTypes: [String] { get }     func determineCompatibleFileTypes(completionHandler handler: @escaping ([String]) -> Swift.Void) } extension AVAssetExportSession {     var timeRange: CMTimeRange     var maxDuration: CMTime { get }     var estimatedOutputFileLength: Int64 { get }     var fileLengthLimit: Int64 } extension AVAssetExportSession {     var metadata: [AVMetadataItem]?     var metadataItemFilter: AVMetadataItemFilter? } extension AVAssetExportSession {     var audioTimePitchAlgorithm: String     @NSCopying var audioMix: AVAudioMix?     @NSCopying var videoComposition: AVVideoComposition?     var customVideoCompositor: AVVideoCompositing? { get } } extension AVAssetExportSession {     var canPerformMultiplePassesOverSourceMediaData: Bool     var directoryForTemporaryFiles: URL? } ``` | CVarArg, Equatable, Hashable |

Modified [AVAssetExportSession.determineCompatibility(ofExportPreset: String, with: AVAsset, outputFileType: String?, completionHandler: (Bool) -> Swift.Void) [class]](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1385821-determinecompatibilityofexportpr)

|  | Declaration |
| --- | --- |
| From | ``` class func determineCompatibilityOfExportPreset(_ presetName: String, withAsset asset: AVAsset, outputFileType outputFileType: String?, completionHandler handler: (Bool) -> Void) ``` |
| To | ``` class func determineCompatibility(ofExportPreset presetName: String, with asset: AVAsset, outputFileType outputFileType: String?, completionHandler handler: @escaping (Bool) -> Swift.Void) ``` |

Modified [AVAssetExportSession.determineCompatibleFileTypes(completionHandler: ([String]) -> Swift.Void)](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1387907-determinecompatiblefiletypes)

|  | Declaration |
| --- | --- |
| From | ``` func determineCompatibleFileTypesWithCompletionHandler(_ handler: ([String]) -> Void) ``` |
| To | ``` func determineCompatibleFileTypes(completionHandler handler: @escaping ([String]) -> Swift.Void) ``` |

Modified [AVAssetExportSession.directoryForTemporaryFiles](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1388699-directoryfortemporaryfiles)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var directoryForTemporaryFiles: NSURL? ``` |
| To | ``` var directoryForTemporaryFiles: URL? ``` |

Modified [AVAssetExportSession.error](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1385936-error)

|  | Declaration |
| --- | --- |
| From | ``` var error: NSError? { get } ``` |
| To | ``` var error: Error? { get } ``` |

Modified [AVAssetExportSession.exportAsynchronously(completionHandler: () -> Swift.Void)](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1388005-exportasynchronouslywithcompleti)

|  | Declaration |
| --- | --- |
| From | ``` func exportAsynchronouslyWithCompletionHandler(_ handler: () -> Void) ``` |
| To | ``` func exportAsynchronously(completionHandler handler: @escaping () -> Swift.Void) ``` |

Modified [AVAssetExportSession.exportPresets(compatibleWith: AVAsset) -> [String] [class]](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1390567-exportpresetscompatiblewithasset)

|  | Declaration |
| --- | --- |
| From | ``` class func exportPresetsCompatibleWithAsset(_ asset: AVAsset) -> [String] ``` |
| To | ``` class func exportPresets(compatibleWith asset: AVAsset) -> [String] ``` |

Modified [AVAssetExportSession.outputURL](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1389970-outputurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var outputURL: NSURL? ``` |
| To | ``` var outputURL: URL? ``` |

Modified [AVAssetExportSessionStatus [enum]](https://developer.apple.com/documentation/avfoundation/avassetexportsession/status)

|  | Declaration |
| --- | --- |
| From | ``` enum AVAssetExportSessionStatus : Int {     case Unknown     case Waiting     case Exporting     case Completed     case Failed     case Cancelled } ``` |
| To | ``` enum AVAssetExportSessionStatus : Int {     case unknown     case waiting     case exporting     case completed     case failed     case cancelled } ``` |

Modified [AVAssetExportSessionStatus.cancelled](https://developer.apple.com/documentation/avfoundation/avassetexportsession/status/cancelled)

|  | Declaration |
| --- | --- |
| From | ``` case Cancelled ``` |
| To | ``` case cancelled ``` |

Modified [AVAssetExportSessionStatus.completed](https://developer.apple.com/documentation/avfoundation/avassetexportsession/status/completed)

|  | Declaration |
| --- | --- |
| From | ``` case Completed ``` |
| To | ``` case completed ``` |

Modified [AVAssetExportSessionStatus.exporting](https://developer.apple.com/documentation/avfoundation/avassetexportsession/status/exporting)

|  | Declaration |
| --- | --- |
| From | ``` case Exporting ``` |
| To | ``` case exporting ``` |

Modified [AVAssetExportSessionStatus.failed](https://developer.apple.com/documentation/avfoundation/avassetexportsessionstatus/avassetexportsessionstatusfailed)

|  | Declaration |
| --- | --- |
| From | ``` case Failed ``` |
| To | ``` case failed ``` |

Modified [AVAssetExportSessionStatus.unknown](https://developer.apple.com/documentation/avfoundation/avassetexportsession/status/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [AVAssetExportSessionStatus.waiting](https://developer.apple.com/documentation/avfoundation/avassetexportsession/status/waiting)

|  | Declaration |
| --- | --- |
| From | ``` case Waiting ``` |
| To | ``` case waiting ``` |

Modified [AVAssetImageGenerator](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetImageGenerator : NSObject {     convenience init()     var asset: AVAsset { get }     var appliesPreferredTrackTransform: Bool     var maximumSize: CGSize     var apertureMode: String?     @NSCopying var videoComposition: AVVideoComposition?     var customVideoCompositor: AVVideoCompositing? { get }     var requestedTimeToleranceBefore: CMTime     var requestedTimeToleranceAfter: CMTime     convenience init(asset asset: AVAsset)     class func assetImageGeneratorWithAsset(_ asset: AVAsset) -> Self     init(asset asset: AVAsset)     func copyCGImageAtTime(_ requestedTime: CMTime, actualTime actualTime: UnsafeMutablePointer<CMTime>) throws -> CGImage     func generateCGImagesAsynchronouslyForTimes(_ requestedTimes: [NSValue], completionHandler handler: AVAssetImageGeneratorCompletionHandler)     func cancelAllCGImageGeneration() } ``` | -- |
| To | ``` class AVAssetImageGenerator : NSObject {     convenience init()     var asset: AVAsset { get }     var appliesPreferredTrackTransform: Bool     var maximumSize: CGSize     var apertureMode: String?     @NSCopying var videoComposition: AVVideoComposition?     var customVideoCompositor: AVVideoCompositing? { get }     var requestedTimeToleranceBefore: CMTime     var requestedTimeToleranceAfter: CMTime     convenience init(asset asset: AVAsset)     class func withAsset(_ asset: AVAsset) -> Self     init(asset asset: AVAsset)     func copyCGImage(at requestedTime: CMTime, actualTime actualTime: UnsafeMutablePointer<CMTime>?) throws -> CGImage     func generateCGImagesAsynchronously(forTimes requestedTimes: [NSValue], completionHandler handler: AVFoundation.AVAssetImageGeneratorCompletionHandler)     func cancelAllCGImageGeneration()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetImageGenerator : CVarArg { } extension AVAssetImageGenerator : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAssetImageGenerator.copyCGImage(at: CMTime, actualTime: UnsafeMutablePointer<CMTime>?) throws -> CGImage](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1387303-copycgimageattime)

|  | Declaration |
| --- | --- |
| From | ``` func copyCGImageAtTime(_ requestedTime: CMTime, actualTime actualTime: UnsafeMutablePointer<CMTime>) throws -> CGImage ``` |
| To | ``` func copyCGImage(at requestedTime: CMTime, actualTime actualTime: UnsafeMutablePointer<CMTime>?) throws -> CGImage ``` |

Modified [AVAssetImageGenerator.generateCGImagesAsynchronously(forTimes: [NSValue], completionHandler: AVFoundation.AVAssetImageGeneratorCompletionHandler)](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1388100-generatecgimagesasynchronouslyfo)

|  | Declaration |
| --- | --- |
| From | ``` func generateCGImagesAsynchronouslyForTimes(_ requestedTimes: [NSValue], completionHandler handler: AVAssetImageGeneratorCompletionHandler) ``` |
| To | ``` func generateCGImagesAsynchronously(forTimes requestedTimes: [NSValue], completionHandler handler: AVFoundation.AVAssetImageGeneratorCompletionHandler) ``` |

Modified [AVAssetImageGeneratorResult [enum]](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/result)

|  | Declaration |
| --- | --- |
| From | ``` enum AVAssetImageGeneratorResult : Int {     case Succeeded     case Failed     case Cancelled } ``` |
| To | ``` enum AVAssetImageGeneratorResult : Int {     case succeeded     case failed     case cancelled } ``` |

Modified [AVAssetImageGeneratorResult.cancelled](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/result/cancelled)

|  | Declaration |
| --- | --- |
| From | ``` case Cancelled ``` |
| To | ``` case cancelled ``` |

Modified [AVAssetImageGeneratorResult.failed](https://developer.apple.com/documentation/avfoundation/avassetimagegeneratorresult/avassetimagegeneratorfailed)

|  | Declaration |
| --- | --- |
| From | ``` case Failed ``` |
| To | ``` case failed ``` |

Modified [AVAssetImageGeneratorResult.succeeded](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/result/succeeded)

|  | Declaration |
| --- | --- |
| From | ``` case Succeeded ``` |
| To | ``` case succeeded ``` |

Modified [AVAssetReader](https://developer.apple.com/documentation/avfoundation/avassetreader)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetReader : NSObject {     convenience init()     convenience init(asset asset: AVAsset) throws     class func assetReaderWithAsset(_ asset: AVAsset) throws -> Self     init(asset asset: AVAsset) throws     var asset: AVAsset { get }     var status: AVAssetReaderStatus { get }     var error: NSError? { get }     var timeRange: CMTimeRange     var outputs: [AVAssetReaderOutput] { get }     func canAddOutput(_ output: AVAssetReaderOutput) -> Bool     func addOutput(_ output: AVAssetReaderOutput)     func startReading() -> Bool     func cancelReading() } ``` | -- |
| To | ``` class AVAssetReader : NSObject {     convenience init()     convenience init(asset asset: AVAsset) throws     class func withAsset(_ asset: AVAsset) throws -> Self     init(asset asset: AVAsset) throws     var asset: AVAsset { get }     var status: AVAssetReaderStatus { get }     var error: Error? { get }     var timeRange: CMTimeRange     var outputs: [AVAssetReaderOutput] { get }     func canAdd(_ output: AVAssetReaderOutput) -> Bool     func add(_ output: AVAssetReaderOutput)     func startReading() -> Bool     func cancelReading()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetReader : CVarArg { } extension AVAssetReader : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAssetReader.add(_: AVAssetReaderOutput)](https://developer.apple.com/documentation/avfoundation/avassetreader/1390110-addoutput)

|  | Declaration |
| --- | --- |
| From | ``` func addOutput(_ output: AVAssetReaderOutput) ``` |
| To | ``` func add(_ output: AVAssetReaderOutput) ``` |

Modified [AVAssetReader.canAdd(_: AVAssetReaderOutput) -> Bool](https://developer.apple.com/documentation/avfoundation/avassetreader/1387485-canadd)

|  | Declaration |
| --- | --- |
| From | ``` func canAddOutput(_ output: AVAssetReaderOutput) -> Bool ``` |
| To | ``` func canAdd(_ output: AVAssetReaderOutput) -> Bool ``` |

Modified [AVAssetReader.error](https://developer.apple.com/documentation/avfoundation/avassetreader/1388114-error)

|  | Declaration |
| --- | --- |
| From | ``` var error: NSError? { get } ``` |
| To | ``` var error: Error? { get } ``` |

Modified [AVAssetReaderAudioMixOutput](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetReaderAudioMixOutput : AVAssetReaderOutput {     convenience init()     convenience init(audioTracks audioTracks: [AVAssetTrack], audioSettings audioSettings: [String : AnyObject]?)     class func assetReaderAudioMixOutputWithAudioTracks(_ audioTracks: [AVAssetTrack], audioSettings audioSettings: [String : AnyObject]?) -> Self     init(audioTracks audioTracks: [AVAssetTrack], audioSettings audioSettings: [String : AnyObject]?)     var audioTracks: [AVAssetTrack] { get }     var audioSettings: [String : AnyObject]? { get }     @NSCopying var audioMix: AVAudioMix?     var audioTimePitchAlgorithm: String } ``` | -- |
| To | ``` class AVAssetReaderAudioMixOutput : AVAssetReaderOutput {     convenience init()     convenience init(audioTracks audioTracks: [AVAssetTrack], audioSettings audioSettings: [String : Any]?)     class func withAudioTracks(_ audioTracks: [AVAssetTrack], audioSettings audioSettings: [String : Any]?) -> Self     init(audioTracks audioTracks: [AVAssetTrack], audioSettings audioSettings: [String : Any]?)     var audioTracks: [AVAssetTrack] { get }     var audioSettings: [String : Any]? { get }     @NSCopying var audioMix: AVAudioMix?     var audioTimePitchAlgorithm: String     var supportsRandomAccess: Bool     func reset(forReadingTimeRanges timeRanges: [NSValue])     func markConfigurationAsFinal()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetReaderAudioMixOutput : CVarArg { } extension AVAssetReaderAudioMixOutput : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAssetReaderAudioMixOutput.audioSettings](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/1388860-audiosettings)

|  | Declaration |
| --- | --- |
| From | ``` var audioSettings: [String : AnyObject]? { get } ``` |
| To | ``` var audioSettings: [String : Any]? { get } ``` |

Modified [AVAssetReaderAudioMixOutput.init(audioTracks: [AVAssetTrack], audioSettings: [String : Any]?)](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/1388883-init)

|  | Declaration |
| --- | --- |
| From | ``` init(audioTracks audioTracks: [AVAssetTrack], audioSettings audioSettings: [String : AnyObject]?) ``` |
| To | ``` init(audioTracks audioTracks: [AVAssetTrack], audioSettings audioSettings: [String : Any]?) ``` |

Modified [AVAssetReaderOutput](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetReaderOutput : NSObject {     var mediaType: String { get }     var alwaysCopiesSampleData: Bool     func copyNextSampleBuffer() -> CMSampleBuffer? } extension AVAssetReaderOutput {     var supportsRandomAccess: Bool     func resetForReadingTimeRanges(_ timeRanges: [NSValue])     func markConfigurationAsFinal() } ``` | -- |
| To | ``` class AVAssetReaderOutput : NSObject {     var mediaType: String { get }     var alwaysCopiesSampleData: Bool     func copyNextSampleBuffer() -> CMSampleBuffer?     var supportsRandomAccess: Bool     func reset(forReadingTimeRanges timeRanges: [NSValue])     func markConfigurationAsFinal()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetReaderOutput : CVarArg { } extension AVAssetReaderOutput : Equatable, Hashable {     var hashValue: Int { get } } extension AVAssetReaderOutput {     var supportsRandomAccess: Bool     func reset(forReadingTimeRanges timeRanges: [NSValue])     func markConfigurationAsFinal() } ``` | CVarArg, Equatable, Hashable |

Modified [AVAssetReaderOutput.reset(forReadingTimeRanges: [NSValue])](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/1388890-reset)

|  | Declaration |
| --- | --- |
| From | ``` func resetForReadingTimeRanges(_ timeRanges: [NSValue]) ``` |
| To | ``` func reset(forReadingTimeRanges timeRanges: [NSValue]) ``` |

Modified [AVAssetReaderOutputMetadataAdaptor](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputmetadataadaptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetReaderOutputMetadataAdaptor : NSObject {     convenience init()     convenience init(assetReaderTrackOutput trackOutput: AVAssetReaderTrackOutput)     class func assetReaderOutputMetadataAdaptorWithAssetReaderTrackOutput(_ trackOutput: AVAssetReaderTrackOutput) -> Self     init(assetReaderTrackOutput trackOutput: AVAssetReaderTrackOutput)     var assetReaderTrackOutput: AVAssetReaderTrackOutput { get }     func nextTimedMetadataGroup() -> AVTimedMetadataGroup? } ``` | -- |
| To | ``` class AVAssetReaderOutputMetadataAdaptor : NSObject {     convenience init()     convenience init(assetReaderTrackOutput trackOutput: AVAssetReaderTrackOutput)     class func withAssetReaderTrackOutput(_ trackOutput: AVAssetReaderTrackOutput) -> Self     init(assetReaderTrackOutput trackOutput: AVAssetReaderTrackOutput)     var assetReaderTrackOutput: AVAssetReaderTrackOutput { get }     func nextTimedMetadataGroup() -> AVTimedMetadataGroup?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetReaderOutputMetadataAdaptor : CVarArg { } extension AVAssetReaderOutputMetadataAdaptor : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAssetReaderSampleReferenceOutput](https://developer.apple.com/documentation/avfoundation/avassetreadersamplereferenceoutput)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetReaderSampleReferenceOutput : AVAssetReaderOutput {     convenience init()     convenience init(track track: AVAssetTrack)     class func assetReaderSampleReferenceOutputWithTrack(_ track: AVAssetTrack) -> Self     init(track track: AVAssetTrack)     var track: AVAssetTrack { get } } ``` | -- |
| To | ``` class AVAssetReaderSampleReferenceOutput : AVAssetReaderOutput {     convenience init()     convenience init(track track: AVAssetTrack)     class func withTrack(_ track: AVAssetTrack) -> Self     init(track track: AVAssetTrack)     var track: AVAssetTrack { get }     var supportsRandomAccess: Bool     func reset(forReadingTimeRanges timeRanges: [NSValue])     func markConfigurationAsFinal()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetReaderSampleReferenceOutput : CVarArg { } extension AVAssetReaderSampleReferenceOutput : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAssetReaderStatus [enum]](https://developer.apple.com/documentation/avfoundation/avassetreader/status)

|  | Declaration |
| --- | --- |
| From | ``` enum AVAssetReaderStatus : Int {     case Unknown     case Reading     case Completed     case Failed     case Cancelled } ``` |
| To | ``` enum AVAssetReaderStatus : Int {     case unknown     case reading     case completed     case failed     case cancelled } ``` |

Modified [AVAssetReaderStatus.cancelled](https://developer.apple.com/documentation/avfoundation/avassetreader/status/cancelled)

|  | Declaration |
| --- | --- |
| From | ``` case Cancelled ``` |
| To | ``` case cancelled ``` |

Modified [AVAssetReaderStatus.completed](https://developer.apple.com/documentation/avfoundation/avassetreader/status/completed)

|  | Declaration |
| --- | --- |
| From | ``` case Completed ``` |
| To | ``` case completed ``` |

Modified [AVAssetReaderStatus.failed](https://developer.apple.com/documentation/avfoundation/avassetreader/status/failed)

|  | Declaration |
| --- | --- |
| From | ``` case Failed ``` |
| To | ``` case failed ``` |

Modified [AVAssetReaderStatus.reading](https://developer.apple.com/documentation/avfoundation/avassetreaderstatus/avassetreaderstatusreading)

|  | Declaration |
| --- | --- |
| From | ``` case Reading ``` |
| To | ``` case reading ``` |

Modified [AVAssetReaderStatus.unknown](https://developer.apple.com/documentation/avfoundation/avassetreader/status/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [AVAssetReaderTrackOutput](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetReaderTrackOutput : AVAssetReaderOutput {     convenience init()     convenience init(track track: AVAssetTrack, outputSettings outputSettings: [String : AnyObject]?)     class func assetReaderTrackOutputWithTrack(_ track: AVAssetTrack, outputSettings outputSettings: [String : AnyObject]?) -> Self     init(track track: AVAssetTrack, outputSettings outputSettings: [String : AnyObject]?)     var track: AVAssetTrack { get }     var outputSettings: [String : AnyObject]? { get }     var audioTimePitchAlgorithm: String } ``` | -- |
| To | ``` class AVAssetReaderTrackOutput : AVAssetReaderOutput {     convenience init()     convenience init(track track: AVAssetTrack, outputSettings outputSettings: [String : Any]?)     class func withTrack(_ track: AVAssetTrack, outputSettings outputSettings: [String : Any]?) -> Self     init(track track: AVAssetTrack, outputSettings outputSettings: [String : Any]?)     var track: AVAssetTrack { get }     var outputSettings: [String : Any]? { get }     var audioTimePitchAlgorithm: String     var supportsRandomAccess: Bool     func reset(forReadingTimeRanges timeRanges: [NSValue])     func markConfigurationAsFinal()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetReaderTrackOutput : CVarArg { } extension AVAssetReaderTrackOutput : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAssetReaderTrackOutput.init(track: AVAssetTrack, outputSettings: [String : Any]?)](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput/1385807-initwithtrack)

|  | Declaration |
| --- | --- |
| From | ``` init(track track: AVAssetTrack, outputSettings outputSettings: [String : AnyObject]?) ``` |
| To | ``` init(track track: AVAssetTrack, outputSettings outputSettings: [String : Any]?) ``` |

Modified [AVAssetReaderTrackOutput.outputSettings](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput/1387163-outputsettings)

|  | Declaration |
| --- | --- |
| From | ``` var outputSettings: [String : AnyObject]? { get } ``` |
| To | ``` var outputSettings: [String : Any]? { get } ``` |

Modified [AVAssetReaderVideoCompositionOutput](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetReaderVideoCompositionOutput : AVAssetReaderOutput {     convenience init()     convenience init(videoTracks videoTracks: [AVAssetTrack], videoSettings videoSettings: [String : AnyObject]?)     class func assetReaderVideoCompositionOutputWithVideoTracks(_ videoTracks: [AVAssetTrack], videoSettings videoSettings: [String : AnyObject]?) -> Self     init(videoTracks videoTracks: [AVAssetTrack], videoSettings videoSettings: [String : AnyObject]?)     var videoTracks: [AVAssetTrack] { get }     var videoSettings: [String : AnyObject]? { get }     @NSCopying var videoComposition: AVVideoComposition?     var customVideoCompositor: AVVideoCompositing? { get } } ``` | -- |
| To | ``` class AVAssetReaderVideoCompositionOutput : AVAssetReaderOutput {     convenience init()     convenience init(videoTracks videoTracks: [AVAssetTrack], videoSettings videoSettings: [String : Any]?)     class func withVideoTracks(_ videoTracks: [AVAssetTrack], videoSettings videoSettings: [String : Any]?) -> Self     init(videoTracks videoTracks: [AVAssetTrack], videoSettings videoSettings: [String : Any]?)     var videoTracks: [AVAssetTrack] { get }     var videoSettings: [String : Any]? { get }     @NSCopying var videoComposition: AVVideoComposition?     var customVideoCompositor: AVVideoCompositing? { get }     var supportsRandomAccess: Bool     func reset(forReadingTimeRanges timeRanges: [NSValue])     func markConfigurationAsFinal()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetReaderVideoCompositionOutput : CVarArg { } extension AVAssetReaderVideoCompositionOutput : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAssetReaderVideoCompositionOutput.init(videoTracks: [AVAssetTrack], videoSettings: [String : Any]?)](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/1386676-init)

|  | Declaration |
| --- | --- |
| From | ``` init(videoTracks videoTracks: [AVAssetTrack], videoSettings videoSettings: [String : AnyObject]?) ``` |
| To | ``` init(videoTracks videoTracks: [AVAssetTrack], videoSettings videoSettings: [String : Any]?) ``` |

Modified [AVAssetReaderVideoCompositionOutput.videoSettings](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/1389247-videosettings)

|  | Declaration |
| --- | --- |
| From | ``` var videoSettings: [String : AnyObject]? { get } ``` |
| To | ``` var videoSettings: [String : Any]? { get } ``` |

Modified [AVAssetReferenceRestrictions [struct]](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVAssetReferenceRestrictions : OptionSetType {     init(rawValue rawValue: UInt)     static var ForbidNone: AVAssetReferenceRestrictions { get }     static var ForbidRemoteReferenceToLocal: AVAssetReferenceRestrictions { get }     static var ForbidLocalReferenceToRemote: AVAssetReferenceRestrictions { get }     static var ForbidCrossSiteReference: AVAssetReferenceRestrictions { get }     static var ForbidLocalReferenceToLocal: AVAssetReferenceRestrictions { get }     static var ForbidAll: AVAssetReferenceRestrictions { get } } ``` | OptionSetType |
| To | ``` struct AVAssetReferenceRestrictions : OptionSet {     init(rawValue rawValue: UInt)     static var forbidNone: AVAssetReferenceRestrictions { get }     static var forbidRemoteReferenceToLocal: AVAssetReferenceRestrictions { get }     static var forbidLocalReferenceToRemote: AVAssetReferenceRestrictions { get }     static var forbidCrossSiteReference: AVAssetReferenceRestrictions { get }     static var forbidLocalReferenceToLocal: AVAssetReferenceRestrictions { get }     static var forbidAll: AVAssetReferenceRestrictions { get }     func intersect(_ other: AVAssetReferenceRestrictions) -> AVAssetReferenceRestrictions     func exclusiveOr(_ other: AVAssetReferenceRestrictions) -> AVAssetReferenceRestrictions     mutating func unionInPlace(_ other: AVAssetReferenceRestrictions)     mutating func intersectInPlace(_ other: AVAssetReferenceRestrictions)     mutating func exclusiveOrInPlace(_ other: AVAssetReferenceRestrictions)     func isSubsetOf(_ other: AVAssetReferenceRestrictions) -> Bool     func isDisjointWith(_ other: AVAssetReferenceRestrictions) -> Bool     func isSupersetOf(_ other: AVAssetReferenceRestrictions) -> Bool     mutating func subtractInPlace(_ other: AVAssetReferenceRestrictions)     func isStrictSupersetOf(_ other: AVAssetReferenceRestrictions) -> Bool     func isStrictSubsetOf(_ other: AVAssetReferenceRestrictions) -> Bool } extension AVAssetReferenceRestrictions {     func union(_ other: AVAssetReferenceRestrictions) -> AVAssetReferenceRestrictions     func intersection(_ other: AVAssetReferenceRestrictions) -> AVAssetReferenceRestrictions     func symmetricDifference(_ other: AVAssetReferenceRestrictions) -> AVAssetReferenceRestrictions } extension AVAssetReferenceRestrictions {     func contains(_ member: AVAssetReferenceRestrictions) -> Bool     mutating func insert(_ newMember: AVAssetReferenceRestrictions) -> (inserted: Bool, memberAfterInsert: AVAssetReferenceRestrictions)     mutating func remove(_ member: AVAssetReferenceRestrictions) -> AVAssetReferenceRestrictions?     mutating func update(with newMember: AVAssetReferenceRestrictions) -> AVAssetReferenceRestrictions? } extension AVAssetReferenceRestrictions {     convenience init()     mutating func formUnion(_ other: AVAssetReferenceRestrictions)     mutating func formIntersection(_ other: AVAssetReferenceRestrictions)     mutating func formSymmetricDifference(_ other: AVAssetReferenceRestrictions) } extension AVAssetReferenceRestrictions {     convenience init<S : Sequence where S.Iterator.Element == AVAssetReferenceRestrictions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AVAssetReferenceRestrictions...)     mutating func subtract(_ other: AVAssetReferenceRestrictions)     func isSubset(of other: AVAssetReferenceRestrictions) -> Bool     func isSuperset(of other: AVAssetReferenceRestrictions) -> Bool     func isDisjoint(with other: AVAssetReferenceRestrictions) -> Bool     func subtracting(_ other: AVAssetReferenceRestrictions) -> AVAssetReferenceRestrictions     var isEmpty: Bool { get }     func isStrictSuperset(of other: AVAssetReferenceRestrictions) -> Bool     func isStrictSubset(of other: AVAssetReferenceRestrictions) -> Bool } ``` | OptionSet |

Modified [AVAssetReferenceRestrictions.forbidAll](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/1387554-forbidall)

|  | Declaration |
| --- | --- |
| From | ``` static var ForbidAll: AVAssetReferenceRestrictions { get } ``` |
| To | ``` static var forbidAll: AVAssetReferenceRestrictions { get } ``` |

Modified [AVAssetReferenceRestrictions.forbidCrossSiteReference](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/avassetreferencerestrictionforbidcrosssitereference)

|  | Declaration |
| --- | --- |
| From | ``` static var ForbidCrossSiteReference: AVAssetReferenceRestrictions { get } ``` |
| To | ``` static var forbidCrossSiteReference: AVAssetReferenceRestrictions { get } ``` |

Modified [AVAssetReferenceRestrictions.forbidLocalReferenceToLocal](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/avassetreferencerestrictionforbidlocalreferencetolocal)

|  | Declaration |
| --- | --- |
| From | ``` static var ForbidLocalReferenceToLocal: AVAssetReferenceRestrictions { get } ``` |
| To | ``` static var forbidLocalReferenceToLocal: AVAssetReferenceRestrictions { get } ``` |

Modified [AVAssetReferenceRestrictions.forbidLocalReferenceToRemote](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/avassetreferencerestrictionforbidlocalreferencetoremote)

|  | Declaration |
| --- | --- |
| From | ``` static var ForbidLocalReferenceToRemote: AVAssetReferenceRestrictions { get } ``` |
| To | ``` static var forbidLocalReferenceToRemote: AVAssetReferenceRestrictions { get } ``` |

Modified [AVAssetReferenceRestrictions.forbidRemoteReferenceToLocal](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/1387464-forbidremotereferencetolocal)

|  | Declaration |
| --- | --- |
| From | ``` static var ForbidRemoteReferenceToLocal: AVAssetReferenceRestrictions { get } ``` |
| To | ``` static var forbidRemoteReferenceToLocal: AVAssetReferenceRestrictions { get } ``` |

Modified [AVAssetResourceLoader](https://developer.apple.com/documentation/avfoundation/avassetresourceloader)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetResourceLoader : NSObject {     init()     func setDelegate(_ delegate: AVAssetResourceLoaderDelegate?, queue delegateQueue: dispatch_queue_t?)     weak var delegate: AVAssetResourceLoaderDelegate? { get }     var delegateQueue: dispatch_queue_t? { get } } extension AVAssetResourceLoader {     var preloadsEligibleContentKeys: Bool } ``` | -- |
| To | ``` class AVAssetResourceLoader : NSObject {     init()     func setDelegate(_ delegate: AVAssetResourceLoaderDelegate?, queue delegateQueue: DispatchQueue?)     weak var delegate: AVAssetResourceLoaderDelegate? { get }     var delegateQueue: DispatchQueue? { get }     var preloadsEligibleContentKeys: Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetResourceLoader : CVarArg { } extension AVAssetResourceLoader : Equatable, Hashable {     var hashValue: Int { get } } extension AVAssetResourceLoader {     var preloadsEligibleContentKeys: Bool } ``` | CVarArg, Equatable, Hashable |

Modified [AVAssetResourceLoader.delegateQueue](https://developer.apple.com/documentation/avfoundation/avassetresourceloader/1387678-delegatequeue)

|  | Declaration |
| --- | --- |
| From | ``` var delegateQueue: dispatch_queue_t? { get } ``` |
| To | ``` var delegateQueue: DispatchQueue? { get } ``` |

Modified [AVAssetResourceLoader.setDelegate(_: AVAssetResourceLoaderDelegate?, queue: DispatchQueue?)](https://developer.apple.com/documentation/avfoundation/avassetresourceloader/1388314-setdelegate)

|  | Declaration |
| --- | --- |
| From | ``` func setDelegate(_ delegate: AVAssetResourceLoaderDelegate?, queue delegateQueue: dispatch_queue_t?) ``` |
| To | ``` func setDelegate(_ delegate: AVAssetResourceLoaderDelegate?, queue delegateQueue: DispatchQueue?) ``` |

Modified [AVAssetResourceLoaderDelegate](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVAssetResourceLoaderDelegate : NSObjectProtocol {     optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, shouldWaitForLoadingOfRequestedResource loadingRequest: AVAssetResourceLoadingRequest) -> Bool     optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, shouldWaitForRenewalOfRequestedResource renewalRequest: AVAssetResourceRenewalRequest) -> Bool     optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, didCancelLoadingRequest loadingRequest: AVAssetResourceLoadingRequest)     optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, shouldWaitForResponseToAuthenticationChallenge authenticationChallenge: NSURLAuthenticationChallenge) -> Bool     optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, didCancelAuthenticationChallenge authenticationChallenge: NSURLAuthenticationChallenge) } ``` |
| To | ``` protocol AVAssetResourceLoaderDelegate : NSObjectProtocol {     optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, shouldWaitForLoadingOfRequestedResource loadingRequest: AVAssetResourceLoadingRequest) -> Bool     optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, shouldWaitForRenewalOfRequestedResource renewalRequest: AVAssetResourceRenewalRequest) -> Bool     optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, didCancel loadingRequest: AVAssetResourceLoadingRequest)     optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, shouldWaitForResponseTo authenticationChallenge: URLAuthenticationChallenge) -> Bool     optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, didCancel authenticationChallenge: URLAuthenticationChallenge) } ``` |

Modified [AVAssetResourceLoaderDelegate.resourceLoader(_: AVAssetResourceLoader, didCancel: URLAuthenticationChallenge)](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/1387929-resourceloader)

|  | Declaration |
| --- | --- |
| From | ``` optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, didCancelAuthenticationChallenge authenticationChallenge: NSURLAuthenticationChallenge) ``` |
| To | ``` optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, didCancel authenticationChallenge: URLAuthenticationChallenge) ``` |

Modified [AVAssetResourceLoaderDelegate.resourceLoader(_: AVAssetResourceLoader, didCancel: AVAssetResourceLoadingRequest)](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/1387722-resourceloader)

|  | Declaration |
| --- | --- |
| From | ``` optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, didCancelLoadingRequest loadingRequest: AVAssetResourceLoadingRequest) ``` |
| To | ``` optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, didCancel loadingRequest: AVAssetResourceLoadingRequest) ``` |

Modified [AVAssetResourceLoaderDelegate.resourceLoader(_: AVAssetResourceLoader, shouldWaitForResponseTo: URLAuthenticationChallenge) -> Bool](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/1388736-resourceloader)

|  | Declaration |
| --- | --- |
| From | ``` optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, shouldWaitForResponseToAuthenticationChallenge authenticationChallenge: NSURLAuthenticationChallenge) -> Bool ``` |
| To | ``` optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, shouldWaitForResponseTo authenticationChallenge: URLAuthenticationChallenge) -> Bool ``` |

Modified [AVAssetResourceLoadingContentInformationRequest](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetResourceLoadingContentInformationRequest : NSObject {     init()     var contentType: String?     var contentLength: Int64     var byteRangeAccessSupported: Bool     @NSCopying var renewalDate: NSDate? } ``` | -- |
| To | ``` class AVAssetResourceLoadingContentInformationRequest : NSObject {     init()     var contentType: String?     var contentLength: Int64     var isByteRangeAccessSupported: Bool     var renewalDate: Date?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetResourceLoadingContentInformationRequest : CVarArg { } extension AVAssetResourceLoadingContentInformationRequest : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAssetResourceLoadingContentInformationRequest.isByteRangeAccessSupported](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/1386054-isbyterangeaccesssupported)

|  | Declaration |
| --- | --- |
| From | ``` var byteRangeAccessSupported: Bool ``` |
| To | ``` var isByteRangeAccessSupported: Bool ``` |

Modified [AVAssetResourceLoadingContentInformationRequest.renewalDate](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/1390683-renewaldate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var renewalDate: NSDate? ``` |
| To | ``` var renewalDate: Date? ``` |

Modified [AVAssetResourceLoadingDataRequest](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetResourceLoadingDataRequest : NSObject {     init()     var requestedOffset: Int64 { get }     var requestedLength: Int { get }     var requestsAllDataToEndOfResource: Bool { get }     var currentOffset: Int64 { get }     func respondWithData(_ data: NSData) } ``` | -- |
| To | ``` class AVAssetResourceLoadingDataRequest : NSObject {     init()     var requestedOffset: Int64 { get }     var requestedLength: Int { get }     var requestsAllDataToEndOfResource: Bool { get }     var currentOffset: Int64 { get }     func respond(with data: Data)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetResourceLoadingDataRequest : CVarArg { } extension AVAssetResourceLoadingDataRequest : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAssetResourceLoadingDataRequest.respond(with: Data)](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest/1390581-respondwithdata)

|  | Declaration |
| --- | --- |
| From | ``` func respondWithData(_ data: NSData) ``` |
| To | ``` func respond(with data: Data) ``` |

Modified [AVAssetResourceLoadingRequest](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetResourceLoadingRequest : NSObject {     init()     var request: NSURLRequest { get }     var finished: Bool { get }     var cancelled: Bool { get }     var contentInformationRequest: AVAssetResourceLoadingContentInformationRequest? { get }     var dataRequest: AVAssetResourceLoadingDataRequest? { get }     @NSCopying var response: NSURLResponse?     @NSCopying var redirect: NSURLRequest?     func finishLoading()     func finishLoadingWithError(_ error: NSError?) } extension AVAssetResourceLoadingRequest {     func streamingContentKeyRequestDataForApp(_ appIdentifier: NSData, contentIdentifier contentIdentifier: NSData, options options: [String : AnyObject]?) throws -> NSData     func persistentContentKeyFromKeyVendorResponse(_ keyVendorResponse: NSData, options options: [String : AnyObject]?, error outError: NSErrorPointer) -> NSData } extension AVAssetResourceLoadingRequest {     func finishLoadingWithResponse(_ response: NSURLResponse?, data data: NSData?, redirect redirect: NSURLRequest?) } ``` | -- |
| To | ``` class AVAssetResourceLoadingRequest : NSObject {     init()     var request: URLRequest { get }     var isFinished: Bool { get }     var isCancelled: Bool { get }     var contentInformationRequest: AVAssetResourceLoadingContentInformationRequest? { get }     var dataRequest: AVAssetResourceLoadingDataRequest? { get }     @NSCopying var response: URLResponse?     var redirect: URLRequest?     func finishLoading()     func finishLoading(with error: Error?)     func finishLoading(with response: URLResponse?, data data: Data?, redirect redirect: URLRequest?)     func streamingContentKeyRequestData(forApp appIdentifier: Data, contentIdentifier contentIdentifier: Data, options options: [String : Any]? = nil) throws -> Data     func persistentContentKey(fromKeyVendorResponse keyVendorResponse: Data, options options: [String : Any]? = nil, error outError: NSErrorPointer) -> Data     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetResourceLoadingRequest : CVarArg { } extension AVAssetResourceLoadingRequest : Equatable, Hashable {     var hashValue: Int { get } } extension AVAssetResourceLoadingRequest {     func streamingContentKeyRequestData(forApp appIdentifier: Data, contentIdentifier contentIdentifier: Data, options options: [String : Any]? = nil) throws -> Data     func persistentContentKey(fromKeyVendorResponse keyVendorResponse: Data, options options: [String : Any]? = nil, error outError: NSErrorPointer) -> Data } extension AVAssetResourceLoadingRequest {     func finishLoading(with response: URLResponse?, data data: Data?, redirect redirect: URLRequest?) } ``` | CVarArg, Equatable, Hashable |

Modified [AVAssetResourceLoadingRequest.finishLoading(with: Error?)](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1390491-finishloadingwitherror)

|  | Declaration |
| --- | --- |
| From | ``` func finishLoadingWithError(_ error: NSError?) ``` |
| To | ``` func finishLoading(with error: Error?) ``` |

Modified [AVAssetResourceLoadingRequest.isCancelled](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1389518-iscancelled)

|  | Declaration |
| --- | --- |
| From | ``` var cancelled: Bool { get } ``` |
| To | ``` var isCancelled: Bool { get } ``` |

Modified [AVAssetResourceLoadingRequest.isFinished](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1389270-isfinished)

|  | Declaration |
| --- | --- |
| From | ``` var finished: Bool { get } ``` |
| To | ``` var isFinished: Bool { get } ``` |

Modified [AVAssetResourceLoadingRequest.persistentContentKey(fromKeyVendorResponse: Data, options: [String : Any]?, error: NSErrorPointer) -> Data](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1623676-persistentcontentkey)

|  | Declaration |
| --- | --- |
| From | ``` func persistentContentKeyFromKeyVendorResponse(_ keyVendorResponse: NSData, options options: [String : AnyObject]?, error outError: NSErrorPointer) -> NSData ``` |
| To | ``` func persistentContentKey(fromKeyVendorResponse keyVendorResponse: Data, options options: [String : Any]? = nil, error outError: NSErrorPointer) -> Data ``` |

Modified [AVAssetResourceLoadingRequest.redirect](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1390854-redirect)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var redirect: NSURLRequest? ``` |
| To | ``` var redirect: URLRequest? ``` |

Modified [AVAssetResourceLoadingRequest.request](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1386220-request)

|  | Declaration |
| --- | --- |
| From | ``` var request: NSURLRequest { get } ``` |
| To | ``` var request: URLRequest { get } ``` |

Modified [AVAssetResourceLoadingRequest.response](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1389034-response)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var response: NSURLResponse? ``` |
| To | ``` @NSCopying var response: URLResponse? ``` |

Modified [AVAssetResourceLoadingRequest.streamingContentKeyRequestData(forApp: Data, contentIdentifier: Data, options: [String : Any]?) throws -> Data](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1386116-streamingcontentkeyrequestdatafo)

|  | Declaration |
| --- | --- |
| From | ``` func streamingContentKeyRequestDataForApp(_ appIdentifier: NSData, contentIdentifier contentIdentifier: NSData, options options: [String : AnyObject]?) throws -> NSData ``` |
| To | ``` func streamingContentKeyRequestData(forApp appIdentifier: Data, contentIdentifier contentIdentifier: Data, options options: [String : Any]? = nil) throws -> Data ``` |

Modified [AVAssetResourceRenewalRequest](https://developer.apple.com/documentation/avfoundation/avassetresourcerenewalrequest)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetResourceRenewalRequest : AVAssetResourceLoadingRequest { } ``` | -- |
| To | ``` class AVAssetResourceRenewalRequest : AVAssetResourceLoadingRequest {     func finishLoading(with response: URLResponse?, data data: Data?, redirect redirect: URLRequest?)     func streamingContentKeyRequestData(forApp appIdentifier: Data, contentIdentifier contentIdentifier: Data, options options: [String : Any]? = nil) throws -> Data     func persistentContentKey(fromKeyVendorResponse keyVendorResponse: Data, options options: [String : Any]? = nil, error outError: NSErrorPointer) -> Data     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetResourceRenewalRequest : CVarArg { } extension AVAssetResourceRenewalRequest : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAssetTrack](https://developer.apple.com/documentation/avfoundation/avassettrack)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetTrack : NSObject, NSCopying, AVAsynchronousKeyValueLoading {     init()     weak var asset: AVAsset? { get }     var trackID: CMPersistentTrackID { get } } extension AVAssetTrack {     var mediaType: String { get }     var formatDescriptions: [AnyObject] { get }     var playable: Bool { get }     var enabled: Bool { get }     var selfContained: Bool { get }     var totalSampleDataLength: Int64 { get }     func hasMediaCharacteristic(_ mediaCharacteristic: String) -> Bool } extension AVAssetTrack {     var timeRange: CMTimeRange { get }     var naturalTimeScale: CMTimeScale { get }     var estimatedDataRate: Float { get } } extension AVAssetTrack {     var languageCode: String { get }     var extendedLanguageTag: String { get } } extension AVAssetTrack {     var naturalSize: CGSize { get }     var preferredTransform: CGAffineTransform { get } } extension AVAssetTrack {     var preferredVolume: Float { get } } extension AVAssetTrack {     var nominalFrameRate: Float { get }     var minFrameDuration: CMTime { get }     var requiresFrameReordering: Bool { get } } extension AVAssetTrack {     var segments: [AVAssetTrackSegment] { get }     func segmentForTrackTime(_ trackTime: CMTime) -> AVAssetTrackSegment?     func samplePresentationTimeForTrackTime(_ trackTime: CMTime) -> CMTime } extension AVAssetTrack {     var commonMetadata: [AVMetadataItem] { get }     var metadata: [AVMetadataItem] { get }     var availableMetadataFormats: [String] { get }     func metadataForFormat(_ format: String) -> [AVMetadataItem] } extension AVAssetTrack {     var availableTrackAssociationTypes: [String] { get }     func associatedTracksOfType(_ trackAssociationType: String) -> [AVAssetTrack] } ``` | AVAsynchronousKeyValueLoading, NSCopying |
| To | ``` class AVAssetTrack : NSObject, NSCopying, AVAsynchronousKeyValueLoading {     init()     weak var asset: AVAsset? { get }     var trackID: CMPersistentTrackID { get }     var availableTrackAssociationTypes: [String] { get }     func associatedTracks(ofType trackAssociationType: String) -> [AVAssetTrack]     var commonMetadata: [AVMetadataItem] { get }     var metadata: [AVMetadataItem] { get }     var availableMetadataFormats: [String] { get }     func metadata(forFormat format: String) -> [AVMetadataItem]     var segments: [AVAssetTrackSegment] { get }     func segment(forTrackTime trackTime: CMTime) -> AVAssetTrackSegment?     func samplePresentationTime(forTrackTime trackTime: CMTime) -> CMTime     var nominalFrameRate: Float { get }     var minFrameDuration: CMTime { get }     var requiresFrameReordering: Bool { get }     var preferredVolume: Float { get }     var naturalSize: CGSize { get }     var preferredTransform: CGAffineTransform { get }     var languageCode: String? { get }     var extendedLanguageTag: String? { get }     var timeRange: CMTimeRange { get }     var naturalTimeScale: CMTimeScale { get }     var estimatedDataRate: Float { get }     var mediaType: String { get }     var formatDescriptions: [Any] { get }     var isPlayable: Bool { get }     var isEnabled: Bool { get }     var isSelfContained: Bool { get }     var totalSampleDataLength: Int64 { get }     func hasMediaCharacteristic(_ mediaCharacteristic: String) -> Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetTrack : CVarArg { } extension AVAssetTrack : Equatable, Hashable {     var hashValue: Int { get } } extension AVAssetTrack {     var mediaType: String { get }     var formatDescriptions: [Any] { get }     var isPlayable: Bool { get }     var isEnabled: Bool { get }     var isSelfContained: Bool { get }     var totalSampleDataLength: Int64 { get }     func hasMediaCharacteristic(_ mediaCharacteristic: String) -> Bool } extension AVAssetTrack {     var timeRange: CMTimeRange { get }     var naturalTimeScale: CMTimeScale { get }     var estimatedDataRate: Float { get } } extension AVAssetTrack {     var languageCode: String? { get }     var extendedLanguageTag: String? { get } } extension AVAssetTrack {     var naturalSize: CGSize { get }     var preferredTransform: CGAffineTransform { get } } extension AVAssetTrack {     var preferredVolume: Float { get } } extension AVAssetTrack {     var nominalFrameRate: Float { get }     var minFrameDuration: CMTime { get }     var requiresFrameReordering: Bool { get } } extension AVAssetTrack {     var segments: [AVAssetTrackSegment] { get }     func segment(forTrackTime trackTime: CMTime) -> AVAssetTrackSegment?     func samplePresentationTime(forTrackTime trackTime: CMTime) -> CMTime } extension AVAssetTrack {     var commonMetadata: [AVMetadataItem] { get }     var metadata: [AVMetadataItem] { get }     var availableMetadataFormats: [String] { get }     func metadata(forFormat format: String) -> [AVMetadataItem] } extension AVAssetTrack {     var availableTrackAssociationTypes: [String] { get }     func associatedTracks(ofType trackAssociationType: String) -> [AVAssetTrack] } ``` | AVAsynchronousKeyValueLoading, CVarArg, Equatable, Hashable, NSCopying |

Modified [AVAssetTrack.associatedTracks(ofType: String) -> [AVAssetTrack]](https://developer.apple.com/documentation/avfoundation/avassettrack/1389251-associatedtracksoftype)

|  | Declaration |
| --- | --- |
| From | ``` func associatedTracksOfType(_ trackAssociationType: String) -> [AVAssetTrack] ``` |
| To | ``` func associatedTracks(ofType trackAssociationType: String) -> [AVAssetTrack] ``` |

Modified [AVAssetTrack.extendedLanguageTag](https://developer.apple.com/documentation/avfoundation/avassettrack/1389105-extendedlanguagetag)

|  | Declaration |
| --- | --- |
| From | ``` var extendedLanguageTag: String { get } ``` |
| To | ``` var extendedLanguageTag: String? { get } ``` |

Modified [AVAssetTrack.formatDescriptions](https://developer.apple.com/documentation/avfoundation/avassettrack/1386694-formatdescriptions)

|  | Declaration |
| --- | --- |
| From | ``` var formatDescriptions: [AnyObject] { get } ``` |
| To | ``` var formatDescriptions: [Any] { get } ``` |

Modified [AVAssetTrack.isEnabled](https://developer.apple.com/documentation/avfoundation/avassettrack/1387546-enabled)

|  | Declaration |
| --- | --- |
| From | ``` var enabled: Bool { get } ``` |
| To | ``` var isEnabled: Bool { get } ``` |

Modified [AVAssetTrack.isPlayable](https://developer.apple.com/documentation/avfoundation/avassettrack/1388276-playable)

|  | Declaration |
| --- | --- |
| From | ``` var playable: Bool { get } ``` |
| To | ``` var isPlayable: Bool { get } ``` |

Modified [AVAssetTrack.isSelfContained](https://developer.apple.com/documentation/avfoundation/avassettrack/1387643-selfcontained)

|  | Declaration |
| --- | --- |
| From | ``` var selfContained: Bool { get } ``` |
| To | ``` var isSelfContained: Bool { get } ``` |

Modified [AVAssetTrack.languageCode](https://developer.apple.com/documentation/avfoundation/avassettrack/1388627-languagecode)

|  | Declaration |
| --- | --- |
| From | ``` var languageCode: String { get } ``` |
| To | ``` var languageCode: String? { get } ``` |

Modified [AVAssetTrack.metadata(forFormat: String) -> [AVMetadataItem]](https://developer.apple.com/documentation/avfoundation/avassettrack/1387921-metadataforformat)

|  | Declaration |
| --- | --- |
| From | ``` func metadataForFormat(_ format: String) -> [AVMetadataItem] ``` |
| To | ``` func metadata(forFormat format: String) -> [AVMetadataItem] ``` |

Modified [AVAssetTrack.samplePresentationTime(forTrackTime: CMTime) -> CMTime](https://developer.apple.com/documentation/avfoundation/avassettrack/1388248-samplepresentationtime)

|  | Declaration |
| --- | --- |
| From | ``` func samplePresentationTimeForTrackTime(_ trackTime: CMTime) -> CMTime ``` |
| To | ``` func samplePresentationTime(forTrackTime trackTime: CMTime) -> CMTime ``` |

Modified [AVAssetTrack.segment(forTrackTime: CMTime) -> AVAssetTrackSegment?](https://developer.apple.com/documentation/avfoundation/avassettrack/1387186-segmentfortracktime)

|  | Declaration |
| --- | --- |
| From | ``` func segmentForTrackTime(_ trackTime: CMTime) -> AVAssetTrackSegment? ``` |
| To | ``` func segment(forTrackTime trackTime: CMTime) -> AVAssetTrackSegment? ``` |

Modified [AVAssetTrackGroup](https://developer.apple.com/documentation/avfoundation/avassettrackgroup)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetTrackGroup : NSObject, NSCopying {     var trackIDs: [NSNumber] { get } } ``` | NSCopying |
| To | ``` class AVAssetTrackGroup : NSObject, NSCopying {     var trackIDs: [NSNumber] { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetTrackGroup : CVarArg { } extension AVAssetTrackGroup : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [AVAssetTrackSegment](https://developer.apple.com/documentation/avfoundation/avassettracksegment)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetTrackSegment : NSObject {     init()     var timeMapping: CMTimeMapping { get }     var empty: Bool { get } } ``` | -- |
| To | ``` class AVAssetTrackSegment : NSObject {     init()     var timeMapping: CMTimeMapping { get }     var isEmpty: Bool { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetTrackSegment : CVarArg { } extension AVAssetTrackSegment : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAssetTrackSegment.isEmpty](https://developer.apple.com/documentation/avfoundation/avassettracksegment/1385714-isempty)

|  | Declaration |
| --- | --- |
| From | ``` var empty: Bool { get } ``` |
| To | ``` var isEmpty: Bool { get } ``` |

Modified [AVAssetWriter](https://developer.apple.com/documentation/avfoundation/avassetwriter)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetWriter : NSObject {     convenience init()     convenience init(URL outputURL: NSURL, fileType outputFileType: String) throws     class func assetWriterWithURL(_ outputURL: NSURL, fileType outputFileType: String) throws -> Self     init(URL outputURL: NSURL, fileType outputFileType: String) throws     @NSCopying var outputURL: NSURL { get }     var outputFileType: String { get }     var availableMediaTypes: [String] { get }     var status: AVAssetWriterStatus { get }     var error: NSError? { get }     var metadata: [AVMetadataItem]     var shouldOptimizeForNetworkUse: Bool     @NSCopying var directoryForTemporaryFiles: NSURL?     var inputs: [AVAssetWriterInput] { get }     func canApplyOutputSettings(_ outputSettings: [String : AnyObject]?, forMediaType mediaType: String) -> Bool     func canAddInput(_ input: AVAssetWriterInput) -> Bool     func addInput(_ input: AVAssetWriterInput)     func startWriting() -> Bool     func startSessionAtSourceTime(_ startTime: CMTime)     func endSessionAtSourceTime(_ endTime: CMTime)     func cancelWriting()     func finishWriting() -> Bool     func finishWritingWithCompletionHandler(_ handler: () -> Void) } extension AVAssetWriter {     var movieFragmentInterval: CMTime     var overallDurationHint: CMTime     var movieTimeScale: CMTimeScale } extension AVAssetWriter {     func canAddInputGroup(_ inputGroup: AVAssetWriterInputGroup) -> Bool     func addInputGroup(_ inputGroup: AVAssetWriterInputGroup)     var inputGroups: [AVAssetWriterInputGroup] { get } } ``` | -- |
| To | ``` class AVAssetWriter : NSObject {     convenience init()     convenience init(url outputURL: URL, fileType outputFileType: String) throws     class func withURL(_ outputURL: URL, fileType outputFileType: String) throws -> Self     init(outputURL outputURL: URL, fileType outputFileType: String) throws     var outputURL: URL { get }     var outputFileType: String { get }     var availableMediaTypes: [String] { get }     var status: AVAssetWriterStatus { get }     var error: Error? { get }     var metadata: [AVMetadataItem]     var shouldOptimizeForNetworkUse: Bool     var directoryForTemporaryFiles: URL?     var inputs: [AVAssetWriterInput] { get }     func canApply(outputSettings outputSettings: [String : Any]?, forMediaType mediaType: String) -> Bool     func canAdd(_ input: AVAssetWriterInput) -> Bool     func add(_ input: AVAssetWriterInput)     func startWriting() -> Bool     func startSession(atSourceTime startTime: CMTime)     func endSession(atSourceTime endTime: CMTime)     func cancelWriting()     func finishWriting() -> Bool     func finishWriting(completionHandler handler: @escaping () -> Swift.Void)     func canAdd(_ inputGroup: AVAssetWriterInputGroup) -> Bool     func add(_ inputGroup: AVAssetWriterInputGroup)     var inputGroups: [AVAssetWriterInputGroup] { get }     var movieFragmentInterval: CMTime     var overallDurationHint: CMTime     var movieTimeScale: CMTimeScale     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetWriter : CVarArg { } extension AVAssetWriter : Equatable, Hashable {     var hashValue: Int { get } } extension AVAssetWriter {     var movieFragmentInterval: CMTime     var overallDurationHint: CMTime     var movieTimeScale: CMTimeScale } extension AVAssetWriter {     func canAdd(_ inputGroup: AVAssetWriterInputGroup) -> Bool     func add(_ inputGroup: AVAssetWriterInputGroup)     var inputGroups: [AVAssetWriterInputGroup] { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAssetWriter.add(_: AVAssetWriterInputGroup)](https://developer.apple.com/documentation/avfoundation/avassetwriter/1385643-add)

|  | Declaration |
| --- | --- |
| From | ``` func addInputGroup(_ inputGroup: AVAssetWriterInputGroup) ``` |
| To | ``` func add(_ inputGroup: AVAssetWriterInputGroup) ``` |

Modified [AVAssetWriter.add(_: AVAssetWriterInput)](https://developer.apple.com/documentation/avfoundation/avassetwriter/1390389-addinput)

|  | Declaration |
| --- | --- |
| From | ``` func addInput(_ input: AVAssetWriterInput) ``` |
| To | ``` func add(_ input: AVAssetWriterInput) ``` |

Modified [AVAssetWriter.canAdd(_: AVAssetWriterInputGroup) -> Bool](https://developer.apple.com/documentation/avfoundation/avassetwriter/1386698-canadd)

|  | Declaration |
| --- | --- |
| From | ``` func canAddInputGroup(_ inputGroup: AVAssetWriterInputGroup) -> Bool ``` |
| To | ``` func canAdd(_ inputGroup: AVAssetWriterInputGroup) -> Bool ``` |

Modified [AVAssetWriter.canAdd(_: AVAssetWriterInput) -> Bool](https://developer.apple.com/documentation/avfoundation/avassetwriter/1387863-canaddinput)

|  | Declaration |
| --- | --- |
| From | ``` func canAddInput(_ input: AVAssetWriterInput) -> Bool ``` |
| To | ``` func canAdd(_ input: AVAssetWriterInput) -> Bool ``` |

Modified [AVAssetWriter.canApply(outputSettings: [String : Any]?, forMediaType: String) -> Bool](https://developer.apple.com/documentation/avfoundation/avassetwriter/1388842-canapplyoutputsettings)

|  | Declaration |
| --- | --- |
| From | ``` func canApplyOutputSettings(_ outputSettings: [String : AnyObject]?, forMediaType mediaType: String) -> Bool ``` |
| To | ``` func canApply(outputSettings outputSettings: [String : Any]?, forMediaType mediaType: String) -> Bool ``` |

Modified [AVAssetWriter.directoryForTemporaryFiles](https://developer.apple.com/documentation/avfoundation/avassetwriter/1387445-directoryfortemporaryfiles)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var directoryForTemporaryFiles: NSURL? ``` |
| To | ``` var directoryForTemporaryFiles: URL? ``` |

Modified [AVAssetWriter.endSession(atSourceTime: CMTime)](https://developer.apple.com/documentation/avfoundation/avassetwriter/1389921-endsessionatsourcetime)

|  | Declaration |
| --- | --- |
| From | ``` func endSessionAtSourceTime(_ endTime: CMTime) ``` |
| To | ``` func endSession(atSourceTime endTime: CMTime) ``` |

Modified [AVAssetWriter.error](https://developer.apple.com/documentation/avfoundation/avassetwriter/1390725-error)

|  | Declaration |
| --- | --- |
| From | ``` var error: NSError? { get } ``` |
| To | ``` var error: Error? { get } ``` |

Modified [AVAssetWriter.finishWriting(completionHandler: () -> Swift.Void)](https://developer.apple.com/documentation/avfoundation/avassetwriter/1390432-finishwritingwithcompletionhandl)

|  | Declaration |
| --- | --- |
| From | ``` func finishWritingWithCompletionHandler(_ handler: () -> Void) ``` |
| To | ``` func finishWriting(completionHandler handler: @escaping () -> Swift.Void) ``` |

Modified [AVAssetWriter.init(outputURL: URL, fileType: String) throws](https://developer.apple.com/documentation/avfoundation/avassetwriter/1389201-init)

|  | Declaration |
| --- | --- |
| From | ``` init(URL outputURL: NSURL, fileType outputFileType: String) throws ``` |
| To | ``` init(outputURL outputURL: URL, fileType outputFileType: String) throws ``` |

Modified [AVAssetWriter.outputURL](https://developer.apple.com/documentation/avfoundation/avassetwriter/1387731-outputurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var outputURL: NSURL { get } ``` |
| To | ``` var outputURL: URL { get } ``` |

Modified [AVAssetWriter.startSession(atSourceTime: CMTime)](https://developer.apple.com/documentation/avfoundation/avassetwriter/1389908-startsession)

|  | Declaration |
| --- | --- |
| From | ``` func startSessionAtSourceTime(_ startTime: CMTime) ``` |
| To | ``` func startSession(atSourceTime startTime: CMTime) ``` |

Modified [AVAssetWriterInput](https://developer.apple.com/documentation/avfoundation/avassetwriterinput)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetWriterInput : NSObject {     convenience init()     convenience init(mediaType mediaType: String, outputSettings outputSettings: [String : AnyObject]?)     class func assetWriterInputWithMediaType(_ mediaType: String, outputSettings outputSettings: [String : AnyObject]?) -> Self     convenience init(mediaType mediaType: String, outputSettings outputSettings: [String : AnyObject]?, sourceFormatHint sourceFormatHint: CMFormatDescription?)     class func assetWriterInputWithMediaType(_ mediaType: String, outputSettings outputSettings: [String : AnyObject]?, sourceFormatHint sourceFormatHint: CMFormatDescription?) -> Self     convenience init(mediaType mediaType: String, outputSettings outputSettings: [String : AnyObject]?)     init(mediaType mediaType: String, outputSettings outputSettings: [String : AnyObject]?, sourceFormatHint sourceFormatHint: CMFormatDescription?)     var mediaType: String { get }     var outputSettings: [String : AnyObject]? { get }     var sourceFormatHint: CMFormatDescription? { get }     var metadata: [AVMetadataItem]     var readyForMoreMediaData: Bool { get }     var expectsMediaDataInRealTime: Bool     func requestMediaDataWhenReadyOnQueue(_ queue: dispatch_queue_t, usingBlock block: () -> Void)     func appendSampleBuffer(_ sampleBuffer: CMSampleBuffer) -> Bool     func markAsFinished() } extension AVAssetWriterInput {     var languageCode: String?     var extendedLanguageTag: String? } extension AVAssetWriterInput {     var naturalSize: CGSize     var transform: CGAffineTransform } extension AVAssetWriterInput {     var preferredVolume: Float } extension AVAssetWriterInput {     var marksOutputTrackAsEnabled: Bool     var mediaTimeScale: CMTimeScale     var preferredMediaChunkDuration: CMTime     var preferredMediaChunkAlignment: Int     @NSCopying var sampleReferenceBaseURL: NSURL? } extension AVAssetWriterInput {     func canAddTrackAssociationWithTrackOfInput(_ input: AVAssetWriterInput, type trackAssociationType: String) -> Bool     func addTrackAssociationWithTrackOfInput(_ input: AVAssetWriterInput, type trackAssociationType: String) } extension AVAssetWriterInput {     var performsMultiPassEncodingIfSupported: Bool     var canPerformMultiplePasses: Bool { get }     var currentPassDescription: AVAssetWriterInputPassDescription? { get }     func respondToEachPassDescriptionOnQueue(_ queue: dispatch_queue_t, usingBlock block: dispatch_block_t)     func markCurrentPassAsFinished() } ``` | -- |
| To | ``` class AVAssetWriterInput : NSObject {     convenience init()     convenience init(mediaType mediaType: String, outputSettings outputSettings: [String : Any]?)     class func withMediaType(_ mediaType: String, outputSettings outputSettings: [String : Any]?) -> Self     convenience init(mediaType mediaType: String, outputSettings outputSettings: [String : Any]?, sourceFormatHint sourceFormatHint: CMFormatDescription?)     class func withMediaType(_ mediaType: String, outputSettings outputSettings: [String : Any]?, sourceFormatHint sourceFormatHint: CMFormatDescription?) -> Self     convenience init(mediaType mediaType: String, outputSettings outputSettings: [String : Any]?)     init(mediaType mediaType: String, outputSettings outputSettings: [String : Any]?, sourceFormatHint sourceFormatHint: CMFormatDescription?)     var mediaType: String { get }     var outputSettings: [String : Any]? { get }     var sourceFormatHint: CMFormatDescription? { get }     var metadata: [AVMetadataItem]     var isReadyForMoreMediaData: Bool { get }     var expectsMediaDataInRealTime: Bool     func requestMediaDataWhenReady(on queue: DispatchQueue, using block: @escaping () -> Swift.Void)     func append(_ sampleBuffer: CMSampleBuffer) -> Bool     func markAsFinished()     var performsMultiPassEncodingIfSupported: Bool     var canPerformMultiplePasses: Bool { get }     var currentPassDescription: AVAssetWriterInputPassDescription? { get }     func respondToEachPassDescription(on queue: DispatchQueue, using block: @escaping () -> Swift.Void)     func markCurrentPassAsFinished()     func canAddTrackAssociation(withTrackOf input: AVAssetWriterInput, type trackAssociationType: String) -> Bool     func addTrackAssociation(withTrackOf input: AVAssetWriterInput, type trackAssociationType: String)     var marksOutputTrackAsEnabled: Bool     var mediaTimeScale: CMTimeScale     var preferredMediaChunkDuration: CMTime     var preferredMediaChunkAlignment: Int     var sampleReferenceBaseURL: URL?     var preferredVolume: Float     var naturalSize: CGSize     var transform: CGAffineTransform     var languageCode: String?     var extendedLanguageTag: String?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetWriterInput : CVarArg { } extension AVAssetWriterInput : Equatable, Hashable {     var hashValue: Int { get } } extension AVAssetWriterInput {     var languageCode: String?     var extendedLanguageTag: String? } extension AVAssetWriterInput {     var naturalSize: CGSize     var transform: CGAffineTransform } extension AVAssetWriterInput {     var preferredVolume: Float } extension AVAssetWriterInput {     var marksOutputTrackAsEnabled: Bool     var mediaTimeScale: CMTimeScale     var preferredMediaChunkDuration: CMTime     var preferredMediaChunkAlignment: Int     var sampleReferenceBaseURL: URL? } extension AVAssetWriterInput {     func canAddTrackAssociation(withTrackOf input: AVAssetWriterInput, type trackAssociationType: String) -> Bool     func addTrackAssociation(withTrackOf input: AVAssetWriterInput, type trackAssociationType: String) } extension AVAssetWriterInput {     var performsMultiPassEncodingIfSupported: Bool     var canPerformMultiplePasses: Bool { get }     var currentPassDescription: AVAssetWriterInputPassDescription? { get }     func respondToEachPassDescription(on queue: DispatchQueue, using block: @escaping () -> Swift.Void)     func markCurrentPassAsFinished() } ``` | CVarArg, Equatable, Hashable |

Modified [AVAssetWriterInput.addTrackAssociation(withTrackOf: AVAssetWriterInput, type: String)](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1388347-addtrackassociationwithtrackofin)

|  | Declaration |
| --- | --- |
| From | ``` func addTrackAssociationWithTrackOfInput(_ input: AVAssetWriterInput, type trackAssociationType: String) ``` |
| To | ``` func addTrackAssociation(withTrackOf input: AVAssetWriterInput, type trackAssociationType: String) ``` |

Modified [AVAssetWriterInput.append(_: CMSampleBuffer) -> Bool](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1389566-append)

|  | Declaration |
| --- | --- |
| From | ``` func appendSampleBuffer(_ sampleBuffer: CMSampleBuffer) -> Bool ``` |
| To | ``` func append(_ sampleBuffer: CMSampleBuffer) -> Bool ``` |

Modified [AVAssetWriterInput.canAddTrackAssociation(withTrackOf: AVAssetWriterInput, type: String) -> Bool](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1388292-canaddtrackassociationwithtracko)

|  | Declaration |
| --- | --- |
| From | ``` func canAddTrackAssociationWithTrackOfInput(_ input: AVAssetWriterInput, type trackAssociationType: String) -> Bool ``` |
| To | ``` func canAddTrackAssociation(withTrackOf input: AVAssetWriterInput, type trackAssociationType: String) -> Bool ``` |

Modified [AVAssetWriterInput.init(mediaType: String, outputSettings: [String : Any]?)](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1385912-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(mediaType mediaType: String, outputSettings outputSettings: [String : AnyObject]?) ``` |
| To | ``` convenience init(mediaType mediaType: String, outputSettings outputSettings: [String : Any]?) ``` |

Modified [AVAssetWriterInput.init(mediaType: String, outputSettings: [String : Any]?, sourceFormatHint: CMFormatDescription?)](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1389994-init)

|  | Declaration |
| --- | --- |
| From | ``` init(mediaType mediaType: String, outputSettings outputSettings: [String : AnyObject]?, sourceFormatHint sourceFormatHint: CMFormatDescription?) ``` |
| To | ``` init(mediaType mediaType: String, outputSettings outputSettings: [String : Any]?, sourceFormatHint sourceFormatHint: CMFormatDescription?) ``` |

Modified [AVAssetWriterInput.isReadyForMoreMediaData](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1389084-readyformoremediadata)

|  | Declaration |
| --- | --- |
| From | ``` var readyForMoreMediaData: Bool { get } ``` |
| To | ``` var isReadyForMoreMediaData: Bool { get } ``` |

Modified [AVAssetWriterInput.outputSettings](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1388406-outputsettings)

|  | Declaration |
| --- | --- |
| From | ``` var outputSettings: [String : AnyObject]? { get } ``` |
| To | ``` var outputSettings: [String : Any]? { get } ``` |

Modified [AVAssetWriterInput.requestMediaDataWhenReady(on: DispatchQueue, using: () -> Swift.Void)](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1387508-requestmediadatawhenreadyonqueue)

|  | Declaration |
| --- | --- |
| From | ``` func requestMediaDataWhenReadyOnQueue(_ queue: dispatch_queue_t, usingBlock block: () -> Void) ``` |
| To | ``` func requestMediaDataWhenReady(on queue: DispatchQueue, using block: @escaping () -> Swift.Void) ``` |

Modified [AVAssetWriterInput.respondToEachPassDescription(on: DispatchQueue, using: () -> Swift.Void)](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1388489-respondtoeachpassdescription)

|  | Declaration |
| --- | --- |
| From | ``` func respondToEachPassDescriptionOnQueue(_ queue: dispatch_queue_t, usingBlock block: dispatch_block_t) ``` |
| To | ``` func respondToEachPassDescription(on queue: DispatchQueue, using block: @escaping () -> Swift.Void) ``` |

Modified [AVAssetWriterInput.sampleReferenceBaseURL](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1386316-samplereferencebaseurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var sampleReferenceBaseURL: NSURL? ``` |
| To | ``` var sampleReferenceBaseURL: URL? ``` |

Modified [AVAssetWriterInputGroup](https://developer.apple.com/documentation/avfoundation/avassetwriterinputgroup)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetWriterInputGroup : AVMediaSelectionGroup {     convenience init()     convenience init(inputs inputs: [AVAssetWriterInput], defaultInput defaultInput: AVAssetWriterInput?)     class func assetWriterInputGroupWithInputs(_ inputs: [AVAssetWriterInput], defaultInput defaultInput: AVAssetWriterInput?) -> Self     init(inputs inputs: [AVAssetWriterInput], defaultInput defaultInput: AVAssetWriterInput?)     var inputs: [AVAssetWriterInput] { get }     var defaultInput: AVAssetWriterInput? { get } } ``` | -- |
| To | ``` class AVAssetWriterInputGroup : AVMediaSelectionGroup {     convenience init()     convenience init(inputs inputs: [AVAssetWriterInput], defaultInput defaultInput: AVAssetWriterInput?)     class func withInputs(_ inputs: [AVAssetWriterInput], defaultInput defaultInput: AVAssetWriterInput?) -> Self     init(inputs inputs: [AVAssetWriterInput], defaultInput defaultInput: AVAssetWriterInput?)     var inputs: [AVAssetWriterInput] { get }     var defaultInput: AVAssetWriterInput? { get }     class func playableMediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption]) -> [AVMediaSelectionOption]     class func mediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption], filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [String]) -> [AVMediaSelectionOption]     class func mediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption], with locale: Locale) -> [AVMediaSelectionOption]     class func mediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption], withMediaCharacteristics mediaCharacteristics: [String]) -> [AVMediaSelectionOption]     class func mediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption], withoutMediaCharacteristics mediaCharacteristics: [String]) -> [AVMediaSelectionOption]     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetWriterInputGroup : CVarArg { } extension AVAssetWriterInputGroup : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAssetWriterInputMetadataAdaptor](https://developer.apple.com/documentation/avfoundation/avassetwriterinputmetadataadaptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetWriterInputMetadataAdaptor : NSObject {     convenience init()     convenience init(assetWriterInput input: AVAssetWriterInput)     class func assetWriterInputMetadataAdaptorWithAssetWriterInput(_ input: AVAssetWriterInput) -> Self     init(assetWriterInput input: AVAssetWriterInput)     var assetWriterInput: AVAssetWriterInput { get }     func appendTimedMetadataGroup(_ timedMetadataGroup: AVTimedMetadataGroup) -> Bool } ``` | -- |
| To | ``` class AVAssetWriterInputMetadataAdaptor : NSObject {     convenience init()     convenience init(assetWriterInput input: AVAssetWriterInput)     class func withAssetWriterInput(_ input: AVAssetWriterInput) -> Self     init(assetWriterInput input: AVAssetWriterInput)     var assetWriterInput: AVAssetWriterInput { get }     func append(_ timedMetadataGroup: AVTimedMetadataGroup) -> Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetWriterInputMetadataAdaptor : CVarArg { } extension AVAssetWriterInputMetadataAdaptor : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAssetWriterInputMetadataAdaptor.append(_: AVTimedMetadataGroup) -> Bool](https://developer.apple.com/documentation/avfoundation/avassetwriterinputmetadataadaptor/1389014-append)

|  | Declaration |
| --- | --- |
| From | ``` func appendTimedMetadataGroup(_ timedMetadataGroup: AVTimedMetadataGroup) -> Bool ``` |
| To | ``` func append(_ timedMetadataGroup: AVTimedMetadataGroup) -> Bool ``` |

Modified [AVAssetWriterInputPassDescription](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpassdescription)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetWriterInputPassDescription : NSObject {     init()     var sourceTimeRanges: [NSValue] { get } } ``` | -- |
| To | ``` class AVAssetWriterInputPassDescription : NSObject {     init()     var sourceTimeRanges: [NSValue] { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetWriterInputPassDescription : CVarArg { } extension AVAssetWriterInputPassDescription : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAssetWriterInputPixelBufferAdaptor](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAssetWriterInputPixelBufferAdaptor : NSObject {     convenience init()     convenience init(assetWriterInput input: AVAssetWriterInput, sourcePixelBufferAttributes sourcePixelBufferAttributes: [String : AnyObject]?)     class func assetWriterInputPixelBufferAdaptorWithAssetWriterInput(_ input: AVAssetWriterInput, sourcePixelBufferAttributes sourcePixelBufferAttributes: [String : AnyObject]?) -> Self     init(assetWriterInput input: AVAssetWriterInput, sourcePixelBufferAttributes sourcePixelBufferAttributes: [String : AnyObject]?)     var assetWriterInput: AVAssetWriterInput { get }     var sourcePixelBufferAttributes: [String : AnyObject]? { get }     var pixelBufferPool: CVPixelBufferPool? { get }     func appendPixelBuffer(_ pixelBuffer: CVPixelBuffer, withPresentationTime presentationTime: CMTime) -> Bool } ``` | -- |
| To | ``` class AVAssetWriterInputPixelBufferAdaptor : NSObject {     convenience init()     convenience init(assetWriterInput input: AVAssetWriterInput, sourcePixelBufferAttributes sourcePixelBufferAttributes: [String : Any]? = nil)     class func withAssetWriterInput(_ input: AVAssetWriterInput, sourcePixelBufferAttributes sourcePixelBufferAttributes: [String : Any]? = nil) -> Self     init(assetWriterInput input: AVAssetWriterInput, sourcePixelBufferAttributes sourcePixelBufferAttributes: [String : Any]? = nil)     var assetWriterInput: AVAssetWriterInput { get }     var sourcePixelBufferAttributes: [String : Any]? { get }     var pixelBufferPool: CVPixelBufferPool? { get }     func append(_ pixelBuffer: CVPixelBuffer, withPresentationTime presentationTime: CMTime) -> Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAssetWriterInputPixelBufferAdaptor : CVarArg { } extension AVAssetWriterInputPixelBufferAdaptor : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAssetWriterInputPixelBufferAdaptor.append(_: CVPixelBuffer, withPresentationTime: CMTime) -> Bool](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/1388102-appendpixelbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func appendPixelBuffer(_ pixelBuffer: CVPixelBuffer, withPresentationTime presentationTime: CMTime) -> Bool ``` |
| To | ``` func append(_ pixelBuffer: CVPixelBuffer, withPresentationTime presentationTime: CMTime) -> Bool ``` |

Modified [AVAssetWriterInputPixelBufferAdaptor.init(assetWriterInput: AVAssetWriterInput, sourcePixelBufferAttributes: [String : Any]?)](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/1390639-init)

|  | Declaration |
| --- | --- |
| From | ``` init(assetWriterInput input: AVAssetWriterInput, sourcePixelBufferAttributes sourcePixelBufferAttributes: [String : AnyObject]?) ``` |
| To | ``` init(assetWriterInput input: AVAssetWriterInput, sourcePixelBufferAttributes sourcePixelBufferAttributes: [String : Any]? = nil) ``` |

Modified [AVAssetWriterInputPixelBufferAdaptor.sourcePixelBufferAttributes](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/1387829-sourcepixelbufferattributes)

|  | Declaration |
| --- | --- |
| From | ``` var sourcePixelBufferAttributes: [String : AnyObject]? { get } ``` |
| To | ``` var sourcePixelBufferAttributes: [String : Any]? { get } ``` |

Modified [AVAssetWriterStatus [enum]](https://developer.apple.com/documentation/avfoundation/avassetwriter/status)

|  | Declaration |
| --- | --- |
| From | ``` enum AVAssetWriterStatus : Int {     case Unknown     case Writing     case Completed     case Failed     case Cancelled } ``` |
| To | ``` enum AVAssetWriterStatus : Int {     case unknown     case writing     case completed     case failed     case cancelled } ``` |

Modified [AVAssetWriterStatus.cancelled](https://developer.apple.com/documentation/avfoundation/avassetwriter/status/cancelled)

|  | Declaration |
| --- | --- |
| From | ``` case Cancelled ``` |
| To | ``` case cancelled ``` |

Modified [AVAssetWriterStatus.completed](https://developer.apple.com/documentation/avfoundation/avassetwriter/status/completed)

|  | Declaration |
| --- | --- |
| From | ``` case Completed ``` |
| To | ``` case completed ``` |

Modified [AVAssetWriterStatus.failed](https://developer.apple.com/documentation/avfoundation/avassetwriter/status/failed)

|  | Declaration |
| --- | --- |
| From | ``` case Failed ``` |
| To | ``` case failed ``` |

Modified [AVAssetWriterStatus.unknown](https://developer.apple.com/documentation/avfoundation/avassetwriter/status/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [AVAssetWriterStatus.writing](https://developer.apple.com/documentation/avfoundation/avassetwriterstatus/avassetwriterstatuswriting)

|  | Declaration |
| --- | --- |
| From | ``` case Writing ``` |
| To | ``` case writing ``` |

Modified [AVAsynchronousCIImageFilteringRequest](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAsynchronousCIImageFilteringRequest : NSObject, NSCopying {     var renderSize: CGSize { get }     var compositionTime: CMTime { get }     var sourceImage: CIImage { get }     func finishWithImage(_ filteredImage: CIImage, context context: CIContext?)     func finishWithError(_ error: NSError) } ``` | NSCopying |
| To | ``` class AVAsynchronousCIImageFilteringRequest : NSObject, NSCopying {     var renderSize: CGSize { get }     var compositionTime: CMTime { get }     var sourceImage: CIImage { get }     func finish(with filteredImage: CIImage, context context: CIContext?)     func finish(with error: Error)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAsynchronousCIImageFilteringRequest : CVarArg { } extension AVAsynchronousCIImageFilteringRequest : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [AVAsynchronousCIImageFilteringRequest.finish(with: Error)](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/1386608-finish)

|  | Declaration |
| --- | --- |
| From | ``` func finishWithError(_ error: NSError) ``` |
| To | ``` func finish(with error: Error) ``` |

Modified [AVAsynchronousCIImageFilteringRequest.finish(with: CIImage, context: CIContext?)](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/1389124-finish)

|  | Declaration |
| --- | --- |
| From | ``` func finishWithImage(_ filteredImage: CIImage, context context: CIContext?) ``` |
| To | ``` func finish(with filteredImage: CIImage, context context: CIContext?) ``` |

Modified [AVAsynchronousKeyValueLoading](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVAsynchronousKeyValueLoading {     func statusOfValueForKey(_ key: String, error outError: NSErrorPointer) -> AVKeyValueStatus     func loadValuesAsynchronouslyForKeys(_ keys: [String], completionHandler handler: (() -> Void)?) } ``` |
| To | ``` protocol AVAsynchronousKeyValueLoading {     func statusOfValue(forKey key: String, error outError: NSErrorPointer) -> AVKeyValueStatus     func loadValuesAsynchronously(forKeys keys: [String], completionHandler handler: (@escaping () -> Swift.Void)? = nil) } ``` |

Modified [AVAsynchronousKeyValueLoading.loadValuesAsynchronously() -> Swift.Void)? = nil)](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/1387321-loadvaluesasynchronouslyforkeys)

|  | Declaration |
| --- | --- |
| From | ``` func loadValuesAsynchronouslyForKeys(_ keys: [String], completionHandler handler: (() -> Void)?) ``` |
| To | ``` func loadValuesAsynchronously(forKeys keys: [String], completionHandler handler: (@escaping () -> Swift.Void)? = nil) ``` |

Modified [AVAsynchronousKeyValueLoading.statusOfValue(forKey: String, error: NSErrorPointer) -> AVKeyValueStatus](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/1386816-statusofvalue)

|  | Declaration |
| --- | --- |
| From | ``` func statusOfValueForKey(_ key: String, error outError: NSErrorPointer) -> AVKeyValueStatus ``` |
| To | ``` func statusOfValue(forKey key: String, error outError: NSErrorPointer) -> AVKeyValueStatus ``` |

Modified [AVAsynchronousVideoCompositionRequest](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAsynchronousVideoCompositionRequest : NSObject, NSCopying {     var renderContext: AVVideoCompositionRenderContext { get }     var compositionTime: CMTime { get }     var sourceTrackIDs: [NSNumber] { get }     var videoCompositionInstruction: AVVideoCompositionInstructionProtocol { get }     func sourceFrameByTrackID(_ trackID: CMPersistentTrackID) -> CVPixelBuffer?     func finishWithComposedVideoFrame(_ composedVideoFrame: CVPixelBuffer)     func finishWithError(_ error: NSError)     func finishCancelledRequest() } ``` | NSCopying |
| To | ``` class AVAsynchronousVideoCompositionRequest : NSObject, NSCopying {     var renderContext: AVVideoCompositionRenderContext { get }     var compositionTime: CMTime { get }     var sourceTrackIDs: [NSNumber] { get }     var videoCompositionInstruction: AVVideoCompositionInstructionProtocol { get }     func sourceFrame(byTrackID trackID: CMPersistentTrackID) -> CVPixelBuffer?     func finish(withComposedVideoFrame composedVideoFrame: CVPixelBuffer)     func finish(with error: Error)     func finishCancelledRequest()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAsynchronousVideoCompositionRequest : CVarArg { } extension AVAsynchronousVideoCompositionRequest : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [AVAsynchronousVideoCompositionRequest.finish(with: Error)](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1390797-finishwitherror)

|  | Declaration |
| --- | --- |
| From | ``` func finishWithError(_ error: NSError) ``` |
| To | ``` func finish(with error: Error) ``` |

Modified [AVAsynchronousVideoCompositionRequest.finish(withComposedVideoFrame: CVPixelBuffer)](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1387450-finishwithcomposedvideoframe)

|  | Declaration |
| --- | --- |
| From | ``` func finishWithComposedVideoFrame(_ composedVideoFrame: CVPixelBuffer) ``` |
| To | ``` func finish(withComposedVideoFrame composedVideoFrame: CVPixelBuffer) ``` |

Modified [AVAsynchronousVideoCompositionRequest.sourceFrame(byTrackID: CMPersistentTrackID) -> CVPixelBuffer?](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1390379-sourceframebytrackid)

|  | Declaration |
| --- | --- |
| From | ``` func sourceFrameByTrackID(_ trackID: CMPersistentTrackID) -> CVPixelBuffer? ``` |
| To | ``` func sourceFrame(byTrackID trackID: CMPersistentTrackID) -> CVPixelBuffer? ``` |

Modified [AVAudio3DMixingRenderingAlgorithm [enum]](https://developer.apple.com/documentation/avfoundation/avaudio3dmixingrenderingalgorithm)

|  | Declaration |
| --- | --- |
| From | ``` enum AVAudio3DMixingRenderingAlgorithm : Int {     case EqualPowerPanning     case SphericalHead     case HRTF     case SoundField     case StereoPassThrough } ``` |
| To | ``` enum AVAudio3DMixingRenderingAlgorithm : Int {     case equalPowerPanning     case sphericalHead     case HRTF     case soundField     case stereoPassThrough } ``` |

Modified [AVAudio3DMixingRenderingAlgorithm.equalPowerPanning](https://developer.apple.com/documentation/avfoundation/avaudio3dmixingrenderingalgorithm/avaudio3dmixingrenderingalgorithmequalpowerpanning)

|  | Declaration |
| --- | --- |
| From | ``` case EqualPowerPanning ``` |
| To | ``` case equalPowerPanning ``` |

Modified [AVAudio3DMixingRenderingAlgorithm.soundField](https://developer.apple.com/documentation/avfoundation/avaudio3dmixingrenderingalgorithm/soundfield)

|  | Declaration |
| --- | --- |
| From | ``` case SoundField ``` |
| To | ``` case soundField ``` |

Modified [AVAudio3DMixingRenderingAlgorithm.sphericalHead](https://developer.apple.com/documentation/avfoundation/avaudio3dmixingrenderingalgorithm/avaudio3dmixingrenderingalgorithmsphericalhead)

|  | Declaration |
| --- | --- |
| From | ``` case SphericalHead ``` |
| To | ``` case sphericalHead ``` |

Modified [AVAudio3DMixingRenderingAlgorithm.stereoPassThrough](https://developer.apple.com/documentation/avfoundation/avaudio3dmixingrenderingalgorithm/avaudio3dmixingrenderingalgorithmstereopassthrough)

|  | Declaration |
| --- | --- |
| From | ``` case StereoPassThrough ``` |
| To | ``` case stereoPassThrough ``` |

Modified [AVAudioBuffer](https://developer.apple.com/documentation/avfoundation/avaudiobuffer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioBuffer : NSObject, NSCopying, NSMutableCopying {     var format: AVAudioFormat { get }     var audioBufferList: UnsafePointer<AudioBufferList> { get }     var mutableAudioBufferList: UnsafeMutablePointer<AudioBufferList> { get } } ``` | NSCopying, NSMutableCopying |
| To | ``` class AVAudioBuffer : NSObject, NSCopying, NSMutableCopying {     var format: AVAudioFormat { get }     var audioBufferList: UnsafePointer<AudioBufferList> { get }     var mutableAudioBufferList: UnsafeMutablePointer<AudioBufferList> { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioBuffer : CVarArg { } extension AVAudioBuffer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSMutableCopying |

Modified [AVAudioChannelLayout](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioChannelLayout : NSObject, NSSecureCoding {     convenience init(layoutTag layoutTag: AudioChannelLayoutTag)     init(layout layout: UnsafePointer<AudioChannelLayout>)     func isEqual(_ object: AnyObject) -> Bool     class func layoutWithLayoutTag(_ layoutTag: AudioChannelLayoutTag) -> Self     class func layoutWithLayout(_ layout: UnsafePointer<AudioChannelLayout>) -> Self     var layoutTag: AudioChannelLayoutTag { get }     var layout: UnsafePointer<AudioChannelLayout> { get }     var channelCount: AVAudioChannelCount { get } } ``` | NSSecureCoding |
| To | ``` class AVAudioChannelLayout : NSObject, NSSecureCoding {     convenience init()     convenience init(layoutTag layoutTag: AudioChannelLayoutTag)     init(layout layout: UnsafePointer<AudioChannelLayout>)     func isEqual(_ object: Any) -> Bool     class func withLayoutTag(_ layoutTag: AudioChannelLayoutTag) -> Self     class func withLayout(_ layout: UnsafePointer<AudioChannelLayout>) -> Self     var layoutTag: AudioChannelLayoutTag { get }     var layout: UnsafePointer<AudioChannelLayout> { get }     var channelCount: AVAudioChannelCount { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioChannelLayout : CVarArg { } extension AVAudioChannelLayout : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSSecureCoding |

Modified [AVAudioChannelLayout.isEqual(_: Any) -> Bool](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1389677-isequal)

|  | Declaration |
| --- | --- |
| From | ``` func isEqual(_ object: AnyObject) -> Bool ``` |
| To | ``` func isEqual(_ object: Any) -> Bool ``` |

Modified [AVAudioCommonFormat [enum]](https://developer.apple.com/documentation/avfoundation/avaudiocommonformat)

|  | Declaration |
| --- | --- |
| From | ``` enum AVAudioCommonFormat : UInt {     case OtherFormat     case PCMFormatFloat32     case PCMFormatFloat64     case PCMFormatInt16     case PCMFormatInt32 } ``` |
| To | ``` enum AVAudioCommonFormat : UInt {     case otherFormat     case pcmFormatFloat32     case pcmFormatFloat64     case pcmFormatInt16     case pcmFormatInt32 } ``` |

Modified [AVAudioCommonFormat.otherFormat](https://developer.apple.com/documentation/avfoundation/avaudiocommonformat/avaudiootherformat)

|  | Declaration |
| --- | --- |
| From | ``` case OtherFormat ``` |
| To | ``` case otherFormat ``` |

Modified [AVAudioCommonFormat.pcmFormatFloat32](https://developer.apple.com/documentation/avfoundation/avaudiocommonformat/pcmformatfloat32)

|  | Declaration |
| --- | --- |
| From | ``` case PCMFormatFloat32 ``` |
| To | ``` case pcmFormatFloat32 ``` |

Modified [AVAudioCommonFormat.pcmFormatFloat64](https://developer.apple.com/documentation/avfoundation/avaudiocommonformat/avaudiopcmformatfloat64)

|  | Declaration |
| --- | --- |
| From | ``` case PCMFormatFloat64 ``` |
| To | ``` case pcmFormatFloat64 ``` |

Modified [AVAudioCommonFormat.pcmFormatInt16](https://developer.apple.com/documentation/avfoundation/avaudiocommonformat/pcmformatint16)

|  | Declaration |
| --- | --- |
| From | ``` case PCMFormatInt16 ``` |
| To | ``` case pcmFormatInt16 ``` |

Modified [AVAudioCommonFormat.pcmFormatInt32](https://developer.apple.com/documentation/avfoundation/avaudiocommonformat/avaudiopcmformatint32)

|  | Declaration |
| --- | --- |
| From | ``` case PCMFormatInt32 ``` |
| To | ``` case pcmFormatInt32 ``` |

Modified [AVAudioCompressedBuffer](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioCompressedBuffer : AVAudioBuffer {     init(format format: AVAudioFormat, packetCapacity packetCapacity: AVAudioPacketCount, maximumPacketSize maximumPacketSize: Int)     init(format format: AVAudioFormat, packetCapacity packetCapacity: AVAudioPacketCount)     var packetCapacity: AVAudioPacketCount { get }     var packetCount: AVAudioPacketCount     var maximumPacketSize: Int { get }     var data: UnsafeMutablePointer<Void> { get }     var packetDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription> { get } } ``` |
| To | ``` class AVAudioCompressedBuffer : AVAudioBuffer {     init(format format: AVAudioFormat, packetCapacity packetCapacity: AVAudioPacketCount, maximumPacketSize maximumPacketSize: Int)     init(format format: AVAudioFormat, packetCapacity packetCapacity: AVAudioPacketCount)     var packetCapacity: AVAudioPacketCount { get }     var packetCount: AVAudioPacketCount     var maximumPacketSize: Int { get }     var data: UnsafeMutableRawPointer { get }     var packetDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>? { get } } ``` |

Modified [AVAudioCompressedBuffer.data](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1390620-data)

|  | Declaration |
| --- | --- |
| From | ``` var data: UnsafeMutablePointer<Void> { get } ``` |
| To | ``` var data: UnsafeMutableRawPointer { get } ``` |

Modified [AVAudioCompressedBuffer.packetDescriptions](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1389750-packetdescriptions)

|  | Declaration |
| --- | --- |
| From | ``` var packetDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription> { get } ``` |
| To | ``` var packetDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>? { get } ``` |

Modified [AVAudioConnectionPoint](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioConnectionPoint : NSObject {     init(node node: AVAudioNode, bus bus: AVAudioNodeBus)     weak var node: AVAudioNode? { get }     var bus: AVAudioNodeBus { get } } ``` | -- |
| To | ``` class AVAudioConnectionPoint : NSObject {     init(node node: AVAudioNode, bus bus: AVAudioNodeBus)     convenience init()     weak var node: AVAudioNode? { get }     var bus: AVAudioNodeBus { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioConnectionPoint : CVarArg { } extension AVAudioConnectionPoint : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAudioConverter](https://developer.apple.com/documentation/avfoundation/avaudioconverter)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioConverter : NSObject {     init(fromFormat fromFormat: AVAudioFormat, toFormat toFormat: AVAudioFormat)     func reset()     var inputFormat: AVAudioFormat { get }     var outputFormat: AVAudioFormat { get }     var channelMap: [NSNumber]     var magicCookie: NSData?     var downmix: Bool     var dither: Bool     var sampleRateConverterQuality: Int     var sampleRateConverterAlgorithm: String     var primeMethod: AVAudioConverterPrimeMethod     var primeInfo: AVAudioConverterPrimeInfo     func convertToBuffer(_ outputBuffer: AVAudioPCMBuffer, fromBuffer inputBuffer: AVAudioPCMBuffer) throws     func convertToBuffer(_ outputBuffer: AVAudioBuffer, error outError: NSErrorPointer, withInputFromBlock inputBlock: AVAudioConverterInputBlock) -> AVAudioConverterOutputStatus } extension AVAudioConverter {     var bitRate: Int     var bitRateStrategy: String?     var maximumOutputPacketSize: Int { get }     var availableEncodeBitRates: [NSNumber]? { get }     var applicableEncodeBitRates: [NSNumber]? { get }     var availableEncodeSampleRates: [NSNumber]? { get }     var applicableEncodeSampleRates: [NSNumber]? { get }     var availableEncodeChannelLayoutTags: [NSNumber]? { get } } ``` | -- |
| To | ``` class AVAudioConverter : NSObject {     init(from fromFormat: AVAudioFormat, to toFormat: AVAudioFormat)     func reset()     var inputFormat: AVAudioFormat { get }     var outputFormat: AVAudioFormat { get }     var channelMap: [NSNumber]     var magicCookie: Data?     var downmix: Bool     var dither: Bool     var sampleRateConverterQuality: Int     var sampleRateConverterAlgorithm: String     var primeMethod: AVAudioConverterPrimeMethod     var primeInfo: AVAudioConverterPrimeInfo     func convert(to outputBuffer: AVAudioPCMBuffer, from inputBuffer: AVAudioPCMBuffer) throws     func convert(to outputBuffer: AVAudioBuffer, error outError: NSErrorPointer, withInputFrom inputBlock: AVFoundation.AVAudioConverterInputBlock) -> AVAudioConverterOutputStatus     var bitRate: Int     var bitRateStrategy: String?     var maximumOutputPacketSize: Int { get }     var availableEncodeBitRates: [NSNumber]? { get }     var applicableEncodeBitRates: [NSNumber]? { get }     var availableEncodeSampleRates: [NSNumber]? { get }     var applicableEncodeSampleRates: [NSNumber]? { get }     var availableEncodeChannelLayoutTags: [NSNumber]? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioConverter : CVarArg { } extension AVAudioConverter : Equatable, Hashable {     var hashValue: Int { get } } extension AVAudioConverter {     var bitRate: Int     var bitRateStrategy: String?     var maximumOutputPacketSize: Int { get }     var availableEncodeBitRates: [NSNumber]? { get }     var applicableEncodeBitRates: [NSNumber]? { get }     var availableEncodeSampleRates: [NSNumber]? { get }     var applicableEncodeSampleRates: [NSNumber]? { get }     var availableEncodeChannelLayoutTags: [NSNumber]? { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAudioConverter.convert(to: AVAudioBuffer, error: NSErrorPointer, withInputFrom: AVFoundation.AVAudioConverterInputBlock) -> AVAudioConverterOutputStatus](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387865-convert)

|  | Declaration |
| --- | --- |
| From | ``` func convertToBuffer(_ outputBuffer: AVAudioBuffer, error outError: NSErrorPointer, withInputFromBlock inputBlock: AVAudioConverterInputBlock) -> AVAudioConverterOutputStatus ``` |
| To | ``` func convert(to outputBuffer: AVAudioBuffer, error outError: NSErrorPointer, withInputFrom inputBlock: AVFoundation.AVAudioConverterInputBlock) -> AVAudioConverterOutputStatus ``` |

Modified [AVAudioConverter.convert(to: AVAudioPCMBuffer, from: AVAudioPCMBuffer) throws](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388341-converttobuffer)

|  | Declaration |
| --- | --- |
| From | ``` func convertToBuffer(_ outputBuffer: AVAudioPCMBuffer, fromBuffer inputBuffer: AVAudioPCMBuffer) throws ``` |
| To | ``` func convert(to outputBuffer: AVAudioPCMBuffer, from inputBuffer: AVAudioPCMBuffer) throws ``` |

Modified [AVAudioConverter.init(from: AVAudioFormat, to: AVAudioFormat)](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387008-initfromformat)

|  | Declaration |
| --- | --- |
| From | ``` init(fromFormat fromFormat: AVAudioFormat, toFormat toFormat: AVAudioFormat) ``` |
| To | ``` init(from fromFormat: AVAudioFormat, to toFormat: AVAudioFormat) ``` |

Modified [AVAudioConverter.magicCookie](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390770-magiccookie)

|  | Declaration |
| --- | --- |
| From | ``` var magicCookie: NSData? ``` |
| To | ``` var magicCookie: Data? ``` |

Modified [AVAudioConverterInputStatus [enum]](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum AVAudioConverterInputStatus : Int {     case HaveData     case NoDataNow     case EndOfStream } ``` |
| To | ``` enum AVAudioConverterInputStatus : Int {     case haveData     case noDataNow     case endOfStream } ``` |

Modified [AVAudioConverterInputStatus.endOfStream](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus/endofstream)

|  | Declaration |
| --- | --- |
| From | ``` case EndOfStream ``` |
| To | ``` case endOfStream ``` |

Modified [AVAudioConverterInputStatus.haveData](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus/avaudioconverterinputstatus_havedata)

|  | Declaration |
| --- | --- |
| From | ``` case HaveData ``` |
| To | ``` case haveData ``` |

Modified [AVAudioConverterInputStatus.noDataNow](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus/nodatanow)

|  | Declaration |
| --- | --- |
| From | ``` case NoDataNow ``` |
| To | ``` case noDataNow ``` |

Modified [AVAudioConverterOutputStatus [enum]](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum AVAudioConverterOutputStatus : Int {     case HaveData     case InputRanDry     case EndOfStream     case Error } ``` |
| To | ``` enum AVAudioConverterOutputStatus : Int {     case haveData     case inputRanDry     case endOfStream     case error } ``` |

Modified [AVAudioConverterOutputStatus.endOfStream](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/endofstream)

|  | Declaration |
| --- | --- |
| From | ``` case EndOfStream ``` |
| To | ``` case endOfStream ``` |

Modified [AVAudioConverterOutputStatus.error](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/error)

|  | Declaration |
| --- | --- |
| From | ``` case Error ``` |
| To | ``` case error ``` |

Modified [AVAudioConverterOutputStatus.haveData](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/avaudioconverteroutputstatus_havedata)

|  | Declaration |
| --- | --- |
| From | ``` case HaveData ``` |
| To | ``` case haveData ``` |

Modified [AVAudioConverterOutputStatus.inputRanDry](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/inputrandry)

|  | Declaration |
| --- | --- |
| From | ``` case InputRanDry ``` |
| To | ``` case inputRanDry ``` |

Modified [AVAudioConverterPrimeMethod [enum]](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod)

|  | Declaration |
| --- | --- |
| From | ``` enum AVAudioConverterPrimeMethod : Int {     case Pre     case Normal     case None } ``` |
| To | ``` enum AVAudioConverterPrimeMethod : Int {     case pre     case normal     case none } ``` |

Modified [AVAudioConverterPrimeMethod.none](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod/none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [AVAudioConverterPrimeMethod.normal](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod/normal)

|  | Declaration |
| --- | --- |
| From | ``` case Normal ``` |
| To | ``` case normal ``` |

Modified [AVAudioConverterPrimeMethod.pre](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod/pre)

|  | Declaration |
| --- | --- |
| From | ``` case Pre ``` |
| To | ``` case pre ``` |

Modified [AVAudioEngine](https://developer.apple.com/documentation/avfoundation/avaudioengine)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioEngine : NSObject {     init()     func attachNode(_ node: AVAudioNode)     func detachNode(_ node: AVAudioNode)     func connect(_ node1: AVAudioNode, to node2: AVAudioNode, fromBus bus1: AVAudioNodeBus, toBus bus2: AVAudioNodeBus, format format: AVAudioFormat?)     func connect(_ node1: AVAudioNode, to node2: AVAudioNode, format format: AVAudioFormat?)     func connect(_ sourceNode: AVAudioNode, toConnectionPoints destNodes: [AVAudioConnectionPoint], fromBus sourceBus: AVAudioNodeBus, format format: AVAudioFormat?)     func disconnectNodeInput(_ node: AVAudioNode, bus bus: AVAudioNodeBus)     func disconnectNodeInput(_ node: AVAudioNode)     func disconnectNodeOutput(_ node: AVAudioNode, bus bus: AVAudioNodeBus)     func disconnectNodeOutput(_ node: AVAudioNode)     func prepare()     func start() throws     func pause()     func reset()     func stop()     func inputConnectionPointForNode(_ node: AVAudioNode, inputBus bus: AVAudioNodeBus) -> AVAudioConnectionPoint?     func outputConnectionPointsForNode(_ node: AVAudioNode, outputBus bus: AVAudioNodeBus) -> [AVAudioConnectionPoint]     var musicSequence: MusicSequence     var outputNode: AVAudioOutputNode { get }     var inputNode: AVAudioInputNode? { get }     var mainMixerNode: AVAudioMixerNode { get }     var running: Bool { get } } ``` | -- |
| To | ``` class AVAudioEngine : NSObject {     init()     func attach(_ node: AVAudioNode)     func detach(_ node: AVAudioNode)     func connect(_ node1: AVAudioNode, to node2: AVAudioNode, fromBus bus1: AVAudioNodeBus, toBus bus2: AVAudioNodeBus, format format: AVAudioFormat?)     func connect(_ node1: AVAudioNode, to node2: AVAudioNode, format format: AVAudioFormat?)     func connect(_ sourceNode: AVAudioNode, to destNodes: [AVAudioConnectionPoint], fromBus sourceBus: AVAudioNodeBus, format format: AVAudioFormat?)     func disconnectNodeInput(_ node: AVAudioNode, bus bus: AVAudioNodeBus)     func disconnectNodeInput(_ node: AVAudioNode)     func disconnectNodeOutput(_ node: AVAudioNode, bus bus: AVAudioNodeBus)     func disconnectNodeOutput(_ node: AVAudioNode)     func prepare()     func start() throws     func pause()     func reset()     func stop()     func inputConnectionPoint(for node: AVAudioNode, inputBus bus: AVAudioNodeBus) -> AVAudioConnectionPoint?     func outputConnectionPoints(for node: AVAudioNode, outputBus bus: AVAudioNodeBus) -> [AVAudioConnectionPoint]     var musicSequence: MusicSequence?     var outputNode: AVAudioOutputNode { get }     var inputNode: AVAudioInputNode? { get }     var mainMixerNode: AVAudioMixerNode { get }     var isRunning: Bool { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioEngine : CVarArg { } extension AVAudioEngine : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAudioEngine.attach(_: AVAudioNode)](https://developer.apple.com/documentation/avfoundation/avaudioengine/1390685-attachnode)

|  | Declaration |
| --- | --- |
| From | ``` func attachNode(_ node: AVAudioNode) ``` |
| To | ``` func attach(_ node: AVAudioNode) ``` |

Modified [AVAudioEngine.connect(_: AVAudioNode, to: [AVAudioConnectionPoint], fromBus: AVAudioNodeBus, format: AVAudioFormat?)](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389510-connect)

|  | Declaration |
| --- | --- |
| From | ``` func connect(_ sourceNode: AVAudioNode, toConnectionPoints destNodes: [AVAudioConnectionPoint], fromBus sourceBus: AVAudioNodeBus, format format: AVAudioFormat?) ``` |
| To | ``` func connect(_ sourceNode: AVAudioNode, to destNodes: [AVAudioConnectionPoint], fromBus sourceBus: AVAudioNodeBus, format format: AVAudioFormat?) ``` |

Modified [AVAudioEngine.detach(_: AVAudioNode)](https://developer.apple.com/documentation/avfoundation/avaudioengine/1388198-detachnode)

|  | Declaration |
| --- | --- |
| From | ``` func detachNode(_ node: AVAudioNode) ``` |
| To | ``` func detach(_ node: AVAudioNode) ``` |

Modified [AVAudioEngine.inputConnectionPoint(for: AVAudioNode, inputBus: AVAudioNodeBus) -> AVAudioConnectionPoint?](https://developer.apple.com/documentation/avfoundation/avaudioengine/1387521-inputconnectionpoint)

|  | Declaration |
| --- | --- |
| From | ``` func inputConnectionPointForNode(_ node: AVAudioNode, inputBus bus: AVAudioNodeBus) -> AVAudioConnectionPoint? ``` |
| To | ``` func inputConnectionPoint(for node: AVAudioNode, inputBus bus: AVAudioNodeBus) -> AVAudioConnectionPoint? ``` |

Modified [AVAudioEngine.isRunning](https://developer.apple.com/documentation/avfoundation/avaudioengine/1388591-running)

|  | Declaration |
| --- | --- |
| From | ``` var running: Bool { get } ``` |
| To | ``` var isRunning: Bool { get } ``` |

Modified [AVAudioEngine.musicSequence](https://developer.apple.com/documentation/avfoundation/avaudioengine/1390410-musicsequence)

|  | Declaration |
| --- | --- |
| From | ``` var musicSequence: MusicSequence ``` |
| To | ``` var musicSequence: MusicSequence? ``` |

Modified [AVAudioEngine.outputConnectionPoints(for: AVAudioNode, outputBus: AVAudioNodeBus) -> [AVAudioConnectionPoint]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389298-outputconnectionpointsfornode)

|  | Declaration |
| --- | --- |
| From | ``` func outputConnectionPointsForNode(_ node: AVAudioNode, outputBus bus: AVAudioNodeBus) -> [AVAudioConnectionPoint] ``` |
| To | ``` func outputConnectionPoints(for node: AVAudioNode, outputBus bus: AVAudioNodeBus) -> [AVAudioConnectionPoint] ``` |

Modified [AVAudioEnvironmentDistanceAttenuationModel [enum]](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationmodel)

|  | Declaration |
| --- | --- |
| From | ``` enum AVAudioEnvironmentDistanceAttenuationModel : Int {     case Exponential     case Inverse     case Linear } ``` |
| To | ``` enum AVAudioEnvironmentDistanceAttenuationModel : Int {     case exponential     case inverse     case linear } ``` |

Modified [AVAudioEnvironmentDistanceAttenuationModel.exponential](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationmodel/exponential)

|  | Declaration |
| --- | --- |
| From | ``` case Exponential ``` |
| To | ``` case exponential ``` |

Modified [AVAudioEnvironmentDistanceAttenuationModel.inverse](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationmodel/inverse)

|  | Declaration |
| --- | --- |
| From | ``` case Inverse ``` |
| To | ``` case inverse ``` |

Modified [AVAudioEnvironmentDistanceAttenuationModel.linear](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationmodel/linear)

|  | Declaration |
| --- | --- |
| From | ``` case Linear ``` |
| To | ``` case linear ``` |

Modified [AVAudioEnvironmentDistanceAttenuationParameters](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationparameters)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioEnvironmentDistanceAttenuationParameters : NSObject {     var distanceAttenuationModel: AVAudioEnvironmentDistanceAttenuationModel     var referenceDistance: Float     var maximumDistance: Float     var rolloffFactor: Float } ``` | -- |
| To | ``` class AVAudioEnvironmentDistanceAttenuationParameters : NSObject {     var distanceAttenuationModel: AVAudioEnvironmentDistanceAttenuationModel     var referenceDistance: Float     var maximumDistance: Float     var rolloffFactor: Float     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioEnvironmentDistanceAttenuationParameters : CVarArg { } extension AVAudioEnvironmentDistanceAttenuationParameters : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAudioEnvironmentNode](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioEnvironmentNode : AVAudioNode, AVAudioMixing {     var outputVolume: Float     var nextAvailableInputBus: AVAudioNodeBus { get }     var listenerPosition: AVAudio3DPoint     var listenerVectorOrientation: AVAudio3DVectorOrientation     var listenerAngularOrientation: AVAudio3DAngularOrientation     var distanceAttenuationParameters: AVAudioEnvironmentDistanceAttenuationParameters { get }     var reverbParameters: AVAudioEnvironmentReverbParameters { get }     var applicableRenderingAlgorithms: [NSNumber] { get } } ``` |
| To | ``` class AVAudioEnvironmentNode : AVAudioNode, AVAudioMixing {     init()     var outputVolume: Float     var nextAvailableInputBus: AVAudioNodeBus { get }     var listenerPosition: AVAudio3DPoint     var listenerVectorOrientation: AVAudio3DVectorOrientation     var listenerAngularOrientation: AVAudio3DAngularOrientation     var distanceAttenuationParameters: AVAudioEnvironmentDistanceAttenuationParameters { get }     var reverbParameters: AVAudioEnvironmentReverbParameters { get }     var applicableRenderingAlgorithms: [NSNumber] { get } } ``` |

Modified [AVAudioEnvironmentReverbParameters](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentreverbparameters)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioEnvironmentReverbParameters : NSObject {     var enable: Bool     var level: Float     var filterParameters: AVAudioUnitEQFilterParameters { get }     func loadFactoryReverbPreset(_ preset: AVAudioUnitReverbPreset) } ``` | -- |
| To | ``` class AVAudioEnvironmentReverbParameters : NSObject {     var enable: Bool     var level: Float     var filterParameters: AVAudioUnitEQFilterParameters { get }     func loadFactoryReverbPreset(_ preset: AVAudioUnitReverbPreset)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioEnvironmentReverbParameters : CVarArg { } extension AVAudioEnvironmentReverbParameters : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAudioFile](https://developer.apple.com/documentation/avfoundation/avaudiofile)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioFile : NSObject {     init(forReading fileURL: NSURL) throws     init(forReading fileURL: NSURL, commonFormat format: AVAudioCommonFormat, interleaved interleaved: Bool) throws     init(forWriting fileURL: NSURL, settings settings: [String : AnyObject]) throws     init(forWriting fileURL: NSURL, settings settings: [String : AnyObject], commonFormat format: AVAudioCommonFormat, interleaved interleaved: Bool) throws     func readIntoBuffer(_ buffer: AVAudioPCMBuffer) throws     func readIntoBuffer(_ buffer: AVAudioPCMBuffer, frameCount frames: AVAudioFrameCount) throws     func writeFromBuffer(_ buffer: AVAudioPCMBuffer) throws     var url: NSURL { get }     var fileFormat: AVAudioFormat { get }     var processingFormat: AVAudioFormat { get }     var length: AVAudioFramePosition { get }     var framePosition: AVAudioFramePosition } ``` | -- |
| To | ``` class AVAudioFile : NSObject {     init(forReading fileURL: URL) throws     init(forReading fileURL: URL, commonFormat format: AVAudioCommonFormat, interleaved interleaved: Bool) throws     init(forWriting fileURL: URL, settings settings: [String : Any]) throws     init(forWriting fileURL: URL, settings settings: [String : Any], commonFormat format: AVAudioCommonFormat, interleaved interleaved: Bool) throws     func read(into buffer: AVAudioPCMBuffer) throws     func read(into buffer: AVAudioPCMBuffer, frameCount frames: AVAudioFrameCount) throws     func write(from buffer: AVAudioPCMBuffer) throws     var url: URL { get }     var fileFormat: AVAudioFormat { get }     var processingFormat: AVAudioFormat { get }     var length: AVAudioFramePosition { get }     var framePosition: AVAudioFramePosition     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioFile : CVarArg { } extension AVAudioFile : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAudioFile.init(forReading: URL) throws](https://developer.apple.com/documentation/avfoundation/avaudiofile/1388218-init)

|  | Declaration |
| --- | --- |
| From | ``` init(forReading fileURL: NSURL) throws ``` |
| To | ``` init(forReading fileURL: URL) throws ``` |

Modified [AVAudioFile.init(forReading: URL, commonFormat: AVAudioCommonFormat, interleaved: Bool) throws](https://developer.apple.com/documentation/avfoundation/avaudiofile/1387283-initforreading)

|  | Declaration |
| --- | --- |
| From | ``` init(forReading fileURL: NSURL, commonFormat format: AVAudioCommonFormat, interleaved interleaved: Bool) throws ``` |
| To | ``` init(forReading fileURL: URL, commonFormat format: AVAudioCommonFormat, interleaved interleaved: Bool) throws ``` |

Modified [AVAudioFile.init(forWriting: URL, settings: [String : Any]) throws](https://developer.apple.com/documentation/avfoundation/avaudiofile/1390840-initforwriting)

|  | Declaration |
| --- | --- |
| From | ``` init(forWriting fileURL: NSURL, settings settings: [String : AnyObject]) throws ``` |
| To | ``` init(forWriting fileURL: URL, settings settings: [String : Any]) throws ``` |

Modified [AVAudioFile.init(forWriting: URL, settings: [String : Any], commonFormat: AVAudioCommonFormat, interleaved: Bool) throws](https://developer.apple.com/documentation/avfoundation/avaudiofile/1387154-initforwriting)

|  | Declaration |
| --- | --- |
| From | ``` init(forWriting fileURL: NSURL, settings settings: [String : AnyObject], commonFormat format: AVAudioCommonFormat, interleaved interleaved: Bool) throws ``` |
| To | ``` init(forWriting fileURL: URL, settings settings: [String : Any], commonFormat format: AVAudioCommonFormat, interleaved interleaved: Bool) throws ``` |

Modified [AVAudioFile.read(into: AVAudioPCMBuffer) throws](https://developer.apple.com/documentation/avfoundation/avaudiofile/1388043-read)

|  | Declaration |
| --- | --- |
| From | ``` func readIntoBuffer(_ buffer: AVAudioPCMBuffer) throws ``` |
| To | ``` func read(into buffer: AVAudioPCMBuffer) throws ``` |

Modified [AVAudioFile.read(into: AVAudioPCMBuffer, frameCount: AVAudioFrameCount) throws](https://developer.apple.com/documentation/avfoundation/avaudiofile/1389774-read)

|  | Declaration |
| --- | --- |
| From | ``` func readIntoBuffer(_ buffer: AVAudioPCMBuffer, frameCount frames: AVAudioFrameCount) throws ``` |
| To | ``` func read(into buffer: AVAudioPCMBuffer, frameCount frames: AVAudioFrameCount) throws ``` |

Modified [AVAudioFile.url](https://developer.apple.com/documentation/avfoundation/avaudiofile/1387360-url)

|  | Declaration |
| --- | --- |
| From | ``` var url: NSURL { get } ``` |
| To | ``` var url: URL { get } ``` |

Modified [AVAudioFile.write(from: AVAudioPCMBuffer) throws](https://developer.apple.com/documentation/avfoundation/avaudiofile/1385637-write)

|  | Declaration |
| --- | --- |
| From | ``` func writeFromBuffer(_ buffer: AVAudioPCMBuffer) throws ``` |
| To | ``` func write(from buffer: AVAudioPCMBuffer) throws ``` |

Modified [AVAudioFormat](https://developer.apple.com/documentation/avfoundation/avaudioformat)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioFormat : NSObject, NSSecureCoding {     init(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>)     init(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>, channelLayout layout: AVAudioChannelLayout?)     init(standardFormatWithSampleRate sampleRate: Double, channels channels: AVAudioChannelCount)     init(standardFormatWithSampleRate sampleRate: Double, channelLayout layout: AVAudioChannelLayout)     init(commonFormat format: AVAudioCommonFormat, sampleRate sampleRate: Double, channels channels: AVAudioChannelCount, interleaved interleaved: Bool)     init(commonFormat format: AVAudioCommonFormat, sampleRate sampleRate: Double, interleaved interleaved: Bool, channelLayout layout: AVAudioChannelLayout)     init(settings settings: [String : AnyObject])     init(CMAudioFormatDescription formatDescription: CMAudioFormatDescription)     func isEqual(_ object: AnyObject) -> Bool     var standard: Bool { get }     var commonFormat: AVAudioCommonFormat { get }     var channelCount: AVAudioChannelCount { get }     var sampleRate: Double { get }     var interleaved: Bool { get }     var streamDescription: UnsafePointer<AudioStreamBasicDescription> { get }     var channelLayout: AVAudioChannelLayout? { get }     var settings: [String : AnyObject] { get }     var formatDescription: CMAudioFormatDescription { get } } ``` | NSSecureCoding |
| To | ``` class AVAudioFormat : NSObject, NSSecureCoding {     init(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>)     init(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>, channelLayout layout: AVAudioChannelLayout?)     init(standardFormatWithSampleRate sampleRate: Double, channels channels: AVAudioChannelCount)     init(standardFormatWithSampleRate sampleRate: Double, channelLayout layout: AVAudioChannelLayout)     init(commonFormat format: AVAudioCommonFormat, sampleRate sampleRate: Double, channels channels: AVAudioChannelCount, interleaved interleaved: Bool)     init(commonFormat format: AVAudioCommonFormat, sampleRate sampleRate: Double, interleaved interleaved: Bool, channelLayout layout: AVAudioChannelLayout)     init(settings settings: [String : Any])     init(cmAudioFormatDescription formatDescription: CMAudioFormatDescription)     func isEqual(_ object: Any) -> Bool     var isStandard: Bool { get }     var commonFormat: AVAudioCommonFormat { get }     var channelCount: AVAudioChannelCount { get }     var sampleRate: Double { get }     var isInterleaved: Bool { get }     var streamDescription: UnsafePointer<AudioStreamBasicDescription> { get }     var channelLayout: AVAudioChannelLayout? { get }     var magicCookie: Data?     var settings: [String : Any] { get }     var formatDescription: CMAudioFormatDescription { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioFormat : CVarArg { } extension AVAudioFormat : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSSecureCoding |

Modified [AVAudioFormat.init(cmAudioFormatDescription: CMAudioFormatDescription)](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387465-initwithcmaudioformatdescription)

|  | Declaration |
| --- | --- |
| From | ``` init(CMAudioFormatDescription formatDescription: CMAudioFormatDescription) ``` |
| To | ``` init(cmAudioFormatDescription formatDescription: CMAudioFormatDescription) ``` |

Modified [AVAudioFormat.init(settings: [String : Any])](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387931-init)

|  | Declaration |
| --- | --- |
| From | ``` init(settings settings: [String : AnyObject]) ``` |
| To | ``` init(settings settings: [String : Any]) ``` |

Modified [AVAudioFormat.isEqual(_: Any) -> Bool](https://developer.apple.com/documentation/avfoundation/avaudioformat/1385683-isequal)

|  | Declaration |
| --- | --- |
| From | ``` func isEqual(_ object: AnyObject) -> Bool ``` |
| To | ``` func isEqual(_ object: Any) -> Bool ``` |

Modified [AVAudioFormat.isInterleaved](https://developer.apple.com/documentation/avfoundation/avaudioformat/1389340-interleaved)

|  | Declaration |
| --- | --- |
| From | ``` var interleaved: Bool { get } ``` |
| To | ``` var isInterleaved: Bool { get } ``` |

Modified [AVAudioFormat.isStandard](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387347-isstandard)

|  | Declaration |
| --- | --- |
| From | ``` var standard: Bool { get } ``` |
| To | ``` var isStandard: Bool { get } ``` |

Modified [AVAudioFormat.settings](https://developer.apple.com/documentation/avfoundation/avaudioformat/1386904-settings)

|  | Declaration |
| --- | --- |
| From | ``` var settings: [String : AnyObject] { get } ``` |
| To | ``` var settings: [String : Any] { get } ``` |

Modified [AVAudioIONode](https://developer.apple.com/documentation/avfoundation/avaudioionode)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioIONode : AVAudioNode {     var presentationLatency: NSTimeInterval { get }     var audioUnit: AudioUnit { get } } ``` |
| To | ``` class AVAudioIONode : AVAudioNode {     var presentationLatency: TimeInterval { get }     var audioUnit: AudioUnit? { get } } ``` |

Modified [AVAudioIONode.audioUnit](https://developer.apple.com/documentation/avfoundation/avaudioionode/1390587-audiounit)

|  | Declaration |
| --- | --- |
| From | ``` var audioUnit: AudioUnit { get } ``` |
| To | ``` var audioUnit: AudioUnit? { get } ``` |

Modified [AVAudioIONode.presentationLatency](https://developer.apple.com/documentation/avfoundation/avaudioionode/1385631-presentationlatency)

|  | Declaration |
| --- | --- |
| From | ``` var presentationLatency: NSTimeInterval { get } ``` |
| To | ``` var presentationLatency: TimeInterval { get } ``` |

Modified [AVAudioMix](https://developer.apple.com/documentation/avfoundation/avaudiomix)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioMix : NSObject, NSCopying, NSMutableCopying {     var inputParameters: [AVAudioMixInputParameters] { get } } ``` | NSCopying, NSMutableCopying |
| To | ``` class AVAudioMix : NSObject, NSCopying, NSMutableCopying {     var inputParameters: [AVAudioMixInputParameters] { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioMix : CVarArg { } extension AVAudioMix : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSMutableCopying |

Modified [AVAudioMixerNode](https://developer.apple.com/documentation/avfoundation/avaudiomixernode)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioMixerNode : AVAudioNode, AVAudioMixing {     var outputVolume: Float     var nextAvailableInputBus: AVAudioNodeBus { get } } ``` |
| To | ``` class AVAudioMixerNode : AVAudioNode, AVAudioMixing {     init()     var outputVolume: Float     var nextAvailableInputBus: AVAudioNodeBus { get } } ``` |

Modified [AVAudioMixing](https://developer.apple.com/documentation/avfoundation/avaudiomixing)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVAudioMixing : AVAudioStereoMixing, AVAudio3DMixing {     func destinationForMixer(_ mixer: AVAudioNode, bus bus: AVAudioNodeBus) -> AVAudioMixingDestination?     var volume: Float { get set } } ``` |
| To | ``` protocol AVAudioMixing : AVAudioStereoMixing, AVAudio3DMixing {     func destination(forMixer mixer: AVAudioNode, bus bus: AVAudioNodeBus) -> AVAudioMixingDestination?     var volume: Float { get set } } ``` |

Modified [AVAudioMixing.destination(forMixer: AVAudioNode, bus: AVAudioNodeBus) -> AVAudioMixingDestination?](https://developer.apple.com/documentation/avfoundation/avaudiomixing/1390356-destination)

|  | Declaration |
| --- | --- |
| From | ``` func destinationForMixer(_ mixer: AVAudioNode, bus bus: AVAudioNodeBus) -> AVAudioMixingDestination? ``` |
| To | ``` func destination(forMixer mixer: AVAudioNode, bus bus: AVAudioNodeBus) -> AVAudioMixingDestination? ``` |

Modified [AVAudioMixingDestination](https://developer.apple.com/documentation/avfoundation/avaudiomixingdestination)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioMixingDestination : NSObject, AVAudioMixing {     var connectionPoint: AVAudioConnectionPoint { get } } ``` | AVAudioMixing |
| To | ``` class AVAudioMixingDestination : NSObject, AVAudioMixing {     var connectionPoint: AVAudioConnectionPoint { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioMixingDestination : CVarArg { } extension AVAudioMixingDestination : Equatable, Hashable {     var hashValue: Int { get } } ``` | AVAudioMixing, CVarArg, Equatable, Hashable |

Modified [AVAudioMixInputParameters](https://developer.apple.com/documentation/avfoundation/avaudiomixinputparameters)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioMixInputParameters : NSObject, NSCopying, NSMutableCopying {     var trackID: CMPersistentTrackID { get }     var audioTimePitchAlgorithm: String? { get }     var audioTapProcessor: MTAudioProcessingTap? { get }     func getVolumeRampForTime(_ time: CMTime, startVolume startVolume: UnsafeMutablePointer<Float>, endVolume endVolume: UnsafeMutablePointer<Float>, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool } ``` | NSCopying, NSMutableCopying |
| To | ``` class AVAudioMixInputParameters : NSObject, NSCopying, NSMutableCopying {     var trackID: CMPersistentTrackID { get }     var audioTimePitchAlgorithm: String? { get }     var audioTapProcessor: MTAudioProcessingTap? { get }     func getVolumeRamp(for time: CMTime, startVolume startVolume: UnsafeMutablePointer<Float>?, endVolume endVolume: UnsafeMutablePointer<Float>?, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioMixInputParameters : CVarArg { } extension AVAudioMixInputParameters : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSMutableCopying |

Modified [AVAudioMixInputParameters.getVolumeRamp(for: CMTime, startVolume: UnsafeMutablePointer<Float>?, endVolume: UnsafeMutablePointer<Float>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool](https://developer.apple.com/documentation/avfoundation/avaudiomixinputparameters/1389578-getvolumerampfortime)

|  | Declaration |
| --- | --- |
| From | ``` func getVolumeRampForTime(_ time: CMTime, startVolume startVolume: UnsafeMutablePointer<Float>, endVolume endVolume: UnsafeMutablePointer<Float>, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool ``` |
| To | ``` func getVolumeRamp(for time: CMTime, startVolume startVolume: UnsafeMutablePointer<Float>?, endVolume endVolume: UnsafeMutablePointer<Float>?, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool ``` |

Modified [AVAudioNode](https://developer.apple.com/documentation/avfoundation/avaudionode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioNode : NSObject {     func reset()     func inputFormatForBus(_ bus: AVAudioNodeBus) -> AVAudioFormat     func outputFormatForBus(_ bus: AVAudioNodeBus) -> AVAudioFormat     func nameForInputBus(_ bus: AVAudioNodeBus) -> String     func nameForOutputBus(_ bus: AVAudioNodeBus) -> String     func installTapOnBus(_ bus: AVAudioNodeBus, bufferSize bufferSize: AVAudioFrameCount, format format: AVAudioFormat?, block tapBlock: AVAudioNodeTapBlock)     func removeTapOnBus(_ bus: AVAudioNodeBus)     var engine: AVAudioEngine? { get }     var numberOfInputs: Int { get }     var numberOfOutputs: Int { get }     var lastRenderTime: AVAudioTime? { get } } ``` | -- |
| To | ``` class AVAudioNode : NSObject {     func reset()     func inputFormat(forBus bus: AVAudioNodeBus) -> AVAudioFormat     func outputFormat(forBus bus: AVAudioNodeBus) -> AVAudioFormat     func name(forInputBus bus: AVAudioNodeBus) -> String     func name(forOutputBus bus: AVAudioNodeBus) -> String     func installTap(onBus bus: AVAudioNodeBus, bufferSize bufferSize: AVAudioFrameCount, format format: AVAudioFormat?, block tapBlock: AVFoundation.AVAudioNodeTapBlock)     func removeTap(onBus bus: AVAudioNodeBus)     var engine: AVAudioEngine? { get }     var numberOfInputs: Int { get }     var numberOfOutputs: Int { get }     var lastRenderTime: AVAudioTime? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioNode : CVarArg { } extension AVAudioNode : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAudioNode.inputFormat(forBus: AVAudioNodeBus) -> AVAudioFormat](https://developer.apple.com/documentation/avfoundation/avaudionode/1390147-inputformat)

|  | Declaration |
| --- | --- |
| From | ``` func inputFormatForBus(_ bus: AVAudioNodeBus) -> AVAudioFormat ``` |
| To | ``` func inputFormat(forBus bus: AVAudioNodeBus) -> AVAudioFormat ``` |

Modified [AVAudioNode.installTap(onBus: AVAudioNodeBus, bufferSize: AVAudioFrameCount, format: AVAudioFormat?, block: AVFoundation.AVAudioNodeTapBlock)](https://developer.apple.com/documentation/avfoundation/avaudionode/1387122-installtap)

|  | Declaration |
| --- | --- |
| From | ``` func installTapOnBus(_ bus: AVAudioNodeBus, bufferSize bufferSize: AVAudioFrameCount, format format: AVAudioFormat?, block tapBlock: AVAudioNodeTapBlock) ``` |
| To | ``` func installTap(onBus bus: AVAudioNodeBus, bufferSize bufferSize: AVAudioFrameCount, format format: AVAudioFormat?, block tapBlock: AVFoundation.AVAudioNodeTapBlock) ``` |

Modified [AVAudioNode.name(forInputBus: AVAudioNodeBus) -> String](https://developer.apple.com/documentation/avfoundation/avaudionode/1387710-nameforinputbus)

|  | Declaration |
| --- | --- |
| From | ``` func nameForInputBus(_ bus: AVAudioNodeBus) -> String ``` |
| To | ``` func name(forInputBus bus: AVAudioNodeBus) -> String ``` |

Modified [AVAudioNode.name(forOutputBus: AVAudioNodeBus) -> String](https://developer.apple.com/documentation/avfoundation/avaudionode/1390811-name)

|  | Declaration |
| --- | --- |
| From | ``` func nameForOutputBus(_ bus: AVAudioNodeBus) -> String ``` |
| To | ``` func name(forOutputBus bus: AVAudioNodeBus) -> String ``` |

Modified [AVAudioNode.outputFormat(forBus: AVAudioNodeBus) -> AVAudioFormat](https://developer.apple.com/documentation/avfoundation/avaudionode/1389195-outputformat)

|  | Declaration |
| --- | --- |
| From | ``` func outputFormatForBus(_ bus: AVAudioNodeBus) -> AVAudioFormat ``` |
| To | ``` func outputFormat(forBus bus: AVAudioNodeBus) -> AVAudioFormat ``` |

Modified [AVAudioNode.removeTap(onBus: AVAudioNodeBus)](https://developer.apple.com/documentation/avfoundation/avaudionode/1388717-removetap)

|  | Declaration |
| --- | --- |
| From | ``` func removeTapOnBus(_ bus: AVAudioNodeBus) ``` |
| To | ``` func removeTap(onBus bus: AVAudioNodeBus) ``` |

Modified [AVAudioOutputNode](https://developer.apple.com/documentation/avfoundation/avaudiooutputnode)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioOutputNode : AVAudioIONode { } ``` |
| To | ``` class AVAudioOutputNode : AVAudioIONode {     init() } ``` |

Modified [AVAudioPCMBuffer](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioPCMBuffer : AVAudioBuffer {     init(PCMFormat format: AVAudioFormat, frameCapacity frameCapacity: AVAudioFrameCount)     var frameCapacity: AVAudioFrameCount { get }     var frameLength: AVAudioFrameCount     var stride: Int { get }     var floatChannelData: UnsafePointer<UnsafeMutablePointer<Float>> { get }     var int16ChannelData: UnsafePointer<UnsafeMutablePointer<Int16>> { get }     var int32ChannelData: UnsafePointer<UnsafeMutablePointer<Int32>> { get } } ``` |
| To | ``` class AVAudioPCMBuffer : AVAudioBuffer {     init(pcmFormat format: AVAudioFormat, frameCapacity frameCapacity: AVAudioFrameCount)     var frameCapacity: AVAudioFrameCount { get }     var frameLength: AVAudioFrameCount     var stride: Int { get }     var floatChannelData: UnsafePointer<UnsafeMutablePointer<Float>>? { get }     var int16ChannelData: UnsafePointer<UnsafeMutablePointer<Int16>>? { get }     var int32ChannelData: UnsafePointer<UnsafeMutablePointer<Int32>>? { get } } ``` |

Modified [AVAudioPCMBuffer.floatChannelData](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1386212-floatchanneldata)

|  | Declaration |
| --- | --- |
| From | ``` var floatChannelData: UnsafePointer<UnsafeMutablePointer<Float>> { get } ``` |
| To | ``` var floatChannelData: UnsafePointer<UnsafeMutablePointer<Float>>? { get } ``` |

Modified [AVAudioPCMBuffer.init(pcmFormat: AVAudioFormat, frameCapacity: AVAudioFrameCount)](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1389630-initwithpcmformat)

|  | Declaration |
| --- | --- |
| From | ``` init(PCMFormat format: AVAudioFormat, frameCapacity frameCapacity: AVAudioFrameCount) ``` |
| To | ``` init(pcmFormat format: AVAudioFormat, frameCapacity frameCapacity: AVAudioFrameCount) ``` |

Modified [AVAudioPCMBuffer.int16ChannelData](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1388925-int16channeldata)

|  | Declaration |
| --- | --- |
| From | ``` var int16ChannelData: UnsafePointer<UnsafeMutablePointer<Int16>> { get } ``` |
| To | ``` var int16ChannelData: UnsafePointer<UnsafeMutablePointer<Int16>>? { get } ``` |

Modified [AVAudioPCMBuffer.int32ChannelData](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1389756-int32channeldata)

|  | Declaration |
| --- | --- |
| From | ``` var int32ChannelData: UnsafePointer<UnsafeMutablePointer<Int32>> { get } ``` |
| To | ``` var int32ChannelData: UnsafePointer<UnsafeMutablePointer<Int32>>? { get } ``` |

Modified [AVAudioPlayer](https://developer.apple.com/documentation/avfoundation/avaudioplayer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioPlayer : NSObject {     init(contentsOfURL url: NSURL) throws     init(data data: NSData) throws     init(contentsOfURL url: NSURL, fileTypeHint utiString: String?) throws     init(data data: NSData, fileTypeHint utiString: String?) throws     func prepareToPlay() -> Bool     func play() -> Bool     func playAtTime(_ time: NSTimeInterval) -> Bool     func pause()     func stop()     var playing: Bool { get }     var numberOfChannels: Int { get }     var duration: NSTimeInterval { get }     unowned(unsafe) var delegate: AVAudioPlayerDelegate?     var url: NSURL? { get }     var data: NSData? { get }     var pan: Float     var volume: Float     var enableRate: Bool     var rate: Float     var currentTime: NSTimeInterval     var deviceCurrentTime: NSTimeInterval { get }     var numberOfLoops: Int     var settings: [String : AnyObject] { get }     var meteringEnabled: Bool     func updateMeters()     func peakPowerForChannel(_ channelNumber: Int) -> Float     func averagePowerForChannel(_ channelNumber: Int) -> Float     var channelAssignments: [NSNumber]? } ``` | -- |
| To | ``` class AVAudioPlayer : NSObject {     init(contentsOf url: URL) throws     init(data data: Data) throws     init(contentsOf url: URL, fileTypeHint utiString: String?) throws     init(data data: Data, fileTypeHint utiString: String?) throws     func prepareToPlay() -> Bool     func play() -> Bool     func play(atTime time: TimeInterval) -> Bool     func pause()     func stop()     var isPlaying: Bool { get }     var numberOfChannels: Int { get }     var duration: TimeInterval { get }     unowned(unsafe) var delegate: AVAudioPlayerDelegate?     var url: URL? { get }     var data: Data? { get }     var pan: Float     var volume: Float     func setVolume(_ volume: Float, fadeDuration duration: TimeInterval)     var enableRate: Bool     var rate: Float     var currentTime: TimeInterval     var deviceCurrentTime: TimeInterval { get }     var numberOfLoops: Int     var settings: [String : Any] { get }     var format: AVAudioFormat { get }     var isMeteringEnabled: Bool     func updateMeters()     func peakPower(forChannel channelNumber: Int) -> Float     func averagePower(forChannel channelNumber: Int) -> Float     var channelAssignments: [AVAudioSessionChannelDescription]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioPlayer : CVarArg { } extension AVAudioPlayer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAudioPlayer.averagePower(forChannel: Int) -> Float](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1390838-averagepowerforchannel)

|  | Declaration |
| --- | --- |
| From | ``` func averagePowerForChannel(_ channelNumber: Int) -> Float ``` |
| To | ``` func averagePower(forChannel channelNumber: Int) -> Float ``` |

Modified [AVAudioPlayer.channelAssignments](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1624038-channelassignments)

|  | Declaration |
| --- | --- |
| From | ``` var channelAssignments: [NSNumber]? ``` |
| To | ``` var channelAssignments: [AVAudioSessionChannelDescription]? ``` |

Modified [AVAudioPlayer.currentTime](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387297-currenttime)

|  | Declaration |
| --- | --- |
| From | ``` var currentTime: NSTimeInterval ``` |
| To | ``` var currentTime: TimeInterval ``` |

Modified [AVAudioPlayer.data](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389437-data)

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData? { get } ``` |
| To | ``` var data: Data? { get } ``` |

Modified [AVAudioPlayer.deviceCurrentTime](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387462-devicecurrenttime)

|  | Declaration |
| --- | --- |
| From | ``` var deviceCurrentTime: NSTimeInterval { get } ``` |
| To | ``` var deviceCurrentTime: TimeInterval { get } ``` |

Modified [AVAudioPlayer.duration](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388395-duration)

|  | Declaration |
| --- | --- |
| From | ``` var duration: NSTimeInterval { get } ``` |
| To | ``` var duration: TimeInterval { get } ``` |

Modified [AVAudioPlayer.init(contentsOf: URL) throws](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387281-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfURL url: NSURL) throws ``` |
| To | ``` init(contentsOf url: URL) throws ``` |

Modified [AVAudioPlayer.init(contentsOf: URL, fileTypeHint: String?) throws](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388349-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfURL url: NSURL, fileTypeHint utiString: String?) throws ``` |
| To | ``` init(contentsOf url: URL, fileTypeHint utiString: String?) throws ``` |

Modified [AVAudioPlayer.init(data: Data) throws](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388809-init)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData) throws ``` |
| To | ``` init(data data: Data) throws ``` |

Modified [AVAudioPlayer.init(data: Data, fileTypeHint: String?) throws](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388525-init)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData, fileTypeHint utiString: String?) throws ``` |
| To | ``` init(data data: Data, fileTypeHint utiString: String?) throws ``` |

Modified [AVAudioPlayer.isMeteringEnabled](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387935-meteringenabled)

|  | Declaration |
| --- | --- |
| From | ``` var meteringEnabled: Bool ``` |
| To | ``` var isMeteringEnabled: Bool ``` |

Modified [AVAudioPlayer.isPlaying](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1390139-playing)

|  | Declaration |
| --- | --- |
| From | ``` var playing: Bool { get } ``` |
| To | ``` var isPlaying: Bool { get } ``` |

Modified [AVAudioPlayer.peakPower(forChannel: Int) -> Float](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388509-peakpower)

|  | Declaration |
| --- | --- |
| From | ``` func peakPowerForChannel(_ channelNumber: Int) -> Float ``` |
| To | ``` func peakPower(forChannel channelNumber: Int) -> Float ``` |

Modified [AVAudioPlayer.play(atTime: TimeInterval) -> Bool](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389324-playattime)

|  | Declaration |
| --- | --- |
| From | ``` func playAtTime(_ time: NSTimeInterval) -> Bool ``` |
| To | ``` func play(atTime time: TimeInterval) -> Bool ``` |

Modified [AVAudioPlayer.settings](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389359-settings)

|  | Declaration |
| --- | --- |
| From | ``` var settings: [String : AnyObject] { get } ``` |
| To | ``` var settings: [String : Any] { get } ``` |

Modified [AVAudioPlayer.url](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387448-url)

|  | Declaration |
| --- | --- |
| From | ``` var url: NSURL? { get } ``` |
| To | ``` var url: URL? { get } ``` |

Modified [AVAudioPlayerDelegate](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVAudioPlayerDelegate : NSObjectProtocol {     optional func audioPlayerDidFinishPlaying(_ player: AVAudioPlayer, successfully flag: Bool)     optional func audioPlayerDecodeErrorDidOccur(_ player: AVAudioPlayer, error error: NSError?)     optional func audioPlayerBeginInterruption(_ player: AVAudioPlayer)     optional func audioPlayerEndInterruption(_ player: AVAudioPlayer, withOptions flags: Int)     optional func audioPlayerEndInterruption(_ player: AVAudioPlayer, withFlags flags: Int)     optional func audioPlayerEndInterruption(_ player: AVAudioPlayer) } ``` |
| To | ``` protocol AVAudioPlayerDelegate : NSObjectProtocol {     optional func audioPlayerDidFinishPlaying(_ player: AVAudioPlayer, successfully flag: Bool)     optional func audioPlayerDecodeErrorDidOccur(_ player: AVAudioPlayer, error error: Error?)     optional func audioPlayerBeginInterruption(_ player: AVAudioPlayer)     optional func audioPlayerEndInterruption(_ player: AVAudioPlayer, withOptions flags: Int)     optional func audioPlayerEndInterruption(_ player: AVAudioPlayer, withFlags flags: Int)     optional func audioPlayerEndInterruption(_ player: AVAudioPlayer) } ``` |

Modified [AVAudioPlayerDelegate.audioPlayerDecodeErrorDidOccur(_: AVAudioPlayer, error: Error?)](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1387676-audioplayerdecodeerrordidoccur)

|  | Declaration |
| --- | --- |
| From | ``` optional func audioPlayerDecodeErrorDidOccur(_ player: AVAudioPlayer, error error: NSError?) ``` |
| To | ``` optional func audioPlayerDecodeErrorDidOccur(_ player: AVAudioPlayer, error error: Error?) ``` |

Modified [AVAudioPlayerNode](https://developer.apple.com/documentation/avfoundation/avaudioplayernode)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioPlayerNode : AVAudioNode, AVAudioMixing {     func scheduleBuffer(_ buffer: AVAudioPCMBuffer, completionHandler completionHandler: AVAudioNodeCompletionHandler?)     func scheduleBuffer(_ buffer: AVAudioPCMBuffer, atTime when: AVAudioTime?, options options: AVAudioPlayerNodeBufferOptions, completionHandler completionHandler: AVAudioNodeCompletionHandler?)     func scheduleFile(_ file: AVAudioFile, atTime when: AVAudioTime?, completionHandler completionHandler: AVAudioNodeCompletionHandler?)     func scheduleSegment(_ file: AVAudioFile, startingFrame startFrame: AVAudioFramePosition, frameCount numberFrames: AVAudioFrameCount, atTime when: AVAudioTime?, completionHandler completionHandler: AVAudioNodeCompletionHandler?)     func stop()     func prepareWithFrameCount(_ frameCount: AVAudioFrameCount)     func play()     func playAtTime(_ when: AVAudioTime?)     func pause()     func nodeTimeForPlayerTime(_ playerTime: AVAudioTime) -> AVAudioTime?     func playerTimeForNodeTime(_ nodeTime: AVAudioTime) -> AVAudioTime?     var playing: Bool { get } } ``` |
| To | ``` class AVAudioPlayerNode : AVAudioNode, AVAudioMixing {     init()     func scheduleBuffer(_ buffer: AVAudioPCMBuffer, completionHandler completionHandler: AVFoundation.AVAudioNodeCompletionHandler? = nil)     func scheduleBuffer(_ buffer: AVAudioPCMBuffer, at when: AVAudioTime?, options options: AVAudioPlayerNodeBufferOptions = [], completionHandler completionHandler: AVFoundation.AVAudioNodeCompletionHandler? = nil)     func scheduleFile(_ file: AVAudioFile, at when: AVAudioTime?, completionHandler completionHandler: AVFoundation.AVAudioNodeCompletionHandler? = nil)     func scheduleSegment(_ file: AVAudioFile, startingFrame startFrame: AVAudioFramePosition, frameCount numberFrames: AVAudioFrameCount, at when: AVAudioTime?, completionHandler completionHandler: AVFoundation.AVAudioNodeCompletionHandler? = nil)     func stop()     func prepare(withFrameCount frameCount: AVAudioFrameCount)     func play()     func play(at when: AVAudioTime?)     func pause()     func nodeTime(forPlayerTime playerTime: AVAudioTime) -> AVAudioTime?     func playerTime(forNodeTime nodeTime: AVAudioTime) -> AVAudioTime?     var isPlaying: Bool { get } } ``` |

Modified [AVAudioPlayerNode.isPlaying](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1390631-isplaying)

|  | Declaration |
| --- | --- |
| From | ``` var playing: Bool { get } ``` |
| To | ``` var isPlaying: Bool { get } ``` |

Modified [AVAudioPlayerNode.nodeTime(forPlayerTime: AVAudioTime) -> AVAudioTime?](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1386450-nodetimeforplayertime)

|  | Declaration |
| --- | --- |
| From | ``` func nodeTimeForPlayerTime(_ playerTime: AVAudioTime) -> AVAudioTime? ``` |
| To | ``` func nodeTime(forPlayerTime playerTime: AVAudioTime) -> AVAudioTime? ``` |

Modified [AVAudioPlayerNode.play(at: AVAudioTime?)](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1389304-play)

|  | Declaration |
| --- | --- |
| From | ``` func playAtTime(_ when: AVAudioTime?) ``` |
| To | ``` func play(at when: AVAudioTime?) ``` |

Modified [AVAudioPlayerNode.playerTime(forNodeTime: AVAudioTime) -> AVAudioTime?](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1390449-playertime)

|  | Declaration |
| --- | --- |
| From | ``` func playerTimeForNodeTime(_ nodeTime: AVAudioTime) -> AVAudioTime? ``` |
| To | ``` func playerTime(forNodeTime nodeTime: AVAudioTime) -> AVAudioTime? ``` |

Modified [AVAudioPlayerNode.prepare(withFrameCount: AVAudioFrameCount)](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1388511-prepare)

|  | Declaration |
| --- | --- |
| From | ``` func prepareWithFrameCount(_ frameCount: AVAudioFrameCount) ``` |
| To | ``` func prepare(withFrameCount frameCount: AVAudioFrameCount) ``` |

Modified [AVAudioPlayerNode.scheduleBuffer(_: AVAudioPCMBuffer, at: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionHandler: AVFoundation.AVAudioNodeCompletionHandler?)](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1388422-schedulebuffer)

|  | Declaration |
| --- | --- |
| From | ``` func scheduleBuffer(_ buffer: AVAudioPCMBuffer, atTime when: AVAudioTime?, options options: AVAudioPlayerNodeBufferOptions, completionHandler completionHandler: AVAudioNodeCompletionHandler?) ``` |
| To | ``` func scheduleBuffer(_ buffer: AVAudioPCMBuffer, at when: AVAudioTime?, options options: AVAudioPlayerNodeBufferOptions = [], completionHandler completionHandler: AVFoundation.AVAudioNodeCompletionHandler? = nil) ``` |

Modified [AVAudioPlayerNode.scheduleBuffer(_: AVAudioPCMBuffer, completionHandler: AVFoundation.AVAudioNodeCompletionHandler?)](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1389996-schedulebuffer)

|  | Declaration |
| --- | --- |
| From | ``` func scheduleBuffer(_ buffer: AVAudioPCMBuffer, completionHandler completionHandler: AVAudioNodeCompletionHandler?) ``` |
| To | ``` func scheduleBuffer(_ buffer: AVAudioPCMBuffer, completionHandler completionHandler: AVFoundation.AVAudioNodeCompletionHandler? = nil) ``` |

Modified [AVAudioPlayerNode.scheduleFile(_: AVAudioFile, at: AVAudioTime?, completionHandler: AVFoundation.AVAudioNodeCompletionHandler?)](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1390047-schedulefile)

|  | Declaration |
| --- | --- |
| From | ``` func scheduleFile(_ file: AVAudioFile, atTime when: AVAudioTime?, completionHandler completionHandler: AVAudioNodeCompletionHandler?) ``` |
| To | ``` func scheduleFile(_ file: AVAudioFile, at when: AVAudioTime?, completionHandler completionHandler: AVFoundation.AVAudioNodeCompletionHandler? = nil) ``` |

Modified [AVAudioPlayerNode.scheduleSegment(_: AVAudioFile, startingFrame: AVAudioFramePosition, frameCount: AVAudioFrameCount, at: AVAudioTime?, completionHandler: AVFoundation.AVAudioNodeCompletionHandler?)](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1385884-schedulesegment)

|  | Declaration |
| --- | --- |
| From | ``` func scheduleSegment(_ file: AVAudioFile, startingFrame startFrame: AVAudioFramePosition, frameCount numberFrames: AVAudioFrameCount, atTime when: AVAudioTime?, completionHandler completionHandler: AVAudioNodeCompletionHandler?) ``` |
| To | ``` func scheduleSegment(_ file: AVAudioFile, startingFrame startFrame: AVAudioFramePosition, frameCount numberFrames: AVAudioFrameCount, at when: AVAudioTime?, completionHandler completionHandler: AVFoundation.AVAudioNodeCompletionHandler? = nil) ``` |

Modified [AVAudioPlayerNodeBufferOptions [struct]](https://developer.apple.com/documentation/avfoundation/avaudioplayernodebufferoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVAudioPlayerNodeBufferOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var Loops: AVAudioPlayerNodeBufferOptions { get }     static var Interrupts: AVAudioPlayerNodeBufferOptions { get }     static var InterruptsAtLoop: AVAudioPlayerNodeBufferOptions { get } } ``` | OptionSetType |
| To | ``` struct AVAudioPlayerNodeBufferOptions : OptionSet {     init(rawValue rawValue: UInt)     static var loops: AVAudioPlayerNodeBufferOptions { get }     static var interrupts: AVAudioPlayerNodeBufferOptions { get }     static var interruptsAtLoop: AVAudioPlayerNodeBufferOptions { get }     func intersect(_ other: AVAudioPlayerNodeBufferOptions) -> AVAudioPlayerNodeBufferOptions     func exclusiveOr(_ other: AVAudioPlayerNodeBufferOptions) -> AVAudioPlayerNodeBufferOptions     mutating func unionInPlace(_ other: AVAudioPlayerNodeBufferOptions)     mutating func intersectInPlace(_ other: AVAudioPlayerNodeBufferOptions)     mutating func exclusiveOrInPlace(_ other: AVAudioPlayerNodeBufferOptions)     func isSubsetOf(_ other: AVAudioPlayerNodeBufferOptions) -> Bool     func isDisjointWith(_ other: AVAudioPlayerNodeBufferOptions) -> Bool     func isSupersetOf(_ other: AVAudioPlayerNodeBufferOptions) -> Bool     mutating func subtractInPlace(_ other: AVAudioPlayerNodeBufferOptions)     func isStrictSupersetOf(_ other: AVAudioPlayerNodeBufferOptions) -> Bool     func isStrictSubsetOf(_ other: AVAudioPlayerNodeBufferOptions) -> Bool } extension AVAudioPlayerNodeBufferOptions {     func union(_ other: AVAudioPlayerNodeBufferOptions) -> AVAudioPlayerNodeBufferOptions     func intersection(_ other: AVAudioPlayerNodeBufferOptions) -> AVAudioPlayerNodeBufferOptions     func symmetricDifference(_ other: AVAudioPlayerNodeBufferOptions) -> AVAudioPlayerNodeBufferOptions } extension AVAudioPlayerNodeBufferOptions {     func contains(_ member: AVAudioPlayerNodeBufferOptions) -> Bool     mutating func insert(_ newMember: AVAudioPlayerNodeBufferOptions) -> (inserted: Bool, memberAfterInsert: AVAudioPlayerNodeBufferOptions)     mutating func remove(_ member: AVAudioPlayerNodeBufferOptions) -> AVAudioPlayerNodeBufferOptions?     mutating func update(with newMember: AVAudioPlayerNodeBufferOptions) -> AVAudioPlayerNodeBufferOptions? } extension AVAudioPlayerNodeBufferOptions {     convenience init()     mutating func formUnion(_ other: AVAudioPlayerNodeBufferOptions)     mutating func formIntersection(_ other: AVAudioPlayerNodeBufferOptions)     mutating func formSymmetricDifference(_ other: AVAudioPlayerNodeBufferOptions) } extension AVAudioPlayerNodeBufferOptions {     convenience init<S : Sequence where S.Iterator.Element == AVAudioPlayerNodeBufferOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AVAudioPlayerNodeBufferOptions...)     mutating func subtract(_ other: AVAudioPlayerNodeBufferOptions)     func isSubset(of other: AVAudioPlayerNodeBufferOptions) -> Bool     func isSuperset(of other: AVAudioPlayerNodeBufferOptions) -> Bool     func isDisjoint(with other: AVAudioPlayerNodeBufferOptions) -> Bool     func subtracting(_ other: AVAudioPlayerNodeBufferOptions) -> AVAudioPlayerNodeBufferOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: AVAudioPlayerNodeBufferOptions) -> Bool     func isStrictSubset(of other: AVAudioPlayerNodeBufferOptions) -> Bool } ``` | OptionSet |

Modified [AVAudioPlayerNodeBufferOptions.interrupts](https://developer.apple.com/documentation/avfoundation/avaudioplayernodebufferoptions/1387416-interrupts)

|  | Declaration |
| --- | --- |
| From | ``` static var Interrupts: AVAudioPlayerNodeBufferOptions { get } ``` |
| To | ``` static var interrupts: AVAudioPlayerNodeBufferOptions { get } ``` |

Modified [AVAudioPlayerNodeBufferOptions.interruptsAtLoop](https://developer.apple.com/documentation/avfoundation/avaudioplayernodebufferoptions/1385595-interruptsatloop)

|  | Declaration |
| --- | --- |
| From | ``` static var InterruptsAtLoop: AVAudioPlayerNodeBufferOptions { get } ``` |
| To | ``` static var interruptsAtLoop: AVAudioPlayerNodeBufferOptions { get } ``` |

Modified [AVAudioPlayerNodeBufferOptions.loops](https://developer.apple.com/documentation/avfoundation/avaudioplayernodebufferoptions/1388143-loops)

|  | Declaration |
| --- | --- |
| From | ``` static var Loops: AVAudioPlayerNodeBufferOptions { get } ``` |
| To | ``` static var loops: AVAudioPlayerNodeBufferOptions { get } ``` |

Modified [AVAudioQuality [enum]](https://developer.apple.com/documentation/avfoundation/avaudioquality)

|  | Declaration |
| --- | --- |
| From | ``` enum AVAudioQuality : Int {     case Min     case Low     case Medium     case High     case Max } ``` |
| To | ``` enum AVAudioQuality : Int {     case min     case low     case medium     case high     case max } ``` |

Modified [AVAudioQuality.high](https://developer.apple.com/documentation/avfoundation/avaudioquality/high)

|  | Declaration |
| --- | --- |
| From | ``` case High ``` |
| To | ``` case high ``` |

Modified [AVAudioQuality.low](https://developer.apple.com/documentation/avfoundation/avaudioquality/avaudioqualitylow)

|  | Declaration |
| --- | --- |
| From | ``` case Low ``` |
| To | ``` case low ``` |

Modified [AVAudioQuality.max](https://developer.apple.com/documentation/avfoundation/avaudioquality/max)

|  | Declaration |
| --- | --- |
| From | ``` case Max ``` |
| To | ``` case max ``` |

Modified [AVAudioQuality.medium](https://developer.apple.com/documentation/avfoundation/avaudioquality/avaudioqualitymedium)

|  | Declaration |
| --- | --- |
| From | ``` case Medium ``` |
| To | ``` case medium ``` |

Modified [AVAudioQuality.min](https://developer.apple.com/documentation/avfoundation/avaudioquality/min)

|  | Declaration |
| --- | --- |
| From | ``` case Min ``` |
| To | ``` case min ``` |

Modified [AVAudioSequencer](https://developer.apple.com/documentation/avfoundation/avaudiosequencer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioSequencer : NSObject {     init()     init(audioEngine engine: AVAudioEngine)     func loadFromURL(_ fileURL: NSURL, options options: AVMusicSequenceLoadOptions) throws     func loadFromData(_ data: NSData, options options: AVMusicSequenceLoadOptions) throws     func writeToURL(_ fileURL: NSURL, SMPTEResolution resolution: Int, replaceExisting replace: Bool) throws     func dataWithSMPTEResolution(_ SMPTEResolution: Int, error outError: NSErrorPointer) -> NSData     func secondsForBeats(_ beats: AVMusicTimeStamp) -> NSTimeInterval     func beatsForSeconds(_ seconds: NSTimeInterval) -> AVMusicTimeStamp     var tracks: [AVMusicTrack] { get }     var tempoTrack: AVMusicTrack { get }     var userInfo: [String : AnyObject] { get } } extension AVAudioSequencer {     var currentPositionInSeconds: NSTimeInterval     var currentPositionInBeats: NSTimeInterval     var playing: Bool { get }     var rate: Float     func hostTimeForBeats(_ inBeats: AVMusicTimeStamp, error outError: NSErrorPointer) -> UInt64     func beatsForHostTime(_ inHostTime: UInt64, error outError: NSErrorPointer) -> AVMusicTimeStamp     func prepareToPlay()     func start() throws     func stop() } ``` | -- |
| To | ``` class AVAudioSequencer : NSObject {     init()     init(audioEngine engine: AVAudioEngine)     func load(from fileURL: URL, options options: AVMusicSequenceLoadOptions = []) throws     func load(from data: Data, options options: AVMusicSequenceLoadOptions = []) throws     func write(to fileURL: URL, smpteResolution resolution: Int, replaceExisting replace: Bool) throws     func data(withSMPTEResolution SMPTEResolution: Int, error outError: NSErrorPointer) -> Data     func seconds(forBeats beats: AVMusicTimeStamp) -> TimeInterval     func beats(forSeconds seconds: TimeInterval) -> AVMusicTimeStamp     var tracks: [AVMusicTrack] { get }     var tempoTrack: AVMusicTrack { get }     var userInfo: [String : Any] { get }     var currentPositionInSeconds: TimeInterval     var currentPositionInBeats: TimeInterval     var isPlaying: Bool { get }     var rate: Float     func hostTime(forBeats inBeats: AVMusicTimeStamp, error outError: NSErrorPointer) -> UInt64     func beats(forHostTime inHostTime: UInt64, error outError: NSErrorPointer) -> AVMusicTimeStamp     func prepareToPlay()     func start() throws     func stop()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioSequencer : CVarArg { } extension AVAudioSequencer : Equatable, Hashable {     var hashValue: Int { get } } extension AVAudioSequencer {     var currentPositionInSeconds: TimeInterval     var currentPositionInBeats: TimeInterval     var isPlaying: Bool { get }     var rate: Float     func hostTime(forBeats inBeats: AVMusicTimeStamp, error outError: NSErrorPointer) -> UInt64     func beats(forHostTime inHostTime: UInt64, error outError: NSErrorPointer) -> AVMusicTimeStamp     func prepareToPlay()     func start() throws     func stop() } ``` | CVarArg, Equatable, Hashable |

Modified [AVAudioSequencer.beats(forHostTime: UInt64, error: NSErrorPointer) -> AVMusicTimeStamp](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1389012-beatsforhosttime)

|  | Declaration |
| --- | --- |
| From | ``` func beatsForHostTime(_ inHostTime: UInt64, error outError: NSErrorPointer) -> AVMusicTimeStamp ``` |
| To | ``` func beats(forHostTime inHostTime: UInt64, error outError: NSErrorPointer) -> AVMusicTimeStamp ``` |

Modified [AVAudioSequencer.beats(forSeconds: TimeInterval) -> AVMusicTimeStamp](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387853-beats)

|  | Declaration |
| --- | --- |
| From | ``` func beatsForSeconds(_ seconds: NSTimeInterval) -> AVMusicTimeStamp ``` |
| To | ``` func beats(forSeconds seconds: TimeInterval) -> AVMusicTimeStamp ``` |

Modified [AVAudioSequencer.currentPositionInBeats](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388910-currentpositioninbeats)

|  | Declaration |
| --- | --- |
| From | ``` var currentPositionInBeats: NSTimeInterval ``` |
| To | ``` var currentPositionInBeats: TimeInterval ``` |

Modified [AVAudioSequencer.currentPositionInSeconds](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1390524-currentpositioninseconds)

|  | Declaration |
| --- | --- |
| From | ``` var currentPositionInSeconds: NSTimeInterval ``` |
| To | ``` var currentPositionInSeconds: TimeInterval ``` |

Modified [AVAudioSequencer.data(withSMPTEResolution: Int, error: NSErrorPointer) -> Data](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388701-datawithsmpteresolution)

|  | Declaration |
| --- | --- |
| From | ``` func dataWithSMPTEResolution(_ SMPTEResolution: Int, error outError: NSErrorPointer) -> NSData ``` |
| To | ``` func data(withSMPTEResolution SMPTEResolution: Int, error outError: NSErrorPointer) -> Data ``` |

Modified [AVAudioSequencer.hostTime(forBeats: AVMusicTimeStamp, error: NSErrorPointer) -> UInt64](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1386184-hosttime)

|  | Declaration |
| --- | --- |
| From | ``` func hostTimeForBeats(_ inBeats: AVMusicTimeStamp, error outError: NSErrorPointer) -> UInt64 ``` |
| To | ``` func hostTime(forBeats inBeats: AVMusicTimeStamp, error outError: NSErrorPointer) -> UInt64 ``` |

Modified [AVAudioSequencer.isPlaying](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388402-playing)

|  | Declaration |
| --- | --- |
| From | ``` var playing: Bool { get } ``` |
| To | ``` var isPlaying: Bool { get } ``` |

Modified [AVAudioSequencer.load(from: URL, options: AVMusicSequenceLoadOptions) throws](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1386241-loadfromurl)

|  | Declaration |
| --- | --- |
| From | ``` func loadFromURL(_ fileURL: NSURL, options options: AVMusicSequenceLoadOptions) throws ``` |
| To | ``` func load(from fileURL: URL, options options: AVMusicSequenceLoadOptions = []) throws ``` |

Modified [AVAudioSequencer.load(from: Data, options: AVMusicSequenceLoadOptions) throws](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1389720-loadfromdata)

|  | Declaration |
| --- | --- |
| From | ``` func loadFromData(_ data: NSData, options options: AVMusicSequenceLoadOptions) throws ``` |
| To | ``` func load(from data: Data, options options: AVMusicSequenceLoadOptions = []) throws ``` |

Modified [AVAudioSequencer.seconds(forBeats: AVMusicTimeStamp) -> TimeInterval](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387615-seconds)

|  | Declaration |
| --- | --- |
| From | ``` func secondsForBeats(_ beats: AVMusicTimeStamp) -> NSTimeInterval ``` |
| To | ``` func seconds(forBeats beats: AVMusicTimeStamp) -> TimeInterval ``` |

Modified [AVAudioSequencer.userInfo](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1389262-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [String : AnyObject] { get } ``` |
| To | ``` var userInfo: [String : Any] { get } ``` |

Modified [AVAudioSequencer.write(to: URL, smpteResolution: Int, replaceExisting: Bool) throws](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1390589-write)

|  | Declaration |
| --- | --- |
| From | ``` func writeToURL(_ fileURL: NSURL, SMPTEResolution resolution: Int, replaceExisting replace: Bool) throws ``` |
| To | ``` func write(to fileURL: URL, smpteResolution resolution: Int, replaceExisting replace: Bool) throws ``` |

Modified [AVAudioSession](https://developer.apple.com/documentation/avfoundation/avaudiosession)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioSession : NSObject {     class func sharedInstance() -> AVAudioSession     func setActive(_ active: Bool) throws     func setActive(_ active: Bool, withOptions options: AVAudioSessionSetActiveOptions) throws     var availableCategories: [String] { get }     func setCategory(_ category: String) throws     func setCategory(_ category: String, withOptions options: AVAudioSessionCategoryOptions) throws     var category: String { get }     func recordPermission() -> AVAudioSessionRecordPermission     func requestRecordPermission(_ response: PermissionBlock)     var categoryOptions: AVAudioSessionCategoryOptions { get }     var availableModes: [String] { get }     func setMode(_ mode: String) throws     var mode: String { get }     func overrideOutputAudioPort(_ portOverride: AVAudioSessionPortOverride) throws     var otherAudioPlaying: Bool { get }     var secondaryAudioShouldBeSilencedHint: Bool { get }     var currentRoute: AVAudioSessionRouteDescription { get }     func setPreferredInput(_ inPort: AVAudioSessionPortDescription?) throws     var preferredInput: AVAudioSessionPortDescription? { get }     var availableInputs: [AVAudioSessionPortDescription]? { get } } extension AVAudioSession {     func setPreferredSampleRate(_ sampleRate: Double) throws     var preferredSampleRate: Double { get }     func setPreferredIOBufferDuration(_ duration: NSTimeInterval) throws     var preferredIOBufferDuration: NSTimeInterval { get }     func setPreferredInputNumberOfChannels(_ count: Int) throws     var preferredInputNumberOfChannels: Int { get }     func setPreferredOutputNumberOfChannels(_ count: Int) throws     var preferredOutputNumberOfChannels: Int { get }     var maximumInputNumberOfChannels: Int { get }     var maximumOutputNumberOfChannels: Int { get }     func setInputGain(_ gain: Float) throws     var inputGain: Float { get }     var inputGainSettable: Bool { get }     var inputAvailable: Bool { get }     var inputDataSources: [AVAudioSessionDataSourceDescription]? { get }     var inputDataSource: AVAudioSessionDataSourceDescription? { get }     func setInputDataSource(_ dataSource: AVAudioSessionDataSourceDescription?) throws     var outputDataSources: [AVAudioSessionDataSourceDescription]? { get }     var outputDataSource: AVAudioSessionDataSourceDescription? { get }     func setOutputDataSource(_ dataSource: AVAudioSessionDataSourceDescription?) throws     var sampleRate: Double { get }     var inputNumberOfChannels: Int { get }     var outputNumberOfChannels: Int { get }     var outputVolume: Float { get }     var inputLatency: NSTimeInterval { get }     var outputLatency: NSTimeInterval { get }     var IOBufferDuration: NSTimeInterval { get } } extension AVAudioSession {     unowned(unsafe) var delegate: AVAudioSessionDelegate?     func setActive(_ active: Bool, withFlags flags: Int) throws     var inputIsAvailable: Bool { get }     var currentHardwareSampleRate: Double { get }     var currentHardwareInputNumberOfChannels: Int { get }     var currentHardwareOutputNumberOfChannels: Int { get }     func setPreferredHardwareSampleRate(_ sampleRate: Double) throws     var preferredHardwareSampleRate: Double { get } } ``` | -- |
| To | ``` class AVAudioSession : NSObject {     class func sharedInstance() -> AVAudioSession     func setActive(_ active: Bool) throws     func setActive(_ active: Bool, with options: AVAudioSessionSetActiveOptions = []) throws     var availableCategories: [String] { get }     func setCategory(_ category: String) throws     func setCategory(_ category: String, with options: AVAudioSessionCategoryOptions = []) throws     func setCategory(_ category: String, mode mode: String, options options: AVAudioSessionCategoryOptions = []) throws     var category: String { get }     func recordPermission() -> AVAudioSessionRecordPermission     func requestRecordPermission(_ response: AVFoundation.PermissionBlock)     var categoryOptions: AVAudioSessionCategoryOptions { get }     var availableModes: [String] { get }     func setMode(_ mode: String) throws     var mode: String { get }     func overrideOutputAudioPort(_ portOverride: AVAudioSessionPortOverride) throws     var isOtherAudioPlaying: Bool { get }     var secondaryAudioShouldBeSilencedHint: Bool { get }     var currentRoute: AVAudioSessionRouteDescription { get }     func setPreferredInput(_ inPort: AVAudioSessionPortDescription?) throws     var preferredInput: AVAudioSessionPortDescription? { get }     var availableInputs: [AVAudioSessionPortDescription]? { get }     unowned(unsafe) var delegate: AVAudioSessionDelegate?     func setActive(_ active: Bool, withFlags flags: Int) throws     var inputIsAvailable: Bool { get }     var currentHardwareSampleRate: Double { get }     var currentHardwareInputNumberOfChannels: Int { get }     var currentHardwareOutputNumberOfChannels: Int { get }     func setPreferredHardwareSampleRate(_ sampleRate: Double) throws     var preferredHardwareSampleRate: Double { get }     func setPreferredSampleRate(_ sampleRate: Double) throws     var preferredSampleRate: Double { get }     func setPreferredIOBufferDuration(_ duration: TimeInterval) throws     var preferredIOBufferDuration: TimeInterval { get }     func setPreferredInputNumberOfChannels(_ count: Int) throws     var preferredInputNumberOfChannels: Int { get }     func setPreferredOutputNumberOfChannels(_ count: Int) throws     var preferredOutputNumberOfChannels: Int { get }     var maximumInputNumberOfChannels: Int { get }     var maximumOutputNumberOfChannels: Int { get }     func setInputGain(_ gain: Float) throws     var inputGain: Float { get }     var isInputGainSettable: Bool { get }     var isInputAvailable: Bool { get }     var inputDataSources: [AVAudioSessionDataSourceDescription]? { get }     var inputDataSource: AVAudioSessionDataSourceDescription? { get }     func setInputDataSource(_ dataSource: AVAudioSessionDataSourceDescription?) throws     var outputDataSources: [AVAudioSessionDataSourceDescription]? { get }     var outputDataSource: AVAudioSessionDataSourceDescription? { get }     func setOutputDataSource(_ dataSource: AVAudioSessionDataSourceDescription?) throws     var sampleRate: Double { get }     var inputNumberOfChannels: Int { get }     var outputNumberOfChannels: Int { get }     var outputVolume: Float { get }     var inputLatency: TimeInterval { get }     var outputLatency: TimeInterval { get }     var ioBufferDuration: TimeInterval { get }     func setAggregatedIOPreference(_ inIOType: AVAudioSessionIOType) throws     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioSession : CVarArg { } extension AVAudioSession : Equatable, Hashable {     var hashValue: Int { get } } extension AVAudioSession {     func setPreferredSampleRate(_ sampleRate: Double) throws     var preferredSampleRate: Double { get }     func setPreferredIOBufferDuration(_ duration: TimeInterval) throws     var preferredIOBufferDuration: TimeInterval { get }     func setPreferredInputNumberOfChannels(_ count: Int) throws     var preferredInputNumberOfChannels: Int { get }     func setPreferredOutputNumberOfChannels(_ count: Int) throws     var preferredOutputNumberOfChannels: Int { get }     var maximumInputNumberOfChannels: Int { get }     var maximumOutputNumberOfChannels: Int { get }     func setInputGain(_ gain: Float) throws     var inputGain: Float { get }     var isInputGainSettable: Bool { get }     var isInputAvailable: Bool { get }     var inputDataSources: [AVAudioSessionDataSourceDescription]? { get }     var inputDataSource: AVAudioSessionDataSourceDescription? { get }     func setInputDataSource(_ dataSource: AVAudioSessionDataSourceDescription?) throws     var outputDataSources: [AVAudioSessionDataSourceDescription]? { get }     var outputDataSource: AVAudioSessionDataSourceDescription? { get }     func setOutputDataSource(_ dataSource: AVAudioSessionDataSourceDescription?) throws     var sampleRate: Double { get }     var inputNumberOfChannels: Int { get }     var outputNumberOfChannels: Int { get }     var outputVolume: Float { get }     var inputLatency: TimeInterval { get }     var outputLatency: TimeInterval { get }     var ioBufferDuration: TimeInterval { get }     func setAggregatedIOPreference(_ inIOType: AVAudioSessionIOType) throws } extension AVAudioSession {     unowned(unsafe) var delegate: AVAudioSessionDelegate?     func setActive(_ active: Bool, withFlags flags: Int) throws     var inputIsAvailable: Bool { get }     var currentHardwareSampleRate: Double { get }     var currentHardwareInputNumberOfChannels: Int { get }     var currentHardwareOutputNumberOfChannels: Int { get }     func setPreferredHardwareSampleRate(_ sampleRate: Double) throws     var preferredHardwareSampleRate: Double { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAudioSession.inputLatency](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616537-inputlatency)

|  | Declaration |
| --- | --- |
| From | ``` var inputLatency: NSTimeInterval { get } ``` |
| To | ``` var inputLatency: TimeInterval { get } ``` |

Modified [AVAudioSession.ioBufferDuration](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616498-iobufferduration)

|  | Declaration |
| --- | --- |
| From | ``` var IOBufferDuration: NSTimeInterval { get } ``` |
| To | ``` var ioBufferDuration: TimeInterval { get } ``` |

Modified [AVAudioSession.isInputAvailable](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616524-isinputavailable)

|  | Declaration |
| --- | --- |
| From | ``` var inputAvailable: Bool { get } ``` |
| To | ``` var isInputAvailable: Bool { get } ``` |

Modified [AVAudioSession.isInputGainSettable](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616502-isinputgainsettable)

|  | Declaration |
| --- | --- |
| From | ``` var inputGainSettable: Bool { get } ``` |
| To | ``` var isInputGainSettable: Bool { get } ``` |

Modified [AVAudioSession.isOtherAudioPlaying](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616610-isotheraudioplaying)

|  | Declaration |
| --- | --- |
| From | ``` var otherAudioPlaying: Bool { get } ``` |
| To | ``` var isOtherAudioPlaying: Bool { get } ``` |

Modified [AVAudioSession.outputLatency](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616500-outputlatency)

|  | Declaration |
| --- | --- |
| From | ``` var outputLatency: NSTimeInterval { get } ``` |
| To | ``` var outputLatency: TimeInterval { get } ``` |

Modified [AVAudioSession.preferredIOBufferDuration](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616464-preferrediobufferduration)

|  | Declaration |
| --- | --- |
| From | ``` var preferredIOBufferDuration: NSTimeInterval { get } ``` |
| To | ``` var preferredIOBufferDuration: TimeInterval { get } ``` |

Modified [AVAudioSession.setActive(_: Bool, with: AVAudioSessionSetActiveOptions) throws](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616627-setactive)

|  | Declaration |
| --- | --- |
| From | ``` func setActive(_ active: Bool, withOptions options: AVAudioSessionSetActiveOptions) throws ``` |
| To | ``` func setActive(_ active: Bool, with options: AVAudioSessionSetActiveOptions = []) throws ``` |

Modified [AVAudioSession.setCategory(_: String, with: AVAudioSessionCategoryOptions) throws](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616442-setcategory)

|  | Declaration |
| --- | --- |
| From | ``` func setCategory(_ category: String, withOptions options: AVAudioSessionCategoryOptions) throws ``` |
| To | ``` func setCategory(_ category: String, with options: AVAudioSessionCategoryOptions = []) throws ``` |

Modified [AVAudioSession.setPreferredIOBufferDuration(_: TimeInterval) throws](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616589-setpreferrediobufferduration)

|  | Declaration |
| --- | --- |
| From | ``` func setPreferredIOBufferDuration(_ duration: NSTimeInterval) throws ``` |
| To | ``` func setPreferredIOBufferDuration(_ duration: TimeInterval) throws ``` |

Modified [AVAudioSessionCategoryOptions [struct]](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVAudioSessionCategoryOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var MixWithOthers: AVAudioSessionCategoryOptions { get }     static var DuckOthers: AVAudioSessionCategoryOptions { get }     static var AllowBluetooth: AVAudioSessionCategoryOptions { get }     static var DefaultToSpeaker: AVAudioSessionCategoryOptions { get }     static var InterruptSpokenAudioAndMixWithOthers: AVAudioSessionCategoryOptions { get } } ``` | OptionSetType |
| To | ``` struct AVAudioSessionCategoryOptions : OptionSet {     init(rawValue rawValue: UInt)     static var mixWithOthers: AVAudioSessionCategoryOptions { get }     static var duckOthers: AVAudioSessionCategoryOptions { get }     static var allowBluetooth: AVAudioSessionCategoryOptions { get }     static var defaultToSpeaker: AVAudioSessionCategoryOptions { get }     static var interruptSpokenAudioAndMixWithOthers: AVAudioSessionCategoryOptions { get }     static var allowBluetoothA2DP: AVAudioSessionCategoryOptions { get }     static var allowAirPlay: AVAudioSessionCategoryOptions { get }     func intersect(_ other: AVAudioSessionCategoryOptions) -> AVAudioSessionCategoryOptions     func exclusiveOr(_ other: AVAudioSessionCategoryOptions) -> AVAudioSessionCategoryOptions     mutating func unionInPlace(_ other: AVAudioSessionCategoryOptions)     mutating func intersectInPlace(_ other: AVAudioSessionCategoryOptions)     mutating func exclusiveOrInPlace(_ other: AVAudioSessionCategoryOptions)     func isSubsetOf(_ other: AVAudioSessionCategoryOptions) -> Bool     func isDisjointWith(_ other: AVAudioSessionCategoryOptions) -> Bool     func isSupersetOf(_ other: AVAudioSessionCategoryOptions) -> Bool     mutating func subtractInPlace(_ other: AVAudioSessionCategoryOptions)     func isStrictSupersetOf(_ other: AVAudioSessionCategoryOptions) -> Bool     func isStrictSubsetOf(_ other: AVAudioSessionCategoryOptions) -> Bool } extension AVAudioSessionCategoryOptions {     func union(_ other: AVAudioSessionCategoryOptions) -> AVAudioSessionCategoryOptions     func intersection(_ other: AVAudioSessionCategoryOptions) -> AVAudioSessionCategoryOptions     func symmetricDifference(_ other: AVAudioSessionCategoryOptions) -> AVAudioSessionCategoryOptions } extension AVAudioSessionCategoryOptions {     func contains(_ member: AVAudioSessionCategoryOptions) -> Bool     mutating func insert(_ newMember: AVAudioSessionCategoryOptions) -> (inserted: Bool, memberAfterInsert: AVAudioSessionCategoryOptions)     mutating func remove(_ member: AVAudioSessionCategoryOptions) -> AVAudioSessionCategoryOptions?     mutating func update(with newMember: AVAudioSessionCategoryOptions) -> AVAudioSessionCategoryOptions? } extension AVAudioSessionCategoryOptions {     convenience init()     mutating func formUnion(_ other: AVAudioSessionCategoryOptions)     mutating func formIntersection(_ other: AVAudioSessionCategoryOptions)     mutating func formSymmetricDifference(_ other: AVAudioSessionCategoryOptions) } extension AVAudioSessionCategoryOptions {     convenience init<S : Sequence where S.Iterator.Element == AVAudioSessionCategoryOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AVAudioSessionCategoryOptions...)     mutating func subtract(_ other: AVAudioSessionCategoryOptions)     func isSubset(of other: AVAudioSessionCategoryOptions) -> Bool     func isSuperset(of other: AVAudioSessionCategoryOptions) -> Bool     func isDisjoint(with other: AVAudioSessionCategoryOptions) -> Bool     func subtracting(_ other: AVAudioSessionCategoryOptions) -> AVAudioSessionCategoryOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: AVAudioSessionCategoryOptions) -> Bool     func isStrictSubset(of other: AVAudioSessionCategoryOptions) -> Bool } ``` | OptionSet |

Modified [AVAudioSessionCategoryOptions.duckOthers](https://developer.apple.com/documentation/avfoundation/avaudiosession/categoryoptions/1616618-duckothers)

|  | Declaration |
| --- | --- |
| From | ``` static var DuckOthers: AVAudioSessionCategoryOptions { get } ``` |
| To | ``` static var duckOthers: AVAudioSessionCategoryOptions { get } ``` |

Modified [AVAudioSessionCategoryOptions.interruptSpokenAudioAndMixWithOthers](https://developer.apple.com/documentation/avfoundation/avaudiosession/categoryoptions/1616534-interruptspokenaudioandmixwithot)

|  | Declaration |
| --- | --- |
| From | ``` static var InterruptSpokenAudioAndMixWithOthers: AVAudioSessionCategoryOptions { get } ``` |
| To | ``` static var interruptSpokenAudioAndMixWithOthers: AVAudioSessionCategoryOptions { get } ``` |

Modified [AVAudioSessionCategoryOptions.mixWithOthers](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryoptions/avaudiosessioncategoryoptionmixwithothers)

|  | Declaration |
| --- | --- |
| From | ``` static var MixWithOthers: AVAudioSessionCategoryOptions { get } ``` |
| To | ``` static var mixWithOthers: AVAudioSessionCategoryOptions { get } ``` |

Modified [AVAudioSessionChannelDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessionchanneldescription)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioSessionChannelDescription : NSObject {     var channelName: String { get }     var owningPortUID: String { get }     var channelNumber: Int { get }     var channelLabel: AudioChannelLabel { get } } ``` | -- |
| To | ``` class AVAudioSessionChannelDescription : NSObject {     var channelName: String { get }     var owningPortUID: String { get }     var channelNumber: Int { get }     var channelLabel: AudioChannelLabel { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioSessionChannelDescription : CVarArg { } extension AVAudioSessionChannelDescription : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAudioSessionDataSourceDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioSessionDataSourceDescription : NSObject {     var dataSourceID: NSNumber { get }     var dataSourceName: String { get }     var location: String? { get }     var orientation: String? { get }     var supportedPolarPatterns: [String]? { get }     var selectedPolarPattern: String? { get }     var preferredPolarPattern: String? { get }     func setPreferredPolarPattern(_ pattern: String?) throws } ``` | -- |
| To | ``` class AVAudioSessionDataSourceDescription : NSObject {     var dataSourceID: NSNumber { get }     var dataSourceName: String { get }     var location: String? { get }     var orientation: String? { get }     var supportedPolarPatterns: [String]? { get }     var selectedPolarPattern: String? { get }     var preferredPolarPattern: String? { get }     func setPreferredPolarPattern(_ pattern: String?) throws     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioSessionDataSourceDescription : CVarArg { } extension AVAudioSessionDataSourceDescription : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAudioSessionErrorCode [enum]](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode)

|  | Declaration |
| --- | --- |
| From | ``` enum AVAudioSessionErrorCode : Int {     case CodeNone     case CodeMediaServicesFailed     case CodeIsBusy     case CodeIncompatibleCategory     case CodeCannotInterruptOthers     case CodeMissingEntitlement     case CodeSiriIsRecording     case CodeCannotStartPlaying     case CodeCannotStartRecording     case CodeBadParam     case InsufficientPriority     case CodeResourceNotAvailable     case CodeUnspecified } ``` |
| To | ``` enum AVAudioSessionErrorCode : Int {     case codeNone     case codeMediaServicesFailed     case codeIsBusy     case codeIncompatibleCategory     case codeCannotInterruptOthers     case codeMissingEntitlement     case codeSiriIsRecording     case codeCannotStartPlaying     case codeCannotStartRecording     case codeBadParam     case insufficientPriority     case codeResourceNotAvailable     case codeUnspecified } ``` |

Modified [AVAudioSessionErrorCode.codeBadParam](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/badparam)

|  | Declaration |
| --- | --- |
| From | ``` case CodeBadParam ``` |
| To | ``` case codeBadParam ``` |

Modified [AVAudioSessionErrorCode.codeCannotInterruptOthers](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/cannotinterruptothers)

|  | Declaration |
| --- | --- |
| From | ``` case CodeCannotInterruptOthers ``` |
| To | ``` case codeCannotInterruptOthers ``` |

Modified [AVAudioSessionErrorCode.codeCannotStartPlaying](https://developer.apple.com/documentation/avfoundation/avaudiosessionerrorcode/avaudiosessionerrorcodecannotstartplaying)

|  | Declaration |
| --- | --- |
| From | ``` case CodeCannotStartPlaying ``` |
| To | ``` case codeCannotStartPlaying ``` |

Modified [AVAudioSessionErrorCode.codeCannotStartRecording](https://developer.apple.com/documentation/avfoundation/avaudiosessionerrorcode/avaudiosessionerrorcodecannotstartrecording)

|  | Declaration |
| --- | --- |
| From | ``` case CodeCannotStartRecording ``` |
| To | ``` case codeCannotStartRecording ``` |

Modified [AVAudioSessionErrorCode.codeIncompatibleCategory](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/incompatiblecategory)

|  | Declaration |
| --- | --- |
| From | ``` case CodeIncompatibleCategory ``` |
| To | ``` case codeIncompatibleCategory ``` |

Modified [AVAudioSessionErrorCode.codeIsBusy](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/isbusy)

|  | Declaration |
| --- | --- |
| From | ``` case CodeIsBusy ``` |
| To | ``` case codeIsBusy ``` |

Modified [AVAudioSessionErrorCode.codeMediaServicesFailed](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/mediaservicesfailed)

|  | Declaration |
| --- | --- |
| From | ``` case CodeMediaServicesFailed ``` |
| To | ``` case codeMediaServicesFailed ``` |

Modified [AVAudioSessionErrorCode.codeMissingEntitlement](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/missingentitlement)

|  | Declaration |
| --- | --- |
| From | ``` case CodeMissingEntitlement ``` |
| To | ``` case codeMissingEntitlement ``` |

Modified [AVAudioSessionErrorCode.codeNone](https://developer.apple.com/documentation/avfoundation/avaudiosessionerrorcode/avaudiosessionerrorcodenone)

|  | Declaration |
| --- | --- |
| From | ``` case CodeNone ``` |
| To | ``` case codeNone ``` |

Modified [AVAudioSessionErrorCode.codeResourceNotAvailable](https://developer.apple.com/documentation/avfoundation/avaudiosessionerrorcode/avaudiosessionerrorcoderesourcenotavailable)

|  | Declaration |
| --- | --- |
| From | ``` case CodeResourceNotAvailable ``` |
| To | ``` case codeResourceNotAvailable ``` |

Modified [AVAudioSessionErrorCode.codeSiriIsRecording](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/siriisrecording)

|  | Declaration |
| --- | --- |
| From | ``` case CodeSiriIsRecording ``` |
| To | ``` case codeSiriIsRecording ``` |

Modified [AVAudioSessionErrorCode.codeUnspecified](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/unspecified)

|  | Declaration |
| --- | --- |
| From | ``` case CodeUnspecified ``` |
| To | ``` case codeUnspecified ``` |

Modified [AVAudioSessionErrorCode.insufficientPriority](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/avaudiosessionerrorinsufficientpriority)

|  | Declaration |
| --- | --- |
| From | ``` case InsufficientPriority ``` |
| To | ``` case insufficientPriority ``` |

Modified [AVAudioSessionInterruptionOptions [struct]](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptionoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVAudioSessionInterruptionOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var ShouldResume: AVAudioSessionInterruptionOptions { get } } ``` | OptionSetType |
| To | ``` struct AVAudioSessionInterruptionOptions : OptionSet {     init(rawValue rawValue: UInt)     static var shouldResume: AVAudioSessionInterruptionOptions { get }     func intersect(_ other: AVAudioSessionInterruptionOptions) -> AVAudioSessionInterruptionOptions     func exclusiveOr(_ other: AVAudioSessionInterruptionOptions) -> AVAudioSessionInterruptionOptions     mutating func unionInPlace(_ other: AVAudioSessionInterruptionOptions)     mutating func intersectInPlace(_ other: AVAudioSessionInterruptionOptions)     mutating func exclusiveOrInPlace(_ other: AVAudioSessionInterruptionOptions)     func isSubsetOf(_ other: AVAudioSessionInterruptionOptions) -> Bool     func isDisjointWith(_ other: AVAudioSessionInterruptionOptions) -> Bool     func isSupersetOf(_ other: AVAudioSessionInterruptionOptions) -> Bool     mutating func subtractInPlace(_ other: AVAudioSessionInterruptionOptions)     func isStrictSupersetOf(_ other: AVAudioSessionInterruptionOptions) -> Bool     func isStrictSubsetOf(_ other: AVAudioSessionInterruptionOptions) -> Bool } extension AVAudioSessionInterruptionOptions {     func union(_ other: AVAudioSessionInterruptionOptions) -> AVAudioSessionInterruptionOptions     func intersection(_ other: AVAudioSessionInterruptionOptions) -> AVAudioSessionInterruptionOptions     func symmetricDifference(_ other: AVAudioSessionInterruptionOptions) -> AVAudioSessionInterruptionOptions } extension AVAudioSessionInterruptionOptions {     func contains(_ member: AVAudioSessionInterruptionOptions) -> Bool     mutating func insert(_ newMember: AVAudioSessionInterruptionOptions) -> (inserted: Bool, memberAfterInsert: AVAudioSessionInterruptionOptions)     mutating func remove(_ member: AVAudioSessionInterruptionOptions) -> AVAudioSessionInterruptionOptions?     mutating func update(with newMember: AVAudioSessionInterruptionOptions) -> AVAudioSessionInterruptionOptions? } extension AVAudioSessionInterruptionOptions {     convenience init()     mutating func formUnion(_ other: AVAudioSessionInterruptionOptions)     mutating func formIntersection(_ other: AVAudioSessionInterruptionOptions)     mutating func formSymmetricDifference(_ other: AVAudioSessionInterruptionOptions) } extension AVAudioSessionInterruptionOptions {     convenience init<S : Sequence where S.Iterator.Element == AVAudioSessionInterruptionOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AVAudioSessionInterruptionOptions...)     mutating func subtract(_ other: AVAudioSessionInterruptionOptions)     func isSubset(of other: AVAudioSessionInterruptionOptions) -> Bool     func isSuperset(of other: AVAudioSessionInterruptionOptions) -> Bool     func isDisjoint(with other: AVAudioSessionInterruptionOptions) -> Bool     func subtracting(_ other: AVAudioSessionInterruptionOptions) -> AVAudioSessionInterruptionOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: AVAudioSessionInterruptionOptions) -> Bool     func isStrictSubset(of other: AVAudioSessionInterruptionOptions) -> Bool } ``` | OptionSet |

Modified [AVAudioSessionInterruptionOptions.shouldResume](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptionoptions/avaudiosessioninterruptionoptionshouldresume)

|  | Declaration |
| --- | --- |
| From | ``` static var ShouldResume: AVAudioSessionInterruptionOptions { get } ``` |
| To | ``` static var shouldResume: AVAudioSessionInterruptionOptions { get } ``` |

Modified [AVAudioSessionInterruptionType [enum]](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptiontype)

|  | Declaration |
| --- | --- |
| From | ``` enum AVAudioSessionInterruptionType : UInt {     case Began     case Ended } ``` |
| To | ``` enum AVAudioSessionInterruptionType : UInt {     case began     case ended } ``` |

Modified [AVAudioSessionInterruptionType.began](https://developer.apple.com/documentation/avfoundation/avaudiosession/interruptiontype/began)

|  | Declaration |
| --- | --- |
| From | ``` case Began ``` |
| To | ``` case began ``` |

Modified [AVAudioSessionInterruptionType.ended](https://developer.apple.com/documentation/avfoundation/avaudiosession/interruptiontype/ended)

|  | Declaration |
| --- | --- |
| From | ``` case Ended ``` |
| To | ``` case ended ``` |

Modified [AVAudioSessionPortDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioSessionPortDescription : NSObject {     var portType: String { get }     var portName: String { get }     var UID: String { get }     var channels: [AVAudioSessionChannelDescription]? { get }     var dataSources: [AVAudioSessionDataSourceDescription]? { get }     var selectedDataSource: AVAudioSessionDataSourceDescription? { get }     var preferredDataSource: AVAudioSessionDataSourceDescription? { get }     func setPreferredDataSource(_ dataSource: AVAudioSessionDataSourceDescription?) throws } ``` | -- |
| To | ``` class AVAudioSessionPortDescription : NSObject {     var portType: String { get }     var portName: String { get }     var uid: String { get }     var hasHardwareVoiceCallProcessing: Bool { get }     var channels: [AVAudioSessionChannelDescription]? { get }     var dataSources: [AVAudioSessionDataSourceDescription]? { get }     var selectedDataSource: AVAudioSessionDataSourceDescription? { get }     var preferredDataSource: AVAudioSessionDataSourceDescription? { get }     func setPreferredDataSource(_ dataSource: AVAudioSessionDataSourceDescription?) throws     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioSessionPortDescription : CVarArg { } extension AVAudioSessionPortDescription : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAudioSessionPortDescription.uid](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616617-uid)

|  | Declaration |
| --- | --- |
| From | ``` var UID: String { get } ``` |
| To | ``` var uid: String { get } ``` |

Modified [AVAudioSessionPortOverride [enum]](https://developer.apple.com/documentation/avfoundation/avaudiosession/portoverride)

|  | Declaration |
| --- | --- |
| From | ``` enum AVAudioSessionPortOverride : UInt {     case None     case Speaker } ``` |
| To | ``` enum AVAudioSessionPortOverride : UInt {     case none     case speaker } ``` |

Modified [AVAudioSessionPortOverride.none](https://developer.apple.com/documentation/avfoundation/avaudiosession/portoverride/none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [AVAudioSessionRouteChangeReason [enum]](https://developer.apple.com/documentation/avfoundation/avaudiosession/routechangereason)

|  | Declaration |
| --- | --- |
| From | ``` enum AVAudioSessionRouteChangeReason : UInt {     case Unknown     case NewDeviceAvailable     case OldDeviceUnavailable     case CategoryChange     case Override     case WakeFromSleep     case NoSuitableRouteForCategory     case RouteConfigurationChange } ``` |
| To | ``` enum AVAudioSessionRouteChangeReason : UInt {     case unknown     case newDeviceAvailable     case oldDeviceUnavailable     case categoryChange     case override     case wakeFromSleep     case noSuitableRouteForCategory     case routeConfigurationChange } ``` |

Modified [AVAudioSessionRouteChangeReason.categoryChange](https://developer.apple.com/documentation/avfoundation/avaudiosession/routechangereason/categorychange)

|  | Declaration |
| --- | --- |
| From | ``` case CategoryChange ``` |
| To | ``` case categoryChange ``` |

Modified [AVAudioSessionRouteChangeReason.newDeviceAvailable](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereason/avaudiosessionroutechangereasonnewdeviceavailable)

|  | Declaration |
| --- | --- |
| From | ``` case NewDeviceAvailable ``` |
| To | ``` case newDeviceAvailable ``` |

Modified [AVAudioSessionRouteChangeReason.noSuitableRouteForCategory](https://developer.apple.com/documentation/avfoundation/avaudiosession/routechangereason/nosuitablerouteforcategory)

|  | Declaration |
| --- | --- |
| From | ``` case NoSuitableRouteForCategory ``` |
| To | ``` case noSuitableRouteForCategory ``` |

Modified [AVAudioSessionRouteChangeReason.oldDeviceUnavailable](https://developer.apple.com/documentation/avfoundation/avaudiosession/routechangereason/olddeviceunavailable)

|  | Declaration |
| --- | --- |
| From | ``` case OldDeviceUnavailable ``` |
| To | ``` case oldDeviceUnavailable ``` |

Modified [AVAudioSessionRouteChangeReason.override](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereason/avaudiosessionroutechangereasonoverride)

|  | Declaration |
| --- | --- |
| From | ``` case Override ``` |
| To | ``` case override ``` |

Modified [AVAudioSessionRouteChangeReason.routeConfigurationChange](https://developer.apple.com/documentation/avfoundation/avaudiosession/routechangereason/routeconfigurationchange)

|  | Declaration |
| --- | --- |
| From | ``` case RouteConfigurationChange ``` |
| To | ``` case routeConfigurationChange ``` |

Modified [AVAudioSessionRouteChangeReason.unknown](https://developer.apple.com/documentation/avfoundation/avaudiosession/routechangereason/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [AVAudioSessionRouteChangeReason.wakeFromSleep](https://developer.apple.com/documentation/avfoundation/avaudiosession/routechangereason/wakefromsleep)

|  | Declaration |
| --- | --- |
| From | ``` case WakeFromSleep ``` |
| To | ``` case wakeFromSleep ``` |

Modified [AVAudioSessionRouteDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutedescription)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioSessionRouteDescription : NSObject {     var inputs: [AVAudioSessionPortDescription] { get }     var outputs: [AVAudioSessionPortDescription] { get } } ``` | -- |
| To | ``` class AVAudioSessionRouteDescription : NSObject {     var inputs: [AVAudioSessionPortDescription] { get }     var outputs: [AVAudioSessionPortDescription] { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioSessionRouteDescription : CVarArg { } extension AVAudioSessionRouteDescription : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAudioSessionSetActiveOptions [struct]](https://developer.apple.com/documentation/avfoundation/avaudiosessionsetactiveoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVAudioSessionSetActiveOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var NotifyOthersOnDeactivation: AVAudioSessionSetActiveOptions { get } } ``` | OptionSetType |
| To | ``` struct AVAudioSessionSetActiveOptions : OptionSet {     init(rawValue rawValue: UInt)     static var notifyOthersOnDeactivation: AVAudioSessionSetActiveOptions { get }     func intersect(_ other: AVAudioSessionSetActiveOptions) -> AVAudioSessionSetActiveOptions     func exclusiveOr(_ other: AVAudioSessionSetActiveOptions) -> AVAudioSessionSetActiveOptions     mutating func unionInPlace(_ other: AVAudioSessionSetActiveOptions)     mutating func intersectInPlace(_ other: AVAudioSessionSetActiveOptions)     mutating func exclusiveOrInPlace(_ other: AVAudioSessionSetActiveOptions)     func isSubsetOf(_ other: AVAudioSessionSetActiveOptions) -> Bool     func isDisjointWith(_ other: AVAudioSessionSetActiveOptions) -> Bool     func isSupersetOf(_ other: AVAudioSessionSetActiveOptions) -> Bool     mutating func subtractInPlace(_ other: AVAudioSessionSetActiveOptions)     func isStrictSupersetOf(_ other: AVAudioSessionSetActiveOptions) -> Bool     func isStrictSubsetOf(_ other: AVAudioSessionSetActiveOptions) -> Bool } extension AVAudioSessionSetActiveOptions {     func union(_ other: AVAudioSessionSetActiveOptions) -> AVAudioSessionSetActiveOptions     func intersection(_ other: AVAudioSessionSetActiveOptions) -> AVAudioSessionSetActiveOptions     func symmetricDifference(_ other: AVAudioSessionSetActiveOptions) -> AVAudioSessionSetActiveOptions } extension AVAudioSessionSetActiveOptions {     func contains(_ member: AVAudioSessionSetActiveOptions) -> Bool     mutating func insert(_ newMember: AVAudioSessionSetActiveOptions) -> (inserted: Bool, memberAfterInsert: AVAudioSessionSetActiveOptions)     mutating func remove(_ member: AVAudioSessionSetActiveOptions) -> AVAudioSessionSetActiveOptions?     mutating func update(with newMember: AVAudioSessionSetActiveOptions) -> AVAudioSessionSetActiveOptions? } extension AVAudioSessionSetActiveOptions {     convenience init()     mutating func formUnion(_ other: AVAudioSessionSetActiveOptions)     mutating func formIntersection(_ other: AVAudioSessionSetActiveOptions)     mutating func formSymmetricDifference(_ other: AVAudioSessionSetActiveOptions) } extension AVAudioSessionSetActiveOptions {     convenience init<S : Sequence where S.Iterator.Element == AVAudioSessionSetActiveOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AVAudioSessionSetActiveOptions...)     mutating func subtract(_ other: AVAudioSessionSetActiveOptions)     func isSubset(of other: AVAudioSessionSetActiveOptions) -> Bool     func isSuperset(of other: AVAudioSessionSetActiveOptions) -> Bool     func isDisjoint(with other: AVAudioSessionSetActiveOptions) -> Bool     func subtracting(_ other: AVAudioSessionSetActiveOptions) -> AVAudioSessionSetActiveOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: AVAudioSessionSetActiveOptions) -> Bool     func isStrictSubset(of other: AVAudioSessionSetActiveOptions) -> Bool } ``` | OptionSet |

Modified [AVAudioSessionSetActiveOptions.notifyOthersOnDeactivation](https://developer.apple.com/documentation/avfoundation/avaudiosessionsetactiveoptions/avaudiosessionsetactiveoptionnotifyothersondeactivation)

|  | Declaration |
| --- | --- |
| From | ``` static var NotifyOthersOnDeactivation: AVAudioSessionSetActiveOptions { get } ``` |
| To | ``` static var notifyOthersOnDeactivation: AVAudioSessionSetActiveOptions { get } ``` |

Modified [AVAudioSessionSilenceSecondaryAudioHintType [enum]](https://developer.apple.com/documentation/avfoundation/avaudiosession/silencesecondaryaudiohinttype)

|  | Declaration |
| --- | --- |
| From | ``` enum AVAudioSessionSilenceSecondaryAudioHintType : UInt {     case Begin     case End } ``` |
| To | ``` enum AVAudioSessionSilenceSecondaryAudioHintType : UInt {     case begin     case end } ``` |

Modified [AVAudioSessionSilenceSecondaryAudioHintType.begin](https://developer.apple.com/documentation/avfoundation/avaudiosession/silencesecondaryaudiohinttype/begin)

|  | Declaration |
| --- | --- |
| From | ``` case Begin ``` |
| To | ``` case begin ``` |

Modified [AVAudioSessionSilenceSecondaryAudioHintType.end](https://developer.apple.com/documentation/avfoundation/avaudiosessionsilencesecondaryaudiohinttype/avaudiosessionsilencesecondaryaudiohinttypeend)

|  | Declaration |
| --- | --- |
| From | ``` case End ``` |
| To | ``` case end ``` |

Modified [AVAudioTime](https://developer.apple.com/documentation/avfoundation/avaudiotime)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioTime : NSObject {     init(audioTimeStamp ts: UnsafePointer<AudioTimeStamp>, sampleRate sampleRate: Double)     init(hostTime hostTime: UInt64)     init(sampleTime sampleTime: AVAudioFramePosition, atRate sampleRate: Double)     init(hostTime hostTime: UInt64, sampleTime sampleTime: AVAudioFramePosition, atRate sampleRate: Double)     class func timeWithAudioTimeStamp(_ ts: UnsafePointer<AudioTimeStamp>, sampleRate sampleRate: Double) -> Self     class func timeWithHostTime(_ hostTime: UInt64) -> Self     class func timeWithSampleTime(_ sampleTime: AVAudioFramePosition, atRate sampleRate: Double) -> Self     class func timeWithHostTime(_ hostTime: UInt64, sampleTime sampleTime: AVAudioFramePosition, atRate sampleRate: Double) -> Self     class func hostTimeForSeconds(_ seconds: NSTimeInterval) -> UInt64     class func secondsForHostTime(_ hostTime: UInt64) -> NSTimeInterval     func extrapolateTimeFromAnchor(_ anchorTime: AVAudioTime) -> AVAudioTime     var hostTimeValid: Bool { get }     var hostTime: UInt64 { get }     var sampleTimeValid: Bool { get }     var sampleTime: AVAudioFramePosition { get }     var sampleRate: Double { get }     var audioTimeStamp: AudioTimeStamp { get } } ``` | -- |
| To | ``` class AVAudioTime : NSObject {     init(audioTimeStamp ts: UnsafePointer<AudioTimeStamp>, sampleRate sampleRate: Double)     init(hostTime hostTime: UInt64)     init(sampleTime sampleTime: AVAudioFramePosition, atRate sampleRate: Double)     init(hostTime hostTime: UInt64, sampleTime sampleTime: AVAudioFramePosition, atRate sampleRate: Double)     class func withAudioTimeStamp(_ ts: UnsafePointer<AudioTimeStamp>, sampleRate sampleRate: Double) -> Self     class func withHostTime(_ hostTime: UInt64) -> Self     class func withSampleTime(_ sampleTime: AVAudioFramePosition, atRate sampleRate: Double) -> Self     class func withHostTime(_ hostTime: UInt64, sampleTime sampleTime: AVAudioFramePosition, atRate sampleRate: Double) -> Self     class func hostTime(forSeconds seconds: TimeInterval) -> UInt64     class func seconds(forHostTime hostTime: UInt64) -> TimeInterval     func extrapolateTime(fromAnchor anchorTime: AVAudioTime) -> AVAudioTime     var isHostTimeValid: Bool { get }     var hostTime: UInt64 { get }     var isSampleTimeValid: Bool { get }     var sampleTime: AVAudioFramePosition { get }     var sampleRate: Double { get }     var audioTimeStamp: AudioTimeStamp { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioTime : CVarArg { } extension AVAudioTime : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAudioTime.extrapolateTime(fromAnchor: AVAudioTime) -> AVAudioTime](https://developer.apple.com/documentation/avfoundation/avaudiotime/1387772-extrapolatetime)

|  | Declaration |
| --- | --- |
| From | ``` func extrapolateTimeFromAnchor(_ anchorTime: AVAudioTime) -> AVAudioTime ``` |
| To | ``` func extrapolateTime(fromAnchor anchorTime: AVAudioTime) -> AVAudioTime ``` |

Modified [AVAudioTime.hostTime(forSeconds: TimeInterval) -> UInt64 [class]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1388521-hosttime)

|  | Declaration |
| --- | --- |
| From | ``` class func hostTimeForSeconds(_ seconds: NSTimeInterval) -> UInt64 ``` |
| To | ``` class func hostTime(forSeconds seconds: TimeInterval) -> UInt64 ``` |

Modified [AVAudioTime.isHostTimeValid](https://developer.apple.com/documentation/avfoundation/avaudiotime/1387611-ishosttimevalid)

|  | Declaration |
| --- | --- |
| From | ``` var hostTimeValid: Bool { get } ``` |
| To | ``` var isHostTimeValid: Bool { get } ``` |

Modified [AVAudioTime.isSampleTimeValid](https://developer.apple.com/documentation/avfoundation/avaudiotime/1385868-issampletimevalid)

|  | Declaration |
| --- | --- |
| From | ``` var sampleTimeValid: Bool { get } ``` |
| To | ``` var isSampleTimeValid: Bool { get } ``` |

Modified [AVAudioTime.seconds(forHostTime: UInt64) -> TimeInterval [class]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1386096-seconds)

|  | Declaration |
| --- | --- |
| From | ``` class func secondsForHostTime(_ hostTime: UInt64) -> NSTimeInterval ``` |
| To | ``` class func seconds(forHostTime hostTime: UInt64) -> TimeInterval ``` |

Modified [AVAudioUnit](https://developer.apple.com/documentation/avfoundation/avaudiounit)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioUnit : AVAudioNode {     class func instantiateWithComponentDescription(_ audioComponentDescription: AudioComponentDescription, options options: AudioComponentInstantiationOptions, completionHandler completionHandler: (AVAudioUnit?, NSError?) -> Void)     func loadAudioUnitPresetAtURL(_ url: NSURL) throws     var audioComponentDescription: AudioComponentDescription { get }     var audioUnit: AudioUnit { get }     var AUAudioUnit: AUAudioUnit { get }     var name: String { get }     var manufacturerName: String { get }     var version: Int { get } } ``` |
| To | ``` class AVAudioUnit : AVAudioNode {     class func instantiate(with audioComponentDescription: AudioComponentDescription, options options: AudioComponentInstantiationOptions = [], completionHandler completionHandler: @escaping (AVAudioUnit?, Error?) -> Swift.Void)     func loadPreset(at url: URL) throws     var audioComponentDescription: AudioComponentDescription { get }     var audioUnit: AudioUnit { get }     var auAudioUnit: AUAudioUnit { get }     var name: String { get }     var manufacturerName: String { get }     var version: Int { get } } ``` |

Modified [AVAudioUnit.auAudioUnit](https://developer.apple.com/documentation/avfoundation/avaudiounit/1388167-auaudiounit)

|  | Declaration |
| --- | --- |
| From | ``` var AUAudioUnit: AUAudioUnit { get } ``` |
| To | ``` var auAudioUnit: AUAudioUnit { get } ``` |

Modified [AVAudioUnit.instantiate(with: AudioComponentDescription, options: AudioComponentInstantiationOptions, completionHandler: (AVAudioUnit?, Error?) -> Swift.Void) [class]](https://developer.apple.com/documentation/avfoundation/avaudiounit/1390583-instantiatewithcomponentdescript)

|  | Declaration |
| --- | --- |
| From | ``` class func instantiateWithComponentDescription(_ audioComponentDescription: AudioComponentDescription, options options: AudioComponentInstantiationOptions, completionHandler completionHandler: (AVAudioUnit?, NSError?) -> Void) ``` |
| To | ``` class func instantiate(with audioComponentDescription: AudioComponentDescription, options options: AudioComponentInstantiationOptions = [], completionHandler completionHandler: @escaping (AVAudioUnit?, Error?) -> Swift.Void) ``` |

Modified [AVAudioUnit.loadPreset(at: URL) throws](https://developer.apple.com/documentation/avfoundation/avaudiounit/1387527-loadpreset)

|  | Declaration |
| --- | --- |
| From | ``` func loadAudioUnitPresetAtURL(_ url: NSURL) throws ``` |
| To | ``` func loadPreset(at url: URL) throws ``` |

Modified [AVAudioUnitComponent](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioUnitComponent : NSObject {     var name: String { get }     var typeName: String { get }     var localizedTypeName: String { get }     var manufacturerName: String { get }     var version: Int { get }     var versionString: String { get }     var componentURL: NSURL? { get }     var availableArchitectures: [NSNumber] { get }     var sandboxSafe: Bool { get }     var hasMIDIInput: Bool { get }     var hasMIDIOutput: Bool { get }     var audioComponent: AudioComponent { get }     var userTagNames: [String]     var allTagNames: [String] { get }     var audioComponentDescription: AudioComponentDescription { get }     var iconURL: NSURL? { get }     var passesAUVal: Bool { get }     var hasCustomView: Bool { get }     var configurationDictionary: [String : AnyObject] { get }     func supportsNumberInputChannels(_ numInputChannels: Int, outputChannels numOutputChannels: Int) -> Bool } ``` | -- |
| To | ``` class AVAudioUnitComponent : NSObject {     var name: String { get }     var typeName: String { get }     var localizedTypeName: String { get }     var manufacturerName: String { get }     var version: Int { get }     var versionString: String { get }     var componentURL: URL? { get }     var availableArchitectures: [NSNumber] { get }     var isSandboxSafe: Bool { get }     var hasMIDIInput: Bool { get }     var hasMIDIOutput: Bool { get }     var audioComponent: AudioComponent { get }     var userTagNames: [String]     var allTagNames: [String] { get }     var audioComponentDescription: AudioComponentDescription { get }     var iconURL: URL? { get }     var passesAUVal: Bool { get }     var hasCustomView: Bool { get }     var configurationDictionary: [String : Any] { get }     func supportsNumberInputChannels(_ numInputChannels: Int, outputChannels numOutputChannels: Int) -> Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioUnitComponent : CVarArg { } extension AVAudioUnitComponent : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAudioUnitComponent.isSandboxSafe](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1390100-issandboxsafe)

|  | Declaration |
| --- | --- |
| From | ``` var sandboxSafe: Bool { get } ``` |
| To | ``` var isSandboxSafe: Bool { get } ``` |

Modified [AVAudioUnitComponentManager](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioUnitComponentManager : NSObject {     var tagNames: [String] { get }     var standardLocalizedTagNames: [String] { get }     class func sharedAudioUnitComponentManager() -> Self     func componentsMatchingPredicate(_ predicate: NSPredicate) -> [AVAudioUnitComponent]     func componentsPassingTest(_ testHandler: (AVAudioUnitComponent, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AVAudioUnitComponent]     func componentsMatchingDescription(_ desc: AudioComponentDescription) -> [AVAudioUnitComponent] } ``` | -- |
| To | ``` class AVAudioUnitComponentManager : NSObject {     var tagNames: [String] { get }     var standardLocalizedTagNames: [String] { get }     class func shared() -> Self     func components(matching predicate: NSPredicate) -> [AVAudioUnitComponent]     func components(passingTest testHandler: @escaping (AVAudioUnitComponent, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AVAudioUnitComponent]     func components(matching desc: AudioComponentDescription) -> [AVAudioUnitComponent]     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioUnitComponentManager : CVarArg { } extension AVAudioUnitComponentManager : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAudioUnitComponentManager.components(matching: AudioComponentDescription) -> [AVAudioUnitComponent]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1386367-components)

|  | Declaration |
| --- | --- |
| From | ``` func componentsMatchingDescription(_ desc: AudioComponentDescription) -> [AVAudioUnitComponent] ``` |
| To | ``` func components(matching desc: AudioComponentDescription) -> [AVAudioUnitComponent] ``` |

Modified [AVAudioUnitComponentManager.components(matching: NSPredicate) -> [AVAudioUnitComponent]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1386487-components)

|  | Declaration |
| --- | --- |
| From | ``` func componentsMatchingPredicate(_ predicate: NSPredicate) -> [AVAudioUnitComponent] ``` |
| To | ``` func components(matching predicate: NSPredicate) -> [AVAudioUnitComponent] ``` |

Modified [AVAudioUnitComponentManager.components(passingTest: (AVAudioUnitComponent, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AVAudioUnitComponent]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1390260-components)

|  | Declaration |
| --- | --- |
| From | ``` func componentsPassingTest(_ testHandler: (AVAudioUnitComponent, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AVAudioUnitComponent] ``` |
| To | ``` func components(passingTest testHandler: @escaping (AVAudioUnitComponent, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AVAudioUnitComponent] ``` |

Modified [AVAudioUnitComponentManager.shared() -> Self [class]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1390177-shared)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedAudioUnitComponentManager() -> Self ``` |
| To | ``` class func shared() -> Self ``` |

Modified [AVAudioUnitDelay](https://developer.apple.com/documentation/avfoundation/avaudiounitdelay)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioUnitDelay : AVAudioUnitEffect {     var delayTime: NSTimeInterval     var feedback: Float     var lowPassCutoff: Float     var wetDryMix: Float } ``` |
| To | ``` class AVAudioUnitDelay : AVAudioUnitEffect {     var delayTime: TimeInterval     var feedback: Float     var lowPassCutoff: Float     var wetDryMix: Float } ``` |

Modified [AVAudioUnitDelay.delayTime](https://developer.apple.com/documentation/avfoundation/avaudiounitdelay/1386919-delaytime)

|  | Declaration |
| --- | --- |
| From | ``` var delayTime: NSTimeInterval ``` |
| To | ``` var delayTime: TimeInterval ``` |

Modified [AVAudioUnitDistortionPreset [enum]](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset)

|  | Declaration |
| --- | --- |
| From | ``` enum AVAudioUnitDistortionPreset : Int {     case DrumsBitBrush     case DrumsBufferBeats     case DrumsLoFi     case MultiBrokenSpeaker     case MultiCellphoneConcert     case MultiDecimated1     case MultiDecimated2     case MultiDecimated3     case MultiDecimated4     case MultiDistortedFunk     case MultiDistortedCubed     case MultiDistortedSquared     case MultiEcho1     case MultiEcho2     case MultiEchoTight1     case MultiEchoTight2     case MultiEverythingIsBroken     case SpeechAlienChatter     case SpeechCosmicInterference     case SpeechGoldenPi     case SpeechRadioTower     case SpeechWaves } ``` |
| To | ``` enum AVAudioUnitDistortionPreset : Int {     case drumsBitBrush     case drumsBufferBeats     case drumsLoFi     case multiBrokenSpeaker     case multiCellphoneConcert     case multiDecimated1     case multiDecimated2     case multiDecimated3     case multiDecimated4     case multiDistortedFunk     case multiDistortedCubed     case multiDistortedSquared     case multiEcho1     case multiEcho2     case multiEchoTight1     case multiEchoTight2     case multiEverythingIsBroken     case speechAlienChatter     case speechCosmicInterference     case speechGoldenPi     case speechRadioTower     case speechWaves } ``` |

Modified [AVAudioUnitDistortionPreset.drumsBitBrush](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/drumsbitbrush)

|  | Declaration |
| --- | --- |
| From | ``` case DrumsBitBrush ``` |
| To | ``` case drumsBitBrush ``` |

Modified [AVAudioUnitDistortionPreset.drumsBufferBeats](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetdrumsbufferbeats)

|  | Declaration |
| --- | --- |
| From | ``` case DrumsBufferBeats ``` |
| To | ``` case drumsBufferBeats ``` |

Modified [AVAudioUnitDistortionPreset.drumsLoFi](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/drumslofi)

|  | Declaration |
| --- | --- |
| From | ``` case DrumsLoFi ``` |
| To | ``` case drumsLoFi ``` |

Modified [AVAudioUnitDistortionPreset.multiBrokenSpeaker](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multibrokenspeaker)

|  | Declaration |
| --- | --- |
| From | ``` case MultiBrokenSpeaker ``` |
| To | ``` case multiBrokenSpeaker ``` |

Modified [AVAudioUnitDistortionPreset.multiCellphoneConcert](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multicellphoneconcert)

|  | Declaration |
| --- | --- |
| From | ``` case MultiCellphoneConcert ``` |
| To | ``` case multiCellphoneConcert ``` |

Modified [AVAudioUnitDistortionPreset.multiDecimated1](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multidecimated1)

|  | Declaration |
| --- | --- |
| From | ``` case MultiDecimated1 ``` |
| To | ``` case multiDecimated1 ``` |

Modified [AVAudioUnitDistortionPreset.multiDecimated2](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multidecimated2)

|  | Declaration |
| --- | --- |
| From | ``` case MultiDecimated2 ``` |
| To | ``` case multiDecimated2 ``` |

Modified [AVAudioUnitDistortionPreset.multiDecimated3](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetmultidecimated3)

|  | Declaration |
| --- | --- |
| From | ``` case MultiDecimated3 ``` |
| To | ``` case multiDecimated3 ``` |

Modified [AVAudioUnitDistortionPreset.multiDecimated4](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetmultidecimated4)

|  | Declaration |
| --- | --- |
| From | ``` case MultiDecimated4 ``` |
| To | ``` case multiDecimated4 ``` |

Modified [AVAudioUnitDistortionPreset.multiDistortedCubed](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetmultidistortedcubed)

|  | Declaration |
| --- | --- |
| From | ``` case MultiDistortedCubed ``` |
| To | ``` case multiDistortedCubed ``` |

Modified [AVAudioUnitDistortionPreset.multiDistortedFunk](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetmultidistortedfunk)

|  | Declaration |
| --- | --- |
| From | ``` case MultiDistortedFunk ``` |
| To | ``` case multiDistortedFunk ``` |

Modified [AVAudioUnitDistortionPreset.multiDistortedSquared](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multidistortedsquared)

|  | Declaration |
| --- | --- |
| From | ``` case MultiDistortedSquared ``` |
| To | ``` case multiDistortedSquared ``` |

Modified [AVAudioUnitDistortionPreset.multiEcho1](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetmultiecho1)

|  | Declaration |
| --- | --- |
| From | ``` case MultiEcho1 ``` |
| To | ``` case multiEcho1 ``` |

Modified [AVAudioUnitDistortionPreset.multiEcho2](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetmultiecho2)

|  | Declaration |
| --- | --- |
| From | ``` case MultiEcho2 ``` |
| To | ``` case multiEcho2 ``` |

Modified [AVAudioUnitDistortionPreset.multiEchoTight1](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetmultiechotight1)

|  | Declaration |
| --- | --- |
| From | ``` case MultiEchoTight1 ``` |
| To | ``` case multiEchoTight1 ``` |

Modified [AVAudioUnitDistortionPreset.multiEchoTight2](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetmultiechotight2)

|  | Declaration |
| --- | --- |
| From | ``` case MultiEchoTight2 ``` |
| To | ``` case multiEchoTight2 ``` |

Modified [AVAudioUnitDistortionPreset.multiEverythingIsBroken](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetmultieverythingisbroken)

|  | Declaration |
| --- | --- |
| From | ``` case MultiEverythingIsBroken ``` |
| To | ``` case multiEverythingIsBroken ``` |

Modified [AVAudioUnitDistortionPreset.speechAlienChatter](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/speechalienchatter)

|  | Declaration |
| --- | --- |
| From | ``` case SpeechAlienChatter ``` |
| To | ``` case speechAlienChatter ``` |

Modified [AVAudioUnitDistortionPreset.speechCosmicInterference](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetspeechcosmicinterference)

|  | Declaration |
| --- | --- |
| From | ``` case SpeechCosmicInterference ``` |
| To | ``` case speechCosmicInterference ``` |

Modified [AVAudioUnitDistortionPreset.speechGoldenPi](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/speechgoldenpi)

|  | Declaration |
| --- | --- |
| From | ``` case SpeechGoldenPi ``` |
| To | ``` case speechGoldenPi ``` |

Modified [AVAudioUnitDistortionPreset.speechRadioTower](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetspeechradiotower)

|  | Declaration |
| --- | --- |
| From | ``` case SpeechRadioTower ``` |
| To | ``` case speechRadioTower ``` |

Modified [AVAudioUnitDistortionPreset.speechWaves](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetspeechwaves)

|  | Declaration |
| --- | --- |
| From | ``` case SpeechWaves ``` |
| To | ``` case speechWaves ``` |

Modified [AVAudioUnitEQFilterParameters](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfilterparameters)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioUnitEQFilterParameters : NSObject {     var filterType: AVAudioUnitEQFilterType     var frequency: Float     var bandwidth: Float     var gain: Float     var bypass: Bool } ``` | -- |
| To | ``` class AVAudioUnitEQFilterParameters : NSObject {     var filterType: AVAudioUnitEQFilterType     var frequency: Float     var bandwidth: Float     var gain: Float     var bypass: Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVAudioUnitEQFilterParameters : CVarArg { } extension AVAudioUnitEQFilterParameters : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVAudioUnitEQFilterType [enum]](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype)

|  | Declaration |
| --- | --- |
| From | ``` enum AVAudioUnitEQFilterType : Int {     case Parametric     case LowPass     case HighPass     case ResonantLowPass     case ResonantHighPass     case BandPass     case BandStop     case LowShelf     case HighShelf     case ResonantLowShelf     case ResonantHighShelf } ``` |
| To | ``` enum AVAudioUnitEQFilterType : Int {     case parametric     case lowPass     case highPass     case resonantLowPass     case resonantHighPass     case bandPass     case bandStop     case lowShelf     case highShelf     case resonantLowShelf     case resonantHighShelf } ``` |

Modified [AVAudioUnitEQFilterType.bandPass](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/avaudiouniteqfiltertypebandpass)

|  | Declaration |
| --- | --- |
| From | ``` case BandPass ``` |
| To | ``` case bandPass ``` |

Modified [AVAudioUnitEQFilterType.bandStop](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/avaudiouniteqfiltertypebandstop)

|  | Declaration |
| --- | --- |
| From | ``` case BandStop ``` |
| To | ``` case bandStop ``` |

Modified [AVAudioUnitEQFilterType.highPass](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/highpass)

|  | Declaration |
| --- | --- |
| From | ``` case HighPass ``` |
| To | ``` case highPass ``` |

Modified [AVAudioUnitEQFilterType.highShelf](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/highshelf)

|  | Declaration |
| --- | --- |
| From | ``` case HighShelf ``` |
| To | ``` case highShelf ``` |

Modified [AVAudioUnitEQFilterType.lowPass](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/avaudiouniteqfiltertypelowpass)

|  | Declaration |
| --- | --- |
| From | ``` case LowPass ``` |
| To | ``` case lowPass ``` |

Modified [AVAudioUnitEQFilterType.lowShelf](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/avaudiouniteqfiltertypelowshelf)

|  | Declaration |
| --- | --- |
| From | ``` case LowShelf ``` |
| To | ``` case lowShelf ``` |

Modified [AVAudioUnitEQFilterType.parametric](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/parametric)

|  | Declaration |
| --- | --- |
| From | ``` case Parametric ``` |
| To | ``` case parametric ``` |

Modified [AVAudioUnitEQFilterType.resonantHighPass](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/resonanthighpass)

|  | Declaration |
| --- | --- |
| From | ``` case ResonantHighPass ``` |
| To | ``` case resonantHighPass ``` |

Modified [AVAudioUnitEQFilterType.resonantHighShelf](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/resonanthighshelf)

|  | Declaration |
| --- | --- |
| From | ``` case ResonantHighShelf ``` |
| To | ``` case resonantHighShelf ``` |

Modified [AVAudioUnitEQFilterType.resonantLowPass](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/avaudiouniteqfiltertyperesonantlowpass)

|  | Declaration |
| --- | --- |
| From | ``` case ResonantLowPass ``` |
| To | ``` case resonantLowPass ``` |

Modified [AVAudioUnitEQFilterType.resonantLowShelf](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/resonantlowshelf)

|  | Declaration |
| --- | --- |
| From | ``` case ResonantLowShelf ``` |
| To | ``` case resonantLowShelf ``` |

Modified [AVAudioUnitMIDIInstrument](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioUnitMIDIInstrument : AVAudioUnit, AVAudioMixing {     init(audioComponentDescription description: AudioComponentDescription)     func startNote(_ note: UInt8, withVelocity velocity: UInt8, onChannel channel: UInt8)     func stopNote(_ note: UInt8, onChannel channel: UInt8)     func sendController(_ controller: UInt8, withValue value: UInt8, onChannel channel: UInt8)     func sendPitchBend(_ pitchbend: UInt16, onChannel channel: UInt8)     func sendPressure(_ pressure: UInt8, onChannel channel: UInt8)     func sendPressureForKey(_ key: UInt8, withValue value: UInt8, onChannel channel: UInt8)     func sendProgramChange(_ program: UInt8, onChannel channel: UInt8)     func sendProgramChange(_ program: UInt8, bankMSB bankMSB: UInt8, bankLSB bankLSB: UInt8, onChannel channel: UInt8)     func sendMIDIEvent(_ midiStatus: UInt8, data1 data1: UInt8, data2 data2: UInt8)     func sendMIDIEvent(_ midiStatus: UInt8, data1 data1: UInt8)     func sendMIDISysExEvent(_ midiData: NSData) } ``` |
| To | ``` class AVAudioUnitMIDIInstrument : AVAudioUnit, AVAudioMixing {     init(audioComponentDescription description: AudioComponentDescription)     func startNote(_ note: UInt8, withVelocity velocity: UInt8, onChannel channel: UInt8)     func stopNote(_ note: UInt8, onChannel channel: UInt8)     func sendController(_ controller: UInt8, withValue value: UInt8, onChannel channel: UInt8)     func sendPitchBend(_ pitchbend: UInt16, onChannel channel: UInt8)     func sendPressure(_ pressure: UInt8, onChannel channel: UInt8)     func sendPressure(forKey key: UInt8, withValue value: UInt8, onChannel channel: UInt8)     func sendProgramChange(_ program: UInt8, onChannel channel: UInt8)     func sendProgramChange(_ program: UInt8, bankMSB bankMSB: UInt8, bankLSB bankLSB: UInt8, onChannel channel: UInt8)     func sendMIDIEvent(_ midiStatus: UInt8, data1 data1: UInt8, data2 data2: UInt8)     func sendMIDIEvent(_ midiStatus: UInt8, data1 data1: UInt8)     func sendMIDISysExEvent(_ midiData: Data) } ``` |

Modified [AVAudioUnitMIDIInstrument.sendMIDISysExEvent(_: Data)](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1387812-sendmidisysexevent)

|  | Declaration |
| --- | --- |
| From | ``` func sendMIDISysExEvent(_ midiData: NSData) ``` |
| To | ``` func sendMIDISysExEvent(_ midiData: Data) ``` |

Modified [AVAudioUnitMIDIInstrument.sendPressure(forKey: UInt8, withValue: UInt8, onChannel: UInt8)](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1388563-sendpressureforkey)

|  | Declaration |
| --- | --- |
| From | ``` func sendPressureForKey(_ key: UInt8, withValue value: UInt8, onChannel channel: UInt8) ``` |
| To | ``` func sendPressure(forKey key: UInt8, withValue value: UInt8, onChannel channel: UInt8) ``` |

Modified [AVAudioUnitReverbPreset [enum]](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset)

|  | Declaration |
| --- | --- |
| From | ``` enum AVAudioUnitReverbPreset : Int {     case SmallRoom     case MediumRoom     case LargeRoom     case MediumHall     case LargeHall     case Plate     case MediumChamber     case LargeChamber     case Cathedral     case LargeRoom2     case MediumHall2     case MediumHall3     case LargeHall2 } ``` |
| To | ``` enum AVAudioUnitReverbPreset : Int {     case smallRoom     case mediumRoom     case largeRoom     case mediumHall     case largeHall     case plate     case mediumChamber     case largeChamber     case cathedral     case largeRoom2     case mediumHall2     case mediumHall3     case largeHall2 } ``` |

Modified [AVAudioUnitReverbPreset.cathedral](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/avaudiounitreverbpresetcathedral)

|  | Declaration |
| --- | --- |
| From | ``` case Cathedral ``` |
| To | ``` case cathedral ``` |

Modified [AVAudioUnitReverbPreset.largeChamber](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/largechamber)

|  | Declaration |
| --- | --- |
| From | ``` case LargeChamber ``` |
| To | ``` case largeChamber ``` |

Modified [AVAudioUnitReverbPreset.largeHall](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/avaudiounitreverbpresetlargehall)

|  | Declaration |
| --- | --- |
| From | ``` case LargeHall ``` |
| To | ``` case largeHall ``` |

Modified [AVAudioUnitReverbPreset.largeHall2](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/largehall2)

|  | Declaration |
| --- | --- |
| From | ``` case LargeHall2 ``` |
| To | ``` case largeHall2 ``` |

Modified [AVAudioUnitReverbPreset.largeRoom](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/avaudiounitreverbpresetlargeroom)

|  | Declaration |
| --- | --- |
| From | ``` case LargeRoom ``` |
| To | ``` case largeRoom ``` |

Modified [AVAudioUnitReverbPreset.largeRoom2](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/avaudiounitreverbpresetlargeroom2)

|  | Declaration |
| --- | --- |
| From | ``` case LargeRoom2 ``` |
| To | ``` case largeRoom2 ``` |

Modified [AVAudioUnitReverbPreset.mediumChamber](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/mediumchamber)

|  | Declaration |
| --- | --- |
| From | ``` case MediumChamber ``` |
| To | ``` case mediumChamber ``` |

Modified [AVAudioUnitReverbPreset.mediumHall](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/mediumhall)

|  | Declaration |
| --- | --- |
| From | ``` case MediumHall ``` |
| To | ``` case mediumHall ``` |

Modified [AVAudioUnitReverbPreset.mediumHall2](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/mediumhall2)

|  | Declaration |
| --- | --- |
| From | ``` case MediumHall2 ``` |
| To | ``` case mediumHall2 ``` |

Modified [AVAudioUnitReverbPreset.mediumHall3](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/mediumhall3)

|  | Declaration |
| --- | --- |
| From | ``` case MediumHall3 ``` |
| To | ``` case mediumHall3 ``` |

Modified [AVAudioUnitReverbPreset.mediumRoom](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/avaudiounitreverbpresetmediumroom)

|  | Declaration |
| --- | --- |
| From | ``` case MediumRoom ``` |
| To | ``` case mediumRoom ``` |

Modified [AVAudioUnitReverbPreset.plate](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/avaudiounitreverbpresetplate)

|  | Declaration |
| --- | --- |
| From | ``` case Plate ``` |
| To | ``` case plate ``` |

Modified [AVAudioUnitReverbPreset.smallRoom](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/smallroom)

|  | Declaration |
| --- | --- |
| From | ``` case SmallRoom ``` |
| To | ``` case smallRoom ``` |

Modified [AVAudioUnitSampler](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioUnitSampler : AVAudioUnitMIDIInstrument {     func loadSoundBankInstrumentAtURL(_ bankURL: NSURL, program program: UInt8, bankMSB bankMSB: UInt8, bankLSB bankLSB: UInt8) throws     func loadInstrumentAtURL(_ instrumentURL: NSURL) throws     func loadAudioFilesAtURLs(_ audioFiles: [NSURL]) throws     var stereoPan: Float     var masterGain: Float     var globalTuning: Float } ``` |
| To | ``` class AVAudioUnitSampler : AVAudioUnitMIDIInstrument {     func loadSoundBankInstrument(at bankURL: URL, program program: UInt8, bankMSB bankMSB: UInt8, bankLSB bankLSB: UInt8) throws     func loadInstrument(at instrumentURL: URL) throws     func loadAudioFiles(at audioFiles: [URL]) throws     var stereoPan: Float     var masterGain: Float     var globalTuning: Float } ``` |

Modified [AVAudioUnitSampler.loadAudioFiles(at: [URL]) throws](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1388631-loadaudiofilesaturls)

|  | Declaration |
| --- | --- |
| From | ``` func loadAudioFilesAtURLs(_ audioFiles: [NSURL]) throws ``` |
| To | ``` func loadAudioFiles(at audioFiles: [URL]) throws ``` |

Modified [AVAudioUnitSampler.loadInstrument(at: URL) throws](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1389514-loadinstrumentaturl)

|  | Declaration |
| --- | --- |
| From | ``` func loadInstrumentAtURL(_ instrumentURL: NSURL) throws ``` |
| To | ``` func loadInstrument(at instrumentURL: URL) throws ``` |

Modified [AVAudioUnitSampler.loadSoundBankInstrument(at: URL, program: UInt8, bankMSB: UInt8, bankLSB: UInt8) throws](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1385687-loadsoundbankinstrumentaturl)

|  | Declaration |
| --- | --- |
| From | ``` func loadSoundBankInstrumentAtURL(_ bankURL: NSURL, program program: UInt8, bankMSB bankMSB: UInt8, bankLSB bankLSB: UInt8) throws ``` |
| To | ``` func loadSoundBankInstrument(at bankURL: URL, program program: UInt8, bankMSB bankMSB: UInt8, bankLSB bankLSB: UInt8) throws ``` |

Modified [AVCaptureDevice.authorizationStatus(forMediaType: String!) -> AVAuthorizationStatus [class]](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624613-authorizationstatusformediatype)

|  | Declaration |
| --- | --- |
| From | ``` class func authorizationStatusForMediaType(_ mediaType: String!) -> AVAuthorizationStatus ``` |
| To | ``` class func authorizationStatus(forMediaType mediaType: String!) -> AVAuthorizationStatus ``` |

Modified [AVCaptureDevice.chromaticityValues(forDeviceWhiteBalanceGains: AVCaptureWhiteBalanceGains) -> AVCaptureWhiteBalanceChromaticityValues](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624650-chromaticityvaluesfordevicewhite)

|  | Declaration |
| --- | --- |
| From | ``` func chromaticityValuesForDeviceWhiteBalanceGains(_ whiteBalanceGains: AVCaptureWhiteBalanceGains) -> AVCaptureWhiteBalanceChromaticityValues ``` |
| To | ``` func chromaticityValues(forDeviceWhiteBalanceGains whiteBalanceGains: AVCaptureWhiteBalanceGains) -> AVCaptureWhiteBalanceChromaticityValues ``` |

Modified [AVCaptureDevice.deviceWhiteBalanceGains(for: AVCaptureWhiteBalanceChromaticityValues) -> AVCaptureWhiteBalanceGains](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624575-devicewhitebalancegainsforchroma)

|  | Declaration |
| --- | --- |
| From | ``` func deviceWhiteBalanceGainsForChromaticityValues(_ chromaticityValues: AVCaptureWhiteBalanceChromaticityValues) -> AVCaptureWhiteBalanceGains ``` |
| To | ``` func deviceWhiteBalanceGains(for chromaticityValues: AVCaptureWhiteBalanceChromaticityValues) -> AVCaptureWhiteBalanceGains ``` |

Modified [AVCaptureDevice.deviceWhiteBalanceGains(for: AVCaptureWhiteBalanceTemperatureAndTintValues) -> AVCaptureWhiteBalanceGains](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624628-devicewhitebalancegainsfortemper)

|  | Declaration |
| --- | --- |
| From | ``` func deviceWhiteBalanceGainsForTemperatureAndTintValues(_ tempAndTintValues: AVCaptureWhiteBalanceTemperatureAndTintValues) -> AVCaptureWhiteBalanceGains ``` |
| To | ``` func deviceWhiteBalanceGains(for tempAndTintValues: AVCaptureWhiteBalanceTemperatureAndTintValues) -> AVCaptureWhiteBalanceGains ``` |

Modified [AVCaptureDevice.flashMode](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1388116-flashmode)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 10.0 |

Modified [AVCaptureDevice.isAdjustingExposure](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1386253-adjustingexposure)

|  | Declaration |
| --- | --- |
| From | ``` var adjustingExposure: Bool { get } ``` |
| To | ``` var isAdjustingExposure: Bool { get } ``` |

Modified [AVCaptureDevice.isAdjustingFocus](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1390577-isadjustingfocus)

|  | Declaration |
| --- | --- |
| From | ``` var adjustingFocus: Bool { get } ``` |
| To | ``` var isAdjustingFocus: Bool { get } ``` |

Modified [AVCaptureDevice.isAdjustingWhiteBalance](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1386544-isadjustingwhitebalance)

|  | Declaration |
| --- | --- |
| From | ``` var adjustingWhiteBalance: Bool { get } ``` |
| To | ``` var isAdjustingWhiteBalance: Bool { get } ``` |

Modified [AVCaptureDevice.isAutoFocusRangeRestrictionSupported](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624570-isautofocusrangerestrictionsuppo)

|  | Declaration |
| --- | --- |
| From | ``` var autoFocusRangeRestrictionSupported: Bool { get } ``` |
| To | ``` var isAutoFocusRangeRestrictionSupported: Bool { get } ``` |

Modified [AVCaptureDevice.isExposurePointOfInterestSupported](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1387263-exposurepointofinterestsupported)

|  | Declaration |
| --- | --- |
| From | ``` var exposurePointOfInterestSupported: Bool { get } ``` |
| To | ``` var isExposurePointOfInterestSupported: Bool { get } ``` |

Modified [AVCaptureDevice.isFlashActive](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624598-isflashactive)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var flashActive: Bool { get } ``` | -- |
| To | ``` var isFlashActive: Bool { get } ``` | tvOS 10.0 |

Modified [AVCaptureDevice.isFlashAvailable](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624627-flashavailable)

|  | Declaration |
| --- | --- |
| From | ``` var flashAvailable: Bool { get } ``` |
| To | ``` var isFlashAvailable: Bool { get } ``` |

Modified [AVCaptureDevice.isFlashModeSupported(_: AVCaptureFlashMode) -> Bool](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1386434-isflashmodesupported)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 10.0 |

Modified [AVCaptureDevice.isFocusPointOfInterestSupported](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1390436-isfocuspointofinterestsupported)

|  | Declaration |
| --- | --- |
| From | ``` var focusPointOfInterestSupported: Bool { get } ``` |
| To | ``` var isFocusPointOfInterestSupported: Bool { get } ``` |

Modified [AVCaptureDevice.isLowLightBoostEnabled](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624602-islowlightboostenabled)

|  | Declaration |
| --- | --- |
| From | ``` var lowLightBoostEnabled: Bool { get } ``` |
| To | ``` var isLowLightBoostEnabled: Bool { get } ``` |

Modified [AVCaptureDevice.isLowLightBoostSupported](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624595-lowlightboostsupported)

|  | Declaration |
| --- | --- |
| From | ``` var lowLightBoostSupported: Bool { get } ``` |
| To | ``` var isLowLightBoostSupported: Bool { get } ``` |

Modified [AVCaptureDevice.iso](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624649-iso)

|  | Declaration |
| --- | --- |
| From | ``` var ISO: Float { get } ``` |
| To | ``` var iso: Float { get } ``` |

Modified [AVCaptureDevice.isRampingVideoZoom](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624588-rampingvideozoom)

|  | Declaration |
| --- | --- |
| From | ``` var rampingVideoZoom: Bool { get } ``` |
| To | ``` var isRampingVideoZoom: Bool { get } ``` |

Modified [AVCaptureDevice.isSmoothAutoFocusEnabled](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624653-smoothautofocusenabled)

|  | Declaration |
| --- | --- |
| From | ``` var smoothAutoFocusEnabled: Bool ``` |
| To | ``` var isSmoothAutoFocusEnabled: Bool ``` |

Modified [AVCaptureDevice.isSmoothAutoFocusSupported](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624625-smoothautofocussupported)

|  | Declaration |
| --- | --- |
| From | ``` var smoothAutoFocusSupported: Bool { get } ``` |
| To | ``` var isSmoothAutoFocusSupported: Bool { get } ``` |

Modified [AVCaptureDevice.isSubjectAreaChangeMonitoringEnabled](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624644-subjectareachangemonitoringenabl)

|  | Declaration |
| --- | --- |
| From | ``` var subjectAreaChangeMonitoringEnabled: Bool ``` |
| To | ``` var isSubjectAreaChangeMonitoringEnabled: Bool ``` |

Modified [AVCaptureDevice.isTorchActive](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624578-torchactive)

|  | Declaration |
| --- | --- |
| From | ``` var torchActive: Bool { get } ``` |
| To | ``` var isTorchActive: Bool { get } ``` |

Modified [AVCaptureDevice.isTorchAvailable](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624626-istorchavailable)

|  | Declaration |
| --- | --- |
| From | ``` var torchAvailable: Bool { get } ``` |
| To | ``` var isTorchAvailable: Bool { get } ``` |

Modified [AVCaptureDevice.isVideoHDREnabled](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624645-isvideohdrenabled)

|  | Declaration |
| --- | --- |
| From | ``` var videoHDREnabled: Bool ``` |
| To | ``` var isVideoHDREnabled: Bool ``` |

Modified [AVCaptureDevice.ramp(toVideoZoomFactor: CGFloat, withRate: Float)](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624614-ramptovideozoomfactor)

|  | Declaration |
| --- | --- |
| From | ``` func rampToVideoZoomFactor(_ factor: CGFloat, withRate rate: Float) ``` |
| To | ``` func ramp(toVideoZoomFactor factor: CGFloat, withRate rate: Float) ``` |

Modified [AVCaptureDevice.requestAccess(forMediaType: String!, completionHandler: ( (Bool) -> Swift.Void)!) [class]](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624584-requestaccess)

|  | Declaration |
| --- | --- |
| From | ``` class func requestAccessForMediaType(_ mediaType: String!, completionHandler handler: ((Bool) -> Void)!) ``` |
| To | ``` class func requestAccess(forMediaType mediaType: String!, completionHandler handler: (@escaping (Bool) -> Swift.Void)!) ``` |

Modified [AVCaptureDevice.setExposureModeCustomWithDuration(_: CMTime, iso: Float, completionHandler: ( (CMTime) -> Swift.Void)!)](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624646-setexposuremodecustomwithduratio)

|  | Declaration |
| --- | --- |
| From | ``` func setExposureModeCustomWithDuration(_ duration: CMTime, ISO ISO: Float, completionHandler handler: ((CMTime) -> Void)!) ``` |
| To | ``` func setExposureModeCustomWithDuration(_ duration: CMTime, iso ISO: Float, completionHandler handler: (@escaping (CMTime) -> Swift.Void)!) ``` |

Modified [AVCaptureDevice.setExposureTargetBias(_: Float, completionHandler: ( (CMTime) -> Swift.Void)!)](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624637-setexposuretargetbias)

|  | Declaration |
| --- | --- |
| From | ``` func setExposureTargetBias(_ bias: Float, completionHandler handler: ((CMTime) -> Void)!) ``` |
| To | ``` func setExposureTargetBias(_ bias: Float, completionHandler handler: (@escaping (CMTime) -> Swift.Void)!) ``` |

Modified [AVCaptureDevice.setFocusModeLockedWithLensPosition(_: Float, completionHandler: ( (CMTime) -> Swift.Void)!)](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624617-setfocusmodelocked)

|  | Declaration |
| --- | --- |
| From | ``` func setFocusModeLockedWithLensPosition(_ lensPosition: Float, completionHandler handler: ((CMTime) -> Void)!) ``` |
| To | ``` func setFocusModeLockedWithLensPosition(_ lensPosition: Float, completionHandler handler: (@escaping (CMTime) -> Swift.Void)!) ``` |

Modified [AVCaptureDevice.setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains(_: AVCaptureWhiteBalanceGains, completionHandler: ( (CMTime) -> Swift.Void)!)](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624568-setwhitebalancemodelocked)

|  | Declaration |
| --- | --- |
| From | ``` func setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains(_ whiteBalanceGains: AVCaptureWhiteBalanceGains, completionHandler handler: ((CMTime) -> Void)!) ``` |
| To | ``` func setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains(_ whiteBalanceGains: AVCaptureWhiteBalanceGains, completionHandler handler: (@escaping (CMTime) -> Swift.Void)!) ``` |

Modified [AVCaptureDevice.temperatureAndTintValues(forDeviceWhiteBalanceGains: AVCaptureWhiteBalanceGains) -> AVCaptureWhiteBalanceTemperatureAndTintValues](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624640-temperatureandtintvaluesfordevic)

|  | Declaration |
| --- | --- |
| From | ``` func temperatureAndTintValuesForDeviceWhiteBalanceGains(_ whiteBalanceGains: AVCaptureWhiteBalanceGains) -> AVCaptureWhiteBalanceTemperatureAndTintValues ``` |
| To | ``` func temperatureAndTintValues(forDeviceWhiteBalanceGains whiteBalanceGains: AVCaptureWhiteBalanceGains) -> AVCaptureWhiteBalanceTemperatureAndTintValues ``` |

Modified [AVCaptureStillImageOutput.captureStillImageBracketAsynchronously(from: AVCaptureConnection!, withSettingsArray: [Any]!, completionHandler: ( (CMSampleBuffer?, AVCaptureBracketedStillImageSettings?, Error?) -> Swift.Void)!)](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616285-capturestillimagebracketasynchro)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func captureStillImageBracketAsynchronouslyFromConnection(_ connection: AVCaptureConnection!, withSettingsArray settings: [AnyObject]!, completionHandler handler: ((CMSampleBuffer!, AVCaptureBracketedStillImageSettings!, NSError!) -> Void)!) ``` | -- |
| To | ``` func captureStillImageBracketAsynchronously(from connection: AVCaptureConnection!, withSettingsArray settings: [Any]!, completionHandler handler: (@escaping (CMSampleBuffer?, AVCaptureBracketedStillImageSettings?, Error?) -> Swift.Void)!) ``` | tvOS 10.0 |

Modified [AVCaptureStillImageOutput.isLensStabilizationDuringBracketedCaptureEnabled](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616287-islensstabilizationduringbracket)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var lensStabilizationDuringBracketedCaptureEnabled: Bool ``` | -- |
| To | ``` var isLensStabilizationDuringBracketedCaptureEnabled: Bool ``` | tvOS 10.0 |

Modified [AVCaptureStillImageOutput.isLensStabilizationDuringBracketedCaptureSupported](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616288-islensstabilizationduringbracket)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var lensStabilizationDuringBracketedCaptureSupported: Bool { get } ``` | -- |
| To | ``` var isLensStabilizationDuringBracketedCaptureSupported: Bool { get } ``` | tvOS 10.0 |

Modified [AVCaptureStillImageOutput.maxBracketedCaptureStillImageCount](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616294-maxbracketedcapturestillimagecou)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 10.0 |

Modified [AVCaptureStillImageOutput.prepareToCaptureStillImageBracket(from: AVCaptureConnection!, withSettingsArray: [Any]!, completionHandler: ( (Bool, Error?) -> Swift.Void)!)](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616298-preparetocapturestillimagebracke)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func prepareToCaptureStillImageBracketFromConnection(_ connection: AVCaptureConnection!, withSettingsArray settings: [AnyObject]!, completionHandler handler: ((Bool, NSError!) -> Void)!) ``` | -- |
| To | ``` func prepareToCaptureStillImageBracket(from connection: AVCaptureConnection!, withSettingsArray settings: [Any]!, completionHandler handler: (@escaping (Bool, Error?) -> Swift.Void)!) ``` | tvOS 10.0 |

Modified [AVComposition](https://developer.apple.com/documentation/avfoundation/avcomposition)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVComposition : AVAsset, NSMutableCopying {     var tracks: [AVCompositionTrack] { get }     var naturalSize: CGSize { get }     var URLAssetInitializationOptions: [String : AnyObject] { get } } extension AVComposition {     func trackWithTrackID(_ trackID: CMPersistentTrackID) -> AVCompositionTrack?     func tracksWithMediaType(_ mediaType: String) -> [AVCompositionTrack]     func tracksWithMediaCharacteristic(_ mediaCharacteristic: String) -> [AVCompositionTrack] } ``` | NSMutableCopying |
| To | ``` class AVComposition : AVAsset, NSMutableCopying {     var tracks: [AVCompositionTrack] { get }     var naturalSize: CGSize { get }     var urlAssetInitializationOptions: [String : Any] { get }     func track(withTrackID trackID: CMPersistentTrackID) -> AVCompositionTrack?     func tracks(withMediaType mediaType: String) -> [AVCompositionTrack]     func tracks(withMediaCharacteristic mediaCharacteristic: String) -> [AVCompositionTrack]     func unusedTrackID() -> CMPersistentTrackID     var isPlayable: Bool { get }     var isExportable: Bool { get }     var isReadable: Bool { get }     var isComposable: Bool { get }     var isCompatibleWithSavedPhotosAlbum: Bool { get }     var isCompatibleWithAirPlayVideo: Bool { get }     var canContainFragments: Bool { get }     var containsFragments: Bool { get }     var hasProtectedContent: Bool { get }     var availableMediaCharacteristicsWithMediaSelectionOptions: [String] { get }     func mediaSelectionGroup(forMediaCharacteristic mediaCharacteristic: String) -> AVMediaSelectionGroup?     var preferredMediaSelection: AVMediaSelection { get }     var availableChapterLocales: [Locale] { get }     func chapterMetadataGroups(withTitleLocale locale: Locale, containingItemsWithCommonKeys commonKeys: [String]?) -> [AVTimedMetadataGroup]     func chapterMetadataGroups(bestMatchingPreferredLanguages preferredLanguages: [String]) -> [AVTimedMetadataGroup]     var creationDate: AVMetadataItem? { get }     var lyrics: String? { get }     var commonMetadata: [AVMetadataItem] { get }     var metadata: [AVMetadataItem] { get }     var availableMetadataFormats: [String] { get }     func metadata(forFormat format: String) -> [AVMetadataItem]     var tracks: [AVAssetTrack] { get }     var trackGroups: [AVAssetTrackGroup] { get }     var referenceRestrictions: AVAssetReferenceRestrictions { get }     var providesPreciseDurationAndTiming: Bool { get }     func cancelLoading()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVComposition : CVarArg { } extension AVComposition : Equatable, Hashable {     var hashValue: Int { get } } extension AVComposition {     func track(withTrackID trackID: CMPersistentTrackID) -> AVCompositionTrack?     func tracks(withMediaType mediaType: String) -> [AVCompositionTrack]     func tracks(withMediaCharacteristic mediaCharacteristic: String) -> [AVCompositionTrack] } ``` | CVarArg, Equatable, Hashable, NSMutableCopying |

Modified [AVComposition.track(withTrackID: CMPersistentTrackID) -> AVCompositionTrack?](https://developer.apple.com/documentation/avfoundation/avcomposition/1388473-track)

|  | Declaration |
| --- | --- |
| From | ``` func trackWithTrackID(_ trackID: CMPersistentTrackID) -> AVCompositionTrack? ``` |
| To | ``` func track(withTrackID trackID: CMPersistentTrackID) -> AVCompositionTrack? ``` |

Modified [AVComposition.tracks(withMediaCharacteristic: String) -> [AVCompositionTrack]](https://developer.apple.com/documentation/avfoundation/avcomposition/1387525-trackswithmediacharacteristic)

|  | Declaration |
| --- | --- |
| From | ``` func tracksWithMediaCharacteristic(_ mediaCharacteristic: String) -> [AVCompositionTrack] ``` |
| To | ``` func tracks(withMediaCharacteristic mediaCharacteristic: String) -> [AVCompositionTrack] ``` |

Modified [AVComposition.tracks(withMediaType: String) -> [AVCompositionTrack]](https://developer.apple.com/documentation/avfoundation/avcomposition/1386534-trackswithmediatype)

|  | Declaration |
| --- | --- |
| From | ``` func tracksWithMediaType(_ mediaType: String) -> [AVCompositionTrack] ``` |
| To | ``` func tracks(withMediaType mediaType: String) -> [AVCompositionTrack] ``` |

Modified [AVComposition.urlAssetInitializationOptions](https://developer.apple.com/documentation/avfoundation/avcomposition/1387080-urlassetinitializationoptions)

|  | Declaration |
| --- | --- |
| From | ``` var URLAssetInitializationOptions: [String : AnyObject] { get } ``` |
| To | ``` var urlAssetInitializationOptions: [String : Any] { get } ``` |

Modified [AVCompositionTrack](https://developer.apple.com/documentation/avfoundation/avcompositiontrack)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVCompositionTrack : AVAssetTrack {     var segments: [AVCompositionTrackSegment] { get } } ``` | -- |
| To | ``` class AVCompositionTrack : AVAssetTrack {     var segments: [AVCompositionTrackSegment] { get }     var availableTrackAssociationTypes: [String] { get }     func associatedTracks(ofType trackAssociationType: String) -> [AVAssetTrack]     var commonMetadata: [AVMetadataItem] { get }     var metadata: [AVMetadataItem] { get }     var availableMetadataFormats: [String] { get }     func metadata(forFormat format: String) -> [AVMetadataItem]     var segments: [AVAssetTrackSegment] { get }     func segment(forTrackTime trackTime: CMTime) -> AVAssetTrackSegment?     func samplePresentationTime(forTrackTime trackTime: CMTime) -> CMTime     var nominalFrameRate: Float { get }     var minFrameDuration: CMTime { get }     var requiresFrameReordering: Bool { get }     var preferredVolume: Float { get }     var naturalSize: CGSize { get }     var preferredTransform: CGAffineTransform { get }     var languageCode: String? { get }     var extendedLanguageTag: String? { get }     var timeRange: CMTimeRange { get }     var naturalTimeScale: CMTimeScale { get }     var estimatedDataRate: Float { get }     var mediaType: String { get }     var formatDescriptions: [Any] { get }     var isPlayable: Bool { get }     var isEnabled: Bool { get }     var isSelfContained: Bool { get }     var totalSampleDataLength: Int64 { get }     func hasMediaCharacteristic(_ mediaCharacteristic: String) -> Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVCompositionTrack : CVarArg { } extension AVCompositionTrack : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVCompositionTrackSegment](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment)

|  | Declaration |
| --- | --- |
| From | ``` class AVCompositionTrackSegment : AVAssetTrackSegment {     convenience init(URL URL: NSURL, trackID trackID: CMPersistentTrackID, sourceTimeRange sourceTimeRange: CMTimeRange, targetTimeRange targetTimeRange: CMTimeRange)     class func compositionTrackSegmentWithURL(_ URL: NSURL, trackID trackID: CMPersistentTrackID, sourceTimeRange sourceTimeRange: CMTimeRange, targetTimeRange targetTimeRange: CMTimeRange) -> Self     convenience init(timeRange timeRange: CMTimeRange)     class func compositionTrackSegmentWithTimeRange(_ timeRange: CMTimeRange) -> Self     init(URL URL: NSURL, trackID trackID: CMPersistentTrackID, sourceTimeRange sourceTimeRange: CMTimeRange, targetTimeRange targetTimeRange: CMTimeRange)     init(timeRange timeRange: CMTimeRange)     var empty: Bool { get }     var sourceURL: NSURL? { get }     var sourceTrackID: CMPersistentTrackID { get } } ``` |
| To | ``` class AVCompositionTrackSegment : AVAssetTrackSegment {     convenience init(url URL: URL, trackID trackID: CMPersistentTrackID, sourceTimeRange sourceTimeRange: CMTimeRange, targetTimeRange targetTimeRange: CMTimeRange)     class func withURL(_ URL: URL, trackID trackID: CMPersistentTrackID, sourceTimeRange sourceTimeRange: CMTimeRange, targetTimeRange targetTimeRange: CMTimeRange) -> Self     convenience init(timeRange timeRange: CMTimeRange)     class func withTimeRange(_ timeRange: CMTimeRange) -> Self     init(url URL: URL, trackID trackID: CMPersistentTrackID, sourceTimeRange sourceTimeRange: CMTimeRange, targetTimeRange targetTimeRange: CMTimeRange)     init(timeRange timeRange: CMTimeRange)     var isEmpty: Bool { get }     var sourceURL: URL? { get }     var sourceTrackID: CMPersistentTrackID { get } } ``` |

Modified [AVCompositionTrackSegment.init(url: URL, trackID: CMPersistentTrackID, sourceTimeRange: CMTimeRange, targetTimeRange: CMTimeRange)](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/1390282-initwithurl)

|  | Declaration |
| --- | --- |
| From | ``` init(URL URL: NSURL, trackID trackID: CMPersistentTrackID, sourceTimeRange sourceTimeRange: CMTimeRange, targetTimeRange targetTimeRange: CMTimeRange) ``` |
| To | ``` init(url URL: URL, trackID trackID: CMPersistentTrackID, sourceTimeRange sourceTimeRange: CMTimeRange, targetTimeRange targetTimeRange: CMTimeRange) ``` |

Modified [AVCompositionTrackSegment.isEmpty](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/1389592-isempty)

|  | Declaration |
| --- | --- |
| From | ``` var empty: Bool { get } ``` |
| To | ``` var isEmpty: Bool { get } ``` |

Modified [AVCompositionTrackSegment.sourceURL](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/1386814-sourceurl)

|  | Declaration |
| --- | --- |
| From | ``` var sourceURL: NSURL? { get } ``` |
| To | ``` var sourceURL: URL? { get } ``` |

Modified [AVDateRangeMetadataGroup](https://developer.apple.com/documentation/avfoundation/avdaterangemetadatagroup)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVDateRangeMetadataGroup : AVMetadataGroup, NSCopying, NSMutableCopying {     init(items items: [AVMetadataItem], startDate startDate: NSDate, endDate endDate: NSDate?)     @NSCopying var startDate: NSDate { get }     @NSCopying var endDate: NSDate? { get }     var items: [AVMetadataItem] { get } } ``` | NSCopying, NSMutableCopying |
| To | ``` class AVDateRangeMetadataGroup : AVMetadataGroup, NSCopying, NSMutableCopying {     init(items items: [AVMetadataItem], start startDate: Date, end endDate: Date?)     var startDate: Date { get }     var endDate: Date? { get }     var items: [AVMetadataItem] { get }     var classifyingLabel: String? { get }     var uniqueID: String? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVDateRangeMetadataGroup : CVarArg { } extension AVDateRangeMetadataGroup : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSMutableCopying |

Modified [AVDateRangeMetadataGroup.endDate](https://developer.apple.com/documentation/avfoundation/avdaterangemetadatagroup/1386255-enddate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var endDate: NSDate? { get } ``` |
| To | ``` var endDate: Date? { get } ``` |

Modified [AVDateRangeMetadataGroup.init(items: [AVMetadataItem], start: Date, end: Date?)](https://developer.apple.com/documentation/avfoundation/avdaterangemetadatagroup/1389614-init)

|  | Declaration |
| --- | --- |
| From | ``` init(items items: [AVMetadataItem], startDate startDate: NSDate, endDate endDate: NSDate?) ``` |
| To | ``` init(items items: [AVMetadataItem], start startDate: Date, end endDate: Date?) ``` |

Modified [AVDateRangeMetadataGroup.startDate](https://developer.apple.com/documentation/avfoundation/avdaterangemetadatagroup/1386420-startdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var startDate: NSDate { get } ``` |
| To | ``` var startDate: Date { get } ``` |

Modified [AVError.Code [enum]](https://developer.apple.com/documentation/avfoundation/averror/code)

|  | Declaration |
| --- | --- |
| From | ``` enum AVError : Int {     case Unknown     case OutOfMemory     case SessionNotRunning     case DeviceAlreadyUsedByAnotherSession     case NoDataCaptured     case SessionConfigurationChanged     case DiskFull     case DeviceWasDisconnected     case MediaChanged     case MaximumDurationReached     case MaximumFileSizeReached     case MediaDiscontinuity     case MaximumNumberOfSamplesForFileFormatReached     case DeviceNotConnected     case DeviceInUseByAnotherApplication     case DeviceLockedForConfigurationByAnotherProcess     case SessionWasInterrupted     case MediaServicesWereReset     case ExportFailed     case DecodeFailed     case InvalidSourceMedia     case FileAlreadyExists     case CompositionTrackSegmentsNotContiguous     case InvalidCompositionTrackSegmentDuration     case InvalidCompositionTrackSegmentSourceStartTime     case InvalidCompositionTrackSegmentSourceDuration     case FileFormatNotRecognized     case FileFailedToParse     case MaximumStillImageCaptureRequestsExceeded     case ContentIsProtected     case NoImageAtTime     case DecoderNotFound     case EncoderNotFound     case ContentIsNotAuthorized     case ApplicationIsNotAuthorized     case DeviceIsNotAvailableInBackground     case OperationNotSupportedForAsset     case DecoderTemporarilyUnavailable     case EncoderTemporarilyUnavailable     case InvalidVideoComposition     case ReferenceForbiddenByReferencePolicy     case InvalidOutputURLPathExtension     case ScreenCaptureFailed     case DisplayWasDisabled     case TorchLevelUnavailable     case OperationInterrupted     case IncompatibleAsset     case FailedToLoadMediaData     case ServerIncorrectlyConfigured     case ApplicationIsNotAuthorizedToUseDevice     case FailedToParse     case FileTypeDoesNotSupportSampleReferences     case UndecodableMediaData     case AirPlayControllerRequiresInternet     case AirPlayReceiverRequiresInternet     case VideoCompositorFailed     case RecordingAlreadyInProgress } extension AVError : _BridgedNSError { } extension AVError : _BridgedNSError { } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = AVError         case unknown         case outOfMemory         case sessionNotRunning         case deviceAlreadyUsedByAnotherSession         case noDataCaptured         case sessionConfigurationChanged         case diskFull         case deviceWasDisconnected         case mediaChanged         case maximumDurationReached         case maximumFileSizeReached         case mediaDiscontinuity         case maximumNumberOfSamplesForFileFormatReached         case deviceNotConnected         case deviceInUseByAnotherApplication         case deviceLockedForConfigurationByAnotherProcess         case sessionWasInterrupted         case mediaServicesWereReset         case exportFailed         case decodeFailed         case invalidSourceMedia         case fileAlreadyExists         case compositionTrackSegmentsNotContiguous         case invalidCompositionTrackSegmentDuration         case invalidCompositionTrackSegmentSourceStartTime         case invalidCompositionTrackSegmentSourceDuration         case fileFormatNotRecognized         case fileFailedToParse         case maximumStillImageCaptureRequestsExceeded         case contentIsProtected         case noImageAtTime         case decoderNotFound         case encoderNotFound         case contentIsNotAuthorized         case applicationIsNotAuthorized         case deviceIsNotAvailableInBackground         case operationNotSupportedForAsset         case decoderTemporarilyUnavailable         case encoderTemporarilyUnavailable         case invalidVideoComposition         case referenceForbiddenByReferencePolicy         case invalidOutputURLPathExtension         case screenCaptureFailed         case displayWasDisabled         case torchLevelUnavailable         case operationInterrupted         case incompatibleAsset         case failedToLoadMediaData         case serverIncorrectlyConfigured         case applicationIsNotAuthorizedToUseDevice         case failedToParse         case fileTypeDoesNotSupportSampleReferences         case undecodableMediaData         case airPlayControllerRequiresInternet         case airPlayReceiverRequiresInternet         case videoCompositorFailed         case recordingAlreadyInProgress         case unsupportedOutputSettings         case operationNotAllowed     } ``` |

Modified [AVError.Code.airPlayControllerRequiresInternet](https://developer.apple.com/documentation/avfoundation/averror/averrorairplaycontrollerrequiresinternet)

|  | Declaration |
| --- | --- |
| From | ``` case AirPlayControllerRequiresInternet ``` |
| To | ``` case airPlayControllerRequiresInternet ``` |

Modified [AVError.Code.airPlayReceiverRequiresInternet](https://developer.apple.com/documentation/avfoundation/averror/code/airplayreceiverrequiresinternet)

|  | Declaration |
| --- | --- |
| From | ``` case AirPlayReceiverRequiresInternet ``` |
| To | ``` case airPlayReceiverRequiresInternet ``` |

Modified [AVError.Code.applicationIsNotAuthorized](https://developer.apple.com/documentation/avfoundation/averror/code/applicationisnotauthorized)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case ApplicationIsNotAuthorized ``` | tvOS 9.0 |
| To | ``` case applicationIsNotAuthorized ``` | tvOS 10.0 |

Modified [AVError.Code.applicationIsNotAuthorizedToUseDevice](https://developer.apple.com/documentation/avfoundation/averror/code/applicationisnotauthorizedtousedevice)

|  | Declaration |
| --- | --- |
| From | ``` case ApplicationIsNotAuthorizedToUseDevice ``` |
| To | ``` case applicationIsNotAuthorizedToUseDevice ``` |

Modified [AVError.Code.compositionTrackSegmentsNotContiguous](https://developer.apple.com/documentation/avfoundation/averror/averrorcompositiontracksegmentsnotcontiguous)

|  | Declaration |
| --- | --- |
| From | ``` case CompositionTrackSegmentsNotContiguous ``` |
| To | ``` case compositionTrackSegmentsNotContiguous ``` |

Modified [AVError.Code.contentIsNotAuthorized](https://developer.apple.com/documentation/avfoundation/averror/averrorcontentisnotauthorized)

|  | Declaration |
| --- | --- |
| From | ``` case ContentIsNotAuthorized ``` |
| To | ``` case contentIsNotAuthorized ``` |

Modified [AVError.Code.contentIsProtected](https://developer.apple.com/documentation/avfoundation/averror/code/contentisprotected)

|  | Declaration |
| --- | --- |
| From | ``` case ContentIsProtected ``` |
| To | ``` case contentIsProtected ``` |

Modified [AVError.Code.decodeFailed](https://developer.apple.com/documentation/avfoundation/averror/code/decodefailed)

|  | Declaration |
| --- | --- |
| From | ``` case DecodeFailed ``` |
| To | ``` case decodeFailed ``` |

Modified [AVError.Code.decoderNotFound](https://developer.apple.com/documentation/avfoundation/averror/code/decodernotfound)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case DecoderNotFound ``` | tvOS 9.0 |
| To | ``` case decoderNotFound ``` | tvOS 10.0 |

Modified [AVError.Code.decoderTemporarilyUnavailable](https://developer.apple.com/documentation/avfoundation/averror/code/decodertemporarilyunavailable)

|  | Declaration |
| --- | --- |
| From | ``` case DecoderTemporarilyUnavailable ``` |
| To | ``` case decoderTemporarilyUnavailable ``` |

Modified [AVError.Code.deviceAlreadyUsedByAnotherSession](https://developer.apple.com/documentation/avfoundation/averror/averrordevicealreadyusedbyanothersession)

|  | Declaration |
| --- | --- |
| From | ``` case DeviceAlreadyUsedByAnotherSession ``` |
| To | ``` case deviceAlreadyUsedByAnotherSession ``` |

Modified [AVError.Code.deviceInUseByAnotherApplication](https://developer.apple.com/documentation/avfoundation/averror/code/deviceinusebyanotherapplication)

|  | Declaration |
| --- | --- |
| From | ``` case DeviceInUseByAnotherApplication ``` |
| To | ``` case deviceInUseByAnotherApplication ``` |

Modified [AVError.Code.deviceIsNotAvailableInBackground](https://developer.apple.com/documentation/avfoundation/averror/averrordeviceisnotavailableinbackground)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case DeviceIsNotAvailableInBackground ``` | tvOS 9.0 |
| To | ``` case deviceIsNotAvailableInBackground ``` | tvOS 10.0 |

Modified [AVError.Code.deviceLockedForConfigurationByAnotherProcess](https://developer.apple.com/documentation/avfoundation/averror/averrordevicelockedforconfigurationbyanotherprocess)

|  | Declaration |
| --- | --- |
| From | ``` case DeviceLockedForConfigurationByAnotherProcess ``` |
| To | ``` case deviceLockedForConfigurationByAnotherProcess ``` |

Modified [AVError.Code.deviceNotConnected](https://developer.apple.com/documentation/avfoundation/averror/averrordevicenotconnected)

|  | Declaration |
| --- | --- |
| From | ``` case DeviceNotConnected ``` |
| To | ``` case deviceNotConnected ``` |

Modified [AVError.Code.deviceWasDisconnected](https://developer.apple.com/documentation/avfoundation/averror/code/devicewasdisconnected)

|  | Declaration |
| --- | --- |
| From | ``` case DeviceWasDisconnected ``` |
| To | ``` case deviceWasDisconnected ``` |

Modified [AVError.Code.diskFull](https://developer.apple.com/documentation/avfoundation/averror/averrordiskfull)

|  | Declaration |
| --- | --- |
| From | ``` case DiskFull ``` |
| To | ``` case diskFull ``` |

Modified [AVError.Code.displayWasDisabled](https://developer.apple.com/documentation/avfoundation/averror/averrordisplaywasdisabled)

|  | Declaration |
| --- | --- |
| From | ``` case DisplayWasDisabled ``` |
| To | ``` case displayWasDisabled ``` |

Modified [AVError.Code.encoderNotFound](https://developer.apple.com/documentation/avfoundation/averror/code/encodernotfound)

|  | Declaration |
| --- | --- |
| From | ``` case EncoderNotFound ``` |
| To | ``` case encoderNotFound ``` |

Modified [AVError.Code.encoderTemporarilyUnavailable](https://developer.apple.com/documentation/avfoundation/averror/averrorencodertemporarilyunavailable)

|  | Declaration |
| --- | --- |
| From | ``` case EncoderTemporarilyUnavailable ``` |
| To | ``` case encoderTemporarilyUnavailable ``` |

Modified [AVError.Code.exportFailed](https://developer.apple.com/documentation/avfoundation/averror/averrorexportfailed)

|  | Declaration |
| --- | --- |
| From | ``` case ExportFailed ``` |
| To | ``` case exportFailed ``` |

Modified [AVError.Code.failedToLoadMediaData](https://developer.apple.com/documentation/avfoundation/averror/code/failedtoloadmediadata)

|  | Declaration |
| --- | --- |
| From | ``` case FailedToLoadMediaData ``` |
| To | ``` case failedToLoadMediaData ``` |

Modified [AVError.Code.failedToParse](https://developer.apple.com/documentation/avfoundation/averror/averrorfailedtoparse)

|  | Declaration |
| --- | --- |
| From | ``` case FailedToParse ``` |
| To | ``` case failedToParse ``` |

Modified [AVError.Code.fileAlreadyExists](https://developer.apple.com/documentation/avfoundation/averror/averrorfilealreadyexists)

|  | Declaration |
| --- | --- |
| From | ``` case FileAlreadyExists ``` |
| To | ``` case fileAlreadyExists ``` |

Modified [AVError.Code.fileFailedToParse](https://developer.apple.com/documentation/avfoundation/averror/code/filefailedtoparse)

|  | Declaration |
| --- | --- |
| From | ``` case FileFailedToParse ``` |
| To | ``` case fileFailedToParse ``` |

Modified [AVError.Code.fileFormatNotRecognized](https://developer.apple.com/documentation/avfoundation/averror/code/fileformatnotrecognized)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case FileFormatNotRecognized ``` | tvOS 9.0 |
| To | ``` case fileFormatNotRecognized ``` | tvOS 10.0 |

Modified [AVError.Code.fileTypeDoesNotSupportSampleReferences](https://developer.apple.com/documentation/avfoundation/averror/averrorfiletypedoesnotsupportsamplereferences)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case FileTypeDoesNotSupportSampleReferences ``` | tvOS 9.0 |
| To | ``` case fileTypeDoesNotSupportSampleReferences ``` | tvOS 10.0 |

Modified [AVError.Code.incompatibleAsset](https://developer.apple.com/documentation/avfoundation/averror/averrorincompatibleasset)

|  | Declaration |
| --- | --- |
| From | ``` case IncompatibleAsset ``` |
| To | ``` case incompatibleAsset ``` |

Modified [AVError.Code.invalidCompositionTrackSegmentDuration](https://developer.apple.com/documentation/avfoundation/averror/code/invalidcompositiontracksegmentduration)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidCompositionTrackSegmentDuration ``` |
| To | ``` case invalidCompositionTrackSegmentDuration ``` |

Modified [AVError.Code.invalidCompositionTrackSegmentSourceDuration](https://developer.apple.com/documentation/avfoundation/averror/code/invalidcompositiontracksegmentsourceduration)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case InvalidCompositionTrackSegmentSourceDuration ``` | tvOS 9.0 |
| To | ``` case invalidCompositionTrackSegmentSourceDuration ``` | tvOS 10.0 |

Modified [AVError.Code.invalidCompositionTrackSegmentSourceStartTime](https://developer.apple.com/documentation/avfoundation/averror/averrorinvalidcompositiontracksegmentsourcestarttime)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidCompositionTrackSegmentSourceStartTime ``` |
| To | ``` case invalidCompositionTrackSegmentSourceStartTime ``` |

Modified [AVError.Code.invalidOutputURLPathExtension](https://developer.apple.com/documentation/avfoundation/averror/averrorinvalidoutputurlpathextension)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidOutputURLPathExtension ``` |
| To | ``` case invalidOutputURLPathExtension ``` |

Modified [AVError.Code.invalidSourceMedia](https://developer.apple.com/documentation/avfoundation/averror/averrorinvalidsourcemedia)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidSourceMedia ``` |
| To | ``` case invalidSourceMedia ``` |

Modified [AVError.Code.invalidVideoComposition](https://developer.apple.com/documentation/avfoundation/averror/code/invalidvideocomposition)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidVideoComposition ``` |
| To | ``` case invalidVideoComposition ``` |

Modified [AVError.Code.maximumDurationReached](https://developer.apple.com/documentation/avfoundation/averror/code/maximumdurationreached)

|  | Declaration |
| --- | --- |
| From | ``` case MaximumDurationReached ``` |
| To | ``` case maximumDurationReached ``` |

Modified [AVError.Code.maximumFileSizeReached](https://developer.apple.com/documentation/avfoundation/averror/code/maximumfilesizereached)

|  | Declaration |
| --- | --- |
| From | ``` case MaximumFileSizeReached ``` |
| To | ``` case maximumFileSizeReached ``` |

Modified [AVError.Code.maximumNumberOfSamplesForFileFormatReached](https://developer.apple.com/documentation/avfoundation/averror/averrormaximumnumberofsamplesforfileformatreached)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case MaximumNumberOfSamplesForFileFormatReached ``` | tvOS 9.0 |
| To | ``` case maximumNumberOfSamplesForFileFormatReached ``` | tvOS 10.0 |

Modified [AVError.Code.maximumStillImageCaptureRequestsExceeded](https://developer.apple.com/documentation/avfoundation/averror/averrormaximumstillimagecapturerequestsexceeded)

|  | Declaration |
| --- | --- |
| From | ``` case MaximumStillImageCaptureRequestsExceeded ``` |
| To | ``` case maximumStillImageCaptureRequestsExceeded ``` |

Modified [AVError.Code.mediaChanged](https://developer.apple.com/documentation/avfoundation/averror/averrormediachanged)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case MediaChanged ``` | tvOS 9.0 |
| To | ``` case mediaChanged ``` | tvOS 10.0 |

Modified [AVError.Code.mediaDiscontinuity](https://developer.apple.com/documentation/avfoundation/averror/averrormediadiscontinuity)

|  | Declaration |
| --- | --- |
| From | ``` case MediaDiscontinuity ``` |
| To | ``` case mediaDiscontinuity ``` |

Modified [AVError.Code.mediaServicesWereReset](https://developer.apple.com/documentation/avfoundation/averror/code/mediaserviceswerereset)

|  | Declaration |
| --- | --- |
| From | ``` case MediaServicesWereReset ``` |
| To | ``` case mediaServicesWereReset ``` |

Modified [AVError.Code.noDataCaptured](https://developer.apple.com/documentation/avfoundation/averror/code/nodatacaptured)

|  | Declaration |
| --- | --- |
| From | ``` case NoDataCaptured ``` |
| To | ``` case noDataCaptured ``` |

Modified [AVError.Code.noImageAtTime](https://developer.apple.com/documentation/avfoundation/averror/averrornoimageattime)

|  | Declaration |
| --- | --- |
| From | ``` case NoImageAtTime ``` |
| To | ``` case noImageAtTime ``` |

Modified [AVError.Code.operationInterrupted](https://developer.apple.com/documentation/avfoundation/averror/code/operationinterrupted)

|  | Declaration |
| --- | --- |
| From | ``` case OperationInterrupted ``` |
| To | ``` case operationInterrupted ``` |

Modified [AVError.Code.operationNotSupportedForAsset](https://developer.apple.com/documentation/avfoundation/averror/averroroperationnotsupportedforasset)

|  | Declaration |
| --- | --- |
| From | ``` case OperationNotSupportedForAsset ``` |
| To | ``` case operationNotSupportedForAsset ``` |

Modified [AVError.Code.outOfMemory](https://developer.apple.com/documentation/avfoundation/averror/averroroutofmemory)

|  | Declaration |
| --- | --- |
| From | ``` case OutOfMemory ``` |
| To | ``` case outOfMemory ``` |

Modified [AVError.Code.recordingAlreadyInProgress](https://developer.apple.com/documentation/avfoundation/averror/code/recordingalreadyinprogress)

|  | Declaration |
| --- | --- |
| From | ``` case RecordingAlreadyInProgress ``` |
| To | ``` case recordingAlreadyInProgress ``` |

Modified [AVError.Code.referenceForbiddenByReferencePolicy](https://developer.apple.com/documentation/avfoundation/averror/averrorreferenceforbiddenbyreferencepolicy)

|  | Declaration |
| --- | --- |
| From | ``` case ReferenceForbiddenByReferencePolicy ``` |
| To | ``` case referenceForbiddenByReferencePolicy ``` |

Modified [AVError.Code.screenCaptureFailed](https://developer.apple.com/documentation/avfoundation/averror/averrorscreencapturefailed)

|  | Declaration |
| --- | --- |
| From | ``` case ScreenCaptureFailed ``` |
| To | ``` case screenCaptureFailed ``` |

Modified [AVError.Code.serverIncorrectlyConfigured](https://developer.apple.com/documentation/avfoundation/averror/code/serverincorrectlyconfigured)

|  | Declaration |
| --- | --- |
| From | ``` case ServerIncorrectlyConfigured ``` |
| To | ``` case serverIncorrectlyConfigured ``` |

Modified [AVError.Code.sessionConfigurationChanged](https://developer.apple.com/documentation/avfoundation/averror/averrorsessionconfigurationchanged)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case SessionConfigurationChanged ``` | tvOS 9.0 |
| To | ``` case sessionConfigurationChanged ``` | tvOS 10.0 |

Modified [AVError.Code.sessionNotRunning](https://developer.apple.com/documentation/avfoundation/averror/averrorsessionnotrunning)

|  | Declaration |
| --- | --- |
| From | ``` case SessionNotRunning ``` |
| To | ``` case sessionNotRunning ``` |

Modified [AVError.Code.sessionWasInterrupted](https://developer.apple.com/documentation/avfoundation/averror/averrorsessionwasinterrupted)

|  | Declaration |
| --- | --- |
| From | ``` case SessionWasInterrupted ``` |
| To | ``` case sessionWasInterrupted ``` |

Modified [AVError.Code.torchLevelUnavailable](https://developer.apple.com/documentation/avfoundation/averror/code/torchlevelunavailable)

|  | Declaration |
| --- | --- |
| From | ``` case TorchLevelUnavailable ``` |
| To | ``` case torchLevelUnavailable ``` |

Modified [AVError.Code.undecodableMediaData](https://developer.apple.com/documentation/avfoundation/averror/code/undecodablemediadata)

|  | Declaration |
| --- | --- |
| From | ``` case UndecodableMediaData ``` |
| To | ``` case undecodableMediaData ``` |

Modified [AVError.Code.unknown](https://developer.apple.com/documentation/avfoundation/averror/averrorunknown)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case Unknown ``` | tvOS 9.0 |
| To | ``` case unknown ``` | tvOS 10.0 |

Modified [AVError.Code.videoCompositorFailed](https://developer.apple.com/documentation/avfoundation/averror/averrorvideocompositorfailed)

|  | Declaration |
| --- | --- |
| From | ``` case VideoCompositorFailed ``` |
| To | ``` case videoCompositorFailed ``` |

Modified [AVFragmentedAsset.track(withTrackID: CMPersistentTrackID) -> AVFragmentedAssetTrack?](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/1385712-trackwithtrackid)

|  | Declaration |
| --- | --- |
| From | ``` func trackWithTrackID(_ trackID: CMPersistentTrackID) -> AVFragmentedAssetTrack? ``` |
| To | ``` func track(withTrackID trackID: CMPersistentTrackID) -> AVFragmentedAssetTrack? ``` |

Modified [AVFragmentedAsset.tracks(withMediaCharacteristic: String) -> [AVFragmentedAssetTrack]](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/1387259-tracks)

|  | Declaration |
| --- | --- |
| From | ``` func tracksWithMediaCharacteristic(_ mediaCharacteristic: String) -> [AVFragmentedAssetTrack] ``` |
| To | ``` func tracks(withMediaCharacteristic mediaCharacteristic: String) -> [AVFragmentedAssetTrack] ``` |

Modified [AVFragmentedAsset.tracks(withMediaType: String) -> [AVFragmentedAssetTrack]](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/1387253-tracks)

|  | Declaration |
| --- | --- |
| From | ``` func tracksWithMediaType(_ mediaType: String) -> [AVFragmentedAssetTrack] ``` |
| To | ``` func tracks(withMediaType mediaType: String) -> [AVFragmentedAssetTrack] ``` |

Modified [AVFragmentMinding](https://developer.apple.com/documentation/avfoundation/avfragmentminding)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVFragmentMinding {     var associatedWithFragmentMinder: Bool { get } } ``` |
| To | ``` protocol AVFragmentMinding {     var isAssociatedWithFragmentMinder: Bool { get } } ``` |

Modified [AVKeyValueStatus [enum]](https://developer.apple.com/documentation/avfoundation/avkeyvaluestatus)

|  | Declaration |
| --- | --- |
| From | ``` enum AVKeyValueStatus : Int {     case Unknown     case Loading     case Loaded     case Failed     case Cancelled } ``` |
| To | ``` enum AVKeyValueStatus : Int {     case unknown     case loading     case loaded     case failed     case cancelled } ``` |

Modified [AVKeyValueStatus.cancelled](https://developer.apple.com/documentation/avfoundation/avkeyvaluestatus/cancelled)

|  | Declaration |
| --- | --- |
| From | ``` case Cancelled ``` |
| To | ``` case cancelled ``` |

Modified [AVKeyValueStatus.failed](https://developer.apple.com/documentation/avfoundation/avkeyvaluestatus/failed)

|  | Declaration |
| --- | --- |
| From | ``` case Failed ``` |
| To | ``` case failed ``` |

Modified [AVKeyValueStatus.loaded](https://developer.apple.com/documentation/avfoundation/avkeyvaluestatus/avkeyvaluestatusloaded)

|  | Declaration |
| --- | --- |
| From | ``` case Loaded ``` |
| To | ``` case loaded ``` |

Modified [AVKeyValueStatus.loading](https://developer.apple.com/documentation/avfoundation/avkeyvaluestatus/loading)

|  | Declaration |
| --- | --- |
| From | ``` case Loading ``` |
| To | ``` case loading ``` |

Modified [AVKeyValueStatus.unknown](https://developer.apple.com/documentation/avfoundation/avkeyvaluestatus/avkeyvaluestatusunknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [AVMediaSelection](https://developer.apple.com/documentation/avfoundation/avmediaselection)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVMediaSelection : NSObject, NSCopying, NSMutableCopying {     weak var asset: AVAsset? { get }     func selectedMediaOptionInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption?     func mediaSelectionCriteriaCanBeAppliedAutomaticallyToMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup) -> Bool } ``` | NSCopying, NSMutableCopying |
| To | ``` class AVMediaSelection : NSObject, NSCopying, NSMutableCopying {     weak var asset: AVAsset? { get }     func selectedMediaOption(in mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption?     func mediaSelectionCriteriaCanBeAppliedAutomatically(to mediaSelectionGroup: AVMediaSelectionGroup) -> Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVMediaSelection : CVarArg { } extension AVMediaSelection : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSMutableCopying |

Modified [AVMediaSelection.mediaSelectionCriteriaCanBeAppliedAutomatically(to: AVMediaSelectionGroup) -> Bool](https://developer.apple.com/documentation/avfoundation/avmediaselection/1386716-mediaselectioncriteriacanbeappli)

|  | Declaration |
| --- | --- |
| From | ``` func mediaSelectionCriteriaCanBeAppliedAutomaticallyToMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup) -> Bool ``` |
| To | ``` func mediaSelectionCriteriaCanBeAppliedAutomatically(to mediaSelectionGroup: AVMediaSelectionGroup) -> Bool ``` |

Modified [AVMediaSelection.selectedMediaOption(in: AVMediaSelectionGroup) -> AVMediaSelectionOption?](https://developer.apple.com/documentation/avfoundation/avmediaselection/1389197-selectedmediaoptioninmediaselect)

|  | Declaration |
| --- | --- |
| From | ``` func selectedMediaOptionInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption? ``` |
| To | ``` func selectedMediaOption(in mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption? ``` |

Modified [AVMediaSelectionGroup](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVMediaSelectionGroup : NSObject, NSCopying {     var options: [AVMediaSelectionOption] { get }     var defaultOption: AVMediaSelectionOption? { get }     var allowsEmptySelection: Bool { get }     func mediaSelectionOptionWithPropertyList(_ plist: AnyObject) -> AVMediaSelectionOption? } extension AVMediaSelectionGroup {     class func playableMediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AVMediaSelectionOption]) -> [AVMediaSelectionOption]     class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AVMediaSelectionOption], filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [String]) -> [AVMediaSelectionOption]     class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AVMediaSelectionOption], withLocale locale: NSLocale) -> [AVMediaSelectionOption]     class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AVMediaSelectionOption], withMediaCharacteristics mediaCharacteristics: [String]) -> [AVMediaSelectionOption]     class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AVMediaSelectionOption], withoutMediaCharacteristics mediaCharacteristics: [String]) -> [AVMediaSelectionOption] } extension AVMediaSelectionGroup {     func makeNowPlayingInfoLanguageOptionGroup() -> MPNowPlayingInfoLanguageOptionGroup } ``` | NSCopying |
| To | ``` class AVMediaSelectionGroup : NSObject, NSCopying {     var options: [AVMediaSelectionOption] { get }     var defaultOption: AVMediaSelectionOption? { get }     var allowsEmptySelection: Bool { get }     func mediaSelectionOption(withPropertyList plist: Any) -> AVMediaSelectionOption?     class func playableMediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption]) -> [AVMediaSelectionOption]     class func mediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption], filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [String]) -> [AVMediaSelectionOption]     class func mediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption], with locale: Locale) -> [AVMediaSelectionOption]     class func mediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption], withMediaCharacteristics mediaCharacteristics: [String]) -> [AVMediaSelectionOption]     class func mediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption], withoutMediaCharacteristics mediaCharacteristics: [String]) -> [AVMediaSelectionOption]     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVMediaSelectionGroup : CVarArg { } extension AVMediaSelectionGroup : Equatable, Hashable {     var hashValue: Int { get } } extension AVMediaSelectionGroup {     class func playableMediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption]) -> [AVMediaSelectionOption]     class func mediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption], filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [String]) -> [AVMediaSelectionOption]     class func mediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption], with locale: Locale) -> [AVMediaSelectionOption]     class func mediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption], withMediaCharacteristics mediaCharacteristics: [String]) -> [AVMediaSelectionOption]     class func mediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption], withoutMediaCharacteristics mediaCharacteristics: [String]) -> [AVMediaSelectionOption] } extension AVMediaSelectionGroup {     func makeNowPlayingInfoLanguageOptionGroup() -> MPNowPlayingInfoLanguageOptionGroup } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [AVMediaSelectionGroup.mediaSelectionOption(withPropertyList: Any) -> AVMediaSelectionOption?](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1389968-mediaselectionoption)

|  | Declaration |
| --- | --- |
| From | ``` func mediaSelectionOptionWithPropertyList(_ plist: AnyObject) -> AVMediaSelectionOption? ``` |
| To | ``` func mediaSelectionOption(withPropertyList plist: Any) -> AVMediaSelectionOption? ``` |

Modified [AVMediaSelectionGroup.mediaSelectionOptions(from: [AVMediaSelectionOption], filteredAndSortedAccordingToPreferredLanguages: [String]) -> [AVMediaSelectionOption] [class]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1387034-mediaselectionoptions)

|  | Declaration |
| --- | --- |
| From | ``` class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AVMediaSelectionOption], filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [String]) -> [AVMediaSelectionOption] ``` |
| To | ``` class func mediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption], filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [String]) -> [AVMediaSelectionOption] ``` |

Modified [AVMediaSelectionGroup.mediaSelectionOptions(from: [AVMediaSelectionOption], with: Locale) -> [AVMediaSelectionOption] [class]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1387494-mediaselectionoptionsfromarray)

|  | Declaration |
| --- | --- |
| From | ``` class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AVMediaSelectionOption], withLocale locale: NSLocale) -> [AVMediaSelectionOption] ``` |
| To | ``` class func mediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption], with locale: Locale) -> [AVMediaSelectionOption] ``` |

Modified [AVMediaSelectionGroup.mediaSelectionOptions(from: [AVMediaSelectionOption], withMediaCharacteristics: [String]) -> [AVMediaSelectionOption] [class]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1388258-mediaselectionoptions)

|  | Declaration |
| --- | --- |
| From | ``` class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AVMediaSelectionOption], withMediaCharacteristics mediaCharacteristics: [String]) -> [AVMediaSelectionOption] ``` |
| To | ``` class func mediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption], withMediaCharacteristics mediaCharacteristics: [String]) -> [AVMediaSelectionOption] ``` |

Modified [AVMediaSelectionGroup.mediaSelectionOptions(from: [AVMediaSelectionOption], withoutMediaCharacteristics: [String]) -> [AVMediaSelectionOption] [class]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1387631-mediaselectionoptionsfromarray)

|  | Declaration |
| --- | --- |
| From | ``` class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AVMediaSelectionOption], withoutMediaCharacteristics mediaCharacteristics: [String]) -> [AVMediaSelectionOption] ``` |
| To | ``` class func mediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption], withoutMediaCharacteristics mediaCharacteristics: [String]) -> [AVMediaSelectionOption] ``` |

Modified [AVMediaSelectionGroup.playableMediaSelectionOptions(from: [AVMediaSelectionOption]) -> [AVMediaSelectionOption] [class]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1387351-playablemediaselectionoptions)

|  | Declaration |
| --- | --- |
| From | ``` class func playableMediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AVMediaSelectionOption]) -> [AVMediaSelectionOption] ``` |
| To | ``` class func playableMediaSelectionOptions(from mediaSelectionOptions: [AVMediaSelectionOption]) -> [AVMediaSelectionOption] ``` |

Modified [AVMediaSelectionOption](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVMediaSelectionOption : NSObject, NSCopying {     var mediaType: String { get }     var mediaSubTypes: [NSNumber] { get }     func hasMediaCharacteristic(_ mediaCharacteristic: String) -> Bool     var playable: Bool { get }     var extendedLanguageTag: String? { get }     var locale: NSLocale? { get }     var commonMetadata: [AVMetadataItem] { get }     var availableMetadataFormats: [String] { get }     func metadataForFormat(_ format: String) -> [AVMetadataItem]     func associatedMediaSelectionOptionInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption?     func propertyList() -> AnyObject     func displayNameWithLocale(_ locale: NSLocale) -> String     var displayName: String { get } } extension AVMediaSelectionOption {     func makeNowPlayingInfoLanguageOption() -> MPNowPlayingInfoLanguageOption? } ``` | NSCopying |
| To | ``` class AVMediaSelectionOption : NSObject, NSCopying {     var mediaType: String { get }     var mediaSubTypes: [NSNumber] { get }     func hasMediaCharacteristic(_ mediaCharacteristic: String) -> Bool     var isPlayable: Bool { get }     var extendedLanguageTag: String? { get }     var locale: Locale? { get }     var commonMetadata: [AVMetadataItem] { get }     var availableMetadataFormats: [String] { get }     func metadata(forFormat format: String) -> [AVMetadataItem]     func associatedMediaSelectionOption(in mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption?     func propertyList() -> Any     func displayName(with locale: Locale) -> String     var displayName: String { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVMediaSelectionOption : CVarArg { } extension AVMediaSelectionOption : Equatable, Hashable {     var hashValue: Int { get } } extension AVMediaSelectionOption {     func makeNowPlayingInfoLanguageOption() -> MPNowPlayingInfoLanguageOption? } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [AVMediaSelectionOption.associatedMediaSelectionOption(in: AVMediaSelectionGroup) -> AVMediaSelectionOption?](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1388232-associatedmediaselectionoption)

|  | Declaration |
| --- | --- |
| From | ``` func associatedMediaSelectionOptionInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption? ``` |
| To | ``` func associatedMediaSelectionOption(in mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption? ``` |

Modified [AVMediaSelectionOption.displayName(with: Locale) -> String](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1388021-displayname)

|  | Declaration |
| --- | --- |
| From | ``` func displayNameWithLocale(_ locale: NSLocale) -> String ``` |
| To | ``` func displayName(with locale: Locale) -> String ``` |

Modified [AVMediaSelectionOption.isPlayable](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1390917-playable)

|  | Declaration |
| --- | --- |
| From | ``` var playable: Bool { get } ``` |
| To | ``` var isPlayable: Bool { get } ``` |

Modified [AVMediaSelectionOption.locale](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1388436-locale)

|  | Declaration |
| --- | --- |
| From | ``` var locale: NSLocale? { get } ``` |
| To | ``` var locale: Locale? { get } ``` |

Modified [AVMediaSelectionOption.metadata(forFormat: String) -> [AVMetadataItem]](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1386666-metadataforformat)

|  | Declaration |
| --- | --- |
| From | ``` func metadataForFormat(_ format: String) -> [AVMetadataItem] ``` |
| To | ``` func metadata(forFormat format: String) -> [AVMetadataItem] ``` |

Modified [AVMediaSelectionOption.propertyList() -> Any](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1386310-propertylist)

|  | Declaration |
| --- | --- |
| From | ``` func propertyList() -> AnyObject ``` |
| To | ``` func propertyList() -> Any ``` |

Modified [AVMetadataGroup](https://developer.apple.com/documentation/avfoundation/avmetadatagroup)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVMetadataGroup : NSObject {     var items: [AVMetadataItem] { get } } extension AVMetadataGroup {     var classifyingLabel: String? { get }     var uniqueID: String? { get } } ``` | -- |
| To | ``` class AVMetadataGroup : NSObject {     var items: [AVMetadataItem] { get }     var classifyingLabel: String? { get }     var uniqueID: String? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVMetadataGroup : CVarArg { } extension AVMetadataGroup : Equatable, Hashable {     var hashValue: Int { get } } extension AVMetadataGroup {     var classifyingLabel: String? { get }     var uniqueID: String? { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVMetadataItem](https://developer.apple.com/documentation/avfoundation/avmetadataitem)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVMetadataItem : NSObject, AVAsynchronousKeyValueLoading, NSCopying, NSMutableCopying {     var identifier: String? { get }     var extendedLanguageTag: String? { get }     @NSCopying var locale: NSLocale? { get }     var time: CMTime { get }     var duration: CMTime { get }     var dataType: String? { get }     @NSCopying var value: protocol<NSCopying, NSObjectProtocol>? { get }     var extraAttributes: [String : AnyObject]? { get } } extension AVMetadataItem {     @NSCopying var startDate: NSDate? { get } } extension AVMetadataItem {     var stringValue: String? { get }     var numberValue: NSNumber? { get }     var dateValue: NSDate? { get }     var dataValue: NSData? { get } } extension AVMetadataItem {     func statusOfValueForKey(_ key: String, error outError: NSErrorPointer) -> AVKeyValueStatus     func loadValuesAsynchronouslyForKeys(_ keys: [String], completionHandler handler: (() -> Void)?) } extension AVMetadataItem {     class func metadataItemsFromArray(_ metadataItems: [AVMetadataItem], filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [String]) -> [AVMetadataItem]     class func metadataItemsFromArray(_ metadataItems: [AVMetadataItem], filteredByIdentifier identifier: String) -> [AVMetadataItem]     class func metadataItemsFromArray(_ metadataItems: [AVMetadataItem], filteredByMetadataItemFilter metadataItemFilter: AVMetadataItemFilter) -> [AVMetadataItem] } extension AVMetadataItem {     class func identifierForKey(_ key: AnyObject, keySpace keySpace: String) -> String?     class func keySpaceForIdentifier(_ identifier: String) -> String?     class func keyForIdentifier(_ identifier: String) -> AnyObject?     @NSCopying var key: protocol<NSCopying, NSObjectProtocol>? { get }     var commonKey: String? { get }     var keySpace: String? { get } } extension AVMetadataItem {      init(propertiesOfMetadataItem metadataItem: AVMetadataItem, valueLoadingHandler handler: (AVMetadataItemValueRequest) -> Void)     class func metadataItemWithPropertiesOfMetadataItem(_ metadataItem: AVMetadataItem, valueLoadingHandler handler: (AVMetadataItemValueRequest) -> Void) -> AVMetadataItem } extension AVMetadataItem {     class func metadataItemsFromArray(_ metadataItems: [AVMetadataItem], withLocale locale: NSLocale) -> [AVMetadataItem]     class func metadataItemsFromArray(_ metadataItems: [AVMetadataItem], withKey key: AnyObject?, keySpace keySpace: String?) -> [AVMetadataItem] } ``` | AVAsynchronousKeyValueLoading, NSCopying, NSMutableCopying |
| To | ``` class AVMetadataItem : NSObject, AVAsynchronousKeyValueLoading, NSCopying, NSMutableCopying {     var identifier: String? { get }     var extendedLanguageTag: String? { get }     var locale: Locale? { get }     var time: CMTime { get }     var duration: CMTime { get }     var dataType: String? { get }     @NSCopying var value: (NSCopying & NSObjectProtocol)? { get }     var extraAttributes: [String : Any]? { get }     class func metadataItems(from metadataItems: [AVMetadataItem], with locale: Locale) -> [AVMetadataItem]     class func metadataItems(from metadataItems: [AVMetadataItem], withKey key: Any?, keySpace keySpace: String?) -> [AVMetadataItem]      init(propertiesOf metadataItem: AVMetadataItem, valueLoadingHandler handler: @escaping (AVMetadataItemValueRequest) -> Swift.Void)     class func withPropertiesOf(_ metadataItem: AVMetadataItem, valueLoadingHandler handler: @escaping (AVMetadataItemValueRequest) -> Swift.Void) -> AVMetadataItem     class func identifier(forKey key: Any, keySpace keySpace: String) -> String?     class func keySpace(forIdentifier identifier: String) -> String?     class func key(forIdentifier identifier: String) -> Any?     @NSCopying var key: (NSCopying & NSObjectProtocol)? { get }     var commonKey: String? { get }     var keySpace: String? { get }     class func metadataItems(from metadataItems: [AVMetadataItem], filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [String]) -> [AVMetadataItem]     class func metadataItems(from metadataItems: [AVMetadataItem], filteredByIdentifier identifier: String) -> [AVMetadataItem]     class func metadataItems(from metadataItems: [AVMetadataItem], filteredBy metadataItemFilter: AVMetadataItemFilter) -> [AVMetadataItem]     func statusOfValue(forKey key: String, error outError: NSErrorPointer) -> AVKeyValueStatus     func loadValuesAsynchronously(forKeys keys: [String], completionHandler handler: (@escaping () -> Swift.Void)? = nil)     var stringValue: String? { get }     var numberValue: NSNumber? { get }     var dateValue: Date? { get }     var dataValue: Data? { get }     var startDate: Date? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVMetadataItem : CVarArg { } extension AVMetadataItem : Equatable, Hashable {     var hashValue: Int { get } } extension AVMetadataItem {     var startDate: Date? { get } } extension AVMetadataItem {     var stringValue: String? { get }     var numberValue: NSNumber? { get }     var dateValue: Date? { get }     var dataValue: Data? { get } } extension AVMetadataItem {     func statusOfValue(forKey key: String, error outError: NSErrorPointer) -> AVKeyValueStatus     func loadValuesAsynchronously(forKeys keys: [String], completionHandler handler: (@escaping () -> Swift.Void)? = nil) } extension AVMetadataItem {     class func metadataItems(from metadataItems: [AVMetadataItem], filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [String]) -> [AVMetadataItem]     class func metadataItems(from metadataItems: [AVMetadataItem], filteredByIdentifier identifier: String) -> [AVMetadataItem]     class func metadataItems(from metadataItems: [AVMetadataItem], filteredBy metadataItemFilter: AVMetadataItemFilter) -> [AVMetadataItem] } extension AVMetadataItem {     class func identifier(forKey key: Any, keySpace keySpace: String) -> String?     class func keySpace(forIdentifier identifier: String) -> String?     class func key(forIdentifier identifier: String) -> Any?     @NSCopying var key: (NSCopying & NSObjectProtocol)? { get }     var commonKey: String? { get }     var keySpace: String? { get } } extension AVMetadataItem {      init(propertiesOf metadataItem: AVMetadataItem, valueLoadingHandler handler: @escaping (AVMetadataItemValueRequest) -> Swift.Void)     class func withPropertiesOf(_ metadataItem: AVMetadataItem, valueLoadingHandler handler: @escaping (AVMetadataItemValueRequest) -> Swift.Void) -> AVMetadataItem } extension AVMetadataItem {     class func metadataItems(from metadataItems: [AVMetadataItem], with locale: Locale) -> [AVMetadataItem]     class func metadataItems(from metadataItems: [AVMetadataItem], withKey key: Any?, keySpace keySpace: String?) -> [AVMetadataItem] } ``` | AVAsynchronousKeyValueLoading, CVarArg, Equatable, Hashable, NSCopying, NSMutableCopying |

Modified [AVMetadataItem.dataValue](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387641-datavalue)

|  | Declaration |
| --- | --- |
| From | ``` var dataValue: NSData? { get } ``` |
| To | ``` var dataValue: Data? { get } ``` |

Modified [AVMetadataItem.dateValue](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1385563-datevalue)

|  | Declaration |
| --- | --- |
| From | ``` var dateValue: NSDate? { get } ``` |
| To | ``` var dateValue: Date? { get } ``` |

Modified [AVMetadataItem.extraAttributes](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1389570-extraattributes)

|  | Declaration |
| --- | --- |
| From | ``` var extraAttributes: [String : AnyObject]? { get } ``` |
| To | ``` var extraAttributes: [String : Any]? { get } ``` |

Modified [AVMetadataItem.identifier(forKey: Any, keySpace: String) -> String? [class]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387869-identifier)

|  | Declaration |
| --- | --- |
| From | ``` class func identifierForKey(_ key: AnyObject, keySpace keySpace: String) -> String? ``` |
| To | ``` class func identifier(forKey key: Any, keySpace keySpace: String) -> String? ``` |

Modified [AVMetadataItem.init(propertiesOf: AVMetadataItem, valueLoadingHandler: (AVMetadataItemValueRequest) -> Swift.Void)](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387745-metadataitemwithpropertiesofmeta)

|  | Declaration |
| --- | --- |
| From | ``` init(propertiesOfMetadataItem metadataItem: AVMetadataItem, valueLoadingHandler handler: (AVMetadataItemValueRequest) -> Void) ``` |
| To | ``` init(propertiesOf metadataItem: AVMetadataItem, valueLoadingHandler handler: @escaping (AVMetadataItemValueRequest) -> Swift.Void) ``` |

Modified [AVMetadataItem.key](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387843-key)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var key: protocol<NSCopying, NSObjectProtocol>? { get } ``` |
| To | ``` @NSCopying var key: (NSCopying & NSObjectProtocol)? { get } ``` |

Modified [AVMetadataItem.key(forIdentifier: String) -> Any? [class]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1385613-keyforidentifier)

|  | Declaration |
| --- | --- |
| From | ``` class func keyForIdentifier(_ identifier: String) -> AnyObject? ``` |
| To | ``` class func key(forIdentifier identifier: String) -> Any? ``` |

Modified [AVMetadataItem.keySpace(forIdentifier: String) -> String? [class]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1390663-keyspaceforidentifier)

|  | Declaration |
| --- | --- |
| From | ``` class func keySpaceForIdentifier(_ identifier: String) -> String? ``` |
| To | ``` class func keySpace(forIdentifier identifier: String) -> String? ``` |

Modified [AVMetadataItem.loadValuesAsynchronously(forKeys: [String], completionHandler: ( () -> Swift.Void)?)](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387102-loadvaluesasynchronouslyforkeys)

|  | Declaration |
| --- | --- |
| From | ``` func loadValuesAsynchronouslyForKeys(_ keys: [String], completionHandler handler: (() -> Void)?) ``` |
| To | ``` func loadValuesAsynchronously(forKeys keys: [String], completionHandler handler: (@escaping () -> Swift.Void)? = nil) ``` |

Modified [AVMetadataItem.locale](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387114-locale)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var locale: NSLocale? { get } ``` |
| To | ``` var locale: Locale? { get } ``` |

Modified [AVMetadataItem.metadataItems(from: [AVMetadataItem], filteredAndSortedAccordingToPreferredLanguages: [String]) -> [AVMetadataItem] [class]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387901-metadataitemsfromarray)

|  | Declaration |
| --- | --- |
| From | ``` class func metadataItemsFromArray(_ metadataItems: [AVMetadataItem], filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [String]) -> [AVMetadataItem] ``` |
| To | ``` class func metadataItems(from metadataItems: [AVMetadataItem], filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [String]) -> [AVMetadataItem] ``` |

Modified [AVMetadataItem.metadataItems(from: [AVMetadataItem], filteredBy: AVMetadataItemFilter) -> [AVMetadataItem] [class]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1390238-metadataitems)

|  | Declaration |
| --- | --- |
| From | ``` class func metadataItemsFromArray(_ metadataItems: [AVMetadataItem], filteredByMetadataItemFilter metadataItemFilter: AVMetadataItemFilter) -> [AVMetadataItem] ``` |
| To | ``` class func metadataItems(from metadataItems: [AVMetadataItem], filteredBy metadataItemFilter: AVMetadataItemFilter) -> [AVMetadataItem] ``` |

Modified [AVMetadataItem.metadataItems(from: [AVMetadataItem], filteredByIdentifier: String) -> [AVMetadataItem] [class]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1385843-metadataitems)

|  | Declaration |
| --- | --- |
| From | ``` class func metadataItemsFromArray(_ metadataItems: [AVMetadataItem], filteredByIdentifier identifier: String) -> [AVMetadataItem] ``` |
| To | ``` class func metadataItems(from metadataItems: [AVMetadataItem], filteredByIdentifier identifier: String) -> [AVMetadataItem] ``` |

Modified [AVMetadataItem.metadataItems(from: [AVMetadataItem], with: Locale) -> [AVMetadataItem] [class]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1389374-metadataitemsfromarray)

|  | Declaration |
| --- | --- |
| From | ``` class func metadataItemsFromArray(_ metadataItems: [AVMetadataItem], withLocale locale: NSLocale) -> [AVMetadataItem] ``` |
| To | ``` class func metadataItems(from metadataItems: [AVMetadataItem], with locale: Locale) -> [AVMetadataItem] ``` |

Modified [AVMetadataItem.metadataItems(from: [AVMetadataItem], withKey: Any?, keySpace: String?) -> [AVMetadataItem] [class]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1386083-metadataitems)

|  | Declaration |
| --- | --- |
| From | ``` class func metadataItemsFromArray(_ metadataItems: [AVMetadataItem], withKey key: AnyObject?, keySpace keySpace: String?) -> [AVMetadataItem] ``` |
| To | ``` class func metadataItems(from metadataItems: [AVMetadataItem], withKey key: Any?, keySpace keySpace: String?) -> [AVMetadataItem] ``` |

Modified [AVMetadataItem.startDate](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1388535-startdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var startDate: NSDate? { get } ``` |
| To | ``` var startDate: Date? { get } ``` |

Modified [AVMetadataItem.statusOfValue(forKey: String, error: NSErrorPointer) -> AVKeyValueStatus](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1388523-statusofvalueforkey)

|  | Declaration |
| --- | --- |
| From | ``` func statusOfValueForKey(_ key: String, error outError: NSErrorPointer) -> AVKeyValueStatus ``` |
| To | ``` func statusOfValue(forKey key: String, error outError: NSErrorPointer) -> AVKeyValueStatus ``` |

Modified [AVMetadataItem.value](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1390537-value)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var value: protocol<NSCopying, NSObjectProtocol>? { get } ``` |
| To | ``` @NSCopying var value: (NSCopying & NSObjectProtocol)? { get } ``` |

Modified [AVMetadataItemFilter](https://developer.apple.com/documentation/avfoundation/avmetadataitemfilter)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVMetadataItemFilter : NSObject {     class func metadataItemFilterForSharing() -> AVMetadataItemFilter } ``` | -- |
| To | ``` class AVMetadataItemFilter : NSObject {     class func forSharing() -> AVMetadataItemFilter     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVMetadataItemFilter : CVarArg { } extension AVMetadataItemFilter : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVMetadataItemFilter.forSharing() -> AVMetadataItemFilter [class]](https://developer.apple.com/documentation/avfoundation/avmetadataitemfilter/1387905-forsharing)

|  | Declaration |
| --- | --- |
| From | ``` class func metadataItemFilterForSharing() -> AVMetadataItemFilter ``` |
| To | ``` class func forSharing() -> AVMetadataItemFilter ``` |

Modified [AVMetadataItemValueRequest](https://developer.apple.com/documentation/avfoundation/avmetadataitemvaluerequest)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVMetadataItemValueRequest : NSObject {     weak var metadataItem: AVMetadataItem? { get }     func respondWithValue(_ value: protocol<NSCopying, NSObjectProtocol>)     func respondWithError(_ error: NSError) } ``` | -- |
| To | ``` class AVMetadataItemValueRequest : NSObject {     weak var metadataItem: AVMetadataItem? { get }     func respond(withValue value: NSCopying & NSObjectProtocol)     func respondWithError(_ error: Error)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVMetadataItemValueRequest : CVarArg { } extension AVMetadataItemValueRequest : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVMetadataItemValueRequest.respond(withValue: NSCopying & NSObjectProtocol)](https://developer.apple.com/documentation/avfoundation/avmetadataitemvaluerequest/1386820-respond)

|  | Declaration |
| --- | --- |
| From | ``` func respondWithValue(_ value: protocol<NSCopying, NSObjectProtocol>) ``` |
| To | ``` func respond(withValue value: NSCopying & NSObjectProtocol) ``` |

Modified [AVMetadataItemValueRequest.respondWithError(_: Error)](https://developer.apple.com/documentation/avfoundation/avmetadataitemvaluerequest/1390783-respondwitherror)

|  | Declaration |
| --- | --- |
| From | ``` func respondWithError(_ error: NSError) ``` |
| To | ``` func respondWithError(_ error: Error) ``` |

Modified [AVMIDIPlayer](https://developer.apple.com/documentation/avfoundation/avmidiplayer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVMIDIPlayer : NSObject {     init(contentsOfURL inURL: NSURL, soundBankURL bankURL: NSURL?) throws     init(data data: NSData, soundBankURL bankURL: NSURL?) throws     func prepareToPlay()     func play(_ completionHandler: AVMIDIPlayerCompletionHandler?)     func stop()     var duration: NSTimeInterval { get }     var playing: Bool { get }     var rate: Float     var currentPosition: NSTimeInterval } ``` | -- |
| To | ``` class AVMIDIPlayer : NSObject {     init(contentsOf inURL: URL, soundBankURL bankURL: URL?) throws     init(data data: Data, soundBankURL bankURL: URL?) throws     func prepareToPlay()     func play(_ completionHandler: AVFoundation.AVMIDIPlayerCompletionHandler? = nil)     func stop()     var duration: TimeInterval { get }     var isPlaying: Bool { get }     var rate: Float     var currentPosition: TimeInterval     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVMIDIPlayer : CVarArg { } extension AVMIDIPlayer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVMIDIPlayer.currentPosition](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1389636-currentposition)

|  | Declaration |
| --- | --- |
| From | ``` var currentPosition: NSTimeInterval ``` |
| To | ``` var currentPosition: TimeInterval ``` |

Modified [AVMIDIPlayer.duration](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1386440-duration)

|  | Declaration |
| --- | --- |
| From | ``` var duration: NSTimeInterval { get } ``` |
| To | ``` var duration: TimeInterval { get } ``` |

Modified [AVMIDIPlayer.init(contentsOf: URL, soundBankURL: URL?) throws](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1390856-init)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfURL inURL: NSURL, soundBankURL bankURL: NSURL?) throws ``` |
| To | ``` init(contentsOf inURL: URL, soundBankURL bankURL: URL?) throws ``` |

Modified [AVMIDIPlayer.init(data: Data, soundBankURL: URL?) throws](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1389225-init)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData, soundBankURL bankURL: NSURL?) throws ``` |
| To | ``` init(data data: Data, soundBankURL bankURL: URL?) throws ``` |

Modified [AVMIDIPlayer.isPlaying](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1385747-isplaying)

|  | Declaration |
| --- | --- |
| From | ``` var playing: Bool { get } ``` |
| To | ``` var isPlaying: Bool { get } ``` |

Modified [AVMIDIPlayer.play(_: AVFoundation.AVMIDIPlayerCompletionHandler?)](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1388390-play)

|  | Declaration |
| --- | --- |
| From | ``` func play(_ completionHandler: AVMIDIPlayerCompletionHandler?) ``` |
| To | ``` func play(_ completionHandler: AVFoundation.AVMIDIPlayerCompletionHandler? = nil) ``` |

Modified [AVMusicSequenceLoadOptions [struct]](https://developer.apple.com/documentation/avfoundation/avmusicsequenceloadoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVMusicSequenceLoadOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var SMF_PreserveTracks: AVMusicSequenceLoadOptions { get }     static var SMF_ChannelsToTracks: AVMusicSequenceLoadOptions { get } } ``` | OptionSetType |
| To | ``` struct AVMusicSequenceLoadOptions : OptionSet {     init(rawValue rawValue: UInt)     static var smf_PreserveTracks: AVMusicSequenceLoadOptions { get }     static var smfChannelsToTracks: AVMusicSequenceLoadOptions { get }     func intersect(_ other: AVMusicSequenceLoadOptions) -> AVMusicSequenceLoadOptions     func exclusiveOr(_ other: AVMusicSequenceLoadOptions) -> AVMusicSequenceLoadOptions     mutating func unionInPlace(_ other: AVMusicSequenceLoadOptions)     mutating func intersectInPlace(_ other: AVMusicSequenceLoadOptions)     mutating func exclusiveOrInPlace(_ other: AVMusicSequenceLoadOptions)     func isSubsetOf(_ other: AVMusicSequenceLoadOptions) -> Bool     func isDisjointWith(_ other: AVMusicSequenceLoadOptions) -> Bool     func isSupersetOf(_ other: AVMusicSequenceLoadOptions) -> Bool     mutating func subtractInPlace(_ other: AVMusicSequenceLoadOptions)     func isStrictSupersetOf(_ other: AVMusicSequenceLoadOptions) -> Bool     func isStrictSubsetOf(_ other: AVMusicSequenceLoadOptions) -> Bool } extension AVMusicSequenceLoadOptions {     func union(_ other: AVMusicSequenceLoadOptions) -> AVMusicSequenceLoadOptions     func intersection(_ other: AVMusicSequenceLoadOptions) -> AVMusicSequenceLoadOptions     func symmetricDifference(_ other: AVMusicSequenceLoadOptions) -> AVMusicSequenceLoadOptions } extension AVMusicSequenceLoadOptions {     func contains(_ member: AVMusicSequenceLoadOptions) -> Bool     mutating func insert(_ newMember: AVMusicSequenceLoadOptions) -> (inserted: Bool, memberAfterInsert: AVMusicSequenceLoadOptions)     mutating func remove(_ member: AVMusicSequenceLoadOptions) -> AVMusicSequenceLoadOptions?     mutating func update(with newMember: AVMusicSequenceLoadOptions) -> AVMusicSequenceLoadOptions? } extension AVMusicSequenceLoadOptions {     convenience init()     mutating func formUnion(_ other: AVMusicSequenceLoadOptions)     mutating func formIntersection(_ other: AVMusicSequenceLoadOptions)     mutating func formSymmetricDifference(_ other: AVMusicSequenceLoadOptions) } extension AVMusicSequenceLoadOptions {     convenience init<S : Sequence where S.Iterator.Element == AVMusicSequenceLoadOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AVMusicSequenceLoadOptions...)     mutating func subtract(_ other: AVMusicSequenceLoadOptions)     func isSubset(of other: AVMusicSequenceLoadOptions) -> Bool     func isSuperset(of other: AVMusicSequenceLoadOptions) -> Bool     func isDisjoint(with other: AVMusicSequenceLoadOptions) -> Bool     func subtracting(_ other: AVMusicSequenceLoadOptions) -> AVMusicSequenceLoadOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: AVMusicSequenceLoadOptions) -> Bool     func isStrictSubset(of other: AVMusicSequenceLoadOptions) -> Bool } ``` | OptionSet |

Modified [AVMusicSequenceLoadOptions.smfChannelsToTracks](https://developer.apple.com/documentation/avfoundation/avmusicsequenceloadoptions/avmusicsequenceloadsmf_channelstotracks)

|  | Declaration |
| --- | --- |
| From | ``` static var SMF_ChannelsToTracks: AVMusicSequenceLoadOptions { get } ``` |
| To | ``` static var smfChannelsToTracks: AVMusicSequenceLoadOptions { get } ``` |

Modified [AVMusicTrack](https://developer.apple.com/documentation/avfoundation/avmusictrack)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVMusicTrack : NSObject {     var destinationAudioUnit: AVAudioUnit?     var loopRange: AVBeatRange     var loopingEnabled: Bool     var numberOfLoops: Int     var offsetTime: AVMusicTimeStamp     var muted: Bool     var soloed: Bool     var lengthInBeats: AVMusicTimeStamp     var lengthInSeconds: NSTimeInterval     var timeResolution: Int { get } } ``` | -- |
| To | ``` class AVMusicTrack : NSObject {     var destinationAudioUnit: AVAudioUnit?     var loopRange: AVBeatRange     var isLoopingEnabled: Bool     var numberOfLoops: Int     var offsetTime: AVMusicTimeStamp     var isMuted: Bool     var isSoloed: Bool     var lengthInBeats: AVMusicTimeStamp     var lengthInSeconds: TimeInterval     var timeResolution: Int { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVMusicTrack : CVarArg { } extension AVMusicTrack : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVMusicTrack.isLoopingEnabled](https://developer.apple.com/documentation/avfoundation/avmusictrack/1385811-loopingenabled)

|  | Declaration |
| --- | --- |
| From | ``` var loopingEnabled: Bool ``` |
| To | ``` var isLoopingEnabled: Bool ``` |

Modified [AVMusicTrack.isMuted](https://developer.apple.com/documentation/avfoundation/avmusictrack/1387694-muted)

|  | Declaration |
| --- | --- |
| From | ``` var muted: Bool ``` |
| To | ``` var isMuted: Bool ``` |

Modified [AVMusicTrack.isSoloed](https://developer.apple.com/documentation/avfoundation/avmusictrack/1387883-soloed)

|  | Declaration |
| --- | --- |
| From | ``` var soloed: Bool ``` |
| To | ``` var isSoloed: Bool ``` |

Modified [AVMusicTrack.lengthInSeconds](https://developer.apple.com/documentation/avfoundation/avmusictrack/1385749-lengthinseconds)

|  | Declaration |
| --- | --- |
| From | ``` var lengthInSeconds: NSTimeInterval ``` |
| To | ``` var lengthInSeconds: TimeInterval ``` |

Modified [AVMusicTrackLoopCount [enum]](https://developer.apple.com/documentation/avfoundation/avmusictrackloopcount)

|  | Declaration |
| --- | --- |
| From | ``` enum AVMusicTrackLoopCount : Int {     case Forever } ``` |
| To | ``` enum AVMusicTrackLoopCount : Int {     case forever } ``` |

Modified [AVMusicTrackLoopCount.forever](https://developer.apple.com/documentation/avfoundation/avmusictrackloopcount/forever)

|  | Declaration |
| --- | --- |
| From | ``` case Forever ``` |
| To | ``` case forever ``` |

Modified [AVMutableAudioMixInputParameters](https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters)

|  | Declaration |
| --- | --- |
| From | ``` class AVMutableAudioMixInputParameters : AVAudioMixInputParameters {     convenience init(track track: AVAssetTrack?)     class func audioMixInputParametersWithTrack(_ track: AVAssetTrack?) -> Self     convenience init()     class func audioMixInputParameters() -> Self     var trackID: CMPersistentTrackID     var audioTimePitchAlgorithm: String?     var audioTapProcessor: MTAudioProcessingTap?     func setVolumeRampFromStartVolume(_ startVolume: Float, toEndVolume endVolume: Float, timeRange timeRange: CMTimeRange)     func setVolume(_ volume: Float, atTime time: CMTime) } ``` |
| To | ``` class AVMutableAudioMixInputParameters : AVAudioMixInputParameters {     convenience init(track track: AVAssetTrack?)     class func withTrack(_ track: AVAssetTrack?) -> Self     convenience init()     class func audioMixInputParameters() -> Self     var trackID: CMPersistentTrackID     var audioTimePitchAlgorithm: String?     var audioTapProcessor: MTAudioProcessingTap?     func setVolumeRamp(fromStartVolume startVolume: Float, toEndVolume endVolume: Float, timeRange timeRange: CMTimeRange)     func setVolume(_ volume: Float, at time: CMTime) } ``` |

Modified [AVMutableAudioMixInputParameters.setVolume(_: Float, at: CMTime)](https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/1389875-setvolume)

|  | Declaration |
| --- | --- |
| From | ``` func setVolume(_ volume: Float, atTime time: CMTime) ``` |
| To | ``` func setVolume(_ volume: Float, at time: CMTime) ``` |

Modified [AVMutableAudioMixInputParameters.setVolumeRamp(fromStartVolume: Float, toEndVolume: Float, timeRange: CMTimeRange)](https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/1386056-setvolumerampfromstartvolume)

|  | Declaration |
| --- | --- |
| From | ``` func setVolumeRampFromStartVolume(_ startVolume: Float, toEndVolume endVolume: Float, timeRange timeRange: CMTimeRange) ``` |
| To | ``` func setVolumeRamp(fromStartVolume startVolume: Float, toEndVolume endVolume: Float, timeRange timeRange: CMTimeRange) ``` |

Modified [AVMutableComposition](https://developer.apple.com/documentation/avfoundation/avmutablecomposition)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVMutableComposition : AVComposition {     var tracks: [AVMutableCompositionTrack] { get }     var naturalSize: CGSize     convenience init()     class func composition() -> Self     convenience init(URLAssetInitializationOptions URLAssetInitializationOptions: [String : AnyObject]?)     class func compositionWithURLAssetInitializationOptions(_ URLAssetInitializationOptions: [String : AnyObject]?) -> Self } extension AVMutableComposition {     func insertTimeRange(_ timeRange: CMTimeRange, ofAsset asset: AVAsset, atTime startTime: CMTime) throws     func insertEmptyTimeRange(_ timeRange: CMTimeRange)     func removeTimeRange(_ timeRange: CMTimeRange)     func scaleTimeRange(_ timeRange: CMTimeRange, toDuration duration: CMTime) } extension AVMutableComposition {     func addMutableTrackWithMediaType(_ mediaType: String, preferredTrackID preferredTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack     func removeTrack(_ track: AVCompositionTrack)     func mutableTrackCompatibleWithTrack(_ track: AVAssetTrack) -> AVMutableCompositionTrack? } extension AVMutableComposition {     func trackWithTrackID(_ trackID: CMPersistentTrackID) -> AVMutableCompositionTrack?     func tracksWithMediaType(_ mediaType: String) -> [AVMutableCompositionTrack]     func tracksWithMediaCharacteristic(_ mediaCharacteristic: String) -> [AVMutableCompositionTrack] } ``` | -- |
| To | ``` class AVMutableComposition : AVComposition {     var tracks: [AVMutableCompositionTrack] { get }     var naturalSize: CGSize     convenience init()     class func composition() -> Self     convenience init(urlAssetInitializationOptions URLAssetInitializationOptions: [String : Any]? = nil)     class func withURLAssetInitializationOptions(_ URLAssetInitializationOptions: [String : Any]? = nil) -> Self     func track(withTrackID trackID: CMPersistentTrackID) -> AVMutableCompositionTrack?     func tracks(withMediaType mediaType: String) -> [AVMutableCompositionTrack]     func tracks(withMediaCharacteristic mediaCharacteristic: String) -> [AVMutableCompositionTrack]     func addMutableTrack(withMediaType mediaType: String, preferredTrackID preferredTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack     func removeTrack(_ track: AVCompositionTrack)     func mutableTrack(compatibleWith track: AVAssetTrack) -> AVMutableCompositionTrack?     func insertTimeRange(_ timeRange: CMTimeRange, of asset: AVAsset, at startTime: CMTime) throws     func insertEmptyTimeRange(_ timeRange: CMTimeRange)     func removeTimeRange(_ timeRange: CMTimeRange)     func scaleTimeRange(_ timeRange: CMTimeRange, toDuration duration: CMTime)     func unusedTrackID() -> CMPersistentTrackID     var isPlayable: Bool { get }     var isExportable: Bool { get }     var isReadable: Bool { get }     var isComposable: Bool { get }     var isCompatibleWithSavedPhotosAlbum: Bool { get }     var isCompatibleWithAirPlayVideo: Bool { get }     var canContainFragments: Bool { get }     var containsFragments: Bool { get }     var hasProtectedContent: Bool { get }     var availableMediaCharacteristicsWithMediaSelectionOptions: [String] { get }     func mediaSelectionGroup(forMediaCharacteristic mediaCharacteristic: String) -> AVMediaSelectionGroup?     var preferredMediaSelection: AVMediaSelection { get }     var availableChapterLocales: [Locale] { get }     func chapterMetadataGroups(withTitleLocale locale: Locale, containingItemsWithCommonKeys commonKeys: [String]?) -> [AVTimedMetadataGroup]     func chapterMetadataGroups(bestMatchingPreferredLanguages preferredLanguages: [String]) -> [AVTimedMetadataGroup]     var creationDate: AVMetadataItem? { get }     var lyrics: String? { get }     var commonMetadata: [AVMetadataItem] { get }     var metadata: [AVMetadataItem] { get }     var availableMetadataFormats: [String] { get }     func metadata(forFormat format: String) -> [AVMetadataItem]     var tracks: [AVAssetTrack] { get }     var trackGroups: [AVAssetTrackGroup] { get }     var referenceRestrictions: AVAssetReferenceRestrictions { get }     var providesPreciseDurationAndTiming: Bool { get }     func cancelLoading()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVMutableComposition : CVarArg { } extension AVMutableComposition : Equatable, Hashable {     var hashValue: Int { get } } extension AVMutableComposition {     func insertTimeRange(_ timeRange: CMTimeRange, of asset: AVAsset, at startTime: CMTime) throws     func insertEmptyTimeRange(_ timeRange: CMTimeRange)     func removeTimeRange(_ timeRange: CMTimeRange)     func scaleTimeRange(_ timeRange: CMTimeRange, toDuration duration: CMTime) } extension AVMutableComposition {     func addMutableTrack(withMediaType mediaType: String, preferredTrackID preferredTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack     func removeTrack(_ track: AVCompositionTrack)     func mutableTrack(compatibleWith track: AVAssetTrack) -> AVMutableCompositionTrack? } extension AVMutableComposition {     func track(withTrackID trackID: CMPersistentTrackID) -> AVMutableCompositionTrack?     func tracks(withMediaType mediaType: String) -> [AVMutableCompositionTrack]     func tracks(withMediaCharacteristic mediaCharacteristic: String) -> [AVMutableCompositionTrack] } ``` | CVarArg, Equatable, Hashable |

Modified [AVMutableComposition.addMutableTrack(withMediaType: String, preferredTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1387601-addmutabletrack)

|  | Declaration |
| --- | --- |
| From | ``` func addMutableTrackWithMediaType(_ mediaType: String, preferredTrackID preferredTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack ``` |
| To | ``` func addMutableTrack(withMediaType mediaType: String, preferredTrackID preferredTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack ``` |

Modified [AVMutableComposition.init(urlAssetInitializationOptions: [String : Any]?)](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1390705-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(URLAssetInitializationOptions URLAssetInitializationOptions: [String : AnyObject]?) ``` |
| To | ``` convenience init(urlAssetInitializationOptions URLAssetInitializationOptions: [String : Any]? = nil) ``` |

Modified [AVMutableComposition.insertTimeRange(_: CMTimeRange, of: AVAsset, at: CMTime) throws](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1385943-inserttimerange)

|  | Declaration |
| --- | --- |
| From | ``` func insertTimeRange(_ timeRange: CMTimeRange, ofAsset asset: AVAsset, atTime startTime: CMTime) throws ``` |
| To | ``` func insertTimeRange(_ timeRange: CMTimeRange, of asset: AVAsset, at startTime: CMTime) throws ``` |

Modified [AVMutableComposition.mutableTrack(compatibleWith: AVAssetTrack) -> AVMutableCompositionTrack?](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1386662-mutabletrack)

|  | Declaration |
| --- | --- |
| From | ``` func mutableTrackCompatibleWithTrack(_ track: AVAssetTrack) -> AVMutableCompositionTrack? ``` |
| To | ``` func mutableTrack(compatibleWith track: AVAssetTrack) -> AVMutableCompositionTrack? ``` |

Modified [AVMutableComposition.track(withTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack?](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1390074-trackwithtrackid)

|  | Declaration |
| --- | --- |
| From | ``` func trackWithTrackID(_ trackID: CMPersistentTrackID) -> AVMutableCompositionTrack? ``` |
| To | ``` func track(withTrackID trackID: CMPersistentTrackID) -> AVMutableCompositionTrack? ``` |

Modified [AVMutableComposition.tracks(withMediaCharacteristic: String) -> [AVMutableCompositionTrack]](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1388464-trackswithmediacharacteristic)

|  | Declaration |
| --- | --- |
| From | ``` func tracksWithMediaCharacteristic(_ mediaCharacteristic: String) -> [AVMutableCompositionTrack] ``` |
| To | ``` func tracks(withMediaCharacteristic mediaCharacteristic: String) -> [AVMutableCompositionTrack] ``` |

Modified [AVMutableComposition.tracks(withMediaType: String) -> [AVMutableCompositionTrack]](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1385724-tracks)

|  | Declaration |
| --- | --- |
| From | ``` func tracksWithMediaType(_ mediaType: String) -> [AVMutableCompositionTrack] ``` |
| To | ``` func tracks(withMediaType mediaType: String) -> [AVMutableCompositionTrack] ``` |

Modified [AVMutableCompositionTrack](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack)

|  | Declaration |
| --- | --- |
| From | ``` class AVMutableCompositionTrack : AVCompositionTrack {     var naturalTimeScale: CMTimeScale     var languageCode: String?     var extendedLanguageTag: String?     var preferredTransform: CGAffineTransform     var preferredVolume: Float     var segments: [AVCompositionTrackSegment]!     func insertTimeRange(_ timeRange: CMTimeRange, ofTrack track: AVAssetTrack, atTime startTime: CMTime) throws     func insertTimeRanges(_ timeRanges: [NSValue], ofTracks tracks: [AVAssetTrack], atTime startTime: CMTime) throws     func insertEmptyTimeRange(_ timeRange: CMTimeRange)     func removeTimeRange(_ timeRange: CMTimeRange)     func scaleTimeRange(_ timeRange: CMTimeRange, toDuration duration: CMTime)     func validateTrackSegments(_ trackSegments: [AVCompositionTrackSegment]) throws } ``` |
| To | ``` class AVMutableCompositionTrack : AVCompositionTrack {     var naturalTimeScale: CMTimeScale     var languageCode: String?     var extendedLanguageTag: String?     var preferredTransform: CGAffineTransform     var preferredVolume: Float     var segments: [AVCompositionTrackSegment]!     func insertTimeRange(_ timeRange: CMTimeRange, of track: AVAssetTrack, at startTime: CMTime) throws     func insertTimeRanges(_ timeRanges: [NSValue], of tracks: [AVAssetTrack], at startTime: CMTime) throws     func insertEmptyTimeRange(_ timeRange: CMTimeRange)     func removeTimeRange(_ timeRange: CMTimeRange)     func scaleTimeRange(_ timeRange: CMTimeRange, toDuration duration: CMTime)     func validateSegments(_ trackSegments: [AVCompositionTrackSegment]) throws } ``` |

Modified [AVMutableCompositionTrack.insertTimeRange(_: CMTimeRange, of: AVAssetTrack, at: CMTime) throws](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/1390691-inserttimerange)

|  | Declaration |
| --- | --- |
| From | ``` func insertTimeRange(_ timeRange: CMTimeRange, ofTrack track: AVAssetTrack, atTime startTime: CMTime) throws ``` |
| To | ``` func insertTimeRange(_ timeRange: CMTimeRange, of track: AVAssetTrack, at startTime: CMTime) throws ``` |

Modified [AVMutableCompositionTrack.insertTimeRanges(_: [NSValue], of: [AVAssetTrack], at: CMTime) throws](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/1388629-inserttimeranges)

|  | Declaration |
| --- | --- |
| From | ``` func insertTimeRanges(_ timeRanges: [NSValue], ofTracks tracks: [AVAssetTrack], atTime startTime: CMTime) throws ``` |
| To | ``` func insertTimeRanges(_ timeRanges: [NSValue], of tracks: [AVAssetTrack], at startTime: CMTime) throws ``` |

Modified [AVMutableCompositionTrack.validateSegments(_: [AVCompositionTrackSegment]) throws](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/1388746-validatesegments)

|  | Declaration |
| --- | --- |
| From | ``` func validateTrackSegments(_ trackSegments: [AVCompositionTrackSegment]) throws ``` |
| To | ``` func validateSegments(_ trackSegments: [AVCompositionTrackSegment]) throws ``` |

Modified [AVMutableDateRangeMetadataGroup](https://developer.apple.com/documentation/avfoundation/avmutabledaterangemetadatagroup)

|  | Declaration |
| --- | --- |
| From | ``` class AVMutableDateRangeMetadataGroup : AVDateRangeMetadataGroup {     @NSCopying var startDate: NSDate     @NSCopying var endDate: NSDate?     var items: [AVMetadataItem] } ``` |
| To | ``` class AVMutableDateRangeMetadataGroup : AVDateRangeMetadataGroup {     var startDate: Date     var endDate: Date?     var items: [AVMetadataItem] } ``` |

Modified [AVMutableDateRangeMetadataGroup.endDate](https://developer.apple.com/documentation/avfoundation/avmutabledaterangemetadatagroup/1387651-enddate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var endDate: NSDate? ``` |
| To | ``` var endDate: Date? ``` |

Modified [AVMutableDateRangeMetadataGroup.startDate](https://developer.apple.com/documentation/avfoundation/avmutabledaterangemetadatagroup/1390555-startdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var startDate: NSDate ``` |
| To | ``` var startDate: Date ``` |

Modified [AVMutableMediaSelection](https://developer.apple.com/documentation/avfoundation/avmutablemediaselection)

|  | Declaration |
| --- | --- |
| From | ``` class AVMutableMediaSelection : AVMediaSelection {     func selectMediaOption(_ mediaSelectionOption: AVMediaSelectionOption?, inMediaSelectionGroup mediaSelectionGroup: AVMediaSelectionGroup) } ``` |
| To | ``` class AVMutableMediaSelection : AVMediaSelection {     func select(_ mediaSelectionOption: AVMediaSelectionOption?, in mediaSelectionGroup: AVMediaSelectionGroup) } ``` |

Modified [AVMutableMediaSelection.select(_: AVMediaSelectionOption?, in: AVMediaSelectionGroup)](https://developer.apple.com/documentation/avfoundation/avmutablemediaselection/1386768-selectmediaoption)

|  | Declaration |
| --- | --- |
| From | ``` func selectMediaOption(_ mediaSelectionOption: AVMediaSelectionOption?, inMediaSelectionGroup mediaSelectionGroup: AVMediaSelectionGroup) ``` |
| To | ``` func select(_ mediaSelectionOption: AVMediaSelectionOption?, in mediaSelectionGroup: AVMediaSelectionGroup) ``` |

Modified [AVMutableMetadataItem](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVMutableMetadataItem : AVMetadataItem {     var identifier: String?     var extendedLanguageTag: String?     @NSCopying var locale: NSLocale?     var time: CMTime     var duration: CMTime     var dataType: String?     @NSCopying var value: protocol<NSCopying, NSObjectProtocol>?     var extraAttributes: [String : AnyObject]?      init()     class func metadataItem() -> AVMutableMetadataItem } extension AVMutableMetadataItem {     @NSCopying var startDate: NSDate? } extension AVMutableMetadataItem {     var keySpace: String?     @NSCopying var key: protocol<NSCopying, NSObjectProtocol>? } ``` | -- |
| To | ``` class AVMutableMetadataItem : AVMetadataItem {     var identifier: String?     var extendedLanguageTag: String?     var locale: Locale?     var time: CMTime     var duration: CMTime     var dataType: String?     @NSCopying var value: (NSCopying & NSObjectProtocol)?     var extraAttributes: [String : Any]?      init()     class func metadataItem() -> AVMutableMetadataItem     var keySpace: String?     @NSCopying var key: (NSCopying & NSObjectProtocol)?     var startDate: Date?     class func metadataItems(from metadataItems: [AVMetadataItem], with locale: Locale) -> [AVMetadataItem]     class func metadataItems(from metadataItems: [AVMetadataItem], withKey key: Any?, keySpace keySpace: String?) -> [AVMetadataItem]      init(propertiesOf metadataItem: AVMetadataItem, valueLoadingHandler handler: @escaping (AVMetadataItemValueRequest) -> Void)     class func withPropertiesOf(_ metadataItem: AVMetadataItem, valueLoadingHandler handler: @escaping (AVMetadataItemValueRequest) -> Void) -> AVMetadataItem     class func identifier(forKey key: Any, keySpace keySpace: String) -> String?     class func keySpace(forIdentifier identifier: String) -> String?     class func key(forIdentifier identifier: String) -> Any?     @NSCopying var key: (NSCopying & NSObjectProtocol)? { get }     var commonKey: String? { get }     var keySpace: String? { get }     class func metadataItems(from metadataItems: [AVMetadataItem], filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [String]) -> [AVMetadataItem]     class func metadataItems(from metadataItems: [AVMetadataItem], filteredByIdentifier identifier: String) -> [AVMetadataItem]     class func metadataItems(from metadataItems: [AVMetadataItem], filteredBy metadataItemFilter: AVMetadataItemFilter) -> [AVMetadataItem]     func statusOfValue(forKey key: String, error outError: NSErrorPointer) -> AVKeyValueStatus     func loadValuesAsynchronously(forKeys keys: [String], completionHandler handler: (@escaping () -> Void)? = nil)     var stringValue: String? { get }     var numberValue: NSNumber? { get }     var dateValue: Date? { get }     var dataValue: Data? { get }     var startDate: Date? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVMutableMetadataItem : CVarArg { } extension AVMutableMetadataItem : Equatable, Hashable {     var hashValue: Int { get } } extension AVMutableMetadataItem {     var startDate: Date? } extension AVMutableMetadataItem {     var keySpace: String?     @NSCopying var key: (NSCopying & NSObjectProtocol)? } ``` | CVarArg, Equatable, Hashable |

Modified [AVMutableMetadataItem.extraAttributes](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1390397-extraattributes)

|  | Declaration |
| --- | --- |
| From | ``` var extraAttributes: [String : AnyObject]? ``` |
| To | ``` var extraAttributes: [String : Any]? ``` |

Modified [AVMutableMetadataItem.key](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1386776-key)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var key: protocol<NSCopying, NSObjectProtocol>? ``` |
| To | ``` @NSCopying var key: (NSCopying & NSObjectProtocol)? ``` |

Modified [AVMutableMetadataItem.locale](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1389292-locale)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var locale: NSLocale? ``` |
| To | ``` var locale: Locale? ``` |

Modified [AVMutableMetadataItem.startDate](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1389966-startdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var startDate: NSDate? ``` |
| To | ``` var startDate: Date? ``` |

Modified [AVMutableMetadataItem.value](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1388296-value)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var value: protocol<NSCopying, NSObjectProtocol>? ``` |
| To | ``` @NSCopying var value: (NSCopying & NSObjectProtocol)? ``` |

Modified [AVMutableTimedMetadataGroup](https://developer.apple.com/documentation/avfoundation/avmutabletimedmetadatagroup)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVMutableTimedMetadataGroup : AVTimedMetadataGroup {     var timeRange: CMTimeRange     var items: [AVMetadataItem] } ``` | -- |
| To | ``` class AVMutableTimedMetadataGroup : AVTimedMetadataGroup {     var timeRange: CMTimeRange     var items: [AVMetadataItem]     func copyFormatDescription() -> CMMetadataFormatDescription?     var classifyingLabel: String? { get }     var uniqueID: String? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVMutableTimedMetadataGroup : CVarArg { } extension AVMutableTimedMetadataGroup : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVMutableVideoComposition](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVMutableVideoComposition : AVVideoComposition {      init()     class func videoComposition() -> AVMutableVideoComposition      init(propertiesOfAsset asset: AVAsset)     class func videoCompositionWithPropertiesOfAsset(_ asset: AVAsset) -> AVMutableVideoComposition     var customVideoCompositorClass: AnyObject.Type?     var frameDuration: CMTime     var renderSize: CGSize     var renderScale: Float     var instructions: [AVVideoCompositionInstructionProtocol]     var animationTool: AVVideoCompositionCoreAnimationTool? } extension AVMutableVideoComposition {      init(asset asset: AVAsset, applyingCIFiltersWithHandler applier: (AVAsynchronousCIImageFilteringRequest) -> Void)     class func videoCompositionWithAsset(_ asset: AVAsset, applyingCIFiltersWithHandler applier: (AVAsynchronousCIImageFilteringRequest) -> Void) -> AVMutableVideoComposition } ``` | -- |
| To | ``` class AVMutableVideoComposition : AVVideoComposition {      init()     class func videoComposition() -> AVMutableVideoComposition      init(propertiesOf asset: AVAsset)     class func withPropertiesOf(_ asset: AVAsset) -> AVMutableVideoComposition     var customVideoCompositorClass: AVVideoCompositing.Type?     var frameDuration: CMTime     var renderSize: CGSize     var renderScale: Float     var instructions: [AVVideoCompositionInstructionProtocol]     var animationTool: AVVideoCompositionCoreAnimationTool?      init(asset asset: AVAsset, applyingCIFiltersWithHandler applier: @escaping (AVAsynchronousCIImageFilteringRequest) -> Swift.Void)     class func withAsset(_ asset: AVAsset, applyingCIFiltersWithHandler applier: @escaping (AVAsynchronousCIImageFilteringRequest) -> Swift.Void) -> AVMutableVideoComposition     var colorPrimaries: String?     var colorYCbCrMatrix: String?     var colorTransferFunction: String?     func isValid(for asset: AVAsset?, timeRange timeRange: CMTimeRange, validationDelegate validationDelegate: AVVideoCompositionValidationHandling?) -> Bool      init(asset asset: AVAsset, applyingCIFiltersWithHandler applier: @escaping (AVAsynchronousCIImageFilteringRequest) -> Void)     class func withAsset(_ asset: AVAsset, applyingCIFiltersWithHandler applier: @escaping (AVAsynchronousCIImageFilteringRequest) -> Void) -> AVVideoComposition     var colorPrimaries: String? { get }     var colorYCbCrMatrix: String? { get }     var colorTransferFunction: String? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVMutableVideoComposition : CVarArg { } extension AVMutableVideoComposition : Equatable, Hashable {     var hashValue: Int { get } } extension AVMutableVideoComposition {     var colorPrimaries: String?     var colorYCbCrMatrix: String?     var colorTransferFunction: String? } extension AVMutableVideoComposition {      init(asset asset: AVAsset, applyingCIFiltersWithHandler applier: @escaping (AVAsynchronousCIImageFilteringRequest) -> Swift.Void)     class func withAsset(_ asset: AVAsset, applyingCIFiltersWithHandler applier: @escaping (AVAsynchronousCIImageFilteringRequest) -> Swift.Void) -> AVMutableVideoComposition } ``` | CVarArg, Equatable, Hashable |

Modified [AVMutableVideoComposition.customVideoCompositorClass](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1390649-customvideocompositorclass)

|  | Declaration |
| --- | --- |
| From | ``` var customVideoCompositorClass: AnyObject.Type? ``` |
| To | ``` var customVideoCompositorClass: AVVideoCompositing.Type? ``` |

Modified [AVMutableVideoComposition.init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Swift.Void)](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1387006-videocompositionwithasset)

|  | Declaration |
| --- | --- |
| From | ``` init(asset asset: AVAsset, applyingCIFiltersWithHandler applier: (AVAsynchronousCIImageFilteringRequest) -> Void) ``` |
| To | ``` init(asset asset: AVAsset, applyingCIFiltersWithHandler applier: @escaping (AVAsynchronousCIImageFilteringRequest) -> Swift.Void) ``` |

Modified [AVMutableVideoComposition.init(propertiesOf: AVAsset)](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1388430-init)

|  | Declaration |
| --- | --- |
| From | ``` init(propertiesOfAsset asset: AVAsset) ``` |
| To | ``` init(propertiesOf asset: AVAsset) ``` |

Modified [AVMutableVideoCompositionLayerInstruction](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction)

|  | Declaration |
| --- | --- |
| From | ``` class AVMutableVideoCompositionLayerInstruction : AVVideoCompositionLayerInstruction {     convenience init(assetTrack track: AVAssetTrack)     class func videoCompositionLayerInstructionWithAssetTrack(_ track: AVAssetTrack) -> Self     convenience init()     class func videoCompositionLayerInstruction() -> Self     var trackID: CMPersistentTrackID     func setTransformRampFromStartTransform(_ startTransform: CGAffineTransform, toEndTransform endTransform: CGAffineTransform, timeRange timeRange: CMTimeRange)     func setTransform(_ transform: CGAffineTransform, atTime time: CMTime)     func setOpacityRampFromStartOpacity(_ startOpacity: Float, toEndOpacity endOpacity: Float, timeRange timeRange: CMTimeRange)     func setOpacity(_ opacity: Float, atTime time: CMTime)     func setCropRectangleRampFromStartCropRectangle(_ startCropRectangle: CGRect, toEndCropRectangle endCropRectangle: CGRect, timeRange timeRange: CMTimeRange)     func setCropRectangle(_ cropRectangle: CGRect, atTime time: CMTime) } ``` |
| To | ``` class AVMutableVideoCompositionLayerInstruction : AVVideoCompositionLayerInstruction {     convenience init(assetTrack track: AVAssetTrack)     class func withAssetTrack(_ track: AVAssetTrack) -> Self     convenience init()     class func videoCompositionLayerInstruction() -> Self     var trackID: CMPersistentTrackID     func setTransformRamp(fromStart startTransform: CGAffineTransform, toEnd endTransform: CGAffineTransform, timeRange timeRange: CMTimeRange)     func setTransform(_ transform: CGAffineTransform, at time: CMTime)     func setOpacityRamp(fromStartOpacity startOpacity: Float, toEndOpacity endOpacity: Float, timeRange timeRange: CMTimeRange)     func setOpacity(_ opacity: Float, at time: CMTime)     func setCropRectangleRamp(fromStartCropRectangle startCropRectangle: CGRect, toEndCropRectangle endCropRectangle: CGRect, timeRange timeRange: CMTimeRange)     func setCropRectangle(_ cropRectangle: CGRect, at time: CMTime) } ``` |

Modified [AVMutableVideoCompositionLayerInstruction.setCropRectangle(_: CGRect, at: CMTime)](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/1387402-setcroprectangle)

|  | Declaration |
| --- | --- |
| From | ``` func setCropRectangle(_ cropRectangle: CGRect, atTime time: CMTime) ``` |
| To | ``` func setCropRectangle(_ cropRectangle: CGRect, at time: CMTime) ``` |

Modified [AVMutableVideoCompositionLayerInstruction.setCropRectangleRamp(fromStartCropRectangle: CGRect, toEndCropRectangle: CGRect, timeRange: CMTimeRange)](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/1385677-setcroprectangleramp)

|  | Declaration |
| --- | --- |
| From | ``` func setCropRectangleRampFromStartCropRectangle(_ startCropRectangle: CGRect, toEndCropRectangle endCropRectangle: CGRect, timeRange timeRange: CMTimeRange) ``` |
| To | ``` func setCropRectangleRamp(fromStartCropRectangle startCropRectangle: CGRect, toEndCropRectangle endCropRectangle: CGRect, timeRange timeRange: CMTimeRange) ``` |

Modified [AVMutableVideoCompositionLayerInstruction.setOpacity(_: Float, at: CMTime)](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/1390758-setopacity)

|  | Declaration |
| --- | --- |
| From | ``` func setOpacity(_ opacity: Float, atTime time: CMTime) ``` |
| To | ``` func setOpacity(_ opacity: Float, at time: CMTime) ``` |

Modified [AVMutableVideoCompositionLayerInstruction.setOpacityRamp(fromStartOpacity: Float, toEndOpacity: Float, timeRange: CMTimeRange)](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/1387532-setopacityrampfromstartopacity)

|  | Declaration |
| --- | --- |
| From | ``` func setOpacityRampFromStartOpacity(_ startOpacity: Float, toEndOpacity endOpacity: Float, timeRange timeRange: CMTimeRange) ``` |
| To | ``` func setOpacityRamp(fromStartOpacity startOpacity: Float, toEndOpacity endOpacity: Float, timeRange timeRange: CMTimeRange) ``` |

Modified [AVMutableVideoCompositionLayerInstruction.setTransform(_: CGAffineTransform, at: CMTime)](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/1390899-settransform)

|  | Declaration |
| --- | --- |
| From | ``` func setTransform(_ transform: CGAffineTransform, atTime time: CMTime) ``` |
| To | ``` func setTransform(_ transform: CGAffineTransform, at time: CMTime) ``` |

Modified [AVMutableVideoCompositionLayerInstruction.setTransformRamp(fromStart: CGAffineTransform, toEnd: CGAffineTransform, timeRange: CMTimeRange)](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/1388192-settransformramp)

|  | Declaration |
| --- | --- |
| From | ``` func setTransformRampFromStartTransform(_ startTransform: CGAffineTransform, toEndTransform endTransform: CGAffineTransform, timeRange timeRange: CMTimeRange) ``` |
| To | ``` func setTransformRamp(fromStart startTransform: CGAffineTransform, toEnd endTransform: CGAffineTransform, timeRange timeRange: CMTimeRange) ``` |

Modified [AVOutputSettingsAssistant](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVOutputSettingsAssistant : NSObject {     init()     class func availableOutputSettingsPresets() -> [String]     convenience init?(preset presetIdentifier: String)     class func outputSettingsAssistantWithPreset(_ presetIdentifier: String) -> Self?     var audioSettings: [String : AnyObject]? { get }     var videoSettings: [String : AnyObject]? { get }     var outputFileType: String { get } } extension AVOutputSettingsAssistant {     var sourceAudioFormat: CMAudioFormatDescription?     var sourceVideoFormat: CMVideoFormatDescription?     var sourceVideoAverageFrameDuration: CMTime     var sourceVideoMinFrameDuration: CMTime } ``` | -- |
| To | ``` class AVOutputSettingsAssistant : NSObject {     init()     class func availableOutputSettingsPresets() -> [String]     convenience init?(preset presetIdentifier: String)     class func withPreset(_ presetIdentifier: String) -> Self?     var audioSettings: [String : Any]? { get }     var videoSettings: [String : Any]? { get }     var outputFileType: String { get }     var sourceAudioFormat: CMAudioFormatDescription?     var sourceVideoFormat: CMVideoFormatDescription?     var sourceVideoAverageFrameDuration: CMTime     var sourceVideoMinFrameDuration: CMTime     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVOutputSettingsAssistant : CVarArg { } extension AVOutputSettingsAssistant : Equatable, Hashable {     var hashValue: Int { get } } extension AVOutputSettingsAssistant {     var sourceAudioFormat: CMAudioFormatDescription?     var sourceVideoFormat: CMVideoFormatDescription?     var sourceVideoAverageFrameDuration: CMTime     var sourceVideoMinFrameDuration: CMTime } ``` | CVarArg, Equatable, Hashable |

Modified [AVOutputSettingsAssistant.audioSettings](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1386233-audiosettings)

|  | Declaration |
| --- | --- |
| From | ``` var audioSettings: [String : AnyObject]? { get } ``` |
| To | ``` var audioSettings: [String : Any]? { get } ``` |

Modified [AVOutputSettingsAssistant.videoSettings](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1386880-videosettings)

|  | Declaration |
| --- | --- |
| From | ``` var videoSettings: [String : AnyObject]? { get } ``` |
| To | ``` var videoSettings: [String : Any]? { get } ``` |

Modified [AVPlayer](https://developer.apple.com/documentation/avfoundation/avplayer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVPlayer : NSObject {     convenience init(URL URL: NSURL)     class func playerWithURL(_ URL: NSURL) -> Self     convenience init(playerItem item: AVPlayerItem)     class func playerWithPlayerItem(_ item: AVPlayerItem) -> Self     init(URL URL: NSURL)     init(playerItem item: AVPlayerItem)     var status: AVPlayerStatus { get }     var error: NSError? { get } } extension AVPlayer {     var rate: Float     func play()     func pause() } extension AVPlayer {     var currentItem: AVPlayerItem? { get }     func replaceCurrentItemWithPlayerItem(_ item: AVPlayerItem?)     var actionAtItemEnd: AVPlayerActionAtItemEnd } extension AVPlayer {     func currentTime() -> CMTime     func seekToDate(_ date: NSDate)     func seekToDate(_ date: NSDate, completionHandler completionHandler: (Bool) -> Void)     func seekToTime(_ time: CMTime)     func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime)     func seekToTime(_ time: CMTime, completionHandler completionHandler: (Bool) -> Void)     func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime, completionHandler completionHandler: (Bool) -> Void) } extension AVPlayer {     func setRate(_ rate: Float, time itemTime: CMTime, atHostTime hostClockTime: CMTime)     func prerollAtRate(_ rate: Float, completionHandler completionHandler: ((Bool) -> Void)?)     func cancelPendingPrerolls()     var masterClock: CMClock? } extension AVPlayer {     func addPeriodicTimeObserverForInterval(_ interval: CMTime, queue queue: dispatch_queue_t?, usingBlock block: (CMTime) -> Void) -> AnyObject     func addBoundaryTimeObserverForTimes(_ times: [NSValue], queue queue: dispatch_queue_t?, usingBlock block: () -> Void) -> AnyObject     func removeTimeObserver(_ observer: AnyObject) } extension AVPlayer {     var volume: Float     var muted: Bool     var closedCaptionDisplayEnabled: Bool } extension AVPlayer {     var appliesMediaSelectionCriteriaAutomatically: Bool     func setMediaSelectionCriteria(_ criteria: AVPlayerMediaSelectionCriteria?, forMediaCharacteristic mediaCharacteristic: String)     func mediaSelectionCriteriaForMediaCharacteristic(_ mediaCharacteristic: String) -> AVPlayerMediaSelectionCriteria? } extension AVPlayer {     var audioOutputDeviceUniqueID: String? } extension AVPlayer {     var allowsExternalPlayback: Bool     var externalPlaybackActive: Bool { get }     var usesExternalPlaybackWhileExternalScreenIsActive: Bool     var externalPlaybackVideoGravity: String } extension AVPlayer {     var allowsAirPlayVideo: Bool     var airPlayVideoActive: Bool { get }     var usesAirPlayVideoWhileAirPlayScreenIsActive: Bool } extension AVPlayer {     var outputObscuredDueToInsufficientExternalProtection: Bool { get } } ``` | -- |
| To | ``` class AVPlayer : NSObject {     convenience init(url URL: URL)     class func withURL(_ URL: URL) -> Self     convenience init(playerItem item: AVPlayerItem?)     class func withPlayerItem(_ item: AVPlayerItem?) -> Self     init(url URL: URL)     init(playerItem item: AVPlayerItem?)     var status: AVPlayerStatus { get }     var error: Error? { get }     var isOutputObscuredDueToInsufficientExternalProtection: Bool { get }     var allowsAirPlayVideo: Bool     var isAirPlayVideoActive: Bool { get }     var usesAirPlayVideoWhileAirPlayScreenIsActive: Bool     var allowsExternalPlayback: Bool     var isExternalPlaybackActive: Bool { get }     var usesExternalPlaybackWhileExternalScreenIsActive: Bool     var externalPlaybackVideoGravity: String     var audioOutputDeviceUniqueID: String?     var appliesMediaSelectionCriteriaAutomatically: Bool     func setMediaSelectionCriteria(_ criteria: AVPlayerMediaSelectionCriteria?, forMediaCharacteristic mediaCharacteristic: String)     func mediaSelectionCriteria(forMediaCharacteristic mediaCharacteristic: String) -> AVPlayerMediaSelectionCriteria?     var volume: Float     var isMuted: Bool     var isClosedCaptionDisplayEnabled: Bool     func addPeriodicTimeObserver(forInterval interval: CMTime, queue queue: DispatchQueue?, using block: @escaping (CMTime) -> Swift.Void) -> Any     func addBoundaryTimeObserver(forTimes times: [NSValue], queue queue: DispatchQueue?, using block: @escaping () -> Swift.Void) -> Any     func removeTimeObserver(_ observer: Any)     var automaticallyWaitsToMinimizeStalling: Bool     func setRate(_ rate: Float, time itemTime: CMTime, atHostTime hostClockTime: CMTime)     func preroll(atRate rate: Float, completionHandler completionHandler: (@escaping (Bool) -> Swift.Void)? = nil)     func cancelPendingPrerolls()     var masterClock: CMClock?     func currentTime() -> CMTime     func seek(to date: Date)     func seek(to date: Date, completionHandler completionHandler: @escaping (Bool) -> Swift.Void)     func seek(to time: CMTime)     func seek(to time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime)     func seek(to time: CMTime, completionHandler completionHandler: @escaping (Bool) -> Swift.Void)     func seek(to time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime, completionHandler completionHandler: @escaping (Bool) -> Swift.Void)     var currentItem: AVPlayerItem? { get }     func replaceCurrentItem(with item: AVPlayerItem?)     var actionAtItemEnd: AVPlayerActionAtItemEnd     var rate: Float     func play()     func pause()     var timeControlStatus: AVPlayerTimeControlStatus { get }     var reasonForWaitingToPlay: String? { get }     func playImmediately(atRate rate: Float)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVPlayer : CVarArg { } extension AVPlayer : Equatable, Hashable {     var hashValue: Int { get } } extension AVPlayer {     var rate: Float     func play()     func pause()     var timeControlStatus: AVPlayerTimeControlStatus { get }     var reasonForWaitingToPlay: String? { get }     func playImmediately(atRate rate: Float) } extension AVPlayer {     var currentItem: AVPlayerItem? { get }     func replaceCurrentItem(with item: AVPlayerItem?)     var actionAtItemEnd: AVPlayerActionAtItemEnd } extension AVPlayer {     func currentTime() -> CMTime     func seek(to date: Date)     func seek(to date: Date, completionHandler completionHandler: @escaping (Bool) -> Swift.Void)     func seek(to time: CMTime)     func seek(to time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime)     func seek(to time: CMTime, completionHandler completionHandler: @escaping (Bool) -> Swift.Void)     func seek(to time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime, completionHandler completionHandler: @escaping (Bool) -> Swift.Void) } extension AVPlayer {     var automaticallyWaitsToMinimizeStalling: Bool     func setRate(_ rate: Float, time itemTime: CMTime, atHostTime hostClockTime: CMTime)     func preroll(atRate rate: Float, completionHandler completionHandler: (@escaping (Bool) -> Swift.Void)? = nil)     func cancelPendingPrerolls()     var masterClock: CMClock? } extension AVPlayer {     func addPeriodicTimeObserver(forInterval interval: CMTime, queue queue: DispatchQueue?, using block: @escaping (CMTime) -> Swift.Void) -> Any     func addBoundaryTimeObserver(forTimes times: [NSValue], queue queue: DispatchQueue?, using block: @escaping () -> Swift.Void) -> Any     func removeTimeObserver(_ observer: Any) } extension AVPlayer {     var volume: Float     var isMuted: Bool     var isClosedCaptionDisplayEnabled: Bool } extension AVPlayer {     var appliesMediaSelectionCriteriaAutomatically: Bool     func setMediaSelectionCriteria(_ criteria: AVPlayerMediaSelectionCriteria?, forMediaCharacteristic mediaCharacteristic: String)     func mediaSelectionCriteria(forMediaCharacteristic mediaCharacteristic: String) -> AVPlayerMediaSelectionCriteria? } extension AVPlayer {     var audioOutputDeviceUniqueID: String? } extension AVPlayer {     var allowsExternalPlayback: Bool     var isExternalPlaybackActive: Bool { get }     var usesExternalPlaybackWhileExternalScreenIsActive: Bool     var externalPlaybackVideoGravity: String } extension AVPlayer {     var allowsAirPlayVideo: Bool     var isAirPlayVideoActive: Bool { get }     var usesAirPlayVideoWhileAirPlayScreenIsActive: Bool } extension AVPlayer {     var isOutputObscuredDueToInsufficientExternalProtection: Bool { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVPlayer.addBoundaryTimeObserver(forTimes: [NSValue], queue: DispatchQueue?, using: () -> Swift.Void) -> Any](https://developer.apple.com/documentation/avfoundation/avplayer/1388027-addboundarytimeobserverfortimes)

|  | Declaration |
| --- | --- |
| From | ``` func addBoundaryTimeObserverForTimes(_ times: [NSValue], queue queue: dispatch_queue_t?, usingBlock block: () -> Void) -> AnyObject ``` |
| To | ``` func addBoundaryTimeObserver(forTimes times: [NSValue], queue queue: DispatchQueue?, using block: @escaping () -> Swift.Void) -> Any ``` |

Modified [AVPlayer.addPeriodicTimeObserver(forInterval: CMTime, queue: DispatchQueue?, using: (CMTime) -> Swift.Void) -> Any](https://developer.apple.com/documentation/avfoundation/avplayer/1385829-addperiodictimeobserverforinterv)

|  | Declaration |
| --- | --- |
| From | ``` func addPeriodicTimeObserverForInterval(_ interval: CMTime, queue queue: dispatch_queue_t?, usingBlock block: (CMTime) -> Void) -> AnyObject ``` |
| To | ``` func addPeriodicTimeObserver(forInterval interval: CMTime, queue queue: DispatchQueue?, using block: @escaping (CMTime) -> Swift.Void) -> Any ``` |

Modified [AVPlayer.error](https://developer.apple.com/documentation/avfoundation/avplayer/1387764-error)

|  | Declaration |
| --- | --- |
| From | ``` var error: NSError? { get } ``` |
| To | ``` var error: Error? { get } ``` |

Modified [AVPlayer.init(playerItem: AVPlayerItem?)](https://developer.apple.com/documentation/avfoundation/avplayer/1387104-initwithplayeritem)

|  | Declaration |
| --- | --- |
| From | ``` init(playerItem item: AVPlayerItem) ``` |
| To | ``` init(playerItem item: AVPlayerItem?) ``` |

Modified [AVPlayer.init(url: URL)](https://developer.apple.com/documentation/avfoundation/avplayer/1385706-init)

|  | Declaration |
| --- | --- |
| From | ``` init(URL URL: NSURL) ``` |
| To | ``` init(url URL: URL) ``` |

Modified [AVPlayer.isClosedCaptionDisplayEnabled](https://developer.apple.com/documentation/avfoundation/avplayer/1386458-isclosedcaptiondisplayenabled)

|  | Declaration |
| --- | --- |
| From | ``` var closedCaptionDisplayEnabled: Bool ``` |
| To | ``` var isClosedCaptionDisplayEnabled: Bool ``` |

Modified [AVPlayer.isExternalPlaybackActive](https://developer.apple.com/documentation/avfoundation/avplayer/1388982-isexternalplaybackactive)

|  | Declaration |
| --- | --- |
| From | ``` var externalPlaybackActive: Bool { get } ``` |
| To | ``` var isExternalPlaybackActive: Bool { get } ``` |

Modified [AVPlayer.isMuted](https://developer.apple.com/documentation/avfoundation/avplayer/1387544-muted)

|  | Declaration |
| --- | --- |
| From | ``` var muted: Bool ``` |
| To | ``` var isMuted: Bool ``` |

Modified [AVPlayer.isOutputObscuredDueToInsufficientExternalProtection](https://developer.apple.com/documentation/avfoundation/avplayer/1624254-isoutputobscuredduetoinsufficien)

|  | Declaration |
| --- | --- |
| From | ``` var outputObscuredDueToInsufficientExternalProtection: Bool { get } ``` |
| To | ``` var isOutputObscuredDueToInsufficientExternalProtection: Bool { get } ``` |

Modified [AVPlayer.mediaSelectionCriteria(forMediaCharacteristic: String) -> AVPlayerMediaSelectionCriteria?](https://developer.apple.com/documentation/avfoundation/avplayer/1387825-mediaselectioncriteria)

|  | Declaration |
| --- | --- |
| From | ``` func mediaSelectionCriteriaForMediaCharacteristic(_ mediaCharacteristic: String) -> AVPlayerMediaSelectionCriteria? ``` |
| To | ``` func mediaSelectionCriteria(forMediaCharacteristic mediaCharacteristic: String) -> AVPlayerMediaSelectionCriteria? ``` |

Modified [AVPlayer.preroll(atRate: Float, completionHandler: ( (Bool) -> Swift.Void)?)](https://developer.apple.com/documentation/avfoundation/avplayer/1389712-preroll)

|  | Declaration |
| --- | --- |
| From | ``` func prerollAtRate(_ rate: Float, completionHandler completionHandler: ((Bool) -> Void)?) ``` |
| To | ``` func preroll(atRate rate: Float, completionHandler completionHandler: (@escaping (Bool) -> Swift.Void)? = nil) ``` |

Modified [AVPlayer.removeTimeObserver(_: Any)](https://developer.apple.com/documentation/avfoundation/avplayer/1387552-removetimeobserver)

|  | Declaration |
| --- | --- |
| From | ``` func removeTimeObserver(_ observer: AnyObject) ``` |
| To | ``` func removeTimeObserver(_ observer: Any) ``` |

Modified [AVPlayer.replaceCurrentItem(with: AVPlayerItem?)](https://developer.apple.com/documentation/avfoundation/avplayer/1390806-replacecurrentitem)

|  | Declaration |
| --- | --- |
| From | ``` func replaceCurrentItemWithPlayerItem(_ item: AVPlayerItem?) ``` |
| To | ``` func replaceCurrentItem(with item: AVPlayerItem?) ``` |

Modified [AVPlayer.seek(to: CMTime)](https://developer.apple.com/documentation/avfoundation/avplayer/1385953-seek)

|  | Declaration |
| --- | --- |
| From | ``` func seekToTime(_ time: CMTime) ``` |
| To | ``` func seek(to time: CMTime) ``` |

Modified [AVPlayer.seek(to: Date)](https://developer.apple.com/documentation/avfoundation/avplayer/1386114-seektodate)

|  | Declaration |
| --- | --- |
| From | ``` func seekToDate(_ date: NSDate) ``` |
| To | ``` func seek(to date: Date) ``` |

Modified [AVPlayer.seek(to: CMTime, completionHandler: (Bool) -> Swift.Void)](https://developer.apple.com/documentation/avfoundation/avplayer/1387018-seektotime)

|  | Declaration |
| --- | --- |
| From | ``` func seekToTime(_ time: CMTime, completionHandler completionHandler: (Bool) -> Void) ``` |
| To | ``` func seek(to time: CMTime, completionHandler completionHandler: @escaping (Bool) -> Swift.Void) ``` |

Modified [AVPlayer.seek(to: Date, completionHandler: (Bool) -> Swift.Void)](https://developer.apple.com/documentation/avfoundation/avplayer/1386108-seektodate)

|  | Declaration |
| --- | --- |
| From | ``` func seekToDate(_ date: NSDate, completionHandler completionHandler: (Bool) -> Void) ``` |
| To | ``` func seek(to date: Date, completionHandler completionHandler: @escaping (Bool) -> Swift.Void) ``` |

Modified [AVPlayer.seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime)](https://developer.apple.com/documentation/avfoundation/avplayer/1387741-seek)

|  | Declaration |
| --- | --- |
| From | ``` func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime) ``` |
| To | ``` func seek(to time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime) ``` |

Modified [AVPlayer.seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: (Bool) -> Swift.Void)](https://developer.apple.com/documentation/avfoundation/avplayer/1388493-seektotime)

|  | Declaration |
| --- | --- |
| From | ``` func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime, completionHandler completionHandler: (Bool) -> Void) ``` |
| To | ``` func seek(to time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime, completionHandler completionHandler: @escaping (Bool) -> Swift.Void) ``` |

Modified [AVPlayerActionAtItemEnd [enum]](https://developer.apple.com/documentation/avfoundation/avplayer/actionatitemend)

|  | Declaration |
| --- | --- |
| From | ``` enum AVPlayerActionAtItemEnd : Int {     case Advance     case Pause     case None } ``` |
| To | ``` enum AVPlayerActionAtItemEnd : Int {     case advance     case pause     case none } ``` |

Modified [AVPlayerActionAtItemEnd.advance](https://developer.apple.com/documentation/avfoundation/avplayer/actionatitemend/advance)

|  | Declaration |
| --- | --- |
| From | ``` case Advance ``` |
| To | ``` case advance ``` |

Modified [AVPlayerActionAtItemEnd.none](https://developer.apple.com/documentation/avfoundation/avplayer/actionatitemend/none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [AVPlayerActionAtItemEnd.pause](https://developer.apple.com/documentation/avfoundation/avplayer/actionatitemend/pause)

|  | Declaration |
| --- | --- |
| From | ``` case Pause ``` |
| To | ``` case pause ``` |

Modified [AVPlayerItem](https://developer.apple.com/documentation/avfoundation/avplayeritem)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVPlayerItem : NSObject, NSCopying {     convenience init()      init(URL URL: NSURL)     class func playerItemWithURL(_ URL: NSURL) -> AVPlayerItem      init(asset asset: AVAsset)     class func playerItemWithAsset(_ asset: AVAsset) -> AVPlayerItem      init(asset asset: AVAsset, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [String]?)     class func playerItemWithAsset(_ asset: AVAsset, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [String]?) -> AVPlayerItem     convenience init(URL URL: NSURL)     convenience init(asset asset: AVAsset)     init(asset asset: AVAsset, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [String]?)     var status: AVPlayerItemStatus { get }     var error: NSError? { get } } extension AVPlayerItem {     var asset: AVAsset { get }     var tracks: [AVPlayerItemTrack] { get }     var duration: CMTime { get }     var presentationSize: CGSize { get }     var timedMetadata: [AVMetadataItem]? { get }     var automaticallyLoadedAssetKeys: [String] { get } } extension AVPlayerItem {     var canPlayFastForward: Bool { get }     var canPlaySlowForward: Bool { get }     var canPlayReverse: Bool { get }     var canPlaySlowReverse: Bool { get }     var canPlayFastReverse: Bool { get }     var canStepForward: Bool { get }     var canStepBackward: Bool { get } } extension AVPlayerItem {     func currentTime() -> CMTime     var forwardPlaybackEndTime: CMTime     var reversePlaybackEndTime: CMTime     var seekableTimeRanges: [NSValue] { get }     func seekToTime(_ time: CMTime)     func seekToTime(_ time: CMTime, completionHandler completionHandler: (Bool) -> Void)     func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime)     func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime, completionHandler completionHandler: (Bool) -> Void)     func cancelPendingSeeks()     func currentDate() -> NSDate?     func seekToDate(_ date: NSDate) -> Bool     func seekToDate(_ date: NSDate, completionHandler completionHandler: (Bool) -> Void) -> Bool     func stepByCount(_ stepCount: Int)     var timebase: CMTimebase? { get } } extension AVPlayerItem {     @NSCopying var videoComposition: AVVideoComposition?     var customVideoCompositor: AVVideoCompositing? { get }     var seekingWaitsForVideoCompositionRendering: Bool     var textStyleRules: [AVTextStyleRule]? } extension AVPlayerItem {     var audioTimePitchAlgorithm: String     @NSCopying var audioMix: AVAudioMix? } extension AVPlayerItem {     var loadedTimeRanges: [NSValue] { get }     var playbackLikelyToKeepUp: Bool { get }     var playbackBufferFull: Bool { get }     var playbackBufferEmpty: Bool { get }     var canUseNetworkResourcesForLiveStreamingWhilePaused: Bool } extension AVPlayerItem {     var preferredPeakBitRate: Double } extension AVPlayerItem {     func selectMediaOption(_ mediaSelectionOption: AVMediaSelectionOption?, inMediaSelectionGroup mediaSelectionGroup: AVMediaSelectionGroup)     func selectMediaOptionAutomaticallyInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup)     func selectedMediaOptionInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption?     var currentMediaSelection: AVMediaSelection { get } } extension AVPlayerItem {     func accessLog() -> AVPlayerItemAccessLog?     func errorLog() -> AVPlayerItemErrorLog? } extension AVPlayerItem {     func addOutput(_ output: AVPlayerItemOutput)     func removeOutput(_ output: AVPlayerItemOutput)     var outputs: [AVPlayerItemOutput] { get } } extension AVPlayerItem {     func addMediaDataCollector(_ collector: AVPlayerItemMediaDataCollector)     func removeMediaDataCollector(_ collector: AVPlayerItemMediaDataCollector)     var mediaDataCollectors: [AVPlayerItemMediaDataCollector] { get } } extension AVPlayerItem {     var navigationMarkerGroups: [AVNavigationMarkersGroup]     var externalMetadata: [AVMetadataItem]     var interstitialTimeRanges: [AVInterstitialTimeRange] } extension AVPlayerItem {     var externalSubtitleOptionLanguages: [String]     var selectedExternalSubtitleOptionLanguage: String } ``` | NSCopying |
| To | ``` class AVPlayerItem : NSObject, NSCopying {     convenience init()     convenience init(url URL: URL)     class func withURL(_ URL: URL) -> Self     convenience init(asset asset: AVAsset)     class func withAsset(_ asset: AVAsset) -> Self     convenience init(asset asset: AVAsset, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [String]?)     class func withAsset(_ asset: AVAsset, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [String]?) -> Self     convenience init(url URL: URL)     convenience init(asset asset: AVAsset)     init(asset asset: AVAsset, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [String]?)     var status: AVPlayerItemStatus { get }     var error: Error? { get }     func add(_ collector: AVPlayerItemMediaDataCollector)     func remove(_ collector: AVPlayerItemMediaDataCollector)     var mediaDataCollectors: [AVPlayerItemMediaDataCollector] { get }     func add(_ output: AVPlayerItemOutput)     func remove(_ output: AVPlayerItemOutput)     var outputs: [AVPlayerItemOutput] { get }     func accessLog() -> AVPlayerItemAccessLog?     func errorLog() -> AVPlayerItemErrorLog?     func select(_ mediaSelectionOption: AVMediaSelectionOption?, in mediaSelectionGroup: AVMediaSelectionGroup)     func selectMediaOptionAutomatically(in mediaSelectionGroup: AVMediaSelectionGroup)     func selectedMediaOption(in mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption?     var currentMediaSelection: AVMediaSelection { get }     var preferredPeakBitRate: Double     var loadedTimeRanges: [NSValue] { get }     var isPlaybackLikelyToKeepUp: Bool { get }     var isPlaybackBufferFull: Bool { get }     var isPlaybackBufferEmpty: Bool { get }     var canUseNetworkResourcesForLiveStreamingWhilePaused: Bool     var preferredForwardBufferDuration: TimeInterval     var audioTimePitchAlgorithm: String     @NSCopying var audioMix: AVAudioMix?     @NSCopying var videoComposition: AVVideoComposition?     var customVideoCompositor: AVVideoCompositing? { get }     var seekingWaitsForVideoCompositionRendering: Bool     var textStyleRules: [AVTextStyleRule]?     func currentTime() -> CMTime     var forwardPlaybackEndTime: CMTime     var reversePlaybackEndTime: CMTime     var seekableTimeRanges: [NSValue] { get }     func seek(to time: CMTime)     func seek(to time: CMTime, completionHandler completionHandler: @escaping (Bool) -> Swift.Void)     func seek(to time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime)     func seek(to time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime, completionHandler completionHandler: @escaping (Bool) -> Swift.Void)     func cancelPendingSeeks()     func currentDate() -> Date?     func seek(to date: Date) -> Bool     func seek(to date: Date, completionHandler completionHandler: @escaping (Bool) -> Swift.Void) -> Bool     func step(byCount stepCount: Int)     var timebase: CMTimebase? { get }     var canPlayFastForward: Bool { get }     var canPlaySlowForward: Bool { get }     var canPlayReverse: Bool { get }     var canPlaySlowReverse: Bool { get }     var canPlayFastReverse: Bool { get }     var canStepForward: Bool { get }     var canStepBackward: Bool { get }     var asset: AVAsset { get }     var tracks: [AVPlayerItemTrack] { get }     var duration: CMTime { get }     var presentationSize: CGSize { get }     var timedMetadata: [AVMetadataItem]? { get }     var automaticallyLoadedAssetKeys: [String] { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVPlayerItem : CVarArg { } extension AVPlayerItem : Equatable, Hashable {     var hashValue: Int { get } } extension AVPlayerItem {     var asset: AVAsset { get }     var tracks: [AVPlayerItemTrack] { get }     var duration: CMTime { get }     var presentationSize: CGSize { get }     var timedMetadata: [AVMetadataItem]? { get }     var automaticallyLoadedAssetKeys: [String] { get } } extension AVPlayerItem {     var canPlayFastForward: Bool { get }     var canPlaySlowForward: Bool { get }     var canPlayReverse: Bool { get }     var canPlaySlowReverse: Bool { get }     var canPlayFastReverse: Bool { get }     var canStepForward: Bool { get }     var canStepBackward: Bool { get } } extension AVPlayerItem {     func currentTime() -> CMTime     var forwardPlaybackEndTime: CMTime     var reversePlaybackEndTime: CMTime     var seekableTimeRanges: [NSValue] { get }     func seek(to time: CMTime)     func seek(to time: CMTime, completionHandler completionHandler: @escaping (Bool) -> Swift.Void)     func seek(to time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime)     func seek(to time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime, completionHandler completionHandler: @escaping (Bool) -> Swift.Void)     func cancelPendingSeeks()     func currentDate() -> Date?     func seek(to date: Date) -> Bool     func seek(to date: Date, completionHandler completionHandler: @escaping (Bool) -> Swift.Void) -> Bool     func step(byCount stepCount: Int)     var timebase: CMTimebase? { get } } extension AVPlayerItem {     @NSCopying var videoComposition: AVVideoComposition?     var customVideoCompositor: AVVideoCompositing? { get }     var seekingWaitsForVideoCompositionRendering: Bool     var textStyleRules: [AVTextStyleRule]? } extension AVPlayerItem {     var audioTimePitchAlgorithm: String     @NSCopying var audioMix: AVAudioMix? } extension AVPlayerItem {     var loadedTimeRanges: [NSValue] { get }     var isPlaybackLikelyToKeepUp: Bool { get }     var isPlaybackBufferFull: Bool { get }     var isPlaybackBufferEmpty: Bool { get }     var canUseNetworkResourcesForLiveStreamingWhilePaused: Bool     var preferredForwardBufferDuration: TimeInterval } extension AVPlayerItem {     var preferredPeakBitRate: Double } extension AVPlayerItem {     func select(_ mediaSelectionOption: AVMediaSelectionOption?, in mediaSelectionGroup: AVMediaSelectionGroup)     func selectMediaOptionAutomatically(in mediaSelectionGroup: AVMediaSelectionGroup)     func selectedMediaOption(in mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption?     var currentMediaSelection: AVMediaSelection { get } } extension AVPlayerItem {     func accessLog() -> AVPlayerItemAccessLog?     func errorLog() -> AVPlayerItemErrorLog? } extension AVPlayerItem {     func add(_ output: AVPlayerItemOutput)     func remove(_ output: AVPlayerItemOutput)     var outputs: [AVPlayerItemOutput] { get } } extension AVPlayerItem {     func add(_ collector: AVPlayerItemMediaDataCollector)     func remove(_ collector: AVPlayerItemMediaDataCollector)     var mediaDataCollectors: [AVPlayerItemMediaDataCollector] { get } } extension AVPlayerItem {     var nextContentProposal: AVContentProposal? } extension AVPlayerItem {     var navigationMarkerGroups: [AVNavigationMarkersGroup]     var externalMetadata: [AVMetadataItem]     var interstitialTimeRanges: [AVInterstitialTimeRange] } extension AVPlayerItem {     var externalSubtitleOptionLanguages: [String]     var selectedExternalSubtitleOptionLanguage: String } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [AVPlayerItem.add(_: AVPlayerItemOutput)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389782-add)

|  | Declaration |
| --- | --- |
| From | ``` func addOutput(_ output: AVPlayerItemOutput) ``` |
| To | ``` func add(_ output: AVPlayerItemOutput) ``` |

Modified [AVPlayerItem.add(_: AVPlayerItemMediaDataCollector)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1624164-addmediadatacollector)

|  | Declaration |
| --- | --- |
| From | ``` func addMediaDataCollector(_ collector: AVPlayerItemMediaDataCollector) ``` |
| To | ``` func add(_ collector: AVPlayerItemMediaDataCollector) ``` |

Modified [AVPlayerItem.currentDate() -> Date?](https://developer.apple.com/documentation/avfoundation/avplayeritem/1386188-currentdate)

|  | Declaration |
| --- | --- |
| From | ``` func currentDate() -> NSDate? ``` |
| To | ``` func currentDate() -> Date? ``` |

Modified [AVPlayerItem.error](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389185-error)

|  | Declaration |
| --- | --- |
| From | ``` var error: NSError? { get } ``` |
| To | ``` var error: Error? { get } ``` |

Modified [AVPlayerItem.init(url: URL)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387558-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(URL URL: NSURL) ``` |
| To | ``` convenience init(url URL: URL) ``` |

Modified [AVPlayerItem.isPlaybackBufferEmpty](https://developer.apple.com/documentation/avfoundation/avplayeritem/1386960-playbackbufferempty)

|  | Declaration |
| --- | --- |
| From | ``` var playbackBufferEmpty: Bool { get } ``` |
| To | ``` var isPlaybackBufferEmpty: Bool { get } ``` |

Modified [AVPlayerItem.isPlaybackBufferFull](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388852-isplaybackbufferfull)

|  | Declaration |
| --- | --- |
| From | ``` var playbackBufferFull: Bool { get } ``` |
| To | ``` var isPlaybackBufferFull: Bool { get } ``` |

Modified [AVPlayerItem.isPlaybackLikelyToKeepUp](https://developer.apple.com/documentation/avfoundation/avplayeritem/1390348-playbacklikelytokeepup)

|  | Declaration |
| --- | --- |
| From | ``` var playbackLikelyToKeepUp: Bool { get } ``` |
| To | ``` var isPlaybackLikelyToKeepUp: Bool { get } ``` |

Modified [AVPlayerItem.remove(_: AVPlayerItemMediaDataCollector)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1624163-remove)

|  | Declaration |
| --- | --- |
| From | ``` func removeMediaDataCollector(_ collector: AVPlayerItemMediaDataCollector) ``` |
| To | ``` func remove(_ collector: AVPlayerItemMediaDataCollector) ``` |

Modified [AVPlayerItem.remove(_: AVPlayerItemOutput)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388756-remove)

|  | Declaration |
| --- | --- |
| From | ``` func removeOutput(_ output: AVPlayerItemOutput) ``` |
| To | ``` func remove(_ output: AVPlayerItemOutput) ``` |

Modified [AVPlayerItem.seek(to: CMTime)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1390153-seektotime)

|  | Declaration |
| --- | --- |
| From | ``` func seekToTime(_ time: CMTime) ``` |
| To | ``` func seek(to time: CMTime) ``` |

Modified [AVPlayerItem.seek(to: Date) -> Bool](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389067-seektodate)

|  | Declaration |
| --- | --- |
| From | ``` func seekToDate(_ date: NSDate) -> Bool ``` |
| To | ``` func seek(to date: Date) -> Bool ``` |

Modified [AVPlayerItem.seek(to: Date, completionHandler: (Bool) -> Swift.Void) -> Bool](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389877-seek)

|  | Declaration |
| --- | --- |
| From | ``` func seekToDate(_ date: NSDate, completionHandler completionHandler: (Bool) -> Void) -> Bool ``` |
| To | ``` func seek(to date: Date, completionHandler completionHandler: @escaping (Bool) -> Swift.Void) -> Bool ``` |

Modified [AVPlayerItem.seek(to: CMTime, completionHandler: (Bool) -> Swift.Void)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387418-seek)

|  | Declaration |
| --- | --- |
| From | ``` func seekToTime(_ time: CMTime, completionHandler completionHandler: (Bool) -> Void) ``` |
| To | ``` func seek(to time: CMTime, completionHandler completionHandler: @escaping (Bool) -> Swift.Void) ``` |

Modified [AVPlayerItem.seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1385620-seektotime)

|  | Declaration |
| --- | --- |
| From | ``` func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime) ``` |
| To | ``` func seek(to time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime) ``` |

Modified [AVPlayerItem.seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: (Bool) -> Swift.Void)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387753-seek)

|  | Declaration |
| --- | --- |
| From | ``` func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime, completionHandler completionHandler: (Bool) -> Void) ``` |
| To | ``` func seek(to time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime, completionHandler completionHandler: @escaping (Bool) -> Swift.Void) ``` |

Modified [AVPlayerItem.select(_: AVMediaSelectionOption?, in: AVMediaSelectionGroup)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389610-selectmediaoption)

|  | Declaration |
| --- | --- |
| From | ``` func selectMediaOption(_ mediaSelectionOption: AVMediaSelectionOption?, inMediaSelectionGroup mediaSelectionGroup: AVMediaSelectionGroup) ``` |
| To | ``` func select(_ mediaSelectionOption: AVMediaSelectionOption?, in mediaSelectionGroup: AVMediaSelectionGroup) ``` |

Modified [AVPlayerItem.selectedMediaOption(in: AVMediaSelectionGroup) -> AVMediaSelectionOption?](https://developer.apple.com/documentation/avfoundation/avplayeritem/1386314-selectedmediaoptioninmediaselect)

|  | Declaration |
| --- | --- |
| From | ``` func selectedMediaOptionInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption? ``` |
| To | ``` func selectedMediaOption(in mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption? ``` |

Modified [AVPlayerItem.selectMediaOptionAutomatically(in: AVMediaSelectionGroup)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388268-selectmediaoptionautomatically)

|  | Declaration |
| --- | --- |
| From | ``` func selectMediaOptionAutomaticallyInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup) ``` |
| To | ``` func selectMediaOptionAutomatically(in mediaSelectionGroup: AVMediaSelectionGroup) ``` |

Modified [AVPlayerItem.step(byCount: Int)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387968-step)

|  | Declaration |
| --- | --- |
| From | ``` func stepByCount(_ stepCount: Int) ``` |
| To | ``` func step(byCount stepCount: Int) ``` |

Modified [AVPlayerItemAccessLog](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslog)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVPlayerItemAccessLog : NSObject, NSCopying {     func extendedLogData() -> NSData?     var extendedLogDataStringEncoding: UInt { get }     var events: [AVPlayerItemAccessLogEvent] { get } } ``` | NSCopying |
| To | ``` class AVPlayerItemAccessLog : NSObject, NSCopying {     init()     func extendedLogData() -> Data?     var extendedLogDataStringEncoding: UInt { get }     var events: [AVPlayerItemAccessLogEvent] { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVPlayerItemAccessLog : CVarArg { } extension AVPlayerItemAccessLog : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [AVPlayerItemAccessLog.extendedLogData() -> Data?](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslog/1386892-extendedlogdata)

|  | Declaration |
| --- | --- |
| From | ``` func extendedLogData() -> NSData? ``` |
| To | ``` func extendedLogData() -> Data? ``` |

Modified [AVPlayerItemAccessLogEvent](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVPlayerItemAccessLogEvent : NSObject, NSCopying {     var numberOfSegmentsDownloaded: Int { get }     var numberOfMediaRequests: Int { get }     var playbackStartDate: NSDate? { get }     var URI: String? { get }     var serverAddress: String? { get }     var numberOfServerAddressChanges: Int { get }     var playbackSessionID: String? { get }     var playbackStartOffset: NSTimeInterval { get }     var segmentsDownloadedDuration: NSTimeInterval { get }     var durationWatched: NSTimeInterval { get }     var numberOfStalls: Int { get }     var numberOfBytesTransferred: Int64 { get }     var transferDuration: NSTimeInterval { get }     var observedBitrate: Double { get }     var indicatedBitrate: Double { get }     var numberOfDroppedVideoFrames: Int { get }     var startupTime: NSTimeInterval { get }     var downloadOverdue: Int { get }     var observedMaxBitrate: Double { get }     var observedMinBitrate: Double { get }     var observedBitrateStandardDeviation: Double { get }     var playbackType: String? { get }     var mediaRequestsWWAN: Int { get }     var switchBitrate: Double { get } } ``` | NSCopying |
| To | ``` class AVPlayerItemAccessLogEvent : NSObject, NSCopying {     init()     var numberOfSegmentsDownloaded: Int { get }     var numberOfMediaRequests: Int { get }     var playbackStartDate: Date? { get }     var uri: String? { get }     var serverAddress: String? { get }     var numberOfServerAddressChanges: Int { get }     var playbackSessionID: String? { get }     var playbackStartOffset: TimeInterval { get }     var segmentsDownloadedDuration: TimeInterval { get }     var durationWatched: TimeInterval { get }     var numberOfStalls: Int { get }     var numberOfBytesTransferred: Int64 { get }     var transferDuration: TimeInterval { get }     var observedBitrate: Double { get }     var indicatedBitrate: Double { get }     var indicatedAverageBitrate: Double { get }     var averageVideoBitrate: Double { get }     var averageAudioBitrate: Double { get }     var numberOfDroppedVideoFrames: Int { get }     var startupTime: TimeInterval { get }     var downloadOverdue: Int { get }     var observedMaxBitrate: Double { get }     var observedMinBitrate: Double { get }     var observedBitrateStandardDeviation: Double { get }     var playbackType: String? { get }     var mediaRequestsWWAN: Int { get }     var switchBitrate: Double { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVPlayerItemAccessLogEvent : CVarArg { } extension AVPlayerItemAccessLogEvent : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [AVPlayerItemAccessLogEvent.durationWatched](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1388200-durationwatched)

|  | Declaration |
| --- | --- |
| From | ``` var durationWatched: NSTimeInterval { get } ``` |
| To | ``` var durationWatched: TimeInterval { get } ``` |

Modified [AVPlayerItemAccessLogEvent.playbackStartDate](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1390502-playbackstartdate)

|  | Declaration |
| --- | --- |
| From | ``` var playbackStartDate: NSDate? { get } ``` |
| To | ``` var playbackStartDate: Date? { get } ``` |

Modified [AVPlayerItemAccessLogEvent.playbackStartOffset](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1385922-playbackstartoffset)

|  | Declaration |
| --- | --- |
| From | ``` var playbackStartOffset: NSTimeInterval { get } ``` |
| To | ``` var playbackStartOffset: TimeInterval { get } ``` |

Modified [AVPlayerItemAccessLogEvent.segmentsDownloadedDuration](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1388147-segmentsdownloadedduration)

|  | Declaration |
| --- | --- |
| From | ``` var segmentsDownloadedDuration: NSTimeInterval { get } ``` |
| To | ``` var segmentsDownloadedDuration: TimeInterval { get } ``` |

Modified [AVPlayerItemAccessLogEvent.startupTime](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1389138-startuptime)

|  | Declaration |
| --- | --- |
| From | ``` var startupTime: NSTimeInterval { get } ``` |
| To | ``` var startupTime: TimeInterval { get } ``` |

Modified [AVPlayerItemAccessLogEvent.transferDuration](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1387370-transferduration)

|  | Declaration |
| --- | --- |
| From | ``` var transferDuration: NSTimeInterval { get } ``` |
| To | ``` var transferDuration: TimeInterval { get } ``` |

Modified [AVPlayerItemAccessLogEvent.uri](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1388643-uri)

|  | Declaration |
| --- | --- |
| From | ``` var URI: String? { get } ``` |
| To | ``` var uri: String? { get } ``` |

Modified [AVPlayerItemErrorLog](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlog)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVPlayerItemErrorLog : NSObject, NSCopying {     func extendedLogData() -> NSData?     var extendedLogDataStringEncoding: UInt { get }     var events: [AVPlayerItemErrorLogEvent] { get } } ``` | NSCopying |
| To | ``` class AVPlayerItemErrorLog : NSObject, NSCopying {     init()     func extendedLogData() -> Data?     var extendedLogDataStringEncoding: UInt { get }     var events: [AVPlayerItemErrorLogEvent] { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVPlayerItemErrorLog : CVarArg { } extension AVPlayerItemErrorLog : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [AVPlayerItemErrorLog.extendedLogData() -> Data?](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlog/1389100-extendedlogdata)

|  | Declaration |
| --- | --- |
| From | ``` func extendedLogData() -> NSData? ``` |
| To | ``` func extendedLogData() -> Data? ``` |

Modified [AVPlayerItemErrorLogEvent](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVPlayerItemErrorLogEvent : NSObject, NSCopying {     var date: NSDate? { get }     var URI: String? { get }     var serverAddress: String? { get }     var playbackSessionID: String? { get }     var errorStatusCode: Int { get }     var errorDomain: String { get }     var errorComment: String? { get } } ``` | NSCopying |
| To | ``` class AVPlayerItemErrorLogEvent : NSObject, NSCopying {     init()     var date: Date? { get }     var uri: String? { get }     var serverAddress: String? { get }     var playbackSessionID: String? { get }     var errorStatusCode: Int { get }     var errorDomain: String { get }     var errorComment: String? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVPlayerItemErrorLogEvent : CVarArg { } extension AVPlayerItemErrorLogEvent : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [AVPlayerItemErrorLogEvent.date](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/1388416-date)

|  | Declaration |
| --- | --- |
| From | ``` var date: NSDate? { get } ``` |
| To | ``` var date: Date? { get } ``` |

Modified [AVPlayerItemErrorLogEvent.uri](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/1389302-uri)

|  | Declaration |
| --- | --- |
| From | ``` var URI: String? { get } ``` |
| To | ``` var uri: String? { get } ``` |

Modified [AVPlayerItemLegibleOutput](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput)

|  | Declaration |
| --- | --- |
| From | ``` class AVPlayerItemLegibleOutput : AVPlayerItemOutput {     func setDelegate(_ delegate: AVPlayerItemLegibleOutputPushDelegate?, queue delegateQueue: dispatch_queue_t?)     weak var delegate: AVPlayerItemLegibleOutputPushDelegate? { get }     var delegateQueue: dispatch_queue_t? { get }     var advanceIntervalForDelegateInvocation: NSTimeInterval } extension AVPlayerItemLegibleOutput {     init(mediaSubtypesForNativeRepresentation subtypes: [NSNumber]) } extension AVPlayerItemLegibleOutput {     var textStylingResolution: String } ``` |
| To | ``` class AVPlayerItemLegibleOutput : AVPlayerItemOutput {     func setDelegate(_ delegate: AVPlayerItemLegibleOutputPushDelegate?, queue delegateQueue: DispatchQueue?)     weak var delegate: AVPlayerItemLegibleOutputPushDelegate? { get }     var delegateQueue: DispatchQueue? { get }     var advanceIntervalForDelegateInvocation: TimeInterval     var textStylingResolution: String     init(mediaSubtypesForNativeRepresentation subtypes: [NSNumber]) } extension AVPlayerItemLegibleOutput {     init(mediaSubtypesForNativeRepresentation subtypes: [NSNumber]) } extension AVPlayerItemLegibleOutput {     var textStylingResolution: String } ``` |

Modified [AVPlayerItemLegibleOutput.advanceIntervalForDelegateInvocation](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/1388098-advanceintervalfordelegateinvoca)

|  | Declaration |
| --- | --- |
| From | ``` var advanceIntervalForDelegateInvocation: NSTimeInterval ``` |
| To | ``` var advanceIntervalForDelegateInvocation: TimeInterval ``` |

Modified [AVPlayerItemLegibleOutput.delegateQueue](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/1386275-delegatequeue)

|  | Declaration |
| --- | --- |
| From | ``` var delegateQueue: dispatch_queue_t? { get } ``` |
| To | ``` var delegateQueue: DispatchQueue? { get } ``` |

Modified [AVPlayerItemLegibleOutput.setDelegate(_: AVPlayerItemLegibleOutputPushDelegate?, queue: DispatchQueue?)](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/1386204-setdelegate)

|  | Declaration |
| --- | --- |
| From | ``` func setDelegate(_ delegate: AVPlayerItemLegibleOutputPushDelegate?, queue delegateQueue: dispatch_queue_t?) ``` |
| To | ``` func setDelegate(_ delegate: AVPlayerItemLegibleOutputPushDelegate?, queue delegateQueue: DispatchQueue?) ``` |

Modified [AVPlayerItemLegibleOutputPushDelegate](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutputpushdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVPlayerItemLegibleOutputPushDelegate : AVPlayerItemOutputPushDelegate {     optional func legibleOutput(_ output: AVPlayerItemLegibleOutput, didOutputAttributedStrings strings: [NSAttributedString], nativeSampleBuffers nativeSamples: [AnyObject], forItemTime itemTime: CMTime) } ``` |
| To | ``` protocol AVPlayerItemLegibleOutputPushDelegate : AVPlayerItemOutputPushDelegate {     optional func legibleOutput(_ output: AVPlayerItemLegibleOutput, didOutputAttributedStrings strings: [NSAttributedString], nativeSampleBuffers nativeSamples: [Any], forItemTime itemTime: CMTime) } ``` |

Modified [AVPlayerItemLegibleOutputPushDelegate.legibleOutput(_: AVPlayerItemLegibleOutput, didOutputAttributedStrings: [NSAttributedString], nativeSampleBuffers: [Any], forItemTime: CMTime)](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutputpushdelegate/1386790-legibleoutput)

|  | Declaration |
| --- | --- |
| From | ``` optional func legibleOutput(_ output: AVPlayerItemLegibleOutput, didOutputAttributedStrings strings: [NSAttributedString], nativeSampleBuffers nativeSamples: [AnyObject], forItemTime itemTime: CMTime) ``` |
| To | ``` optional func legibleOutput(_ output: AVPlayerItemLegibleOutput, didOutputAttributedStrings strings: [NSAttributedString], nativeSampleBuffers nativeSamples: [Any], forItemTime itemTime: CMTime) ``` |

Modified [AVPlayerItemMediaDataCollector](https://developer.apple.com/documentation/avfoundation/avplayeritemmediadatacollector)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVPlayerItemMediaDataCollector : NSObject { } ``` | -- |
| To | ``` class AVPlayerItemMediaDataCollector : NSObject {     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVPlayerItemMediaDataCollector : CVarArg { } extension AVPlayerItemMediaDataCollector : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVPlayerItemMetadataCollector](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollector)

|  | Declaration |
| --- | --- |
| From | ``` class AVPlayerItemMetadataCollector : AVPlayerItemMediaDataCollector {     init(identifiers identifiers: [String]?, classifyingLabels classifyingLabels: [String]?)     func setDelegate(_ delegate: AVPlayerItemMetadataCollectorPushDelegate?, queue delegateQueue: dispatch_queue_t?)     weak var delegate: AVPlayerItemMetadataCollectorPushDelegate? { get }     var delegateQueue: dispatch_queue_t? { get } } ``` |
| To | ``` class AVPlayerItemMetadataCollector : AVPlayerItemMediaDataCollector {     init(identifiers identifiers: [String]?, classifyingLabels classifyingLabels: [String]?)     func setDelegate(_ delegate: AVPlayerItemMetadataCollectorPushDelegate?, queue delegateQueue: DispatchQueue?)     weak var delegate: AVPlayerItemMetadataCollectorPushDelegate? { get }     var delegateQueue: DispatchQueue? { get } } ``` |

Modified [AVPlayerItemMetadataCollector.delegateQueue](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollector/1617192-delegatequeue)

|  | Declaration |
| --- | --- |
| From | ``` var delegateQueue: dispatch_queue_t? { get } ``` |
| To | ``` var delegateQueue: DispatchQueue? { get } ``` |

Modified [AVPlayerItemMetadataCollector.setDelegate(_: AVPlayerItemMetadataCollectorPushDelegate?, queue: DispatchQueue?)](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollector/1617195-setdelegate)

|  | Declaration |
| --- | --- |
| From | ``` func setDelegate(_ delegate: AVPlayerItemMetadataCollectorPushDelegate?, queue delegateQueue: dispatch_queue_t?) ``` |
| To | ``` func setDelegate(_ delegate: AVPlayerItemMetadataCollectorPushDelegate?, queue delegateQueue: DispatchQueue?) ``` |

Modified [AVPlayerItemMetadataCollectorPushDelegate](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollectorpushdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVPlayerItemMetadataCollectorPushDelegate : NSObjectProtocol {     func metadataCollector(_ metadataCollector: AVPlayerItemMetadataCollector, didCollectDateRangeMetadataGroups metadataGroups: [AVDateRangeMetadataGroup], indexesOfNewGroups indexesOfNewGroups: NSIndexSet, indexesOfModifiedGroups indexesOfModifiedGroups: NSIndexSet) } ``` |
| To | ``` protocol AVPlayerItemMetadataCollectorPushDelegate : NSObjectProtocol {     func metadataCollector(_ metadataCollector: AVPlayerItemMetadataCollector, didCollect metadataGroups: [AVDateRangeMetadataGroup], indexesOfNewGroups indexesOfNewGroups: IndexSet, indexesOfModifiedGroups indexesOfModifiedGroups: IndexSet) } ``` |

Modified [AVPlayerItemMetadataCollectorPushDelegate.metadataCollector(_: AVPlayerItemMetadataCollector, didCollect: [AVDateRangeMetadataGroup], indexesOfNewGroups: IndexSet, indexesOfModifiedGroups: IndexSet)](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollectorpushdelegate/1617190-metadatacollector)

|  | Declaration |
| --- | --- |
| From | ``` func metadataCollector(_ metadataCollector: AVPlayerItemMetadataCollector, didCollectDateRangeMetadataGroups metadataGroups: [AVDateRangeMetadataGroup], indexesOfNewGroups indexesOfNewGroups: NSIndexSet, indexesOfModifiedGroups indexesOfModifiedGroups: NSIndexSet) ``` |
| To | ``` func metadataCollector(_ metadataCollector: AVPlayerItemMetadataCollector, didCollect metadataGroups: [AVDateRangeMetadataGroup], indexesOfNewGroups indexesOfNewGroups: IndexSet, indexesOfModifiedGroups indexesOfModifiedGroups: IndexSet) ``` |

Modified [AVPlayerItemMetadataOutput](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput)

|  | Declaration |
| --- | --- |
| From | ``` class AVPlayerItemMetadataOutput : AVPlayerItemOutput {     init(identifiers identifiers: [String]?)     func setDelegate(_ delegate: AVPlayerItemMetadataOutputPushDelegate?, queue delegateQueue: dispatch_queue_t?)     weak var delegate: AVPlayerItemMetadataOutputPushDelegate? { get }     var delegateQueue: dispatch_queue_t? { get }     var advanceIntervalForDelegateInvocation: NSTimeInterval } ``` |
| To | ``` class AVPlayerItemMetadataOutput : AVPlayerItemOutput {     init(identifiers identifiers: [String]?)     func setDelegate(_ delegate: AVPlayerItemMetadataOutputPushDelegate?, queue delegateQueue: DispatchQueue?)     weak var delegate: AVPlayerItemMetadataOutputPushDelegate? { get }     var delegateQueue: DispatchQueue? { get }     var advanceIntervalForDelegateInvocation: TimeInterval } ``` |

Modified [AVPlayerItemMetadataOutput.advanceIntervalForDelegateInvocation](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput/1387372-advanceintervalfordelegateinvoca)

|  | Declaration |
| --- | --- |
| From | ``` var advanceIntervalForDelegateInvocation: NSTimeInterval ``` |
| To | ``` var advanceIntervalForDelegateInvocation: TimeInterval ``` |

Modified [AVPlayerItemMetadataOutput.delegateQueue](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput/1387265-delegatequeue)

|  | Declaration |
| --- | --- |
| From | ``` var delegateQueue: dispatch_queue_t? { get } ``` |
| To | ``` var delegateQueue: DispatchQueue? { get } ``` |

Modified [AVPlayerItemMetadataOutput.setDelegate(_: AVPlayerItemMetadataOutputPushDelegate?, queue: DispatchQueue?)](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput/1385728-setdelegate)

|  | Declaration |
| --- | --- |
| From | ``` func setDelegate(_ delegate: AVPlayerItemMetadataOutputPushDelegate?, queue delegateQueue: dispatch_queue_t?) ``` |
| To | ``` func setDelegate(_ delegate: AVPlayerItemMetadataOutputPushDelegate?, queue delegateQueue: DispatchQueue?) ``` |

Modified [AVPlayerItemMetadataOutputPushDelegate](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutputpushdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVPlayerItemMetadataOutputPushDelegate : AVPlayerItemOutputPushDelegate {     optional func metadataOutput(_ output: AVPlayerItemMetadataOutput, didOutputTimedMetadataGroups groups: [AVTimedMetadataGroup], fromPlayerItemTrack track: AVPlayerItemTrack) } ``` |
| To | ``` protocol AVPlayerItemMetadataOutputPushDelegate : AVPlayerItemOutputPushDelegate {     optional func metadataOutput(_ output: AVPlayerItemMetadataOutput, didOutputTimedMetadataGroups groups: [AVTimedMetadataGroup], from track: AVPlayerItemTrack) } ``` |

Modified [AVPlayerItemMetadataOutputPushDelegate.metadataOutput(_: AVPlayerItemMetadataOutput, didOutputTimedMetadataGroups: [AVTimedMetadataGroup], from: AVPlayerItemTrack)](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutputpushdelegate/1388071-metadataoutput)

|  | Declaration |
| --- | --- |
| From | ``` optional func metadataOutput(_ output: AVPlayerItemMetadataOutput, didOutputTimedMetadataGroups groups: [AVTimedMetadataGroup], fromPlayerItemTrack track: AVPlayerItemTrack) ``` |
| To | ``` optional func metadataOutput(_ output: AVPlayerItemMetadataOutput, didOutputTimedMetadataGroups groups: [AVTimedMetadataGroup], from track: AVPlayerItemTrack) ``` |

Modified [AVPlayerItemOutput](https://developer.apple.com/documentation/avfoundation/avplayeritemoutput)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVPlayerItemOutput : NSObject {     func itemTimeForHostTime(_ hostTimeInSeconds: CFTimeInterval) -> CMTime     func itemTimeForMachAbsoluteTime(_ machAbsoluteTime: Int64) -> CMTime     var suppressesPlayerRendering: Bool } ``` | -- |
| To | ``` class AVPlayerItemOutput : NSObject {     func itemTime(forHostTime hostTimeInSeconds: CFTimeInterval) -> CMTime     func itemTime(forMachAbsoluteTime machAbsoluteTime: Int64) -> CMTime     var suppressesPlayerRendering: Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVPlayerItemOutput : CVarArg { } extension AVPlayerItemOutput : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVPlayerItemOutput.itemTime(forHostTime: CFTimeInterval) -> CMTime](https://developer.apple.com/documentation/avfoundation/avplayeritemoutput/1386538-itemtimeforhosttime)

|  | Declaration |
| --- | --- |
| From | ``` func itemTimeForHostTime(_ hostTimeInSeconds: CFTimeInterval) -> CMTime ``` |
| To | ``` func itemTime(forHostTime hostTimeInSeconds: CFTimeInterval) -> CMTime ``` |

Modified [AVPlayerItemOutput.itemTime(forMachAbsoluteTime: Int64) -> CMTime](https://developer.apple.com/documentation/avfoundation/avplayeritemoutput/1386962-itemtimeformachabsolutetime)

|  | Declaration |
| --- | --- |
| From | ``` func itemTimeForMachAbsoluteTime(_ machAbsoluteTime: Int64) -> CMTime ``` |
| To | ``` func itemTime(forMachAbsoluteTime machAbsoluteTime: Int64) -> CMTime ``` |

Modified [AVPlayerItemStatus [enum]](https://developer.apple.com/documentation/avfoundation/avplayeritem/status)

|  | Declaration |
| --- | --- |
| From | ``` enum AVPlayerItemStatus : Int {     case Unknown     case ReadyToPlay     case Failed } ``` |
| To | ``` enum AVPlayerItemStatus : Int {     case unknown     case readyToPlay     case failed } ``` |

Modified [AVPlayerItemStatus.failed](https://developer.apple.com/documentation/avfoundation/avplayeritemstatus/avplayeritemstatusfailed)

|  | Declaration |
| --- | --- |
| From | ``` case Failed ``` |
| To | ``` case failed ``` |

Modified [AVPlayerItemStatus.readyToPlay](https://developer.apple.com/documentation/avfoundation/avplayeritem/status/readytoplay)

|  | Declaration |
| --- | --- |
| From | ``` case ReadyToPlay ``` |
| To | ``` case readyToPlay ``` |

Modified [AVPlayerItemStatus.unknown](https://developer.apple.com/documentation/avfoundation/avplayeritem/status/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [AVPlayerItemTrack](https://developer.apple.com/documentation/avfoundation/avplayeritemtrack)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVPlayerItemTrack : NSObject {     var assetTrack: AVAssetTrack { get }     var enabled: Bool     var currentVideoFrameRate: Float { get } } ``` | -- |
| To | ``` class AVPlayerItemTrack : NSObject {     var assetTrack: AVAssetTrack { get }     var isEnabled: Bool     var currentVideoFrameRate: Float { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVPlayerItemTrack : CVarArg { } extension AVPlayerItemTrack : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVPlayerItemTrack.isEnabled](https://developer.apple.com/documentation/avfoundation/avplayeritemtrack/1387062-enabled)

|  | Declaration |
| --- | --- |
| From | ``` var enabled: Bool ``` |
| To | ``` var isEnabled: Bool ``` |

Modified [AVPlayerItemVideoOutput](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput)

|  | Declaration |
| --- | --- |
| From | ``` class AVPlayerItemVideoOutput : AVPlayerItemOutput {     init(pixelBufferAttributes pixelBufferAttributes: [String : AnyObject]?)     func hasNewPixelBufferForItemTime(_ itemTime: CMTime) -> Bool     func copyPixelBufferForItemTime(_ itemTime: CMTime, itemTimeForDisplay outItemTimeForDisplay: UnsafeMutablePointer<CMTime>) -> CVPixelBuffer?     func setDelegate(_ delegate: AVPlayerItemOutputPullDelegate?, queue delegateQueue: dispatch_queue_t?)     func requestNotificationOfMediaDataChangeWithAdvanceInterval(_ interval: NSTimeInterval)     unowned(unsafe) var delegate: AVPlayerItemOutputPullDelegate? { get }     var delegateQueue: dispatch_queue_t? { get } } ``` |
| To | ``` class AVPlayerItemVideoOutput : AVPlayerItemOutput {     init(pixelBufferAttributes pixelBufferAttributes: [String : Any]? = nil)     init(outputSettings outputSettings: [String : Any]?)     func hasNewPixelBuffer(forItemTime itemTime: CMTime) -> Bool     func copyPixelBuffer(forItemTime itemTime: CMTime, itemTimeForDisplay outItemTimeForDisplay: UnsafeMutablePointer<CMTime>?) -> CVPixelBuffer?     func setDelegate(_ delegate: AVPlayerItemOutputPullDelegate?, queue delegateQueue: DispatchQueue?)     func requestNotificationOfMediaDataChange(withAdvanceInterval interval: TimeInterval)     unowned(unsafe) var delegate: AVPlayerItemOutputPullDelegate? { get }     var delegateQueue: DispatchQueue? { get } } ``` |

Modified [AVPlayerItemVideoOutput.copyPixelBuffer(forItemTime: CMTime, itemTimeForDisplay: UnsafeMutablePointer<CMTime>?) -> CVPixelBuffer?](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1386148-copypixelbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func copyPixelBufferForItemTime(_ itemTime: CMTime, itemTimeForDisplay outItemTimeForDisplay: UnsafeMutablePointer<CMTime>) -> CVPixelBuffer? ``` |
| To | ``` func copyPixelBuffer(forItemTime itemTime: CMTime, itemTimeForDisplay outItemTimeForDisplay: UnsafeMutablePointer<CMTime>?) -> CVPixelBuffer? ``` |

Modified [AVPlayerItemVideoOutput.delegateQueue](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1388108-delegatequeue)

|  | Declaration |
| --- | --- |
| From | ``` var delegateQueue: dispatch_queue_t? { get } ``` |
| To | ``` var delegateQueue: DispatchQueue? { get } ``` |

Modified [AVPlayerItemVideoOutput.hasNewPixelBuffer(forItemTime: CMTime) -> Bool](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1386444-hasnewpixelbufferforitemtime)

|  | Declaration |
| --- | --- |
| From | ``` func hasNewPixelBufferForItemTime(_ itemTime: CMTime) -> Bool ``` |
| To | ``` func hasNewPixelBuffer(forItemTime itemTime: CMTime) -> Bool ``` |

Modified [AVPlayerItemVideoOutput.init(pixelBufferAttributes: [String : Any]?)](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1389231-initwithpixelbufferattributes)

|  | Declaration |
| --- | --- |
| From | ``` init(pixelBufferAttributes pixelBufferAttributes: [String : AnyObject]?) ``` |
| To | ``` init(pixelBufferAttributes pixelBufferAttributes: [String : Any]? = nil) ``` |

Modified [AVPlayerItemVideoOutput.requestNotificationOfMediaDataChange(withAdvanceInterval: TimeInterval)](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1386046-requestnotificationofmediadatach)

|  | Declaration |
| --- | --- |
| From | ``` func requestNotificationOfMediaDataChangeWithAdvanceInterval(_ interval: NSTimeInterval) ``` |
| To | ``` func requestNotificationOfMediaDataChange(withAdvanceInterval interval: TimeInterval) ``` |

Modified [AVPlayerItemVideoOutput.setDelegate(_: AVPlayerItemOutputPullDelegate?, queue: DispatchQueue?)](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1386824-setdelegate)

|  | Declaration |
| --- | --- |
| From | ``` func setDelegate(_ delegate: AVPlayerItemOutputPullDelegate?, queue delegateQueue: dispatch_queue_t?) ``` |
| To | ``` func setDelegate(_ delegate: AVPlayerItemOutputPullDelegate?, queue delegateQueue: DispatchQueue?) ``` |

Modified [AVPlayerLayer](https://developer.apple.com/documentation/avfoundation/avplayerlayer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVPlayerLayer : CALayer {      init(player player: AVPlayer?)     class func playerLayerWithPlayer(_ player: AVPlayer?) -> AVPlayerLayer     var player: AVPlayer?     var videoGravity: String     var readyForDisplay: Bool { get }     var videoRect: CGRect { get }     var pixelBufferAttributes: [String : AnyObject]? } ``` | -- |
| To | ``` class AVPlayerLayer : CALayer {      init(player player: AVPlayer?)     class func withPlayer(_ player: AVPlayer?) -> AVPlayerLayer     var player: AVPlayer?     var videoGravity: String     var isReadyForDisplay: Bool { get }     var videoRect: CGRect { get }     var pixelBufferAttributes: [String : Any]?     func scroll(_ p: CGPoint)     func scrollRectToVisible(_ r: CGRect)     var visibleRect: CGRect { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVPlayerLayer : CVarArg { } extension AVPlayerLayer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVPlayerLayer.isReadyForDisplay](https://developer.apple.com/documentation/avfoundation/avplayerlayer/1389748-readyfordisplay)

|  | Declaration |
| --- | --- |
| From | ``` var readyForDisplay: Bool { get } ``` |
| To | ``` var isReadyForDisplay: Bool { get } ``` |

Modified [AVPlayerLayer.pixelBufferAttributes](https://developer.apple.com/documentation/avfoundation/avplayerlayer/1390055-pixelbufferattributes)

|  | Declaration |
| --- | --- |
| From | ``` var pixelBufferAttributes: [String : AnyObject]? ``` |
| To | ``` var pixelBufferAttributes: [String : Any]? ``` |

Modified [AVPlayerMediaSelectionCriteria](https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVPlayerMediaSelectionCriteria : NSObject {     var preferredLanguages: [String]? { get }     var preferredMediaCharacteristics: [String]? { get }     init(preferredLanguages preferredLanguages: [String]?, preferredMediaCharacteristics preferredMediaCharacteristics: [String]?) } ``` | -- |
| To | ``` class AVPlayerMediaSelectionCriteria : NSObject {     var preferredLanguages: [String]? { get }     var preferredMediaCharacteristics: [String]? { get }     init(preferredLanguages preferredLanguages: [String]?, preferredMediaCharacteristics preferredMediaCharacteristics: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVPlayerMediaSelectionCriteria : CVarArg { } extension AVPlayerMediaSelectionCriteria : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVPlayerStatus [enum]](https://developer.apple.com/documentation/avfoundation/avplayer/status)

|  | Declaration |
| --- | --- |
| From | ``` enum AVPlayerStatus : Int {     case Unknown     case ReadyToPlay     case Failed } ``` |
| To | ``` enum AVPlayerStatus : Int {     case unknown     case readyToPlay     case failed } ``` |

Modified [AVPlayerStatus.failed](https://developer.apple.com/documentation/avfoundation/avplayerstatus/avplayerstatusfailed)

|  | Declaration |
| --- | --- |
| From | ``` case Failed ``` |
| To | ``` case failed ``` |

Modified [AVPlayerStatus.readyToPlay](https://developer.apple.com/documentation/avfoundation/avplayerstatus/avplayerstatusreadytoplay)

|  | Declaration |
| --- | --- |
| From | ``` case ReadyToPlay ``` |
| To | ``` case readyToPlay ``` |

Modified [AVPlayerStatus.unknown](https://developer.apple.com/documentation/avfoundation/avplayerstatus/avplayerstatusunknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [AVQueuePlayer](https://developer.apple.com/documentation/avfoundation/avqueueplayer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVQueuePlayer : AVPlayer {     convenience init(items items: [AVPlayerItem])     class func queuePlayerWithItems(_ items: [AVPlayerItem]) -> Self     init(items items: [AVPlayerItem])     func items() -> [AVPlayerItem]     func advanceToNextItem()     func canInsertItem(_ item: AVPlayerItem, afterItem afterItem: AVPlayerItem?) -> Bool     func insertItem(_ item: AVPlayerItem, afterItem afterItem: AVPlayerItem?)     func removeItem(_ item: AVPlayerItem)     func removeAllItems() } ``` | -- |
| To | ``` class AVQueuePlayer : AVPlayer {     convenience init(items items: [AVPlayerItem])     class func withItems(_ items: [AVPlayerItem]) -> Self     init(items items: [AVPlayerItem])     func items() -> [AVPlayerItem]     func advanceToNextItem()     func canInsert(_ item: AVPlayerItem, after afterItem: AVPlayerItem?) -> Bool     func insert(_ item: AVPlayerItem, after afterItem: AVPlayerItem?)     func remove(_ item: AVPlayerItem)     func removeAllItems()     var isOutputObscuredDueToInsufficientExternalProtection: Bool { get }     var allowsAirPlayVideo: Bool     var isAirPlayVideoActive: Bool { get }     var usesAirPlayVideoWhileAirPlayScreenIsActive: Bool     var allowsExternalPlayback: Bool     var isExternalPlaybackActive: Bool { get }     var usesExternalPlaybackWhileExternalScreenIsActive: Bool     var externalPlaybackVideoGravity: String     var audioOutputDeviceUniqueID: String?     var appliesMediaSelectionCriteriaAutomatically: Bool     func setMediaSelectionCriteria(_ criteria: AVPlayerMediaSelectionCriteria?, forMediaCharacteristic mediaCharacteristic: String)     func mediaSelectionCriteria(forMediaCharacteristic mediaCharacteristic: String) -> AVPlayerMediaSelectionCriteria?     var volume: Float     var isMuted: Bool     var isClosedCaptionDisplayEnabled: Bool     func addPeriodicTimeObserver(forInterval interval: CMTime, queue queue: DispatchQueue?, using block: @escaping (CMTime) -> Void) -> Any     func addBoundaryTimeObserver(forTimes times: [NSValue], queue queue: DispatchQueue?, using block: @escaping () -> Void) -> Any     func removeTimeObserver(_ observer: Any)     var automaticallyWaitsToMinimizeStalling: Bool     func setRate(_ rate: Float, time itemTime: CMTime, atHostTime hostClockTime: CMTime)     func preroll(atRate rate: Float, completionHandler completionHandler: (@escaping (Bool) -> Void)? = nil)     func cancelPendingPrerolls()     var masterClock: CMClock?     func currentTime() -> CMTime     func seek(to date: Date)     func seek(to date: Date, completionHandler completionHandler: @escaping (Bool) -> Void)     func seek(to time: CMTime)     func seek(to time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime)     func seek(to time: CMTime, completionHandler completionHandler: @escaping (Bool) -> Void)     func seek(to time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime, completionHandler completionHandler: @escaping (Bool) -> Void)     var currentItem: AVPlayerItem? { get }     func replaceCurrentItem(with item: AVPlayerItem?)     var actionAtItemEnd: AVPlayerActionAtItemEnd     var rate: Float     func play()     func pause()     var timeControlStatus: AVPlayerTimeControlStatus { get }     var reasonForWaitingToPlay: String? { get }     func playImmediately(atRate rate: Float)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVQueuePlayer : CVarArg { } extension AVQueuePlayer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVQueuePlayer.canInsert(_: AVPlayerItem, after: AVPlayerItem?) -> Bool](https://developer.apple.com/documentation/avfoundation/avqueueplayer/1387289-caninsert)

|  | Declaration |
| --- | --- |
| From | ``` func canInsertItem(_ item: AVPlayerItem, afterItem afterItem: AVPlayerItem?) -> Bool ``` |
| To | ``` func canInsert(_ item: AVPlayerItem, after afterItem: AVPlayerItem?) -> Bool ``` |

Modified [AVQueuePlayer.insert(_: AVPlayerItem, after: AVPlayerItem?)](https://developer.apple.com/documentation/avfoundation/avqueueplayer/1388543-insert)

|  | Declaration |
| --- | --- |
| From | ``` func insertItem(_ item: AVPlayerItem, afterItem afterItem: AVPlayerItem?) ``` |
| To | ``` func insert(_ item: AVPlayerItem, after afterItem: AVPlayerItem?) ``` |

Modified [AVQueuePlayer.remove(_: AVPlayerItem)](https://developer.apple.com/documentation/avfoundation/avqueueplayer/1387400-remove)

|  | Declaration |
| --- | --- |
| From | ``` func removeItem(_ item: AVPlayerItem) ``` |
| To | ``` func remove(_ item: AVPlayerItem) ``` |

Modified [AVSampleBufferDisplayLayer.enqueue(_: CMSampleBuffer)](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/1387599-enqueue)

|  | Declaration |
| --- | --- |
| From | ``` func enqueueSampleBuffer(_ sampleBuffer: CMSampleBuffer) ``` |
| To | ``` func enqueue(_ sampleBuffer: CMSampleBuffer) ``` |

Modified [AVSampleBufferDisplayLayer.isReadyForMoreMediaData](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/1387317-isreadyformoremediadata)

|  | Declaration |
| --- | --- |
| From | ``` var readyForMoreMediaData: Bool { get } ``` |
| To | ``` var isReadyForMoreMediaData: Bool { get } ``` |

Modified [AVSampleBufferDisplayLayer.requestMediaDataWhenReady(on: DispatchQueue, using: () -> Swift.Void)](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/1387778-requestmediadatawhenready)

|  | Declaration |
| --- | --- |
| From | ``` func requestMediaDataWhenReadyOnQueue(_ queue: dispatch_queue_t, usingBlock block: () -> Void) ``` |
| To | ``` func requestMediaDataWhenReady(on queue: DispatchQueue, using block: @escaping () -> Swift.Void) ``` |

Modified [AVSpeechBoundary [enum]](https://developer.apple.com/documentation/avfoundation/avspeechboundary)

|  | Declaration |
| --- | --- |
| From | ``` enum AVSpeechBoundary : Int {     case Immediate     case Word } ``` |
| To | ``` enum AVSpeechBoundary : Int {     case immediate     case word } ``` |

Modified [AVSpeechBoundary.immediate](https://developer.apple.com/documentation/avfoundation/avspeechboundary/immediate)

|  | Declaration |
| --- | --- |
| From | ``` case Immediate ``` |
| To | ``` case immediate ``` |

Modified [AVSpeechBoundary.word](https://developer.apple.com/documentation/avfoundation/avspeechboundary/avspeechboundaryword)

|  | Declaration |
| --- | --- |
| From | ``` case Word ``` |
| To | ``` case word ``` |

Modified [AVSpeechSynthesisVoice](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVSpeechSynthesisVoice : NSObject, NSSecureCoding {     class func speechVoices() -> [AVSpeechSynthesisVoice]     class func currentLanguageCode() -> String      init?(language languageCode: String?)     class func voiceWithLanguage(_ languageCode: String?) -> AVSpeechSynthesisVoice?      init?(identifier identifier: String)     class func voiceWithIdentifier(_ identifier: String) -> AVSpeechSynthesisVoice?     var language: String { get }     var identifier: String { get }     var name: String { get }     var quality: AVSpeechSynthesisVoiceQuality { get } } ``` | NSSecureCoding |
| To | ``` class AVSpeechSynthesisVoice : NSObject, NSSecureCoding {     class func speechVoices() -> [AVSpeechSynthesisVoice]     class func currentLanguageCode() -> String      init?(language languageCode: String?)     class func withLanguage(_ languageCode: String?) -> AVSpeechSynthesisVoice?      init?(identifier identifier: String)     class func withIdentifier(_ identifier: String) -> AVSpeechSynthesisVoice?     var language: String { get }     var identifier: String { get }     var name: String { get }     var quality: AVSpeechSynthesisVoiceQuality { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVSpeechSynthesisVoice : CVarArg { } extension AVSpeechSynthesisVoice : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSSecureCoding |

Modified [AVSpeechSynthesisVoiceQuality [enum]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoicequality)

|  | Declaration |
| --- | --- |
| From | ``` enum AVSpeechSynthesisVoiceQuality : Int {     case Default     case Enhanced } ``` |
| To | ``` enum AVSpeechSynthesisVoiceQuality : Int {     case `default`     case enhanced } ``` |

Modified [AVSpeechSynthesisVoiceQuality.default](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoicequality/default)

|  | Declaration |
| --- | --- |
| From | ``` case Default ``` |
| To | ``` case `default` ``` |

Modified [AVSpeechSynthesisVoiceQuality.enhanced](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoicequality/avspeechsynthesisvoicequalityenhanced)

|  | Declaration |
| --- | --- |
| From | ``` case Enhanced ``` |
| To | ``` case enhanced ``` |

Modified [AVSpeechSynthesizer](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVSpeechSynthesizer : NSObject {     unowned(unsafe) var delegate: AVSpeechSynthesizerDelegate?     var speaking: Bool { get }     var paused: Bool { get }     func speakUtterance(_ utterance: AVSpeechUtterance)     func stopSpeakingAtBoundary(_ boundary: AVSpeechBoundary) -> Bool     func pauseSpeakingAtBoundary(_ boundary: AVSpeechBoundary) -> Bool     func continueSpeaking() -> Bool } ``` | -- |
| To | ``` class AVSpeechSynthesizer : NSObject {     unowned(unsafe) var delegate: AVSpeechSynthesizerDelegate?     var isSpeaking: Bool { get }     var isPaused: Bool { get }     func speak(_ utterance: AVSpeechUtterance)     func stopSpeaking(at boundary: AVSpeechBoundary) -> Bool     func pauseSpeaking(at boundary: AVSpeechBoundary) -> Bool     func continueSpeaking() -> Bool     var outputChannels: [AVAudioSessionChannelDescription]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVSpeechSynthesizer : CVarArg { } extension AVSpeechSynthesizer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVSpeechSynthesizer.isPaused](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619692-paused)

|  | Declaration |
| --- | --- |
| From | ``` var paused: Bool { get } ``` |
| To | ``` var isPaused: Bool { get } ``` |

Modified [AVSpeechSynthesizer.isSpeaking](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619680-isspeaking)

|  | Declaration |
| --- | --- |
| From | ``` var speaking: Bool { get } ``` |
| To | ``` var isSpeaking: Bool { get } ``` |

Modified [AVSpeechSynthesizer.pauseSpeaking(at: AVSpeechBoundary) -> Bool](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619689-pausespeakingatboundary)

|  | Declaration |
| --- | --- |
| From | ``` func pauseSpeakingAtBoundary(_ boundary: AVSpeechBoundary) -> Bool ``` |
| To | ``` func pauseSpeaking(at boundary: AVSpeechBoundary) -> Bool ``` |

Modified [AVSpeechSynthesizer.speak(_: AVSpeechUtterance)](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619686-speak)

|  | Declaration |
| --- | --- |
| From | ``` func speakUtterance(_ utterance: AVSpeechUtterance) ``` |
| To | ``` func speak(_ utterance: AVSpeechUtterance) ``` |

Modified [AVSpeechSynthesizer.stopSpeaking(at: AVSpeechBoundary) -> Bool](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619676-stopspeakingatboundary)

|  | Declaration |
| --- | --- |
| From | ``` func stopSpeakingAtBoundary(_ boundary: AVSpeechBoundary) -> Bool ``` |
| To | ``` func stopSpeaking(at boundary: AVSpeechBoundary) -> Bool ``` |

Modified [AVSpeechSynthesizerDelegate](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVSpeechSynthesizerDelegate : NSObjectProtocol {     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didStartSpeechUtterance utterance: AVSpeechUtterance)     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didFinishSpeechUtterance utterance: AVSpeechUtterance)     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didPauseSpeechUtterance utterance: AVSpeechUtterance)     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didContinueSpeechUtterance utterance: AVSpeechUtterance)     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didCancelSpeechUtterance utterance: AVSpeechUtterance)     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, willSpeakRangeOfSpeechString characterRange: NSRange, utterance utterance: AVSpeechUtterance) } ``` |
| To | ``` protocol AVSpeechSynthesizerDelegate : NSObjectProtocol {     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didStart utterance: AVSpeechUtterance)     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didFinish utterance: AVSpeechUtterance)     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didPause utterance: AVSpeechUtterance)     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didContinue utterance: AVSpeechUtterance)     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didCancel utterance: AVSpeechUtterance)     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, willSpeakRangeOfSpeechString characterRange: NSRange, utterance utterance: AVSpeechUtterance) } ``` |

Modified [AVSpeechSynthesizerDelegate.speechSynthesizer(_: AVSpeechSynthesizer, didCancel: AVSpeechUtterance)](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619678-speechsynthesizer)

|  | Declaration |
| --- | --- |
| From | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didCancelSpeechUtterance utterance: AVSpeechUtterance) ``` |
| To | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didCancel utterance: AVSpeechUtterance) ``` |

Modified [AVSpeechSynthesizerDelegate.speechSynthesizer(_: AVSpeechSynthesizer, didContinue: AVSpeechUtterance)](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619677-speechsynthesizer)

|  | Declaration |
| --- | --- |
| From | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didContinueSpeechUtterance utterance: AVSpeechUtterance) ``` |
| To | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didContinue utterance: AVSpeechUtterance) ``` |

Modified [AVSpeechSynthesizerDelegate.speechSynthesizer(_: AVSpeechSynthesizer, didFinish: AVSpeechUtterance)](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619700-speechsynthesizer)

|  | Declaration |
| --- | --- |
| From | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didFinishSpeechUtterance utterance: AVSpeechUtterance) ``` |
| To | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didFinish utterance: AVSpeechUtterance) ``` |

Modified [AVSpeechSynthesizerDelegate.speechSynthesizer(_: AVSpeechSynthesizer, didPause: AVSpeechUtterance)](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619675-speechsynthesizer)

|  | Declaration |
| --- | --- |
| From | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didPauseSpeechUtterance utterance: AVSpeechUtterance) ``` |
| To | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didPause utterance: AVSpeechUtterance) ``` |

Modified [AVSpeechSynthesizerDelegate.speechSynthesizer(_: AVSpeechSynthesizer, didStart: AVSpeechUtterance)](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619701-speechsynthesizer)

|  | Declaration |
| --- | --- |
| From | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didStartSpeechUtterance utterance: AVSpeechUtterance) ``` |
| To | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didStart utterance: AVSpeechUtterance) ``` |

Modified [AVSpeechUtterance](https://developer.apple.com/documentation/avfoundation/avspeechutterance)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVSpeechUtterance : NSObject, NSCopying, NSSecureCoding {     convenience init(string string: String)     class func speechUtteranceWithString(_ string: String) -> Self     init(string string: String)     var voice: AVSpeechSynthesisVoice?     var speechString: String { get }     var rate: Float     var pitchMultiplier: Float     var volume: Float     var preUtteranceDelay: NSTimeInterval     var postUtteranceDelay: NSTimeInterval } ``` | NSCopying, NSSecureCoding |
| To | ``` class AVSpeechUtterance : NSObject, NSCopying, NSSecureCoding {     convenience init(string string: String)     class func withString(_ string: String) -> Self     convenience init(attributedString string: NSAttributedString)     class func withAttributedString(_ string: NSAttributedString) -> Self     init(string string: String)     init(attributedString string: NSAttributedString)     var voice: AVSpeechSynthesisVoice?     var speechString: String { get }     var attributedSpeechString: NSAttributedString { get }     var rate: Float     var pitchMultiplier: Float     var volume: Float     var preUtteranceDelay: TimeInterval     var postUtteranceDelay: TimeInterval     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVSpeechUtterance : CVarArg { } extension AVSpeechUtterance : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [AVSpeechUtterance.postUtteranceDelay](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619694-postutterancedelay)

|  | Declaration |
| --- | --- |
| From | ``` var postUtteranceDelay: NSTimeInterval ``` |
| To | ``` var postUtteranceDelay: TimeInterval ``` |

Modified [AVSpeechUtterance.preUtteranceDelay](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619679-preutterancedelay)

|  | Declaration |
| --- | --- |
| From | ``` var preUtteranceDelay: NSTimeInterval ``` |
| To | ``` var preUtteranceDelay: TimeInterval ``` |

Modified [AVSynchronizedLayer](https://developer.apple.com/documentation/avfoundation/avsynchronizedlayer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVSynchronizedLayer : CALayer {      init(playerItem playerItem: AVPlayerItem)     class func synchronizedLayerWithPlayerItem(_ playerItem: AVPlayerItem) -> AVSynchronizedLayer     var playerItem: AVPlayerItem? } ``` | -- |
| To | ``` class AVSynchronizedLayer : CALayer {      init(playerItem playerItem: AVPlayerItem)     class func withPlayerItem(_ playerItem: AVPlayerItem) -> AVSynchronizedLayer     var playerItem: AVPlayerItem?     func scroll(_ p: CGPoint)     func scrollRectToVisible(_ r: CGRect)     var visibleRect: CGRect { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVSynchronizedLayer : CVarArg { } extension AVSynchronizedLayer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVTextStyleRule](https://developer.apple.com/documentation/avfoundation/avtextstylerule)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVTextStyleRule : NSObject, NSCopying {     convenience init()     class func propertyListForTextStyleRules(_ textStyleRules: [AVTextStyleRule]) -> AnyObject     class func textStyleRulesFromPropertyList(_ plist: AnyObject) -> [AVTextStyleRule]?      init?(textMarkupAttributes textMarkupAttributes: [String : AnyObject])     class func textStyleRuleWithTextMarkupAttributes(_ textMarkupAttributes: [String : AnyObject]) -> AVTextStyleRule?      init?(textMarkupAttributes textMarkupAttributes: [String : AnyObject], textSelector textSelector: String?)     class func textStyleRuleWithTextMarkupAttributes(_ textMarkupAttributes: [String : AnyObject], textSelector textSelector: String?) -> AVTextStyleRule?     convenience init?(textMarkupAttributes textMarkupAttributes: [String : AnyObject])     init?(textMarkupAttributes textMarkupAttributes: [String : AnyObject], textSelector textSelector: String?)     var textMarkupAttributes: [String : AnyObject] { get }     var textSelector: String? { get } } ``` | NSCopying |
| To | ``` class AVTextStyleRule : NSObject, NSCopying {     convenience init()     class func propertyList(for textStyleRules: [AVTextStyleRule]) -> Any     class func textStyleRules(fromPropertyList plist: Any) -> [AVTextStyleRule]?      init?(textMarkupAttributes textMarkupAttributes: [String : Any] = [:])     class func withTextMarkupAttributes(_ textMarkupAttributes: [String : Any] = [:]) -> AVTextStyleRule?      init?(textMarkupAttributes textMarkupAttributes: [String : Any] = [:], textSelector textSelector: String?)     class func withTextMarkupAttributes(_ textMarkupAttributes: [String : Any] = [:], textSelector textSelector: String?) -> AVTextStyleRule?     convenience init?(textMarkupAttributes textMarkupAttributes: [String : Any] = [:])     init?(textMarkupAttributes textMarkupAttributes: [String : Any] = [:], textSelector textSelector: String?)     var textMarkupAttributes: [String : Any] { get }     var textSelector: String? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVTextStyleRule : CVarArg { } extension AVTextStyleRule : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [AVTextStyleRule.init(textMarkupAttributes: [String : Any])](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1385849-initwithtextmarkupattributes)

|  | Declaration |
| --- | --- |
| From | ``` convenience init?(textMarkupAttributes textMarkupAttributes: [String : AnyObject]) ``` |
| To | ``` convenience init?(textMarkupAttributes textMarkupAttributes: [String : Any] = [:]) ``` |

Modified [AVTextStyleRule.init(textMarkupAttributes: [String : Any], textSelector: String?)](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1389854-init)

|  | Declaration |
| --- | --- |
| From | ``` init?(textMarkupAttributes textMarkupAttributes: [String : AnyObject], textSelector textSelector: String?) ``` |
| To | ``` init?(textMarkupAttributes textMarkupAttributes: [String : Any] = [:], textSelector textSelector: String?) ``` |

Modified [AVTextStyleRule.propertyList(for: [AVTextStyleRule]) -> Any [class]](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1387970-propertylistfortextstylerules)

|  | Declaration |
| --- | --- |
| From | ``` class func propertyListForTextStyleRules(_ textStyleRules: [AVTextStyleRule]) -> AnyObject ``` |
| To | ``` class func propertyList(for textStyleRules: [AVTextStyleRule]) -> Any ``` |

Modified [AVTextStyleRule.textMarkupAttributes](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1387945-textmarkupattributes)

|  | Declaration |
| --- | --- |
| From | ``` var textMarkupAttributes: [String : AnyObject] { get } ``` |
| To | ``` var textMarkupAttributes: [String : Any] { get } ``` |

Modified [AVTextStyleRule.textStyleRules(fromPropertyList: Any) -> [AVTextStyleRule]? [class]](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1387802-textstylerules)

|  | Declaration |
| --- | --- |
| From | ``` class func textStyleRulesFromPropertyList(_ plist: AnyObject) -> [AVTextStyleRule]? ``` |
| To | ``` class func textStyleRules(fromPropertyList plist: Any) -> [AVTextStyleRule]? ``` |

Modified [AVTimedMetadataGroup](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVTimedMetadataGroup : AVMetadataGroup, NSCopying, NSMutableCopying {     init(items items: [AVMetadataItem], timeRange timeRange: CMTimeRange)     init?(sampleBuffer sampleBuffer: CMSampleBuffer)     var timeRange: CMTimeRange { get }     var items: [AVMetadataItem] { get } } extension AVTimedMetadataGroup {     func copyFormatDescription() -> CMMetadataFormatDescription? } ``` | NSCopying, NSMutableCopying |
| To | ``` class AVTimedMetadataGroup : AVMetadataGroup, NSCopying, NSMutableCopying {     init(items items: [AVMetadataItem], timeRange timeRange: CMTimeRange)     init?(sampleBuffer sampleBuffer: CMSampleBuffer)     var timeRange: CMTimeRange { get }     var items: [AVMetadataItem] { get }     func copyFormatDescription() -> CMMetadataFormatDescription?     var classifyingLabel: String? { get }     var uniqueID: String? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVTimedMetadataGroup : CVarArg { } extension AVTimedMetadataGroup : Equatable, Hashable {     var hashValue: Int { get } } extension AVTimedMetadataGroup {     func copyFormatDescription() -> CMMetadataFormatDescription? } ``` | CVarArg, Equatable, Hashable, NSCopying, NSMutableCopying |

Modified [AVURLAsset](https://developer.apple.com/documentation/avfoundation/avurlasset)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVURLAsset : AVAsset {     convenience init()     class func audiovisualTypes() -> [String]     class func audiovisualMIMETypes() -> [String]     class func isPlayableExtendedMIMEType(_ extendedMIMEType: String) -> Bool     convenience init(URL URL: NSURL, options options: [String : AnyObject]?)     class func URLAssetWithURL(_ URL: NSURL, options options: [String : AnyObject]?) -> Self     init(URL URL: NSURL, options options: [String : AnyObject]?)     @NSCopying var URL: NSURL { get } } extension AVURLAsset {     var resourceLoader: AVAssetResourceLoader { get } } extension AVURLAsset {     func compatibleTrackForCompositionTrack(_ compositionTrack: AVCompositionTrack) -> AVAssetTrack? } ``` | -- |
| To | ``` class AVURLAsset : AVAsset {     convenience init()     class func audiovisualTypes() -> [String]     class func audiovisualMIMETypes() -> [String]     class func isPlayableExtendedMIMEType(_ extendedMIMEType: String) -> Bool     convenience init(url URL: URL, options options: [String : Any]? = nil)     class func withURL(_ URL: URL, options options: [String : Any]? = nil) -> Self     init(url URL: URL, options options: [String : Any]? = nil)     var url: URL { get }     func compatibleTrack(for compositionTrack: AVCompositionTrack) -> AVAssetTrack?     var assetCache: AVAssetCache? { get }     var resourceLoader: AVAssetResourceLoader { get }     func unusedTrackID() -> CMPersistentTrackID     var isPlayable: Bool { get }     var isExportable: Bool { get }     var isReadable: Bool { get }     var isComposable: Bool { get }     var isCompatibleWithSavedPhotosAlbum: Bool { get }     var isCompatibleWithAirPlayVideo: Bool { get }     var canContainFragments: Bool { get }     var containsFragments: Bool { get }     var hasProtectedContent: Bool { get }     var availableMediaCharacteristicsWithMediaSelectionOptions: [String] { get }     func mediaSelectionGroup(forMediaCharacteristic mediaCharacteristic: String) -> AVMediaSelectionGroup?     var preferredMediaSelection: AVMediaSelection { get }     var availableChapterLocales: [Locale] { get }     func chapterMetadataGroups(withTitleLocale locale: Locale, containingItemsWithCommonKeys commonKeys: [String]?) -> [AVTimedMetadataGroup]     func chapterMetadataGroups(bestMatchingPreferredLanguages preferredLanguages: [String]) -> [AVTimedMetadataGroup]     var creationDate: AVMetadataItem? { get }     var lyrics: String? { get }     var commonMetadata: [AVMetadataItem] { get }     var metadata: [AVMetadataItem] { get }     var availableMetadataFormats: [String] { get }     func metadata(forFormat format: String) -> [AVMetadataItem]     var tracks: [AVAssetTrack] { get }     func track(withTrackID trackID: CMPersistentTrackID) -> AVAssetTrack?     func tracks(withMediaType mediaType: String) -> [AVAssetTrack]     func tracks(withMediaCharacteristic mediaCharacteristic: String) -> [AVAssetTrack]     var trackGroups: [AVAssetTrackGroup] { get }     var referenceRestrictions: AVAssetReferenceRestrictions { get }     var providesPreciseDurationAndTiming: Bool { get }     func cancelLoading()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVURLAsset : CVarArg { } extension AVURLAsset : Equatable, Hashable {     var hashValue: Int { get } } extension AVURLAsset {     var resourceLoader: AVAssetResourceLoader { get } } extension AVURLAsset {     var assetCache: AVAssetCache? { get } } extension AVURLAsset {     func compatibleTrack(for compositionTrack: AVCompositionTrack) -> AVAssetTrack? } ``` | CVarArg, Equatable, Hashable |

Modified [AVURLAsset.compatibleTrack(for: AVCompositionTrack) -> AVAssetTrack?](https://developer.apple.com/documentation/avfoundation/avurlasset/1389650-compatibletrack)

|  | Declaration |
| --- | --- |
| From | ``` func compatibleTrackForCompositionTrack(_ compositionTrack: AVCompositionTrack) -> AVAssetTrack? ``` |
| To | ``` func compatibleTrack(for compositionTrack: AVCompositionTrack) -> AVAssetTrack? ``` |

Modified [AVURLAsset.init(url: URL, options: [String : Any]?)](https://developer.apple.com/documentation/avfoundation/avurlasset/1385698-init)

|  | Declaration |
| --- | --- |
| From | ``` init(URL URL: NSURL, options options: [String : AnyObject]?) ``` |
| To | ``` init(url URL: URL, options options: [String : Any]? = nil) ``` |

Modified [AVURLAsset.url](https://developer.apple.com/documentation/avfoundation/avurlasset/1388127-url)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var URL: NSURL { get } ``` |
| To | ``` var url: URL { get } ``` |

Modified [AVVideoCompositing](https://developer.apple.com/documentation/avfoundation/avvideocompositing)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVVideoCompositing : NSObjectProtocol {     var sourcePixelBufferAttributes: [String : AnyObject]? { get }     var requiredPixelBufferAttributesForRenderContext: [String : AnyObject] { get }     func renderContextChanged(_ newRenderContext: AVVideoCompositionRenderContext)     func startVideoCompositionRequest(_ asyncVideoCompositionRequest: AVAsynchronousVideoCompositionRequest)     optional func cancelAllPendingVideoCompositionRequests() } ``` |
| To | ``` protocol AVVideoCompositing : NSObjectProtocol {     var sourcePixelBufferAttributes: [String : Any]? { get }     var requiredPixelBufferAttributesForRenderContext: [String : Any] { get }     func renderContextChanged(_ newRenderContext: AVVideoCompositionRenderContext)     func startRequest(_ asyncVideoCompositionRequest: AVAsynchronousVideoCompositionRequest)     optional func cancelAllPendingVideoCompositionRequests()     optional var supportsWideColorSourceFrames: Bool { get } } ``` |

Modified [AVVideoCompositing.requiredPixelBufferAttributesForRenderContext](https://developer.apple.com/documentation/avfoundation/avvideocompositing/1386414-requiredpixelbufferattributesfor)

|  | Declaration |
| --- | --- |
| From | ``` var requiredPixelBufferAttributesForRenderContext: [String : AnyObject] { get } ``` |
| To | ``` var requiredPixelBufferAttributesForRenderContext: [String : Any] { get } ``` |

Modified [AVVideoCompositing.sourcePixelBufferAttributes](https://developer.apple.com/documentation/avfoundation/avvideocompositing/1388610-sourcepixelbufferattributes)

|  | Declaration |
| --- | --- |
| From | ``` var sourcePixelBufferAttributes: [String : AnyObject]? { get } ``` |
| To | ``` var sourcePixelBufferAttributes: [String : Any]? { get } ``` |

Modified [AVVideoCompositing.startRequest(_: AVAsynchronousVideoCompositionRequest)](https://developer.apple.com/documentation/avfoundation/avvideocompositing/1388894-startvideocompositionrequest)

|  | Declaration |
| --- | --- |
| From | ``` func startVideoCompositionRequest(_ asyncVideoCompositionRequest: AVAsynchronousVideoCompositionRequest) ``` |
| To | ``` func startRequest(_ asyncVideoCompositionRequest: AVAsynchronousVideoCompositionRequest) ``` |

Modified [AVVideoComposition](https://developer.apple.com/documentation/avfoundation/avvideocomposition)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVVideoComposition : NSObject, NSCopying, NSMutableCopying {      init(propertiesOfAsset asset: AVAsset)     class func videoCompositionWithPropertiesOfAsset(_ asset: AVAsset) -> AVVideoComposition     var customVideoCompositorClass: AnyObject.Type? { get }     var frameDuration: CMTime { get }     var renderSize: CGSize { get }     var renderScale: Float { get }     var instructions: [AVVideoCompositionInstructionProtocol] { get }     var animationTool: AVVideoCompositionCoreAnimationTool? { get } } extension AVVideoComposition {      init(asset asset: AVAsset, applyingCIFiltersWithHandler applier: (AVAsynchronousCIImageFilteringRequest) -> Void)     class func videoCompositionWithAsset(_ asset: AVAsset, applyingCIFiltersWithHandler applier: (AVAsynchronousCIImageFilteringRequest) -> Void) -> AVVideoComposition } extension AVVideoComposition {     func isValidForAsset(_ asset: AVAsset?, timeRange timeRange: CMTimeRange, validationDelegate validationDelegate: AVVideoCompositionValidationHandling?) -> Bool } ``` | NSCopying, NSMutableCopying |
| To | ``` class AVVideoComposition : NSObject, NSCopying, NSMutableCopying {      init(propertiesOf asset: AVAsset)     class func withPropertiesOf(_ asset: AVAsset) -> AVVideoComposition     var customVideoCompositorClass: AVVideoCompositing.Type? { get }     var frameDuration: CMTime { get }     var renderSize: CGSize { get }     var renderScale: Float { get }     var instructions: [AVVideoCompositionInstructionProtocol] { get }     var animationTool: AVVideoCompositionCoreAnimationTool? { get }     func isValid(for asset: AVAsset?, timeRange timeRange: CMTimeRange, validationDelegate validationDelegate: AVVideoCompositionValidationHandling?) -> Bool      init(asset asset: AVAsset, applyingCIFiltersWithHandler applier: @escaping (AVAsynchronousCIImageFilteringRequest) -> Swift.Void)     class func withAsset(_ asset: AVAsset, applyingCIFiltersWithHandler applier: @escaping (AVAsynchronousCIImageFilteringRequest) -> Swift.Void) -> AVVideoComposition     var colorPrimaries: String? { get }     var colorYCbCrMatrix: String? { get }     var colorTransferFunction: String? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVVideoComposition : CVarArg { } extension AVVideoComposition : Equatable, Hashable {     var hashValue: Int { get } } extension AVVideoComposition {     var colorPrimaries: String? { get }     var colorYCbCrMatrix: String? { get }     var colorTransferFunction: String? { get } } extension AVVideoComposition {      init(asset asset: AVAsset, applyingCIFiltersWithHandler applier: @escaping (AVAsynchronousCIImageFilteringRequest) -> Swift.Void)     class func withAsset(_ asset: AVAsset, applyingCIFiltersWithHandler applier: @escaping (AVAsynchronousCIImageFilteringRequest) -> Swift.Void) -> AVVideoComposition } extension AVVideoComposition {     func isValid(for asset: AVAsset?, timeRange timeRange: CMTimeRange, validationDelegate validationDelegate: AVVideoCompositionValidationHandling?) -> Bool } ``` | CVarArg, Equatable, Hashable, NSCopying, NSMutableCopying |

Modified [AVVideoComposition.customVideoCompositorClass](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1389622-customvideocompositorclass)

|  | Declaration |
| --- | --- |
| From | ``` var customVideoCompositorClass: AnyObject.Type? { get } ``` |
| To | ``` var customVideoCompositorClass: AVVideoCompositing.Type? { get } ``` |

Modified [AVVideoComposition.init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Swift.Void)](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1389556-videocompositionwithasset)

|  | Declaration |
| --- | --- |
| From | ``` init(asset asset: AVAsset, applyingCIFiltersWithHandler applier: (AVAsynchronousCIImageFilteringRequest) -> Void) ``` |
| To | ``` init(asset asset: AVAsset, applyingCIFiltersWithHandler applier: @escaping (AVAsynchronousCIImageFilteringRequest) -> Swift.Void) ``` |

Modified [AVVideoComposition.init(propertiesOf: AVAsset)](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1385892-init)

|  | Declaration |
| --- | --- |
| From | ``` init(propertiesOfAsset asset: AVAsset) ``` |
| To | ``` init(propertiesOf asset: AVAsset) ``` |

Modified [AVVideoComposition.isValid(for: AVAsset?, timeRange: CMTimeRange, validationDelegate: AVVideoCompositionValidationHandling?) -> Bool](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1389917-isvalidforasset)

|  | Declaration |
| --- | --- |
| From | ``` func isValidForAsset(_ asset: AVAsset?, timeRange timeRange: CMTimeRange, validationDelegate validationDelegate: AVVideoCompositionValidationHandling?) -> Bool ``` |
| To | ``` func isValid(for asset: AVAsset?, timeRange timeRange: CMTimeRange, validationDelegate validationDelegate: AVVideoCompositionValidationHandling?) -> Bool ``` |

Modified [AVVideoCompositionCoreAnimationTool](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVVideoCompositionCoreAnimationTool : NSObject {     convenience init(additionalLayer layer: CALayer, asTrackID trackID: CMPersistentTrackID)     class func videoCompositionCoreAnimationToolWithAdditionalLayer(_ layer: CALayer, asTrackID trackID: CMPersistentTrackID) -> Self     convenience init(postProcessingAsVideoLayer videoLayer: CALayer, inLayer animationLayer: CALayer)     class func videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayer(_ videoLayer: CALayer, inLayer animationLayer: CALayer) -> Self     convenience init(postProcessingAsVideoLayers videoLayers: [CALayer], inLayer animationLayer: CALayer)     class func videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayers(_ videoLayers: [CALayer], inLayer animationLayer: CALayer) -> Self } ``` | -- |
| To | ``` class AVVideoCompositionCoreAnimationTool : NSObject {     convenience init(additionalLayer layer: CALayer, asTrackID trackID: CMPersistentTrackID)     class func withAdditionalLayer(_ layer: CALayer, asTrackID trackID: CMPersistentTrackID) -> Self     convenience init(postProcessingAsVideoLayer videoLayer: CALayer, in animationLayer: CALayer)     class func withPostProcessing(asVideoLayer videoLayer: CALayer, in animationLayer: CALayer) -> Self     convenience init(postProcessingAsVideoLayers videoLayers: [CALayer], in animationLayer: CALayer)     class func withPostProcessing(asVideoLayers videoLayers: [CALayer], in animationLayer: CALayer) -> Self     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVVideoCompositionCoreAnimationTool : CVarArg { } extension AVVideoCompositionCoreAnimationTool : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVVideoCompositionCoreAnimationTool.init(postProcessingAsVideoLayer: CALayer, in: CALayer)](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/1389594-videocompositioncoreanimationtoo)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(postProcessingAsVideoLayer videoLayer: CALayer, inLayer animationLayer: CALayer) ``` |
| To | ``` convenience init(postProcessingAsVideoLayer videoLayer: CALayer, in animationLayer: CALayer) ``` |

Modified [AVVideoCompositionCoreAnimationTool.init(postProcessingAsVideoLayers: [CALayer], in: CALayer)](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/1389778-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(postProcessingAsVideoLayers videoLayers: [CALayer], inLayer animationLayer: CALayer) ``` |
| To | ``` convenience init(postProcessingAsVideoLayers videoLayers: [CALayer], in animationLayer: CALayer) ``` |

Modified [AVVideoCompositionInstruction](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVVideoCompositionInstruction : NSObject, NSSecureCoding, NSCopying, NSMutableCopying, AVVideoCompositionInstructionProtocol {     var timeRange: CMTimeRange { get }     var backgroundColor: CGColor? { get }     var layerInstructions: [AVVideoCompositionLayerInstruction] { get }     var enablePostProcessing: Bool { get }     var requiredSourceTrackIDs: [NSValue] { get }     var passthroughTrackID: CMPersistentTrackID { get } } ``` | AVVideoCompositionInstructionProtocol, NSCopying, NSMutableCopying, NSSecureCoding |
| To | ``` class AVVideoCompositionInstruction : NSObject, NSSecureCoding, NSCopying, NSMutableCopying, AVVideoCompositionInstructionProtocol {     var timeRange: CMTimeRange { get }     var backgroundColor: CGColor? { get }     var layerInstructions: [AVVideoCompositionLayerInstruction] { get }     var enablePostProcessing: Bool { get }     var requiredSourceTrackIDs: [NSValue] { get }     var passthroughTrackID: CMPersistentTrackID { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVVideoCompositionInstruction : CVarArg { } extension AVVideoCompositionInstruction : Equatable, Hashable {     var hashValue: Int { get } } ``` | AVVideoCompositionInstructionProtocol, CVarArg, Equatable, Hashable, NSCopying, NSMutableCopying, NSSecureCoding |

Modified [AVVideoCompositionLayerInstruction](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVVideoCompositionLayerInstruction : NSObject, NSSecureCoding, NSCopying, NSMutableCopying {     var trackID: CMPersistentTrackID { get }     func getTransformRampForTime(_ time: CMTime, startTransform startTransform: UnsafeMutablePointer<CGAffineTransform>, endTransform endTransform: UnsafeMutablePointer<CGAffineTransform>, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool     func getOpacityRampForTime(_ time: CMTime, startOpacity startOpacity: UnsafeMutablePointer<Float>, endOpacity endOpacity: UnsafeMutablePointer<Float>, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool     func getCropRectangleRampForTime(_ time: CMTime, startCropRectangle startCropRectangle: UnsafeMutablePointer<CGRect>, endCropRectangle endCropRectangle: UnsafeMutablePointer<CGRect>, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool } ``` | NSCopying, NSMutableCopying, NSSecureCoding |
| To | ``` class AVVideoCompositionLayerInstruction : NSObject, NSSecureCoding, NSCopying, NSMutableCopying {     var trackID: CMPersistentTrackID { get }     func getTransformRamp(for time: CMTime, start startTransform: UnsafeMutablePointer<CGAffineTransform>?, end endTransform: UnsafeMutablePointer<CGAffineTransform>?, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool     func getOpacityRamp(for time: CMTime, startOpacity startOpacity: UnsafeMutablePointer<Float>?, endOpacity endOpacity: UnsafeMutablePointer<Float>?, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool     func getCropRectangleRamp(for time: CMTime, startCropRectangle startCropRectangle: UnsafeMutablePointer<CGRect>?, endCropRectangle endCropRectangle: UnsafeMutablePointer<CGRect>?, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVVideoCompositionLayerInstruction : CVarArg { } extension AVVideoCompositionLayerInstruction : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSMutableCopying, NSSecureCoding |

Modified [AVVideoCompositionLayerInstruction.getCropRectangleRamp(for: CMTime, startCropRectangle: UnsafeMutablePointer<CGRect>?, endCropRectangle: UnsafeMutablePointer<CGRect>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/1387998-getcroprectangleramp)

|  | Declaration |
| --- | --- |
| From | ``` func getCropRectangleRampForTime(_ time: CMTime, startCropRectangle startCropRectangle: UnsafeMutablePointer<CGRect>, endCropRectangle endCropRectangle: UnsafeMutablePointer<CGRect>, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool ``` |
| To | ``` func getCropRectangleRamp(for time: CMTime, startCropRectangle startCropRectangle: UnsafeMutablePointer<CGRect>?, endCropRectangle endCropRectangle: UnsafeMutablePointer<CGRect>?, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool ``` |

Modified [AVVideoCompositionLayerInstruction.getOpacityRamp(for: CMTime, startOpacity: UnsafeMutablePointer<Float>?, endOpacity: UnsafeMutablePointer<Float>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/1388471-getopacityramp)

|  | Declaration |
| --- | --- |
| From | ``` func getOpacityRampForTime(_ time: CMTime, startOpacity startOpacity: UnsafeMutablePointer<Float>, endOpacity endOpacity: UnsafeMutablePointer<Float>, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool ``` |
| To | ``` func getOpacityRamp(for time: CMTime, startOpacity startOpacity: UnsafeMutablePointer<Float>?, endOpacity endOpacity: UnsafeMutablePointer<Float>?, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool ``` |

Modified [AVVideoCompositionLayerInstruction.getTransformRamp(for: CMTime, start: UnsafeMutablePointer<CGAffineTransform>?, end: UnsafeMutablePointer<CGAffineTransform>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/1387257-gettransformrampfortime)

|  | Declaration |
| --- | --- |
| From | ``` func getTransformRampForTime(_ time: CMTime, startTransform startTransform: UnsafeMutablePointer<CGAffineTransform>, endTransform endTransform: UnsafeMutablePointer<CGAffineTransform>, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool ``` |
| To | ``` func getTransformRamp(for time: CMTime, start startTransform: UnsafeMutablePointer<CGAffineTransform>?, end endTransform: UnsafeMutablePointer<CGAffineTransform>?, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool ``` |

Modified [AVVideoCompositionRenderContext](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVVideoCompositionRenderContext : NSObject {     var size: CGSize { get }     var renderTransform: CGAffineTransform { get }     var renderScale: Float { get }     var pixelAspectRatio: AVPixelAspectRatio { get }     var edgeWidths: AVEdgeWidths { get }     var highQualityRendering: Bool { get }     var videoComposition: AVVideoComposition { get }     func newPixelBuffer() -> CVPixelBuffer? } ``` | -- |
| To | ``` class AVVideoCompositionRenderContext : NSObject {     var size: CGSize { get }     var renderTransform: CGAffineTransform { get }     var renderScale: Float { get }     var pixelAspectRatio: AVPixelAspectRatio { get }     var edgeWidths: AVEdgeWidths { get }     var highQualityRendering: Bool { get }     var videoComposition: AVVideoComposition { get }     func newPixelBuffer() -> CVPixelBuffer?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVVideoCompositionRenderContext : CVarArg { } extension AVVideoCompositionRenderContext : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVVideoCompositionValidationHandling](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVVideoCompositionValidationHandling : NSObjectProtocol {     optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidValueForKey key: String) -> Bool     optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingEmptyTimeRange timeRange: CMTimeRange) -> Bool     optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction videoCompositionInstruction: AVVideoCompositionInstructionProtocol) -> Bool     optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction videoCompositionInstruction: AVVideoCompositionInstructionProtocol, layerInstruction layerInstruction: AVVideoCompositionLayerInstruction, asset asset: AVAsset) -> Bool } ``` |
| To | ``` protocol AVVideoCompositionValidationHandling : NSObjectProtocol {     optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidValueForKey key: String) -> Bool     optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingEmptyTimeRange timeRange: CMTimeRange) -> Bool     optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTimeRangeIn videoCompositionInstruction: AVVideoCompositionInstructionProtocol) -> Bool     optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTrackIDIn videoCompositionInstruction: AVVideoCompositionInstructionProtocol, layerInstruction layerInstruction: AVVideoCompositionLayerInstruction, asset asset: AVAsset) -> Bool } ``` |

Modified [AVVideoCompositionValidationHandling.videoComposition(_: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTimeRangeIn: AVVideoCompositionInstructionProtocol) -> Bool](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/1390721-videocomposition)

|  | Declaration |
| --- | --- |
| From | ``` optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction videoCompositionInstruction: AVVideoCompositionInstructionProtocol) -> Bool ``` |
| To | ``` optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTimeRangeIn videoCompositionInstruction: AVVideoCompositionInstructionProtocol) -> Bool ``` |

Modified [AVVideoCompositionValidationHandling.videoComposition(_: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTrackIDIn: AVVideoCompositionInstructionProtocol, layerInstruction: AVVideoCompositionLayerInstruction, asset: AVAsset) -> Bool](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/1388452-videocomposition)

|  | Declaration |
| --- | --- |
| From | ``` optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction videoCompositionInstruction: AVVideoCompositionInstructionProtocol, layerInstruction layerInstruction: AVVideoCompositionLayerInstruction, asset asset: AVAsset) -> Bool ``` |
| To | ``` optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTrackIDIn videoCompositionInstruction: AVVideoCompositionInstructionProtocol, layerInstruction layerInstruction: AVVideoCompositionLayerInstruction, asset asset: AVAsset) -> Bool ``` |

Modified [NSCoder.decodeTime(forKey: String) -> CMTime](https://developer.apple.com/documentation/foundation/nscoder/1389544-decodetime)

|  | Declaration |
| --- | --- |
| From | ``` func decodeCMTimeForKey(_ key: String) -> CMTime ``` |
| To | ``` func decodeTime(forKey key: String) -> CMTime ``` |

Modified [NSCoder.decodeTimeMapping(forKey: String) -> CMTimeMapping](https://developer.apple.com/documentation/foundation/nscoder/1389860-decodetimemapping)

|  | Declaration |
| --- | --- |
| From | ``` func decodeCMTimeMappingForKey(_ key: String) -> CMTimeMapping ``` |
| To | ``` func decodeTimeMapping(forKey key: String) -> CMTimeMapping ``` |

Modified [NSCoder.decodeTimeRange(forKey: String) -> CMTimeRange](https://developer.apple.com/documentation/foundation/nscoder/1385718-decodecmtimerangeforkey)

|  | Declaration |
| --- | --- |
| From | ``` func decodeCMTimeRangeForKey(_ key: String) -> CMTimeRange ``` |
| To | ``` func decodeTimeRange(forKey key: String) -> CMTimeRange ``` |

Modified [NSCoder.encode(_: CMTimeRange, forKey: String)](https://developer.apple.com/documentation/foundation/nscoder/1386649-encode)

|  | Declaration |
| --- | --- |
| From | ``` func encodeCMTimeRange(_ timeRange: CMTimeRange, forKey key: String) ``` |
| To | ``` func encode(_ timeRange: CMTimeRange, forKey key: String) ``` |

Modified [NSCoder.encode(_: CMTime, forKey: String)](https://developer.apple.com/documentation/foundation/nscoder/1388869-encodecmtime)

|  | Declaration |
| --- | --- |
| From | ``` func encodeCMTime(_ time: CMTime, forKey key: String) ``` |
| To | ``` func encode(_ time: CMTime, forKey key: String) ``` |

Modified [NSCoder.encode(_: CMTimeMapping, forKey: String)](https://developer.apple.com/documentation/foundation/nscoder/1389496-encode)

|  | Declaration |
| --- | --- |
| From | ``` func encodeCMTimeMapping(_ timeMapping: CMTimeMapping, forKey key: String) ``` |
| To | ``` func encode(_ timeMapping: CMTimeMapping, forKey key: String) ``` |

Modified [NSNotification.Name.AVAssetChapterMetadataGroupsDidChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1386794-avassetchaptermetadatagroupsdidc)

|  | Name | Declaration |
| --- | --- | --- |
| From | AVAssetChapterMetadataGroupsDidChangeNotification | ``` let AVAssetChapterMetadataGroupsDidChangeNotification: String ``` |
| To | AVAssetChapterMetadataGroupsDidChange | ``` static let AVAssetChapterMetadataGroupsDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.AVAssetDurationDidChange](https://developer.apple.com/documentation/avfoundation/avassetdurationdidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | AVAssetDurationDidChangeNotification | ``` let AVAssetDurationDidChangeNotification: String ``` |
| To | AVAssetDurationDidChange | ``` static let AVAssetDurationDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.AVAssetMediaSelectionGroupsDidChange](https://developer.apple.com/documentation/avfoundation/avassetmediaselectiongroupsdidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | AVAssetMediaSelectionGroupsDidChangeNotification | ``` let AVAssetMediaSelectionGroupsDidChangeNotification: String ``` |
| To | AVAssetMediaSelectionGroupsDidChange | ``` static let AVAssetMediaSelectionGroupsDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.AVAssetTrackSegmentsDidChange](https://developer.apple.com/documentation/avfoundation/avassettracksegmentsdidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | AVAssetTrackSegmentsDidChangeNotification | ``` let AVAssetTrackSegmentsDidChangeNotification: String ``` |
| To | AVAssetTrackSegmentsDidChange | ``` static let AVAssetTrackSegmentsDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.AVAssetTrackTimeRangeDidChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1385765-avassettracktimerangedidchange)

|  | Name | Declaration |
| --- | --- | --- |
| From | AVAssetTrackTimeRangeDidChangeNotification | ``` let AVAssetTrackTimeRangeDidChangeNotification: String ``` |
| To | AVAssetTrackTimeRangeDidChange | ``` static let AVAssetTrackTimeRangeDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.AVAssetTrackTrackAssociationsDidChange](https://developer.apple.com/documentation/avfoundation/avassettracktrackassociationsdidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | AVAssetTrackTrackAssociationsDidChangeNotification | ``` let AVAssetTrackTrackAssociationsDidChangeNotification: String ``` |
| To | AVAssetTrackTrackAssociationsDidChange | ``` static let AVAssetTrackTrackAssociationsDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.AVAudioEngineConfigurationChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1389078-avaudioengineconfigurationchange)

|  | Name | Declaration |
| --- | --- | --- |
| From | AVAudioEngineConfigurationChangeNotification | ``` let AVAudioEngineConfigurationChangeNotification: String ``` |
| To | AVAudioEngineConfigurationChange | ``` static let AVAudioEngineConfigurationChange: NSNotification.Name ``` |

Modified [NSNotification.Name.AVAudioSessionInterruption](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616596-interruptionnotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | AVAudioSessionInterruptionNotification | ``` let AVAudioSessionInterruptionNotification: String ``` |
| To | AVAudioSessionInterruption | ``` static let AVAudioSessionInterruption: NSNotification.Name ``` |

Modified [NSNotification.Name.AVAudioSessionMediaServicesWereLost](https://developer.apple.com/documentation/avfoundation/avaudiosessionmediaserviceswerelostnotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | AVAudioSessionMediaServicesWereLostNotification | ``` let AVAudioSessionMediaServicesWereLostNotification: String ``` |
| To | AVAudioSessionMediaServicesWereLost | ``` static let AVAudioSessionMediaServicesWereLost: NSNotification.Name ``` |

Modified [NSNotification.Name.AVAudioSessionMediaServicesWereReset](https://developer.apple.com/documentation/avfoundation/avaudiosessionmediaserviceswereresetnotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | AVAudioSessionMediaServicesWereResetNotification | ``` let AVAudioSessionMediaServicesWereResetNotification: String ``` |
| To | AVAudioSessionMediaServicesWereReset | ``` static let AVAudioSessionMediaServicesWereReset: NSNotification.Name ``` |

Modified [NSNotification.Name.AVAudioSessionRouteChange](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616493-routechangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | AVAudioSessionRouteChangeNotification | ``` let AVAudioSessionRouteChangeNotification: String ``` |
| To | AVAudioSessionRouteChange | ``` static let AVAudioSessionRouteChange: NSNotification.Name ``` |

Modified [NSNotification.Name.AVAudioSessionSilenceSecondaryAudioHint](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616622-silencesecondaryaudiohintnotific)

|  | Name | Declaration |
| --- | --- | --- |
| From | AVAudioSessionSilenceSecondaryAudioHintNotification | ``` let AVAudioSessionSilenceSecondaryAudioHintNotification: String ``` |
| To | AVAudioSessionSilenceSecondaryAudioHint | ``` static let AVAudioSessionSilenceSecondaryAudioHint: NSNotification.Name ``` |

Modified [NSNotification.Name.AVAudioUnitComponentTagsDidChange](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponenttagsdidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | AVAudioUnitComponentTagsDidChangeNotification | ``` let AVAudioUnitComponentTagsDidChangeNotification: String ``` |
| To | AVAudioUnitComponentTagsDidChange | ``` static let AVAudioUnitComponentTagsDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.AVPlayerItemDidPlayToEndTime](https://developer.apple.com/documentation/foundation/nsnotification/name/1386566-avplayeritemdidplaytoendtime)

|  | Name | Declaration |
| --- | --- | --- |
| From | AVPlayerItemDidPlayToEndTimeNotification | ``` let AVPlayerItemDidPlayToEndTimeNotification: String ``` |
| To | AVPlayerItemDidPlayToEndTime | ``` static let AVPlayerItemDidPlayToEndTime: NSNotification.Name ``` |

Modified [NSNotification.Name.AVPlayerItemFailedToPlayToEndTime](https://developer.apple.com/documentation/foundation/nsnotification/name/1388007-avplayeritemfailedtoplaytoendtim)

|  | Name | Declaration |
| --- | --- | --- |
| From | AVPlayerItemFailedToPlayToEndTimeNotification | ``` let AVPlayerItemFailedToPlayToEndTimeNotification: String ``` |
| To | AVPlayerItemFailedToPlayToEndTime | ``` static let AVPlayerItemFailedToPlayToEndTime: NSNotification.Name ``` |

Modified [NSNotification.Name.AVPlayerItemNewAccessLogEntry](https://developer.apple.com/documentation/avfoundation/avplayeritemnewaccesslogentrynotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | AVPlayerItemNewAccessLogEntryNotification | ``` let AVPlayerItemNewAccessLogEntryNotification: String ``` |
| To | AVPlayerItemNewAccessLogEntry | ``` static let AVPlayerItemNewAccessLogEntry: NSNotification.Name ``` |

Modified [NSNotification.Name.AVPlayerItemNewErrorLogEntry](https://developer.apple.com/documentation/foundation/nsnotification/name/1388450-avplayeritemnewerrorlogentry)

|  | Name | Declaration |
| --- | --- | --- |
| From | AVPlayerItemNewErrorLogEntryNotification | ``` let AVPlayerItemNewErrorLogEntryNotification: String ``` |
| To | AVPlayerItemNewErrorLogEntry | ``` static let AVPlayerItemNewErrorLogEntry: NSNotification.Name ``` |

Modified [NSNotification.Name.AVPlayerItemPlaybackStalled](https://developer.apple.com/documentation/foundation/nsnotification/name/1387661-avplayeritemplaybackstalled)

|  | Name | Declaration |
| --- | --- | --- |
| From | AVPlayerItemPlaybackStalledNotification | ``` let AVPlayerItemPlaybackStalledNotification: String ``` |
| To | AVPlayerItemPlaybackStalled | ``` static let AVPlayerItemPlaybackStalled: NSNotification.Name ``` |

Modified [NSNotification.Name.AVPlayerItemTimeJumped](https://developer.apple.com/documentation/avfoundation/avplayeritemtimejumpednotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | AVPlayerItemTimeJumpedNotification | ``` let AVPlayerItemTimeJumpedNotification: String ``` |
| To | AVPlayerItemTimeJumped | ``` static let AVPlayerItemTimeJumped: NSNotification.Name ``` |

Modified [NSValue.init(time: CMTime)](https://developer.apple.com/documentation/foundation/nsvalue/1388561-init)

|  | Declaration |
| --- | --- |
| From | ``` init(CMTime time: CMTime) ``` |
| To | ``` init(time time: CMTime) ``` |

Modified [NSValue.init(timeMapping: CMTimeMapping)](https://developer.apple.com/documentation/foundation/nsvalue/1387556-valuewithcmtimemapping)

|  | Declaration |
| --- | --- |
| From | ``` init(CMTimeMapping timeMapping: CMTimeMapping) ``` |
| To | ``` init(timeMapping timeMapping: CMTimeMapping) ``` |

Modified [NSValue.init(timeRange: CMTimeRange)](https://developer.apple.com/documentation/foundation/nsvalue/1386915-init)

|  | Declaration |
| --- | --- |
| From | ``` init(CMTimeRange timeRange: CMTimeRange) ``` |
| To | ``` init(timeRange timeRange: CMTimeRange) ``` |

Modified [NSValue.timeMappingValue](https://developer.apple.com/documentation/foundation/nsvalue/1387277-timemappingvalue)

|  | Declaration |
| --- | --- |
| From | ``` var CMTimeMappingValue: CMTimeMapping { get } ``` |
| To | ``` var timeMappingValue: CMTimeMapping { get } ``` |

Modified [NSValue.timeRangeValue](https://developer.apple.com/documentation/foundation/nsvalue/1385930-cmtimerangevalue)

|  | Declaration |
| --- | --- |
| From | ``` var CMTimeRangeValue: CMTimeRange { get } ``` |
| To | ``` var timeRangeValue: CMTimeRange { get } ``` |

Modified [NSValue.timeValue](https://developer.apple.com/documentation/foundation/nsvalue/1388151-cmtimevalue)

|  | Declaration |
| --- | --- |
| From | ``` var CMTimeValue: CMTime { get } ``` |
| To | ``` var timeValue: CMTime { get } ``` |

Modified [AVAssetImageGeneratorCompletionHandler](https://developer.apple.com/documentation/avfoundation/avassetimagegeneratorcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias AVAssetImageGeneratorCompletionHandler = (CMTime, CGImage?, CMTime, AVAssetImageGeneratorResult, NSError?) -> Void ``` |
| To | ``` typealias AVAssetImageGeneratorCompletionHandler = (CMTime, CGImage?, CMTime, AVAssetImageGeneratorResult, Error?) -> Swift.Void ``` |

Modified [AVAudioNodeCompletionHandler](https://developer.apple.com/documentation/avfoundation/avaudionodecompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias AVAudioNodeCompletionHandler = () -> Void ``` |
| To | ``` typealias AVAudioNodeCompletionHandler = () -> Swift.Void ``` |

Modified [AVAudioNodeTapBlock](https://developer.apple.com/documentation/avfoundation/avaudionodetapblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias AVAudioNodeTapBlock = (AVAudioPCMBuffer, AVAudioTime) -> Void ``` |
| To | ``` typealias AVAudioNodeTapBlock = (AVAudioPCMBuffer, AVAudioTime) -> Swift.Void ``` |

Modified [AVMakeRect(aspectRatio: CGSize, insideRect: CGRect) -> CGRect](https://developer.apple.com/documentation/avfoundation/1390116-avmakerectwithaspectratioinsider)

|  | Declaration |
| --- | --- |
| From | ``` func AVMakeRectWithAspectRatioInsideRect(_ aspectRatio: CGSize, _ boundingRect: CGRect) -> CGRect ``` |
| To | ``` func AVMakeRect(aspectRatio aspectRatio: CGSize, insideRect boundingRect: CGRect) -> CGRect ``` |

Modified [AVMIDIPlayerCompletionHandler](https://developer.apple.com/documentation/avfoundation/avmidiplayercompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias AVMIDIPlayerCompletionHandler = () -> Void ``` |
| To | ``` typealias AVMIDIPlayerCompletionHandler = () -> Swift.Void ``` |

Modified [PermissionBlock](https://developer.apple.com/documentation/avfoundation/permissionblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias PermissionBlock = (Bool) -> Void ``` |
| To | ``` typealias PermissionBlock = (Bool) -> Swift.Void ``` |

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
