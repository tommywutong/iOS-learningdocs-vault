---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/ExternalAccessory.html
archived_at: '2026-07-18T02:55:20.704520Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# ExternalAccessory Changes for Swift

### ExternalAccessory

Added [EABluetoothAccessoryPickerError [struct]](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererror)Added [EABluetoothAccessoryPickerError.alreadyConnected](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererror/2335351-alreadyconnected)Added EABluetoothAccessoryPickerError.init(_nsError: NSError)Added [EABluetoothAccessoryPickerError.resultCancelled](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererror/2335353-resultcancelled)Added [EABluetoothAccessoryPickerError.resultFailed](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererror/2335352-resultfailed)Added [EABluetoothAccessoryPickerError.resultNotFound](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererror/2335354-resultnotfound)Modified [EAAccessory](https://developer.apple.com/documentation/externalaccessory/eaaccessory)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class EAAccessory : NSObject {     var connected: Bool { get }     var connectionID: Int { get }     var manufacturer: String { get }     var name: String { get }     var modelNumber: String { get }     var serialNumber: String { get }     var firmwareRevision: String { get }     var hardwareRevision: String { get }     var dockType: String { get }     var protocolStrings: [String] { get }     unowned(unsafe) var delegate: EAAccessoryDelegate? } ``` | -- |
| To | ``` class EAAccessory : NSObject {     var isConnected: Bool { get }     var connectionID: Int { get }     var manufacturer: String { get }     var name: String { get }     var modelNumber: String { get }     var serialNumber: String { get }     var firmwareRevision: String { get }     var hardwareRevision: String { get }     var dockType: String { get }     var protocolStrings: [String] { get }     unowned(unsafe) var delegate: EAAccessoryDelegate?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension EAAccessory : CVarArg { } extension EAAccessory : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [EAAccessory.isConnected](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613803-isconnected)

|  | Declaration |
| --- | --- |
| From | ``` var connected: Bool { get } ``` |
| To | ``` var isConnected: Bool { get } ``` |

Modified [EAAccessoryManager](https://developer.apple.com/documentation/externalaccessory/eaaccessorymanager)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class EAAccessoryManager : NSObject {     class func sharedAccessoryManager() -> EAAccessoryManager     func showBluetoothAccessoryPickerWithNameFilter(_ predicate: NSPredicate?, completion completion: EABluetoothAccessoryPickerCompletion?)     func registerForLocalNotifications()     func unregisterForLocalNotifications()     var connectedAccessories: [EAAccessory] { get } } ``` | -- |
| To | ``` class EAAccessoryManager : NSObject {     class func shared() -> EAAccessoryManager     func showBluetoothAccessoryPicker(withNameFilter predicate: NSPredicate?, completion completion: ExternalAccessory.EABluetoothAccessoryPickerCompletion? = nil)     func registerForLocalNotifications()     func unregisterForLocalNotifications()     var connectedAccessories: [EAAccessory] { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension EAAccessoryManager : CVarArg { } extension EAAccessoryManager : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [EAAccessoryManager.shared() -> EAAccessoryManager [class]](https://developer.apple.com/documentation/externalaccessory/eaaccessorymanager/1613887-shared)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedAccessoryManager() -> EAAccessoryManager ``` |
| To | ``` class func shared() -> EAAccessoryManager ``` |

Modified [EAAccessoryManager.showBluetoothAccessoryPicker(withNameFilter: NSPredicate?, completion: ExternalAccessory.EABluetoothAccessoryPickerCompletion?)](https://developer.apple.com/documentation/externalaccessory/eaaccessorymanager/1613913-showbluetoothaccessorypickerwith)

|  | Declaration |
| --- | --- |
| From | ``` func showBluetoothAccessoryPickerWithNameFilter(_ predicate: NSPredicate?, completion completion: EABluetoothAccessoryPickerCompletion?) ``` |
| To | ``` func showBluetoothAccessoryPicker(withNameFilter predicate: NSPredicate?, completion completion: ExternalAccessory.EABluetoothAccessoryPickerCompletion? = nil) ``` |

Modified [EABluetoothAccessoryPickerError.Code [enum]](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererrorcode)

|  | Declaration |
| --- | --- |
| From | ``` enum EABluetoothAccessoryPickerErrorCode : Int {     case AlreadyConnected     case ResultNotFound     case ResultCancelled     case ResultFailed } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = EABluetoothAccessoryPickerError         case alreadyConnected         case resultNotFound         case resultCancelled         case resultFailed     } ``` |

Modified [EABluetoothAccessoryPickerError.Code.alreadyConnected](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererrorcode/eabluetoothaccessorypickeralreadyconnected)

|  | Declaration |
| --- | --- |
| From | ``` case AlreadyConnected ``` |
| To | ``` case alreadyConnected ``` |

Modified [EABluetoothAccessoryPickerError.Code.resultCancelled](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererrorcode/eabluetoothaccessorypickerresultcancelled)

|  | Declaration |
| --- | --- |
| From | ``` case ResultCancelled ``` |
| To | ``` case resultCancelled ``` |

Modified [EABluetoothAccessoryPickerError.Code.resultFailed](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererrorcode/eabluetoothaccessorypickerresultfailed)

|  | Declaration |
| --- | --- |
| From | ``` case ResultFailed ``` |
| To | ``` case resultFailed ``` |

Modified [EABluetoothAccessoryPickerError.Code.resultNotFound](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererrorcode/eabluetoothaccessorypickerresultnotfound)

|  | Declaration |
| --- | --- |
| From | ``` case ResultNotFound ``` |
| To | ``` case resultNotFound ``` |

Modified [EASession](https://developer.apple.com/documentation/externalaccessory/easession)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class EASession : NSObject {     init(accessory accessory: EAAccessory, forProtocol protocolString: String)     var accessory: EAAccessory { get }     var protocolString: String { get }     var inputStream: NSInputStream? { get }     var outputStream: NSOutputStream? { get } } ``` | -- |
| To | ``` class EASession : NSObject {     init(accessory accessory: EAAccessory, forProtocol protocolString: String)     var accessory: EAAccessory { get }     var protocolString: String { get }     var inputStream: InputStream? { get }     var outputStream: OutputStream? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension EASession : CVarArg { } extension EASession : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [EASession.inputStream](https://developer.apple.com/documentation/externalaccessory/easession/1613867-inputstream)

|  | Declaration |
| --- | --- |
| From | ``` var inputStream: NSInputStream? { get } ``` |
| To | ``` var inputStream: InputStream? { get } ``` |

Modified [EASession.outputStream](https://developer.apple.com/documentation/externalaccessory/easession/1613823-outputstream)

|  | Declaration |
| --- | --- |
| From | ``` var outputStream: NSOutputStream? { get } ``` |
| To | ``` var outputStream: OutputStream? { get } ``` |

Modified [EAWiFiUnconfiguredAccessory](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class EAWiFiUnconfiguredAccessory : NSObject {     var name: String { get }     var manufacturer: String { get }     var model: String { get }     var ssid: String { get }     var macAddress: String { get }     var properties: EAWiFiUnconfiguredAccessoryProperties { get } } ``` | -- |
| To | ``` class EAWiFiUnconfiguredAccessory : NSObject {     var name: String { get }     var manufacturer: String { get }     var model: String { get }     var ssid: String { get }     var macAddress: String { get }     var properties: EAWiFiUnconfiguredAccessoryProperties { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension EAWiFiUnconfiguredAccessory : CVarArg { } extension EAWiFiUnconfiguredAccessory : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [EAWiFiUnconfiguredAccessoryBrowser](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class EAWiFiUnconfiguredAccessoryBrowser : NSObject {     weak var delegate: EAWiFiUnconfiguredAccessoryBrowserDelegate?     var unconfiguredAccessories: Set<EAWiFiUnconfiguredAccessory> { get }     init(delegate delegate: EAWiFiUnconfiguredAccessoryBrowserDelegate?, queue queue: dispatch_queue_t?)     func startSearchingForUnconfiguredAccessoriesMatchingPredicate(_ predicate: NSPredicate?)     func stopSearchingForUnconfiguredAccessories()     func configureAccessory(_ accessory: EAWiFiUnconfiguredAccessory, withConfigurationUIOnViewController viewController: UIViewController) } ``` | -- |
| To | ``` class EAWiFiUnconfiguredAccessoryBrowser : NSObject {     weak var delegate: EAWiFiUnconfiguredAccessoryBrowserDelegate?     var unconfiguredAccessories: Set<EAWiFiUnconfiguredAccessory> { get }     init(delegate delegate: EAWiFiUnconfiguredAccessoryBrowserDelegate?, queue queue: DispatchQueue?)     func startSearchingForUnconfiguredAccessories(matching predicate: NSPredicate?)     func stopSearchingForUnconfiguredAccessories()     func configureAccessory(_ accessory: EAWiFiUnconfiguredAccessory, withConfigurationUIOn viewController: UIViewController)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension EAWiFiUnconfiguredAccessoryBrowser : CVarArg { } extension EAWiFiUnconfiguredAccessoryBrowser : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [EAWiFiUnconfiguredAccessoryBrowser.configureAccessory(_: EAWiFiUnconfiguredAccessory, withConfigurationUIOn: UIViewController)](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/1613907-configureaccessory)

|  | Declaration |
| --- | --- |
| From | ``` func configureAccessory(_ accessory: EAWiFiUnconfiguredAccessory, withConfigurationUIOnViewController viewController: UIViewController) ``` |
| To | ``` func configureAccessory(_ accessory: EAWiFiUnconfiguredAccessory, withConfigurationUIOn viewController: UIViewController) ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowser.init(delegate: EAWiFiUnconfiguredAccessoryBrowserDelegate?, queue: DispatchQueue?)](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/1613881-initwithdelegate)

|  | Declaration |
| --- | --- |
| From | ``` init(delegate delegate: EAWiFiUnconfiguredAccessoryBrowserDelegate?, queue queue: dispatch_queue_t?) ``` |
| To | ``` init(delegate delegate: EAWiFiUnconfiguredAccessoryBrowserDelegate?, queue queue: DispatchQueue?) ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowser.startSearchingForUnconfiguredAccessories(matching: NSPredicate?)](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/1613869-startsearchingforunconfiguredacc)

|  | Declaration |
| --- | --- |
| From | ``` func startSearchingForUnconfiguredAccessoriesMatchingPredicate(_ predicate: NSPredicate?) ``` |
| To | ``` func startSearchingForUnconfiguredAccessories(matching predicate: NSPredicate?) ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowserDelegate](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol EAWiFiUnconfiguredAccessoryBrowserDelegate : NSObjectProtocol {     func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didUpdateState state: EAWiFiUnconfiguredAccessoryBrowserState)     func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didFindUnconfiguredAccessories accessories: Set<EAWiFiUnconfiguredAccessory>)     func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didRemoveUnconfiguredAccessories accessories: Set<EAWiFiUnconfiguredAccessory>)     func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didFinishConfiguringAccessory accessory: EAWiFiUnconfiguredAccessory, withStatus status: EAWiFiUnconfiguredAccessoryConfigurationStatus) } ``` |
| To | ``` protocol EAWiFiUnconfiguredAccessoryBrowserDelegate : NSObjectProtocol {     func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didUpdate state: EAWiFiUnconfiguredAccessoryBrowserState)     func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didFindUnconfiguredAccessories accessories: Set<EAWiFiUnconfiguredAccessory>)     func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didRemoveUnconfiguredAccessories accessories: Set<EAWiFiUnconfiguredAccessory>)     func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didFinishConfiguringAccessory accessory: EAWiFiUnconfiguredAccessory, with status: EAWiFiUnconfiguredAccessoryConfigurationStatus) } ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowserDelegate.accessoryBrowser(_: EAWiFiUnconfiguredAccessoryBrowser, didFinishConfiguringAccessory: EAWiFiUnconfiguredAccessory, with: EAWiFiUnconfiguredAccessoryConfigurationStatus)](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserdelegate/1613911-accessorybrowser)

