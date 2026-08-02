---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/ImageCaptureCore.html
archived_at: '2026-07-18T02:51:26.800520Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# ImageCaptureCore Changes for Swift

### ImageCaptureCore

Removed ICCameraDeviceSupportsFastPTPAdded ICReturnCode.deviceIsBusyEnumeratingModified ICCameraDevice

|  | Declaration |
| --- | --- |
| From | ``` class ICCameraDevice : ICDevice {     var batteryLevelAvailable: Bool { get }     var batteryLevel: Int { get }     var contentCatalogPercentCompleted: Int { get }     var contents: [ICCameraItem]? { get }     var mediaFiles: [ICCameraItem]? { get }     var timeOffset: NSTimeInterval { get }     var isAccessRestrictedAppleDevice: Bool { get }     var mountPoint: String? { get }     var tetheredCaptureEnabled: Bool     func filesOfType(_ fileUTType: String) -> [String]     func requestSyncClock()     func requestEnableTethering()     func requestDisableTethering()     func requestTakePicture()     func requestDeleteFiles(_ files: [ICCameraItem])     func cancelDelete()     func requestDownloadFile(_ file: ICCameraFile, options options: [String : AnyObject]?, downloadDelegate downloadDelegate: ICCameraDeviceDownloadDelegate, didDownloadSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func cancelDownload()     func requestUploadFile(_ fileURL: NSURL, options options: [String : AnyObject]?, uploadDelegate uploadDelegate: AnyObject, didUploadSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func requestReadDataFromFile(_ file: ICCameraFile, atOffset offset: off_t, length length: off_t, readDelegate readDelegate: AnyObject, didReadDataSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func requestSendPTPCommand(_ command: NSData, outData data: NSData, sendCommandDelegate sendCommandDelegate: AnyObject, didSendCommandSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) } ``` |
| To | ``` class ICCameraDevice : ICDevice {     var batteryLevelAvailable: Bool { get }     var batteryLevel: Int { get }     var contentCatalogPercentCompleted: Int { get }     var contents: [ICCameraItem]? { get }     var mediaFiles: [ICCameraItem]? { get }     var timeOffset: TimeInterval { get }     var isAccessRestrictedAppleDevice: Bool { get }     var mountPoint: String? { get }     var tetheredCaptureEnabled: Bool     func files(ofType fileUTType: String) -> [String]?     func requestSyncClock()     func requestEnableTethering()     func requestDisableTethering()     func requestTakePicture()     func requestDeleteFiles(_ files: [ICCameraItem])     func cancelDelete()     func requestDownloadFile(_ file: ICCameraFile, options options: [String : Any]? = nil, downloadDelegate downloadDelegate: ICCameraDeviceDownloadDelegate, didDownloadSelector selector: Selector, contextInfo contextInfo: UnsafeMutableRawPointer?)     func cancelDownload()     func requestUploadFile(_ fileURL: URL, options options: [String : Any]? = nil, uploadDelegate uploadDelegate: Any, didUploadSelector selector: Selector, contextInfo contextInfo: UnsafeMutableRawPointer?)     func requestReadData(from file: ICCameraFile, atOffset offset: off_t, length length: off_t, readDelegate readDelegate: Any, didReadDataSelector selector: Selector, contextInfo contextInfo: UnsafeMutableRawPointer?)     func requestSendPTPCommand(_ command: Data, outData data: Data, sendCommandDelegate sendCommandDelegate: Any, didSendCommand selector: Selector, contextInfo contextInfo: UnsafeMutableRawPointer?) } ``` |

Modified ICCameraDevice.files(ofType: String) -> [String]?

|  | Declaration |
| --- | --- |
| From | ``` func filesOfType(_ fileUTType: String) -> [String] ``` |
| To | ``` func files(ofType fileUTType: String) -> [String]? ``` |

Modified ICCameraDevice.requestDownloadFile(_: ICCameraFile, options: [String : Any]?, downloadDelegate: ICCameraDeviceDownloadDelegate, didDownloadSelector: Selector, contextInfo: UnsafeMutableRawPointer?)

