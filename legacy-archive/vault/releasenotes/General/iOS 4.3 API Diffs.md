---
title: iOS 4.3 API Diffs
apple_id: TP40010594
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2011-02-28'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS43APIDiffs/index.html
archived_at: '2026-07-18T02:55:46.660942Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)


# iOS 4.2 to iOS 4.3 API Differences

## Accelerate

No changes

## AddressBook

No changes

## AddressBookUI

No changes

## AssetsLibrary

No changes

## AudioToolbox

AudioConverter.hAdded [kAudioConverterErr_NoHardwarePermission](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertererr_nohardwarepermission)AudioFile.hAdded [#def kAFInfoDictionary_ISRC](https://developer.apple.com/documentation/audiotoolbox/kafinfodictionary_isrc)Added [#def kAFInfoDictionary_SourceBitDepth](https://developer.apple.com/documentation/audiotoolbox/kafinfodictionary_sourcebitdepth)Added [#def kAFInfoDictionary_SubTitle](https://developer.apple.com/documentation/audiotoolbox/kafinfodictionary_subtitle)Added [kAudioFilePropertySourceBitDepth](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepropertysourcebitdepth)AudioFormat.hAdded [ExtendedAudioFormatInfo](https://developer.apple.com/documentation/audiotoolbox/extendedaudioformatinfo)

## AudioUnit

AudioUnitProperties.hAdded [AudioUnitParameterHistoryInfo](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterhistoryinfo)Added [kAudioUnitParameterFlag_PlotHistory](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1439089-flag_plothistory)Added [kAudioUnitProperty_ParameterHistoryInfo](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_parameterhistoryinfo)

## AVFoundation

AVAsset.hAdded [AVAsset.availableChapterLocales](https://developer.apple.com/documentation/avfoundation/avasset/1388228-availablechapterlocales)Added [-[AVAsset chapterMetadataGroupsWithTitleLocale:containingItemsWithCommonKeys:]](https://developer.apple.com/documentation/avfoundation/avasset/1388966-chaptermetadatagroupswithtitlelo)Added [AVAsset.composable](https://developer.apple.com/documentation/avfoundation/avasset/1386129-composable)Added [AVAsset.exportable](https://developer.apple.com/documentation/avfoundation/avasset/1389245-isexportable)Added [AVAsset.playable](https://developer.apple.com/documentation/avfoundation/avasset/1385974-playable)Added [AVAsset.readable](https://developer.apple.com/documentation/avfoundation/avasset/1390475-readable)Added AVAsset(AVAssetChapterInspection)Added AVAsset(AVAssetUsability)AVAssetWriter.hAdded [AVAssetWriter.movieTimeScale](https://developer.apple.com/documentation/avfoundation/avassetwriter/1386762-movietimescale)Added AVAssetWriter(AVAssetWriterFileTypeSpecificProperties)AVAssetWriterInput.hAdded [AVAssetWriterInput.mediaTimeScale](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1386902-mediatimescale)Added AVAssetWriterInput(AVAssetWriterInputFileTypeSpecificProperties)Added AVAssetWriterInput(AVAssetWriterInputPropertiesForVisualCharacteristic)AVBase.hAdded #def NS_CLASS_AVAILABLEAVError.hAdded [AVErrorApplicationIsNotAuthorized](https://developer.apple.com/documentation/avfoundation/averror/averrorapplicationisnotauthorized)Added [AVErrorContentIsNotAuthorized](https://developer.apple.com/documentation/avfoundation/averror/averrorcontentisnotauthorized)Added [AVErrorDecoderNotFound](https://developer.apple.com/documentation/avfoundation/averror/code/decodernotfound)Added [AVErrorDeviceIsNotAvailableInBackground](https://developer.apple.com/documentation/avfoundation/averror/averrordeviceisnotavailableinbackground)Added [AVErrorEncoderNotFound](https://developer.apple.com/documentation/avfoundation/averror/averrorencodernotfound)Added [AVErrorMediaSubTypeKey](https://developer.apple.com/documentation/avfoundation/averrormediasubtypekey)Added [AVErrorMediaTypeKey](https://developer.apple.com/documentation/avfoundation/averrormediatypekey)AVMetadataFormat.hAdded [AVMetadataQuickTimeMetadataKeyCollectionUser](https://developer.apple.com/documentation/avfoundation/avmetadatakey/1386696-quicktimemetadatakeycollectionus)Added [AVMetadataQuickTimeMetadataKeyDirectionFacing](https://developer.apple.com/documentation/avfoundation/avmetadatakey/1388990-quicktimemetadatakeydirectionfac)Added [AVMetadataQuickTimeMetadataKeyDirectionMotion](https://developer.apple.com/documentation/avfoundation/avmetadataquicktimemetadatakeydirectionmotion)Added [AVMetadataQuickTimeMetadataKeyLocationBody](https://developer.apple.com/documentation/avfoundation/avmetadataquicktimemetadatakeylocationbody)Added [AVMetadataQuickTimeMetadataKeyLocationDate](https://developer.apple.com/documentation/avfoundation/avmetadatakey/1389508-quicktimemetadatakeylocationdate)Added [AVMetadataQuickTimeMetadataKeyLocationName](https://developer.apple.com/documentation/avfoundation/avmetadataquicktimemetadatakeylocationname)Added [AVMetadataQuickTimeMetadataKeyLocationNote](https://developer.apple.com/documentation/avfoundation/avmetadataquicktimemetadatakeylocationnote)Added [AVMetadataQuickTimeMetadataKeyLocationRole](https://developer.apple.com/documentation/avfoundation/avmetadatakey/1389449-quicktimemetadatakeylocationrole)Added [AVMetadataQuickTimeMetadataKeyRatingUser](https://developer.apple.com/documentation/avfoundation/avmetadataquicktimemetadatakeyratinguser)Added [AVMetadataQuickTimeMetadataKeyTitle](https://developer.apple.com/documentation/avfoundation/avmetadatakey/1387911-quicktimemetadatakeytitle)AVMetadataItem.hAdded [-[AVMetadataItem loadValuesAsynchronouslyForKeys:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387102-loadvaluesasynchronouslyforkeys)Added [-[AVMetadataItem statusOfValueForKey:error:]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1388523-statusofvalueforkey)Added AVMetadataItem(AVAsynchronousKeyValueLoading)AVPlayerItem.hAdded [-[AVPlayerItem accessLog]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388499-accesslog)Added [-[AVPlayerItem currentDate]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1386188-currentdate)Added [AVPlayerItem.duration](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389386-duration)Added [-[AVPlayerItem errorLog]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387573-errorlog)Added [AVPlayerItemAccessLog](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslog)Added [AVPlayerItemAccessLog.events](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslog/1387406-events)Added [-[AVPlayerItemAccessLog extendedLogData]](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslog/1386892-extendedlogdata)Added [-[AVPlayerItemAccessLog extendedLogDataStringEncoding]](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslog/1390863-extendedlogdatastringencoding)Added [AVPlayerItemAccessLogEvent](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent)Added [AVPlayerItemAccessLogEvent.URI](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1388643-uri)Added [AVPlayerItemAccessLogEvent.durationWatched](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1388200-durationwatched)Added [AVPlayerItemAccessLogEvent.indicatedBitrate](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1388123-indicatedbitrate)Added [AVPlayerItemAccessLogEvent.numberOfBytesTransferred](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1387305-numberofbytestransferred)Added [AVPlayerItemAccessLogEvent.numberOfDroppedVideoFrames](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1388647-numberofdroppedvideoframes)Added [AVPlayerItemAccessLogEvent.numberOfSegmentsDownloaded](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1588090-numberofsegmentsdownloaded)Added [AVPlayerItemAccessLogEvent.numberOfServerAddressChanges](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1388076-numberofserveraddresschanges)Added [AVPlayerItemAccessLogEvent.numberOfStalls](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1387712-numberofstalls)Added [AVPlayerItemAccessLogEvent.observedBitrate](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1390804-observedbitrate)Added [AVPlayerItemAccessLogEvent.playbackSessionID](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1388462-playbacksessionid)Added [AVPlayerItemAccessLogEvent.playbackStartDate](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1390502-playbackstartdate)Added [AVPlayerItemAccessLogEvent.playbackStartOffset](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1385922-playbackstartoffset)Added [AVPlayerItemAccessLogEvent.segmentsDownloadedDuration](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1388147-segmentsdownloadedduration)Added [AVPlayerItemAccessLogEvent.serverAddress](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1390315-serveraddress)Added [AVPlayerItemErrorLog](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlog)Added [AVPlayerItemErrorLog.events](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlog/1387637-events)Added [-[AVPlayerItemErrorLog extendedLogData]](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlog/1389100-extendedlogdata)Added [-[AVPlayerItemErrorLog extendedLogDataStringEncoding]](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlog/1387271-extendedlogdatastringencoding)Added [AVPlayerItemErrorLogEvent](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent)Added [AVPlayerItemErrorLogEvent.URI](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/1389302-uri)Added [AVPlayerItemErrorLogEvent.date](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/1388416-date)Added [AVPlayerItemErrorLogEvent.errorComment](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/1388011-errorcomment)Added [AVPlayerItemErrorLogEvent.errorDomain](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/1388603-errordomain)Added [AVPlayerItemErrorLogEvent.errorStatusCode](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/1387875-errorstatuscode)Added [AVPlayerItemErrorLogEvent.playbackSessionID](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/1385934-playbacksessionid)Added [AVPlayerItemErrorLogEvent.serverAddress](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/1385797-serveraddress)Added AVPlayerItem(AVPlayerItemLogging)Added [AVPlayerItemFailedToPlayToEndTimeErrorKey](https://developer.apple.com/documentation/avfoundation/avplayeritemfailedtoplaytoendtimeerrorkey)Added [AVPlayerItemFailedToPlayToEndTimeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1388007-avplayeritemfailedtoplaytoendtim)AVTimedMetadataGroup.hAdded [AVMutableTimedMetadataGroup](https://developer.apple.com/documentation/avfoundation/avmutabletimedmetadatagroup)Added [AVMutableTimedMetadataGroup.items](https://developer.apple.com/documentation/avfoundation/avmutabletimedmetadatagroup/1386481-items)Added [AVMutableTimedMetadataGroup.timeRange](https://developer.apple.com/documentation/avfoundation/avmutabletimedmetadatagroup/1387595-timerange)Added [AVTimedMetadataGroup](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup)Added [-[AVTimedMetadataGroup initWithItems:timeRange:]](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/1389632-init)Added [AVTimedMetadataGroup.items](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/1385928-items)Added [AVTimedMetadataGroup.timeRange](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/1387992-timerange)

## CFNetwork

No changes

## CoreAudio

CoreAudioTypes.hAdded [kAudio_FileNotFoundError](https://developer.apple.com/documentation/coreaudio/1572099-anonymous/kaudio_filenotfounderror)

## CoreData

No changes

## CoreFoundation

CFBase.hAdded [#def kCFCoreFoundationVersionNumber10_6_4](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_6_4)Added [#def kCFCoreFoundationVersionNumber10_6_5](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_6_5)Added [#def kCFCoreFoundationVersionNumber_iOS_4_1](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_4_1)Added [#def kCFCoreFoundationVersionNumber_iOS_4_2](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber_ios_4_2)CFString.hAdded [CFStringIsHyphenationAvailableForLocale()](https://developer.apple.com/documentation/corefoundation/1543237-cfstringishyphenationavailablefo)

## CoreGraphics

No changes

## CoreLocation

No changes

## CoreMedia

CMBufferQueue.hAdded [CMBufferQueueGetCallbacksForSampleBuffersSortedByOutputPTS()](https://developer.apple.com/documentation/coremedia/1489625-cmbufferqueuegetcallbacksforsamp)CMFormatDescription.hAdded [CMFormatDescriptionEqualIgnoringExtensionKeys()](https://developer.apple.com/documentation/coremedia/1489465-cmformatdescriptionequalignoring)Added [kCMFormatDescriptionExtension_FullRangeVideo](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_fullrangevideo)Added [kCMVideoCodecType_AppleProRes422](https://developer.apple.com/documentation/coremedia/kcmvideocodectype_appleprores422)Added [kCMVideoCodecType_AppleProRes422HQ](https://developer.apple.com/documentation/coremedia/1564239-video_codec_constants/kcmvideocodectype_appleprores422hq)Added [kCMVideoCodecType_AppleProRes422LT](https://developer.apple.com/documentation/coremedia/kcmvideocodectype_appleprores422lt)Added [kCMVideoCodecType_AppleProRes422Proxy](https://developer.apple.com/documentation/coremedia/1564239-video_codec_constants/kcmvideocodectype_appleprores422proxy)Added [kCMVideoCodecType_AppleProRes4444](https://developer.apple.com/documentation/coremedia/kcmvideocodectype_appleprores4444)Modified [CMFormatDescriptionEqual()](https://developer.apple.com/documentation/coremedia/1489825-cmformatdescriptionequal)

|  | Declaration |
| --- | --- |
| From | Boolean CMFormatDescriptionEqual ( CMFormatDescriptionRef ffd1, CMFormatDescriptionRef ffd2); |
| To | Boolean CMFormatDescriptionEqual ( CMFormatDescriptionRef desc1, CMFormatDescriptionRef desc2); |

CMSampleBuffer.hAdded [kCMSampleBufferAttachmentKey_GradualDecoderRefresh](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_gradualdecoderrefresh)Added [kCMSampleBufferConduitNotificationParameter_MinUpcomingOutputPTS](https://developer.apple.com/documentation/coremedia/kcmsamplebufferconduitnotificationparameter_minupcomingoutputpts)Added [kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange](https://developer.apple.com/documentation/coremedia/kcmsamplebufferconduitnotificationparameter_upcomingoutputptsrangemayoverlapqueuedoutputptsrange)Added [kCMSampleBufferConduitNotification_UpcomingOutputPTSRangeChanged](https://developer.apple.com/documentation/coremedia/kcmsamplebufferconduitnotification_upcomingoutputptsrangechanged)

## CoreMIDI

No changes

## CoreMotion

No changes

## CoreTelephony

CoreTelephonyDefines.hAdded #def CORETELEPHONY_CLASS_AVAILABLE

## CoreText

CTFont.hAdded [kCTFontTableKerx](https://developer.apple.com/documentation/coretext/1524658-anonymous/kctfonttablekerx)CTFontTraits.hAdded [kCTFontColorGlyphsTrait](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/1508808-colorglyphstrait)CTFrame.hAdded [kCTFrameClippingPathsAttributeName](https://developer.apple.com/documentation/coretext/kctframeclippingpathsattributename)Added [kCTFramePathClippingPathAttributeName](https://developer.apple.com/documentation/coretext/kctframepathclippingpathattributename)CTParagraphStyle.hAdded [kCTParagraphStyleSpecifierLineSpacingAdjustment](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/linespacingadjustment)Added [kCTParagraphStyleSpecifierMaximumLineSpacing](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/maximumlinespacing)Added [kCTParagraphStyleSpecifierMinimumLineSpacing](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/kctparagraphstylespecifierminimumlinespacing)CTStringAttributes.hAdded [kCTVerticalFormsAttributeName](https://developer.apple.com/documentation/coretext/kctverticalformsattributename)

## CoreVideo

CVPixelBuffer.hAdded [kCVPixelFormatType_30RGB](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_30rgb)Added [kCVPixelFormatType_4444AYpCbCr16](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_4444aypcbcr16)Added [kCVPixelFormatType_4444AYpCbCr8](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_4444aypcbcr8)CVPixelFormatDescription.hAdded [kCVPixelFormatContainsAlpha](https://developer.apple.com/documentation/corevideo/kcvpixelformatcontainsalpha)

## EventKit

No changes

## EventKitUI

No changes

## ExternalAccessory

No changes

## Foundation

NSObjCRuntime.hAdded [#def NSFoundationVersionNumber10_6_3](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_6_3)Added [#def NSFoundationVersionNumber10_6_4](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_6_4)Added [#def NSFoundationVersionNumber10_6_5](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber10_6_5)Added [#def NSFoundationVersionNumber_iOS_4_1](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber_ios_4_1)Added [#def NSFoundationVersionNumber_iOS_4_2](https://developer.apple.com/documentation/foundation/nsfoundationversionnumber_ios_4_2)

## GameKit

No changes

## iAd

ADBannerView.hAdded [ADErrorApplicationInactive](https://developer.apple.com/documentation/iad/aderror/aderrorapplicationinactive)ADInterstitialAd.hAdded [ADInterstitialAd](https://developer.apple.com/documentation/iad/adinterstitialad)Added [ADInterstitialAd.actionInProgress](https://developer.apple.com/documentation/iad/adinterstitialad/1614658-actioninprogress)Added [-[ADInterstitialAd cancelAction]](https://developer.apple.com/documentation/iad/adinterstitialad/1614616-cancelaction)Added [ADInterstitialAd.delegate](https://developer.apple.com/documentation/iad/adinterstitialad/1614647-delegate)Added [ADInterstitialAd.loaded](https://developer.apple.com/documentation/iad/adinterstitialad/1614653-isloaded)Added [-[ADInterstitialAd presentFromViewController:]](https://developer.apple.com/documentation/iad/adinterstitialad/1621985-presentfromviewcontroller)Added [-[ADInterstitialAd presentInView:]](https://developer.apple.com/documentation/iad/adinterstitialad/1614646-presentinview)Added [ADInterstitialAdDelegate](https://developer.apple.com/documentation/iad/adinterstitialaddelegate)Added [-[ADInterstitialAdDelegate interstitialAd:didFailWithError:]](https://developer.apple.com/documentation/iad/adinterstitialaddelegate/1614645-interstitialad)Added [-[ADInterstitialAdDelegate interstitialAdActionDidFinish:]](https://developer.apple.com/documentation/iad/adinterstitialaddelegate/1614637-interstitialadactiondidfinish)Added [-[ADInterstitialAdDelegate interstitialAdActionShouldBegin:willLeaveApplication:]](https://developer.apple.com/documentation/iad/adinterstitialaddelegate/1614652-interstitialadactionshouldbegin)Added [-[ADInterstitialAdDelegate interstitialAdDidLoad:]](https://developer.apple.com/documentation/iad/adinterstitialaddelegate/1614609-interstitialaddidload)Added [-[ADInterstitialAdDelegate interstitialAdDidUnload:]](https://developer.apple.com/documentation/iad/adinterstitialaddelegate/1614651-interstitialaddidunload)

## ImageIO

CGImageProperties.hAdded [kCGImagePropertyExifBodySerialNumber](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifbodyserialnumber)Added [kCGImagePropertyExifCameraOwnerName](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifcameraownername)Added [kCGImagePropertyExifLensMake](https://developer.apple.com/documentation/imageio/kcgimagepropertyexiflensmake)Added [kCGImagePropertyExifLensModel](https://developer.apple.com/documentation/imageio/kcgimagepropertyexiflensmodel)Added [kCGImagePropertyExifLensSerialNumber](https://developer.apple.com/documentation/imageio/kcgimagepropertyexiflensserialnumber)Added [kCGImagePropertyExifLensSpecification](https://developer.apple.com/documentation/imageio/kcgimagepropertyexiflensspecification)

## MapKit

No changes

## MediaPlayer

MPMoviePlayerController.hRemoved [-[MPMoviePlayerController contentURL]](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620847-contenturl)Removed [-[MPMoviePlayerController setContentURL:]](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620847-contenturl)Added [MPMovieAccessLog](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslog)Added [MPMovieAccessLog.events](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslog/1620820-events)Added [MPMovieAccessLog.extendedLogData](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslog/1620870-extendedlogdata)Added [MPMovieAccessLog.extendedLogDataStringEncoding](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslog/1620814-extendedlogdatastringencoding)Added [MPMovieAccessLogEvent](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent)Added [MPMovieAccessLogEvent.URI](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620959-uri)Added [MPMovieAccessLogEvent.durationWatched](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620880-durationwatched)Added [MPMovieAccessLogEvent.indicatedBitrate](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620932-indicatedbitrate)Added [MPMovieAccessLogEvent.numberOfBytesTransferred](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620949-numberofbytestransferred)Added [MPMovieAccessLogEvent.numberOfDroppedVideoFrames](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620884-numberofdroppedvideoframes)Added [MPMovieAccessLogEvent.numberOfSegmentsDownloaded](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620937-numberofsegmentsdownloaded)Added [MPMovieAccessLogEvent.numberOfServerAddressChanges](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620801-numberofserveraddresschanges)Added [MPMovieAccessLogEvent.numberOfStalls](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620925-numberofstalls)Added [MPMovieAccessLogEvent.observedBitrate](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620827-observedbitrate)Added [MPMovieAccessLogEvent.playbackSessionID](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620926-playbacksessionid)Added [MPMovieAccessLogEvent.playbackStartDate](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620868-playbackstartdate)Added [MPMovieAccessLogEvent.playbackStartOffset](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620902-playbackstartoffset)Added [MPMovieAccessLogEvent.segmentsDownloadedDuration](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620944-segmentsdownloadedduration)Added [MPMovieAccessLogEvent.serverAddress](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620862-serveraddress)Added [MPMovieErrorLog](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlog)Added [MPMovieErrorLog.events](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlog/1620929-events)Added [MPMovieErrorLog.extendedLogData](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlog/1620797-extendedlogdata)Added [MPMovieErrorLog.extendedLogDataStringEncoding](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlog/1620806-extendedlogdatastringencoding)Added [MPMovieErrorLogEvent](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent)Added [MPMovieErrorLogEvent.URI](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent/1620913-uri)Added [MPMovieErrorLogEvent.date](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent/1620794-date)Added [MPMovieErrorLogEvent.errorComment](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent/1620941-errorcomment)Added [MPMovieErrorLogEvent.errorDomain](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent/1620818-errordomain)Added [MPMovieErrorLogEvent.errorStatusCode](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent/1620782-errorstatuscode)Added [MPMovieErrorLogEvent.playbackSessionID](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent/1620890-playbacksessionid)Added [MPMovieErrorLogEvent.serverAddress](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent/1620908-serveraddress)Added [MPMoviePlayerController.accessLog](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620922-accesslog)Added [MPMoviePlayerController.allowsAirPlay](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620781-allowsairplay)Added [MPMoviePlayerController.contentURL](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620847-contenturl)Added [MPMoviePlayerController.errorLog](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620798-errorlog)Added MPMoviePlayerController(MPMovieLogging)

## MessageUI

No changes

## MobileCoreServices

No changes

## OpenAL

No changes

## OpenGLES

No changes

## QuartzCore

No changes

## QuickLook

No changes

## Security

No changes

## StoreKit

No changes

## SystemConfiguration

No changes

## UIKit

UIScreen.hAdded [UIScreen.mirroredScreen](https://developer.apple.com/documentation/uikit/uiscreen/1617829-mirrored)Added [UIScreen.preferredMode](https://developer.apple.com/documentation/uikit/uiscreen/1617823-preferredmode)UIViewController.hAdded [-[UIViewController disablesAutomaticKeyboardDismissal]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621385-disablesautomatickeyboarddismiss)

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
