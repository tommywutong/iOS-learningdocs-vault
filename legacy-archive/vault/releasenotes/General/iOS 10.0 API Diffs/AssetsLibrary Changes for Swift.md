---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/AssetsLibrary.html
archived_at: '2026-07-18T02:55:06.557001Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# AssetsLibrary Changes for Swift

### AssetsLibrary

Removed ALAssetsLibrary.enumerateGroupsWithTypes(_: UInt32, usingBlock: ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock: ALAssetsLibraryAccessFailureBlock!)Added [ALAssetsLibrary.enumerateGroupsWithTypes(_: UInt32, usingBlock: AssetsLibrary.ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock: AssetsLibrary.ALAssetsLibraryAccessFailureBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1779575-enumerategroupswithtypes)Modified [ALAsset](https://developer.apple.com/documentation/assetslibrary/alasset)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ALAsset : NSObject {     func valueForProperty(_ property: String!) -> AnyObject!     func defaultRepresentation() -> ALAssetRepresentation!     func representationForUTI(_ representationUTI: String!) -> ALAssetRepresentation!     func thumbnail() -> Unmanaged<CGImage>!     func aspectRatioThumbnail() -> Unmanaged<CGImage>!     func writeModifiedImageDataToSavedPhotosAlbum(_ imageData: NSData!, metadata metadata: [NSObject : AnyObject]!, completionBlock completionBlock: ALAssetsLibraryWriteImageCompletionBlock!)     func writeModifiedVideoAtPathToSavedPhotosAlbum(_ videoPathURL: NSURL!, completionBlock completionBlock: ALAssetsLibraryWriteVideoCompletionBlock!)     var originalAsset: ALAsset! { get }     var editable: Bool { get }     func setImageData(_ imageData: NSData!, metadata metadata: [NSObject : AnyObject]!, completionBlock completionBlock: ALAssetsLibraryWriteImageCompletionBlock!)     func setVideoAtPath(_ videoPathURL: NSURL!, completionBlock completionBlock: ALAssetsLibraryWriteVideoCompletionBlock!) } ``` | -- |
| To | ``` class ALAsset : NSObject {     func value(forProperty property: String!) -> Any!     func defaultRepresentation() -> ALAssetRepresentation!     func representation(forUTI representationUTI: String!) -> ALAssetRepresentation!     func thumbnail() -> Unmanaged<CGImage>!     func aspectRatioThumbnail() -> Unmanaged<CGImage>!     func writeModifiedImageData(toSavedPhotosAlbum imageData: Data!, metadata metadata: [AnyHashable : Any]!, completionBlock completionBlock: AssetsLibrary.ALAssetsLibraryWriteImageCompletionBlock!)     func writeModifiedVideoAtPath(toSavedPhotosAlbum videoPathURL: URL!, completionBlock completionBlock: AssetsLibrary.ALAssetsLibraryWriteVideoCompletionBlock!)     var original: ALAsset! { get }     var isEditable: Bool { get }     func setImageData(_ imageData: Data!, metadata metadata: [AnyHashable : Any]!, completionBlock completionBlock: AssetsLibrary.ALAssetsLibraryWriteImageCompletionBlock!)     func setVideoAtPath(_ videoPathURL: URL!, completionBlock completionBlock: AssetsLibrary.ALAssetsLibraryWriteVideoCompletionBlock!)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ALAsset : CVarArg { } extension ALAsset : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [ALAsset.isEditable](https://developer.apple.com/documentation/assetslibrary/alasset/1615867-iseditable)

|  | Declaration |
| --- | --- |
| From | ``` var editable: Bool { get } ``` |
| To | ``` var isEditable: Bool { get } ``` |

Modified [ALAsset.original](https://developer.apple.com/documentation/assetslibrary/alasset/1615857-originalasset)

|  | Declaration |
| --- | --- |
| From | ``` var originalAsset: ALAsset! { get } ``` |
| To | ``` var original: ALAsset! { get } ``` |

Modified [ALAsset.representation(forUTI: String!) -> ALAssetRepresentation!](https://developer.apple.com/documentation/assetslibrary/alasset/1615859-representation)

|  | Declaration |
| --- | --- |
| From | ``` func representationForUTI(_ representationUTI: String!) -> ALAssetRepresentation! ``` |
| To | ``` func representation(forUTI representationUTI: String!) -> ALAssetRepresentation! ``` |

Modified [ALAsset.setImageData(_: Data!, metadata: [AnyHashable : Any]!, completionBlock: AssetsLibrary.ALAssetsLibraryWriteImageCompletionBlock!)](https://developer.apple.com/documentation/assetslibrary/alasset/1615874-setimagedata)

|  | Declaration |
| --- | --- |
| From | ``` func setImageData(_ imageData: NSData!, metadata metadata: [NSObject : AnyObject]!, completionBlock completionBlock: ALAssetsLibraryWriteImageCompletionBlock!) ``` |
| To | ``` func setImageData(_ imageData: Data!, metadata metadata: [AnyHashable : Any]!, completionBlock completionBlock: AssetsLibrary.ALAssetsLibraryWriteImageCompletionBlock!) ``` |

Modified [ALAsset.setVideoAtPath(_: URL!, completionBlock: AssetsLibrary.ALAssetsLibraryWriteVideoCompletionBlock!)](https://developer.apple.com/documentation/assetslibrary/alasset/1615880-setvideoatpath)

|  | Declaration |
| --- | --- |
| From | ``` func setVideoAtPath(_ videoPathURL: NSURL!, completionBlock completionBlock: ALAssetsLibraryWriteVideoCompletionBlock!) ``` |
| To | ``` func setVideoAtPath(_ videoPathURL: URL!, completionBlock completionBlock: AssetsLibrary.ALAssetsLibraryWriteVideoCompletionBlock!) ``` |

Modified [ALAsset.value(forProperty: String!) -> Any!](https://developer.apple.com/documentation/assetslibrary/alasset/1615862-valueforproperty)

|  | Declaration |
| --- | --- |
| From | ``` func valueForProperty(_ property: String!) -> AnyObject! ``` |
| To | ``` func value(forProperty property: String!) -> Any! ``` |

Modified [ALAsset.writeModifiedImageData(toSavedPhotosAlbum: Data!, metadata: [AnyHashable : Any]!, completionBlock: AssetsLibrary.ALAssetsLibraryWriteImageCompletionBlock!)](https://developer.apple.com/documentation/assetslibrary/alasset/1615863-writemodifiedimagedatatosavedpho)

|  | Declaration |
| --- | --- |
| From | ``` func writeModifiedImageDataToSavedPhotosAlbum(_ imageData: NSData!, metadata metadata: [NSObject : AnyObject]!, completionBlock completionBlock: ALAssetsLibraryWriteImageCompletionBlock!) ``` |
| To | ``` func writeModifiedImageData(toSavedPhotosAlbum imageData: Data!, metadata metadata: [AnyHashable : Any]!, completionBlock completionBlock: AssetsLibrary.ALAssetsLibraryWriteImageCompletionBlock!) ``` |

Modified [ALAsset.writeModifiedVideoAtPath(toSavedPhotosAlbum: URL!, completionBlock: AssetsLibrary.ALAssetsLibraryWriteVideoCompletionBlock!)](https://developer.apple.com/documentation/assetslibrary/alasset/1615878-writemodifiedvideoatpathtosavedp)

|  | Declaration |
| --- | --- |
| From | ``` func writeModifiedVideoAtPathToSavedPhotosAlbum(_ videoPathURL: NSURL!, completionBlock completionBlock: ALAssetsLibraryWriteVideoCompletionBlock!) ``` |
| To | ``` func writeModifiedVideoAtPath(toSavedPhotosAlbum videoPathURL: URL!, completionBlock completionBlock: AssetsLibrary.ALAssetsLibraryWriteVideoCompletionBlock!) ``` |

Modified [ALAssetOrientation [enum]](https://developer.apple.com/documentation/assetslibrary/alassetorientation)

|  | Declaration |
| --- | --- |
| From | ``` enum ALAssetOrientation : Int {     case Up     case Down     case Left     case Right     case UpMirrored     case DownMirrored     case LeftMirrored     case RightMirrored } ``` |
| To | ``` enum ALAssetOrientation : Int {     case up     case down     case left     case right     case upMirrored     case downMirrored     case leftMirrored     case rightMirrored } ``` |

Modified [ALAssetOrientation.down](https://developer.apple.com/documentation/assetslibrary/alassetorientation/down)

|  | Declaration |
| --- | --- |
| From | ``` case Down ``` |
| To | ``` case down ``` |

Modified [ALAssetOrientation.downMirrored](https://developer.apple.com/documentation/assetslibrary/alassetorientation/alassetorientationdownmirrored)

|  | Declaration |
| --- | --- |
| From | ``` case DownMirrored ``` |
| To | ``` case downMirrored ``` |

Modified [ALAssetOrientation.left](https://developer.apple.com/documentation/assetslibrary/alassetorientation/left)

|  | Declaration |
| --- | --- |
| From | ``` case Left ``` |
| To | ``` case left ``` |

Modified [ALAssetOrientation.leftMirrored](https://developer.apple.com/documentation/assetslibrary/alassetorientation/leftmirrored)

|  | Declaration |
| --- | --- |
| From | ``` case LeftMirrored ``` |
| To | ``` case leftMirrored ``` |

Modified [ALAssetOrientation.right](https://developer.apple.com/documentation/assetslibrary/alassetorientation/alassetorientationright)

|  | Declaration |
| --- | --- |
| From | ``` case Right ``` |
| To | ``` case right ``` |

Modified [ALAssetOrientation.rightMirrored](https://developer.apple.com/documentation/assetslibrary/alassetorientation/rightmirrored)

|  | Declaration |
| --- | --- |
| From | ``` case RightMirrored ``` |
| To | ``` case rightMirrored ``` |

Modified [ALAssetOrientation.up](https://developer.apple.com/documentation/assetslibrary/alassetorientation/up)

|  | Declaration |
| --- | --- |
| From | ``` case Up ``` |
| To | ``` case up ``` |

Modified [ALAssetOrientation.upMirrored](https://developer.apple.com/documentation/assetslibrary/alassetorientation/alassetorientationupmirrored)

|  | Declaration |
| --- | --- |
| From | ``` case UpMirrored ``` |
| To | ``` case upMirrored ``` |

Modified [ALAssetRepresentation](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ALAssetRepresentation : NSObject {     func UTI() -> String!     func dimensions() -> CGSize     func size() -> Int64     func getBytes(_ buffer: UnsafeMutablePointer<UInt8>, fromOffset offset: Int64, length length: Int, error error: NSErrorPointer) -> Int     func fullResolutionImage() -> Unmanaged<CGImage>!     func CGImageWithOptions(_ options: [NSObject : AnyObject]!) -> Unmanaged<CGImage>!     func fullScreenImage() -> Unmanaged<CGImage>!     func url() -> NSURL!     func metadata() -> [NSObject : AnyObject]!     func orientation() -> ALAssetOrientation     func scale() -> Float     func filename() -> String! } ``` | -- |
| To | ``` class ALAssetRepresentation : NSObject {     func uti() -> String!     func dimensions() -> CGSize     func size() -> Int64     func getBytes(_ buffer: UnsafeMutablePointer<UInt8>!, fromOffset offset: Int64, length length: Int, error error: NSErrorPointer) -> Int     func fullResolutionImage() -> Unmanaged<CGImage>!     func cgImage(options options: [AnyHashable : Any]! = [:]) -> Unmanaged<CGImage>!     func fullScreenImage() -> Unmanaged<CGImage>!     func url() -> URL!     func metadata() -> [AnyHashable : Any]!     func orientation() -> ALAssetOrientation     func scale() -> Float     func filename() -> String!     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ALAssetRepresentation : CVarArg { } extension ALAssetRepresentation : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [ALAssetRepresentation.cgImage(options: [AnyHashable : Any]!) -> Unmanaged<CGImage>!](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/1617855-cgimage)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageWithOptions(_ options: [NSObject : AnyObject]!) -> Unmanaged<CGImage>! ``` |
| To | ``` func cgImage(options options: [AnyHashable : Any]! = [:]) -> Unmanaged<CGImage>! ``` |

Modified [ALAssetRepresentation.getBytes(_: UnsafeMutablePointer<UInt8>!, fromOffset: Int64, length: Int, error: NSErrorPointer) -> Int](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/1617860-getbytes)

|  | Declaration |
| --- | --- |
| From | ``` func getBytes(_ buffer: UnsafeMutablePointer<UInt8>, fromOffset offset: Int64, length length: Int, error error: NSErrorPointer) -> Int ``` |
| To | ``` func getBytes(_ buffer: UnsafeMutablePointer<UInt8>!, fromOffset offset: Int64, length length: Int, error error: NSErrorPointer) -> Int ``` |

Modified [ALAssetRepresentation.metadata() -> [AnyHashable : Any]!](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/1617859-metadata)

|  | Declaration |
| --- | --- |
| From | ``` func metadata() -> [NSObject : AnyObject]! ``` |
| To | ``` func metadata() -> [AnyHashable : Any]! ``` |

Modified [ALAssetRepresentation.url() -> URL!](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/1617853-url)

|  | Declaration |
| --- | --- |
| From | ``` func url() -> NSURL! ``` |
| To | ``` func url() -> URL! ``` |

Modified [ALAssetRepresentation.uti() -> String!](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/1617865-uti)

|  | Declaration |
| --- | --- |
| From | ``` func UTI() -> String! ``` |
| To | ``` func uti() -> String! ``` |

Modified [ALAssetsFilter](https://developer.apple.com/documentation/assetslibrary/alassetsfilter)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ALAssetsFilter : NSObject {     class func allPhotos() -> ALAssetsFilter!     class func allVideos() -> ALAssetsFilter!     class func allAssets() -> ALAssetsFilter! } ``` | -- |
| To | ``` class ALAssetsFilter : NSObject {     class func allPhotos() -> ALAssetsFilter!     class func allVideos() -> ALAssetsFilter!     class func allAssets() -> ALAssetsFilter!     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ALAssetsFilter : CVarArg { } extension ALAssetsFilter : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [ALAssetsGroup](https://developer.apple.com/documentation/assetslibrary/alassetsgroup)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ALAssetsGroup : NSObject {     func valueForProperty(_ property: String!) -> AnyObject!     func posterImage() -> Unmanaged<CGImage>!     func setAssetsFilter(_ filter: ALAssetsFilter!)     func numberOfAssets() -> Int     func enumerateAssetsUsingBlock(_ enumerationBlock: ALAssetsGroupEnumerationResultsBlock!)     func enumerateAssetsWithOptions(_ options: NSEnumerationOptions, usingBlock enumerationBlock: ALAssetsGroupEnumerationResultsBlock!)     func enumerateAssetsAtIndexes(_ indexSet: NSIndexSet!, options options: NSEnumerationOptions, usingBlock enumerationBlock: ALAssetsGroupEnumerationResultsBlock!)     var editable: Bool { get }     func addAsset(_ asset: ALAsset!) -> Bool } ``` | -- |
| To | ``` class ALAssetsGroup : NSObject {     func value(forProperty property: String!) -> Any!     func posterImage() -> Unmanaged<CGImage>!     func setAssetsFilter(_ filter: ALAssetsFilter!)     func numberOfAssets() -> Int     func enumerateAssets(_ enumerationBlock: AssetsLibrary.ALAssetsGroupEnumerationResultsBlock!)     func enumerateAssets(options options: NSEnumerationOptions = [], using enumerationBlock: AssetsLibrary.ALAssetsGroupEnumerationResultsBlock!)     func enumerateAssets(at indexSet: IndexSet!, options options: NSEnumerationOptions = [], using enumerationBlock: AssetsLibrary.ALAssetsGroupEnumerationResultsBlock!)     var isEditable: Bool { get }     func add(_ asset: ALAsset!) -> Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ALAssetsGroup : CVarArg { } extension ALAssetsGroup : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [ALAssetsGroup.add(_: ALAsset!) -> Bool](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/1621964-addasset)

|  | Declaration |
| --- | --- |
| From | ``` func addAsset(_ asset: ALAsset!) -> Bool ``` |
| To | ``` func add(_ asset: ALAsset!) -> Bool ``` |

Modified [ALAssetsGroup.enumerateAssets(_: AssetsLibrary.ALAssetsGroupEnumerationResultsBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/1621968-enumerateassets)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateAssetsUsingBlock(_ enumerationBlock: ALAssetsGroupEnumerationResultsBlock!) ``` |
| To | ``` func enumerateAssets(_ enumerationBlock: AssetsLibrary.ALAssetsGroupEnumerationResultsBlock!) ``` |

Modified [ALAssetsGroup.enumerateAssets(at: IndexSet!, options: NSEnumerationOptions, using: AssetsLibrary.ALAssetsGroupEnumerationResultsBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/1621966-enumerateassetsatindexes)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateAssetsAtIndexes(_ indexSet: NSIndexSet!, options options: NSEnumerationOptions, usingBlock enumerationBlock: ALAssetsGroupEnumerationResultsBlock!) ``` |
| To | ``` func enumerateAssets(at indexSet: IndexSet!, options options: NSEnumerationOptions = [], using enumerationBlock: AssetsLibrary.ALAssetsGroupEnumerationResultsBlock!) ``` |

Modified [ALAssetsGroup.enumerateAssets(options: NSEnumerationOptions, using: AssetsLibrary.ALAssetsGroupEnumerationResultsBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/1621960-enumerateassetswithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateAssetsWithOptions(_ options: NSEnumerationOptions, usingBlock enumerationBlock: ALAssetsGroupEnumerationResultsBlock!) ``` |
| To | ``` func enumerateAssets(options options: NSEnumerationOptions = [], using enumerationBlock: AssetsLibrary.ALAssetsGroupEnumerationResultsBlock!) ``` |

Modified [ALAssetsGroup.isEditable](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/1621969-iseditable)

|  | Declaration |
| --- | --- |
| From | ``` var editable: Bool { get } ``` |
| To | ``` var isEditable: Bool { get } ``` |

Modified [ALAssetsGroup.value(forProperty: String!) -> Any!](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/1621971-value)

|  | Declaration |
| --- | --- |
| From | ``` func valueForProperty(_ property: String!) -> AnyObject! ``` |
| To | ``` func value(forProperty property: String!) -> Any! ``` |

Modified [ALAssetsLibrary](https://developer.apple.com/documentation/assetslibrary/alassetslibrary)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ALAssetsLibrary : NSObject {     func enumerateGroupsWithTypes(_ types: ALAssetsGroupType, usingBlock enumerationBlock: ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!)     func assetForURL(_ assetURL: NSURL!, resultBlock resultBlock: ALAssetsLibraryAssetForURLResultBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!)     func groupForURL(_ groupURL: NSURL!, resultBlock resultBlock: ALAssetsLibraryGroupResultBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!)     func addAssetsGroupAlbumWithName(_ name: String!, resultBlock resultBlock: ALAssetsLibraryGroupResultBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!)     func writeImageToSavedPhotosAlbum(_ imageRef: CGImage!, orientation orientation: ALAssetOrientation, completionBlock completionBlock: ALAssetsLibraryWriteImageCompletionBlock!)     func writeImageToSavedPhotosAlbum(_ imageRef: CGImage!, metadata metadata: [NSObject : AnyObject]!, completionBlock completionBlock: ALAssetsLibraryWriteImageCompletionBlock!)     func writeImageDataToSavedPhotosAlbum(_ imageData: NSData!, metadata metadata: [NSObject : AnyObject]!, completionBlock completionBlock: ALAssetsLibraryWriteImageCompletionBlock!)     func writeVideoAtPathToSavedPhotosAlbum(_ videoPathURL: NSURL!, completionBlock completionBlock: ALAssetsLibraryWriteVideoCompletionBlock!)     func videoAtPathIsCompatibleWithSavedPhotosAlbum(_ videoPathURL: NSURL!) -> Bool     class func authorizationStatus() -> ALAuthorizationStatus     class func disableSharedPhotoStreamsSupport() } extension ALAssetsLibrary {     @nonobjc func enumerateGroupsWithTypes(_ types: UInt32, usingBlock enumerationBlock: ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!) } extension ALAssetsLibrary {     @nonobjc func enumerateGroupsWithTypes(_ types: UInt32, usingBlock enumerationBlock: ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!) } ``` | -- |
| To | ``` class ALAssetsLibrary : NSObject {     func enumerateGroups(withTypes types: ALAssetsGroupType, using enumerationBlock: AssetsLibrary.ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock failureBlock: AssetsLibrary.ALAssetsLibraryAccessFailureBlock!)     func asset(for assetURL: URL!, resultBlock resultBlock: AssetsLibrary.ALAssetsLibraryAssetForURLResultBlock!, failureBlock failureBlock: AssetsLibrary.ALAssetsLibraryAccessFailureBlock!)     func group(for groupURL: URL!, resultBlock resultBlock: AssetsLibrary.ALAssetsLibraryGroupResultBlock!, failureBlock failureBlock: AssetsLibrary.ALAssetsLibraryAccessFailureBlock!)     func addAssetsGroupAlbum(withName name: String!, resultBlock resultBlock: AssetsLibrary.ALAssetsLibraryGroupResultBlock!, failureBlock failureBlock: AssetsLibrary.ALAssetsLibraryAccessFailureBlock!)     func writeImage(toSavedPhotosAlbum imageRef: CGImage!, orientation orientation: ALAssetOrientation, completionBlock completionBlock: AssetsLibrary.ALAssetsLibraryWriteImageCompletionBlock!)     func writeImage(toSavedPhotosAlbum imageRef: CGImage!, metadata metadata: [AnyHashable : Any]!, completionBlock completionBlock: AssetsLibrary.ALAssetsLibraryWriteImageCompletionBlock!)     func writeImageData(toSavedPhotosAlbum imageData: Data!, metadata metadata: [AnyHashable : Any]!, completionBlock completionBlock: AssetsLibrary.ALAssetsLibraryWriteImageCompletionBlock!)     func writeVideoAtPath(toSavedPhotosAlbum videoPathURL: URL!, completionBlock completionBlock: AssetsLibrary.ALAssetsLibraryWriteVideoCompletionBlock!)     func videoAtPathIs(compatibleWithSavedPhotosAlbum videoPathURL: URL!) -> Bool     class func authorizationStatus() -> ALAuthorizationStatus     class func disableSharedPhotoStreamsSupport()     @nonobjc func enumerateGroupsWithTypes(_ types: UInt32, usingBlock enumerationBlock: AssetsLibrary.ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock failureBlock: AssetsLibrary.ALAssetsLibraryAccessFailureBlock!)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ALAssetsLibrary : CVarArg { } extension ALAssetsLibrary : Equatable, Hashable {     var hashValue: Int { get } } extension ALAssetsLibrary {     @nonobjc func enumerateGroupsWithTypes(_ types: UInt32, usingBlock enumerationBlock: AssetsLibrary.ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock failureBlock: AssetsLibrary.ALAssetsLibraryAccessFailureBlock!) } ``` | CVarArg, Equatable, Hashable |

Modified [ALAssetsLibrary.addAssetsGroupAlbum(withName: String!, resultBlock: AssetsLibrary.ALAssetsLibraryGroupResultBlock!, failureBlock: AssetsLibrary.ALAssetsLibraryAccessFailureBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617872-addassetsgroupalbumwithname)

|  | Declaration |
| --- | --- |
| From | ``` func addAssetsGroupAlbumWithName(_ name: String!, resultBlock resultBlock: ALAssetsLibraryGroupResultBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!) ``` |
| To | ``` func addAssetsGroupAlbum(withName name: String!, resultBlock resultBlock: AssetsLibrary.ALAssetsLibraryGroupResultBlock!, failureBlock failureBlock: AssetsLibrary.ALAssetsLibraryAccessFailureBlock!) ``` |

Modified [ALAssetsLibrary.asset(for: URL!, resultBlock: AssetsLibrary.ALAssetsLibraryAssetForURLResultBlock!, failureBlock: AssetsLibrary.ALAssetsLibraryAccessFailureBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617909-assetforurl)

|  | Declaration |
| --- | --- |
| From | ``` func assetForURL(_ assetURL: NSURL!, resultBlock resultBlock: ALAssetsLibraryAssetForURLResultBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!) ``` |
| To | ``` func asset(for assetURL: URL!, resultBlock resultBlock: AssetsLibrary.ALAssetsLibraryAssetForURLResultBlock!, failureBlock failureBlock: AssetsLibrary.ALAssetsLibraryAccessFailureBlock!) ``` |

Modified [ALAssetsLibrary.enumerateGroups(withTypes: ALAssetsGroupType, using: AssetsLibrary.ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock: AssetsLibrary.ALAssetsLibraryAccessFailureBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617900-enumerategroupswithtypes)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateGroupsWithTypes(_ types: ALAssetsGroupType, usingBlock enumerationBlock: ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!) ``` |
| To | ``` func enumerateGroups(withTypes types: ALAssetsGroupType, using enumerationBlock: AssetsLibrary.ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock failureBlock: AssetsLibrary.ALAssetsLibraryAccessFailureBlock!) ``` |

Modified [ALAssetsLibrary.group(for: URL!, resultBlock: AssetsLibrary.ALAssetsLibraryGroupResultBlock!, failureBlock: AssetsLibrary.ALAssetsLibraryAccessFailureBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617907-groupforurl)

|  | Declaration |
| --- | --- |
| From | ``` func groupForURL(_ groupURL: NSURL!, resultBlock resultBlock: ALAssetsLibraryGroupResultBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!) ``` |
| To | ``` func group(for groupURL: URL!, resultBlock resultBlock: AssetsLibrary.ALAssetsLibraryGroupResultBlock!, failureBlock failureBlock: AssetsLibrary.ALAssetsLibraryAccessFailureBlock!) ``` |

Modified [ALAssetsLibrary.videoAtPathIs(compatibleWithSavedPhotosAlbum: URL!) -> Bool](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617920-videoatpathiscompatiblewithsaved)

|  | Declaration |
| --- | --- |
| From | ``` func videoAtPathIsCompatibleWithSavedPhotosAlbum(_ videoPathURL: NSURL!) -> Bool ``` |
| To | ``` func videoAtPathIs(compatibleWithSavedPhotosAlbum videoPathURL: URL!) -> Bool ``` |

Modified [ALAssetsLibrary.writeImage(toSavedPhotosAlbum: CGImage!, metadata: [AnyHashable : Any]!, completionBlock: AssetsLibrary.ALAssetsLibraryWriteImageCompletionBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617898-writeimagetosavedphotosalbum)

|  | Declaration |
| --- | --- |
| From | ``` func writeImageToSavedPhotosAlbum(_ imageRef: CGImage!, metadata metadata: [NSObject : AnyObject]!, completionBlock completionBlock: ALAssetsLibraryWriteImageCompletionBlock!) ``` |
| To | ``` func writeImage(toSavedPhotosAlbum imageRef: CGImage!, metadata metadata: [AnyHashable : Any]!, completionBlock completionBlock: AssetsLibrary.ALAssetsLibraryWriteImageCompletionBlock!) ``` |

Modified [ALAssetsLibrary.writeImage(toSavedPhotosAlbum: CGImage!, orientation: ALAssetOrientation, completionBlock: AssetsLibrary.ALAssetsLibraryWriteImageCompletionBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617913-writeimagetosavedphotosalbum)

|  | Declaration |
| --- | --- |
| From | ``` func writeImageToSavedPhotosAlbum(_ imageRef: CGImage!, orientation orientation: ALAssetOrientation, completionBlock completionBlock: ALAssetsLibraryWriteImageCompletionBlock!) ``` |
| To | ``` func writeImage(toSavedPhotosAlbum imageRef: CGImage!, orientation orientation: ALAssetOrientation, completionBlock completionBlock: AssetsLibrary.ALAssetsLibraryWriteImageCompletionBlock!) ``` |

Modified [ALAssetsLibrary.writeImageData(toSavedPhotosAlbum: Data!, metadata: [AnyHashable : Any]!, completionBlock: AssetsLibrary.ALAssetsLibraryWriteImageCompletionBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617926-writeimagedata)

|  | Declaration |
| --- | --- |
| From | ``` func writeImageDataToSavedPhotosAlbum(_ imageData: NSData!, metadata metadata: [NSObject : AnyObject]!, completionBlock completionBlock: ALAssetsLibraryWriteImageCompletionBlock!) ``` |
| To | ``` func writeImageData(toSavedPhotosAlbum imageData: Data!, metadata metadata: [AnyHashable : Any]!, completionBlock completionBlock: AssetsLibrary.ALAssetsLibraryWriteImageCompletionBlock!) ``` |

Modified [ALAssetsLibrary.writeVideoAtPath(toSavedPhotosAlbum: URL!, completionBlock: AssetsLibrary.ALAssetsLibraryWriteVideoCompletionBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617921-writevideoatpathtosavedphotosalb)

|  | Declaration |
| --- | --- |
| From | ``` func writeVideoAtPathToSavedPhotosAlbum(_ videoPathURL: NSURL!, completionBlock completionBlock: ALAssetsLibraryWriteVideoCompletionBlock!) ``` |
| To | ``` func writeVideoAtPath(toSavedPhotosAlbum videoPathURL: URL!, completionBlock completionBlock: AssetsLibrary.ALAssetsLibraryWriteVideoCompletionBlock!) ``` |

Modified [ALAuthorizationStatus [enum]](https://developer.apple.com/documentation/assetslibrary/alauthorizationstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum ALAuthorizationStatus : Int {     case NotDetermined     case Restricted     case Denied     case Authorized } ``` |
| To | ``` enum ALAuthorizationStatus : Int {     case notDetermined     case restricted     case denied     case authorized } ``` |

Modified [ALAuthorizationStatus.authorized](https://developer.apple.com/documentation/assetslibrary/alauthorizationstatus/authorized)

|  | Declaration |
| --- | --- |
| From | ``` case Authorized ``` |
| To | ``` case authorized ``` |

Modified [ALAuthorizationStatus.denied](https://developer.apple.com/documentation/assetslibrary/alauthorizationstatus/alauthorizationstatusdenied)

|  | Declaration |
| --- | --- |
| From | ``` case Denied ``` |
| To | ``` case denied ``` |

Modified [ALAuthorizationStatus.notDetermined](https://developer.apple.com/documentation/assetslibrary/alauthorizationstatus/notdetermined)

|  | Declaration |
| --- | --- |
| From | ``` case NotDetermined ``` |
| To | ``` case notDetermined ``` |

Modified [ALAuthorizationStatus.restricted](https://developer.apple.com/documentation/assetslibrary/alauthorizationstatus/alauthorizationstatusrestricted)

|  | Declaration |
| --- | --- |
| From | ``` case Restricted ``` |
| To | ``` case restricted ``` |

Modified [NSNotification.Name.ALAssetsLibraryChanged](https://developer.apple.com/documentation/foundation/nsnotification/name/1617908-alassetslibrarychanged)

|  | Name | Declaration |
| --- | --- | --- |
| From | ALAssetsLibraryChangedNotification | ``` let ALAssetsLibraryChangedNotification: String ``` |
| To | ALAssetsLibraryChanged | ``` static let ALAssetsLibraryChanged: NSNotification.Name ``` |

Modified [ALAssetsGroupEnumerationResultsBlock](https://developer.apple.com/documentation/assetslibrary/alassetsgroupenumerationresultsblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias ALAssetsGroupEnumerationResultsBlock = (ALAsset!, Int, UnsafeMutablePointer<ObjCBool>) -> Void ``` |
| To | ``` typealias ALAssetsGroupEnumerationResultsBlock = (ALAsset?, Int, UnsafeMutablePointer<ObjCBool>?) -> Swift.Void ``` |

Modified [ALAssetsLibraryAccessFailureBlock](https://developer.apple.com/documentation/assetslibrary/alassetslibraryaccessfailureblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias ALAssetsLibraryAccessFailureBlock = (NSError!) -> Void ``` |
| To | ``` typealias ALAssetsLibraryAccessFailureBlock = (Error?) -> Swift.Void ``` |

Modified [ALAssetsLibraryAssetForURLResultBlock](https://developer.apple.com/documentation/assetslibrary/alassetslibraryassetforurlresultblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias ALAssetsLibraryAssetForURLResultBlock = (ALAsset!) -> Void ``` |
| To | ``` typealias ALAssetsLibraryAssetForURLResultBlock = (ALAsset?) -> Swift.Void ``` |

Modified [ALAssetsLibraryGroupResultBlock](https://developer.apple.com/documentation/assetslibrary/alassetslibrarygroupresultblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias ALAssetsLibraryGroupResultBlock = (ALAssetsGroup!) -> Void ``` |
| To | ``` typealias ALAssetsLibraryGroupResultBlock = (ALAssetsGroup?) -> Swift.Void ``` |

Modified [ALAssetsLibraryGroupsEnumerationResultsBlock](https://developer.apple.com/documentation/assetslibrary/alassetslibrarygroupsenumerationresultsblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias ALAssetsLibraryGroupsEnumerationResultsBlock = (ALAssetsGroup!, UnsafeMutablePointer<ObjCBool>) -> Void ``` |
| To | ``` typealias ALAssetsLibraryGroupsEnumerationResultsBlock = (ALAssetsGroup?, UnsafeMutablePointer<ObjCBool>?) -> Swift.Void ``` |

Modified [ALAssetsLibraryWriteImageCompletionBlock](https://developer.apple.com/documentation/assetslibrary/alassetslibrarywriteimagecompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias ALAssetsLibraryWriteImageCompletionBlock = (NSURL!, NSError!) -> Void ``` |
| To | ``` typealias ALAssetsLibraryWriteImageCompletionBlock = (URL?, Error?) -> Swift.Void ``` |

Modified [ALAssetsLibraryWriteVideoCompletionBlock](https://developer.apple.com/documentation/assetslibrary/alassetslibrarywritevideocompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias ALAssetsLibraryWriteVideoCompletionBlock = (NSURL!, NSError!) -> Void ``` |
| To | ``` typealias ALAssetsLibraryWriteVideoCompletionBlock = (URL?, Error?) -> Swift.Void ``` |

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