|  | Declaration |
| --- | --- |
| From | ``` func requestDownloadFile(_ file: ICCameraFile, options options: [String : AnyObject]?, downloadDelegate downloadDelegate: ICCameraDeviceDownloadDelegate, didDownloadSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` func requestDownloadFile(_ file: ICCameraFile, options options: [String : Any]? = nil, downloadDelegate downloadDelegate: ICCameraDeviceDownloadDelegate, didDownloadSelector selector: Selector, contextInfo contextInfo: UnsafeMutableRawPointer?) ``` |

Modified ICCameraDevice.requestReadData(from: ICCameraFile, atOffset: off_t, length: off_t, readDelegate: Any, didReadDataSelector: Selector, contextInfo: UnsafeMutableRawPointer?)

|  | Declaration |
| --- | --- |
| From | ``` func requestReadDataFromFile(_ file: ICCameraFile, atOffset offset: off_t, length length: off_t, readDelegate readDelegate: AnyObject, didReadDataSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` func requestReadData(from file: ICCameraFile, atOffset offset: off_t, length length: off_t, readDelegate readDelegate: Any, didReadDataSelector selector: Selector, contextInfo contextInfo: UnsafeMutableRawPointer?) ``` |

Modified ICCameraDevice.requestSendPTPCommand(_: Data, outData: Data, sendCommandDelegate: Any, didSendCommand: Selector, contextInfo: UnsafeMutableRawPointer?)

|  | Declaration |
| --- | --- |
| From | ``` func requestSendPTPCommand(_ command: NSData, outData data: NSData, sendCommandDelegate sendCommandDelegate: AnyObject, didSendCommandSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` func requestSendPTPCommand(_ command: Data, outData data: Data, sendCommandDelegate sendCommandDelegate: Any, didSendCommand selector: Selector, contextInfo contextInfo: UnsafeMutableRawPointer?) ``` |

Modified ICCameraDevice.requestUploadFile(_: URL, options: [String : Any]?, uploadDelegate: Any, didUploadSelector: Selector, contextInfo: UnsafeMutableRawPointer?)

|  | Declaration |
| --- | --- |
| From | ``` func requestUploadFile(_ fileURL: NSURL, options options: [String : AnyObject]?, uploadDelegate uploadDelegate: AnyObject, didUploadSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` func requestUploadFile(_ fileURL: URL, options options: [String : Any]? = nil, uploadDelegate uploadDelegate: Any, didUploadSelector selector: Selector, contextInfo contextInfo: UnsafeMutableRawPointer?) ``` |

Modified ICCameraDevice.timeOffset

|  | Declaration |
| --- | --- |
| From | ``` var timeOffset: NSTimeInterval { get } ``` |
| To | ``` var timeOffset: TimeInterval { get } ``` |

Modified ICCameraDeviceDelegate

|  | Declaration |
| --- | --- |
| From | ``` protocol ICCameraDeviceDelegate : ICDeviceDelegate {     optional func cameraDevice(_ camera: ICCameraDevice, didAddItem item: ICCameraItem)     optional func cameraDevice(_ camera: ICCameraDevice, didAddItems items: [ICCameraItem])     optional func cameraDevice(_ camera: ICCameraDevice, didRemoveItem item: ICCameraItem)     optional func cameraDevice(_ camera: ICCameraDevice, didRemoveItems items: [ICCameraItem])     optional func cameraDevice(_ camera: ICCameraDevice, didRenameItems items: [ICCameraItem])     optional func cameraDevice(_ scanner: ICCameraDevice, didCompleteDeleteFilesWithError error: NSError?)     optional func cameraDeviceDidChangeCapability(_ camera: ICCameraDevice)     optional func cameraDevice(_ camera: ICCameraDevice, didReceiveThumbnailForItem item: ICCameraItem)     optional func cameraDevice(_ camera: ICCameraDevice, didReceiveMetadataForItem item: ICCameraItem)     optional func cameraDevice(_ camera: ICCameraDevice, didReceivePTPEvent eventData: NSData)     optional func deviceDidBecomeReadyWithCompleteContentCatalog(_ device: ICDevice)     optional func cameraDevice(_ cameraDevice: ICCameraDevice, shouldGetThumbnailOfItem item: ICCameraItem) -> Bool     optional func cameraDevice(_ cameraDevice: ICCameraDevice, shouldGetMetadataOfItem item: ICCameraItem) -> Bool } ``` |
| To | ``` protocol ICCameraDeviceDelegate : ICDeviceDelegate {     optional func cameraDevice(_ camera: ICCameraDevice, didAdd item: ICCameraItem)     optional func cameraDevice(_ camera: ICCameraDevice, didAdd items: [ICCameraItem])     optional func cameraDevice(_ camera: ICCameraDevice, didRemove item: ICCameraItem)     optional func cameraDevice(_ camera: ICCameraDevice, didRemove items: [ICCameraItem])     optional func cameraDevice(_ camera: ICCameraDevice, didRenameItems items: [ICCameraItem])     optional func cameraDevice(_ scanner: ICCameraDevice, didCompleteDeleteFilesWithError error: Error?)     optional func cameraDeviceDidChangeCapability(_ camera: ICCameraDevice)     optional func cameraDevice(_ camera: ICCameraDevice, didReceiveThumbnailFor item: ICCameraItem)     optional func cameraDevice(_ camera: ICCameraDevice, didReceiveMetadataFor item: ICCameraItem)     optional func cameraDevice(_ camera: ICCameraDevice, didReceivePTPEvent eventData: Data)     optional func deviceDidBecomeReady(withCompleteContentCatalog device: ICDevice)     optional func cameraDevice(_ cameraDevice: ICCameraDevice, shouldGetThumbnailOf item: ICCameraItem) -> Bool     optional func cameraDevice(_ cameraDevice: ICCameraDevice, shouldGetMetadataOf item: ICCameraItem) -> Bool } ``` |

Modified ICCameraDeviceDelegate.cameraDevice(_: ICCameraDevice, didAdd: ICCameraItem)

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDevice(_ camera: ICCameraDevice, didAddItem item: ICCameraItem) ``` |
| To | ``` optional func cameraDevice(_ camera: ICCameraDevice, didAdd item: ICCameraItem) ``` |

Modified ICCameraDeviceDelegate.cameraDevice(_: ICCameraDevice, didAdd: [ICCameraItem])

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDevice(_ camera: ICCameraDevice, didAddItems items: [ICCameraItem]) ``` |
| To | ``` optional func cameraDevice(_ camera: ICCameraDevice, didAdd items: [ICCameraItem]) ``` |

Modified ICCameraDeviceDelegate.cameraDevice(_: ICCameraDevice, didCompleteDeleteFilesWithError: Error?)

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDevice(_ scanner: ICCameraDevice, didCompleteDeleteFilesWithError error: NSError?) ``` |
| To | ``` optional func cameraDevice(_ scanner: ICCameraDevice, didCompleteDeleteFilesWithError error: Error?) ``` |

Modified ICCameraDeviceDelegate.cameraDevice(_: ICCameraDevice, didReceiveMetadataFor: ICCameraItem)

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDevice(_ camera: ICCameraDevice, didReceiveMetadataForItem item: ICCameraItem) ``` |
| To | ``` optional func cameraDevice(_ camera: ICCameraDevice, didReceiveMetadataFor item: ICCameraItem) ``` |

Modified ICCameraDeviceDelegate.cameraDevice(_: ICCameraDevice, didReceivePTPEvent: Data)

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDevice(_ camera: ICCameraDevice, didReceivePTPEvent eventData: NSData) ``` |
| To | ``` optional func cameraDevice(_ camera: ICCameraDevice, didReceivePTPEvent eventData: Data) ``` |

Modified ICCameraDeviceDelegate.cameraDevice(_: ICCameraDevice, didReceiveThumbnailFor: ICCameraItem)

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDevice(_ camera: ICCameraDevice, didReceiveThumbnailForItem item: ICCameraItem) ``` |
| To | ``` optional func cameraDevice(_ camera: ICCameraDevice, didReceiveThumbnailFor item: ICCameraItem) ``` |

Modified ICCameraDeviceDelegate.cameraDevice(_: ICCameraDevice, didRemove: ICCameraItem)

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDevice(_ camera: ICCameraDevice, didRemoveItem item: ICCameraItem) ``` |
| To | ``` optional func cameraDevice(_ camera: ICCameraDevice, didRemove item: ICCameraItem) ``` |

Modified ICCameraDeviceDelegate.cameraDevice(_: ICCameraDevice, didRemove: [ICCameraItem])

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDevice(_ camera: ICCameraDevice, didRemoveItems items: [ICCameraItem]) ``` |
| To | ``` optional func cameraDevice(_ camera: ICCameraDevice, didRemove items: [ICCameraItem]) ``` |

Modified ICCameraDeviceDelegate.cameraDevice(_: ICCameraDevice, shouldGetMetadataOf: ICCameraItem) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDevice(_ cameraDevice: ICCameraDevice, shouldGetMetadataOfItem item: ICCameraItem) -> Bool ``` |
| To | ``` optional func cameraDevice(_ cameraDevice: ICCameraDevice, shouldGetMetadataOf item: ICCameraItem) -> Bool ``` |

Modified ICCameraDeviceDelegate.cameraDevice(_: ICCameraDevice, shouldGetThumbnailOf: ICCameraItem) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` optional func cameraDevice(_ cameraDevice: ICCameraDevice, shouldGetThumbnailOfItem item: ICCameraItem) -> Bool ``` |
| To | ``` optional func cameraDevice(_ cameraDevice: ICCameraDevice, shouldGetThumbnailOf item: ICCameraItem) -> Bool ``` |

Modified ICCameraDeviceDelegate.deviceDidBecomeReady(withCompleteContentCatalog: ICDevice)

|  | Declaration |
| --- | --- |
| From | ``` optional func deviceDidBecomeReadyWithCompleteContentCatalog(_ device: ICDevice) ``` |
| To | ``` optional func deviceDidBecomeReady(withCompleteContentCatalog device: ICDevice) ``` |

Modified ICCameraDeviceDownloadDelegate

|  | Declaration |
| --- | --- |
| From | ``` protocol ICCameraDeviceDownloadDelegate : NSObjectProtocol {     optional func didDownloadFile(_ file: ICCameraFile, error error: NSError?, options options: [String : AnyObject]?, contextInfo contextInfo: UnsafeMutablePointer<Void>)     optional func didReceiveDownloadProgressForFile(_ file: ICCameraFile, downloadedBytes downloadedBytes: off_t, maxBytes maxBytes: off_t) } ``` |
| To | ``` protocol ICCameraDeviceDownloadDelegate : NSObjectProtocol {     optional func didDownloadFile(_ file: ICCameraFile, error error: Error?, options options: [String : Any]? = nil, contextInfo contextInfo: UnsafeMutableRawPointer?)     optional func didReceiveDownloadProgress(for file: ICCameraFile, downloadedBytes downloadedBytes: off_t, maxBytes maxBytes: off_t) } ``` |

Modified ICCameraDeviceDownloadDelegate.didDownloadFile()

|  | Declaration |
| --- | --- |
| From | ``` optional func didDownloadFile(_ file: ICCameraFile, error error: NSError?, options options: [String : AnyObject]?, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` optional func didDownloadFile(_ file: ICCameraFile, error error: Error?, options options: [String : Any]? = nil, contextInfo contextInfo: UnsafeMutableRawPointer?) ``` |

Modified ICCameraDeviceDownloadDelegate.didReceiveDownloadProgress(for: ICCameraFile, downloadedBytes: off_t, maxBytes: off_t)

|  | Declaration |
| --- | --- |
| From | ``` optional func didReceiveDownloadProgressForFile(_ file: ICCameraFile, downloadedBytes downloadedBytes: off_t, maxBytes maxBytes: off_t) ``` |
| To | ``` optional func didReceiveDownloadProgress(for file: ICCameraFile, downloadedBytes downloadedBytes: off_t, maxBytes maxBytes: off_t) ``` |

Modified ICCameraItem

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ICCameraItem : NSObject {     var device: ICCameraDevice { get }     var parentFolder: ICCameraFolder { get }     var name: String { get }     var UTI: String { get }     var fileSystemPath: String { get }     var locked: Bool { get }     var raw: Bool { get }     var inTemporaryStore: Bool { get }     var creationDate: NSDate { get }     var modificationDate: NSDate { get }     var thumbnailIfAvailable: CGImage? { get }     var largeThumbnailIfAvailable: CGImage? { get }     var metadataIfAvailable: [String : AnyObject]? { get }     var userData: NSMutableDictionary? { get }     var ptpObjectHandle: UInt32 { get }     var addedAfterContentCatalogCompleted: Bool { get } } ``` | -- |
| To | ``` class ICCameraItem : NSObject {     var device: ICCameraDevice { get }     var parentFolder: ICCameraFolder { get }     var name: String { get }     var uti: String { get }     var fileSystemPath: String? { get }     var isLocked: Bool { get }     var isRaw: Bool { get }     var isInTemporaryStore: Bool { get }     var creationDate: Date? { get }     var modificationDate: Date? { get }     var thumbnailIfAvailable: CGImage? { get }     var largeThumbnailIfAvailable: CGImage? { get }     var metadataIfAvailable: [String : Any]? { get }     var userData: NSMutableDictionary? { get }     var ptpObjectHandle: UInt32 { get }     var wasAddedAfterContentCatalogCompleted: Bool { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ICCameraItem : CVarArg { } extension ICCameraItem : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified ICCameraItem.creationDate

|  | Declaration |
| --- | --- |
| From | ``` var creationDate: NSDate { get } ``` |
| To | ``` var creationDate: Date? { get } ``` |

Modified ICCameraItem.fileSystemPath

|  | Declaration |
| --- | --- |
| From | ``` var fileSystemPath: String { get } ``` |
| To | ``` var fileSystemPath: String? { get } ``` |

Modified ICCameraItem.isInTemporaryStore

|  | Declaration |
| --- | --- |
| From | ``` var inTemporaryStore: Bool { get } ``` |
| To | ``` var isInTemporaryStore: Bool { get } ``` |

Modified ICCameraItem.isLocked

|  | Declaration |
| --- | --- |
| From | ``` var locked: Bool { get } ``` |
| To | ``` var isLocked: Bool { get } ``` |

Modified ICCameraItem.isRaw

|  | Declaration |
| --- | --- |
| From | ``` var raw: Bool { get } ``` |
| To | ``` var isRaw: Bool { get } ``` |

Modified ICCameraItem.metadataIfAvailable

|  | Declaration |
| --- | --- |
| From | ``` var metadataIfAvailable: [String : AnyObject]? { get } ``` |
| To | ``` var metadataIfAvailable: [String : Any]? { get } ``` |

Modified ICCameraItem.modificationDate

|  | Declaration |
| --- | --- |
| From | ``` var modificationDate: NSDate { get } ``` |
| To | ``` var modificationDate: Date? { get } ``` |

Modified ICCameraItem.uti

|  | Declaration |
| --- | --- |
| From | ``` var UTI: String { get } ``` |
| To | ``` var uti: String { get } ``` |

Modified ICCameraItem.wasAddedAfterContentCatalogCompleted

|  | Declaration |
| --- | --- |
| From | ``` var addedAfterContentCatalogCompleted: Bool { get } ``` |
| To | ``` var wasAddedAfterContentCatalogCompleted: Bool { get } ``` |

Modified ICDevice

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ICDevice : NSObject {     unowned(unsafe) var delegate: ICDeviceDelegate?     var type: ICDeviceType { get }     var name: String? { get }     var icon: CGImage? { get }     var capabilities: [String] { get }     var modulePath: String { get }     var moduleVersion: String { get }     var moduleExecutableArchitecture: Int32 { get }     var remote: Bool { get }     var shared: Bool { get }     var hasConfigurableWiFiInterface: Bool { get }     var transportType: String { get }     var usbLocationID: Int32 { get }     var usbProductID: Int32 { get }     var usbVendorID: Int32 { get }     var fwGUID: Int64 { get }     var serialNumberString: String? { get }     var locationDescription: String? { get }     var hasOpenSession: Bool { get }     var UUIDString: String? { get }     var persistentIDString: String? { get }     var buttonPressed: String { get }     var autolaunchApplicationPath: String?     var userData: NSMutableDictionary? { get }     func requestOpenSession()     func requestCloseSession()     func requestYield()     func requestSendMessage(_ messageCode: UInt32, outData data: NSData, maxReturnedDataSize maxReturnedDataSize: UInt32, sendMessageDelegate sendMessageDelegate: AnyObject, didSendMessageSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func requestEjectOrDisconnect() } ``` | -- |
| To | ``` class ICDevice : NSObject {     unowned(unsafe) var delegate: ICDeviceDelegate?     var type: ICDeviceType { get }     var name: String? { get }     var icon: CGImage? { get }     var capabilities: [String] { get }     var modulePath: String { get }     var moduleVersion: String { get }     var moduleExecutableArchitecture: Int32 { get }     var isRemote: Bool { get }     var isShared: Bool { get }     var hasConfigurableWiFiInterface: Bool { get }     var transportType: String { get }     var usbLocationID: Int32 { get }     var usbProductID: Int32 { get }     var usbVendorID: Int32 { get }     var fwGUID: Int64 { get }     var serialNumberString: String? { get }     var locationDescription: String? { get }     var hasOpenSession: Bool { get }     var uuidString: String? { get }     var persistentIDString: String? { get }     var buttonPressed: String { get }     var autolaunchApplicationPath: String?     var userData: NSMutableDictionary? { get }     func requestOpenSession()     func requestCloseSession()     func requestYield()     func requestSendMessage(_ messageCode: UInt32, outData data: Data, maxReturnedDataSize maxReturnedDataSize: UInt32, sendMessageDelegate sendMessageDelegate: Any, didSendMessageSelector selector: Selector, contextInfo contextInfo: UnsafeMutableRawPointer?)     func requestEjectOrDisconnect()     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ICDevice : CVarArg { } extension ICDevice : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified ICDevice.isRemote

|  | Declaration |
| --- | --- |
| From | ``` var remote: Bool { get } ``` |
| To | ``` var isRemote: Bool { get } ``` |

Modified ICDevice.isShared

|  | Declaration |
| --- | --- |
| From | ``` var shared: Bool { get } ``` |
| To | ``` var isShared: Bool { get } ``` |

Modified ICDevice.requestSendMessage(_: UInt32, outData: Data, maxReturnedDataSize: UInt32, sendMessageDelegate: Any, didSendMessageSelector: Selector, contextInfo: UnsafeMutableRawPointer?)

|  | Declaration |
| --- | --- |
| From | ``` func requestSendMessage(_ messageCode: UInt32, outData data: NSData, maxReturnedDataSize maxReturnedDataSize: UInt32, sendMessageDelegate sendMessageDelegate: AnyObject, didSendMessageSelector selector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` func requestSendMessage(_ messageCode: UInt32, outData data: Data, maxReturnedDataSize maxReturnedDataSize: UInt32, sendMessageDelegate sendMessageDelegate: Any, didSendMessageSelector selector: Selector, contextInfo contextInfo: UnsafeMutableRawPointer?) ``` |

Modified ICDevice.uuidString

|  | Declaration |
| --- | --- |
| From | ``` var UUIDString: String? { get } ``` |
| To | ``` var uuidString: String? { get } ``` |

Modified ICDeviceBrowser

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ICDeviceBrowser : NSObject {     unowned(unsafe) var delegate: ICDeviceBrowserDelegate?     var browsing: Bool { get }     var browsedDeviceTypeMask: ICDeviceTypeMask     var devices: [ICDevice]? { get }     func preferredDevice() -> ICDevice     init()     func start()     func stop() } ``` | -- |
| To | ``` class ICDeviceBrowser : NSObject {     unowned(unsafe) var delegate: ICDeviceBrowserDelegate?     var isBrowsing: Bool { get }     var browsedDeviceTypeMask: ICDeviceTypeMask     var devices: [ICDevice]? { get }     func preferredDevice() -> ICDevice?     init()     func start()     func stop()     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ICDeviceBrowser : CVarArg { } extension ICDeviceBrowser : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified ICDeviceBrowser.isBrowsing

|  | Declaration |
| --- | --- |
| From | ``` var browsing: Bool { get } ``` |
| To | ``` var isBrowsing: Bool { get } ``` |

Modified ICDeviceBrowser.preferredDevice() -> ICDevice?

|  | Declaration |
| --- | --- |
| From | ``` func preferredDevice() -> ICDevice ``` |
| To | ``` func preferredDevice() -> ICDevice? ``` |

Modified ICDeviceBrowserDelegate

|  | Declaration |
| --- | --- |
| From | ``` protocol ICDeviceBrowserDelegate : NSObjectProtocol {     func deviceBrowser(_ browser: ICDeviceBrowser, didAddDevice device: ICDevice, moreComing moreComing: Bool)     func deviceBrowser(_ browser: ICDeviceBrowser, didRemoveDevice device: ICDevice, moreGoing moreGoing: Bool)     optional func deviceBrowser(_ browser: ICDeviceBrowser, deviceDidChangeName device: ICDevice)     optional func deviceBrowser(_ browser: ICDeviceBrowser, deviceDidChangeSharingState device: ICDevice)     optional func deviceBrowser(_ browser: ICDeviceBrowser, requestsSelectDevice device: ICDevice)     optional func deviceBrowserDidEnumerateLocalDevices(_ browser: ICDeviceBrowser) } ``` |
| To | ``` protocol ICDeviceBrowserDelegate : NSObjectProtocol {     func deviceBrowser(_ browser: ICDeviceBrowser, didAdd device: ICDevice, moreComing moreComing: Bool)     func deviceBrowser(_ browser: ICDeviceBrowser, didRemove device: ICDevice, moreGoing moreGoing: Bool)     optional func deviceBrowser(_ browser: ICDeviceBrowser, deviceDidChangeName device: ICDevice)     optional func deviceBrowser(_ browser: ICDeviceBrowser, deviceDidChangeSharingState device: ICDevice)     optional func deviceBrowser(_ browser: ICDeviceBrowser, requestsSelect device: ICDevice)     optional func deviceBrowserDidEnumerateLocalDevices(_ browser: ICDeviceBrowser) } ``` |

Modified ICDeviceBrowserDelegate.deviceBrowser(_: ICDeviceBrowser, didAdd: ICDevice, moreComing: Bool)

|  | Declaration |
| --- | --- |
| From | ``` func deviceBrowser(_ browser: ICDeviceBrowser, didAddDevice device: ICDevice, moreComing moreComing: Bool) ``` |
| To | ``` func deviceBrowser(_ browser: ICDeviceBrowser, didAdd device: ICDevice, moreComing moreComing: Bool) ``` |

Modified ICDeviceBrowserDelegate.deviceBrowser(_: ICDeviceBrowser, didRemove: ICDevice, moreGoing: Bool)

|  | Declaration |
| --- | --- |
| From | ``` func deviceBrowser(_ browser: ICDeviceBrowser, didRemoveDevice device: ICDevice, moreGoing moreGoing: Bool) ``` |
| To | ``` func deviceBrowser(_ browser: ICDeviceBrowser, didRemove device: ICDevice, moreGoing moreGoing: Bool) ``` |

Modified ICDeviceBrowserDelegate.deviceBrowser(_: ICDeviceBrowser, requestsSelect: ICDevice)

|  | Declaration |
| --- | --- |
| From | ``` optional func deviceBrowser(_ browser: ICDeviceBrowser, requestsSelectDevice device: ICDevice) ``` |
| To | ``` optional func deviceBrowser(_ browser: ICDeviceBrowser, requestsSelect device: ICDevice) ``` |

Modified ICDeviceDelegate

|  | Declaration |
| --- | --- |
| From | ``` protocol ICDeviceDelegate : NSObjectProtocol {     func didRemoveDevice(_ device: ICDevice)     optional func device(_ device: ICDevice, didOpenSessionWithError error: NSError?)     optional func deviceDidBecomeReady(_ device: ICDevice)     optional func device(_ device: ICDevice, didCloseSessionWithError error: NSError?)     optional func deviceDidChangeName(_ device: ICDevice)     optional func deviceDidChangeSharingState(_ device: ICDevice)     optional func device(_ device: ICDevice, didReceiveStatusInformation status: [String : AnyObject])     optional func device(_ device: ICDevice, didEncounterError error: NSError?)     optional func device(_ device: ICDevice, didReceiveButtonPress buttonType: String)     optional func device(_ device: ICDevice, didReceiveCustomNotification notification: [String : AnyObject], data data: NSData) } ``` |
| To | ``` protocol ICDeviceDelegate : NSObjectProtocol {     func didRemove(_ device: ICDevice)     optional func device(_ device: ICDevice, didOpenSessionWithError error: Error?)     optional func deviceDidBecomeReady(_ device: ICDevice)     optional func device(_ device: ICDevice, didCloseSessionWithError error: Error?)     optional func deviceDidChangeName(_ device: ICDevice)     optional func deviceDidChangeSharingState(_ device: ICDevice)     optional func device(_ device: ICDevice, didReceiveStatusInformation status: [String : Any])     optional func device(_ device: ICDevice, didEncounterError error: Error?)     optional func device(_ device: ICDevice, didReceiveButtonPress buttonType: String)     optional func device(_ device: ICDevice, didReceiveCustomNotification notification: [String : Any], data data: Data) } ``` |

Modified ICDeviceDelegate.device(_: ICDevice, didCloseSessionWithError: Error?)

|  | Declaration |
| --- | --- |
| From | ``` optional func device(_ device: ICDevice, didCloseSessionWithError error: NSError?) ``` |
| To | ``` optional func device(_ device: ICDevice, didCloseSessionWithError error: Error?) ``` |

Modified ICDeviceDelegate.device(_: ICDevice, didEncounterError: Error?)

|  | Declaration |
| --- | --- |
| From | ``` optional func device(_ device: ICDevice, didEncounterError error: NSError?) ``` |
| To | ``` optional func device(_ device: ICDevice, didEncounterError error: Error?) ``` |

Modified ICDeviceDelegate.device(_: ICDevice, didOpenSessionWithError: Error?)

|  | Declaration |
| --- | --- |
| From | ``` optional func device(_ device: ICDevice, didOpenSessionWithError error: NSError?) ``` |
| To | ``` optional func device(_ device: ICDevice, didOpenSessionWithError error: Error?) ``` |

Modified ICDeviceDelegate.device(_: ICDevice, didReceiveCustomNotification: [String : Any], data: Data)

|  | Declaration |
| --- | --- |
| From | ``` optional func device(_ device: ICDevice, didReceiveCustomNotification notification: [String : AnyObject], data data: NSData) ``` |
| To | ``` optional func device(_ device: ICDevice, didReceiveCustomNotification notification: [String : Any], data data: Data) ``` |

Modified ICDeviceDelegate.device(_: ICDevice, didReceiveStatusInformation: [String : Any])

|  | Declaration |
| --- | --- |
| From | ``` optional func device(_ device: ICDevice, didReceiveStatusInformation status: [String : AnyObject]) ``` |
| To | ``` optional func device(_ device: ICDevice, didReceiveStatusInformation status: [String : Any]) ``` |

Modified ICDeviceDelegate.didRemove(_: ICDevice)

|  | Declaration |
| --- | --- |
| From | ``` func didRemoveDevice(_ device: ICDevice) ``` |
| To | ``` func didRemove(_ device: ICDevice) ``` |

Modified ICDeviceLocationType [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum ICDeviceLocationType : UInt {     case Local     case Shared     case Bonjour     case Bluetooth } ``` |
| To | ``` enum ICDeviceLocationType : UInt {     case local     case shared     case bonjour     case bluetooth } ``` |

Modified ICDeviceLocationType.bluetooth

|  | Declaration |
| --- | --- |
| From | ``` case Bluetooth ``` |
| To | ``` case bluetooth ``` |

Modified ICDeviceLocationType.bonjour

|  | Declaration |
| --- | --- |
| From | ``` case Bonjour ``` |
| To | ``` case bonjour ``` |

Modified ICDeviceLocationType.local

|  | Declaration |
| --- | --- |
| From | ``` case Local ``` |
| To | ``` case local ``` |

Modified ICDeviceLocationType.shared

|  | Declaration |
| --- | --- |
| From | ``` case Shared ``` |
| To | ``` case shared ``` |

Modified ICDeviceLocationTypeMask [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum ICDeviceLocationTypeMask : UInt {     case Local     case Shared     case Bonjour     case Bluetooth     case Remote } ``` |
| To | ``` enum ICDeviceLocationTypeMask : UInt {     case local     case shared     case bonjour     case bluetooth     case remote } ``` |

Modified ICDeviceLocationTypeMask.bluetooth

|  | Declaration |
| --- | --- |
| From | ``` case Bluetooth ``` |
| To | ``` case bluetooth ``` |

Modified ICDeviceLocationTypeMask.bonjour

|  | Declaration |
| --- | --- |
| From | ``` case Bonjour ``` |
| To | ``` case bonjour ``` |

Modified ICDeviceLocationTypeMask.local

|  | Declaration |
| --- | --- |
| From | ``` case Local ``` |
| To | ``` case local ``` |

Modified ICDeviceLocationTypeMask.remote

|  | Declaration |
| --- | --- |
| From | ``` case Remote ``` |
| To | ``` case remote ``` |

Modified ICDeviceLocationTypeMask.shared

|  | Declaration |
| --- | --- |
| From | ``` case Shared ``` |
| To | ``` case shared ``` |

Modified ICDeviceType [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum ICDeviceType : UInt {     case Camera     case Scanner } ``` |
| To | ``` enum ICDeviceType : UInt {     case camera     case scanner } ``` |

Modified ICDeviceType.camera

|  | Declaration |
| --- | --- |
| From | ``` case Camera ``` |
| To | ``` case camera ``` |

Modified ICDeviceType.scanner

|  | Declaration |
| --- | --- |
| From | ``` case Scanner ``` |
| To | ``` case scanner ``` |

Modified ICDeviceTypeMask [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum ICDeviceTypeMask : UInt {     case Camera     case Scanner } ``` |
| To | ``` enum ICDeviceTypeMask : UInt {     case camera     case scanner } ``` |

Modified ICDeviceTypeMask.camera

|  | Declaration |
| --- | --- |
| From | ``` case Camera ``` |
| To | ``` case camera ``` |

Modified ICDeviceTypeMask.scanner

|  | Declaration |
| --- | --- |
| From | ``` case Scanner ``` |
| To | ``` case scanner ``` |

Modified ICEXIFOrientationType [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum ICEXIFOrientationType : UInt {     case Orientation1     case Orientation2     case Orientation3     case Orientation4     case Orientation5     case Orientation6     case Orientation7     case Orientation8 } ``` |
| To | ``` enum ICEXIFOrientationType : UInt {     case orientation1     case orientation2     case orientation3     case orientation4     case orientation5     case orientation6     case orientation7     case orientation8 } ``` |

Modified ICEXIFOrientationType.orientation1

|  | Declaration |
| --- | --- |
| From | ``` case Orientation1 ``` |
| To | ``` case orientation1 ``` |

Modified ICEXIFOrientationType.orientation2

|  | Declaration |
| --- | --- |
| From | ``` case Orientation2 ``` |
| To | ``` case orientation2 ``` |

Modified ICEXIFOrientationType.orientation3

|  | Declaration |
| --- | --- |
| From | ``` case Orientation3 ``` |
| To | ``` case orientation3 ``` |

Modified ICEXIFOrientationType.orientation4

|  | Declaration |
| --- | --- |
| From | ``` case Orientation4 ``` |
| To | ``` case orientation4 ``` |

Modified ICEXIFOrientationType.orientation5

|  | Declaration |
| --- | --- |
| From | ``` case Orientation5 ``` |
| To | ``` case orientation5 ``` |

Modified ICEXIFOrientationType.orientation6

|  | Declaration |
| --- | --- |
| From | ``` case Orientation6 ``` |
| To | ``` case orientation6 ``` |

Modified ICEXIFOrientationType.orientation7

|  | Declaration |
| --- | --- |
| From | ``` case Orientation7 ``` |
| To | ``` case orientation7 ``` |

Modified ICEXIFOrientationType.orientation8

|  | Declaration |
| --- | --- |
| From | ``` case Orientation8 ``` |
| To | ``` case orientation8 ``` |

Modified ICReturnCode [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum ICReturnCode : Int {     case Success     case InvalidParam     case CommunicationTimedOut     case ScanOperationCanceled     case ScannerInUseByLocalUser     case ScannerInUseByRemoteUser     case DeviceFailedToOpenSession     case DeviceFailedToCloseSession     case ScannerFailedToSelectFunctionalUnit     case ScannerFailedToCompleteOverviewScan     case ScannerFailedToCompleteScan     case ReceivedUnsolicitedScannerStatusInfo     case ReceivedUnsolicitedScannerErrorInfo     case DownloadFailed     case UploadFailed     case FailedToCompletePassThroughCommand     case DownloadCanceled     case FailedToEnabeTethering     case FailedToDisabeTethering     case FailedToCompleteSendMessageRequest     case DeleteFilesFailed     case DeleteFilesCanceled     case DeviceIsPasscodeLocked     case DeviceFailedToTakePicture     case DeviceSoftwareNotInstalled     case DeviceSoftwareIsBeingInstalled     case DeviceSoftwareInstallationCompleted     case DeviceSoftwareInstallationCanceled     case DeviceSoftwareInstallationFailed     case DeviceSoftwareNotAvailable     case DeviceCouldNotPair     case DeviceCouldNotUnpair     case DeviceNeedsCredentials } ``` |
| To | ``` enum ICReturnCode : Int {     case success     case invalidParam     case communicationTimedOut     case scanOperationCanceled     case scannerInUseByLocalUser     case scannerInUseByRemoteUser     case deviceFailedToOpenSession     case deviceFailedToCloseSession     case scannerFailedToSelectFunctionalUnit     case scannerFailedToCompleteOverviewScan     case scannerFailedToCompleteScan     case receivedUnsolicitedScannerStatusInfo     case receivedUnsolicitedScannerErrorInfo     case downloadFailed     case uploadFailed     case failedToCompletePassThroughCommand     case downloadCanceled     case failedToEnabeTethering     case failedToDisabeTethering     case failedToCompleteSendMessageRequest     case deleteFilesFailed     case deleteFilesCanceled     case deviceIsPasscodeLocked     case deviceFailedToTakePicture     case deviceSoftwareNotInstalled     case deviceSoftwareIsBeingInstalled     case deviceSoftwareInstallationCompleted     case deviceSoftwareInstallationCanceled     case deviceSoftwareInstallationFailed     case deviceSoftwareNotAvailable     case deviceCouldNotPair     case deviceCouldNotUnpair     case deviceNeedsCredentials     case deviceIsBusyEnumerating } ``` |

Modified ICReturnCode.communicationTimedOut

|  | Declaration |
| --- | --- |
| From | ``` case CommunicationTimedOut ``` |
| To | ``` case communicationTimedOut ``` |

Modified ICReturnCode.deleteFilesCanceled

|  | Declaration |
| --- | --- |
| From | ``` case DeleteFilesCanceled ``` |
| To | ``` case deleteFilesCanceled ``` |

Modified ICReturnCode.deleteFilesFailed

|  | Declaration |
| --- | --- |
| From | ``` case DeleteFilesFailed ``` |
| To | ``` case deleteFilesFailed ``` |

Modified ICReturnCode.deviceCouldNotPair

|  | Declaration |
| --- | --- |
| From | ``` case DeviceCouldNotPair ``` |
| To | ``` case deviceCouldNotPair ``` |

Modified ICReturnCode.deviceCouldNotUnpair

|  | Declaration |
| --- | --- |
| From | ``` case DeviceCouldNotUnpair ``` |
| To | ``` case deviceCouldNotUnpair ``` |

Modified ICReturnCode.deviceFailedToCloseSession

|  | Declaration |
| --- | --- |
| From | ``` case DeviceFailedToCloseSession ``` |
| To | ``` case deviceFailedToCloseSession ``` |

Modified ICReturnCode.deviceFailedToOpenSession

|  | Declaration |
| --- | --- |
| From | ``` case DeviceFailedToOpenSession ``` |
| To | ``` case deviceFailedToOpenSession ``` |

Modified ICReturnCode.deviceFailedToTakePicture

|  | Declaration |
| --- | --- |
| From | ``` case DeviceFailedToTakePicture ``` |
| To | ``` case deviceFailedToTakePicture ``` |

Modified ICReturnCode.deviceIsPasscodeLocked

|  | Declaration |
| --- | --- |
| From | ``` case DeviceIsPasscodeLocked ``` |
| To | ``` case deviceIsPasscodeLocked ``` |

Modified ICReturnCode.deviceNeedsCredentials

|  | Declaration |
| --- | --- |
| From | ``` case DeviceNeedsCredentials ``` |
| To | ``` case deviceNeedsCredentials ``` |

Modified ICReturnCode.deviceSoftwareInstallationCanceled

|  | Declaration |
| --- | --- |
| From | ``` case DeviceSoftwareInstallationCanceled ``` |
| To | ``` case deviceSoftwareInstallationCanceled ``` |

Modified ICReturnCode.deviceSoftwareInstallationCompleted

|  | Declaration |
| --- | --- |
| From | ``` case DeviceSoftwareInstallationCompleted ``` |
| To | ``` case deviceSoftwareInstallationCompleted ``` |

Modified ICReturnCode.deviceSoftwareInstallationFailed

|  | Declaration |
| --- | --- |
| From | ``` case DeviceSoftwareInstallationFailed ``` |
| To | ``` case deviceSoftwareInstallationFailed ``` |

Modified ICReturnCode.deviceSoftwareIsBeingInstalled

|  | Declaration |
| --- | --- |
| From | ``` case DeviceSoftwareIsBeingInstalled ``` |
| To | ``` case deviceSoftwareIsBeingInstalled ``` |

Modified ICReturnCode.deviceSoftwareNotAvailable

|  | Declaration |
| --- | --- |
| From | ``` case DeviceSoftwareNotAvailable ``` |
| To | ``` case deviceSoftwareNotAvailable ``` |

Modified ICReturnCode.deviceSoftwareNotInstalled

|  | Declaration |
| --- | --- |
| From | ``` case DeviceSoftwareNotInstalled ``` |
| To | ``` case deviceSoftwareNotInstalled ``` |

Modified ICReturnCode.downloadCanceled

|  | Declaration |
| --- | --- |
| From | ``` case DownloadCanceled ``` |
| To | ``` case downloadCanceled ``` |

Modified ICReturnCode.downloadFailed

|  | Declaration |
| --- | --- |
| From | ``` case DownloadFailed ``` |
| To | ``` case downloadFailed ``` |

Modified ICReturnCode.failedToCompletePassThroughCommand

|  | Declaration |
| --- | --- |
| From | ``` case FailedToCompletePassThroughCommand ``` |
| To | ``` case failedToCompletePassThroughCommand ``` |

Modified ICReturnCode.failedToCompleteSendMessageRequest

|  | Declaration |
| --- | --- |
| From | ``` case FailedToCompleteSendMessageRequest ``` |
| To | ``` case failedToCompleteSendMessageRequest ``` |

Modified ICReturnCode.failedToDisabeTethering

|  | Declaration |
| --- | --- |
| From | ``` case FailedToDisabeTethering ``` |
| To | ``` case failedToDisabeTethering ``` |

Modified ICReturnCode.failedToEnabeTethering

|  | Declaration |
| --- | --- |
| From | ``` case FailedToEnabeTethering ``` |
| To | ``` case failedToEnabeTethering ``` |

Modified ICReturnCode.invalidParam

|  | Declaration |
| --- | --- |
| From | ``` case InvalidParam ``` |
| To | ``` case invalidParam ``` |

Modified ICReturnCode.receivedUnsolicitedScannerErrorInfo

|  | Declaration |
| --- | --- |
| From | ``` case ReceivedUnsolicitedScannerErrorInfo ``` |
| To | ``` case receivedUnsolicitedScannerErrorInfo ``` |

Modified ICReturnCode.receivedUnsolicitedScannerStatusInfo

|  | Declaration |
| --- | --- |
| From | ``` case ReceivedUnsolicitedScannerStatusInfo ``` |
| To | ``` case receivedUnsolicitedScannerStatusInfo ``` |

Modified ICReturnCode.scannerFailedToCompleteOverviewScan

|  | Declaration |
| --- | --- |
| From | ``` case ScannerFailedToCompleteOverviewScan ``` |
| To | ``` case scannerFailedToCompleteOverviewScan ``` |

Modified ICReturnCode.scannerFailedToCompleteScan

|  | Declaration |
| --- | --- |
| From | ``` case ScannerFailedToCompleteScan ``` |
| To | ``` case scannerFailedToCompleteScan ``` |

Modified ICReturnCode.scannerFailedToSelectFunctionalUnit

|  | Declaration |
| --- | --- |
| From | ``` case ScannerFailedToSelectFunctionalUnit ``` |
| To | ``` case scannerFailedToSelectFunctionalUnit ``` |

Modified ICReturnCode.scannerInUseByLocalUser

|  | Declaration |
| --- | --- |
| From | ``` case ScannerInUseByLocalUser ``` |
| To | ``` case scannerInUseByLocalUser ``` |

Modified ICReturnCode.scannerInUseByRemoteUser

|  | Declaration |
| --- | --- |
| From | ``` case ScannerInUseByRemoteUser ``` |
| To | ``` case scannerInUseByRemoteUser ``` |

Modified ICReturnCode.scanOperationCanceled

|  | Declaration |
| --- | --- |
| From | ``` case ScanOperationCanceled ``` |
| To | ``` case scanOperationCanceled ``` |

Modified ICReturnCode.success

|  | Declaration |
| --- | --- |
| From | ``` case Success ``` |
| To | ``` case success ``` |

Modified ICReturnCode.uploadFailed

|  | Declaration |
| --- | --- |
| From | ``` case UploadFailed ``` |
| To | ``` case uploadFailed ``` |

Modified ICScannerBandData

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ICScannerBandData : NSObject {     var fullImageWidth: Int { get }     var fullImageHeight: Int { get }     var bitsPerPixel: Int { get }     var bitsPerComponent: Int { get }     var numComponents: Int { get }     var bigEndian: Bool { get }     var pixelDataType: ICScannerPixelDataType { get }     var colorSyncProfilePath: String? { get }     var bytesPerRow: Int { get }     var dataStartRow: Int { get }     var dataNumRows: Int { get }     var dataSize: Int { get }     var dataBuffer: NSData? { get } } ``` | -- |
| To | ``` class ICScannerBandData : NSObject {     var fullImageWidth: Int { get }     var fullImageHeight: Int { get }     var bitsPerPixel: Int { get }     var bitsPerComponent: Int { get }     var numComponents: Int { get }     var isBigEndian: Bool { get }     var pixelDataType: ICScannerPixelDataType { get }     var colorSyncProfilePath: String? { get }     var bytesPerRow: Int { get }     var dataStartRow: Int { get }     var dataNumRows: Int { get }     var dataSize: Int { get }     var dataBuffer: Data? { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ICScannerBandData : CVarArg { } extension ICScannerBandData : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified ICScannerBandData.dataBuffer

|  | Declaration |
| --- | --- |
| From | ``` var dataBuffer: NSData? { get } ``` |
| To | ``` var dataBuffer: Data? { get } ``` |

Modified ICScannerBandData.isBigEndian

|  | Declaration |
| --- | --- |
| From | ``` var bigEndian: Bool { get } ``` |
| To | ``` var isBigEndian: Bool { get } ``` |

Modified ICScannerBitDepth [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum ICScannerBitDepth : UInt {     case Depth1Bit     case Depth8Bits     case Depth16Bits } ``` |
| To | ``` enum ICScannerBitDepth : UInt {     case depth1Bit     case depth8Bits     case depth16Bits } ``` |

Modified ICScannerBitDepth.depth16Bits

|  | Declaration |
| --- | --- |
| From | ``` case Depth16Bits ``` |
| To | ``` case depth16Bits ``` |

Modified ICScannerBitDepth.depth1Bit

|  | Declaration |
| --- | --- |
| From | ``` case Depth1Bit ``` |
| To | ``` case depth1Bit ``` |

Modified ICScannerBitDepth.depth8Bits

|  | Declaration |
| --- | --- |
| From | ``` case Depth8Bits ``` |
| To | ``` case depth8Bits ``` |

Modified ICScannerColorDataFormatType [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum ICScannerColorDataFormatType : UInt {     case Chunky     case Planar } ``` |
| To | ``` enum ICScannerColorDataFormatType : UInt {     case chunky     case planar } ``` |

Modified ICScannerColorDataFormatType.chunky

|  | Declaration |
| --- | --- |
| From | ``` case Chunky ``` |
| To | ``` case chunky ``` |

Modified ICScannerColorDataFormatType.planar

|  | Declaration |
| --- | --- |
| From | ``` case Planar ``` |
| To | ``` case planar ``` |

Modified ICScannerDevice

|  | Declaration |
| --- | --- |
| From | ``` class ICScannerDevice : ICDevice {     var availableFunctionalUnitTypes: [NSNumber] { get }     var selectedFunctionalUnit: ICScannerFunctionalUnit { get }     var transferMode: ICScannerTransferMode     var maxMemoryBandSize: UInt32     var downloadsDirectory: NSURL     var documentName: String     var documentUTI: String     func requestSelectFunctionalUnit(_ type: ICScannerFunctionalUnitType)     func requestOverviewScan()     func requestScan()     func cancelScan() } ``` |
| To | ``` class ICScannerDevice : ICDevice {     var availableFunctionalUnitTypes: [NSNumber] { get }     var selectedFunctionalUnit: ICScannerFunctionalUnit { get }     var transferMode: ICScannerTransferMode     var maxMemoryBandSize: UInt32     var downloadsDirectory: URL     var documentName: String     var documentUTI: String     func requestSelect(_ type: ICScannerFunctionalUnitType)     func requestOverviewScan()     func requestScan()     func cancelScan() } ``` |

Modified ICScannerDevice.downloadsDirectory

|  | Declaration |
| --- | --- |
| From | ``` var downloadsDirectory: NSURL ``` |
| To | ``` var downloadsDirectory: URL ``` |

Modified ICScannerDevice.requestSelect(_: ICScannerFunctionalUnitType)

|  | Declaration |
| --- | --- |
| From | ``` func requestSelectFunctionalUnit(_ type: ICScannerFunctionalUnitType) ``` |
| To | ``` func requestSelect(_ type: ICScannerFunctionalUnitType) ``` |

Modified ICScannerDeviceDelegate

|  | Declaration |
| --- | --- |
| From | ``` protocol ICScannerDeviceDelegate : ICDeviceDelegate {     optional func scannerDeviceDidBecomeAvailable(_ scanner: ICScannerDevice)     optional func scannerDevice(_ scanner: ICScannerDevice, didSelectFunctionalUnit functionalUnit: ICScannerFunctionalUnit, error error: NSError?)     optional func scannerDevice(_ scanner: ICScannerDevice, didScanToURL url: NSURL, data data: NSData)     optional func scannerDevice(_ scanner: ICScannerDevice, didScanToURL url: NSURL)     optional func scannerDevice(_ scanner: ICScannerDevice, didScanToBandData data: ICScannerBandData)     optional func scannerDevice(_ scanner: ICScannerDevice, didCompleteOverviewScanWithError error: NSError?)     optional func scannerDevice(_ scanner: ICScannerDevice, didCompleteScanWithError error: NSError?) } ``` |
| To | ``` protocol ICScannerDeviceDelegate : ICDeviceDelegate {     optional func scannerDeviceDidBecomeAvailable(_ scanner: ICScannerDevice)     optional func scannerDevice(_ scanner: ICScannerDevice, didSelect functionalUnit: ICScannerFunctionalUnit, error error: Error?)     optional func scannerDevice(_ scanner: ICScannerDevice, didScanTo url: URL, data data: Data)     optional func scannerDevice(_ scanner: ICScannerDevice, didScanTo url: URL)     optional func scannerDevice(_ scanner: ICScannerDevice, didScanTo data: ICScannerBandData)     optional func scannerDevice(_ scanner: ICScannerDevice, didCompleteOverviewScanWithError error: Error?)     optional func scannerDevice(_ scanner: ICScannerDevice, didCompleteScanWithError error: Error?) } ``` |

Modified ICScannerDeviceDelegate.scannerDevice(_: ICScannerDevice, didCompleteOverviewScanWithError: Error?)

|  | Declaration |
| --- | --- |
| From | ``` optional func scannerDevice(_ scanner: ICScannerDevice, didCompleteOverviewScanWithError error: NSError?) ``` |
| To | ``` optional func scannerDevice(_ scanner: ICScannerDevice, didCompleteOverviewScanWithError error: Error?) ``` |

Modified ICScannerDeviceDelegate.scannerDevice(_: ICScannerDevice, didCompleteScanWithError: Error?)

|  | Declaration |
| --- | --- |
| From | ``` optional func scannerDevice(_ scanner: ICScannerDevice, didCompleteScanWithError error: NSError?) ``` |
| To | ``` optional func scannerDevice(_ scanner: ICScannerDevice, didCompleteScanWithError error: Error?) ``` |

Modified ICScannerDeviceDelegate.scannerDevice(_: ICScannerDevice, didScanTo: ICScannerBandData)

|  | Declaration |
| --- | --- |
| From | ``` optional func scannerDevice(_ scanner: ICScannerDevice, didScanToBandData data: ICScannerBandData) ``` |
| To | ``` optional func scannerDevice(_ scanner: ICScannerDevice, didScanTo data: ICScannerBandData) ``` |

Modified ICScannerDeviceDelegate.scannerDevice(_: ICScannerDevice, didScanTo: URL)

|  | Declaration |
| --- | --- |
| From | ``` optional func scannerDevice(_ scanner: ICScannerDevice, didScanToURL url: NSURL) ``` |
| To | ``` optional func scannerDevice(_ scanner: ICScannerDevice, didScanTo url: URL) ``` |

Modified ICScannerDeviceDelegate.scannerDevice(_: ICScannerDevice, didSelect: ICScannerFunctionalUnit, error: Error?)

|  | Declaration |
| --- | --- |
| From | ``` optional func scannerDevice(_ scanner: ICScannerDevice, didSelectFunctionalUnit functionalUnit: ICScannerFunctionalUnit, error error: NSError?) ``` |
| To | ``` optional func scannerDevice(_ scanner: ICScannerDevice, didSelect functionalUnit: ICScannerFunctionalUnit, error error: Error?) ``` |

Modified ICScannerDocumentType [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum ICScannerDocumentType : UInt {     case TypeDefault     case TypeA4     case TypeB5     case TypeUSLetter     case TypeUSLegal     case TypeA5     case TypeISOB4     case TypeISOB6     case TypeUSLedger     case TypeUSExecutive     case TypeA3     case TypeISOB3     case TypeA6     case TypeC4     case TypeC5     case TypeC6     case Type4A0     case Type2A0     case TypeA0     case TypeA1     case TypeA2     case TypeA7     case TypeA8     case TypeA9     case Type10     case TypeISOB0     case TypeISOB1     case TypeISOB2     case TypeISOB5     case TypeISOB7     case TypeISOB8     case TypeISOB9     case TypeISOB10     case TypeJISB0     case TypeJISB1     case TypeJISB2     case TypeJISB3     case TypeJISB4     case TypeJISB6     case TypeJISB7     case TypeJISB8     case TypeJISB9     case TypeJISB10     case TypeC0     case TypeC1     case TypeC2     case TypeC3     case TypeC7     case TypeC8     case TypeC9     case TypeC10     case TypeUSStatement     case TypeBusinessCard     case TypeE     case Type3R     case Type4R     case Type5R     case Type6R     case Type8R     case TypeS8R     case Type10R     case TypeS10R     case Type11R     case Type12R     case TypeS12R     case Type110     case TypeAPSH     case TypeAPSC     case TypeAPSP     case Type135     case TypeMF     case TypeLF } ``` |
| To | ``` enum ICScannerDocumentType : UInt {     case typeDefault     case typeA4     case typeB5     case typeUSLetter     case typeUSLegal     case typeA5     case typeISOB4     case typeISOB6     case typeUSLedger     case typeUSExecutive     case typeA3     case typeISOB3     case typeA6     case typeC4     case typeC5     case typeC6     case type4A0     case type2A0     case typeA0     case typeA1     case typeA2     case typeA7     case typeA8     case typeA9     case type10     case typeISOB0     case typeISOB1     case typeISOB2     case typeISOB5     case typeISOB7     case typeISOB8     case typeISOB9     case typeISOB10     case typeJISB0     case typeJISB1     case typeJISB2     case typeJISB3     case typeJISB4     case typeJISB6     case typeJISB7     case typeJISB8     case typeJISB9     case typeJISB10     case typeC0     case typeC1     case typeC2     case typeC3     case typeC7     case typeC8     case typeC9     case typeC10     case typeUSStatement     case typeBusinessCard     case typeE     case type3R     case type4R     case type5R     case type6R     case type8R     case typeS8R     case type10R     case typeS10R     case type11R     case type12R     case typeS12R     case type110     case typeAPSH     case typeAPSC     case typeAPSP     case type135     case typeMF     case typeLF } ``` |

Modified ICScannerDocumentType.type10

|  | Declaration |
| --- | --- |
| From | ``` case Type10 ``` |
| To | ``` case type10 ``` |

Modified ICScannerDocumentType.type10R

|  | Declaration |
| --- | --- |
| From | ``` case Type10R ``` |
| To | ``` case type10R ``` |

Modified ICScannerDocumentType.type110

|  | Declaration |
| --- | --- |
| From | ``` case Type110 ``` |
| To | ``` case type110 ``` |

Modified ICScannerDocumentType.type11R

|  | Declaration |
| --- | --- |
| From | ``` case Type11R ``` |
| To | ``` case type11R ``` |

Modified ICScannerDocumentType.type12R

|  | Declaration |
| --- | --- |
| From | ``` case Type12R ``` |
| To | ``` case type12R ``` |

Modified ICScannerDocumentType.type135

|  | Declaration |
| --- | --- |
| From | ``` case Type135 ``` |
| To | ``` case type135 ``` |

Modified ICScannerDocumentType.type2A0

|  | Declaration |
| --- | --- |
| From | ``` case Type2A0 ``` |
| To | ``` case type2A0 ``` |

Modified ICScannerDocumentType.type3R

|  | Declaration |
| --- | --- |
| From | ``` case Type3R ``` |
| To | ``` case type3R ``` |

Modified ICScannerDocumentType.type4A0

|  | Declaration |
| --- | --- |
| From | ``` case Type4A0 ``` |
| To | ``` case type4A0 ``` |

Modified ICScannerDocumentType.type4R

|  | Declaration |
| --- | --- |
| From | ``` case Type4R ``` |
| To | ``` case type4R ``` |

Modified ICScannerDocumentType.type5R

|  | Declaration |
| --- | --- |
| From | ``` case Type5R ``` |
| To | ``` case type5R ``` |

Modified ICScannerDocumentType.type6R

|  | Declaration |
| --- | --- |
| From | ``` case Type6R ``` |
| To | ``` case type6R ``` |

Modified ICScannerDocumentType.type8R

|  | Declaration |
| --- | --- |
| From | ``` case Type8R ``` |
| To | ``` case type8R ``` |

Modified ICScannerDocumentType.typeA0

|  | Declaration |
| --- | --- |
| From | ``` case TypeA0 ``` |
| To | ``` case typeA0 ``` |

Modified ICScannerDocumentType.typeA1

|  | Declaration |
| --- | --- |
| From | ``` case TypeA1 ``` |
| To | ``` case typeA1 ``` |

Modified ICScannerDocumentType.typeA2

|  | Declaration |
| --- | --- |
| From | ``` case TypeA2 ``` |
| To | ``` case typeA2 ``` |

Modified ICScannerDocumentType.typeA3

|  | Declaration |
| --- | --- |
| From | ``` case TypeA3 ``` |
| To | ``` case typeA3 ``` |

Modified ICScannerDocumentType.typeA4

|  | Declaration |
| --- | --- |
| From | ``` case TypeA4 ``` |
| To | ``` case typeA4 ``` |

Modified ICScannerDocumentType.typeA5

|  | Declaration |
| --- | --- |
| From | ``` case TypeA5 ``` |
| To | ``` case typeA5 ``` |

Modified ICScannerDocumentType.typeA6

|  | Declaration |
| --- | --- |
| From | ``` case TypeA6 ``` |
| To | ``` case typeA6 ``` |

Modified ICScannerDocumentType.typeA7

|  | Declaration |
| --- | --- |
| From | ``` case TypeA7 ``` |
| To | ``` case typeA7 ``` |

Modified ICScannerDocumentType.typeA8

|  | Declaration |
| --- | --- |
| From | ``` case TypeA8 ``` |
| To | ``` case typeA8 ``` |

Modified ICScannerDocumentType.typeA9

|  | Declaration |
| --- | --- |
| From | ``` case TypeA9 ``` |
| To | ``` case typeA9 ``` |

Modified ICScannerDocumentType.typeAPSC

|  | Declaration |
| --- | --- |
| From | ``` case TypeAPSC ``` |
| To | ``` case typeAPSC ``` |

Modified ICScannerDocumentType.typeAPSH

|  | Declaration |
| --- | --- |
| From | ``` case TypeAPSH ``` |
| To | ``` case typeAPSH ``` |

Modified ICScannerDocumentType.typeAPSP

|  | Declaration |
| --- | --- |
| From | ``` case TypeAPSP ``` |
| To | ``` case typeAPSP ``` |

Modified ICScannerDocumentType.typeB5

|  | Declaration |
| --- | --- |
| From | ``` case TypeB5 ``` |
| To | ``` case typeB5 ``` |

Modified ICScannerDocumentType.typeBusinessCard

|  | Declaration |
| --- | --- |
| From | ``` case TypeBusinessCard ``` |
| To | ``` case typeBusinessCard ``` |

Modified ICScannerDocumentType.typeC0

|  | Declaration |
| --- | --- |
| From | ``` case TypeC0 ``` |
| To | ``` case typeC0 ``` |

Modified ICScannerDocumentType.typeC1

|  | Declaration |
| --- | --- |
| From | ``` case TypeC1 ``` |
| To | ``` case typeC1 ``` |

Modified ICScannerDocumentType.typeC10

|  | Declaration |
| --- | --- |
| From | ``` case TypeC10 ``` |
| To | ``` case typeC10 ``` |

Modified ICScannerDocumentType.typeC2

|  | Declaration |
| --- | --- |
| From | ``` case TypeC2 ``` |
| To | ``` case typeC2 ``` |

Modified ICScannerDocumentType.typeC3

|  | Declaration |
| --- | --- |
| From | ``` case TypeC3 ``` |
| To | ``` case typeC3 ``` |

Modified ICScannerDocumentType.typeC4

|  | Declaration |
| --- | --- |
| From | ``` case TypeC4 ``` |
| To | ``` case typeC4 ``` |

Modified ICScannerDocumentType.typeC5

|  | Declaration |
| --- | --- |
| From | ``` case TypeC5 ``` |
| To | ``` case typeC5 ``` |

Modified ICScannerDocumentType.typeC6

|  | Declaration |
| --- | --- |
| From | ``` case TypeC6 ``` |
| To | ``` case typeC6 ``` |

Modified ICScannerDocumentType.typeC7

|  | Declaration |
| --- | --- |
| From | ``` case TypeC7 ``` |
| To | ``` case typeC7 ``` |

Modified ICScannerDocumentType.typeC8

|  | Declaration |
| --- | --- |
| From | ``` case TypeC8 ``` |
| To | ``` case typeC8 ``` |

Modified ICScannerDocumentType.typeC9

|  | Declaration |
| --- | --- |
| From | ``` case TypeC9 ``` |
| To | ``` case typeC9 ``` |

Modified ICScannerDocumentType.typeDefault

|  | Declaration |
| --- | --- |
| From | ``` case TypeDefault ``` |
| To | ``` case typeDefault ``` |

Modified ICScannerDocumentType.typeE

|  | Declaration |
| --- | --- |
| From | ``` case TypeE ``` |
| To | ``` case typeE ``` |

Modified ICScannerDocumentType.typeISOB0

|  | Declaration |
| --- | --- |
| From | ``` case TypeISOB0 ``` |
| To | ``` case typeISOB0 ``` |

Modified ICScannerDocumentType.typeISOB1

|  | Declaration |
| --- | --- |
| From | ``` case TypeISOB1 ``` |
| To | ``` case typeISOB1 ``` |

Modified ICScannerDocumentType.typeISOB10

|  | Declaration |
| --- | --- |
| From | ``` case TypeISOB10 ``` |
| To | ``` case typeISOB10 ``` |

Modified ICScannerDocumentType.typeISOB2

|  | Declaration |
| --- | --- |
| From | ``` case TypeISOB2 ``` |
| To | ``` case typeISOB2 ``` |

Modified ICScannerDocumentType.typeISOB3

|  | Declaration |
| --- | --- |
| From | ``` case TypeISOB3 ``` |
| To | ``` case typeISOB3 ``` |

Modified ICScannerDocumentType.typeISOB4

|  | Declaration |
| --- | --- |
| From | ``` case TypeISOB4 ``` |
| To | ``` case typeISOB4 ``` |

Modified ICScannerDocumentType.typeISOB5

|  | Declaration |
| --- | --- |
| From | ``` case TypeISOB5 ``` |
| To | ``` case typeISOB5 ``` |

Modified ICScannerDocumentType.typeISOB6

|  | Declaration |
| --- | --- |
| From | ``` case TypeISOB6 ``` |
| To | ``` case typeISOB6 ``` |

Modified ICScannerDocumentType.typeISOB7

|  | Declaration |
| --- | --- |
| From | ``` case TypeISOB7 ``` |
| To | ``` case typeISOB7 ``` |

Modified ICScannerDocumentType.typeISOB8

|  | Declaration |
| --- | --- |
| From | ``` case TypeISOB8 ``` |
| To | ``` case typeISOB8 ``` |

Modified ICScannerDocumentType.typeISOB9

|  | Declaration |
| --- | --- |
| From | ``` case TypeISOB9 ``` |
| To | ``` case typeISOB9 ``` |

Modified ICScannerDocumentType.typeJISB0

|  | Declaration |
| --- | --- |
| From | ``` case TypeJISB0 ``` |
| To | ``` case typeJISB0 ``` |

Modified ICScannerDocumentType.typeJISB1

|  | Declaration |
| --- | --- |
| From | ``` case TypeJISB1 ``` |
| To | ``` case typeJISB1 ``` |

Modified ICScannerDocumentType.typeJISB10

|  | Declaration |
| --- | --- |
| From | ``` case TypeJISB10 ``` |
| To | ``` case typeJISB10 ``` |

Modified ICScannerDocumentType.typeJISB2

|  | Declaration |
| --- | --- |
| From | ``` case TypeJISB2 ``` |
| To | ``` case typeJISB2 ``` |

Modified ICScannerDocumentType.typeJISB3

|  | Declaration |
| --- | --- |
| From | ``` case TypeJISB3 ``` |
| To | ``` case typeJISB3 ``` |

Modified ICScannerDocumentType.typeJISB4

|  | Declaration |
| --- | --- |
| From | ``` case TypeJISB4 ``` |
| To | ``` case typeJISB4 ``` |

Modified ICScannerDocumentType.typeJISB6

|  | Declaration |
| --- | --- |
| From | ``` case TypeJISB6 ``` |
| To | ``` case typeJISB6 ``` |

Modified ICScannerDocumentType.typeJISB7

|  | Declaration |
| --- | --- |
| From | ``` case TypeJISB7 ``` |
| To | ``` case typeJISB7 ``` |

Modified ICScannerDocumentType.typeJISB8

|  | Declaration |
| --- | --- |
| From | ``` case TypeJISB8 ``` |
| To | ``` case typeJISB8 ``` |

Modified ICScannerDocumentType.typeJISB9

|  | Declaration |
| --- | --- |
| From | ``` case TypeJISB9 ``` |
| To | ``` case typeJISB9 ``` |

Modified ICScannerDocumentType.typeLF

|  | Declaration |
| --- | --- |
| From | ``` case TypeLF ``` |
| To | ``` case typeLF ``` |

Modified ICScannerDocumentType.typeMF

|  | Declaration |
| --- | --- |
| From | ``` case TypeMF ``` |
| To | ``` case typeMF ``` |

Modified ICScannerDocumentType.typeS10R

|  | Declaration |
| --- | --- |
| From | ``` case TypeS10R ``` |
| To | ``` case typeS10R ``` |

Modified ICScannerDocumentType.typeS12R

|  | Declaration |
| --- | --- |
| From | ``` case TypeS12R ``` |
| To | ``` case typeS12R ``` |

Modified ICScannerDocumentType.typeS8R

|  | Declaration |
| --- | --- |
| From | ``` case TypeS8R ``` |
| To | ``` case typeS8R ``` |

Modified ICScannerDocumentType.typeUSExecutive

|  | Declaration |
| --- | --- |
| From | ``` case TypeUSExecutive ``` |
| To | ``` case typeUSExecutive ``` |

Modified ICScannerDocumentType.typeUSLedger

|  | Declaration |
| --- | --- |
| From | ``` case TypeUSLedger ``` |
| To | ``` case typeUSLedger ``` |

Modified ICScannerDocumentType.typeUSLegal

|  | Declaration |
| --- | --- |
| From | ``` case TypeUSLegal ``` |
| To | ``` case typeUSLegal ``` |

Modified ICScannerDocumentType.typeUSLetter

|  | Declaration |
| --- | --- |
| From | ``` case TypeUSLetter ``` |
| To | ``` case typeUSLetter ``` |

Modified ICScannerDocumentType.typeUSStatement

|  | Declaration |
| --- | --- |
| From | ``` case TypeUSStatement ``` |
| To | ``` case typeUSStatement ``` |

Modified ICScannerFeature

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ICScannerFeature : NSObject {     var type: ICScannerFeatureType { get }     var internalName: String? { get }     var humanReadableName: String? { get }     var tooltip: String? { get } } ``` | -- |
| To | ``` class ICScannerFeature : NSObject {     var type: ICScannerFeatureType { get }     var internalName: String? { get }     var humanReadableName: String? { get }     var tooltip: String? { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ICScannerFeature : CVarArg { } extension ICScannerFeature : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified ICScannerFeatureEnumeration

|  | Declaration |
| --- | --- |
| From | ``` class ICScannerFeatureEnumeration : ICScannerFeature {     unowned(unsafe) var currentValue: AnyObject     var defaultValue: AnyObject { get }     var values: [NSNumber] { get }     var menuItemLabels: [String] { get }     var menuItemLabelsTooltips: [String] { get } } ``` |
| To | ``` class ICScannerFeatureEnumeration : ICScannerFeature {     unowned(unsafe) var currentValue: AnyObject     var defaultValue: Any { get }     var values: [NSNumber] { get }     var menuItemLabels: [String] { get }     var menuItemLabelsTooltips: [String] { get } } ``` |

Modified ICScannerFeatureEnumeration.defaultValue

|  | Declaration |
| --- | --- |
| From | ``` var defaultValue: AnyObject { get } ``` |
| To | ``` var defaultValue: Any { get } ``` |

Modified ICScannerFeatureType [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum ICScannerFeatureType : UInt {     case Enumeration     case Range     case Boolean     case Template } ``` |
| To | ``` enum ICScannerFeatureType : UInt {     case enumeration     case range     case boolean     case template } ``` |

Modified ICScannerFeatureType.boolean

|  | Declaration |
| --- | --- |
| From | ``` case Boolean ``` |
| To | ``` case boolean ``` |

Modified ICScannerFeatureType.enumeration

|  | Declaration |
| --- | --- |
| From | ``` case Enumeration ``` |
| To | ``` case enumeration ``` |

Modified ICScannerFeatureType.range

|  | Declaration |
| --- | --- |
| From | ``` case Range ``` |
| To | ``` case range ``` |

Modified ICScannerFeatureType.template

|  | Declaration |
| --- | --- |
| From | ``` case Template ``` |
| To | ``` case template ``` |

Modified ICScannerFunctionalUnit

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ICScannerFunctionalUnit : NSObject {     var type: ICScannerFunctionalUnitType { get }     var pixelDataType: ICScannerPixelDataType     var supportedBitDepths: NSIndexSet { get }     var bitDepth: ICScannerBitDepth     var supportedMeasurementUnits: NSIndexSet { get }     var measurementUnit: ICScannerMeasurementUnit     var supportedResolutions: NSIndexSet { get }     var preferredResolutions: NSIndexSet { get }     var resolution: Int     var nativeXResolution: Int { get }     var nativeYResolution: Int { get }     var supportedScaleFactors: NSIndexSet { get }     var preferredScaleFactors: NSIndexSet { get }     var scaleFactor: Int     var templates: [ICScannerFeatureTemplate] { get }     var vendorFeatures: [ICScannerFeature]? { get }     var physicalSize: NSSize { get }     var scanArea: NSRect     var scanAreaOrientation: ICEXIFOrientationType     var acceptsThresholdForBlackAndWhiteScanning: Bool { get }     var usesThresholdForBlackAndWhiteScanning: Bool     var defaultThresholdForBlackAndWhiteScanning: UInt8 { get }     var thresholdForBlackAndWhiteScanning: UInt8     var state: ICScannerFunctionalUnitState { get }     var scanInProgress: Bool { get }     var scanProgressPercentDone: CGFloat { get }     var canPerformOverviewScan: Bool { get }     var overviewScanInProgress: Bool { get }     var overviewImage: CGImage? { get }     var overviewResolution: Int } ``` | -- |
| To | ``` class ICScannerFunctionalUnit : NSObject {     var type: ICScannerFunctionalUnitType { get }     var pixelDataType: ICScannerPixelDataType     var supportedBitDepths: IndexSet { get }     var bitDepth: ICScannerBitDepth     var supportedMeasurementUnits: IndexSet { get }     var measurementUnit: ICScannerMeasurementUnit     var supportedResolutions: IndexSet { get }     var preferredResolutions: IndexSet { get }     var resolution: Int     var nativeXResolution: Int { get }     var nativeYResolution: Int { get }     var supportedScaleFactors: IndexSet { get }     var preferredScaleFactors: IndexSet { get }     var scaleFactor: Int     var templates: [ICScannerFeatureTemplate] { get }     var vendorFeatures: [ICScannerFeature]? { get }     var physicalSize: NSSize { get }     var scanArea: NSRect     var scanAreaOrientation: ICEXIFOrientationType     var acceptsThresholdForBlackAndWhiteScanning: Bool { get }     var usesThresholdForBlackAndWhiteScanning: Bool     var defaultThresholdForBlackAndWhiteScanning: UInt8 { get }     var thresholdForBlackAndWhiteScanning: UInt8     var state: ICScannerFunctionalUnitState { get }     var scanInProgress: Bool { get }     var scanProgressPercentDone: CGFloat { get }     var canPerformOverviewScan: Bool { get }     var overviewScanInProgress: Bool { get }     var overviewImage: CGImage? { get }     var overviewResolution: Int     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ICScannerFunctionalUnit : CVarArg { } extension ICScannerFunctionalUnit : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified ICScannerFunctionalUnit.preferredResolutions

|  | Declaration |
| --- | --- |
| From | ``` var preferredResolutions: NSIndexSet { get } ``` |
| To | ``` var preferredResolutions: IndexSet { get } ``` |

Modified ICScannerFunctionalUnit.preferredScaleFactors

|  | Declaration |
| --- | --- |
| From | ``` var preferredScaleFactors: NSIndexSet { get } ``` |
| To | ``` var preferredScaleFactors: IndexSet { get } ``` |

Modified ICScannerFunctionalUnit.supportedBitDepths

|  | Declaration |
| --- | --- |
| From | ``` var supportedBitDepths: NSIndexSet { get } ``` |
| To | ``` var supportedBitDepths: IndexSet { get } ``` |

Modified ICScannerFunctionalUnit.supportedMeasurementUnits

|  | Declaration |
| --- | --- |
| From | ``` var supportedMeasurementUnits: NSIndexSet { get } ``` |
| To | ``` var supportedMeasurementUnits: IndexSet { get } ``` |

Modified ICScannerFunctionalUnit.supportedResolutions

|  | Declaration |
| --- | --- |
| From | ``` var supportedResolutions: NSIndexSet { get } ``` |
| To | ``` var supportedResolutions: IndexSet { get } ``` |

Modified ICScannerFunctionalUnit.supportedScaleFactors

|  | Declaration |
| --- | --- |
| From | ``` var supportedScaleFactors: NSIndexSet { get } ``` |
| To | ``` var supportedScaleFactors: IndexSet { get } ``` |

Modified ICScannerFunctionalUnitDocumentFeeder

|  | Declaration |
| --- | --- |
| From | ``` class ICScannerFunctionalUnitDocumentFeeder : ICScannerFunctionalUnit {     var supportedDocumentTypes: NSIndexSet { get }     var documentType: ICScannerDocumentType     var documentSize: NSSize { get }     var supportsDuplexScanning: Bool { get }     var duplexScanningEnabled: Bool     var documentLoaded: Bool { get }     var oddPageOrientation: ICEXIFOrientationType     var evenPageOrientation: ICEXIFOrientationType     var reverseFeederPageOrder: Bool { get } } ``` |
| To | ``` class ICScannerFunctionalUnitDocumentFeeder : ICScannerFunctionalUnit {     var supportedDocumentTypes: IndexSet { get }     var documentType: ICScannerDocumentType     var documentSize: NSSize { get }     var supportsDuplexScanning: Bool { get }     var duplexScanningEnabled: Bool     var documentLoaded: Bool { get }     var oddPageOrientation: ICEXIFOrientationType     var evenPageOrientation: ICEXIFOrientationType     var reverseFeederPageOrder: Bool { get } } ``` |

Modified ICScannerFunctionalUnitDocumentFeeder.supportedDocumentTypes

|  | Declaration |
| --- | --- |
| From | ``` var supportedDocumentTypes: NSIndexSet { get } ``` |
| To | ``` var supportedDocumentTypes: IndexSet { get } ``` |

Modified ICScannerFunctionalUnitFlatbed

|  | Declaration |
| --- | --- |
| From | ``` class ICScannerFunctionalUnitFlatbed : ICScannerFunctionalUnit {     var supportedDocumentTypes: NSIndexSet { get }     var documentType: ICScannerDocumentType     var documentSize: NSSize { get } } ``` |
| To | ``` class ICScannerFunctionalUnitFlatbed : ICScannerFunctionalUnit {     var supportedDocumentTypes: IndexSet { get }     var documentType: ICScannerDocumentType     var documentSize: NSSize { get } } ``` |

Modified ICScannerFunctionalUnitFlatbed.supportedDocumentTypes

|  | Declaration |
| --- | --- |
| From | ``` var supportedDocumentTypes: NSIndexSet { get } ``` |
| To | ``` var supportedDocumentTypes: IndexSet { get } ``` |

Modified ICScannerFunctionalUnitNegativeTransparency

|  | Declaration |
| --- | --- |
| From | ``` class ICScannerFunctionalUnitNegativeTransparency : ICScannerFunctionalUnit {     var supportedDocumentTypes: NSIndexSet { get }     var documentType: ICScannerDocumentType     var documentSize: NSSize { get } } ``` |
| To | ``` class ICScannerFunctionalUnitNegativeTransparency : ICScannerFunctionalUnit {     var supportedDocumentTypes: IndexSet { get }     var documentType: ICScannerDocumentType     var documentSize: NSSize { get } } ``` |

Modified ICScannerFunctionalUnitNegativeTransparency.supportedDocumentTypes

|  | Declaration |
| --- | --- |
| From | ``` var supportedDocumentTypes: NSIndexSet { get } ``` |
| To | ``` var supportedDocumentTypes: IndexSet { get } ``` |

Modified ICScannerFunctionalUnitPositiveTransparency

|  | Declaration |
| --- | --- |
| From | ``` class ICScannerFunctionalUnitPositiveTransparency : ICScannerFunctionalUnit {     var supportedDocumentTypes: NSIndexSet { get }     var documentType: ICScannerDocumentType     var documentSize: NSSize { get } } ``` |
| To | ``` class ICScannerFunctionalUnitPositiveTransparency : ICScannerFunctionalUnit {     var supportedDocumentTypes: IndexSet { get }     var documentType: ICScannerDocumentType     var documentSize: NSSize { get } } ``` |

Modified ICScannerFunctionalUnitPositiveTransparency.supportedDocumentTypes

|  | Declaration |
| --- | --- |
| From | ``` var supportedDocumentTypes: NSIndexSet { get } ``` |
| To | ``` var supportedDocumentTypes: IndexSet { get } ``` |

Modified ICScannerFunctionalUnitState [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum ICScannerFunctionalUnitState : UInt32 {     case Ready     case ScanInProgress     case OverviewScanInProgress } ``` |
| To | ``` enum ICScannerFunctionalUnitState : UInt32 {     case ready     case scanInProgress     case overviewScanInProgress } ``` |

Modified ICScannerFunctionalUnitState.overviewScanInProgress

|  | Declaration |
| --- | --- |
| From | ``` case OverviewScanInProgress ``` |
| To | ``` case overviewScanInProgress ``` |

Modified ICScannerFunctionalUnitState.ready

|  | Declaration |
| --- | --- |
| From | ``` case Ready ``` |
| To | ``` case ready ``` |

Modified ICScannerFunctionalUnitState.scanInProgress

|  | Declaration |
| --- | --- |
| From | ``` case ScanInProgress ``` |
| To | ``` case scanInProgress ``` |

Modified ICScannerFunctionalUnitType [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum ICScannerFunctionalUnitType : UInt {     case Flatbed     case PositiveTransparency     case NegativeTransparency     case DocumentFeeder } ``` |
| To | ``` enum ICScannerFunctionalUnitType : UInt {     case flatbed     case positiveTransparency     case negativeTransparency     case documentFeeder } ``` |

Modified ICScannerFunctionalUnitType.documentFeeder

|  | Declaration |
| --- | --- |
| From | ``` case DocumentFeeder ``` |
| To | ``` case documentFeeder ``` |

Modified ICScannerFunctionalUnitType.flatbed

|  | Declaration |
| --- | --- |
| From | ``` case Flatbed ``` |
| To | ``` case flatbed ``` |

Modified ICScannerFunctionalUnitType.negativeTransparency

|  | Declaration |
| --- | --- |
| From | ``` case NegativeTransparency ``` |
| To | ``` case negativeTransparency ``` |

Modified ICScannerFunctionalUnitType.positiveTransparency

|  | Declaration |
| --- | --- |
| From | ``` case PositiveTransparency ``` |
| To | ``` case positiveTransparency ``` |

Modified ICScannerMeasurementUnit [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum ICScannerMeasurementUnit : UInt {     case Inches     case Centimeters     case Picas     case Points     case Twips     case Pixels } ``` |
| To | ``` enum ICScannerMeasurementUnit : UInt {     case inches     case centimeters     case picas     case points     case twips     case pixels } ``` |

Modified ICScannerMeasurementUnit.centimeters

|  | Declaration |
| --- | --- |
| From | ``` case Centimeters ``` |
| To | ``` case centimeters ``` |

Modified ICScannerMeasurementUnit.inches

|  | Declaration |
| --- | --- |
| From | ``` case Inches ``` |
| To | ``` case inches ``` |

Modified ICScannerMeasurementUnit.picas

|  | Declaration |
| --- | --- |
| From | ``` case Picas ``` |
| To | ``` case picas ``` |

Modified ICScannerMeasurementUnit.pixels

|  | Declaration |
| --- | --- |
| From | ``` case Pixels ``` |
| To | ``` case pixels ``` |

Modified ICScannerMeasurementUnit.points

|  | Declaration |
| --- | --- |
| From | ``` case Points ``` |
| To | ``` case points ``` |

Modified ICScannerMeasurementUnit.twips

|  | Declaration |
| --- | --- |
| From | ``` case Twips ``` |
| To | ``` case twips ``` |

Modified ICScannerPixelDataType [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum ICScannerPixelDataType : UInt {     case BW     case Gray     case RGB     case Palette     case CMY     case CMYK     case YUV     case YUVK     case CIEXYZ } ``` |
| To | ``` enum ICScannerPixelDataType : UInt {     case BW     case gray     case RGB     case palette     case CMY     case CMYK     case YUV     case YUVK     case CIEXYZ } ``` |

Modified ICScannerPixelDataType.gray

|  | Declaration |
| --- | --- |
| From | ``` case Gray ``` |
| To | ``` case gray ``` |

Modified ICScannerPixelDataType.palette

|  | Declaration |
| --- | --- |
| From | ``` case Palette ``` |
| To | ``` case palette ``` |

Modified ICScannerTransferMode [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum ICScannerTransferMode : UInt {     case FileBased     case MemoryBased } ``` |
| To | ``` enum ICScannerTransferMode : UInt {     case fileBased     case memoryBased } ``` |

Modified ICScannerTransferMode.fileBased

|  | Declaration |
| --- | --- |
| From | ``` case FileBased ``` |
| To | ``` case fileBased ``` |

Modified ICScannerTransferMode.memoryBased

|  | Declaration |
| --- | --- |
| From | ``` case MemoryBased ``` |
| To | ``` case memoryBased ``` |

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