|  | Declaration |
| --- | --- |
| From | ``` func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didFinishConfiguringAccessory accessory: EAWiFiUnconfiguredAccessory, withStatus status: EAWiFiUnconfiguredAccessoryConfigurationStatus) ``` |
| To | ``` func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didFinishConfiguringAccessory accessory: EAWiFiUnconfiguredAccessory, with status: EAWiFiUnconfiguredAccessoryConfigurationStatus) ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowserDelegate.accessoryBrowser(_: EAWiFiUnconfiguredAccessoryBrowser, didUpdate: EAWiFiUnconfiguredAccessoryBrowserState)](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserdelegate/1613845-accessorybrowser)

|  | Declaration |
| --- | --- |
| From | ``` func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didUpdateState state: EAWiFiUnconfiguredAccessoryBrowserState) ``` |
| To | ``` func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didUpdate state: EAWiFiUnconfiguredAccessoryBrowserState) ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowserState [enum]](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserstate)

|  | Declaration |
| --- | --- |
| From | ``` enum EAWiFiUnconfiguredAccessoryBrowserState : Int {     case WiFiUnavailable     case Stopped     case Searching     case Configuring } ``` |
| To | ``` enum EAWiFiUnconfiguredAccessoryBrowserState : Int {     case wiFiUnavailable     case stopped     case searching     case configuring } ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowserState.configuring](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserstate/configuring)

|  | Declaration |
| --- | --- |
| From | ``` case Configuring ``` |
| To | ``` case configuring ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowserState.searching](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserstate/searching)

