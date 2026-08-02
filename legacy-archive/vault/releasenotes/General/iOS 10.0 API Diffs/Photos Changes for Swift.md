---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/Photos.html
archived_at: '2026-07-18T02:55:36.000140Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# Photos Changes for Swift

### Photos

Removed [PHAssetBurstSelectionType.None](https://developer.apple.com/documentation/photokit/phassetburstselectiontype/phassetburstselectiontypenone)Removed [PHAssetMediaSubtype.None](https://developer.apple.com/documentation/photokit/phassetmediasubtype/phassetmediasubtypenone)Removed [PHAssetSourceType.TypeNone](https://developer.apple.com/documentation/photokit/phassetsourcetype/phassetsourcetypenone)Removed [PHChange.changeDetailsForFetchResult(_: PHFetchResult) -> PHFetchResultChangeDetails?](https://developer.apple.com/documentation/photokit/phchange/1613912-changedetails)Removed [PHChange.changeDetailsForObject(_: PHObject) -> PHObjectChangeDetails?](https://developer.apple.com/documentation/photokit/phchange/1613918-changedetails)Added [PHAssetResourceType.adjustmentBasePairedVideo](https://developer.apple.com/documentation/photokit/phassetresourcetype/adjustmentbasepairedvideo)Added [PHAssetResourceType.fullSizePairedVideo](https://developer.apple.com/documentation/photokit/phassetresourcetype/fullsizepairedvideo)Added [PHChange.changeDetails<T : PHObject>(for: PHFetchResult<T>) -> PHFetchResultChangeDetails<T>?](https://developer.apple.com/documentation/photokit/phchange/2437203-changedetails)Added [PHChange.changeDetails<T : PHObject>(for: T) -> PHObjectChangeDetails<T>?](https://developer.apple.com/documentation/photokit/phchange/2437204-changedetails)Added [PHContentEditingInput.livePhoto](https://developer.apple.com/documentation/photokit/phcontenteditinginput/1638106-livephoto)Added [PHLivePhotoEditingContext](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext)Added [PHLivePhotoEditingContext.audioVolume](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642113-audiovolume)Added [PHLivePhotoEditingContext.cancel()](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642083-cancel)Added [PHLivePhotoEditingContext.duration](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642109-duration)Added [PHLivePhotoEditingContext.frameProcessor](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642132-frameprocessor)Added [PHLivePhotoEditingContext.fullSizeImage](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642106-fullsizeimage)Added [PHLivePhotoEditingContext.init(livePhotoEditingInput: PHContentEditingInput)](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642121-init)Added [PHLivePhotoEditingContext.orientation](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642093-orientation)Added [PHLivePhotoEditingContext.photoTime](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642131-phototime)Added [PHLivePhotoEditingContext.prepareLivePhotoForPlayback(withTargetSize: CGSize, options: [String : Any]?, completionHandler: (PHLivePhoto?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642101-preparelivephotoforplayback)Added [PHLivePhotoEditingContext.saveLivePhoto(to: PHContentEditingOutput, options: [String : Any]?, completionHandler: (Bool, Error?) -> Swift.Void)](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642082-savelivephoto)Added [PHLivePhotoEditingOption [struct]](https://developer.apple.com/documentation/photokit/phlivephotoeditingoption)Added [PHLivePhotoEditingOption.init(rawValue: String)](https://developer.apple.com/documentation/photokit/phlivephotoeditingoption/1823510-init)Added [PHLivePhotoEditingOption.shouldRenderAtPlaybackTime](https://developer.apple.com/documentation/photokit/phlivephotoeditingoption/1642124-shouldrenderatplaybacktime)Added [PHLivePhotoFrame](https://developer.apple.com/documentation/photokit/phlivephotoframe)Added [PHLivePhotoFrame.image](https://developer.apple.com/documentation/photokit/phlivephotoframe/1642114-image)Added [PHLivePhotoFrame.renderScale](https://developer.apple.com/documentation/photokit/phlivephotoframe/1642123-renderscale)Added [PHLivePhotoFrame.time](https://developer.apple.com/documentation/photokit/phlivephotoframe/1642126-time)Added [PHLivePhotoFrame.type](https://developer.apple.com/documentation/photokit/phlivephotoframe/1642087-type)Added [PHLivePhotoFrameType [enum]](https://developer.apple.com/documentation/photokit/phlivephotoframetype)Added [PHLivePhotoFrameType.photo](https://developer.apple.com/documentation/photokit/phlivephotoframetype/phlivephotoframetypephoto)Added [PHLivePhotoFrameType.video](https://developer.apple.com/documentation/photokit/phlivephotoframetype/video)Added [PHLivePhotoRequestOptions.version](https://developer.apple.com/documentation/photokit/phlivephotorequestoptions/1648591-version)Added [PHLivePhotoFrameProcessingBlock](https://developer.apple.com/documentation/photokit/phlivephotoframeprocessingblock)Modified [PHAdjustmentData](https://developer.apple.com/documentation/photokit/phadjustmentdata)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHAdjustmentData : NSObject {     init(formatIdentifier formatIdentifier: String, formatVersion formatVersion: String, data data: NSData)     var formatIdentifier: String { get }     var formatVersion: String { get }     var data: NSData { get } } ``` | -- |
| To | ``` class PHAdjustmentData : NSObject {     init(formatIdentifier formatIdentifier: String, formatVersion formatVersion: String, data data: Data)     var formatIdentifier: String { get }     var formatVersion: String { get }     var data: Data { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHAdjustmentData : CVarArg { } extension PHAdjustmentData : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PHAdjustmentData.data](https://developer.apple.com/documentation/photokit/phadjustmentdata/1518617-data)

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData { get } ``` |
| To | ``` var data: Data { get } ``` |

Modified [PHAdjustmentData.init(formatIdentifier: String, formatVersion: String, data: Data)](https://developer.apple.com/documentation/photokit/phadjustmentdata/1518669-initwithformatidentifier)

|  | Declaration |
| --- | --- |
| From | ``` init(formatIdentifier formatIdentifier: String, formatVersion formatVersion: String, data data: NSData) ``` |
| To | ``` init(formatIdentifier formatIdentifier: String, formatVersion formatVersion: String, data data: Data) ``` |

Modified [PHAsset](https://developer.apple.com/documentation/photokit/phasset)

|  | Declaration |
| --- | --- |
| From | ``` class PHAsset : PHObject {     var mediaType: PHAssetMediaType { get }     var mediaSubtypes: PHAssetMediaSubtype { get }     var pixelWidth: Int { get }     var pixelHeight: Int { get }     var creationDate: NSDate? { get }     var modificationDate: NSDate? { get }     var location: CLLocation? { get }     var duration: NSTimeInterval { get }     var hidden: Bool { get }     var favorite: Bool { get }     var burstIdentifier: String? { get }     var burstSelectionTypes: PHAssetBurstSelectionType { get }     var representsBurst: Bool { get }     var sourceType: PHAssetSourceType { get }     func canPerformEditOperation(_ editOperation: PHAssetEditOperation) -> Bool     class func fetchAssetsInAssetCollection(_ assetCollection: PHAssetCollection, options options: PHFetchOptions?) -> PHFetchResult     class func fetchAssetsWithLocalIdentifiers(_ identifiers: [String], options options: PHFetchOptions?) -> PHFetchResult     class func fetchKeyAssetsInAssetCollection(_ assetCollection: PHAssetCollection, options options: PHFetchOptions?) -> PHFetchResult?     class func fetchAssetsWithBurstIdentifier(_ burstIdentifier: String, options options: PHFetchOptions?) -> PHFetchResult     class func fetchAssetsWithOptions(_ options: PHFetchOptions?) -> PHFetchResult     class func fetchAssetsWithMediaType(_ mediaType: PHAssetMediaType, options options: PHFetchOptions?) -> PHFetchResult     class func fetchAssetsWithALAssetURLs(_ assetURLs: [NSURL], options options: PHFetchOptions?) -> PHFetchResult } extension PHAsset {     func requestContentEditingInputWithOptions(_ options: PHContentEditingInputRequestOptions?, completionHandler completionHandler: (PHContentEditingInput?, [NSObject : AnyObject]) -> Void) -> PHContentEditingInputRequestID     func cancelContentEditingInputRequest(_ requestID: PHContentEditingInputRequestID) } ``` |
| To | ``` class PHAsset : PHObject {     var mediaType: PHAssetMediaType { get }     var mediaSubtypes: PHAssetMediaSubtype { get }     var pixelWidth: Int { get }     var pixelHeight: Int { get }     var creationDate: Date? { get }     var modificationDate: Date? { get }     var location: CLLocation? { get }     var duration: TimeInterval { get }     var isHidden: Bool { get }     var isFavorite: Bool { get }     var burstIdentifier: String? { get }     var burstSelectionTypes: PHAssetBurstSelectionType { get }     var representsBurst: Bool { get }     var sourceType: PHAssetSourceType { get }     func canPerform(_ editOperation: PHAssetEditOperation) -> Bool     class func fetchAssets(in assetCollection: PHAssetCollection, options options: PHFetchOptions?) -> PHFetchResult<PHAsset>     class func fetchAssets(withLocalIdentifiers identifiers: [String], options options: PHFetchOptions?) -> PHFetchResult<PHAsset>     class func fetchKeyAssets(in assetCollection: PHAssetCollection, options options: PHFetchOptions?) -> PHFetchResult<PHAsset>?     class func fetchAssets(withBurstIdentifier burstIdentifier: String, options options: PHFetchOptions?) -> PHFetchResult<PHAsset>     class func fetchAssets(with options: PHFetchOptions?) -> PHFetchResult<PHAsset>     class func fetchAssets(with mediaType: PHAssetMediaType, options options: PHFetchOptions?) -> PHFetchResult<PHAsset>     class func fetchAssets(withALAssetURLs assetURLs: [URL], options options: PHFetchOptions?) -> PHFetchResult<PHAsset>     func requestContentEditingInput(with options: PHContentEditingInputRequestOptions?, completionHandler completionHandler: @escaping (PHContentEditingInput?, [AnyHashable : Any]) -> Swift.Void) -> PHContentEditingInputRequestID     func cancelContentEditingInputRequest(_ requestID: PHContentEditingInputRequestID) } extension PHAsset {     func requestContentEditingInput(with options: PHContentEditingInputRequestOptions?, completionHandler completionHandler: @escaping (PHContentEditingInput?, [AnyHashable : Any]) -> Swift.Void) -> PHContentEditingInputRequestID     func cancelContentEditingInputRequest(_ requestID: PHContentEditingInputRequestID) } ``` |

Modified [PHAsset.canPerform(_: PHAssetEditOperation) -> Bool](https://developer.apple.com/documentation/photokit/phasset/1624779-canperformeditoperation)

|  | Declaration |
| --- | --- |
| From | ``` func canPerformEditOperation(_ editOperation: PHAssetEditOperation) -> Bool ``` |
| To | ``` func canPerform(_ editOperation: PHAssetEditOperation) -> Bool ``` |

Modified [PHAsset.creationDate](https://developer.apple.com/documentation/photokit/phasset/1624776-creationdate)

|  | Declaration |
| --- | --- |
| From | ``` var creationDate: NSDate? { get } ``` |
| To | ``` var creationDate: Date? { get } ``` |

Modified [PHAsset.duration](https://developer.apple.com/documentation/photokit/phasset/1624741-duration)

|  | Declaration |
| --- | --- |
| From | ``` var duration: NSTimeInterval { get } ``` |
| To | ``` var duration: TimeInterval { get } ``` |

Modified [PHAsset.fetchAssets(in: PHAssetCollection, options: PHFetchOptions?) -> PHFetchResult<PHAsset> [class]](https://developer.apple.com/documentation/photokit/phasset/1624757-fetchassetsinassetcollection)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAssetsInAssetCollection(_ assetCollection: PHAssetCollection, options options: PHFetchOptions?) -> PHFetchResult ``` |
| To | ``` class func fetchAssets(in assetCollection: PHAssetCollection, options options: PHFetchOptions?) -> PHFetchResult<PHAsset> ``` |

Modified [PHAsset.fetchAssets(with: PHFetchOptions?) -> PHFetchResult<PHAsset> [class]](https://developer.apple.com/documentation/photokit/phasset/1624783-fetchassetswithoptions)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAssetsWithOptions(_ options: PHFetchOptions?) -> PHFetchResult ``` |
| To | ``` class func fetchAssets(with options: PHFetchOptions?) -> PHFetchResult<PHAsset> ``` |

Modified [PHAsset.fetchAssets(with: PHAssetMediaType, options: PHFetchOptions?) -> PHFetchResult<PHAsset> [class]](https://developer.apple.com/documentation/photokit/phasset/1624725-fetchassets)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAssetsWithMediaType(_ mediaType: PHAssetMediaType, options options: PHFetchOptions?) -> PHFetchResult ``` |
| To | ``` class func fetchAssets(with mediaType: PHAssetMediaType, options options: PHFetchOptions?) -> PHFetchResult<PHAsset> ``` |

Modified [PHAsset.fetchAssets(withALAssetURLs: [URL], options: PHFetchOptions?) -> PHFetchResult<PHAsset> [class]](https://developer.apple.com/documentation/photokit/phasset/1624782-fetchassetswithalasseturls)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAssetsWithALAssetURLs(_ assetURLs: [NSURL], options options: PHFetchOptions?) -> PHFetchResult ``` |
| To | ``` class func fetchAssets(withALAssetURLs assetURLs: [URL], options options: PHFetchOptions?) -> PHFetchResult<PHAsset> ``` |

Modified [PHAsset.fetchAssets(withBurstIdentifier: String, options: PHFetchOptions?) -> PHFetchResult<PHAsset> [class]](https://developer.apple.com/documentation/photokit/phasset/1624723-fetchassets)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAssetsWithBurstIdentifier(_ burstIdentifier: String, options options: PHFetchOptions?) -> PHFetchResult ``` |
| To | ``` class func fetchAssets(withBurstIdentifier burstIdentifier: String, options options: PHFetchOptions?) -> PHFetchResult<PHAsset> ``` |

Modified [PHAsset.fetchAssets(withLocalIdentifiers: [String], options: PHFetchOptions?) -> PHFetchResult<PHAsset> [class]](https://developer.apple.com/documentation/photokit/phasset/1624732-fetchassetswithlocalidentifiers)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAssetsWithLocalIdentifiers(_ identifiers: [String], options options: PHFetchOptions?) -> PHFetchResult ``` |
| To | ``` class func fetchAssets(withLocalIdentifiers identifiers: [String], options options: PHFetchOptions?) -> PHFetchResult<PHAsset> ``` |

Modified [PHAsset.fetchKeyAssets(in: PHAssetCollection, options: PHFetchOptions?) -> PHFetchResult<PHAsset>? [class]](https://developer.apple.com/documentation/photokit/phasset/1624778-fetchkeyassets)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchKeyAssetsInAssetCollection(_ assetCollection: PHAssetCollection, options options: PHFetchOptions?) -> PHFetchResult? ``` |
| To | ``` class func fetchKeyAssets(in assetCollection: PHAssetCollection, options options: PHFetchOptions?) -> PHFetchResult<PHAsset>? ``` |

Modified [PHAsset.isFavorite](https://developer.apple.com/documentation/photokit/phasset/1624755-isfavorite)

|  | Declaration |
| --- | --- |
| From | ``` var favorite: Bool { get } ``` |
| To | ``` var isFavorite: Bool { get } ``` |

Modified [PHAsset.isHidden](https://developer.apple.com/documentation/photokit/phasset/1624773-ishidden)

|  | Declaration |
| --- | --- |
| From | ``` var hidden: Bool { get } ``` |
| To | ``` var isHidden: Bool { get } ``` |

Modified [PHAsset.modificationDate](https://developer.apple.com/documentation/photokit/phasset/1624731-modificationdate)

|  | Declaration |
| --- | --- |
| From | ``` var modificationDate: NSDate? { get } ``` |
| To | ``` var modificationDate: Date? { get } ``` |

Modified [PHAsset.requestContentEditingInput(with: PHContentEditingInputRequestOptions?, completionHandler: (PHContentEditingInput?, [AnyHashable : Any]) -> Swift.Void) -> PHContentEditingInputRequestID](https://developer.apple.com/documentation/photokit/phasset/1624061-requestcontenteditinginputwithop)

|  | Declaration |
| --- | --- |
| From | ``` func requestContentEditingInputWithOptions(_ options: PHContentEditingInputRequestOptions?, completionHandler completionHandler: (PHContentEditingInput?, [NSObject : AnyObject]) -> Void) -> PHContentEditingInputRequestID ``` |
| To | ``` func requestContentEditingInput(with options: PHContentEditingInputRequestOptions?, completionHandler completionHandler: @escaping (PHContentEditingInput?, [AnyHashable : Any]) -> Swift.Void) -> PHContentEditingInputRequestID ``` |

Modified [PHAssetBurstSelectionType [struct]](https://developer.apple.com/documentation/photokit/phassetburstselectiontype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct PHAssetBurstSelectionType : OptionSetType {     init(rawValue rawValue: UInt)     static var None: PHAssetBurstSelectionType { get }     static var AutoPick: PHAssetBurstSelectionType { get }     static var UserPick: PHAssetBurstSelectionType { get } } ``` | OptionSetType |
| To | ``` struct PHAssetBurstSelectionType : OptionSet {     init(rawValue rawValue: UInt)     static var none: PHAssetBurstSelectionType { get }     static var autoPick: PHAssetBurstSelectionType { get }     static var userPick: PHAssetBurstSelectionType { get }     func intersect(_ other: PHAssetBurstSelectionType) -> PHAssetBurstSelectionType     func exclusiveOr(_ other: PHAssetBurstSelectionType) -> PHAssetBurstSelectionType     mutating func unionInPlace(_ other: PHAssetBurstSelectionType)     mutating func intersectInPlace(_ other: PHAssetBurstSelectionType)     mutating func exclusiveOrInPlace(_ other: PHAssetBurstSelectionType)     func isSubsetOf(_ other: PHAssetBurstSelectionType) -> Bool     func isDisjointWith(_ other: PHAssetBurstSelectionType) -> Bool     func isSupersetOf(_ other: PHAssetBurstSelectionType) -> Bool     mutating func subtractInPlace(_ other: PHAssetBurstSelectionType)     func isStrictSupersetOf(_ other: PHAssetBurstSelectionType) -> Bool     func isStrictSubsetOf(_ other: PHAssetBurstSelectionType) -> Bool } extension PHAssetBurstSelectionType {     func union(_ other: PHAssetBurstSelectionType) -> PHAssetBurstSelectionType     func intersection(_ other: PHAssetBurstSelectionType) -> PHAssetBurstSelectionType     func symmetricDifference(_ other: PHAssetBurstSelectionType) -> PHAssetBurstSelectionType } extension PHAssetBurstSelectionType {     func contains(_ member: PHAssetBurstSelectionType) -> Bool     mutating func insert(_ newMember: PHAssetBurstSelectionType) -> (inserted: Bool, memberAfterInsert: PHAssetBurstSelectionType)     mutating func remove(_ member: PHAssetBurstSelectionType) -> PHAssetBurstSelectionType?     mutating func update(with newMember: PHAssetBurstSelectionType) -> PHAssetBurstSelectionType? } extension PHAssetBurstSelectionType {     convenience init()     mutating func formUnion(_ other: PHAssetBurstSelectionType)     mutating func formIntersection(_ other: PHAssetBurstSelectionType)     mutating func formSymmetricDifference(_ other: PHAssetBurstSelectionType) } extension PHAssetBurstSelectionType {     convenience init<S : Sequence where S.Iterator.Element == PHAssetBurstSelectionType>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: PHAssetBurstSelectionType...)     mutating func subtract(_ other: PHAssetBurstSelectionType)     func isSubset(of other: PHAssetBurstSelectionType) -> Bool     func isSuperset(of other: PHAssetBurstSelectionType) -> Bool     func isDisjoint(with other: PHAssetBurstSelectionType) -> Bool     func subtracting(_ other: PHAssetBurstSelectionType) -> PHAssetBurstSelectionType     var isEmpty: Bool { get }     func isStrictSuperset(of other: PHAssetBurstSelectionType) -> Bool     func isStrictSubset(of other: PHAssetBurstSelectionType) -> Bool } ``` | OptionSet |

Modified [PHAssetBurstSelectionType.autoPick](https://developer.apple.com/documentation/photokit/phassetburstselectiontype/1613985-autopick)

|  | Declaration |
| --- | --- |
| From | ``` static var AutoPick: PHAssetBurstSelectionType { get } ``` |
| To | ``` static var autoPick: PHAssetBurstSelectionType { get } ``` |

Modified [PHAssetBurstSelectionType.userPick](https://developer.apple.com/documentation/photokit/phassetburstselectiontype/1614045-userpick)

|  | Declaration |
| --- | --- |
| From | ``` static var UserPick: PHAssetBurstSelectionType { get } ``` |
| To | ``` static var userPick: PHAssetBurstSelectionType { get } ``` |

Modified [PHAssetChangeRequest](https://developer.apple.com/documentation/photokit/phassetchangerequest)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHAssetChangeRequest : NSObject {     class func creationRequestForAssetFromImage(_ image: UIImage) -> Self     class func creationRequestForAssetFromImageAtFileURL(_ fileURL: NSURL) -> Self?     class func creationRequestForAssetFromVideoAtFileURL(_ fileURL: NSURL) -> Self?     var placeholderForCreatedAsset: PHObjectPlaceholder? { get }     class func deleteAssets(_ assets: NSFastEnumeration)     convenience init(forAsset asset: PHAsset)     class func changeRequestForAsset(_ asset: PHAsset) -> Self     var creationDate: NSDate?     var location: CLLocation?     var favorite: Bool     var hidden: Bool     var contentEditingOutput: PHContentEditingOutput?     func revertAssetContentToOriginal() } ``` | -- |
| To | ``` class PHAssetChangeRequest : NSObject {     class func creationRequestForAsset(from image: UIImage) -> Self     class func creationRequestForAssetFromImage(atFileURL fileURL: URL) -> Self?     class func creationRequestForAssetFromVideo(atFileURL fileURL: URL) -> Self?     var placeholderForCreatedAsset: PHObjectPlaceholder? { get }     class func deleteAssets(_ assets: NSFastEnumeration)     convenience init(for asset: PHAsset)     class func forAsset(_ asset: PHAsset) -> Self     var creationDate: Date?     var location: CLLocation?     var isFavorite: Bool     var isHidden: Bool     var contentEditingOutput: PHContentEditingOutput?     func revertAssetContentToOriginal()     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHAssetChangeRequest : CVarArg { } extension PHAssetChangeRequest : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PHAssetChangeRequest.creationDate](https://developer.apple.com/documentation/photokit/phassetchangerequest/1624054-creationdate)

|  | Declaration |
| --- | --- |
| From | ``` var creationDate: NSDate? ``` |
| To | ``` var creationDate: Date? ``` |

Modified [PHAssetChangeRequest.creationRequestForAsset(from: UIImage) -> Self [class]](https://developer.apple.com/documentation/photokit/phassetchangerequest/1624060-creationrequestforassetfromimage)

|  | Declaration |
| --- | --- |
| From | ``` class func creationRequestForAssetFromImage(_ image: UIImage) -> Self ``` |
| To | ``` class func creationRequestForAsset(from image: UIImage) -> Self ``` |

Modified [PHAssetChangeRequest.creationRequestForAssetFromImage(atFileURL: URL) -> Self? [class]](https://developer.apple.com/documentation/photokit/phassetchangerequest/1624059-creationrequestforassetfromimage)

|  | Declaration |
| --- | --- |
| From | ``` class func creationRequestForAssetFromImageAtFileURL(_ fileURL: NSURL) -> Self? ``` |
| To | ``` class func creationRequestForAssetFromImage(atFileURL fileURL: URL) -> Self? ``` |

Modified [PHAssetChangeRequest.creationRequestForAssetFromVideo(atFileURL: URL) -> Self? [class]](https://developer.apple.com/documentation/photokit/phassetchangerequest/1624057-creationrequestforassetfromvideo)

|  | Declaration |
| --- | --- |
| From | ``` class func creationRequestForAssetFromVideoAtFileURL(_ fileURL: NSURL) -> Self? ``` |
| To | ``` class func creationRequestForAssetFromVideo(atFileURL fileURL: URL) -> Self? ``` |

Modified [PHAssetChangeRequest.init(for: PHAsset)](https://developer.apple.com/documentation/photokit/phassetchangerequest/1624050-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(forAsset asset: PHAsset) ``` |
| To | ``` convenience init(for asset: PHAsset) ``` |

Modified [PHAssetChangeRequest.isFavorite](https://developer.apple.com/documentation/photokit/phassetchangerequest/1624063-favorite)

|  | Declaration |
| --- | --- |
| From | ``` var favorite: Bool ``` |
| To | ``` var isFavorite: Bool ``` |

Modified [PHAssetChangeRequest.isHidden](https://developer.apple.com/documentation/photokit/phassetchangerequest/1624065-hidden)

|  | Declaration |
| --- | --- |
| From | ``` var hidden: Bool ``` |
| To | ``` var isHidden: Bool ``` |

Modified [PHAssetCollection](https://developer.apple.com/documentation/photokit/phassetcollection)

|  | Declaration |
| --- | --- |
| From | ``` class PHAssetCollection : PHCollection {     var assetCollectionType: PHAssetCollectionType { get }     var assetCollectionSubtype: PHAssetCollectionSubtype { get }     var estimatedAssetCount: Int { get }     var startDate: NSDate? { get }     var endDate: NSDate? { get }     var approximateLocation: CLLocation? { get }     var localizedLocationNames: [String] { get }     class func fetchAssetCollectionsWithLocalIdentifiers(_ identifiers: [String], options options: PHFetchOptions?) -> PHFetchResult     class func fetchAssetCollectionsWithType(_ type: PHAssetCollectionType, subtype subtype: PHAssetCollectionSubtype, options options: PHFetchOptions?) -> PHFetchResult     class func fetchAssetCollectionsContainingAsset(_ asset: PHAsset, withType type: PHAssetCollectionType, options options: PHFetchOptions?) -> PHFetchResult     class func fetchAssetCollectionsWithALAssetGroupURLs(_ assetGroupURLs: [NSURL], options options: PHFetchOptions?) -> PHFetchResult     class func fetchMomentsInMomentList(_ momentList: PHCollectionList, options options: PHFetchOptions?) -> PHFetchResult     class func fetchMomentsWithOptions(_ options: PHFetchOptions?) -> PHFetchResult     class func transientAssetCollectionWithAssets(_ assets: [PHAsset], title title: String?) -> PHAssetCollection     class func transientAssetCollectionWithAssetFetchResult(_ fetchResult: PHFetchResult, title title: String?) -> PHAssetCollection } ``` |
| To | ``` class PHAssetCollection : PHCollection {     var assetCollectionType: PHAssetCollectionType { get }     var assetCollectionSubtype: PHAssetCollectionSubtype { get }     var estimatedAssetCount: Int { get }     var startDate: Date? { get }     var endDate: Date? { get }     var approximateLocation: CLLocation? { get }     var localizedLocationNames: [String] { get }     class func fetchAssetCollections(withLocalIdentifiers identifiers: [String], options options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>     class func fetchAssetCollections(with type: PHAssetCollectionType, subtype subtype: PHAssetCollectionSubtype, options options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>     class func fetchAssetCollectionsContaining(_ asset: PHAsset, with type: PHAssetCollectionType, options options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>     class func fetchAssetCollections(withALAssetGroupURLs assetGroupURLs: [URL], options options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>     class func fetchMoments(inMomentList momentList: PHCollectionList, options options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>     class func fetchMoments(with options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>     class func transientAssetCollection(with assets: [PHAsset], title title: String?) -> PHAssetCollection     class func transientAssetCollection(withAssetFetchResult fetchResult: PHFetchResult<PHAsset>, title title: String?) -> PHAssetCollection } ``` |

Modified [PHAssetCollection.endDate](https://developer.apple.com/documentation/photokit/phassetcollection/1618517-enddate)

|  | Declaration |
| --- | --- |
| From | ``` var endDate: NSDate? { get } ``` |
| To | ``` var endDate: Date? { get } ``` |

Modified [PHAssetCollection.fetchAssetCollections(with: PHAssetCollectionType, subtype: PHAssetCollectionSubtype, options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection> [class]](https://developer.apple.com/documentation/photokit/phassetcollection/1618544-fetchassetcollectionswithtype)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAssetCollectionsWithType(_ type: PHAssetCollectionType, subtype subtype: PHAssetCollectionSubtype, options options: PHFetchOptions?) -> PHFetchResult ``` |
| To | ``` class func fetchAssetCollections(with type: PHAssetCollectionType, subtype subtype: PHAssetCollectionSubtype, options options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection> ``` |

Modified [PHAssetCollection.fetchAssetCollections(withALAssetGroupURLs: [URL], options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection> [class]](https://developer.apple.com/documentation/photokit/phassetcollection/1618533-fetchassetcollectionswithalasset)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAssetCollectionsWithALAssetGroupURLs(_ assetGroupURLs: [NSURL], options options: PHFetchOptions?) -> PHFetchResult ``` |
| To | ``` class func fetchAssetCollections(withALAssetGroupURLs assetGroupURLs: [URL], options options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection> ``` |

Modified [PHAssetCollection.fetchAssetCollections(withLocalIdentifiers: [String], options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection> [class]](https://developer.apple.com/documentation/photokit/phassetcollection/1618510-fetchassetcollections)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAssetCollectionsWithLocalIdentifiers(_ identifiers: [String], options options: PHFetchOptions?) -> PHFetchResult ``` |
| To | ``` class func fetchAssetCollections(withLocalIdentifiers identifiers: [String], options options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection> ``` |

Modified [PHAssetCollection.fetchAssetCollectionsContaining(_: PHAsset, with: PHAssetCollectionType, options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection> [class]](https://developer.apple.com/documentation/photokit/phassetcollection/1618530-fetchassetcollectionscontaininga)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchAssetCollectionsContainingAsset(_ asset: PHAsset, withType type: PHAssetCollectionType, options options: PHFetchOptions?) -> PHFetchResult ``` |
| To | ``` class func fetchAssetCollectionsContaining(_ asset: PHAsset, with type: PHAssetCollectionType, options options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection> ``` |

Modified [PHAssetCollection.fetchMoments(inMomentList: PHCollectionList, options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection> [class]](https://developer.apple.com/documentation/photokit/phassetcollection/1618522-fetchmoments)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchMomentsInMomentList(_ momentList: PHCollectionList, options options: PHFetchOptions?) -> PHFetchResult ``` |
| To | ``` class func fetchMoments(inMomentList momentList: PHCollectionList, options options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection> ``` |

Modified [PHAssetCollection.fetchMoments(with: PHFetchOptions?) -> PHFetchResult<PHAssetCollection> [class]](https://developer.apple.com/documentation/photokit/phassetcollection/1618531-fetchmoments)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchMomentsWithOptions(_ options: PHFetchOptions?) -> PHFetchResult ``` |
| To | ``` class func fetchMoments(with options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection> ``` |

Modified [PHAssetCollection.startDate](https://developer.apple.com/documentation/photokit/phassetcollection/1618514-startdate)

|  | Declaration |
| --- | --- |
| From | ``` var startDate: NSDate? { get } ``` |
| To | ``` var startDate: Date? { get } ``` |

Modified [PHAssetCollection.transientAssetCollection(with: [PHAsset], title: String?) -> PHAssetCollection [class]](https://developer.apple.com/documentation/photokit/phassetcollection/1618529-transientassetcollection)

|  | Declaration |
| --- | --- |
| From | ``` class func transientAssetCollectionWithAssets(_ assets: [PHAsset], title title: String?) -> PHAssetCollection ``` |
| To | ``` class func transientAssetCollection(with assets: [PHAsset], title title: String?) -> PHAssetCollection ``` |

Modified [PHAssetCollection.transientAssetCollection(withAssetFetchResult: PHFetchResult<PHAsset>, title: String?) -> PHAssetCollection [class]](https://developer.apple.com/documentation/photokit/phassetcollection/1618511-transientassetcollectionwithasse)

|  | Declaration |
| --- | --- |
| From | ``` class func transientAssetCollectionWithAssetFetchResult(_ fetchResult: PHFetchResult, title title: String?) -> PHAssetCollection ``` |
| To | ``` class func transientAssetCollection(withAssetFetchResult fetchResult: PHFetchResult<PHAsset>, title title: String?) -> PHAssetCollection ``` |

Modified [PHAssetCollectionChangeRequest](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHAssetCollectionChangeRequest : NSObject {     class func creationRequestForAssetCollectionWithTitle(_ title: String) -> Self     var placeholderForCreatedAssetCollection: PHObjectPlaceholder { get }     class func deleteAssetCollections(_ assetCollections: NSFastEnumeration)     convenience init?(forAssetCollection assetCollection: PHAssetCollection)     class func changeRequestForAssetCollection(_ assetCollection: PHAssetCollection) -> Self?     convenience init?(forAssetCollection assetCollection: PHAssetCollection, assets assets: PHFetchResult)     class func changeRequestForAssetCollection(_ assetCollection: PHAssetCollection, assets assets: PHFetchResult) -> Self?     var title: String     func addAssets(_ assets: NSFastEnumeration)     func insertAssets(_ assets: NSFastEnumeration, atIndexes indexes: NSIndexSet)     func removeAssets(_ assets: NSFastEnumeration)     func removeAssetsAtIndexes(_ indexes: NSIndexSet)     func replaceAssetsAtIndexes(_ indexes: NSIndexSet, withAssets assets: NSFastEnumeration)     func moveAssetsAtIndexes(_ fromIndexes: NSIndexSet, toIndex toIndex: Int) } ``` | -- |
| To | ``` class PHAssetCollectionChangeRequest : NSObject {     class func creationRequestForAssetCollection(withTitle title: String) -> Self     var placeholderForCreatedAssetCollection: PHObjectPlaceholder { get }     class func deleteAssetCollections(_ assetCollections: NSFastEnumeration)     convenience init?(for assetCollection: PHAssetCollection)     class func forAssetCollection(_ assetCollection: PHAssetCollection) -> Self?     convenience init?(for assetCollection: PHAssetCollection, assets assets: PHFetchResult<PHAsset>)     class func forAssetCollection(_ assetCollection: PHAssetCollection, assets assets: PHFetchResult<PHAsset>) -> Self?     var title: String     func addAssets(_ assets: NSFastEnumeration)     func insertAssets(_ assets: NSFastEnumeration, at indexes: IndexSet)     func removeAssets(_ assets: NSFastEnumeration)     func removeAssets(at indexes: IndexSet)     func replaceAssets(at indexes: IndexSet, withAssets assets: NSFastEnumeration)     func moveAssets(at fromIndexes: IndexSet, to toIndex: Int)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHAssetCollectionChangeRequest : CVarArg { } extension PHAssetCollectionChangeRequest : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PHAssetCollectionChangeRequest.creationRequestForAssetCollection(withTitle: String) -> Self [class]](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest/1619454-creationrequestforassetcollectio)

|  | Declaration |
| --- | --- |
| From | ``` class func creationRequestForAssetCollectionWithTitle(_ title: String) -> Self ``` |
| To | ``` class func creationRequestForAssetCollection(withTitle title: String) -> Self ``` |

Modified [PHAssetCollectionChangeRequest.init(for: PHAssetCollection)](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest/1619451-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init?(forAssetCollection assetCollection: PHAssetCollection) ``` |
| To | ``` convenience init?(for assetCollection: PHAssetCollection) ``` |

Modified [PHAssetCollectionChangeRequest.init(for: PHAssetCollection, assets: PHFetchResult<PHAsset>)](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest/1619445-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init?(forAssetCollection assetCollection: PHAssetCollection, assets assets: PHFetchResult) ``` |
| To | ``` convenience init?(for assetCollection: PHAssetCollection, assets assets: PHFetchResult<PHAsset>) ``` |

Modified [PHAssetCollectionChangeRequest.insertAssets(_: NSFastEnumeration, at: IndexSet)](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest/1619447-insertassets)

|  | Declaration |
| --- | --- |
| From | ``` func insertAssets(_ assets: NSFastEnumeration, atIndexes indexes: NSIndexSet) ``` |
| To | ``` func insertAssets(_ assets: NSFastEnumeration, at indexes: IndexSet) ``` |

Modified [PHAssetCollectionChangeRequest.moveAssets(at: IndexSet, to: Int)](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest/1619443-moveassets)

|  | Declaration |
| --- | --- |
| From | ``` func moveAssetsAtIndexes(_ fromIndexes: NSIndexSet, toIndex toIndex: Int) ``` |
| To | ``` func moveAssets(at fromIndexes: IndexSet, to toIndex: Int) ``` |

Modified [PHAssetCollectionChangeRequest.removeAssets(at: IndexSet)](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest/1619444-removeassets)

|  | Declaration |
| --- | --- |
| From | ``` func removeAssetsAtIndexes(_ indexes: NSIndexSet) ``` |
| To | ``` func removeAssets(at indexes: IndexSet) ``` |

Modified [PHAssetCollectionChangeRequest.replaceAssets(at: IndexSet, withAssets: NSFastEnumeration)](https://developer.apple.com/documentation/photokit/phassetcollectionchangerequest/1619448-replaceassets)

|  | Declaration |
| --- | --- |
| From | ``` func replaceAssetsAtIndexes(_ indexes: NSIndexSet, withAssets assets: NSFastEnumeration) ``` |
| To | ``` func replaceAssets(at indexes: IndexSet, withAssets assets: NSFastEnumeration) ``` |

Modified [PHAssetCollectionSubtype [enum]](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype)

|  | Declaration |
| --- | --- |
| From | ``` enum PHAssetCollectionSubtype : Int {     case AlbumRegular     case AlbumSyncedEvent     case AlbumSyncedFaces     case AlbumSyncedAlbum     case AlbumImported     case AlbumMyPhotoStream     case AlbumCloudShared     case SmartAlbumGeneric     case SmartAlbumPanoramas     case SmartAlbumVideos     case SmartAlbumFavorites     case SmartAlbumTimelapses     case SmartAlbumAllHidden     case SmartAlbumRecentlyAdded     case SmartAlbumBursts     case SmartAlbumSlomoVideos     case SmartAlbumUserLibrary     case SmartAlbumSelfPortraits     case SmartAlbumScreenshots     case Any } ``` |
| To | ``` enum PHAssetCollectionSubtype : Int {     case albumRegular     case albumSyncedEvent     case albumSyncedFaces     case albumSyncedAlbum     case albumImported     case albumMyPhotoStream     case albumCloudShared     case smartAlbumGeneric     case smartAlbumPanoramas     case smartAlbumVideos     case smartAlbumFavorites     case smartAlbumTimelapses     case smartAlbumAllHidden     case smartAlbumRecentlyAdded     case smartAlbumBursts     case smartAlbumSlomoVideos     case smartAlbumUserLibrary     case smartAlbumSelfPortraits     case smartAlbumScreenshots     case any } ``` |

Modified [PHAssetCollectionSubtype.albumCloudShared](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/albumcloudshared)

|  | Declaration |
| --- | --- |
| From | ``` case AlbumCloudShared ``` |
| To | ``` case albumCloudShared ``` |

Modified [PHAssetCollectionSubtype.albumImported](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/albumimported)

|  | Declaration |
| --- | --- |
| From | ``` case AlbumImported ``` |
| To | ``` case albumImported ``` |

Modified [PHAssetCollectionSubtype.albumMyPhotoStream](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/albummyphotostream)

|  | Declaration |
| --- | --- |
| From | ``` case AlbumMyPhotoStream ``` |
| To | ``` case albumMyPhotoStream ``` |

Modified [PHAssetCollectionSubtype.albumRegular](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/albumregular)

|  | Declaration |
| --- | --- |
| From | ``` case AlbumRegular ``` |
| To | ``` case albumRegular ``` |

Modified [PHAssetCollectionSubtype.albumSyncedAlbum](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/albumsyncedalbum)

|  | Declaration |
| --- | --- |
| From | ``` case AlbumSyncedAlbum ``` |
| To | ``` case albumSyncedAlbum ``` |

Modified [PHAssetCollectionSubtype.albumSyncedEvent](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/albumsyncedevent)

|  | Declaration |
| --- | --- |
| From | ``` case AlbumSyncedEvent ``` |
| To | ``` case albumSyncedEvent ``` |

Modified [PHAssetCollectionSubtype.albumSyncedFaces](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/phassetcollectionsubtypealbumsyncedfaces)

|  | Declaration |
| --- | --- |
| From | ``` case AlbumSyncedFaces ``` |
| To | ``` case albumSyncedFaces ``` |

Modified [PHAssetCollectionSubtype.any](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/phassetcollectionsubtypeany)

|  | Declaration |
| --- | --- |
| From | ``` case Any ``` |
| To | ``` case any ``` |

Modified [PHAssetCollectionSubtype.smartAlbumAllHidden](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/phassetcollectionsubtypesmartalbumallhidden)

|  | Declaration |
| --- | --- |
| From | ``` case SmartAlbumAllHidden ``` |
| To | ``` case smartAlbumAllHidden ``` |

Modified [PHAssetCollectionSubtype.smartAlbumBursts](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/smartalbumbursts)

|  | Declaration |
| --- | --- |
| From | ``` case SmartAlbumBursts ``` |
| To | ``` case smartAlbumBursts ``` |

Modified [PHAssetCollectionSubtype.smartAlbumFavorites](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/phassetcollectionsubtypesmartalbumfavorites)

|  | Declaration |
| --- | --- |
| From | ``` case SmartAlbumFavorites ``` |
| To | ``` case smartAlbumFavorites ``` |

Modified [PHAssetCollectionSubtype.smartAlbumGeneric](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/smartalbumgeneric)

|  | Declaration |
| --- | --- |
| From | ``` case SmartAlbumGeneric ``` |
| To | ``` case smartAlbumGeneric ``` |

Modified [PHAssetCollectionSubtype.smartAlbumPanoramas](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/phassetcollectionsubtypesmartalbumpanoramas)

|  | Declaration |
| --- | --- |
| From | ``` case SmartAlbumPanoramas ``` |
| To | ``` case smartAlbumPanoramas ``` |

Modified [PHAssetCollectionSubtype.smartAlbumRecentlyAdded](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/phassetcollectionsubtypesmartalbumrecentlyadded)

|  | Declaration |
| --- | --- |
| From | ``` case SmartAlbumRecentlyAdded ``` |
| To | ``` case smartAlbumRecentlyAdded ``` |

Modified [PHAssetCollectionSubtype.smartAlbumScreenshots](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/phassetcollectionsubtypesmartalbumscreenshots)

|  | Declaration |
| --- | --- |
| From | ``` case SmartAlbumScreenshots ``` |
| To | ``` case smartAlbumScreenshots ``` |

Modified [PHAssetCollectionSubtype.smartAlbumSelfPortraits](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/smartalbumselfportraits)

|  | Declaration |
| --- | --- |
| From | ``` case SmartAlbumSelfPortraits ``` |
| To | ``` case smartAlbumSelfPortraits ``` |

Modified [PHAssetCollectionSubtype.smartAlbumSlomoVideos](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/phassetcollectionsubtypesmartalbumslomovideos)

|  | Declaration |
| --- | --- |
| From | ``` case SmartAlbumSlomoVideos ``` |
| To | ``` case smartAlbumSlomoVideos ``` |

Modified [PHAssetCollectionSubtype.smartAlbumTimelapses](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/smartalbumtimelapses)

|  | Declaration |
| --- | --- |
| From | ``` case SmartAlbumTimelapses ``` |
| To | ``` case smartAlbumTimelapses ``` |

Modified [PHAssetCollectionSubtype.smartAlbumUserLibrary](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/smartalbumuserlibrary)

|  | Declaration |
| --- | --- |
| From | ``` case SmartAlbumUserLibrary ``` |
| To | ``` case smartAlbumUserLibrary ``` |

Modified [PHAssetCollectionSubtype.smartAlbumVideos](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/smartalbumvideos)

|  | Declaration |
| --- | --- |
| From | ``` case SmartAlbumVideos ``` |
| To | ``` case smartAlbumVideos ``` |

Modified [PHAssetCollectionType [enum]](https://developer.apple.com/documentation/photokit/phassetcollectiontype)

|  | Declaration |
| --- | --- |
| From | ``` enum PHAssetCollectionType : Int {     case Album     case SmartAlbum     case Moment } ``` |
| To | ``` enum PHAssetCollectionType : Int {     case album     case smartAlbum     case moment } ``` |

Modified [PHAssetCollectionType.album](https://developer.apple.com/documentation/photokit/phassetcollectiontype/album)

|  | Declaration |
| --- | --- |
| From | ``` case Album ``` |
| To | ``` case album ``` |

Modified [PHAssetCollectionType.moment](https://developer.apple.com/documentation/photokit/phassetcollectiontype/phassetcollectiontypemoment)

|  | Declaration |
| --- | --- |
| From | ``` case Moment ``` |
| To | ``` case moment ``` |

Modified [PHAssetCollectionType.smartAlbum](https://developer.apple.com/documentation/photokit/phassetcollectiontype/phassetcollectiontypesmartalbum)

|  | Declaration |
| --- | --- |
| From | ``` case SmartAlbum ``` |
| To | ``` case smartAlbum ``` |

Modified [PHAssetCreationRequest](https://developer.apple.com/documentation/photokit/phassetcreationrequest)

|  | Declaration |
| --- | --- |
| From | ``` class PHAssetCreationRequest : PHAssetChangeRequest {     class func creationRequestForAsset() -> Self     class func supportsAssetResourceTypes(_ types: [NSNumber]) -> Bool     func addResourceWithType(_ type: PHAssetResourceType, fileURL fileURL: NSURL, options options: PHAssetResourceCreationOptions?)     func addResourceWithType(_ type: PHAssetResourceType, data data: NSData, options options: PHAssetResourceCreationOptions?) } ``` |
| To | ``` class PHAssetCreationRequest : PHAssetChangeRequest {     class func forAsset() -> Self     class func supportsAssetResourceTypes(_ types: [NSNumber]) -> Bool     func addResource(with type: PHAssetResourceType, fileURL fileURL: URL, options options: PHAssetResourceCreationOptions?)     func addResource(with type: PHAssetResourceType, data data: Data, options options: PHAssetResourceCreationOptions?) } ``` |

Modified [PHAssetCreationRequest.addResource(with: PHAssetResourceType, data: Data, options: PHAssetResourceCreationOptions?)](https://developer.apple.com/documentation/photokit/phassetcreationrequest/1622684-addresourcewithtype)

|  | Declaration |
| --- | --- |
| From | ``` func addResourceWithType(_ type: PHAssetResourceType, data data: NSData, options options: PHAssetResourceCreationOptions?) ``` |
| To | ``` func addResource(with type: PHAssetResourceType, data data: Data, options options: PHAssetResourceCreationOptions?) ``` |

Modified [PHAssetCreationRequest.addResource(with: PHAssetResourceType, fileURL: URL, options: PHAssetResourceCreationOptions?)](https://developer.apple.com/documentation/photokit/phassetcreationrequest/1622681-addresourcewithtype)

|  | Declaration |
| --- | --- |
| From | ``` func addResourceWithType(_ type: PHAssetResourceType, fileURL fileURL: NSURL, options options: PHAssetResourceCreationOptions?) ``` |
| To | ``` func addResource(with type: PHAssetResourceType, fileURL fileURL: URL, options options: PHAssetResourceCreationOptions?) ``` |

Modified [PHAssetCreationRequest.forAsset() -> Self [class]](https://developer.apple.com/documentation/photokit/phassetcreationrequest/1622682-creationrequestforasset)

|  | Declaration |
| --- | --- |
| From | ``` class func creationRequestForAsset() -> Self ``` |
| To | ``` class func forAsset() -> Self ``` |

Modified [PHAssetEditOperation [enum]](https://developer.apple.com/documentation/photokit/phasseteditoperation)

|  | Declaration |
| --- | --- |
| From | ``` enum PHAssetEditOperation : Int {     case Delete     case Content     case Properties } ``` |
| To | ``` enum PHAssetEditOperation : Int {     case delete     case content     case properties } ``` |

Modified [PHAssetEditOperation.content](https://developer.apple.com/documentation/photokit/phasseteditoperation/content)

|  | Declaration |
| --- | --- |
| From | ``` case Content ``` |
| To | ``` case content ``` |

Modified [PHAssetEditOperation.delete](https://developer.apple.com/documentation/photokit/phasseteditoperation/delete)

|  | Declaration |
| --- | --- |
| From | ``` case Delete ``` |
| To | ``` case delete ``` |

Modified [PHAssetEditOperation.properties](https://developer.apple.com/documentation/photokit/phasseteditoperation/properties)

|  | Declaration |
| --- | --- |
| From | ``` case Properties ``` |
| To | ``` case properties ``` |

Modified [PHAssetMediaSubtype [struct]](https://developer.apple.com/documentation/photokit/phassetmediasubtype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct PHAssetMediaSubtype : OptionSetType {     init(rawValue rawValue: UInt)     static var None: PHAssetMediaSubtype { get }     static var PhotoPanorama: PHAssetMediaSubtype { get }     static var PhotoHDR: PHAssetMediaSubtype { get }     static var PhotoScreenshot: PHAssetMediaSubtype { get }     static var PhotoLive: PHAssetMediaSubtype { get }     static var VideoStreamed: PHAssetMediaSubtype { get }     static var VideoHighFrameRate: PHAssetMediaSubtype { get }     static var VideoTimelapse: PHAssetMediaSubtype { get } } ``` | OptionSetType |
| To | ``` struct PHAssetMediaSubtype : OptionSet {     init(rawValue rawValue: UInt)     static var none: PHAssetMediaSubtype { get }     static var photoPanorama: PHAssetMediaSubtype { get }     static var photoHDR: PHAssetMediaSubtype { get }     static var photoScreenshot: PHAssetMediaSubtype { get }     static var photoLive: PHAssetMediaSubtype { get }     static var videoStreamed: PHAssetMediaSubtype { get }     static var videoHighFrameRate: PHAssetMediaSubtype { get }     static var videoTimelapse: PHAssetMediaSubtype { get }     func intersect(_ other: PHAssetMediaSubtype) -> PHAssetMediaSubtype     func exclusiveOr(_ other: PHAssetMediaSubtype) -> PHAssetMediaSubtype     mutating func unionInPlace(_ other: PHAssetMediaSubtype)     mutating func intersectInPlace(_ other: PHAssetMediaSubtype)     mutating func exclusiveOrInPlace(_ other: PHAssetMediaSubtype)     func isSubsetOf(_ other: PHAssetMediaSubtype) -> Bool     func isDisjointWith(_ other: PHAssetMediaSubtype) -> Bool     func isSupersetOf(_ other: PHAssetMediaSubtype) -> Bool     mutating func subtractInPlace(_ other: PHAssetMediaSubtype)     func isStrictSupersetOf(_ other: PHAssetMediaSubtype) -> Bool     func isStrictSubsetOf(_ other: PHAssetMediaSubtype) -> Bool } extension PHAssetMediaSubtype {     func union(_ other: PHAssetMediaSubtype) -> PHAssetMediaSubtype     func intersection(_ other: PHAssetMediaSubtype) -> PHAssetMediaSubtype     func symmetricDifference(_ other: PHAssetMediaSubtype) -> PHAssetMediaSubtype } extension PHAssetMediaSubtype {     func contains(_ member: PHAssetMediaSubtype) -> Bool     mutating func insert(_ newMember: PHAssetMediaSubtype) -> (inserted: Bool, memberAfterInsert: PHAssetMediaSubtype)     mutating func remove(_ member: PHAssetMediaSubtype) -> PHAssetMediaSubtype?     mutating func update(with newMember: PHAssetMediaSubtype) -> PHAssetMediaSubtype? } extension PHAssetMediaSubtype {     convenience init()     mutating func formUnion(_ other: PHAssetMediaSubtype)     mutating func formIntersection(_ other: PHAssetMediaSubtype)     mutating func formSymmetricDifference(_ other: PHAssetMediaSubtype) } extension PHAssetMediaSubtype {     convenience init<S : Sequence where S.Iterator.Element == PHAssetMediaSubtype>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: PHAssetMediaSubtype...)     mutating func subtract(_ other: PHAssetMediaSubtype)     func isSubset(of other: PHAssetMediaSubtype) -> Bool     func isSuperset(of other: PHAssetMediaSubtype) -> Bool     func isDisjoint(with other: PHAssetMediaSubtype) -> Bool     func subtracting(_ other: PHAssetMediaSubtype) -> PHAssetMediaSubtype     var isEmpty: Bool { get }     func isStrictSuperset(of other: PHAssetMediaSubtype) -> Bool     func isStrictSubset(of other: PHAssetMediaSubtype) -> Bool } ``` | OptionSet |

Modified [PHAssetMediaSubtype.photoHDR](https://developer.apple.com/documentation/photokit/phassetmediasubtype/1518631-photohdr)

|  | Declaration |
| --- | --- |
| From | ``` static var PhotoHDR: PHAssetMediaSubtype { get } ``` |
| To | ``` static var photoHDR: PHAssetMediaSubtype { get } ``` |

Modified [PHAssetMediaSubtype.photoLive](https://developer.apple.com/documentation/photokit/phassetmediasubtype/1614007-photolive)

|  | Declaration |
| --- | --- |
| From | ``` static var PhotoLive: PHAssetMediaSubtype { get } ``` |
| To | ``` static var photoLive: PHAssetMediaSubtype { get } ``` |

Modified [PHAssetMediaSubtype.photoPanorama](https://developer.apple.com/documentation/photokit/phassetmediasubtype/phassetmediasubtypephotopanorama)

|  | Declaration |
| --- | --- |
| From | ``` static var PhotoPanorama: PHAssetMediaSubtype { get } ``` |
| To | ``` static var photoPanorama: PHAssetMediaSubtype { get } ``` |

Modified [PHAssetMediaSubtype.photoScreenshot](https://developer.apple.com/documentation/photokit/phassetmediasubtype/1518653-photoscreenshot)

|  | Declaration |
| --- | --- |
| From | ``` static var PhotoScreenshot: PHAssetMediaSubtype { get } ``` |
| To | ``` static var photoScreenshot: PHAssetMediaSubtype { get } ``` |

Modified [PHAssetMediaSubtype.videoHighFrameRate](https://developer.apple.com/documentation/photokit/phassetmediasubtype/phassetmediasubtypevideohighframerate)

|  | Declaration |
| --- | --- |
| From | ``` static var VideoHighFrameRate: PHAssetMediaSubtype { get } ``` |
| To | ``` static var videoHighFrameRate: PHAssetMediaSubtype { get } ``` |

Modified [PHAssetMediaSubtype.videoStreamed](https://developer.apple.com/documentation/photokit/phassetmediasubtype/1518637-videostreamed)

|  | Declaration |
| --- | --- |
| From | ``` static var VideoStreamed: PHAssetMediaSubtype { get } ``` |
| To | ``` static var videoStreamed: PHAssetMediaSubtype { get } ``` |

Modified [PHAssetMediaSubtype.videoTimelapse](https://developer.apple.com/documentation/photokit/phassetmediasubtype/1518665-videotimelapse)

|  | Declaration |
| --- | --- |
| From | ``` static var VideoTimelapse: PHAssetMediaSubtype { get } ``` |
| To | ``` static var videoTimelapse: PHAssetMediaSubtype { get } ``` |

Modified [PHAssetMediaType [enum]](https://developer.apple.com/documentation/photokit/phassetmediatype)

|  | Declaration |
| --- | --- |
| From | ``` enum PHAssetMediaType : Int {     case Unknown     case Image     case Video     case Audio } ``` |
| To | ``` enum PHAssetMediaType : Int {     case unknown     case image     case video     case audio } ``` |

Modified [PHAssetMediaType.audio](https://developer.apple.com/documentation/photokit/phassetmediatype/phassetmediatypeaudio)

|  | Declaration |
| --- | --- |
| From | ``` case Audio ``` |
| To | ``` case audio ``` |

Modified [PHAssetMediaType.image](https://developer.apple.com/documentation/photokit/phassetmediatype/image)

|  | Declaration |
| --- | --- |
| From | ``` case Image ``` |
| To | ``` case image ``` |

Modified [PHAssetMediaType.unknown](https://developer.apple.com/documentation/photokit/phassetmediatype/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [PHAssetMediaType.video](https://developer.apple.com/documentation/photokit/phassetmediatype/phassetmediatypevideo)

|  | Declaration |
| --- | --- |
| From | ``` case Video ``` |
| To | ``` case video ``` |

Modified [PHAssetResource](https://developer.apple.com/documentation/photokit/phassetresource)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHAssetResource : NSObject {     var type: PHAssetResourceType { get }     var assetLocalIdentifier: String { get }     var uniformTypeIdentifier: String { get }     var originalFilename: String { get }     class func assetResourcesForAsset(_ asset: PHAsset) -> [PHAssetResource]     class func assetResourcesForLivePhoto(_ livePhoto: PHLivePhoto) -> [PHAssetResource] } ``` | -- |
| To | ``` class PHAssetResource : NSObject {     var type: PHAssetResourceType { get }     var assetLocalIdentifier: String { get }     var uniformTypeIdentifier: String { get }     var originalFilename: String { get }     class func assetResources(for asset: PHAsset) -> [PHAssetResource]     class func assetResources(for livePhoto: PHLivePhoto) -> [PHAssetResource]     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHAssetResource : CVarArg { } extension PHAssetResource : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PHAssetResource.assetResources(for: PHLivePhoto) -> [PHAssetResource] [class]](https://developer.apple.com/documentation/photokit/phassetresource/1623984-assetresourcesforlivephoto)

|  | Declaration |
| --- | --- |
| From | ``` class func assetResourcesForLivePhoto(_ livePhoto: PHLivePhoto) -> [PHAssetResource] ``` |
| To | ``` class func assetResources(for livePhoto: PHLivePhoto) -> [PHAssetResource] ``` |

Modified [PHAssetResource.assetResources(for: PHAsset) -> [PHAssetResource] [class]](https://developer.apple.com/documentation/photokit/phassetresource/1623988-assetresourcesforasset)

|  | Declaration |
| --- | --- |
| From | ``` class func assetResourcesForAsset(_ asset: PHAsset) -> [PHAssetResource] ``` |
| To | ``` class func assetResources(for asset: PHAsset) -> [PHAssetResource] ``` |

Modified [PHAssetResourceCreationOptions](https://developer.apple.com/documentation/photokit/phassetresourcecreationoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHAssetResourceCreationOptions : NSObject, NSCopying {     var originalFilename: String?     var uniformTypeIdentifier: String?     var shouldMoveFile: Bool } ``` | NSCopying |
| To | ``` class PHAssetResourceCreationOptions : NSObject, NSCopying {     var originalFilename: String?     var uniformTypeIdentifier: String?     var shouldMoveFile: Bool     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHAssetResourceCreationOptions : CVarArg { } extension PHAssetResourceCreationOptions : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [PHAssetResourceManager](https://developer.apple.com/documentation/photokit/phassetresourcemanager)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHAssetResourceManager : NSObject {     class func defaultManager() -> PHAssetResourceManager     func requestDataForAssetResource(_ resource: PHAssetResource, options options: PHAssetResourceRequestOptions?, dataReceivedHandler handler: (NSData) -> Void, completionHandler completionHandler: (NSError?) -> Void) -> PHAssetResourceDataRequestID     func writeDataForAssetResource(_ resource: PHAssetResource, toFile fileURL: NSURL, options options: PHAssetResourceRequestOptions?, completionHandler completionHandler: (NSError?) -> Void)     func cancelDataRequest(_ requestID: PHAssetResourceDataRequestID) } ``` | -- |
| To | ``` class PHAssetResourceManager : NSObject {     class func `default`() -> PHAssetResourceManager     func requestData(for resource: PHAssetResource, options options: PHAssetResourceRequestOptions?, dataReceivedHandler handler: @escaping (Data) -> Swift.Void, completionHandler completionHandler: @escaping (Error?) -> Swift.Void) -> PHAssetResourceDataRequestID     func writeData(for resource: PHAssetResource, toFile fileURL: URL, options options: PHAssetResourceRequestOptions?, completionHandler completionHandler: @escaping (Error?) -> Swift.Void)     func cancelDataRequest(_ requestID: PHAssetResourceDataRequestID)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHAssetResourceManager : CVarArg { } extension PHAssetResourceManager : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PHAssetResourceManager.default() [class]](https://developer.apple.com/documentation/photokit/phassetresourcemanager/1616270-defaultmanager)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultManager() -> PHAssetResourceManager ``` |
| To | ``` class func `default`() -> PHAssetResourceManager ``` |

Modified [PHAssetResourceManager.requestData(for: PHAssetResource, options: PHAssetResourceRequestOptions?, dataReceivedHandler: (Data) -> Swift.Void, completionHandler: (Error?) -> Swift.Void) -> PHAssetResourceDataRequestID](https://developer.apple.com/documentation/photokit/phassetresourcemanager/1616279-requestdataforassetresource)

|  | Declaration |
| --- | --- |
| From | ``` func requestDataForAssetResource(_ resource: PHAssetResource, options options: PHAssetResourceRequestOptions?, dataReceivedHandler handler: (NSData) -> Void, completionHandler completionHandler: (NSError?) -> Void) -> PHAssetResourceDataRequestID ``` |
| To | ``` func requestData(for resource: PHAssetResource, options options: PHAssetResourceRequestOptions?, dataReceivedHandler handler: @escaping (Data) -> Swift.Void, completionHandler completionHandler: @escaping (Error?) -> Swift.Void) -> PHAssetResourceDataRequestID ``` |

Modified [PHAssetResourceManager.writeData(for: PHAssetResource, toFile: URL, options: PHAssetResourceRequestOptions?, completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/photokit/phassetresourcemanager/1616280-writedataforassetresource)

|  | Declaration |
| --- | --- |
| From | ``` func writeDataForAssetResource(_ resource: PHAssetResource, toFile fileURL: NSURL, options options: PHAssetResourceRequestOptions?, completionHandler completionHandler: (NSError?) -> Void) ``` |
| To | ``` func writeData(for resource: PHAssetResource, toFile fileURL: URL, options options: PHAssetResourceRequestOptions?, completionHandler completionHandler: @escaping (Error?) -> Swift.Void) ``` |

Modified [PHAssetResourceRequestOptions](https://developer.apple.com/documentation/photokit/phassetresourcerequestoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHAssetResourceRequestOptions : NSObject, NSCopying {     var networkAccessAllowed: Bool     var progressHandler: PHAssetResourceProgressHandler? } ``` | NSCopying |
| To | ``` class PHAssetResourceRequestOptions : NSObject, NSCopying {     var isNetworkAccessAllowed: Bool     var progressHandler: Photos.PHAssetResourceProgressHandler?     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHAssetResourceRequestOptions : CVarArg { } extension PHAssetResourceRequestOptions : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [PHAssetResourceRequestOptions.isNetworkAccessAllowed](https://developer.apple.com/documentation/photokit/phassetresourcerequestoptions/1616275-networkaccessallowed)

|  | Declaration |
| --- | --- |
| From | ``` var networkAccessAllowed: Bool ``` |
| To | ``` var isNetworkAccessAllowed: Bool ``` |

Modified [PHAssetResourceRequestOptions.progressHandler](https://developer.apple.com/documentation/photokit/phassetresourcerequestoptions/1616272-progresshandler)

|  | Declaration |
| --- | --- |
| From | ``` var progressHandler: PHAssetResourceProgressHandler? ``` |
| To | ``` var progressHandler: Photos.PHAssetResourceProgressHandler? ``` |

Modified [PHAssetResourceType [enum]](https://developer.apple.com/documentation/photokit/phassetresourcetype)

|  | Declaration |
| --- | --- |
| From | ``` enum PHAssetResourceType : Int {     case Photo     case Video     case Audio     case AlternatePhoto     case FullSizePhoto     case FullSizeVideo     case AdjustmentData     case AdjustmentBasePhoto     case PairedVideo } ``` |
| To | ``` enum PHAssetResourceType : Int {     case photo     case video     case audio     case alternatePhoto     case fullSizePhoto     case fullSizeVideo     case adjustmentData     case adjustmentBasePhoto     case pairedVideo     case fullSizePairedVideo     case adjustmentBasePairedVideo } ``` |

Modified [PHAssetResourceType.adjustmentBasePhoto](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypeadjustmentbasephoto)

|  | Declaration |
| --- | --- |
| From | ``` case AdjustmentBasePhoto ``` |
| To | ``` case adjustmentBasePhoto ``` |

Modified [PHAssetResourceType.adjustmentData](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypeadjustmentdata)

|  | Declaration |
| --- | --- |
| From | ``` case AdjustmentData ``` |
| To | ``` case adjustmentData ``` |

Modified [PHAssetResourceType.alternatePhoto](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypealternatephoto)

|  | Declaration |
| --- | --- |
| From | ``` case AlternatePhoto ``` |
| To | ``` case alternatePhoto ``` |

Modified [PHAssetResourceType.audio](https://developer.apple.com/documentation/photokit/phassetresourcetype/audio)

|  | Declaration |
| --- | --- |
| From | ``` case Audio ``` |
| To | ``` case audio ``` |

Modified [PHAssetResourceType.fullSizePhoto](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypefullsizephoto)

|  | Declaration |
| --- | --- |
| From | ``` case FullSizePhoto ``` |
| To | ``` case fullSizePhoto ``` |

Modified [PHAssetResourceType.fullSizeVideo](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypefullsizevideo)

|  | Declaration |
| --- | --- |
| From | ``` case FullSizeVideo ``` |
| To | ``` case fullSizeVideo ``` |

Modified [PHAssetResourceType.pairedVideo](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypepairedvideo)

|  | Declaration |
| --- | --- |
| From | ``` case PairedVideo ``` |
| To | ``` case pairedVideo ``` |

Modified [PHAssetResourceType.photo](https://developer.apple.com/documentation/photokit/phassetresourcetype/photo)

|  | Declaration |
| --- | --- |
| From | ``` case Photo ``` |
| To | ``` case photo ``` |

Modified [PHAssetResourceType.video](https://developer.apple.com/documentation/photokit/phassetresourcetype/video)

|  | Declaration |
| --- | --- |
| From | ``` case Video ``` |
| To | ``` case video ``` |

Modified [PHAssetSourceType [struct]](https://developer.apple.com/documentation/photokit/phassetsourcetype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct PHAssetSourceType : OptionSetType {     init(rawValue rawValue: UInt)     static var TypeNone: PHAssetSourceType { get }     static var TypeUserLibrary: PHAssetSourceType { get }     static var TypeCloudShared: PHAssetSourceType { get }     static var TypeiTunesSynced: PHAssetSourceType { get } } ``` | OptionSetType |
| To | ``` struct PHAssetSourceType : OptionSet {     init(rawValue rawValue: UInt)     static var typeNone: PHAssetSourceType { get }     static var typeUserLibrary: PHAssetSourceType { get }     static var typeCloudShared: PHAssetSourceType { get }     static var typeiTunesSynced: PHAssetSourceType { get }     func intersect(_ other: PHAssetSourceType) -> PHAssetSourceType     func exclusiveOr(_ other: PHAssetSourceType) -> PHAssetSourceType     mutating func unionInPlace(_ other: PHAssetSourceType)     mutating func intersectInPlace(_ other: PHAssetSourceType)     mutating func exclusiveOrInPlace(_ other: PHAssetSourceType)     func isSubsetOf(_ other: PHAssetSourceType) -> Bool     func isDisjointWith(_ other: PHAssetSourceType) -> Bool     func isSupersetOf(_ other: PHAssetSourceType) -> Bool     mutating func subtractInPlace(_ other: PHAssetSourceType)     func isStrictSupersetOf(_ other: PHAssetSourceType) -> Bool     func isStrictSubsetOf(_ other: PHAssetSourceType) -> Bool } extension PHAssetSourceType {     func union(_ other: PHAssetSourceType) -> PHAssetSourceType     func intersection(_ other: PHAssetSourceType) -> PHAssetSourceType     func symmetricDifference(_ other: PHAssetSourceType) -> PHAssetSourceType } extension PHAssetSourceType {     func contains(_ member: PHAssetSourceType) -> Bool     mutating func insert(_ newMember: PHAssetSourceType) -> (inserted: Bool, memberAfterInsert: PHAssetSourceType)     mutating func remove(_ member: PHAssetSourceType) -> PHAssetSourceType?     mutating func update(with newMember: PHAssetSourceType) -> PHAssetSourceType? } extension PHAssetSourceType {     convenience init()     mutating func formUnion(_ other: PHAssetSourceType)     mutating func formIntersection(_ other: PHAssetSourceType)     mutating func formSymmetricDifference(_ other: PHAssetSourceType) } extension PHAssetSourceType {     convenience init<S : Sequence where S.Iterator.Element == PHAssetSourceType>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: PHAssetSourceType...)     mutating func subtract(_ other: PHAssetSourceType)     func isSubset(of other: PHAssetSourceType) -> Bool     func isSuperset(of other: PHAssetSourceType) -> Bool     func isDisjoint(with other: PHAssetSourceType) -> Bool     func subtracting(_ other: PHAssetSourceType) -> PHAssetSourceType     var isEmpty: Bool { get }     func isStrictSuperset(of other: PHAssetSourceType) -> Bool     func isStrictSubset(of other: PHAssetSourceType) -> Bool } ``` | OptionSet |

Modified [PHAssetSourceType.typeCloudShared](https://developer.apple.com/documentation/photokit/phassetsourcetype/phassetsourcetypecloudshared)

|  | Declaration |
| --- | --- |
| From | ``` static var TypeCloudShared: PHAssetSourceType { get } ``` |
| To | ``` static var typeCloudShared: PHAssetSourceType { get } ``` |

Modified [PHAssetSourceType.typeiTunesSynced](https://developer.apple.com/documentation/photokit/phassetsourcetype/phassetsourcetypeitunessynced)

|  | Declaration |
| --- | --- |
| From | ``` static var TypeiTunesSynced: PHAssetSourceType { get } ``` |
| To | ``` static var typeiTunesSynced: PHAssetSourceType { get } ``` |

Modified [PHAssetSourceType.typeUserLibrary](https://developer.apple.com/documentation/photokit/phassetsourcetype/phassetsourcetypeuserlibrary)

|  | Declaration |
| --- | --- |
| From | ``` static var TypeUserLibrary: PHAssetSourceType { get } ``` |
| To | ``` static var typeUserLibrary: PHAssetSourceType { get } ``` |

Modified [PHAuthorizationStatus [enum]](https://developer.apple.com/documentation/photokit/phauthorizationstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum PHAuthorizationStatus : Int {     case NotDetermined     case Restricted     case Denied     case Authorized } ``` |
| To | ``` enum PHAuthorizationStatus : Int {     case notDetermined     case restricted     case denied     case authorized } ``` |

Modified [PHAuthorizationStatus.authorized](https://developer.apple.com/documentation/photokit/phauthorizationstatus/authorized)

|  | Declaration |
| --- | --- |
| From | ``` case Authorized ``` |
| To | ``` case authorized ``` |

Modified [PHAuthorizationStatus.denied](https://developer.apple.com/documentation/photokit/phauthorizationstatus/phauthorizationstatusdenied)

|  | Declaration |
| --- | --- |
| From | ``` case Denied ``` |
| To | ``` case denied ``` |

Modified [PHAuthorizationStatus.notDetermined](https://developer.apple.com/documentation/photokit/phauthorizationstatus/notdetermined)

|  | Declaration |
| --- | --- |
| From | ``` case NotDetermined ``` |
| To | ``` case notDetermined ``` |

Modified [PHAuthorizationStatus.restricted](https://developer.apple.com/documentation/photokit/phauthorizationstatus/restricted)

|  | Declaration |
| --- | --- |
| From | ``` case Restricted ``` |
| To | ``` case restricted ``` |

Modified [PHCachingImageManager](https://developer.apple.com/documentation/photokit/phcachingimagemanager)

|  | Declaration |
| --- | --- |
| From | ``` class PHCachingImageManager : PHImageManager {     var allowsCachingHighQualityImages: Bool     func startCachingImagesForAssets(_ assets: [PHAsset], targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions?)     func stopCachingImagesForAssets(_ assets: [PHAsset], targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions?)     func stopCachingImagesForAllAssets() } ``` |
| To | ``` class PHCachingImageManager : PHImageManager {     var allowsCachingHighQualityImages: Bool     func startCachingImages(for assets: [PHAsset], targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions?)     func stopCachingImages(for assets: [PHAsset], targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions?)     func stopCachingImagesForAllAssets() } ``` |

Modified [PHCachingImageManager.startCachingImages(for: [PHAsset], targetSize: CGSize, contentMode: PHImageContentMode, options: PHImageRequestOptions?)](https://developer.apple.com/documentation/photokit/phcachingimagemanager/1616986-startcachingimagesforassets)

|  | Declaration |
| --- | --- |
| From | ``` func startCachingImagesForAssets(_ assets: [PHAsset], targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions?) ``` |
| To | ``` func startCachingImages(for assets: [PHAsset], targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions?) ``` |

Modified [PHCachingImageManager.stopCachingImages(for: [PHAsset], targetSize: CGSize, contentMode: PHImageContentMode, options: PHImageRequestOptions?)](https://developer.apple.com/documentation/photokit/phcachingimagemanager/1616968-stopcachingimages)

|  | Declaration |
| --- | --- |
| From | ``` func stopCachingImagesForAssets(_ assets: [PHAsset], targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions?) ``` |
| To | ``` func stopCachingImages(for assets: [PHAsset], targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions?) ``` |

Modified [PHChange](https://developer.apple.com/documentation/photokit/phchange)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHChange : NSObject {     func changeDetailsForObject(_ object: PHObject) -> PHObjectChangeDetails?     func changeDetailsForFetchResult(_ object: PHFetchResult) -> PHFetchResultChangeDetails? } ``` | -- |
| To | ``` class PHChange : NSObject {     func __changeDetails(for object: PHObject) -> PHObjectChangeDetails<PHObject>?     func __changeDetails(for object: PHFetchResult<AnyObject>) -> PHFetchResultChangeDetails<PHObject>?     func changeDetails<T : PHObject>(for object: T) -> PHObjectChangeDetails<T>?     func changeDetails<T : PHObject>(for fetchResult: PHFetchResult<T>) -> PHFetchResultChangeDetails<T>?     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHChange : CVarArg { } extension PHChange : Equatable, Hashable {     var hashValue: Int { get } } extension PHChange {     func changeDetails<T : PHObject>(for object: T) -> PHObjectChangeDetails<T>?     func changeDetails<T : PHObject>(for fetchResult: PHFetchResult<T>) -> PHFetchResultChangeDetails<T>? } ``` | CVarArg, Equatable, Hashable |

Modified [PHCollection](https://developer.apple.com/documentation/photokit/phcollection)

|  | Declaration |
| --- | --- |
| From | ``` class PHCollection : PHObject {     var canContainAssets: Bool { get }     var canContainCollections: Bool { get }     var localizedTitle: String? { get }     func canPerformEditOperation(_ anOperation: PHCollectionEditOperation) -> Bool     class func fetchCollectionsInCollectionList(_ collectionList: PHCollectionList, options options: PHFetchOptions?) -> PHFetchResult     class func fetchTopLevelUserCollectionsWithOptions(_ options: PHFetchOptions?) -> PHFetchResult } ``` |
| To | ``` class PHCollection : PHObject {     var canContainAssets: Bool { get }     var canContainCollections: Bool { get }     var localizedTitle: String? { get }     func canPerform(_ anOperation: PHCollectionEditOperation) -> Bool     class func fetchCollections(in collectionList: PHCollectionList, options options: PHFetchOptions?) -> PHFetchResult<PHCollection>     class func fetchTopLevelUserCollections(with options: PHFetchOptions?) -> PHFetchResult<PHCollection> } ``` |

Modified [PHCollection.canPerform(_: PHCollectionEditOperation) -> Bool](https://developer.apple.com/documentation/photokit/phcollection/1618518-canperform)

|  | Declaration |
| --- | --- |
| From | ``` func canPerformEditOperation(_ anOperation: PHCollectionEditOperation) -> Bool ``` |
| To | ``` func canPerform(_ anOperation: PHCollectionEditOperation) -> Bool ``` |

Modified [PHCollection.fetchCollections(in: PHCollectionList, options: PHFetchOptions?) -> PHFetchResult<PHCollection> [class]](https://developer.apple.com/documentation/photokit/phcollection/1618515-fetchcollectionsincollectionlist)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchCollectionsInCollectionList(_ collectionList: PHCollectionList, options options: PHFetchOptions?) -> PHFetchResult ``` |
| To | ``` class func fetchCollections(in collectionList: PHCollectionList, options options: PHFetchOptions?) -> PHFetchResult<PHCollection> ``` |

Modified [PHCollection.fetchTopLevelUserCollections(with: PHFetchOptions?) -> PHFetchResult<PHCollection> [class]](https://developer.apple.com/documentation/photokit/phcollection/1618513-fetchtoplevelusercollections)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchTopLevelUserCollectionsWithOptions(_ options: PHFetchOptions?) -> PHFetchResult ``` |
| To | ``` class func fetchTopLevelUserCollections(with options: PHFetchOptions?) -> PHFetchResult<PHCollection> ``` |

Modified [PHCollectionEditOperation [enum]](https://developer.apple.com/documentation/photokit/phcollectioneditoperation)

|  | Declaration |
| --- | --- |
| From | ``` enum PHCollectionEditOperation : Int {     case DeleteContent     case RemoveContent     case AddContent     case CreateContent     case RearrangeContent     case Delete     case Rename } ``` |
| To | ``` enum PHCollectionEditOperation : Int {     case deleteContent     case removeContent     case addContent     case createContent     case rearrangeContent     case delete     case rename } ``` |

Modified [PHCollectionEditOperation.addContent](https://developer.apple.com/documentation/photokit/phcollectioneditoperation/addcontent)

|  | Declaration |
| --- | --- |
| From | ``` case AddContent ``` |
| To | ``` case addContent ``` |

Modified [PHCollectionEditOperation.createContent](https://developer.apple.com/documentation/photokit/phcollectioneditoperation/createcontent)

|  | Declaration |
| --- | --- |
| From | ``` case CreateContent ``` |
| To | ``` case createContent ``` |

Modified [PHCollectionEditOperation.delete](https://developer.apple.com/documentation/photokit/phcollectioneditoperation/delete)

|  | Declaration |
| --- | --- |
| From | ``` case Delete ``` |
| To | ``` case delete ``` |

Modified [PHCollectionEditOperation.deleteContent](https://developer.apple.com/documentation/photokit/phcollectioneditoperation/phcollectioneditoperationdeletecontent)

|  | Declaration |
| --- | --- |
| From | ``` case DeleteContent ``` |
| To | ``` case deleteContent ``` |

Modified [PHCollectionEditOperation.rearrangeContent](https://developer.apple.com/documentation/photokit/phcollectioneditoperation/phcollectioneditoperationrearrangecontent)

|  | Declaration |
| --- | --- |
| From | ``` case RearrangeContent ``` |
| To | ``` case rearrangeContent ``` |

Modified [PHCollectionEditOperation.removeContent](https://developer.apple.com/documentation/photokit/phcollectioneditoperation/phcollectioneditoperationremovecontent)

|  | Declaration |
| --- | --- |
| From | ``` case RemoveContent ``` |
| To | ``` case removeContent ``` |

Modified [PHCollectionEditOperation.rename](https://developer.apple.com/documentation/photokit/phcollectioneditoperation/rename)

|  | Declaration |
| --- | --- |
| From | ``` case Rename ``` |
| To | ``` case rename ``` |

Modified [PHCollectionList](https://developer.apple.com/documentation/photokit/phcollectionlist)

|  | Declaration |
| --- | --- |
| From | ``` class PHCollectionList : PHCollection {     var collectionListType: PHCollectionListType { get }     var collectionListSubtype: PHCollectionListSubtype { get }     var startDate: NSDate? { get }     var endDate: NSDate? { get }     var localizedLocationNames: [String] { get }     class func fetchCollectionListsContainingCollection(_ collection: PHCollection, options options: PHFetchOptions?) -> PHFetchResult     class func fetchCollectionListsWithLocalIdentifiers(_ identifiers: [String], options options: PHFetchOptions?) -> PHFetchResult     class func fetchCollectionListsWithType(_ collectionListType: PHCollectionListType, subtype subtype: PHCollectionListSubtype, options options: PHFetchOptions?) -> PHFetchResult     class func fetchMomentListsWithSubtype(_ momentListSubtype: PHCollectionListSubtype, containingMoment moment: PHAssetCollection, options options: PHFetchOptions?) -> PHFetchResult     class func fetchMomentListsWithSubtype(_ momentListSubtype: PHCollectionListSubtype, options options: PHFetchOptions?) -> PHFetchResult     class func transientCollectionListWithCollections(_ collections: [PHCollection], title title: String?) -> PHCollectionList     class func transientCollectionListWithCollectionsFetchResult(_ fetchResult: PHFetchResult, title title: String?) -> PHCollectionList } ``` |
| To | ``` class PHCollectionList : PHCollection {     var collectionListType: PHCollectionListType { get }     var collectionListSubtype: PHCollectionListSubtype { get }     var startDate: Date? { get }     var endDate: Date? { get }     var localizedLocationNames: [String] { get }     class func fetchCollectionListsContaining(_ collection: PHCollection, options options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>     class func fetchCollectionLists(withLocalIdentifiers identifiers: [String], options options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>     class func fetchCollectionLists(with collectionListType: PHCollectionListType, subtype subtype: PHCollectionListSubtype, options options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>     class func fetchMomentLists(with momentListSubtype: PHCollectionListSubtype, containingMoment moment: PHAssetCollection, options options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>     class func fetchMomentLists(with momentListSubtype: PHCollectionListSubtype, options options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>     class func transientCollectionList(with collections: [PHCollection], title title: String?) -> PHCollectionList     class func transientCollectionList(withCollectionsFetchResult fetchResult: PHFetchResult<PHCollection>, title title: String?) -> PHCollectionList } ``` |

Modified [PHCollectionList.endDate](https://developer.apple.com/documentation/photokit/phcollectionlist/1618509-enddate)

|  | Declaration |
| --- | --- |
| From | ``` var endDate: NSDate? { get } ``` |
| To | ``` var endDate: Date? { get } ``` |

Modified [PHCollectionList.fetchCollectionLists(with: PHCollectionListType, subtype: PHCollectionListSubtype, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList> [class]](https://developer.apple.com/documentation/photokit/phcollectionlist/1618520-fetchcollectionlists)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchCollectionListsWithType(_ collectionListType: PHCollectionListType, subtype subtype: PHCollectionListSubtype, options options: PHFetchOptions?) -> PHFetchResult ``` |
| To | ``` class func fetchCollectionLists(with collectionListType: PHCollectionListType, subtype subtype: PHCollectionListSubtype, options options: PHFetchOptions?) -> PHFetchResult<PHCollectionList> ``` |

Modified [PHCollectionList.fetchCollectionLists(withLocalIdentifiers: [String], options: PHFetchOptions?) -> PHFetchResult<PHCollectionList> [class]](https://developer.apple.com/documentation/photokit/phcollectionlist/1618525-fetchcollectionlists)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchCollectionListsWithLocalIdentifiers(_ identifiers: [String], options options: PHFetchOptions?) -> PHFetchResult ``` |
| To | ``` class func fetchCollectionLists(withLocalIdentifiers identifiers: [String], options options: PHFetchOptions?) -> PHFetchResult<PHCollectionList> ``` |

Modified [PHCollectionList.fetchCollectionListsContaining(_: PHCollection, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList> [class]](https://developer.apple.com/documentation/photokit/phcollectionlist/1618523-fetchcollectionlistscontainingco)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchCollectionListsContainingCollection(_ collection: PHCollection, options options: PHFetchOptions?) -> PHFetchResult ``` |
| To | ``` class func fetchCollectionListsContaining(_ collection: PHCollection, options options: PHFetchOptions?) -> PHFetchResult<PHCollectionList> ``` |

Modified [PHCollectionList.fetchMomentLists(with: PHCollectionListSubtype, containingMoment: PHAssetCollection, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList> [class]](https://developer.apple.com/documentation/photokit/phcollectionlist/1618536-fetchmomentlists)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchMomentListsWithSubtype(_ momentListSubtype: PHCollectionListSubtype, containingMoment moment: PHAssetCollection, options options: PHFetchOptions?) -> PHFetchResult ``` |
| To | ``` class func fetchMomentLists(with momentListSubtype: PHCollectionListSubtype, containingMoment moment: PHAssetCollection, options options: PHFetchOptions?) -> PHFetchResult<PHCollectionList> ``` |

Modified [PHCollectionList.fetchMomentLists(with: PHCollectionListSubtype, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList> [class]](https://developer.apple.com/documentation/photokit/phcollectionlist/1618540-fetchmomentlists)

|  | Declaration |
| --- | --- |
| From | ``` class func fetchMomentListsWithSubtype(_ momentListSubtype: PHCollectionListSubtype, options options: PHFetchOptions?) -> PHFetchResult ``` |
| To | ``` class func fetchMomentLists(with momentListSubtype: PHCollectionListSubtype, options options: PHFetchOptions?) -> PHFetchResult<PHCollectionList> ``` |

Modified [PHCollectionList.startDate](https://developer.apple.com/documentation/photokit/phcollectionlist/1618521-startdate)

|  | Declaration |
| --- | --- |
| From | ``` var startDate: NSDate? { get } ``` |
| To | ``` var startDate: Date? { get } ``` |

Modified [PHCollectionList.transientCollectionList(with: [PHCollection], title: String?) -> PHCollectionList [class]](https://developer.apple.com/documentation/photokit/phcollectionlist/1618537-transientcollectionlistwithcolle)

|  | Declaration |
| --- | --- |
| From | ``` class func transientCollectionListWithCollections(_ collections: [PHCollection], title title: String?) -> PHCollectionList ``` |
| To | ``` class func transientCollectionList(with collections: [PHCollection], title title: String?) -> PHCollectionList ``` |

Modified [PHCollectionList.transientCollectionList(withCollectionsFetchResult: PHFetchResult<PHCollection>, title: String?) -> PHCollectionList [class]](https://developer.apple.com/documentation/photokit/phcollectionlist/1618526-transientcollectionlistwithcolle)

|  | Declaration |
| --- | --- |
| From | ``` class func transientCollectionListWithCollectionsFetchResult(_ fetchResult: PHFetchResult, title title: String?) -> PHCollectionList ``` |
| To | ``` class func transientCollectionList(withCollectionsFetchResult fetchResult: PHFetchResult<PHCollection>, title title: String?) -> PHCollectionList ``` |

Modified [PHCollectionListChangeRequest](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHCollectionListChangeRequest : NSObject {     class func creationRequestForCollectionListWithTitle(_ title: String) -> Self     var placeholderForCreatedCollectionList: PHObjectPlaceholder { get }     class func deleteCollectionLists(_ collectionLists: NSFastEnumeration)     convenience init?(forCollectionList collectionList: PHCollectionList)     class func changeRequestForCollectionList(_ collectionList: PHCollectionList) -> Self?     convenience init?(forCollectionList collectionList: PHCollectionList, childCollections childCollections: PHFetchResult)     class func changeRequestForCollectionList(_ collectionList: PHCollectionList, childCollections childCollections: PHFetchResult) -> Self?     var title: String     func addChildCollections(_ collections: NSFastEnumeration)     func insertChildCollections(_ collections: NSFastEnumeration, atIndexes indexes: NSIndexSet)     func removeChildCollections(_ collections: NSFastEnumeration)     func removeChildCollectionsAtIndexes(_ indexes: NSIndexSet)     func replaceChildCollectionsAtIndexes(_ indexes: NSIndexSet, withChildCollections collections: NSFastEnumeration)     func moveChildCollectionsAtIndexes(_ indexes: NSIndexSet, toIndex toIndex: Int) } ``` | -- |
| To | ``` class PHCollectionListChangeRequest : NSObject {     class func creationRequestForCollectionList(withTitle title: String) -> Self     var placeholderForCreatedCollectionList: PHObjectPlaceholder { get }     class func deleteCollectionLists(_ collectionLists: NSFastEnumeration)     convenience init?(for collectionList: PHCollectionList)     class func forCollectionList(_ collectionList: PHCollectionList) -> Self?     convenience init?(for collectionList: PHCollectionList, childCollections childCollections: PHFetchResult<PHCollection>)     class func forCollectionList(_ collectionList: PHCollectionList, childCollections childCollections: PHFetchResult<PHCollection>) -> Self?     var title: String     func addChildCollections(_ collections: NSFastEnumeration)     func insertChildCollections(_ collections: NSFastEnumeration, at indexes: IndexSet)     func removeChildCollections(_ collections: NSFastEnumeration)     func removeChildCollections(at indexes: IndexSet)     func replaceChildCollections(at indexes: IndexSet, withChildCollections collections: NSFastEnumeration)     func moveChildCollections(at indexes: IndexSet, to toIndex: Int)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHCollectionListChangeRequest : CVarArg { } extension PHCollectionListChangeRequest : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PHCollectionListChangeRequest.creationRequestForCollectionList(withTitle: String) -> Self [class]](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest/1622858-creationrequestforcollectionlist)

|  | Declaration |
| --- | --- |
| From | ``` class func creationRequestForCollectionListWithTitle(_ title: String) -> Self ``` |
| To | ``` class func creationRequestForCollectionList(withTitle title: String) -> Self ``` |

Modified [PHCollectionListChangeRequest.init(for: PHCollectionList)](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest/1622855-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init?(forCollectionList collectionList: PHCollectionList) ``` |
| To | ``` convenience init?(for collectionList: PHCollectionList) ``` |

Modified [PHCollectionListChangeRequest.init(for: PHCollectionList, childCollections: PHFetchResult<PHCollection>)](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest/1622850-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init?(forCollectionList collectionList: PHCollectionList, childCollections childCollections: PHFetchResult) ``` |
| To | ``` convenience init?(for collectionList: PHCollectionList, childCollections childCollections: PHFetchResult<PHCollection>) ``` |

Modified [PHCollectionListChangeRequest.insertChildCollections(_: NSFastEnumeration, at: IndexSet)](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest/1622862-insertchildcollections)

|  | Declaration |
| --- | --- |
| From | ``` func insertChildCollections(_ collections: NSFastEnumeration, atIndexes indexes: NSIndexSet) ``` |
| To | ``` func insertChildCollections(_ collections: NSFastEnumeration, at indexes: IndexSet) ``` |

Modified [PHCollectionListChangeRequest.moveChildCollections(at: IndexSet, to: Int)](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest/1622859-movechildcollections)

|  | Declaration |
| --- | --- |
| From | ``` func moveChildCollectionsAtIndexes(_ indexes: NSIndexSet, toIndex toIndex: Int) ``` |
| To | ``` func moveChildCollections(at indexes: IndexSet, to toIndex: Int) ``` |

Modified [PHCollectionListChangeRequest.removeChildCollections(at: IndexSet)](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest/1622857-removechildcollections)

|  | Declaration |
| --- | --- |
| From | ``` func removeChildCollectionsAtIndexes(_ indexes: NSIndexSet) ``` |
| To | ``` func removeChildCollections(at indexes: IndexSet) ``` |

Modified [PHCollectionListChangeRequest.replaceChildCollections(at: IndexSet, withChildCollections: NSFastEnumeration)](https://developer.apple.com/documentation/photokit/phcollectionlistchangerequest/1622856-replacechildcollectionsatindexes)

|  | Declaration |
| --- | --- |
| From | ``` func replaceChildCollectionsAtIndexes(_ indexes: NSIndexSet, withChildCollections collections: NSFastEnumeration) ``` |
| To | ``` func replaceChildCollections(at indexes: IndexSet, withChildCollections collections: NSFastEnumeration) ``` |

Modified [PHCollectionListSubtype [enum]](https://developer.apple.com/documentation/photokit/phcollectionlistsubtype)

|  | Declaration |
| --- | --- |
| From | ``` enum PHCollectionListSubtype : Int {     case MomentListCluster     case MomentListYear     case RegularFolder     case SmartFolderEvents     case SmartFolderFaces     case Any } ``` |
| To | ``` enum PHCollectionListSubtype : Int {     case momentListCluster     case momentListYear     case regularFolder     case smartFolderEvents     case smartFolderFaces     case any } ``` |

Modified [PHCollectionListSubtype.any](https://developer.apple.com/documentation/photokit/phcollectionlistsubtype/any)

|  | Declaration |
| --- | --- |
| From | ``` case Any ``` |
| To | ``` case any ``` |

Modified [PHCollectionListSubtype.momentListCluster](https://developer.apple.com/documentation/photokit/phcollectionlistsubtype/phcollectionlistsubtypemomentlistcluster)

|  | Declaration |
| --- | --- |
| From | ``` case MomentListCluster ``` |
| To | ``` case momentListCluster ``` |

Modified [PHCollectionListSubtype.momentListYear](https://developer.apple.com/documentation/photokit/phcollectionlistsubtype/phcollectionlistsubtypemomentlistyear)

|  | Declaration |
| --- | --- |
| From | ``` case MomentListYear ``` |
| To | ``` case momentListYear ``` |

Modified [PHCollectionListSubtype.regularFolder](https://developer.apple.com/documentation/photokit/phcollectionlistsubtype/regularfolder)

|  | Declaration |
| --- | --- |
| From | ``` case RegularFolder ``` |
| To | ``` case regularFolder ``` |

Modified [PHCollectionListSubtype.smartFolderEvents](https://developer.apple.com/documentation/photokit/phcollectionlistsubtype/phcollectionlistsubtypesmartfolderevents)

|  | Declaration |
| --- | --- |
| From | ``` case SmartFolderEvents ``` |
| To | ``` case smartFolderEvents ``` |

Modified [PHCollectionListSubtype.smartFolderFaces](https://developer.apple.com/documentation/photokit/phcollectionlistsubtype/smartfolderfaces)

|  | Declaration |
| --- | --- |
| From | ``` case SmartFolderFaces ``` |
| To | ``` case smartFolderFaces ``` |

Modified [PHCollectionListType [enum]](https://developer.apple.com/documentation/photokit/phcollectionlisttype)

|  | Declaration |
| --- | --- |
| From | ``` enum PHCollectionListType : Int {     case MomentList     case Folder     case SmartFolder } ``` |
| To | ``` enum PHCollectionListType : Int {     case momentList     case folder     case smartFolder } ``` |

Modified [PHCollectionListType.folder](https://developer.apple.com/documentation/photokit/phcollectionlisttype/folder)

|  | Declaration |
| --- | --- |
| From | ``` case Folder ``` |
| To | ``` case folder ``` |

Modified [PHCollectionListType.momentList](https://developer.apple.com/documentation/photokit/phcollectionlisttype/momentlist)

|  | Declaration |
| --- | --- |
| From | ``` case MomentList ``` |
| To | ``` case momentList ``` |

Modified [PHCollectionListType.smartFolder](https://developer.apple.com/documentation/photokit/phcollectionlisttype/phcollectionlisttypesmartfolder)

|  | Declaration |
| --- | --- |
| From | ``` case SmartFolder ``` |
| To | ``` case smartFolder ``` |

Modified [PHContentEditingInput](https://developer.apple.com/documentation/photokit/phcontenteditinginput)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHContentEditingInput : NSObject {     var mediaType: PHAssetMediaType { get }     var mediaSubtypes: PHAssetMediaSubtype { get }     @NSCopying var creationDate: NSDate? { get }     @NSCopying var location: CLLocation? { get }     var uniformTypeIdentifier: String? { get }     var adjustmentData: PHAdjustmentData { get }     var displaySizeImage: UIImage? { get }     @NSCopying var fullSizeImageURL: NSURL? { get }     var fullSizeImageOrientation: Int32 { get }     var avAsset: AVAsset? { get }     var audiovisualAsset: AVAsset? { get } } ``` | -- |
| To | ``` class PHContentEditingInput : NSObject {     var mediaType: PHAssetMediaType { get }     var mediaSubtypes: PHAssetMediaSubtype { get }     var creationDate: Date? { get }     @NSCopying var location: CLLocation? { get }     var uniformTypeIdentifier: String? { get }     var adjustmentData: PHAdjustmentData? { get }     var displaySizeImage: UIImage? { get }     var fullSizeImageURL: URL? { get }     var fullSizeImageOrientation: Int32 { get }     var avAsset: AVAsset? { get }     var audiovisualAsset: AVAsset? { get }     var livePhoto: PHLivePhoto? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHContentEditingInput : CVarArg { } extension PHContentEditingInput : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PHContentEditingInput.adjustmentData](https://developer.apple.com/documentation/photokit/phcontenteditinginput/1518657-adjustmentdata)

|  | Declaration |
| --- | --- |
| From | ``` var adjustmentData: PHAdjustmentData { get } ``` |
| To | ``` var adjustmentData: PHAdjustmentData? { get } ``` |

Modified [PHContentEditingInput.creationDate](https://developer.apple.com/documentation/photokit/phcontenteditinginput/1518619-creationdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var creationDate: NSDate? { get } ``` |
| To | ``` var creationDate: Date? { get } ``` |

Modified [PHContentEditingInput.fullSizeImageURL](https://developer.apple.com/documentation/photokit/phcontenteditinginput/1518671-fullsizeimageurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var fullSizeImageURL: NSURL? { get } ``` |
| To | ``` var fullSizeImageURL: URL? { get } ``` |

Modified [PHContentEditingInputRequestOptions](https://developer.apple.com/documentation/photokit/phcontenteditinginputrequestoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHContentEditingInputRequestOptions : NSObject {     var canHandleAdjustmentData: (PHAdjustmentData) -> Bool     var networkAccessAllowed: Bool     var progressHandler: ((Double, UnsafeMutablePointer<ObjCBool>) -> Void)? } ``` | -- |
| To | ``` class PHContentEditingInputRequestOptions : NSObject {     var canHandleAdjustmentData: (PHAdjustmentData) -> Bool     var isNetworkAccessAllowed: Bool     var progressHandler: ((Double, UnsafeMutablePointer<ObjCBool>) -> Swift.Void)?     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHContentEditingInputRequestOptions : CVarArg { } extension PHContentEditingInputRequestOptions : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PHContentEditingInputRequestOptions.isNetworkAccessAllowed](https://developer.apple.com/documentation/photokit/phcontenteditinginputrequestoptions/1624049-isnetworkaccessallowed)

|  | Declaration |
| --- | --- |
| From | ``` var networkAccessAllowed: Bool ``` |
| To | ``` var isNetworkAccessAllowed: Bool ``` |

Modified [PHContentEditingInputRequestOptions.progressHandler](https://developer.apple.com/documentation/photokit/phcontenteditinginputrequestoptions/1624053-progresshandler)

|  | Declaration |
| --- | --- |
| From | ``` var progressHandler: ((Double, UnsafeMutablePointer<ObjCBool>) -> Void)? ``` |
| To | ``` var progressHandler: ((Double, UnsafeMutablePointer<ObjCBool>) -> Swift.Void)? ``` |

Modified [PHContentEditingOutput](https://developer.apple.com/documentation/photokit/phcontenteditingoutput)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHContentEditingOutput : NSObject {     init(contentEditingInput contentEditingInput: PHContentEditingInput)     var adjustmentData: PHAdjustmentData?     @NSCopying var renderedContentURL: NSURL { get } } extension PHContentEditingOutput {     init(placeholderForCreatedAsset placeholderForCreatedAsset: PHObjectPlaceholder) } ``` | -- |
| To | ``` class PHContentEditingOutput : NSObject {     init(contentEditingInput contentEditingInput: PHContentEditingInput)     var adjustmentData: PHAdjustmentData?     var renderedContentURL: URL { get }     init(placeholderForCreatedAsset placeholderForCreatedAsset: PHObjectPlaceholder)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHContentEditingOutput {     init(placeholderForCreatedAsset placeholderForCreatedAsset: PHObjectPlaceholder) } extension PHContentEditingOutput : CVarArg { } extension PHContentEditingOutput : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PHContentEditingOutput.renderedContentURL](https://developer.apple.com/documentation/photokit/phcontenteditingoutput/1518655-renderedcontenturl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var renderedContentURL: NSURL { get } ``` |
| To | ``` var renderedContentURL: URL { get } ``` |

Modified [PHFetchOptions](https://developer.apple.com/documentation/photokit/phfetchoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHFetchOptions : NSObject, NSCopying {     var predicate: NSPredicate?     var sortDescriptors: [NSSortDescriptor]?     var includeHiddenAssets: Bool     var includeAllBurstAssets: Bool     var includeAssetSourceTypes: PHAssetSourceType     var fetchLimit: Int     var wantsIncrementalChangeDetails: Bool } ``` | NSCopying |
| To | ``` class PHFetchOptions : NSObject, NSCopying {     var predicate: NSPredicate?     var sortDescriptors: [NSSortDescriptor]?     var includeHiddenAssets: Bool     var includeAllBurstAssets: Bool     var includeAssetSourceTypes: PHAssetSourceType     var fetchLimit: Int     var wantsIncrementalChangeDetails: Bool     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHFetchOptions : CVarArg { } extension PHFetchOptions : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [PHFetchResult](https://developer.apple.com/documentation/photokit/phfetchresult)

|  | Declaration | Protocols | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` class PHFetchResult : NSObject, NSCopying, NSFastEnumeration {     var count: Int { get }     func objectAtIndex(_ index: Int) -> AnyObject     subscript (_ idx: Int) -> AnyObject { get }     func objectAtIndexedSubscript(_ idx: Int) -> AnyObject     func containsObject(_ anObject: AnyObject) -> Bool     func indexOfObject(_ anObject: AnyObject) -> Int     func indexOfObject(_ anObject: AnyObject, inRange range: NSRange) -> Int     var firstObject: AnyObject? { get }     var lastObject: AnyObject? { get }     func objectsAtIndexes(_ indexes: NSIndexSet) -> [AnyObject]     func enumerateObjectsUsingBlock(_ block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func countOfAssetsWithMediaType(_ mediaType: PHAssetMediaType) -> Int } ``` | NSCopying, NSFastEnumeration | ```  ``` | -- |
| To | ``` class PHFetchResult<ObjectType : AnyObject> : NSObject, NSCopying, NSFastEnumeration {     var count: Int { get }     func object(at index: Int) -> ObjectType     subscript(_ idx: Int) -> ObjectType { get }     func objectAtIndexedSubscript(_ idx: Int) -> ObjectType     func contains(_ anObject: ObjectType) -> Bool     func index(of anObject: ObjectType) -> Int     func index(of anObject: ObjectType, in range: NSRange) -> Int     var firstObject: ObjectType? { get }     var lastObject: ObjectType? { get }     func objects(at indexes: IndexSet) -> [ObjectType]     func enumerateObjects(_ block: @escaping (ObjectType, Int, UnsafeMutablePointer<ObjCBool>) -> Swift.Void)     func enumerateObjects(options opts: NSEnumerationOptions = [], using block: @escaping (ObjectType, Int, UnsafeMutablePointer<ObjCBool>) -> Swift.Void)     func enumerateObjects(at s: IndexSet, options opts: NSEnumerationOptions = [], using block: @escaping (ObjectType, Int, UnsafeMutablePointer<ObjCBool>) -> Swift.Void)     func countOfAssets(with mediaType: PHAssetMediaType) -> Int     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHFetchResult : CVarArg { } extension PHFetchResult : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSFastEnumeration | ``` ObjectType : AnyObject ``` | ObjectType |

Modified [PHFetchResult.contains(_: ObjectType) -> Bool](https://developer.apple.com/documentation/photokit/phfetchresult/1621005-contains)

|  | Declaration |
| --- | --- |
| From | ``` func containsObject(_ anObject: AnyObject) -> Bool ``` |
| To | ``` func contains(_ anObject: ObjectType) -> Bool ``` |

Modified [PHFetchResult.countOfAssets(with: PHAssetMediaType) -> Int](https://developer.apple.com/documentation/photokit/phfetchresult/1620997-countofassetswithmediatype)

|  | Declaration |
| --- | --- |
| From | ``` func countOfAssetsWithMediaType(_ mediaType: PHAssetMediaType) -> Int ``` |
| To | ``` func countOfAssets(with mediaType: PHAssetMediaType) -> Int ``` |

Modified [PHFetchResult.enumerateObjects(_: (ObjectType, Int, UnsafeMutablePointer<ObjCBool>) -> Swift.Void)](https://developer.apple.com/documentation/photokit/phfetchresult/1620999-enumerateobjects)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateObjectsUsingBlock(_ block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateObjects(_ block: @escaping (ObjectType, Int, UnsafeMutablePointer<ObjCBool>) -> Swift.Void) ``` |

Modified [PHFetchResult.enumerateObjects(at: IndexSet, options: NSEnumerationOptions, using: (ObjectType, Int, UnsafeMutablePointer<ObjCBool>) -> Swift.Void)](https://developer.apple.com/documentation/photokit/phfetchresult/1620998-enumerateobjectsatindexes)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateObjectsAtIndexes(_ s: NSIndexSet, options opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateObjects(at s: IndexSet, options opts: NSEnumerationOptions = [], using block: @escaping (ObjectType, Int, UnsafeMutablePointer<ObjCBool>) -> Swift.Void) ``` |

Modified [PHFetchResult.enumerateObjects(options: NSEnumerationOptions, using: (ObjectType, Int, UnsafeMutablePointer<ObjCBool>) -> Swift.Void)](https://developer.apple.com/documentation/photokit/phfetchresult/1621006-enumerateobjects)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateObjectsWithOptions(_ opts: NSEnumerationOptions, usingBlock block: (AnyObject, Int, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateObjects(options opts: NSEnumerationOptions = [], using block: @escaping (ObjectType, Int, UnsafeMutablePointer<ObjCBool>) -> Swift.Void) ``` |

Modified [PHFetchResult.firstObject](https://developer.apple.com/documentation/photokit/phfetchresult/1621003-firstobject)

|  | Declaration |
| --- | --- |
| From | ``` var firstObject: AnyObject? { get } ``` |
| To | ``` var firstObject: ObjectType? { get } ``` |

Modified [PHFetchResult.index(of: ObjectType) -> Int](https://developer.apple.com/documentation/photokit/phfetchresult/1621007-indexofobject)

|  | Declaration |
| --- | --- |
| From | ``` func indexOfObject(_ anObject: AnyObject) -> Int ``` |
| To | ``` func index(of anObject: ObjectType) -> Int ``` |

Modified [PHFetchResult.index(of: ObjectType, in: NSRange) -> Int](https://developer.apple.com/documentation/photokit/phfetchresult/1621009-index)

|  | Declaration |
| --- | --- |
| From | ``` func indexOfObject(_ anObject: AnyObject, inRange range: NSRange) -> Int ``` |
| To | ``` func index(of anObject: ObjectType, in range: NSRange) -> Int ``` |

Modified [PHFetchResult.lastObject](https://developer.apple.com/documentation/photokit/phfetchresult/1621001-lastobject)

|  | Declaration |
| --- | --- |
| From | ``` var lastObject: AnyObject? { get } ``` |
| To | ``` var lastObject: ObjectType? { get } ``` |

Modified [PHFetchResult.object(at: Int) -> ObjectType](https://developer.apple.com/documentation/photokit/phfetchresult/1621002-object)

|  | Declaration |
| --- | --- |
| From | ``` func objectAtIndex(_ index: Int) -> AnyObject ``` |
| To | ``` func object(at index: Int) -> ObjectType ``` |

Modified [PHFetchResult.objects(at: IndexSet) -> [ObjectType]](https://developer.apple.com/documentation/photokit/phfetchresult/1621008-objectsatindexes)

|  | Declaration |
| --- | --- |
| From | ``` func objectsAtIndexes(_ indexes: NSIndexSet) -> [AnyObject] ``` |
| To | ``` func objects(at indexes: IndexSet) -> [ObjectType] ``` |

Modified [PHFetchResult.subscript(_: Int) -> ObjectType](https://developer.apple.com/documentation/photokit/phfetchresult/1621000-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ idx: Int) -> AnyObject { get } ``` |
| To | ``` subscript(_ idx: Int) -> ObjectType { get } ``` |

Modified [PHFetchResultChangeDetails](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails)

|  | Declaration | Protocols | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` class PHFetchResultChangeDetails : NSObject {     var fetchResultBeforeChanges: PHFetchResult { get }     var fetchResultAfterChanges: PHFetchResult { get }     var hasIncrementalChanges: Bool { get }     var removedIndexes: NSIndexSet? { get }     var removedObjects: [PHObject] { get }     var insertedIndexes: NSIndexSet? { get }     var insertedObjects: [PHObject] { get }     var changedIndexes: NSIndexSet? { get }     var changedObjects: [PHObject] { get }     func enumerateMovesWithBlock(_ handler: (Int, Int) -> Void)     var hasMoves: Bool { get }     convenience init(fromFetchResult fromResult: PHFetchResult, toFetchResult toResult: PHFetchResult, changedObjects changedObjects: [PHObject])     class func changeDetailsFromFetchResult(_ fromResult: PHFetchResult, toFetchResult toResult: PHFetchResult, changedObjects changedObjects: [PHObject]) -> Self } ``` | -- | ```  ``` | -- |
| To | ``` class PHFetchResultChangeDetails<ObjectType : PHObject> : NSObject {     var fetchResultBeforeChanges: PHFetchResult<ObjectType> { get }     var fetchResultAfterChanges: PHFetchResult<ObjectType> { get }     var hasIncrementalChanges: Bool { get }     var removedIndexes: IndexSet? { get }     var removedObjects: [ObjectType] { get }     var insertedIndexes: IndexSet? { get }     var insertedObjects: [ObjectType] { get }     var changedIndexes: IndexSet? { get }     var changedObjects: [ObjectType] { get }     func enumerateMoves(_ handler: @escaping (Int, Int) -> Swift.Void)     var hasMoves: Bool { get }     convenience init(from fromResult: PHFetchResult<ObjectType>, to toResult: PHFetchResult<ObjectType>, changedObjects changedObjects: [ObjectType])     class func fromFetchResult(_ fromResult: PHFetchResult<ObjectType>, to toResult: PHFetchResult<ObjectType>, changedObjects changedObjects: [ObjectType]) -> Self     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHFetchResultChangeDetails : CVarArg { } extension PHFetchResultChangeDetails : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable | ``` ObjectType : PHObject ``` | ObjectType |

Modified [PHFetchResultChangeDetails.changedIndexes](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613922-changedindexes)

|  | Declaration |
| --- | --- |
| From | ``` var changedIndexes: NSIndexSet? { get } ``` |
| To | ``` var changedIndexes: IndexSet? { get } ``` |

Modified [PHFetchResultChangeDetails.changedObjects](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613910-changedobjects)

|  | Declaration |
| --- | --- |
| From | ``` var changedObjects: [PHObject] { get } ``` |
| To | ``` var changedObjects: [ObjectType] { get } ``` |

Modified [PHFetchResultChangeDetails.enumerateMoves(_: (Int, Int) -> Swift.Void)](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613898-enumeratemoves)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateMovesWithBlock(_ handler: (Int, Int) -> Void) ``` |
| To | ``` func enumerateMoves(_ handler: @escaping (Int, Int) -> Swift.Void) ``` |

Modified [PHFetchResultChangeDetails.fetchResultAfterChanges](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613894-fetchresultafterchanges)

|  | Declaration |
| --- | --- |
| From | ``` var fetchResultAfterChanges: PHFetchResult { get } ``` |
| To | ``` var fetchResultAfterChanges: PHFetchResult<ObjectType> { get } ``` |

Modified [PHFetchResultChangeDetails.fetchResultBeforeChanges](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613892-fetchresultbeforechanges)

|  | Declaration |
| --- | --- |
| From | ``` var fetchResultBeforeChanges: PHFetchResult { get } ``` |
| To | ``` var fetchResultBeforeChanges: PHFetchResult<ObjectType> { get } ``` |

Modified [PHFetchResultChangeDetails.init(from: PHFetchResult<ObjectType>, to: PHFetchResult<ObjectType>, changedObjects: [ObjectType])](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613921-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(fromFetchResult fromResult: PHFetchResult, toFetchResult toResult: PHFetchResult, changedObjects changedObjects: [PHObject]) ``` |
| To | ``` convenience init(from fromResult: PHFetchResult<ObjectType>, to toResult: PHFetchResult<ObjectType>, changedObjects changedObjects: [ObjectType]) ``` |

Modified [PHFetchResultChangeDetails.insertedIndexes](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613919-insertedindexes)

|  | Declaration |
| --- | --- |
| From | ``` var insertedIndexes: NSIndexSet? { get } ``` |
| To | ``` var insertedIndexes: IndexSet? { get } ``` |

Modified [PHFetchResultChangeDetails.insertedObjects](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613908-insertedobjects)

|  | Declaration |
| --- | --- |
| From | ``` var insertedObjects: [PHObject] { get } ``` |
| To | ``` var insertedObjects: [ObjectType] { get } ``` |

Modified [PHFetchResultChangeDetails.removedIndexes](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613920-removedindexes)

|  | Declaration |
| --- | --- |
| From | ``` var removedIndexes: NSIndexSet? { get } ``` |
| To | ``` var removedIndexes: IndexSet? { get } ``` |

Modified [PHFetchResultChangeDetails.removedObjects](https://developer.apple.com/documentation/photokit/phfetchresultchangedetails/1613902-removedobjects)

|  | Declaration |
| --- | --- |
| From | ``` var removedObjects: [PHObject] { get } ``` |
| To | ``` var removedObjects: [ObjectType] { get } ``` |

Modified [PHImageContentMode [enum]](https://developer.apple.com/documentation/photokit/phimagecontentmode)

|  | Declaration |
| --- | --- |
| From | ``` enum PHImageContentMode : Int {     case AspectFit     case AspectFill     static var Default: PHImageContentMode { get } } ``` |
| To | ``` enum PHImageContentMode : Int {     case aspectFit     case aspectFill     static var `default`: PHImageContentMode { get } } ``` |

Modified [PHImageContentMode.aspectFill](https://developer.apple.com/documentation/photokit/phimagecontentmode/phimagecontentmodeaspectfill)

|  | Declaration |
| --- | --- |
| From | ``` case AspectFill ``` |
| To | ``` case aspectFill ``` |

Modified [PHImageContentMode.aspectFit](https://developer.apple.com/documentation/photokit/phimagecontentmode/phimagecontentmodeaspectfit)

|  | Declaration |
| --- | --- |
| From | ``` case AspectFit ``` |
| To | ``` case aspectFit ``` |

Modified [PHImageContentMode.default](https://developer.apple.com/documentation/photokit/phimagecontentmode/1614052-default)

|  | Declaration |
| --- | --- |
| From | ``` static var Default: PHImageContentMode { get } ``` |
| To | ``` static var `default`: PHImageContentMode { get } ``` |

Modified [PHImageManager](https://developer.apple.com/documentation/photokit/phimagemanager)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHImageManager : NSObject {     class func defaultManager() -> PHImageManager     func requestImageForAsset(_ asset: PHAsset, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions?, resultHandler resultHandler: (UIImage?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID     func requestImageDataForAsset(_ asset: PHAsset, options options: PHImageRequestOptions?, resultHandler resultHandler: (NSData?, String?, UIImageOrientation, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID     func cancelImageRequest(_ requestID: PHImageRequestID)     func requestLivePhotoForAsset(_ asset: PHAsset, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHLivePhotoRequestOptions?, resultHandler resultHandler: (PHLivePhoto?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID     func requestPlayerItemForVideo(_ asset: PHAsset, options options: PHVideoRequestOptions?, resultHandler resultHandler: (AVPlayerItem?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID     func requestExportSessionForVideo(_ asset: PHAsset, options options: PHVideoRequestOptions?, exportPreset exportPreset: String, resultHandler resultHandler: (AVAssetExportSession?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID     func requestAVAssetForVideo(_ asset: PHAsset, options options: PHVideoRequestOptions?, resultHandler resultHandler: (AVAsset?, AVAudioMix?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID } ``` | -- |
| To | ``` class PHImageManager : NSObject {     class func `default`() -> PHImageManager     func requestImage(for asset: PHAsset, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions?, resultHandler resultHandler: @escaping (UIImage?, [AnyHashable : Any]?) -> Swift.Void) -> PHImageRequestID     func requestImageData(for asset: PHAsset, options options: PHImageRequestOptions?, resultHandler resultHandler: @escaping (Data?, String?, UIImageOrientation, [AnyHashable : Any]?) -> Swift.Void) -> PHImageRequestID     func cancelImageRequest(_ requestID: PHImageRequestID)     func requestLivePhoto(for asset: PHAsset, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHLivePhotoRequestOptions?, resultHandler resultHandler: @escaping (PHLivePhoto?, [AnyHashable : Any]?) -> Swift.Void) -> PHImageRequestID     func requestPlayerItem(forVideo asset: PHAsset, options options: PHVideoRequestOptions?, resultHandler resultHandler: @escaping (AVPlayerItem?, [AnyHashable : Any]?) -> Swift.Void) -> PHImageRequestID     func requestExportSession(forVideo asset: PHAsset, options options: PHVideoRequestOptions?, exportPreset exportPreset: String, resultHandler resultHandler: @escaping (AVAssetExportSession?, [AnyHashable : Any]?) -> Swift.Void) -> PHImageRequestID     func requestAVAsset(forVideo asset: PHAsset, options options: PHVideoRequestOptions?, resultHandler resultHandler: @escaping (AVAsset?, AVAudioMix?, [AnyHashable : Any]?) -> Swift.Void) -> PHImageRequestID     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHImageManager : CVarArg { } extension PHImageManager : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PHImageManager.default() [class]](https://developer.apple.com/documentation/photokit/phimagemanager/1616933-default)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultManager() -> PHImageManager ``` |
| To | ``` class func `default`() -> PHImageManager ``` |

Modified [PHImageManager.requestAVAsset(forVideo: PHAsset, options: PHVideoRequestOptions?, resultHandler: (AVAsset?, AVAudioMix?, [AnyHashable : Any]?) -> Swift.Void) -> PHImageRequestID](https://developer.apple.com/documentation/photokit/phimagemanager/1616935-requestavassetforvideo)

|  | Declaration |
| --- | --- |
| From | ``` func requestAVAssetForVideo(_ asset: PHAsset, options options: PHVideoRequestOptions?, resultHandler resultHandler: (AVAsset?, AVAudioMix?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID ``` |
| To | ``` func requestAVAsset(forVideo asset: PHAsset, options options: PHVideoRequestOptions?, resultHandler resultHandler: @escaping (AVAsset?, AVAudioMix?, [AnyHashable : Any]?) -> Swift.Void) -> PHImageRequestID ``` |

Modified [PHImageManager.requestExportSession(forVideo: PHAsset, options: PHVideoRequestOptions?, exportPreset: String, resultHandler: (AVAssetExportSession?, [AnyHashable : Any]?) -> Swift.Void) -> PHImageRequestID](https://developer.apple.com/documentation/photokit/phimagemanager/1616981-requestexportsessionforvideo)

|  | Declaration |
| --- | --- |
| From | ``` func requestExportSessionForVideo(_ asset: PHAsset, options options: PHVideoRequestOptions?, exportPreset exportPreset: String, resultHandler resultHandler: (AVAssetExportSession?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID ``` |
| To | ``` func requestExportSession(forVideo asset: PHAsset, options options: PHVideoRequestOptions?, exportPreset exportPreset: String, resultHandler resultHandler: @escaping (AVAssetExportSession?, [AnyHashable : Any]?) -> Swift.Void) -> PHImageRequestID ``` |

Modified [PHImageManager.requestImage(for: PHAsset, targetSize: CGSize, contentMode: PHImageContentMode, options: PHImageRequestOptions?, resultHandler: (UIImage?, [AnyHashable : Any]?) -> Swift.Void) -> PHImageRequestID](https://developer.apple.com/documentation/photokit/phimagemanager/1616964-requestimageforasset)

|  | Declaration |
| --- | --- |
| From | ``` func requestImageForAsset(_ asset: PHAsset, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions?, resultHandler resultHandler: (UIImage?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID ``` |
| To | ``` func requestImage(for asset: PHAsset, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHImageRequestOptions?, resultHandler resultHandler: @escaping (UIImage?, [AnyHashable : Any]?) -> Swift.Void) -> PHImageRequestID ``` |

Modified [PHImageManager.requestImageData(for: PHAsset, options: PHImageRequestOptions?, resultHandler: (Data?, String?, UIImageOrientation, [AnyHashable : Any]?) -> Swift.Void) -> PHImageRequestID](https://developer.apple.com/documentation/photokit/phimagemanager/1616957-requestimagedataforasset)

|  | Declaration |
| --- | --- |
| From | ``` func requestImageDataForAsset(_ asset: PHAsset, options options: PHImageRequestOptions?, resultHandler resultHandler: (NSData?, String?, UIImageOrientation, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID ``` |
| To | ``` func requestImageData(for asset: PHAsset, options options: PHImageRequestOptions?, resultHandler resultHandler: @escaping (Data?, String?, UIImageOrientation, [AnyHashable : Any]?) -> Swift.Void) -> PHImageRequestID ``` |

Modified [PHImageManager.requestLivePhoto(for: PHAsset, targetSize: CGSize, contentMode: PHImageContentMode, options: PHLivePhotoRequestOptions?, resultHandler: (PHLivePhoto?, [AnyHashable : Any]?) -> Swift.Void) -> PHImageRequestID](https://developer.apple.com/documentation/photokit/phimagemanager/1616984-requestlivephotoforasset)

|  | Declaration |
| --- | --- |
| From | ``` func requestLivePhotoForAsset(_ asset: PHAsset, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHLivePhotoRequestOptions?, resultHandler resultHandler: (PHLivePhoto?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID ``` |
| To | ``` func requestLivePhoto(for asset: PHAsset, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, options options: PHLivePhotoRequestOptions?, resultHandler resultHandler: @escaping (PHLivePhoto?, [AnyHashable : Any]?) -> Swift.Void) -> PHImageRequestID ``` |

Modified [PHImageManager.requestPlayerItem(forVideo: PHAsset, options: PHVideoRequestOptions?, resultHandler: (AVPlayerItem?, [AnyHashable : Any]?) -> Swift.Void) -> PHImageRequestID](https://developer.apple.com/documentation/photokit/phimagemanager/1616958-requestplayeritem)

|  | Declaration |
| --- | --- |
| From | ``` func requestPlayerItemForVideo(_ asset: PHAsset, options options: PHVideoRequestOptions?, resultHandler resultHandler: (AVPlayerItem?, [NSObject : AnyObject]?) -> Void) -> PHImageRequestID ``` |
| To | ``` func requestPlayerItem(forVideo asset: PHAsset, options options: PHVideoRequestOptions?, resultHandler resultHandler: @escaping (AVPlayerItem?, [AnyHashable : Any]?) -> Swift.Void) -> PHImageRequestID ``` |

Modified [PHImageRequestOptions](https://developer.apple.com/documentation/photokit/phimagerequestoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHImageRequestOptions : NSObject, NSCopying {     var version: PHImageRequestOptionsVersion     var deliveryMode: PHImageRequestOptionsDeliveryMode     var resizeMode: PHImageRequestOptionsResizeMode     var normalizedCropRect: CGRect     var networkAccessAllowed: Bool     var synchronous: Bool     var progressHandler: PHAssetImageProgressHandler? } ``` | NSCopying |
| To | ``` class PHImageRequestOptions : NSObject, NSCopying {     var version: PHImageRequestOptionsVersion     var deliveryMode: PHImageRequestOptionsDeliveryMode     var resizeMode: PHImageRequestOptionsResizeMode     var normalizedCropRect: CGRect     var isNetworkAccessAllowed: Bool     var isSynchronous: Bool     var progressHandler: Photos.PHAssetImageProgressHandler?     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHImageRequestOptions : CVarArg { } extension PHImageRequestOptions : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [PHImageRequestOptions.isNetworkAccessAllowed](https://developer.apple.com/documentation/photokit/phimagerequestoptions/1616934-networkaccessallowed)

|  | Declaration |
| --- | --- |
| From | ``` var networkAccessAllowed: Bool ``` |
| To | ``` var isNetworkAccessAllowed: Bool ``` |

Modified [PHImageRequestOptions.isSynchronous](https://developer.apple.com/documentation/photokit/phimagerequestoptions/1616945-issynchronous)

|  | Declaration |
| --- | --- |
| From | ``` var synchronous: Bool ``` |
| To | ``` var isSynchronous: Bool ``` |

Modified [PHImageRequestOptions.progressHandler](https://developer.apple.com/documentation/photokit/phimagerequestoptions/1616939-progresshandler)

|  | Declaration |
| --- | --- |
| From | ``` var progressHandler: PHAssetImageProgressHandler? ``` |
| To | ``` var progressHandler: Photos.PHAssetImageProgressHandler? ``` |

Modified [PHImageRequestOptionsDeliveryMode [enum]](https://developer.apple.com/documentation/photokit/phimagerequestoptionsdeliverymode)

|  | Declaration |
| --- | --- |
| From | ``` enum PHImageRequestOptionsDeliveryMode : Int {     case Opportunistic     case HighQualityFormat     case FastFormat } ``` |
| To | ``` enum PHImageRequestOptionsDeliveryMode : Int {     case opportunistic     case highQualityFormat     case fastFormat } ``` |

Modified [PHImageRequestOptionsDeliveryMode.fastFormat](https://developer.apple.com/documentation/photokit/phimagerequestoptionsdeliverymode/fastformat)

|  | Declaration |
| --- | --- |
| From | ``` case FastFormat ``` |
| To | ``` case fastFormat ``` |

Modified [PHImageRequestOptionsDeliveryMode.highQualityFormat](https://developer.apple.com/documentation/photokit/phimagerequestoptionsdeliverymode/phimagerequestoptionsdeliverymodehighqualityformat)

|  | Declaration |
| --- | --- |
| From | ``` case HighQualityFormat ``` |
| To | ``` case highQualityFormat ``` |

Modified [PHImageRequestOptionsDeliveryMode.opportunistic](https://developer.apple.com/documentation/photokit/phimagerequestoptionsdeliverymode/phimagerequestoptionsdeliverymodeopportunistic)

|  | Declaration |
| --- | --- |
| From | ``` case Opportunistic ``` |
| To | ``` case opportunistic ``` |

Modified [PHImageRequestOptionsResizeMode [enum]](https://developer.apple.com/documentation/photokit/phimagerequestoptionsresizemode)

|  | Declaration |
| --- | --- |
| From | ``` enum PHImageRequestOptionsResizeMode : Int {     case None     case Fast     case Exact } ``` |
| To | ``` enum PHImageRequestOptionsResizeMode : Int {     case none     case fast     case exact } ``` |

Modified [PHImageRequestOptionsResizeMode.exact](https://developer.apple.com/documentation/photokit/phimagerequestoptionsresizemode/phimagerequestoptionsresizemodeexact)

|  | Declaration |
| --- | --- |
| From | ``` case Exact ``` |
| To | ``` case exact ``` |

Modified [PHImageRequestOptionsResizeMode.fast](https://developer.apple.com/documentation/photokit/phimagerequestoptionsresizemode/fast)

|  | Declaration |
| --- | --- |
| From | ``` case Fast ``` |
| To | ``` case fast ``` |

Modified [PHImageRequestOptionsResizeMode.none](https://developer.apple.com/documentation/photokit/phimagerequestoptionsresizemode/none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [PHImageRequestOptionsVersion [enum]](https://developer.apple.com/documentation/photokit/phimagerequestoptionsversion)

|  | Declaration |
| --- | --- |
| From | ``` enum PHImageRequestOptionsVersion : Int {     case Current     case Unadjusted     case Original } ``` |
| To | ``` enum PHImageRequestOptionsVersion : Int {     case current     case unadjusted     case original } ``` |

Modified [PHImageRequestOptionsVersion.current](https://developer.apple.com/documentation/photokit/phimagerequestoptionsversion/phimagerequestoptionsversioncurrent)

|  | Declaration |
| --- | --- |
| From | ``` case Current ``` |
| To | ``` case current ``` |

Modified [PHImageRequestOptionsVersion.original](https://developer.apple.com/documentation/photokit/phimagerequestoptionsversion/original)

|  | Declaration |
| --- | --- |
| From | ``` case Original ``` |
| To | ``` case original ``` |

Modified [PHImageRequestOptionsVersion.unadjusted](https://developer.apple.com/documentation/photokit/phimagerequestoptionsversion/unadjusted)

|  | Declaration |
| --- | --- |
| From | ``` case Unadjusted ``` |
| To | ``` case unadjusted ``` |

Modified [PHLivePhoto](https://developer.apple.com/documentation/photokit/phlivephoto)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHLivePhoto : NSObject, NSCopying, NSSecureCoding {     var size: CGSize { get }     class func requestLivePhotoWithResourceFileURLs(_ fileURLs: [NSURL], placeholderImage image: UIImage?, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, resultHandler resultHandler: (PHLivePhoto?, [NSObject : AnyObject]) -> Void) -> PHLivePhotoRequestID     class func cancelLivePhotoRequestWithRequestID(_ requestID: PHLivePhotoRequestID) } ``` | NSCopying, NSSecureCoding |
| To | ``` class PHLivePhoto : NSObject, NSCopying, NSSecureCoding {     var size: CGSize { get }     class func request(withResourceFileURLs fileURLs: [URL], placeholderImage image: UIImage?, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, resultHandler resultHandler: @escaping (PHLivePhoto?, [AnyHashable : Any]) -> Swift.Void) -> PHLivePhotoRequestID     class func cancelRequest(withRequestID requestID: PHLivePhotoRequestID)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHLivePhoto : CVarArg { } extension PHLivePhoto : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [PHLivePhoto.cancelRequest(withRequestID: PHLivePhotoRequestID) [class]](https://developer.apple.com/documentation/photokit/phlivephoto/1616436-cancellivephotorequestwithreques)

|  | Declaration |
| --- | --- |
| From | ``` class func cancelLivePhotoRequestWithRequestID(_ requestID: PHLivePhotoRequestID) ``` |
| To | ``` class func cancelRequest(withRequestID requestID: PHLivePhotoRequestID) ``` |

Modified [PHLivePhoto.request(withResourceFileURLs: [URL], placeholderImage: UIImage?, targetSize: CGSize, contentMode: PHImageContentMode, resultHandler: (PHLivePhoto?, [AnyHashable : Any]) -> Swift.Void) -> PHLivePhotoRequestID [class]](https://developer.apple.com/documentation/photokit/phlivephoto/1616434-requestlivephotowithresourcefile)

|  | Declaration |
| --- | --- |
| From | ``` class func requestLivePhotoWithResourceFileURLs(_ fileURLs: [NSURL], placeholderImage image: UIImage?, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, resultHandler resultHandler: (PHLivePhoto?, [NSObject : AnyObject]) -> Void) -> PHLivePhotoRequestID ``` |
| To | ``` class func request(withResourceFileURLs fileURLs: [URL], placeholderImage image: UIImage?, targetSize targetSize: CGSize, contentMode contentMode: PHImageContentMode, resultHandler resultHandler: @escaping (PHLivePhoto?, [AnyHashable : Any]) -> Swift.Void) -> PHLivePhotoRequestID ``` |

Modified [PHLivePhotoRequestOptions](https://developer.apple.com/documentation/photokit/phlivephotorequestoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHLivePhotoRequestOptions : NSObject, NSCopying {     var deliveryMode: PHImageRequestOptionsDeliveryMode     var networkAccessAllowed: Bool     var progressHandler: PHAssetImageProgressHandler? } ``` | NSCopying |
| To | ``` class PHLivePhotoRequestOptions : NSObject, NSCopying {     var version: PHImageRequestOptionsVersion     var deliveryMode: PHImageRequestOptionsDeliveryMode     var isNetworkAccessAllowed: Bool     var progressHandler: Photos.PHAssetImageProgressHandler?     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHLivePhotoRequestOptions : CVarArg { } extension PHLivePhotoRequestOptions : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [PHLivePhotoRequestOptions.isNetworkAccessAllowed](https://developer.apple.com/documentation/photokit/phlivephotorequestoptions/1616989-networkaccessallowed)

|  | Declaration |
| --- | --- |
| From | ``` var networkAccessAllowed: Bool ``` |
| To | ``` var isNetworkAccessAllowed: Bool ``` |

Modified [PHLivePhotoRequestOptions.progressHandler](https://developer.apple.com/documentation/photokit/phlivephotorequestoptions/1616961-progresshandler)

|  | Declaration |
| --- | --- |
| From | ``` var progressHandler: PHAssetImageProgressHandler? ``` |
| To | ``` var progressHandler: Photos.PHAssetImageProgressHandler? ``` |

Modified [PHObject](https://developer.apple.com/documentation/photokit/phobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHObject : NSObject, NSCopying {     var localIdentifier: String { get } } ``` | NSCopying |
| To | ``` class PHObject : NSObject, NSCopying {     var localIdentifier: String { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHObject : CVarArg { } extension PHObject : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [PHObjectChangeDetails](https://developer.apple.com/documentation/photokit/phobjectchangedetails)

|  | Declaration | Protocols | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` class PHObjectChangeDetails : NSObject {     var objectBeforeChanges: PHObject { get }     var objectAfterChanges: PHObject? { get }     var assetContentChanged: Bool { get }     var objectWasDeleted: Bool { get } } ``` | -- | ```  ``` | -- |
| To | ``` class PHObjectChangeDetails<ObjectType : PHObject> : NSObject {     var objectBeforeChanges: PHObject { get }     var objectAfterChanges: PHObject? { get }     var assetContentChanged: Bool { get }     var objectWasDeleted: Bool { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHObjectChangeDetails : CVarArg { } extension PHObjectChangeDetails : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable | ``` ObjectType : PHObject ``` | ObjectType |

Modified [PHPhotoLibrary](https://developer.apple.com/documentation/photokit/phphotolibrary)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHPhotoLibrary : NSObject {     class func sharedPhotoLibrary() -> PHPhotoLibrary     class func authorizationStatus() -> PHAuthorizationStatus     class func requestAuthorization(_ handler: (PHAuthorizationStatus) -> Void)     func performChanges(_ changeBlock: dispatch_block_t, completionHandler completionHandler: ((Bool, NSError?) -> Void)?)     func performChangesAndWait(_ changeBlock: dispatch_block_t) throws     func registerChangeObserver(_ observer: PHPhotoLibraryChangeObserver)     func unregisterChangeObserver(_ observer: PHPhotoLibraryChangeObserver) } ``` | -- |
| To | ``` class PHPhotoLibrary : NSObject {     class func shared() -> PHPhotoLibrary     class func authorizationStatus() -> PHAuthorizationStatus     class func requestAuthorization(_ handler: @escaping (PHAuthorizationStatus) -> Swift.Void)     func performChanges(_ changeBlock: @escaping () -> Swift.Void, completionHandler completionHandler: (@escaping (Bool, Error?) -> Swift.Void)? = nil)     func performChangesAndWait(_ changeBlock: @escaping () -> Swift.Void) throws     func register(_ observer: PHPhotoLibraryChangeObserver)     func unregisterChangeObserver(_ observer: PHPhotoLibraryChangeObserver)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHPhotoLibrary : CVarArg { } extension PHPhotoLibrary : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PHPhotoLibrary.performChanges(_: () -> Swift.Void, completionHandler: ( (Bool, Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/photokit/phphotolibrary/1620743-performchanges)

|  | Declaration |
| --- | --- |
| From | ``` func performChanges(_ changeBlock: dispatch_block_t, completionHandler completionHandler: ((Bool, NSError?) -> Void)?) ``` |
| To | ``` func performChanges(_ changeBlock: @escaping () -> Swift.Void, completionHandler completionHandler: (@escaping (Bool, Error?) -> Swift.Void)? = nil) ``` |

Modified [PHPhotoLibrary.performChangesAndWait(_: () -> Swift.Void) throws](https://developer.apple.com/documentation/photokit/phphotolibrary/1620747-performchangesandwait)

|  | Declaration |
| --- | --- |
| From | ``` func performChangesAndWait(_ changeBlock: dispatch_block_t) throws ``` |
| To | ``` func performChangesAndWait(_ changeBlock: @escaping () -> Swift.Void) throws ``` |

Modified [PHPhotoLibrary.register(_: PHPhotoLibraryChangeObserver)](https://developer.apple.com/documentation/photokit/phphotolibrary/1620741-register)

|  | Declaration |
| --- | --- |
| From | ``` func registerChangeObserver(_ observer: PHPhotoLibraryChangeObserver) ``` |
| To | ``` func register(_ observer: PHPhotoLibraryChangeObserver) ``` |

Modified [PHPhotoLibrary.requestAuthorization(_: (PHAuthorizationStatus) -> Swift.Void) [class]](https://developer.apple.com/documentation/photokit/phphotolibrary/1620736-requestauthorization)

|  | Declaration |
| --- | --- |
| From | ``` class func requestAuthorization(_ handler: (PHAuthorizationStatus) -> Void) ``` |
| To | ``` class func requestAuthorization(_ handler: @escaping (PHAuthorizationStatus) -> Swift.Void) ``` |

Modified [PHPhotoLibrary.shared() -> PHPhotoLibrary [class]](https://developer.apple.com/documentation/photokit/phphotolibrary/1620737-sharedphotolibrary)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedPhotoLibrary() -> PHPhotoLibrary ``` |
| To | ``` class func shared() -> PHPhotoLibrary ``` |

Modified [PHVideoRequestOptions](https://developer.apple.com/documentation/photokit/phvideorequestoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHVideoRequestOptions : NSObject {     var networkAccessAllowed: Bool     var version: PHVideoRequestOptionsVersion     var deliveryMode: PHVideoRequestOptionsDeliveryMode     var progressHandler: PHAssetVideoProgressHandler? } ``` | -- |
| To | ``` class PHVideoRequestOptions : NSObject {     var isNetworkAccessAllowed: Bool     var version: PHVideoRequestOptionsVersion     var deliveryMode: PHVideoRequestOptionsDeliveryMode     var progressHandler: Photos.PHAssetVideoProgressHandler?     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHVideoRequestOptions : CVarArg { } extension PHVideoRequestOptions : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PHVideoRequestOptions.isNetworkAccessAllowed](https://developer.apple.com/documentation/photokit/phvideorequestoptions/1616931-isnetworkaccessallowed)

|  | Declaration |
| --- | --- |
| From | ``` var networkAccessAllowed: Bool ``` |
| To | ``` var isNetworkAccessAllowed: Bool ``` |

Modified [PHVideoRequestOptions.progressHandler](https://developer.apple.com/documentation/photokit/phvideorequestoptions/1616930-progresshandler)

|  | Declaration |
| --- | --- |
| From | ``` var progressHandler: PHAssetVideoProgressHandler? ``` |
| To | ``` var progressHandler: Photos.PHAssetVideoProgressHandler? ``` |

Modified [PHVideoRequestOptionsDeliveryMode [enum]](https://developer.apple.com/documentation/photokit/phvideorequestoptionsdeliverymode)

|  | Declaration |
| --- | --- |
| From | ``` enum PHVideoRequestOptionsDeliveryMode : Int {     case Automatic     case HighQualityFormat     case MediumQualityFormat     case FastFormat } ``` |
| To | ``` enum PHVideoRequestOptionsDeliveryMode : Int {     case automatic     case highQualityFormat     case mediumQualityFormat     case fastFormat } ``` |

Modified [PHVideoRequestOptionsDeliveryMode.automatic](https://developer.apple.com/documentation/photokit/phvideorequestoptionsdeliverymode/automatic)

|  | Declaration |
| --- | --- |
| From | ``` case Automatic ``` |
| To | ``` case automatic ``` |

Modified [PHVideoRequestOptionsDeliveryMode.fastFormat](https://developer.apple.com/documentation/photokit/phvideorequestoptionsdeliverymode/fastformat)

|  | Declaration |
| --- | --- |
| From | ``` case FastFormat ``` |
| To | ``` case fastFormat ``` |

Modified [PHVideoRequestOptionsDeliveryMode.highQualityFormat](https://developer.apple.com/documentation/photokit/phvideorequestoptionsdeliverymode/highqualityformat)

|  | Declaration |
| --- | --- |
| From | ``` case HighQualityFormat ``` |
| To | ``` case highQualityFormat ``` |

Modified [PHVideoRequestOptionsDeliveryMode.mediumQualityFormat](https://developer.apple.com/documentation/photokit/phvideorequestoptionsdeliverymode/phvideorequestoptionsdeliverymodemediumqualityformat)

|  | Declaration |
| --- | --- |
| From | ``` case MediumQualityFormat ``` |
| To | ``` case mediumQualityFormat ``` |

Modified [PHVideoRequestOptionsVersion [enum]](https://developer.apple.com/documentation/photokit/phvideorequestoptionsversion)

|  | Declaration |
| --- | --- |
| From | ``` enum PHVideoRequestOptionsVersion : Int {     case Current     case Original } ``` |
| To | ``` enum PHVideoRequestOptionsVersion : Int {     case current     case original } ``` |

Modified [PHVideoRequestOptionsVersion.current](https://developer.apple.com/documentation/photokit/phvideorequestoptionsversion/current)

|  | Declaration |
| --- | --- |
| From | ``` case Current ``` |
| To | ``` case current ``` |

Modified [PHVideoRequestOptionsVersion.original](https://developer.apple.com/documentation/photokit/phvideorequestoptionsversion/phvideorequestoptionsversionoriginal)

|  | Declaration |
| --- | --- |
| From | ``` case Original ``` |
| To | ``` case original ``` |

Modified [PHAssetImageProgressHandler](https://developer.apple.com/documentation/photokit/phassetimageprogresshandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias PHAssetImageProgressHandler = (Double, NSError?, UnsafeMutablePointer<ObjCBool>, [NSObject : AnyObject]?) -> Void ``` |
| To | ``` typealias PHAssetImageProgressHandler = (Double, Error?, UnsafeMutablePointer<ObjCBool>, [AnyHashable : Any]?) -> Swift.Void ``` |

Modified [PHAssetResourceProgressHandler](https://developer.apple.com/documentation/photokit/phassetresourceprogresshandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias PHAssetResourceProgressHandler = (Double) -> Void ``` |
| To | ``` typealias PHAssetResourceProgressHandler = (Double) -> Swift.Void ``` |

Modified [PHAssetVideoProgressHandler](https://developer.apple.com/documentation/photokit/phassetvideoprogresshandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias PHAssetVideoProgressHandler = (Double, NSError?, UnsafeMutablePointer<ObjCBool>, [NSObject : AnyObject]?) -> Void ``` |
| To | ``` typealias PHAssetVideoProgressHandler = (Double, Error?, UnsafeMutablePointer<ObjCBool>, [AnyHashable : Any]?) -> Swift.Void ``` |

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
