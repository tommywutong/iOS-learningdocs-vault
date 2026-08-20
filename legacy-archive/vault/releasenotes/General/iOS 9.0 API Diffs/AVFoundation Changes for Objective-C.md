---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/AVFoundation.html
archived_at: '2026-07-18T02:56:28.966163Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# AVFoundation Changes for Objective-C

### AVFoundation

#### AVAsset.h

Added [AVAsset.canContainFragments](https://developer.apple.com/documentation/avfoundation/avasset/1389520-cancontainfragments)Added [AVAsset.compatibleWithAirPlayVideo](https://developer.apple.com/documentation/avfoundation/avasset/1390333-compatiblewithairplayvideo)Added [AVAsset.containsFragments](https://developer.apple.com/documentation/avfoundation/avasset/1385589-containsfragments)Added [AVAsset.preferredMediaSelection](https://developer.apple.com/documentation/avfoundation/avasset/1386122-preferredmediaselection)Added [-[AVFragmentedAsset tracksWithMediaCharacteristic:]](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/1387259-tracks)Added [-[AVFragmentedAsset tracksWithMediaType:]](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/1387253-tracks)Added [-[AVFragmentedAsset trackWithTrackID:]](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/1385712-track)Added [AVFragmentMinding](https://developer.apple.com/documentation/avfoundation/avfragmentminding)Added AVAsset(AVAssetFragments)Added [AVAssetChapterMetadataGroupsDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1386794-avassetchaptermetadatagroupsdidc)Added [AVAssetDurationDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1386249-avassetdurationdidchange)Added [AVAssetMediaSelectionGroupsDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1387984-avassetmediaselectiongroupsdidch)Added AVFragmentedAsset(AVFragmentedAssetTrackInspection)Modified [+[AVAsset assetWithURL:]](https://developer.apple.com/documentation/avfoundation/avasset/1389943-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)assetWithURL:(NSURL *)URL ``` |
| To | ``` + (instancetype _Nonnull)assetWithURL:(NSURL * _Nonnull)URL ``` |

Modified [AVAsset.availableChapterLocales](https://developer.apple.com/documentation/avfoundation/avasset/1388228-availablechapterlocales)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *availableChapterLocales ``` |
| To | ``` @property(readonly, nonnull) NSArray<NSLocale *> *availableChapterLocales ``` |

Modified [AVAsset.availableMediaCharacteristicsWithMediaSelectionOptions](https://developer.apple.com/documentation/avfoundation/avasset/1389433-availablemediacharacteristicswit)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *availableMediaCharacteristicsWithMediaSelectionOptions ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *availableMediaCharacteristicsWithMediaSelectionOptions ``` |

Modified [AVAsset.availableMetadataFormats](https://developer.apple.com/documentation/avfoundation/avasset/1385823-availablemetadataformats)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *availableMetadataFormats ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *availableMetadataFormats ``` |

Modified [-[AVAsset chapterMetadataGroupsBestMatchingPreferredLanguages:]](https://developer.apple.com/documentation/avfoundation/avasset/1390909-chaptermetadatagroupsbestmatchin)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)chapterMetadataGroupsBestMatchingPreferredLanguages:(NSArray *)preferredLanguages ``` |
| To | ``` - (NSArray<AVTimedMetadataGroup *> * _Nonnull)chapterMetadataGroupsBestMatchingPreferredLanguages:(NSArray<NSString *> * _Nonnull)preferredLanguages ``` |

Modified [-[AVAsset chapterMetadataGroupsWithTitleLocale:containingItemsWithCommonKeys:]](https://developer.apple.com/documentation/avfoundation/avasset/1388966-chaptermetadatagroupswithtitlelo)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)chapterMetadataGroupsWithTitleLocale:(NSLocale *)locale containingItemsWithCommonKeys:(NSArray *)commonKeys ``` |
| To | ``` - (NSArray<AVTimedMetadataGroup *> * _Nonnull)chapterMetadataGroupsWithTitleLocale:(NSLocale * _Nonnull)locale containingItemsWithCommonKeys:(NSArray<NSString *> * _Nullable)commonKeys ``` |

Modified [AVAsset.commonMetadata](https://developer.apple.com/documentation/avfoundation/avasset/1390498-commonmetadata)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *commonMetadata ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVMetadataItem *> *commonMetadata ``` |

Modified [AVAsset.metadata](https://developer.apple.com/documentation/avfoundation/avasset/1386884-metadata)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *metadata ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVMetadataItem *> *metadata ``` |

Modified [-[AVAsset metadataForFormat:]](https://developer.apple.com/documentation/avfoundation/avasset/1387759-metadataforformat)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)metadataForFormat:(NSString *)format ``` |
| To | ``` - (NSArray<AVMetadataItem *> * _Nonnull)metadataForFormat:(NSString * _Nonnull)format ``` |

Modified [AVAsset.trackGroups](https://developer.apple.com/documentation/avfoundation/avasset/1390697-trackgroups)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *trackGroups ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVAssetTrackGroup *> *trackGroups ``` |

Modified [AVAsset.tracks](https://developer.apple.com/documentation/avfoundation/avasset/1387953-tracks)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *tracks ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVAssetTrack *> *tracks ``` |

Modified [-[AVAsset tracksWithMediaCharacteristic:]](https://developer.apple.com/documentation/avfoundation/avasset/1389554-tracks)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)tracksWithMediaCharacteristic:(NSString *)mediaCharacteristic ``` |
| To | ``` - (NSArray<AVAssetTrack *> * _Nonnull)tracksWithMediaCharacteristic:(NSString * _Nonnull)mediaCharacteristic ``` |

Modified [-[AVAsset tracksWithMediaType:]](https://developer.apple.com/documentation/avfoundation/avasset/1387140-trackswithmediatype)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)tracksWithMediaType:(NSString *)mediaType ``` |
| To | ``` - (NSArray<AVAssetTrack *> * _Nonnull)tracksWithMediaType:(NSString * _Nonnull)mediaType ``` |

Modified [+[AVURLAsset audiovisualMIMETypes]](https://developer.apple.com/documentation/avfoundation/avurlasset/1390006-audiovisualmimetypes)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)audiovisualMIMETypes ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)audiovisualMIMETypes ``` |

Modified [+[AVURLAsset audiovisualTypes]](https://developer.apple.com/documentation/avfoundation/avurlasset/1386800-audiovisualtypes)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)audiovisualTypes ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)audiovisualTypes ``` |

Modified [-[AVURLAsset initWithURL:options:]](https://developer.apple.com/documentation/avfoundation/avurlasset/1385698-initwithurl)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithURL:(NSURL *)URL options:(NSDictionary *)options ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithURL:(NSURL * _Nonnull)URL options:(NSDictionary<NSString *,id> * _Nullable)options ``` | yes |

Modified [+[AVURLAsset URLAssetWithURL:options:]](https://developer.apple.com/documentation/avfoundation/avurlasset/1508727-urlassetwithurl)

|  | Declaration |
| --- | --- |
| From | ``` + (AVURLAsset *)URLAssetWithURL:(NSURL *)URL options:(NSDictionary *)options ``` |
| To | ``` + (instancetype _Nonnull)URLAssetWithURL:(NSURL * _Nonnull)URL options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

#### AVAssetDownloadTask.h (Added)

Added [AVAssetDownloadDelegate](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate)Added [-[AVAssetDownloadDelegate URLSession:assetDownloadTask:didLoadTimeRange:totalTimeRangesLoaded:timeRangeExpectedToLoad:]](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/1621019-urlsession)Added [-[AVAssetDownloadDelegate URLSession:assetDownloadTask:didResolveMediaSelection:]](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/1621023-urlsession)Added [AVAssetDownloadTask](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask)Added [AVAssetDownloadTask.destinationURL](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask/1621022-destinationurl)Added [AVAssetDownloadTask.loadedTimeRanges](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask/1621026-loadedtimeranges)Added [AVAssetDownloadTask.options](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask/1621014-options)Added [AVAssetDownloadTask.URLAsset](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask/1621024-urlasset)Added [AVAssetDownloadURLSession](https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession)Added [-[AVAssetDownloadURLSession assetDownloadTaskWithURLAsset:destinationURL:options:]](https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession/1621018-assetdownloadtaskwithurlasset)Added [+[AVAssetDownloadURLSession sessionWithConfiguration:assetDownloadDelegate:delegateQueue:]](https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession/1621015-init)Added [AVAssetDownloadTaskMediaSelectionKey](https://developer.apple.com/documentation/avfoundation/avassetdownloadtaskmediaselectionkey)Added [AVAssetDownloadTaskMinimumRequiredMediaBitrateKey](https://developer.apple.com/documentation/avfoundation/avassetdownloadtaskminimumrequiredmediabitratekey)

#### AVAssetExportSession.h

Added [AVAssetExportPreset3840x2160](https://developer.apple.com/documentation/avfoundation/avassetexportpreset3840x2160)Added AVAssetExportSession(AVAssetExportSessionDurationAndLength)Added AVAssetExportSession(AVAssetExportSessionFileTypes)Added AVAssetExportSession(AVAssetExportSessionMediaProcessing)Added AVAssetExportSession(AVAssetExportSessionMetadata)Added AVAssetExportSession(AVAssetExportSessionMultipass)Added AVAssetExportSession(AVAssetExportSessionPresets)Modified [+[AVAssetExportSession allExportPresets]](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1387150-allexportpresets)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)allExportPresets ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)allExportPresets ``` |

Modified [-[AVAssetExportSession determineCompatibleFileTypesWithCompletionHandler:]](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1387907-determinecompatiblefiletypeswith)

|  | Declaration |
| --- | --- |
| From | ``` - (void)determineCompatibleFileTypesWithCompletionHandler:(void (^)(NSArray *compatibleFileTypes))handler ``` |
| To | ``` - (void)determineCompatibleFileTypesWithCompletionHandler:(void (^ _Nonnull)(NSArray<NSString *> * _Nonnull compatibleFileTypes))handler ``` |

Modified [+[AVAssetExportSession exportPresetsCompatibleWithAsset:]](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1390567-exportpresetscompatiblewithasset)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)exportPresetsCompatibleWithAsset:(AVAsset *)asset ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)exportPresetsCompatibleWithAsset:(AVAsset * _Nonnull)asset ``` |

Modified [+[AVAssetExportSession exportSessionWithAsset:presetName:]](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1564246-exportsessionwithasset)

|  | Declaration |
| --- | --- |
| From | ``` + (AVAssetExportSession *)exportSessionWithAsset:(AVAsset *)asset presetName:(NSString *)presetName ``` |
| To | ``` + (instancetype _Nullable)exportSessionWithAsset:(AVAsset * _Nonnull)asset presetName:(NSString * _Nonnull)presetName ``` |

Modified [-[AVAssetExportSession initWithAsset:presetName:]](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1389367-initwithasset)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [AVAssetExportSession.metadata](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1390453-metadata)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *metadata ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<AVMetadataItem *> *metadata ``` |

Modified [AVAssetExportSession.supportedFileTypes](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1388762-supportedfiletypes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *supportedFileTypes ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *supportedFileTypes ``` |

#### AVAssetImageGenerator.h

Modified [+[AVAssetImageGenerator assetImageGeneratorWithAsset:]](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1426634-assetimagegeneratorwithasset)

|  | Declaration |
| --- | --- |
| From | ``` + (AVAssetImageGenerator *)assetImageGeneratorWithAsset:(AVAsset *)asset ``` |
| To | ``` + (instancetype _Nonnull)assetImageGeneratorWithAsset:(AVAsset * _Nonnull)asset ``` |

Modified [-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1388100-generatecgimagesasynchronously)

|  | Declaration |
| --- | --- |
| From | ``` - (void)generateCGImagesAsynchronouslyForTimes:(NSArray *)requestedTimes completionHandler:(AVAssetImageGeneratorCompletionHandler)handler ``` |
| To | ``` - (void)generateCGImagesAsynchronouslyForTimes:(NSArray<NSValue *> * _Nonnull)requestedTimes completionHandler:(AVAssetImageGeneratorCompletionHandler _Nonnull)handler ``` |

Modified [-[AVAssetImageGenerator initWithAsset:]](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1387855-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### AVAssetReader.h

Modified [-[AVAssetReader initWithAsset:error:]](https://developer.apple.com/documentation/avfoundation/avassetreader/1385593-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [AVAssetReader.outputs](https://developer.apple.com/documentation/avfoundation/avassetreader/1387132-outputs)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *outputs ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVAssetReaderOutput *> *outputs ``` |

#### AVAssetReaderOutput.h

Modified [+[AVAssetReaderAudioMixOutput assetReaderAudioMixOutputWithAudioTracks:audioSettings:]](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/1490328-assetreaderaudiomixoutputwithaud)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)assetReaderAudioMixOutputWithAudioTracks:(NSArray *)audioTracks audioSettings:(NSDictionary *)audioSettings ``` |
| To | ``` + (instancetype _Nonnull)assetReaderAudioMixOutputWithAudioTracks:(NSArray<AVAssetTrack *> * _Nonnull)audioTracks audioSettings:(NSDictionary<NSString *,id> * _Nullable)audioSettings ``` |

Modified [AVAssetReaderAudioMixOutput.audioSettings](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/1388860-audiosettings)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDictionary *audioSettings ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSDictionary<NSString *,id> *audioSettings ``` |

Modified [AVAssetReaderAudioMixOutput.audioTracks](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/1385635-audiotracks)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *audioTracks ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVAssetTrack *> *audioTracks ``` |

Modified [-[AVAssetReaderAudioMixOutput initWithAudioTracks:audioSettings:]](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/1388883-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithAudioTracks:(NSArray *)audioTracks audioSettings:(NSDictionary *)audioSettings ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithAudioTracks:(NSArray<AVAssetTrack *> * _Nonnull)audioTracks audioSettings:(NSDictionary<NSString *,id> * _Nullable)audioSettings ``` | yes |

Modified [-[AVAssetReaderOutput resetForReadingTimeRanges:]](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/1388890-resetforreadingtimeranges)

|  | Declaration |
| --- | --- |
| From | ``` - (void)resetForReadingTimeRanges:(NSArray *)timeRanges ``` |
| To | ``` - (void)resetForReadingTimeRanges:(NSArray<NSValue *> * _Nonnull)timeRanges ``` |

Modified [-[AVAssetReaderOutputMetadataAdaptor initWithAssetReaderTrackOutput:]](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputmetadataadaptor/1388009-initwithassetreadertrackoutput)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [+[AVAssetReaderSampleReferenceOutput assetReaderSampleReferenceOutputWithTrack:]](https://developer.apple.com/documentation/avfoundation/avassetreadersamplereferenceoutput/1490320-assetreadersamplereferenceoutput)

|  | Declaration |
| --- | --- |
| From | ``` + (AVAssetReaderSampleReferenceOutput *)assetReaderSampleReferenceOutputWithTrack:(AVAssetTrack *)track ``` |
| To | ``` + (instancetype _Nonnull)assetReaderSampleReferenceOutputWithTrack:(AVAssetTrack * _Nonnull)track ``` |

Modified [-[AVAssetReaderSampleReferenceOutput initWithTrack:]](https://developer.apple.com/documentation/avfoundation/avassetreadersamplereferenceoutput/1387339-initwithtrack)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [+[AVAssetReaderTrackOutput assetReaderTrackOutputWithTrack:outputSettings:]](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput/1490322-assetreadertrackoutputwithtrack)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)assetReaderTrackOutputWithTrack:(AVAssetTrack *)track outputSettings:(NSDictionary *)outputSettings ``` |
| To | ``` + (instancetype _Nonnull)assetReaderTrackOutputWithTrack:(AVAssetTrack * _Nonnull)track outputSettings:(NSDictionary<NSString *,id> * _Nullable)outputSettings ``` |

Modified [-[AVAssetReaderTrackOutput initWithTrack:outputSettings:]](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput/1385807-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithTrack:(AVAssetTrack *)track outputSettings:(NSDictionary *)outputSettings ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithTrack:(AVAssetTrack * _Nonnull)track outputSettings:(NSDictionary<NSString *,id> * _Nullable)outputSettings ``` | yes |

Modified [AVAssetReaderTrackOutput.outputSettings](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput/1387163-outputsettings)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDictionary *outputSettings ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSDictionary<NSString *,id> *outputSettings ``` |

Modified [+[AVAssetReaderVideoCompositionOutput assetReaderVideoCompositionOutputWithVideoTracks:videoSettings:]](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/1490331-assetreadervideocompositionoutpu)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)assetReaderVideoCompositionOutputWithVideoTracks:(NSArray *)videoTracks videoSettings:(NSDictionary *)videoSettings ``` |
| To | ``` + (instancetype _Nonnull)assetReaderVideoCompositionOutputWithVideoTracks:(NSArray<AVAssetTrack *> * _Nonnull)videoTracks videoSettings:(NSDictionary<NSString *,id> * _Nullable)videoSettings ``` |

Modified [-[AVAssetReaderVideoCompositionOutput initWithVideoTracks:videoSettings:]](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/1386676-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithVideoTracks:(NSArray *)videoTracks videoSettings:(NSDictionary *)videoSettings ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithVideoTracks:(NSArray<AVAssetTrack *> * _Nonnull)videoTracks videoSettings:(NSDictionary<NSString *,id> * _Nullable)videoSettings ``` | yes |

Modified [AVAssetReaderVideoCompositionOutput.videoSettings](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/1389247-videosettings)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDictionary *videoSettings ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSDictionary<NSString *,id> *videoSettings ``` |

Modified [AVAssetReaderVideoCompositionOutput.videoTracks](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/1389000-videotracks)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *videoTracks ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVAssetTrack *> *videoTracks ``` |

#### AVAssetResourceLoader.h

Removed AVAssetResourceLoadingRequest(AVAssetResourceLoader_ContentKeyRequestSupport)Added [AVAssetResourceLoader.preloadsEligibleContentKeys](https://developer.apple.com/documentation/avfoundation/avassetresourceloader/1386939-preloadseligiblecontentkeys)Added [AVAssetResourceLoadingDataRequest.requestsAllDataToEndOfResource](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest/1386864-requestsalldatatoendofresource)Added [-[AVAssetResourceLoadingRequest persistentContentKeyFromKeyVendorResponse:options:error:]](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1623676-persistentcontentkey)Added AVAssetResourceLoader(AVAssetResourceLoaderContentKeySupport)Added AVAssetResourceLoadingRequest(AVAssetResourceLoadingRequestContentKeyRequestSupport)Added [AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey)Modified [AVAssetResourceLoader.delegate](https://developer.apple.com/documentation/avfoundation/avassetresourceloader/1387913-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id<AVAssetResourceLoaderDelegate> delegate ``` |
| To | ``` @property(nonatomic, readonly, weak, nullable) id<AVAssetResourceLoaderDelegate> delegate ``` |

Modified [-[AVAssetResourceLoadingRequest streamingContentKeyRequestDataForApp:contentIdentifier:options:error:]](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1386116-streamingcontentkeyrequestdata)

|  | Declaration |
| --- | --- |
| From | ``` - (NSData *)streamingContentKeyRequestDataForApp:(NSData *)appIdentifier contentIdentifier:(NSData *)contentIdentifier options:(NSDictionary *)options error:(NSError **)outError ``` |
| To | ``` - (NSData * _Nullable)streamingContentKeyRequestDataForApp:(NSData * _Nonnull)appIdentifier contentIdentifier:(NSData * _Nonnull)contentIdentifier options:(NSDictionary<NSString *,id> * _Nullable)options error:(NSError * _Nullable * _Nullable)outError ``` |

#### AVAssetTrack.h

Added [AVAssetTrackSegmentsDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1386848-avassettracksegmentsdidchange)Added [AVAssetTrackTimeRangeDidChangeNotification](https://developer.apple.com/documentation/avfoundation/avassettracktimerangedidchangenotification)Added [AVAssetTrackTrackAssociationsDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1388487-avassettracktrackassociationsdid)Modified [AVAssetTrack.asset](https://developer.apple.com/documentation/avfoundation/avassettrack/1385611-asset)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVAsset *asset ``` |
| To | ``` @property(nonatomic, readonly, weak, nullable) AVAsset *asset ``` |

Modified [-[AVAssetTrack associatedTracksOfType:]](https://developer.apple.com/documentation/avfoundation/avassettrack/1389251-associatedtracksoftype)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)associatedTracksOfType:(NSString *)trackAssociationType ``` |
| To | ``` - (NSArray<AVAssetTrack *> * _Nonnull)associatedTracksOfType:(NSString * _Nonnull)trackAssociationType ``` |

Modified [AVAssetTrack.availableMetadataFormats](https://developer.apple.com/documentation/avfoundation/avassettrack/1385751-availablemetadataformats)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *availableMetadataFormats ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *availableMetadataFormats ``` |

Modified [AVAssetTrack.availableTrackAssociationTypes](https://developer.apple.com/documentation/avfoundation/avassettrack/1388065-availabletrackassociationtypes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *availableTrackAssociationTypes ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *availableTrackAssociationTypes ``` |

Modified [AVAssetTrack.commonMetadata](https://developer.apple.com/documentation/avfoundation/avassettrack/1390832-commonmetadata)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *commonMetadata ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVMetadataItem *> *commonMetadata ``` |

Modified [AVAssetTrack.metadata](https://developer.apple.com/documentation/avfoundation/avassettrack/1389054-metadata)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *metadata ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVMetadataItem *> *metadata ``` |

Modified [-[AVAssetTrack metadataForFormat:]](https://developer.apple.com/documentation/avfoundation/avassettrack/1387921-metadataforformat)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)metadataForFormat:(NSString *)format ``` |
| To | ``` - (NSArray<AVMetadataItem *> * _Nonnull)metadataForFormat:(NSString * _Nonnull)format ``` |

Modified [AVAssetTrack.segments](https://developer.apple.com/documentation/avfoundation/avassettrack/1390665-segments)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy, readonly) NSArray *segments ``` |
| To | ``` @property(nonatomic, copy, readonly, nonnull) NSArray<AVAssetTrackSegment *> *segments ``` |

#### AVAssetTrackGroup.h

Modified [AVAssetTrackGroup.trackIDs](https://developer.apple.com/documentation/avfoundation/avassettrackgroup/1389024-trackids)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *trackIDs ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSNumber *> *trackIDs ``` |

#### AVAssetWriter.h

Added [AVAssetWriter.overallDurationHint](https://developer.apple.com/documentation/avfoundation/avassetwriter/1388408-overalldurationhint)Modified [AVAssetWriter.availableMediaTypes](https://developer.apple.com/documentation/avfoundation/avassetwriter/1388730-availablemediatypes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *availableMediaTypes ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *availableMediaTypes ``` |

Modified [-[AVAssetWriter canApplyOutputSettings:forMediaType:]](https://developer.apple.com/documentation/avfoundation/avassetwriter/1388842-canapply)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)canApplyOutputSettings:(NSDictionary *)outputSettings forMediaType:(NSString *)mediaType ``` |
| To | ``` - (BOOL)canApplyOutputSettings:(NSDictionary<NSString *,id> * _Nullable)outputSettings forMediaType:(NSString * _Nonnull)mediaType ``` |

Modified [-[AVAssetWriter initWithURL:fileType:error:]](https://developer.apple.com/documentation/avfoundation/avassetwriter/1389201-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [AVAssetWriter.inputGroups](https://developer.apple.com/documentation/avfoundation/avassetwriter/1388432-inputgroups)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *inputGroups ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVAssetWriterInputGroup *> *inputGroups ``` |

Modified [AVAssetWriter.inputs](https://developer.apple.com/documentation/avfoundation/avassetwriter/1388264-inputs)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *inputs ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVAssetWriterInput *> *inputs ``` |

Modified [AVAssetWriter.metadata](https://developer.apple.com/documentation/avfoundation/avassetwriter/1387974-metadata)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *metadata ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSArray<AVMetadataItem *> *metadata ``` |

Modified [+[AVAssetWriterInputGroup assetWriterInputGroupWithInputs:defaultInput:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinputgroup/1426655-assetwriterinputgroupwithinputs)

|  | Declaration |
| --- | --- |
| From | ``` + (AVAssetWriterInputGroup *)assetWriterInputGroupWithInputs:(NSArray *)inputs defaultInput:(AVAssetWriterInput *)defaultInput ``` |
| To | ``` + (instancetype _Nonnull)assetWriterInputGroupWithInputs:(NSArray<AVAssetWriterInput *> * _Nonnull)inputs defaultInput:(AVAssetWriterInput * _Nullable)defaultInput ``` |

Modified [-[AVAssetWriterInputGroup initWithInputs:defaultInput:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinputgroup/1389502-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithInputs:(NSArray *)inputs defaultInput:(AVAssetWriterInput *)defaultInput ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithInputs:(NSArray<AVAssetWriterInput *> * _Nonnull)inputs defaultInput:(AVAssetWriterInput * _Nullable)defaultInput ``` | yes |

Modified [AVAssetWriterInputGroup.inputs](https://developer.apple.com/documentation/avfoundation/avassetwriterinputgroup/1388226-inputs)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *inputs ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVAssetWriterInput *> *inputs ``` |

#### AVAssetWriterInput.h

Modified [+[AVAssetWriterInput assetWriterInputWithMediaType:outputSettings:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1449070-assetwriterinputwithmediatype)

|  | Declaration |
| --- | --- |
| From | ``` + (AVAssetWriterInput *)assetWriterInputWithMediaType:(NSString *)mediaType outputSettings:(NSDictionary *)outputSettings ``` |
| To | ``` + (instancetype _Nonnull)assetWriterInputWithMediaType:(NSString * _Nonnull)mediaType outputSettings:(NSDictionary<NSString *,id> * _Nullable)outputSettings ``` |

Modified [+[AVAssetWriterInput assetWriterInputWithMediaType:outputSettings:sourceFormatHint:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1449091-assetwriterinputwithmediatype)

|  | Declaration |
| --- | --- |
| From | ``` + (AVAssetWriterInput *)assetWriterInputWithMediaType:(NSString *)mediaType outputSettings:(NSDictionary *)outputSettings sourceFormatHint:(CMFormatDescriptionRef)sourceFormatHint ``` |
| To | ``` + (instancetype _Nonnull)assetWriterInputWithMediaType:(NSString * _Nonnull)mediaType outputSettings:(NSDictionary<NSString *,id> * _Nullable)outputSettings sourceFormatHint:(CMFormatDescriptionRef _Nullable)sourceFormatHint ``` |

Modified [-[AVAssetWriterInput initWithMediaType:outputSettings:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1385912-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithMediaType:(NSString *)mediaType outputSettings:(NSDictionary *)outputSettings ``` |
| To | ``` - (instancetype _Nonnull)initWithMediaType:(NSString * _Nonnull)mediaType outputSettings:(NSDictionary<NSString *,id> * _Nullable)outputSettings ``` |

Modified [-[AVAssetWriterInput initWithMediaType:outputSettings:sourceFormatHint:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1389994-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithMediaType:(NSString *)mediaType outputSettings:(NSDictionary *)outputSettings sourceFormatHint:(CMFormatDescriptionRef)sourceFormatHint ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithMediaType:(NSString * _Nonnull)mediaType outputSettings:(NSDictionary<NSString *,id> * _Nullable)outputSettings sourceFormatHint:(CMFormatDescriptionRef _Nullable)sourceFormatHint ``` | yes |

Modified [AVAssetWriterInput.metadata](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1386328-metadata)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *metadata ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSArray<AVMetadataItem *> *metadata ``` |

Modified [AVAssetWriterInput.outputSettings](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1388406-outputsettings)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDictionary *outputSettings ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSDictionary<NSString *,id> *outputSettings ``` |

Modified [-[AVAssetWriterInputMetadataAdaptor initWithAssetWriterInput:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinputmetadataadaptor/1389706-initwithassetwriterinput)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [AVAssetWriterInputPassDescription.sourceTimeRanges](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpassdescription/1388732-sourcetimeranges)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *sourceTimeRanges ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSValue *> *sourceTimeRanges ``` |

Modified [+[AVAssetWriterInputPixelBufferAdaptor assetWriterInputPixelBufferAdaptorWithAssetWriterInput:sourcePixelBufferAttributes:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/1449096-assetwriterinputpixelbufferadapt)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)assetWriterInputPixelBufferAdaptorWithAssetWriterInput:(AVAssetWriterInput *)input sourcePixelBufferAttributes:(NSDictionary *)sourcePixelBufferAttributes ``` |
| To | ``` + (instancetype _Nonnull)assetWriterInputPixelBufferAdaptorWithAssetWriterInput:(AVAssetWriterInput * _Nonnull)input sourcePixelBufferAttributes:(NSDictionary<NSString *,id> * _Nullable)sourcePixelBufferAttributes ``` |

Modified [-[AVAssetWriterInputPixelBufferAdaptor initWithAssetWriterInput:sourcePixelBufferAttributes:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/1390639-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithAssetWriterInput:(AVAssetWriterInput *)input sourcePixelBufferAttributes:(NSDictionary *)sourcePixelBufferAttributes ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithAssetWriterInput:(AVAssetWriterInput * _Nonnull)input sourcePixelBufferAttributes:(NSDictionary<NSString *,id> * _Nullable)sourcePixelBufferAttributes ``` | yes |

Modified [AVAssetWriterInputPixelBufferAdaptor.sourcePixelBufferAttributes](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/1387829-sourcepixelbufferattributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDictionary *sourcePixelBufferAttributes ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSDictionary<NSString *,id> *sourcePixelBufferAttributes ``` |

#### AVAsynchronousKeyValueLoading.h

Modified [-[AVAsynchronousKeyValueLoading loadValuesAsynchronouslyForKeys:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/1387321-loadvaluesasynchronouslyforkeys)

|  | Declaration |
| --- | --- |
| From | ``` - (void)loadValuesAsynchronouslyForKeys:(NSArray *)keys completionHandler:(void (^)(void))handler ``` |
| To | ``` - (void)loadValuesAsynchronouslyForKeys:(NSArray<NSString *> * _Nonnull)keys completionHandler:(void (^ _Nullable)(void))handler ``` |

#### AVAudioBuffer.h

Added [AVAudioCompressedBuffer](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer)Added [AVAudioCompressedBuffer.data](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1390620-data)Added [-[AVAudioCompressedBuffer initWithFormat:packetCapacity:]](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1387124-init)Added [-[AVAudioCompressedBuffer initWithFormat:packetCapacity:maximumPacketSize:]](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1386718-initwithformat)Added [AVAudioCompressedBuffer.maximumPacketSize](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1389326-maximumpacketsize)Added [AVAudioCompressedBuffer.packetCapacity](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1386081-packetcapacity)Added [AVAudioCompressedBuffer.packetCount](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1386000-packetcount)Added [AVAudioCompressedBuffer.packetDescriptions](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1389750-packetdescriptions)Modified [-[AVAudioPCMBuffer initWithPCMFormat:frameCapacity:]](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1389630-initwithpcmformat)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### AVAudioChannelLayout.h

Modified [AVAudioChannelLayout](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSSecureCoding |

Modified [-[AVAudioChannelLayout initWithLayout:]](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1387623-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### AVAudioConnectionPoint.h (Added)

Added [AVAudioConnectionPoint](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint)Added [AVAudioConnectionPoint.bus](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint/1389288-bus)Added [-[AVAudioConnectionPoint initWithNode:bus:]](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint/1388569-initwithnode)Added [AVAudioConnectionPoint.node](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint/1386935-node)

#### AVAudioConverter.h (Added)

Added [AVAudioConverter](https://developer.apple.com/documentation/avfoundation/avaudioconverter)Added [AVAudioConverter.applicableEncodeBitRates](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388940-applicableencodebitrates)Added [AVAudioConverter.applicableEncodeSampleRates](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1389427-applicableencodesamplerates)Added [AVAudioConverter.availableEncodeBitRates](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388589-availableencodebitrates)Added [AVAudioConverter.availableEncodeChannelLayoutTags](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387337-availableencodechannellayouttags)Added [AVAudioConverter.availableEncodeSampleRates](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1386202-availableencodesamplerates)Added [AVAudioConverter.bitRate](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390373-bitrate)Added [AVAudioConverter.bitRateStrategy](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1386092-bitratestrategy)Added [AVAudioConverter.channelMap](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390653-channelmap)Added [-[AVAudioConverter convertToBuffer:error:withInputFromBlock:]](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387865-converttobuffer)Added [-[AVAudioConverter convertToBuffer:fromBuffer:error:]](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388341-converttobuffer)Added [AVAudioConverter.dither](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1386312-dither)Added [AVAudioConverter.downmix](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388244-downmix)Added [-[AVAudioConverter initFromFormat:toFormat:]](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387008-initfromformat)Added [AVAudioConverter.inputFormat](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388914-inputformat)Added [AVAudioConverter.magicCookie](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390770-magiccookie)Added [AVAudioConverter.maximumOutputPacketSize](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390069-maximumoutputpacketsize)Added [AVAudioConverter.outputFormat](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387563-outputformat)Added [AVAudioConverter.primeInfo](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1389770-primeinfo)Added [AVAudioConverter.primeMethod](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387299-primemethod)Added [-[AVAudioConverter reset]](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390876-reset)Added [AVAudioConverter.sampleRateConverterAlgorithm](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387976-samplerateconverteralgorithm)Added [AVAudioConverter.sampleRateConverterQuality](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390887-samplerateconverterquality)Added AVAudioConverter(Encoding)Added [AVAudioConverterInputBlock](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputblock)Added [AVAudioConverterInputStatus](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus)Added [AVAudioConverterInputStatus_EndOfStream](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus/endofstream)Added [AVAudioConverterInputStatus_HaveData](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus/havedata)Added [AVAudioConverterInputStatus_NoDataNow](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus/avaudioconverterinputstatus_nodatanow)Added [AVAudioConverterOutputStatus](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus)Added [AVAudioConverterOutputStatus_EndOfStream](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/endofstream)Added [AVAudioConverterOutputStatus_Error](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/error)Added [AVAudioConverterOutputStatus_HaveData](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/havedata)Added [AVAudioConverterOutputStatus_InputRanDry](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/inputrandry)Added [AVAudioConverterPrimeInfo](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimeinfo)Added [AVAudioConverterPrimeMethod](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod)Added [AVAudioConverterPrimeMethod_None](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod/none)Added [AVAudioConverterPrimeMethod_Normal](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod/normal)Added [AVAudioConverterPrimeMethod_Pre](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod/avaudioconverterprimemethod_pre)

#### AVAudioEngine.h

Added [-[AVAudioEngine connect:toConnectionPoints:fromBus:format:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389510-connect)Added [-[AVAudioEngine inputConnectionPointForNode:inputBus:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1387521-inputconnectionpoint)Added [-[AVAudioEngine outputConnectionPointsForNode:outputBus:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389298-outputconnectionpointsfornode)

#### AVAudioEnvironmentNode.h

Modified [AVAudioEnvironmentNode.applicableRenderingAlgorithms](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1390049-applicablerenderingalgorithms)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)applicableRenderingAlgorithms ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSNumber *> *applicableRenderingAlgorithms ``` |

#### AVAudioFile.h

Modified [-[AVAudioFile initForWriting:settings:commonFormat:interleaved:error:]](https://developer.apple.com/documentation/avfoundation/avaudiofile/1387154-initforwriting)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initForWriting:(NSURL *)fileURL settings:(NSDictionary *)settings commonFormat:(AVAudioCommonFormat)format interleaved:(BOOL)interleaved error:(NSError **)outError ``` |
| To | ``` - (instancetype _Nullable)initForWriting:(NSURL * _Nonnull)fileURL settings:(NSDictionary<NSString *,id> * _Nonnull)settings commonFormat:(AVAudioCommonFormat)format interleaved:(BOOL)interleaved error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [-[AVAudioFile initForWriting:settings:error:]](https://developer.apple.com/documentation/avfoundation/avaudiofile/1390840-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initForWriting:(NSURL *)fileURL settings:(NSDictionary *)settings error:(NSError **)outError ``` |
| To | ``` - (instancetype _Nullable)initForWriting:(NSURL * _Nonnull)fileURL settings:(NSDictionary<NSString *,id> * _Nonnull)settings error:(NSError * _Nullable * _Nullable)outError ``` |

#### AVAudioFormat.h

Added [AVAudioFormat.formatDescription](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387467-formatdescription)Added [-[AVAudioFormat initWithCMAudioFormatDescription:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387465-init)Modified [AVAudioFormat](https://developer.apple.com/documentation/avfoundation/avaudioformat)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSSecureCoding |

Modified [-[AVAudioFormat initWithSettings:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387931-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSettings:(NSDictionary *)settings ``` |
| To | ``` - (instancetype _Nonnull)initWithSettings:(NSDictionary<NSString *,id> * _Nonnull)settings ``` |

Modified [AVAudioFormat.settings](https://developer.apple.com/documentation/avfoundation/avaudioformat/1386904-settings)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDictionary *settings ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSDictionary<NSString *,id> *settings ``` |

#### AVAudioMix.h

Modified [AVAudioMix.inputParameters](https://developer.apple.com/documentation/avfoundation/avaudiomix/1388791-inputparameters)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *inputParameters ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<AVAudioMixInputParameters *> *inputParameters ``` |

Modified [+[AVMutableAudioMix audioMix]](https://developer.apple.com/documentation/avfoundation/avmutableaudiomix/1560973-audiomix)

|  | Declaration |
| --- | --- |
| From | ``` + (AVMutableAudioMix *)audioMix ``` |
| To | ``` + (instancetype _Nonnull)audioMix ``` |

Modified [AVMutableAudioMix.inputParameters](https://developer.apple.com/documentation/avfoundation/avmutableaudiomix/1388159-inputparameters)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *inputParameters ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSArray<AVAudioMixInputParameters *> *inputParameters ``` |

Modified [+[AVMutableAudioMixInputParameters audioMixInputParameters]](https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/1560974-audiomixinputparameters)

|  | Declaration |
| --- | --- |
| From | ``` + (AVMutableAudioMixInputParameters *)audioMixInputParameters ``` |
| To | ``` + (instancetype _Nonnull)audioMixInputParameters ``` |

Modified [+[AVMutableAudioMixInputParameters audioMixInputParametersWithTrack:]](https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/1386858-audiomixinputparameterswithtrack)

|  | Declaration |
| --- | --- |
| From | ``` + (AVMutableAudioMixInputParameters *)audioMixInputParametersWithTrack:(AVAssetTrack *)track ``` |
| To | ``` + (instancetype _Nonnull)audioMixInputParametersWithTrack:(AVAssetTrack * _Nullable)track ``` |

#### AVAudioMixing.h

Added [-[AVAudioMixing destinationForMixer:bus:]](https://developer.apple.com/documentation/avfoundation/avaudiomixing/1390356-destination)Added [AVAudioMixingDestination](https://developer.apple.com/documentation/avfoundation/avaudiomixingdestination)Added [AVAudioMixingDestination.connectionPoint](https://developer.apple.com/documentation/avfoundation/avaudiomixingdestination/1389898-connectionpoint)

#### AVAudioPlayer.h

Modified [AVAudioPlayer.channelAssignments](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1624038-channelassignments)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *channelAssignments ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSNumber *> *channelAssignments ``` |

Modified [AVAudioPlayer.settings](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389359-settings)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSDictionary *settings ``` |
| To | ``` @property(readonly, nonnull) NSDictionary<NSString *,id> *settings ``` |

#### AVAudioRecorder.h

Modified [AVAudioRecorder.channelAssignments](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1624903-channelassignments)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *channelAssignments ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSNumber *> *channelAssignments ``` |

Modified [-[AVAudioRecorder initWithURL:settings:error:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1388386-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithURL:(NSURL *)url settings:(NSDictionary *)settings error:(NSError **)outError ``` |
| To | ``` - (instancetype _Nullable)initWithURL:(NSURL * _Nonnull)url settings:(NSDictionary<NSString *,id> * _Nonnull)settings error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [AVAudioRecorder.settings](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1390903-settings)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSDictionary *settings ``` |
| To | ``` @property(readonly, nonnull) NSDictionary<NSString *,id> *settings ``` |

#### AVAudioSequencer.h (Added)

Added [AVAudioSequencer](https://developer.apple.com/documentation/avfoundation/avaudiosequencer)Added [-[AVAudioSequencer beatsForHostTime:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1389012-beats)Added [-[AVAudioSequencer beatsForSeconds:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387853-beats)Added [AVAudioSequencer.currentPositionInBeats](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388910-currentpositioninbeats)Added [AVAudioSequencer.currentPositionInSeconds](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1390524-currentpositioninseconds)Added [-[AVAudioSequencer dataWithSMPTEResolution:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388701-datawithsmpteresolution)Added [-[AVAudioSequencer hostTimeForBeats:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1386184-hosttime)Added [-[AVAudioSequencer init]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1385851-init)Added [-[AVAudioSequencer initWithAudioEngine:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388339-init)Added [-[AVAudioSequencer loadFromData:options:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1389720-load)Added [-[AVAudioSequencer loadFromURL:options:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1386241-load)Added [AVAudioSequencer.playing](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388402-playing)Added [-[AVAudioSequencer prepareToPlay]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1385633-preparetoplay)Added [AVAudioSequencer.rate](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387903-rate)Added [-[AVAudioSequencer secondsForBeats:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387615-seconds)Added [-[AVAudioSequencer startAndReturnError:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387594-start)Added [-[AVAudioSequencer stop]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1386674-stop)Added [AVAudioSequencer.tempoTrack](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1390252-tempotrack)Added [AVAudioSequencer.tracks](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387567-tracks)Added [AVAudioSequencer.userInfo](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1389262-userinfo)Added [-[AVAudioSequencer writeToURL:SMPTEResolution:replaceExisting:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1390589-write)Added [AVMusicTrack](https://developer.apple.com/documentation/avfoundation/avmusictrack)Added [AVMusicTrack.destinationAudioUnit](https://developer.apple.com/documentation/avfoundation/avmusictrack/1390533-destinationaudiounit)Added [AVMusicTrack.destinationMIDIEndpoint](https://developer.apple.com/documentation/avfoundation/avmusictrack/1388828-destinationmidiendpoint)Added [AVMusicTrack.lengthInBeats](https://developer.apple.com/documentation/avfoundation/avmusictrack/1389910-lengthinbeats)Added [AVMusicTrack.lengthInSeconds](https://developer.apple.com/documentation/avfoundation/avmusictrack/1385749-lengthinseconds)Added [AVMusicTrack.loopingEnabled](https://developer.apple.com/documentation/avfoundation/avmusictrack/1385811-isloopingenabled)Added [AVMusicTrack.loopRange](https://developer.apple.com/documentation/avfoundation/avmusictrack/1386292-looprange)Added [AVMusicTrack.muted](https://developer.apple.com/documentation/avfoundation/avmusictrack/1387694-muted)Added [AVMusicTrack.numberOfLoops](https://developer.apple.com/documentation/avfoundation/avmusictrack/1389268-numberofloops)Added [AVMusicTrack.offsetTime](https://developer.apple.com/documentation/avfoundation/avmusictrack/1386336-offsettime)Added [AVMusicTrack.soloed](https://developer.apple.com/documentation/avfoundation/avmusictrack/1387883-issoloed)Added [AVMusicTrack.timeResolution](https://developer.apple.com/documentation/avfoundation/avmusictrack/1387198-timeresolution)Added AVAudioSequencer(AVAudioSequencer_Player)Added [AVBeatRange](https://developer.apple.com/documentation/avfoundation/avbeatrange)Added [AVMakeBeatRange()](https://developer.apple.com/documentation/avfoundation/1386774-avmakebeatrange)Added [AVMusicSequenceLoadOptions](https://developer.apple.com/documentation/avfoundation/avmusicsequenceloadoptions)Added [AVMusicSequenceLoadSMF_ChannelsToTracks](https://developer.apple.com/documentation/avfoundation/avmusicsequenceloadoptions/1388410-smfchannelstotracks)Added [AVMusicSequenceLoadSMF_PreserveTracks](https://developer.apple.com/documentation/avfoundation/avmusicsequenceloadoptions/avmusicsequenceloadsmf_preservetracks)Added [AVMusicTimeStamp](https://developer.apple.com/documentation/avfoundation/avmusictimestamp)Added [AVMusicTrackLoopCount](https://developer.apple.com/documentation/avfoundation/avmusictrackloopcount)Added [AVMusicTrackLoopCountForever](https://developer.apple.com/documentation/avfoundation/avmusictrackloopcount/avmusictrackloopcountforever)

#### AVAudioSession.h

Added [AVAudioSession.availableCategories](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616591-availablecategories)Added [AVAudioSession.availableModes](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616517-availablemodes)Added [AVAudioSessionCategoryOptionInterruptSpokenAudioAndMixWithOthers](https://developer.apple.com/documentation/avfoundation/avaudiosession/categoryoptions/1616534-interruptspokenaudioandmixwithot)Added [AVAudioSessionErrorCodeResourceNotAvailable](https://developer.apple.com/documentation/avfoundation/avaudiosessionerrorcode/avaudiosessionerrorcoderesourcenotavailable)Added [AVAudioSessionModeSpokenAudio](https://developer.apple.com/documentation/avfoundation/avaudiosession/mode/1616510-spokenaudio)Modified [AVAudioSession.availableInputs](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616557-availableinputs)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *availableInputs ``` |
| To | ``` @property(readonly, nullable) NSArray<AVAudioSessionPortDescription *> *availableInputs ``` |

Modified [AVAudioSession.inputDataSources](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616513-inputdatasources)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *inputDataSources ``` |
| To | ``` @property(readonly, nullable) NSArray<AVAudioSessionDataSourceDescription *> *inputDataSources ``` |

Modified [AVAudioSession.outputDataSources](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616479-outputdatasources)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *outputDataSources ``` |
| To | ``` @property(readonly, nullable) NSArray<AVAudioSessionDataSourceDescription *> *outputDataSources ``` |

Modified [AVAudioSessionDataSourceDescription.supportedPolarPatterns](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616450-supportedpolarpatterns)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *supportedPolarPatterns ``` |
| To | ``` @property(readonly, nullable) NSArray<NSString *> *supportedPolarPatterns ``` |

Modified [AVAudioSessionPortDescription.channels](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616574-channels)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *channels ``` |
| To | ``` @property(readonly, nullable) NSArray<AVAudioSessionChannelDescription *> *channels ``` |

Modified [AVAudioSessionPortDescription.dataSources](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616570-datasources)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *dataSources ``` |
| To | ``` @property(readonly, nullable) NSArray<AVAudioSessionDataSourceDescription *> *dataSources ``` |

Modified [AVAudioSessionRouteDescription.inputs](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutedescription/1616474-inputs)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *inputs ``` |
| To | ``` @property(readonly, nonnull) NSArray<AVAudioSessionPortDescription *> *inputs ``` |

Modified [AVAudioSessionRouteDescription.outputs](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutedescription/1616552-outputs)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *outputs ``` |
| To | ``` @property(readonly, nonnull) NSArray<AVAudioSessionPortDescription *> *outputs ``` |

#### AVAudioTypes.h

Added [AVAudioPacketCount](https://developer.apple.com/documentation/avfoundation/avaudiopacketcount)

#### AVAudioUnit.h

Added [AVAudioUnit.AUAudioUnit](https://developer.apple.com/documentation/avfoundation/avaudiounit/1388167-auaudiounit)Added [+[AVAudioUnit instantiateWithComponentDescription:options:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avaudiounit/1390583-instantiate)Modified [-[AVAudioUnit loadAudioUnitPresetAtURL:error:]](https://developer.apple.com/documentation/avfoundation/avaudiounit/1387527-loadpreset)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)loadAudioUnitPresetAtURL:(NSURL *)url error:(NSError **)error ``` |
| To | ``` - (BOOL)loadAudioUnitPresetAtURL:(NSURL * _Nonnull)url error:(NSError * _Nullable * _Nullable)outError ``` |

#### AVAudioUnitComponent.h (Added)

Added [AVAudioUnitComponent](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent)Added [AVAudioUnitComponent.allTagNames](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387996-alltagnames)Added [AVAudioUnitComponent.audioComponent](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1385910-audiocomponent)Added [AVAudioUnitComponent.audioComponentDescription](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387404-audiocomponentdescription)Added [AVAudioUnitComponent.hasMIDIInput](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1389600-hasmidiinput)Added [AVAudioUnitComponent.hasMIDIOutput](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387070-hasmidioutput)Added [AVAudioUnitComponent.localizedTypeName](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1390541-localizedtypename)Added [AVAudioUnitComponent.manufacturerName](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387472-manufacturername)Added [AVAudioUnitComponent.name](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1385941-name)Added [AVAudioUnitComponent.sandboxSafe](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1390100-sandboxsafe)Added [AVAudioUnitComponent.typeName](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1389988-typename)Added [AVAudioUnitComponent.version](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387762-version)Added [AVAudioUnitComponent.versionString](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1388446-versionstring)Added [AVAudioUnitComponentManager](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager)Added [-[AVAudioUnitComponentManager componentsMatchingDescription:]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1386367-components)Added [-[AVAudioUnitComponentManager componentsMatchingPredicate:]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1386487-components)Added [-[AVAudioUnitComponentManager componentsPassingTest:]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1390260-components)Added [+[AVAudioUnitComponentManager sharedAudioUnitComponentManager]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1390177-sharedaudiounitcomponentmanager)Added [AVAudioUnitComponentManager.standardLocalizedTagNames](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1388545-standardlocalizedtagnames)Added [AVAudioUnitComponentManager.tagNames](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1390133-tagnames)Added [AVAudioUnitComponentTagsDidChangeNotification](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponenttagsdidchangenotification)Added [AVAudioUnitManufacturerNameApple](https://developer.apple.com/documentation/avfoundation/avaudiounitmanufacturernameapple)Added [AVAudioUnitTypeEffect](https://developer.apple.com/documentation/avfoundation/avaudiounittypeeffect)Added [AVAudioUnitTypeFormatConverter](https://developer.apple.com/documentation/avfoundation/avaudiounittypeformatconverter)Added [AVAudioUnitTypeGenerator](https://developer.apple.com/documentation/avfoundation/avaudiounittypegenerator)Added [AVAudioUnitTypeMIDIProcessor](https://developer.apple.com/documentation/avfoundation/avaudiounittypemidiprocessor)Added [AVAudioUnitTypeMixer](https://developer.apple.com/documentation/avfoundation/avaudiounittypemixer)Added [AVAudioUnitTypeMusicDevice](https://developer.apple.com/documentation/avfoundation/avaudiounittypemusicdevice)Added [AVAudioUnitTypeMusicEffect](https://developer.apple.com/documentation/avfoundation/avaudiounittypemusiceffect)Added [AVAudioUnitTypeOfflineEffect](https://developer.apple.com/documentation/avfoundation/avaudiounittypeofflineeffect)Added [AVAudioUnitTypeOutput](https://developer.apple.com/documentation/avfoundation/avaudiounittypeoutput)Added [AVAudioUnitTypePanner](https://developer.apple.com/documentation/avfoundation/avaudiounittypepanner)

#### AVAudioUnitEQ.h

Modified [AVAudioUnitEQ.bands](https://developer.apple.com/documentation/avfoundation/avaudiouniteq/1388840-bands)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *bands ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVAudioUnitEQFilterParameters *> *bands ``` |

#### AVAudioUnitMIDIInstrument.h

Added #def AVAudioUnitMIDIInstrument_MixingConformanceModified [AVAudioUnitMIDIInstrument](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument)

|  | Protocols |
| --- | --- |
| From | -- |
| To | AVAudioMixing |

#### AVAudioUnitSampler.h

Modified [-[AVAudioUnitSampler loadAudioFilesAtURLs:error:]](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1388631-loadaudiofilesaturls)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)loadAudioFilesAtURLs:(NSArray *)audioFiles error:(NSError **)outError ``` |
| To | ``` - (BOOL)loadAudioFilesAtURLs:(NSArray<NSURL *> * _Nonnull)audioFiles error:(NSError * _Nullable * _Nullable)outError ``` |

#### AVBase.h

Added #def AV_GENERICAdded #def AV_GENERIC_CLASSAdded #def AV_INIT_UNAVAILABLEAdded #def AV_PARAMETERIZED_TYPE

#### AVCaptureInput.h

Added [AVCaptureMetadataInput](https://developer.apple.com/documentation/avfoundation/avcapturemetadatainput)Added [-[AVCaptureMetadataInput appendTimedMetadataGroup:error:]](https://developer.apple.com/documentation/avfoundation/avcapturemetadatainput/1622266-append)Added [-[AVCaptureMetadataInput initWithFormatDescription:clock:]](https://developer.apple.com/documentation/avfoundation/avcapturemetadatainput/1622268-init)Added [+[AVCaptureMetadataInput metadataInputWithFormatDescription:clock:]](https://developer.apple.com/documentation/avfoundation/avcapturemetadatainput/1622269-metadatainputwithformatdescripti)Modified [+[AVCaptureDeviceInput deviceInputWithDevice:error:]](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/1450880-deviceinputwithdevice)

|  | Declaration |
| --- | --- |
| From | ``` + (id)deviceInputWithDevice:(AVCaptureDevice *)device error:(NSError **)outError ``` |
| To | ``` + (instancetype)deviceInputWithDevice:(AVCaptureDevice *)device error:(NSError **)outError ``` |

Modified [-[AVCaptureDeviceInput initWithDevice:error:]](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/1387609-initwithdevice)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDevice:(AVCaptureDevice *)device error:(NSError **)outError ``` |
| To | ``` - (instancetype)initWithDevice:(AVCaptureDevice *)device error:(NSError **)outError ``` |

#### AVCaptureOutput.h

Added [-[AVCaptureMovieFileOutput recordsVideoOrientationAndMirroringChangesAsMetadataTrackForConnection:]](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/1616292-recordsvideoorientationandmirror)Added [-[AVCaptureMovieFileOutput setRecordsVideoOrientationAndMirroringChanges:asMetadataTrackForConnection:]](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/1616284-setrecordsvideoorientationandmir)Added [AVCaptureStillImageOutput.lensStabilizationDuringBracketedCaptureEnabled](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616287-lensstabilizationduringbracketed)Added [AVCaptureStillImageOutput.lensStabilizationDuringBracketedCaptureSupported](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616288-islensstabilizationduringbracket)

#### AVCaptureSession.h

Added [AVCaptureSessionInterruptionReason](https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionreason)Added [AVCaptureSessionInterruptionReasonAudioDeviceInUseByAnotherClient](https://developer.apple.com/documentation/avfoundation/avcapturesessioninterruptionreason/avcapturesessioninterruptionreasonaudiodeviceinusebyanotherclient)Added [AVCaptureSessionInterruptionReasonKey](https://developer.apple.com/documentation/avfoundation/avcapturesessioninterruptionreasonkey)Added [AVCaptureSessionInterruptionReasonVideoDeviceInUseByAnotherClient](https://developer.apple.com/documentation/avfoundation/avcapturesessioninterruptionreason/avcapturesessioninterruptionreasonvideodeviceinusebyanotherclient)Added [AVCaptureSessionInterruptionReasonVideoDeviceNotAvailableInBackground](https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionreason/videodevicenotavailableinbackground)Added [AVCaptureSessionInterruptionReasonVideoDeviceNotAvailableWithMultipleForegroundApps](https://developer.apple.com/documentation/avfoundation/avcapturesessioninterruptionreason/avcapturesessioninterruptionreasonvideodevicenotavailablewithmultipleforegroundapps)Added [AVCaptureSessionPreset3840x2160](https://developer.apple.com/documentation/avfoundation/avcapturesession/preset/1620474-hd4k3840x2160)Modified [+[AVCaptureConnection connectionWithInputPort:videoPreviewLayer:]](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1444495-connectionwithinputport)

|  | Declaration |
| --- | --- |
| From | ``` + (AVCaptureConnection *)connectionWithInputPort:(AVCaptureInputPort *)port videoPreviewLayer:(AVCaptureVideoPreviewLayer *)layer ``` |
| To | ``` + (instancetype)connectionWithInputPort:(AVCaptureInputPort *)port videoPreviewLayer:(AVCaptureVideoPreviewLayer *)layer ``` |

Modified [+[AVCaptureConnection connectionWithInputPorts:output:]](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1444473-connectionwithinputports)

|  | Declaration |
| --- | --- |
| From | ``` + (AVCaptureConnection *)connectionWithInputPorts:(NSArray *)ports output:(AVCaptureOutput *)output ``` |
| To | ``` + (instancetype)connectionWithInputPorts:(NSArray *)ports output:(AVCaptureOutput *)output ``` |

Modified [-[AVCaptureConnection initWithInputPort:videoPreviewLayer:]](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1385882-initwithinputport)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithInputPort:(AVCaptureInputPort *)port videoPreviewLayer:(AVCaptureVideoPreviewLayer *)layer ``` |
| To | ``` - (instancetype)initWithInputPort:(AVCaptureInputPort *)port videoPreviewLayer:(AVCaptureVideoPreviewLayer *)layer ``` |

Modified [-[AVCaptureConnection initWithInputPorts:output:]](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1388896-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithInputPorts:(NSArray *)ports output:(AVCaptureOutput *)output ``` |
| To | ``` - (instancetype)initWithInputPorts:(NSArray *)ports output:(AVCaptureOutput *)output ``` |

#### AVCaptureVideoPreviewLayer.h

Modified [-[AVCaptureVideoPreviewLayer initWithSession:]](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/1387766-initwithsession)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithSession:(AVCaptureSession *)session ``` |
| To | ``` - (instancetype)initWithSession:(AVCaptureSession *)session ``` |

Modified [-[AVCaptureVideoPreviewLayer initWithSessionWithNoConnection:]](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/1387426-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithSessionWithNoConnection:(AVCaptureSession *)session ``` |
| To | ``` - (instancetype)initWithSessionWithNoConnection:(AVCaptureSession *)session ``` |

Modified [+[AVCaptureVideoPreviewLayer layerWithSession:]](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/1567198-layerwithsession)

|  | Declaration |
| --- | --- |
| From | ``` + (id)layerWithSession:(AVCaptureSession *)session ``` |
| To | ``` + (instancetype)layerWithSession:(AVCaptureSession *)session ``` |

Modified [+[AVCaptureVideoPreviewLayer layerWithSessionWithNoConnection:]](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/1567197-layerwithsessionwithnoconnection)

|  | Declaration |
| --- | --- |
| From | ``` + (id)layerWithSessionWithNoConnection:(AVCaptureSession *)session ``` |
| To | ``` + (instancetype)layerWithSessionWithNoConnection:(AVCaptureSession *)session ``` |

#### AVComposition.h

Added [-[AVComposition tracksWithMediaCharacteristic:]](https://developer.apple.com/documentation/avfoundation/avcomposition/1387525-trackswithmediacharacteristic)Added [-[AVComposition tracksWithMediaType:]](https://developer.apple.com/documentation/avfoundation/avcomposition/1386534-trackswithmediatype)Added [-[AVComposition trackWithTrackID:]](https://developer.apple.com/documentation/avfoundation/avcomposition/1388473-track)Added [AVComposition.URLAssetInitializationOptions](https://developer.apple.com/documentation/avfoundation/avcomposition/1387080-urlassetinitializationoptions)Added [+[AVMutableComposition compositionWithURLAssetInitializationOptions:]](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1390705-compositionwithurlassetinitializ)Added [-[AVMutableComposition tracksWithMediaCharacteristic:]](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1388464-trackswithmediacharacteristic)Added [-[AVMutableComposition tracksWithMediaType:]](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1385724-trackswithmediatype)Added [-[AVMutableComposition trackWithTrackID:]](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1390074-track)Added AVComposition(AVCompositionTrackInspection)Added AVMutableComposition(AVMutableCompositionTrackInspection)Modified [AVComposition.tracks](https://developer.apple.com/documentation/avfoundation/avcomposition/1390165-tracks)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *tracks ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVCompositionTrack *> *tracks ``` |

Modified [+[AVMutableComposition composition]](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1495098-composition)

|  | Declaration |
| --- | --- |
| From | ``` + (AVMutableComposition *)composition ``` |
| To | ``` + (instancetype _Nonnull)composition ``` |

Modified [AVMutableComposition.tracks](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1389937-tracks)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *tracks ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVMutableCompositionTrack *> *tracks ``` |

#### AVCompositionTrack.h

Modified [AVCompositionTrack.segments](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/1387267-segments)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *segments ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<AVCompositionTrackSegment *> *segments ``` |

Modified [-[AVMutableCompositionTrack insertTimeRange:ofTrack:atTime:error:]](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/1390691-inserttimerange)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)insertTimeRange:(CMTimeRange)timeRange ofTrack:(AVAssetTrack *)track atTime:(CMTime)startTime error:(NSError **)error ``` |
| To | ``` - (BOOL)insertTimeRange:(CMTimeRange)timeRange ofTrack:(AVAssetTrack * _Nonnull)track atTime:(CMTime)startTime error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [-[AVMutableCompositionTrack insertTimeRanges:ofTracks:atTime:error:]](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/1388629-inserttimeranges)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)insertTimeRanges:(NSArray *)timeRanges ofTracks:(NSArray *)tracks atTime:(CMTime)startTime error:(NSError **)error ``` |
| To | ``` - (BOOL)insertTimeRanges:(NSArray<NSValue *> * _Nonnull)timeRanges ofTracks:(NSArray<AVAssetTrack *> * _Nonnull)tracks atTime:(CMTime)startTime error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [AVMutableCompositionTrack.segments](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/1390321-segments)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *segments ``` |
| To | ``` @property(nonatomic, copy) NSArray<AVCompositionTrackSegment *> * _Null_unspecified segments ``` |

Modified [-[AVMutableCompositionTrack validateTrackSegments:error:]](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/1388746-validatesegments)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)validateTrackSegments:(NSArray *)trackSegments error:(NSError **)error ``` |
| To | ``` - (BOOL)validateTrackSegments:(NSArray<AVCompositionTrackSegment *> * _Nonnull)trackSegments error:(NSError * _Nullable * _Nullable)outError ``` |

#### AVCompositionTrackSegment.h

Modified [+[AVCompositionTrackSegment compositionTrackSegmentWithTimeRange:]](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/1400556-compositiontracksegmentwithtimer)

|  | Declaration |
| --- | --- |
| From | ``` + (AVCompositionTrackSegment *)compositionTrackSegmentWithTimeRange:(CMTimeRange)timeRange ``` |
| To | ``` + (instancetype _Nonnull)compositionTrackSegmentWithTimeRange:(CMTimeRange)timeRange ``` |

Modified [+[AVCompositionTrackSegment compositionTrackSegmentWithURL:trackID:sourceTimeRange:targetTimeRange:]](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/1400552-compositiontracksegmentwithurl)

|  | Declaration |
| --- | --- |
| From | ``` + (AVCompositionTrackSegment *)compositionTrackSegmentWithURL:(NSURL *)URL trackID:(CMPersistentTrackID)trackID sourceTimeRange:(CMTimeRange)sourceTimeRange targetTimeRange:(CMTimeRange)targetTimeRange ``` |
| To | ``` + (instancetype _Nonnull)compositionTrackSegmentWithURL:(NSURL * _Nonnull)URL trackID:(CMPersistentTrackID)trackID sourceTimeRange:(CMTimeRange)sourceTimeRange targetTimeRange:(CMTimeRange)targetTimeRange ``` |

Modified [-[AVCompositionTrackSegment initWithTimeRange:]](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/1386841-initwithtimerange)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[AVCompositionTrackSegment initWithURL:trackID:sourceTimeRange:targetTimeRange:]](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/1390282-initwithurl)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### AVError.h

Added [AVErrorRecordingAlreadyInProgress](https://developer.apple.com/documentation/avfoundation/averror/averrorrecordingalreadyinprogress)Added [AVErrorVideoCompositorFailed](https://developer.apple.com/documentation/avfoundation/averror/code/videocompositorfailed)Modified [AVErrorDeviceIsNotAvailableInBackground](https://developer.apple.com/documentation/avfoundation/averror/averrordeviceisnotavailableinbackground)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### AVMediaFormat.h

Added [AVFileTypeEnhancedAC3](https://developer.apple.com/documentation/avfoundation/avfiletype/1387645-eac3)Added [AVMediaCharacteristicDubbedTranslation](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/1387476-dubbedtranslation)Added [AVMediaCharacteristicLanguageTranslation](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/1388194-languagetranslation)Added [AVMediaCharacteristicVoiceOverTranslation](https://developer.apple.com/documentation/avfoundation/avmediacharacteristicvoiceovertranslation)Added [AVMediaTypeMetadataObject](https://developer.apple.com/documentation/avfoundation/avmediatypemetadataobject)Added [AVStreamingKeyDeliveryContentKeyType](https://developer.apple.com/documentation/avfoundation/avstreamingkeydeliverycontentkeytype)Added [AVStreamingKeyDeliveryPersistentContentKeyType](https://developer.apple.com/documentation/avfoundation/avstreamingkeydeliverypersistentcontentkeytype)Modified [AVFileType3GPP2](https://developer.apple.com/documentation/avfoundation/avfiletype/1388141-mobile3gpp2)

|  | Introduction |
| --- | --- |
| From | iOS 7.0 |
| To | iOS 4.0 |

#### AVMediaSelection.h (Added)

Added [AVMediaSelection](https://developer.apple.com/documentation/avfoundation/avmediaselection)Added [AVMediaSelection.asset](https://developer.apple.com/documentation/avfoundation/avmediaselection/1390874-asset)Added [-[AVMediaSelection mediaSelectionCriteriaCanBeAppliedAutomaticallyToMediaSelectionGroup:]](https://developer.apple.com/documentation/avfoundation/avmediaselection/1386716-mediaselectioncriteriacanbeappli)Added [-[AVMediaSelection selectedMediaOptionInMediaSelectionGroup:]](https://developer.apple.com/documentation/avfoundation/avmediaselection/1389197-selectedmediaoption)Added [AVMutableMediaSelection](https://developer.apple.com/documentation/avfoundation/avmutablemediaselection)Added [-[AVMutableMediaSelection selectMediaOption:inMediaSelectionGroup:]](https://developer.apple.com/documentation/avfoundation/avmutablemediaselection/1386768-selectmediaoption)

#### AVMediaSelectionGroup.h

Modified [+[AVMediaSelectionGroup mediaSelectionOptionsFromArray:filteredAndSortedAccordingToPreferredLanguages:]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1387034-mediaselectionoptions)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)mediaSelectionOptionsFromArray:(NSArray *)mediaSelectionOptions filteredAndSortedAccordingToPreferredLanguages:(NSArray *)preferredLanguages ``` |
| To | ``` + (NSArray<AVMediaSelectionOption *> * _Nonnull)mediaSelectionOptionsFromArray:(NSArray<AVMediaSelectionOption *> * _Nonnull)mediaSelectionOptions filteredAndSortedAccordingToPreferredLanguages:(NSArray<NSString *> * _Nonnull)preferredLanguages ``` |

Modified [+[AVMediaSelectionGroup mediaSelectionOptionsFromArray:withLocale:]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1387494-mediaselectionoptionsfromarray)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)mediaSelectionOptionsFromArray:(NSArray *)mediaSelectionOptions withLocale:(NSLocale *)locale ``` |
| To | ``` + (NSArray<AVMediaSelectionOption *> * _Nonnull)mediaSelectionOptionsFromArray:(NSArray<AVMediaSelectionOption *> * _Nonnull)mediaSelectionOptions withLocale:(NSLocale * _Nonnull)locale ``` |

Modified [+[AVMediaSelectionGroup mediaSelectionOptionsFromArray:withMediaCharacteristics:]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1388258-mediaselectionoptions)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)mediaSelectionOptionsFromArray:(NSArray *)mediaSelectionOptions withMediaCharacteristics:(NSArray *)mediaCharacteristics ``` |
| To | ``` + (NSArray<AVMediaSelectionOption *> * _Nonnull)mediaSelectionOptionsFromArray:(NSArray<AVMediaSelectionOption *> * _Nonnull)mediaSelectionOptions withMediaCharacteristics:(NSArray<NSString *> * _Nonnull)mediaCharacteristics ``` |

Modified [+[AVMediaSelectionGroup mediaSelectionOptionsFromArray:withoutMediaCharacteristics:]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1387631-mediaselectionoptionsfromarray)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)mediaSelectionOptionsFromArray:(NSArray *)mediaSelectionOptions withoutMediaCharacteristics:(NSArray *)mediaCharacteristics ``` |
| To | ``` + (NSArray<AVMediaSelectionOption *> * _Nonnull)mediaSelectionOptionsFromArray:(NSArray<AVMediaSelectionOption *> * _Nonnull)mediaSelectionOptions withoutMediaCharacteristics:(NSArray<NSString *> * _Nonnull)mediaCharacteristics ``` |

Modified [AVMediaSelectionGroup.options](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1388351-options)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *options ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVMediaSelectionOption *> *options ``` |

Modified [+[AVMediaSelectionGroup playableMediaSelectionOptionsFromArray:]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1387351-playablemediaselectionoptions)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)playableMediaSelectionOptionsFromArray:(NSArray *)mediaSelectionOptions ``` |
| To | ``` + (NSArray<AVMediaSelectionOption *> * _Nonnull)playableMediaSelectionOptionsFromArray:(NSArray<AVMediaSelectionOption *> * _Nonnull)mediaSelectionOptions ``` |

Modified [AVMediaSelectionOption.availableMetadataFormats](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1389504-availablemetadataformats)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *availableMetadataFormats ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *availableMetadataFormats ``` |

Modified [AVMediaSelectionOption.commonMetadata](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1387859-commonmetadata)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *commonMetadata ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVMetadataItem *> *commonMetadata ``` |

Modified [AVMediaSelectionOption.mediaSubTypes](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1385587-mediasubtypes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *mediaSubTypes ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSNumber *> *mediaSubTypes ``` |

Modified [-[AVMediaSelectionOption metadataForFormat:]](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1386666-metadataforformat)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)metadataForFormat:(NSString *)format ``` |
| To | ``` - (NSArray<AVMetadataItem *> * _Nonnull)metadataForFormat:(NSString * _Nonnull)format ``` |

#### AVMetadataFormat.h

Added [AVMetadataExtraAttributeInfoKey](https://developer.apple.com/documentation/avfoundation/avmetadataextraattributekey/1388595-info)Added [AVMetadataID3MetadataKeyCommercial](https://developer.apple.com/documentation/avfoundation/avmetadataid3metadatakeycommercial)Added [AVMetadataQuickTimeMetadataKeyContentIdentifier](https://developer.apple.com/documentation/avfoundation/avmetadataquicktimemetadatakeycontentidentifier)Modified [AVMetadataID3MetadataKeyCommerical](https://developer.apple.com/documentation/avfoundation/avmetadataid3metadatakeycommerical)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### AVMetadataIdentifiers.h

Added [AVMetadataIdentifierID3MetadataCommercial](https://developer.apple.com/documentation/avfoundation/avmetadataidentifier/1389685-id3metadatacommercial)Added [AVMetadataIdentifierQuickTimeMetadataContentIdentifier](https://developer.apple.com/documentation/avfoundation/avmetadataidentifierquicktimemetadatacontentidentifier)Added [AVMetadataIdentifierQuickTimeMetadataDetectedFace](https://developer.apple.com/documentation/avfoundation/avmetadataidentifierquicktimemetadatadetectedface)Added [AVMetadataIdentifierQuickTimeMetadataVideoOrientation](https://developer.apple.com/documentation/avfoundation/avmetadataidentifierquicktimemetadatavideoorientation)Modified [AVMetadataIdentifierID3MetadataCommerical](https://developer.apple.com/documentation/avfoundation/avmetadataidentifier/1388551-id3metadatacommerical)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### AVMetadataItem.h

Added [+[AVMetadataItem metadataItemWithPropertiesOfMetadataItem:valueLoadingHandler:]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387745-init)Added [AVMetadataItem.startDate](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1388535-startdate)Added [AVMetadataItemValueRequest](https://developer.apple.com/documentation/avfoundation/avmetadataitemvaluerequest)Added [AVMetadataItemValueRequest.metadataItem](https://developer.apple.com/documentation/avfoundation/avmetadataitemvaluerequest/1388069-metadataitem)Added [-[AVMetadataItemValueRequest respondWithError:]](https://developer.apple.com/documentation/avfoundation/avmetadataitemvaluerequest/1390783-respondwitherror)Added [-[AVMetadataItemValueRequest respondWithValue:]](https://developer.apple.com/documentation/avfoundation/avmetadataitemvaluerequest/1386820-respondwithvalue)Added [AVMutableMetadataItem.startDate](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1389966-startdate)Added AVMetadataItem(AVMetadataItemDateRepresentation)Added AVMetadataItem(AVMetadataItemLazyValueLoading)Added AVMutableMetadataItem(AVMutableMetadataItemDateRepresentation)Modified [AVMetadataItem.commonKey](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1389864-commonkey)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *commonKey ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *commonKey ``` |

Modified [AVMetadataItem.dataType](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1386856-datatype)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *dataType ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *dataType ``` |

Modified [AVMetadataItem.dataValue](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387641-datavalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSData *dataValue ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSData *dataValue ``` |

Modified [AVMetadataItem.dateValue](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1385563-datevalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSDate *dateValue ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSDate *dateValue ``` |

Modified [AVMetadataItem.duration](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1386610-duration)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) CMTime duration ``` |
| To | ``` @property(nonatomic, readonly) CMTime duration ``` |

Modified [AVMetadataItem.extendedLanguageTag](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387068-extendedlanguagetag)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *extendedLanguageTag ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *extendedLanguageTag ``` |

Modified [AVMetadataItem.extraAttributes](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1389570-extraattributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *extraAttributes ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSDictionary<NSString *,id> *extraAttributes ``` |

Modified [AVMetadataItem.identifier](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1386968-identifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *identifier ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *identifier ``` |

Modified [AVMetadataItem.key](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387843-key)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) id<NSObject, NSCopying> key ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) id<NSObject, NSCopying> key ``` |

Modified [AVMetadataItem.keySpace](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1385757-keyspace)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *keySpace ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *keySpace ``` |

Modified [-[AVMetadataItem loadValuesAsynchronouslyForKeys:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387102-loadvaluesasynchronouslyforkeys)

|  | Declaration |
| --- | --- |
| From | ``` - (void)loadValuesAsynchronouslyForKeys:(NSArray *)keys completionHandler:(void (^)(void))handler ``` |
| To | ``` - (void)loadValuesAsynchronouslyForKeys:(NSArray<NSString *> * _Nonnull)keys completionHandler:(void (^ _Nullable)(void))handler ``` |

Modified [AVMetadataItem.locale](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387114-locale)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSLocale *locale ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSLocale *locale ``` |

Modified [+[AVMetadataItem metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387901-metadataitemsfromarray)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)metadataItemsFromArray:(NSArray *)metadataItems filteredAndSortedAccordingToPreferredLanguages:(NSArray *)preferredLanguages ``` |
| To | ``` + (NSArray<AVMetadataItem *> * _Nonnull)metadataItemsFromArray:(NSArray<AVMetadataItem *> * _Nonnull)metadataItems filteredAndSortedAccordingToPreferredLanguages:(NSArray<NSString *> * _Nonnull)preferredLanguages ``` |

Modified [+[AVMetadataItem metadataItemsFromArray:filteredByIdentifier:]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1385843-metadataitems)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)metadataItemsFromArray:(NSArray *)metadataItems filteredByIdentifier:(NSString *)identifier ``` |
| To | ``` + (NSArray<AVMetadataItem *> * _Nonnull)metadataItemsFromArray:(NSArray<AVMetadataItem *> * _Nonnull)metadataItems filteredByIdentifier:(NSString * _Nonnull)identifier ``` |

Modified [+[AVMetadataItem metadataItemsFromArray:filteredByMetadataItemFilter:]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1390238-metadataitemsfromarray)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)metadataItemsFromArray:(NSArray *)metadataItems filteredByMetadataItemFilter:(AVMetadataItemFilter *)metadataItemFilter ``` |
| To | ``` + (NSArray<AVMetadataItem *> * _Nonnull)metadataItemsFromArray:(NSArray<AVMetadataItem *> * _Nonnull)metadataItems filteredByMetadataItemFilter:(AVMetadataItemFilter * _Nonnull)metadataItemFilter ``` |

Modified [+[AVMetadataItem metadataItemsFromArray:withKey:keySpace:]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1386083-metadataitems)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)metadataItemsFromArray:(NSArray *)metadataItems withKey:(id)key keySpace:(NSString *)keySpace ``` |
| To | ``` + (NSArray<AVMetadataItem *> * _Nonnull)metadataItemsFromArray:(NSArray<AVMetadataItem *> * _Nonnull)metadataItems withKey:(id _Nullable)key keySpace:(NSString * _Nullable)keySpace ``` |

Modified [+[AVMetadataItem metadataItemsFromArray:withLocale:]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1389374-metadataitemsfromarray)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)metadataItemsFromArray:(NSArray *)metadataItems withLocale:(NSLocale *)locale ``` |
| To | ``` + (NSArray<AVMetadataItem *> * _Nonnull)metadataItemsFromArray:(NSArray<AVMetadataItem *> * _Nonnull)metadataItems withLocale:(NSLocale * _Nonnull)locale ``` |

Modified [AVMetadataItem.numberValue](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1390681-numbervalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSNumber *numberValue ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSNumber *numberValue ``` |

Modified [AVMetadataItem.stringValue](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1390846-stringvalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *stringValue ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSString *stringValue ``` |

Modified [AVMetadataItem.time](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1388612-time)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) CMTime time ``` |
| To | ``` @property(nonatomic, readonly) CMTime time ``` |

Modified [AVMetadataItem.value](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1390537-value)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) id<NSObject, NSCopying> value ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) id<NSObject, NSCopying> value ``` |

Modified [AVMutableMetadataItem.dataType](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1389471-datatype)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, copy) NSString *dataType ``` |
| To | ``` @property(nonatomic, readwrite, copy, nullable) NSString *dataType ``` |

Modified [AVMutableMetadataItem.duration](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1389980-duration)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite) CMTime duration ``` |
| To | ``` @property(nonatomic, readwrite) CMTime duration ``` |

Modified [AVMutableMetadataItem.extendedLanguageTag](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1386664-extendedlanguagetag)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, copy) NSString *extendedLanguageTag ``` |
| To | ``` @property(nonatomic, readwrite, copy, nullable) NSString *extendedLanguageTag ``` |

Modified [AVMutableMetadataItem.extraAttributes](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1390397-extraattributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, copy) NSDictionary *extraAttributes ``` |
| To | ``` @property(nonatomic, readwrite, copy, nullable) NSDictionary<NSString *,id> *extraAttributes ``` |

Modified [AVMutableMetadataItem.identifier](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1386688-identifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, copy) NSString *identifier ``` |
| To | ``` @property(nonatomic, readwrite, copy, nullable) NSString *identifier ``` |

Modified [AVMutableMetadataItem.key](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1386776-key)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, copy) id<NSObject, NSCopying> key ``` |
| To | ``` @property(nonatomic, readwrite, copy, nullable) id<NSObject, NSCopying> key ``` |

Modified [AVMutableMetadataItem.keySpace](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1385655-keyspace)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, copy) NSString *keySpace ``` |
| To | ``` @property(nonatomic, readwrite, copy, nullable) NSString *keySpace ``` |

Modified [AVMutableMetadataItem.locale](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1389292-locale)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, copy) NSLocale *locale ``` |
| To | ``` @property(nonatomic, readwrite, copy, nullable) NSLocale *locale ``` |

Modified [AVMutableMetadataItem.time](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1389990-time)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite) CMTime time ``` |
| To | ``` @property(nonatomic, readwrite) CMTime time ``` |

Modified [AVMutableMetadataItem.value](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1388296-value)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, copy) id<NSObject, NSCopying> value ``` |
| To | ``` @property(nonatomic, readwrite, copy, nullable) id<NSObject, NSCopying> value ``` |

#### AVOutputSettingsAssistant.h

Added [AVOutputSettingsPreset3840x2160](https://developer.apple.com/documentation/avfoundation/avoutputsettingspreset/1388286-preset3840x2160)Modified [AVOutputSettingsAssistant.audioSettings](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1386233-audiosettings)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDictionary *audioSettings ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSDictionary<NSString *,id> *audioSettings ``` |

Modified [+[AVOutputSettingsAssistant availableOutputSettingsPresets]](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1388118-availableoutputsettingspresets)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)availableOutputSettingsPresets ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)availableOutputSettingsPresets ``` |

Modified [AVOutputSettingsAssistant.videoSettings](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1386880-videosettings)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDictionary *videoSettings ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSDictionary<NSString *,id> *videoSettings ``` |

#### AVPlayer.h

Modified [-[AVPlayer addBoundaryTimeObserverForTimes:queue:usingBlock:]](https://developer.apple.com/documentation/avfoundation/avplayer/1388027-addboundarytimeobserver)

|  | Declaration |
| --- | --- |
| From | ``` - (id)addBoundaryTimeObserverForTimes:(NSArray *)times queue:(dispatch_queue_t)queue usingBlock:(void (^)(void))block ``` |
| To | ``` - (id _Nonnull)addBoundaryTimeObserverForTimes:(NSArray<NSValue *> * _Nonnull)times queue:(dispatch_queue_t _Nullable)queue usingBlock:(void (^ _Nonnull)(void))block ``` |

Modified [+[AVPlayer playerWithPlayerItem:]](https://developer.apple.com/documentation/avfoundation/avplayer/1538390-playerwithplayeritem)

|  | Declaration |
| --- | --- |
| From | ``` + (id)playerWithPlayerItem:(AVPlayerItem *)item ``` |
| To | ``` + (instancetype _Nonnull)playerWithPlayerItem:(AVPlayerItem * _Nonnull)item ``` |

Modified [+[AVPlayer playerWithURL:]](https://developer.apple.com/documentation/avfoundation/avplayer/1538409-playerwithurl)

|  | Declaration |
| --- | --- |
| From | ``` + (id)playerWithURL:(NSURL *)URL ``` |
| To | ``` + (instancetype _Nonnull)playerWithURL:(NSURL * _Nonnull)URL ``` |

Modified [-[AVQueuePlayer initWithItems:]](https://developer.apple.com/documentation/avfoundation/avqueueplayer/1389345-initwithitems)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithItems:(NSArray *)items ``` |
| To | ``` - (AVQueuePlayer * _Nonnull)initWithItems:(NSArray<AVPlayerItem *> * _Nonnull)items ``` |

Modified [-[AVQueuePlayer items]](https://developer.apple.com/documentation/avfoundation/avqueueplayer/1390539-items)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)items ``` |
| To | ``` - (NSArray<AVPlayerItem *> * _Nonnull)items ``` |

Modified [+[AVQueuePlayer queuePlayerWithItems:]](https://developer.apple.com/documentation/avfoundation/avqueueplayer/1538384-queueplayerwithitems)

|  | Declaration |
| --- | --- |
| From | ``` + (id)queuePlayerWithItems:(NSArray *)items ``` |
| To | ``` + (instancetype _Nonnull)queuePlayerWithItems:(NSArray<AVPlayerItem *> * _Nonnull)items ``` |

#### AVPlayerItem.h

Added [AVPlayerItem.canUseNetworkResourcesForLiveStreamingWhilePaused](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388752-canusenetworkresourcesforlivestr)Added [AVPlayerItem.currentMediaSelection](https://developer.apple.com/documentation/avfoundation/avplayeritem/1386519-currentmediaselection)Modified [AVPlayerItem.automaticallyLoadedAssetKeys](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388633-automaticallyloadedassetkeys)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *automaticallyLoadedAssetKeys ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *automaticallyLoadedAssetKeys ``` |

Modified [-[AVPlayerItem initWithAsset:automaticallyLoadedAssetKeys:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387529-initwithasset)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithAsset:(AVAsset *)asset automaticallyLoadedAssetKeys:(NSArray *)automaticallyLoadedAssetKeys ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithAsset:(AVAsset * _Nonnull)asset automaticallyLoadedAssetKeys:(NSArray<NSString *> * _Nullable)automaticallyLoadedAssetKeys ``` | yes |

Modified [AVPlayerItem.loadedTimeRanges](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389953-loadedtimeranges)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *loadedTimeRanges ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSValue *> *loadedTimeRanges ``` |

Modified [AVPlayerItem.outputs](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389090-outputs)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *outputs ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVPlayerItemOutput *> *outputs ``` |

Modified [+[AVPlayerItem playerItemWithAsset:automaticallyLoadedAssetKeys:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1588088-playeritemwithasset)

|  | Declaration |
| --- | --- |
| From | ``` + (AVPlayerItem *)playerItemWithAsset:(AVAsset *)asset automaticallyLoadedAssetKeys:(NSArray *)automaticallyLoadedAssetKeys ``` |
| To | ``` + (AVPlayerItem * _Nonnull)playerItemWithAsset:(AVAsset * _Nonnull)asset automaticallyLoadedAssetKeys:(NSArray<NSString *> * _Nullable)automaticallyLoadedAssetKeys ``` |

Modified [AVPlayerItem.seekableTimeRanges](https://developer.apple.com/documentation/avfoundation/avplayeritem/1386155-seekabletimeranges)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *seekableTimeRanges ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSValue *> *seekableTimeRanges ``` |

Modified [AVPlayerItem.textStyleRules](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389681-textstylerules)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *textStyleRules ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<AVTextStyleRule *> *textStyleRules ``` |

Modified [AVPlayerItem.timedMetadata](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389602-timedmetadata)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *timedMetadata ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<AVMetadataItem *> *timedMetadata ``` |

Modified [AVPlayerItem.tracks](https://developer.apple.com/documentation/avfoundation/avplayeritem/1386361-tracks)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *tracks ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVPlayerItemTrack *> *tracks ``` |

Modified [AVPlayerItemAccessLog.events](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslog/1387406-events)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *events ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVPlayerItemAccessLogEvent *> *events ``` |

Modified [AVPlayerItemErrorLog.events](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlog/1387637-events)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *events ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVPlayerItemErrorLogEvent *> *events ``` |

#### AVPlayerItemOutput.h

Modified [AVPlayerItemLegibleOutput.delegate](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/1387877-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id<AVPlayerItemLegibleOutputPushDelegate> delegate ``` |
| To | ``` @property(nonatomic, readonly, weak, nullable) id<AVPlayerItemLegibleOutputPushDelegate> delegate ``` |

Modified [-[AVPlayerItemLegibleOutput initWithMediaSubtypesForNativeRepresentation:]](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/1390500-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithMediaSubtypesForNativeRepresentation:(NSArray *)subtypes ``` |
| To | ``` - (instancetype _Nonnull)initWithMediaSubtypesForNativeRepresentation:(NSArray<NSNumber *> * _Nonnull)subtypes ``` |

Modified [-[AVPlayerItemLegibleOutputPushDelegate legibleOutput:didOutputAttributedStrings:nativeSampleBuffers:forItemTime:]](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutputpushdelegate/1386790-legibleoutput)

|  | Declaration |
| --- | --- |
| From | ``` - (void)legibleOutput:(AVPlayerItemLegibleOutput *)output didOutputAttributedStrings:(NSArray *)strings nativeSampleBuffers:(NSArray *)nativeSamples forItemTime:(CMTime)itemTime ``` |
| To | ``` - (void)legibleOutput:(AVPlayerItemLegibleOutput * _Nonnull)output didOutputAttributedStrings:(NSArray<NSAttributedString *> * _Nonnull)strings nativeSampleBuffers:(NSArray * _Nonnull)nativeSamples forItemTime:(CMTime)itemTime ``` |

Modified [AVPlayerItemMetadataOutput.delegate](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput/1387200-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id<AVPlayerItemMetadataOutputPushDelegate> delegate ``` |
| To | ``` @property(nonatomic, readonly, weak, nullable) id<AVPlayerItemMetadataOutputPushDelegate> delegate ``` |

Modified [-[AVPlayerItemMetadataOutput initWithIdentifiers:]](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput/1390205-initwithidentifiers)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithIdentifiers:(NSArray *)identifiers ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithIdentifiers:(NSArray<NSString *> * _Nullable)identifiers ``` | yes |

Modified [-[AVPlayerItemMetadataOutputPushDelegate metadataOutput:didOutputTimedMetadataGroups:fromPlayerItemTrack:]](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutputpushdelegate/1388071-metadataoutput)

|  | Declaration |
| --- | --- |
| From | ``` - (void)metadataOutput:(AVPlayerItemMetadataOutput *)output didOutputTimedMetadataGroups:(NSArray *)groups fromPlayerItemTrack:(AVPlayerItemTrack *)track ``` |
| To | ``` - (void)metadataOutput:(AVPlayerItemMetadataOutput * _Nonnull)output didOutputTimedMetadataGroups:(NSArray<AVTimedMetadataGroup *> * _Nonnull)groups fromPlayerItemTrack:(AVPlayerItemTrack * _Nonnull)track ``` |

Modified [AVPlayerItemVideoOutput.delegate](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1385827-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id<AVPlayerItemOutputPullDelegate> delegate ``` |
| To | ``` @property(nonatomic, readonly, assign, nullable) id<AVPlayerItemOutputPullDelegate> delegate ``` |

Modified [-[AVPlayerItemVideoOutput initWithPixelBufferAttributes:]](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1389231-initwithpixelbufferattributes)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithPixelBufferAttributes:(NSDictionary *)pixelBufferAttributes ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithPixelBufferAttributes:(NSDictionary<NSString *,id> * _Nullable)pixelBufferAttributes ``` | yes |

#### AVPlayerLayer.h

Added [AVPlayerLayer.pixelBufferAttributes](https://developer.apple.com/documentation/avfoundation/avplayerlayer/1390055-pixelbufferattributes)

#### AVPlayerMediaSelectionCriteria.h

Modified [-[AVPlayerMediaSelectionCriteria initWithPreferredLanguages:preferredMediaCharacteristics:]](https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria/1387627-initwithpreferredlanguages)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithPreferredLanguages:(NSArray *)preferredLanguages preferredMediaCharacteristics:(NSArray *)preferredMediaCharacteristics ``` |
| To | ``` - (instancetype _Nonnull)initWithPreferredLanguages:(NSArray<NSString *> * _Nullable)preferredLanguages preferredMediaCharacteristics:(NSArray<NSString *> * _Nullable)preferredMediaCharacteristics ``` |

Modified [AVPlayerMediaSelectionCriteria.preferredLanguages](https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria/1388559-preferredlanguages)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *preferredLanguages ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<NSString *> *preferredLanguages ``` |

Modified [AVPlayerMediaSelectionCriteria.preferredMediaCharacteristics](https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria/1385734-preferredmediacharacteristics)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *preferredMediaCharacteristics ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<NSString *> *preferredMediaCharacteristics ``` |

#### AVSpeechSynthesis.h

Added [AVSpeechSynthesisVoice.identifier](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619670-identifier)Added [AVSpeechSynthesisVoice.name](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619669-name)Added [AVSpeechSynthesisVoice.quality](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619688-quality)Added [+[AVSpeechSynthesisVoice voiceWithIdentifier:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619711-voicewithidentifier)Added [AVSpeechSynthesisVoiceIdentifierAlex](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoiceidentifieralex)Added [AVSpeechSynthesisVoiceQuality](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoicequality)Added [AVSpeechSynthesisVoiceQualityDefault](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoicequality/default)Added [AVSpeechSynthesisVoiceQualityEnhanced](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoicequality/enhanced)Modified [+[AVSpeechSynthesisVoice speechVoices]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619697-speechvoices)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)speechVoices ``` |
| To | ``` + (NSArray<AVSpeechSynthesisVoice *> * _Nonnull)speechVoices ``` |

Modified [+[AVSpeechSynthesisVoice voiceWithLanguage:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619699-init)

|  | Declaration |
| --- | --- |
| From | ``` + (AVSpeechSynthesisVoice *)voiceWithLanguage:(NSString *)language ``` |
| To | ``` + (AVSpeechSynthesisVoice * _Nullable)voiceWithLanguage:(NSString * _Nullable)languageCode ``` |

#### AVTextStyleRule.h

Modified [-[AVTextStyleRule initWithTextMarkupAttributes:]](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1385849-initwithtextmarkupattributes)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithTextMarkupAttributes:(NSDictionary *)textMarkupAttributes ``` |
| To | ``` - (instancetype _Nullable)initWithTextMarkupAttributes:(NSDictionary<NSString *,id> * _Nonnull)textMarkupAttributes ``` |

Modified [-[AVTextStyleRule initWithTextMarkupAttributes:textSelector:]](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1389854-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithTextMarkupAttributes:(NSDictionary *)textMarkupAttributes textSelector:(NSString *)textSelector ``` | -- |
| To | ``` - (instancetype _Nullable)initWithTextMarkupAttributes:(NSDictionary<NSString *,id> * _Nonnull)textMarkupAttributes textSelector:(NSString * _Nullable)textSelector ``` | yes |

Modified [+[AVTextStyleRule propertyListForTextStyleRules:]](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1387970-propertylistfortextstylerules)

|  | Declaration |
| --- | --- |
| From | ``` + (id)propertyListForTextStyleRules:(NSArray *)textStyleRules ``` |
| To | ``` + (id _Nonnull)propertyListForTextStyleRules:(NSArray<AVTextStyleRule *> * _Nonnull)textStyleRules ``` |

Modified [AVTextStyleRule.textMarkupAttributes](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1387945-textmarkupattributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDictionary *textMarkupAttributes ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSDictionary<NSString *,id> *textMarkupAttributes ``` |

Modified [+[AVTextStyleRule textStyleRulesFromPropertyList:]](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1387802-textstylerulesfrompropertylist)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)textStyleRulesFromPropertyList:(id)plist ``` |
| To | ``` + (NSArray<AVTextStyleRule *> * _Nullable)textStyleRulesFromPropertyList:(id _Nonnull)plist ``` |

Modified [+[AVTextStyleRule textStyleRuleWithTextMarkupAttributes:]](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1584360-textstylerulewithtextmarkupattri)

|  | Declaration |
| --- | --- |
| From | ``` + (AVTextStyleRule *)textStyleRuleWithTextMarkupAttributes:(NSDictionary *)textMarkupAttributes ``` |
| To | ``` + (AVTextStyleRule * _Nullable)textStyleRuleWithTextMarkupAttributes:(NSDictionary<NSString *,id> * _Nonnull)textMarkupAttributes ``` |

Modified [+[AVTextStyleRule textStyleRuleWithTextMarkupAttributes:textSelector:]](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1584361-textstylerulewithtextmarkupattri)

|  | Declaration |
| --- | --- |
| From | ``` + (AVTextStyleRule *)textStyleRuleWithTextMarkupAttributes:(NSDictionary *)textMarkupAttributes textSelector:(NSString *)textSelector ``` |
| To | ``` + (AVTextStyleRule * _Nullable)textStyleRuleWithTextMarkupAttributes:(NSDictionary<NSString *,id> * _Nonnull)textMarkupAttributes textSelector:(NSString * _Nullable)textSelector ``` |

#### AVTimedMetadataGroup.h

Added [AVDateRangeMetadataGroup](https://developer.apple.com/documentation/avfoundation/avdaterangemetadatagroup)Added [AVDateRangeMetadataGroup.endDate](https://developer.apple.com/documentation/avfoundation/avdaterangemetadatagroup/1386255-enddate)Added [-[AVDateRangeMetadataGroup initWithItems:startDate:endDate:]](https://developer.apple.com/documentation/avfoundation/avdaterangemetadatagroup/1389614-initwithitems)Added [AVDateRangeMetadataGroup.items](https://developer.apple.com/documentation/avfoundation/avdaterangemetadatagroup/1390120-items)Added [AVDateRangeMetadataGroup.startDate](https://developer.apple.com/documentation/avfoundation/avdaterangemetadatagroup/1386420-startdate)Added [AVMetadataGroup](https://developer.apple.com/documentation/avfoundation/avmetadatagroup)Added [AVMetadataGroup.items](https://developer.apple.com/documentation/avfoundation/avmetadatagroup/1389935-items)Added [AVMutableDateRangeMetadataGroup](https://developer.apple.com/documentation/avfoundation/avmutabledaterangemetadatagroup)Added [AVMutableDateRangeMetadataGroup.endDate](https://developer.apple.com/documentation/avfoundation/avmutabledaterangemetadatagroup/1387651-enddate)Added [AVMutableDateRangeMetadataGroup.items](https://developer.apple.com/documentation/avfoundation/avmutabledaterangemetadatagroup/1388262-items)Added [AVMutableDateRangeMetadataGroup.startDate](https://developer.apple.com/documentation/avfoundation/avmutabledaterangemetadatagroup/1390555-startdate)Modified [AVMutableTimedMetadataGroup.items](https://developer.apple.com/documentation/avfoundation/avmutabletimedmetadatagroup/1386481-items)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, copy) NSArray *items ``` |
| To | ``` @property(nonatomic, readwrite, copy, nonnull) NSArray<AVMetadataItem *> *items ``` |

Modified [AVMutableTimedMetadataGroup.timeRange](https://developer.apple.com/documentation/avfoundation/avmutabletimedmetadatagroup/1387595-timerange)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite) CMTimeRange timeRange ``` |
| To | ``` @property(nonatomic, readwrite) CMTimeRange timeRange ``` |

Modified [AVTimedMetadataGroup](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup)

|  | Superclasses | Protocols |
| --- | --- | --- |
| From | NSObject | NSCopying |
| To | AVMetadataGroup | NSCopying, NSMutableCopying |

Modified [-[AVTimedMetadataGroup initWithItems:timeRange:]](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/1389632-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithItems:(NSArray *)items timeRange:(CMTimeRange)timeRange ``` |
| To | ``` - (instancetype _Nonnull)initWithItems:(NSArray<AVMetadataItem *> * _Nonnull)items timeRange:(CMTimeRange)timeRange ``` |

Modified [AVTimedMetadataGroup.items](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/1385928-items)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *items ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<AVMetadataItem *> *items ``` |

Modified [AVTimedMetadataGroup.timeRange](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/1387992-timerange)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) CMTimeRange timeRange ``` |
| To | ``` @property(nonatomic, readonly) CMTimeRange timeRange ``` |

#### AVVideoCompositing.h

Added [AVAsynchronousCIImageFilteringRequest](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest)Added [AVAsynchronousCIImageFilteringRequest.compositionTime](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/1388240-compositiontime)Added [-[AVAsynchronousCIImageFilteringRequest finishWithError:]](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/1386608-finishwitherror)Added [-[AVAsynchronousCIImageFilteringRequest finishWithImage:context:]](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/1389124-finish)Added [AVAsynchronousCIImageFilteringRequest.renderSize](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/1387933-rendersize)Added [AVAsynchronousCIImageFilteringRequest.sourceImage](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/1387577-sourceimage)Modified [AVAsynchronousVideoCompositionRequest.sourceTrackIDs](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1388898-sourcetrackids)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *sourceTrackIDs ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSNumber *> *sourceTrackIDs ``` |

Modified [AVVideoCompositing.requiredPixelBufferAttributesForRenderContext](https://developer.apple.com/documentation/avfoundation/avvideocompositing/1386414-requiredpixelbufferattributesfor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDictionary *requiredPixelBufferAttributesForRenderContext ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSDictionary<NSString *,id> *requiredPixelBufferAttributesForRenderContext ``` |

Modified [AVVideoCompositing.sourcePixelBufferAttributes](https://developer.apple.com/documentation/avfoundation/avvideocompositing/1388610-sourcepixelbufferattributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDictionary *sourcePixelBufferAttributes ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSDictionary<NSString *,id> *sourcePixelBufferAttributes ``` |

Modified [AVVideoCompositionInstruction.requiredSourceTrackIDs](https://developer.apple.com/documentation/avfoundation/1386654-avvideocompositioninstruction/1388661-requiredsourcetrackids)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *requiredSourceTrackIDs ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<NSValue *> *requiredSourceTrackIDs ``` |

#### AVVideoComposition.h

Added [+[AVMutableVideoComposition videoCompositionWithAsset:applyingCIFiltersWithHandler:]](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1387006-videocompositionwithasset)Added [+[AVVideoComposition videoCompositionWithAsset:applyingCIFiltersWithHandler:]](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1389556-init)Added AVMutableVideoComposition(AVMutableVideoCompositionFiltering)Added AVVideoComposition(AVVideoCompositionFiltering)Modified [AVMutableVideoComposition.instructions](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1385815-instructions)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *instructions ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSArray<id<AVVideoCompositionInstruction>> *instructions ``` |

Modified [AVMutableVideoCompositionInstruction.layerInstructions](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositioninstruction/1388912-layerinstructions)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *layerInstructions ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSArray<AVVideoCompositionLayerInstruction *> *layerInstructions ``` |

Modified [+[AVMutableVideoCompositionInstruction videoCompositionInstruction]](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositioninstruction/1519701-videocompositioninstruction)

|  | Declaration |
| --- | --- |
| From | ``` + (AVMutableVideoCompositionInstruction *)videoCompositionInstruction ``` |
| To | ``` + (instancetype _Nonnull)videoCompositionInstruction ``` |

Modified [+[AVMutableVideoCompositionLayerInstruction videoCompositionLayerInstruction]](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/1519717-videocompositionlayerinstruction)

|  | Declaration |
| --- | --- |
| From | ``` + (AVMutableVideoCompositionLayerInstruction *)videoCompositionLayerInstruction ``` |
| To | ``` + (instancetype _Nonnull)videoCompositionLayerInstruction ``` |

Modified [+[AVMutableVideoCompositionLayerInstruction videoCompositionLayerInstructionWithAssetTrack:]](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/1389691-init)

|  | Declaration |
| --- | --- |
| From | ``` + (AVMutableVideoCompositionLayerInstruction *)videoCompositionLayerInstructionWithAssetTrack:(AVAssetTrack *)track ``` |
| To | ``` + (instancetype _Nonnull)videoCompositionLayerInstructionWithAssetTrack:(AVAssetTrack * _Nonnull)track ``` |

Modified [AVVideoComposition.instructions](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1389211-instructions)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *instructions ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<id<AVVideoCompositionInstruction>> *instructions ``` |

Modified [+[AVVideoCompositionCoreAnimationTool videoCompositionCoreAnimationToolWithAdditionalLayer:asTrackID:]](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/1388345-videocompositioncoreanimationtoo)

|  | Declaration |
| --- | --- |
| From | ``` + (AVVideoCompositionCoreAnimationTool *)videoCompositionCoreAnimationToolWithAdditionalLayer:(CALayer *)layer asTrackID:(CMPersistentTrackID)trackID ``` |
| To | ``` + (instancetype _Nonnull)videoCompositionCoreAnimationToolWithAdditionalLayer:(CALayer * _Nonnull)layer asTrackID:(CMPersistentTrackID)trackID ``` |

Modified [+[AVVideoCompositionCoreAnimationTool videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayer:inLayer:]](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/1389594-videocompositioncoreanimationtoo)

|  | Declaration |
| --- | --- |
| From | ``` + (AVVideoCompositionCoreAnimationTool *)videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayer:(CALayer *)videoLayer inLayer:(CALayer *)animationLayer ``` |
| To | ``` + (instancetype _Nonnull)videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayer:(CALayer * _Nonnull)videoLayer inLayer:(CALayer * _Nonnull)animationLayer ``` |

Modified [+[AVVideoCompositionCoreAnimationTool videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayers:inLayer:]](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/1389778-init)

|  | Declaration |
| --- | --- |
| From | ``` + (AVVideoCompositionCoreAnimationTool *)videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayers:(NSArray *)videoLayers inLayer:(CALayer *)animationLayer ``` |
| To | ``` + (instancetype _Nonnull)videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayers:(NSArray<CALayer *> * _Nonnull)videoLayers inLayer:(CALayer * _Nonnull)animationLayer ``` |

Modified [AVVideoCompositionInstruction.backgroundColor](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction/1389384-backgroundcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) CGColorRef backgroundColor ``` |
| To | ``` @property(nonatomic, readonly, retain, nullable) CGColorRef backgroundColor ``` |

Modified [AVVideoCompositionInstruction.layerInstructions](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction/1389689-layerinstructions)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *layerInstructions ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<AVVideoCompositionLayerInstruction *> *layerInstructions ``` |

Modified [AVVideoCompositionInstruction.requiredSourceTrackIDs](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction/1390913-requiredsourcetrackids)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *requiredSourceTrackIDs ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSValue *> *requiredSourceTrackIDs ``` |

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