|  | Declaration |
| --- | --- |
| From | ``` case Searching ``` |
| To | ``` case searching ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowserState.stopped](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserstate/stopped)

|  | Declaration |
| --- | --- |
| From | ``` case Stopped ``` |
| To | ``` case stopped ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowserState.wiFiUnavailable](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserstate/eawifiunconfiguredaccessorybrowserstatewifiunavailable)

|  | Declaration |
| --- | --- |
| From | ``` case WiFiUnavailable ``` |
| To | ``` case wiFiUnavailable ``` |

Modified [EAWiFiUnconfiguredAccessoryConfigurationStatus [enum]](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryconfigurationstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum EAWiFiUnconfiguredAccessoryConfigurationStatus : Int {     case Success     case UserCancelledConfiguration     case Failed } ``` |
| To | ``` enum EAWiFiUnconfiguredAccessoryConfigurationStatus : Int {     case success     case userCancelledConfiguration     case failed } ``` |

Modified [EAWiFiUnconfiguredAccessoryConfigurationStatus.failed](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryconfigurationstatus/eawifiunconfiguredaccessoryconfigurationstatusfailed)

|  | Declaration |
| --- | --- |
| From | ``` case Failed ``` |
| To | ``` case failed ``` |

Modified [EAWiFiUnconfiguredAccessoryConfigurationStatus.success](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryconfigurationstatus/success)

|  | Declaration |
| --- | --- |
| From | ``` case Success ``` |
| To | ``` case success ``` |

Modified [EAWiFiUnconfiguredAccessoryConfigurationStatus.userCancelledConfiguration](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryconfigurationstatus/usercancelledconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` case UserCancelledConfiguration ``` |
| To | ``` case userCancelledConfiguration ``` |

Modified [EAWiFiUnconfiguredAccessoryProperties [struct]](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryproperties)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct EAWiFiUnconfiguredAccessoryProperties : OptionSetType {     init(rawValue rawValue: UInt)     static var PropertySupportsAirPlay: EAWiFiUnconfiguredAccessoryProperties { get }     static var PropertySupportsAirPrint: EAWiFiUnconfiguredAccessoryProperties { get }     static var PropertySupportsHomeKit: EAWiFiUnconfiguredAccessoryProperties { get } } ``` | OptionSetType |
| To | ``` struct EAWiFiUnconfiguredAccessoryProperties : OptionSet {     init(rawValue rawValue: UInt)     static var propertySupportsAirPlay: EAWiFiUnconfiguredAccessoryProperties { get }     static var propertySupportsAirPrint: EAWiFiUnconfiguredAccessoryProperties { get }     static var propertySupportsHomeKit: EAWiFiUnconfiguredAccessoryProperties { get }     func intersect(_ other: EAWiFiUnconfiguredAccessoryProperties) -> EAWiFiUnconfiguredAccessoryProperties     func exclusiveOr(_ other: EAWiFiUnconfiguredAccessoryProperties) -> EAWiFiUnconfiguredAccessoryProperties     mutating func unionInPlace(_ other: EAWiFiUnconfiguredAccessoryProperties)     mutating func intersectInPlace(_ other: EAWiFiUnconfiguredAccessoryProperties)     mutating func exclusiveOrInPlace(_ other: EAWiFiUnconfiguredAccessoryProperties)     func isSubsetOf(_ other: EAWiFiUnconfiguredAccessoryProperties) -> Bool     func isDisjointWith(_ other: EAWiFiUnconfiguredAccessoryProperties) -> Bool     func isSupersetOf(_ other: EAWiFiUnconfiguredAccessoryProperties) -> Bool     mutating func subtractInPlace(_ other: EAWiFiUnconfiguredAccessoryProperties)     func isStrictSupersetOf(_ other: EAWiFiUnconfiguredAccessoryProperties) -> Bool     func isStrictSubsetOf(_ other: EAWiFiUnconfiguredAccessoryProperties) -> Bool } extension EAWiFiUnconfiguredAccessoryProperties {     func union(_ other: EAWiFiUnconfiguredAccessoryProperties) -> EAWiFiUnconfiguredAccessoryProperties     func intersection(_ other: EAWiFiUnconfiguredAccessoryProperties) -> EAWiFiUnconfiguredAccessoryProperties     func symmetricDifference(_ other: EAWiFiUnconfiguredAccessoryProperties) -> EAWiFiUnconfiguredAccessoryProperties } extension EAWiFiUnconfiguredAccessoryProperties {     func contains(_ member: EAWiFiUnconfiguredAccessoryProperties) -> Bool     mutating func insert(_ newMember: EAWiFiUnconfiguredAccessoryProperties) -> (inserted: Bool, memberAfterInsert: EAWiFiUnconfiguredAccessoryProperties)     mutating func remove(_ member: EAWiFiUnconfiguredAccessoryProperties) -> EAWiFiUnconfiguredAccessoryProperties?     mutating func update(with newMember: EAWiFiUnconfiguredAccessoryProperties) -> EAWiFiUnconfiguredAccessoryProperties? } extension EAWiFiUnconfiguredAccessoryProperties {     convenience init()     mutating func formUnion(_ other: EAWiFiUnconfiguredAccessoryProperties)     mutating func formIntersection(_ other: EAWiFiUnconfiguredAccessoryProperties)     mutating func formSymmetricDifference(_ other: EAWiFiUnconfiguredAccessoryProperties) } extension EAWiFiUnconfiguredAccessoryProperties {     convenience init<S : Sequence where S.Iterator.Element == EAWiFiUnconfiguredAccessoryProperties>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: EAWiFiUnconfiguredAccessoryProperties...)     mutating func subtract(_ other: EAWiFiUnconfiguredAccessoryProperties)     func isSubset(of other: EAWiFiUnconfiguredAccessoryProperties) -> Bool     func isSuperset(of other: EAWiFiUnconfiguredAccessoryProperties) -> Bool     func isDisjoint(with other: EAWiFiUnconfiguredAccessoryProperties) -> Bool     func subtracting(_ other: EAWiFiUnconfiguredAccessoryProperties) -> EAWiFiUnconfiguredAccessoryProperties     var isEmpty: Bool { get }     func isStrictSuperset(of other: EAWiFiUnconfiguredAccessoryProperties) -> Bool     func isStrictSubset(of other: EAWiFiUnconfiguredAccessoryProperties) -> Bool } ``` | OptionSet |

Modified [EAWiFiUnconfiguredAccessoryProperties.propertySupportsAirPlay](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryproperties/1613793-propertysupportsairplay)

|  | Declaration |
| --- | --- |
| From | ``` static var PropertySupportsAirPlay: EAWiFiUnconfiguredAccessoryProperties { get } ``` |
| To | ``` static var propertySupportsAirPlay: EAWiFiUnconfiguredAccessoryProperties { get } ``` |

Modified [EAWiFiUnconfiguredAccessoryProperties.propertySupportsAirPrint](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryproperties/eawifiunconfiguredaccessorypropertysupportsairprint)

|  | Declaration |
| --- | --- |
| From | ``` static var PropertySupportsAirPrint: EAWiFiUnconfiguredAccessoryProperties { get } ``` |
| To | ``` static var propertySupportsAirPrint: EAWiFiUnconfiguredAccessoryProperties { get } ``` |

Modified [EAWiFiUnconfiguredAccessoryProperties.propertySupportsHomeKit](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryproperties/eawifiunconfiguredaccessorypropertysupportshomekit)

|  | Declaration |
| --- | --- |
| From | ``` static var PropertySupportsHomeKit: EAWiFiUnconfiguredAccessoryProperties { get } ``` |
| To | ``` static var propertySupportsHomeKit: EAWiFiUnconfiguredAccessoryProperties { get } ``` |

Modified [NSNotification.Name.EAAccessoryDidConnect](https://developer.apple.com/documentation/externalaccessory/eaaccessorydidconnectnotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | EAAccessoryDidConnectNotification | ``` let EAAccessoryDidConnectNotification: String ``` |
| To | EAAccessoryDidConnect | ``` static let EAAccessoryDidConnect: NSNotification.Name ``` |

Modified [NSNotification.Name.EAAccessoryDidDisconnect](https://developer.apple.com/documentation/foundation/nsnotification/name/1613901-eaaccessorydiddisconnect)

|  | Name | Declaration |
| --- | --- | --- |
| From | EAAccessoryDidDisconnectNotification | ``` let EAAccessoryDidDisconnectNotification: String ``` |
| To | EAAccessoryDidDisconnect | ``` static let EAAccessoryDidDisconnect: NSNotification.Name ``` |

Modified [EABluetoothAccessoryPickerCompletion](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickercompletion)

|  | Declaration |
| --- | --- |
| From | ``` typealias EABluetoothAccessoryPickerCompletion = (NSError?) -> Void ``` |
| To | ``` typealias EABluetoothAccessoryPickerCompletion = (Error?) -> Swift.Void ``` |

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
