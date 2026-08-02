---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/AVFoundation.html
archived_at: '2026-07-18T02:56:38.556651Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# AVFoundation Changes for Swift

### AVFoundation

Removed AVAssetReferenceRestrictions.init(_: UInt)Removed AVAudioEnvironmentNode.applicableRenderingAlgorithms() -> [AnyObject]!Removed AVAudioPlayerNodeBufferOptions.init(_: UInt)Removed AVAudioSessionCategoryOptions.init(_: UInt)Removed AVAudioSessionInterruptionOptions.init(_: UInt)Removed AVAudioSessionRecordPermission.init(_: UInt)Removed AVAudioSessionSetActiveOptions.init(_: UInt)Removed AVCaptureDeviceInput.deviceInputWithDevice(_: AVCaptureDevice!, error: NSErrorPointer) -> AnyObject! [class]Removed AVCaptureVideoPreviewLayer.layerWithSession(_: AVCaptureSession!) -> AnyObject! [class]Removed AVCaptureVideoPreviewLayer.layerWithSessionWithNoConnection(_: AVCaptureSession!) -> AnyObject! [class]Removed AVPlayer.playerWithPlayerItem(_: AVPlayerItem!) -> AnyObject! [class]Removed AVPlayer.playerWithURL(_: NSURL!) -> AnyObject! [class]Removed AVQueuePlayer.queuePlayerWithItems(_: [AnyObject]!) -> AnyObject! [class]Added [AVAsset.canContainFragments](https://developer.apple.com/documentation/avfoundation/avasset/1389520-cancontainfragments)Added [AVAsset.compatibleWithAirPlayVideo](https://developer.apple.com/documentation/avfoundation/avasset/1390333-compatiblewithairplayvideo)Added [AVAsset.containsFragments](https://developer.apple.com/documentation/avfoundation/avasset/1385589-containsfragments)Added [AVAsset.preferredMediaSelection](https://developer.apple.com/documentation/avfoundation/avasset/1386122-preferredmediaselection)Added [AVAssetDownloadDelegate](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate)Added [AVAssetDownloadDelegate.URLSession(_: NSURLSession, assetDownloadTask: AVAssetDownloadTask, didLoadTimeRange: CMTimeRange, totalTimeRangesLoaded: [NSValue], timeRangeExpectedToLoad: CMTimeRange)](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/1621019-urlsession)Added [AVAssetDownloadDelegate.URLSession(_: NSURLSession, assetDownloadTask: AVAssetDownloadTask, didResolveMediaSelection: AVMediaSelection)](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/1621023-urlsession)Added [AVAssetDownloadTask](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask)Added [AVAssetDownloadTask.destinationURL](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask/1621022-destinationurl)Added [AVAssetDownloadTask.loadedTimeRanges](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask/1621026-loadedtimeranges)Added [AVAssetDownloadTask.options](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask/1621014-options)Added [AVAssetDownloadTask.URLAsset](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask/1621024-urlasset)Added [AVAssetDownloadURLSession](https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession)Added [AVAssetDownloadURLSession.assetDownloadTaskWithURLAsset(_: AVURLAsset, destinationURL: NSURL, options: [String : AnyObject]?) -> AVAssetDownloadTask?](https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession/1621018-assetdownloadtaskwithurlasset)Added [AVAssetDownloadURLSession.init(configuration: NSURLSessionConfiguration, assetDownloadDelegate: AVAssetDownloadDelegate?, delegateQueue: NSOperationQueue?)](https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession/1621015-sessionwithconfiguration)Added [AVAssetResourceLoader.preloadsEligibleContentKeys](https://developer.apple.com/documentation/avfoundation/avassetresourceloader/1386939-preloadseligiblecontentkeys)Added [AVAssetResourceLoadingDataRequest.requestsAllDataToEndOfResource](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest/1386864-requestsalldatatoendofresource)Added [AVAssetResourceLoadingRequest.persistentContentKeyFromKeyVendorResponse(_: NSData, options: [String : AnyObject]?, error: NSErrorPointer) -> NSData](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1623676-persistentcontentkey)Added [AVAssetWriter.overallDurationHint](https://developer.apple.com/documentation/avfoundation/avassetwriter/1388408-overalldurationhint)Added [AVAsynchronousCIImageFilteringRequest](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest)Added [AVAsynchronousCIImageFilteringRequest.compositionTime](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/1388240-compositiontime)Added [AVAsynchronousCIImageFilteringRequest.finishWithError(_: NSError)](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/1386608-finish)Added [AVAsynchronousCIImageFilteringRequest.finishWithImage(_: CIImage, context: CIContext?)](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/1389124-finish)Added [AVAsynchronousCIImageFilteringRequest.renderSize](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/1387933-rendersize)Added [AVAsynchronousCIImageFilteringRequest.sourceImage](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/1387577-sourceimage)Added [AVAudioCompressedBuffer](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer)Added [AVAudioCompressedBuffer.data](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1390620-data)Added [AVAudioCompressedBuffer.init(format: AVAudioFormat, packetCapacity: AVAudioPacketCount)](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1387124-initwithformat)Added [AVAudioCompressedBuffer.init(format: AVAudioFormat, packetCapacity: AVAudioPacketCount, maximumPacketSize: Int)](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1386718-initwithformat)Added [AVAudioCompressedBuffer.maximumPacketSize](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1389326-maximumpacketsize)Added [AVAudioCompressedBuffer.packetCapacity](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1386081-packetcapacity)Added [AVAudioCompressedBuffer.packetCount](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1386000-packetcount)Added [AVAudioCompressedBuffer.packetDescriptions](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1389750-packetdescriptions)Added [AVAudioConnectionPoint](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint)Added [AVAudioConnectionPoint.bus](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint/1389288-bus)Added [AVAudioConnectionPoint.init(node: AVAudioNode, bus: AVAudioNodeBus)](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint/1388569-init)Added [AVAudioConnectionPoint.node](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint/1386935-node)Added [AVAudioConverter](https://developer.apple.com/documentation/avfoundation/avaudioconverter)Added [AVAudioConverter.applicableEncodeBitRates](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388940-applicableencodebitrates)Added [AVAudioConverter.applicableEncodeSampleRates](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1389427-applicableencodesamplerates)Added [AVAudioConverter.availableEncodeBitRates](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388589-availableencodebitrates)Added [AVAudioConverter.availableEncodeChannelLayoutTags](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387337-availableencodechannellayouttags)Added [AVAudioConverter.availableEncodeSampleRates](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1386202-availableencodesamplerates)Added [AVAudioConverter.bitRate](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390373-bitrate)Added [AVAudioConverter.bitRateStrategy](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1386092-bitratestrategy)Added [AVAudioConverter.channelMap](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390653-channelmap)Added [AVAudioConverter.convertToBuffer(_: AVAudioBuffer, error: NSErrorPointer, withInputFromBlock: AVAudioConverterInputBlock) -> AVAudioConverterOutputStatus](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387865-convert)Added [AVAudioConverter.convertToBuffer(_: AVAudioPCMBuffer, fromBuffer: AVAudioPCMBuffer) throws](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388341-converttobuffer)Added [AVAudioConverter.dither](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1386312-dither)Added [AVAudioConverter.downmix](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388244-downmix)Added [AVAudioConverter.init(fromFormat: AVAudioFormat, toFormat: AVAudioFormat)](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387008-initfromformat)Added [AVAudioConverter.inputFormat](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388914-inputformat)Added [AVAudioConverter.magicCookie](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390770-magiccookie)Added [AVAudioConverter.maximumOutputPacketSize](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390069-maximumoutputpacketsize)Added [AVAudioConverter.outputFormat](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387563-outputformat)Added [AVAudioConverter.primeInfo](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1389770-primeinfo)Added [AVAudioConverter.primeMethod](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387299-primemethod)Added [AVAudioConverter.reset()](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390876-reset)Added [AVAudioConverter.sampleRateConverterAlgorithm](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387976-samplerateconverteralgorithm)Added [AVAudioConverter.sampleRateConverterQuality](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390887-samplerateconverterquality)Added [AVAudioConverterInputStatus [enum]](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus)Added [AVAudioConverterInputStatus.EndOfStream](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus/endofstream)Added [AVAudioConverterInputStatus.HaveData](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus/avaudioconverterinputstatus_havedata)Added [AVAudioConverterInputStatus.NoDataNow](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus/nodatanow)Added [AVAudioConverterOutputStatus [enum]](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus)Added [AVAudioConverterOutputStatus.EndOfStream](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/endofstream)Added [AVAudioConverterOutputStatus.Error](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/error)Added [AVAudioConverterOutputStatus.HaveData](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/avaudioconverteroutputstatus_havedata)Added [AVAudioConverterOutputStatus.InputRanDry](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/inputrandry)Added [AVAudioConverterPrimeInfo [struct]](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimeinfo)Added AVAudioConverterPrimeInfo.init()Added AVAudioConverterPrimeInfo.init(leadingFrames: AVAudioFrameCount, trailingFrames: AVAudioFrameCount)Added [AVAudioConverterPrimeInfo.leadingFrames](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimeinfo/1386016-leadingframes)Added [AVAudioConverterPrimeInfo.trailingFrames](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimeinfo/1386943-trailingframes)Added [AVAudioConverterPrimeMethod [enum]](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod)Added [AVAudioConverterPrimeMethod.None](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod/none)Added [AVAudioConverterPrimeMethod.Normal](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod/normal)Added [AVAudioConverterPrimeMethod.Pre](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod/pre)Added [AVAudioEngine.connect(_: AVAudioNode, toConnectionPoints: [AVAudioConnectionPoint], fromBus: AVAudioNodeBus, format: AVAudioFormat?)](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389510-connect)Added [AVAudioEngine.inputConnectionPointForNode(_: AVAudioNode, inputBus: AVAudioNodeBus) -> AVAudioConnectionPoint?](https://developer.apple.com/documentation/avfoundation/avaudioengine/1387521-inputconnectionpoint)Added [AVAudioEngine.outputConnectionPointsForNode(_: AVAudioNode, outputBus: AVAudioNodeBus) -> [AVAudioConnectionPoint]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389298-outputconnectionpointsfornode)Added [AVAudioEnvironmentNode.applicableRenderingAlgorithms](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1390049-applicablerenderingalgorithms)Added [AVAudioFormat.formatDescription](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387467-formatdescription)Added [AVAudioFormat.init(CMAudioFormatDescription: CMAudioFormatDescription)](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387465-initwithcmaudioformatdescription)Added [AVAudioMixing.destinationForMixer(_: AVAudioNode, bus: AVAudioNodeBus) -> AVAudioMixingDestination?](https://developer.apple.com/documentation/avfoundation/avaudiomixing/1390356-destination)Added [AVAudioMixingDestination](https://developer.apple.com/documentation/avfoundation/avaudiomixingdestination)Added [AVAudioMixingDestination.connectionPoint](https://developer.apple.com/documentation/avfoundation/avaudiomixingdestination/1389898-connectionpoint)Added [AVAudioSequencer](https://developer.apple.com/documentation/avfoundation/avaudiosequencer)Added [AVAudioSequencer.beatsForHostTime(_: UInt64, error: NSErrorPointer) -> AVMusicTimeStamp](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1389012-beatsforhosttime)Added [AVAudioSequencer.beatsForSeconds(_: NSTimeInterval) -> AVMusicTimeStamp](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387853-beats)Added [AVAudioSequencer.currentPositionInBeats](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388910-currentpositioninbeats)Added [AVAudioSequencer.currentPositionInSeconds](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1390524-currentpositioninseconds)Added [AVAudioSequencer.dataWithSMPTEResolution(_: Int, error: NSErrorPointer) -> NSData](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388701-datawithsmpteresolution)Added [AVAudioSequencer.hostTimeForBeats(_: AVMusicTimeStamp, error: NSErrorPointer) -> UInt64](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1386184-hosttime)Added [AVAudioSequencer.init()](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1385851-init)Added [AVAudioSequencer.init(audioEngine: AVAudioEngine)](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388339-init)Added [AVAudioSequencer.loadFromData(_: NSData, options: AVMusicSequenceLoadOptions) throws](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1389720-loadfromdata)Added [AVAudioSequencer.loadFromURL(_: NSURL, options: AVMusicSequenceLoadOptions) throws](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1386241-loadfromurl)Added [AVAudioSequencer.playing](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388402-playing)Added [AVAudioSequencer.prepareToPlay()](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1385633-preparetoplay)Added [AVAudioSequencer.rate](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387903-rate)Added [AVAudioSequencer.secondsForBeats(_: AVMusicTimeStamp) -> NSTimeInterval](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387615-seconds)Added [AVAudioSequencer.start() throws](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387594-startandreturnerror)Added [AVAudioSequencer.stop()](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1386674-stop)Added [AVAudioSequencer.tempoTrack](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1390252-tempotrack)Added [AVAudioSequencer.tracks](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387567-tracks)Added [AVAudioSequencer.userInfo](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1389262-userinfo)Added [AVAudioSequencer.writeToURL(_: NSURL, SMPTEResolution: Int, replaceExisting: Bool) throws](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1390589-write)Added [AVAudioSession.availableCategories](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616591-availablecategories)Added [AVAudioSession.availableModes](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616517-availablemodes)Added [AVAudioSessionCategoryOptions.InterruptSpokenAudioAndMixWithOthers](https://developer.apple.com/documentation/avfoundation/avaudiosession/categoryoptions/1616534-interruptspokenaudioandmixwithot)Added [AVAudioSessionErrorCode.CodeResourceNotAvailable](https://developer.apple.com/documentation/avfoundation/avaudiosessionerrorcode/avaudiosessionerrorcoderesourcenotavailable)Added [AVAudioUnit.AUAudioUnit](https://developer.apple.com/documentation/avfoundation/avaudiounit/1388167-auaudiounit)Added [AVAudioUnit.instantiateWithComponentDescription(_: AudioComponentDescription, options: AudioComponentInstantiationOptions, completionHandler: (AVAudioUnit?, NSError?) -> Void) [class]](https://developer.apple.com/documentation/avfoundation/avaudiounit/1390583-instantiatewithcomponentdescript)Added [AVAudioUnitComponent](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent)Added [AVAudioUnitComponent.allTagNames](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387996-alltagnames)Added [AVAudioUnitComponent.audioComponent](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1385910-audiocomponent)Added [AVAudioUnitComponent.audioComponentDescription](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387404-audiocomponentdescription)Added [AVAudioUnitComponent.hasMIDIInput](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1389600-hasmidiinput)Added [AVAudioUnitComponent.hasMIDIOutput](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387070-hasmidioutput)Added [AVAudioUnitComponent.localizedTypeName](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1390541-localizedtypename)Added [AVAudioUnitComponent.manufacturerName](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387472-manufacturername)Added [AVAudioUnitComponent.name](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1385941-name)Added [AVAudioUnitComponent.sandboxSafe](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1390100-issandboxsafe)Added [AVAudioUnitComponent.typeName](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1389988-typename)Added [AVAudioUnitComponent.version](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387762-version)Added [AVAudioUnitComponent.versionString](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1388446-versionstring)Added [AVAudioUnitComponentManager](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager)Added [AVAudioUnitComponentManager.componentsMatchingDescription(_: AudioComponentDescription) -> [AVAudioUnitComponent]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1386367-components)Added [AVAudioUnitComponentManager.componentsMatchingPredicate(_: NSPredicate) -> [AVAudioUnitComponent]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1386487-components)Added [AVAudioUnitComponentManager.componentsPassingTest(_: (AVAudioUnitComponent, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AVAudioUnitComponent]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1390260-components)Added [AVAudioUnitComponentManager.sharedAudioUnitComponentManager() -> Self [class]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1390177-shared)Added [AVAudioUnitComponentManager.standardLocalizedTagNames](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1388545-standardlocalizedtagnames)Added [AVAudioUnitComponentManager.tagNames](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1390133-tagnames)Added [AVCaptureMetadataInput](https://developer.apple.com/documentation/avfoundation/avcapturemetadatainput)Added [AVCaptureMetadataInput.appendTimedMetadataGroup(_: AVTimedMetadataGroup!) throws](https://developer.apple.com/documentation/avfoundation/avcapturemetadatainput/1622266-appendtimedmetadatagroup)Added [AVCaptureMetadataInput.init(formatDescription: CMMetadataFormatDescription!, clock: CMClock!)](https://developer.apple.com/documentation/avfoundation/avcapturemetadatainput/1622268-init)Added [AVCaptureMovieFileOutput.recordsVideoOrientationAndMirroringChangesAsMetadataTrackForConnection(_: AVCaptureConnection!) -> Bool](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/1616292-recordsvideoorientationandmirror)Added [AVCaptureMovieFileOutput.setRecordsVideoOrientationAndMirroringChanges(_: Bool, asMetadataTrackForConnection: AVCaptureConnection!)](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/1616284-setrecordsvideoorientationandmir)Added [AVCaptureSessionInterruptionReason [enum]](https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionreason)Added [AVCaptureSessionInterruptionReason.AudioDeviceInUseByAnotherClient](https://developer.apple.com/documentation/avfoundation/avcapturesessioninterruptionreason/avcapturesessioninterruptionreasonaudiodeviceinusebyanotherclient)Added [AVCaptureSessionInterruptionReason.VideoDeviceInUseByAnotherClient](https://developer.apple.com/documentation/avfoundation/avcapturesessioninterruptionreason/avcapturesessioninterruptionreasonvideodeviceinusebyanotherclient)Added [AVCaptureSessionInterruptionReason.VideoDeviceNotAvailableInBackground](https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionreason/videodevicenotavailableinbackground)Added [AVCaptureSessionInterruptionReason.VideoDeviceNotAvailableWithMultipleForegroundApps](https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionreason/videodevicenotavailablewithmultipleforegroundapps)Added [AVCaptureStillImageOutput.lensStabilizationDuringBracketedCaptureEnabled](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616287-islensstabilizationduringbracket)Added [AVCaptureStillImageOutput.lensStabilizationDuringBracketedCaptureSupported](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616288-islensstabilizationduringbracket)Added [AVComposition.tracksWithMediaCharacteristic(_: String) -> [AVCompositionTrack]](https://developer.apple.com/documentation/avfoundation/avcomposition/1387525-trackswithmediacharacteristic)Added [AVComposition.tracksWithMediaType(_: String) -> [AVCompositionTrack]](https://developer.apple.com/documentation/avfoundation/avcomposition/1386534-trackswithmediatype)Added [AVComposition.trackWithTrackID(_: CMPersistentTrackID) -> AVCompositionTrack?](https://developer.apple.com/documentation/avfoundation/avcomposition/1388473-track)Added [AVComposition.URLAssetInitializationOptions](https://developer.apple.com/documentation/avfoundation/avcomposition/1387080-urlassetinitializationoptions)Added [AVDateRangeMetadataGroup](https://developer.apple.com/documentation/avfoundation/avdaterangemetadatagroup)Added [AVDateRangeMetadataGroup.endDate](https://developer.apple.com/documentation/avfoundation/avdaterangemetadatagroup/1386255-enddate)Added [AVDateRangeMetadataGroup.init(items: [AVMetadataItem], startDate: NSDate, endDate: NSDate?)](https://developer.apple.com/documentation/avfoundation/avdaterangemetadatagroup/1389614-init)Added [AVDateRangeMetadataGroup.items](https://developer.apple.com/documentation/avfoundation/avdaterangemetadatagroup/1390120-items)Added [AVDateRangeMetadataGroup.startDate](https://developer.apple.com/documentation/avfoundation/avdaterangemetadatagroup/1386420-startdate)Added [AVError.RecordingAlreadyInProgress](https://developer.apple.com/documentation/avfoundation/averror/code/recordingalreadyinprogress)Added [AVError.VideoCompositorFailed](https://developer.apple.com/documentation/avfoundation/averror/averrorvideocompositorfailed)Added [AVFragmentedAsset.tracksWithMediaCharacteristic(_: String) -> [AVFragmentedAssetTrack]](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/1387259-tracks)Added [AVFragmentedAsset.tracksWithMediaType(_: String) -> [AVFragmentedAssetTrack]](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/1387253-tracks)Added [AVFragmentedAsset.trackWithTrackID(_: CMPersistentTrackID) -> AVFragmentedAssetTrack?](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/1385712-trackwithtrackid)Added [AVFragmentMinding](https://developer.apple.com/documentation/avfoundation/avfragmentminding)Added [AVMediaSelection](https://developer.apple.com/documentation/avfoundation/avmediaselection)Added [AVMediaSelection.asset](https://developer.apple.com/documentation/avfoundation/avmediaselection/1390874-asset)Added [AVMediaSelection.mediaSelectionCriteriaCanBeAppliedAutomaticallyToMediaSelectionGroup(_: AVMediaSelectionGroup) -> Bool](https://developer.apple.com/documentation/avfoundation/avmediaselection/1386716-mediaselectioncriteriacanbeappli)Added [AVMediaSelection.selectedMediaOptionInMediaSelectionGroup(_: AVMediaSelectionGroup) -> AVMediaSelectionOption?](https://developer.apple.com/documentation/avfoundation/avmediaselection/1389197-selectedmediaoptioninmediaselect)Added [AVMetadataGroup](https://developer.apple.com/documentation/avfoundation/avmetadatagroup)Added [AVMetadataGroup.items](https://developer.apple.com/documentation/avfoundation/avmetadatagroup/1389935-items)Added [AVMetadataItem.init(propertiesOfMetadataItem: AVMetadataItem, valueLoadingHandler: (AVMetadataItemValueRequest) -> Void)](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387745-metadataitemwithpropertiesofmeta)Added [AVMetadataItem.startDate](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1388535-startdate)Added [AVMetadataItemValueRequest](https://developer.apple.com/documentation/avfoundation/avmetadataitemvaluerequest)Added [AVMetadataItemValueRequest.metadataItem](https://developer.apple.com/documentation/avfoundation/avmetadataitemvaluerequest/1388069-metadataitem)Added [AVMetadataItemValueRequest.respondWithError(_: NSError)](https://developer.apple.com/documentation/avfoundation/avmetadataitemvaluerequest/1390783-respondwitherror)Added [AVMetadataItemValueRequest.respondWithValue(_: protocol<NSCopying, NSObjectProtocol>)](https://developer.apple.com/documentation/avfoundation/avmetadataitemvaluerequest/1386820-respond)Added [AVMusicSequenceLoadOptions [struct]](https://developer.apple.com/documentation/avfoundation/avmusicsequenceloadoptions)Added AVMusicSequenceLoadOptions.init(rawValue: UInt)Added [AVMusicSequenceLoadOptions.SMF_ChannelsToTracks](https://developer.apple.com/documentation/avfoundation/avmusicsequenceloadoptions/avmusicsequenceloadsmf_channelstotracks)Added [AVMusicSequenceLoadOptions.SMF_PreserveTracks](https://developer.apple.com/documentation/avfoundation/avmusicsequenceloadoptions/avmusicsequenceloadsmf_preservetracks)Added [AVMusicTrack](https://developer.apple.com/documentation/avfoundation/avmusictrack)Added [AVMusicTrack.destinationAudioUnit](https://developer.apple.com/documentation/avfoundation/avmusictrack/1390533-destinationaudiounit)Added [AVMusicTrack.destinationMIDIEndpoint](https://developer.apple.com/documentation/avfoundation/avmusictrack/1388828-destinationmidiendpoint)Added [AVMusicTrack.lengthInBeats](https://developer.apple.com/documentation/avfoundation/avmusictrack/1389910-lengthinbeats)Added [AVMusicTrack.lengthInSeconds](https://developer.apple.com/documentation/avfoundation/avmusictrack/1385749-lengthinseconds)Added [AVMusicTrack.loopingEnabled](https://developer.apple.com/documentation/avfoundation/avmusictrack/1385811-loopingenabled)Added [AVMusicTrack.loopRange](https://developer.apple.com/documentation/avfoundation/avmusictrack/1386292-looprange)Added [AVMusicTrack.muted](https://developer.apple.com/documentation/avfoundation/avmusictrack/1387694-muted)Added [AVMusicTrack.numberOfLoops](https://developer.apple.com/documentation/avfoundation/avmusictrack/1389268-numberofloops)Added [AVMusicTrack.offsetTime](https://developer.apple.com/documentation/avfoundation/avmusictrack/1386336-offsettime)Added [AVMusicTrack.soloed](https://developer.apple.com/documentation/avfoundation/avmusictrack/1387883-soloed)Added [AVMusicTrack.timeResolution](https://developer.apple.com/documentation/avfoundation/avmusictrack/1387198-timeresolution)Added [AVMusicTrackLoopCount [enum]](https://developer.apple.com/documentation/avfoundation/avmusictrackloopcount)Added [AVMusicTrackLoopCount.Forever](https://developer.apple.com/documentation/avfoundation/avmusictrackloopcount/forever)Added [AVMutableComposition.init(URLAssetInitializationOptions: [String : AnyObject]?)](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1390705-init)Added [AVMutableComposition.tracksWithMediaCharacteristic(_: String) -> [AVMutableCompositionTrack]](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1388464-trackswithmediacharacteristic)Added [AVMutableComposition.tracksWithMediaType(_: String) -> [AVMutableCompositionTrack]](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1385724-tracks)Added [AVMutableComposition.trackWithTrackID(_: CMPersistentTrackID) -> AVMutableCompositionTrack?](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1390074-trackwithtrackid)Added [AVMutableDateRangeMetadataGroup](https://developer.apple.com/documentation/avfoundation/avmutabledaterangemetadatagroup)Added [AVMutableDateRangeMetadataGroup.endDate](https://developer.apple.com/documentation/avfoundation/avmutabledaterangemetadatagroup/1387651-enddate)Added [AVMutableDateRangeMetadataGroup.items](https://developer.apple.com/documentation/avfoundation/avmutabledaterangemetadatagroup/1388262-items)Added [AVMutableDateRangeMetadataGroup.startDate](https://developer.apple.com/documentation/avfoundation/avmutabledaterangemetadatagroup/1390555-startdate)Added [AVMutableMediaSelection](https://developer.apple.com/documentation/avfoundation/avmutablemediaselection)Added [AVMutableMediaSelection.selectMediaOption(_: AVMediaSelectionOption?, inMediaSelectionGroup: AVMediaSelectionGroup)](https://developer.apple.com/documentation/avfoundation/avmutablemediaselection/1386768-selectmediaoption)Added [AVMutableMetadataItem.startDate](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1389966-startdate)Added [AVMutableVideoComposition.init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void)](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1387006-videocompositionwithasset)Added [AVPlayerItem.canUseNetworkResourcesForLiveStreamingWhilePaused](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388752-canusenetworkresourcesforlivestr)Added [AVPlayerItem.currentMediaSelection](https://developer.apple.com/documentation/avfoundation/avplayeritem/1386519-currentmediaselection)Added [AVPlayerLayer.pixelBufferAttributes](https://developer.apple.com/documentation/avfoundation/avplayerlayer/1390055-pixelbufferattributes)Added [AVSpeechSynthesisVoice.identifier](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619670-identifier)Added [AVSpeechSynthesisVoice.init(identifier: String)](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619711-voicewithidentifier)Added [AVSpeechSynthesisVoice.name](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619669-name)Added [AVSpeechSynthesisVoice.quality](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619688-quality)Added [AVSpeechSynthesisVoiceQuality [enum]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoicequality)Added [AVSpeechSynthesisVoiceQuality.Default](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoicequality/default)Added [AVSpeechSynthesisVoiceQuality.Enhanced](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoicequality/avspeechsynthesisvoicequalityenhanced)Added [AVVideoComposition.init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void)](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1389556-videocompositionwithasset)Added [AVAssetChapterMetadataGroupsDidChangeNotification](https://developer.apple.com/documentation/avfoundation/avassetchaptermetadatagroupsdidchangenotification)Added [AVAssetDownloadTaskMediaSelectionKey](https://developer.apple.com/documentation/avfoundation/avassetdownloadtaskmediaselectionkey)Added [AVAssetDownloadTaskMinimumRequiredMediaBitrateKey](https://developer.apple.com/documentation/avfoundation/avassetdownloadtaskminimumrequiredmediabitratekey)Added [AVAssetDurationDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1386249-avassetdurationdidchange)Added [AVAssetExportPreset3840x2160](https://developer.apple.com/documentation/avfoundation/avassetexportpreset3840x2160)Added [AVAssetMediaSelectionGroupsDidChangeNotification](https://developer.apple.com/documentation/avfoundation/avassetmediaselectiongroupsdidchangenotification)Added [AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey)Added [AVAssetTrackSegmentsDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1386848-avassettracksegmentsdidchange)Added [AVAssetTrackTimeRangeDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1385765-avassettracktimerangedidchange)Added [AVAssetTrackTrackAssociationsDidChangeNotification](https://developer.apple.com/documentation/avfoundation/avassettracktrackassociationsdidchangenotification)Added [AVAudioConverterInputBlock](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputblock)Added [AVAudioPacketCount](https://developer.apple.com/documentation/avfoundation/avaudiopacketcount)Added [AVAudioSessionModeSpokenAudio](https://developer.apple.com/documentation/avfoundation/avaudiosessionmodespokenaudio)Added [AVAudioUnitComponentTagsDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1387538-avaudiounitcomponenttagsdidchang)Added [AVAudioUnitManufacturerNameApple](https://developer.apple.com/documentation/avfoundation/avaudiounitmanufacturernameapple)Added [AVAudioUnitTypeEffect](https://developer.apple.com/documentation/avfoundation/avaudiounittypeeffect)Added [AVAudioUnitTypeFormatConverter](https://developer.apple.com/documentation/avfoundation/avaudiounittypeformatconverter)Added [AVAudioUnitTypeGenerator](https://developer.apple.com/documentation/avfoundation/avaudiounittypegenerator)Added [AVAudioUnitTypeMIDIProcessor](https://developer.apple.com/documentation/avfoundation/avaudiounittypemidiprocessor)Added [AVAudioUnitTypeMixer](https://developer.apple.com/documentation/avfoundation/avaudiounittypemixer)Added [AVAudioUnitTypeMusicDevice](https://developer.apple.com/documentation/avfoundation/avaudiounittypemusicdevice)Added [AVAudioUnitTypeMusicEffect](https://developer.apple.com/documentation/avfoundation/avaudiounittypemusiceffect)Added [AVAudioUnitTypeOfflineEffect](https://developer.apple.com/documentation/avfoundation/avaudiounittypeofflineeffect)Added [AVAudioUnitTypeOutput](https://developer.apple.com/documentation/avfoundation/avaudiounittypeoutput)Added [AVAudioUnitTypePanner](https://developer.apple.com/documentation/avfoundation/avaudiounittypepanner)Added [AVBeatRange](https://developer.apple.com/documentation/avfoundation/avbeatrange)Added [AVCaptureSessionInterruptionReasonKey](https://developer.apple.com/documentation/avfoundation/avcapturesessioninterruptionreasonkey)Added [AVCaptureSessionPreset3840x2160](https://developer.apple.com/documentation/avfoundation/avcapturesession/preset/1620474-hd4k3840x2160)Added [AVFileTypeEnhancedAC3](https://developer.apple.com/documentation/avfoundation/avfiletype/1387645-eac3)Added [AVMakeBeatRange(_: AVMusicTimeStamp, _: AVMusicTimeStamp) -> AVBeatRange](https://developer.apple.com/documentation/avfoundation/1386774-avmakebeatrange)Added [AVMediaCharacteristicDubbedTranslation](https://developer.apple.com/documentation/avfoundation/avmediacharacteristicdubbedtranslation)Added [AVMediaCharacteristicLanguageTranslation](https://developer.apple.com/documentation/avfoundation/avmediacharacteristiclanguagetranslation)Added [AVMediaCharacteristicVoiceOverTranslation](https://developer.apple.com/documentation/avfoundation/avmediacharacteristicvoiceovertranslation)Added [AVMediaTypeMetadataObject](https://developer.apple.com/documentation/avfoundation/avmediatype/1621241-metadataobject)Added [AVMetadataExtraAttributeInfoKey](https://developer.apple.com/documentation/avfoundation/avmetadataextraattributeinfokey)Added [AVMetadataID3MetadataKeyCommercial](https://developer.apple.com/documentation/avfoundation/avmetadataid3metadatakeycommercial)Added [AVMetadataIdentifierID3MetadataCommercial](https://developer.apple.com/documentation/avfoundation/avmetadataidentifier/1389685-id3metadatacommercial)Added [AVMetadataIdentifierQuickTimeMetadataContentIdentifier](https://developer.apple.com/documentation/avfoundation/avmetadataidentifier/1387194-quicktimemetadatacontentidentifi)Added [AVMetadataIdentifierQuickTimeMetadataDetectedFace](https://developer.apple.com/documentation/avfoundation/avmetadataidentifierquicktimemetadatadetectedface)Added [AVMetadataIdentifierQuickTimeMetadataVideoOrientation](https://developer.apple.com/documentation/avfoundation/avmetadataidentifierquicktimemetadatavideoorientation)Added [AVMetadataQuickTimeMetadataKeyContentIdentifier](https://developer.apple.com/documentation/avfoundation/avmetadataquicktimemetadatakeycontentidentifier)Added [AVMusicTimeStamp](https://developer.apple.com/documentation/avfoundation/avmusictimestamp)Added [AVOutputSettingsPreset3840x2160](https://developer.apple.com/documentation/avfoundation/avoutputsettingspreset3840x2160)Added [AVSpeechSynthesisVoiceIdentifierAlex](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoiceidentifieralex)Added [AVStreamingKeyDeliveryContentKeyType](https://developer.apple.com/documentation/avfoundation/avstreamingkeydeliverycontentkeytype)Added [AVStreamingKeyDeliveryPersistentContentKeyType](https://developer.apple.com/documentation/avfoundation/avstreamingkeydeliverypersistentcontentkeytype)Modified [AVAsset](https://developer.apple.com/documentation/avfoundation/avasset)

|  | Declaration |
| --- | --- |
| From | ``` class AVAsset : NSObject, NSCopying, AVAsynchronousKeyValueLoading {     class func assetWithURL(_ URL: NSURL!) -> AnyObject!     var duration: CMTime { get }     var preferredRate: Float { get }     var preferredVolume: Float { get }     var preferredTransform: CGAffineTransform { get }     var naturalSize: CGSize { get } } extension AVAsset {     var providesPreciseDurationAndTiming: Bool { get }     func cancelLoading() } extension AVAsset {     var referenceRestrictions: AVAssetReferenceRestrictions { get } } extension AVAsset {     var tracks: [AnyObject]! { get }     func trackWithTrackID(_ trackID: CMPersistentTrackID) -> AVAssetTrack!     func tracksWithMediaType(_ mediaType: String!) -> [AnyObject]!     func tracksWithMediaCharacteristic(_ mediaCharacteristic: String!) -> [AnyObject]!     var trackGroups: [AnyObject]! { get } } extension AVAsset {     var creationDate: AVMetadataItem! { get }     var lyrics: String! { get }     var commonMetadata: [AnyObject]! { get }     var metadata: [AnyObject]! { get }     var availableMetadataFormats: [AnyObject]! { get }     func metadataForFormat(_ format: String!) -> [AnyObject]! } extension AVAsset {     var availableChapterLocales: [AnyObject]! { get }     func chapterMetadataGroupsWithTitleLocale(_ locale: NSLocale!, containingItemsWithCommonKeys commonKeys: [AnyObject]!) -> [AnyObject]!     func chapterMetadataGroupsBestMatchingPreferredLanguages(_ preferredLanguages: [AnyObject]!) -> [AnyObject]! } extension AVAsset {     var availableMediaCharacteristicsWithMediaSelectionOptions: [AnyObject]! { get }     func mediaSelectionGroupForMediaCharacteristic(_ mediaCharacteristic: String!) -> AVMediaSelectionGroup! } extension AVAsset {     var hasProtectedContent: Bool { get } } extension AVAsset {     var playable: Bool { get }     var exportable: Bool { get }     var readable: Bool { get }     var composable: Bool { get }     var compatibleWithSavedPhotosAlbum: Bool { get } } extension AVAsset {     func unusedTrackID() -> CMPersistentTrackID } ``` |
| To | ``` class AVAsset : NSObject, NSCopying, AVAsynchronousKeyValueLoading {     convenience init(URL URL: NSURL)     class func assetWithURL(_ URL: NSURL) -> Self     var duration: CMTime { get }     var preferredRate: Float { get }     var preferredVolume: Float { get }     var preferredTransform: CGAffineTransform { get }     var naturalSize: CGSize { get } } extension AVAsset {     var providesPreciseDurationAndTiming: Bool { get }     func cancelLoading() } extension AVAsset {     var referenceRestrictions: AVAssetReferenceRestrictions { get } } extension AVAsset {     var tracks: [AVAssetTrack] { get }     func trackWithTrackID(_ trackID: CMPersistentTrackID) -> AVAssetTrack?     func tracksWithMediaType(_ mediaType: String) -> [AVAssetTrack]     func tracksWithMediaCharacteristic(_ mediaCharacteristic: String) -> [AVAssetTrack]     var trackGroups: [AVAssetTrackGroup] { get } } extension AVAsset {     var creationDate: AVMetadataItem? { get }     var lyrics: String? { get }     var commonMetadata: [AVMetadataItem] { get }     var metadata: [AVMetadataItem] { get }     var availableMetadataFormats: [String] { get }     func metadataForFormat(_ format: String) -> [AVMetadataItem] } extension AVAsset {     var availableChapterLocales: [NSLocale] { get }     func chapterMetadataGroupsWithTitleLocale(_ locale: NSLocale, containingItemsWithCommonKeys commonKeys: [String]?) -> [AVTimedMetadataGroup]     func chapterMetadataGroupsBestMatchingPreferredLanguages(_ preferredLanguages: [String]) -> [AVTimedMetadataGroup] } extension AVAsset {     var availableMediaCharacteristicsWithMediaSelectionOptions: [String] { get }     func mediaSelectionGroupForMediaCharacteristic(_ mediaCharacteristic: String) -> AVMediaSelectionGroup?     var preferredMediaSelection: AVMediaSelection { get } } extension AVAsset {     var hasProtectedContent: Bool { get } } extension AVAsset {     var canContainFragments: Bool { get }     var containsFragments: Bool { get } } extension AVAsset {     var playable: Bool { get }     var exportable: Bool { get }     var readable: Bool { get }     var composable: Bool { get }     var compatibleWithSavedPhotosAlbum: Bool { get }     var compatibleWithAirPlayVideo: Bool { get } } extension AVAsset {     func unusedTrackID() -> CMPersistentTrackID } ``` |

Modified [AVAsset.availableChapterLocales](https://developer.apple.com/documentation/avfoundation/avasset/1388228-availablechapterlocales)

|  | Declaration |
| --- | --- |
| From | ``` var availableChapterLocales: [AnyObject]! { get } ``` |
| To | ``` var availableChapterLocales: [NSLocale] { get } ``` |

Modified [AVAsset.availableMediaCharacteristicsWithMediaSelectionOptions](https://developer.apple.com/documentation/avfoundation/avasset/1389433-availablemediacharacteristicswit)

|  | Declaration |
| --- | --- |
| From | ``` var availableMediaCharacteristicsWithMediaSelectionOptions: [AnyObject]! { get } ``` |
| To | ``` var availableMediaCharacteristicsWithMediaSelectionOptions: [String] { get } ``` |

Modified [AVAsset.availableMetadataFormats](https://developer.apple.com/documentation/avfoundation/avasset/1385823-availablemetadataformats)

|  | Declaration |
| --- | --- |
| From | ``` var availableMetadataFormats: [AnyObject]! { get } ``` |
| To | ``` var availableMetadataFormats: [String] { get } ``` |

Modified [AVAsset.chapterMetadataGroupsBestMatchingPreferredLanguages(_: [String]) -> [AVTimedMetadataGroup]](https://developer.apple.com/documentation/avfoundation/avasset/1390909-chaptermetadatagroupsbestmatchin)

|  | Declaration |
| --- | --- |
| From | ``` func chapterMetadataGroupsBestMatchingPreferredLanguages(_ preferredLanguages: [AnyObject]!) -> [AnyObject]! ``` |
| To | ``` func chapterMetadataGroupsBestMatchingPreferredLanguages(_ preferredLanguages: [String]) -> [AVTimedMetadataGroup] ``` |

Modified [AVAsset.chapterMetadataGroupsWithTitleLocale(_: NSLocale, containingItemsWithCommonKeys: [String]?) -> [AVTimedMetadataGroup]](https://developer.apple.com/documentation/avfoundation/avasset/1388966-chaptermetadatagroupswithtitlelo)

|  | Declaration |
| --- | --- |
| From | ``` func chapterMetadataGroupsWithTitleLocale(_ locale: NSLocale!, containingItemsWithCommonKeys commonKeys: [AnyObject]!) -> [AnyObject]! ``` |
| To | ``` func chapterMetadataGroupsWithTitleLocale(_ locale: NSLocale, containingItemsWithCommonKeys commonKeys: [String]?) -> [AVTimedMetadataGroup] ``` |

Modified [AVAsset.commonMetadata](https://developer.apple.com/documentation/avfoundation/avasset/1390498-commonmetadata)

|  | Declaration |
| --- | --- |
| From | ``` var commonMetadata: [AnyObject]! { get } ``` |
| To | ``` var commonMetadata: [AVMetadataItem] { get } ``` |

Modified [AVAsset.creationDate](https://developer.apple.com/documentation/avfoundation/avasset/1386342-creationdate)

|  | Declaration |
| --- | --- |
| From | ``` var creationDate: AVMetadataItem! { get } ``` |
| To | ``` var creationDate: AVMetadataItem? { get } ``` |

Modified [AVAsset.init(URL: NSURL)](https://developer.apple.com/documentation/avfoundation/avasset/1389943-assetwithurl)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | assetWithURL(_:) | ``` class func assetWithURL(_ URL: NSURL!) -> AnyObject! ``` | iOS 8.0 |
| To | init(URL:) | ``` convenience init(URL URL: NSURL) ``` | iOS 9.0 |

Modified [AVAsset.lyrics](https://developer.apple.com/documentation/avfoundation/avasset/1388104-lyrics)

|  | Declaration |
| --- | --- |
| From | ``` var lyrics: String! { get } ``` |
| To | ``` var lyrics: String? { get } ``` |

Modified [AVAsset.mediaSelectionGroupForMediaCharacteristic(_: String) -> AVMediaSelectionGroup?](https://developer.apple.com/documentation/avfoundation/avasset/1387496-mediaselectiongroupformediachara)

|  | Declaration |
| --- | --- |
| From | ``` func mediaSelectionGroupForMediaCharacteristic(_ mediaCharacteristic: String!) -> AVMediaSelectionGroup! ``` |
| To | ``` func mediaSelectionGroupForMediaCharacteristic(_ mediaCharacteristic: String) -> AVMediaSelectionGroup? ``` |

Modified [AVAsset.metadata](https://developer.apple.com/documentation/avfoundation/avasset/1386884-metadata)

|  | Declaration |
| --- | --- |
| From | ``` var metadata: [AnyObject]! { get } ``` |
| To | ``` var metadata: [AVMetadataItem] { get } ``` |

Modified [AVAsset.metadataForFormat(_: String) -> [AVMetadataItem]](https://developer.apple.com/documentation/avfoundation/avasset/1387759-metadata)

|  | Declaration |
| --- | --- |
| From | ``` func metadataForFormat(_ format: String!) -> [AnyObject]! ``` |
| To | ``` func metadataForFormat(_ format: String) -> [AVMetadataItem] ``` |

Modified [AVAsset.trackGroups](https://developer.apple.com/documentation/avfoundation/avasset/1390697-trackgroups)

|  | Declaration |
| --- | --- |
| From | ``` var trackGroups: [AnyObject]! { get } ``` |
| To | ``` var trackGroups: [AVAssetTrackGroup] { get } ``` |

Modified [AVAsset.tracks](https://developer.apple.com/documentation/avfoundation/avasset/1387953-tracks)

|  | Declaration |
| --- | --- |
| From | ``` var tracks: [AnyObject]! { get } ``` |
| To | ``` var tracks: [AVAssetTrack] { get } ``` |

Modified [AVAsset.tracksWithMediaCharacteristic(_: String) -> [AVAssetTrack]](https://developer.apple.com/documentation/avfoundation/avasset/1389554-trackswithmediacharacteristic)

|  | Declaration |
| --- | --- |
| From | ``` func tracksWithMediaCharacteristic(_ mediaCharacteristic: String!) -> [AnyObject]! ``` |
| To | ``` func tracksWithMediaCharacteristic(_ mediaCharacteristic: String) -> [AVAssetTrack] ``` |

Modified [AVAsset.tracksWithMediaType(_: String) -> [AVAssetTrack]](https://developer.apple.com/documentation/avfoundation/avasset/1387140-trackswithmediatype)

|  | Declaration |
| --- | --- |
| From | ``` func tracksWithMediaType(_ mediaType: String!) -> [AnyObject]! ``` |
| To | ``` func tracksWithMediaType(_ mediaType: String) -> [AVAssetTrack] ``` |

Modified [AVAsset.trackWithTrackID(_: CMPersistentTrackID) -> AVAssetTrack?](https://developer.apple.com/documentation/avfoundation/avasset/1390145-track)

|  | Declaration |
| --- | --- |
| From | ``` func trackWithTrackID(_ trackID: CMPersistentTrackID) -> AVAssetTrack! ``` |
| To | ``` func trackWithTrackID(_ trackID: CMPersistentTrackID) -> AVAssetTrack? ``` |

Modified [AVAssetExportSession](https://developer.apple.com/documentation/avfoundation/avassetexportsession)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetExportSession : NSObject {     class func allExportPresets() -> [AnyObject]!     class func exportPresetsCompatibleWithAsset(_ asset: AVAsset!) -> [AnyObject]!     class func determineCompatibilityOfExportPreset(_ presetName: String!, withAsset asset: AVAsset!, outputFileType outputFileType: String!, completionHandler handler: ((Bool) -> Void)!)     init!(asset asset: AVAsset!, presetName presetName: String!) -> AVAssetExportSession     class func exportSessionWithAsset(_ asset: AVAsset!, presetName presetName: String!) -> AVAssetExportSession!     init!(asset asset: AVAsset!, presetName presetName: String!)     var presetName: String! { get }     var asset: AVAsset! { get }     var supportedFileTypes: [AnyObject]! { get }     var outputFileType: String!     @NSCopying var outputURL: NSURL!     var status: AVAssetExportSessionStatus { get }     var error: NSError! { get }     var progress: Float { get }     var maxDuration: CMTime { get }     var estimatedOutputFileLength: Int64 { get }     var timeRange: CMTimeRange     var metadata: [AnyObject]!     var metadataItemFilter: AVMetadataItemFilter!     var fileLengthLimit: Int64     var audioTimePitchAlgorithm: String!     @NSCopying var audioMix: AVAudioMix!     @NSCopying var videoComposition: AVVideoComposition!     var customVideoCompositor: AVVideoCompositing! { get }     var shouldOptimizeForNetworkUse: Bool     var canPerformMultiplePassesOverSourceMediaData: Bool     @NSCopying var directoryForTemporaryFiles: NSURL!     func determineCompatibleFileTypesWithCompletionHandler(_ handler: (([AnyObject]!) -> Void)!)     func exportAsynchronouslyWithCompletionHandler(_ handler: (() -> Void)!)     func cancelExport() } ``` |
| To | ``` class AVAssetExportSession : NSObject {     convenience init()     convenience init?(asset asset: AVAsset, presetName presetName: String)     class func exportSessionWithAsset(_ asset: AVAsset, presetName presetName: String) -> Self?     init?(asset asset: AVAsset, presetName presetName: String)     var presetName: String { get }     var asset: AVAsset { get }     var outputFileType: String?     @NSCopying var outputURL: NSURL?     var shouldOptimizeForNetworkUse: Bool     var status: AVAssetExportSessionStatus { get }     var error: NSError? { get }     func exportAsynchronouslyWithCompletionHandler(_ handler: () -> Void)     var progress: Float { get }     func cancelExport() } extension AVAssetExportSession {     class func allExportPresets() -> [String]     class func exportPresetsCompatibleWithAsset(_ asset: AVAsset) -> [String]     class func determineCompatibilityOfExportPreset(_ presetName: String, withAsset asset: AVAsset, outputFileType outputFileType: String?, completionHandler handler: (Bool) -> Void) } extension AVAssetExportSession {     var supportedFileTypes: [String] { get }     func determineCompatibleFileTypesWithCompletionHandler(_ handler: ([String]) -> Void) } extension AVAssetExportSession {     var timeRange: CMTimeRange     var maxDuration: CMTime { get }     var estimatedOutputFileLength: Int64 { get }     var fileLengthLimit: Int64 } extension AVAssetExportSession {     var metadata: [AVMetadataItem]?     var metadataItemFilter: AVMetadataItemFilter? } extension AVAssetExportSession {     var audioTimePitchAlgorithm: String     @NSCopying var audioMix: AVAudioMix?     @NSCopying var videoComposition: AVVideoComposition?     var customVideoCompositor: AVVideoCompositing? { get } } extension AVAssetExportSession {     var canPerformMultiplePassesOverSourceMediaData: Bool     @NSCopying var directoryForTemporaryFiles: NSURL? } ``` |

Modified [AVAssetExportSession.allExportPresets() -> [String] [class]](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1387150-allexportpresets)

|  | Declaration |
| --- | --- |
| From | ``` class func allExportPresets() -> [AnyObject]! ``` |
| To | ``` class func allExportPresets() -> [String] ``` |

Modified [AVAssetExportSession.asset](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1385690-asset)

|  | Declaration |
| --- | --- |
| From | ``` var asset: AVAsset! { get } ``` |
| To | ``` var asset: AVAsset { get } ``` |

Modified [AVAssetExportSession.audioMix](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1388155-audiomix)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var audioMix: AVAudioMix! ``` |
| To | ``` @NSCopying var audioMix: AVAudioMix? ``` |

Modified [AVAssetExportSession.audioTimePitchAlgorithm](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1385835-audiotimepitchalgorithm)

|  | Declaration |
| --- | --- |
| From | ``` var audioTimePitchAlgorithm: String! ``` |
| To | ``` var audioTimePitchAlgorithm: String ``` |

Modified [AVAssetExportSession.customVideoCompositor](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1388288-customvideocompositor)

|  | Declaration |
| --- | --- |
| From | ``` var customVideoCompositor: AVVideoCompositing! { get } ``` |
| To | ``` var customVideoCompositor: AVVideoCompositing? { get } ``` |

Modified [AVAssetExportSession.determineCompatibilityOfExportPreset(_: String, withAsset: AVAsset, outputFileType: String?, completionHandler: (Bool) -> Void) [class]](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1385821-determinecompatibilityofexportpr)

|  | Declaration |
| --- | --- |
| From | ``` class func determineCompatibilityOfExportPreset(_ presetName: String!, withAsset asset: AVAsset!, outputFileType outputFileType: String!, completionHandler handler: ((Bool) -> Void)!) ``` |
| To | ``` class func determineCompatibilityOfExportPreset(_ presetName: String, withAsset asset: AVAsset, outputFileType outputFileType: String?, completionHandler handler: (Bool) -> Void) ``` |

Modified [AVAssetExportSession.determineCompatibleFileTypesWithCompletionHandler(_: ([String]) -> Void)](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1387907-determinecompatiblefiletypes)

|  | Declaration |
| --- | --- |
| From | ``` func determineCompatibleFileTypesWithCompletionHandler(_ handler: (([AnyObject]!) -> Void)!) ``` |
| To | ``` func determineCompatibleFileTypesWithCompletionHandler(_ handler: ([String]) -> Void) ``` |

Modified [AVAssetExportSession.directoryForTemporaryFiles](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1388699-directoryfortemporaryfiles)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var directoryForTemporaryFiles: NSURL! ``` |
| To | ``` @NSCopying var directoryForTemporaryFiles: NSURL? ``` |

Modified [AVAssetExportSession.error](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1385936-error)

|  | Declaration |
| --- | --- |
| From | ``` var error: NSError! { get } ``` |
| To | ``` var error: NSError? { get } ``` |

Modified [AVAssetExportSession.exportAsynchronouslyWithCompletionHandler(_: () -> Void)](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1388005-exportasynchronouslywithcompleti)

|  | Declaration |
| --- | --- |
| From | ``` func exportAsynchronouslyWithCompletionHandler(_ handler: (() -> Void)!) ``` |
| To | ``` func exportAsynchronouslyWithCompletionHandler(_ handler: () -> Void) ``` |

Modified [AVAssetExportSession.exportPresetsCompatibleWithAsset(_: AVAsset) -> [String] [class]](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1390567-exportpresetscompatiblewithasset)

|  | Declaration |
| --- | --- |
| From | ``` class func exportPresetsCompatibleWithAsset(_ asset: AVAsset!) -> [AnyObject]! ``` |
| To | ``` class func exportPresetsCompatibleWithAsset(_ asset: AVAsset) -> [String] ``` |

Modified [AVAssetExportSession.fileLengthLimit](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1622333-filelengthlimit)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified [AVAssetExportSession.init(asset: AVAsset, presetName: String)](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1389367-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(asset asset: AVAsset!, presetName presetName: String!) ``` |
| To | ``` init?(asset asset: AVAsset, presetName presetName: String) ``` |

Modified [AVAssetExportSession.maxDuration](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1622332-maxduration)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified [AVAssetExportSession.metadata](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1390453-metadata)

|  | Declaration |
| --- | --- |
| From | ``` var metadata: [AnyObject]! ``` |
| To | ``` var metadata: [AVMetadataItem]? ``` |

Modified [AVAssetExportSession.metadataItemFilter](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1390226-metadataitemfilter)

|  | Declaration |
| --- | --- |
| From | ``` var metadataItemFilter: AVMetadataItemFilter! ``` |
| To | ``` var metadataItemFilter: AVMetadataItemFilter? ``` |

Modified [AVAssetExportSession.outputFileType](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1387110-outputfiletype)

|  | Declaration |
| --- | --- |
| From | ``` var outputFileType: String! ``` |
| To | ``` var outputFileType: String? ``` |

Modified [AVAssetExportSession.outputURL](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1389970-outputurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var outputURL: NSURL! ``` |
| To | ``` @NSCopying var outputURL: NSURL? ``` |

Modified [AVAssetExportSession.presetName](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1390467-presetname)

|  | Declaration |
| --- | --- |
| From | ``` var presetName: String! { get } ``` |
| To | ``` var presetName: String { get } ``` |

Modified [AVAssetExportSession.supportedFileTypes](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1388762-supportedfiletypes)

|  | Declaration |
| --- | --- |
| From | ``` var supportedFileTypes: [AnyObject]! { get } ``` |
| To | ``` var supportedFileTypes: [String] { get } ``` |

Modified [AVAssetExportSession.videoComposition](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1389477-videocomposition)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var videoComposition: AVVideoComposition! ``` |
| To | ``` @NSCopying var videoComposition: AVVideoComposition? ``` |

Modified [AVAssetExportSessionStatus [enum]](https://developer.apple.com/documentation/avfoundation/avassetexportsession/status)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVAssetImageGenerator](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetImageGenerator : NSObject {     var asset: AVAsset! { get }     var appliesPreferredTrackTransform: Bool     var maximumSize: CGSize     var apertureMode: String!     @NSCopying var videoComposition: AVVideoComposition!     var customVideoCompositor: AVVideoCompositing! { get }     var requestedTimeToleranceBefore: CMTime     var requestedTimeToleranceAfter: CMTime     init!(asset asset: AVAsset!) -> AVAssetImageGenerator     class func assetImageGeneratorWithAsset(_ asset: AVAsset!) -> AVAssetImageGenerator!     init!(asset asset: AVAsset!)     func copyCGImageAtTime(_ requestedTime: CMTime, actualTime actualTime: UnsafeMutablePointer<CMTime>, error outError: NSErrorPointer) -> CGImage!     func generateCGImagesAsynchronouslyForTimes(_ requestedTimes: [AnyObject]!, completionHandler handler: AVAssetImageGeneratorCompletionHandler!)     func cancelAllCGImageGeneration() } ``` |
| To | ``` class AVAssetImageGenerator : NSObject {     convenience init()     var asset: AVAsset { get }     var appliesPreferredTrackTransform: Bool     var maximumSize: CGSize     var apertureMode: String?     @NSCopying var videoComposition: AVVideoComposition?     var customVideoCompositor: AVVideoCompositing? { get }     var requestedTimeToleranceBefore: CMTime     var requestedTimeToleranceAfter: CMTime     convenience init(asset asset: AVAsset)     class func assetImageGeneratorWithAsset(_ asset: AVAsset) -> Self     init(asset asset: AVAsset)     func copyCGImageAtTime(_ requestedTime: CMTime, actualTime actualTime: UnsafeMutablePointer<CMTime>) throws -> CGImage     func generateCGImagesAsynchronouslyForTimes(_ requestedTimes: [NSValue], completionHandler handler: AVAssetImageGeneratorCompletionHandler)     func cancelAllCGImageGeneration() } ``` |

Modified [AVAssetImageGenerator.apertureMode](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1389314-aperturemode)

|  | Declaration |
| --- | --- |
| From | ``` var apertureMode: String! ``` |
| To | ``` var apertureMode: String? ``` |

Modified [AVAssetImageGenerator.asset](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1390689-asset)

|  | Declaration |
| --- | --- |
| From | ``` var asset: AVAsset! { get } ``` |
| To | ``` var asset: AVAsset { get } ``` |

Modified [AVAssetImageGenerator.copyCGImageAtTime(_: CMTime, actualTime: UnsafeMutablePointer<CMTime>) throws -> CGImage](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1387303-copycgimageattime)

|  | Declaration |
| --- | --- |
| From | ``` func copyCGImageAtTime(_ requestedTime: CMTime, actualTime actualTime: UnsafeMutablePointer<CMTime>, error outError: NSErrorPointer) -> CGImage! ``` |
| To | ``` func copyCGImageAtTime(_ requestedTime: CMTime, actualTime actualTime: UnsafeMutablePointer<CMTime>) throws -> CGImage ``` |

Modified [AVAssetImageGenerator.customVideoCompositor](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1386469-customvideocompositor)

|  | Declaration |
| --- | --- |
| From | ``` var customVideoCompositor: AVVideoCompositing! { get } ``` |
| To | ``` var customVideoCompositor: AVVideoCompositing? { get } ``` |

Modified [AVAssetImageGenerator.generateCGImagesAsynchronouslyForTimes(_: [NSValue], completionHandler: AVAssetImageGeneratorCompletionHandler)](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1388100-generatecgimagesasynchronouslyfo)

|  | Declaration |
| --- | --- |
| From | ``` func generateCGImagesAsynchronouslyForTimes(_ requestedTimes: [AnyObject]!, completionHandler handler: AVAssetImageGeneratorCompletionHandler!) ``` |
| To | ``` func generateCGImagesAsynchronouslyForTimes(_ requestedTimes: [NSValue], completionHandler handler: AVAssetImageGeneratorCompletionHandler) ``` |

Modified [AVAssetImageGenerator.init(asset: AVAsset)](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1387855-initwithasset)

|  | Declaration |
| --- | --- |
| From | ``` init!(asset asset: AVAsset!) ``` |
| To | ``` init(asset asset: AVAsset) ``` |

Modified [AVAssetImageGenerator.videoComposition](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1390189-videocomposition)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var videoComposition: AVVideoComposition! ``` |
| To | ``` @NSCopying var videoComposition: AVVideoComposition? ``` |

Modified [AVAssetImageGeneratorResult [enum]](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/result)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVAssetReader](https://developer.apple.com/documentation/avfoundation/avassetreader)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetReader : NSObject {     convenience init!(asset asset: AVAsset!, error outError: NSErrorPointer)     class func assetReaderWithAsset(_ asset: AVAsset!, error outError: NSErrorPointer) -> Self!     init!(asset asset: AVAsset!, error outError: NSErrorPointer)     var asset: AVAsset! { get }     var status: AVAssetReaderStatus { get }     var error: NSError! { get }     var timeRange: CMTimeRange     var outputs: [AnyObject]! { get }     func canAddOutput(_ output: AVAssetReaderOutput!) -> Bool     func addOutput(_ output: AVAssetReaderOutput!)     func startReading() -> Bool     func cancelReading() } ``` |
| To | ``` class AVAssetReader : NSObject {     convenience init()     convenience init(asset asset: AVAsset) throws     class func assetReaderWithAsset(_ asset: AVAsset) throws -> Self     init(asset asset: AVAsset) throws     var asset: AVAsset { get }     var status: AVAssetReaderStatus { get }     var error: NSError? { get }     var timeRange: CMTimeRange     var outputs: [AVAssetReaderOutput] { get }     func canAddOutput(_ output: AVAssetReaderOutput) -> Bool     func addOutput(_ output: AVAssetReaderOutput)     func startReading() -> Bool     func cancelReading() } ``` |

Modified [AVAssetReader.addOutput(_: AVAssetReaderOutput)](https://developer.apple.com/documentation/avfoundation/avassetreader/1390110-addoutput)

|  | Declaration |
| --- | --- |
| From | ``` func addOutput(_ output: AVAssetReaderOutput!) ``` |
| To | ``` func addOutput(_ output: AVAssetReaderOutput) ``` |

Modified [AVAssetReader.asset](https://developer.apple.com/documentation/avfoundation/avassetreader/1389128-asset)

|  | Declaration |
| --- | --- |
| From | ``` var asset: AVAsset! { get } ``` |
| To | ``` var asset: AVAsset { get } ``` |

Modified [AVAssetReader.canAddOutput(_: AVAssetReaderOutput) -> Bool](https://developer.apple.com/documentation/avfoundation/avassetreader/1387485-canadd)

|  | Declaration |
| --- | --- |
| From | ``` func canAddOutput(_ output: AVAssetReaderOutput!) -> Bool ``` |
| To | ``` func canAddOutput(_ output: AVAssetReaderOutput) -> Bool ``` |

Modified [AVAssetReader.error](https://developer.apple.com/documentation/avfoundation/avassetreader/1388114-error)

|  | Declaration |
| --- | --- |
| From | ``` var error: NSError! { get } ``` |
| To | ``` var error: NSError? { get } ``` |

Modified [AVAssetReader.init(asset: AVAsset) throws](https://developer.apple.com/documentation/avfoundation/avassetreader/1385593-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(asset asset: AVAsset!, error outError: NSErrorPointer) ``` |
| To | ``` init(asset asset: AVAsset) throws ``` |

Modified [AVAssetReader.outputs](https://developer.apple.com/documentation/avfoundation/avassetreader/1387132-outputs)

|  | Declaration |
| --- | --- |
| From | ``` var outputs: [AnyObject]! { get } ``` |
| To | ``` var outputs: [AVAssetReaderOutput] { get } ``` |

Modified [AVAssetReaderAudioMixOutput](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetReaderAudioMixOutput : AVAssetReaderOutput {     convenience init!(audioTracks audioTracks: [AnyObject]!, audioSettings audioSettings: [NSObject : AnyObject]!)     class func assetReaderAudioMixOutputWithAudioTracks(_ audioTracks: [AnyObject]!, audioSettings audioSettings: [NSObject : AnyObject]!) -> Self!     init!(audioTracks audioTracks: [AnyObject]!, audioSettings audioSettings: [NSObject : AnyObject]!)     var audioTracks: [AnyObject]! { get }     var audioSettings: [NSObject : AnyObject]! { get }     @NSCopying var audioMix: AVAudioMix!     var audioTimePitchAlgorithm: String! } ``` |
| To | ``` class AVAssetReaderAudioMixOutput : AVAssetReaderOutput {     convenience init()     convenience init(audioTracks audioTracks: [AVAssetTrack], audioSettings audioSettings: [String : AnyObject]?)     class func assetReaderAudioMixOutputWithAudioTracks(_ audioTracks: [AVAssetTrack], audioSettings audioSettings: [String : AnyObject]?) -> Self     init(audioTracks audioTracks: [AVAssetTrack], audioSettings audioSettings: [String : AnyObject]?)     var audioTracks: [AVAssetTrack] { get }     var audioSettings: [String : AnyObject]? { get }     @NSCopying var audioMix: AVAudioMix?     var audioTimePitchAlgorithm: String } ``` |

Modified [AVAssetReaderAudioMixOutput.audioMix](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/1387074-audiomix)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var audioMix: AVAudioMix! ``` |
| To | ``` @NSCopying var audioMix: AVAudioMix? ``` |

Modified [AVAssetReaderAudioMixOutput.audioSettings](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/1388860-audiosettings)

|  | Declaration |
| --- | --- |
| From | ``` var audioSettings: [NSObject : AnyObject]! { get } ``` |
| To | ``` var audioSettings: [String : AnyObject]? { get } ``` |

Modified [AVAssetReaderAudioMixOutput.audioTimePitchAlgorithm](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/1388713-audiotimepitchalgorithm)

|  | Declaration |
| --- | --- |
| From | ``` var audioTimePitchAlgorithm: String! ``` |
| To | ``` var audioTimePitchAlgorithm: String ``` |

Modified [AVAssetReaderAudioMixOutput.audioTracks](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/1385635-audiotracks)

|  | Declaration |
| --- | --- |
| From | ``` var audioTracks: [AnyObject]! { get } ``` |
| To | ``` var audioTracks: [AVAssetTrack] { get } ``` |

Modified [AVAssetReaderAudioMixOutput.init(audioTracks: [AVAssetTrack], audioSettings: [String : AnyObject]?)](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/1388883-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(audioTracks audioTracks: [AnyObject]!, audioSettings audioSettings: [NSObject : AnyObject]!) ``` |
| To | ``` init(audioTracks audioTracks: [AVAssetTrack], audioSettings audioSettings: [String : AnyObject]?) ``` |

Modified [AVAssetReaderOutput](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetReaderOutput : NSObject {     var mediaType: String! { get }     var alwaysCopiesSampleData: Bool     func copyNextSampleBuffer() -> CMSampleBuffer! } extension AVAssetReaderOutput {     var supportsRandomAccess: Bool     func resetForReadingTimeRanges(_ timeRanges: [AnyObject]!)     func markConfigurationAsFinal() } ``` |
| To | ``` class AVAssetReaderOutput : NSObject {     var mediaType: String { get }     var alwaysCopiesSampleData: Bool     func copyNextSampleBuffer() -> CMSampleBuffer? } extension AVAssetReaderOutput {     var supportsRandomAccess: Bool     func resetForReadingTimeRanges(_ timeRanges: [NSValue])     func markConfigurationAsFinal() } ``` |

Modified [AVAssetReaderOutput.copyNextSampleBuffer() -> CMSampleBuffer?](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/1385732-copynextsamplebuffer)

|  | Declaration |
| --- | --- |
| From | ``` func copyNextSampleBuffer() -> CMSampleBuffer! ``` |
| To | ``` func copyNextSampleBuffer() -> CMSampleBuffer? ``` |

Modified [AVAssetReaderOutput.mediaType](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/1390880-mediatype)

|  | Declaration |
| --- | --- |
| From | ``` var mediaType: String! { get } ``` |
| To | ``` var mediaType: String { get } ``` |

Modified [AVAssetReaderOutput.resetForReadingTimeRanges(_: [NSValue])](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/1388890-reset)

|  | Declaration |
| --- | --- |
| From | ``` func resetForReadingTimeRanges(_ timeRanges: [AnyObject]!) ``` |
| To | ``` func resetForReadingTimeRanges(_ timeRanges: [NSValue]) ``` |

Modified [AVAssetReaderOutputMetadataAdaptor](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputmetadataadaptor)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetReaderOutputMetadataAdaptor : NSObject {     convenience init!(assetReaderTrackOutput trackOutput: AVAssetReaderTrackOutput!)     class func assetReaderOutputMetadataAdaptorWithAssetReaderTrackOutput(_ trackOutput: AVAssetReaderTrackOutput!) -> Self!     init!(assetReaderTrackOutput trackOutput: AVAssetReaderTrackOutput!)     var assetReaderTrackOutput: AVAssetReaderTrackOutput! { get }     func nextTimedMetadataGroup() -> AVTimedMetadataGroup! } ``` |
| To | ``` class AVAssetReaderOutputMetadataAdaptor : NSObject {     convenience init()     convenience init(assetReaderTrackOutput trackOutput: AVAssetReaderTrackOutput)     class func assetReaderOutputMetadataAdaptorWithAssetReaderTrackOutput(_ trackOutput: AVAssetReaderTrackOutput) -> Self     init(assetReaderTrackOutput trackOutput: AVAssetReaderTrackOutput)     var assetReaderTrackOutput: AVAssetReaderTrackOutput { get }     func nextTimedMetadataGroup() -> AVTimedMetadataGroup? } ``` |

Modified [AVAssetReaderOutputMetadataAdaptor.assetReaderTrackOutput](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputmetadataadaptor/1388330-assetreadertrackoutput)

|  | Declaration |
| --- | --- |
| From | ``` var assetReaderTrackOutput: AVAssetReaderTrackOutput! { get } ``` |
| To | ``` var assetReaderTrackOutput: AVAssetReaderTrackOutput { get } ``` |

Modified [AVAssetReaderOutputMetadataAdaptor.init(assetReaderTrackOutput: AVAssetReaderTrackOutput)](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputmetadataadaptor/1388009-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(assetReaderTrackOutput trackOutput: AVAssetReaderTrackOutput!) ``` |
| To | ``` init(assetReaderTrackOutput trackOutput: AVAssetReaderTrackOutput) ``` |

Modified [AVAssetReaderOutputMetadataAdaptor.nextTimedMetadataGroup() -> AVTimedMetadataGroup?](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputmetadataadaptor/1390008-nexttimedmetadatagroup)

|  | Declaration |
| --- | --- |
| From | ``` func nextTimedMetadataGroup() -> AVTimedMetadataGroup! ``` |
| To | ``` func nextTimedMetadataGroup() -> AVTimedMetadataGroup? ``` |

Modified [AVAssetReaderSampleReferenceOutput](https://developer.apple.com/documentation/avfoundation/avassetreadersamplereferenceoutput)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetReaderSampleReferenceOutput : AVAssetReaderOutput {     init!(track track: AVAssetTrack!) -> AVAssetReaderSampleReferenceOutput     class func assetReaderSampleReferenceOutputWithTrack(_ track: AVAssetTrack!) -> AVAssetReaderSampleReferenceOutput!     init!(track track: AVAssetTrack!)     var track: AVAssetTrack! { get } } ``` |
| To | ``` class AVAssetReaderSampleReferenceOutput : AVAssetReaderOutput {     convenience init()     convenience init(track track: AVAssetTrack)     class func assetReaderSampleReferenceOutputWithTrack(_ track: AVAssetTrack) -> Self     init(track track: AVAssetTrack)     var track: AVAssetTrack { get } } ``` |

Modified [AVAssetReaderSampleReferenceOutput.init(track: AVAssetTrack)](https://developer.apple.com/documentation/avfoundation/avassetreadersamplereferenceoutput/1387339-initwithtrack)

|  | Declaration |
| --- | --- |
| From | ``` init!(track track: AVAssetTrack!) ``` |
| To | ``` init(track track: AVAssetTrack) ``` |

Modified [AVAssetReaderSampleReferenceOutput.track](https://developer.apple.com/documentation/avfoundation/avassetreadersamplereferenceoutput/1390057-track)

|  | Declaration |
| --- | --- |
| From | ``` var track: AVAssetTrack! { get } ``` |
| To | ``` var track: AVAssetTrack { get } ``` |

Modified [AVAssetReaderStatus [enum]](https://developer.apple.com/documentation/avfoundation/avassetreader/status)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVAssetReaderTrackOutput](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetReaderTrackOutput : AVAssetReaderOutput {     convenience init!(track track: AVAssetTrack!, outputSettings outputSettings: [NSObject : AnyObject]!)     class func assetReaderTrackOutputWithTrack(_ track: AVAssetTrack!, outputSettings outputSettings: [NSObject : AnyObject]!) -> Self!     init!(track track: AVAssetTrack!, outputSettings outputSettings: [NSObject : AnyObject]!)     var track: AVAssetTrack! { get }     var outputSettings: [NSObject : AnyObject]! { get }     var audioTimePitchAlgorithm: String! } ``` |
| To | ``` class AVAssetReaderTrackOutput : AVAssetReaderOutput {     convenience init()     convenience init(track track: AVAssetTrack, outputSettings outputSettings: [String : AnyObject]?)     class func assetReaderTrackOutputWithTrack(_ track: AVAssetTrack, outputSettings outputSettings: [String : AnyObject]?) -> Self     init(track track: AVAssetTrack, outputSettings outputSettings: [String : AnyObject]?)     var track: AVAssetTrack { get }     var outputSettings: [String : AnyObject]? { get }     var audioTimePitchAlgorithm: String } ``` |

Modified [AVAssetReaderTrackOutput.audioTimePitchAlgorithm](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput/1387851-audiotimepitchalgorithm)

|  | Declaration |
| --- | --- |
| From | ``` var audioTimePitchAlgorithm: String! ``` |
| To | ``` var audioTimePitchAlgorithm: String ``` |

Modified [AVAssetReaderTrackOutput.init(track: AVAssetTrack, outputSettings: [String : AnyObject]?)](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput/1385807-initwithtrack)

|  | Declaration |
| --- | --- |
| From | ``` init!(track track: AVAssetTrack!, outputSettings outputSettings: [NSObject : AnyObject]!) ``` |
| To | ``` init(track track: AVAssetTrack, outputSettings outputSettings: [String : AnyObject]?) ``` |

Modified [AVAssetReaderTrackOutput.outputSettings](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput/1387163-outputsettings)

|  | Declaration |
| --- | --- |
| From | ``` var outputSettings: [NSObject : AnyObject]! { get } ``` |
| To | ``` var outputSettings: [String : AnyObject]? { get } ``` |

Modified [AVAssetReaderTrackOutput.track](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput/1386921-track)

|  | Declaration |
| --- | --- |
| From | ``` var track: AVAssetTrack! { get } ``` |
| To | ``` var track: AVAssetTrack { get } ``` |

Modified [AVAssetReaderVideoCompositionOutput](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetReaderVideoCompositionOutput : AVAssetReaderOutput {     convenience init!(videoTracks videoTracks: [AnyObject]!, videoSettings videoSettings: [NSObject : AnyObject]!)     class func assetReaderVideoCompositionOutputWithVideoTracks(_ videoTracks: [AnyObject]!, videoSettings videoSettings: [NSObject : AnyObject]!) -> Self!     init!(videoTracks videoTracks: [AnyObject]!, videoSettings videoSettings: [NSObject : AnyObject]!)     var videoTracks: [AnyObject]! { get }     var videoSettings: [NSObject : AnyObject]! { get }     @NSCopying var videoComposition: AVVideoComposition!     var customVideoCompositor: AVVideoCompositing! { get } } ``` |
| To | ``` class AVAssetReaderVideoCompositionOutput : AVAssetReaderOutput {     convenience init()     convenience init(videoTracks videoTracks: [AVAssetTrack], videoSettings videoSettings: [String : AnyObject]?)     class func assetReaderVideoCompositionOutputWithVideoTracks(_ videoTracks: [AVAssetTrack], videoSettings videoSettings: [String : AnyObject]?) -> Self     init(videoTracks videoTracks: [AVAssetTrack], videoSettings videoSettings: [String : AnyObject]?)     var videoTracks: [AVAssetTrack] { get }     var videoSettings: [String : AnyObject]? { get }     @NSCopying var videoComposition: AVVideoComposition?     var customVideoCompositor: AVVideoCompositing? { get } } ``` |

Modified [AVAssetReaderVideoCompositionOutput.customVideoCompositor](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/1388310-customvideocompositor)

|  | Declaration |
| --- | --- |
| From | ``` var customVideoCompositor: AVVideoCompositing! { get } ``` |
| To | ``` var customVideoCompositor: AVVideoCompositing? { get } ``` |

Modified [AVAssetReaderVideoCompositionOutput.init(videoTracks: [AVAssetTrack], videoSettings: [String : AnyObject]?)](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/1386676-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(videoTracks videoTracks: [AnyObject]!, videoSettings videoSettings: [NSObject : AnyObject]!) ``` |
| To | ``` init(videoTracks videoTracks: [AVAssetTrack], videoSettings videoSettings: [String : AnyObject]?) ``` |

Modified [AVAssetReaderVideoCompositionOutput.videoComposition](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/1388927-videocomposition)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var videoComposition: AVVideoComposition! ``` |
| To | ``` @NSCopying var videoComposition: AVVideoComposition? ``` |

Modified [AVAssetReaderVideoCompositionOutput.videoSettings](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/1389247-videosettings)

|  | Declaration |
| --- | --- |
| From | ``` var videoSettings: [NSObject : AnyObject]! { get } ``` |
| To | ``` var videoSettings: [String : AnyObject]? { get } ``` |

Modified [AVAssetReaderVideoCompositionOutput.videoTracks](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/1389000-videotracks)

|  | Declaration |
| --- | --- |
| From | ``` var videoTracks: [AnyObject]! { get } ``` |
| To | ``` var videoTracks: [AVAssetTrack] { get } ``` |

Modified [AVAssetReferenceRestrictions [struct]](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVAssetReferenceRestrictions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var RestrictionForbidNone: AVAssetReferenceRestrictions { get }     static var RestrictionForbidRemoteReferenceToLocal: AVAssetReferenceRestrictions { get }     static var RestrictionForbidLocalReferenceToRemote: AVAssetReferenceRestrictions { get }     static var RestrictionForbidCrossSiteReference: AVAssetReferenceRestrictions { get }     static var RestrictionForbidLocalReferenceToLocal: AVAssetReferenceRestrictions { get }     static var RestrictionForbidAll: AVAssetReferenceRestrictions { get } } ``` | RawOptionSetType |
| To | ``` struct AVAssetReferenceRestrictions : OptionSetType {     init(rawValue rawValue: UInt)     static var ForbidNone: AVAssetReferenceRestrictions { get }     static var ForbidRemoteReferenceToLocal: AVAssetReferenceRestrictions { get }     static var ForbidLocalReferenceToRemote: AVAssetReferenceRestrictions { get }     static var ForbidCrossSiteReference: AVAssetReferenceRestrictions { get }     static var ForbidLocalReferenceToLocal: AVAssetReferenceRestrictions { get }     static var ForbidAll: AVAssetReferenceRestrictions { get } } ``` | OptionSetType |

Modified [AVAssetReferenceRestrictions.ForbidAll](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/1387554-forbidall)

|  | Declaration |
| --- | --- |
| From | ``` static var RestrictionForbidAll: AVAssetReferenceRestrictions { get } ``` |
| To | ``` static var ForbidAll: AVAssetReferenceRestrictions { get } ``` |

Modified [AVAssetReferenceRestrictions.ForbidCrossSiteReference](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/avassetreferencerestrictionforbidcrosssitereference)

|  | Declaration |
| --- | --- |
| From | ``` static var RestrictionForbidCrossSiteReference: AVAssetReferenceRestrictions { get } ``` |
| To | ``` static var ForbidCrossSiteReference: AVAssetReferenceRestrictions { get } ``` |

Modified [AVAssetReferenceRestrictions.ForbidLocalReferenceToLocal](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/avassetreferencerestrictionforbidlocalreferencetolocal)

|  | Declaration |
| --- | --- |
| From | ``` static var RestrictionForbidLocalReferenceToLocal: AVAssetReferenceRestrictions { get } ``` |
| To | ``` static var ForbidLocalReferenceToLocal: AVAssetReferenceRestrictions { get } ``` |

Modified [AVAssetReferenceRestrictions.ForbidLocalReferenceToRemote](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/avassetreferencerestrictionforbidlocalreferencetoremote)

|  | Declaration |
| --- | --- |
| From | ``` static var RestrictionForbidLocalReferenceToRemote: AVAssetReferenceRestrictions { get } ``` |
| To | ``` static var ForbidLocalReferenceToRemote: AVAssetReferenceRestrictions { get } ``` |

Modified [AVAssetReferenceRestrictions.ForbidNone](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/avassetreferencerestrictionforbidnone)

|  | Declaration |
| --- | --- |
| From | ``` static var RestrictionForbidNone: AVAssetReferenceRestrictions { get } ``` |
| To | ``` static var ForbidNone: AVAssetReferenceRestrictions { get } ``` |

Modified [AVAssetReferenceRestrictions.ForbidRemoteReferenceToLocal](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/1387464-forbidremotereferencetolocal)

|  | Declaration |
| --- | --- |
| From | ``` static var RestrictionForbidRemoteReferenceToLocal: AVAssetReferenceRestrictions { get } ``` |
| To | ``` static var ForbidRemoteReferenceToLocal: AVAssetReferenceRestrictions { get } ``` |

Modified [AVAssetResourceLoader](https://developer.apple.com/documentation/avfoundation/avassetresourceloader)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetResourceLoader : NSObject {     func setDelegate(_ delegate: AVAssetResourceLoaderDelegate!, queue delegateQueue: dispatch_queue_t!)     var delegate: AVAssetResourceLoaderDelegate! { get }     var delegateQueue: dispatch_queue_t! { get } } ``` |
| To | ``` class AVAssetResourceLoader : NSObject {     init()     func setDelegate(_ delegate: AVAssetResourceLoaderDelegate?, queue delegateQueue: dispatch_queue_t?)     weak var delegate: AVAssetResourceLoaderDelegate? { get }     var delegateQueue: dispatch_queue_t? { get } } extension AVAssetResourceLoader {     var preloadsEligibleContentKeys: Bool } ``` |

Modified [AVAssetResourceLoader.delegate](https://developer.apple.com/documentation/avfoundation/avassetresourceloader/1387913-delegate)

|  | Declaration |
| --- | --- |
| From | ``` var delegate: AVAssetResourceLoaderDelegate! { get } ``` |
| To | ``` weak var delegate: AVAssetResourceLoaderDelegate? { get } ``` |

Modified [AVAssetResourceLoader.delegateQueue](https://developer.apple.com/documentation/avfoundation/avassetresourceloader/1387678-delegatequeue)

|  | Declaration |
| --- | --- |
| From | ``` var delegateQueue: dispatch_queue_t! { get } ``` |
| To | ``` var delegateQueue: dispatch_queue_t? { get } ``` |

Modified [AVAssetResourceLoader.setDelegate(_: AVAssetResourceLoaderDelegate?, queue: dispatch_queue_t?)](https://developer.apple.com/documentation/avfoundation/avassetresourceloader/1388314-setdelegate)

|  | Declaration |
| --- | --- |
| From | ``` func setDelegate(_ delegate: AVAssetResourceLoaderDelegate!, queue delegateQueue: dispatch_queue_t!) ``` |
| To | ``` func setDelegate(_ delegate: AVAssetResourceLoaderDelegate?, queue delegateQueue: dispatch_queue_t?) ``` |

Modified [AVAssetResourceLoaderDelegate](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVAssetResourceLoaderDelegate : NSObjectProtocol {     optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader!, shouldWaitForLoadingOfRequestedResource loadingRequest: AVAssetResourceLoadingRequest!) -> Bool     optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader!, shouldWaitForRenewalOfRequestedResource renewalRequest: AVAssetResourceRenewalRequest!) -> Bool     optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader!, didCancelLoadingRequest loadingRequest: AVAssetResourceLoadingRequest!)     optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader!, shouldWaitForResponseToAuthenticationChallenge authenticationChallenge: NSURLAuthenticationChallenge!) -> Bool     optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader!, didCancelAuthenticationChallenge authenticationChallenge: NSURLAuthenticationChallenge!) } ``` |
| To | ``` protocol AVAssetResourceLoaderDelegate : NSObjectProtocol {     optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, shouldWaitForLoadingOfRequestedResource loadingRequest: AVAssetResourceLoadingRequest) -> Bool     optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, shouldWaitForRenewalOfRequestedResource renewalRequest: AVAssetResourceRenewalRequest) -> Bool     optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, didCancelLoadingRequest loadingRequest: AVAssetResourceLoadingRequest)     optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, shouldWaitForResponseToAuthenticationChallenge authenticationChallenge: NSURLAuthenticationChallenge) -> Bool     optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, didCancelAuthenticationChallenge authenticationChallenge: NSURLAuthenticationChallenge) } ``` |

Modified [AVAssetResourceLoaderDelegate.resourceLoader(_: AVAssetResourceLoader, didCancelAuthenticationChallenge: NSURLAuthenticationChallenge)](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/1387929-resourceloader)

|  | Declaration |
| --- | --- |
| From | ``` optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader!, didCancelAuthenticationChallenge authenticationChallenge: NSURLAuthenticationChallenge!) ``` |
| To | ``` optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, didCancelAuthenticationChallenge authenticationChallenge: NSURLAuthenticationChallenge) ``` |

Modified [AVAssetResourceLoaderDelegate.resourceLoader(_: AVAssetResourceLoader, didCancelLoadingRequest: AVAssetResourceLoadingRequest)](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/1387722-resourceloader)

|  | Declaration |
| --- | --- |
| From | ``` optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader!, didCancelLoadingRequest loadingRequest: AVAssetResourceLoadingRequest!) ``` |
| To | ``` optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, didCancelLoadingRequest loadingRequest: AVAssetResourceLoadingRequest) ``` |

Modified [AVAssetResourceLoaderDelegate.resourceLoader(_: AVAssetResourceLoader, shouldWaitForLoadingOfRequestedResource: AVAssetResourceLoadingRequest) -> Bool](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/1388121-resourceloader)

|  | Declaration |
| --- | --- |
| From | ``` optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader!, shouldWaitForLoadingOfRequestedResource loadingRequest: AVAssetResourceLoadingRequest!) -> Bool ``` |
| To | ``` optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, shouldWaitForLoadingOfRequestedResource loadingRequest: AVAssetResourceLoadingRequest) -> Bool ``` |

Modified [AVAssetResourceLoaderDelegate.resourceLoader(_: AVAssetResourceLoader, shouldWaitForRenewalOfRequestedResource: AVAssetResourceRenewalRequest) -> Bool](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/1387058-resourceloader)

|  | Declaration |
| --- | --- |
| From | ``` optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader!, shouldWaitForRenewalOfRequestedResource renewalRequest: AVAssetResourceRenewalRequest!) -> Bool ``` |
| To | ``` optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, shouldWaitForRenewalOfRequestedResource renewalRequest: AVAssetResourceRenewalRequest) -> Bool ``` |

Modified [AVAssetResourceLoaderDelegate.resourceLoader(_: AVAssetResourceLoader, shouldWaitForResponseToAuthenticationChallenge: NSURLAuthenticationChallenge) -> Bool](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/1388736-resourceloader)

|  | Declaration |
| --- | --- |
| From | ``` optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader!, shouldWaitForResponseToAuthenticationChallenge authenticationChallenge: NSURLAuthenticationChallenge!) -> Bool ``` |
| To | ``` optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, shouldWaitForResponseToAuthenticationChallenge authenticationChallenge: NSURLAuthenticationChallenge) -> Bool ``` |

Modified [AVAssetResourceLoadingContentInformationRequest](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetResourceLoadingContentInformationRequest : NSObject {     var contentType: String!     var contentLength: Int64     var byteRangeAccessSupported: Bool     @NSCopying var renewalDate: NSDate! } ``` |
| To | ``` class AVAssetResourceLoadingContentInformationRequest : NSObject {     init()     var contentType: String?     var contentLength: Int64     var byteRangeAccessSupported: Bool     @NSCopying var renewalDate: NSDate? } ``` |

Modified [AVAssetResourceLoadingContentInformationRequest.contentType](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/1388529-contenttype)

|  | Declaration |
| --- | --- |
| From | ``` var contentType: String! ``` |
| To | ``` var contentType: String? ``` |

Modified [AVAssetResourceLoadingContentInformationRequest.renewalDate](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/1390683-renewaldate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var renewalDate: NSDate! ``` |
| To | ``` @NSCopying var renewalDate: NSDate? ``` |

Modified [AVAssetResourceLoadingDataRequest](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetResourceLoadingDataRequest : NSObject {     var requestedOffset: Int64 { get }     var requestedLength: Int { get }     var currentOffset: Int64 { get }     func respondWithData(_ data: NSData!) } ``` |
| To | ``` class AVAssetResourceLoadingDataRequest : NSObject {     init()     var requestedOffset: Int64 { get }     var requestedLength: Int { get }     var requestsAllDataToEndOfResource: Bool { get }     var currentOffset: Int64 { get }     func respondWithData(_ data: NSData) } ``` |

Modified [AVAssetResourceLoadingDataRequest.respondWithData(_: NSData)](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest/1390581-respondwithdata)

|  | Declaration |
| --- | --- |
| From | ``` func respondWithData(_ data: NSData!) ``` |
| To | ``` func respondWithData(_ data: NSData) ``` |

Modified [AVAssetResourceLoadingRequest](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetResourceLoadingRequest : NSObject {     var request: NSURLRequest! { get }     var finished: Bool { get }     var cancelled: Bool { get }     var contentInformationRequest: AVAssetResourceLoadingContentInformationRequest! { get }     var dataRequest: AVAssetResourceLoadingDataRequest! { get }     @NSCopying var response: NSURLResponse!     @NSCopying var redirect: NSURLRequest!     func finishLoading()     func finishLoadingWithError(_ error: NSError!) } extension AVAssetResourceLoadingRequest {     func streamingContentKeyRequestDataForApp(_ appIdentifier: NSData!, contentIdentifier contentIdentifier: NSData!, options options: [NSObject : AnyObject]!, error outError: NSErrorPointer) -> NSData! } extension AVAssetResourceLoadingRequest {     func finishLoadingWithResponse(_ response: NSURLResponse!, data data: NSData!, redirect redirect: NSURLRequest!) } ``` |
| To | ``` class AVAssetResourceLoadingRequest : NSObject {     init()     var request: NSURLRequest { get }     var finished: Bool { get }     var cancelled: Bool { get }     var contentInformationRequest: AVAssetResourceLoadingContentInformationRequest? { get }     var dataRequest: AVAssetResourceLoadingDataRequest? { get }     @NSCopying var response: NSURLResponse?     @NSCopying var redirect: NSURLRequest?     func finishLoading()     func finishLoadingWithError(_ error: NSError?) } extension AVAssetResourceLoadingRequest {     func streamingContentKeyRequestDataForApp(_ appIdentifier: NSData, contentIdentifier contentIdentifier: NSData, options options: [String : AnyObject]?) throws -> NSData     func persistentContentKeyFromKeyVendorResponse(_ keyVendorResponse: NSData, options options: [String : AnyObject]?, error outError: NSErrorPointer) -> NSData } extension AVAssetResourceLoadingRequest {     func finishLoadingWithResponse(_ response: NSURLResponse?, data data: NSData?, redirect redirect: NSURLRequest?) } ``` |

Modified [AVAssetResourceLoadingRequest.contentInformationRequest](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1390340-contentinformationrequest)

|  | Declaration |
| --- | --- |
| From | ``` var contentInformationRequest: AVAssetResourceLoadingContentInformationRequest! { get } ``` |
| To | ``` var contentInformationRequest: AVAssetResourceLoadingContentInformationRequest? { get } ``` |

Modified [AVAssetResourceLoadingRequest.dataRequest](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1388779-datarequest)

|  | Declaration |
| --- | --- |
| From | ``` var dataRequest: AVAssetResourceLoadingDataRequest! { get } ``` |
| To | ``` var dataRequest: AVAssetResourceLoadingDataRequest? { get } ``` |

Modified [AVAssetResourceLoadingRequest.finishLoadingWithError(_: NSError?)](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1390491-finishloadingwitherror)

|  | Declaration |
| --- | --- |
| From | ``` func finishLoadingWithError(_ error: NSError!) ``` |
| To | ``` func finishLoadingWithError(_ error: NSError?) ``` |

Modified [AVAssetResourceLoadingRequest.redirect](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1390854-redirect)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var redirect: NSURLRequest! ``` |
| To | ``` @NSCopying var redirect: NSURLRequest? ``` |

Modified [AVAssetResourceLoadingRequest.request](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1386220-request)

|  | Declaration |
| --- | --- |
| From | ``` var request: NSURLRequest! { get } ``` |
| To | ``` var request: NSURLRequest { get } ``` |

Modified [AVAssetResourceLoadingRequest.response](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1389034-response)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var response: NSURLResponse! ``` |
| To | ``` @NSCopying var response: NSURLResponse? ``` |

Modified [AVAssetResourceLoadingRequest.streamingContentKeyRequestDataForApp(_: NSData, contentIdentifier: NSData, options: [String : AnyObject]?) throws -> NSData](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1386116-streamingcontentkeyrequestdatafo)

|  | Declaration |
| --- | --- |
| From | ``` func streamingContentKeyRequestDataForApp(_ appIdentifier: NSData!, contentIdentifier contentIdentifier: NSData!, options options: [NSObject : AnyObject]!, error outError: NSErrorPointer) -> NSData! ``` |
| To | ``` func streamingContentKeyRequestDataForApp(_ appIdentifier: NSData, contentIdentifier contentIdentifier: NSData, options options: [String : AnyObject]?) throws -> NSData ``` |

Modified [AVAssetTrack](https://developer.apple.com/documentation/avfoundation/avassettrack)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetTrack : NSObject, NSCopying, AVAsynchronousKeyValueLoading {     var asset: AVAsset! { get }     var trackID: CMPersistentTrackID { get } } extension AVAssetTrack {     var mediaType: String! { get }     var formatDescriptions: [AnyObject]! { get }     var playable: Bool { get }     var enabled: Bool { get }     var selfContained: Bool { get }     var totalSampleDataLength: Int64 { get }     func hasMediaCharacteristic(_ mediaCharacteristic: String!) -> Bool } extension AVAssetTrack {     var timeRange: CMTimeRange { get }     var naturalTimeScale: CMTimeScale { get }     var estimatedDataRate: Float { get } } extension AVAssetTrack {     var languageCode: String! { get }     var extendedLanguageTag: String! { get } } extension AVAssetTrack {     var naturalSize: CGSize { get }     var preferredTransform: CGAffineTransform { get } } extension AVAssetTrack {     var preferredVolume: Float { get } } extension AVAssetTrack {     var nominalFrameRate: Float { get }     var minFrameDuration: CMTime { get }     var requiresFrameReordering: Bool { get } } extension AVAssetTrack {     var segments: [AnyObject]! { get }     func segmentForTrackTime(_ trackTime: CMTime) -> AVAssetTrackSegment!     func samplePresentationTimeForTrackTime(_ trackTime: CMTime) -> CMTime } extension AVAssetTrack {     var commonMetadata: [AnyObject]! { get }     var metadata: [AnyObject]! { get }     var availableMetadataFormats: [AnyObject]! { get }     func metadataForFormat(_ format: String!) -> [AnyObject]! } extension AVAssetTrack {     var availableTrackAssociationTypes: [AnyObject]! { get }     func associatedTracksOfType(_ trackAssociationType: String!) -> [AnyObject]! } ``` |
| To | ``` class AVAssetTrack : NSObject, NSCopying, AVAsynchronousKeyValueLoading {     init()     weak var asset: AVAsset? { get }     var trackID: CMPersistentTrackID { get } } extension AVAssetTrack {     var mediaType: String { get }     var formatDescriptions: [AnyObject] { get }     var playable: Bool { get }     var enabled: Bool { get }     var selfContained: Bool { get }     var totalSampleDataLength: Int64 { get }     func hasMediaCharacteristic(_ mediaCharacteristic: String) -> Bool } extension AVAssetTrack {     var timeRange: CMTimeRange { get }     var naturalTimeScale: CMTimeScale { get }     var estimatedDataRate: Float { get } } extension AVAssetTrack {     var languageCode: String { get }     var extendedLanguageTag: String { get } } extension AVAssetTrack {     var naturalSize: CGSize { get }     var preferredTransform: CGAffineTransform { get } } extension AVAssetTrack {     var preferredVolume: Float { get } } extension AVAssetTrack {     var nominalFrameRate: Float { get }     var minFrameDuration: CMTime { get }     var requiresFrameReordering: Bool { get } } extension AVAssetTrack {     var segments: [AVAssetTrackSegment] { get }     func segmentForTrackTime(_ trackTime: CMTime) -> AVAssetTrackSegment?     func samplePresentationTimeForTrackTime(_ trackTime: CMTime) -> CMTime } extension AVAssetTrack {     var commonMetadata: [AVMetadataItem] { get }     var metadata: [AVMetadataItem] { get }     var availableMetadataFormats: [String] { get }     func metadataForFormat(_ format: String) -> [AVMetadataItem] } extension AVAssetTrack {     var availableTrackAssociationTypes: [String] { get }     func associatedTracksOfType(_ trackAssociationType: String) -> [AVAssetTrack] } ``` |

Modified [AVAssetTrack.asset](https://developer.apple.com/documentation/avfoundation/avassettrack/1385611-asset)

|  | Declaration |
| --- | --- |
| From | ``` var asset: AVAsset! { get } ``` |
| To | ``` weak var asset: AVAsset? { get } ``` |

Modified [AVAssetTrack.associatedTracksOfType(_: String) -> [AVAssetTrack]](https://developer.apple.com/documentation/avfoundation/avassettrack/1389251-associatedtracksoftype)

|  | Declaration |
| --- | --- |
| From | ``` func associatedTracksOfType(_ trackAssociationType: String!) -> [AnyObject]! ``` |
| To | ``` func associatedTracksOfType(_ trackAssociationType: String) -> [AVAssetTrack] ``` |

Modified [AVAssetTrack.availableMetadataFormats](https://developer.apple.com/documentation/avfoundation/avassettrack/1385751-availablemetadataformats)

|  | Declaration |
| --- | --- |
| From | ``` var availableMetadataFormats: [AnyObject]! { get } ``` |
| To | ``` var availableMetadataFormats: [String] { get } ``` |

Modified [AVAssetTrack.availableTrackAssociationTypes](https://developer.apple.com/documentation/avfoundation/avassettrack/1388065-availabletrackassociationtypes)

|  | Declaration |
| --- | --- |
| From | ``` var availableTrackAssociationTypes: [AnyObject]! { get } ``` |
| To | ``` var availableTrackAssociationTypes: [String] { get } ``` |

Modified [AVAssetTrack.commonMetadata](https://developer.apple.com/documentation/avfoundation/avassettrack/1390832-commonmetadata)

|  | Declaration |
| --- | --- |
| From | ``` var commonMetadata: [AnyObject]! { get } ``` |
| To | ``` var commonMetadata: [AVMetadataItem] { get } ``` |

Modified [AVAssetTrack.extendedLanguageTag](https://developer.apple.com/documentation/avfoundation/avassettrack/1389105-extendedlanguagetag)

|  | Declaration |
| --- | --- |
| From | ``` var extendedLanguageTag: String! { get } ``` |
| To | ``` var extendedLanguageTag: String { get } ``` |

Modified [AVAssetTrack.formatDescriptions](https://developer.apple.com/documentation/avfoundation/avassettrack/1386694-formatdescriptions)

|  | Declaration |
| --- | --- |
| From | ``` var formatDescriptions: [AnyObject]! { get } ``` |
| To | ``` var formatDescriptions: [AnyObject] { get } ``` |

Modified [AVAssetTrack.hasMediaCharacteristic(_: String) -> Bool](https://developer.apple.com/documentation/avfoundation/avassettrack/1385847-hasmediacharacteristic)

|  | Declaration |
| --- | --- |
| From | ``` func hasMediaCharacteristic(_ mediaCharacteristic: String!) -> Bool ``` |
| To | ``` func hasMediaCharacteristic(_ mediaCharacteristic: String) -> Bool ``` |

Modified [AVAssetTrack.languageCode](https://developer.apple.com/documentation/avfoundation/avassettrack/1388627-languagecode)

|  | Declaration |
| --- | --- |
| From | ``` var languageCode: String! { get } ``` |
| To | ``` var languageCode: String { get } ``` |

Modified [AVAssetTrack.mediaType](https://developer.apple.com/documentation/avfoundation/avassettrack/1385741-mediatype)

|  | Declaration |
| --- | --- |
| From | ``` var mediaType: String! { get } ``` |
| To | ``` var mediaType: String { get } ``` |

Modified [AVAssetTrack.metadata](https://developer.apple.com/documentation/avfoundation/avassettrack/1389054-metadata)

|  | Declaration |
| --- | --- |
| From | ``` var metadata: [AnyObject]! { get } ``` |
| To | ``` var metadata: [AVMetadataItem] { get } ``` |

Modified [AVAssetTrack.metadataForFormat(_: String) -> [AVMetadataItem]](https://developer.apple.com/documentation/avfoundation/avassettrack/1387921-metadataforformat)

|  | Declaration |
| --- | --- |
| From | ``` func metadataForFormat(_ format: String!) -> [AnyObject]! ``` |
| To | ``` func metadataForFormat(_ format: String) -> [AVMetadataItem] ``` |

Modified [AVAssetTrack.segmentForTrackTime(_: CMTime) -> AVAssetTrackSegment?](https://developer.apple.com/documentation/avfoundation/avassettrack/1387186-segmentfortracktime)

|  | Declaration |
| --- | --- |
| From | ``` func segmentForTrackTime(_ trackTime: CMTime) -> AVAssetTrackSegment! ``` |
| To | ``` func segmentForTrackTime(_ trackTime: CMTime) -> AVAssetTrackSegment? ``` |

Modified [AVAssetTrack.segments](https://developer.apple.com/documentation/avfoundation/avassettrack/1390665-segments)

|  | Declaration |
| --- | --- |
| From | ``` var segments: [AnyObject]! { get } ``` |
| To | ``` var segments: [AVAssetTrackSegment] { get } ``` |

Modified [AVAssetTrackGroup](https://developer.apple.com/documentation/avfoundation/avassettrackgroup)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetTrackGroup : NSObject, NSCopying {     var trackIDs: [AnyObject]! { get } } ``` |
| To | ``` class AVAssetTrackGroup : NSObject, NSCopying {     var trackIDs: [NSNumber] { get } } ``` |

Modified [AVAssetTrackGroup.trackIDs](https://developer.apple.com/documentation/avfoundation/avassettrackgroup/1389024-trackids)

|  | Declaration |
| --- | --- |
| From | ``` var trackIDs: [AnyObject]! { get } ``` |
| To | ``` var trackIDs: [NSNumber] { get } ``` |

Modified [AVAssetTrackSegment](https://developer.apple.com/documentation/avfoundation/avassettracksegment)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetTrackSegment : NSObject {     var timeMapping: CMTimeMapping { get }     var empty: Bool { get } } ``` |
| To | ``` class AVAssetTrackSegment : NSObject {     init()     var timeMapping: CMTimeMapping { get }     var empty: Bool { get } } ``` |

Modified [AVAssetWriter](https://developer.apple.com/documentation/avfoundation/avassetwriter)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetWriter : NSObject {     convenience init!(URL outputURL: NSURL!, fileType outputFileType: String!, error outError: NSErrorPointer)     class func assetWriterWithURL(_ outputURL: NSURL!, fileType outputFileType: String!, error outError: NSErrorPointer) -> Self!     init!(URL outputURL: NSURL!, fileType outputFileType: String!, error outError: NSErrorPointer)     @NSCopying var outputURL: NSURL! { get }     var outputFileType: String! { get }     var availableMediaTypes: [AnyObject]! { get }     var status: AVAssetWriterStatus { get }     var error: NSError! { get }     var metadata: [AnyObject]!     var shouldOptimizeForNetworkUse: Bool     @NSCopying var directoryForTemporaryFiles: NSURL!     var inputs: [AnyObject]! { get }     func canApplyOutputSettings(_ outputSettings: [NSObject : AnyObject]!, forMediaType mediaType: String!) -> Bool     func canAddInput(_ input: AVAssetWriterInput!) -> Bool     func addInput(_ input: AVAssetWriterInput!)     func startWriting() -> Bool     func startSessionAtSourceTime(_ startTime: CMTime)     func endSessionAtSourceTime(_ endTime: CMTime)     func cancelWriting()     func finishWriting() -> Bool     func finishWritingWithCompletionHandler(_ handler: (() -> Void)!) } extension AVAssetWriter {     var movieFragmentInterval: CMTime     var movieTimeScale: CMTimeScale } extension AVAssetWriter {     func canAddInputGroup(_ inputGroup: AVAssetWriterInputGroup!) -> Bool     func addInputGroup(_ inputGroup: AVAssetWriterInputGroup!)     var inputGroups: [AnyObject]! { get } } ``` |
| To | ``` class AVAssetWriter : NSObject {     convenience init()     convenience init(URL outputURL: NSURL, fileType outputFileType: String) throws     class func assetWriterWithURL(_ outputURL: NSURL, fileType outputFileType: String) throws -> Self     init(URL outputURL: NSURL, fileType outputFileType: String) throws     @NSCopying var outputURL: NSURL { get }     var outputFileType: String { get }     var availableMediaTypes: [String] { get }     var status: AVAssetWriterStatus { get }     var error: NSError? { get }     var metadata: [AVMetadataItem]     var shouldOptimizeForNetworkUse: Bool     @NSCopying var directoryForTemporaryFiles: NSURL?     var inputs: [AVAssetWriterInput] { get }     func canApplyOutputSettings(_ outputSettings: [String : AnyObject]?, forMediaType mediaType: String) -> Bool     func canAddInput(_ input: AVAssetWriterInput) -> Bool     func addInput(_ input: AVAssetWriterInput)     func startWriting() -> Bool     func startSessionAtSourceTime(_ startTime: CMTime)     func endSessionAtSourceTime(_ endTime: CMTime)     func cancelWriting()     func finishWriting() -> Bool     func finishWritingWithCompletionHandler(_ handler: () -> Void) } extension AVAssetWriter {     var movieFragmentInterval: CMTime     var overallDurationHint: CMTime     var movieTimeScale: CMTimeScale } extension AVAssetWriter {     func canAddInputGroup(_ inputGroup: AVAssetWriterInputGroup) -> Bool     func addInputGroup(_ inputGroup: AVAssetWriterInputGroup)     var inputGroups: [AVAssetWriterInputGroup] { get } } ``` |

Modified [AVAssetWriter.addInput(_: AVAssetWriterInput)](https://developer.apple.com/documentation/avfoundation/avassetwriter/1390389-addinput)

|  | Declaration |
| --- | --- |
| From | ``` func addInput(_ input: AVAssetWriterInput!) ``` |
| To | ``` func addInput(_ input: AVAssetWriterInput) ``` |

Modified [AVAssetWriter.addInputGroup(_: AVAssetWriterInputGroup)](https://developer.apple.com/documentation/avfoundation/avassetwriter/1385643-add)

|  | Declaration |
| --- | --- |
| From | ``` func addInputGroup(_ inputGroup: AVAssetWriterInputGroup!) ``` |
| To | ``` func addInputGroup(_ inputGroup: AVAssetWriterInputGroup) ``` |

Modified [AVAssetWriter.availableMediaTypes](https://developer.apple.com/documentation/avfoundation/avassetwriter/1388730-availablemediatypes)

|  | Declaration |
| --- | --- |
| From | ``` var availableMediaTypes: [AnyObject]! { get } ``` |
| To | ``` var availableMediaTypes: [String] { get } ``` |

Modified [AVAssetWriter.canAddInput(_: AVAssetWriterInput) -> Bool](https://developer.apple.com/documentation/avfoundation/avassetwriter/1387863-canaddinput)

|  | Declaration |
| --- | --- |
| From | ``` func canAddInput(_ input: AVAssetWriterInput!) -> Bool ``` |
| To | ``` func canAddInput(_ input: AVAssetWriterInput) -> Bool ``` |

Modified [AVAssetWriter.canAddInputGroup(_: AVAssetWriterInputGroup) -> Bool](https://developer.apple.com/documentation/avfoundation/avassetwriter/1386698-canadd)

|  | Declaration |
| --- | --- |
| From | ``` func canAddInputGroup(_ inputGroup: AVAssetWriterInputGroup!) -> Bool ``` |
| To | ``` func canAddInputGroup(_ inputGroup: AVAssetWriterInputGroup) -> Bool ``` |

Modified [AVAssetWriter.canApplyOutputSettings(_: [String : AnyObject]?, forMediaType: String) -> Bool](https://developer.apple.com/documentation/avfoundation/avassetwriter/1388842-canapplyoutputsettings)

|  | Declaration |
| --- | --- |
| From | ``` func canApplyOutputSettings(_ outputSettings: [NSObject : AnyObject]!, forMediaType mediaType: String!) -> Bool ``` |
| To | ``` func canApplyOutputSettings(_ outputSettings: [String : AnyObject]?, forMediaType mediaType: String) -> Bool ``` |

Modified [AVAssetWriter.directoryForTemporaryFiles](https://developer.apple.com/documentation/avfoundation/avassetwriter/1387445-directoryfortemporaryfiles)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var directoryForTemporaryFiles: NSURL! ``` |
| To | ``` @NSCopying var directoryForTemporaryFiles: NSURL? ``` |

Modified [AVAssetWriter.error](https://developer.apple.com/documentation/avfoundation/avassetwriter/1390725-error)

|  | Declaration |
| --- | --- |
| From | ``` var error: NSError! { get } ``` |
| To | ``` var error: NSError? { get } ``` |

Modified [AVAssetWriter.finishWritingWithCompletionHandler(_: () -> Void)](https://developer.apple.com/documentation/avfoundation/avassetwriter/1390432-finishwritingwithcompletionhandl)

|  | Declaration |
| --- | --- |
| From | ``` func finishWritingWithCompletionHandler(_ handler: (() -> Void)!) ``` |
| To | ``` func finishWritingWithCompletionHandler(_ handler: () -> Void) ``` |

Modified [AVAssetWriter.init(URL: NSURL, fileType: String) throws](https://developer.apple.com/documentation/avfoundation/avassetwriter/1389201-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(URL outputURL: NSURL!, fileType outputFileType: String!, error outError: NSErrorPointer) ``` |
| To | ``` init(URL outputURL: NSURL, fileType outputFileType: String) throws ``` |

Modified [AVAssetWriter.inputGroups](https://developer.apple.com/documentation/avfoundation/avassetwriter/1388432-inputgroups)

|  | Declaration |
| --- | --- |
| From | ``` var inputGroups: [AnyObject]! { get } ``` |
| To | ``` var inputGroups: [AVAssetWriterInputGroup] { get } ``` |

Modified [AVAssetWriter.inputs](https://developer.apple.com/documentation/avfoundation/avassetwriter/1388264-inputs)

|  | Declaration |
| --- | --- |
| From | ``` var inputs: [AnyObject]! { get } ``` |
| To | ``` var inputs: [AVAssetWriterInput] { get } ``` |

Modified [AVAssetWriter.metadata](https://developer.apple.com/documentation/avfoundation/avassetwriter/1387974-metadata)

|  | Declaration |
| --- | --- |
| From | ``` var metadata: [AnyObject]! ``` |
| To | ``` var metadata: [AVMetadataItem] ``` |

Modified [AVAssetWriter.outputFileType](https://developer.apple.com/documentation/avfoundation/avassetwriter/1387349-outputfiletype)

|  | Declaration |
| --- | --- |
| From | ``` var outputFileType: String! { get } ``` |
| To | ``` var outputFileType: String { get } ``` |

Modified [AVAssetWriter.outputURL](https://developer.apple.com/documentation/avfoundation/avassetwriter/1387731-outputurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var outputURL: NSURL! { get } ``` |
| To | ``` @NSCopying var outputURL: NSURL { get } ``` |

Modified [AVAssetWriterInput](https://developer.apple.com/documentation/avfoundation/avassetwriterinput)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetWriterInput : NSObject {     init!(mediaType mediaType: String!, outputSettings outputSettings: [NSObject : AnyObject]!) -> AVAssetWriterInput     class func assetWriterInputWithMediaType(_ mediaType: String!, outputSettings outputSettings: [NSObject : AnyObject]!) -> AVAssetWriterInput!     init!(mediaType mediaType: String!, outputSettings outputSettings: [NSObject : AnyObject]!, sourceFormatHint sourceFormatHint: CMFormatDescription!) -> AVAssetWriterInput     class func assetWriterInputWithMediaType(_ mediaType: String!, outputSettings outputSettings: [NSObject : AnyObject]!, sourceFormatHint sourceFormatHint: CMFormatDescription!) -> AVAssetWriterInput!     init!(mediaType mediaType: String!, outputSettings outputSettings: [NSObject : AnyObject]!)     init!(mediaType mediaType: String!, outputSettings outputSettings: [NSObject : AnyObject]!, sourceFormatHint sourceFormatHint: CMFormatDescription!)     var mediaType: String! { get }     var outputSettings: [NSObject : AnyObject]! { get }     var sourceFormatHint: CMFormatDescription! { get }     var metadata: [AnyObject]!     var readyForMoreMediaData: Bool { get }     var expectsMediaDataInRealTime: Bool     func requestMediaDataWhenReadyOnQueue(_ queue: dispatch_queue_t!, usingBlock block: (() -> Void)!)     func appendSampleBuffer(_ sampleBuffer: CMSampleBuffer!) -> Bool     func markAsFinished() } extension AVAssetWriterInput {     var languageCode: String!     var extendedLanguageTag: String! } extension AVAssetWriterInput {     var naturalSize: CGSize     var transform: CGAffineTransform } extension AVAssetWriterInput {     var preferredVolume: Float } extension AVAssetWriterInput {     var marksOutputTrackAsEnabled: Bool     var mediaTimeScale: CMTimeScale     var preferredMediaChunkDuration: CMTime     var preferredMediaChunkAlignment: Int     @NSCopying var sampleReferenceBaseURL: NSURL! } extension AVAssetWriterInput {     func canAddTrackAssociationWithTrackOfInput(_ input: AVAssetWriterInput!, type trackAssociationType: String!) -> Bool     func addTrackAssociationWithTrackOfInput(_ input: AVAssetWriterInput!, type trackAssociationType: String!) } extension AVAssetWriterInput {     var performsMultiPassEncodingIfSupported: Bool     var canPerformMultiplePasses: Bool { get }     var currentPassDescription: AVAssetWriterInputPassDescription! { get }     func respondToEachPassDescriptionOnQueue(_ queue: dispatch_queue_t!, usingBlock block: dispatch_block_t!)     func markCurrentPassAsFinished() } ``` |
| To | ``` class AVAssetWriterInput : NSObject {     convenience init()     convenience init(mediaType mediaType: String, outputSettings outputSettings: [String : AnyObject]?)     class func assetWriterInputWithMediaType(_ mediaType: String, outputSettings outputSettings: [String : AnyObject]?) -> Self     convenience init(mediaType mediaType: String, outputSettings outputSettings: [String : AnyObject]?, sourceFormatHint sourceFormatHint: CMFormatDescription?)     class func assetWriterInputWithMediaType(_ mediaType: String, outputSettings outputSettings: [String : AnyObject]?, sourceFormatHint sourceFormatHint: CMFormatDescription?) -> Self     convenience init(mediaType mediaType: String, outputSettings outputSettings: [String : AnyObject]?)     init(mediaType mediaType: String, outputSettings outputSettings: [String : AnyObject]?, sourceFormatHint sourceFormatHint: CMFormatDescription?)     var mediaType: String { get }     var outputSettings: [String : AnyObject]? { get }     var sourceFormatHint: CMFormatDescription? { get }     var metadata: [AVMetadataItem]     var readyForMoreMediaData: Bool { get }     var expectsMediaDataInRealTime: Bool     func requestMediaDataWhenReadyOnQueue(_ queue: dispatch_queue_t, usingBlock block: () -> Void)     func appendSampleBuffer(_ sampleBuffer: CMSampleBuffer) -> Bool     func markAsFinished() } extension AVAssetWriterInput {     var languageCode: String?     var extendedLanguageTag: String? } extension AVAssetWriterInput {     var naturalSize: CGSize     var transform: CGAffineTransform } extension AVAssetWriterInput {     var preferredVolume: Float } extension AVAssetWriterInput {     var marksOutputTrackAsEnabled: Bool     var mediaTimeScale: CMTimeScale     var preferredMediaChunkDuration: CMTime     var preferredMediaChunkAlignment: Int     @NSCopying var sampleReferenceBaseURL: NSURL? } extension AVAssetWriterInput {     func canAddTrackAssociationWithTrackOfInput(_ input: AVAssetWriterInput, type trackAssociationType: String) -> Bool     func addTrackAssociationWithTrackOfInput(_ input: AVAssetWriterInput, type trackAssociationType: String) } extension AVAssetWriterInput {     var performsMultiPassEncodingIfSupported: Bool     var canPerformMultiplePasses: Bool { get }     var currentPassDescription: AVAssetWriterInputPassDescription? { get }     func respondToEachPassDescriptionOnQueue(_ queue: dispatch_queue_t, usingBlock block: dispatch_block_t)     func markCurrentPassAsFinished() } ``` |

Modified [AVAssetWriterInput.addTrackAssociationWithTrackOfInput(_: AVAssetWriterInput, type: String)](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1388347-addtrackassociationwithtrackofin)

|  | Declaration |
| --- | --- |
| From | ``` func addTrackAssociationWithTrackOfInput(_ input: AVAssetWriterInput!, type trackAssociationType: String!) ``` |
| To | ``` func addTrackAssociationWithTrackOfInput(_ input: AVAssetWriterInput, type trackAssociationType: String) ``` |

Modified [AVAssetWriterInput.appendSampleBuffer(_: CMSampleBuffer) -> Bool](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1389566-append)

|  | Declaration |
| --- | --- |
| From | ``` func appendSampleBuffer(_ sampleBuffer: CMSampleBuffer!) -> Bool ``` |
| To | ``` func appendSampleBuffer(_ sampleBuffer: CMSampleBuffer) -> Bool ``` |

Modified [AVAssetWriterInput.canAddTrackAssociationWithTrackOfInput(_: AVAssetWriterInput, type: String) -> Bool](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1388292-canaddtrackassociationwithtracko)

|  | Declaration |
| --- | --- |
| From | ``` func canAddTrackAssociationWithTrackOfInput(_ input: AVAssetWriterInput!, type trackAssociationType: String!) -> Bool ``` |
| To | ``` func canAddTrackAssociationWithTrackOfInput(_ input: AVAssetWriterInput, type trackAssociationType: String) -> Bool ``` |

Modified [AVAssetWriterInput.currentPassDescription](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1390627-currentpassdescription)

|  | Declaration |
| --- | --- |
| From | ``` var currentPassDescription: AVAssetWriterInputPassDescription! { get } ``` |
| To | ``` var currentPassDescription: AVAssetWriterInputPassDescription? { get } ``` |

Modified [AVAssetWriterInput.extendedLanguageTag](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1390768-extendedlanguagetag)

|  | Declaration |
| --- | --- |
| From | ``` var extendedLanguageTag: String! ``` |
| To | ``` var extendedLanguageTag: String? ``` |

Modified [AVAssetWriterInput.init(mediaType: String, outputSettings: [String : AnyObject]?)](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1385912-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(mediaType mediaType: String!, outputSettings outputSettings: [NSObject : AnyObject]!) ``` |
| To | ``` convenience init(mediaType mediaType: String, outputSettings outputSettings: [String : AnyObject]?) ``` |

Modified [AVAssetWriterInput.init(mediaType: String, outputSettings: [String : AnyObject]?, sourceFormatHint: CMFormatDescription?)](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1389994-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(mediaType mediaType: String!, outputSettings outputSettings: [NSObject : AnyObject]!, sourceFormatHint sourceFormatHint: CMFormatDescription!) ``` |
| To | ``` init(mediaType mediaType: String, outputSettings outputSettings: [String : AnyObject]?, sourceFormatHint sourceFormatHint: CMFormatDescription?) ``` |

Modified [AVAssetWriterInput.languageCode](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1388507-languagecode)

|  | Declaration |
| --- | --- |
| From | ``` var languageCode: String! ``` |
| To | ``` var languageCode: String? ``` |

Modified [AVAssetWriterInput.mediaType](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1385565-mediatype)

|  | Declaration |
| --- | --- |
| From | ``` var mediaType: String! { get } ``` |
| To | ``` var mediaType: String { get } ``` |

Modified [AVAssetWriterInput.metadata](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1386328-metadata)

|  | Declaration |
| --- | --- |
| From | ``` var metadata: [AnyObject]! ``` |
| To | ``` var metadata: [AVMetadataItem] ``` |

Modified [AVAssetWriterInput.outputSettings](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1388406-outputsettings)

|  | Declaration |
| --- | --- |
| From | ``` var outputSettings: [NSObject : AnyObject]! { get } ``` |
| To | ``` var outputSettings: [String : AnyObject]? { get } ``` |

Modified [AVAssetWriterInput.requestMediaDataWhenReadyOnQueue(_: dispatch_queue_t, usingBlock: () -> Void)](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1387508-requestmediadatawhenreadyonqueue)

|  | Declaration |
| --- | --- |
| From | ``` func requestMediaDataWhenReadyOnQueue(_ queue: dispatch_queue_t!, usingBlock block: (() -> Void)!) ``` |
| To | ``` func requestMediaDataWhenReadyOnQueue(_ queue: dispatch_queue_t, usingBlock block: () -> Void) ``` |

Modified [AVAssetWriterInput.respondToEachPassDescriptionOnQueue(_: dispatch_queue_t, usingBlock: dispatch_block_t)](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1388489-respondtoeachpassdescription)

|  | Declaration |
| --- | --- |
| From | ``` func respondToEachPassDescriptionOnQueue(_ queue: dispatch_queue_t!, usingBlock block: dispatch_block_t!) ``` |
| To | ``` func respondToEachPassDescriptionOnQueue(_ queue: dispatch_queue_t, usingBlock block: dispatch_block_t) ``` |

Modified [AVAssetWriterInput.sampleReferenceBaseURL](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1386316-samplereferencebaseurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var sampleReferenceBaseURL: NSURL! ``` |
| To | ``` @NSCopying var sampleReferenceBaseURL: NSURL? ``` |

Modified [AVAssetWriterInput.sourceFormatHint](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1387647-sourceformathint)

|  | Declaration |
| --- | --- |
| From | ``` var sourceFormatHint: CMFormatDescription! { get } ``` |
| To | ``` var sourceFormatHint: CMFormatDescription? { get } ``` |

Modified [AVAssetWriterInputGroup](https://developer.apple.com/documentation/avfoundation/avassetwriterinputgroup)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetWriterInputGroup : AVMediaSelectionGroup {     init!(inputs inputs: [AnyObject]!, defaultInput defaultInput: AVAssetWriterInput!) -> AVAssetWriterInputGroup     class func assetWriterInputGroupWithInputs(_ inputs: [AnyObject]!, defaultInput defaultInput: AVAssetWriterInput!) -> AVAssetWriterInputGroup!     init!(inputs inputs: [AnyObject]!, defaultInput defaultInput: AVAssetWriterInput!)     var inputs: [AnyObject]! { get }     var defaultInput: AVAssetWriterInput! { get } } ``` |
| To | ``` class AVAssetWriterInputGroup : AVMediaSelectionGroup {     convenience init()     convenience init(inputs inputs: [AVAssetWriterInput], defaultInput defaultInput: AVAssetWriterInput?)     class func assetWriterInputGroupWithInputs(_ inputs: [AVAssetWriterInput], defaultInput defaultInput: AVAssetWriterInput?) -> Self     init(inputs inputs: [AVAssetWriterInput], defaultInput defaultInput: AVAssetWriterInput?)     var inputs: [AVAssetWriterInput] { get }     var defaultInput: AVAssetWriterInput? { get } } ``` |

Modified [AVAssetWriterInputGroup.defaultInput](https://developer.apple.com/documentation/avfoundation/avassetwriterinputgroup/1389698-defaultinput)

|  | Declaration |
| --- | --- |
| From | ``` var defaultInput: AVAssetWriterInput! { get } ``` |
| To | ``` var defaultInput: AVAssetWriterInput? { get } ``` |

Modified [AVAssetWriterInputGroup.init(inputs: [AVAssetWriterInput], defaultInput: AVAssetWriterInput?)](https://developer.apple.com/documentation/avfoundation/avassetwriterinputgroup/1389502-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(inputs inputs: [AnyObject]!, defaultInput defaultInput: AVAssetWriterInput!) ``` |
| To | ``` init(inputs inputs: [AVAssetWriterInput], defaultInput defaultInput: AVAssetWriterInput?) ``` |

Modified [AVAssetWriterInputGroup.inputs](https://developer.apple.com/documentation/avfoundation/avassetwriterinputgroup/1388226-inputs)

|  | Declaration |
| --- | --- |
| From | ``` var inputs: [AnyObject]! { get } ``` |
| To | ``` var inputs: [AVAssetWriterInput] { get } ``` |

Modified [AVAssetWriterInputMetadataAdaptor](https://developer.apple.com/documentation/avfoundation/avassetwriterinputmetadataadaptor)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetWriterInputMetadataAdaptor : NSObject {     convenience init!(assetWriterInput input: AVAssetWriterInput!)     class func assetWriterInputMetadataAdaptorWithAssetWriterInput(_ input: AVAssetWriterInput!) -> Self!     init!(assetWriterInput input: AVAssetWriterInput!)     var assetWriterInput: AVAssetWriterInput! { get }     func appendTimedMetadataGroup(_ timedMetadataGroup: AVTimedMetadataGroup!) -> Bool } ``` |
| To | ``` class AVAssetWriterInputMetadataAdaptor : NSObject {     convenience init()     convenience init(assetWriterInput input: AVAssetWriterInput)     class func assetWriterInputMetadataAdaptorWithAssetWriterInput(_ input: AVAssetWriterInput) -> Self     init(assetWriterInput input: AVAssetWriterInput)     var assetWriterInput: AVAssetWriterInput { get }     func appendTimedMetadataGroup(_ timedMetadataGroup: AVTimedMetadataGroup) -> Bool } ``` |

Modified [AVAssetWriterInputMetadataAdaptor.appendTimedMetadataGroup(_: AVTimedMetadataGroup) -> Bool](https://developer.apple.com/documentation/avfoundation/avassetwriterinputmetadataadaptor/1389014-append)

|  | Declaration |
| --- | --- |
| From | ``` func appendTimedMetadataGroup(_ timedMetadataGroup: AVTimedMetadataGroup!) -> Bool ``` |
| To | ``` func appendTimedMetadataGroup(_ timedMetadataGroup: AVTimedMetadataGroup) -> Bool ``` |

Modified [AVAssetWriterInputMetadataAdaptor.assetWriterInput](https://developer.apple.com/documentation/avfoundation/avassetwriterinputmetadataadaptor/1386633-assetwriterinput)

|  | Declaration |
| --- | --- |
| From | ``` var assetWriterInput: AVAssetWriterInput! { get } ``` |
| To | ``` var assetWriterInput: AVAssetWriterInput { get } ``` |

Modified [AVAssetWriterInputMetadataAdaptor.init(assetWriterInput: AVAssetWriterInput)](https://developer.apple.com/documentation/avfoundation/avassetwriterinputmetadataadaptor/1389706-initwithassetwriterinput)

|  | Declaration |
| --- | --- |
| From | ``` init!(assetWriterInput input: AVAssetWriterInput!) ``` |
| To | ``` init(assetWriterInput input: AVAssetWriterInput) ``` |

Modified [AVAssetWriterInputPassDescription](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpassdescription)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetWriterInputPassDescription : NSObject {     var sourceTimeRanges: [AnyObject]! { get } } ``` |
| To | ``` class AVAssetWriterInputPassDescription : NSObject {     init()     var sourceTimeRanges: [NSValue] { get } } ``` |

Modified [AVAssetWriterInputPassDescription.sourceTimeRanges](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpassdescription/1388732-sourcetimeranges)

|  | Declaration |
| --- | --- |
| From | ``` var sourceTimeRanges: [AnyObject]! { get } ``` |
| To | ``` var sourceTimeRanges: [NSValue] { get } ``` |

Modified [AVAssetWriterInputPixelBufferAdaptor](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor)

|  | Declaration |
| --- | --- |
| From | ``` class AVAssetWriterInputPixelBufferAdaptor : NSObject {     convenience init!(assetWriterInput input: AVAssetWriterInput!, sourcePixelBufferAttributes sourcePixelBufferAttributes: [NSObject : AnyObject]!)     class func assetWriterInputPixelBufferAdaptorWithAssetWriterInput(_ input: AVAssetWriterInput!, sourcePixelBufferAttributes sourcePixelBufferAttributes: [NSObject : AnyObject]!) -> Self!     init!(assetWriterInput input: AVAssetWriterInput!, sourcePixelBufferAttributes sourcePixelBufferAttributes: [NSObject : AnyObject]!)     var assetWriterInput: AVAssetWriterInput! { get }     var sourcePixelBufferAttributes: [NSObject : AnyObject]! { get }     var pixelBufferPool: CVPixelBufferPool! { get }     func appendPixelBuffer(_ pixelBuffer: CVPixelBuffer!, withPresentationTime presentationTime: CMTime) -> Bool } ``` |
| To | ``` class AVAssetWriterInputPixelBufferAdaptor : NSObject {     convenience init()     convenience init(assetWriterInput input: AVAssetWriterInput, sourcePixelBufferAttributes sourcePixelBufferAttributes: [String : AnyObject]?)     class func assetWriterInputPixelBufferAdaptorWithAssetWriterInput(_ input: AVAssetWriterInput, sourcePixelBufferAttributes sourcePixelBufferAttributes: [String : AnyObject]?) -> Self     init(assetWriterInput input: AVAssetWriterInput, sourcePixelBufferAttributes sourcePixelBufferAttributes: [String : AnyObject]?)     var assetWriterInput: AVAssetWriterInput { get }     var sourcePixelBufferAttributes: [String : AnyObject]? { get }     var pixelBufferPool: CVPixelBufferPool? { get }     func appendPixelBuffer(_ pixelBuffer: CVPixelBuffer, withPresentationTime presentationTime: CMTime) -> Bool } ``` |

Modified [AVAssetWriterInputPixelBufferAdaptor.appendPixelBuffer(_: CVPixelBuffer, withPresentationTime: CMTime) -> Bool](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/1388102-appendpixelbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func appendPixelBuffer(_ pixelBuffer: CVPixelBuffer!, withPresentationTime presentationTime: CMTime) -> Bool ``` |
| To | ``` func appendPixelBuffer(_ pixelBuffer: CVPixelBuffer, withPresentationTime presentationTime: CMTime) -> Bool ``` |

Modified [AVAssetWriterInputPixelBufferAdaptor.assetWriterInput](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/1387565-assetwriterinput)

|  | Declaration |
| --- | --- |
| From | ``` var assetWriterInput: AVAssetWriterInput! { get } ``` |
| To | ``` var assetWriterInput: AVAssetWriterInput { get } ``` |

Modified [AVAssetWriterInputPixelBufferAdaptor.init(assetWriterInput: AVAssetWriterInput, sourcePixelBufferAttributes: [String : AnyObject]?)](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/1390639-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(assetWriterInput input: AVAssetWriterInput!, sourcePixelBufferAttributes sourcePixelBufferAttributes: [NSObject : AnyObject]!) ``` |
| To | ``` init(assetWriterInput input: AVAssetWriterInput, sourcePixelBufferAttributes sourcePixelBufferAttributes: [String : AnyObject]?) ``` |

Modified [AVAssetWriterInputPixelBufferAdaptor.pixelBufferPool](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/1389662-pixelbufferpool)

|  | Declaration |
| --- | --- |
| From | ``` var pixelBufferPool: CVPixelBufferPool! { get } ``` |
| To | ``` var pixelBufferPool: CVPixelBufferPool? { get } ``` |

Modified [AVAssetWriterInputPixelBufferAdaptor.sourcePixelBufferAttributes](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/1387829-sourcepixelbufferattributes)

|  | Declaration |
| --- | --- |
| From | ``` var sourcePixelBufferAttributes: [NSObject : AnyObject]! { get } ``` |
| To | ``` var sourcePixelBufferAttributes: [String : AnyObject]? { get } ``` |

Modified [AVAssetWriterStatus [enum]](https://developer.apple.com/documentation/avfoundation/avassetwriter/status)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVAsynchronousKeyValueLoading](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVAsynchronousKeyValueLoading {     func statusOfValueForKey(_ key: String!, error outError: NSErrorPointer) -> AVKeyValueStatus     func loadValuesAsynchronouslyForKeys(_ keys: [AnyObject]!, completionHandler handler: (() -> Void)!) } ``` |
| To | ``` protocol AVAsynchronousKeyValueLoading {     func statusOfValueForKey(_ key: String, error outError: NSErrorPointer) -> AVKeyValueStatus     func loadValuesAsynchronouslyForKeys(_ keys: [String], completionHandler handler: (() -> Void)?) } ``` |

Modified [AVAsynchronousKeyValueLoading.loadValuesAsynchronouslyForKeys(_: [String], completionHandler: (() -> Void)?)](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/1387321-loadvaluesasynchronouslyforkeys)

|  | Declaration |
| --- | --- |
| From | ``` func loadValuesAsynchronouslyForKeys(_ keys: [AnyObject]!, completionHandler handler: (() -> Void)!) ``` |
| To | ``` func loadValuesAsynchronouslyForKeys(_ keys: [String], completionHandler handler: (() -> Void)?) ``` |

Modified [AVAsynchronousKeyValueLoading.statusOfValueForKey(_: String, error: NSErrorPointer) -> AVKeyValueStatus](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/1386816-statusofvalue)

|  | Declaration |
| --- | --- |
| From | ``` func statusOfValueForKey(_ key: String!, error outError: NSErrorPointer) -> AVKeyValueStatus ``` |
| To | ``` func statusOfValueForKey(_ key: String, error outError: NSErrorPointer) -> AVKeyValueStatus ``` |

Modified [AVAsynchronousVideoCompositionRequest](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest)

|  | Declaration |
| --- | --- |
| From | ``` class AVAsynchronousVideoCompositionRequest : NSObject, NSCopying {     var renderContext: AVVideoCompositionRenderContext! { get }     var compositionTime: CMTime { get }     var sourceTrackIDs: [AnyObject]! { get }     var videoCompositionInstruction: AVVideoCompositionInstructionProtocol! { get }     func sourceFrameByTrackID(_ trackID: CMPersistentTrackID) -> Unmanaged<CVPixelBuffer>!     func finishWithComposedVideoFrame(_ composedVideoFrame: CVPixelBuffer!)     func finishWithError(_ error: NSError!)     func finishCancelledRequest() } ``` |
| To | ``` class AVAsynchronousVideoCompositionRequest : NSObject, NSCopying {     var renderContext: AVVideoCompositionRenderContext { get }     var compositionTime: CMTime { get }     var sourceTrackIDs: [NSNumber] { get }     var videoCompositionInstruction: AVVideoCompositionInstructionProtocol { get }     func sourceFrameByTrackID(_ trackID: CMPersistentTrackID) -> CVPixelBuffer?     func finishWithComposedVideoFrame(_ composedVideoFrame: CVPixelBuffer)     func finishWithError(_ error: NSError)     func finishCancelledRequest() } ``` |

Modified [AVAsynchronousVideoCompositionRequest.finishWithComposedVideoFrame(_: CVPixelBuffer)](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1387450-finishwithcomposedvideoframe)

|  | Declaration |
| --- | --- |
| From | ``` func finishWithComposedVideoFrame(_ composedVideoFrame: CVPixelBuffer!) ``` |
| To | ``` func finishWithComposedVideoFrame(_ composedVideoFrame: CVPixelBuffer) ``` |

Modified [AVAsynchronousVideoCompositionRequest.finishWithError(_: NSError)](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1390797-finishwitherror)

|  | Declaration |
| --- | --- |
| From | ``` func finishWithError(_ error: NSError!) ``` |
| To | ``` func finishWithError(_ error: NSError) ``` |

Modified [AVAsynchronousVideoCompositionRequest.renderContext](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1389112-rendercontext)

|  | Declaration |
| --- | --- |
| From | ``` var renderContext: AVVideoCompositionRenderContext! { get } ``` |
| To | ``` var renderContext: AVVideoCompositionRenderContext { get } ``` |

Modified [AVAsynchronousVideoCompositionRequest.sourceFrameByTrackID(_: CMPersistentTrackID) -> CVPixelBuffer?](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1390379-sourceframebytrackid)

|  | Declaration |
| --- | --- |
| From | ``` func sourceFrameByTrackID(_ trackID: CMPersistentTrackID) -> Unmanaged<CVPixelBuffer>! ``` |
| To | ``` func sourceFrameByTrackID(_ trackID: CMPersistentTrackID) -> CVPixelBuffer? ``` |

Modified [AVAsynchronousVideoCompositionRequest.sourceTrackIDs](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1388898-sourcetrackids)

|  | Declaration |
| --- | --- |
| From | ``` var sourceTrackIDs: [AnyObject]! { get } ``` |
| To | ``` var sourceTrackIDs: [NSNumber] { get } ``` |

Modified [AVAsynchronousVideoCompositionRequest.videoCompositionInstruction](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1386672-videocompositioninstruction)

|  | Declaration |
| --- | --- |
| From | ``` var videoCompositionInstruction: AVVideoCompositionInstructionProtocol! { get } ``` |
| To | ``` var videoCompositionInstruction: AVVideoCompositionInstructionProtocol { get } ``` |

Modified [AVAudio3DMixingRenderingAlgorithm [enum]](https://developer.apple.com/documentation/avfoundation/avaudio3dmixingrenderingalgorithm)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVAudioBuffer](https://developer.apple.com/documentation/avfoundation/avaudiobuffer)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioBuffer : NSObject, NSCopying, NSMutableCopying {     var format: AVAudioFormat! { get }     var audioBufferList: UnsafePointer<AudioBufferList> { get }     var mutableAudioBufferList: UnsafeMutablePointer<AudioBufferList> { get } } ``` |
| To | ``` class AVAudioBuffer : NSObject, NSCopying, NSMutableCopying {     var format: AVAudioFormat { get }     var audioBufferList: UnsafePointer<AudioBufferList> { get }     var mutableAudioBufferList: UnsafeMutablePointer<AudioBufferList> { get } } ``` |

Modified [AVAudioBuffer.format](https://developer.apple.com/documentation/avfoundation/avaudiobuffer/1387540-format)

|  | Declaration |
| --- | --- |
| From | ``` var format: AVAudioFormat! { get } ``` |
| To | ``` var format: AVAudioFormat { get } ``` |

Modified [AVAudioChannelLayout](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioChannelLayout : NSObject {     init!(layoutTag layoutTag: AudioChannelLayoutTag)     init!(layout layout: UnsafePointer<AudioChannelLayout>)     func isEqual(_ object: AnyObject!) -> Bool     class func layoutWithLayoutTag(_ layoutTag: AudioChannelLayoutTag) -> Self!     class func layoutWithLayout(_ layout: UnsafePointer<AudioChannelLayout>) -> Self!     var layoutTag: AudioChannelLayoutTag { get }     var layout: UnsafePointer<AudioChannelLayout> { get }     var channelCount: AVAudioChannelCount { get } } ``` | AnyObject |
| To | ``` class AVAudioChannelLayout : NSObject, NSSecureCoding, NSCoding {     convenience init(layoutTag layoutTag: AudioChannelLayoutTag)     init(layout layout: UnsafePointer<AudioChannelLayout>)     func isEqual(_ object: AnyObject) -> Bool     class func layoutWithLayoutTag(_ layoutTag: AudioChannelLayoutTag) -> Self     class func layoutWithLayout(_ layout: UnsafePointer<AudioChannelLayout>) -> Self     var layoutTag: AudioChannelLayoutTag { get }     var layout: UnsafePointer<AudioChannelLayout> { get }     var channelCount: AVAudioChannelCount { get } } ``` | AnyObject, NSCoding, NSSecureCoding |

Modified [AVAudioChannelLayout.init(layout: UnsafePointer<AudioChannelLayout>)](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1387623-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(layout layout: UnsafePointer<AudioChannelLayout>) ``` |
| To | ``` init(layout layout: UnsafePointer<AudioChannelLayout>) ``` |

Modified [AVAudioChannelLayout.init(layoutTag: AudioChannelLayoutTag)](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1388320-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(layoutTag layoutTag: AudioChannelLayoutTag) ``` |
| To | ``` convenience init(layoutTag layoutTag: AudioChannelLayoutTag) ``` |

Modified [AVAudioChannelLayout.isEqual(_: AnyObject) -> Bool](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1389677-isequal)

|  | Declaration |
| --- | --- |
| From | ``` func isEqual(_ object: AnyObject!) -> Bool ``` |
| To | ``` func isEqual(_ object: AnyObject) -> Bool ``` |

Modified [AVAudioCommonFormat [enum]](https://developer.apple.com/documentation/avfoundation/avaudiocommonformat)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [AVAudioEngine](https://developer.apple.com/documentation/avfoundation/avaudioengine)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioEngine : NSObject {     init!()     func attachNode(_ node: AVAudioNode!)     func detachNode(_ node: AVAudioNode!)     func connect(_ node1: AVAudioNode!, to node2: AVAudioNode!, fromBus bus1: AVAudioNodeBus, toBus bus2: AVAudioNodeBus, format format: AVAudioFormat!)     func connect(_ node1: AVAudioNode!, to node2: AVAudioNode!, format format: AVAudioFormat!)     func disconnectNodeInput(_ node: AVAudioNode!, bus bus: AVAudioNodeBus)     func disconnectNodeInput(_ node: AVAudioNode!)     func disconnectNodeOutput(_ node: AVAudioNode!, bus bus: AVAudioNodeBus)     func disconnectNodeOutput(_ node: AVAudioNode!)     func prepare()     func startAndReturnError(_ outError: NSErrorPointer) -> Bool     func pause()     func reset()     func stop()     var musicSequence: MusicSequence     var outputNode: AVAudioOutputNode! { get }     var inputNode: AVAudioInputNode! { get }     var mainMixerNode: AVAudioMixerNode! { get }     var running: Bool { get } } ``` |
| To | ``` class AVAudioEngine : NSObject {     init()     func attachNode(_ node: AVAudioNode)     func detachNode(_ node: AVAudioNode)     func connect(_ node1: AVAudioNode, to node2: AVAudioNode, fromBus bus1: AVAudioNodeBus, toBus bus2: AVAudioNodeBus, format format: AVAudioFormat?)     func connect(_ node1: AVAudioNode, to node2: AVAudioNode, format format: AVAudioFormat?)     func connect(_ sourceNode: AVAudioNode, toConnectionPoints destNodes: [AVAudioConnectionPoint], fromBus sourceBus: AVAudioNodeBus, format format: AVAudioFormat?)     func disconnectNodeInput(_ node: AVAudioNode, bus bus: AVAudioNodeBus)     func disconnectNodeInput(_ node: AVAudioNode)     func disconnectNodeOutput(_ node: AVAudioNode, bus bus: AVAudioNodeBus)     func disconnectNodeOutput(_ node: AVAudioNode)     func prepare()     func start() throws     func pause()     func reset()     func stop()     func inputConnectionPointForNode(_ node: AVAudioNode, inputBus bus: AVAudioNodeBus) -> AVAudioConnectionPoint?     func outputConnectionPointsForNode(_ node: AVAudioNode, outputBus bus: AVAudioNodeBus) -> [AVAudioConnectionPoint]     var musicSequence: MusicSequence     var outputNode: AVAudioOutputNode { get }     var inputNode: AVAudioInputNode? { get }     var mainMixerNode: AVAudioMixerNode { get }     var running: Bool { get } } ``` |

Modified [AVAudioEngine.attachNode(_: AVAudioNode)](https://developer.apple.com/documentation/avfoundation/avaudioengine/1390685-attachnode)

|  | Declaration |
| --- | --- |
| From | ``` func attachNode(_ node: AVAudioNode!) ``` |
| To | ``` func attachNode(_ node: AVAudioNode) ``` |

Modified [AVAudioEngine.connect(_: AVAudioNode, to: AVAudioNode, format: AVAudioFormat?)](https://developer.apple.com/documentation/avfoundation/avaudioengine/1388974-connect)

|  | Declaration |
| --- | --- |
| From | ``` func connect(_ node1: AVAudioNode!, to node2: AVAudioNode!, format format: AVAudioFormat!) ``` |
| To | ``` func connect(_ node1: AVAudioNode, to node2: AVAudioNode, format format: AVAudioFormat?) ``` |

Modified [AVAudioEngine.connect(_: AVAudioNode, to: AVAudioNode, fromBus: AVAudioNodeBus, toBus: AVAudioNodeBus, format: AVAudioFormat?)](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389776-connect)

|  | Declaration |
| --- | --- |
| From | ``` func connect(_ node1: AVAudioNode!, to node2: AVAudioNode!, fromBus bus1: AVAudioNodeBus, toBus bus2: AVAudioNodeBus, format format: AVAudioFormat!) ``` |
| To | ``` func connect(_ node1: AVAudioNode, to node2: AVAudioNode, fromBus bus1: AVAudioNodeBus, toBus bus2: AVAudioNodeBus, format format: AVAudioFormat?) ``` |

Modified [AVAudioEngine.detachNode(_: AVAudioNode)](https://developer.apple.com/documentation/avfoundation/avaudioengine/1388198-detachnode)

|  | Declaration |
| --- | --- |
| From | ``` func detachNode(_ node: AVAudioNode!) ``` |
| To | ``` func detachNode(_ node: AVAudioNode) ``` |

Modified [AVAudioEngine.disconnectNodeInput(_: AVAudioNode)](https://developer.apple.com/documentation/avfoundation/avaudioengine/1388181-disconnectnodeinput)

|  | Declaration |
| --- | --- |
| From | ``` func disconnectNodeInput(_ node: AVAudioNode!) ``` |
| To | ``` func disconnectNodeInput(_ node: AVAudioNode) ``` |

Modified [AVAudioEngine.disconnectNodeInput(_: AVAudioNode, bus: AVAudioNodeBus)](https://developer.apple.com/documentation/avfoundation/avaudioengine/1387251-disconnectnodeinput)

|  | Declaration |
| --- | --- |
| From | ``` func disconnectNodeInput(_ node: AVAudioNode!, bus bus: AVAudioNodeBus) ``` |
| To | ``` func disconnectNodeInput(_ node: AVAudioNode, bus bus: AVAudioNodeBus) ``` |

Modified [AVAudioEngine.disconnectNodeOutput(_: AVAudioNode)](https://developer.apple.com/documentation/avfoundation/avaudioengine/1386992-disconnectnodeoutput)

|  | Declaration |
| --- | --- |
| From | ``` func disconnectNodeOutput(_ node: AVAudioNode!) ``` |
| To | ``` func disconnectNodeOutput(_ node: AVAudioNode) ``` |

Modified [AVAudioEngine.disconnectNodeOutput(_: AVAudioNode, bus: AVAudioNodeBus)](https://developer.apple.com/documentation/avfoundation/avaudioengine/1390352-disconnectnodeoutput)

|  | Declaration |
| --- | --- |
| From | ``` func disconnectNodeOutput(_ node: AVAudioNode!, bus bus: AVAudioNodeBus) ``` |
| To | ``` func disconnectNodeOutput(_ node: AVAudioNode, bus bus: AVAudioNodeBus) ``` |

Modified [AVAudioEngine.init()](https://developer.apple.com/documentation/avfoundation/avaudioengine/1390381-init)

|  | Declaration |
| --- | --- |
| From | ``` init!() ``` |
| To | ``` init() ``` |

Modified [AVAudioEngine.inputNode](https://developer.apple.com/documentation/avfoundation/avaudioengine/1386063-inputnode)

|  | Declaration |
| --- | --- |
| From | ``` var inputNode: AVAudioInputNode! { get } ``` |
| To | ``` var inputNode: AVAudioInputNode? { get } ``` |

Modified [AVAudioEngine.mainMixerNode](https://developer.apple.com/documentation/avfoundation/avaudioengine/1385813-mainmixernode)

|  | Declaration |
| --- | --- |
| From | ``` var mainMixerNode: AVAudioMixerNode! { get } ``` |
| To | ``` var mainMixerNode: AVAudioMixerNode { get } ``` |

Modified [AVAudioEngine.outputNode](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389103-outputnode)

|  | Declaration |
| --- | --- |
| From | ``` var outputNode: AVAudioOutputNode! { get } ``` |
| To | ``` var outputNode: AVAudioOutputNode { get } ``` |

Modified [AVAudioEngine.start() throws](https://developer.apple.com/documentation/avfoundation/avaudioengine/1387024-start)

|  | Declaration |
| --- | --- |
| From | ``` func startAndReturnError(_ outError: NSErrorPointer) -> Bool ``` |
| To | ``` func start() throws ``` |

Modified [AVAudioEnvironmentDistanceAttenuationModel [enum]](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationmodel)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVAudioEnvironmentNode](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioEnvironmentNode : AVAudioNode, AVAudioMixing, AVAudioStereoMixing, NSObjectProtocol, AVAudio3DMixing {     var outputVolume: Float     var nextAvailableInputBus: AVAudioNodeBus { get }     var listenerPosition: AVAudio3DPoint     var listenerVectorOrientation: AVAudio3DVectorOrientation     var listenerAngularOrientation: AVAudio3DAngularOrientation     var distanceAttenuationParameters: AVAudioEnvironmentDistanceAttenuationParameters! { get }     var reverbParameters: AVAudioEnvironmentReverbParameters! { get }     func applicableRenderingAlgorithms() -> [AnyObject]! } ``` |
| To | ``` class AVAudioEnvironmentNode : AVAudioNode, AVAudioMixing, AVAudioStereoMixing, AVAudio3DMixing {     var outputVolume: Float     var nextAvailableInputBus: AVAudioNodeBus { get }     var listenerPosition: AVAudio3DPoint     var listenerVectorOrientation: AVAudio3DVectorOrientation     var listenerAngularOrientation: AVAudio3DAngularOrientation     var distanceAttenuationParameters: AVAudioEnvironmentDistanceAttenuationParameters { get }     var reverbParameters: AVAudioEnvironmentReverbParameters { get }     var applicableRenderingAlgorithms: [NSNumber] { get } } ``` |

Modified [AVAudioEnvironmentNode.distanceAttenuationParameters](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1387396-distanceattenuationparameters)

|  | Declaration |
| --- | --- |
| From | ``` var distanceAttenuationParameters: AVAudioEnvironmentDistanceAttenuationParameters! { get } ``` |
| To | ``` var distanceAttenuationParameters: AVAudioEnvironmentDistanceAttenuationParameters { get } ``` |

Modified [AVAudioEnvironmentNode.reverbParameters](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1389020-reverbparameters)

|  | Declaration |
| --- | --- |
| From | ``` var reverbParameters: AVAudioEnvironmentReverbParameters! { get } ``` |
| To | ``` var reverbParameters: AVAudioEnvironmentReverbParameters { get } ``` |

Modified [AVAudioEnvironmentReverbParameters](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentreverbparameters)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioEnvironmentReverbParameters : NSObject {     var enable: Bool     var level: Float     var filterParameters: AVAudioUnitEQFilterParameters! { get }     func loadFactoryReverbPreset(_ preset: AVAudioUnitReverbPreset) } ``` |
| To | ``` class AVAudioEnvironmentReverbParameters : NSObject {     var enable: Bool     var level: Float     var filterParameters: AVAudioUnitEQFilterParameters { get }     func loadFactoryReverbPreset(_ preset: AVAudioUnitReverbPreset) } ``` |

Modified [AVAudioEnvironmentReverbParameters.filterParameters](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentreverbparameters/1387313-filterparameters)

|  | Declaration |
| --- | --- |
| From | ``` var filterParameters: AVAudioUnitEQFilterParameters! { get } ``` |
| To | ``` var filterParameters: AVAudioUnitEQFilterParameters { get } ``` |

Modified [AVAudioFile](https://developer.apple.com/documentation/avfoundation/avaudiofile)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioFile : NSObject {     init!(forReading fileURL: NSURL!, error outError: NSErrorPointer)     init!(forReading fileURL: NSURL!, commonFormat format: AVAudioCommonFormat, interleaved interleaved: Bool, error outError: NSErrorPointer)     init!(forWriting fileURL: NSURL!, settings settings: [NSObject : AnyObject]!, error outError: NSErrorPointer)     init!(forWriting fileURL: NSURL!, settings settings: [NSObject : AnyObject]!, commonFormat format: AVAudioCommonFormat, interleaved interleaved: Bool, error outError: NSErrorPointer)     func readIntoBuffer(_ buffer: AVAudioPCMBuffer!, error outError: NSErrorPointer) -> Bool     func readIntoBuffer(_ buffer: AVAudioPCMBuffer!, frameCount frames: AVAudioFrameCount, error outError: NSErrorPointer) -> Bool     func writeFromBuffer(_ buffer: AVAudioPCMBuffer!, error outError: NSErrorPointer) -> Bool     var url: NSURL! { get }     var fileFormat: AVAudioFormat! { get }     var processingFormat: AVAudioFormat! { get }     var length: AVAudioFramePosition { get }     var framePosition: AVAudioFramePosition } ``` |
| To | ``` class AVAudioFile : NSObject {     init(forReading fileURL: NSURL) throws     init(forReading fileURL: NSURL, commonFormat format: AVAudioCommonFormat, interleaved interleaved: Bool) throws     init(forWriting fileURL: NSURL, settings settings: [String : AnyObject]) throws     init(forWriting fileURL: NSURL, settings settings: [String : AnyObject], commonFormat format: AVAudioCommonFormat, interleaved interleaved: Bool) throws     func readIntoBuffer(_ buffer: AVAudioPCMBuffer) throws     func readIntoBuffer(_ buffer: AVAudioPCMBuffer, frameCount frames: AVAudioFrameCount) throws     func writeFromBuffer(_ buffer: AVAudioPCMBuffer) throws     var url: NSURL { get }     var fileFormat: AVAudioFormat { get }     var processingFormat: AVAudioFormat { get }     var length: AVAudioFramePosition { get }     var framePosition: AVAudioFramePosition } ``` |

Modified [AVAudioFile.fileFormat](https://developer.apple.com/documentation/avfoundation/avaudiofile/1387096-fileformat)

|  | Declaration |
| --- | --- |
| From | ``` var fileFormat: AVAudioFormat! { get } ``` |
| To | ``` var fileFormat: AVAudioFormat { get } ``` |

Modified [AVAudioFile.init(forReading: NSURL) throws](https://developer.apple.com/documentation/avfoundation/avaudiofile/1388218-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(forReading fileURL: NSURL!, error outError: NSErrorPointer) ``` |
| To | ``` init(forReading fileURL: NSURL) throws ``` |

Modified [AVAudioFile.init(forReading: NSURL, commonFormat: AVAudioCommonFormat, interleaved: Bool) throws](https://developer.apple.com/documentation/avfoundation/avaudiofile/1387283-initforreading)

|  | Declaration |
| --- | --- |
| From | ``` init!(forReading fileURL: NSURL!, commonFormat format: AVAudioCommonFormat, interleaved interleaved: Bool, error outError: NSErrorPointer) ``` |
| To | ``` init(forReading fileURL: NSURL, commonFormat format: AVAudioCommonFormat, interleaved interleaved: Bool) throws ``` |

Modified [AVAudioFile.init(forWriting: NSURL, settings: [String : AnyObject]) throws](https://developer.apple.com/documentation/avfoundation/avaudiofile/1390840-initforwriting)

|  | Declaration |
| --- | --- |
| From | ``` init!(forWriting fileURL: NSURL!, settings settings: [NSObject : AnyObject]!, error outError: NSErrorPointer) ``` |
| To | ``` init(forWriting fileURL: NSURL, settings settings: [String : AnyObject]) throws ``` |

Modified [AVAudioFile.init(forWriting: NSURL, settings: [String : AnyObject], commonFormat: AVAudioCommonFormat, interleaved: Bool) throws](https://developer.apple.com/documentation/avfoundation/avaudiofile/1387154-initforwriting)

|  | Declaration |
| --- | --- |
| From | ``` init!(forWriting fileURL: NSURL!, settings settings: [NSObject : AnyObject]!, commonFormat format: AVAudioCommonFormat, interleaved interleaved: Bool, error outError: NSErrorPointer) ``` |
| To | ``` init(forWriting fileURL: NSURL, settings settings: [String : AnyObject], commonFormat format: AVAudioCommonFormat, interleaved interleaved: Bool) throws ``` |

Modified [AVAudioFile.processingFormat](https://developer.apple.com/documentation/avfoundation/avaudiofile/1388308-processingformat)

|  | Declaration |
| --- | --- |
| From | ``` var processingFormat: AVAudioFormat! { get } ``` |
| To | ``` var processingFormat: AVAudioFormat { get } ``` |

Modified [AVAudioFile.readIntoBuffer(_: AVAudioPCMBuffer) throws](https://developer.apple.com/documentation/avfoundation/avaudiofile/1388043-read)

|  | Declaration |
| --- | --- |
| From | ``` func readIntoBuffer(_ buffer: AVAudioPCMBuffer!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func readIntoBuffer(_ buffer: AVAudioPCMBuffer) throws ``` |

Modified [AVAudioFile.readIntoBuffer(_: AVAudioPCMBuffer, frameCount: AVAudioFrameCount) throws](https://developer.apple.com/documentation/avfoundation/avaudiofile/1389774-read)

|  | Declaration |
| --- | --- |
| From | ``` func readIntoBuffer(_ buffer: AVAudioPCMBuffer!, frameCount frames: AVAudioFrameCount, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func readIntoBuffer(_ buffer: AVAudioPCMBuffer, frameCount frames: AVAudioFrameCount) throws ``` |

Modified [AVAudioFile.url](https://developer.apple.com/documentation/avfoundation/avaudiofile/1387360-url)

|  | Declaration |
| --- | --- |
| From | ``` var url: NSURL! { get } ``` |
| To | ``` var url: NSURL { get } ``` |

Modified [AVAudioFile.writeFromBuffer(_: AVAudioPCMBuffer) throws](https://developer.apple.com/documentation/avfoundation/avaudiofile/1385637-write)

|  | Declaration |
| --- | --- |
| From | ``` func writeFromBuffer(_ buffer: AVAudioPCMBuffer!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func writeFromBuffer(_ buffer: AVAudioPCMBuffer) throws ``` |

Modified [AVAudioFormat](https://developer.apple.com/documentation/avfoundation/avaudioformat)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioFormat : NSObject {     init!(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>)     init!(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>, channelLayout layout: AVAudioChannelLayout!)     init!(standardFormatWithSampleRate sampleRate: Double, channels channels: AVAudioChannelCount)     init!(standardFormatWithSampleRate sampleRate: Double, channelLayout layout: AVAudioChannelLayout!)     init!(commonFormat format: AVAudioCommonFormat, sampleRate sampleRate: Double, channels channels: AVAudioChannelCount, interleaved interleaved: Bool)     init!(commonFormat format: AVAudioCommonFormat, sampleRate sampleRate: Double, interleaved interleaved: Bool, channelLayout layout: AVAudioChannelLayout!)     init!(settings settings: [NSObject : AnyObject]!)     func isEqual(_ object: AnyObject!) -> Bool     var standard: Bool { get }     var commonFormat: AVAudioCommonFormat { get }     var channelCount: AVAudioChannelCount { get }     var sampleRate: Double { get }     var interleaved: Bool { get }     var streamDescription: UnsafePointer<AudioStreamBasicDescription> { get }     var channelLayout: AVAudioChannelLayout! { get }     var settings: [NSObject : AnyObject]! { get } } ``` | AnyObject |
| To | ``` class AVAudioFormat : NSObject, NSSecureCoding, NSCoding {     init(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>)     init(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>, channelLayout layout: AVAudioChannelLayout?)     init(standardFormatWithSampleRate sampleRate: Double, channels channels: AVAudioChannelCount)     init(standardFormatWithSampleRate sampleRate: Double, channelLayout layout: AVAudioChannelLayout)     init(commonFormat format: AVAudioCommonFormat, sampleRate sampleRate: Double, channels channels: AVAudioChannelCount, interleaved interleaved: Bool)     init(commonFormat format: AVAudioCommonFormat, sampleRate sampleRate: Double, interleaved interleaved: Bool, channelLayout layout: AVAudioChannelLayout)     init(settings settings: [String : AnyObject])     init(CMAudioFormatDescription formatDescription: CMAudioFormatDescription)     func isEqual(_ object: AnyObject) -> Bool     var standard: Bool { get }     var commonFormat: AVAudioCommonFormat { get }     var channelCount: AVAudioChannelCount { get }     var sampleRate: Double { get }     var interleaved: Bool { get }     var streamDescription: UnsafePointer<AudioStreamBasicDescription> { get }     var channelLayout: AVAudioChannelLayout? { get }     var settings: [String : AnyObject] { get }     var formatDescription: CMAudioFormatDescription { get } } ``` | AnyObject, NSCoding, NSSecureCoding |

Modified [AVAudioFormat.channelLayout](https://developer.apple.com/documentation/avfoundation/avaudioformat/1390671-channellayout)

|  | Declaration |
| --- | --- |
| From | ``` var channelLayout: AVAudioChannelLayout! { get } ``` |
| To | ``` var channelLayout: AVAudioChannelLayout? { get } ``` |

Modified [AVAudioFormat.init(commonFormat: AVAudioCommonFormat, sampleRate: Double, channels: AVAudioChannelCount, interleaved: Bool)](https://developer.apple.com/documentation/avfoundation/avaudioformat/1390591-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(commonFormat format: AVAudioCommonFormat, sampleRate sampleRate: Double, channels channels: AVAudioChannelCount, interleaved interleaved: Bool) ``` |
| To | ``` init(commonFormat format: AVAudioCommonFormat, sampleRate sampleRate: Double, channels channels: AVAudioChannelCount, interleaved interleaved: Bool) ``` |

Modified [AVAudioFormat.init(commonFormat: AVAudioCommonFormat, sampleRate: Double, interleaved: Bool, channelLayout: AVAudioChannelLayout)](https://developer.apple.com/documentation/avfoundation/avaudioformat/1389361-initwithcommonformat)

|  | Declaration |
| --- | --- |
| From | ``` init!(commonFormat format: AVAudioCommonFormat, sampleRate sampleRate: Double, interleaved interleaved: Bool, channelLayout layout: AVAudioChannelLayout!) ``` |
| To | ``` init(commonFormat format: AVAudioCommonFormat, sampleRate sampleRate: Double, interleaved interleaved: Bool, channelLayout layout: AVAudioChannelLayout) ``` |

Modified [AVAudioFormat.init(settings: [String : AnyObject])](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387931-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(settings settings: [NSObject : AnyObject]!) ``` |
| To | ``` init(settings settings: [String : AnyObject]) ``` |

Modified [AVAudioFormat.init(standardFormatWithSampleRate: Double, channelLayout: AVAudioChannelLayout)](https://developer.apple.com/documentation/avfoundation/avaudioformat/1388426-initstandardformatwithsamplerate)

|  | Declaration |
| --- | --- |
| From | ``` init!(standardFormatWithSampleRate sampleRate: Double, channelLayout layout: AVAudioChannelLayout!) ``` |
| To | ``` init(standardFormatWithSampleRate sampleRate: Double, channelLayout layout: AVAudioChannelLayout) ``` |

Modified [AVAudioFormat.init(standardFormatWithSampleRate: Double, channels: AVAudioChannelCount)](https://developer.apple.com/documentation/avfoundation/avaudioformat/1390416-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(standardFormatWithSampleRate sampleRate: Double, channels channels: AVAudioChannelCount) ``` |
| To | ``` init(standardFormatWithSampleRate sampleRate: Double, channels channels: AVAudioChannelCount) ``` |

Modified [AVAudioFormat.init(streamDescription: UnsafePointer<AudioStreamBasicDescription>)](https://developer.apple.com/documentation/avfoundation/avaudioformat/1390106-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>) ``` |
| To | ``` init(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>) ``` |

Modified [AVAudioFormat.init(streamDescription: UnsafePointer<AudioStreamBasicDescription>, channelLayout: AVAudioChannelLayout?)](https://developer.apple.com/documentation/avfoundation/avaudioformat/1389347-initwithstreamdescription)

|  | Declaration |
| --- | --- |
| From | ``` init!(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>, channelLayout layout: AVAudioChannelLayout!) ``` |
| To | ``` init(streamDescription asbd: UnsafePointer<AudioStreamBasicDescription>, channelLayout layout: AVAudioChannelLayout?) ``` |

Modified [AVAudioFormat.isEqual(_: AnyObject) -> Bool](https://developer.apple.com/documentation/avfoundation/avaudioformat/1385683-isequal)

|  | Declaration |
| --- | --- |
| From | ``` func isEqual(_ object: AnyObject!) -> Bool ``` |
| To | ``` func isEqual(_ object: AnyObject) -> Bool ``` |

Modified [AVAudioFormat.settings](https://developer.apple.com/documentation/avfoundation/avaudioformat/1386904-settings)

|  | Declaration |
| --- | --- |
| From | ``` var settings: [NSObject : AnyObject]! { get } ``` |
| To | ``` var settings: [String : AnyObject] { get } ``` |

Modified [AVAudioInputNode](https://developer.apple.com/documentation/avfoundation/avaudioinputnode)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioInputNode : AVAudioIONode, AVAudioMixing, AVAudioStereoMixing, NSObjectProtocol, AVAudio3DMixing { } ``` |
| To | ``` class AVAudioInputNode : AVAudioIONode, AVAudioMixing, AVAudioStereoMixing, AVAudio3DMixing { } ``` |

Modified [AVAudioMix](https://developer.apple.com/documentation/avfoundation/avaudiomix)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioMix : NSObject, NSCopying, NSMutableCopying {     var inputParameters: [AnyObject]! { get } } ``` |
| To | ``` class AVAudioMix : NSObject, NSCopying, NSMutableCopying {     var inputParameters: [AVAudioMixInputParameters] { get } } ``` |

Modified [AVAudioMix.inputParameters](https://developer.apple.com/documentation/avfoundation/avaudiomix/1388791-inputparameters)

|  | Declaration |
| --- | --- |
| From | ``` var inputParameters: [AnyObject]! { get } ``` |
| To | ``` var inputParameters: [AVAudioMixInputParameters] { get } ``` |

Modified [AVAudioMixerNode](https://developer.apple.com/documentation/avfoundation/avaudiomixernode)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioMixerNode : AVAudioNode, AVAudioMixing, AVAudioStereoMixing, NSObjectProtocol, AVAudio3DMixing {     var outputVolume: Float     var nextAvailableInputBus: AVAudioNodeBus { get } } ``` |
| To | ``` class AVAudioMixerNode : AVAudioNode, AVAudioMixing, AVAudioStereoMixing, AVAudio3DMixing {     var outputVolume: Float     var nextAvailableInputBus: AVAudioNodeBus { get } } ``` |

Modified [AVAudioMixing](https://developer.apple.com/documentation/avfoundation/avaudiomixing)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVAudioMixing : AVAudioStereoMixing, NSObjectProtocol, AVAudio3DMixing {     var volume: Float { get set } } ``` |
| To | ``` protocol AVAudioMixing : AVAudioStereoMixing, NSObjectProtocol, AVAudio3DMixing {     func destinationForMixer(_ mixer: AVAudioNode, bus bus: AVAudioNodeBus) -> AVAudioMixingDestination?     var volume: Float { get set } } ``` |

Modified [AVAudioMixInputParameters](https://developer.apple.com/documentation/avfoundation/avaudiomixinputparameters)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioMixInputParameters : NSObject, NSCopying, NSMutableCopying {     var trackID: CMPersistentTrackID { get }     var audioTimePitchAlgorithm: String! { get }     var audioTapProcessor: MTAudioProcessingTap! { get }     func getVolumeRampForTime(_ time: CMTime, startVolume startVolume: UnsafeMutablePointer<Float>, endVolume endVolume: UnsafeMutablePointer<Float>, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool } ``` |
| To | ``` class AVAudioMixInputParameters : NSObject, NSCopying, NSMutableCopying {     var trackID: CMPersistentTrackID { get }     var audioTimePitchAlgorithm: String? { get }     var audioTapProcessor: MTAudioProcessingTap? { get }     func getVolumeRampForTime(_ time: CMTime, startVolume startVolume: UnsafeMutablePointer<Float>, endVolume endVolume: UnsafeMutablePointer<Float>, timeRange timeRange: UnsafeMutablePointer<CMTimeRange>) -> Bool } ``` |

Modified [AVAudioMixInputParameters.audioTapProcessor](https://developer.apple.com/documentation/avfoundation/avaudiomixinputparameters/1388578-audiotapprocessor)

|  | Declaration |
| --- | --- |
| From | ``` var audioTapProcessor: MTAudioProcessingTap! { get } ``` |
| To | ``` var audioTapProcessor: MTAudioProcessingTap? { get } ``` |

Modified [AVAudioMixInputParameters.audioTimePitchAlgorithm](https://developer.apple.com/documentation/avfoundation/avaudiomixinputparameters/1387042-audiotimepitchalgorithm)

|  | Declaration |
| --- | --- |
| From | ``` var audioTimePitchAlgorithm: String! { get } ``` |
| To | ``` var audioTimePitchAlgorithm: String? { get } ``` |

Modified [AVAudioNode](https://developer.apple.com/documentation/avfoundation/avaudionode)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioNode : NSObject {     func reset()     func inputFormatForBus(_ bus: AVAudioNodeBus) -> AVAudioFormat!     func outputFormatForBus(_ bus: AVAudioNodeBus) -> AVAudioFormat!     func nameForInputBus(_ bus: AVAudioNodeBus) -> String!     func nameForOutputBus(_ bus: AVAudioNodeBus) -> String!     func installTapOnBus(_ bus: AVAudioNodeBus, bufferSize bufferSize: AVAudioFrameCount, format format: AVAudioFormat!, block tapBlock: AVAudioNodeTapBlock!)     func removeTapOnBus(_ bus: AVAudioNodeBus)     var engine: AVAudioEngine! { get }     var numberOfInputs: Int { get }     var numberOfOutputs: Int { get }     var lastRenderTime: AVAudioTime! { get } } ``` |
| To | ``` class AVAudioNode : NSObject {     func reset()     func inputFormatForBus(_ bus: AVAudioNodeBus) -> AVAudioFormat     func outputFormatForBus(_ bus: AVAudioNodeBus) -> AVAudioFormat     func nameForInputBus(_ bus: AVAudioNodeBus) -> String     func nameForOutputBus(_ bus: AVAudioNodeBus) -> String     func installTapOnBus(_ bus: AVAudioNodeBus, bufferSize bufferSize: AVAudioFrameCount, format format: AVAudioFormat?, block tapBlock: AVAudioNodeTapBlock)     func removeTapOnBus(_ bus: AVAudioNodeBus)     var engine: AVAudioEngine? { get }     var numberOfInputs: Int { get }     var numberOfOutputs: Int { get }     var lastRenderTime: AVAudioTime? { get } } ``` |

Modified [AVAudioNode.engine](https://developer.apple.com/documentation/avfoundation/avaudionode/1386896-engine)

|  | Declaration |
| --- | --- |
| From | ``` var engine: AVAudioEngine! { get } ``` |
| To | ``` var engine: AVAudioEngine? { get } ``` |

Modified [AVAudioNode.inputFormatForBus(_: AVAudioNodeBus) -> AVAudioFormat](https://developer.apple.com/documentation/avfoundation/avaudionode/1390147-inputformat)

|  | Declaration |
| --- | --- |
| From | ``` func inputFormatForBus(_ bus: AVAudioNodeBus) -> AVAudioFormat! ``` |
| To | ``` func inputFormatForBus(_ bus: AVAudioNodeBus) -> AVAudioFormat ``` |

Modified [AVAudioNode.installTapOnBus(_: AVAudioNodeBus, bufferSize: AVAudioFrameCount, format: AVAudioFormat?, block: AVAudioNodeTapBlock)](https://developer.apple.com/documentation/avfoundation/avaudionode/1387122-installtap)

|  | Declaration |
| --- | --- |
| From | ``` func installTapOnBus(_ bus: AVAudioNodeBus, bufferSize bufferSize: AVAudioFrameCount, format format: AVAudioFormat!, block tapBlock: AVAudioNodeTapBlock!) ``` |
| To | ``` func installTapOnBus(_ bus: AVAudioNodeBus, bufferSize bufferSize: AVAudioFrameCount, format format: AVAudioFormat?, block tapBlock: AVAudioNodeTapBlock) ``` |

Modified [AVAudioNode.lastRenderTime](https://developer.apple.com/documentation/avfoundation/avaudionode/1385978-lastrendertime)

|  | Declaration |
| --- | --- |
| From | ``` var lastRenderTime: AVAudioTime! { get } ``` |
| To | ``` var lastRenderTime: AVAudioTime? { get } ``` |

Modified [AVAudioNode.nameForInputBus(_: AVAudioNodeBus) -> String](https://developer.apple.com/documentation/avfoundation/avaudionode/1387710-nameforinputbus)

|  | Declaration |
| --- | --- |
| From | ``` func nameForInputBus(_ bus: AVAudioNodeBus) -> String! ``` |
| To | ``` func nameForInputBus(_ bus: AVAudioNodeBus) -> String ``` |

Modified [AVAudioNode.nameForOutputBus(_: AVAudioNodeBus) -> String](https://developer.apple.com/documentation/avfoundation/avaudionode/1390811-name)

|  | Declaration |
| --- | --- |
| From | ``` func nameForOutputBus(_ bus: AVAudioNodeBus) -> String! ``` |
| To | ``` func nameForOutputBus(_ bus: AVAudioNodeBus) -> String ``` |

Modified [AVAudioNode.outputFormatForBus(_: AVAudioNodeBus) -> AVAudioFormat](https://developer.apple.com/documentation/avfoundation/avaudionode/1389195-outputformat)

|  | Declaration |
| --- | --- |
| From | ``` func outputFormatForBus(_ bus: AVAudioNodeBus) -> AVAudioFormat! ``` |
| To | ``` func outputFormatForBus(_ bus: AVAudioNodeBus) -> AVAudioFormat ``` |

Modified [AVAudioPCMBuffer](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioPCMBuffer : AVAudioBuffer {     init!(PCMFormat format: AVAudioFormat!, frameCapacity frameCapacity: AVAudioFrameCount)     var frameCapacity: AVAudioFrameCount { get }     var frameLength: AVAudioFrameCount     var stride: Int { get }     var floatChannelData: UnsafePointer<UnsafeMutablePointer<Float>> { get }     var int16ChannelData: UnsafePointer<UnsafeMutablePointer<Int16>> { get }     var int32ChannelData: UnsafePointer<UnsafeMutablePointer<Int32>> { get } } ``` |
| To | ``` class AVAudioPCMBuffer : AVAudioBuffer {     init(PCMFormat format: AVAudioFormat, frameCapacity frameCapacity: AVAudioFrameCount)     var frameCapacity: AVAudioFrameCount { get }     var frameLength: AVAudioFrameCount     var stride: Int { get }     var floatChannelData: UnsafePointer<UnsafeMutablePointer<Float>> { get }     var int16ChannelData: UnsafePointer<UnsafeMutablePointer<Int16>> { get }     var int32ChannelData: UnsafePointer<UnsafeMutablePointer<Int32>> { get } } ``` |

Modified [AVAudioPCMBuffer.init(PCMFormat: AVAudioFormat, frameCapacity: AVAudioFrameCount)](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1389630-initwithpcmformat)

|  | Declaration |
| --- | --- |
| From | ``` init!(PCMFormat format: AVAudioFormat!, frameCapacity frameCapacity: AVAudioFrameCount) ``` |
| To | ``` init(PCMFormat format: AVAudioFormat, frameCapacity frameCapacity: AVAudioFrameCount) ``` |

Modified [AVAudioPlayer](https://developer.apple.com/documentation/avfoundation/avaudioplayer)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioPlayer : NSObject {     init!(contentsOfURL url: NSURL!, error outError: NSErrorPointer)     init!(data data: NSData!, error outError: NSErrorPointer)     init!(contentsOfURL url: NSURL!, fileTypeHint utiString: String!, error outError: NSErrorPointer)     init!(data data: NSData!, fileTypeHint utiString: String!, error outError: NSErrorPointer)     func prepareToPlay() -> Bool     func play() -> Bool     func playAtTime(_ time: NSTimeInterval) -> Bool     func pause()     func stop()     var playing: Bool { get }     var numberOfChannels: Int { get }     var duration: NSTimeInterval { get }     unowned(unsafe) var delegate: AVAudioPlayerDelegate!     var url: NSURL! { get }     var data: NSData! { get }     var pan: Float     var volume: Float     var enableRate: Bool     var rate: Float     var currentTime: NSTimeInterval     var deviceCurrentTime: NSTimeInterval { get }     var numberOfLoops: Int     var settings: [NSObject : AnyObject]! { get }     var meteringEnabled: Bool     func updateMeters()     func peakPowerForChannel(_ channelNumber: Int) -> Float     func averagePowerForChannel(_ channelNumber: Int) -> Float     var channelAssignments: [AnyObject]! } ``` |
| To | ``` class AVAudioPlayer : NSObject {     init(contentsOfURL url: NSURL) throws     init(data data: NSData) throws     init(contentsOfURL url: NSURL, fileTypeHint utiString: String?) throws     init(data data: NSData, fileTypeHint utiString: String?) throws     func prepareToPlay() -> Bool     func play() -> Bool     func playAtTime(_ time: NSTimeInterval) -> Bool     func pause()     func stop()     var playing: Bool { get }     var numberOfChannels: Int { get }     var duration: NSTimeInterval { get }     unowned(unsafe) var delegate: AVAudioPlayerDelegate?     var url: NSURL? { get }     var data: NSData? { get }     var pan: Float     var volume: Float     var enableRate: Bool     var rate: Float     var currentTime: NSTimeInterval     var deviceCurrentTime: NSTimeInterval { get }     var numberOfLoops: Int     var settings: [String : AnyObject] { get }     var meteringEnabled: Bool     func updateMeters()     func peakPowerForChannel(_ channelNumber: Int) -> Float     func averagePowerForChannel(_ channelNumber: Int) -> Float     var channelAssignments: [NSNumber]? } ``` |

Modified [AVAudioPlayer.channelAssignments](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1624038-channelassignments)

|  | Declaration |
| --- | --- |
| From | ``` var channelAssignments: [AnyObject]! ``` |
| To | ``` var channelAssignments: [NSNumber]? ``` |

Modified [AVAudioPlayer.data](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389437-data)

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData! { get } ``` |
| To | ``` var data: NSData? { get } ``` |

Modified [AVAudioPlayer.delegate](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387134-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: AVAudioPlayerDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: AVAudioPlayerDelegate? ``` |

Modified [AVAudioPlayer.init(contentsOfURL: NSURL) throws](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387281-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` init!(contentsOfURL url: NSURL!, error outError: NSErrorPointer) ``` |
| To | ``` init(contentsOfURL url: NSURL) throws ``` |

Modified [AVAudioPlayer.init(contentsOfURL: NSURL, fileTypeHint: String?) throws](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388349-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` init!(contentsOfURL url: NSURL!, fileTypeHint utiString: String!, error outError: NSErrorPointer) ``` |
| To | ``` init(contentsOfURL url: NSURL, fileTypeHint utiString: String?) throws ``` |

Modified [AVAudioPlayer.init(data: NSData) throws](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388809-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(data data: NSData!, error outError: NSErrorPointer) ``` |
| To | ``` init(data data: NSData) throws ``` |

Modified [AVAudioPlayer.init(data: NSData, fileTypeHint: String?) throws](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388525-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(data data: NSData!, fileTypeHint utiString: String!, error outError: NSErrorPointer) ``` |
| To | ``` init(data data: NSData, fileTypeHint utiString: String?) throws ``` |

Modified [AVAudioPlayer.settings](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389359-settings)

|  | Declaration |
| --- | --- |
| From | ``` var settings: [NSObject : AnyObject]! { get } ``` |
| To | ``` var settings: [String : AnyObject] { get } ``` |

Modified [AVAudioPlayer.url](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387448-url)

|  | Declaration |
| --- | --- |
| From | ``` var url: NSURL! { get } ``` |
| To | ``` var url: NSURL? { get } ``` |

Modified [AVAudioPlayerDelegate](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVAudioPlayerDelegate : NSObjectProtocol {     optional func audioPlayerDidFinishPlaying(_ player: AVAudioPlayer!, successfully flag: Bool)     optional func audioPlayerDecodeErrorDidOccur(_ player: AVAudioPlayer!, error error: NSError!)     optional func audioPlayerBeginInterruption(_ player: AVAudioPlayer!)     optional func audioPlayerEndInterruption(_ player: AVAudioPlayer!, withOptions flags: Int)     optional func audioPlayerEndInterruption(_ player: AVAudioPlayer!, withFlags flags: Int)     optional func audioPlayerEndInterruption(_ player: AVAudioPlayer!) } ``` |
| To | ``` protocol AVAudioPlayerDelegate : NSObjectProtocol {     optional func audioPlayerDidFinishPlaying(_ player: AVAudioPlayer, successfully flag: Bool)     optional func audioPlayerDecodeErrorDidOccur(_ player: AVAudioPlayer, error error: NSError?)     optional func audioPlayerBeginInterruption(_ player: AVAudioPlayer)     optional func audioPlayerEndInterruption(_ player: AVAudioPlayer, withOptions flags: Int)     optional func audioPlayerEndInterruption(_ player: AVAudioPlayer, withFlags flags: Int)     optional func audioPlayerEndInterruption(_ player: AVAudioPlayer) } ``` |

Modified [AVAudioPlayerDelegate.audioPlayerBeginInterruption(_: AVAudioPlayer)](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1624037-audioplayerbegininterruption)

|  | Declaration |
| --- | --- |
| From | ``` optional func audioPlayerBeginInterruption(_ player: AVAudioPlayer!) ``` |
| To | ``` optional func audioPlayerBeginInterruption(_ player: AVAudioPlayer) ``` |

Modified [AVAudioPlayerDelegate.audioPlayerDecodeErrorDidOccur(_: AVAudioPlayer, error: NSError?)](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1387676-audioplayerdecodeerrordidoccur)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func audioPlayerDecodeErrorDidOccur(_ player: AVAudioPlayer!, error error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func audioPlayerDecodeErrorDidOccur(_ player: AVAudioPlayer, error error: NSError?) ``` | iOS 2.2 |

Modified [AVAudioPlayerDelegate.audioPlayerDidFinishPlaying(_: AVAudioPlayer, successfully: Bool)](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1389160-audioplayerdidfinishplaying)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func audioPlayerDidFinishPlaying(_ player: AVAudioPlayer!, successfully flag: Bool) ``` | iOS 8.0 |
| To | ``` optional func audioPlayerDidFinishPlaying(_ player: AVAudioPlayer, successfully flag: Bool) ``` | iOS 2.2 |

Modified [AVAudioPlayerDelegate.audioPlayerEndInterruption(_: AVAudioPlayer, withOptions: Int)](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1624040-audioplayerendinterruption)

|  | Declaration |
| --- | --- |
| From | ``` optional func audioPlayerEndInterruption(_ player: AVAudioPlayer!, withOptions flags: Int) ``` |
| To | ``` optional func audioPlayerEndInterruption(_ player: AVAudioPlayer, withOptions flags: Int) ``` |

Modified [AVAudioPlayerNode](https://developer.apple.com/documentation/avfoundation/avaudioplayernode)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioPlayerNode : AVAudioNode, AVAudioMixing, AVAudioStereoMixing, NSObjectProtocol, AVAudio3DMixing {     func scheduleBuffer(_ buffer: AVAudioPCMBuffer!, completionHandler completionHandler: AVAudioNodeCompletionHandler!)     func scheduleBuffer(_ buffer: AVAudioPCMBuffer!, atTime when: AVAudioTime!, options options: AVAudioPlayerNodeBufferOptions, completionHandler completionHandler: AVAudioNodeCompletionHandler!)     func scheduleFile(_ file: AVAudioFile!, atTime when: AVAudioTime!, completionHandler completionHandler: AVAudioNodeCompletionHandler!)     func scheduleSegment(_ file: AVAudioFile!, startingFrame startFrame: AVAudioFramePosition, frameCount numberFrames: AVAudioFrameCount, atTime when: AVAudioTime!, completionHandler completionHandler: AVAudioNodeCompletionHandler!)     func stop()     func prepareWithFrameCount(_ frameCount: AVAudioFrameCount)     func play()     func playAtTime(_ when: AVAudioTime!)     func pause()     func nodeTimeForPlayerTime(_ playerTime: AVAudioTime!) -> AVAudioTime!     func playerTimeForNodeTime(_ nodeTime: AVAudioTime!) -> AVAudioTime!     var playing: Bool { get } } ``` |
| To | ``` class AVAudioPlayerNode : AVAudioNode, AVAudioMixing, AVAudioStereoMixing, AVAudio3DMixing {     func scheduleBuffer(_ buffer: AVAudioPCMBuffer, completionHandler completionHandler: AVAudioNodeCompletionHandler?)     func scheduleBuffer(_ buffer: AVAudioPCMBuffer, atTime when: AVAudioTime?, options options: AVAudioPlayerNodeBufferOptions, completionHandler completionHandler: AVAudioNodeCompletionHandler?)     func scheduleFile(_ file: AVAudioFile, atTime when: AVAudioTime?, completionHandler completionHandler: AVAudioNodeCompletionHandler?)     func scheduleSegment(_ file: AVAudioFile, startingFrame startFrame: AVAudioFramePosition, frameCount numberFrames: AVAudioFrameCount, atTime when: AVAudioTime?, completionHandler completionHandler: AVAudioNodeCompletionHandler?)     func stop()     func prepareWithFrameCount(_ frameCount: AVAudioFrameCount)     func play()     func playAtTime(_ when: AVAudioTime?)     func pause()     func nodeTimeForPlayerTime(_ playerTime: AVAudioTime) -> AVAudioTime?     func playerTimeForNodeTime(_ nodeTime: AVAudioTime) -> AVAudioTime?     var playing: Bool { get } } ``` |

Modified [AVAudioPlayerNode.nodeTimeForPlayerTime(_: AVAudioTime) -> AVAudioTime?](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1386450-nodetimeforplayertime)

|  | Declaration |
| --- | --- |
| From | ``` func nodeTimeForPlayerTime(_ playerTime: AVAudioTime!) -> AVAudioTime! ``` |
| To | ``` func nodeTimeForPlayerTime(_ playerTime: AVAudioTime) -> AVAudioTime? ``` |

Modified [AVAudioPlayerNode.playAtTime(_: AVAudioTime?)](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1389304-play)

|  | Declaration |
| --- | --- |
| From | ``` func playAtTime(_ when: AVAudioTime!) ``` |
| To | ``` func playAtTime(_ when: AVAudioTime?) ``` |

Modified [AVAudioPlayerNode.playerTimeForNodeTime(_: AVAudioTime) -> AVAudioTime?](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1390449-playertime)

|  | Declaration |
| --- | --- |
| From | ``` func playerTimeForNodeTime(_ nodeTime: AVAudioTime!) -> AVAudioTime! ``` |
| To | ``` func playerTimeForNodeTime(_ nodeTime: AVAudioTime) -> AVAudioTime? ``` |

Modified [AVAudioPlayerNode.scheduleBuffer(_: AVAudioPCMBuffer, atTime: AVAudioTime?, options: AVAudioPlayerNodeBufferOptions, completionHandler: AVAudioNodeCompletionHandler?)](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1388422-schedulebuffer)

|  | Declaration |
| --- | --- |
| From | ``` func scheduleBuffer(_ buffer: AVAudioPCMBuffer!, atTime when: AVAudioTime!, options options: AVAudioPlayerNodeBufferOptions, completionHandler completionHandler: AVAudioNodeCompletionHandler!) ``` |
| To | ``` func scheduleBuffer(_ buffer: AVAudioPCMBuffer, atTime when: AVAudioTime?, options options: AVAudioPlayerNodeBufferOptions, completionHandler completionHandler: AVAudioNodeCompletionHandler?) ``` |

Modified [AVAudioPlayerNode.scheduleBuffer(_: AVAudioPCMBuffer, completionHandler: AVAudioNodeCompletionHandler?)](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1389996-schedulebuffer)

|  | Declaration |
| --- | --- |
| From | ``` func scheduleBuffer(_ buffer: AVAudioPCMBuffer!, completionHandler completionHandler: AVAudioNodeCompletionHandler!) ``` |
| To | ``` func scheduleBuffer(_ buffer: AVAudioPCMBuffer, completionHandler completionHandler: AVAudioNodeCompletionHandler?) ``` |

Modified [AVAudioPlayerNode.scheduleFile(_: AVAudioFile, atTime: AVAudioTime?, completionHandler: AVAudioNodeCompletionHandler?)](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1390047-schedulefile)

|  | Declaration |
| --- | --- |
| From | ``` func scheduleFile(_ file: AVAudioFile!, atTime when: AVAudioTime!, completionHandler completionHandler: AVAudioNodeCompletionHandler!) ``` |
| To | ``` func scheduleFile(_ file: AVAudioFile, atTime when: AVAudioTime?, completionHandler completionHandler: AVAudioNodeCompletionHandler?) ``` |

Modified [AVAudioPlayerNode.scheduleSegment(_: AVAudioFile, startingFrame: AVAudioFramePosition, frameCount: AVAudioFrameCount, atTime: AVAudioTime?, completionHandler: AVAudioNodeCompletionHandler?)](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1385884-schedulesegment)

|  | Declaration |
| --- | --- |
| From | ``` func scheduleSegment(_ file: AVAudioFile!, startingFrame startFrame: AVAudioFramePosition, frameCount numberFrames: AVAudioFrameCount, atTime when: AVAudioTime!, completionHandler completionHandler: AVAudioNodeCompletionHandler!) ``` |
| To | ``` func scheduleSegment(_ file: AVAudioFile, startingFrame startFrame: AVAudioFramePosition, frameCount numberFrames: AVAudioFrameCount, atTime when: AVAudioTime?, completionHandler completionHandler: AVAudioNodeCompletionHandler?) ``` |

Modified [AVAudioPlayerNodeBufferOptions [struct]](https://developer.apple.com/documentation/avfoundation/avaudioplayernodebufferoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVAudioPlayerNodeBufferOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Loops: AVAudioPlayerNodeBufferOptions { get }     static var Interrupts: AVAudioPlayerNodeBufferOptions { get }     static var InterruptsAtLoop: AVAudioPlayerNodeBufferOptions { get } } ``` | RawOptionSetType |
| To | ``` struct AVAudioPlayerNodeBufferOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var Loops: AVAudioPlayerNodeBufferOptions { get }     static var Interrupts: AVAudioPlayerNodeBufferOptions { get }     static var InterruptsAtLoop: AVAudioPlayerNodeBufferOptions { get } } ``` | OptionSetType |

Modified [AVAudioQuality [enum]](https://developer.apple.com/documentation/avfoundation/avaudioquality)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVAudioRecorder](https://developer.apple.com/documentation/avfoundation/avaudiorecorder)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioRecorder : NSObject {     init!(URL url: NSURL!, settings settings: [NSObject : AnyObject]!, error outError: NSErrorPointer)     func prepareToRecord() -> Bool     func record() -> Bool     func recordAtTime(_ time: NSTimeInterval) -> Bool     func recordForDuration(_ duration: NSTimeInterval) -> Bool     func recordAtTime(_ time: NSTimeInterval, forDuration duration: NSTimeInterval) -> Bool     func pause()     func stop()     func deleteRecording() -> Bool     var recording: Bool { get }     var url: NSURL! { get }     var settings: [NSObject : AnyObject]! { get }     unowned(unsafe) var delegate: AVAudioRecorderDelegate!     var currentTime: NSTimeInterval { get }     var deviceCurrentTime: NSTimeInterval { get }     var meteringEnabled: Bool     func updateMeters()     func peakPowerForChannel(_ channelNumber: Int) -> Float     func averagePowerForChannel(_ channelNumber: Int) -> Float     var channelAssignments: [AnyObject]! } ``` |
| To | ``` class AVAudioRecorder : NSObject {     init(URL url: NSURL, settings settings: [String : AnyObject]) throws     func prepareToRecord() -> Bool     func record() -> Bool     func recordAtTime(_ time: NSTimeInterval) -> Bool     func recordForDuration(_ duration: NSTimeInterval) -> Bool     func recordAtTime(_ time: NSTimeInterval, forDuration duration: NSTimeInterval) -> Bool     func pause()     func stop()     func deleteRecording() -> Bool     var recording: Bool { get }     var url: NSURL { get }     var settings: [String : AnyObject] { get }     unowned(unsafe) var delegate: AVAudioRecorderDelegate?     var currentTime: NSTimeInterval { get }     var deviceCurrentTime: NSTimeInterval { get }     var meteringEnabled: Bool     func updateMeters()     func peakPowerForChannel(_ channelNumber: Int) -> Float     func averagePowerForChannel(_ channelNumber: Int) -> Float     var channelAssignments: [NSNumber]? } ``` |

Modified [AVAudioRecorder.channelAssignments](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1624903-channelassignments)

|  | Declaration |
| --- | --- |
| From | ``` var channelAssignments: [AnyObject]! ``` |
| To | ``` var channelAssignments: [NSNumber]? ``` |

Modified [AVAudioRecorder.delegate](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1385839-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: AVAudioRecorderDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: AVAudioRecorderDelegate? ``` |

Modified [AVAudioRecorder.init(URL: NSURL, settings: [String : AnyObject]) throws](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1388386-initwithurl)

|  | Declaration |
| --- | --- |
| From | ``` init!(URL url: NSURL!, settings settings: [NSObject : AnyObject]!, error outError: NSErrorPointer) ``` |
| To | ``` init(URL url: NSURL, settings settings: [String : AnyObject]) throws ``` |

Modified [AVAudioRecorder.settings](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1390903-settings)

|  | Declaration |
| --- | --- |
| From | ``` var settings: [NSObject : AnyObject]! { get } ``` |
| To | ``` var settings: [String : AnyObject] { get } ``` |

Modified [AVAudioRecorder.url](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1389050-url)

|  | Declaration |
| --- | --- |
| From | ``` var url: NSURL! { get } ``` |
| To | ``` var url: NSURL { get } ``` |

Modified [AVAudioRecorderDelegate](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVAudioRecorderDelegate : NSObjectProtocol {     optional func audioRecorderDidFinishRecording(_ recorder: AVAudioRecorder!, successfully flag: Bool)     optional func audioRecorderEncodeErrorDidOccur(_ recorder: AVAudioRecorder!, error error: NSError!)     optional func audioRecorderBeginInterruption(_ recorder: AVAudioRecorder!)     optional func audioRecorderEndInterruption(_ recorder: AVAudioRecorder!, withOptions flags: Int)     optional func audioRecorderEndInterruption(_ recorder: AVAudioRecorder!, withFlags flags: Int)     optional func audioRecorderEndInterruption(_ recorder: AVAudioRecorder!) } ``` |
| To | ``` protocol AVAudioRecorderDelegate : NSObjectProtocol {     optional func audioRecorderDidFinishRecording(_ recorder: AVAudioRecorder, successfully flag: Bool)     optional func audioRecorderEncodeErrorDidOccur(_ recorder: AVAudioRecorder, error error: NSError?)     optional func audioRecorderBeginInterruption(_ recorder: AVAudioRecorder)     optional func audioRecorderEndInterruption(_ recorder: AVAudioRecorder, withOptions flags: Int)     optional func audioRecorderEndInterruption(_ recorder: AVAudioRecorder, withFlags flags: Int)     optional func audioRecorderEndInterruption(_ recorder: AVAudioRecorder) } ``` |

Modified [AVAudioRecorderDelegate.audioRecorderBeginInterruption(_: AVAudioRecorder)](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate/1624897-audiorecorderbegininterruption)

|  | Declaration |
| --- | --- |
| From | ``` optional func audioRecorderBeginInterruption(_ recorder: AVAudioRecorder!) ``` |
| To | ``` optional func audioRecorderBeginInterruption(_ recorder: AVAudioRecorder) ``` |

Modified [AVAudioRecorderDelegate.audioRecorderDidFinishRecording(_: AVAudioRecorder, successfully: Bool)](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate/1388688-audiorecorderdidfinishrecording)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func audioRecorderDidFinishRecording(_ recorder: AVAudioRecorder!, successfully flag: Bool) ``` | iOS 8.0 |
| To | ``` optional func audioRecorderDidFinishRecording(_ recorder: AVAudioRecorder, successfully flag: Bool) ``` | iOS 3.0 |

Modified [AVAudioRecorderDelegate.audioRecorderEncodeErrorDidOccur(_: AVAudioRecorder, error: NSError?)](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate/1387774-audiorecorderencodeerrordidoccur)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func audioRecorderEncodeErrorDidOccur(_ recorder: AVAudioRecorder!, error error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func audioRecorderEncodeErrorDidOccur(_ recorder: AVAudioRecorder, error error: NSError?) ``` | iOS 3.0 |

Modified [AVAudioRecorderDelegate.audioRecorderEndInterruption(_: AVAudioRecorder, withOptions: Int)](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate/1624901-audiorecorderendinterruption)

|  | Declaration |
| --- | --- |
| From | ``` optional func audioRecorderEndInterruption(_ recorder: AVAudioRecorder!, withOptions flags: Int) ``` |
| To | ``` optional func audioRecorderEndInterruption(_ recorder: AVAudioRecorder, withOptions flags: Int) ``` |

Modified [AVAudioSession](https://developer.apple.com/documentation/avfoundation/avaudiosession)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioSession : NSObject {     class func sharedInstance() -> AVAudioSession!     func setActive(_ active: Bool, error outError: NSErrorPointer) -> Bool     func setActive(_ active: Bool, withOptions options: AVAudioSessionSetActiveOptions, error outError: NSErrorPointer) -> Bool     func setCategory(_ category: String!, error outError: NSErrorPointer) -> Bool     func setCategory(_ category: String!, withOptions options: AVAudioSessionCategoryOptions, error outError: NSErrorPointer) -> Bool     func recordPermission() -> AVAudioSessionRecordPermission     func requestRecordPermission(_ response: PermissionBlock!)     var category: String! { get }     var categoryOptions: AVAudioSessionCategoryOptions { get }     func setMode(_ mode: String!, error outError: NSErrorPointer) -> Bool     var mode: String! { get }     func overrideOutputAudioPort(_ portOverride: AVAudioSessionPortOverride, error outError: NSErrorPointer) -> Bool     var otherAudioPlaying: Bool { get }     var secondaryAudioShouldBeSilencedHint: Bool { get }     var currentRoute: AVAudioSessionRouteDescription! { get }     func setPreferredInput(_ inPort: AVAudioSessionPortDescription!, error outError: NSErrorPointer) -> Bool     var preferredInput: AVAudioSessionPortDescription! { get }     var availableInputs: [AnyObject]! { get } } extension AVAudioSession {     func setPreferredSampleRate(_ sampleRate: Double, error outError: NSErrorPointer) -> Bool     var preferredSampleRate: Double { get }     func setPreferredIOBufferDuration(_ duration: NSTimeInterval, error outError: NSErrorPointer) -> Bool     var preferredIOBufferDuration: NSTimeInterval { get }     func setPreferredInputNumberOfChannels(_ count: Int, error outError: NSErrorPointer) -> Bool     var preferredInputNumberOfChannels: Int { get }     func setPreferredOutputNumberOfChannels(_ count: Int, error outError: NSErrorPointer) -> Bool     var preferredOutputNumberOfChannels: Int { get }     var maximumInputNumberOfChannels: Int { get }     var maximumOutputNumberOfChannels: Int { get }     func setInputGain(_ gain: Float, error outError: NSErrorPointer) -> Bool     var inputGain: Float { get }     var inputGainSettable: Bool { get }     var inputAvailable: Bool { get }     var inputDataSources: [AnyObject]! { get }     var inputDataSource: AVAudioSessionDataSourceDescription! { get }     func setInputDataSource(_ dataSource: AVAudioSessionDataSourceDescription!, error outError: NSErrorPointer) -> Bool     var outputDataSources: [AnyObject]! { get }     var outputDataSource: AVAudioSessionDataSourceDescription! { get }     func setOutputDataSource(_ dataSource: AVAudioSessionDataSourceDescription!, error outError: NSErrorPointer) -> Bool     var sampleRate: Double { get }     var inputNumberOfChannels: Int { get }     var outputNumberOfChannels: Int { get }     var outputVolume: Float { get }     var inputLatency: NSTimeInterval { get }     var outputLatency: NSTimeInterval { get }     var IOBufferDuration: NSTimeInterval { get } } extension AVAudioSession {     unowned(unsafe) var delegate: AVAudioSessionDelegate!     func setActive(_ active: Bool, withFlags flags: Int, error outError: NSErrorPointer) -> Bool     var inputIsAvailable: Bool { get }     var currentHardwareSampleRate: Double { get }     var currentHardwareInputNumberOfChannels: Int { get }     var currentHardwareOutputNumberOfChannels: Int { get }     func setPreferredHardwareSampleRate(_ sampleRate: Double, error outError: NSErrorPointer) -> Bool     var preferredHardwareSampleRate: Double { get } } ``` |
| To | ``` class AVAudioSession : NSObject {     class func sharedInstance() -> AVAudioSession     func setActive(_ active: Bool) throws     func setActive(_ active: Bool, withOptions options: AVAudioSessionSetActiveOptions) throws     var availableCategories: [String] { get }     func setCategory(_ category: String) throws     func setCategory(_ category: String, withOptions options: AVAudioSessionCategoryOptions) throws     var category: String { get }     func recordPermission() -> AVAudioSessionRecordPermission     func requestRecordPermission(_ response: PermissionBlock)     var categoryOptions: AVAudioSessionCategoryOptions { get }     var availableModes: [String] { get }     func setMode(_ mode: String) throws     var mode: String { get }     func overrideOutputAudioPort(_ portOverride: AVAudioSessionPortOverride) throws     var otherAudioPlaying: Bool { get }     var secondaryAudioShouldBeSilencedHint: Bool { get }     var currentRoute: AVAudioSessionRouteDescription { get }     func setPreferredInput(_ inPort: AVAudioSessionPortDescription?) throws     var preferredInput: AVAudioSessionPortDescription? { get }     var availableInputs: [AVAudioSessionPortDescription]? { get } } extension AVAudioSession {     func setPreferredSampleRate(_ sampleRate: Double) throws     var preferredSampleRate: Double { get }     func setPreferredIOBufferDuration(_ duration: NSTimeInterval) throws     var preferredIOBufferDuration: NSTimeInterval { get }     func setPreferredInputNumberOfChannels(_ count: Int) throws     var preferredInputNumberOfChannels: Int { get }     func setPreferredOutputNumberOfChannels(_ count: Int) throws     var preferredOutputNumberOfChannels: Int { get }     var maximumInputNumberOfChannels: Int { get }     var maximumOutputNumberOfChannels: Int { get }     func setInputGain(_ gain: Float) throws     var inputGain: Float { get }     var inputGainSettable: Bool { get }     var inputAvailable: Bool { get }     var inputDataSources: [AVAudioSessionDataSourceDescription]? { get }     var inputDataSource: AVAudioSessionDataSourceDescription? { get }     func setInputDataSource(_ dataSource: AVAudioSessionDataSourceDescription?) throws     var outputDataSources: [AVAudioSessionDataSourceDescription]? { get }     var outputDataSource: AVAudioSessionDataSourceDescription? { get }     func setOutputDataSource(_ dataSource: AVAudioSessionDataSourceDescription?) throws     var sampleRate: Double { get }     var inputNumberOfChannels: Int { get }     var outputNumberOfChannels: Int { get }     var outputVolume: Float { get }     var inputLatency: NSTimeInterval { get }     var outputLatency: NSTimeInterval { get }     var IOBufferDuration: NSTimeInterval { get } } extension AVAudioSession {     unowned(unsafe) var delegate: AVAudioSessionDelegate?     func setActive(_ active: Bool, withFlags flags: Int) throws     var inputIsAvailable: Bool { get }     var currentHardwareSampleRate: Double { get }     var currentHardwareInputNumberOfChannels: Int { get }     var currentHardwareOutputNumberOfChannels: Int { get }     func setPreferredHardwareSampleRate(_ sampleRate: Double) throws     var preferredHardwareSampleRate: Double { get } } ``` |

Modified [AVAudioSession.availableInputs](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616557-availableinputs)

|  | Declaration |
| --- | --- |
| From | ``` var availableInputs: [AnyObject]! { get } ``` |
| To | ``` var availableInputs: [AVAudioSessionPortDescription]? { get } ``` |

Modified [AVAudioSession.category](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616615-category)

|  | Declaration |
| --- | --- |
| From | ``` var category: String! { get } ``` |
| To | ``` var category: String { get } ``` |

Modified [AVAudioSession.currentRoute](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616453-currentroute)

|  | Declaration |
| --- | --- |
| From | ``` var currentRoute: AVAudioSessionRouteDescription! { get } ``` |
| To | ``` var currentRoute: AVAudioSessionRouteDescription { get } ``` |

Modified [AVAudioSession.inputDataSource](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616485-inputdatasource)

|  | Declaration |
| --- | --- |
| From | ``` var inputDataSource: AVAudioSessionDataSourceDescription! { get } ``` |
| To | ``` var inputDataSource: AVAudioSessionDataSourceDescription? { get } ``` |

Modified [AVAudioSession.inputDataSources](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616513-inputdatasources)

|  | Declaration |
| --- | --- |
| From | ``` var inputDataSources: [AnyObject]! { get } ``` |
| To | ``` var inputDataSources: [AVAudioSessionDataSourceDescription]? { get } ``` |

Modified [AVAudioSession.mode](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616508-mode)

|  | Declaration |
| --- | --- |
| From | ``` var mode: String! { get } ``` |
| To | ``` var mode: String { get } ``` |

Modified [AVAudioSession.outputDataSource](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616572-outputdatasource)

|  | Declaration |
| --- | --- |
| From | ``` var outputDataSource: AVAudioSessionDataSourceDescription! { get } ``` |
| To | ``` var outputDataSource: AVAudioSessionDataSourceDescription? { get } ``` |

Modified [AVAudioSession.outputDataSources](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616479-outputdatasources)

|  | Declaration |
| --- | --- |
| From | ``` var outputDataSources: [AnyObject]! { get } ``` |
| To | ``` var outputDataSources: [AVAudioSessionDataSourceDescription]? { get } ``` |

Modified [AVAudioSession.overrideOutputAudioPort(_: AVAudioSessionPortOverride) throws](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616443-overrideoutputaudioport)

|  | Declaration |
| --- | --- |
| From | ``` func overrideOutputAudioPort(_ portOverride: AVAudioSessionPortOverride, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func overrideOutputAudioPort(_ portOverride: AVAudioSessionPortOverride) throws ``` |

Modified [AVAudioSession.preferredInput](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616536-preferredinput)

|  | Declaration |
| --- | --- |
| From | ``` var preferredInput: AVAudioSessionPortDescription! { get } ``` |
| To | ``` var preferredInput: AVAudioSessionPortDescription? { get } ``` |

Modified [AVAudioSession.requestRecordPermission(_: PermissionBlock)](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616601-requestrecordpermission)

|  | Declaration |
| --- | --- |
| From | ``` func requestRecordPermission(_ response: PermissionBlock!) ``` |
| To | ``` func requestRecordPermission(_ response: PermissionBlock) ``` |

Modified [AVAudioSession.setActive(_: Bool) throws](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616597-setactive)

|  | Declaration |
| --- | --- |
| From | ``` func setActive(_ active: Bool, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setActive(_ active: Bool) throws ``` |

Modified [AVAudioSession.setActive(_: Bool, withOptions: AVAudioSessionSetActiveOptions) throws](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616627-setactive)

|  | Declaration |
| --- | --- |
| From | ``` func setActive(_ active: Bool, withOptions options: AVAudioSessionSetActiveOptions, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setActive(_ active: Bool, withOptions options: AVAudioSessionSetActiveOptions) throws ``` |

Modified [AVAudioSession.setCategory(_: String) throws](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616583-setcategory)

|  | Declaration |
| --- | --- |
| From | ``` func setCategory(_ category: String!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setCategory(_ category: String) throws ``` |

Modified [AVAudioSession.setCategory(_: String, withOptions: AVAudioSessionCategoryOptions) throws](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616442-setcategory)

|  | Declaration |
| --- | --- |
| From | ``` func setCategory(_ category: String!, withOptions options: AVAudioSessionCategoryOptions, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setCategory(_ category: String, withOptions options: AVAudioSessionCategoryOptions) throws ``` |

Modified [AVAudioSession.setInputDataSource(_: AVAudioSessionDataSourceDescription?) throws](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616507-setinputdatasource)

|  | Declaration |
| --- | --- |
| From | ``` func setInputDataSource(_ dataSource: AVAudioSessionDataSourceDescription!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setInputDataSource(_ dataSource: AVAudioSessionDataSourceDescription?) throws ``` |

Modified [AVAudioSession.setInputGain(_: Float) throws](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616546-setinputgain)

|  | Declaration |
| --- | --- |
| From | ``` func setInputGain(_ gain: Float, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setInputGain(_ gain: Float) throws ``` |

Modified [AVAudioSession.setMode(_: String) throws](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616614-setmode)

|  | Declaration |
| --- | --- |
| From | ``` func setMode(_ mode: String!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setMode(_ mode: String) throws ``` |

Modified [AVAudioSession.setOutputDataSource(_: AVAudioSessionDataSourceDescription?) throws](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616582-setoutputdatasource)

|  | Declaration |
| --- | --- |
| From | ``` func setOutputDataSource(_ dataSource: AVAudioSessionDataSourceDescription!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setOutputDataSource(_ dataSource: AVAudioSessionDataSourceDescription?) throws ``` |

Modified [AVAudioSession.setPreferredInput(_: AVAudioSessionPortDescription?) throws](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616491-setpreferredinput)

|  | Declaration |
| --- | --- |
| From | ``` func setPreferredInput(_ inPort: AVAudioSessionPortDescription!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setPreferredInput(_ inPort: AVAudioSessionPortDescription?) throws ``` |

Modified [AVAudioSession.setPreferredInputNumberOfChannels(_: Int) throws](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616483-setpreferredinputnumberofchannel)

|  | Declaration |
| --- | --- |
| From | ``` func setPreferredInputNumberOfChannels(_ count: Int, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setPreferredInputNumberOfChannels(_ count: Int) throws ``` |

Modified [AVAudioSession.setPreferredIOBufferDuration(_: NSTimeInterval) throws](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616589-setpreferrediobufferduration)

|  | Declaration |
| --- | --- |
| From | ``` func setPreferredIOBufferDuration(_ duration: NSTimeInterval, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setPreferredIOBufferDuration(_ duration: NSTimeInterval) throws ``` |

Modified [AVAudioSession.setPreferredOutputNumberOfChannels(_: Int) throws](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616481-setpreferredoutputnumberofchanne)

|  | Declaration |
| --- | --- |
| From | ``` func setPreferredOutputNumberOfChannels(_ count: Int, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setPreferredOutputNumberOfChannels(_ count: Int) throws ``` |

Modified [AVAudioSession.setPreferredSampleRate(_: Double) throws](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616523-setpreferredsamplerate)

|  | Declaration |
| --- | --- |
| From | ``` func setPreferredSampleRate(_ sampleRate: Double, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setPreferredSampleRate(_ sampleRate: Double) throws ``` |

Modified [AVAudioSession.sharedInstance() -> AVAudioSession [class]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616504-sharedinstance)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedInstance() -> AVAudioSession! ``` |
| To | ``` class func sharedInstance() -> AVAudioSession ``` |

Modified [AVAudioSessionCategoryOptions [struct]](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVAudioSessionCategoryOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var MixWithOthers: AVAudioSessionCategoryOptions { get }     static var DuckOthers: AVAudioSessionCategoryOptions { get }     static var AllowBluetooth: AVAudioSessionCategoryOptions { get }     static var DefaultToSpeaker: AVAudioSessionCategoryOptions { get } } ``` | RawOptionSetType |
| To | ``` struct AVAudioSessionCategoryOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var MixWithOthers: AVAudioSessionCategoryOptions { get }     static var DuckOthers: AVAudioSessionCategoryOptions { get }     static var AllowBluetooth: AVAudioSessionCategoryOptions { get }     static var DefaultToSpeaker: AVAudioSessionCategoryOptions { get }     static var InterruptSpokenAudioAndMixWithOthers: AVAudioSessionCategoryOptions { get } } ``` | OptionSetType |

Modified [AVAudioSessionChannelDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessionchanneldescription)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioSessionChannelDescription : NSObject {     var channelName: String! { get }     var owningPortUID: String! { get }     var channelNumber: Int { get }     var channelLabel: AudioChannelLabel { get } } ``` |
| To | ``` class AVAudioSessionChannelDescription : NSObject {     var channelName: String { get }     var owningPortUID: String { get }     var channelNumber: Int { get }     var channelLabel: AudioChannelLabel { get } } ``` |

Modified [AVAudioSessionChannelDescription.channelName](https://developer.apple.com/documentation/avfoundation/avaudiosessionchanneldescription/1616521-channelname)

|  | Declaration |
| --- | --- |
| From | ``` var channelName: String! { get } ``` |
| To | ``` var channelName: String { get } ``` |

Modified [AVAudioSessionChannelDescription.owningPortUID](https://developer.apple.com/documentation/avfoundation/avaudiosessionchanneldescription/1616562-owningportuid)

|  | Declaration |
| --- | --- |
| From | ``` var owningPortUID: String! { get } ``` |
| To | ``` var owningPortUID: String { get } ``` |

Modified [AVAudioSessionDataSourceDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioSessionDataSourceDescription : NSObject {     var dataSourceID: NSNumber! { get }     var dataSourceName: String! { get }     var location: String! { get }     var orientation: String! { get }     var supportedPolarPatterns: [AnyObject]! { get }     var selectedPolarPattern: String! { get }     var preferredPolarPattern: String! { get }     func setPreferredPolarPattern(_ pattern: String!, error outError: NSErrorPointer) -> Bool } ``` |
| To | ``` class AVAudioSessionDataSourceDescription : NSObject {     var dataSourceID: NSNumber { get }     var dataSourceName: String { get }     var location: String? { get }     var orientation: String? { get }     var supportedPolarPatterns: [String]? { get }     var selectedPolarPattern: String? { get }     var preferredPolarPattern: String? { get }     func setPreferredPolarPattern(_ pattern: String?) throws } ``` |

Modified [AVAudioSessionDataSourceDescription.dataSourceID](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616584-datasourceid)

|  | Declaration |
| --- | --- |
| From | ``` var dataSourceID: NSNumber! { get } ``` |
| To | ``` var dataSourceID: NSNumber { get } ``` |

Modified [AVAudioSessionDataSourceDescription.dataSourceName](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616595-datasourcename)

|  | Declaration |
| --- | --- |
| From | ``` var dataSourceName: String! { get } ``` |
| To | ``` var dataSourceName: String { get } ``` |

Modified [AVAudioSessionDataSourceDescription.location](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616495-location)

|  | Declaration |
| --- | --- |
| From | ``` var location: String! { get } ``` |
| To | ``` var location: String? { get } ``` |

Modified [AVAudioSessionDataSourceDescription.orientation](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616456-orientation)

|  | Declaration |
| --- | --- |
| From | ``` var orientation: String! { get } ``` |
| To | ``` var orientation: String? { get } ``` |

Modified [AVAudioSessionDataSourceDescription.preferredPolarPattern](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616446-preferredpolarpattern)

|  | Declaration |
| --- | --- |
| From | ``` var preferredPolarPattern: String! { get } ``` |
| To | ``` var preferredPolarPattern: String? { get } ``` |

Modified [AVAudioSessionDataSourceDescription.selectedPolarPattern](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616619-selectedpolarpattern)

|  | Declaration |
| --- | --- |
| From | ``` var selectedPolarPattern: String! { get } ``` |
| To | ``` var selectedPolarPattern: String? { get } ``` |

Modified [AVAudioSessionDataSourceDescription.setPreferredPolarPattern(_: String?) throws](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616516-setpreferredpolarpattern)

|  | Declaration |
| --- | --- |
| From | ``` func setPreferredPolarPattern(_ pattern: String!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setPreferredPolarPattern(_ pattern: String?) throws ``` |

Modified [AVAudioSessionDataSourceDescription.supportedPolarPatterns](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616450-supportedpolarpatterns)

|  | Declaration |
| --- | --- |
| From | ``` var supportedPolarPatterns: [AnyObject]! { get } ``` |
| To | ``` var supportedPolarPatterns: [String]? { get } ``` |

Modified [AVAudioSessionErrorCode [enum]](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum AVAudioSessionErrorCode : Int {     case CodeNone     case CodeMediaServicesFailed     case CodeIsBusy     case CodeIncompatibleCategory     case CodeCannotInterruptOthers     case CodeMissingEntitlement     case CodeSiriIsRecording     case CodeCannotStartPlaying     case CodeCannotStartRecording     case CodeBadParam     case InsufficientPriority     case CodeUnspecified } ``` | -- |
| To | ``` enum AVAudioSessionErrorCode : Int {     case CodeNone     case CodeMediaServicesFailed     case CodeIsBusy     case CodeIncompatibleCategory     case CodeCannotInterruptOthers     case CodeMissingEntitlement     case CodeSiriIsRecording     case CodeCannotStartPlaying     case CodeCannotStartRecording     case CodeBadParam     case InsufficientPriority     case CodeResourceNotAvailable     case CodeUnspecified } ``` | Int |

Modified [AVAudioSessionInterruptionOptions [struct]](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptionoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVAudioSessionInterruptionOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var OptionShouldResume: AVAudioSessionInterruptionOptions { get } } ``` | RawOptionSetType |
| To | ``` struct AVAudioSessionInterruptionOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var ShouldResume: AVAudioSessionInterruptionOptions { get } } ``` | OptionSetType |

Modified [AVAudioSessionInterruptionOptions.ShouldResume](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptionoptions/avaudiosessioninterruptionoptionshouldresume)

|  | Declaration |
| --- | --- |
| From | ``` static var OptionShouldResume: AVAudioSessionInterruptionOptions { get } ``` |
| To | ``` static var ShouldResume: AVAudioSessionInterruptionOptions { get } ``` |

Modified [AVAudioSessionInterruptionType [enum]](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptiontype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [AVAudioSessionPortDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioSessionPortDescription : NSObject {     var portType: String! { get }     var portName: String! { get }     var UID: String! { get }     var channels: [AnyObject]! { get }     var dataSources: [AnyObject]! { get }     var selectedDataSource: AVAudioSessionDataSourceDescription! { get }     var preferredDataSource: AVAudioSessionDataSourceDescription! { get }     func setPreferredDataSource(_ dataSource: AVAudioSessionDataSourceDescription!, error outError: NSErrorPointer) -> Bool } ``` |
| To | ``` class AVAudioSessionPortDescription : NSObject {     var portType: String { get }     var portName: String { get }     var UID: String { get }     var channels: [AVAudioSessionChannelDescription]? { get }     var dataSources: [AVAudioSessionDataSourceDescription]? { get }     var selectedDataSource: AVAudioSessionDataSourceDescription? { get }     var preferredDataSource: AVAudioSessionDataSourceDescription? { get }     func setPreferredDataSource(_ dataSource: AVAudioSessionDataSourceDescription?) throws } ``` |

Modified [AVAudioSessionPortDescription.channels](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616574-channels)

|  | Declaration |
| --- | --- |
| From | ``` var channels: [AnyObject]! { get } ``` |
| To | ``` var channels: [AVAudioSessionChannelDescription]? { get } ``` |

Modified [AVAudioSessionPortDescription.dataSources](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616570-datasources)

|  | Declaration |
| --- | --- |
| From | ``` var dataSources: [AnyObject]! { get } ``` |
| To | ``` var dataSources: [AVAudioSessionDataSourceDescription]? { get } ``` |

Modified [AVAudioSessionPortDescription.portName](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616497-portname)

|  | Declaration |
| --- | --- |
| From | ``` var portName: String! { get } ``` |
| To | ``` var portName: String { get } ``` |

Modified [AVAudioSessionPortDescription.portType](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616445-porttype)

|  | Declaration |
| --- | --- |
| From | ``` var portType: String! { get } ``` |
| To | ``` var portType: String { get } ``` |

Modified [AVAudioSessionPortDescription.preferredDataSource](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616628-preferreddatasource)

|  | Declaration |
| --- | --- |
| From | ``` var preferredDataSource: AVAudioSessionDataSourceDescription! { get } ``` |
| To | ``` var preferredDataSource: AVAudioSessionDataSourceDescription? { get } ``` |

Modified [AVAudioSessionPortDescription.selectedDataSource](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616538-selecteddatasource)

|  | Declaration |
| --- | --- |
| From | ``` var selectedDataSource: AVAudioSessionDataSourceDescription! { get } ``` |
| To | ``` var selectedDataSource: AVAudioSessionDataSourceDescription? { get } ``` |

Modified [AVAudioSessionPortDescription.setPreferredDataSource(_: AVAudioSessionDataSourceDescription?) throws](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616554-setpreferreddatasource)

|  | Declaration |
| --- | --- |
| From | ``` func setPreferredDataSource(_ dataSource: AVAudioSessionDataSourceDescription!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setPreferredDataSource(_ dataSource: AVAudioSessionDataSourceDescription?) throws ``` |

Modified [AVAudioSessionPortDescription.UID](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616617-uid)

|  | Declaration |
| --- | --- |
| From | ``` var UID: String! { get } ``` |
| To | ``` var UID: String { get } ``` |

Modified [AVAudioSessionPortOverride [enum]](https://developer.apple.com/documentation/avfoundation/avaudiosession/portoverride)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [AVAudioSessionRecordPermission [struct]](https://developer.apple.com/documentation/avfoundation/avaudiosessionrecordpermission)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVAudioSessionRecordPermission : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Undetermined: AVAudioSessionRecordPermission { get }     static var Denied: AVAudioSessionRecordPermission { get }     static var Granted: AVAudioSessionRecordPermission { get } } ``` | RawOptionSetType |
| To | ``` struct AVAudioSessionRecordPermission : OptionSetType {     init(rawValue rawValue: UInt)     static var Undetermined: AVAudioSessionRecordPermission { get }     static var Denied: AVAudioSessionRecordPermission { get }     static var Granted: AVAudioSessionRecordPermission { get } } ``` | OptionSetType |

Modified [AVAudioSessionRouteChangeReason [enum]](https://developer.apple.com/documentation/avfoundation/avaudiosession/routechangereason)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [AVAudioSessionRouteDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutedescription)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioSessionRouteDescription : NSObject {     var inputs: [AnyObject]! { get }     var outputs: [AnyObject]! { get } } ``` |
| To | ``` class AVAudioSessionRouteDescription : NSObject {     var inputs: [AVAudioSessionPortDescription] { get }     var outputs: [AVAudioSessionPortDescription] { get } } ``` |

Modified [AVAudioSessionRouteDescription.inputs](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutedescription/1616474-inputs)

|  | Declaration |
| --- | --- |
| From | ``` var inputs: [AnyObject]! { get } ``` |
| To | ``` var inputs: [AVAudioSessionPortDescription] { get } ``` |

Modified [AVAudioSessionRouteDescription.outputs](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutedescription/1616552-outputs)

|  | Declaration |
| --- | --- |
| From | ``` var outputs: [AnyObject]! { get } ``` |
| To | ``` var outputs: [AVAudioSessionPortDescription] { get } ``` |

Modified [AVAudioSessionSetActiveOptions [struct]](https://developer.apple.com/documentation/avfoundation/avaudiosessionsetactiveoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVAudioSessionSetActiveOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var OptionNotifyOthersOnDeactivation: AVAudioSessionSetActiveOptions { get } } ``` | RawOptionSetType |
| To | ``` struct AVAudioSessionSetActiveOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var NotifyOthersOnDeactivation: AVAudioSessionSetActiveOptions { get } } ``` | OptionSetType |

Modified [AVAudioSessionSetActiveOptions.NotifyOthersOnDeactivation](https://developer.apple.com/documentation/avfoundation/avaudiosessionsetactiveoptions/avaudiosessionsetactiveoptionnotifyothersondeactivation)

|  | Declaration |
| --- | --- |
| From | ``` static var OptionNotifyOthersOnDeactivation: AVAudioSessionSetActiveOptions { get } ``` |
| To | ``` static var NotifyOthersOnDeactivation: AVAudioSessionSetActiveOptions { get } ``` |

Modified [AVAudioSessionSilenceSecondaryAudioHintType [enum]](https://developer.apple.com/documentation/avfoundation/avaudiosession/silencesecondaryaudiohinttype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [AVAudioTime](https://developer.apple.com/documentation/avfoundation/avaudiotime)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioTime : NSObject {     init!(audioTimeStamp ts: UnsafePointer<AudioTimeStamp>, sampleRate sampleRate: Double)     init!(hostTime hostTime: UInt64)     init!(sampleTime sampleTime: AVAudioFramePosition, atRate sampleRate: Double)     init!(hostTime hostTime: UInt64, sampleTime sampleTime: AVAudioFramePosition, atRate sampleRate: Double)     class func timeWithAudioTimeStamp(_ ts: UnsafePointer<AudioTimeStamp>, sampleRate sampleRate: Double) -> Self!     class func timeWithHostTime(_ hostTime: UInt64) -> Self!     class func timeWithSampleTime(_ sampleTime: AVAudioFramePosition, atRate sampleRate: Double) -> Self!     class func timeWithHostTime(_ hostTime: UInt64, sampleTime sampleTime: AVAudioFramePosition, atRate sampleRate: Double) -> Self!     class func hostTimeForSeconds(_ seconds: NSTimeInterval) -> UInt64     class func secondsForHostTime(_ hostTime: UInt64) -> NSTimeInterval     func extrapolateTimeFromAnchor(_ anchorTime: AVAudioTime!) -> AVAudioTime!     var hostTimeValid: Bool { get }     var hostTime: UInt64 { get }     var sampleTimeValid: Bool { get }     var sampleTime: AVAudioFramePosition { get }     var sampleRate: Double { get }     var audioTimeStamp: AudioTimeStamp { get } } ``` |
| To | ``` class AVAudioTime : NSObject {     init(audioTimeStamp ts: UnsafePointer<AudioTimeStamp>, sampleRate sampleRate: Double)     init(hostTime hostTime: UInt64)     init(sampleTime sampleTime: AVAudioFramePosition, atRate sampleRate: Double)     init(hostTime hostTime: UInt64, sampleTime sampleTime: AVAudioFramePosition, atRate sampleRate: Double)     class func timeWithAudioTimeStamp(_ ts: UnsafePointer<AudioTimeStamp>, sampleRate sampleRate: Double) -> Self     class func timeWithHostTime(_ hostTime: UInt64) -> Self     class func timeWithSampleTime(_ sampleTime: AVAudioFramePosition, atRate sampleRate: Double) -> Self     class func timeWithHostTime(_ hostTime: UInt64, sampleTime sampleTime: AVAudioFramePosition, atRate sampleRate: Double) -> Self     class func hostTimeForSeconds(_ seconds: NSTimeInterval) -> UInt64     class func secondsForHostTime(_ hostTime: UInt64) -> NSTimeInterval     func extrapolateTimeFromAnchor(_ anchorTime: AVAudioTime) -> AVAudioTime     var hostTimeValid: Bool { get }     var hostTime: UInt64 { get }     var sampleTimeValid: Bool { get }     var sampleTime: AVAudioFramePosition { get }     var sampleRate: Double { get }     var audioTimeStamp: AudioTimeStamp { get } } ``` |

Modified [AVAudioTime.extrapolateTimeFromAnchor(_: AVAudioTime) -> AVAudioTime](https://developer.apple.com/documentation/avfoundation/avaudiotime/1387772-extrapolatetime)

|  | Declaration |
| --- | --- |
| From | ``` func extrapolateTimeFromAnchor(_ anchorTime: AVAudioTime!) -> AVAudioTime! ``` |
| To | ``` func extrapolateTimeFromAnchor(_ anchorTime: AVAudioTime) -> AVAudioTime ``` |

Modified [AVAudioTime.init(audioTimeStamp: UnsafePointer<AudioTimeStamp>, sampleRate: Double)](https://developer.apple.com/documentation/avfoundation/avaudiotime/1389146-initwithaudiotimestamp)

|  | Declaration |
| --- | --- |
| From | ``` init!(audioTimeStamp ts: UnsafePointer<AudioTimeStamp>, sampleRate sampleRate: Double) ``` |
| To | ``` init(audioTimeStamp ts: UnsafePointer<AudioTimeStamp>, sampleRate sampleRate: Double) ``` |

Modified [AVAudioTime.init(hostTime: UInt64)](https://developer.apple.com/documentation/avfoundation/avaudiotime/1386954-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(hostTime hostTime: UInt64) ``` |
| To | ``` init(hostTime hostTime: UInt64) ``` |

Modified [AVAudioTime.init(hostTime: UInt64, sampleTime: AVAudioFramePosition, atRate: Double)](https://developer.apple.com/documentation/avfoundation/avaudiotime/1386568-initwithhosttime)

|  | Declaration |
| --- | --- |
| From | ``` init!(hostTime hostTime: UInt64, sampleTime sampleTime: AVAudioFramePosition, atRate sampleRate: Double) ``` |
| To | ``` init(hostTime hostTime: UInt64, sampleTime sampleTime: AVAudioFramePosition, atRate sampleRate: Double) ``` |

Modified [AVAudioTime.init(sampleTime: AVAudioFramePosition, atRate: Double)](https://developer.apple.com/documentation/avfoundation/avaudiotime/1387972-initwithsampletime)

|  | Declaration |
| --- | --- |
| From | ``` init!(sampleTime sampleTime: AVAudioFramePosition, atRate sampleRate: Double) ``` |
| To | ``` init(sampleTime sampleTime: AVAudioFramePosition, atRate sampleRate: Double) ``` |

Modified [AVAudioUnit](https://developer.apple.com/documentation/avfoundation/avaudiounit)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioUnit : AVAudioNode {     func loadAudioUnitPresetAtURL(_ url: NSURL!, error error: NSErrorPointer) -> Bool     var audioComponentDescription: AudioComponentDescription { get }     var audioUnit: AudioUnit { get }     var name: String! { get }     var manufacturerName: String! { get }     var version: Int { get } } ``` |
| To | ``` class AVAudioUnit : AVAudioNode {     class func instantiateWithComponentDescription(_ audioComponentDescription: AudioComponentDescription, options options: AudioComponentInstantiationOptions, completionHandler completionHandler: (AVAudioUnit?, NSError?) -> Void)     func loadAudioUnitPresetAtURL(_ url: NSURL) throws     var audioComponentDescription: AudioComponentDescription { get }     var audioUnit: AudioUnit { get }     var AUAudioUnit: AUAudioUnit { get }     var name: String { get }     var manufacturerName: String { get }     var version: Int { get } } ``` |

Modified [AVAudioUnit.loadAudioUnitPresetAtURL(_: NSURL) throws](https://developer.apple.com/documentation/avfoundation/avaudiounit/1387527-loadpreset)

|  | Declaration |
| --- | --- |
| From | ``` func loadAudioUnitPresetAtURL(_ url: NSURL!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func loadAudioUnitPresetAtURL(_ url: NSURL) throws ``` |

Modified [AVAudioUnit.manufacturerName](https://developer.apple.com/documentation/avfoundation/avaudiounit/1388972-manufacturername)

|  | Declaration |
| --- | --- |
| From | ``` var manufacturerName: String! { get } ``` |
| To | ``` var manufacturerName: String { get } ``` |

Modified [AVAudioUnit.name](https://developer.apple.com/documentation/avfoundation/avaudiounit/1390637-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [AVAudioUnitDistortionPreset [enum]](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVAudioUnitEffect](https://developer.apple.com/documentation/avfoundation/avaudiouniteffect)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioUnitEffect : AVAudioUnit {     init!(audioComponentDescription audioComponentDescription: AudioComponentDescription)     var bypass: Bool } ``` |
| To | ``` class AVAudioUnitEffect : AVAudioUnit {     init(audioComponentDescription audioComponentDescription: AudioComponentDescription)     var bypass: Bool } ``` |

Modified [AVAudioUnitEffect.init(audioComponentDescription: AudioComponentDescription)](https://developer.apple.com/documentation/avfoundation/avaudiouniteffect/1388397-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(audioComponentDescription audioComponentDescription: AudioComponentDescription) ``` |
| To | ``` init(audioComponentDescription audioComponentDescription: AudioComponentDescription) ``` |

Modified [AVAudioUnitEQ](https://developer.apple.com/documentation/avfoundation/avaudiouniteq)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioUnitEQ : AVAudioUnitEffect {     init!(numberOfBands numberOfBands: Int)     var bands: [AnyObject]! { get }     var globalGain: Float } ``` |
| To | ``` class AVAudioUnitEQ : AVAudioUnitEffect {     init(numberOfBands numberOfBands: Int)     var bands: [AVAudioUnitEQFilterParameters] { get }     var globalGain: Float } ``` |

Modified [AVAudioUnitEQ.bands](https://developer.apple.com/documentation/avfoundation/avaudiouniteq/1388840-bands)

|  | Declaration |
| --- | --- |
| From | ``` var bands: [AnyObject]! { get } ``` |
| To | ``` var bands: [AVAudioUnitEQFilterParameters] { get } ``` |

Modified [AVAudioUnitEQ.init(numberOfBands: Int)](https://developer.apple.com/documentation/avfoundation/avaudiouniteq/1390915-initwithnumberofbands)

|  | Declaration |
| --- | --- |
| From | ``` init!(numberOfBands numberOfBands: Int) ``` |
| To | ``` init(numberOfBands numberOfBands: Int) ``` |

Modified [AVAudioUnitEQFilterType [enum]](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVAudioUnitGenerator](https://developer.apple.com/documentation/avfoundation/avaudiounitgenerator)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioUnitGenerator : AVAudioUnit, AVAudioMixing, AVAudioStereoMixing, NSObjectProtocol, AVAudio3DMixing {     init!(audioComponentDescription audioComponentDescription: AudioComponentDescription)     var bypass: Bool } ``` |
| To | ``` class AVAudioUnitGenerator : AVAudioUnit, AVAudioMixing, AVAudioStereoMixing, AVAudio3DMixing {     init(audioComponentDescription audioComponentDescription: AudioComponentDescription)     var bypass: Bool } ``` |

Modified [AVAudioUnitGenerator.init(audioComponentDescription: AudioComponentDescription)](https://developer.apple.com/documentation/avfoundation/avaudiounitgenerator/1387964-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(audioComponentDescription audioComponentDescription: AudioComponentDescription) ``` |
| To | ``` init(audioComponentDescription audioComponentDescription: AudioComponentDescription) ``` |

Modified [AVAudioUnitMIDIInstrument](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVAudioUnitMIDIInstrument : AVAudioUnit {     init!(audioComponentDescription description: AudioComponentDescription)     func startNote(_ note: UInt8, withVelocity velocity: UInt8, onChannel channel: UInt8)     func stopNote(_ note: UInt8, onChannel channel: UInt8)     func sendController(_ controller: UInt8, withValue value: UInt8, onChannel channel: UInt8)     func sendPitchBend(_ pitchbend: UInt16, onChannel channel: UInt8)     func sendPressure(_ pressure: UInt8, onChannel channel: UInt8)     func sendPressureForKey(_ key: UInt8, withValue value: UInt8, onChannel channel: UInt8)     func sendProgramChange(_ program: UInt8, onChannel channel: UInt8)     func sendProgramChange(_ program: UInt8, bankMSB bankMSB: UInt8, bankLSB bankLSB: UInt8, onChannel channel: UInt8)     func sendMIDIEvent(_ midiStatus: UInt8, data1 data1: UInt8, data2 data2: UInt8)     func sendMIDIEvent(_ midiStatus: UInt8, data1 data1: UInt8)     func sendMIDISysExEvent(_ midiData: NSData!) } ``` | AnyObject |
| To | ``` class AVAudioUnitMIDIInstrument : AVAudioUnit, AVAudioMixing, AVAudioStereoMixing, AVAudio3DMixing {     init(audioComponentDescription description: AudioComponentDescription)     func startNote(_ note: UInt8, withVelocity velocity: UInt8, onChannel channel: UInt8)     func stopNote(_ note: UInt8, onChannel channel: UInt8)     func sendController(_ controller: UInt8, withValue value: UInt8, onChannel channel: UInt8)     func sendPitchBend(_ pitchbend: UInt16, onChannel channel: UInt8)     func sendPressure(_ pressure: UInt8, onChannel channel: UInt8)     func sendPressureForKey(_ key: UInt8, withValue value: UInt8, onChannel channel: UInt8)     func sendProgramChange(_ program: UInt8, onChannel channel: UInt8)     func sendProgramChange(_ program: UInt8, bankMSB bankMSB: UInt8, bankLSB bankLSB: UInt8, onChannel channel: UInt8)     func sendMIDIEvent(_ midiStatus: UInt8, data1 data1: UInt8, data2 data2: UInt8)     func sendMIDIEvent(_ midiStatus: UInt8, data1 data1: UInt8)     func sendMIDISysExEvent(_ midiData: NSData) } ``` | AVAudio3DMixing, AVAudioMixing, AVAudioStereoMixing, AnyObject, NSObjectProtocol |

Modified [AVAudioUnitMIDIInstrument.init(audioComponentDescription: AudioComponentDescription)](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1386929-initwithaudiocomponentdescriptio)

|  | Declaration |
| --- | --- |
| From | ``` init!(audioComponentDescription description: AudioComponentDescription) ``` |
| To | ``` init(audioComponentDescription description: AudioComponentDescription) ``` |

Modified [AVAudioUnitMIDIInstrument.sendMIDISysExEvent(_: NSData)](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1387812-sendmidisysexevent)

|  | Declaration |
| --- | --- |
| From | ``` func sendMIDISysExEvent(_ midiData: NSData!) ``` |
| To | ``` func sendMIDISysExEvent(_ midiData: NSData) ``` |

Modified [AVAudioUnitReverbPreset [enum]](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVAudioUnitSampler](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioUnitSampler : AVAudioUnitMIDIInstrument {     func loadSoundBankInstrumentAtURL(_ bankURL: NSURL!, program program: UInt8, bankMSB bankMSB: UInt8, bankLSB bankLSB: UInt8, error outError: NSErrorPointer) -> Bool     func loadInstrumentAtURL(_ instrumentURL: NSURL!, error outError: NSErrorPointer) -> Bool     func loadAudioFilesAtURLs(_ audioFiles: [AnyObject]!, error outError: NSErrorPointer) -> Bool     var stereoPan: Float     var masterGain: Float     var globalTuning: Float } ``` |
| To | ``` class AVAudioUnitSampler : AVAudioUnitMIDIInstrument {     func loadSoundBankInstrumentAtURL(_ bankURL: NSURL, program program: UInt8, bankMSB bankMSB: UInt8, bankLSB bankLSB: UInt8) throws     func loadInstrumentAtURL(_ instrumentURL: NSURL) throws     func loadAudioFilesAtURLs(_ audioFiles: [NSURL]) throws     var stereoPan: Float     var masterGain: Float     var globalTuning: Float } ``` |

Modified [AVAudioUnitSampler.loadAudioFilesAtURLs(_: [NSURL]) throws](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1388631-loadaudiofilesaturls)

|  | Declaration |
| --- | --- |
| From | ``` func loadAudioFilesAtURLs(_ audioFiles: [AnyObject]!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func loadAudioFilesAtURLs(_ audioFiles: [NSURL]) throws ``` |

Modified [AVAudioUnitSampler.loadInstrumentAtURL(_: NSURL) throws](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1389514-loadinstrumentaturl)

|  | Declaration |
| --- | --- |
| From | ``` func loadInstrumentAtURL(_ instrumentURL: NSURL!, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func loadInstrumentAtURL(_ instrumentURL: NSURL) throws ``` |

Modified [AVAudioUnitSampler.loadSoundBankInstrumentAtURL(_: NSURL, program: UInt8, bankMSB: UInt8, bankLSB: UInt8) throws](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1385687-loadsoundbankinstrumentaturl)

|  | Declaration |
| --- | --- |
| From | ``` func loadSoundBankInstrumentAtURL(_ bankURL: NSURL!, program program: UInt8, bankMSB bankMSB: UInt8, bankLSB bankLSB: UInt8, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func loadSoundBankInstrumentAtURL(_ bankURL: NSURL, program program: UInt8, bankMSB bankMSB: UInt8, bankLSB bankLSB: UInt8) throws ``` |

Modified [AVAudioUnitTimeEffect](https://developer.apple.com/documentation/avfoundation/avaudiounittimeeffect)

|  | Declaration |
| --- | --- |
| From | ``` class AVAudioUnitTimeEffect : AVAudioUnit {     init!(audioComponentDescription audioComponentDescription: AudioComponentDescription)     var bypass: Bool } ``` |
| To | ``` class AVAudioUnitTimeEffect : AVAudioUnit {     init(audioComponentDescription audioComponentDescription: AudioComponentDescription)     var bypass: Bool } ``` |

Modified [AVAudioUnitTimeEffect.init(audioComponentDescription: AudioComponentDescription)](https://developer.apple.com/documentation/avfoundation/avaudiounittimeeffect/1390254-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(audioComponentDescription audioComponentDescription: AudioComponentDescription) ``` |
| To | ``` init(audioComponentDescription audioComponentDescription: AudioComponentDescription) ``` |

Modified [AVAuthorizationStatus [enum]](https://developer.apple.com/documentation/avfoundation/avauthorizationstatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVCaptureAudioDataOutputSampleBufferDelegate.captureOutput(_: AVCaptureOutput!, didOutputSampleBuffer: CMSampleBuffer!, fromConnection: AVCaptureConnection!)](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutputsamplebufferdelegate/1386039-captureoutput)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified [AVCaptureAutoFocusRangeRestriction [enum]](https://developer.apple.com/documentation/avfoundation/avcaptureautofocusrangerestriction)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVCaptureAutoFocusSystem [enum]](https://developer.apple.com/documentation/avfoundation/avcaptureautofocussystem)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVCaptureConnection](https://developer.apple.com/documentation/avfoundation/avcaptureconnection)

|  | Declaration |
| --- | --- |
| From | ``` class AVCaptureConnection : NSObject {     init!(inputPorts ports: [AnyObject]!, output output: AVCaptureOutput!) -> AVCaptureConnection     class func connectionWithInputPorts(_ ports: [AnyObject]!, output output: AVCaptureOutput!) -> AVCaptureConnection!     init!(inputPort port: AVCaptureInputPort!, videoPreviewLayer layer: AVCaptureVideoPreviewLayer!) -> AVCaptureConnection     class func connectionWithInputPort(_ port: AVCaptureInputPort!, videoPreviewLayer layer: AVCaptureVideoPreviewLayer!) -> AVCaptureConnection!     init!(inputPorts ports: [AnyObject]!, output output: AVCaptureOutput!)     init!(inputPort port: AVCaptureInputPort!, videoPreviewLayer layer: AVCaptureVideoPreviewLayer!)     var inputPorts: [AnyObject]! { get }     var output: AVCaptureOutput! { get }     var videoPreviewLayer: AVCaptureVideoPreviewLayer! { get }     var enabled: Bool     var active: Bool { get }     var audioChannels: [AnyObject]! { get }     var supportsVideoMirroring: Bool { get }     var videoMirrored: Bool     var automaticallyAdjustsVideoMirroring: Bool     var supportsVideoOrientation: Bool { get }     var videoOrientation: AVCaptureVideoOrientation     var supportsVideoMinFrameDuration: Bool { get }     var videoMinFrameDuration: CMTime     var supportsVideoMaxFrameDuration: Bool { get }     var videoMaxFrameDuration: CMTime     var videoMaxScaleAndCropFactor: CGFloat { get }     var videoScaleAndCropFactor: CGFloat     var preferredVideoStabilizationMode: AVCaptureVideoStabilizationMode     var activeVideoStabilizationMode: AVCaptureVideoStabilizationMode { get }     var supportsVideoStabilization: Bool { get }     var videoStabilizationEnabled: Bool { get }     var enablesVideoStabilizationWhenAvailable: Bool } ``` |
| To | ``` class AVCaptureConnection : NSObject {     convenience init!(inputPorts ports: [AnyObject]!, output output: AVCaptureOutput!)     class func connectionWithInputPorts(_ ports: [AnyObject]!, output output: AVCaptureOutput!) -> Self!     convenience init!(inputPort port: AVCaptureInputPort!, videoPreviewLayer layer: AVCaptureVideoPreviewLayer!)     class func connectionWithInputPort(_ port: AVCaptureInputPort!, videoPreviewLayer layer: AVCaptureVideoPreviewLayer!) -> Self!     init!(inputPorts ports: [AnyObject]!, output output: AVCaptureOutput!)     init!(inputPort port: AVCaptureInputPort!, videoPreviewLayer layer: AVCaptureVideoPreviewLayer!)     var inputPorts: [AnyObject]! { get }     var output: AVCaptureOutput! { get }     var videoPreviewLayer: AVCaptureVideoPreviewLayer! { get }     var enabled: Bool     var active: Bool { get }     var audioChannels: [AnyObject]! { get }     var supportsVideoMirroring: Bool { get }     var videoMirrored: Bool     var automaticallyAdjustsVideoMirroring: Bool     var supportsVideoOrientation: Bool { get }     var videoOrientation: AVCaptureVideoOrientation     var supportsVideoMinFrameDuration: Bool { get }     var videoMinFrameDuration: CMTime     var supportsVideoMaxFrameDuration: Bool { get }     var videoMaxFrameDuration: CMTime     var videoMaxScaleAndCropFactor: CGFloat { get }     var videoScaleAndCropFactor: CGFloat     var preferredVideoStabilizationMode: AVCaptureVideoStabilizationMode     var activeVideoStabilizationMode: AVCaptureVideoStabilizationMode { get }     var supportsVideoStabilization: Bool { get }     var videoStabilizationEnabled: Bool { get }     var enablesVideoStabilizationWhenAvailable: Bool } ``` |

Modified [AVCaptureDevice](https://developer.apple.com/documentation/avfoundation/avcapturedevice)

|  | Declaration |
| --- | --- |
| From | ``` class AVCaptureDevice : NSObject {     class func devices() -> [AnyObject]!     class func devicesWithMediaType(_ mediaType: String!) -> [AnyObject]!     class func defaultDeviceWithMediaType(_ mediaType: String!) -> AVCaptureDevice!     init!(uniqueID deviceUniqueID: String!) -> AVCaptureDevice     class func deviceWithUniqueID(_ deviceUniqueID: String!) -> AVCaptureDevice!     var uniqueID: String! { get }     var modelID: String! { get }     var localizedName: String! { get }     func hasMediaType(_ mediaType: String!) -> Bool     func lockForConfiguration(_ outError: NSErrorPointer) -> Bool     func unlockForConfiguration()     func supportsAVCaptureSessionPreset(_ preset: String!) -> Bool     var connected: Bool { get }     var formats: [AnyObject]! { get }     var activeFormat: AVCaptureDeviceFormat!     var activeVideoMinFrameDuration: CMTime     var activeVideoMaxFrameDuration: CMTime } extension AVCaptureDevice {     var position: AVCaptureDevicePosition { get } } extension AVCaptureDevice {     var hasFlash: Bool { get }     var flashAvailable: Bool { get }     var flashActive: Bool { get }     func isFlashModeSupported(_ flashMode: AVCaptureFlashMode) -> Bool     var flashMode: AVCaptureFlashMode } extension AVCaptureDevice {     var hasTorch: Bool { get }     var torchAvailable: Bool { get }     var torchActive: Bool { get }     var torchLevel: Float { get }     func isTorchModeSupported(_ torchMode: AVCaptureTorchMode) -> Bool     var torchMode: AVCaptureTorchMode     func setTorchModeOnWithLevel(_ torchLevel: Float, error outError: NSErrorPointer) -> Bool } extension AVCaptureDevice {     func isFocusModeSupported(_ focusMode: AVCaptureFocusMode) -> Bool     var focusMode: AVCaptureFocusMode     var focusPointOfInterestSupported: Bool { get }     var focusPointOfInterest: CGPoint     var adjustingFocus: Bool { get }     var autoFocusRangeRestrictionSupported: Bool { get }     var autoFocusRangeRestriction: AVCaptureAutoFocusRangeRestriction     var smoothAutoFocusSupported: Bool { get }     var smoothAutoFocusEnabled: Bool     var lensPosition: Float { get }     func setFocusModeLockedWithLensPosition(_ lensPosition: Float, completionHandler handler: ((CMTime) -> Void)!) } extension AVCaptureDevice {     func isExposureModeSupported(_ exposureMode: AVCaptureExposureMode) -> Bool     var exposureMode: AVCaptureExposureMode     var exposurePointOfInterestSupported: Bool { get }     var exposurePointOfInterest: CGPoint     var adjustingExposure: Bool { get }     var lensAperture: Float { get }     var exposureDuration: CMTime { get }     var ISO: Float { get }     func setExposureModeCustomWithDuration(_ duration: CMTime, ISO ISO: Float, completionHandler handler: ((CMTime) -> Void)!)     var exposureTargetOffset: Float { get }     var exposureTargetBias: Float { get }     var minExposureTargetBias: Float { get }     var maxExposureTargetBias: Float { get }     func setExposureTargetBias(_ bias: Float, completionHandler handler: ((CMTime) -> Void)!) } extension AVCaptureDevice {     func isWhiteBalanceModeSupported(_ whiteBalanceMode: AVCaptureWhiteBalanceMode) -> Bool     var whiteBalanceMode: AVCaptureWhiteBalanceMode     var adjustingWhiteBalance: Bool { get }     var deviceWhiteBalanceGains: AVCaptureWhiteBalanceGains { get }     var grayWorldDeviceWhiteBalanceGains: AVCaptureWhiteBalanceGains { get }     var maxWhiteBalanceGain: Float { get }     func setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains(_ whiteBalanceGains: AVCaptureWhiteBalanceGains, completionHandler handler: ((CMTime) -> Void)!)     func chromaticityValuesForDeviceWhiteBalanceGains(_ whiteBalanceGains: AVCaptureWhiteBalanceGains) -> AVCaptureWhiteBalanceChromaticityValues     func deviceWhiteBalanceGainsForChromaticityValues(_ chromaticityValues: AVCaptureWhiteBalanceChromaticityValues) -> AVCaptureWhiteBalanceGains     func temperatureAndTintValuesForDeviceWhiteBalanceGains(_ whiteBalanceGains: AVCaptureWhiteBalanceGains) -> AVCaptureWhiteBalanceTemperatureAndTintValues     func deviceWhiteBalanceGainsForTemperatureAndTintValues(_ tempAndTintValues: AVCaptureWhiteBalanceTemperatureAndTintValues) -> AVCaptureWhiteBalanceGains } extension AVCaptureDevice {     var subjectAreaChangeMonitoringEnabled: Bool } extension AVCaptureDevice {     var lowLightBoostSupported: Bool { get }     var lowLightBoostEnabled: Bool { get }     var automaticallyEnablesLowLightBoostWhenAvailable: Bool } extension AVCaptureDevice {     var videoZoomFactor: CGFloat     func rampToVideoZoomFactor(_ factor: CGFloat, withRate rate: Float)     var rampingVideoZoom: Bool { get }     func cancelVideoZoomRamp() } extension AVCaptureDevice {     class func authorizationStatusForMediaType(_ mediaType: String!) -> AVAuthorizationStatus     class func requestAccessForMediaType(_ mediaType: String!, completionHandler handler: ((Bool) -> Void)!) } extension AVCaptureDevice {     var automaticallyAdjustsVideoHDREnabled: Bool     var videoHDREnabled: Bool } ``` |
| To | ``` class AVCaptureDevice : NSObject {     class func devices() -> [AnyObject]!     class func devicesWithMediaType(_ mediaType: String!) -> [AnyObject]!     class func defaultDeviceWithMediaType(_ mediaType: String!) -> AVCaptureDevice!      init!(uniqueID deviceUniqueID: String!)     class func deviceWithUniqueID(_ deviceUniqueID: String!) -> AVCaptureDevice!     var uniqueID: String! { get }     var modelID: String! { get }     var localizedName: String! { get }     func hasMediaType(_ mediaType: String!) -> Bool     func lockForConfiguration() throws     func unlockForConfiguration()     func supportsAVCaptureSessionPreset(_ preset: String!) -> Bool     var connected: Bool { get }     var formats: [AnyObject]! { get }     var activeFormat: AVCaptureDeviceFormat!     var activeVideoMinFrameDuration: CMTime     var activeVideoMaxFrameDuration: CMTime } extension AVCaptureDevice {     var position: AVCaptureDevicePosition { get } } extension AVCaptureDevice {     var hasFlash: Bool { get }     var flashAvailable: Bool { get }     var flashActive: Bool { get }     func isFlashModeSupported(_ flashMode: AVCaptureFlashMode) -> Bool     var flashMode: AVCaptureFlashMode } extension AVCaptureDevice {     var hasTorch: Bool { get }     var torchAvailable: Bool { get }     var torchActive: Bool { get }     var torchLevel: Float { get }     func isTorchModeSupported(_ torchMode: AVCaptureTorchMode) -> Bool     var torchMode: AVCaptureTorchMode     func setTorchModeOnWithLevel(_ torchLevel: Float) throws } extension AVCaptureDevice {     func isFocusModeSupported(_ focusMode: AVCaptureFocusMode) -> Bool     var focusMode: AVCaptureFocusMode     var focusPointOfInterestSupported: Bool { get }     var focusPointOfInterest: CGPoint     var adjustingFocus: Bool { get }     var autoFocusRangeRestrictionSupported: Bool { get }     var autoFocusRangeRestriction: AVCaptureAutoFocusRangeRestriction     var smoothAutoFocusSupported: Bool { get }     var smoothAutoFocusEnabled: Bool     var lensPosition: Float { get }     func setFocusModeLockedWithLensPosition(_ lensPosition: Float, completionHandler handler: ((CMTime) -> Void)!) } extension AVCaptureDevice {     func isExposureModeSupported(_ exposureMode: AVCaptureExposureMode) -> Bool     var exposureMode: AVCaptureExposureMode     var exposurePointOfInterestSupported: Bool { get }     var exposurePointOfInterest: CGPoint     var adjustingExposure: Bool { get }     var lensAperture: Float { get }     var exposureDuration: CMTime { get }     var ISO: Float { get }     func setExposureModeCustomWithDuration(_ duration: CMTime, ISO ISO: Float, completionHandler handler: ((CMTime) -> Void)!)     var exposureTargetOffset: Float { get }     var exposureTargetBias: Float { get }     var minExposureTargetBias: Float { get }     var maxExposureTargetBias: Float { get }     func setExposureTargetBias(_ bias: Float, completionHandler handler: ((CMTime) -> Void)!) } extension AVCaptureDevice {     func isWhiteBalanceModeSupported(_ whiteBalanceMode: AVCaptureWhiteBalanceMode) -> Bool     var whiteBalanceMode: AVCaptureWhiteBalanceMode     var adjustingWhiteBalance: Bool { get }     var deviceWhiteBalanceGains: AVCaptureWhiteBalanceGains { get }     var grayWorldDeviceWhiteBalanceGains: AVCaptureWhiteBalanceGains { get }     var maxWhiteBalanceGain: Float { get }     func setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains(_ whiteBalanceGains: AVCaptureWhiteBalanceGains, completionHandler handler: ((CMTime) -> Void)!)     func chromaticityValuesForDeviceWhiteBalanceGains(_ whiteBalanceGains: AVCaptureWhiteBalanceGains) -> AVCaptureWhiteBalanceChromaticityValues     func deviceWhiteBalanceGainsForChromaticityValues(_ chromaticityValues: AVCaptureWhiteBalanceChromaticityValues) -> AVCaptureWhiteBalanceGains     func temperatureAndTintValuesForDeviceWhiteBalanceGains(_ whiteBalanceGains: AVCaptureWhiteBalanceGains) -> AVCaptureWhiteBalanceTemperatureAndTintValues     func deviceWhiteBalanceGainsForTemperatureAndTintValues(_ tempAndTintValues: AVCaptureWhiteBalanceTemperatureAndTintValues) -> AVCaptureWhiteBalanceGains } extension AVCaptureDevice {     var subjectAreaChangeMonitoringEnabled: Bool } extension AVCaptureDevice {     var lowLightBoostSupported: Bool { get }     var lowLightBoostEnabled: Bool { get }     var automaticallyEnablesLowLightBoostWhenAvailable: Bool } extension AVCaptureDevice {     var videoZoomFactor: CGFloat     func rampToVideoZoomFactor(_ factor: CGFloat, withRate rate: Float)     var rampingVideoZoom: Bool { get }     func cancelVideoZoomRamp() } extension AVCaptureDevice {     class func authorizationStatusForMediaType(_ mediaType: String!) -> AVAuthorizationStatus     class func requestAccessForMediaType(_ mediaType: String!, completionHandler handler: ((Bool) -> Void)!) } extension AVCaptureDevice {     var automaticallyAdjustsVideoHDREnabled: Bool     var videoHDREnabled: Bool } ``` |

Modified [AVCaptureDevice.init(uniqueID: String!)](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1388904-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(uniqueID deviceUniqueID: String!) -> AVCaptureDevice ``` |
| To | ``` init!(uniqueID deviceUniqueID: String!) ``` |

Modified [AVCaptureDevice.lockForConfiguration() throws](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1387810-lockforconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` func lockForConfiguration(_ outError: NSErrorPointer) -> Bool ``` |
| To | ``` func lockForConfiguration() throws ``` |

Modified [AVCaptureDevice.setTorchModeOnWithLevel(_: Float) throws](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624609-settorchmodeon)

|  | Declaration |
| --- | --- |
| From | ``` func setTorchModeOnWithLevel(_ torchLevel: Float, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func setTorchModeOnWithLevel(_ torchLevel: Float) throws ``` |

Modified [AVCaptureDeviceInput](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput)

|  | Declaration |
| --- | --- |
| From | ``` class AVCaptureDeviceInput : AVCaptureInput {     class func deviceInputWithDevice(_ device: AVCaptureDevice!, error outError: NSErrorPointer) -> AnyObject!     init!(device device: AVCaptureDevice!, error outError: NSErrorPointer)     var device: AVCaptureDevice! { get } } ``` |
| To | ``` class AVCaptureDeviceInput : AVCaptureInput {     convenience init(device device: AVCaptureDevice!) throws     class func deviceInputWithDevice(_ device: AVCaptureDevice!) throws -> Self     init(device device: AVCaptureDevice!) throws     var device: AVCaptureDevice! { get } } ``` |

Modified [AVCaptureDeviceInput.init(device: AVCaptureDevice!) throws](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/1387609-initwithdevice)

|  | Declaration |
| --- | --- |
| From | ``` init!(device device: AVCaptureDevice!, error outError: NSErrorPointer) ``` |
| To | ``` init(device device: AVCaptureDevice!) throws ``` |

Modified [AVCaptureDevicePosition [enum]](https://developer.apple.com/documentation/avfoundation/avcapturedeviceposition)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVCaptureExposureMode [enum]](https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposuremode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVCaptureFileOutputRecordingDelegate.captureOutput(_: AVCaptureFileOutput!, didFinishRecordingToOutputFileAtURL: NSURL!, fromConnections: [AnyObject]!, error: NSError!)](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate/1390612-captureoutput)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified [AVCaptureFileOutputRecordingDelegate.captureOutput(_: AVCaptureFileOutput!, didStartRecordingToOutputFileAtURL: NSURL!, fromConnections: [AnyObject]!)](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate/1387301-captureoutput)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified [AVCaptureFlashMode [enum]](https://developer.apple.com/documentation/avfoundation/avcapturedevice/flashmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVCaptureFocusMode [enum]](https://developer.apple.com/documentation/avfoundation/avcapturedevice/focusmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVCaptureMetadataOutputObjectsDelegate.captureOutput(_: AVCaptureOutput!, didOutputMetadataObjects: [AnyObject]!, fromConnection: AVCaptureConnection!)](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutputobjectsdelegate/1389481-metadataoutput)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified [AVCaptureMovieFileOutput](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput)

|  | Declaration |
| --- | --- |
| From | ``` class AVCaptureMovieFileOutput : AVCaptureFileOutput {     var movieFragmentInterval: CMTime     var metadata: [AnyObject]! } ``` |
| To | ``` class AVCaptureMovieFileOutput : AVCaptureFileOutput {     var movieFragmentInterval: CMTime     var metadata: [AnyObject]!     func recordsVideoOrientationAndMirroringChangesAsMetadataTrackForConnection(_ connection: AVCaptureConnection!) -> Bool     func setRecordsVideoOrientationAndMirroringChanges(_ doRecordChanges: Bool, asMetadataTrackForConnection connection: AVCaptureConnection!) } ``` |

Modified [AVCaptureStillImageOutput](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput)

|  | Declaration |
| --- | --- |
| From | ``` class AVCaptureStillImageOutput : AVCaptureOutput {     var outputSettings: [NSObject : AnyObject]!     var availableImageDataCVPixelFormatTypes: [AnyObject]! { get }     var availableImageDataCodecTypes: [AnyObject]! { get }     var stillImageStabilizationSupported: Bool { get }     var automaticallyEnablesStillImageStabilizationWhenAvailable: Bool     var stillImageStabilizationActive: Bool { get }     var highResolutionStillImageOutputEnabled: Bool     var capturingStillImage: Bool { get }     func captureStillImageAsynchronouslyFromConnection(_ connection: AVCaptureConnection!, completionHandler handler: ((CMSampleBuffer!, NSError!) -> Void)!)     class func jpegStillImageNSDataRepresentation(_ jpegSampleBuffer: CMSampleBuffer!) -> NSData! } extension AVCaptureStillImageOutput {     var maxBracketedCaptureStillImageCount: Int { get }     func prepareToCaptureStillImageBracketFromConnection(_ connection: AVCaptureConnection!, withSettingsArray settings: [AnyObject]!, completionHandler handler: ((Bool, NSError!) -> Void)!)     func captureStillImageBracketAsynchronouslyFromConnection(_ connection: AVCaptureConnection!, withSettingsArray settings: [AnyObject]!, completionHandler handler: ((CMSampleBuffer!, AVCaptureBracketedStillImageSettings!, NSError!) -> Void)!) } ``` |
| To | ``` class AVCaptureStillImageOutput : AVCaptureOutput {     var outputSettings: [NSObject : AnyObject]!     var availableImageDataCVPixelFormatTypes: [AnyObject]! { get }     var availableImageDataCodecTypes: [AnyObject]! { get }     var stillImageStabilizationSupported: Bool { get }     var automaticallyEnablesStillImageStabilizationWhenAvailable: Bool     var stillImageStabilizationActive: Bool { get }     var highResolutionStillImageOutputEnabled: Bool     var capturingStillImage: Bool { get }     func captureStillImageAsynchronouslyFromConnection(_ connection: AVCaptureConnection!, completionHandler handler: ((CMSampleBuffer!, NSError!) -> Void)!)     class func jpegStillImageNSDataRepresentation(_ jpegSampleBuffer: CMSampleBuffer!) -> NSData! } extension AVCaptureStillImageOutput {     var maxBracketedCaptureStillImageCount: Int { get }     var lensStabilizationDuringBracketedCaptureSupported: Bool { get }     var lensStabilizationDuringBracketedCaptureEnabled: Bool     func prepareToCaptureStillImageBracketFromConnection(_ connection: AVCaptureConnection!, withSettingsArray settings: [AnyObject]!, completionHandler handler: ((Bool, NSError!) -> Void)!)     func captureStillImageBracketAsynchronouslyFromConnection(_ connection: AVCaptureConnection!, withSettingsArray settings: [AnyObject]!, completionHandler handler: ((CMSampleBuffer!, AVCaptureBracketedStillImageSettings!, NSError!) -> Void)!) } ``` |

Modified [AVCaptureTorchMode [enum]](https://developer.apple.com/documentation/avfoundation/avcapturedevice/torchmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVCaptureVideoDataOutputSampleBufferDelegate.captureOutput(_: AVCaptureOutput!, didOutputSampleBuffer: CMSampleBuffer!, fromConnection: AVCaptureConnection!)](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate/1385775-captureoutput)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified [AVCaptureVideoOrientation [enum]](https://developer.apple.com/documentation/avfoundation/avcapturevideoorientation)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVCaptureVideoPreviewLayer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer)

|  | Declaration |
| --- | --- |
| From | ``` class AVCaptureVideoPreviewLayer : CALayer {     class func layerWithSession(_ session: AVCaptureSession!) -> AnyObject!     init!(session session: AVCaptureSession!)     class func layerWithSessionWithNoConnection(_ session: AVCaptureSession!) -> AnyObject!     init!(sessionWithNoConnection session: AVCaptureSession!)     var session: AVCaptureSession!     func setSessionWithNoConnection(_ session: AVCaptureSession!)     var connection: AVCaptureConnection! { get }     var videoGravity: String!     func captureDevicePointOfInterestForPoint(_ pointInLayer: CGPoint) -> CGPoint     func pointForCaptureDevicePointOfInterest(_ captureDevicePointOfInterest: CGPoint) -> CGPoint     func metadataOutputRectOfInterestForRect(_ rectInLayerCoordinates: CGRect) -> CGRect     func rectForMetadataOutputRectOfInterest(_ rectInMetadataOutputCoordinates: CGRect) -> CGRect     func transformedMetadataObjectForMetadataObject(_ metadataObject: AVMetadataObject!) -> AVMetadataObject!     var orientationSupported: Bool { get }     var orientation: AVCaptureVideoOrientation     var mirroringSupported: Bool { get }     var automaticallyAdjustsMirroring: Bool     var mirrored: Bool } ``` |
| To | ``` class AVCaptureVideoPreviewLayer : CALayer {     convenience init!(session session: AVCaptureSession!)     class func layerWithSession(_ session: AVCaptureSession!) -> Self!     init!(session session: AVCaptureSession!)     convenience init!(sessionWithNoConnection session: AVCaptureSession!)     class func layerWithSessionWithNoConnection(_ session: AVCaptureSession!) -> Self!     init!(sessionWithNoConnection session: AVCaptureSession!)     var session: AVCaptureSession!     func setSessionWithNoConnection(_ session: AVCaptureSession!)     var connection: AVCaptureConnection! { get }     var videoGravity: String!     func captureDevicePointOfInterestForPoint(_ pointInLayer: CGPoint) -> CGPoint     func pointForCaptureDevicePointOfInterest(_ captureDevicePointOfInterest: CGPoint) -> CGPoint     func metadataOutputRectOfInterestForRect(_ rectInLayerCoordinates: CGRect) -> CGRect     func rectForMetadataOutputRectOfInterest(_ rectInMetadataOutputCoordinates: CGRect) -> CGRect     func transformedMetadataObjectForMetadataObject(_ metadataObject: AVMetadataObject!) -> AVMetadataObject!     var orientationSupported: Bool { get }     var orientation: AVCaptureVideoOrientation     var mirroringSupported: Bool { get }     var automaticallyAdjustsMirroring: Bool     var mirrored: Bool } ``` |

Modified [AVCaptureVideoStabilizationMode [enum]](https://developer.apple.com/documentation/avfoundation/avcapturevideostabilizationmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVCaptureWhiteBalanceMode [enum]](https://developer.apple.com/documentation/avfoundation/avcapturedevice/whitebalancemode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVComposition](https://developer.apple.com/documentation/avfoundation/avcomposition)

|  | Declaration |
| --- | --- |
| From | ``` class AVComposition : AVAsset, NSMutableCopying {     var tracks: [AnyObject]! { get }     var naturalSize: CGSize { get } } ``` |
| To | ``` class AVComposition : AVAsset, NSMutableCopying {     var tracks: [AVCompositionTrack] { get }     var naturalSize: CGSize { get }     var URLAssetInitializationOptions: [String : AnyObject] { get } } extension AVComposition {     func trackWithTrackID(_ trackID: CMPersistentTrackID) -> AVCompositionTrack?     func tracksWithMediaType(_ mediaType: String) -> [AVCompositionTrack]     func tracksWithMediaCharacteristic(_ mediaCharacteristic: String) -> [AVCompositionTrack] } ``` |

Modified [AVComposition.tracks](https://developer.apple.com/documentation/avfoundation/avcomposition/1390165-tracks)

|  | Declaration |
| --- | --- |
| From | ``` var tracks: [AnyObject]! { get } ``` |
| To | ``` var tracks: [AVCompositionTrack] { get } ``` |

Modified [AVCompositionTrack](https://developer.apple.com/documentation/avfoundation/avcompositiontrack)

|  | Declaration |
| --- | --- |
| From | ``` class AVCompositionTrack : AVAssetTrack {     var segments: [AnyObject]! { get } } ``` |
| To | ``` class AVCompositionTrack : AVAssetTrack {     var segments: [AVCompositionTrackSegment] { get } } ``` |

Modified [AVCompositionTrack.segments](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/1387267-segments)

|  | Declaration |
| --- | --- |
| From | ``` var segments: [AnyObject]! { get } ``` |
| To | ``` var segments: [AVCompositionTrackSegment] { get } ``` |

Modified [AVCompositionTrackSegment](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment)

|  | Declaration |
| --- | --- |
| From | ``` class AVCompositionTrackSegment : AVAssetTrackSegment {     init!(URL URL: NSURL!, trackID trackID: CMPersistentTrackID, sourceTimeRange sourceTimeRange: CMTimeRange, targetTimeRange targetTimeRange: CMTimeRange) -> AVCompositionTrackSegment     class func compositionTrackSegmentWithURL(_ URL: NSURL!, trackID trackID: CMPersistentTrackID, sourceTimeRange sourceTimeRange: CMTimeRange, targetTimeRange targetTimeRange: CMTimeRange) -> AVCompositionTrackSegment!     init!(timeRange timeRange: CMTimeRange) -> AVCompositionTrackSegment     class func compositionTrackSegmentWithTimeRange(_ timeRange: CMTimeRange) -> AVCompositionTrackSegment!     init!(URL URL: NSURL!, trackID trackID: CMPersistentTrackID, sourceTimeRange sourceTimeRange: CMTimeRange, targetTimeRange targetTimeRange: CMTimeRange)     init!(timeRange timeRange: CMTimeRange)     var empty: Bool { get }     var sourceURL: NSURL! { get }     var sourceTrackID: CMPersistentTrackID { get } } ``` |
| To | ``` class AVCompositionTrackSegment : AVAssetTrackSegment {     convenience init(URL URL: NSURL, trackID trackID: CMPersistentTrackID, sourceTimeRange sourceTimeRange: CMTimeRange, targetTimeRange targetTimeRange: CMTimeRange)     class func compositionTrackSegmentWithURL(_ URL: NSURL, trackID trackID: CMPersistentTrackID, sourceTimeRange sourceTimeRange: CMTimeRange, targetTimeRange targetTimeRange: CMTimeRange) -> Self     convenience init(timeRange timeRange: CMTimeRange)     class func compositionTrackSegmentWithTimeRange(_ timeRange: CMTimeRange) -> Self     init(URL URL: NSURL, trackID trackID: CMPersistentTrackID, sourceTimeRange sourceTimeRange: CMTimeRange, targetTimeRange targetTimeRange: CMTimeRange)     init(timeRange timeRange: CMTimeRange)     var empty: Bool { get }     var sourceURL: NSURL? { get }     var sourceTrackID: CMPersistentTrackID { get } } ``` |

Modified [AVCompositionTrackSegment.init(timeRange: CMTimeRange)](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/1386841-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(timeRange timeRange: CMTimeRange) ``` |
| To | ``` init(timeRange timeRange: CMTimeRange) ``` |

Modified [AVCompositionTrackSegment.init(URL: NSURL, trackID: CMPersistentTrackID, sourceTimeRange: CMTimeRange, targetTimeRange: CMTimeRange)](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/1390282-initwithurl)

|  | Declaration |
| --- | --- |
| From | ``` init!(URL URL: NSURL!, trackID trackID: CMPersistentTrackID, sourceTimeRange sourceTimeRange: CMTimeRange, targetTimeRange targetTimeRange: CMTimeRange) ``` |
| To | ``` init(URL URL: NSURL, trackID trackID: CMPersistentTrackID, sourceTimeRange sourceTimeRange: CMTimeRange, targetTimeRange targetTimeRange: CMTimeRange) ``` |

Modified [AVCompositionTrackSegment.sourceURL](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/1386814-sourceurl)

|  | Declaration |
| --- | --- |
| From | ``` var sourceURL: NSURL! { get } ``` |
| To | ``` var sourceURL: NSURL? { get } ``` |

Modified [AVError [enum]](https://developer.apple.com/documentation/avfoundation/averror/code)

|  | Declaration | Protocols | Raw Value Type |
| --- | --- | --- | --- |
| From | ``` enum AVError : Int {     case Unknown     case OutOfMemory     case SessionNotRunning     case DeviceAlreadyUsedByAnotherSession     case NoDataCaptured     case SessionConfigurationChanged     case DiskFull     case DeviceWasDisconnected     case MediaChanged     case MaximumDurationReached     case MaximumFileSizeReached     case MediaDiscontinuity     case MaximumNumberOfSamplesForFileFormatReached     case DeviceNotConnected     case DeviceInUseByAnotherApplication     case DeviceLockedForConfigurationByAnotherProcess     case SessionWasInterrupted     case MediaServicesWereReset     case ExportFailed     case DecodeFailed     case InvalidSourceMedia     case FileAlreadyExists     case CompositionTrackSegmentsNotContiguous     case InvalidCompositionTrackSegmentDuration     case InvalidCompositionTrackSegmentSourceStartTime     case InvalidCompositionTrackSegmentSourceDuration     case FileFormatNotRecognized     case FileFailedToParse     case MaximumStillImageCaptureRequestsExceeded     case ContentIsProtected     case NoImageAtTime     case DecoderNotFound     case EncoderNotFound     case ContentIsNotAuthorized     case ApplicationIsNotAuthorized     case DeviceIsNotAvailableInBackground     case OperationNotSupportedForAsset     case DecoderTemporarilyUnavailable     case EncoderTemporarilyUnavailable     case InvalidVideoComposition     case ReferenceForbiddenByReferencePolicy     case InvalidOutputURLPathExtension     case ScreenCaptureFailed     case DisplayWasDisabled     case TorchLevelUnavailable     case OperationInterrupted     case IncompatibleAsset     case FailedToLoadMediaData     case ServerIncorrectlyConfigured     case ApplicationIsNotAuthorizedToUseDevice     case FailedToParse     case FileTypeDoesNotSupportSampleReferences     case UndecodableMediaData     case AirPlayControllerRequiresInternet     case AirPlayReceiverRequiresInternet } ``` | Equatable, Hashable, RawRepresentable | -- |
| To | ``` enum AVError : Int {     case Unknown     case OutOfMemory     case SessionNotRunning     case DeviceAlreadyUsedByAnotherSession     case NoDataCaptured     case SessionConfigurationChanged     case DiskFull     case DeviceWasDisconnected     case MediaChanged     case MaximumDurationReached     case MaximumFileSizeReached     case MediaDiscontinuity     case MaximumNumberOfSamplesForFileFormatReached     case DeviceNotConnected     case DeviceInUseByAnotherApplication     case DeviceLockedForConfigurationByAnotherProcess     case SessionWasInterrupted     case MediaServicesWereReset     case ExportFailed     case DecodeFailed     case InvalidSourceMedia     case FileAlreadyExists     case CompositionTrackSegmentsNotContiguous     case InvalidCompositionTrackSegmentDuration     case InvalidCompositionTrackSegmentSourceStartTime     case InvalidCompositionTrackSegmentSourceDuration     case FileFormatNotRecognized     case FileFailedToParse     case MaximumStillImageCaptureRequestsExceeded     case ContentIsProtected     case NoImageAtTime     case DecoderNotFound     case EncoderNotFound     case ContentIsNotAuthorized     case ApplicationIsNotAuthorized     case DeviceIsNotAvailableInBackground     case OperationNotSupportedForAsset     case DecoderTemporarilyUnavailable     case EncoderTemporarilyUnavailable     case InvalidVideoComposition     case ReferenceForbiddenByReferencePolicy     case InvalidOutputURLPathExtension     case ScreenCaptureFailed     case DisplayWasDisabled     case TorchLevelUnavailable     case OperationInterrupted     case IncompatibleAsset     case FailedToLoadMediaData     case ServerIncorrectlyConfigured     case ApplicationIsNotAuthorizedToUseDevice     case FailedToParse     case FileTypeDoesNotSupportSampleReferences     case UndecodableMediaData     case AirPlayControllerRequiresInternet     case AirPlayReceiverRequiresInternet     case VideoCompositorFailed     case RecordingAlreadyInProgress } extension AVError : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension AVError : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable | Int |

Modified [AVError.DeviceIsNotAvailableInBackground](https://developer.apple.com/documentation/avfoundation/averror/code/deviceisnotavailableinbackground)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.3 | iOS 9.0 |

Modified [AVKeyValueStatus [enum]](https://developer.apple.com/documentation/avfoundation/avkeyvaluestatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVMediaSelectionGroup](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup)

|  | Declaration |
| --- | --- |
| From | ``` class AVMediaSelectionGroup : NSObject, NSCopying {     var options: [AnyObject]! { get }     var defaultOption: AVMediaSelectionOption! { get }     var allowsEmptySelection: Bool { get }     func mediaSelectionOptionWithPropertyList(_ plist: AnyObject!) -> AVMediaSelectionOption! } extension AVMediaSelectionGroup {     class func playableMediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AnyObject]!) -> [AnyObject]!     class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AnyObject]!, filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [AnyObject]!) -> [AnyObject]!     class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AnyObject]!, withLocale locale: NSLocale!) -> [AnyObject]!     class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AnyObject]!, withMediaCharacteristics mediaCharacteristics: [AnyObject]!) -> [AnyObject]!     class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AnyObject]!, withoutMediaCharacteristics mediaCharacteristics: [AnyObject]!) -> [AnyObject]! } ``` |
| To | ``` class AVMediaSelectionGroup : NSObject, NSCopying {     var options: [AVMediaSelectionOption] { get }     var defaultOption: AVMediaSelectionOption? { get }     var allowsEmptySelection: Bool { get }     func mediaSelectionOptionWithPropertyList(_ plist: AnyObject) -> AVMediaSelectionOption? } extension AVMediaSelectionGroup {     class func playableMediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AVMediaSelectionOption]) -> [AVMediaSelectionOption]     class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AVMediaSelectionOption], filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [String]) -> [AVMediaSelectionOption]     class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AVMediaSelectionOption], withLocale locale: NSLocale) -> [AVMediaSelectionOption]     class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AVMediaSelectionOption], withMediaCharacteristics mediaCharacteristics: [String]) -> [AVMediaSelectionOption]     class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AVMediaSelectionOption], withoutMediaCharacteristics mediaCharacteristics: [String]) -> [AVMediaSelectionOption] } extension AVMediaSelectionGroup {     func makeNowPlayingInfoLanguageOptionGroup() -> MPNowPlayingInfoLanguageOptionGroup } ``` |

Modified [AVMediaSelectionGroup.defaultOption](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1388440-defaultoption)

|  | Declaration |
| --- | --- |
| From | ``` var defaultOption: AVMediaSelectionOption! { get } ``` |
| To | ``` var defaultOption: AVMediaSelectionOption? { get } ``` |

Modified [AVMediaSelectionGroup.mediaSelectionOptionsFromArray(_: [AVMediaSelectionOption], filteredAndSortedAccordingToPreferredLanguages: [String]) -> [AVMediaSelectionOption] [class]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1387034-mediaselectionoptions)

|  | Declaration |
| --- | --- |
| From | ``` class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AnyObject]!, filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [AnyObject]!) -> [AnyObject]! ``` |
| To | ``` class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AVMediaSelectionOption], filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [String]) -> [AVMediaSelectionOption] ``` |

Modified [AVMediaSelectionGroup.mediaSelectionOptionsFromArray(_: [AVMediaSelectionOption], withLocale: NSLocale) -> [AVMediaSelectionOption] [class]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1387494-mediaselectionoptionsfromarray)

|  | Declaration |
| --- | --- |
| From | ``` class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AnyObject]!, withLocale locale: NSLocale!) -> [AnyObject]! ``` |
| To | ``` class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AVMediaSelectionOption], withLocale locale: NSLocale) -> [AVMediaSelectionOption] ``` |

Modified [AVMediaSelectionGroup.mediaSelectionOptionsFromArray(_: [AVMediaSelectionOption], withMediaCharacteristics: [String]) -> [AVMediaSelectionOption] [class]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1388258-mediaselectionoptions)

|  | Declaration |
| --- | --- |
| From | ``` class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AnyObject]!, withMediaCharacteristics mediaCharacteristics: [AnyObject]!) -> [AnyObject]! ``` |
| To | ``` class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AVMediaSelectionOption], withMediaCharacteristics mediaCharacteristics: [String]) -> [AVMediaSelectionOption] ``` |

Modified [AVMediaSelectionGroup.mediaSelectionOptionsFromArray(_: [AVMediaSelectionOption], withoutMediaCharacteristics: [String]) -> [AVMediaSelectionOption] [class]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1387631-mediaselectionoptionsfromarray)

|  | Declaration |
| --- | --- |
| From | ``` class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AnyObject]!, withoutMediaCharacteristics mediaCharacteristics: [AnyObject]!) -> [AnyObject]! ``` |
| To | ``` class func mediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AVMediaSelectionOption], withoutMediaCharacteristics mediaCharacteristics: [String]) -> [AVMediaSelectionOption] ``` |

Modified [AVMediaSelectionGroup.mediaSelectionOptionWithPropertyList(_: AnyObject) -> AVMediaSelectionOption?](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1389968-mediaselectionoption)

|  | Declaration |
| --- | --- |
| From | ``` func mediaSelectionOptionWithPropertyList(_ plist: AnyObject!) -> AVMediaSelectionOption! ``` |
| To | ``` func mediaSelectionOptionWithPropertyList(_ plist: AnyObject) -> AVMediaSelectionOption? ``` |

Modified [AVMediaSelectionGroup.options](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1388351-options)

|  | Declaration |
| --- | --- |
| From | ``` var options: [AnyObject]! { get } ``` |
| To | ``` var options: [AVMediaSelectionOption] { get } ``` |

Modified [AVMediaSelectionGroup.playableMediaSelectionOptionsFromArray(_: [AVMediaSelectionOption]) -> [AVMediaSelectionOption] [class]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1387351-playablemediaselectionoptions)

|  | Declaration |
| --- | --- |
| From | ``` class func playableMediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AnyObject]!) -> [AnyObject]! ``` |
| To | ``` class func playableMediaSelectionOptionsFromArray(_ mediaSelectionOptions: [AVMediaSelectionOption]) -> [AVMediaSelectionOption] ``` |

Modified [AVMediaSelectionOption](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption)

|  | Declaration |
| --- | --- |
| From | ``` class AVMediaSelectionOption : NSObject, NSCopying {     var mediaType: String! { get }     var mediaSubTypes: [AnyObject]! { get }     func hasMediaCharacteristic(_ mediaCharacteristic: String!) -> Bool     var playable: Bool { get }     var extendedLanguageTag: String! { get }     var locale: NSLocale! { get }     var commonMetadata: [AnyObject]! { get }     var availableMetadataFormats: [AnyObject]! { get }     func metadataForFormat(_ format: String!) -> [AnyObject]!     func associatedMediaSelectionOptionInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup!) -> AVMediaSelectionOption!     func propertyList() -> AnyObject!     func displayNameWithLocale(_ locale: NSLocale!) -> String!     var displayName: String! { get } } ``` |
| To | ``` class AVMediaSelectionOption : NSObject, NSCopying {     var mediaType: String { get }     var mediaSubTypes: [NSNumber] { get }     func hasMediaCharacteristic(_ mediaCharacteristic: String) -> Bool     var playable: Bool { get }     var extendedLanguageTag: String? { get }     var locale: NSLocale? { get }     var commonMetadata: [AVMetadataItem] { get }     var availableMetadataFormats: [String] { get }     func metadataForFormat(_ format: String) -> [AVMetadataItem]     func associatedMediaSelectionOptionInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption?     func propertyList() -> AnyObject     func displayNameWithLocale(_ locale: NSLocale) -> String     var displayName: String { get } } extension AVMediaSelectionOption {     func makeNowPlayingInfoLanguageOption() -> MPNowPlayingInfoLanguageOption? } ``` |

Modified [AVMediaSelectionOption.associatedMediaSelectionOptionInMediaSelectionGroup(_: AVMediaSelectionGroup) -> AVMediaSelectionOption?](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1388232-associatedmediaselectionoption)

|  | Declaration |
| --- | --- |
| From | ``` func associatedMediaSelectionOptionInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup!) -> AVMediaSelectionOption! ``` |
| To | ``` func associatedMediaSelectionOptionInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption? ``` |

Modified [AVMediaSelectionOption.availableMetadataFormats](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1389504-availablemetadataformats)

|  | Declaration |
| --- | --- |
| From | ``` var availableMetadataFormats: [AnyObject]! { get } ``` |
| To | ``` var availableMetadataFormats: [String] { get } ``` |

Modified [AVMediaSelectionOption.commonMetadata](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1387859-commonmetadata)

|  | Declaration |
| --- | --- |
| From | ``` var commonMetadata: [AnyObject]! { get } ``` |
| To | ``` var commonMetadata: [AVMetadataItem] { get } ``` |

Modified [AVMediaSelectionOption.displayName](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1388485-displayname)

|  | Declaration |
| --- | --- |
| From | ``` var displayName: String! { get } ``` |
| To | ``` var displayName: String { get } ``` |

Modified [AVMediaSelectionOption.displayNameWithLocale(_: NSLocale) -> String](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1388021-displayname)

|  | Declaration |
| --- | --- |
| From | ``` func displayNameWithLocale(_ locale: NSLocale!) -> String! ``` |
| To | ``` func displayNameWithLocale(_ locale: NSLocale) -> String ``` |

Modified [AVMediaSelectionOption.extendedLanguageTag](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1387619-extendedlanguagetag)

|  | Declaration |
| --- | --- |
| From | ``` var extendedLanguageTag: String! { get } ``` |
| To | ``` var extendedLanguageTag: String? { get } ``` |

Modified [AVMediaSelectionOption.hasMediaCharacteristic(_: String) -> Bool](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1388531-hasmediacharacteristic)

|  | Declaration |
| --- | --- |
| From | ``` func hasMediaCharacteristic(_ mediaCharacteristic: String!) -> Bool ``` |
| To | ``` func hasMediaCharacteristic(_ mediaCharacteristic: String) -> Bool ``` |

Modified [AVMediaSelectionOption.locale](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1388436-locale)

|  | Declaration |
| --- | --- |
| From | ``` var locale: NSLocale! { get } ``` |
| To | ``` var locale: NSLocale? { get } ``` |

Modified [AVMediaSelectionOption.mediaSubTypes](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1385587-mediasubtypes)

|  | Declaration |
| --- | --- |
| From | ``` var mediaSubTypes: [AnyObject]! { get } ``` |
| To | ``` var mediaSubTypes: [NSNumber] { get } ``` |

Modified [AVMediaSelectionOption.mediaType](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1386322-mediatype)

|  | Declaration |
| --- | --- |
| From | ``` var mediaType: String! { get } ``` |
| To | ``` var mediaType: String { get } ``` |

Modified [AVMediaSelectionOption.metadataForFormat(_: String) -> [AVMetadataItem]](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1386666-metadataforformat)

|  | Declaration |
| --- | --- |
| From | ``` func metadataForFormat(_ format: String!) -> [AnyObject]! ``` |
| To | ``` func metadataForFormat(_ format: String) -> [AVMetadataItem] ``` |

Modified [AVMediaSelectionOption.propertyList() -> AnyObject](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1386310-propertylist)

|  | Declaration |
| --- | --- |
| From | ``` func propertyList() -> AnyObject! ``` |
| To | ``` func propertyList() -> AnyObject ``` |

Modified [AVMetadataItem](https://developer.apple.com/documentation/avfoundation/avmetadataitem)

|  | Declaration |
| --- | --- |
| From | ``` class AVMetadataItem : NSObject, AVAsynchronousKeyValueLoading, NSCopying, NSMutableCopying {     var identifier: String! { get }     var extendedLanguageTag: String! { get }     @NSCopying var locale: NSLocale! { get }     var time: CMTime { get }     var duration: CMTime { get }     var dataType: String! { get }     @NSCopying var value: protocol<NSCopying, NSObjectProtocol>! { get }     var extraAttributes: [NSObject : AnyObject]! { get } } extension AVMetadataItem {     var stringValue: String! { get }     var numberValue: NSNumber! { get }     var dateValue: NSDate! { get }     var dataValue: NSData! { get } } extension AVMetadataItem {     func statusOfValueForKey(_ key: String!, error outError: NSErrorPointer) -> AVKeyValueStatus     func loadValuesAsynchronouslyForKeys(_ keys: [AnyObject]!, completionHandler handler: (() -> Void)!) } extension AVMetadataItem {     class func metadataItemsFromArray(_ metadataItems: [AnyObject]!, filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [AnyObject]!) -> [AnyObject]!     class func metadataItemsFromArray(_ metadataItems: [AnyObject]!, filteredByIdentifier identifier: String!) -> [AnyObject]!     class func metadataItemsFromArray(_ metadataItems: [AnyObject]!, filteredByMetadataItemFilter metadataItemFilter: AVMetadataItemFilter!) -> [AnyObject]! } extension AVMetadataItem {     class func identifierForKey(_ key: AnyObject!, keySpace keySpace: String!) -> String!     class func keySpaceForIdentifier(_ identifier: String!) -> String!     class func keyForIdentifier(_ identifier: String!) -> AnyObject!     @NSCopying var key: protocol<NSCopying, NSObjectProtocol>! { get }     var commonKey: String! { get }     var keySpace: String! { get } } extension AVMetadataItem {     class func metadataItemsFromArray(_ metadataItems: [AnyObject]!, withLocale locale: NSLocale!) -> [AnyObject]!     class func metadataItemsFromArray(_ metadataItems: [AnyObject]!, withKey key: AnyObject!, keySpace keySpace: String!) -> [AnyObject]! } ``` |
| To | ``` class AVMetadataItem : NSObject, AVAsynchronousKeyValueLoading, NSCopying, NSMutableCopying {     var identifier: String? { get }     var extendedLanguageTag: String? { get }     @NSCopying var locale: NSLocale? { get }     var time: CMTime { get }     var duration: CMTime { get }     var dataType: String? { get }     @NSCopying var value: protocol<NSCopying, NSObjectProtocol>? { get }     var extraAttributes: [String : AnyObject]? { get } } extension AVMetadataItem {     @NSCopying var startDate: NSDate? { get } } extension AVMetadataItem {     var stringValue: String? { get }     var numberValue: NSNumber? { get }     var dateValue: NSDate? { get }     var dataValue: NSData? { get } } extension AVMetadataItem {     func statusOfValueForKey(_ key: String, error outError: NSErrorPointer) -> AVKeyValueStatus     func loadValuesAsynchronouslyForKeys(_ keys: [String], completionHandler handler: (() -> Void)?) } extension AVMetadataItem {     class func metadataItemsFromArray(_ metadataItems: [AVMetadataItem], filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [String]) -> [AVMetadataItem]     class func metadataItemsFromArray(_ metadataItems: [AVMetadataItem], filteredByIdentifier identifier: String) -> [AVMetadataItem]     class func metadataItemsFromArray(_ metadataItems: [AVMetadataItem], filteredByMetadataItemFilter metadataItemFilter: AVMetadataItemFilter) -> [AVMetadataItem] } extension AVMetadataItem {     class func identifierForKey(_ key: AnyObject, keySpace keySpace: String) -> String?     class func keySpaceForIdentifier(_ identifier: String) -> String?     class func keyForIdentifier(_ identifier: String) -> AnyObject?     @NSCopying var key: protocol<NSCopying, NSObjectProtocol>? { get }     var commonKey: String? { get }     var keySpace: String? { get } } extension AVMetadataItem {      init(propertiesOfMetadataItem metadataItem: AVMetadataItem, valueLoadingHandler handler: (AVMetadataItemValueRequest) -> Void)     class func metadataItemWithPropertiesOfMetadataItem(_ metadataItem: AVMetadataItem, valueLoadingHandler handler: (AVMetadataItemValueRequest) -> Void) -> AVMetadataItem } extension AVMetadataItem {     class func metadataItemsFromArray(_ metadataItems: [AVMetadataItem], withLocale locale: NSLocale) -> [AVMetadataItem]     class func metadataItemsFromArray(_ metadataItems: [AVMetadataItem], withKey key: AnyObject?, keySpace keySpace: String?) -> [AVMetadataItem] } ``` |

Modified [AVMetadataItem.commonKey](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1389864-commonkey)

|  | Declaration |
| --- | --- |
| From | ``` var commonKey: String! { get } ``` |
| To | ``` var commonKey: String? { get } ``` |

Modified [AVMetadataItem.dataType](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1386856-datatype)

|  | Declaration |
| --- | --- |
| From | ``` var dataType: String! { get } ``` |
| To | ``` var dataType: String? { get } ``` |

Modified [AVMetadataItem.dataValue](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387641-datavalue)

|  | Declaration |
| --- | --- |
| From | ``` var dataValue: NSData! { get } ``` |
| To | ``` var dataValue: NSData? { get } ``` |

Modified [AVMetadataItem.dateValue](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1385563-datevalue)

|  | Declaration |
| --- | --- |
| From | ``` var dateValue: NSDate! { get } ``` |
| To | ``` var dateValue: NSDate? { get } ``` |

Modified [AVMetadataItem.extendedLanguageTag](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387068-extendedlanguagetag)

|  | Declaration |
| --- | --- |
| From | ``` var extendedLanguageTag: String! { get } ``` |
| To | ``` var extendedLanguageTag: String? { get } ``` |

Modified [AVMetadataItem.extraAttributes](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1389570-extraattributes)

|  | Declaration |
| --- | --- |
| From | ``` var extraAttributes: [NSObject : AnyObject]! { get } ``` |
| To | ``` var extraAttributes: [String : AnyObject]? { get } ``` |

Modified [AVMetadataItem.identifier](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1386968-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! { get } ``` |
| To | ``` var identifier: String? { get } ``` |

Modified [AVMetadataItem.identifierForKey(_: AnyObject, keySpace: String) -> String? [class]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387869-identifier)

|  | Declaration |
| --- | --- |
| From | ``` class func identifierForKey(_ key: AnyObject!, keySpace keySpace: String!) -> String! ``` |
| To | ``` class func identifierForKey(_ key: AnyObject, keySpace keySpace: String) -> String? ``` |

Modified [AVMetadataItem.key](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387843-key)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var key: protocol<NSCopying, NSObjectProtocol>! { get } ``` |
| To | ``` @NSCopying var key: protocol<NSCopying, NSObjectProtocol>? { get } ``` |

Modified [AVMetadataItem.keyForIdentifier(_: String) -> AnyObject? [class]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1385613-keyforidentifier)

|  | Declaration |
| --- | --- |
| From | ``` class func keyForIdentifier(_ identifier: String!) -> AnyObject! ``` |
| To | ``` class func keyForIdentifier(_ identifier: String) -> AnyObject? ``` |

Modified [AVMetadataItem.keySpace](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1385757-keyspace)

|  | Declaration |
| --- | --- |
| From | ``` var keySpace: String! { get } ``` |
| To | ``` var keySpace: String? { get } ``` |

Modified [AVMetadataItem.keySpaceForIdentifier(_: String) -> String? [class]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1390663-keyspaceforidentifier)

|  | Declaration |
| --- | --- |
| From | ``` class func keySpaceForIdentifier(_ identifier: String!) -> String! ``` |
| To | ``` class func keySpaceForIdentifier(_ identifier: String) -> String? ``` |

Modified [AVMetadataItem.loadValuesAsynchronouslyForKeys(_: [String], completionHandler: (() -> Void)?)](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387102-loadvaluesasynchronouslyforkeys)

|  | Declaration |
| --- | --- |
| From | ``` func loadValuesAsynchronouslyForKeys(_ keys: [AnyObject]!, completionHandler handler: (() -> Void)!) ``` |
| To | ``` func loadValuesAsynchronouslyForKeys(_ keys: [String], completionHandler handler: (() -> Void)?) ``` |

Modified [AVMetadataItem.locale](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387114-locale)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var locale: NSLocale! { get } ``` |
| To | ``` @NSCopying var locale: NSLocale? { get } ``` |

Modified [AVMetadataItem.metadataItemsFromArray(_: [AVMetadataItem], filteredAndSortedAccordingToPreferredLanguages: [String]) -> [AVMetadataItem] [class]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387901-metadataitemsfromarray)

|  | Declaration |
| --- | --- |
| From | ``` class func metadataItemsFromArray(_ metadataItems: [AnyObject]!, filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [AnyObject]!) -> [AnyObject]! ``` |
| To | ``` class func metadataItemsFromArray(_ metadataItems: [AVMetadataItem], filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [String]) -> [AVMetadataItem] ``` |

Modified [AVMetadataItem.metadataItemsFromArray(_: [AVMetadataItem], filteredByIdentifier: String) -> [AVMetadataItem] [class]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1385843-metadataitems)

|  | Declaration |
| --- | --- |
| From | ``` class func metadataItemsFromArray(_ metadataItems: [AnyObject]!, filteredByIdentifier identifier: String!) -> [AnyObject]! ``` |
| To | ``` class func metadataItemsFromArray(_ metadataItems: [AVMetadataItem], filteredByIdentifier identifier: String) -> [AVMetadataItem] ``` |

Modified [AVMetadataItem.metadataItemsFromArray(_: [AVMetadataItem], filteredByMetadataItemFilter: AVMetadataItemFilter) -> [AVMetadataItem] [class]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1390238-metadataitems)

|  | Declaration |
| --- | --- |
| From | ``` class func metadataItemsFromArray(_ metadataItems: [AnyObject]!, filteredByMetadataItemFilter metadataItemFilter: AVMetadataItemFilter!) -> [AnyObject]! ``` |
| To | ``` class func metadataItemsFromArray(_ metadataItems: [AVMetadataItem], filteredByMetadataItemFilter metadataItemFilter: AVMetadataItemFilter) -> [AVMetadataItem] ``` |

Modified [AVMetadataItem.metadataItemsFromArray(_: [AVMetadataItem], withKey: AnyObject?, keySpace: String?) -> [AVMetadataItem] [class]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1386083-metadataitems)

|  | Declaration |
| --- | --- |
| From | ``` class func metadataItemsFromArray(_ metadataItems: [AnyObject]!, withKey key: AnyObject!, keySpace keySpace: String!) -> [AnyObject]! ``` |
| To | ``` class func metadataItemsFromArray(_ metadataItems: [AVMetadataItem], withKey key: AnyObject?, keySpace keySpace: String?) -> [AVMetadataItem] ``` |

Modified [AVMetadataItem.metadataItemsFromArray(_: [AVMetadataItem], withLocale: NSLocale) -> [AVMetadataItem] [class]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1389374-metadataitemsfromarray)

|  | Declaration |
| --- | --- |
| From | ``` class func metadataItemsFromArray(_ metadataItems: [AnyObject]!, withLocale locale: NSLocale!) -> [AnyObject]! ``` |
| To | ``` class func metadataItemsFromArray(_ metadataItems: [AVMetadataItem], withLocale locale: NSLocale) -> [AVMetadataItem] ``` |

Modified [AVMetadataItem.numberValue](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1390681-numbervalue)

|  | Declaration |
| --- | --- |
| From | ``` var numberValue: NSNumber! { get } ``` |
| To | ``` var numberValue: NSNumber? { get } ``` |

Modified [AVMetadataItem.statusOfValueForKey(_: String, error: NSErrorPointer) -> AVKeyValueStatus](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1388523-statusofvalueforkey)

|  | Declaration |
| --- | --- |
| From | ``` func statusOfValueForKey(_ key: String!, error outError: NSErrorPointer) -> AVKeyValueStatus ``` |
| To | ``` func statusOfValueForKey(_ key: String, error outError: NSErrorPointer) -> AVKeyValueStatus ``` |

Modified [AVMetadataItem.stringValue](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1390846-stringvalue)

|  | Declaration |
| --- | --- |
| From | ``` var stringValue: String! { get } ``` |
| To | ``` var stringValue: String? { get } ``` |

Modified [AVMetadataItem.value](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1390537-value)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var value: protocol<NSCopying, NSObjectProtocol>! { get } ``` |
| To | ``` @NSCopying var value: protocol<NSCopying, NSObjectProtocol>? { get } ``` |

Modified [AVMetadataItemFilter](https://developer.apple.com/documentation/avfoundation/avmetadataitemfilter)

|  | Declaration |
| --- | --- |
| From | ``` class AVMetadataItemFilter : NSObject {     class func metadataItemFilterForSharing() -> AVMetadataItemFilter! } ``` |
| To | ``` class AVMetadataItemFilter : NSObject {     class func metadataItemFilterForSharing() -> AVMetadataItemFilter } ``` |

Modified [AVMetadataItemFilter.metadataItemFilterForSharing() -> AVMetadataItemFilter [class]](https://developer.apple.com/documentation/avfoundation/avmetadataitemfilter/1387905-forsharing)

|  | Declaration |
| --- | --- |
| From | ``` class func metadataItemFilterForSharing() -> AVMetadataItemFilter! ``` |
| To | ``` class func metadataItemFilterForSharing() -> AVMetadataItemFilter ``` |

Modified [AVMIDIPlayer](https://developer.apple.com/documentation/avfoundation/avmidiplayer)

|  | Declaration |
| --- | --- |
| From | ``` class AVMIDIPlayer : NSObject {     init!(contentsOfURL inURL: NSURL!, soundBankURL bankURL: NSURL!, error outError: NSErrorPointer)     init!(data data: NSData!, soundBankURL bankURL: NSURL!, error outError: NSErrorPointer)     func prepareToPlay()     func play(_ completionHandler: AVMIDIPlayerCompletionHandler!)     func stop()     var duration: NSTimeInterval { get }     var playing: Bool { get }     var rate: Float     var currentPosition: NSTimeInterval } ``` |
| To | ``` class AVMIDIPlayer : NSObject {     init(contentsOfURL inURL: NSURL, soundBankURL bankURL: NSURL?) throws     init(data data: NSData, soundBankURL bankURL: NSURL?) throws     func prepareToPlay()     func play(_ completionHandler: AVMIDIPlayerCompletionHandler?)     func stop()     var duration: NSTimeInterval { get }     var playing: Bool { get }     var rate: Float     var currentPosition: NSTimeInterval } ``` |

Modified [AVMIDIPlayer.init(contentsOfURL: NSURL, soundBankURL: NSURL?) throws](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1390856-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(contentsOfURL inURL: NSURL!, soundBankURL bankURL: NSURL!, error outError: NSErrorPointer) ``` |
| To | ``` init(contentsOfURL inURL: NSURL, soundBankURL bankURL: NSURL?) throws ``` |

Modified [AVMIDIPlayer.init(data: NSData, soundBankURL: NSURL?) throws](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1389225-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(data data: NSData!, soundBankURL bankURL: NSURL!, error outError: NSErrorPointer) ``` |
| To | ``` init(data data: NSData, soundBankURL bankURL: NSURL?) throws ``` |

Modified [AVMIDIPlayer.play(_: AVMIDIPlayerCompletionHandler?)](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1388390-play)

|  | Declaration |
| --- | --- |
| From | ``` func play(_ completionHandler: AVMIDIPlayerCompletionHandler!) ``` |
| To | ``` func play(_ completionHandler: AVMIDIPlayerCompletionHandler?) ``` |

Modified [AVMutableAudioMix](https://developer.apple.com/documentation/avfoundation/avmutableaudiomix)

|  | Declaration |
| --- | --- |
| From | ``` class AVMutableAudioMix : AVAudioMix {     init!() -> AVMutableAudioMix     class func audioMix() -> AVMutableAudioMix!     var inputParameters: [AnyObject]! } ``` |
| To | ``` class AVMutableAudioMix : AVAudioMix {     convenience init()     class func audioMix() -> Self     var inputParameters: [AVAudioMixInputParameters] } ``` |

Modified [AVMutableAudioMix.inputParameters](https://developer.apple.com/documentation/avfoundation/avmutableaudiomix/1388159-inputparameters)

|  | Declaration |
| --- | --- |
| From | ``` var inputParameters: [AnyObject]! ``` |
| To | ``` var inputParameters: [AVAudioMixInputParameters] ``` |

Modified [AVMutableAudioMixInputParameters](https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters)

|  | Declaration |
| --- | --- |
| From | ``` class AVMutableAudioMixInputParameters : AVAudioMixInputParameters {     init!(track track: AVAssetTrack!) -> AVMutableAudioMixInputParameters     class func audioMixInputParametersWithTrack(_ track: AVAssetTrack!) -> AVMutableAudioMixInputParameters!     init!() -> AVMutableAudioMixInputParameters     class func audioMixInputParameters() -> AVMutableAudioMixInputParameters!     var trackID: CMPersistentTrackID     var audioTimePitchAlgorithm: String!     var audioTapProcessor: MTAudioProcessingTap!     func setVolumeRampFromStartVolume(_ startVolume: Float, toEndVolume endVolume: Float, timeRange timeRange: CMTimeRange)     func setVolume(_ volume: Float, atTime time: CMTime) } ``` |
| To | ``` class AVMutableAudioMixInputParameters : AVAudioMixInputParameters {     convenience init(track track: AVAssetTrack?)     class func audioMixInputParametersWithTrack(_ track: AVAssetTrack?) -> Self     convenience init()     class func audioMixInputParameters() -> Self     var trackID: CMPersistentTrackID     var audioTimePitchAlgorithm: String?     var audioTapProcessor: MTAudioProcessingTap?     func setVolumeRampFromStartVolume(_ startVolume: Float, toEndVolume endVolume: Float, timeRange timeRange: CMTimeRange)     func setVolume(_ volume: Float, atTime time: CMTime) } ``` |

Modified [AVMutableAudioMixInputParameters.audioTapProcessor](https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/1389296-audiotapprocessor)

|  | Declaration |
| --- | --- |
| From | ``` var audioTapProcessor: MTAudioProcessingTap! ``` |
| To | ``` var audioTapProcessor: MTAudioProcessingTap? ``` |

Modified [AVMutableAudioMixInputParameters.audioTimePitchAlgorithm](https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/1388300-audiotimepitchalgorithm)

|  | Declaration |
| --- | --- |
| From | ``` var audioTimePitchAlgorithm: String! ``` |
| To | ``` var audioTimePitchAlgorithm: String? ``` |

Modified [AVMutableAudioMixInputParameters.init(track: AVAssetTrack?)](https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/1386858-audiomixinputparameterswithtrack)

|  | Declaration |
| --- | --- |
| From | ``` init!(track track: AVAssetTrack!) -> AVMutableAudioMixInputParameters ``` |
| To | ``` convenience init(track track: AVAssetTrack?) ``` |

Modified [AVMutableComposition](https://developer.apple.com/documentation/avfoundation/avmutablecomposition)

|  | Declaration |
| --- | --- |
| From | ``` class AVMutableComposition : AVComposition {     var tracks: [AnyObject]! { get }     var naturalSize: CGSize     init!() -> AVMutableComposition     class func composition() -> AVMutableComposition! } extension AVMutableComposition {     func insertTimeRange(_ timeRange: CMTimeRange, ofAsset asset: AVAsset!, atTime startTime: CMTime, error outError: NSErrorPointer) -> Bool     func insertEmptyTimeRange(_ timeRange: CMTimeRange)     func removeTimeRange(_ timeRange: CMTimeRange)     func scaleTimeRange(_ timeRange: CMTimeRange, toDuration duration: CMTime) } extension AVMutableComposition {     func addMutableTrackWithMediaType(_ mediaType: String!, preferredTrackID preferredTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack!     func removeTrack(_ track: AVCompositionTrack!)     func mutableTrackCompatibleWithTrack(_ track: AVAssetTrack!) -> AVMutableCompositionTrack! } ``` |
| To | ``` class AVMutableComposition : AVComposition {     var tracks: [AVMutableCompositionTrack] { get }     var naturalSize: CGSize     convenience init()     class func composition() -> Self     convenience init(URLAssetInitializationOptions URLAssetInitializationOptions: [String : AnyObject]?)     class func compositionWithURLAssetInitializationOptions(_ URLAssetInitializationOptions: [String : AnyObject]?) -> Self } extension AVMutableComposition {     func insertTimeRange(_ timeRange: CMTimeRange, ofAsset asset: AVAsset, atTime startTime: CMTime) throws     func insertEmptyTimeRange(_ timeRange: CMTimeRange)     func removeTimeRange(_ timeRange: CMTimeRange)     func scaleTimeRange(_ timeRange: CMTimeRange, toDuration duration: CMTime) } extension AVMutableComposition {     func addMutableTrackWithMediaType(_ mediaType: String, preferredTrackID preferredTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack     func removeTrack(_ track: AVCompositionTrack)     func mutableTrackCompatibleWithTrack(_ track: AVAssetTrack) -> AVMutableCompositionTrack? } extension AVMutableComposition {     func trackWithTrackID(_ trackID: CMPersistentTrackID) -> AVMutableCompositionTrack?     func tracksWithMediaType(_ mediaType: String) -> [AVMutableCompositionTrack]     func tracksWithMediaCharacteristic(_ mediaCharacteristic: String) -> [AVMutableCompositionTrack] } ``` |

Modified [AVMutableComposition.addMutableTrackWithMediaType(_: String, preferredTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1387601-addmutabletrack)

|  | Declaration |
| --- | --- |
| From | ``` func addMutableTrackWithMediaType(_ mediaType: String!, preferredTrackID preferredTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack! ``` |
| To | ``` func addMutableTrackWithMediaType(_ mediaType: String, preferredTrackID preferredTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack ``` |

Modified [AVMutableComposition.insertTimeRange(_: CMTimeRange, ofAsset: AVAsset, atTime: CMTime) throws](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1385943-inserttimerange)

|  | Declaration |
| --- | --- |
| From | ``` func insertTimeRange(_ timeRange: CMTimeRange, ofAsset asset: AVAsset!, atTime startTime: CMTime, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func insertTimeRange(_ timeRange: CMTimeRange, ofAsset asset: AVAsset, atTime startTime: CMTime) throws ``` |

Modified [AVMutableComposition.mutableTrackCompatibleWithTrack(_: AVAssetTrack) -> AVMutableCompositionTrack?](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1386662-mutabletrack)

|  | Declaration |
| --- | --- |
| From | ``` func mutableTrackCompatibleWithTrack(_ track: AVAssetTrack!) -> AVMutableCompositionTrack! ``` |
| To | ``` func mutableTrackCompatibleWithTrack(_ track: AVAssetTrack) -> AVMutableCompositionTrack? ``` |

Modified [AVMutableComposition.removeTrack(_: AVCompositionTrack)](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1386818-removetrack)

|  | Declaration |
| --- | --- |
| From | ``` func removeTrack(_ track: AVCompositionTrack!) ``` |
| To | ``` func removeTrack(_ track: AVCompositionTrack) ``` |

Modified [AVMutableComposition.tracks](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1389937-tracks)

|  | Declaration |
| --- | --- |
| From | ``` var tracks: [AnyObject]! { get } ``` |
| To | ``` var tracks: [AVMutableCompositionTrack] { get } ``` |

Modified [AVMutableCompositionTrack](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack)

|  | Declaration |
| --- | --- |
| From | ``` class AVMutableCompositionTrack : AVCompositionTrack {     var naturalTimeScale: CMTimeScale     var languageCode: String!     var extendedLanguageTag: String!     var preferredTransform: CGAffineTransform     var preferredVolume: Float     var segments: [AnyObject]!     func insertTimeRange(_ timeRange: CMTimeRange, ofTrack track: AVAssetTrack!, atTime startTime: CMTime, error error: NSErrorPointer) -> Bool     func insertTimeRanges(_ timeRanges: [AnyObject]!, ofTracks tracks: [AnyObject]!, atTime startTime: CMTime, error error: NSErrorPointer) -> Bool     func insertEmptyTimeRange(_ timeRange: CMTimeRange)     func removeTimeRange(_ timeRange: CMTimeRange)     func scaleTimeRange(_ timeRange: CMTimeRange, toDuration duration: CMTime)     func validateTrackSegments(_ trackSegments: [AnyObject]!, error error: NSErrorPointer) -> Bool } ``` |
| To | ``` class AVMutableCompositionTrack : AVCompositionTrack {     var naturalTimeScale: CMTimeScale     var languageCode: String?     var extendedLanguageTag: String?     var preferredTransform: CGAffineTransform     var preferredVolume: Float     var segments: [AVCompositionTrackSegment]!     func insertTimeRange(_ timeRange: CMTimeRange, ofTrack track: AVAssetTrack, atTime startTime: CMTime) throws     func insertTimeRanges(_ timeRanges: [NSValue], ofTracks tracks: [AVAssetTrack], atTime startTime: CMTime) throws     func insertEmptyTimeRange(_ timeRange: CMTimeRange)     func removeTimeRange(_ timeRange: CMTimeRange)     func scaleTimeRange(_ timeRange: CMTimeRange, toDuration duration: CMTime)     func validateTrackSegments(_ trackSegments: [AVCompositionTrackSegment]) throws } ``` |

Modified [AVMutableCompositionTrack.extendedLanguageTag](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/1388866-extendedlanguagetag)

|  | Declaration |
| --- | --- |
| From | ``` var extendedLanguageTag: String! ``` |
| To | ``` var extendedLanguageTag: String? ``` |

Modified [AVMutableCompositionTrack.insertTimeRange(_: CMTimeRange, ofTrack: AVAssetTrack, atTime: CMTime) throws](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/1390691-inserttimerange)

|  | Declaration |
| --- | --- |
| From | ``` func insertTimeRange(_ timeRange: CMTimeRange, ofTrack track: AVAssetTrack!, atTime startTime: CMTime, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func insertTimeRange(_ timeRange: CMTimeRange, ofTrack track: AVAssetTrack, atTime startTime: CMTime) throws ``` |

Modified [AVMutableCompositionTrack.insertTimeRanges(_: [NSValue], ofTracks: [AVAssetTrack], atTime: CMTime) throws](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/1388629-inserttimeranges)

|  | Declaration |
| --- | --- |
| From | ``` func insertTimeRanges(_ timeRanges: [AnyObject]!, ofTracks tracks: [AnyObject]!, atTime startTime: CMTime, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func insertTimeRanges(_ timeRanges: [NSValue], ofTracks tracks: [AVAssetTrack], atTime startTime: CMTime) throws ``` |

Modified [AVMutableCompositionTrack.languageCode](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/1387192-languagecode)

|  | Declaration |
| --- | --- |
| From | ``` var languageCode: String! ``` |
| To | ``` var languageCode: String? ``` |

Modified [AVMutableCompositionTrack.segments](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/1390321-segments)

|  | Declaration |
| --- | --- |
| From | ``` var segments: [AnyObject]! ``` |
| To | ``` var segments: [AVCompositionTrackSegment]! ``` |

Modified [AVMutableCompositionTrack.validateTrackSegments(_: [AVCompositionTrackSegment]) throws](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/1388746-validatesegments)

|  | Declaration |
| --- | --- |
| From | ``` func validateTrackSegments(_ trackSegments: [AnyObject]!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func validateTrackSegments(_ trackSegments: [AVCompositionTrackSegment]) throws ``` |

Modified [AVMutableMetadataItem](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem)

|  | Declaration |
| --- | --- |
| From | ``` class AVMutableMetadataItem : AVMetadataItem {     var identifier: String!     var extendedLanguageTag: String!     @NSCopying var locale: NSLocale!     var time: CMTime     var duration: CMTime     var dataType: String!     @NSCopying var value: protocol<NSCopying, NSObjectProtocol>!     var extraAttributes: [NSObject : AnyObject]!     init!() -> AVMutableMetadataItem     class func metadataItem() -> AVMutableMetadataItem! } extension AVMutableMetadataItem {     var keySpace: String!     @NSCopying var key: protocol<NSCopying, NSObjectProtocol>! } ``` |
| To | ``` class AVMutableMetadataItem : AVMetadataItem {     var identifier: String?     var extendedLanguageTag: String?     @NSCopying var locale: NSLocale?     var time: CMTime     var duration: CMTime     var dataType: String?     @NSCopying var value: protocol<NSCopying, NSObjectProtocol>?     var extraAttributes: [String : AnyObject]?      init()     class func metadataItem() -> AVMutableMetadataItem } extension AVMutableMetadataItem {     @NSCopying var startDate: NSDate? } extension AVMutableMetadataItem {     var keySpace: String?     @NSCopying var key: protocol<NSCopying, NSObjectProtocol>? } ``` |

Modified [AVMutableMetadataItem.dataType](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1389471-datatype)

|  | Declaration |
| --- | --- |
| From | ``` var dataType: String! ``` |
| To | ``` var dataType: String? ``` |

Modified [AVMutableMetadataItem.extendedLanguageTag](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1386664-extendedlanguagetag)

|  | Declaration |
| --- | --- |
| From | ``` var extendedLanguageTag: String! ``` |
| To | ``` var extendedLanguageTag: String? ``` |

Modified [AVMutableMetadataItem.extraAttributes](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1390397-extraattributes)

|  | Declaration |
| --- | --- |
| From | ``` var extraAttributes: [NSObject : AnyObject]! ``` |
| To | ``` var extraAttributes: [String : AnyObject]? ``` |

Modified [AVMutableMetadataItem.identifier](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1386688-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! ``` |
| To | ``` var identifier: String? ``` |

Modified [AVMutableMetadataItem.key](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1386776-key)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var key: protocol<NSCopying, NSObjectProtocol>! ``` |
| To | ``` @NSCopying var key: protocol<NSCopying, NSObjectProtocol>? ``` |

Modified [AVMutableMetadataItem.keySpace](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1385655-keyspace)

|  | Declaration |
| --- | --- |
| From | ``` var keySpace: String! ``` |
| To | ``` var keySpace: String? ``` |

Modified [AVMutableMetadataItem.locale](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1389292-locale)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var locale: NSLocale! ``` |
| To | ``` @NSCopying var locale: NSLocale? ``` |

Modified [AVMutableMetadataItem.value](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1388296-value)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var value: protocol<NSCopying, NSObjectProtocol>! ``` |
| To | ``` @NSCopying var value: protocol<NSCopying, NSObjectProtocol>? ``` |

Modified [AVMutableTimedMetadataGroup](https://developer.apple.com/documentation/avfoundation/avmutabletimedmetadatagroup)

|  | Declaration |
| --- | --- |
| From | ``` class AVMutableTimedMetadataGroup : AVTimedMetadataGroup {     var timeRange: CMTimeRange     var items: [AnyObject]! } ``` |
| To | ``` class AVMutableTimedMetadataGroup : AVTimedMetadataGroup {     var timeRange: CMTimeRange     var items: [AVMetadataItem] } ``` |

Modified [AVMutableTimedMetadataGroup.items](https://developer.apple.com/documentation/avfoundation/avmutabletimedmetadatagroup/1386481-items)

|  | Declaration |
| --- | --- |
| From | ``` var items: [AnyObject]! ``` |
| To | ``` var items: [AVMetadataItem] ``` |

Modified [AVMutableVideoComposition](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition)

|  | Declaration |
| --- | --- |
| From | ``` class AVMutableVideoComposition : AVVideoComposition {     init!() -> AVMutableVideoComposition     class func videoComposition() -> AVMutableVideoComposition!     init!(propertiesOfAsset asset: AVAsset!) -> AVMutableVideoComposition     class func videoCompositionWithPropertiesOfAsset(_ asset: AVAsset!) -> AVMutableVideoComposition!     var customVideoCompositorClass: AnyObject.Type!     var frameDuration: CMTime     var renderSize: CGSize     var renderScale: Float     var instructions: [AnyObject]!     var animationTool: AVVideoCompositionCoreAnimationTool! } ``` |
| To | ``` class AVMutableVideoComposition : AVVideoComposition {      init()     class func videoComposition() -> AVMutableVideoComposition      init(propertiesOfAsset asset: AVAsset)     class func videoCompositionWithPropertiesOfAsset(_ asset: AVAsset) -> AVMutableVideoComposition     var customVideoCompositorClass: AnyObject.Type?     var frameDuration: CMTime     var renderSize: CGSize     var renderScale: Float     var instructions: [AVVideoCompositionInstructionProtocol]     var animationTool: AVVideoCompositionCoreAnimationTool? } extension AVMutableVideoComposition {      init(asset asset: AVAsset, applyingCIFiltersWithHandler applier: (AVAsynchronousCIImageFilteringRequest) -> Void)     class func videoCompositionWithAsset(_ asset: AVAsset, applyingCIFiltersWithHandler applier: (AVAsynchronousCIImageFilteringRequest) -> Void) -> AVMutableVideoComposition } ``` |

Modified [AVMutableVideoComposition.animationTool](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1390395-animationtool)

|  | Declaration |
| --- | --- |
| From | ``` var animationTool: AVVideoCompositionCoreAnimationTool! ``` |
| To | ``` var animationTool: AVVideoCompositionCoreAnimationTool? ``` |

Modified [AVMutableVideoComposition.customVideoCompositorClass](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1390649-customvideocompositorclass)

|  | Declaration |
| --- | --- |
| From | ``` var customVideoCompositorClass: AnyObject.Type! ``` |
| To | ``` var customVideoCompositorClass: AnyObject.Type? ``` |

Modified [AVMutableVideoComposition.init(propertiesOfAsset: AVAsset)](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1388430-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(propertiesOfAsset asset: AVAsset!) -> AVMutableVideoComposition ``` |
| To | ``` init(propertiesOfAsset asset: AVAsset) ``` |

Modified [AVMutableVideoComposition.instructions](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1385815-instructions)

|  | Declaration |
| --- | --- |
| From | ``` var instructions: [AnyObject]! ``` |
| To | ``` var instructions: [AVVideoCompositionInstructionProtocol] ``` |

Modified [AVMutableVideoCompositionInstruction](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositioninstruction)

|  | Declaration |
| --- | --- |
| From | ``` class AVMutableVideoCompositionInstruction : AVVideoCompositionInstruction {     init!() -> AVMutableVideoCompositionInstruction     class func videoCompositionInstruction() -> AVMutableVideoCompositionInstruction!     var timeRange: CMTimeRange     var backgroundColor: CGColor!     var layerInstructions: [AnyObject]!     var enablePostProcessing: Bool } ``` |
| To | ``` class AVMutableVideoCompositionInstruction : AVVideoCompositionInstruction {     convenience init()     class func videoCompositionInstruction() -> Self     var timeRange: CMTimeRange     var backgroundColor: CGColor?     var layerInstructions: [AVVideoCompositionLayerInstruction]     var enablePostProcessing: Bool } ``` |

Modified [AVMutableVideoCompositionInstruction.backgroundColor](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositioninstruction/1390236-backgroundcolor)

|  | Declaration |
| --- | --- |
| From | ``` var backgroundColor: CGColor! ``` |
| To | ``` var backgroundColor: CGColor? ``` |

Modified [AVMutableVideoCompositionInstruction.layerInstructions](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositioninstruction/1388912-layerinstructions)

|  | Declaration |
| --- | --- |
| From | ``` var layerInstructions: [AnyObject]! ``` |
| To | ``` var layerInstructions: [AVVideoCompositionLayerInstruction] ``` |

Modified [AVMutableVideoCompositionLayerInstruction](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction)

|  | Declaration |
| --- | --- |
| From | ``` class AVMutableVideoCompositionLayerInstruction : AVVideoCompositionLayerInstruction {     init!(assetTrack track: AVAssetTrack!) -> AVMutableVideoCompositionLayerInstruction     class func videoCompositionLayerInstructionWithAssetTrack(_ track: AVAssetTrack!) -> AVMutableVideoCompositionLayerInstruction!     init!() -> AVMutableVideoCompositionLayerInstruction     class func videoCompositionLayerInstruction() -> AVMutableVideoCompositionLayerInstruction!     var trackID: CMPersistentTrackID     func setTransformRampFromStartTransform(_ startTransform: CGAffineTransform, toEndTransform endTransform: CGAffineTransform, timeRange timeRange: CMTimeRange)     func setTransform(_ transform: CGAffineTransform, atTime time: CMTime)     func setOpacityRampFromStartOpacity(_ startOpacity: Float, toEndOpacity endOpacity: Float, timeRange timeRange: CMTimeRange)     func setOpacity(_ opacity: Float, atTime time: CMTime)     func setCropRectangleRampFromStartCropRectangle(_ startCropRectangle: CGRect, toEndCropRectangle endCropRectangle: CGRect, timeRange timeRange: CMTimeRange)     func setCropRectangle(_ cropRectangle: CGRect, atTime time: CMTime) } ``` |
| To | ``` class AVMutableVideoCompositionLayerInstruction : AVVideoCompositionLayerInstruction {     convenience init(assetTrack track: AVAssetTrack)     class func videoCompositionLayerInstructionWithAssetTrack(_ track: AVAssetTrack) -> Self     convenience init()     class func videoCompositionLayerInstruction() -> Self     var trackID: CMPersistentTrackID     func setTransformRampFromStartTransform(_ startTransform: CGAffineTransform, toEndTransform endTransform: CGAffineTransform, timeRange timeRange: CMTimeRange)     func setTransform(_ transform: CGAffineTransform, atTime time: CMTime)     func setOpacityRampFromStartOpacity(_ startOpacity: Float, toEndOpacity endOpacity: Float, timeRange timeRange: CMTimeRange)     func setOpacity(_ opacity: Float, atTime time: CMTime)     func setCropRectangleRampFromStartCropRectangle(_ startCropRectangle: CGRect, toEndCropRectangle endCropRectangle: CGRect, timeRange timeRange: CMTimeRange)     func setCropRectangle(_ cropRectangle: CGRect, atTime time: CMTime) } ``` |

Modified [AVMutableVideoCompositionLayerInstruction.init(assetTrack: AVAssetTrack)](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/1389691-videocompositionlayerinstruction)

|  | Declaration |
| --- | --- |
| From | ``` init!(assetTrack track: AVAssetTrack!) -> AVMutableVideoCompositionLayerInstruction ``` |
| To | ``` convenience init(assetTrack track: AVAssetTrack) ``` |

Modified [AVOutputSettingsAssistant](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant)

|  | Declaration |
| --- | --- |
| From | ``` class AVOutputSettingsAssistant : NSObject {     class func availableOutputSettingsPresets() -> [AnyObject]!     convenience init!(preset presetIdentifier: String!)     class func outputSettingsAssistantWithPreset(_ presetIdentifier: String!) -> Self!     var audioSettings: [NSObject : AnyObject]! { get }     var videoSettings: [NSObject : AnyObject]! { get }     var outputFileType: String! { get } } extension AVOutputSettingsAssistant {     var sourceAudioFormat: CMAudioFormatDescription!     var sourceVideoFormat: CMVideoFormatDescription!     var sourceVideoAverageFrameDuration: CMTime     var sourceVideoMinFrameDuration: CMTime } ``` |
| To | ``` class AVOutputSettingsAssistant : NSObject {     init()     class func availableOutputSettingsPresets() -> [String]     convenience init?(preset presetIdentifier: String)     class func outputSettingsAssistantWithPreset(_ presetIdentifier: String) -> Self?     var audioSettings: [String : AnyObject]? { get }     var videoSettings: [String : AnyObject]? { get }     var outputFileType: String { get } } extension AVOutputSettingsAssistant {     var sourceAudioFormat: CMAudioFormatDescription?     var sourceVideoFormat: CMVideoFormatDescription?     var sourceVideoAverageFrameDuration: CMTime     var sourceVideoMinFrameDuration: CMTime } ``` |

Modified [AVOutputSettingsAssistant.audioSettings](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1386233-audiosettings)

|  | Declaration |
| --- | --- |
| From | ``` var audioSettings: [NSObject : AnyObject]! { get } ``` |
| To | ``` var audioSettings: [String : AnyObject]? { get } ``` |

Modified [AVOutputSettingsAssistant.availableOutputSettingsPresets() -> [String] [class]](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1388118-availableoutputsettingspresets)

|  | Declaration |
| --- | --- |
| From | ``` class func availableOutputSettingsPresets() -> [AnyObject]! ``` |
| To | ``` class func availableOutputSettingsPresets() -> [String] ``` |

Modified [AVOutputSettingsAssistant.init(preset: String)](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1387909-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(preset presetIdentifier: String!) ``` |
| To | ``` convenience init?(preset presetIdentifier: String) ``` |

Modified [AVOutputSettingsAssistant.outputFileType](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1390842-outputfiletype)

|  | Declaration |
| --- | --- |
| From | ``` var outputFileType: String! { get } ``` |
| To | ``` var outputFileType: String { get } ``` |

Modified [AVOutputSettingsAssistant.sourceAudioFormat](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1390673-sourceaudioformat)

|  | Declaration |
| --- | --- |
| From | ``` var sourceAudioFormat: CMAudioFormatDescription! ``` |
| To | ``` var sourceAudioFormat: CMAudioFormatDescription? ``` |

Modified [AVOutputSettingsAssistant.sourceVideoFormat](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1387885-sourcevideoformat)

|  | Declaration |
| --- | --- |
| From | ``` var sourceVideoFormat: CMVideoFormatDescription! ``` |
| To | ``` var sourceVideoFormat: CMVideoFormatDescription? ``` |

Modified [AVOutputSettingsAssistant.videoSettings](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1386880-videosettings)

|  | Declaration |
| --- | --- |
| From | ``` var videoSettings: [NSObject : AnyObject]! { get } ``` |
| To | ``` var videoSettings: [String : AnyObject]? { get } ``` |

Modified [AVPlayer](https://developer.apple.com/documentation/avfoundation/avplayer)

|  | Declaration |
| --- | --- |
| From | ``` class AVPlayer : NSObject {     class func playerWithURL(_ URL: NSURL!) -> AnyObject!     class func playerWithPlayerItem(_ item: AVPlayerItem!) -> AnyObject!     init!(URL URL: NSURL!)     init!(playerItem item: AVPlayerItem!)     var status: AVPlayerStatus { get }     var error: NSError! { get } } extension AVPlayer {     var rate: Float     func play()     func pause() } extension AVPlayer {     var currentItem: AVPlayerItem! { get }     func replaceCurrentItemWithPlayerItem(_ item: AVPlayerItem!)     var actionAtItemEnd: AVPlayerActionAtItemEnd } extension AVPlayer {     func currentTime() -> CMTime     func seekToDate(_ date: NSDate!)     func seekToDate(_ date: NSDate!, completionHandler completionHandler: ((Bool) -> Void)!)     func seekToTime(_ time: CMTime)     func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime)     func seekToTime(_ time: CMTime, completionHandler completionHandler: ((Bool) -> Void)!)     func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime, completionHandler completionHandler: ((Bool) -> Void)!) } extension AVPlayer {     func setRate(_ rate: Float, time itemTime: CMTime, atHostTime hostClockTime: CMTime)     func prerollAtRate(_ rate: Float, completionHandler completionHandler: ((Bool) -> Void)!)     func cancelPendingPrerolls()     var masterClock: CMClock! } extension AVPlayer {     func addPeriodicTimeObserverForInterval(_ interval: CMTime, queue queue: dispatch_queue_t!, usingBlock block: ((CMTime) -> Void)!) -> AnyObject!     func addBoundaryTimeObserverForTimes(_ times: [AnyObject]!, queue queue: dispatch_queue_t!, usingBlock block: (() -> Void)!) -> AnyObject!     func removeTimeObserver(_ observer: AnyObject!) } extension AVPlayer {     var volume: Float     var muted: Bool     var closedCaptionDisplayEnabled: Bool } extension AVPlayer {     var appliesMediaSelectionCriteriaAutomatically: Bool     func setMediaSelectionCriteria(_ criteria: AVPlayerMediaSelectionCriteria!, forMediaCharacteristic mediaCharacteristic: String!)     func mediaSelectionCriteriaForMediaCharacteristic(_ mediaCharacteristic: String!) -> AVPlayerMediaSelectionCriteria! } extension AVPlayer {     var audioOutputDeviceUniqueID: String! } extension AVPlayer {     var allowsExternalPlayback: Bool     var externalPlaybackActive: Bool { get }     var usesExternalPlaybackWhileExternalScreenIsActive: Bool     var externalPlaybackVideoGravity: String! } extension AVPlayer {     var allowsAirPlayVideo: Bool     var airPlayVideoActive: Bool { get }     var usesAirPlayVideoWhileAirPlayScreenIsActive: Bool } extension AVPlayer {     var outputObscuredDueToInsufficientExternalProtection: Bool { get } } ``` |
| To | ``` class AVPlayer : NSObject {     convenience init(URL URL: NSURL)     class func playerWithURL(_ URL: NSURL) -> Self     convenience init(playerItem item: AVPlayerItem)     class func playerWithPlayerItem(_ item: AVPlayerItem) -> Self     init(URL URL: NSURL)     init(playerItem item: AVPlayerItem)     var status: AVPlayerStatus { get }     var error: NSError? { get } } extension AVPlayer {     var rate: Float     func play()     func pause() } extension AVPlayer {     var currentItem: AVPlayerItem? { get }     func replaceCurrentItemWithPlayerItem(_ item: AVPlayerItem?)     var actionAtItemEnd: AVPlayerActionAtItemEnd } extension AVPlayer {     func currentTime() -> CMTime     func seekToDate(_ date: NSDate)     func seekToDate(_ date: NSDate, completionHandler completionHandler: (Bool) -> Void)     func seekToTime(_ time: CMTime)     func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime)     func seekToTime(_ time: CMTime, completionHandler completionHandler: (Bool) -> Void)     func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime, completionHandler completionHandler: (Bool) -> Void) } extension AVPlayer {     func setRate(_ rate: Float, time itemTime: CMTime, atHostTime hostClockTime: CMTime)     func prerollAtRate(_ rate: Float, completionHandler completionHandler: ((Bool) -> Void)?)     func cancelPendingPrerolls()     var masterClock: CMClock? } extension AVPlayer {     func addPeriodicTimeObserverForInterval(_ interval: CMTime, queue queue: dispatch_queue_t?, usingBlock block: (CMTime) -> Void) -> AnyObject     func addBoundaryTimeObserverForTimes(_ times: [NSValue], queue queue: dispatch_queue_t?, usingBlock block: () -> Void) -> AnyObject     func removeTimeObserver(_ observer: AnyObject) } extension AVPlayer {     var volume: Float     var muted: Bool     var closedCaptionDisplayEnabled: Bool } extension AVPlayer {     var appliesMediaSelectionCriteriaAutomatically: Bool     func setMediaSelectionCriteria(_ criteria: AVPlayerMediaSelectionCriteria?, forMediaCharacteristic mediaCharacteristic: String)     func mediaSelectionCriteriaForMediaCharacteristic(_ mediaCharacteristic: String) -> AVPlayerMediaSelectionCriteria? } extension AVPlayer {     var audioOutputDeviceUniqueID: String? } extension AVPlayer {     var allowsExternalPlayback: Bool     var externalPlaybackActive: Bool { get }     var usesExternalPlaybackWhileExternalScreenIsActive: Bool     var externalPlaybackVideoGravity: String } extension AVPlayer {     var allowsAirPlayVideo: Bool     var airPlayVideoActive: Bool { get }     var usesAirPlayVideoWhileAirPlayScreenIsActive: Bool } extension AVPlayer {     var outputObscuredDueToInsufficientExternalProtection: Bool { get } } ``` |

Modified [AVPlayer.addBoundaryTimeObserverForTimes(_: [NSValue], queue: dispatch_queue_t?, usingBlock: () -> Void) -> AnyObject](https://developer.apple.com/documentation/avfoundation/avplayer/1388027-addboundarytimeobserverfortimes)

|  | Declaration |
| --- | --- |
| From | ``` func addBoundaryTimeObserverForTimes(_ times: [AnyObject]!, queue queue: dispatch_queue_t!, usingBlock block: (() -> Void)!) -> AnyObject! ``` |
| To | ``` func addBoundaryTimeObserverForTimes(_ times: [NSValue], queue queue: dispatch_queue_t?, usingBlock block: () -> Void) -> AnyObject ``` |

Modified [AVPlayer.addPeriodicTimeObserverForInterval(_: CMTime, queue: dispatch_queue_t?, usingBlock: (CMTime) -> Void) -> AnyObject](https://developer.apple.com/documentation/avfoundation/avplayer/1385829-addperiodictimeobserverforinterv)

|  | Declaration |
| --- | --- |
| From | ``` func addPeriodicTimeObserverForInterval(_ interval: CMTime, queue queue: dispatch_queue_t!, usingBlock block: ((CMTime) -> Void)!) -> AnyObject! ``` |
| To | ``` func addPeriodicTimeObserverForInterval(_ interval: CMTime, queue queue: dispatch_queue_t?, usingBlock block: (CMTime) -> Void) -> AnyObject ``` |

Modified [AVPlayer.currentItem](https://developer.apple.com/documentation/avfoundation/avplayer/1387569-currentitem)

|  | Declaration |
| --- | --- |
| From | ``` var currentItem: AVPlayerItem! { get } ``` |
| To | ``` var currentItem: AVPlayerItem? { get } ``` |

Modified [AVPlayer.error](https://developer.apple.com/documentation/avfoundation/avplayer/1387764-error)

|  | Declaration |
| --- | --- |
| From | ``` var error: NSError! { get } ``` |
| To | ``` var error: NSError? { get } ``` |

Modified [AVPlayer.externalPlaybackVideoGravity](https://developer.apple.com/documentation/avfoundation/avplayer/1624251-externalplaybackvideogravity)

|  | Declaration |
| --- | --- |
| From | ``` var externalPlaybackVideoGravity: String! ``` |
| To | ``` var externalPlaybackVideoGravity: String ``` |

Modified [AVPlayer.init(playerItem: AVPlayerItem)](https://developer.apple.com/documentation/avfoundation/avplayer/1387104-initwithplayeritem)

|  | Declaration |
| --- | --- |
| From | ``` init!(playerItem item: AVPlayerItem!) ``` |
| To | ``` init(playerItem item: AVPlayerItem) ``` |

Modified [AVPlayer.init(URL: NSURL)](https://developer.apple.com/documentation/avfoundation/avplayer/1385706-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(URL URL: NSURL!) ``` |
| To | ``` init(URL URL: NSURL) ``` |

Modified [AVPlayer.masterClock](https://developer.apple.com/documentation/avfoundation/avplayer/1387066-masterclock)

|  | Declaration |
| --- | --- |
| From | ``` var masterClock: CMClock! ``` |
| To | ``` var masterClock: CMClock? ``` |

Modified [AVPlayer.mediaSelectionCriteriaForMediaCharacteristic(_: String) -> AVPlayerMediaSelectionCriteria?](https://developer.apple.com/documentation/avfoundation/avplayer/1387825-mediaselectioncriteria)

|  | Declaration |
| --- | --- |
| From | ``` func mediaSelectionCriteriaForMediaCharacteristic(_ mediaCharacteristic: String!) -> AVPlayerMediaSelectionCriteria! ``` |
| To | ``` func mediaSelectionCriteriaForMediaCharacteristic(_ mediaCharacteristic: String) -> AVPlayerMediaSelectionCriteria? ``` |

Modified [AVPlayer.prerollAtRate(_: Float, completionHandler: ((Bool) -> Void)?)](https://developer.apple.com/documentation/avfoundation/avplayer/1389712-preroll)

|  | Declaration |
| --- | --- |
| From | ``` func prerollAtRate(_ rate: Float, completionHandler completionHandler: ((Bool) -> Void)!) ``` |
| To | ``` func prerollAtRate(_ rate: Float, completionHandler completionHandler: ((Bool) -> Void)?) ``` |

Modified [AVPlayer.removeTimeObserver(_: AnyObject)](https://developer.apple.com/documentation/avfoundation/avplayer/1387552-removetimeobserver)

|  | Declaration |
| --- | --- |
| From | ``` func removeTimeObserver(_ observer: AnyObject!) ``` |
| To | ``` func removeTimeObserver(_ observer: AnyObject) ``` |

Modified [AVPlayer.replaceCurrentItemWithPlayerItem(_: AVPlayerItem?)](https://developer.apple.com/documentation/avfoundation/avplayer/1390806-replacecurrentitem)

|  | Declaration |
| --- | --- |
| From | ``` func replaceCurrentItemWithPlayerItem(_ item: AVPlayerItem!) ``` |
| To | ``` func replaceCurrentItemWithPlayerItem(_ item: AVPlayerItem?) ``` |

Modified [AVPlayer.seekToDate(_: NSDate)](https://developer.apple.com/documentation/avfoundation/avplayer/1386114-seektodate)

|  | Declaration |
| --- | --- |
| From | ``` func seekToDate(_ date: NSDate!) ``` |
| To | ``` func seekToDate(_ date: NSDate) ``` |

Modified [AVPlayer.seekToDate(_: NSDate, completionHandler: (Bool) -> Void)](https://developer.apple.com/documentation/avfoundation/avplayer/1386108-seektodate)

|  | Declaration |
| --- | --- |
| From | ``` func seekToDate(_ date: NSDate!, completionHandler completionHandler: ((Bool) -> Void)!) ``` |
| To | ``` func seekToDate(_ date: NSDate, completionHandler completionHandler: (Bool) -> Void) ``` |

Modified [AVPlayer.seekToTime(_: CMTime, completionHandler: (Bool) -> Void)](https://developer.apple.com/documentation/avfoundation/avplayer/1387018-seektotime)

|  | Declaration |
| --- | --- |
| From | ``` func seekToTime(_ time: CMTime, completionHandler completionHandler: ((Bool) -> Void)!) ``` |
| To | ``` func seekToTime(_ time: CMTime, completionHandler completionHandler: (Bool) -> Void) ``` |

Modified [AVPlayer.seekToTime(_: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: (Bool) -> Void)](https://developer.apple.com/documentation/avfoundation/avplayer/1388493-seektotime)

|  | Declaration |
| --- | --- |
| From | ``` func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime, completionHandler completionHandler: ((Bool) -> Void)!) ``` |
| To | ``` func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime, completionHandler completionHandler: (Bool) -> Void) ``` |

Modified [AVPlayer.setMediaSelectionCriteria(_: AVPlayerMediaSelectionCriteria?, forMediaCharacteristic: String)](https://developer.apple.com/documentation/avfoundation/avplayer/1390563-setmediaselectioncriteria)

|  | Declaration |
| --- | --- |
| From | ``` func setMediaSelectionCriteria(_ criteria: AVPlayerMediaSelectionCriteria!, forMediaCharacteristic mediaCharacteristic: String!) ``` |
| To | ``` func setMediaSelectionCriteria(_ criteria: AVPlayerMediaSelectionCriteria?, forMediaCharacteristic mediaCharacteristic: String) ``` |

Modified [AVPlayerActionAtItemEnd [enum]](https://developer.apple.com/documentation/avfoundation/avplayer/actionatitemend)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVPlayerItem](https://developer.apple.com/documentation/avfoundation/avplayeritem)

|  | Declaration |
| --- | --- |
| From | ``` class AVPlayerItem : NSObject, NSCopying {     init!(URL URL: NSURL!) -> AVPlayerItem     class func playerItemWithURL(_ URL: NSURL!) -> AVPlayerItem!     init!(asset asset: AVAsset!) -> AVPlayerItem     class func playerItemWithAsset(_ asset: AVAsset!) -> AVPlayerItem!     init!(asset asset: AVAsset!, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [AnyObject]!) -> AVPlayerItem     class func playerItemWithAsset(_ asset: AVAsset!, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [AnyObject]!) -> AVPlayerItem!     init!(URL URL: NSURL!)     init!(asset asset: AVAsset!)     init!(asset asset: AVAsset!, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [AnyObject]!)     var status: AVPlayerItemStatus { get }     var error: NSError! { get } } extension AVPlayerItem {     var asset: AVAsset! { get }     var tracks: [AnyObject]! { get }     var duration: CMTime { get }     var presentationSize: CGSize { get }     var timedMetadata: [AnyObject]! { get }     var automaticallyLoadedAssetKeys: [AnyObject]! { get } } extension AVPlayerItem {     var canPlayFastForward: Bool { get }     var canPlaySlowForward: Bool { get }     var canPlayReverse: Bool { get }     var canPlaySlowReverse: Bool { get }     var canPlayFastReverse: Bool { get }     var canStepForward: Bool { get }     var canStepBackward: Bool { get } } extension AVPlayerItem {     func currentTime() -> CMTime     var forwardPlaybackEndTime: CMTime     var reversePlaybackEndTime: CMTime     var seekableTimeRanges: [AnyObject]! { get }     func seekToTime(_ time: CMTime)     func seekToTime(_ time: CMTime, completionHandler completionHandler: ((Bool) -> Void)!)     func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime)     func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime, completionHandler completionHandler: ((Bool) -> Void)!)     func cancelPendingSeeks()     func currentDate() -> NSDate!     func seekToDate(_ date: NSDate!) -> Bool     func seekToDate(_ date: NSDate!, completionHandler completionHandler: ((Bool) -> Void)!) -> Bool     func stepByCount(_ stepCount: Int)     var timebase: CMTimebase! { get } } extension AVPlayerItem {     @NSCopying var videoComposition: AVVideoComposition!     var customVideoCompositor: AVVideoCompositing! { get }     var seekingWaitsForVideoCompositionRendering: Bool     var textStyleRules: [AnyObject]! } extension AVPlayerItem {     var audioTimePitchAlgorithm: String!     @NSCopying var audioMix: AVAudioMix! } extension AVPlayerItem {     var loadedTimeRanges: [AnyObject]! { get }     var playbackLikelyToKeepUp: Bool { get }     var playbackBufferFull: Bool { get }     var playbackBufferEmpty: Bool { get } } extension AVPlayerItem {     var preferredPeakBitRate: Double } extension AVPlayerItem {     func selectMediaOption(_ mediaSelectionOption: AVMediaSelectionOption!, inMediaSelectionGroup mediaSelectionGroup: AVMediaSelectionGroup!)     func selectMediaOptionAutomaticallyInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup!)     func selectedMediaOptionInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup!) -> AVMediaSelectionOption! } extension AVPlayerItem {     func accessLog() -> AVPlayerItemAccessLog!     func errorLog() -> AVPlayerItemErrorLog! } extension AVPlayerItem {     func addOutput(_ output: AVPlayerItemOutput!)     func removeOutput(_ output: AVPlayerItemOutput!)     var outputs: [AnyObject]! { get } } ``` |
| To | ``` class AVPlayerItem : NSObject, NSCopying {     convenience init()      init(URL URL: NSURL)     class func playerItemWithURL(_ URL: NSURL) -> AVPlayerItem      init(asset asset: AVAsset)     class func playerItemWithAsset(_ asset: AVAsset) -> AVPlayerItem      init(asset asset: AVAsset, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [String]?)     class func playerItemWithAsset(_ asset: AVAsset, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [String]?) -> AVPlayerItem     convenience init(URL URL: NSURL)     convenience init(asset asset: AVAsset)     init(asset asset: AVAsset, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [String]?)     var status: AVPlayerItemStatus { get }     var error: NSError? { get } } extension AVPlayerItem {     var asset: AVAsset { get }     var tracks: [AVPlayerItemTrack] { get }     var duration: CMTime { get }     var presentationSize: CGSize { get }     var timedMetadata: [AVMetadataItem]? { get }     var automaticallyLoadedAssetKeys: [String] { get } } extension AVPlayerItem {     var canPlayFastForward: Bool { get }     var canPlaySlowForward: Bool { get }     var canPlayReverse: Bool { get }     var canPlaySlowReverse: Bool { get }     var canPlayFastReverse: Bool { get }     var canStepForward: Bool { get }     var canStepBackward: Bool { get } } extension AVPlayerItem {     func currentTime() -> CMTime     var forwardPlaybackEndTime: CMTime     var reversePlaybackEndTime: CMTime     var seekableTimeRanges: [NSValue] { get }     func seekToTime(_ time: CMTime)     func seekToTime(_ time: CMTime, completionHandler completionHandler: (Bool) -> Void)     func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime)     func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime, completionHandler completionHandler: (Bool) -> Void)     func cancelPendingSeeks()     func currentDate() -> NSDate?     func seekToDate(_ date: NSDate) -> Bool     func seekToDate(_ date: NSDate, completionHandler completionHandler: (Bool) -> Void) -> Bool     func stepByCount(_ stepCount: Int)     var timebase: CMTimebase? { get } } extension AVPlayerItem {     @NSCopying var videoComposition: AVVideoComposition?     var customVideoCompositor: AVVideoCompositing? { get }     var seekingWaitsForVideoCompositionRendering: Bool     var textStyleRules: [AVTextStyleRule]? } extension AVPlayerItem {     var audioTimePitchAlgorithm: String     @NSCopying var audioMix: AVAudioMix? } extension AVPlayerItem {     var loadedTimeRanges: [NSValue] { get }     var playbackLikelyToKeepUp: Bool { get }     var playbackBufferFull: Bool { get }     var playbackBufferEmpty: Bool { get }     var canUseNetworkResourcesForLiveStreamingWhilePaused: Bool } extension AVPlayerItem {     var preferredPeakBitRate: Double } extension AVPlayerItem {     func selectMediaOption(_ mediaSelectionOption: AVMediaSelectionOption?, inMediaSelectionGroup mediaSelectionGroup: AVMediaSelectionGroup)     func selectMediaOptionAutomaticallyInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup)     func selectedMediaOptionInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption?     var currentMediaSelection: AVMediaSelection { get } } extension AVPlayerItem {     func accessLog() -> AVPlayerItemAccessLog?     func errorLog() -> AVPlayerItemErrorLog? } extension AVPlayerItem {     func addOutput(_ output: AVPlayerItemOutput)     func removeOutput(_ output: AVPlayerItemOutput)     var outputs: [AVPlayerItemOutput] { get } } ``` |

Modified [AVPlayerItem.accessLog() -> AVPlayerItemAccessLog?](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388499-accesslog)

|  | Declaration |
| --- | --- |
| From | ``` func accessLog() -> AVPlayerItemAccessLog! ``` |
| To | ``` func accessLog() -> AVPlayerItemAccessLog? ``` |

Modified [AVPlayerItem.addOutput(_: AVPlayerItemOutput)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389782-add)

|  | Declaration |
| --- | --- |
| From | ``` func addOutput(_ output: AVPlayerItemOutput!) ``` |
| To | ``` func addOutput(_ output: AVPlayerItemOutput) ``` |

Modified [AVPlayerItem.asset](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388177-asset)

|  | Declaration |
| --- | --- |
| From | ``` var asset: AVAsset! { get } ``` |
| To | ``` var asset: AVAsset { get } ``` |

Modified [AVPlayerItem.audioMix](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388037-audiomix)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var audioMix: AVAudioMix! ``` |
| To | ``` @NSCopying var audioMix: AVAudioMix? ``` |

Modified [AVPlayerItem.audioTimePitchAlgorithm](https://developer.apple.com/documentation/avfoundation/avplayeritem/1385855-audiotimepitchalgorithm)

|  | Declaration |
| --- | --- |
| From | ``` var audioTimePitchAlgorithm: String! ``` |
| To | ``` var audioTimePitchAlgorithm: String ``` |

Modified [AVPlayerItem.automaticallyLoadedAssetKeys](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388633-automaticallyloadedassetkeys)

|  | Declaration |
| --- | --- |
| From | ``` var automaticallyLoadedAssetKeys: [AnyObject]! { get } ``` |
| To | ``` var automaticallyLoadedAssetKeys: [String] { get } ``` |

Modified [AVPlayerItem.currentDate() -> NSDate?](https://developer.apple.com/documentation/avfoundation/avplayeritem/1386188-currentdate)

|  | Declaration |
| --- | --- |
| From | ``` func currentDate() -> NSDate! ``` |
| To | ``` func currentDate() -> NSDate? ``` |

Modified [AVPlayerItem.customVideoCompositor](https://developer.apple.com/documentation/avfoundation/avplayeritem/1390669-customvideocompositor)

|  | Declaration |
| --- | --- |
| From | ``` var customVideoCompositor: AVVideoCompositing! { get } ``` |
| To | ``` var customVideoCompositor: AVVideoCompositing? { get } ``` |

Modified [AVPlayerItem.error](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389185-error)

|  | Declaration |
| --- | --- |
| From | ``` var error: NSError! { get } ``` |
| To | ``` var error: NSError? { get } ``` |

Modified [AVPlayerItem.errorLog() -> AVPlayerItemErrorLog?](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387573-errorlog)

|  | Declaration |
| --- | --- |
| From | ``` func errorLog() -> AVPlayerItemErrorLog! ``` |
| To | ``` func errorLog() -> AVPlayerItemErrorLog? ``` |

Modified [AVPlayerItem.init(asset: AVAsset)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1390707-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(asset asset: AVAsset!) ``` |
| To | ``` convenience init(asset asset: AVAsset) ``` |

Modified [AVPlayerItem.init(asset: AVAsset, automaticallyLoadedAssetKeys: [String]?)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387529-initwithasset)

|  | Declaration |
| --- | --- |
| From | ``` init!(asset asset: AVAsset!, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [AnyObject]!) ``` |
| To | ``` init(asset asset: AVAsset, automaticallyLoadedAssetKeys automaticallyLoadedAssetKeys: [String]?) ``` |

Modified [AVPlayerItem.init(URL: NSURL)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387558-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(URL URL: NSURL!) ``` |
| To | ``` convenience init(URL URL: NSURL) ``` |

Modified [AVPlayerItem.loadedTimeRanges](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389953-loadedtimeranges)

|  | Declaration |
| --- | --- |
| From | ``` var loadedTimeRanges: [AnyObject]! { get } ``` |
| To | ``` var loadedTimeRanges: [NSValue] { get } ``` |

Modified [AVPlayerItem.outputs](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389090-outputs)

|  | Declaration |
| --- | --- |
| From | ``` var outputs: [AnyObject]! { get } ``` |
| To | ``` var outputs: [AVPlayerItemOutput] { get } ``` |

Modified [AVPlayerItem.removeOutput(_: AVPlayerItemOutput)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388756-remove)

|  | Declaration |
| --- | --- |
| From | ``` func removeOutput(_ output: AVPlayerItemOutput!) ``` |
| To | ``` func removeOutput(_ output: AVPlayerItemOutput) ``` |

Modified [AVPlayerItem.seekableTimeRanges](https://developer.apple.com/documentation/avfoundation/avplayeritem/1386155-seekabletimeranges)

|  | Declaration |
| --- | --- |
| From | ``` var seekableTimeRanges: [AnyObject]! { get } ``` |
| To | ``` var seekableTimeRanges: [NSValue] { get } ``` |

Modified [AVPlayerItem.seekToDate(_: NSDate) -> Bool](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389067-seektodate)

|  | Declaration |
| --- | --- |
| From | ``` func seekToDate(_ date: NSDate!) -> Bool ``` |
| To | ``` func seekToDate(_ date: NSDate) -> Bool ``` |

Modified [AVPlayerItem.seekToDate(_: NSDate, completionHandler: (Bool) -> Void) -> Bool](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389877-seek)

|  | Declaration |
| --- | --- |
| From | ``` func seekToDate(_ date: NSDate!, completionHandler completionHandler: ((Bool) -> Void)!) -> Bool ``` |
| To | ``` func seekToDate(_ date: NSDate, completionHandler completionHandler: (Bool) -> Void) -> Bool ``` |

Modified [AVPlayerItem.seekToTime(_: CMTime, completionHandler: (Bool) -> Void)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387418-seek)

|  | Declaration |
| --- | --- |
| From | ``` func seekToTime(_ time: CMTime, completionHandler completionHandler: ((Bool) -> Void)!) ``` |
| To | ``` func seekToTime(_ time: CMTime, completionHandler completionHandler: (Bool) -> Void) ``` |

Modified [AVPlayerItem.seekToTime(_: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: (Bool) -> Void)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387753-seek)

|  | Declaration |
| --- | --- |
| From | ``` func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime, completionHandler completionHandler: ((Bool) -> Void)!) ``` |
| To | ``` func seekToTime(_ time: CMTime, toleranceBefore toleranceBefore: CMTime, toleranceAfter toleranceAfter: CMTime, completionHandler completionHandler: (Bool) -> Void) ``` |

Modified [AVPlayerItem.selectedMediaOptionInMediaSelectionGroup(_: AVMediaSelectionGroup) -> AVMediaSelectionOption?](https://developer.apple.com/documentation/avfoundation/avplayeritem/1386314-selectedmediaoptioninmediaselect)

|  | Declaration |
| --- | --- |
| From | ``` func selectedMediaOptionInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup!) -> AVMediaSelectionOption! ``` |
| To | ``` func selectedMediaOptionInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption? ``` |

Modified [AVPlayerItem.selectMediaOption(_: AVMediaSelectionOption?, inMediaSelectionGroup: AVMediaSelectionGroup)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389610-selectmediaoption)

|  | Declaration |
| --- | --- |
| From | ``` func selectMediaOption(_ mediaSelectionOption: AVMediaSelectionOption!, inMediaSelectionGroup mediaSelectionGroup: AVMediaSelectionGroup!) ``` |
| To | ``` func selectMediaOption(_ mediaSelectionOption: AVMediaSelectionOption?, inMediaSelectionGroup mediaSelectionGroup: AVMediaSelectionGroup) ``` |

Modified [AVPlayerItem.selectMediaOptionAutomaticallyInMediaSelectionGroup(_: AVMediaSelectionGroup)](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388268-selectmediaoptionautomatically)

|  | Declaration |
| --- | --- |
| From | ``` func selectMediaOptionAutomaticallyInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup!) ``` |
| To | ``` func selectMediaOptionAutomaticallyInMediaSelectionGroup(_ mediaSelectionGroup: AVMediaSelectionGroup) ``` |

Modified [AVPlayerItem.textStyleRules](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389681-textstylerules)

|  | Declaration |
| --- | --- |
| From | ``` var textStyleRules: [AnyObject]! ``` |
| To | ``` var textStyleRules: [AVTextStyleRule]? ``` |

Modified [AVPlayerItem.timebase](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387605-timebase)

|  | Declaration |
| --- | --- |
| From | ``` var timebase: CMTimebase! { get } ``` |
| To | ``` var timebase: CMTimebase? { get } ``` |

Modified [AVPlayerItem.timedMetadata](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389602-timedmetadata)

|  | Declaration |
| --- | --- |
| From | ``` var timedMetadata: [AnyObject]! { get } ``` |
| To | ``` var timedMetadata: [AVMetadataItem]? { get } ``` |

Modified [AVPlayerItem.tracks](https://developer.apple.com/documentation/avfoundation/avplayeritem/1386361-tracks)

|  | Declaration |
| --- | --- |
| From | ``` var tracks: [AnyObject]! { get } ``` |
| To | ``` var tracks: [AVPlayerItemTrack] { get } ``` |

Modified [AVPlayerItem.videoComposition](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388818-videocomposition)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var videoComposition: AVVideoComposition! ``` |
| To | ``` @NSCopying var videoComposition: AVVideoComposition? ``` |

Modified [AVPlayerItemAccessLog](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslog)

|  | Declaration |
| --- | --- |
| From | ``` class AVPlayerItemAccessLog : NSObject, NSCopying {     func extendedLogData() -> NSData!     var extendedLogDataStringEncoding: UInt { get }     var events: [AnyObject]! { get } } ``` |
| To | ``` class AVPlayerItemAccessLog : NSObject, NSCopying {     func extendedLogData() -> NSData?     var extendedLogDataStringEncoding: UInt { get }     var events: [AVPlayerItemAccessLogEvent] { get } } ``` |

Modified [AVPlayerItemAccessLog.events](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslog/1387406-events)

|  | Declaration |
| --- | --- |
| From | ``` var events: [AnyObject]! { get } ``` |
| To | ``` var events: [AVPlayerItemAccessLogEvent] { get } ``` |

Modified [AVPlayerItemAccessLog.extendedLogData() -> NSData?](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslog/1386892-extendedlogdata)

|  | Declaration |
| --- | --- |
| From | ``` func extendedLogData() -> NSData! ``` |
| To | ``` func extendedLogData() -> NSData? ``` |

Modified [AVPlayerItemAccessLogEvent](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent)

|  | Declaration |
| --- | --- |
| From | ``` class AVPlayerItemAccessLogEvent : NSObject, NSCopying {     var numberOfSegmentsDownloaded: Int { get }     var numberOfMediaRequests: Int { get }     var playbackStartDate: NSDate! { get }     var URI: String! { get }     var serverAddress: String! { get }     var numberOfServerAddressChanges: Int { get }     var playbackSessionID: String! { get }     var playbackStartOffset: NSTimeInterval { get }     var segmentsDownloadedDuration: NSTimeInterval { get }     var durationWatched: NSTimeInterval { get }     var numberOfStalls: Int { get }     var numberOfBytesTransferred: Int64 { get }     var transferDuration: NSTimeInterval { get }     var observedBitrate: Double { get }     var indicatedBitrate: Double { get }     var numberOfDroppedVideoFrames: Int { get }     var startupTime: NSTimeInterval { get }     var downloadOverdue: Int { get }     var observedMaxBitrate: Double { get }     var observedMinBitrate: Double { get }     var observedBitrateStandardDeviation: Double { get }     var playbackType: String! { get }     var mediaRequestsWWAN: Int { get }     var switchBitrate: Double { get } } ``` |
| To | ``` class AVPlayerItemAccessLogEvent : NSObject, NSCopying {     var numberOfSegmentsDownloaded: Int { get }     var numberOfMediaRequests: Int { get }     var playbackStartDate: NSDate? { get }     var URI: String? { get }     var serverAddress: String? { get }     var numberOfServerAddressChanges: Int { get }     var playbackSessionID: String? { get }     var playbackStartOffset: NSTimeInterval { get }     var segmentsDownloadedDuration: NSTimeInterval { get }     var durationWatched: NSTimeInterval { get }     var numberOfStalls: Int { get }     var numberOfBytesTransferred: Int64 { get }     var transferDuration: NSTimeInterval { get }     var observedBitrate: Double { get }     var indicatedBitrate: Double { get }     var numberOfDroppedVideoFrames: Int { get }     var startupTime: NSTimeInterval { get }     var downloadOverdue: Int { get }     var observedMaxBitrate: Double { get }     var observedMinBitrate: Double { get }     var observedBitrateStandardDeviation: Double { get }     var playbackType: String? { get }     var mediaRequestsWWAN: Int { get }     var switchBitrate: Double { get } } ``` |

Modified [AVPlayerItemAccessLogEvent.playbackSessionID](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1388462-playbacksessionid)

|  | Declaration |
| --- | --- |
| From | ``` var playbackSessionID: String! { get } ``` |
| To | ``` var playbackSessionID: String? { get } ``` |

Modified [AVPlayerItemAccessLogEvent.playbackStartDate](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1390502-playbackstartdate)

|  | Declaration |
| --- | --- |
| From | ``` var playbackStartDate: NSDate! { get } ``` |
| To | ``` var playbackStartDate: NSDate? { get } ``` |

Modified [AVPlayerItemAccessLogEvent.playbackType](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1387218-playbacktype)

|  | Declaration |
| --- | --- |
| From | ``` var playbackType: String! { get } ``` |
| To | ``` var playbackType: String? { get } ``` |

Modified [AVPlayerItemAccessLogEvent.serverAddress](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1390315-serveraddress)

|  | Declaration |
| --- | --- |
| From | ``` var serverAddress: String! { get } ``` |
| To | ``` var serverAddress: String? { get } ``` |

Modified [AVPlayerItemAccessLogEvent.URI](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1388643-uri)

|  | Declaration |
| --- | --- |
| From | ``` var URI: String! { get } ``` |
| To | ``` var URI: String? { get } ``` |

Modified [AVPlayerItemErrorLog](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlog)

|  | Declaration |
| --- | --- |
| From | ``` class AVPlayerItemErrorLog : NSObject, NSCopying {     func extendedLogData() -> NSData!     var extendedLogDataStringEncoding: UInt { get }     var events: [AnyObject]! { get } } ``` |
| To | ``` class AVPlayerItemErrorLog : NSObject, NSCopying {     func extendedLogData() -> NSData?     var extendedLogDataStringEncoding: UInt { get }     var events: [AVPlayerItemErrorLogEvent] { get } } ``` |

Modified [AVPlayerItemErrorLog.events](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlog/1387637-events)

|  | Declaration |
| --- | --- |
| From | ``` var events: [AnyObject]! { get } ``` |
| To | ``` var events: [AVPlayerItemErrorLogEvent] { get } ``` |

Modified [AVPlayerItemErrorLog.extendedLogData() -> NSData?](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlog/1389100-extendedlogdata)

|  | Declaration |
| --- | --- |
| From | ``` func extendedLogData() -> NSData! ``` |
| To | ``` func extendedLogData() -> NSData? ``` |

Modified [AVPlayerItemErrorLogEvent](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent)

|  | Declaration |
| --- | --- |
| From | ``` class AVPlayerItemErrorLogEvent : NSObject, NSCopying {     var date: NSDate! { get }     var URI: String! { get }     var serverAddress: String! { get }     var playbackSessionID: String! { get }     var errorStatusCode: Int { get }     var errorDomain: String! { get }     var errorComment: String! { get } } ``` |
| To | ``` class AVPlayerItemErrorLogEvent : NSObject, NSCopying {     var date: NSDate? { get }     var URI: String? { get }     var serverAddress: String? { get }     var playbackSessionID: String? { get }     var errorStatusCode: Int { get }     var errorDomain: String { get }     var errorComment: String? { get } } ``` |

Modified [AVPlayerItemErrorLogEvent.date](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/1388416-date)

|  | Declaration |
| --- | --- |
| From | ``` var date: NSDate! { get } ``` |
| To | ``` var date: NSDate? { get } ``` |

Modified [AVPlayerItemErrorLogEvent.errorComment](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/1388011-errorcomment)

|  | Declaration |
| --- | --- |
| From | ``` var errorComment: String! { get } ``` |
| To | ``` var errorComment: String? { get } ``` |

Modified [AVPlayerItemErrorLogEvent.errorDomain](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/1388603-errordomain)

|  | Declaration |
| --- | --- |
| From | ``` var errorDomain: String! { get } ``` |
| To | ``` var errorDomain: String { get } ``` |

Modified [AVPlayerItemErrorLogEvent.playbackSessionID](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/1385934-playbacksessionid)

|  | Declaration |
| --- | --- |
| From | ``` var playbackSessionID: String! { get } ``` |
| To | ``` var playbackSessionID: String? { get } ``` |

Modified [AVPlayerItemErrorLogEvent.serverAddress](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/1385797-serveraddress)

|  | Declaration |
| --- | --- |
| From | ``` var serverAddress: String! { get } ``` |
| To | ``` var serverAddress: String? { get } ``` |

Modified [AVPlayerItemErrorLogEvent.URI](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/1389302-uri)

|  | Declaration |
| --- | --- |
| From | ``` var URI: String! { get } ``` |
| To | ``` var URI: String? { get } ``` |

Modified [AVPlayerItemLegibleOutput](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput)

|  | Declaration |
| --- | --- |
| From | ``` class AVPlayerItemLegibleOutput : AVPlayerItemOutput {     func setDelegate(_ delegate: AVPlayerItemLegibleOutputPushDelegate!, queue delegateQueue: dispatch_queue_t!)     var delegate: AVPlayerItemLegibleOutputPushDelegate! { get }     var delegateQueue: dispatch_queue_t! { get }     var advanceIntervalForDelegateInvocation: NSTimeInterval } extension AVPlayerItemLegibleOutput {     init!(mediaSubtypesForNativeRepresentation subtypes: [AnyObject]!) } extension AVPlayerItemLegibleOutput {     var textStylingResolution: String! } ``` |
| To | ``` class AVPlayerItemLegibleOutput : AVPlayerItemOutput {     func setDelegate(_ delegate: AVPlayerItemLegibleOutputPushDelegate?, queue delegateQueue: dispatch_queue_t?)     weak var delegate: AVPlayerItemLegibleOutputPushDelegate? { get }     var delegateQueue: dispatch_queue_t? { get }     var advanceIntervalForDelegateInvocation: NSTimeInterval } extension AVPlayerItemLegibleOutput {     init(mediaSubtypesForNativeRepresentation subtypes: [NSNumber]) } extension AVPlayerItemLegibleOutput {     var textStylingResolution: String } ``` |

Modified [AVPlayerItemLegibleOutput.delegate](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/1387877-delegate)

|  | Declaration |
| --- | --- |
| From | ``` var delegate: AVPlayerItemLegibleOutputPushDelegate! { get } ``` |
| To | ``` weak var delegate: AVPlayerItemLegibleOutputPushDelegate? { get } ``` |

Modified [AVPlayerItemLegibleOutput.delegateQueue](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/1386275-delegatequeue)

|  | Declaration |
| --- | --- |
| From | ``` var delegateQueue: dispatch_queue_t! { get } ``` |
| To | ``` var delegateQueue: dispatch_queue_t? { get } ``` |

Modified [AVPlayerItemLegibleOutput.init(mediaSubtypesForNativeRepresentation: [NSNumber])](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/1390500-initwithmediasubtypesfornativere)

|  | Declaration |
| --- | --- |
| From | ``` init!(mediaSubtypesForNativeRepresentation subtypes: [AnyObject]!) ``` |
| To | ``` init(mediaSubtypesForNativeRepresentation subtypes: [NSNumber]) ``` |

Modified [AVPlayerItemLegibleOutput.setDelegate(_: AVPlayerItemLegibleOutputPushDelegate?, queue: dispatch_queue_t?)](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/1386204-setdelegate)

|  | Declaration |
| --- | --- |
| From | ``` func setDelegate(_ delegate: AVPlayerItemLegibleOutputPushDelegate!, queue delegateQueue: dispatch_queue_t!) ``` |
| To | ``` func setDelegate(_ delegate: AVPlayerItemLegibleOutputPushDelegate?, queue delegateQueue: dispatch_queue_t?) ``` |

Modified [AVPlayerItemLegibleOutput.textStylingResolution](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/1385803-textstylingresolution)

|  | Declaration |
| --- | --- |
| From | ``` var textStylingResolution: String! ``` |
| To | ``` var textStylingResolution: String ``` |

Modified [AVPlayerItemLegibleOutputPushDelegate](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutputpushdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVPlayerItemLegibleOutputPushDelegate : AVPlayerItemOutputPushDelegate, NSObjectProtocol {     optional func legibleOutput(_ output: AVPlayerItemLegibleOutput!, didOutputAttributedStrings strings: [AnyObject]!, nativeSampleBuffers nativeSamples: [AnyObject]!, forItemTime itemTime: CMTime) } ``` |
| To | ``` protocol AVPlayerItemLegibleOutputPushDelegate : AVPlayerItemOutputPushDelegate, NSObjectProtocol {     optional func legibleOutput(_ output: AVPlayerItemLegibleOutput, didOutputAttributedStrings strings: [NSAttributedString], nativeSampleBuffers nativeSamples: [AnyObject], forItemTime itemTime: CMTime) } ``` |

Modified [AVPlayerItemLegibleOutputPushDelegate.legibleOutput(_: AVPlayerItemLegibleOutput, didOutputAttributedStrings: [NSAttributedString], nativeSampleBuffers: [AnyObject], forItemTime: CMTime)](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutputpushdelegate/1386790-legibleoutput)

|  | Declaration |
| --- | --- |
| From | ``` optional func legibleOutput(_ output: AVPlayerItemLegibleOutput!, didOutputAttributedStrings strings: [AnyObject]!, nativeSampleBuffers nativeSamples: [AnyObject]!, forItemTime itemTime: CMTime) ``` |
| To | ``` optional func legibleOutput(_ output: AVPlayerItemLegibleOutput, didOutputAttributedStrings strings: [NSAttributedString], nativeSampleBuffers nativeSamples: [AnyObject], forItemTime itemTime: CMTime) ``` |

Modified [AVPlayerItemMetadataOutput](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput)

|  | Declaration |
| --- | --- |
| From | ``` class AVPlayerItemMetadataOutput : AVPlayerItemOutput {     init!(identifiers identifiers: [AnyObject]!)     func setDelegate(_ delegate: AVPlayerItemMetadataOutputPushDelegate!, queue delegateQueue: dispatch_queue_t!)     var delegate: AVPlayerItemMetadataOutputPushDelegate! { get }     var delegateQueue: dispatch_queue_t! { get }     var advanceIntervalForDelegateInvocation: NSTimeInterval } ``` |
| To | ``` class AVPlayerItemMetadataOutput : AVPlayerItemOutput {     init(identifiers identifiers: [String]?)     func setDelegate(_ delegate: AVPlayerItemMetadataOutputPushDelegate?, queue delegateQueue: dispatch_queue_t?)     weak var delegate: AVPlayerItemMetadataOutputPushDelegate? { get }     var delegateQueue: dispatch_queue_t? { get }     var advanceIntervalForDelegateInvocation: NSTimeInterval } ``` |

Modified [AVPlayerItemMetadataOutput.delegate](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput/1387200-delegate)

|  | Declaration |
| --- | --- |
| From | ``` var delegate: AVPlayerItemMetadataOutputPushDelegate! { get } ``` |
| To | ``` weak var delegate: AVPlayerItemMetadataOutputPushDelegate? { get } ``` |

Modified [AVPlayerItemMetadataOutput.delegateQueue](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput/1387265-delegatequeue)

|  | Declaration |
| --- | --- |
| From | ``` var delegateQueue: dispatch_queue_t! { get } ``` |
| To | ``` var delegateQueue: dispatch_queue_t? { get } ``` |

Modified [AVPlayerItemMetadataOutput.init(identifiers: [String]?)](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput/1390205-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(identifiers identifiers: [AnyObject]!) ``` |
| To | ``` init(identifiers identifiers: [String]?) ``` |

Modified [AVPlayerItemMetadataOutput.setDelegate(_: AVPlayerItemMetadataOutputPushDelegate?, queue: dispatch_queue_t?)](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput/1385728-setdelegate)

|  | Declaration |
| --- | --- |
| From | ``` func setDelegate(_ delegate: AVPlayerItemMetadataOutputPushDelegate!, queue delegateQueue: dispatch_queue_t!) ``` |
| To | ``` func setDelegate(_ delegate: AVPlayerItemMetadataOutputPushDelegate?, queue delegateQueue: dispatch_queue_t?) ``` |

Modified [AVPlayerItemMetadataOutputPushDelegate](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutputpushdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVPlayerItemMetadataOutputPushDelegate : AVPlayerItemOutputPushDelegate, NSObjectProtocol {     optional func metadataOutput(_ output: AVPlayerItemMetadataOutput!, didOutputTimedMetadataGroups groups: [AnyObject]!, fromPlayerItemTrack track: AVPlayerItemTrack!) } ``` |
| To | ``` protocol AVPlayerItemMetadataOutputPushDelegate : AVPlayerItemOutputPushDelegate, NSObjectProtocol {     optional func metadataOutput(_ output: AVPlayerItemMetadataOutput, didOutputTimedMetadataGroups groups: [AVTimedMetadataGroup], fromPlayerItemTrack track: AVPlayerItemTrack) } ``` |

Modified [AVPlayerItemMetadataOutputPushDelegate.metadataOutput(_: AVPlayerItemMetadataOutput, didOutputTimedMetadataGroups: [AVTimedMetadataGroup], fromPlayerItemTrack: AVPlayerItemTrack)](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutputpushdelegate/1388071-metadataoutput)

|  | Declaration |
| --- | --- |
| From | ``` optional func metadataOutput(_ output: AVPlayerItemMetadataOutput!, didOutputTimedMetadataGroups groups: [AnyObject]!, fromPlayerItemTrack track: AVPlayerItemTrack!) ``` |
| To | ``` optional func metadataOutput(_ output: AVPlayerItemMetadataOutput, didOutputTimedMetadataGroups groups: [AVTimedMetadataGroup], fromPlayerItemTrack track: AVPlayerItemTrack) ``` |

Modified [AVPlayerItemOutputPullDelegate](https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpulldelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVPlayerItemOutputPullDelegate : NSObjectProtocol {     optional func outputMediaDataWillChange(_ sender: AVPlayerItemOutput!)     optional func outputSequenceWasFlushed(_ output: AVPlayerItemOutput!) } ``` |
| To | ``` protocol AVPlayerItemOutputPullDelegate : NSObjectProtocol {     optional func outputMediaDataWillChange(_ sender: AVPlayerItemOutput)     optional func outputSequenceWasFlushed(_ output: AVPlayerItemOutput) } ``` |

Modified [AVPlayerItemOutputPullDelegate.outputMediaDataWillChange(_: AVPlayerItemOutput)](https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpulldelegate/1387498-outputmediadatawillchange)

|  | Declaration |
| --- | --- |
| From | ``` optional func outputMediaDataWillChange(_ sender: AVPlayerItemOutput!) ``` |
| To | ``` optional func outputMediaDataWillChange(_ sender: AVPlayerItemOutput) ``` |

Modified [AVPlayerItemOutputPullDelegate.outputSequenceWasFlushed(_: AVPlayerItemOutput)](https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpulldelegate/1387279-outputsequencewasflushed)

|  | Declaration |
| --- | --- |
| From | ``` optional func outputSequenceWasFlushed(_ output: AVPlayerItemOutput!) ``` |
| To | ``` optional func outputSequenceWasFlushed(_ output: AVPlayerItemOutput) ``` |

Modified [AVPlayerItemOutputPushDelegate](https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpushdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVPlayerItemOutputPushDelegate : NSObjectProtocol {     optional func outputSequenceWasFlushed(_ output: AVPlayerItemOutput!) } ``` |
| To | ``` protocol AVPlayerItemOutputPushDelegate : NSObjectProtocol {     optional func outputSequenceWasFlushed(_ output: AVPlayerItemOutput) } ``` |

Modified [AVPlayerItemOutputPushDelegate.outputSequenceWasFlushed(_: AVPlayerItemOutput)](https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpushdelegate/1390224-outputsequencewasflushed)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func outputSequenceWasFlushed(_ output: AVPlayerItemOutput!) ``` | iOS 8.0 |
| To | ``` optional func outputSequenceWasFlushed(_ output: AVPlayerItemOutput) ``` | iOS 6.0 |

Modified [AVPlayerItemStatus [enum]](https://developer.apple.com/documentation/avfoundation/avplayeritem/status)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVPlayerItemTrack](https://developer.apple.com/documentation/avfoundation/avplayeritemtrack)

|  | Declaration |
| --- | --- |
| From | ``` class AVPlayerItemTrack : NSObject {     var assetTrack: AVAssetTrack! { get }     var enabled: Bool     var currentVideoFrameRate: Float { get } } ``` |
| To | ``` class AVPlayerItemTrack : NSObject {     var assetTrack: AVAssetTrack { get }     var enabled: Bool     var currentVideoFrameRate: Float { get } } ``` |

Modified [AVPlayerItemTrack.assetTrack](https://developer.apple.com/documentation/avfoundation/avplayeritemtrack/1390701-assettrack)

|  | Declaration |
| --- | --- |
| From | ``` var assetTrack: AVAssetTrack! { get } ``` |
| To | ``` var assetTrack: AVAssetTrack { get } ``` |

Modified [AVPlayerItemVideoOutput](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput)

|  | Declaration |
| --- | --- |
| From | ``` class AVPlayerItemVideoOutput : AVPlayerItemOutput {     init!(pixelBufferAttributes pixelBufferAttributes: [NSObject : AnyObject]!)     func hasNewPixelBufferForItemTime(_ itemTime: CMTime) -> Bool     func copyPixelBufferForItemTime(_ itemTime: CMTime, itemTimeForDisplay outItemTimeForDisplay: UnsafeMutablePointer<CMTime>) -> CVPixelBuffer!     func setDelegate(_ delegate: AVPlayerItemOutputPullDelegate!, queue delegateQueue: dispatch_queue_t!)     func requestNotificationOfMediaDataChangeWithAdvanceInterval(_ interval: NSTimeInterval)     var delegate: AVPlayerItemOutputPullDelegate! { get }     var delegateQueue: dispatch_queue_t! { get } } ``` |
| To | ``` class AVPlayerItemVideoOutput : AVPlayerItemOutput {     init(pixelBufferAttributes pixelBufferAttributes: [String : AnyObject]?)     func hasNewPixelBufferForItemTime(_ itemTime: CMTime) -> Bool     func copyPixelBufferForItemTime(_ itemTime: CMTime, itemTimeForDisplay outItemTimeForDisplay: UnsafeMutablePointer<CMTime>) -> CVPixelBuffer?     func setDelegate(_ delegate: AVPlayerItemOutputPullDelegate?, queue delegateQueue: dispatch_queue_t?)     func requestNotificationOfMediaDataChangeWithAdvanceInterval(_ interval: NSTimeInterval)     unowned(unsafe) var delegate: AVPlayerItemOutputPullDelegate? { get }     var delegateQueue: dispatch_queue_t? { get } } ``` |

Modified [AVPlayerItemVideoOutput.copyPixelBufferForItemTime(_: CMTime, itemTimeForDisplay: UnsafeMutablePointer<CMTime>) -> CVPixelBuffer?](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1386148-copypixelbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func copyPixelBufferForItemTime(_ itemTime: CMTime, itemTimeForDisplay outItemTimeForDisplay: UnsafeMutablePointer<CMTime>) -> CVPixelBuffer! ``` |
| To | ``` func copyPixelBufferForItemTime(_ itemTime: CMTime, itemTimeForDisplay outItemTimeForDisplay: UnsafeMutablePointer<CMTime>) -> CVPixelBuffer? ``` |

Modified [AVPlayerItemVideoOutput.delegate](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1385827-delegate)

|  | Declaration |
| --- | --- |
| From | ``` var delegate: AVPlayerItemOutputPullDelegate! { get } ``` |
| To | ``` unowned(unsafe) var delegate: AVPlayerItemOutputPullDelegate? { get } ``` |

Modified [AVPlayerItemVideoOutput.delegateQueue](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1388108-delegatequeue)

|  | Declaration |
| --- | --- |
| From | ``` var delegateQueue: dispatch_queue_t! { get } ``` |
| To | ``` var delegateQueue: dispatch_queue_t? { get } ``` |

Modified [AVPlayerItemVideoOutput.init(pixelBufferAttributes: [String : AnyObject]?)](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1389231-initwithpixelbufferattributes)

|  | Declaration |
| --- | --- |
| From | ``` init!(pixelBufferAttributes pixelBufferAttributes: [NSObject : AnyObject]!) ``` |
| To | ``` init(pixelBufferAttributes pixelBufferAttributes: [String : AnyObject]?) ``` |

Modified [AVPlayerItemVideoOutput.setDelegate(_: AVPlayerItemOutputPullDelegate?, queue: dispatch_queue_t?)](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1386824-setdelegate)

|  | Declaration |
| --- | --- |
| From | ``` func setDelegate(_ delegate: AVPlayerItemOutputPullDelegate!, queue delegateQueue: dispatch_queue_t!) ``` |
| To | ``` func setDelegate(_ delegate: AVPlayerItemOutputPullDelegate?, queue delegateQueue: dispatch_queue_t?) ``` |

Modified [AVPlayerLayer](https://developer.apple.com/documentation/avfoundation/avplayerlayer)

|  | Declaration |
| --- | --- |
| From | ``` class AVPlayerLayer : CALayer {     init!(player player: AVPlayer!) -> AVPlayerLayer     class func playerLayerWithPlayer(_ player: AVPlayer!) -> AVPlayerLayer!     var player: AVPlayer!     var videoGravity: String!     var readyForDisplay: Bool { get }     var videoRect: CGRect { get } } ``` |
| To | ``` class AVPlayerLayer : CALayer {      init(player player: AVPlayer?)     class func playerLayerWithPlayer(_ player: AVPlayer?) -> AVPlayerLayer     var player: AVPlayer?     var videoGravity: String     var readyForDisplay: Bool { get }     var videoRect: CGRect { get }     var pixelBufferAttributes: [String : AnyObject]? } ``` |

Modified [AVPlayerLayer.init(player: AVPlayer?)](https://developer.apple.com/documentation/avfoundation/avplayerlayer/1389308-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(player player: AVPlayer!) -> AVPlayerLayer ``` |
| To | ``` init(player player: AVPlayer?) ``` |

Modified [AVPlayerLayer.player](https://developer.apple.com/documentation/avfoundation/avplayerlayer/1390434-player)

|  | Declaration |
| --- | --- |
| From | ``` var player: AVPlayer! ``` |
| To | ``` var player: AVPlayer? ``` |

Modified [AVPlayerLayer.videoGravity](https://developer.apple.com/documentation/avfoundation/avplayerlayer/1388915-videogravity)

|  | Declaration |
| --- | --- |
| From | ``` var videoGravity: String! ``` |
| To | ``` var videoGravity: String ``` |

Modified [AVPlayerMediaSelectionCriteria](https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria)

|  | Declaration |
| --- | --- |
| From | ``` class AVPlayerMediaSelectionCriteria : NSObject {     var preferredLanguages: [AnyObject]! { get }     var preferredMediaCharacteristics: [AnyObject]! { get }     init!(preferredLanguages preferredLanguages: [AnyObject]!, preferredMediaCharacteristics preferredMediaCharacteristics: [AnyObject]!) } ``` |
| To | ``` class AVPlayerMediaSelectionCriteria : NSObject {     var preferredLanguages: [String]? { get }     var preferredMediaCharacteristics: [String]? { get }     init(preferredLanguages preferredLanguages: [String]?, preferredMediaCharacteristics preferredMediaCharacteristics: [String]?) } ``` |

Modified [AVPlayerMediaSelectionCriteria.init(preferredLanguages: [String]?, preferredMediaCharacteristics: [String]?)](https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria/1387627-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(preferredLanguages preferredLanguages: [AnyObject]!, preferredMediaCharacteristics preferredMediaCharacteristics: [AnyObject]!) ``` |
| To | ``` init(preferredLanguages preferredLanguages: [String]?, preferredMediaCharacteristics preferredMediaCharacteristics: [String]?) ``` |

Modified [AVPlayerMediaSelectionCriteria.preferredLanguages](https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria/1388559-preferredlanguages)

|  | Declaration |
| --- | --- |
| From | ``` var preferredLanguages: [AnyObject]! { get } ``` |
| To | ``` var preferredLanguages: [String]? { get } ``` |

Modified [AVPlayerMediaSelectionCriteria.preferredMediaCharacteristics](https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria/1385734-preferredmediacharacteristics)

|  | Declaration |
| --- | --- |
| From | ``` var preferredMediaCharacteristics: [AnyObject]! { get } ``` |
| To | ``` var preferredMediaCharacteristics: [String]? { get } ``` |

Modified [AVPlayerStatus [enum]](https://developer.apple.com/documentation/avfoundation/avplayer/status)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVQueuedSampleBufferRenderingStatus [enum]](https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrenderingstatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVQueuePlayer](https://developer.apple.com/documentation/avfoundation/avqueueplayer)

|  | Declaration |
| --- | --- |
| From | ``` class AVQueuePlayer : AVPlayer {     class func queuePlayerWithItems(_ items: [AnyObject]!) -> AnyObject!     init!(items items: [AnyObject]!)     func items() -> [AnyObject]!     func advanceToNextItem()     func canInsertItem(_ item: AVPlayerItem!, afterItem afterItem: AVPlayerItem!) -> Bool     func insertItem(_ item: AVPlayerItem!, afterItem afterItem: AVPlayerItem!)     func removeItem(_ item: AVPlayerItem!)     func removeAllItems() } ``` |
| To | ``` class AVQueuePlayer : AVPlayer {     convenience init(items items: [AVPlayerItem])     class func queuePlayerWithItems(_ items: [AVPlayerItem]) -> Self     init(items items: [AVPlayerItem])     func items() -> [AVPlayerItem]     func advanceToNextItem()     func canInsertItem(_ item: AVPlayerItem, afterItem afterItem: AVPlayerItem?) -> Bool     func insertItem(_ item: AVPlayerItem, afterItem afterItem: AVPlayerItem?)     func removeItem(_ item: AVPlayerItem)     func removeAllItems() } ``` |

Modified [AVQueuePlayer.canInsertItem(_: AVPlayerItem, afterItem: AVPlayerItem?) -> Bool](https://developer.apple.com/documentation/avfoundation/avqueueplayer/1387289-caninsert)

|  | Declaration |
| --- | --- |
| From | ``` func canInsertItem(_ item: AVPlayerItem!, afterItem afterItem: AVPlayerItem!) -> Bool ``` |
| To | ``` func canInsertItem(_ item: AVPlayerItem, afterItem afterItem: AVPlayerItem?) -> Bool ``` |

Modified [AVQueuePlayer.init(items: [AVPlayerItem])](https://developer.apple.com/documentation/avfoundation/avqueueplayer/1389345-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(items items: [AnyObject]!) ``` |
| To | ``` init(items items: [AVPlayerItem]) ``` |

Modified [AVQueuePlayer.insertItem(_: AVPlayerItem, afterItem: AVPlayerItem?)](https://developer.apple.com/documentation/avfoundation/avqueueplayer/1388543-insert)

|  | Declaration |
| --- | --- |
| From | ``` func insertItem(_ item: AVPlayerItem!, afterItem afterItem: AVPlayerItem!) ``` |
| To | ``` func insertItem(_ item: AVPlayerItem, afterItem afterItem: AVPlayerItem?) ``` |

Modified [AVQueuePlayer.items() -> [AVPlayerItem]](https://developer.apple.com/documentation/avfoundation/avqueueplayer/1390539-items)

|  | Declaration |
| --- | --- |
| From | ``` func items() -> [AnyObject]! ``` |
| To | ``` func items() -> [AVPlayerItem] ``` |

Modified [AVQueuePlayer.removeItem(_: AVPlayerItem)](https://developer.apple.com/documentation/avfoundation/avqueueplayer/1387400-remove)

|  | Declaration |
| --- | --- |
| From | ``` func removeItem(_ item: AVPlayerItem!) ``` |
| To | ``` func removeItem(_ item: AVPlayerItem) ``` |

Modified [AVSampleBufferDisplayLayer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer)

|  | Declaration |
| --- | --- |
| From | ``` class AVSampleBufferDisplayLayer : CALayer {     var controlTimebase: CMTimebase!     var videoGravity: String!     var status: AVQueuedSampleBufferRenderingStatus { get }     var error: NSError! { get } } extension AVSampleBufferDisplayLayer {     func enqueueSampleBuffer(_ sampleBuffer: CMSampleBuffer!)     func flush()     func flushAndRemoveImage()     var readyForMoreMediaData: Bool { get }     func requestMediaDataWhenReadyOnQueue(_ queue: dispatch_queue_t!, usingBlock block: (() -> Void)!)     func stopRequestingMediaData() } ``` |
| To | ``` class AVSampleBufferDisplayLayer : CALayer {     var controlTimebase: CMTimebase?     var videoGravity: String     var status: AVQueuedSampleBufferRenderingStatus { get }     var error: NSError? { get } } extension AVSampleBufferDisplayLayer {     func enqueueSampleBuffer(_ sampleBuffer: CMSampleBuffer)     func flush()     func flushAndRemoveImage()     var readyForMoreMediaData: Bool { get }     func requestMediaDataWhenReadyOnQueue(_ queue: dispatch_queue_t, usingBlock block: () -> Void)     func stopRequestingMediaData() } ``` |

Modified [AVSampleBufferDisplayLayer.controlTimebase](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/1390569-controltimebase)

|  | Declaration |
| --- | --- |
| From | ``` var controlTimebase: CMTimebase! ``` |
| To | ``` var controlTimebase: CMTimebase? ``` |

Modified [AVSampleBufferDisplayLayer.enqueueSampleBuffer(_: CMSampleBuffer)](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/1387599-enqueue)

|  | Declaration |
| --- | --- |
| From | ``` func enqueueSampleBuffer(_ sampleBuffer: CMSampleBuffer!) ``` |
| To | ``` func enqueueSampleBuffer(_ sampleBuffer: CMSampleBuffer) ``` |

Modified [AVSampleBufferDisplayLayer.error](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/1390739-error)

|  | Declaration |
| --- | --- |
| From | ``` var error: NSError! { get } ``` |
| To | ``` var error: NSError? { get } ``` |

Modified [AVSampleBufferDisplayLayer.requestMediaDataWhenReadyOnQueue(_: dispatch_queue_t, usingBlock: () -> Void)](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/1387778-requestmediadatawhenready)

|  | Declaration |
| --- | --- |
| From | ``` func requestMediaDataWhenReadyOnQueue(_ queue: dispatch_queue_t!, usingBlock block: (() -> Void)!) ``` |
| To | ``` func requestMediaDataWhenReadyOnQueue(_ queue: dispatch_queue_t, usingBlock block: () -> Void) ``` |

Modified [AVSampleBufferDisplayLayer.videoGravity](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/1387625-videogravity)

|  | Declaration |
| --- | --- |
| From | ``` var videoGravity: String! ``` |
| To | ``` var videoGravity: String ``` |

Modified [AVSpeechBoundary [enum]](https://developer.apple.com/documentation/avfoundation/avspeechboundary)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [AVSpeechSynthesisVoice](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice)

|  | Declaration |
| --- | --- |
| From | ``` class AVSpeechSynthesisVoice : NSObject, NSSecureCoding, NSCoding {     class func speechVoices() -> [AnyObject]!     class func currentLanguageCode() -> String!     init!(language language: String!) -> AVSpeechSynthesisVoice     class func voiceWithLanguage(_ language: String!) -> AVSpeechSynthesisVoice!     var language: String! { get } } ``` |
| To | ``` class AVSpeechSynthesisVoice : NSObject, NSSecureCoding, NSCoding {     class func speechVoices() -> [AVSpeechSynthesisVoice]     class func currentLanguageCode() -> String      init?(language languageCode: String?)     class func voiceWithLanguage(_ languageCode: String?) -> AVSpeechSynthesisVoice?      init?(identifier identifier: String)     class func voiceWithIdentifier(_ identifier: String) -> AVSpeechSynthesisVoice?     var language: String { get }     var identifier: String { get }     var name: String { get }     var quality: AVSpeechSynthesisVoiceQuality { get } } ``` |

Modified [AVSpeechSynthesisVoice.currentLanguageCode() -> String [class]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619707-currentlanguagecode)

|  | Declaration |
| --- | --- |
| From | ``` class func currentLanguageCode() -> String! ``` |
| To | ``` class func currentLanguageCode() -> String ``` |

Modified [AVSpeechSynthesisVoice.init(language: String?)](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619699-voicewithlanguage)

|  | Declaration |
| --- | --- |
| From | ``` init!(language language: String!) -> AVSpeechSynthesisVoice ``` |
| To | ``` init?(language languageCode: String?) ``` |

Modified [AVSpeechSynthesisVoice.language](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619698-language)

|  | Declaration |
| --- | --- |
| From | ``` var language: String! { get } ``` |
| To | ``` var language: String { get } ``` |

Modified [AVSpeechSynthesisVoice.speechVoices() -> [AVSpeechSynthesisVoice] [class]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619697-speechvoices)

|  | Declaration |
| --- | --- |
| From | ``` class func speechVoices() -> [AnyObject]! ``` |
| To | ``` class func speechVoices() -> [AVSpeechSynthesisVoice] ``` |

Modified [AVSpeechSynthesizer](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer)

|  | Declaration |
| --- | --- |
| From | ``` class AVSpeechSynthesizer : NSObject {     unowned(unsafe) var delegate: AVSpeechSynthesizerDelegate!     var speaking: Bool { get }     var paused: Bool { get }     func speakUtterance(_ utterance: AVSpeechUtterance!)     func stopSpeakingAtBoundary(_ boundary: AVSpeechBoundary) -> Bool     func pauseSpeakingAtBoundary(_ boundary: AVSpeechBoundary) -> Bool     func continueSpeaking() -> Bool } ``` |
| To | ``` class AVSpeechSynthesizer : NSObject {     unowned(unsafe) var delegate: AVSpeechSynthesizerDelegate?     var speaking: Bool { get }     var paused: Bool { get }     func speakUtterance(_ utterance: AVSpeechUtterance)     func stopSpeakingAtBoundary(_ boundary: AVSpeechBoundary) -> Bool     func pauseSpeakingAtBoundary(_ boundary: AVSpeechBoundary) -> Bool     func continueSpeaking() -> Bool } ``` |

Modified [AVSpeechSynthesizer.delegate](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619709-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: AVSpeechSynthesizerDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: AVSpeechSynthesizerDelegate? ``` |

Modified [AVSpeechSynthesizer.speakUtterance(_: AVSpeechUtterance)](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619686-speak)

|  | Declaration |
| --- | --- |
| From | ``` func speakUtterance(_ utterance: AVSpeechUtterance!) ``` |
| To | ``` func speakUtterance(_ utterance: AVSpeechUtterance) ``` |

Modified [AVSpeechSynthesizerDelegate](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVSpeechSynthesizerDelegate : NSObjectProtocol {     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer!, didStartSpeechUtterance utterance: AVSpeechUtterance!)     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer!, didFinishSpeechUtterance utterance: AVSpeechUtterance!)     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer!, didPauseSpeechUtterance utterance: AVSpeechUtterance!)     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer!, didContinueSpeechUtterance utterance: AVSpeechUtterance!)     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer!, didCancelSpeechUtterance utterance: AVSpeechUtterance!)     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer!, willSpeakRangeOfSpeechString characterRange: NSRange, utterance utterance: AVSpeechUtterance!) } ``` |
| To | ``` protocol AVSpeechSynthesizerDelegate : NSObjectProtocol {     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didStartSpeechUtterance utterance: AVSpeechUtterance)     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didFinishSpeechUtterance utterance: AVSpeechUtterance)     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didPauseSpeechUtterance utterance: AVSpeechUtterance)     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didContinueSpeechUtterance utterance: AVSpeechUtterance)     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didCancelSpeechUtterance utterance: AVSpeechUtterance)     optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, willSpeakRangeOfSpeechString characterRange: NSRange, utterance utterance: AVSpeechUtterance) } ``` |

Modified [AVSpeechSynthesizerDelegate.speechSynthesizer(_: AVSpeechSynthesizer, didCancelSpeechUtterance: AVSpeechUtterance)](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619678-speechsynthesizer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer!, didCancelSpeechUtterance utterance: AVSpeechUtterance!) ``` | iOS 8.0 |
| To | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didCancelSpeechUtterance utterance: AVSpeechUtterance) ``` | iOS 7.0 |

Modified [AVSpeechSynthesizerDelegate.speechSynthesizer(_: AVSpeechSynthesizer, didContinueSpeechUtterance: AVSpeechUtterance)](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619677-speechsynthesizer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer!, didContinueSpeechUtterance utterance: AVSpeechUtterance!) ``` | iOS 8.0 |
| To | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didContinueSpeechUtterance utterance: AVSpeechUtterance) ``` | iOS 7.0 |

Modified [AVSpeechSynthesizerDelegate.speechSynthesizer(_: AVSpeechSynthesizer, didFinishSpeechUtterance: AVSpeechUtterance)](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619700-speechsynthesizer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer!, didFinishSpeechUtterance utterance: AVSpeechUtterance!) ``` | iOS 8.0 |
| To | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didFinishSpeechUtterance utterance: AVSpeechUtterance) ``` | iOS 7.0 |

Modified [AVSpeechSynthesizerDelegate.speechSynthesizer(_: AVSpeechSynthesizer, didPauseSpeechUtterance: AVSpeechUtterance)](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619675-speechsynthesizer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer!, didPauseSpeechUtterance utterance: AVSpeechUtterance!) ``` | iOS 8.0 |
| To | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didPauseSpeechUtterance utterance: AVSpeechUtterance) ``` | iOS 7.0 |

Modified [AVSpeechSynthesizerDelegate.speechSynthesizer(_: AVSpeechSynthesizer, didStartSpeechUtterance: AVSpeechUtterance)](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619701-speechsynthesizer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer!, didStartSpeechUtterance utterance: AVSpeechUtterance!) ``` | iOS 8.0 |
| To | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didStartSpeechUtterance utterance: AVSpeechUtterance) ``` | iOS 7.0 |

Modified [AVSpeechSynthesizerDelegate.speechSynthesizer(_: AVSpeechSynthesizer, willSpeakRangeOfSpeechString: NSRange, utterance: AVSpeechUtterance)](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619681-speechsynthesizer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer!, willSpeakRangeOfSpeechString characterRange: NSRange, utterance utterance: AVSpeechUtterance!) ``` | iOS 8.0 |
| To | ``` optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, willSpeakRangeOfSpeechString characterRange: NSRange, utterance utterance: AVSpeechUtterance) ``` | iOS 7.0 |

Modified [AVSpeechUtterance](https://developer.apple.com/documentation/avfoundation/avspeechutterance)

|  | Declaration |
| --- | --- |
| From | ``` class AVSpeechUtterance : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init!(string string: String!)     class func speechUtteranceWithString(_ string: String!) -> Self!     init!(string string: String!)     var voice: AVSpeechSynthesisVoice!     var speechString: String! { get }     var rate: Float     var pitchMultiplier: Float     var volume: Float     var preUtteranceDelay: NSTimeInterval     var postUtteranceDelay: NSTimeInterval } ``` |
| To | ``` class AVSpeechUtterance : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init(string string: String)     class func speechUtteranceWithString(_ string: String) -> Self     init(string string: String)     var voice: AVSpeechSynthesisVoice?     var speechString: String { get }     var rate: Float     var pitchMultiplier: Float     var volume: Float     var preUtteranceDelay: NSTimeInterval     var postUtteranceDelay: NSTimeInterval } ``` |

Modified [AVSpeechUtterance.init(string: String)](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619684-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(string string: String!) ``` |
| To | ``` init(string string: String) ``` |

Modified [AVSpeechUtterance.speechString](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619702-speechstring)

|  | Declaration |
| --- | --- |
| From | ``` var speechString: String! { get } ``` |
| To | ``` var speechString: String { get } ``` |

Modified [AVSpeechUtterance.voice](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619710-voice)

|  | Declaration |
| --- | --- |
| From | ``` var voice: AVSpeechSynthesisVoice! ``` |
| To | ``` var voice: AVSpeechSynthesisVoice? ``` |

Modified [AVSynchronizedLayer](https://developer.apple.com/documentation/avfoundation/avsynchronizedlayer)

|  | Declaration |
| --- | --- |
| From | ``` class AVSynchronizedLayer : CALayer {     init!(playerItem playerItem: AVPlayerItem!) -> AVSynchronizedLayer     class func synchronizedLayerWithPlayerItem(_ playerItem: AVPlayerItem!) -> AVSynchronizedLayer!     var playerItem: AVPlayerItem! } ``` |
| To | ``` class AVSynchronizedLayer : CALayer {      init(playerItem playerItem: AVPlayerItem)     class func synchronizedLayerWithPlayerItem(_ playerItem: AVPlayerItem) -> AVSynchronizedLayer     var playerItem: AVPlayerItem? } ``` |

Modified [AVSynchronizedLayer.init(playerItem: AVPlayerItem)](https://developer.apple.com/documentation/avfoundation/avsynchronizedlayer/1388781-synchronizedlayerwithplayeritem)

|  | Declaration |
| --- | --- |
| From | ``` init!(playerItem playerItem: AVPlayerItem!) -> AVSynchronizedLayer ``` |
| To | ``` init(playerItem playerItem: AVPlayerItem) ``` |

Modified [AVSynchronizedLayer.playerItem](https://developer.apple.com/documentation/avfoundation/avsynchronizedlayer/1385679-playeritem)

|  | Declaration |
| --- | --- |
| From | ``` var playerItem: AVPlayerItem! ``` |
| To | ``` var playerItem: AVPlayerItem? ``` |

Modified [AVTextStyleRule](https://developer.apple.com/documentation/avfoundation/avtextstylerule)

|  | Declaration |
| --- | --- |
| From | ``` class AVTextStyleRule : NSObject, NSCopying {     class func propertyListForTextStyleRules(_ textStyleRules: [AnyObject]!) -> AnyObject!     class func textStyleRulesFromPropertyList(_ plist: AnyObject!) -> [AnyObject]!     init!(textMarkupAttributes textMarkupAttributes: [NSObject : AnyObject]!) -> AVTextStyleRule     class func textStyleRuleWithTextMarkupAttributes(_ textMarkupAttributes: [NSObject : AnyObject]!) -> AVTextStyleRule!     init!(textMarkupAttributes textMarkupAttributes: [NSObject : AnyObject]!, textSelector textSelector: String!) -> AVTextStyleRule     class func textStyleRuleWithTextMarkupAttributes(_ textMarkupAttributes: [NSObject : AnyObject]!, textSelector textSelector: String!) -> AVTextStyleRule!     init!(textMarkupAttributes textMarkupAttributes: [NSObject : AnyObject]!)     init!(textMarkupAttributes textMarkupAttributes: [NSObject : AnyObject]!, textSelector textSelector: String!)     var textMarkupAttributes: [NSObject : AnyObject]! { get }     var textSelector: String! { get } } ``` |
| To | ``` class AVTextStyleRule : NSObject, NSCopying {     convenience init()     class func propertyListForTextStyleRules(_ textStyleRules: [AVTextStyleRule]) -> AnyObject     class func textStyleRulesFromPropertyList(_ plist: AnyObject) -> [AVTextStyleRule]?      init?(textMarkupAttributes textMarkupAttributes: [String : AnyObject])     class func textStyleRuleWithTextMarkupAttributes(_ textMarkupAttributes: [String : AnyObject]) -> AVTextStyleRule?      init?(textMarkupAttributes textMarkupAttributes: [String : AnyObject], textSelector textSelector: String?)     class func textStyleRuleWithTextMarkupAttributes(_ textMarkupAttributes: [String : AnyObject], textSelector textSelector: String?) -> AVTextStyleRule?     convenience init?(textMarkupAttributes textMarkupAttributes: [String : AnyObject])     init?(textMarkupAttributes textMarkupAttributes: [String : AnyObject], textSelector textSelector: String?)     var textMarkupAttributes: [String : AnyObject] { get }     var textSelector: String? { get } } ``` |

Modified [AVTextStyleRule.init(textMarkupAttributes: [String : AnyObject])](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1385849-initwithtextmarkupattributes)

|  | Declaration |
| --- | --- |
| From | ``` init!(textMarkupAttributes textMarkupAttributes: [NSObject : AnyObject]!) ``` |
| To | ``` convenience init?(textMarkupAttributes textMarkupAttributes: [String : AnyObject]) ``` |

Modified [AVTextStyleRule.init(textMarkupAttributes: [String : AnyObject], textSelector: String?)](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1389854-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(textMarkupAttributes textMarkupAttributes: [NSObject : AnyObject]!, textSelector textSelector: String!) ``` |
| To | ``` init?(textMarkupAttributes textMarkupAttributes: [String : AnyObject], textSelector textSelector: String?) ``` |

Modified [AVTextStyleRule.propertyListForTextStyleRules(_: [AVTextStyleRule]) -> AnyObject [class]](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1387970-propertylistfortextstylerules)

|  | Declaration |
| --- | --- |
| From | ``` class func propertyListForTextStyleRules(_ textStyleRules: [AnyObject]!) -> AnyObject! ``` |
| To | ``` class func propertyListForTextStyleRules(_ textStyleRules: [AVTextStyleRule]) -> AnyObject ``` |

Modified [AVTextStyleRule.textMarkupAttributes](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1387945-textmarkupattributes)

|  | Declaration |
| --- | --- |
| From | ``` var textMarkupAttributes: [NSObject : AnyObject]! { get } ``` |
| To | ``` var textMarkupAttributes: [String : AnyObject] { get } ``` |

Modified [AVTextStyleRule.textSelector](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1389451-textselector)

|  | Declaration |
| --- | --- |
| From | ``` var textSelector: String! { get } ``` |
| To | ``` var textSelector: String? { get } ``` |

Modified [AVTextStyleRule.textStyleRulesFromPropertyList(_: AnyObject) -> [AVTextStyleRule]? [class]](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1387802-textstylerules)

|  | Declaration |
| --- | --- |
| From | ``` class func textStyleRulesFromPropertyList(_ plist: AnyObject!) -> [AnyObject]! ``` |
| To | ``` class func textStyleRulesFromPropertyList(_ plist: AnyObject) -> [AVTextStyleRule]? ``` |

Modified [AVTimedMetadataGroup](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup)

|  | Declaration | Superclasses | Protocols |
| --- | --- | --- | --- |
| From | ``` class AVTimedMetadataGroup : NSObject, NSCopying {     init!(items items: [AnyObject]!, timeRange timeRange: CMTimeRange)     init!(sampleBuffer sampleBuffer: CMSampleBuffer!)     var timeRange: CMTimeRange { get }     var items: [AnyObject]! { get } } extension AVTimedMetadataGroup {     func copyFormatDescription() -> CMMetadataFormatDescription! } ``` | NSObject | AnyObject, NSCopying |
| To | ``` class AVTimedMetadataGroup : AVMetadataGroup, NSCopying, NSMutableCopying {     init(items items: [AVMetadataItem], timeRange timeRange: CMTimeRange)     init?(sampleBuffer sampleBuffer: CMSampleBuffer)     var timeRange: CMTimeRange { get }     var items: [AVMetadataItem] { get } } extension AVTimedMetadataGroup {     func copyFormatDescription() -> CMMetadataFormatDescription? } ``` | AVMetadataGroup | AnyObject, NSCopying, NSMutableCopying |

Modified [AVTimedMetadataGroup.copyFormatDescription() -> CMMetadataFormatDescription?](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/1389461-copyformatdescription)

|  | Declaration |
| --- | --- |
| From | ``` func copyFormatDescription() -> CMMetadataFormatDescription! ``` |
| To | ``` func copyFormatDescription() -> CMMetadataFormatDescription? ``` |

Modified [AVTimedMetadataGroup.init(items: [AVMetadataItem], timeRange: CMTimeRange)](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/1389632-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(items items: [AnyObject]!, timeRange timeRange: CMTimeRange) ``` |
| To | ``` init(items items: [AVMetadataItem], timeRange timeRange: CMTimeRange) ``` |

Modified [AVTimedMetadataGroup.init(sampleBuffer: CMSampleBuffer)](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/1387128-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(sampleBuffer sampleBuffer: CMSampleBuffer!) ``` |
| To | ``` init?(sampleBuffer sampleBuffer: CMSampleBuffer) ``` |

Modified [AVTimedMetadataGroup.items](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/1385928-items)

|  | Declaration |
| --- | --- |
| From | ``` var items: [AnyObject]! { get } ``` |
| To | ``` var items: [AVMetadataItem] { get } ``` |

Modified [AVURLAsset](https://developer.apple.com/documentation/avfoundation/avurlasset)

|  | Declaration |
| --- | --- |
| From | ``` class AVURLAsset : AVAsset {     class func audiovisualTypes() -> [AnyObject]!     class func audiovisualMIMETypes() -> [AnyObject]!     class func isPlayableExtendedMIMEType(_ extendedMIMEType: String!) -> Bool     init!(URL URL: NSURL!, options options: [NSObject : AnyObject]!) -> AVURLAsset     class func URLAssetWithURL(_ URL: NSURL!, options options: [NSObject : AnyObject]!) -> AVURLAsset!     init!(URL URL: NSURL!, options options: [NSObject : AnyObject]!)     @NSCopying var URL: NSURL! { get } } extension AVURLAsset {     var resourceLoader: AVAssetResourceLoader! { get } } extension AVURLAsset {     func compatibleTrackForCompositionTrack(_ compositionTrack: AVCompositionTrack!) -> AVAssetTrack! } ``` |
| To | ``` class AVURLAsset : AVAsset {     convenience init()     class func audiovisualTypes() -> [String]     class func audiovisualMIMETypes() -> [String]     class func isPlayableExtendedMIMEType(_ extendedMIMEType: String) -> Bool     convenience init(URL URL: NSURL, options options: [String : AnyObject]?)     class func URLAssetWithURL(_ URL: NSURL, options options: [String : AnyObject]?) -> Self     init(URL URL: NSURL, options options: [String : AnyObject]?)     @NSCopying var URL: NSURL { get } } extension AVURLAsset {     var resourceLoader: AVAssetResourceLoader { get } } extension AVURLAsset {     func compatibleTrackForCompositionTrack(_ compositionTrack: AVCompositionTrack) -> AVAssetTrack? } ``` |

Modified [AVURLAsset.audiovisualMIMETypes() -> [String] [class]](https://developer.apple.com/documentation/avfoundation/avurlasset/1390006-audiovisualmimetypes)

|  | Declaration |
| --- | --- |
| From | ``` class func audiovisualMIMETypes() -> [AnyObject]! ``` |
| To | ``` class func audiovisualMIMETypes() -> [String] ``` |

Modified [AVURLAsset.audiovisualTypes() -> [String] [class]](https://developer.apple.com/documentation/avfoundation/avurlasset/1386800-audiovisualtypes)

|  | Declaration |
| --- | --- |
| From | ``` class func audiovisualTypes() -> [AnyObject]! ``` |
| To | ``` class func audiovisualTypes() -> [String] ``` |

Modified [AVURLAsset.compatibleTrackForCompositionTrack(_: AVCompositionTrack) -> AVAssetTrack?](https://developer.apple.com/documentation/avfoundation/avurlasset/1389650-compatibletrack)

|  | Declaration |
| --- | --- |
| From | ``` func compatibleTrackForCompositionTrack(_ compositionTrack: AVCompositionTrack!) -> AVAssetTrack! ``` |
| To | ``` func compatibleTrackForCompositionTrack(_ compositionTrack: AVCompositionTrack) -> AVAssetTrack? ``` |

Modified [AVURLAsset.init(URL: NSURL, options: [String : AnyObject]?)](https://developer.apple.com/documentation/avfoundation/avurlasset/1385698-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(URL URL: NSURL!, options options: [NSObject : AnyObject]!) ``` |
| To | ``` init(URL URL: NSURL, options options: [String : AnyObject]?) ``` |

Modified [AVURLAsset.isPlayableExtendedMIMEType(_: String) -> Bool [class]](https://developer.apple.com/documentation/avfoundation/avurlasset/1387142-isplayableextendedmimetype)

|  | Declaration |
| --- | --- |
| From | ``` class func isPlayableExtendedMIMEType(_ extendedMIMEType: String!) -> Bool ``` |
| To | ``` class func isPlayableExtendedMIMEType(_ extendedMIMEType: String) -> Bool ``` |

Modified [AVURLAsset.resourceLoader](https://developer.apple.com/documentation/avfoundation/avurlasset/1389118-resourceloader)

|  | Declaration |
| --- | --- |
| From | ``` var resourceLoader: AVAssetResourceLoader! { get } ``` |
| To | ``` var resourceLoader: AVAssetResourceLoader { get } ``` |

Modified [AVURLAsset.URL](https://developer.apple.com/documentation/avfoundation/avurlasset/1388127-url)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var URL: NSURL! { get } ``` |
| To | ``` @NSCopying var URL: NSURL { get } ``` |

Modified [AVVideoCompositing](https://developer.apple.com/documentation/avfoundation/avvideocompositing)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVVideoCompositing : NSObjectProtocol {     var sourcePixelBufferAttributes: [NSObject : AnyObject]! { get }     var requiredPixelBufferAttributesForRenderContext: [NSObject : AnyObject]! { get }     func renderContextChanged(_ newRenderContext: AVVideoCompositionRenderContext!)     func startVideoCompositionRequest(_ asyncVideoCompositionRequest: AVAsynchronousVideoCompositionRequest!)     optional func cancelAllPendingVideoCompositionRequests() } ``` |
| To | ``` protocol AVVideoCompositing : NSObjectProtocol {     var sourcePixelBufferAttributes: [String : AnyObject]? { get }     var requiredPixelBufferAttributesForRenderContext: [String : AnyObject] { get }     func renderContextChanged(_ newRenderContext: AVVideoCompositionRenderContext)     func startVideoCompositionRequest(_ asyncVideoCompositionRequest: AVAsynchronousVideoCompositionRequest)     optional func cancelAllPendingVideoCompositionRequests() } ``` |

Modified [AVVideoCompositing.renderContextChanged(_: AVVideoCompositionRenderContext)](https://developer.apple.com/documentation/avfoundation/avvideocompositing/1390363-rendercontextchanged)

|  | Declaration |
| --- | --- |
| From | ``` func renderContextChanged(_ newRenderContext: AVVideoCompositionRenderContext!) ``` |
| To | ``` func renderContextChanged(_ newRenderContext: AVVideoCompositionRenderContext) ``` |

Modified [AVVideoCompositing.requiredPixelBufferAttributesForRenderContext](https://developer.apple.com/documentation/avfoundation/avvideocompositing/1386414-requiredpixelbufferattributesfor)

|  | Declaration |
| --- | --- |
| From | ``` var requiredPixelBufferAttributesForRenderContext: [NSObject : AnyObject]! { get } ``` |
| To | ``` var requiredPixelBufferAttributesForRenderContext: [String : AnyObject] { get } ``` |

Modified [AVVideoCompositing.sourcePixelBufferAttributes](https://developer.apple.com/documentation/avfoundation/avvideocompositing/1388610-sourcepixelbufferattributes)

|  | Declaration |
| --- | --- |
| From | ``` var sourcePixelBufferAttributes: [NSObject : AnyObject]! { get } ``` |
| To | ``` var sourcePixelBufferAttributes: [String : AnyObject]? { get } ``` |

Modified [AVVideoCompositing.startVideoCompositionRequest(_: AVAsynchronousVideoCompositionRequest)](https://developer.apple.com/documentation/avfoundation/avvideocompositing/1388894-startvideocompositionrequest)

|  | Declaration |
| --- | --- |
| From | ``` func startVideoCompositionRequest(_ asyncVideoCompositionRequest: AVAsynchronousVideoCompositionRequest!) ``` |
| To | ``` func startVideoCompositionRequest(_ asyncVideoCompositionRequest: AVAsynchronousVideoCompositionRequest) ``` |

Modified [AVVideoComposition](https://developer.apple.com/documentation/avfoundation/avvideocomposition)

|  | Declaration |
| --- | --- |
| From | ``` class AVVideoComposition : NSObject, NSCopying, NSMutableCopying {     init!(propertiesOfAsset asset: AVAsset!) -> AVVideoComposition     class func videoCompositionWithPropertiesOfAsset(_ asset: AVAsset!) -> AVVideoComposition!     var customVideoCompositorClass: AnyObject.Type! { get }     var frameDuration: CMTime { get }     var renderSize: CGSize { get }     var renderScale: Float { get }     var instructions: [AnyObject]! { get }     var animationTool: AVVideoCompositionCoreAnimationTool! { get } } extension AVVideoComposition {     func isValidForAsset(_ asset: AVAsset!, timeRange timeRange: CMTimeRange, validationDelegate validationDelegate: AVVideoCompositionValidationHandling!) -> Bool } ``` |
| To | ``` class AVVideoComposition : NSObject, NSCopying, NSMutableCopying {      init(propertiesOfAsset asset: AVAsset)     class func videoCompositionWithPropertiesOfAsset(_ asset: AVAsset) -> AVVideoComposition     var customVideoCompositorClass: AnyObject.Type? { get }     var frameDuration: CMTime { get }     var renderSize: CGSize { get }     var renderScale: Float { get }     var instructions: [AVVideoCompositionInstructionProtocol] { get }     var animationTool: AVVideoCompositionCoreAnimationTool? { get } } extension AVVideoComposition {      init(asset asset: AVAsset, applyingCIFiltersWithHandler applier: (AVAsynchronousCIImageFilteringRequest) -> Void)     class func videoCompositionWithAsset(_ asset: AVAsset, applyingCIFiltersWithHandler applier: (AVAsynchronousCIImageFilteringRequest) -> Void) -> AVVideoComposition } extension AVVideoComposition {     func isValidForAsset(_ asset: AVAsset?, timeRange timeRange: CMTimeRange, validationDelegate validationDelegate: AVVideoCompositionValidationHandling?) -> Bool } ``` |

Modified [AVVideoComposition.animationTool](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1387030-animationtool)

|  | Declaration |
| --- | --- |
| From | ``` var animationTool: AVVideoCompositionCoreAnimationTool! { get } ``` |
| To | ``` var animationTool: AVVideoCompositionCoreAnimationTool? { get } ``` |

Modified [AVVideoComposition.customVideoCompositorClass](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1389622-customvideocompositorclass)

|  | Declaration |
| --- | --- |
| From | ``` var customVideoCompositorClass: AnyObject.Type! { get } ``` |
| To | ``` var customVideoCompositorClass: AnyObject.Type? { get } ``` |

Modified [AVVideoComposition.init(propertiesOfAsset: AVAsset)](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1385892-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(propertiesOfAsset asset: AVAsset!) -> AVVideoComposition ``` |
| To | ``` init(propertiesOfAsset asset: AVAsset) ``` |

Modified [AVVideoComposition.instructions](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1389211-instructions)

|  | Declaration |
| --- | --- |
| From | ``` var instructions: [AnyObject]! { get } ``` |
| To | ``` var instructions: [AVVideoCompositionInstructionProtocol] { get } ``` |

Modified [AVVideoComposition.isValidForAsset(_: AVAsset?, timeRange: CMTimeRange, validationDelegate: AVVideoCompositionValidationHandling?) -> Bool](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1389917-isvalidforasset)

|  | Declaration |
| --- | --- |
| From | ``` func isValidForAsset(_ asset: AVAsset!, timeRange timeRange: CMTimeRange, validationDelegate validationDelegate: AVVideoCompositionValidationHandling!) -> Bool ``` |
| To | ``` func isValidForAsset(_ asset: AVAsset?, timeRange timeRange: CMTimeRange, validationDelegate validationDelegate: AVVideoCompositionValidationHandling?) -> Bool ``` |

Modified [AVVideoCompositionCoreAnimationTool](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool)

|  | Declaration |
| --- | --- |
| From | ``` class AVVideoCompositionCoreAnimationTool : NSObject {     init!(additionalLayer layer: CALayer!, asTrackID trackID: CMPersistentTrackID) -> AVVideoCompositionCoreAnimationTool     class func videoCompositionCoreAnimationToolWithAdditionalLayer(_ layer: CALayer!, asTrackID trackID: CMPersistentTrackID) -> AVVideoCompositionCoreAnimationTool!     init!(postProcessingAsVideoLayer videoLayer: CALayer!, inLayer animationLayer: CALayer!) -> AVVideoCompositionCoreAnimationTool     class func videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayer(_ videoLayer: CALayer!, inLayer animationLayer: CALayer!) -> AVVideoCompositionCoreAnimationTool!     init!(postProcessingAsVideoLayers videoLayers: [AnyObject]!, inLayer animationLayer: CALayer!) -> AVVideoCompositionCoreAnimationTool     class func videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayers(_ videoLayers: [AnyObject]!, inLayer animationLayer: CALayer!) -> AVVideoCompositionCoreAnimationTool! } ``` |
| To | ``` class AVVideoCompositionCoreAnimationTool : NSObject {     convenience init(additionalLayer layer: CALayer, asTrackID trackID: CMPersistentTrackID)     class func videoCompositionCoreAnimationToolWithAdditionalLayer(_ layer: CALayer, asTrackID trackID: CMPersistentTrackID) -> Self     convenience init(postProcessingAsVideoLayer videoLayer: CALayer, inLayer animationLayer: CALayer)     class func videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayer(_ videoLayer: CALayer, inLayer animationLayer: CALayer) -> Self     convenience init(postProcessingAsVideoLayers videoLayers: [CALayer], inLayer animationLayer: CALayer)     class func videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayers(_ videoLayers: [CALayer], inLayer animationLayer: CALayer) -> Self } ``` |

Modified [AVVideoCompositionCoreAnimationTool.init(additionalLayer: CALayer, asTrackID: CMPersistentTrackID)](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/1388345-videocompositioncoreanimationtoo)

|  | Declaration |
| --- | --- |
| From | ``` init!(additionalLayer layer: CALayer!, asTrackID trackID: CMPersistentTrackID) -> AVVideoCompositionCoreAnimationTool ``` |
| To | ``` convenience init(additionalLayer layer: CALayer, asTrackID trackID: CMPersistentTrackID) ``` |

Modified [AVVideoCompositionCoreAnimationTool.init(postProcessingAsVideoLayer: CALayer, inLayer: CALayer)](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/1389594-videocompositioncoreanimationtoo)

|  | Declaration |
| --- | --- |
| From | ``` init!(postProcessingAsVideoLayer videoLayer: CALayer!, inLayer animationLayer: CALayer!) -> AVVideoCompositionCoreAnimationTool ``` |
| To | ``` convenience init(postProcessingAsVideoLayer videoLayer: CALayer, inLayer animationLayer: CALayer) ``` |

Modified [AVVideoCompositionCoreAnimationTool.init(postProcessingAsVideoLayers: [CALayer], inLayer: CALayer)](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/1389778-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(postProcessingAsVideoLayers videoLayers: [AnyObject]!, inLayer animationLayer: CALayer!) -> AVVideoCompositionCoreAnimationTool ``` |
| To | ``` convenience init(postProcessingAsVideoLayers videoLayers: [CALayer], inLayer animationLayer: CALayer) ``` |

Modified [AVVideoCompositionInstruction](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction)

|  | Declaration |
| --- | --- |
| From | ``` class AVVideoCompositionInstruction : NSObject, NSSecureCoding, NSCoding, NSCopying, NSMutableCopying, AVVideoCompositionInstructionProtocol, NSObjectProtocol {     var timeRange: CMTimeRange { get }     var backgroundColor: CGColor!     var layerInstructions: [AnyObject]! { get }     var enablePostProcessing: Bool { get }     var requiredSourceTrackIDs: [AnyObject]! { get }     var passthroughTrackID: CMPersistentTrackID { get } } ``` |
| To | ``` class AVVideoCompositionInstruction : NSObject, NSSecureCoding, NSCoding, NSCopying, NSMutableCopying, AVVideoCompositionInstructionProtocol {     var timeRange: CMTimeRange { get }     var backgroundColor: CGColor? { get }     var layerInstructions: [AVVideoCompositionLayerInstruction] { get }     var enablePostProcessing: Bool { get }     var requiredSourceTrackIDs: [NSValue] { get }     var passthroughTrackID: CMPersistentTrackID { get } } ``` |

Modified [AVVideoCompositionInstruction.backgroundColor](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction/1389384-backgroundcolor)

|  | Declaration |
| --- | --- |
| From | ``` var backgroundColor: CGColor! ``` |
| To | ``` var backgroundColor: CGColor? { get } ``` |

Modified [AVVideoCompositionInstruction.layerInstructions](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction/1389689-layerinstructions)

|  | Declaration |
| --- | --- |
| From | ``` var layerInstructions: [AnyObject]! { get } ``` |
| To | ``` var layerInstructions: [AVVideoCompositionLayerInstruction] { get } ``` |

Modified [AVVideoCompositionInstruction.requiredSourceTrackIDs](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction/1390913-requiredsourcetrackids)

|  | Declaration |
| --- | --- |
| From | ``` var requiredSourceTrackIDs: [AnyObject]! { get } ``` |
| To | ``` var requiredSourceTrackIDs: [NSValue] { get } ``` |

Modified [AVVideoCompositionInstructionProtocol](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstructionprotocol)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVVideoCompositionInstructionProtocol : NSObjectProtocol {     var timeRange: CMTimeRange { get }     var enablePostProcessing: Bool { get }     var containsTweening: Bool { get }     var requiredSourceTrackIDs: [AnyObject]! { get }     var passthroughTrackID: CMPersistentTrackID { get } } ``` |
| To | ``` protocol AVVideoCompositionInstructionProtocol : NSObjectProtocol {     var timeRange: CMTimeRange { get }     var enablePostProcessing: Bool { get }     var containsTweening: Bool { get }     var requiredSourceTrackIDs: [NSValue]? { get }     var passthroughTrackID: CMPersistentTrackID { get } } ``` |

Modified [AVVideoCompositionInstructionProtocol.requiredSourceTrackIDs](https://developer.apple.com/documentation/avfoundation/1386654-avvideocompositioninstruction/1388661-requiredsourcetrackids)

|  | Declaration |
| --- | --- |
| From | ``` var requiredSourceTrackIDs: [AnyObject]! { get } ``` |
| To | ``` var requiredSourceTrackIDs: [NSValue]? { get } ``` |

Modified [AVVideoCompositionRenderContext](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext)

|  | Declaration |
| --- | --- |
| From | ``` class AVVideoCompositionRenderContext : NSObject {     var size: CGSize { get }     var renderTransform: CGAffineTransform { get }     var renderScale: Float { get }     var pixelAspectRatio: AVPixelAspectRatio { get }     var edgeWidths: AVEdgeWidths { get }     var highQualityRendering: Bool { get }     var videoComposition: AVVideoComposition! { get }     func newPixelBuffer() -> Unmanaged<CVPixelBuffer>! } ``` |
| To | ``` class AVVideoCompositionRenderContext : NSObject {     var size: CGSize { get }     var renderTransform: CGAffineTransform { get }     var renderScale: Float { get }     var pixelAspectRatio: AVPixelAspectRatio { get }     var edgeWidths: AVEdgeWidths { get }     var highQualityRendering: Bool { get }     var videoComposition: AVVideoComposition { get }     func newPixelBuffer() -> CVPixelBuffer? } ``` |

Modified [AVVideoCompositionRenderContext.newPixelBuffer() -> CVPixelBuffer?](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/1386802-newpixelbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func newPixelBuffer() -> Unmanaged<CVPixelBuffer>! ``` |
| To | ``` func newPixelBuffer() -> CVPixelBuffer? ``` |

Modified [AVVideoCompositionRenderContext.videoComposition](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/1390647-videocomposition)

|  | Declaration |
| --- | --- |
| From | ``` var videoComposition: AVVideoComposition! { get } ``` |
| To | ``` var videoComposition: AVVideoComposition { get } ``` |

Modified [AVVideoCompositionValidationHandling](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVVideoCompositionValidationHandling : NSObjectProtocol {     optional func videoComposition(_ videoComposition: AVVideoComposition!, shouldContinueValidatingAfterFindingInvalidValueForKey key: String!) -> Bool     optional func videoComposition(_ videoComposition: AVVideoComposition!, shouldContinueValidatingAfterFindingEmptyTimeRange timeRange: CMTimeRange) -> Bool     optional func videoComposition(_ videoComposition: AVVideoComposition!, shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction videoCompositionInstruction: AVVideoCompositionInstructionProtocol!) -> Bool     optional func videoComposition(_ videoComposition: AVVideoComposition!, shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction videoCompositionInstruction: AVVideoCompositionInstructionProtocol!, layerInstruction layerInstruction: AVVideoCompositionLayerInstruction!, asset asset: AVAsset!) -> Bool } ``` |
| To | ``` protocol AVVideoCompositionValidationHandling : NSObjectProtocol {     optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidValueForKey key: String) -> Bool     optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingEmptyTimeRange timeRange: CMTimeRange) -> Bool     optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction videoCompositionInstruction: AVVideoCompositionInstructionProtocol) -> Bool     optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction videoCompositionInstruction: AVVideoCompositionInstructionProtocol, layerInstruction layerInstruction: AVVideoCompositionLayerInstruction, asset asset: AVAsset) -> Bool } ``` |

Modified [AVVideoCompositionValidationHandling.videoComposition(_: AVVideoComposition, shouldContinueValidatingAfterFindingEmptyTimeRange: CMTimeRange) -> Bool](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/1388620-videocomposition)

|  | Declaration |
| --- | --- |
| From | ``` optional func videoComposition(_ videoComposition: AVVideoComposition!, shouldContinueValidatingAfterFindingEmptyTimeRange timeRange: CMTimeRange) -> Bool ``` |
| To | ``` optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingEmptyTimeRange timeRange: CMTimeRange) -> Bool ``` |

Modified [AVVideoCompositionValidationHandling.videoComposition(_: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction: AVVideoCompositionInstructionProtocol) -> Bool](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/1390721-videocomposition)

|  | Declaration |
| --- | --- |
| From | ``` optional func videoComposition(_ videoComposition: AVVideoComposition!, shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction videoCompositionInstruction: AVVideoCompositionInstructionProtocol!) -> Bool ``` |
| To | ``` optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction videoCompositionInstruction: AVVideoCompositionInstructionProtocol) -> Bool ``` |

Modified [AVVideoCompositionValidationHandling.videoComposition(_: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction: AVVideoCompositionInstructionProtocol, layerInstruction: AVVideoCompositionLayerInstruction, asset: AVAsset) -> Bool](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/1388452-videocomposition)

|  | Declaration |
| --- | --- |
| From | ``` optional func videoComposition(_ videoComposition: AVVideoComposition!, shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction videoCompositionInstruction: AVVideoCompositionInstructionProtocol!, layerInstruction layerInstruction: AVVideoCompositionLayerInstruction!, asset asset: AVAsset!) -> Bool ``` |
| To | ``` optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction videoCompositionInstruction: AVVideoCompositionInstructionProtocol, layerInstruction layerInstruction: AVVideoCompositionLayerInstruction, asset asset: AVAsset) -> Bool ``` |

Modified [AVVideoCompositionValidationHandling.videoComposition(_: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidValueForKey: String) -> Bool](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/1389404-videocomposition)

|  | Declaration |
| --- | --- |
| From | ``` optional func videoComposition(_ videoComposition: AVVideoComposition!, shouldContinueValidatingAfterFindingInvalidValueForKey key: String!) -> Bool ``` |
| To | ``` optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidValueForKey key: String) -> Bool ``` |

Modified [NSCoder.decodeCMTimeForKey(_: String) -> CMTime](https://developer.apple.com/documentation/foundation/nscoder/1389544-decodetime)

|  | Declaration |
| --- | --- |
| From | ``` func decodeCMTimeForKey(_ key: String!) -> CMTime ``` |
| To | ``` func decodeCMTimeForKey(_ key: String) -> CMTime ``` |

Modified [NSCoder.decodeCMTimeMappingForKey(_: String) -> CMTimeMapping](https://developer.apple.com/documentation/foundation/nscoder/1389860-decodetimemapping)

|  | Declaration |
| --- | --- |
| From | ``` func decodeCMTimeMappingForKey(_ key: String!) -> CMTimeMapping ``` |
| To | ``` func decodeCMTimeMappingForKey(_ key: String) -> CMTimeMapping ``` |

Modified [NSCoder.decodeCMTimeRangeForKey(_: String) -> CMTimeRange](https://developer.apple.com/documentation/foundation/nscoder/1385718-decodecmtimerangeforkey)

|  | Declaration |
| --- | --- |
| From | ``` func decodeCMTimeRangeForKey(_ key: String!) -> CMTimeRange ``` |
| To | ``` func decodeCMTimeRangeForKey(_ key: String) -> CMTimeRange ``` |

Modified [NSCoder.encodeCMTime(_: CMTime, forKey: String)](https://developer.apple.com/documentation/foundation/nscoder/1388869-encodecmtime)

|  | Declaration |
| --- | --- |
| From | ``` func encodeCMTime(_ time: CMTime, forKey key: String!) ``` |
| To | ``` func encodeCMTime(_ time: CMTime, forKey key: String) ``` |

Modified [NSCoder.encodeCMTimeMapping(_: CMTimeMapping, forKey: String)](https://developer.apple.com/documentation/foundation/nscoder/1389496-encode)

|  | Declaration |
| --- | --- |
| From | ``` func encodeCMTimeMapping(_ timeMapping: CMTimeMapping, forKey key: String!) ``` |
| To | ``` func encodeCMTimeMapping(_ timeMapping: CMTimeMapping, forKey key: String) ``` |

Modified [NSCoder.encodeCMTimeRange(_: CMTimeRange, forKey: String)](https://developer.apple.com/documentation/foundation/nscoder/1386649-encode)

|  | Declaration |
| --- | --- |
| From | ``` func encodeCMTimeRange(_ timeRange: CMTimeRange, forKey key: String!) ``` |
| To | ``` func encodeCMTimeRange(_ timeRange: CMTimeRange, forKey key: String) ``` |

Modified [NSValue.init(CMTime: CMTime)](https://developer.apple.com/documentation/foundation/nsvalue/1388561-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(CMTime time: CMTime) -> NSValue ``` |
| To | ``` init(CMTime time: CMTime) ``` |

Modified [NSValue.init(CMTimeMapping: CMTimeMapping)](https://developer.apple.com/documentation/foundation/nsvalue/1387556-valuewithcmtimemapping)

|  | Declaration |
| --- | --- |
| From | ``` init!(CMTimeMapping timeMapping: CMTimeMapping) -> NSValue ``` |
| To | ``` init(CMTimeMapping timeMapping: CMTimeMapping) ``` |

Modified [NSValue.init(CMTimeRange: CMTimeRange)](https://developer.apple.com/documentation/foundation/nsvalue/1386915-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(CMTimeRange timeRange: CMTimeRange) -> NSValue ``` |
| To | ``` init(CMTimeRange timeRange: CMTimeRange) ``` |

Modified [AVAssetImageGeneratorCompletionHandler](https://developer.apple.com/documentation/avfoundation/avassetimagegeneratorcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias AVAssetImageGeneratorCompletionHandler = (CMTime, CGImage!, CMTime, AVAssetImageGeneratorResult, NSError!) -> Void ``` |
| To | ``` typealias AVAssetImageGeneratorCompletionHandler = (CMTime, CGImage?, CMTime, AVAssetImageGeneratorResult, NSError?) -> Void ``` |

Modified [AVAudioNodeTapBlock](https://developer.apple.com/documentation/avfoundation/avaudionodetapblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias AVAudioNodeTapBlock = (AVAudioPCMBuffer!, AVAudioTime!) -> Void ``` |
| To | ``` typealias AVAudioNodeTapBlock = (AVAudioPCMBuffer, AVAudioTime) -> Void ``` |

Modified [AVFileType3GPP2](https://developer.apple.com/documentation/avfoundation/avfiletype/1388141-mobile3gpp2)

|  | Introduction |
| --- | --- |
| From | iOS 7.0 |
| To | iOS 4.0 |

Modified [AVMetadataID3MetadataKeyCommerical](https://developer.apple.com/documentation/avfoundation/avmetadataid3metadatakeycommerical)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [AVMetadataIdentifierID3MetadataCommerical](https://developer.apple.com/documentation/avfoundation/avmetadataidentifierid3metadatacommerical)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [AVSpeechUtteranceDefaultSpeechRate](https://developer.apple.com/documentation/avfoundation/avspeechutterancedefaultspeechrate)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [AVSpeechUtteranceMaximumSpeechRate](https://developer.apple.com/documentation/avfoundation/avspeechutterancemaximumspeechrate)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [AVSpeechUtteranceMinimumSpeechRate](https://developer.apple.com/documentation/avfoundation/avspeechutteranceminimumspeechrate)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

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
