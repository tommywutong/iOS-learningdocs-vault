---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/AVFoundation.html
archived_at: '2026-07-18T02:52:46.524109Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# AVFoundation Changes for Objective-C

### AVFoundation

#### AVAsset.h

Added [AVAsset.canContainFragments](https://developer.apple.com/documentation/avfoundation/avasset/1389520-cancontainfragments)Added [AVAsset.compatibleWithAirPlayVideo](https://developer.apple.com/documentation/avfoundation/avasset/1390333-compatiblewithairplayvideo)Added [AVAsset.containsFragments](https://developer.apple.com/documentation/avfoundation/avasset/1385589-containsfragments)Added [AVAsset.preferredMediaSelection](https://developer.apple.com/documentation/avfoundation/avasset/1386122-preferredmediaselection)Added [AVFragmentedAsset](https://developer.apple.com/documentation/avfoundation/avfragmentedasset)Added [+[AVFragmentedAsset fragmentedAssetWithURL:options:]](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/1508700-fragmentedassetwithurl)Added [AVFragmentedAsset.tracks](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/1387937-tracks)Added [-[AVFragmentedAsset tracksWithMediaCharacteristic:]](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/1387259-tracks)Added [-[AVFragmentedAsset tracksWithMediaType:]](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/1387253-tracks)Added [-[AVFragmentedAsset trackWithTrackID:]](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/1385712-track)Added [AVFragmentedAssetMinder](https://developer.apple.com/documentation/avfoundation/avfragmentedassetminder)Added [-[AVFragmentedAssetMinder addFragmentedAsset:]](https://developer.apple.com/documentation/avfoundation/avfragmentedassetminder/1387483-addfragmentedasset)Added [AVFragmentedAssetMinder.assets](https://developer.apple.com/documentation/avfoundation/avfragmentedassetminder/1390319-assets)Added [+[AVFragmentedAssetMinder fragmentedAssetMinderWithAsset:mindingInterval:]](https://developer.apple.com/documentation/avfoundation/avfragmentedassetminder/1387182-fragmentedassetminderwithasset)Added [AVFragmentedAssetMinder.mindingInterval](https://developer.apple.com/documentation/avfoundation/avfragmentedassetminder/1390760-mindinginterval)Added [-[AVFragmentedAssetMinder removeFragmentedAsset:]](https://developer.apple.com/documentation/avfoundation/avfragmentedassetminder/1389856-removefragmentedasset)Added [AVFragmentMinding](https://developer.apple.com/documentation/avfoundation/avfragmentminding)Added [AVFragmentMinding.associatedWithFragmentMinder](https://developer.apple.com/documentation/avfoundation/avfragmentminding/1390175-associatedwithfragmentminder)Added AVAsset(AVAssetFragments)Added [AVAssetChapterMetadataGroupsDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1386794-avassetchaptermetadatagroupsdidc)Added [AVAssetContainsFragmentsDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1387022-avassetcontainsfragmentsdidchang)Added [AVAssetDurationDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1386249-avassetdurationdidchange)Added [AVAssetMediaSelectionGroupsDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1387984-avassetmediaselectiongroupsdidch)Added [AVAssetWasDefragmentedNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1389894-avassetwasdefragmented)Added AVFragmentedAsset(AVFragmentedAssetTrackInspection)Modified [+[AVAsset assetWithURL:]](https://developer.apple.com/documentation/avfoundation/avasset/1389943-init)

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

Modified [AVAsset.creationDate](https://developer.apple.com/documentation/avfoundation/avasset/1386342-creationdate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVMetadataItem *creationDate ``` |
| To | ``` @property(nonatomic, readonly, nullable) AVMetadataItem *creationDate ``` |

Modified [AVAsset.lyrics](https://developer.apple.com/documentation/avfoundation/avasset/1388104-lyrics)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *lyrics ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSString *lyrics ``` |

Modified [-[AVAsset mediaSelectionGroupForMediaCharacteristic:]](https://developer.apple.com/documentation/avfoundation/avasset/1387496-mediaselectiongroupformediachara)

|  | Declaration |
| --- | --- |
| From | ``` - (AVMediaSelectionGroup *)mediaSelectionGroupForMediaCharacteristic:(NSString *)mediaCharacteristic ``` |
| To | ``` - (AVMediaSelectionGroup * _Nullable)mediaSelectionGroupForMediaCharacteristic:(NSString * _Nonnull)mediaCharacteristic ``` |

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

Modified [-[AVAsset trackWithTrackID:]](https://developer.apple.com/documentation/avfoundation/avasset/1390145-track)

|  | Declaration |
| --- | --- |
| From | ``` - (AVAssetTrack *)trackWithTrackID:(CMPersistentTrackID)trackID ``` |
| To | ``` - (AVAssetTrack * _Nullable)trackWithTrackID:(CMPersistentTrackID)trackID ``` |

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

Modified [-[AVURLAsset compatibleTrackForCompositionTrack:]](https://developer.apple.com/documentation/avfoundation/avurlasset/1389650-compatibletrackforcompositiontra)

|  | Declaration |
| --- | --- |
| From | ``` - (AVAssetTrack *)compatibleTrackForCompositionTrack:(AVCompositionTrack *)compositionTrack ``` |
| To | ``` - (AVAssetTrack * _Nullable)compatibleTrackForCompositionTrack:(AVCompositionTrack * _Nonnull)compositionTrack ``` |

Modified [-[AVURLAsset initWithURL:options:]](https://developer.apple.com/documentation/avfoundation/avurlasset/1385698-initwithurl)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithURL:(NSURL *)URL options:(NSDictionary *)options ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithURL:(NSURL * _Nonnull)URL options:(NSDictionary<NSString *,id> * _Nullable)options ``` | yes |

Modified [+[AVURLAsset isPlayableExtendedMIMEType:]](https://developer.apple.com/documentation/avfoundation/avurlasset/1387142-isplayableextendedmimetype)

|  | Declaration |
| --- | --- |
| From | ``` + (BOOL)isPlayableExtendedMIMEType:(NSString *)extendedMIMEType ``` |
| To | ``` + (BOOL)isPlayableExtendedMIMEType:(NSString * _Nonnull)extendedMIMEType ``` |

Modified [AVURLAsset.resourceLoader](https://developer.apple.com/documentation/avfoundation/avurlasset/1389118-resourceloader)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVAssetResourceLoader *resourceLoader ``` |
| To | ``` @property(nonatomic, readonly, nonnull) AVAssetResourceLoader *resourceLoader ``` |

Modified [AVURLAsset.URL](https://developer.apple.com/documentation/avfoundation/avurlasset/1388127-url)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSURL *URL ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSURL *URL ``` |

Modified [+[AVURLAsset URLAssetWithURL:options:]](https://developer.apple.com/documentation/avfoundation/avurlasset/1508727-urlassetwithurl)

|  | Declaration |
| --- | --- |
| From | ``` + (AVURLAsset *)URLAssetWithURL:(NSURL *)URL options:(NSDictionary *)options ``` |
| To | ``` + (instancetype _Nonnull)URLAssetWithURL:(NSURL * _Nonnull)URL options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

#### AVAssetExportSession.h

Added [AVAssetExportPresetHighestQuality](https://developer.apple.com/documentation/avfoundation/avassetexportpresethighestquality)Added [AVAssetExportPresetLowQuality](https://developer.apple.com/documentation/avfoundation/avassetexportpresetlowquality)Added [AVAssetExportPresetMediumQuality](https://developer.apple.com/documentation/avfoundation/avassetexportpresetmediumquality)Added AVAssetExportSession(AVAssetExportSessionDurationAndLength)Added AVAssetExportSession(AVAssetExportSessionFileTypes)Added AVAssetExportSession(AVAssetExportSessionMediaProcessing)Added AVAssetExportSession(AVAssetExportSessionMetadata)Added AVAssetExportSession(AVAssetExportSessionMultipass)Added AVAssetExportSession(AVAssetExportSessionPresets)Modified [+[AVAssetExportSession allExportPresets]](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1387150-allexportpresets)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)allExportPresets ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)allExportPresets ``` |

Modified [AVAssetExportSession.asset](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1385690-asset)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain, readonly) AVAsset *asset ``` |
| To | ``` @property(nonatomic, retain, readonly, nonnull) AVAsset *asset ``` |

Modified [AVAssetExportSession.audioMix](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1388155-audiomix)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) AVAudioMix *audioMix ``` |
| To | ``` @property(nonatomic, copy, nullable) AVAudioMix *audioMix ``` |

Modified [AVAssetExportSession.audioTimePitchAlgorithm](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1385835-audiotimepitchalgorithm)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *audioTimePitchAlgorithm ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSString *audioTimePitchAlgorithm ``` |

Modified [AVAssetExportSession.customVideoCompositor](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1388288-customvideocompositor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id<AVVideoCompositing> customVideoCompositor ``` |
| To | ``` @property(nonatomic, readonly, nullable) id<AVVideoCompositing> customVideoCompositor ``` |

Modified [+[AVAssetExportSession determineCompatibilityOfExportPreset:withAsset:outputFileType:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1385821-determinecompatibilityofexportpr)

|  | Declaration |
| --- | --- |
| From | ``` + (void)determineCompatibilityOfExportPreset:(NSString *)presetName withAsset:(AVAsset *)asset outputFileType:(NSString *)outputFileType completionHandler:(void (^)(BOOL compatible))handler ``` |
| To | ``` + (void)determineCompatibilityOfExportPreset:(NSString * _Nonnull)presetName withAsset:(AVAsset * _Nonnull)asset outputFileType:(NSString * _Nullable)outputFileType completionHandler:(void (^ _Nonnull)(BOOL compatible))handler ``` |

Modified [-[AVAssetExportSession determineCompatibleFileTypesWithCompletionHandler:]](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1387907-determinecompatiblefiletypeswith)

|  | Declaration |
| --- | --- |
| From | ``` - (void)determineCompatibleFileTypesWithCompletionHandler:(void (^)(NSArray *compatibleFileTypes))handler ``` |
| To | ``` - (void)determineCompatibleFileTypesWithCompletionHandler:(void (^ _Nonnull)(NSArray<NSString *> * _Nonnull compatibleFileTypes))handler ``` |

Modified [AVAssetExportSession.directoryForTemporaryFiles](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1388699-directoryfortemporaryfiles)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSURL *directoryForTemporaryFiles ``` |
| To | ``` @property(nonatomic, copy, nullable) NSURL *directoryForTemporaryFiles ``` |

Modified [AVAssetExportSession.error](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1385936-error)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSError *error ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSError *error ``` |

Modified [-[AVAssetExportSession exportAsynchronouslyWithCompletionHandler:]](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1388005-exportasynchronouslywithcompleti)

|  | Declaration |
| --- | --- |
| From | ``` - (void)exportAsynchronouslyWithCompletionHandler:(void (^)(void))handler ``` |
| To | ``` - (void)exportAsynchronouslyWithCompletionHandler:(void (^ _Nonnull)(void))handler ``` |

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

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithAsset:(AVAsset *)asset presetName:(NSString *)presetName ``` | -- |
| To | ``` - (instancetype _Nullable)initWithAsset:(AVAsset * _Nonnull)asset presetName:(NSString * _Nonnull)presetName ``` | yes |

Modified [AVAssetExportSession.metadata](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1390453-metadata)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *metadata ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<AVMetadataItem *> *metadata ``` |

Modified [AVAssetExportSession.metadataItemFilter](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1390226-metadataitemfilter)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) AVMetadataItemFilter *metadataItemFilter ``` |
| To | ``` @property(nonatomic, retain, nullable) AVMetadataItemFilter *metadataItemFilter ``` |

Modified [AVAssetExportSession.outputFileType](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1387110-outputfiletype)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *outputFileType ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *outputFileType ``` |

Modified [AVAssetExportSession.outputURL](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1389970-outputurl)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSURL *outputURL ``` |
| To | ``` @property(nonatomic, copy, nullable) NSURL *outputURL ``` |

Modified [AVAssetExportSession.presetName](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1390467-presetname)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *presetName ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *presetName ``` |

Modified [AVAssetExportSession.supportedFileTypes](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1388762-supportedfiletypes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *supportedFileTypes ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *supportedFileTypes ``` |

Modified [AVAssetExportSession.videoComposition](https://developer.apple.com/documentation/avfoundation/avassetexportsession/1389477-videocomposition)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) AVVideoComposition *videoComposition ``` |
| To | ``` @property(nonatomic, copy, nullable) AVVideoComposition *videoComposition ``` |

#### AVAssetImageGenerator.h

Modified [AVAssetImageGenerator.apertureMode](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1389314-aperturemode)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *apertureMode ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *apertureMode ``` |

Modified [AVAssetImageGenerator.asset](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1390689-asset)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVAsset *asset ``` |
| To | ``` @property(nonatomic, readonly, nonnull) AVAsset *asset ``` |

Modified [+[AVAssetImageGenerator assetImageGeneratorWithAsset:]](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1426634-assetimagegeneratorwithasset)

|  | Declaration |
| --- | --- |
| From | ``` + (AVAssetImageGenerator *)assetImageGeneratorWithAsset:(AVAsset *)asset ``` |
| To | ``` + (instancetype _Nonnull)assetImageGeneratorWithAsset:(AVAsset * _Nonnull)asset ``` |

Modified [-[AVAssetImageGenerator copyCGImageAtTime:actualTime:error:]](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1387303-copycgimageattime)

|  | Declaration |
| --- | --- |
| From | ``` - (CGImageRef)copyCGImageAtTime:(CMTime)requestedTime actualTime:(CMTime *)actualTime error:(NSError **)outError ``` |
| To | ``` - (CGImageRef _Nullable)copyCGImageAtTime:(CMTime)requestedTime actualTime:(CMTime * _Nullable)actualTime error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [AVAssetImageGenerator.customVideoCompositor](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1386469-customvideocompositor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id<AVVideoCompositing> customVideoCompositor ``` |
| To | ``` @property(nonatomic, readonly, nullable) id<AVVideoCompositing> customVideoCompositor ``` |

Modified [-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1388100-generatecgimagesasynchronously)

|  | Declaration |
| --- | --- |
| From | ``` - (void)generateCGImagesAsynchronouslyForTimes:(NSArray *)requestedTimes completionHandler:(AVAssetImageGeneratorCompletionHandler)handler ``` |
| To | ``` - (void)generateCGImagesAsynchronouslyForTimes:(NSArray<NSValue *> * _Nonnull)requestedTimes completionHandler:(AVAssetImageGeneratorCompletionHandler _Nonnull)handler ``` |

Modified [-[AVAssetImageGenerator initWithAsset:]](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1387855-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithAsset:(AVAsset *)asset ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithAsset:(AVAsset * _Nonnull)asset ``` | yes |

Modified [AVAssetImageGenerator.videoComposition](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/1390189-videocomposition)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) AVVideoComposition *videoComposition ``` |
| To | ``` @property(nonatomic, copy, nullable) AVVideoComposition *videoComposition ``` |

#### AVAssetReader.h

Modified [-[AVAssetReader addOutput:]](https://developer.apple.com/documentation/avfoundation/avassetreader/1390110-addoutput)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addOutput:(AVAssetReaderOutput *)output ``` |
| To | ``` - (void)addOutput:(AVAssetReaderOutput * _Nonnull)output ``` |

Modified [AVAssetReader.asset](https://developer.apple.com/documentation/avfoundation/avassetreader/1389128-asset)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain, readonly) AVAsset *asset ``` |
| To | ``` @property(nonatomic, retain, readonly, nonnull) AVAsset *asset ``` |

Modified [+[AVAssetReader assetReaderWithAsset:error:]](https://developer.apple.com/documentation/avfoundation/avassetreader/1420148-assetreaderwithasset)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)assetReaderWithAsset:(AVAsset *)asset error:(NSError **)outError ``` |
| To | ``` + (instancetype _Nullable)assetReaderWithAsset:(AVAsset * _Nonnull)asset error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [-[AVAssetReader canAddOutput:]](https://developer.apple.com/documentation/avfoundation/avassetreader/1387485-canadd)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)canAddOutput:(AVAssetReaderOutput *)output ``` |
| To | ``` - (BOOL)canAddOutput:(AVAssetReaderOutput * _Nonnull)output ``` |

Modified [AVAssetReader.error](https://developer.apple.com/documentation/avfoundation/avassetreader/1388114-error)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSError *error ``` |
| To | ``` @property(readonly, nullable) NSError *error ``` |

Modified [-[AVAssetReader initWithAsset:error:]](https://developer.apple.com/documentation/avfoundation/avassetreader/1385593-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithAsset:(AVAsset *)asset error:(NSError **)outError ``` | -- |
| To | ``` - (instancetype _Nullable)initWithAsset:(AVAsset * _Nonnull)asset error:(NSError * _Nullable * _Nullable)outError ``` | yes |

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

Modified [AVAssetReaderAudioMixOutput.audioMix](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/1387074-audiomix)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) AVAudioMix *audioMix ``` |
| To | ``` @property(nonatomic, copy, nullable) AVAudioMix *audioMix ``` |

Modified [AVAssetReaderAudioMixOutput.audioSettings](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/1388860-audiosettings)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDictionary *audioSettings ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSDictionary<NSString *,id> *audioSettings ``` |

Modified [AVAssetReaderAudioMixOutput.audioTimePitchAlgorithm](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/1388713-audiotimepitchalgorithm)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *audioTimePitchAlgorithm ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSString *audioTimePitchAlgorithm ``` |

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

Modified [-[AVAssetReaderOutput copyNextSampleBuffer]](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/1385732-copynextsamplebuffer)

|  | Declaration |
| --- | --- |
| From | ``` - (CMSampleBufferRef)copyNextSampleBuffer ``` |
| To | ``` - (CMSampleBufferRef _Nullable)copyNextSampleBuffer ``` |

Modified [AVAssetReaderOutput.mediaType](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/1390880-mediatype)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *mediaType ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *mediaType ``` |

Modified [-[AVAssetReaderOutput resetForReadingTimeRanges:]](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/1388890-resetforreadingtimeranges)

|  | Declaration |
| --- | --- |
| From | ``` - (void)resetForReadingTimeRanges:(NSArray *)timeRanges ``` |
| To | ``` - (void)resetForReadingTimeRanges:(NSArray<NSValue *> * _Nonnull)timeRanges ``` |

Modified [+[AVAssetReaderOutputMetadataAdaptor assetReaderOutputMetadataAdaptorWithAssetReaderTrackOutput:]](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputmetadataadaptor/1490330-assetreaderoutputmetadataadaptor)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)assetReaderOutputMetadataAdaptorWithAssetReaderTrackOutput:(AVAssetReaderTrackOutput *)trackOutput ``` |
| To | ``` + (instancetype _Nonnull)assetReaderOutputMetadataAdaptorWithAssetReaderTrackOutput:(AVAssetReaderTrackOutput * _Nonnull)trackOutput ``` |

Modified [AVAssetReaderOutputMetadataAdaptor.assetReaderTrackOutput](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputmetadataadaptor/1388330-assetreadertrackoutput)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVAssetReaderTrackOutput *assetReaderTrackOutput ``` |
| To | ``` @property(nonatomic, readonly, nonnull) AVAssetReaderTrackOutput *assetReaderTrackOutput ``` |

Modified [-[AVAssetReaderOutputMetadataAdaptor initWithAssetReaderTrackOutput:]](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputmetadataadaptor/1388009-initwithassetreadertrackoutput)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithAssetReaderTrackOutput:(AVAssetReaderTrackOutput *)trackOutput ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithAssetReaderTrackOutput:(AVAssetReaderTrackOutput * _Nonnull)trackOutput ``` | yes |

Modified [-[AVAssetReaderOutputMetadataAdaptor nextTimedMetadataGroup]](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputmetadataadaptor/1390008-nexttimedmetadatagroup)

|  | Declaration |
| --- | --- |
| From | ``` - (AVTimedMetadataGroup *)nextTimedMetadataGroup ``` |
| To | ``` - (AVTimedMetadataGroup * _Nullable)nextTimedMetadataGroup ``` |

Modified [+[AVAssetReaderSampleReferenceOutput assetReaderSampleReferenceOutputWithTrack:]](https://developer.apple.com/documentation/avfoundation/avassetreadersamplereferenceoutput/1490320-assetreadersamplereferenceoutput)

|  | Declaration |
| --- | --- |
| From | ``` + (AVAssetReaderSampleReferenceOutput *)assetReaderSampleReferenceOutputWithTrack:(AVAssetTrack *)track ``` |
| To | ``` + (instancetype _Nonnull)assetReaderSampleReferenceOutputWithTrack:(AVAssetTrack * _Nonnull)track ``` |

Modified [-[AVAssetReaderSampleReferenceOutput initWithTrack:]](https://developer.apple.com/documentation/avfoundation/avassetreadersamplereferenceoutput/1387339-initwithtrack)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithTrack:(AVAssetTrack *)track ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithTrack:(AVAssetTrack * _Nonnull)track ``` | yes |

Modified [AVAssetReaderSampleReferenceOutput.track](https://developer.apple.com/documentation/avfoundation/avassetreadersamplereferenceoutput/1390057-track)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVAssetTrack *track ``` |
| To | ``` @property(nonatomic, readonly, nonnull) AVAssetTrack *track ``` |

Modified [+[AVAssetReaderTrackOutput assetReaderTrackOutputWithTrack:outputSettings:]](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput/1490322-assetreadertrackoutputwithtrack)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)assetReaderTrackOutputWithTrack:(AVAssetTrack *)track outputSettings:(NSDictionary *)outputSettings ``` |
| To | ``` + (instancetype _Nonnull)assetReaderTrackOutputWithTrack:(AVAssetTrack * _Nonnull)track outputSettings:(NSDictionary<NSString *,id> * _Nullable)outputSettings ``` |

Modified [AVAssetReaderTrackOutput.audioTimePitchAlgorithm](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput/1387851-audiotimepitchalgorithm)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *audioTimePitchAlgorithm ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSString *audioTimePitchAlgorithm ``` |

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

Modified [AVAssetReaderTrackOutput.track](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput/1386921-track)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVAssetTrack *track ``` |
| To | ``` @property(nonatomic, readonly, nonnull) AVAssetTrack *track ``` |

Modified [+[AVAssetReaderVideoCompositionOutput assetReaderVideoCompositionOutputWithVideoTracks:videoSettings:]](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/1490331-assetreadervideocompositionoutpu)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)assetReaderVideoCompositionOutputWithVideoTracks:(NSArray *)videoTracks videoSettings:(NSDictionary *)videoSettings ``` |
| To | ``` + (instancetype _Nonnull)assetReaderVideoCompositionOutputWithVideoTracks:(NSArray<AVAssetTrack *> * _Nonnull)videoTracks videoSettings:(NSDictionary<NSString *,id> * _Nullable)videoSettings ``` |

Modified [AVAssetReaderVideoCompositionOutput.customVideoCompositor](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/1388310-customvideocompositor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id<AVVideoCompositing> customVideoCompositor ``` |
| To | ``` @property(nonatomic, readonly, nullable) id<AVVideoCompositing> customVideoCompositor ``` |

Modified [-[AVAssetReaderVideoCompositionOutput initWithVideoTracks:videoSettings:]](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/1386676-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithVideoTracks:(NSArray *)videoTracks videoSettings:(NSDictionary *)videoSettings ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithVideoTracks:(NSArray<AVAssetTrack *> * _Nonnull)videoTracks videoSettings:(NSDictionary<NSString *,id> * _Nullable)videoSettings ``` | yes |

Modified [AVAssetReaderVideoCompositionOutput.videoComposition](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/1388927-videocomposition)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) AVVideoComposition *videoComposition ``` |
| To | ``` @property(nonatomic, copy, nullable) AVVideoComposition *videoComposition ``` |

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

Removed AVAssetResourceLoadingRequest(AVAssetResourceLoader_ContentKeyRequestSupport)Added [AVAssetResourceLoader.preloadsEligibleContentKeys](https://developer.apple.com/documentation/avfoundation/avassetresourceloader/1386939-preloadseligiblecontentkeys)Added [AVAssetResourceLoadingDataRequest.requestsAllDataToEndOfResource](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest/1386864-requestsalldatatoendofresource)Added AVAssetResourceLoader(AVAssetResourceLoaderContentKeySupport)Added AVAssetResourceLoadingRequest(AVAssetResourceLoadingRequestContentKeyRequestSupport)Modified [AVAssetResourceLoader.delegate](https://developer.apple.com/documentation/avfoundation/avassetresourceloader/1387913-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id<AVAssetResourceLoaderDelegate> delegate ``` |
| To | ``` @property(nonatomic, readonly, weak, nullable) id<AVAssetResourceLoaderDelegate> delegate ``` |

Modified [AVAssetResourceLoader.delegateQueue](https://developer.apple.com/documentation/avfoundation/avassetresourceloader/1387678-delegatequeue)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) dispatch_queue_t delegateQueue ``` |
| To | ``` @property(nonatomic, readonly, nullable) dispatch_queue_t delegateQueue ``` |

Modified [-[AVAssetResourceLoader setDelegate:queue:]](https://developer.apple.com/documentation/avfoundation/avassetresourceloader/1388314-setdelegate)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setDelegate:(id<AVAssetResourceLoaderDelegate>)delegate queue:(dispatch_queue_t)delegateQueue ``` |
| To | ``` - (void)setDelegate:(id<AVAssetResourceLoaderDelegate> _Nullable)delegate queue:(dispatch_queue_t _Nullable)delegateQueue ``` |

Modified [-[AVAssetResourceLoaderDelegate resourceLoader:didCancelAuthenticationChallenge:]](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/1387929-resourceloader)

|  | Declaration |
| --- | --- |
| From | ``` - (void)resourceLoader:(AVAssetResourceLoader *)resourceLoader didCancelAuthenticationChallenge:(NSURLAuthenticationChallenge *)authenticationChallenge ``` |
| To | ``` - (void)resourceLoader:(AVAssetResourceLoader * _Nonnull)resourceLoader didCancelAuthenticationChallenge:(NSURLAuthenticationChallenge * _Nonnull)authenticationChallenge ``` |

Modified [-[AVAssetResourceLoaderDelegate resourceLoader:didCancelLoadingRequest:]](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/1387722-resourceloader)

|  | Declaration |
| --- | --- |
| From | ``` - (void)resourceLoader:(AVAssetResourceLoader *)resourceLoader didCancelLoadingRequest:(AVAssetResourceLoadingRequest *)loadingRequest ``` |
| To | ``` - (void)resourceLoader:(AVAssetResourceLoader * _Nonnull)resourceLoader didCancelLoadingRequest:(AVAssetResourceLoadingRequest * _Nonnull)loadingRequest ``` |

Modified [-[AVAssetResourceLoaderDelegate resourceLoader:shouldWaitForLoadingOfRequestedResource:]](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/1388121-resourceloader)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)resourceLoader:(AVAssetResourceLoader *)resourceLoader shouldWaitForLoadingOfRequestedResource:(AVAssetResourceLoadingRequest *)loadingRequest ``` |
| To | ``` - (BOOL)resourceLoader:(AVAssetResourceLoader * _Nonnull)resourceLoader shouldWaitForLoadingOfRequestedResource:(AVAssetResourceLoadingRequest * _Nonnull)loadingRequest ``` |

Modified [-[AVAssetResourceLoaderDelegate resourceLoader:shouldWaitForRenewalOfRequestedResource:]](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/1387058-resourceloader)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)resourceLoader:(AVAssetResourceLoader *)resourceLoader shouldWaitForRenewalOfRequestedResource:(AVAssetResourceRenewalRequest *)renewalRequest ``` |
| To | ``` - (BOOL)resourceLoader:(AVAssetResourceLoader * _Nonnull)resourceLoader shouldWaitForRenewalOfRequestedResource:(AVAssetResourceRenewalRequest * _Nonnull)renewalRequest ``` |

Modified [-[AVAssetResourceLoaderDelegate resourceLoader:shouldWaitForResponseToAuthenticationChallenge:]](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/1388736-resourceloader)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)resourceLoader:(AVAssetResourceLoader *)resourceLoader shouldWaitForResponseToAuthenticationChallenge:(NSURLAuthenticationChallenge *)authenticationChallenge ``` |
| To | ``` - (BOOL)resourceLoader:(AVAssetResourceLoader * _Nonnull)resourceLoader shouldWaitForResponseToAuthenticationChallenge:(NSURLAuthenticationChallenge * _Nonnull)authenticationChallenge ``` |

Modified [AVAssetResourceLoadingContentInformationRequest.contentType](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/1388529-contenttype)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *contentType ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *contentType ``` |

Modified [AVAssetResourceLoadingContentInformationRequest.renewalDate](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/1390683-renewaldate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSDate *renewalDate ``` |
| To | ``` @property(nonatomic, copy, nullable) NSDate *renewalDate ``` |

Modified [-[AVAssetResourceLoadingDataRequest respondWithData:]](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest/1390581-respondwithdata)

|  | Declaration |
| --- | --- |
| From | ``` - (void)respondWithData:(NSData *)data ``` |
| To | ``` - (void)respondWithData:(NSData * _Nonnull)data ``` |

Modified [AVAssetResourceLoadingRequest.contentInformationRequest](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1390340-contentinformationrequest)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVAssetResourceLoadingContentInformationRequest *contentInformationRequest ``` |
| To | ``` @property(nonatomic, readonly, nullable) AVAssetResourceLoadingContentInformationRequest *contentInformationRequest ``` |

Modified [AVAssetResourceLoadingRequest.dataRequest](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1388779-datarequest)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVAssetResourceLoadingDataRequest *dataRequest ``` |
| To | ``` @property(nonatomic, readonly, nullable) AVAssetResourceLoadingDataRequest *dataRequest ``` |

Modified [-[AVAssetResourceLoadingRequest finishLoadingWithError:]](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1390491-finishloading)

|  | Declaration |
| --- | --- |
| From | ``` - (void)finishLoadingWithError:(NSError *)error ``` |
| To | ``` - (void)finishLoadingWithError:(NSError * _Nullable)error ``` |

Modified [AVAssetResourceLoadingRequest.redirect](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1390854-redirect)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSURLRequest *redirect ``` |
| To | ``` @property(nonatomic, copy, nullable) NSURLRequest *redirect ``` |

Modified [AVAssetResourceLoadingRequest.request](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1386220-request)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSURLRequest *request ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSURLRequest *request ``` |

Modified [AVAssetResourceLoadingRequest.response](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1389034-response)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSURLResponse *response ``` |
| To | ``` @property(nonatomic, copy, nullable) NSURLResponse *response ``` |

Modified [-[AVAssetResourceLoadingRequest streamingContentKeyRequestDataForApp:contentIdentifier:options:error:]](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/1386116-streamingcontentkeyrequestdata)

|  | Declaration |
| --- | --- |
| From | ``` - (NSData *)streamingContentKeyRequestDataForApp:(NSData *)appIdentifier contentIdentifier:(NSData *)contentIdentifier options:(NSDictionary *)options error:(NSError **)outError ``` |
| To | ``` - (NSData * _Nullable)streamingContentKeyRequestDataForApp:(NSData * _Nonnull)appIdentifier contentIdentifier:(NSData * _Nonnull)contentIdentifier options:(NSDictionary<NSString *,id> * _Nullable)options error:(NSError * _Nullable * _Nullable)outError ``` |

#### AVAssetTrack.h

Added [AVFragmentedAssetTrack](https://developer.apple.com/documentation/avfoundation/avfragmentedassettrack)Added [AVAssetTrackSegmentsDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1386848-avassettracksegmentsdidchange)Added [AVAssetTrackTimeRangeDidChangeNotification](https://developer.apple.com/documentation/avfoundation/avassettracktimerangedidchangenotification)Added [AVAssetTrackTrackAssociationsDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1388487-avassettracktrackassociationsdid)Modified [AVAssetTrack.asset](https://developer.apple.com/documentation/avfoundation/avassettrack/1385611-asset)

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

Modified [AVAssetTrack.extendedLanguageTag](https://developer.apple.com/documentation/avfoundation/avassettrack/1389105-extendedlanguagetag)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *extendedLanguageTag ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *extendedLanguageTag ``` |

Modified [AVAssetTrack.formatDescriptions](https://developer.apple.com/documentation/avfoundation/avassettrack/1386694-formatdescriptions)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *formatDescriptions ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray *formatDescriptions ``` |

Modified [-[AVAssetTrack hasMediaCharacteristic:]](https://developer.apple.com/documentation/avfoundation/avassettrack/1385847-hasmediacharacteristic)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)hasMediaCharacteristic:(NSString *)mediaCharacteristic ``` |
| To | ``` - (BOOL)hasMediaCharacteristic:(NSString * _Nonnull)mediaCharacteristic ``` |

Modified [AVAssetTrack.languageCode](https://developer.apple.com/documentation/avfoundation/avassettrack/1388627-languagecode)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *languageCode ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *languageCode ``` |

Modified [-[AVAssetTrack makeSampleCursorAtFirstSampleInDecodeOrder]](https://developer.apple.com/documentation/avfoundation/avassettrack/1387226-makesamplecursoratfirstsampleind)

|  | Declaration |
| --- | --- |
| From | ``` - (AVSampleCursor *)makeSampleCursorAtFirstSampleInDecodeOrder ``` |
| To | ``` - (AVSampleCursor * _Nullable)makeSampleCursorAtFirstSampleInDecodeOrder ``` |

Modified [-[AVAssetTrack makeSampleCursorAtLastSampleInDecodeOrder]](https://developer.apple.com/documentation/avfoundation/avassettrack/1386014-makesamplecursoratlastsampleinde)

|  | Declaration |
| --- | --- |
| From | ``` - (AVSampleCursor *)makeSampleCursorAtLastSampleInDecodeOrder ``` |
| To | ``` - (AVSampleCursor * _Nullable)makeSampleCursorAtLastSampleInDecodeOrder ``` |

Modified [-[AVAssetTrack makeSampleCursorWithPresentationTimeStamp:]](https://developer.apple.com/documentation/avfoundation/avassettrack/1390248-makesamplecursor)

|  | Declaration |
| --- | --- |
| From | ``` - (AVSampleCursor *)makeSampleCursorWithPresentationTimeStamp:(CMTime)presentationTimeStamp ``` |
| To | ``` - (AVSampleCursor * _Nullable)makeSampleCursorWithPresentationTimeStamp:(CMTime)presentationTimeStamp ``` |

Modified [AVAssetTrack.mediaType](https://developer.apple.com/documentation/avfoundation/avassettrack/1385741-mediatype)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *mediaType ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *mediaType ``` |

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

Modified [-[AVAssetTrack segmentForTrackTime:]](https://developer.apple.com/documentation/avfoundation/avassettrack/1387186-segmentfortracktime)

|  | Declaration |
| --- | --- |
| From | ``` - (AVAssetTrackSegment *)segmentForTrackTime:(CMTime)trackTime ``` |
| To | ``` - (AVAssetTrackSegment * _Nullable)segmentForTrackTime:(CMTime)trackTime ``` |

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

Added [AVAssetWriter.overallDurationHint](https://developer.apple.com/documentation/avfoundation/avassetwriter/1388408-overalldurationhint)Modified [-[AVAssetWriter addInput:]](https://developer.apple.com/documentation/avfoundation/avassetwriter/1390389-addinput)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addInput:(AVAssetWriterInput *)input ``` |
| To | ``` - (void)addInput:(AVAssetWriterInput * _Nonnull)input ``` |

Modified [-[AVAssetWriter addInputGroup:]](https://developer.apple.com/documentation/avfoundation/avassetwriter/1385643-add)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addInputGroup:(AVAssetWriterInputGroup *)inputGroup ``` |
| To | ``` - (void)addInputGroup:(AVAssetWriterInputGroup * _Nonnull)inputGroup ``` |

Modified [+[AVAssetWriter assetWriterWithURL:fileType:error:]](https://developer.apple.com/documentation/avfoundation/avassetwriter/1426663-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)assetWriterWithURL:(NSURL *)outputURL fileType:(NSString *)outputFileType error:(NSError **)outError ``` |
| To | ``` + (instancetype _Nullable)assetWriterWithURL:(NSURL * _Nonnull)outputURL fileType:(NSString * _Nonnull)outputFileType error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [AVAssetWriter.availableMediaTypes](https://developer.apple.com/documentation/avfoundation/avassetwriter/1388730-availablemediatypes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *availableMediaTypes ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *availableMediaTypes ``` |

Modified [-[AVAssetWriter canAddInput:]](https://developer.apple.com/documentation/avfoundation/avassetwriter/1387863-canaddinput)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)canAddInput:(AVAssetWriterInput *)input ``` |
| To | ``` - (BOOL)canAddInput:(AVAssetWriterInput * _Nonnull)input ``` |

Modified [-[AVAssetWriter canAddInputGroup:]](https://developer.apple.com/documentation/avfoundation/avassetwriter/1386698-canaddinputgroup)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)canAddInputGroup:(AVAssetWriterInputGroup *)inputGroup ``` |
| To | ``` - (BOOL)canAddInputGroup:(AVAssetWriterInputGroup * _Nonnull)inputGroup ``` |

Modified [-[AVAssetWriter canApplyOutputSettings:forMediaType:]](https://developer.apple.com/documentation/avfoundation/avassetwriter/1388842-canapply)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)canApplyOutputSettings:(NSDictionary *)outputSettings forMediaType:(NSString *)mediaType ``` |
| To | ``` - (BOOL)canApplyOutputSettings:(NSDictionary<NSString *,id> * _Nullable)outputSettings forMediaType:(NSString * _Nonnull)mediaType ``` |

Modified [AVAssetWriter.directoryForTemporaryFiles](https://developer.apple.com/documentation/avfoundation/avassetwriter/1387445-directoryfortemporaryfiles)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSURL *directoryForTemporaryFiles ``` |
| To | ``` @property(nonatomic, copy, nullable) NSURL *directoryForTemporaryFiles ``` |

Modified [AVAssetWriter.error](https://developer.apple.com/documentation/avfoundation/avassetwriter/1390725-error)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSError *error ``` |
| To | ``` @property(readonly, nullable) NSError *error ``` |

Modified [-[AVAssetWriter finishWritingWithCompletionHandler:]](https://developer.apple.com/documentation/avfoundation/avassetwriter/1390432-finishwriting)

|  | Declaration |
| --- | --- |
| From | ``` - (void)finishWritingWithCompletionHandler:(void (^)(void))handler ``` |
| To | ``` - (void)finishWritingWithCompletionHandler:(void (^ _Nonnull)(void))handler ``` |

Modified [-[AVAssetWriter initWithURL:fileType:error:]](https://developer.apple.com/documentation/avfoundation/avassetwriter/1389201-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithURL:(NSURL *)outputURL fileType:(NSString *)outputFileType error:(NSError **)outError ``` | -- |
| To | ``` - (instancetype _Nullable)initWithURL:(NSURL * _Nonnull)outputURL fileType:(NSString * _Nonnull)outputFileType error:(NSError * _Nullable * _Nullable)outError ``` | yes |

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

Modified [AVAssetWriter.outputFileType](https://developer.apple.com/documentation/avfoundation/avassetwriter/1387349-outputfiletype)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy, readonly) NSString *outputFileType ``` |
| To | ``` @property(nonatomic, copy, readonly, nonnull) NSString *outputFileType ``` |

Modified [AVAssetWriter.outputURL](https://developer.apple.com/documentation/avfoundation/avassetwriter/1387731-outputurl)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy, readonly) NSURL *outputURL ``` |
| To | ``` @property(nonatomic, copy, readonly, nonnull) NSURL *outputURL ``` |

Modified [+[AVAssetWriterInputGroup assetWriterInputGroupWithInputs:defaultInput:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinputgroup/1426655-assetwriterinputgroupwithinputs)

|  | Declaration |
| --- | --- |
| From | ``` + (AVAssetWriterInputGroup *)assetWriterInputGroupWithInputs:(NSArray *)inputs defaultInput:(AVAssetWriterInput *)defaultInput ``` |
| To | ``` + (instancetype _Nonnull)assetWriterInputGroupWithInputs:(NSArray<AVAssetWriterInput *> * _Nonnull)inputs defaultInput:(AVAssetWriterInput * _Nullable)defaultInput ``` |

Modified [AVAssetWriterInputGroup.defaultInput](https://developer.apple.com/documentation/avfoundation/avassetwriterinputgroup/1389698-defaultinput)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVAssetWriterInput *defaultInput ``` |
| To | ``` @property(nonatomic, readonly, nullable) AVAssetWriterInput *defaultInput ``` |

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

Modified [-[AVAssetWriterInput addTrackAssociationWithTrackOfInput:type:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1388347-addtrackassociationwithtrackofin)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addTrackAssociationWithTrackOfInput:(AVAssetWriterInput *)input type:(NSString *)trackAssociationType ``` |
| To | ``` - (void)addTrackAssociationWithTrackOfInput:(AVAssetWriterInput * _Nonnull)input type:(NSString * _Nonnull)trackAssociationType ``` |

Modified [-[AVAssetWriterInput appendSampleBuffer:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1389566-appendsamplebuffer)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)appendSampleBuffer:(CMSampleBufferRef)sampleBuffer ``` |
| To | ``` - (BOOL)appendSampleBuffer:(CMSampleBufferRef _Nonnull)sampleBuffer ``` |

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

Modified [-[AVAssetWriterInput canAddTrackAssociationWithTrackOfInput:type:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1388292-canaddtrackassociation)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)canAddTrackAssociationWithTrackOfInput:(AVAssetWriterInput *)input type:(NSString *)trackAssociationType ``` |
| To | ``` - (BOOL)canAddTrackAssociationWithTrackOfInput:(AVAssetWriterInput * _Nonnull)input type:(NSString * _Nonnull)trackAssociationType ``` |

Modified [AVAssetWriterInput.currentPassDescription](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1390627-currentpassdescription)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) AVAssetWriterInputPassDescription *currentPassDescription ``` |
| To | ``` @property(readonly, nullable) AVAssetWriterInputPassDescription *currentPassDescription ``` |

Modified [AVAssetWriterInput.extendedLanguageTag](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1390768-extendedlanguagetag)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *extendedLanguageTag ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *extendedLanguageTag ``` |

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

Modified [AVAssetWriterInput.languageCode](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1388507-languagecode)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *languageCode ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *languageCode ``` |

Modified [AVAssetWriterInput.mediaType](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1385565-mediatype)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *mediaType ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *mediaType ``` |

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

Modified [-[AVAssetWriterInput requestMediaDataWhenReadyOnQueue:usingBlock:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1387508-requestmediadatawhenready)

|  | Declaration |
| --- | --- |
| From | ``` - (void)requestMediaDataWhenReadyOnQueue:(dispatch_queue_t)queue usingBlock:(void (^)(void))block ``` |
| To | ``` - (void)requestMediaDataWhenReadyOnQueue:(dispatch_queue_t _Nonnull)queue usingBlock:(void (^ _Nonnull)(void))block ``` |

Modified [-[AVAssetWriterInput respondToEachPassDescriptionOnQueue:usingBlock:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1388489-respondtoeachpassdescription)

|  | Declaration |
| --- | --- |
| From | ``` - (void)respondToEachPassDescriptionOnQueue:(dispatch_queue_t)queue usingBlock:(dispatch_block_t)block ``` |
| To | ``` - (void)respondToEachPassDescriptionOnQueue:(dispatch_queue_t _Nonnull)queue usingBlock:(dispatch_block_t _Nonnull)block ``` |

Modified [AVAssetWriterInput.sampleReferenceBaseURL](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1386316-samplereferencebaseurl)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSURL *sampleReferenceBaseURL ``` |
| To | ``` @property(nonatomic, copy, nullable) NSURL *sampleReferenceBaseURL ``` |

Modified [AVAssetWriterInput.sourceFormatHint](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1387647-sourceformathint)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) CMFormatDescriptionRef sourceFormatHint ``` |
| To | ``` @property(nonatomic, readonly, nullable) CMFormatDescriptionRef sourceFormatHint ``` |

Modified [-[AVAssetWriterInputMetadataAdaptor appendTimedMetadataGroup:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinputmetadataadaptor/1389014-appendtimedmetadatagroup)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)appendTimedMetadataGroup:(AVTimedMetadataGroup *)timedMetadataGroup ``` |
| To | ``` - (BOOL)appendTimedMetadataGroup:(AVTimedMetadataGroup * _Nonnull)timedMetadataGroup ``` |

Modified [AVAssetWriterInputMetadataAdaptor.assetWriterInput](https://developer.apple.com/documentation/avfoundation/avassetwriterinputmetadataadaptor/1386633-assetwriterinput)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVAssetWriterInput *assetWriterInput ``` |
| To | ``` @property(nonatomic, readonly, nonnull) AVAssetWriterInput *assetWriterInput ``` |

Modified [+[AVAssetWriterInputMetadataAdaptor assetWriterInputMetadataAdaptorWithAssetWriterInput:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinputmetadataadaptor/1449094-assetwriterinputmetadataadaptorw)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)assetWriterInputMetadataAdaptorWithAssetWriterInput:(AVAssetWriterInput *)input ``` |
| To | ``` + (instancetype _Nonnull)assetWriterInputMetadataAdaptorWithAssetWriterInput:(AVAssetWriterInput * _Nonnull)input ``` |

Modified [-[AVAssetWriterInputMetadataAdaptor initWithAssetWriterInput:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinputmetadataadaptor/1389706-initwithassetwriterinput)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithAssetWriterInput:(AVAssetWriterInput *)input ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithAssetWriterInput:(AVAssetWriterInput * _Nonnull)input ``` | yes |

Modified [AVAssetWriterInputPassDescription.sourceTimeRanges](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpassdescription/1388732-sourcetimeranges)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *sourceTimeRanges ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSValue *> *sourceTimeRanges ``` |

Modified [-[AVAssetWriterInputPixelBufferAdaptor appendPixelBuffer:withPresentationTime:]](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/1388102-append)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)appendPixelBuffer:(CVPixelBufferRef)pixelBuffer withPresentationTime:(CMTime)presentationTime ``` |
| To | ``` - (BOOL)appendPixelBuffer:(CVPixelBufferRef _Nonnull)pixelBuffer withPresentationTime:(CMTime)presentationTime ``` |

Modified [AVAssetWriterInputPixelBufferAdaptor.assetWriterInput](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/1387565-assetwriterinput)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVAssetWriterInput *assetWriterInput ``` |
| To | ``` @property(nonatomic, readonly, nonnull) AVAssetWriterInput *assetWriterInput ``` |

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

Modified [AVAssetWriterInputPixelBufferAdaptor.pixelBufferPool](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/1389662-pixelbufferpool)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) CVPixelBufferPoolRef pixelBufferPool ``` |
| To | ``` @property(nonatomic, readonly, nullable) CVPixelBufferPoolRef pixelBufferPool ``` |

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

Modified [-[AVAsynchronousKeyValueLoading statusOfValueForKey:error:]](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/1386816-statusofvalueforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (AVKeyValueStatus)statusOfValueForKey:(NSString *)key error:(NSError **)outError ``` |
| To | ``` - (AVKeyValueStatus)statusOfValueForKey:(NSString * _Nonnull)key error:(NSError * _Nullable * _Nullable)outError ``` |

#### AVAudioBuffer.h

Added [AVAudioCompressedBuffer](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer)Added [AVAudioCompressedBuffer.data](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1390620-data)Added [-[AVAudioCompressedBuffer initWithFormat:packetCapacity:]](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1387124-init)Added [-[AVAudioCompressedBuffer initWithFormat:packetCapacity:maximumPacketSize:]](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1386718-initwithformat)Added [AVAudioCompressedBuffer.maximumPacketSize](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1389326-maximumpacketsize)Added [AVAudioCompressedBuffer.packetCapacity](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1386081-packetcapacity)Added [AVAudioCompressedBuffer.packetCount](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1386000-packetcount)Added [AVAudioCompressedBuffer.packetDescriptions](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1389750-packetdescriptions)Modified [AVAudioBuffer.audioBufferList](https://developer.apple.com/documentation/avfoundation/avaudiobuffer/1385579-audiobufferlist)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) const AudioBufferList *audioBufferList ``` |
| To | ``` @property(nonatomic, readonly, nonnull) const AudioBufferList *audioBufferList ``` |

Modified [AVAudioBuffer.format](https://developer.apple.com/documentation/avfoundation/avaudiobuffer/1387540-format)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVAudioFormat *format ``` |
| To | ``` @property(nonatomic, readonly, nonnull) AVAudioFormat *format ``` |

Modified [AVAudioBuffer.mutableAudioBufferList](https://developer.apple.com/documentation/avfoundation/avaudiobuffer/1389207-mutableaudiobufferlist)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AudioBufferList *mutableAudioBufferList ``` |
| To | ``` @property(nonatomic, readonly, nonnull) AudioBufferList *mutableAudioBufferList ``` |

Modified [AVAudioPCMBuffer.floatChannelData](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1386212-floatchanneldata)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) float *const *floatChannelData ``` |
| To | ``` @property(nonatomic, readonly, nonnull) float *const  * _Nullable floatChannelData ``` |

Modified [-[AVAudioPCMBuffer initWithPCMFormat:frameCapacity:]](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1389630-initwithpcmformat)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithPCMFormat:(AVAudioFormat *)format frameCapacity:(AVAudioFrameCount)frameCapacity ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithPCMFormat:(AVAudioFormat * _Nonnull)format frameCapacity:(AVAudioFrameCount)frameCapacity ``` | yes |

Modified [AVAudioPCMBuffer.int16ChannelData](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1388925-int16channeldata)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) int16_t *const *int16ChannelData ``` |
| To | ``` @property(nonatomic, readonly, nonnull) int16_t *const  * _Nullable int16ChannelData ``` |

Modified [AVAudioPCMBuffer.int32ChannelData](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1389756-int32channeldata)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) int32_t *const *int32ChannelData ``` |
| To | ``` @property(nonatomic, readonly, nonnull) int32_t *const  * _Nullable int32ChannelData ``` |

#### AVAudioChannelLayout.h

Modified [AVAudioChannelLayout](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSSecureCoding |

Modified [-[AVAudioChannelLayout initWithLayout:]](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1387623-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithLayout:(const AudioChannelLayout *)layout ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithLayout:(const AudioChannelLayout * _Nonnull)layout ``` | yes |

Modified [-[AVAudioChannelLayout initWithLayoutTag:]](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1388320-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithLayoutTag:(AudioChannelLayoutTag)layoutTag ``` |
| To | ``` - (instancetype _Nonnull)initWithLayoutTag:(AudioChannelLayoutTag)layoutTag ``` |

Modified [-[AVAudioChannelLayout isEqual:]](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1389677-isequal)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isEqual:(id)object ``` |
| To | ``` - (BOOL)isEqual:(id _Nonnull)object ``` |

Modified [AVAudioChannelLayout.layout](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1385786-layout)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) const AudioChannelLayout *layout ``` |
| To | ``` @property(nonatomic, readonly, nonnull) const AudioChannelLayout *layout ``` |

Modified [+[AVAudioChannelLayout layoutWithLayout:]](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1397770-layoutwithlayout)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)layoutWithLayout:(const AudioChannelLayout *)layout ``` |
| To | ``` + (instancetype _Nonnull)layoutWithLayout:(const AudioChannelLayout * _Nonnull)layout ``` |

Modified [+[AVAudioChannelLayout layoutWithLayoutTag:]](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1397765-layoutwithlayouttag)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)layoutWithLayoutTag:(AudioChannelLayoutTag)layoutTag ``` |
| To | ``` + (instancetype _Nonnull)layoutWithLayoutTag:(AudioChannelLayoutTag)layoutTag ``` |

#### AVAudioConnectionPoint.h (Added)

Added [AVAudioConnectionPoint](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint)Added [AVAudioConnectionPoint.bus](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint/1389288-bus)Added [-[AVAudioConnectionPoint initWithNode:bus:]](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint/1388569-initwithnode)Added [AVAudioConnectionPoint.node](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint/1386935-node)

#### AVAudioConverter.h (Added)

Added [AVAudioConverter](https://developer.apple.com/documentation/avfoundation/avaudioconverter)Added [AVAudioConverter.applicableEncodeBitRates](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388940-applicableencodebitrates)Added [AVAudioConverter.applicableEncodeSampleRates](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1389427-applicableencodesamplerates)Added [AVAudioConverter.availableEncodeBitRates](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388589-availableencodebitrates)Added [AVAudioConverter.availableEncodeChannelLayoutTags](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387337-availableencodechannellayouttags)Added [AVAudioConverter.availableEncodeSampleRates](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1386202-availableencodesamplerates)Added [AVAudioConverter.bitRate](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390373-bitrate)Added [AVAudioConverter.bitRateStrategy](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1386092-bitratestrategy)Added [AVAudioConverter.channelMap](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390653-channelmap)Added [-[AVAudioConverter convertToBuffer:error:withInputFromBlock:]](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387865-converttobuffer)Added [-[AVAudioConverter convertToBuffer:fromBuffer:error:]](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388341-converttobuffer)Added [AVAudioConverter.dither](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1386312-dither)Added [AVAudioConverter.downmix](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388244-downmix)Added [-[AVAudioConverter initFromFormat:toFormat:]](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387008-initfromformat)Added [AVAudioConverter.inputFormat](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388914-inputformat)Added [AVAudioConverter.magicCookie](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390770-magiccookie)Added [AVAudioConverter.maximumOutputPacketSize](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390069-maximumoutputpacketsize)Added [AVAudioConverter.outputFormat](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387563-outputformat)Added [AVAudioConverter.primeInfo](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1389770-primeinfo)Added [AVAudioConverter.primeMethod](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387299-primemethod)Added [-[AVAudioConverter reset]](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390876-reset)Added [AVAudioConverter.sampleRateConverterAlgorithm](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387976-samplerateconverteralgorithm)Added [AVAudioConverter.sampleRateConverterQuality](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390887-samplerateconverterquality)Added AVAudioConverter(Encoding)Added [AVAudioConverterInputBlock](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputblock)Added [AVAudioConverterInputStatus](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus)Added [AVAudioConverterInputStatus_EndOfStream](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus/endofstream)Added [AVAudioConverterInputStatus_HaveData](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus/havedata)Added [AVAudioConverterInputStatus_NoDataNow](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus/avaudioconverterinputstatus_nodatanow)Added [AVAudioConverterOutputStatus](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus)Added [AVAudioConverterOutputStatus_EndOfStream](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/endofstream)Added [AVAudioConverterOutputStatus_Error](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/error)Added [AVAudioConverterOutputStatus_HaveData](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/havedata)Added [AVAudioConverterOutputStatus_InputRanDry](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/inputrandry)Added [AVAudioConverterPrimeInfo](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimeinfo)Added [AVAudioConverterPrimeMethod](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod)Added [AVAudioConverterPrimeMethod_None](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod/none)Added [AVAudioConverterPrimeMethod_Normal](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod/normal)Added [AVAudioConverterPrimeMethod_Pre](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod/avaudioconverterprimemethod_pre)

#### AVAudioEngine.h

Added [-[AVAudioEngine connect:toConnectionPoints:fromBus:format:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389510-connect)Added [-[AVAudioEngine inputConnectionPointForNode:inputBus:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1387521-inputconnectionpoint)Added [-[AVAudioEngine outputConnectionPointsForNode:outputBus:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389298-outputconnectionpointsfornode)Modified [-[AVAudioEngine attachNode:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1390685-attach)

|  | Declaration |
| --- | --- |
| From | ``` - (void)attachNode:(AVAudioNode *)node ``` |
| To | ``` - (void)attachNode:(AVAudioNode * _Nonnull)node ``` |

Modified [-[AVAudioEngine connect:to:format:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1388974-connect)

|  | Declaration |
| --- | --- |
| From | ``` - (void)connect:(AVAudioNode *)node1 to:(AVAudioNode *)node2 format:(AVAudioFormat *)format ``` |
| To | ``` - (void)connect:(AVAudioNode * _Nonnull)node1 to:(AVAudioNode * _Nonnull)node2 format:(AVAudioFormat * _Nullable)format ``` |

Modified [-[AVAudioEngine connect:to:fromBus:toBus:format:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389776-connect)

|  | Declaration |
| --- | --- |
| From | ``` - (void)connect:(AVAudioNode *)node1 to:(AVAudioNode *)node2 fromBus:(AVAudioNodeBus)bus1 toBus:(AVAudioNodeBus)bus2 format:(AVAudioFormat *)format ``` |
| To | ``` - (void)connect:(AVAudioNode * _Nonnull)node1 to:(AVAudioNode * _Nonnull)node2 fromBus:(AVAudioNodeBus)bus1 toBus:(AVAudioNodeBus)bus2 format:(AVAudioFormat * _Nullable)format ``` |

Modified [-[AVAudioEngine detachNode:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1388198-detachnode)

|  | Declaration |
| --- | --- |
| From | ``` - (void)detachNode:(AVAudioNode *)node ``` |
| To | ``` - (void)detachNode:(AVAudioNode * _Nonnull)node ``` |

Modified [-[AVAudioEngine disconnectNodeInput:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1388181-disconnectnodeinput)

|  | Declaration |
| --- | --- |
| From | ``` - (void)disconnectNodeInput:(AVAudioNode *)node ``` |
| To | ``` - (void)disconnectNodeInput:(AVAudioNode * _Nonnull)node ``` |

Modified [-[AVAudioEngine disconnectNodeInput:bus:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1387251-disconnectnodeinput)

|  | Declaration |
| --- | --- |
| From | ``` - (void)disconnectNodeInput:(AVAudioNode *)node bus:(AVAudioNodeBus)bus ``` |
| To | ``` - (void)disconnectNodeInput:(AVAudioNode * _Nonnull)node bus:(AVAudioNodeBus)bus ``` |

Modified [-[AVAudioEngine disconnectNodeOutput:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1386992-disconnectnodeoutput)

|  | Declaration |
| --- | --- |
| From | ``` - (void)disconnectNodeOutput:(AVAudioNode *)node ``` |
| To | ``` - (void)disconnectNodeOutput:(AVAudioNode * _Nonnull)node ``` |

Modified [-[AVAudioEngine disconnectNodeOutput:bus:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1390352-disconnectnodeoutput)

|  | Declaration |
| --- | --- |
| From | ``` - (void)disconnectNodeOutput:(AVAudioNode *)node bus:(AVAudioNodeBus)bus ``` |
| To | ``` - (void)disconnectNodeOutput:(AVAudioNode * _Nonnull)node bus:(AVAudioNodeBus)bus ``` |

Modified [-[AVAudioEngine init]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1390381-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)init ``` |
| To | ``` - (instancetype _Nonnull)init ``` |

Modified [AVAudioEngine.inputNode](https://developer.apple.com/documentation/avfoundation/avaudioengine/1386063-inputnode)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) AVAudioInputNode *inputNode ``` |
| To | ``` @property(readonly, nonatomic, nullable) AVAudioInputNode *inputNode ``` |

Modified [AVAudioEngine.mainMixerNode](https://developer.apple.com/documentation/avfoundation/avaudioengine/1385813-mainmixernode)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) AVAudioMixerNode *mainMixerNode ``` |
| To | ``` @property(readonly, nonatomic, nonnull) AVAudioMixerNode *mainMixerNode ``` |

Modified [AVAudioEngine.musicSequence](https://developer.apple.com/documentation/avfoundation/avaudioengine/1390410-musicsequence)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic) MusicSequence musicSequence ``` |
| To | ``` @property(nonatomic, nullable) MusicSequence musicSequence ``` |

Modified [AVAudioEngine.outputNode](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389103-outputnode)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) AVAudioOutputNode *outputNode ``` |
| To | ``` @property(readonly, nonatomic, nonnull) AVAudioOutputNode *outputNode ``` |

Modified [-[AVAudioEngine startAndReturnError:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1387024-startandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)startAndReturnError:(NSError **)outError ``` |
| To | ``` - (BOOL)startAndReturnError:(NSError * _Nullable * _Nullable)outError ``` |

#### AVAudioEnvironmentNode.h

Modified [AVAudioEnvironmentNode.applicableRenderingAlgorithms](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1390049-applicablerenderingalgorithms)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)applicableRenderingAlgorithms ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSNumber *> *applicableRenderingAlgorithms ``` |

Modified [AVAudioEnvironmentNode.distanceAttenuationParameters](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1387396-distanceattenuationparameters)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVAudioEnvironmentDistanceAttenuationParameters *distanceAttenuationParameters ``` |
| To | ``` @property(nonatomic, readonly, nonnull) AVAudioEnvironmentDistanceAttenuationParameters *distanceAttenuationParameters ``` |

Modified [AVAudioEnvironmentNode.reverbParameters](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1389020-reverbparameters)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVAudioEnvironmentReverbParameters *reverbParameters ``` |
| To | ``` @property(nonatomic, readonly, nonnull) AVAudioEnvironmentReverbParameters *reverbParameters ``` |

Modified [AVAudioEnvironmentReverbParameters.filterParameters](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentreverbparameters/1387313-filterparameters)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVAudioUnitEQFilterParameters *filterParameters ``` |
| To | ``` @property(nonatomic, readonly, nonnull) AVAudioUnitEQFilterParameters *filterParameters ``` |

#### AVAudioFile.h

Modified [AVAudioFile.fileFormat](https://developer.apple.com/documentation/avfoundation/avaudiofile/1387096-fileformat)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVAudioFormat *fileFormat ``` |
| To | ``` @property(nonatomic, readonly, nonnull) AVAudioFormat *fileFormat ``` |

Modified [-[AVAudioFile initForReading:commonFormat:interleaved:error:]](https://developer.apple.com/documentation/avfoundation/avaudiofile/1387283-initforreading)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initForReading:(NSURL *)fileURL commonFormat:(AVAudioCommonFormat)format interleaved:(BOOL)interleaved error:(NSError **)outError ``` |
| To | ``` - (instancetype _Nullable)initForReading:(NSURL * _Nonnull)fileURL commonFormat:(AVAudioCommonFormat)format interleaved:(BOOL)interleaved error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [-[AVAudioFile initForReading:error:]](https://developer.apple.com/documentation/avfoundation/avaudiofile/1388218-initforreading)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initForReading:(NSURL *)fileURL error:(NSError **)outError ``` |
| To | ``` - (instancetype _Nullable)initForReading:(NSURL * _Nonnull)fileURL error:(NSError * _Nullable * _Nullable)outError ``` |

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

Modified [AVAudioFile.processingFormat](https://developer.apple.com/documentation/avfoundation/avaudiofile/1388308-processingformat)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVAudioFormat *processingFormat ``` |
| To | ``` @property(nonatomic, readonly, nonnull) AVAudioFormat *processingFormat ``` |

Modified [-[AVAudioFile readIntoBuffer:error:]](https://developer.apple.com/documentation/avfoundation/avaudiofile/1388043-read)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)readIntoBuffer:(AVAudioPCMBuffer *)buffer error:(NSError **)outError ``` |
| To | ``` - (BOOL)readIntoBuffer:(AVAudioPCMBuffer * _Nonnull)buffer error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [-[AVAudioFile readIntoBuffer:frameCount:error:]](https://developer.apple.com/documentation/avfoundation/avaudiofile/1389774-read)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)readIntoBuffer:(AVAudioPCMBuffer *)buffer frameCount:(AVAudioFrameCount)frames error:(NSError **)outError ``` |
| To | ``` - (BOOL)readIntoBuffer:(AVAudioPCMBuffer * _Nonnull)buffer frameCount:(AVAudioFrameCount)frames error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [AVAudioFile.url](https://developer.apple.com/documentation/avfoundation/avaudiofile/1387360-url)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSURL *url ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSURL *url ``` |

Modified [-[AVAudioFile writeFromBuffer:error:]](https://developer.apple.com/documentation/avfoundation/avaudiofile/1385637-write)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)writeFromBuffer:(const AVAudioPCMBuffer *)buffer error:(NSError **)outError ``` |
| To | ``` - (BOOL)writeFromBuffer:(const AVAudioPCMBuffer * _Nonnull)buffer error:(NSError * _Nullable * _Nullable)outError ``` |

#### AVAudioFormat.h

Added [AVAudioFormat.formatDescription](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387467-formatdescription)Added [-[AVAudioFormat initWithCMAudioFormatDescription:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387465-init)Modified [AVAudioFormat](https://developer.apple.com/documentation/avfoundation/avaudioformat)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSSecureCoding |

Modified [AVAudioFormat.channelLayout](https://developer.apple.com/documentation/avfoundation/avaudioformat/1390671-channellayout)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) const AVAudioChannelLayout *channelLayout ``` |
| To | ``` @property(nonatomic, readonly, nullable) const AVAudioChannelLayout *channelLayout ``` |

Modified [-[AVAudioFormat initStandardFormatWithSampleRate:channelLayout:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1388426-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initStandardFormatWithSampleRate:(double)sampleRate channelLayout:(AVAudioChannelLayout *)layout ``` |
| To | ``` - (instancetype _Nonnull)initStandardFormatWithSampleRate:(double)sampleRate channelLayout:(AVAudioChannelLayout * _Nonnull)layout ``` |

Modified [-[AVAudioFormat initStandardFormatWithSampleRate:channels:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1390416-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initStandardFormatWithSampleRate:(double)sampleRate channels:(AVAudioChannelCount)channels ``` |
| To | ``` - (instancetype _Nonnull)initStandardFormatWithSampleRate:(double)sampleRate channels:(AVAudioChannelCount)channels ``` |

Modified [-[AVAudioFormat initWithCommonFormat:sampleRate:channels:interleaved:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1390591-initwithcommonformat)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithCommonFormat:(AVAudioCommonFormat)format sampleRate:(double)sampleRate channels:(AVAudioChannelCount)channels interleaved:(BOOL)interleaved ``` |
| To | ``` - (instancetype _Nonnull)initWithCommonFormat:(AVAudioCommonFormat)format sampleRate:(double)sampleRate channels:(AVAudioChannelCount)channels interleaved:(BOOL)interleaved ``` |

Modified [-[AVAudioFormat initWithCommonFormat:sampleRate:interleaved:channelLayout:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1389361-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithCommonFormat:(AVAudioCommonFormat)format sampleRate:(double)sampleRate interleaved:(BOOL)interleaved channelLayout:(AVAudioChannelLayout *)layout ``` |
| To | ``` - (instancetype _Nonnull)initWithCommonFormat:(AVAudioCommonFormat)format sampleRate:(double)sampleRate interleaved:(BOOL)interleaved channelLayout:(AVAudioChannelLayout * _Nonnull)layout ``` |

Modified [-[AVAudioFormat initWithSettings:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387931-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSettings:(NSDictionary *)settings ``` |
| To | ``` - (instancetype _Nonnull)initWithSettings:(NSDictionary<NSString *,id> * _Nonnull)settings ``` |

Modified [-[AVAudioFormat initWithStreamDescription:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1390106-initwithstreamdescription)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithStreamDescription:(const AudioStreamBasicDescription *)asbd ``` |
| To | ``` - (instancetype _Nonnull)initWithStreamDescription:(const AudioStreamBasicDescription * _Nonnull)asbd ``` |

Modified [-[AVAudioFormat initWithStreamDescription:channelLayout:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1389347-initwithstreamdescription)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithStreamDescription:(const AudioStreamBasicDescription *)asbd channelLayout:(AVAudioChannelLayout *)layout ``` |
| To | ``` - (instancetype _Nonnull)initWithStreamDescription:(const AudioStreamBasicDescription * _Nonnull)asbd channelLayout:(AVAudioChannelLayout * _Nullable)layout ``` |

Modified [-[AVAudioFormat isEqual:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1385683-isequal)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isEqual:(id)object ``` |
| To | ``` - (BOOL)isEqual:(id _Nonnull)object ``` |

Modified [AVAudioFormat.settings](https://developer.apple.com/documentation/avfoundation/avaudioformat/1386904-settings)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDictionary *settings ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSDictionary<NSString *,id> *settings ``` |

Modified [AVAudioFormat.streamDescription](https://developer.apple.com/documentation/avfoundation/avaudioformat/1386843-streamdescription)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) const AudioStreamBasicDescription *streamDescription ``` |
| To | ``` @property(nonatomic, readonly, nonnull) const AudioStreamBasicDescription *streamDescription ``` |

#### AVAudioIONode.h

Modified [AVAudioIONode.audioUnit](https://developer.apple.com/documentation/avfoundation/avaudioionode/1390587-audiounit)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AudioUnit audioUnit ``` |
| To | ``` @property(nonatomic, readonly, nullable) AudioUnit audioUnit ``` |

#### AVAudioMix.h

Modified [AVAudioMix.inputParameters](https://developer.apple.com/documentation/avfoundation/avaudiomix/1388791-inputparameters)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *inputParameters ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<AVAudioMixInputParameters *> *inputParameters ``` |

Modified [AVAudioMixInputParameters.audioTapProcessor](https://developer.apple.com/documentation/avfoundation/avaudiomixinputparameters/1388578-audiotapprocessor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) MTAudioProcessingTapRef audioTapProcessor ``` |
| To | ``` @property(nonatomic, readonly, retain, nullable) MTAudioProcessingTapRef audioTapProcessor ``` |

Modified [AVAudioMixInputParameters.audioTimePitchAlgorithm](https://developer.apple.com/documentation/avfoundation/avaudiomixinputparameters/1387042-audiotimepitchalgorithm)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *audioTimePitchAlgorithm ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *audioTimePitchAlgorithm ``` |

Modified [-[AVAudioMixInputParameters getVolumeRampForTime:startVolume:endVolume:timeRange:]](https://developer.apple.com/documentation/avfoundation/avaudiomixinputparameters/1389578-getvolumerampfortime)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)getVolumeRampForTime:(CMTime)time startVolume:(float *)startVolume endVolume:(float *)endVolume timeRange:(CMTimeRange *)timeRange ``` |
| To | ``` - (BOOL)getVolumeRampForTime:(CMTime)time startVolume:(float * _Nullable)startVolume endVolume:(float * _Nullable)endVolume timeRange:(CMTimeRange * _Nullable)timeRange ``` |

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

Modified [AVMutableAudioMixInputParameters.audioTapProcessor](https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/1389296-audiotapprocessor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) MTAudioProcessingTapRef audioTapProcessor ``` |
| To | ``` @property(nonatomic, retain, nullable) MTAudioProcessingTapRef audioTapProcessor ``` |

Modified [AVMutableAudioMixInputParameters.audioTimePitchAlgorithm](https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/1388300-audiotimepitchalgorithm)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *audioTimePitchAlgorithm ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *audioTimePitchAlgorithm ``` |

#### AVAudioMixing.h

Added [-[AVAudioMixing destinationForMixer:bus:]](https://developer.apple.com/documentation/avfoundation/avaudiomixing/1390356-destination)Added [AVAudioMixingDestination](https://developer.apple.com/documentation/avfoundation/avaudiomixingdestination)Added [AVAudioMixingDestination.connectionPoint](https://developer.apple.com/documentation/avfoundation/avaudiomixingdestination/1389898-connectionpoint)

#### AVAudioNode.h

Modified [AVAudioNode.engine](https://developer.apple.com/documentation/avfoundation/avaudionode/1386896-engine)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVAudioEngine *engine ``` |
| To | ``` @property(nonatomic, readonly, nullable) AVAudioEngine *engine ``` |

Modified [-[AVAudioNode inputFormatForBus:]](https://developer.apple.com/documentation/avfoundation/avaudionode/1390147-inputformat)

|  | Declaration |
| --- | --- |
| From | ``` - (AVAudioFormat *)inputFormatForBus:(AVAudioNodeBus)bus ``` |
| To | ``` - (AVAudioFormat * _Nonnull)inputFormatForBus:(AVAudioNodeBus)bus ``` |

Modified [-[AVAudioNode installTapOnBus:bufferSize:format:block:]](https://developer.apple.com/documentation/avfoundation/avaudionode/1387122-installtap)

|  | Declaration |
| --- | --- |
| From | ``` - (void)installTapOnBus:(AVAudioNodeBus)bus bufferSize:(AVAudioFrameCount)bufferSize format:(AVAudioFormat *)format block:(AVAudioNodeTapBlock)tapBlock ``` |
| To | ``` - (void)installTapOnBus:(AVAudioNodeBus)bus bufferSize:(AVAudioFrameCount)bufferSize format:(AVAudioFormat * _Nullable)format block:(AVAudioNodeTapBlock _Nonnull)tapBlock ``` |

Modified [AVAudioNode.lastRenderTime](https://developer.apple.com/documentation/avfoundation/avaudionode/1385978-lastrendertime)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVAudioTime *lastRenderTime ``` |
| To | ``` @property(nonatomic, readonly, nullable) AVAudioTime *lastRenderTime ``` |

Modified [-[AVAudioNode nameForInputBus:]](https://developer.apple.com/documentation/avfoundation/avaudionode/1387710-name)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)nameForInputBus:(AVAudioNodeBus)bus ``` |
| To | ``` - (NSString * _Nonnull)nameForInputBus:(AVAudioNodeBus)bus ``` |

Modified [-[AVAudioNode nameForOutputBus:]](https://developer.apple.com/documentation/avfoundation/avaudionode/1390811-name)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)nameForOutputBus:(AVAudioNodeBus)bus ``` |
| To | ``` - (NSString * _Nonnull)nameForOutputBus:(AVAudioNodeBus)bus ``` |

Modified [-[AVAudioNode outputFormatForBus:]](https://developer.apple.com/documentation/avfoundation/avaudionode/1389195-outputformatforbus)

|  | Declaration |
| --- | --- |
| From | ``` - (AVAudioFormat *)outputFormatForBus:(AVAudioNodeBus)bus ``` |
| To | ``` - (AVAudioFormat * _Nonnull)outputFormatForBus:(AVAudioNodeBus)bus ``` |

#### AVAudioPlayer.h

Modified [AVAudioPlayer.data](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389437-data)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSData *data ``` |
| To | ``` @property(readonly, nullable) NSData *data ``` |

Modified [AVAudioPlayer.delegate](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387134-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<AVAudioPlayerDelegate> delegate ``` |
| To | ``` @property(assign, nullable) id<AVAudioPlayerDelegate> delegate ``` |

Modified [-[AVAudioPlayer initWithContentsOfURL:error:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387281-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithContentsOfURL:(NSURL *)url error:(NSError **)outError ``` |
| To | ``` - (instancetype _Nullable)initWithContentsOfURL:(NSURL * _Nonnull)url error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [-[AVAudioPlayer initWithContentsOfURL:fileTypeHint:error:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388349-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithContentsOfURL:(NSURL *)url fileTypeHint:(NSString *)utiString error:(NSError **)outError ``` |
| To | ``` - (instancetype _Nullable)initWithContentsOfURL:(NSURL * _Nonnull)url fileTypeHint:(NSString * _Nullable)utiString error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [-[AVAudioPlayer initWithData:error:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388809-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithData:(NSData *)data error:(NSError **)outError ``` |
| To | ``` - (instancetype _Nullable)initWithData:(NSData * _Nonnull)data error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [-[AVAudioPlayer initWithData:fileTypeHint:error:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388525-initwithdata)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithData:(NSData *)data fileTypeHint:(NSString *)utiString error:(NSError **)outError ``` |
| To | ``` - (instancetype _Nullable)initWithData:(NSData * _Nonnull)data fileTypeHint:(NSString * _Nullable)utiString error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [AVAudioPlayer.settings](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389359-settings)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSDictionary *settings ``` |
| To | ``` @property(readonly, nonnull) NSDictionary<NSString *,id> *settings ``` |

Modified [AVAudioPlayer.url](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387448-url)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSURL *url ``` |
| To | ``` @property(readonly, nullable) NSURL *url ``` |

Modified [-[AVAudioPlayerDelegate audioPlayerDecodeErrorDidOccur:error:]](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1387676-audioplayerdecodeerrordidoccur)

|  | Declaration |
| --- | --- |
| From | ``` - (void)audioPlayerDecodeErrorDidOccur:(AVAudioPlayer *)player error:(NSError *)error ``` |
| To | ``` - (void)audioPlayerDecodeErrorDidOccur:(AVAudioPlayer * _Nonnull)player error:(NSError * _Nullable)error ``` |

Modified [-[AVAudioPlayerDelegate audioPlayerDidFinishPlaying:successfully:]](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1389160-audioplayerdidfinishplaying)

|  | Declaration |
| --- | --- |
| From | ``` - (void)audioPlayerDidFinishPlaying:(AVAudioPlayer *)player successfully:(BOOL)flag ``` |
| To | ``` - (void)audioPlayerDidFinishPlaying:(AVAudioPlayer * _Nonnull)player successfully:(BOOL)flag ``` |

#### AVAudioPlayerNode.h

Modified [-[AVAudioPlayerNode nodeTimeForPlayerTime:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1386450-nodetime)

|  | Declaration |
| --- | --- |
| From | ``` - (AVAudioTime *)nodeTimeForPlayerTime:(AVAudioTime *)playerTime ``` |
| To | ``` - (AVAudioTime * _Nullable)nodeTimeForPlayerTime:(AVAudioTime * _Nonnull)playerTime ``` |

Modified [-[AVAudioPlayerNode playAtTime:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1389304-playattime)

|  | Declaration |
| --- | --- |
| From | ``` - (void)playAtTime:(AVAudioTime *)when ``` |
| To | ``` - (void)playAtTime:(AVAudioTime * _Nullable)when ``` |

Modified [-[AVAudioPlayerNode playerTimeForNodeTime:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1390449-playertime)

|  | Declaration |
| --- | --- |
| From | ``` - (AVAudioTime *)playerTimeForNodeTime:(AVAudioTime *)nodeTime ``` |
| To | ``` - (AVAudioTime * _Nullable)playerTimeForNodeTime:(AVAudioTime * _Nonnull)nodeTime ``` |

Modified [-[AVAudioPlayerNode scheduleBuffer:atTime:options:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1388422-schedulebuffer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)scheduleBuffer:(AVAudioPCMBuffer *)buffer atTime:(AVAudioTime *)when options:(AVAudioPlayerNodeBufferOptions)options completionHandler:(AVAudioNodeCompletionHandler)completionHandler ``` |
| To | ``` - (void)scheduleBuffer:(AVAudioPCMBuffer * _Nonnull)buffer atTime:(AVAudioTime * _Nullable)when options:(AVAudioPlayerNodeBufferOptions)options completionHandler:(AVAudioNodeCompletionHandler _Nullable)completionHandler ``` |

Modified [-[AVAudioPlayerNode scheduleBuffer:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1389996-schedulebuffer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)scheduleBuffer:(AVAudioPCMBuffer *)buffer completionHandler:(AVAudioNodeCompletionHandler)completionHandler ``` |
| To | ``` - (void)scheduleBuffer:(AVAudioPCMBuffer * _Nonnull)buffer completionHandler:(AVAudioNodeCompletionHandler _Nullable)completionHandler ``` |

Modified [-[AVAudioPlayerNode scheduleFile:atTime:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1390047-schedulefile)

|  | Declaration |
| --- | --- |
| From | ``` - (void)scheduleFile:(AVAudioFile *)file atTime:(AVAudioTime *)when completionHandler:(AVAudioNodeCompletionHandler)completionHandler ``` |
| To | ``` - (void)scheduleFile:(AVAudioFile * _Nonnull)file atTime:(AVAudioTime * _Nullable)when completionHandler:(AVAudioNodeCompletionHandler _Nullable)completionHandler ``` |

Modified [-[AVAudioPlayerNode scheduleSegment:startingFrame:frameCount:atTime:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1385884-schedulesegment)

|  | Declaration |
| --- | --- |
| From | ``` - (void)scheduleSegment:(AVAudioFile *)file startingFrame:(AVAudioFramePosition)startFrame frameCount:(AVAudioFrameCount)numberFrames atTime:(AVAudioTime *)when completionHandler:(AVAudioNodeCompletionHandler)completionHandler ``` |
| To | ``` - (void)scheduleSegment:(AVAudioFile * _Nonnull)file startingFrame:(AVAudioFramePosition)startFrame frameCount:(AVAudioFrameCount)numberFrames atTime:(AVAudioTime * _Nullable)when completionHandler:(AVAudioNodeCompletionHandler _Nullable)completionHandler ``` |

#### AVAudioRecorder.h

Modified [AVAudioRecorder.delegate](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1385839-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<AVAudioRecorderDelegate> delegate ``` |
| To | ``` @property(assign, nullable) id<AVAudioRecorderDelegate> delegate ``` |

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

Modified [AVAudioRecorder.url](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1389050-url)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSURL *url ``` |
| To | ``` @property(readonly, nonnull) NSURL *url ``` |

Modified [-[AVAudioRecorderDelegate audioRecorderDidFinishRecording:successfully:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate/1388688-audiorecorderdidfinishrecording)

|  | Declaration |
| --- | --- |
| From | ``` - (void)audioRecorderDidFinishRecording:(AVAudioRecorder *)recorder successfully:(BOOL)flag ``` |
| To | ``` - (void)audioRecorderDidFinishRecording:(AVAudioRecorder * _Nonnull)recorder successfully:(BOOL)flag ``` |

Modified [-[AVAudioRecorderDelegate audioRecorderEncodeErrorDidOccur:error:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate/1387774-audiorecorderencodeerrordidoccur)

|  | Declaration |
| --- | --- |
| From | ``` - (void)audioRecorderEncodeErrorDidOccur:(AVAudioRecorder *)recorder error:(NSError *)error ``` |
| To | ``` - (void)audioRecorderEncodeErrorDidOccur:(AVAudioRecorder * _Nonnull)recorder error:(NSError * _Nullable)error ``` |

#### AVAudioSequencer.h (Added)

Added [AVAudioSequencer](https://developer.apple.com/documentation/avfoundation/avaudiosequencer)Added [-[AVAudioSequencer beatsForHostTime:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1389012-beats)Added [-[AVAudioSequencer beatsForSeconds:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387853-beats)Added [AVAudioSequencer.currentPositionInBeats](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388910-currentpositioninbeats)Added [AVAudioSequencer.currentPositionInSeconds](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1390524-currentpositioninseconds)Added [-[AVAudioSequencer dataWithSMPTEResolution:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388701-datawithsmpteresolution)Added [-[AVAudioSequencer hostTimeForBeats:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1386184-hosttime)Added [-[AVAudioSequencer init]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1385851-init)Added [-[AVAudioSequencer initWithAudioEngine:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388339-init)Added [-[AVAudioSequencer loadFromData:options:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1389720-load)Added [-[AVAudioSequencer loadFromURL:options:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1386241-load)Added [AVAudioSequencer.playing](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388402-playing)Added [-[AVAudioSequencer prepareToPlay]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1385633-preparetoplay)Added [AVAudioSequencer.rate](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387903-rate)Added [-[AVAudioSequencer secondsForBeats:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387615-seconds)Added [-[AVAudioSequencer startAndReturnError:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387594-start)Added [-[AVAudioSequencer stop]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1386674-stop)Added [AVAudioSequencer.tempoTrack](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1390252-tempotrack)Added [AVAudioSequencer.tracks](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387567-tracks)Added [AVAudioSequencer.userInfo](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1389262-userinfo)Added [-[AVAudioSequencer writeToURL:SMPTEResolution:replaceExisting:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1390589-write)Added [AVMusicTrack](https://developer.apple.com/documentation/avfoundation/avmusictrack)Added [AVMusicTrack.destinationAudioUnit](https://developer.apple.com/documentation/avfoundation/avmusictrack/1390533-destinationaudiounit)Added [AVMusicTrack.destinationMIDIEndpoint](https://developer.apple.com/documentation/avfoundation/avmusictrack/1388828-destinationmidiendpoint)Added [AVMusicTrack.lengthInBeats](https://developer.apple.com/documentation/avfoundation/avmusictrack/1389910-lengthinbeats)Added [AVMusicTrack.lengthInSeconds](https://developer.apple.com/documentation/avfoundation/avmusictrack/1385749-lengthinseconds)Added [AVMusicTrack.loopingEnabled](https://developer.apple.com/documentation/avfoundation/avmusictrack/1385811-isloopingenabled)Added [AVMusicTrack.loopRange](https://developer.apple.com/documentation/avfoundation/avmusictrack/1386292-looprange)Added [AVMusicTrack.muted](https://developer.apple.com/documentation/avfoundation/avmusictrack/1387694-muted)Added [AVMusicTrack.numberOfLoops](https://developer.apple.com/documentation/avfoundation/avmusictrack/1389268-numberofloops)Added [AVMusicTrack.offsetTime](https://developer.apple.com/documentation/avfoundation/avmusictrack/1386336-offsettime)Added [AVMusicTrack.soloed](https://developer.apple.com/documentation/avfoundation/avmusictrack/1387883-issoloed)Added [AVMusicTrack.timeResolution](https://developer.apple.com/documentation/avfoundation/avmusictrack/1387198-timeresolution)Added AVAudioSequencer(AVAudioSequencer_Player)Added [AVBeatRange](https://developer.apple.com/documentation/avfoundation/avbeatrange)Added [AVMakeBeatRange()](https://developer.apple.com/documentation/avfoundation/1386774-avmakebeatrange)Added [AVMusicSequenceLoadOptions](https://developer.apple.com/documentation/avfoundation/avmusicsequenceloadoptions)Added [AVMusicSequenceLoadSMF_ChannelsToTracks](https://developer.apple.com/documentation/avfoundation/avmusicsequenceloadoptions/1388410-smfchannelstotracks)Added [AVMusicSequenceLoadSMF_PreserveTracks](https://developer.apple.com/documentation/avfoundation/avmusicsequenceloadoptions/avmusicsequenceloadsmf_preservetracks)Added [AVMusicTimeStamp](https://developer.apple.com/documentation/avfoundation/avmusictimestamp)Added [AVMusicTrackLoopCount](https://developer.apple.com/documentation/avfoundation/avmusictrackloopcount)Added [AVMusicTrackLoopCountForever](https://developer.apple.com/documentation/avfoundation/avmusictrackloopcount/avmusictrackloopcountforever)

#### AVAudioTime.h

Modified [-[AVAudioTime extrapolateTimeFromAnchor:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1387772-extrapolatetime)

|  | Declaration |
| --- | --- |
| From | ``` - (AVAudioTime *)extrapolateTimeFromAnchor:(AVAudioTime *)anchorTime ``` |
| To | ``` - (AVAudioTime * _Nonnull)extrapolateTimeFromAnchor:(AVAudioTime * _Nonnull)anchorTime ``` |

Modified [-[AVAudioTime initWithAudioTimeStamp:sampleRate:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1389146-initwithaudiotimestamp)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithAudioTimeStamp:(const AudioTimeStamp *)ts sampleRate:(double)sampleRate ``` |
| To | ``` - (instancetype _Nonnull)initWithAudioTimeStamp:(const AudioTimeStamp * _Nonnull)ts sampleRate:(double)sampleRate ``` |

Modified [-[AVAudioTime initWithHostTime:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1386954-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithHostTime:(uint64_t)hostTime ``` |
| To | ``` - (instancetype _Nonnull)initWithHostTime:(uint64_t)hostTime ``` |

Modified [-[AVAudioTime initWithHostTime:sampleTime:atRate:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1386568-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithHostTime:(uint64_t)hostTime sampleTime:(AVAudioFramePosition)sampleTime atRate:(double)sampleRate ``` |
| To | ``` - (instancetype _Nonnull)initWithHostTime:(uint64_t)hostTime sampleTime:(AVAudioFramePosition)sampleTime atRate:(double)sampleRate ``` |

Modified [-[AVAudioTime initWithSampleTime:atRate:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1387972-initwithsampletime)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSampleTime:(AVAudioFramePosition)sampleTime atRate:(double)sampleRate ``` |
| To | ``` - (instancetype _Nonnull)initWithSampleTime:(AVAudioFramePosition)sampleTime atRate:(double)sampleRate ``` |

Modified [+[AVAudioTime timeWithAudioTimeStamp:sampleRate:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1522153-timewithaudiotimestamp)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)timeWithAudioTimeStamp:(const AudioTimeStamp *)ts sampleRate:(double)sampleRate ``` |
| To | ``` + (instancetype _Nonnull)timeWithAudioTimeStamp:(const AudioTimeStamp * _Nonnull)ts sampleRate:(double)sampleRate ``` |

Modified [+[AVAudioTime timeWithHostTime:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1522148-timewithhosttime)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)timeWithHostTime:(uint64_t)hostTime ``` |
| To | ``` + (instancetype _Nonnull)timeWithHostTime:(uint64_t)hostTime ``` |

Modified [+[AVAudioTime timeWithHostTime:sampleTime:atRate:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1522150-timewithhosttime)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)timeWithHostTime:(uint64_t)hostTime sampleTime:(AVAudioFramePosition)sampleTime atRate:(double)sampleRate ``` |
| To | ``` + (instancetype _Nonnull)timeWithHostTime:(uint64_t)hostTime sampleTime:(AVAudioFramePosition)sampleTime atRate:(double)sampleRate ``` |

Modified [+[AVAudioTime timeWithSampleTime:atRate:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1522149-timewithsampletime)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)timeWithSampleTime:(AVAudioFramePosition)sampleTime atRate:(double)sampleRate ``` |
| To | ``` + (instancetype _Nonnull)timeWithSampleTime:(AVAudioFramePosition)sampleTime atRate:(double)sampleRate ``` |

#### AVAudioTypes.h

Added [AVAudioPacketCount](https://developer.apple.com/documentation/avfoundation/avaudiopacketcount)

#### AVAudioUnit.h

Added [AVAudioUnit.AUAudioUnit](https://developer.apple.com/documentation/avfoundation/avaudiounit/1388167-auaudiounit)Added [+[AVAudioUnit instantiateWithComponentDescription:options:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avaudiounit/1390583-instantiate)Modified [AVAudioUnit.audioUnit](https://developer.apple.com/documentation/avfoundation/avaudiounit/1386098-audiounit)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AudioUnit audioUnit ``` |
| To | ``` @property(nonatomic, readonly, nonnull) AudioUnit audioUnit ``` |

Modified [-[AVAudioUnit loadAudioUnitPresetAtURL:error:]](https://developer.apple.com/documentation/avfoundation/avaudiounit/1387527-loadpreset)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)loadAudioUnitPresetAtURL:(NSURL *)url error:(NSError **)error ``` |
| To | ``` - (BOOL)loadAudioUnitPresetAtURL:(NSURL * _Nonnull)url error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [AVAudioUnit.manufacturerName](https://developer.apple.com/documentation/avfoundation/avaudiounit/1388972-manufacturername)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *manufacturerName ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *manufacturerName ``` |

Modified [AVAudioUnit.name](https://developer.apple.com/documentation/avfoundation/avaudiounit/1390637-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *name ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *name ``` |

#### AVAudioUnitComponent.h

Added [AVAudioUnitComponent.icon](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1385647-icon)Modified [AVAudioUnitComponent.allTagNames](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387996-alltagnames)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *allTagNames ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *allTagNames ``` |

Modified [AVAudioUnitComponent.audioComponent](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1385910-audiocomponent)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AudioComponent audioComponent ``` |
| To | ``` @property(nonatomic, readonly, nonnull) AudioComponent audioComponent ``` |

Modified [AVAudioUnitComponent.availableArchitectures](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387088-availablearchitectures)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *availableArchitectures ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSNumber *> *availableArchitectures ``` |

Modified [AVAudioUnitComponent.componentURL](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1388088-componenturl)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(nonatomic, readonly) NSURL *componentURL ``` | -- |
| To | ``` @property(nonatomic, readonly, nullable) NSURL *componentURL ``` | OS X 10.11 |

Modified [AVAudioUnitComponent.configurationDictionary](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1390327-configurationdictionary)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDictionary *configurationDictionary ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSDictionary<NSString *,id> *configurationDictionary ``` |

Modified [AVAudioUnitComponent.hasMIDIInput](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1389600-hasmidiinput)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) BOOL hasMIDIInput ``` |
| To | ``` @property(nonatomic, readonly) BOOL hasMIDIInput ``` |

Modified [AVAudioUnitComponent.hasMIDIOutput](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387070-hasmidioutput)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) BOOL hasMIDIOutput ``` |
| To | ``` @property(nonatomic, readonly) BOOL hasMIDIOutput ``` |

Modified [AVAudioUnitComponent.iconURL](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1390618-iconurl)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSURL *iconURL ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSURL *iconURL ``` |

Modified [AVAudioUnitComponent.localizedTypeName](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1390541-localizedtypename)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *localizedTypeName ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *localizedTypeName ``` |

Modified [AVAudioUnitComponent.manufacturerName](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387472-manufacturername)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *manufacturerName ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *manufacturerName ``` |

Modified [AVAudioUnitComponent.name](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1385941-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *name ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *name ``` |

Modified [AVAudioUnitComponent.typeName](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1389988-typename)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *typeName ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *typeName ``` |

Modified [AVAudioUnitComponent.userTagNames](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1385609-usertagnames)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *userTagNames ``` |
| To | ``` @property(copy, nonnull) NSArray<NSString *> *userTagNames ``` |

Modified [AVAudioUnitComponent.versionString](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1388446-versionstring)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *versionString ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *versionString ``` |

Modified [-[AVAudioUnitComponentManager componentsMatchingDescription:]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1386367-components)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)componentsMatchingDescription:(AudioComponentDescription)desc ``` |
| To | ``` - (NSArray<AVAudioUnitComponent *> * _Nonnull)componentsMatchingDescription:(AudioComponentDescription)desc ``` |

Modified [-[AVAudioUnitComponentManager componentsMatchingPredicate:]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1386487-components)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)componentsMatchingPredicate:(NSPredicate *)predicate ``` |
| To | ``` - (NSArray<AVAudioUnitComponent *> * _Nonnull)componentsMatchingPredicate:(NSPredicate * _Nonnull)predicate ``` |

Modified [-[AVAudioUnitComponentManager componentsPassingTest:]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1390260-components)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)componentsPassingTest:(BOOL (^)(AVAudioUnitComponent *comp, BOOL *stop))testHandler ``` |
| To | ``` - (NSArray<AVAudioUnitComponent *> * _Nonnull)componentsPassingTest:(BOOL (^ _Nonnull)(AVAudioUnitComponent * _Nonnull comp, BOOL * _Nonnull stop))testHandler ``` |

Modified [+[AVAudioUnitComponentManager sharedAudioUnitComponentManager]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1390177-sharedaudiounitcomponentmanager)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)sharedAudioUnitComponentManager ``` |
| To | ``` + (instancetype _Nonnull)sharedAudioUnitComponentManager ``` |

Modified [AVAudioUnitComponentManager.standardLocalizedTagNames](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1388545-standardlocalizedtagnames)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *standardLocalizedTagNames ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *standardLocalizedTagNames ``` |

Modified [AVAudioUnitComponentManager.tagNames](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1390133-tagnames)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *tagNames ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *tagNames ``` |

#### AVAudioUnitEffect.h

Modified [-[AVAudioUnitEffect initWithAudioComponentDescription:]](https://developer.apple.com/documentation/avfoundation/avaudiouniteffect/1388397-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithAudioComponentDescription:(AudioComponentDescription)audioComponentDescription ``` |
| To | ``` - (instancetype _Nonnull)initWithAudioComponentDescription:(AudioComponentDescription)audioComponentDescription ``` |

#### AVAudioUnitEQ.h

Modified [AVAudioUnitEQ.bands](https://developer.apple.com/documentation/avfoundation/avaudiouniteq/1388840-bands)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *bands ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVAudioUnitEQFilterParameters *> *bands ``` |

Modified [-[AVAudioUnitEQ initWithNumberOfBands:]](https://developer.apple.com/documentation/avfoundation/avaudiouniteq/1390915-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithNumberOfBands:(NSUInteger)numberOfBands ``` |
| To | ``` - (instancetype _Nonnull)initWithNumberOfBands:(NSUInteger)numberOfBands ``` |

#### AVAudioUnitGenerator.h

Modified [-[AVAudioUnitGenerator initWithAudioComponentDescription:]](https://developer.apple.com/documentation/avfoundation/avaudiounitgenerator/1387964-initwithaudiocomponentdescriptio)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithAudioComponentDescription:(AudioComponentDescription)audioComponentDescription ``` |
| To | ``` - (instancetype _Nonnull)initWithAudioComponentDescription:(AudioComponentDescription)audioComponentDescription ``` |

#### AVAudioUnitMIDIInstrument.h

Added #def AVAudioUnitMIDIInstrument_MixingConformanceModified [AVAudioUnitMIDIInstrument](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument)

|  | Protocols |
| --- | --- |
| From | -- |
| To | AVAudioMixing |

Modified [-[AVAudioUnitMIDIInstrument initWithAudioComponentDescription:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1386929-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithAudioComponentDescription:(AudioComponentDescription)description ``` |
| To | ``` - (instancetype _Nonnull)initWithAudioComponentDescription:(AudioComponentDescription)description ``` |

Modified [-[AVAudioUnitMIDIInstrument sendMIDISysExEvent:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1387812-sendmidisysexevent)

|  | Declaration |
| --- | --- |
| From | ``` - (void)sendMIDISysExEvent:(NSData *)midiData ``` |
| To | ``` - (void)sendMIDISysExEvent:(NSData * _Nonnull)midiData ``` |

#### AVAudioUnitSampler.h

Modified [-[AVAudioUnitSampler loadAudioFilesAtURLs:error:]](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1388631-loadaudiofilesaturls)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)loadAudioFilesAtURLs:(NSArray *)audioFiles error:(NSError **)outError ``` |
| To | ``` - (BOOL)loadAudioFilesAtURLs:(NSArray<NSURL *> * _Nonnull)audioFiles error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [-[AVAudioUnitSampler loadInstrumentAtURL:error:]](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1389514-loadinstrumentaturl)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)loadInstrumentAtURL:(NSURL *)instrumentURL error:(NSError **)outError ``` |
| To | ``` - (BOOL)loadInstrumentAtURL:(NSURL * _Nonnull)instrumentURL error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [-[AVAudioUnitSampler loadSoundBankInstrumentAtURL:program:bankMSB:bankLSB:error:]](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1385687-loadsoundbankinstrumentaturl)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)loadSoundBankInstrumentAtURL:(NSURL *)bankURL program:(uint8_t)program bankMSB:(uint8_t)bankMSB bankLSB:(uint8_t)bankLSB error:(NSError **)outError ``` |
| To | ``` - (BOOL)loadSoundBankInstrumentAtURL:(NSURL * _Nonnull)bankURL program:(uint8_t)program bankMSB:(uint8_t)bankMSB bankLSB:(uint8_t)bankLSB error:(NSError * _Nullable * _Nullable)outError ``` |

#### AVAudioUnitTimeEffect.h

Modified [-[AVAudioUnitTimeEffect initWithAudioComponentDescription:]](https://developer.apple.com/documentation/avfoundation/avaudiounittimeeffect/1390254-initwithaudiocomponentdescriptio)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithAudioComponentDescription:(AudioComponentDescription)audioComponentDescription ``` |
| To | ``` - (instancetype _Nonnull)initWithAudioComponentDescription:(AudioComponentDescription)audioComponentDescription ``` |

#### AVBase.h

Added #def AV_GENERICAdded #def AV_GENERIC_CLASSAdded #def AV_INIT_UNAVAILABLEAdded #def AV_PARAMETERIZED_TYPE

#### AVCaptureDevice.h

Added [AVAuthorizationStatus](https://developer.apple.com/documentation/avfoundation/avauthorizationstatus)Added [AVCaptureAutoFocusRangeRestriction](https://developer.apple.com/documentation/avfoundation/avcaptureautofocusrangerestriction)Added [AVCaptureAutoFocusSystem](https://developer.apple.com/documentation/avfoundation/avcaptureautofocussystem)Added AVCaptureDevice(AVCaptureDeviceAuthorization)Added AVCaptureDevice(AVCaptureDeviceHighDynamicRangeSupport)Added AVCaptureDevice(AVCaptureDeviceVideoZoom)Added [AVCaptureVideoStabilizationMode](https://developer.apple.com/documentation/avfoundation/avcapturevideostabilizationmode)

#### AVCaptureInput.h

Modified [+[AVCaptureDeviceInput deviceInputWithDevice:error:]](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/1450880-deviceinputwithdevice)

|  | Declaration |
| --- | --- |
| From | ``` + (id)deviceInputWithDevice:(AVCaptureDevice *)device error:(NSError **)outError ``` |
| To | ``` + (instancetype)deviceInputWithDevice:(AVCaptureDevice *)device error:(NSError **)outError ``` |

Modified [-[AVCaptureDeviceInput initWithDevice:error:]](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/1387609-initwithdevice)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDevice:(AVCaptureDevice *)device error:(NSError **)outError ``` |
| To | ``` - (instancetype)initWithDevice:(AVCaptureDevice *)device error:(NSError **)outError ``` |

Modified [-[AVCaptureScreenInput initWithDisplayID:]](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/1386383-initwithdisplayid)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDisplayID:(CGDirectDisplayID)displayID ``` |
| To | ``` - (instancetype)initWithDisplayID:(CGDirectDisplayID)displayID ``` |

Modified [AVCaptureScreenInput.removesDuplicateFrames](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/1390547-removesduplicateframes)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

#### AVCaptureSession.h

Modified [+[AVCaptureConnection connectionWithInputPort:videoPreviewLayer:]](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1444495-connectionwithinputport)

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

Modified [-[AVMutableComposition addMutableTrackWithMediaType:preferredTrackID:]](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1387601-addmutabletrackwithmediatype)

|  | Declaration |
| --- | --- |
| From | ``` - (AVMutableCompositionTrack *)addMutableTrackWithMediaType:(NSString *)mediaType preferredTrackID:(CMPersistentTrackID)preferredTrackID ``` |
| To | ``` - (AVMutableCompositionTrack * _Nonnull)addMutableTrackWithMediaType:(NSString * _Nonnull)mediaType preferredTrackID:(CMPersistentTrackID)preferredTrackID ``` |

Modified [+[AVMutableComposition composition]](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1495098-composition)

|  | Declaration |
| --- | --- |
| From | ``` + (AVMutableComposition *)composition ``` |
| To | ``` + (instancetype _Nonnull)composition ``` |

Modified [-[AVMutableComposition insertTimeRange:ofAsset:atTime:error:]](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1385943-inserttimerange)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)insertTimeRange:(CMTimeRange)timeRange ofAsset:(AVAsset *)asset atTime:(CMTime)startTime error:(NSError **)outError ``` |
| To | ``` - (BOOL)insertTimeRange:(CMTimeRange)timeRange ofAsset:(AVAsset * _Nonnull)asset atTime:(CMTime)startTime error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [-[AVMutableComposition mutableTrackCompatibleWithTrack:]](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1386662-mutabletrack)

|  | Declaration |
| --- | --- |
| From | ``` - (AVMutableCompositionTrack *)mutableTrackCompatibleWithTrack:(AVAssetTrack *)track ``` |
| To | ``` - (AVMutableCompositionTrack * _Nullable)mutableTrackCompatibleWithTrack:(AVAssetTrack * _Nonnull)track ``` |

Modified [-[AVMutableComposition removeTrack:]](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/1386818-removetrack)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeTrack:(AVCompositionTrack *)track ``` |
| To | ``` - (void)removeTrack:(AVCompositionTrack * _Nonnull)track ``` |

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

Modified [AVMutableCompositionTrack.extendedLanguageTag](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/1388866-extendedlanguagetag)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *extendedLanguageTag ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *extendedLanguageTag ``` |

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

Modified [AVMutableCompositionTrack.languageCode](https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack/1387192-languagecode)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *languageCode ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *languageCode ``` |

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

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithTimeRange:(CMTimeRange)timeRange ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithTimeRange:(CMTimeRange)timeRange ``` | yes |

Modified [-[AVCompositionTrackSegment initWithURL:trackID:sourceTimeRange:targetTimeRange:]](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/1390282-initwithurl)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithURL:(NSURL *)URL trackID:(CMPersistentTrackID)trackID sourceTimeRange:(CMTimeRange)sourceTimeRange targetTimeRange:(CMTimeRange)targetTimeRange ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithURL:(NSURL * _Nonnull)URL trackID:(CMPersistentTrackID)trackID sourceTimeRange:(CMTimeRange)sourceTimeRange targetTimeRange:(CMTimeRange)targetTimeRange ``` | yes |

Modified [AVCompositionTrackSegment.sourceURL](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/1386814-sourceurl)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSURL *sourceURL ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSURL *sourceURL ``` |

#### AVError.h

Added [AVErrorAirPlayControllerRequiresInternet](https://developer.apple.com/documentation/avfoundation/averror/code/airplaycontrollerrequiresinternet)Added [AVErrorAirPlayReceiverRequiresInternet](https://developer.apple.com/documentation/avfoundation/averror/code/airplayreceiverrequiresinternet)Added [AVErrorVideoCompositorFailed](https://developer.apple.com/documentation/avfoundation/averror/code/videocompositorfailed)

#### AVMediaFormat.h

Added [AVFileType3GPP](https://developer.apple.com/documentation/avfoundation/avfiletype/1386854-mobile3gpp)Added [AVFileType3GPP2](https://developer.apple.com/documentation/avfoundation/avfiletype/1388141-mobile3gpp2)Added [AVFileTypeEnhancedAC3](https://developer.apple.com/documentation/avfoundation/avfiletype/1387645-eac3)Added [AVMediaCharacteristicDubbedTranslation](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/1387476-dubbedtranslation)Added [AVMediaCharacteristicLanguageTranslation](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/1388194-languagetranslation)Added [AVMediaCharacteristicVoiceOverTranslation](https://developer.apple.com/documentation/avfoundation/avmediacharacteristicvoiceovertranslation)Added [AVStreamingKeyDeliveryContentKeyType](https://developer.apple.com/documentation/avfoundation/avstreamingkeydeliverycontentkeytype)Added [AVStreamingKeyDeliveryPersistentContentKeyType](https://developer.apple.com/documentation/avfoundation/avstreamingkeydeliverypersistentcontentkeytype)

#### AVMediaSelection.h (Added)

Added [AVMediaSelection](https://developer.apple.com/documentation/avfoundation/avmediaselection)Added [AVMediaSelection.asset](https://developer.apple.com/documentation/avfoundation/avmediaselection/1390874-asset)Added [-[AVMediaSelection mediaSelectionCriteriaCanBeAppliedAutomaticallyToMediaSelectionGroup:]](https://developer.apple.com/documentation/avfoundation/avmediaselection/1386716-mediaselectioncriteriacanbeappli)Added [-[AVMediaSelection selectedMediaOptionInMediaSelectionGroup:]](https://developer.apple.com/documentation/avfoundation/avmediaselection/1389197-selectedmediaoption)Added [AVMutableMediaSelection](https://developer.apple.com/documentation/avfoundation/avmutablemediaselection)Added [-[AVMutableMediaSelection selectMediaOption:inMediaSelectionGroup:]](https://developer.apple.com/documentation/avfoundation/avmutablemediaselection/1386768-selectmediaoption)

#### AVMediaSelectionGroup.h

Modified [AVMediaSelectionGroup.defaultOption](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1388440-defaultoption)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVMediaSelectionOption *defaultOption ``` |
| To | ``` @property(nonatomic, readonly, nullable) AVMediaSelectionOption *defaultOption ``` |

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

Modified [-[AVMediaSelectionGroup mediaSelectionOptionWithPropertyList:]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1389968-mediaselectionoptionwithproperty)

|  | Declaration |
| --- | --- |
| From | ``` - (AVMediaSelectionOption *)mediaSelectionOptionWithPropertyList:(id)plist ``` |
| To | ``` - (AVMediaSelectionOption * _Nullable)mediaSelectionOptionWithPropertyList:(id _Nonnull)plist ``` |

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

Modified [-[AVMediaSelectionOption associatedMediaSelectionOptionInMediaSelectionGroup:]](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1388232-associatedmediaselectionoptionin)

|  | Declaration |
| --- | --- |
| From | ``` - (AVMediaSelectionOption *)associatedMediaSelectionOptionInMediaSelectionGroup:(AVMediaSelectionGroup *)mediaSelectionGroup ``` |
| To | ``` - (AVMediaSelectionOption * _Nullable)associatedMediaSelectionOptionInMediaSelectionGroup:(AVMediaSelectionGroup * _Nonnull)mediaSelectionGroup ``` |

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

Modified [AVMediaSelectionOption.displayName](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1388485-displayname)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *displayName ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *displayName ``` |

Modified [-[AVMediaSelectionOption displayNameWithLocale:]](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1388021-displaynamewithlocale)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)displayNameWithLocale:(NSLocale *)locale ``` |
| To | ``` - (NSString * _Nonnull)displayNameWithLocale:(NSLocale * _Nonnull)locale ``` |

Modified [AVMediaSelectionOption.extendedLanguageTag](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1387619-extendedlanguagetag)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *extendedLanguageTag ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSString *extendedLanguageTag ``` |

Modified [-[AVMediaSelectionOption hasMediaCharacteristic:]](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1388531-hasmediacharacteristic)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)hasMediaCharacteristic:(NSString *)mediaCharacteristic ``` |
| To | ``` - (BOOL)hasMediaCharacteristic:(NSString * _Nonnull)mediaCharacteristic ``` |

Modified [AVMediaSelectionOption.locale](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1388436-locale)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSLocale *locale ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSLocale *locale ``` |

Modified [AVMediaSelectionOption.mediaSubTypes](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1385587-mediasubtypes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *mediaSubTypes ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSNumber *> *mediaSubTypes ``` |

Modified [AVMediaSelectionOption.mediaType](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1386322-mediatype)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *mediaType ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *mediaType ``` |

Modified [-[AVMediaSelectionOption metadataForFormat:]](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1386666-metadataforformat)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)metadataForFormat:(NSString *)format ``` |
| To | ``` - (NSArray<AVMetadataItem *> * _Nonnull)metadataForFormat:(NSString * _Nonnull)format ``` |

Modified [-[AVMediaSelectionOption propertyList]](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1386310-propertylist)

|  | Declaration |
| --- | --- |
| From | ``` - (id)propertyList ``` |
| To | ``` - (id _Nonnull)propertyList ``` |

#### AVMetadataFormat.h

Added [AVMetadataExtraAttributeInfoKey](https://developer.apple.com/documentation/avfoundation/avmetadataextraattributekey/1388595-info)Added [AVMetadataID3MetadataKeyCommercial](https://developer.apple.com/documentation/avfoundation/avmetadataid3metadatakeycommercial)Added [AVMetadataQuickTimeMetadataKeyContentIdentifier](https://developer.apple.com/documentation/avfoundation/avmetadataquicktimemetadatakeycontentidentifier)Modified [AVMetadataID3MetadataKeyCommerical](https://developer.apple.com/documentation/avfoundation/avmetadataid3metadatakeycommerical)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

#### AVMetadataIdentifiers.h

Added [AVMetadataIdentifierID3MetadataCommercial](https://developer.apple.com/documentation/avfoundation/avmetadataidentifier/1389685-id3metadatacommercial)Added [AVMetadataIdentifierQuickTimeMetadataContentIdentifier](https://developer.apple.com/documentation/avfoundation/avmetadataidentifierquicktimemetadatacontentidentifier)Added [AVMetadataIdentifierQuickTimeMetadataDetectedFace](https://developer.apple.com/documentation/avfoundation/avmetadataidentifierquicktimemetadatadetectedface)Added [AVMetadataIdentifierQuickTimeMetadataVideoOrientation](https://developer.apple.com/documentation/avfoundation/avmetadataidentifierquicktimemetadatavideoorientation)Modified [AVMetadataIdentifierID3MetadataCommerical](https://developer.apple.com/documentation/avfoundation/avmetadataidentifier/1388551-id3metadatacommerical)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

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

Modified [+[AVMetadataItem identifierForKey:keySpace:]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387869-identifierforkey)

|  | Declaration |
| --- | --- |
| From | ``` + (NSString *)identifierForKey:(id)key keySpace:(NSString *)keySpace ``` |
| To | ``` + (NSString * _Nullable)identifierForKey:(id _Nonnull)key keySpace:(NSString * _Nonnull)keySpace ``` |

Modified [AVMetadataItem.key](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1387843-key)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) id<NSObject, NSCopying> key ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) id<NSObject, NSCopying> key ``` |

Modified [+[AVMetadataItem keyForIdentifier:]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1385613-key)

|  | Declaration |
| --- | --- |
| From | ``` + (id)keyForIdentifier:(NSString *)identifier ``` |
| To | ``` + (id _Nullable)keyForIdentifier:(NSString * _Nonnull)identifier ``` |

Modified [AVMetadataItem.keySpace](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1385757-keyspace)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *keySpace ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *keySpace ``` |

Modified [+[AVMetadataItem keySpaceForIdentifier:]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1390663-keyspace)

|  | Declaration |
| --- | --- |
| From | ``` + (NSString *)keySpaceForIdentifier:(NSString *)identifier ``` |
| To | ``` + (NSString * _Nullable)keySpaceForIdentifier:(NSString * _Nonnull)identifier ``` |

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

Modified [-[AVMetadataItem statusOfValueForKey:error:]](https://developer.apple.com/documentation/avfoundation/avmetadataitem/1388523-statusofvalueforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (AVKeyValueStatus)statusOfValueForKey:(NSString *)key error:(NSError **)outError ``` |
| To | ``` - (AVKeyValueStatus)statusOfValueForKey:(NSString * _Nonnull)key error:(NSError * _Nullable * _Nullable)outError ``` |

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

Modified [+[AVMetadataItemFilter metadataItemFilterForSharing]](https://developer.apple.com/documentation/avfoundation/avmetadataitemfilter/1387905-forsharing)

|  | Declaration |
| --- | --- |
| From | ``` + (AVMetadataItemFilter *)metadataItemFilterForSharing ``` |
| To | ``` + (AVMetadataItemFilter * _Nonnull)metadataItemFilterForSharing ``` |

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

Modified [+[AVMutableMetadataItem metadataItem]](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/1426379-metadataitem)

|  | Declaration |
| --- | --- |
| From | ``` + (AVMutableMetadataItem *)metadataItem ``` |
| To | ``` + (AVMutableMetadataItem * _Nonnull)metadataItem ``` |

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

#### AVMIDIPlayer.h

Modified [-[AVMIDIPlayer initWithContentsOfURL:soundBankURL:error:]](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1390856-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithContentsOfURL:(NSURL *)inURL soundBankURL:(NSURL *)bankURL error:(NSError **)outError ``` |
| To | ``` - (instancetype _Nullable)initWithContentsOfURL:(NSURL * _Nonnull)inURL soundBankURL:(NSURL * _Nullable)bankURL error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [-[AVMIDIPlayer initWithData:soundBankURL:error:]](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1389225-initwithdata)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithData:(NSData *)data soundBankURL:(NSURL *)bankURL error:(NSError **)outError ``` |
| To | ``` - (instancetype _Nullable)initWithData:(NSData * _Nonnull)data soundBankURL:(NSURL * _Nullable)bankURL error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [-[AVMIDIPlayer play:]](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1388390-play)

|  | Declaration |
| --- | --- |
| From | ``` - (void)play:(AVMIDIPlayerCompletionHandler)completionHandler ``` |
| To | ``` - (void)play:(AVMIDIPlayerCompletionHandler _Nullable)completionHandler ``` |

#### AVMovie.h

Added [-[AVFragmentedMovie tracksWithMediaCharacteristic:]](https://developer.apple.com/documentation/avfoundation/avfragmentedmovie/1388651-trackswithmediacharacteristic)Added [-[AVFragmentedMovie tracksWithMediaType:]](https://developer.apple.com/documentation/avfoundation/avfragmentedmovie/1390553-trackswithmediatype)Added [-[AVFragmentedMovie trackWithTrackID:]](https://developer.apple.com/documentation/avfoundation/avfragmentedmovie/1388343-track)Added [AVMediaDataStorage](https://developer.apple.com/documentation/avfoundation/avmediadatastorage)Added [-[AVMediaDataStorage initWithURL:options:]](https://developer.apple.com/documentation/avfoundation/avmediadatastorage/1386008-initwithurl)Added [-[AVMediaDataStorage URL]](https://developer.apple.com/documentation/avfoundation/avmediadatastorage/1385809-url)Added [AVMovie.containsMovieFragments](https://developer.apple.com/documentation/avfoundation/avmovie/1388597-containsmoviefragments)Added [AVMovie.data](https://developer.apple.com/documentation/avfoundation/avmovie/1388017-data)Added [AVMovie.defaultMediaDataStorage](https://developer.apple.com/documentation/avfoundation/avmovie/1388424-defaultmediadatastorage)Added [-[AVMovie initWithData:options:]](https://developer.apple.com/documentation/avfoundation/avmovie/1388090-initwithdata)Added [-[AVMovie isCompatibleWithFileType:]](https://developer.apple.com/documentation/avfoundation/avmovie/1385982-iscompatiblewithfiletype)Added [-[AVMovie movieHeaderWithFileType:error:]](https://developer.apple.com/documentation/avfoundation/avmovie/1386686-movieheaderwithfiletype)Added [+[AVMovie movieWithData:options:]](https://developer.apple.com/documentation/avfoundation/avmovie/1458261-moviewithdata)Added [-[AVMovie tracksWithMediaCharacteristic:]](https://developer.apple.com/documentation/avfoundation/avmovie/1386839-trackswithmediacharacteristic)Added [-[AVMovie tracksWithMediaType:]](https://developer.apple.com/documentation/avfoundation/avmovie/1388667-trackswithmediatype)Added [-[AVMovie trackWithTrackID:]](https://developer.apple.com/documentation/avfoundation/avmovie/1386722-track)Added [-[AVMovie writeMovieHeaderToURL:fileType:options:error:]](https://developer.apple.com/documentation/avfoundation/avmovie/1386682-writemovieheadertourl)Added [AVMutableMovie](https://developer.apple.com/documentation/avfoundation/avmutablemovie)Added [-[AVMutableMovie addMutableTracksCopyingSettingsFromTracks:options:]](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1389215-addmutabletrackscopyingsettingsf)Added [-[AVMutableMovie addMutableTrackWithMediaType:copySettingsFromTrack:options:]](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1390063-addmutabletrackwithmediatype)Added [AVMutableMovie.defaultMediaDataStorage](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1389320-defaultmediadatastorage)Added [-[AVMutableMovie initWithData:options:error:]](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1388442-init)Added [-[AVMutableMovie initWithSettingsFromMovie:options:error:]](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1386408-initwithsettingsfrommovie)Added [-[AVMutableMovie initWithURL:options:error:]](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1386052-init)Added [-[AVMutableMovie insertEmptyTimeRange:]](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1387515-insertemptytimerange)Added [-[AVMutableMovie insertTimeRange:ofAsset:atTime:copySampleData:error:]](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1389598-inserttimerange)Added [AVMutableMovie.interleavingPeriod](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1386969-interleavingperiod)Added [AVMutableMovie.metadata](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1388742-metadata)Added [AVMutableMovie.modified](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1389960-ismodified)Added [+[AVMutableMovie movieWithData:options:error:]](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1458234-moviewithdata)Added [+[AVMutableMovie movieWithSettingsFromMovie:options:error:]](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1458238-moviewithsettingsfrommovie)Added [+[AVMutableMovie movieWithURL:options:error:]](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1458226-moviewithurl)Added [-[AVMutableMovie mutableTrackCompatibleWithTrack:]](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1388669-mutabletrack)Added [AVMutableMovie.preferredRate](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1387335-preferredrate)Added [AVMutableMovie.preferredTransform](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1388771-preferredtransform)Added [AVMutableMovie.preferredVolume](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1388614-preferredvolume)Added [-[AVMutableMovie removeTimeRange:]](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1385605-removetimerange)Added [-[AVMutableMovie removeTrack:]](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1386735-removetrack)Added [-[AVMutableMovie scaleTimeRange:toDuration:]](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1385653-scaletimerange)Added [AVMutableMovie.timescale](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1390622-timescale)Added [AVMutableMovie.tracks](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1387739-tracks)Added [-[AVMutableMovie tracksWithMediaCharacteristic:]](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1388547-trackswithmediacharacteristic)Added [-[AVMutableMovie tracksWithMediaType:]](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1390443-tracks)Added [-[AVMutableMovie trackWithTrackID:]](https://developer.apple.com/documentation/avfoundation/avmutablemovie/1389467-track)Added AVFragmentedMovie(AVFragmentedMovieTrackInspection)Added [AVFragmentedMovieContainsMovieFragmentsDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1390819-avfragmentedmoviecontainsmoviefr)Added AVMovie(AVMovieMovieHeaderSupport)Added AVMovie(AVMovieTrackInspection)Added [AVMovieWritingAddMovieHeaderToDestination](https://developer.apple.com/documentation/avfoundation/avmoviewritingoptions/avmoviewritingaddmovieheadertodestination)Added [AVMovieWritingOptions](https://developer.apple.com/documentation/avfoundation/avmoviewritingoptions)Added [AVMovieWritingTruncateDestinationToMovieHeaderOnly](https://developer.apple.com/documentation/avfoundation/avmoviewritingoptions/avmoviewritingtruncatedestinationtomovieheaderonly)Added AVMutableMovie(AVMutableMovieMetadataEditing)Added AVMutableMovie(AVMutableMovieMovieLevelEditing)Added AVMutableMovie(AVMutableMovieTrackInspection)Added AVMutableMovie(AVMutableMovieTrackLevelEditing)Modified [AVFragmentedMovie](https://developer.apple.com/documentation/avfoundation/avfragmentedmovie)

|  | Protocols |
| --- | --- |
| From | -- |
| To | AVFragmentMinding |

Modified [AVFragmentedMovie.tracks](https://developer.apple.com/documentation/avfoundation/avfragmentedmovie/1388242-tracks)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *tracks ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVFragmentedMovieTrack *> *tracks ``` |

Modified [AVFragmentedMovieMinder](https://developer.apple.com/documentation/avfoundation/avfragmentedmovieminder)

|  | Superclasses |
| --- | --- |
| From | NSObject |
| To | AVFragmentedAssetMinder |

Modified [-[AVFragmentedMovieMinder addFragmentedMovie:]](https://developer.apple.com/documentation/avfoundation/avfragmentedmovieminder/1386171-addfragmentedmovie)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addFragmentedMovie:(AVFragmentedMovie *)movie ``` |
| To | ``` - (void)addFragmentedMovie:(AVFragmentedMovie * _Nonnull)movie ``` |

Modified [+[AVFragmentedMovieMinder fragmentedMovieMinderWithMovie:mindingInterval:]](https://developer.apple.com/documentation/avfoundation/avfragmentedmovieminder/1458262-fragmentedmovieminderwithmovie)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)fragmentedMovieMinderWithMovie:(AVFragmentedMovie *)movie mindingInterval:(NSTimeInterval)mindingInterval ``` |
| To | ``` + (instancetype _Nonnull)fragmentedMovieMinderWithMovie:(AVFragmentedMovie * _Nonnull)movie mindingInterval:(NSTimeInterval)mindingInterval ``` |

Modified [-[AVFragmentedMovieMinder initWithMovie:mindingInterval:]](https://developer.apple.com/documentation/avfoundation/avfragmentedmovieminder/1390294-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithMovie:(AVFragmentedMovie *)movie mindingInterval:(NSTimeInterval)mindingInterval ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithMovie:(AVFragmentedMovie * _Nonnull)movie mindingInterval:(NSTimeInterval)mindingInterval ``` | yes |

Modified [AVFragmentedMovieMinder.movies](https://developer.apple.com/documentation/avfoundation/avfragmentedmovieminder/1388707-movies)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *movies ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVFragmentedMovie *> *movies ``` |

Modified [-[AVFragmentedMovieMinder removeFragmentedMovie:]](https://developer.apple.com/documentation/avfoundation/avfragmentedmovieminder/1389794-removefragmentedmovie)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeFragmentedMovie:(AVFragmentedMovie *)movie ``` |
| To | ``` - (void)removeFragmentedMovie:(AVFragmentedMovie * _Nonnull)movie ``` |

Modified [AVMovie](https://developer.apple.com/documentation/avfoundation/avmovie)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSCopying, NSMutableCopying |

Modified [-[AVMovie initWithURL:options:]](https://developer.apple.com/documentation/avfoundation/avmovie/1387923-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithURL:(NSURL *)URL options:(NSDictionary *)options ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithURL:(NSURL * _Nonnull)URL options:(NSDictionary<NSString *,id> * _Nullable)options ``` | yes |

Modified [+[AVMovie movieTypes]](https://developer.apple.com/documentation/avfoundation/avmovie/1388690-movietypes)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)movieTypes ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)movieTypes ``` |

Modified [+[AVMovie movieWithURL:options:]](https://developer.apple.com/documentation/avfoundation/avmovie/1458223-moviewithurl)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)movieWithURL:(NSURL *)URL options:(NSDictionary *)options ``` |
| To | ``` + (instancetype _Nonnull)movieWithURL:(NSURL * _Nonnull)URL options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [AVMovie.tracks](https://developer.apple.com/documentation/avfoundation/avmovie/1386485-tracks)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *tracks ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVMovieTrack *> *tracks ``` |

Modified [AVMovie.URL](https://developer.apple.com/documentation/avfoundation/avmovie/1386990-url)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSURL *URL ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSURL *URL ``` |

#### AVMovieTrack.h

Added [AVMovieTrack.alternateGroupID](https://developer.apple.com/documentation/avfoundation/avmovietrack/1387020-alternategroupid)Added [AVMovieTrack.mediaDataStorage](https://developer.apple.com/documentation/avfoundation/avmovietrack/1386868-mediadatastorage)Added [AVMovieTrack.mediaDecodeTimeRange](https://developer.apple.com/documentation/avfoundation/avmovietrack/1388187-mediadecodetimerange)Added [AVMovieTrack.mediaPresentationTimeRange](https://developer.apple.com/documentation/avfoundation/avmovietrack/1389982-mediapresentationtimerange)Added [AVMutableMovieTrack](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack)Added [-[AVMutableMovieTrack addTrackAssociationToTrack:type:]](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1390163-addtrackassociation)Added [AVMutableMovieTrack.alternateGroupID](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1387206-alternategroupid)Added [AVMutableMovieTrack.cleanApertureDimensions](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1386454-cleanaperturedimensions)Added [AVMutableMovieTrack.enabled](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1386340-enabled)Added [AVMutableMovieTrack.encodedPixelsDimensions](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1389417-encodedpixelsdimensions)Added [AVMutableMovieTrack.extendedLanguageTag](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1389056-extendedlanguagetag)Added [AVMutableMovieTrack.hasProtectedContent](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1389542-hasprotectedcontent)Added [-[AVMutableMovieTrack insertEmptyTimeRange:]](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1389441-insertemptytimerange)Added [-[AVMutableMovieTrack insertTimeRange:ofTrack:atTime:copySampleData:error:]](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1387665-inserttimerange)Added [AVMutableMovieTrack.languageCode](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1389736-languagecode)Added [AVMutableMovieTrack.layer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1387655-layer)Added [AVMutableMovieTrack.mediaDataStorage](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1386532-mediadatastorage)Added [AVMutableMovieTrack.metadata](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1390023-metadata)Added [AVMutableMovieTrack.modified](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1390201-modified)Added [AVMutableMovieTrack.naturalSize](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1385900-naturalsize)Added [AVMutableMovieTrack.preferredMediaChunkAlignment](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1390504-preferredmediachunkalignment)Added [AVMutableMovieTrack.preferredMediaChunkDuration](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1390292-preferredmediachunkduration)Added [AVMutableMovieTrack.preferredMediaChunkSize](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1390149-preferredmediachunksize)Added [AVMutableMovieTrack.preferredTransform](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1386593-preferredtransform)Added [AVMutableMovieTrack.preferredVolume](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1390391-preferredvolume)Added [AVMutableMovieTrack.productionApertureDimensions](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1390108-productionaperturedimensions)Added [-[AVMutableMovieTrack removeTimeRange:]](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1385962-removetimerange)Added [-[AVMutableMovieTrack removeTrackAssociationToTrack:type:]](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1389620-removetrackassociationtotrack)Added [AVMutableMovieTrack.sampleReferenceBaseURL](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1385583-samplereferencebaseurl)Added [-[AVMutableMovieTrack scaleTimeRange:toDuration:]](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1388618-scaletimerange)Added [AVMutableMovieTrack.timescale](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/1388055-timescale)Added AVMovieTrack(AVMovieTrackMediaDataStorage)Added AVMutableMovieTrack(AVMutableMovieTrack_ChunkProperties)Added AVMutableMovieTrack(AVMutableMovieTrack_LanguageProperties)Added AVMutableMovieTrack(AVMutableMovieTrack_PropertiesForAudibleCharacteristic)Added AVMutableMovieTrack(AVMutableMovieTrack_PropertiesForVisualCharacteristic)Added AVMutableMovieTrack(AVMutableMovieTrack_TrackLevelEditing)Added AVMutableMovieTrack(AVMutableMovieTrackMetadataEditing)Added AVMutableMovieTrack(AVMutableMovieTrackTrackAssociations)Modified [AVFragmentedMovieTrackTotalSampleDataLengthDidChangeNotification](https://developer.apple.com/documentation/avfoundation/avfragmentedmovietracktotalsampledatalengthdidchangenotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

#### AVOutputSettingsAssistant.h

Modified [AVOutputSettingsAssistant.audioSettings](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1386233-audiosettings)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDictionary *audioSettings ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSDictionary<NSString *,id> *audioSettings ``` |

Modified [+[AVOutputSettingsAssistant availableOutputSettingsPresets]](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1388118-availableoutputsettingspresets)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)availableOutputSettingsPresets ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)availableOutputSettingsPresets ``` |

Modified [AVOutputSettingsAssistant.outputFileType](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1390842-outputfiletype)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *outputFileType ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *outputFileType ``` |

Modified [+[AVOutputSettingsAssistant outputSettingsAssistantWithPreset:]](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1387909-outputsettingsassistantwithprese)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)outputSettingsAssistantWithPreset:(NSString *)presetIdentifier ``` |
| To | ``` + (instancetype _Nullable)outputSettingsAssistantWithPreset:(NSString * _Nonnull)presetIdentifier ``` |

Modified [AVOutputSettingsAssistant.sourceAudioFormat](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1390673-sourceaudioformat)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) CMAudioFormatDescriptionRef sourceAudioFormat ``` |
| To | ``` @property(nonatomic, retain, nullable) CMAudioFormatDescriptionRef sourceAudioFormat ``` |

Modified [AVOutputSettingsAssistant.sourceVideoFormat](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1387885-sourcevideoformat)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) CMVideoFormatDescriptionRef sourceVideoFormat ``` |
| To | ``` @property(nonatomic, retain, nullable) CMVideoFormatDescriptionRef sourceVideoFormat ``` |

Modified [AVOutputSettingsAssistant.videoSettings](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/1386880-videosettings)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDictionary *videoSettings ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSDictionary<NSString *,id> *videoSettings ``` |

#### AVPlayer.h

Added [AVPlayer.allowsExternalPlayback](https://developer.apple.com/documentation/avfoundation/avplayer/1387441-allowsexternalplayback)Added [AVPlayer.externalPlaybackActive](https://developer.apple.com/documentation/avfoundation/avplayer/1388982-externalplaybackactive)Added AVPlayer(AVPlayerExternalPlaybackSupport)Modified [-[AVPlayer addBoundaryTimeObserverForTimes:queue:usingBlock:]](https://developer.apple.com/documentation/avfoundation/avplayer/1388027-addboundarytimeobserver)

|  | Declaration |
| --- | --- |
| From | ``` - (id)addBoundaryTimeObserverForTimes:(NSArray *)times queue:(dispatch_queue_t)queue usingBlock:(void (^)(void))block ``` |
| To | ``` - (id _Nonnull)addBoundaryTimeObserverForTimes:(NSArray<NSValue *> * _Nonnull)times queue:(dispatch_queue_t _Nullable)queue usingBlock:(void (^ _Nonnull)(void))block ``` |

Modified [-[AVPlayer addPeriodicTimeObserverForInterval:queue:usingBlock:]](https://developer.apple.com/documentation/avfoundation/avplayer/1385829-addperiodictimeobserver)

|  | Declaration |
| --- | --- |
| From | ``` - (id)addPeriodicTimeObserverForInterval:(CMTime)interval queue:(dispatch_queue_t)queue usingBlock:(void (^)(CMTime time))block ``` |
| To | ``` - (id _Nonnull)addPeriodicTimeObserverForInterval:(CMTime)interval queue:(dispatch_queue_t _Nullable)queue usingBlock:(void (^ _Nonnull)(CMTime time))block ``` |

Modified [AVPlayer.audioOutputDeviceUniqueID](https://developer.apple.com/documentation/avfoundation/avplayer/1390717-audiooutputdeviceuniqueid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *audioOutputDeviceUniqueID ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *audioOutputDeviceUniqueID ``` |

Modified [AVPlayer.currentItem](https://developer.apple.com/documentation/avfoundation/avplayer/1387569-currentitem)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVPlayerItem *currentItem ``` |
| To | ``` @property(nonatomic, readonly, nullable) AVPlayerItem *currentItem ``` |

Modified [AVPlayer.error](https://developer.apple.com/documentation/avfoundation/avplayer/1387764-error)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSError *error ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSError *error ``` |

Modified [-[AVPlayer initWithPlayerItem:]](https://developer.apple.com/documentation/avfoundation/avplayer/1387104-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithPlayerItem:(AVPlayerItem *)item ``` |
| To | ``` - (instancetype _Nonnull)initWithPlayerItem:(AVPlayerItem * _Nonnull)item ``` |

Modified [-[AVPlayer initWithURL:]](https://developer.apple.com/documentation/avfoundation/avplayer/1385706-initwithurl)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithURL:(NSURL *)URL ``` |
| To | ``` - (instancetype _Nonnull)initWithURL:(NSURL * _Nonnull)URL ``` |

Modified [AVPlayer.masterClock](https://developer.apple.com/documentation/avfoundation/avplayer/1387066-masterclock)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) CMClockRef masterClock ``` |
| To | ``` @property(nonatomic, retain, nullable) CMClockRef masterClock ``` |

Modified [-[AVPlayer mediaSelectionCriteriaForMediaCharacteristic:]](https://developer.apple.com/documentation/avfoundation/avplayer/1387825-mediaselectioncriteriaformediach)

|  | Declaration |
| --- | --- |
| From | ``` - (AVPlayerMediaSelectionCriteria *)mediaSelectionCriteriaForMediaCharacteristic:(NSString *)mediaCharacteristic ``` |
| To | ``` - (AVPlayerMediaSelectionCriteria * _Nullable)mediaSelectionCriteriaForMediaCharacteristic:(NSString * _Nonnull)mediaCharacteristic ``` |

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

Modified [-[AVPlayer prerollAtRate:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avplayer/1389712-preroll)

|  | Declaration |
| --- | --- |
| From | ``` - (void)prerollAtRate:(float)rate completionHandler:(void (^)(BOOL finished))completionHandler ``` |
| To | ``` - (void)prerollAtRate:(float)rate completionHandler:(void (^ _Nullable)(BOOL finished))completionHandler ``` |

Modified [-[AVPlayer removeTimeObserver:]](https://developer.apple.com/documentation/avfoundation/avplayer/1387552-removetimeobserver)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeTimeObserver:(id)observer ``` |
| To | ``` - (void)removeTimeObserver:(id _Nonnull)observer ``` |

Modified [-[AVPlayer replaceCurrentItemWithPlayerItem:]](https://developer.apple.com/documentation/avfoundation/avplayer/1390806-replacecurrentitem)

|  | Declaration |
| --- | --- |
| From | ``` - (void)replaceCurrentItemWithPlayerItem:(AVPlayerItem *)item ``` |
| To | ``` - (void)replaceCurrentItemWithPlayerItem:(AVPlayerItem * _Nullable)item ``` |

Modified [-[AVPlayer seekToDate:]](https://developer.apple.com/documentation/avfoundation/avplayer/1386114-seektodate)

|  | Declaration |
| --- | --- |
| From | ``` - (void)seekToDate:(NSDate *)date ``` |
| To | ``` - (void)seekToDate:(NSDate * _Nonnull)date ``` |

Modified [-[AVPlayer seekToDate:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avplayer/1386108-seek)

|  | Declaration |
| --- | --- |
| From | ``` - (void)seekToDate:(NSDate *)date completionHandler:(void (^)(BOOL finished))completionHandler ``` |
| To | ``` - (void)seekToDate:(NSDate * _Nonnull)date completionHandler:(void (^ _Nonnull)(BOOL finished))completionHandler ``` |

Modified [-[AVPlayer seekToTime:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avplayer/1387018-seektotime)

|  | Declaration |
| --- | --- |
| From | ``` - (void)seekToTime:(CMTime)time completionHandler:(void (^)(BOOL finished))completionHandler ``` |
| To | ``` - (void)seekToTime:(CMTime)time completionHandler:(void (^ _Nonnull)(BOOL finished))completionHandler ``` |

Modified [-[AVPlayer seekToTime:toleranceBefore:toleranceAfter:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avplayer/1388493-seek)

|  | Declaration |
| --- | --- |
| From | ``` - (void)seekToTime:(CMTime)time toleranceBefore:(CMTime)toleranceBefore toleranceAfter:(CMTime)toleranceAfter completionHandler:(void (^)(BOOL finished))completionHandler ``` |
| To | ``` - (void)seekToTime:(CMTime)time toleranceBefore:(CMTime)toleranceBefore toleranceAfter:(CMTime)toleranceAfter completionHandler:(void (^ _Nonnull)(BOOL finished))completionHandler ``` |

Modified [-[AVPlayer setMediaSelectionCriteria:forMediaCharacteristic:]](https://developer.apple.com/documentation/avfoundation/avplayer/1390563-setmediaselectioncriteria)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setMediaSelectionCriteria:(AVPlayerMediaSelectionCriteria *)criteria forMediaCharacteristic:(NSString *)mediaCharacteristic ``` |
| To | ``` - (void)setMediaSelectionCriteria:(AVPlayerMediaSelectionCriteria * _Nullable)criteria forMediaCharacteristic:(NSString * _Nonnull)mediaCharacteristic ``` |

Modified [-[AVQueuePlayer canInsertItem:afterItem:]](https://developer.apple.com/documentation/avfoundation/avqueueplayer/1387289-caninsertitem)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)canInsertItem:(AVPlayerItem *)item afterItem:(AVPlayerItem *)afterItem ``` |
| To | ``` - (BOOL)canInsertItem:(AVPlayerItem * _Nonnull)item afterItem:(AVPlayerItem * _Nullable)afterItem ``` |

Modified [-[AVQueuePlayer initWithItems:]](https://developer.apple.com/documentation/avfoundation/avqueueplayer/1389345-initwithitems)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithItems:(NSArray *)items ``` |
| To | ``` - (AVQueuePlayer * _Nonnull)initWithItems:(NSArray<AVPlayerItem *> * _Nonnull)items ``` |

Modified [-[AVQueuePlayer insertItem:afterItem:]](https://developer.apple.com/documentation/avfoundation/avqueueplayer/1388543-insertitem)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertItem:(AVPlayerItem *)item afterItem:(AVPlayerItem *)afterItem ``` |
| To | ``` - (void)insertItem:(AVPlayerItem * _Nonnull)item afterItem:(AVPlayerItem * _Nullable)afterItem ``` |

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

Modified [-[AVQueuePlayer removeItem:]](https://developer.apple.com/documentation/avfoundation/avqueueplayer/1387400-remove)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeItem:(AVPlayerItem *)item ``` |
| To | ``` - (void)removeItem:(AVPlayerItem * _Nonnull)item ``` |

#### AVPlayerItem.h

Added [AVPlayerItem.canUseNetworkResourcesForLiveStreamingWhilePaused](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388752-canusenetworkresourcesforlivestr)Added [AVPlayerItem.currentMediaSelection](https://developer.apple.com/documentation/avfoundation/avplayeritem/1386519-currentmediaselection)Modified [-[AVPlayerItem accessLog]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388499-accesslog)

|  | Declaration |
| --- | --- |
| From | ``` - (AVPlayerItemAccessLog *)accessLog ``` |
| To | ``` - (AVPlayerItemAccessLog * _Nullable)accessLog ``` |

Modified [-[AVPlayerItem addOutput:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389782-add)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addOutput:(AVPlayerItemOutput *)output ``` |
| To | ``` - (void)addOutput:(AVPlayerItemOutput * _Nonnull)output ``` |

Modified [AVPlayerItem.asset](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388177-asset)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVAsset *asset ``` |
| To | ``` @property(nonatomic, readonly, nonnull) AVAsset *asset ``` |

Modified [AVPlayerItem.audioMix](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388037-audiomix)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) AVAudioMix *audioMix ``` |
| To | ``` @property(nonatomic, copy, nullable) AVAudioMix *audioMix ``` |

Modified [AVPlayerItem.audioTimePitchAlgorithm](https://developer.apple.com/documentation/avfoundation/avplayeritem/1385855-audiotimepitchalgorithm)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *audioTimePitchAlgorithm ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSString *audioTimePitchAlgorithm ``` |

Modified [AVPlayerItem.automaticallyLoadedAssetKeys](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388633-automaticallyloadedassetkeys)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *automaticallyLoadedAssetKeys ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *automaticallyLoadedAssetKeys ``` |

Modified [-[AVPlayerItem currentDate]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1386188-currentdate)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDate *)currentDate ``` |
| To | ``` - (NSDate * _Nullable)currentDate ``` |

Modified [AVPlayerItem.customVideoCompositor](https://developer.apple.com/documentation/avfoundation/avplayeritem/1390669-customvideocompositor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id<AVVideoCompositing> customVideoCompositor ``` |
| To | ``` @property(nonatomic, readonly, nullable) id<AVVideoCompositing> customVideoCompositor ``` |

Modified [AVPlayerItem.error](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389185-error)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSError *error ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSError *error ``` |

Modified [-[AVPlayerItem errorLog]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387573-errorlog)

|  | Declaration |
| --- | --- |
| From | ``` - (AVPlayerItemErrorLog *)errorLog ``` |
| To | ``` - (AVPlayerItemErrorLog * _Nullable)errorLog ``` |

Modified [-[AVPlayerItem initWithAsset:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1390707-initwithasset)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithAsset:(AVAsset *)asset ``` |
| To | ``` - (instancetype _Nonnull)initWithAsset:(AVAsset * _Nonnull)asset ``` |

Modified [-[AVPlayerItem initWithAsset:automaticallyLoadedAssetKeys:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387529-initwithasset)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithAsset:(AVAsset *)asset automaticallyLoadedAssetKeys:(NSArray *)automaticallyLoadedAssetKeys ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithAsset:(AVAsset * _Nonnull)asset automaticallyLoadedAssetKeys:(NSArray<NSString *> * _Nullable)automaticallyLoadedAssetKeys ``` | yes |

Modified [-[AVPlayerItem initWithURL:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387558-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithURL:(NSURL *)URL ``` |
| To | ``` - (instancetype _Nonnull)initWithURL:(NSURL * _Nonnull)URL ``` |

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

Modified [+[AVPlayerItem playerItemWithAsset:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1588087-playeritemwithasset)

|  | Declaration |
| --- | --- |
| From | ``` + (AVPlayerItem *)playerItemWithAsset:(AVAsset *)asset ``` |
| To | ``` + (AVPlayerItem * _Nonnull)playerItemWithAsset:(AVAsset * _Nonnull)asset ``` |

Modified [+[AVPlayerItem playerItemWithAsset:automaticallyLoadedAssetKeys:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1588088-playeritemwithasset)

|  | Declaration |
| --- | --- |
| From | ``` + (AVPlayerItem *)playerItemWithAsset:(AVAsset *)asset automaticallyLoadedAssetKeys:(NSArray *)automaticallyLoadedAssetKeys ``` |
| To | ``` + (AVPlayerItem * _Nonnull)playerItemWithAsset:(AVAsset * _Nonnull)asset automaticallyLoadedAssetKeys:(NSArray<NSString *> * _Nullable)automaticallyLoadedAssetKeys ``` |

Modified [+[AVPlayerItem playerItemWithURL:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1588089-playeritemwithurl)

|  | Declaration |
| --- | --- |
| From | ``` + (AVPlayerItem *)playerItemWithURL:(NSURL *)URL ``` |
| To | ``` + (AVPlayerItem * _Nonnull)playerItemWithURL:(NSURL * _Nonnull)URL ``` |

Modified [-[AVPlayerItem removeOutput:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388756-removeoutput)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeOutput:(AVPlayerItemOutput *)output ``` |
| To | ``` - (void)removeOutput:(AVPlayerItemOutput * _Nonnull)output ``` |

Modified [AVPlayerItem.seekableTimeRanges](https://developer.apple.com/documentation/avfoundation/avplayeritem/1386155-seekabletimeranges)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *seekableTimeRanges ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSValue *> *seekableTimeRanges ``` |

Modified [-[AVPlayerItem seekToDate:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389067-seek)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)seekToDate:(NSDate *)date ``` |
| To | ``` - (BOOL)seekToDate:(NSDate * _Nonnull)date ``` |

Modified [-[AVPlayerItem seekToDate:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389877-seektodate)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)seekToDate:(NSDate *)date completionHandler:(void (^)(BOOL finished))completionHandler ``` |
| To | ``` - (BOOL)seekToDate:(NSDate * _Nonnull)date completionHandler:(void (^ _Nonnull)(BOOL finished))completionHandler ``` |

Modified [-[AVPlayerItem seekToTime:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387418-seektotime)

|  | Declaration |
| --- | --- |
| From | ``` - (void)seekToTime:(CMTime)time completionHandler:(void (^)(BOOL finished))completionHandler ``` |
| To | ``` - (void)seekToTime:(CMTime)time completionHandler:(void (^ _Nonnull)(BOOL finished))completionHandler ``` |

Modified [-[AVPlayerItem seekToTime:toleranceBefore:toleranceAfter:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387753-seek)

|  | Declaration |
| --- | --- |
| From | ``` - (void)seekToTime:(CMTime)time toleranceBefore:(CMTime)toleranceBefore toleranceAfter:(CMTime)toleranceAfter completionHandler:(void (^)(BOOL finished))completionHandler ``` |
| To | ``` - (void)seekToTime:(CMTime)time toleranceBefore:(CMTime)toleranceBefore toleranceAfter:(CMTime)toleranceAfter completionHandler:(void (^ _Nonnull)(BOOL finished))completionHandler ``` |

Modified [-[AVPlayerItem selectedMediaOptionInMediaSelectionGroup:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1386314-selectedmediaoptioninmediaselect)

|  | Declaration |
| --- | --- |
| From | ``` - (AVMediaSelectionOption *)selectedMediaOptionInMediaSelectionGroup:(AVMediaSelectionGroup *)mediaSelectionGroup ``` |
| To | ``` - (AVMediaSelectionOption * _Nullable)selectedMediaOptionInMediaSelectionGroup:(AVMediaSelectionGroup * _Nonnull)mediaSelectionGroup ``` |

Modified [-[AVPlayerItem selectMediaOption:inMediaSelectionGroup:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389610-selectmediaoption)

|  | Declaration |
| --- | --- |
| From | ``` - (void)selectMediaOption:(AVMediaSelectionOption *)mediaSelectionOption inMediaSelectionGroup:(AVMediaSelectionGroup *)mediaSelectionGroup ``` |
| To | ``` - (void)selectMediaOption:(AVMediaSelectionOption * _Nullable)mediaSelectionOption inMediaSelectionGroup:(AVMediaSelectionGroup * _Nonnull)mediaSelectionGroup ``` |

Modified [-[AVPlayerItem selectMediaOptionAutomaticallyInMediaSelectionGroup:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388268-selectmediaoptionautomaticallyin)

|  | Declaration |
| --- | --- |
| From | ``` - (void)selectMediaOptionAutomaticallyInMediaSelectionGroup:(AVMediaSelectionGroup *)mediaSelectionGroup ``` |
| To | ``` - (void)selectMediaOptionAutomaticallyInMediaSelectionGroup:(AVMediaSelectionGroup * _Nonnull)mediaSelectionGroup ``` |

Modified [AVPlayerItem.textStyleRules](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389681-textstylerules)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *textStyleRules ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<AVTextStyleRule *> *textStyleRules ``` |

Modified [AVPlayerItem.timebase](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387605-timebase)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) CMTimebaseRef timebase ``` |
| To | ``` @property(nonatomic, readonly, nullable) CMTimebaseRef timebase ``` |

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

Modified [AVPlayerItem.videoComposition](https://developer.apple.com/documentation/avfoundation/avplayeritem/1388818-videocomposition)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) AVVideoComposition *videoComposition ``` |
| To | ``` @property(nonatomic, copy, nullable) AVVideoComposition *videoComposition ``` |

Modified [AVPlayerItemAccessLog.events](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslog/1387406-events)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *events ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVPlayerItemAccessLogEvent *> *events ``` |

Modified [-[AVPlayerItemAccessLog extendedLogData]](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslog/1386892-extendedlogdata)

|  | Declaration |
| --- | --- |
| From | ``` - (NSData *)extendedLogData ``` |
| To | ``` - (NSData * _Nullable)extendedLogData ``` |

Modified [AVPlayerItemAccessLogEvent.playbackSessionID](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1388462-playbacksessionid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *playbackSessionID ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSString *playbackSessionID ``` |

Modified [AVPlayerItemAccessLogEvent.playbackStartDate](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1390502-playbackstartdate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDate *playbackStartDate ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSDate *playbackStartDate ``` |

Modified [AVPlayerItemAccessLogEvent.playbackType](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1387218-playbacktype)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *playbackType ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSString *playbackType ``` |

Modified [AVPlayerItemAccessLogEvent.serverAddress](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1390315-serveraddress)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *serverAddress ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSString *serverAddress ``` |

Modified [AVPlayerItemAccessLogEvent.URI](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1388643-uri)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *URI ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSString *URI ``` |

Modified [AVPlayerItemErrorLog.events](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlog/1387637-events)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *events ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<AVPlayerItemErrorLogEvent *> *events ``` |

Modified [-[AVPlayerItemErrorLog extendedLogData]](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlog/1389100-extendedlogdata)

|  | Declaration |
| --- | --- |
| From | ``` - (NSData *)extendedLogData ``` |
| To | ``` - (NSData * _Nullable)extendedLogData ``` |

Modified [AVPlayerItemErrorLogEvent.date](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/1388416-date)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDate *date ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSDate *date ``` |

Modified [AVPlayerItemErrorLogEvent.errorComment](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/1388011-errorcomment)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *errorComment ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSString *errorComment ``` |

Modified [AVPlayerItemErrorLogEvent.errorDomain](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/1388603-errordomain)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *errorDomain ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *errorDomain ``` |

Modified [AVPlayerItemErrorLogEvent.playbackSessionID](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/1385934-playbacksessionid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *playbackSessionID ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSString *playbackSessionID ``` |

Modified [AVPlayerItemErrorLogEvent.serverAddress](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/1385797-serveraddress)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *serverAddress ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSString *serverAddress ``` |

Modified [AVPlayerItemErrorLogEvent.URI](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/1389302-uri)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *URI ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSString *URI ``` |

#### AVPlayerItemOutput.h

Modified [AVPlayerItemLegibleOutput.delegate](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/1387877-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id<AVPlayerItemLegibleOutputPushDelegate> delegate ``` |
| To | ``` @property(nonatomic, readonly, weak, nullable) id<AVPlayerItemLegibleOutputPushDelegate> delegate ``` |

Modified [AVPlayerItemLegibleOutput.delegateQueue](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/1386275-delegatequeue)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) dispatch_queue_t delegateQueue ``` |
| To | ``` @property(nonatomic, readonly, nullable) dispatch_queue_t delegateQueue ``` |

Modified [-[AVPlayerItemLegibleOutput initWithMediaSubtypesForNativeRepresentation:]](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/1390500-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithMediaSubtypesForNativeRepresentation:(NSArray *)subtypes ``` |
| To | ``` - (instancetype _Nonnull)initWithMediaSubtypesForNativeRepresentation:(NSArray<NSNumber *> * _Nonnull)subtypes ``` |

Modified [-[AVPlayerItemLegibleOutput setDelegate:queue:]](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/1386204-setdelegate)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setDelegate:(id<AVPlayerItemLegibleOutputPushDelegate>)delegate queue:(dispatch_queue_t)delegateQueue ``` |
| To | ``` - (void)setDelegate:(id<AVPlayerItemLegibleOutputPushDelegate> _Nullable)delegate queue:(dispatch_queue_t _Nullable)delegateQueue ``` |

Modified [AVPlayerItemLegibleOutput.textStylingResolution](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/1385803-textstylingresolution)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *textStylingResolution ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSString *textStylingResolution ``` |

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

Modified [AVPlayerItemMetadataOutput.delegateQueue](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput/1387265-delegatequeue)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) dispatch_queue_t delegateQueue ``` |
| To | ``` @property(nonatomic, readonly, nullable) dispatch_queue_t delegateQueue ``` |

Modified [-[AVPlayerItemMetadataOutput initWithIdentifiers:]](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput/1390205-initwithidentifiers)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithIdentifiers:(NSArray *)identifiers ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithIdentifiers:(NSArray<NSString *> * _Nullable)identifiers ``` | yes |

Modified [-[AVPlayerItemMetadataOutput setDelegate:queue:]](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput/1385728-setdelegate)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setDelegate:(id<AVPlayerItemMetadataOutputPushDelegate>)delegate queue:(dispatch_queue_t)delegateQueue ``` |
| To | ``` - (void)setDelegate:(id<AVPlayerItemMetadataOutputPushDelegate> _Nullable)delegate queue:(dispatch_queue_t _Nullable)delegateQueue ``` |

Modified [-[AVPlayerItemMetadataOutputPushDelegate metadataOutput:didOutputTimedMetadataGroups:fromPlayerItemTrack:]](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutputpushdelegate/1388071-metadataoutput)

|  | Declaration |
| --- | --- |
| From | ``` - (void)metadataOutput:(AVPlayerItemMetadataOutput *)output didOutputTimedMetadataGroups:(NSArray *)groups fromPlayerItemTrack:(AVPlayerItemTrack *)track ``` |
| To | ``` - (void)metadataOutput:(AVPlayerItemMetadataOutput * _Nonnull)output didOutputTimedMetadataGroups:(NSArray<AVTimedMetadataGroup *> * _Nonnull)groups fromPlayerItemTrack:(AVPlayerItemTrack * _Nonnull)track ``` |

Modified [-[AVPlayerItemOutputPullDelegate outputMediaDataWillChange:]](https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpulldelegate/1387498-outputmediadatawillchange)

|  | Declaration |
| --- | --- |
| From | ``` - (void)outputMediaDataWillChange:(AVPlayerItemOutput *)sender ``` |
| To | ``` - (void)outputMediaDataWillChange:(AVPlayerItemOutput * _Nonnull)sender ``` |

Modified [-[AVPlayerItemOutputPullDelegate outputSequenceWasFlushed:]](https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpulldelegate/1387279-outputsequencewasflushed)

|  | Declaration |
| --- | --- |
| From | ``` - (void)outputSequenceWasFlushed:(AVPlayerItemOutput *)output ``` |
| To | ``` - (void)outputSequenceWasFlushed:(AVPlayerItemOutput * _Nonnull)output ``` |

Modified [-[AVPlayerItemOutputPushDelegate outputSequenceWasFlushed:]](https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpushdelegate/1390224-outputsequencewasflushed)

|  | Declaration |
| --- | --- |
| From | ``` - (void)outputSequenceWasFlushed:(AVPlayerItemOutput *)output ``` |
| To | ``` - (void)outputSequenceWasFlushed:(AVPlayerItemOutput * _Nonnull)output ``` |

Modified [-[AVPlayerItemVideoOutput copyPixelBufferForItemTime:itemTimeForDisplay:]](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1386148-copypixelbufferforitemtime)

|  | Declaration |
| --- | --- |
| From | ``` - (CVPixelBufferRef)copyPixelBufferForItemTime:(CMTime)itemTime itemTimeForDisplay:(CMTime *)outItemTimeForDisplay ``` |
| To | ``` - (CVPixelBufferRef _Nullable)copyPixelBufferForItemTime:(CMTime)itemTime itemTimeForDisplay:(CMTime * _Nullable)outItemTimeForDisplay ``` |

Modified [AVPlayerItemVideoOutput.delegate](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1385827-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id<AVPlayerItemOutputPullDelegate> delegate ``` |
| To | ``` @property(nonatomic, readonly, assign, nullable) id<AVPlayerItemOutputPullDelegate> delegate ``` |

Modified [AVPlayerItemVideoOutput.delegateQueue](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1388108-delegatequeue)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) dispatch_queue_t delegateQueue ``` |
| To | ``` @property(nonatomic, readonly, nullable) dispatch_queue_t delegateQueue ``` |

Modified [-[AVPlayerItemVideoOutput initWithPixelBufferAttributes:]](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1389231-initwithpixelbufferattributes)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithPixelBufferAttributes:(NSDictionary *)pixelBufferAttributes ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithPixelBufferAttributes:(NSDictionary<NSString *,id> * _Nullable)pixelBufferAttributes ``` | yes |

Modified [-[AVPlayerItemVideoOutput setDelegate:queue:]](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1386824-setdelegate)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setDelegate:(id<AVPlayerItemOutputPullDelegate>)delegate queue:(dispatch_queue_t)delegateQueue ``` |
| To | ``` - (void)setDelegate:(id<AVPlayerItemOutputPullDelegate> _Nullable)delegate queue:(dispatch_queue_t _Nullable)delegateQueue ``` |

#### AVPlayerItemProtectedContentAdditions.h

Modified [-[AVPlayerItem requestContentAuthorizationAsynchronouslyWithTimeoutInterval:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1390600-requestcontentauthorizationasync)

|  | Declaration |
| --- | --- |
| From | ``` - (void)requestContentAuthorizationAsynchronouslyWithTimeoutInterval:(NSTimeInterval)timeoutInterval completionHandler:(void (^)(void))handler ``` |
| To | ``` - (void)requestContentAuthorizationAsynchronouslyWithTimeoutInterval:(NSTimeInterval)timeoutInterval completionHandler:(void (^ _Nonnull)(void))handler ``` |

#### AVPlayerItemTrack.h

Modified [AVPlayerItemTrack.assetTrack](https://developer.apple.com/documentation/avfoundation/avplayeritemtrack/1390701-assettrack)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVAssetTrack *assetTrack ``` |
| To | ``` @property(nonatomic, readonly, nonnull) AVAssetTrack *assetTrack ``` |

Modified [AVPlayerItemTrack.videoFieldMode](https://developer.apple.com/documentation/avfoundation/avplayeritemtrack/1388045-videofieldmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *videoFieldMode ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *videoFieldMode ``` |

#### AVPlayerLayer.h

Added [AVPlayerLayer.pixelBufferAttributes](https://developer.apple.com/documentation/avfoundation/avplayerlayer/1390055-pixelbufferattributes)Modified [AVPlayerLayer.player](https://developer.apple.com/documentation/avfoundation/avplayerlayer/1390434-player)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) AVPlayer *player ``` |
| To | ``` @property(nonatomic, retain, nullable) AVPlayer *player ``` |

Modified [+[AVPlayerLayer playerLayerWithPlayer:]](https://developer.apple.com/documentation/avfoundation/avplayerlayer/1389308-init)

|  | Declaration |
| --- | --- |
| From | ``` + (AVPlayerLayer *)playerLayerWithPlayer:(AVPlayer *)player ``` |
| To | ``` + (AVPlayerLayer * _Nonnull)playerLayerWithPlayer:(AVPlayer * _Nullable)player ``` |

Modified [AVPlayerLayer.videoGravity](https://developer.apple.com/documentation/avfoundation/avplayerlayer/1388915-videogravity)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *videoGravity ``` |
| To | ``` @property(copy, nonnull) NSString *videoGravity ``` |

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

#### AVSampleBufferDisplayLayer.h

Modified [AVSampleBufferDisplayLayer.controlTimebase](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/1390569-controltimebase)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) CMTimebaseRef controlTimebase ``` |
| To | ``` @property(retain, nullable) CMTimebaseRef controlTimebase ``` |

Modified [-[AVSampleBufferDisplayLayer enqueueSampleBuffer:]](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/1387599-enqueue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enqueueSampleBuffer:(CMSampleBufferRef)sampleBuffer ``` |
| To | ``` - (void)enqueueSampleBuffer:(CMSampleBufferRef _Nonnull)sampleBuffer ``` |

Modified [AVSampleBufferDisplayLayer.error](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/1390739-error)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSError *error ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSError *error ``` |

Modified [-[AVSampleBufferDisplayLayer requestMediaDataWhenReadyOnQueue:usingBlock:]](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/1387778-requestmediadatawhenreadyonqueue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)requestMediaDataWhenReadyOnQueue:(dispatch_queue_t)queue usingBlock:(void (^)(void))block ``` |
| To | ``` - (void)requestMediaDataWhenReadyOnQueue:(dispatch_queue_t _Nonnull)queue usingBlock:(void (^ _Nonnull)(void))block ``` |

Modified [AVSampleBufferDisplayLayer.videoGravity](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/1387625-videogravity)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *videoGravity ``` |
| To | ``` @property(copy, nonnull) NSString *videoGravity ``` |

#### AVSampleBufferGenerator.h

Modified [-[AVSampleBufferGenerator createSampleBufferForRequest:]](https://developer.apple.com/documentation/avfoundation/avsamplebuffergenerator/1387475-createsamplebuffer)

|  | Declaration |
| --- | --- |
| From | ``` - (CMSampleBufferRef)createSampleBufferForRequest:(AVSampleBufferRequest *)request ``` |
| To | ``` - (CMSampleBufferRef _Nonnull)createSampleBufferForRequest:(AVSampleBufferRequest * _Nonnull)request ``` |

Modified [-[AVSampleBufferGenerator initWithAsset:timebase:]](https://developer.apple.com/documentation/avfoundation/avsamplebuffergenerator/1387477-initwithasset)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithAsset:(AVAsset *)asset timebase:(CMTimebaseRef)timebase ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithAsset:(AVAsset * _Nonnull)asset timebase:(CMTimebaseRef _Nullable)timebase ``` | yes |

Modified [+[AVSampleBufferGenerator notifyOfDataReadyForSampleBuffer:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avsamplebuffergenerator/1387295-notifyofdatareadyforsamplebuffer)

|  | Declaration |
| --- | --- |
| From | ``` + (void)notifyOfDataReadyForSampleBuffer:(CMSampleBufferRef)sbuf completionHandler:(void (^)(BOOL dataReady, NSError *error))completionHandler ``` |
| To | ``` + (void)notifyOfDataReadyForSampleBuffer:(CMSampleBufferRef _Nonnull)sbuf completionHandler:(void (^ _Nonnull)(BOOL dataReady, NSError * _Nonnull error))completionHandler ``` |

Modified [-[AVSampleBufferRequest initWithStartCursor:]](https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/1387449-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (instancetype)initWithStartCursor:(AVSampleCursor *)startCursor ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithStartCursor:(AVSampleCursor * _Nonnull)startCursor ``` | yes |

Modified [AVSampleBufferRequest.limitCursor](https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/1387466-limitcursor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) AVSampleCursor *limitCursor ``` |
| To | ``` @property(nonatomic, retain, nullable) AVSampleCursor *limitCursor ``` |

Modified [AVSampleBufferRequest.startCursor](https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/1387398-startcursor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain, readonly) AVSampleCursor *startCursor ``` |
| To | ``` @property(nonatomic, retain, readonly, nonnull) AVSampleCursor *startCursor ``` |

#### AVSampleCursor.h

Added [AVSampleCursor.samplesRequiredForDecoderRefresh](https://developer.apple.com/documentation/avfoundation/avsamplecursor/1386446-samplesrequiredfordecoderrefresh)Modified [-[AVSampleCursor comparePositionInDecodeOrderWithPositionOfCursor:]](https://developer.apple.com/documentation/avfoundation/avsamplecursor/1390608-comparepositionindecodeorder)

|  | Declaration |
| --- | --- |
| From | ``` - (NSComparisonResult)comparePositionInDecodeOrderWithPositionOfCursor:(AVSampleCursor *)cursor ``` |
| To | ``` - (NSComparisonResult)comparePositionInDecodeOrderWithPositionOfCursor:(AVSampleCursor * _Nonnull)cursor ``` |

Modified [-[AVSampleCursor copyCurrentSampleFormatDescription]](https://developer.apple.com/documentation/avfoundation/avsamplecursor/1390703-copycurrentsampleformatdescripti)

|  | Declaration |
| --- | --- |
| From | ``` - (CMFormatDescriptionRef)copyCurrentSampleFormatDescription ``` |
| To | ``` - (CMFormatDescriptionRef _Nonnull)copyCurrentSampleFormatDescription ``` |

Modified [AVSampleCursor.currentChunkStorageURL](https://developer.apple.com/documentation/avfoundation/avsamplecursor/1388328-currentchunkstorageurl)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSURL *currentChunkStorageURL ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSURL *currentChunkStorageURL ``` |

Modified [-[AVSampleCursor samplesWithEarlierDecodeTimeStampsMayHaveLaterPresentationTimeStampsThanCursor:]](https://developer.apple.com/documentation/avfoundation/avsamplecursor/1386558-maysampleswithearlierdecodetimes)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)samplesWithEarlierDecodeTimeStampsMayHaveLaterPresentationTimeStampsThanCursor:(AVSampleCursor *)cursor ``` |
| To | ``` - (BOOL)samplesWithEarlierDecodeTimeStampsMayHaveLaterPresentationTimeStampsThanCursor:(AVSampleCursor * _Nonnull)cursor ``` |

Modified [-[AVSampleCursor samplesWithLaterDecodeTimeStampsMayHaveEarlierPresentationTimeStampsThanCursor:]](https://developer.apple.com/documentation/avfoundation/avsamplecursor/1390029-maysampleswithlaterdecodetimesta)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)samplesWithLaterDecodeTimeStampsMayHaveEarlierPresentationTimeStampsThanCursor:(AVSampleCursor *)cursor ``` |
| To | ``` - (BOOL)samplesWithLaterDecodeTimeStampsMayHaveEarlierPresentationTimeStampsThanCursor:(AVSampleCursor * _Nonnull)cursor ``` |

Modified [-[AVSampleCursor stepByDecodeTime:wasPinned:]](https://developer.apple.com/documentation/avfoundation/avsamplecursor/1389152-stepbydecodetime)

|  | Declaration |
| --- | --- |
| From | ``` - (CMTime)stepByDecodeTime:(CMTime)deltaDecodeTime wasPinned:(BOOL *)outWasPinned ``` |
| To | ``` - (CMTime)stepByDecodeTime:(CMTime)deltaDecodeTime wasPinned:(BOOL * _Nullable)outWasPinned ``` |

Modified [-[AVSampleCursor stepByPresentationTime:wasPinned:]](https://developer.apple.com/documentation/avfoundation/avsamplecursor/1387680-stepbypresentationtime)

|  | Declaration |
| --- | --- |
| From | ``` - (CMTime)stepByPresentationTime:(CMTime)deltaPresentationTime wasPinned:(BOOL *)outWasPinned ``` |
| To | ``` - (CMTime)stepByPresentationTime:(CMTime)deltaPresentationTime wasPinned:(BOOL * _Nullable)outWasPinned ``` |

#### AVSynchronizedLayer.h

Modified [AVSynchronizedLayer.playerItem](https://developer.apple.com/documentation/avfoundation/avsynchronizedlayer/1385679-playeritem)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) AVPlayerItem *playerItem ``` |
| To | ``` @property(nonatomic, retain, nullable) AVPlayerItem *playerItem ``` |

Modified [+[AVSynchronizedLayer synchronizedLayerWithPlayerItem:]](https://developer.apple.com/documentation/avfoundation/avsynchronizedlayer/1388781-synchronizedlayerwithplayeritem)

|  | Declaration |
| --- | --- |
| From | ``` + (AVSynchronizedLayer *)synchronizedLayerWithPlayerItem:(AVPlayerItem *)playerItem ``` |
| To | ``` + (AVSynchronizedLayer * _Nonnull)synchronizedLayerWithPlayerItem:(AVPlayerItem * _Nonnull)playerItem ``` |

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

Modified [AVTextStyleRule.textSelector](https://developer.apple.com/documentation/avfoundation/avtextstylerule/1389451-textselector)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *textSelector ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSString *textSelector ``` |

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

#### AVTime.h

Modified [-[NSCoder decodeCMTimeForKey:]](https://developer.apple.com/documentation/foundation/nscoder/1389544-decodetime)

|  | Declaration |
| --- | --- |
| From | ``` - (CMTime)decodeCMTimeForKey:(NSString *)key ``` |
| To | ``` - (CMTime)decodeCMTimeForKey:(NSString * _Nonnull)key ``` |

Modified [-[NSCoder decodeCMTimeMappingForKey:]](https://developer.apple.com/documentation/foundation/nscoder/1389860-decodecmtimemappingforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (CMTimeMapping)decodeCMTimeMappingForKey:(NSString *)key ``` |
| To | ``` - (CMTimeMapping)decodeCMTimeMappingForKey:(NSString * _Nonnull)key ``` |

Modified [-[NSCoder decodeCMTimeRangeForKey:]](https://developer.apple.com/documentation/foundation/nscoder/1385718-decodecmtimerangeforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (CMTimeRange)decodeCMTimeRangeForKey:(NSString *)key ``` |
| To | ``` - (CMTimeRange)decodeCMTimeRangeForKey:(NSString * _Nonnull)key ``` |

Modified [-[NSCoder encodeCMTime:forKey:]](https://developer.apple.com/documentation/foundation/nscoder/1388869-encode)

|  | Declaration |
| --- | --- |
| From | ``` - (void)encodeCMTime:(CMTime)time forKey:(NSString *)key ``` |
| To | ``` - (void)encodeCMTime:(CMTime)time forKey:(NSString * _Nonnull)key ``` |

Modified [-[NSCoder encodeCMTimeMapping:forKey:]](https://developer.apple.com/documentation/foundation/nscoder/1389496-encode)

|  | Declaration |
| --- | --- |
| From | ``` - (void)encodeCMTimeMapping:(CMTimeMapping)timeMapping forKey:(NSString *)key ``` |
| To | ``` - (void)encodeCMTimeMapping:(CMTimeMapping)timeMapping forKey:(NSString * _Nonnull)key ``` |

Modified [-[NSCoder encodeCMTimeRange:forKey:]](https://developer.apple.com/documentation/foundation/nscoder/1386649-encodecmtimerange)

|  | Declaration |
| --- | --- |
| From | ``` - (void)encodeCMTimeRange:(CMTimeRange)timeRange forKey:(NSString *)key ``` |
| To | ``` - (void)encodeCMTimeRange:(CMTimeRange)timeRange forKey:(NSString * _Nonnull)key ``` |

Modified [+[NSValue valueWithCMTime:]](https://developer.apple.com/documentation/foundation/nsvalue/1388561-valuewithcmtime)

|  | Declaration |
| --- | --- |
| From | ``` + (NSValue *)valueWithCMTime:(CMTime)time ``` |
| To | ``` + (NSValue * _Nonnull)valueWithCMTime:(CMTime)time ``` |

Modified [+[NSValue valueWithCMTimeMapping:]](https://developer.apple.com/documentation/foundation/nsvalue/1387556-valuewithcmtimemapping)

|  | Declaration |
| --- | --- |
| From | ``` + (NSValue *)valueWithCMTimeMapping:(CMTimeMapping)timeMapping ``` |
| To | ``` + (NSValue * _Nonnull)valueWithCMTimeMapping:(CMTimeMapping)timeMapping ``` |

Modified [+[NSValue valueWithCMTimeRange:]](https://developer.apple.com/documentation/foundation/nsvalue/1386915-valuewithcmtimerange)

|  | Declaration |
| --- | --- |
| From | ``` + (NSValue *)valueWithCMTimeRange:(CMTimeRange)timeRange ``` |
| To | ``` + (NSValue * _Nonnull)valueWithCMTimeRange:(CMTimeRange)timeRange ``` |

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

Modified [-[AVTimedMetadataGroup copyFormatDescription]](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/1389461-copyformatdescription)

|  | Declaration |
| --- | --- |
| From | ``` - (CMMetadataFormatDescriptionRef)copyFormatDescription ``` |
| To | ``` - (CMMetadataFormatDescriptionRef _Nullable)copyFormatDescription ``` |

Modified [-[AVTimedMetadataGroup initWithItems:timeRange:]](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/1389632-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithItems:(NSArray *)items timeRange:(CMTimeRange)timeRange ``` |
| To | ``` - (instancetype _Nonnull)initWithItems:(NSArray<AVMetadataItem *> * _Nonnull)items timeRange:(CMTimeRange)timeRange ``` |

Modified [-[AVTimedMetadataGroup initWithSampleBuffer:]](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/1387128-initwithsamplebuffer)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSampleBuffer:(CMSampleBufferRef)sampleBuffer ``` |
| To | ``` - (instancetype _Nullable)initWithSampleBuffer:(CMSampleBufferRef _Nonnull)sampleBuffer ``` |

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

Added [AVAsynchronousCIImageFilteringRequest](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest)Added [AVAsynchronousCIImageFilteringRequest.compositionTime](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/1388240-compositiontime)Added [-[AVAsynchronousCIImageFilteringRequest finishWithError:]](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/1386608-finishwitherror)Added [-[AVAsynchronousCIImageFilteringRequest finishWithImage:context:]](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/1389124-finish)Added [AVAsynchronousCIImageFilteringRequest.renderSize](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/1387933-rendersize)Added [AVAsynchronousCIImageFilteringRequest.sourceImage](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/1387577-sourceimage)Modified [-[AVAsynchronousVideoCompositionRequest finishWithComposedVideoFrame:]](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1387450-finish)

|  | Declaration |
| --- | --- |
| From | ``` - (void)finishWithComposedVideoFrame:(CVPixelBufferRef)composedVideoFrame ``` |
| To | ``` - (void)finishWithComposedVideoFrame:(CVPixelBufferRef _Nonnull)composedVideoFrame ``` |

Modified [-[AVAsynchronousVideoCompositionRequest finishWithError:]](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1390797-finish)

|  | Declaration |
| --- | --- |
| From | ``` - (void)finishWithError:(NSError *)error ``` |
| To | ``` - (void)finishWithError:(NSError * _Nonnull)error ``` |

Modified [AVAsynchronousVideoCompositionRequest.renderContext](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1389112-rendercontext)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVVideoCompositionRenderContext *renderContext ``` |
| To | ``` @property(nonatomic, readonly, nonnull) AVVideoCompositionRenderContext *renderContext ``` |

Modified [-[AVAsynchronousVideoCompositionRequest sourceFrameByTrackID:]](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1390379-sourceframebytrackid)

|  | Declaration |
| --- | --- |
| From | ``` - (CVPixelBufferRef)sourceFrameByTrackID:(CMPersistentTrackID)trackID ``` |
| To | ``` - (CVPixelBufferRef _Nullable)sourceFrameByTrackID:(CMPersistentTrackID)trackID ``` |

Modified [AVAsynchronousVideoCompositionRequest.sourceTrackIDs](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1388898-sourcetrackids)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *sourceTrackIDs ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSNumber *> *sourceTrackIDs ``` |

Modified [AVAsynchronousVideoCompositionRequest.videoCompositionInstruction](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/1386672-videocompositioninstruction)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id<AVVideoCompositionInstruction> videoCompositionInstruction ``` |
| To | ``` @property(nonatomic, readonly, nonnull) id<AVVideoCompositionInstruction> videoCompositionInstruction ``` |

Modified [-[AVVideoCompositing renderContextChanged:]](https://developer.apple.com/documentation/avfoundation/avvideocompositing/1390363-rendercontextchanged)

|  | Declaration |
| --- | --- |
| From | ``` - (void)renderContextChanged:(AVVideoCompositionRenderContext *)newRenderContext ``` |
| To | ``` - (void)renderContextChanged:(AVVideoCompositionRenderContext * _Nonnull)newRenderContext ``` |

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

Modified [-[AVVideoCompositing startVideoCompositionRequest:]](https://developer.apple.com/documentation/avfoundation/avvideocompositing/1388894-startrequest)

|  | Declaration |
| --- | --- |
| From | ``` - (void)startVideoCompositionRequest:(AVAsynchronousVideoCompositionRequest *)asyncVideoCompositionRequest ``` |
| To | ``` - (void)startVideoCompositionRequest:(AVAsynchronousVideoCompositionRequest * _Nonnull)asyncVideoCompositionRequest ``` |

Modified [AVVideoCompositionInstruction.requiredSourceTrackIDs](https://developer.apple.com/documentation/avfoundation/1386654-avvideocompositioninstruction/1388661-requiredsourcetrackids)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *requiredSourceTrackIDs ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<NSValue *> *requiredSourceTrackIDs ``` |

Modified [-[AVVideoCompositionRenderContext newPixelBuffer]](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/1386802-newpixelbuffer)

|  | Declaration |
| --- | --- |
| From | ``` - (CVPixelBufferRef)newPixelBuffer ``` |
| To | ``` - (CVPixelBufferRef _Nullable)newPixelBuffer ``` |

Modified [AVVideoCompositionRenderContext.videoComposition](https://developer.apple.com/documentation/avfoundation/avvideocompositionrendercontext/1390647-videocomposition)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) AVVideoComposition *videoComposition ``` |
| To | ``` @property(nonatomic, readonly, nonnull) AVVideoComposition *videoComposition ``` |

#### AVVideoComposition.h

Added [+[AVMutableVideoComposition videoCompositionWithAsset:applyingCIFiltersWithHandler:]](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1387006-videocompositionwithasset)Added [+[AVVideoComposition videoCompositionWithAsset:applyingCIFiltersWithHandler:]](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1389556-init)Added AVMutableVideoComposition(AVMutableVideoCompositionFiltering)Added AVVideoComposition(AVVideoCompositionFiltering)Modified [AVMutableVideoComposition.animationTool](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1390395-animationtool)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) AVVideoCompositionCoreAnimationTool *animationTool ``` |
| To | ``` @property(nonatomic, retain, nullable) AVVideoCompositionCoreAnimationTool *animationTool ``` |

Modified [AVMutableVideoComposition.customVideoCompositorClass](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1390649-customvideocompositorclass)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) Class<AVVideoCompositing> customVideoCompositorClass ``` |
| To | ``` @property(nonatomic, retain, nullable) Class<AVVideoCompositing> customVideoCompositorClass ``` |

Modified [AVMutableVideoComposition.instructions](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1385815-instructions)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *instructions ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSArray<id<AVVideoCompositionInstruction>> *instructions ``` |

Modified [+[AVMutableVideoComposition videoComposition]](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1519720-videocomposition)

|  | Declaration |
| --- | --- |
| From | ``` + (AVMutableVideoComposition *)videoComposition ``` |
| To | ``` + (AVMutableVideoComposition * _Nonnull)videoComposition ``` |

Modified [+[AVMutableVideoComposition videoCompositionWithPropertiesOfAsset:]](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1388430-videocompositionwithpropertiesof)

|  | Declaration |
| --- | --- |
| From | ``` + (AVMutableVideoComposition *)videoCompositionWithPropertiesOfAsset:(AVAsset *)asset ``` |
| To | ``` + (AVMutableVideoComposition * _Nonnull)videoCompositionWithPropertiesOfAsset:(AVAsset * _Nonnull)asset ``` |

Modified [AVMutableVideoCompositionInstruction.backgroundColor](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositioninstruction/1390236-backgroundcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) CGColorRef backgroundColor ``` |
| To | ``` @property(nonatomic, retain, nullable) CGColorRef backgroundColor ``` |

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

Modified [AVVideoComposition.animationTool](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1387030-animationtool)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) AVVideoCompositionCoreAnimationTool *animationTool ``` |
| To | ``` @property(nonatomic, readonly, retain, nullable) AVVideoCompositionCoreAnimationTool *animationTool ``` |

Modified [AVVideoComposition.customVideoCompositorClass](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1389622-customvideocompositorclass)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) Class<AVVideoCompositing> customVideoCompositorClass ``` |
| To | ``` @property(nonatomic, readonly, nullable) Class<AVVideoCompositing> customVideoCompositorClass ``` |

Modified [AVVideoComposition.instructions](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1389211-instructions)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *instructions ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<id<AVVideoCompositionInstruction>> *instructions ``` |

Modified [-[AVVideoComposition isValidForAsset:timeRange:validationDelegate:]](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1389917-isvalid)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isValidForAsset:(AVAsset *)asset timeRange:(CMTimeRange)timeRange validationDelegate:(id<AVVideoCompositionValidationHandling>)validationDelegate ``` |
| To | ``` - (BOOL)isValidForAsset:(AVAsset * _Nullable)asset timeRange:(CMTimeRange)timeRange validationDelegate:(id<AVVideoCompositionValidationHandling> _Nullable)validationDelegate ``` |

Modified [+[AVVideoComposition videoCompositionWithPropertiesOfAsset:]](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1385892-init)

|  | Declaration |
| --- | --- |
| From | ``` + (AVVideoComposition *)videoCompositionWithPropertiesOfAsset:(AVAsset *)asset ``` |
| To | ``` + (AVVideoComposition * _Nonnull)videoCompositionWithPropertiesOfAsset:(AVAsset * _Nonnull)asset ``` |

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

Modified [-[AVVideoCompositionLayerInstruction getCropRectangleRampForTime:startCropRectangle:endCropRectangle:timeRange:]](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/1387998-getcroprectanglerampfortime)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)getCropRectangleRampForTime:(CMTime)time startCropRectangle:(CGRect *)startCropRectangle endCropRectangle:(CGRect *)endCropRectangle timeRange:(CMTimeRange *)timeRange ``` |
| To | ``` - (BOOL)getCropRectangleRampForTime:(CMTime)time startCropRectangle:(CGRect * _Nullable)startCropRectangle endCropRectangle:(CGRect * _Nullable)endCropRectangle timeRange:(CMTimeRange * _Nullable)timeRange ``` |

Modified [-[AVVideoCompositionLayerInstruction getOpacityRampForTime:startOpacity:endOpacity:timeRange:]](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/1388471-getopacityrampfortime)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)getOpacityRampForTime:(CMTime)time startOpacity:(float *)startOpacity endOpacity:(float *)endOpacity timeRange:(CMTimeRange *)timeRange ``` |
| To | ``` - (BOOL)getOpacityRampForTime:(CMTime)time startOpacity:(float * _Nullable)startOpacity endOpacity:(float * _Nullable)endOpacity timeRange:(CMTimeRange * _Nullable)timeRange ``` |

Modified [-[AVVideoCompositionLayerInstruction getTransformRampForTime:startTransform:endTransform:timeRange:]](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/1387257-gettransformramp)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)getTransformRampForTime:(CMTime)time startTransform:(CGAffineTransform *)startTransform endTransform:(CGAffineTransform *)endTransform timeRange:(CMTimeRange *)timeRange ``` |
| To | ``` - (BOOL)getTransformRampForTime:(CMTime)time startTransform:(CGAffineTransform * _Nullable)startTransform endTransform:(CGAffineTransform * _Nullable)endTransform timeRange:(CMTimeRange * _Nullable)timeRange ``` |

Modified [-[AVVideoCompositionValidationHandling videoComposition:shouldContinueValidatingAfterFindingEmptyTimeRange:]](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/1388620-videocomposition)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)videoComposition:(AVVideoComposition *)videoComposition shouldContinueValidatingAfterFindingEmptyTimeRange:(CMTimeRange)timeRange ``` |
| To | ``` - (BOOL)videoComposition:(AVVideoComposition * _Nonnull)videoComposition shouldContinueValidatingAfterFindingEmptyTimeRange:(CMTimeRange)timeRange ``` |

Modified [-[AVVideoCompositionValidationHandling videoComposition:shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction:]](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/1390721-videocomposition)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)videoComposition:(AVVideoComposition *)videoComposition shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction:(id<AVVideoCompositionInstruction>)videoCompositionInstruction ``` |
| To | ``` - (BOOL)videoComposition:(AVVideoComposition * _Nonnull)videoComposition shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction:(id<AVVideoCompositionInstruction> _Nonnull)videoCompositionInstruction ``` |

Modified [-[AVVideoCompositionValidationHandling videoComposition:shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction:layerInstruction:asset:]](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/1388452-videocomposition)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)videoComposition:(AVVideoComposition *)videoComposition shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction:(id<AVVideoCompositionInstruction>)videoCompositionInstruction layerInstruction:(AVVideoCompositionLayerInstruction *)layerInstruction asset:(AVAsset *)asset ``` |
| To | ``` - (BOOL)videoComposition:(AVVideoComposition * _Nonnull)videoComposition shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction:(id<AVVideoCompositionInstruction> _Nonnull)videoCompositionInstruction layerInstruction:(AVVideoCompositionLayerInstruction * _Nonnull)layerInstruction asset:(AVAsset * _Nonnull)asset ``` |

Modified [-[AVVideoCompositionValidationHandling videoComposition:shouldContinueValidatingAfterFindingInvalidValueForKey:]](https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/1389404-videocomposition)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)videoComposition:(AVVideoComposition *)videoComposition shouldContinueValidatingAfterFindingInvalidValueForKey:(NSString *)key ``` |
| To | ``` - (BOOL)videoComposition:(AVVideoComposition * _Nonnull)videoComposition shouldContinueValidatingAfterFindingInvalidValueForKey:(NSString * _Nonnull)key ``` |

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
