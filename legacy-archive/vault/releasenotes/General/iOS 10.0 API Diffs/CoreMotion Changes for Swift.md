---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/CoreMotion.html
archived_at: '2026-07-18T02:55:16.445507Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# CoreMotion Changes for Swift

### CoreMotion

Removed [CMMagneticFieldCalibrationAccuracy [struct]](https://developer.apple.com/documentation/coremotion/cmmagneticfieldcalibrationaccuracy)Removed CMMagneticFieldCalibrationAccuracy.init(_: Int32)Removed CMMagneticFieldCalibrationAccuracy.init(rawValue: Int32)Removed CMMagneticFieldCalibrationAccuracy.rawValueRemoved [CMMagneticFieldCalibrationAccuracyHigh](https://developer.apple.com/documentation/coremotion/cmmagneticfieldcalibrationaccuracy/high)Removed [CMMagneticFieldCalibrationAccuracyLow](https://developer.apple.com/documentation/coremotion/cmmagneticfieldcalibrationaccuracy/cmmagneticfieldcalibrationaccuracylow)Removed [CMMagneticFieldCalibrationAccuracyMedium](https://developer.apple.com/documentation/coremotion/cmmagneticfieldcalibrationaccuracy/medium)Removed [CMMagneticFieldCalibrationAccuracyUncalibrated](https://developer.apple.com/documentation/coremotion/cmmagneticfieldcalibrationaccuracy/uncalibrated)Added [CMMagneticFieldCalibrationAccuracy [enum]](https://developer.apple.com/documentation/coremotion/cmmagneticfieldcalibrationaccuracy)Added [CMMagneticFieldCalibrationAccuracy.high](https://developer.apple.com/documentation/coremotion/cmmagneticfieldcalibrationaccuracy/cmmagneticfieldcalibrationaccuracyhigh)Added [CMMagneticFieldCalibrationAccuracy.low](https://developer.apple.com/documentation/coremotion/cmmagneticfieldcalibrationaccuracy/cmmagneticfieldcalibrationaccuracylow)Added [CMMagneticFieldCalibrationAccuracy.medium](https://developer.apple.com/documentation/coremotion/cmmagneticfieldcalibrationaccuracy/medium)Added [CMMagneticFieldCalibrationAccuracy.uncalibrated](https://developer.apple.com/documentation/coremotion/cmmagneticfieldcalibrationaccuracy/uncalibrated)Added [CMPedometer.isPedometerEventTrackingAvailable() -> Bool [class]](https://developer.apple.com/documentation/coremotion/cmpedometer/1778440-ispedometereventtrackingavailabl)Added [CMPedometer.startEventUpdates(handler: CoreMotion.CMPedometerEventHandler)](https://developer.apple.com/documentation/coremotion/cmpedometer/1778437-starteventupdates)Added [CMPedometer.stopEventUpdates()](https://developer.apple.com/documentation/coremotion/cmpedometer/1778446-stoppedometereventupdates)Added [CMPedometerData.averageActivePace](https://developer.apple.com/documentation/coremotion/cmpedometerdata/1649705-averageactivepace)Added [CMPedometerEvent](https://developer.apple.com/documentation/coremotion/cmpedometerevent)Added [CMPedometerEvent.date](https://developer.apple.com/documentation/coremotion/cmpedometerevent/1778439-date)Added [CMPedometerEvent.type](https://developer.apple.com/documentation/coremotion/cmpedometerevent/1778448-type)Added [CMPedometerEventType [enum]](https://developer.apple.com/documentation/coremotion/cmpedometereventtype)Added [CMPedometerEventType.pause](https://developer.apple.com/documentation/coremotion/cmpedometereventtype/cmpedometereventtypepause)Added [CMPedometerEventType.resume](https://developer.apple.com/documentation/coremotion/cmpedometereventtype/resume)Added [CMPedometerEventHandler](https://developer.apple.com/documentation/coremotion/cmpedometereventhandler)Modified [CMAltimeter](https://developer.apple.com/documentation/coremotion/cmaltimeter)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CMAltimeter : NSObject {     class func isRelativeAltitudeAvailable() -> Bool     func startRelativeAltitudeUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMAltitudeHandler)     func stopRelativeAltitudeUpdates() } ``` | -- |
| To | ``` class CMAltimeter : NSObject {     class func isRelativeAltitudeAvailable() -> Bool     func startRelativeAltitudeUpdates(to queue: OperationQueue, withHandler handler: CoreMotion.CMAltitudeHandler)     func stopRelativeAltitudeUpdates()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CMAltimeter : CVarArg { } extension CMAltimeter : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CMAltimeter.startRelativeAltitudeUpdates(to: OperationQueue, withHandler: CoreMotion.CMAltitudeHandler)](https://developer.apple.com/documentation/coremotion/cmaltimeter/1616004-startrelativealtitudeupdates)

|  | Declaration |
| --- | --- |
| From | ``` func startRelativeAltitudeUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMAltitudeHandler) ``` |
| To | ``` func startRelativeAltitudeUpdates(to queue: OperationQueue, withHandler handler: CoreMotion.CMAltitudeHandler) ``` |

Modified [CMAttitude](https://developer.apple.com/documentation/coremotion/cmattitude)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CMAttitude : NSObject, NSCopying, NSSecureCoding {     var roll: Double { get }     var pitch: Double { get }     var yaw: Double { get }     var rotationMatrix: CMRotationMatrix { get }     var quaternion: CMQuaternion { get }     func multiplyByInverseOfAttitude(_ attitude: CMAttitude) } ``` | NSCopying, NSSecureCoding |
| To | ``` class CMAttitude : NSObject, NSCopying, NSSecureCoding {     var roll: Double { get }     var pitch: Double { get }     var yaw: Double { get }     var rotationMatrix: CMRotationMatrix { get }     var quaternion: CMQuaternion { get }     func multiply(byInverseOf attitude: CMAttitude)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CMAttitude : CVarArg { } extension CMAttitude : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CMAttitude.multiply(byInverseOf: CMAttitude)](https://developer.apple.com/documentation/coremotion/cmattitude/1615909-multiply)

|  | Declaration |
| --- | --- |
| From | ``` func multiplyByInverseOfAttitude(_ attitude: CMAttitude) ``` |
| To | ``` func multiply(byInverseOf attitude: CMAttitude) ``` |

Modified [CMAttitudeReferenceFrame [struct]](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CMAttitudeReferenceFrame : OptionSetType {     init(rawValue rawValue: UInt)     static var XArbitraryZVertical: CMAttitudeReferenceFrame { get }     static var XArbitraryCorrectedZVertical: CMAttitudeReferenceFrame { get }     static var XMagneticNorthZVertical: CMAttitudeReferenceFrame { get }     static var XTrueNorthZVertical: CMAttitudeReferenceFrame { get } } ``` | OptionSetType |
| To | ``` struct CMAttitudeReferenceFrame : OptionSet {     init(rawValue rawValue: UInt)     static var xArbitraryZVertical: CMAttitudeReferenceFrame { get }     static var xArbitraryCorrectedZVertical: CMAttitudeReferenceFrame { get }     static var xMagneticNorthZVertical: CMAttitudeReferenceFrame { get }     static var xTrueNorthZVertical: CMAttitudeReferenceFrame { get }     func intersect(_ other: CMAttitudeReferenceFrame) -> CMAttitudeReferenceFrame     func exclusiveOr(_ other: CMAttitudeReferenceFrame) -> CMAttitudeReferenceFrame     mutating func unionInPlace(_ other: CMAttitudeReferenceFrame)     mutating func intersectInPlace(_ other: CMAttitudeReferenceFrame)     mutating func exclusiveOrInPlace(_ other: CMAttitudeReferenceFrame)     func isSubsetOf(_ other: CMAttitudeReferenceFrame) -> Bool     func isDisjointWith(_ other: CMAttitudeReferenceFrame) -> Bool     func isSupersetOf(_ other: CMAttitudeReferenceFrame) -> Bool     mutating func subtractInPlace(_ other: CMAttitudeReferenceFrame)     func isStrictSupersetOf(_ other: CMAttitudeReferenceFrame) -> Bool     func isStrictSubsetOf(_ other: CMAttitudeReferenceFrame) -> Bool } extension CMAttitudeReferenceFrame {     func union(_ other: CMAttitudeReferenceFrame) -> CMAttitudeReferenceFrame     func intersection(_ other: CMAttitudeReferenceFrame) -> CMAttitudeReferenceFrame     func symmetricDifference(_ other: CMAttitudeReferenceFrame) -> CMAttitudeReferenceFrame } extension CMAttitudeReferenceFrame {     func contains(_ member: CMAttitudeReferenceFrame) -> Bool     mutating func insert(_ newMember: CMAttitudeReferenceFrame) -> (inserted: Bool, memberAfterInsert: CMAttitudeReferenceFrame)     mutating func remove(_ member: CMAttitudeReferenceFrame) -> CMAttitudeReferenceFrame?     mutating func update(with newMember: CMAttitudeReferenceFrame) -> CMAttitudeReferenceFrame? } extension CMAttitudeReferenceFrame {     convenience init()     mutating func formUnion(_ other: CMAttitudeReferenceFrame)     mutating func formIntersection(_ other: CMAttitudeReferenceFrame)     mutating func formSymmetricDifference(_ other: CMAttitudeReferenceFrame) } extension CMAttitudeReferenceFrame {     convenience init<S : Sequence where S.Iterator.Element == CMAttitudeReferenceFrame>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CMAttitudeReferenceFrame...)     mutating func subtract(_ other: CMAttitudeReferenceFrame)     func isSubset(of other: CMAttitudeReferenceFrame) -> Bool     func isSuperset(of other: CMAttitudeReferenceFrame) -> Bool     func isDisjoint(with other: CMAttitudeReferenceFrame) -> Bool     func subtracting(_ other: CMAttitudeReferenceFrame) -> CMAttitudeReferenceFrame     var isEmpty: Bool { get }     func isStrictSuperset(of other: CMAttitudeReferenceFrame) -> Bool     func isStrictSubset(of other: CMAttitudeReferenceFrame) -> Bool } ``` | OptionSet |

Modified [CMAttitudeReferenceFrame.xArbitraryCorrectedZVertical](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/cmattitudereferenceframexarbitrarycorrectedzvertical)

|  | Declaration |
| --- | --- |
| From | ``` static var XArbitraryCorrectedZVertical: CMAttitudeReferenceFrame { get } ``` |
| To | ``` static var xArbitraryCorrectedZVertical: CMAttitudeReferenceFrame { get } ``` |

Modified [CMAttitudeReferenceFrame.xArbitraryZVertical](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/1615953-xarbitraryzvertical)

|  | Declaration |
| --- | --- |
| From | ``` static var XArbitraryZVertical: CMAttitudeReferenceFrame { get } ``` |
| To | ``` static var xArbitraryZVertical: CMAttitudeReferenceFrame { get } ``` |

Modified [CMAttitudeReferenceFrame.xMagneticNorthZVertical](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/cmattitudereferenceframexmagneticnorthzvertical)

|  | Declaration |
| --- | --- |
| From | ``` static var XMagneticNorthZVertical: CMAttitudeReferenceFrame { get } ``` |
| To | ``` static var xMagneticNorthZVertical: CMAttitudeReferenceFrame { get } ``` |

Modified [CMAttitudeReferenceFrame.xTrueNorthZVertical](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/1616019-xtruenorthzvertical)

|  | Declaration |
| --- | --- |
| From | ``` static var XTrueNorthZVertical: CMAttitudeReferenceFrame { get } ``` |
| To | ``` static var xTrueNorthZVertical: CMAttitudeReferenceFrame { get } ``` |

Modified [CMLogItem](https://developer.apple.com/documentation/coremotion/cmlogitem)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CMLogItem : NSObject, NSSecureCoding, NSCopying {     var timestamp: NSTimeInterval { get } } ``` | NSCopying, NSSecureCoding |
| To | ``` class CMLogItem : NSObject, NSSecureCoding, NSCopying {     var timestamp: TimeInterval { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CMLogItem : CVarArg { } extension CMLogItem : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CMLogItem.timestamp](https://developer.apple.com/documentation/coremotion/cmlogitem/1615939-timestamp)

|  | Declaration |
| --- | --- |
| From | ``` var timestamp: NSTimeInterval { get } ``` |
| To | ``` var timestamp: TimeInterval { get } ``` |

Modified [CMMotionActivity](https://developer.apple.com/documentation/coremotion/cmmotionactivity)

|  | Declaration |
| --- | --- |
| From | ``` class CMMotionActivity : CMLogItem {     var confidence: CMMotionActivityConfidence { get }     var startDate: NSDate { get }     var unknown: Bool { get }     var stationary: Bool { get }     var walking: Bool { get }     var running: Bool { get }     var automotive: Bool { get }     var cycling: Bool { get } } ``` |
| To | ``` class CMMotionActivity : CMLogItem {     var confidence: CMMotionActivityConfidence { get }     var startDate: Date { get }     var unknown: Bool { get }     var stationary: Bool { get }     var walking: Bool { get }     var running: Bool { get }     var automotive: Bool { get }     var cycling: Bool { get } } ``` |

Modified [CMMotionActivity.startDate](https://developer.apple.com/documentation/coremotion/cmmotionactivity/1615453-startdate)

|  | Declaration |
| --- | --- |
| From | ``` var startDate: NSDate { get } ``` |
| To | ``` var startDate: Date { get } ``` |

Modified [CMMotionActivityConfidence [enum]](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence)

|  | Declaration |
| --- | --- |
| From | ``` enum CMMotionActivityConfidence : Int {     case Low     case Medium     case High } ``` |
| To | ``` enum CMMotionActivityConfidence : Int {     case low     case medium     case high } ``` |

Modified [CMMotionActivityConfidence.high](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence/cmmotionactivityconfidencehigh)

|  | Declaration |
| --- | --- |
| From | ``` case High ``` |
| To | ``` case high ``` |

Modified [CMMotionActivityConfidence.low](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence/cmmotionactivityconfidencelow)

|  | Declaration |
| --- | --- |
| From | ``` case Low ``` |
| To | ``` case low ``` |

Modified [CMMotionActivityConfidence.medium](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence/cmmotionactivityconfidencemedium)

|  | Declaration |
| --- | --- |
| From | ``` case Medium ``` |
| To | ``` case medium ``` |

Modified [CMMotionActivityManager](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CMMotionActivityManager : NSObject {     class func isActivityAvailable() -> Bool     func queryActivityStartingFromDate(_ start: NSDate, toDate end: NSDate, toQueue queue: NSOperationQueue, withHandler handler: CMMotionActivityQueryHandler)     func startActivityUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMMotionActivityHandler)     func stopActivityUpdates() } ``` | -- |
| To | ``` class CMMotionActivityManager : NSObject {     class func isActivityAvailable() -> Bool     func queryActivityStarting(from start: Date, to end: Date, to queue: OperationQueue, withHandler handler: CoreMotion.CMMotionActivityQueryHandler)     func startActivityUpdates(to queue: OperationQueue, withHandler handler: CoreMotion.CMMotionActivityHandler)     func stopActivityUpdates()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CMMotionActivityManager : CVarArg { } extension CMMotionActivityManager : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CMMotionActivityManager.queryActivityStarting(from: Date, to: Date, to: OperationQueue, withHandler: CoreMotion.CMMotionActivityQueryHandler)](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/1615929-queryactivitystartingfromdate)

|  | Declaration |
| --- | --- |
| From | ``` func queryActivityStartingFromDate(_ start: NSDate, toDate end: NSDate, toQueue queue: NSOperationQueue, withHandler handler: CMMotionActivityQueryHandler) ``` |
| To | ``` func queryActivityStarting(from start: Date, to end: Date, to queue: OperationQueue, withHandler handler: CoreMotion.CMMotionActivityQueryHandler) ``` |

Modified [CMMotionActivityManager.startActivityUpdates(to: OperationQueue, withHandler: CoreMotion.CMMotionActivityHandler)](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/1615945-startactivityupdates)

|  | Declaration |
| --- | --- |
| From | ``` func startActivityUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMMotionActivityHandler) ``` |
| To | ``` func startActivityUpdates(to queue: OperationQueue, withHandler handler: CoreMotion.CMMotionActivityHandler) ``` |

Modified [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CMMotionManager : NSObject {     var accelerometerUpdateInterval: NSTimeInterval     var accelerometerAvailable: Bool { get }     var accelerometerActive: Bool { get }     var accelerometerData: CMAccelerometerData? { get }     func startAccelerometerUpdates()     func startAccelerometerUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMAccelerometerHandler)     func stopAccelerometerUpdates()     var gyroUpdateInterval: NSTimeInterval     var gyroAvailable: Bool { get }     var gyroActive: Bool { get }     var gyroData: CMGyroData? { get }     func startGyroUpdates()     func startGyroUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMGyroHandler)     func stopGyroUpdates()     var magnetometerUpdateInterval: NSTimeInterval     var magnetometerAvailable: Bool { get }     var magnetometerActive: Bool { get }     var magnetometerData: CMMagnetometerData? { get }     func startMagnetometerUpdates()     func startMagnetometerUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMMagnetometerHandler)     func stopMagnetometerUpdates()     var deviceMotionUpdateInterval: NSTimeInterval     class func availableAttitudeReferenceFrames() -> CMAttitudeReferenceFrame     var attitudeReferenceFrame: CMAttitudeReferenceFrame { get }     var deviceMotionAvailable: Bool { get }     var deviceMotionActive: Bool { get }     var deviceMotion: CMDeviceMotion? { get }     func startDeviceMotionUpdates()     func startDeviceMotionUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMDeviceMotionHandler)     func startDeviceMotionUpdatesUsingReferenceFrame(_ referenceFrame: CMAttitudeReferenceFrame)     func startDeviceMotionUpdatesUsingReferenceFrame(_ referenceFrame: CMAttitudeReferenceFrame, toQueue queue: NSOperationQueue, withHandler handler: CMDeviceMotionHandler)     func stopDeviceMotionUpdates()     var showsDeviceMovementDisplay: Bool } ``` | -- |
| To | ``` class CMMotionManager : NSObject {     var accelerometerUpdateInterval: TimeInterval     var isAccelerometerAvailable: Bool { get }     var isAccelerometerActive: Bool { get }     var accelerometerData: CMAccelerometerData? { get }     func startAccelerometerUpdates()     func startAccelerometerUpdates(to queue: OperationQueue, withHandler handler: CoreMotion.CMAccelerometerHandler)     func stopAccelerometerUpdates()     var gyroUpdateInterval: TimeInterval     var isGyroAvailable: Bool { get }     var isGyroActive: Bool { get }     var gyroData: CMGyroData? { get }     func startGyroUpdates()     func startGyroUpdates(to queue: OperationQueue, withHandler handler: CoreMotion.CMGyroHandler)     func stopGyroUpdates()     var magnetometerUpdateInterval: TimeInterval     var isMagnetometerAvailable: Bool { get }     var isMagnetometerActive: Bool { get }     var magnetometerData: CMMagnetometerData? { get }     func startMagnetometerUpdates()     func startMagnetometerUpdates(to queue: OperationQueue, withHandler handler: CoreMotion.CMMagnetometerHandler)     func stopMagnetometerUpdates()     var deviceMotionUpdateInterval: TimeInterval     class func availableAttitudeReferenceFrames() -> CMAttitudeReferenceFrame     var attitudeReferenceFrame: CMAttitudeReferenceFrame { get }     var isDeviceMotionAvailable: Bool { get }     var isDeviceMotionActive: Bool { get }     var deviceMotion: CMDeviceMotion? { get }     func startDeviceMotionUpdates()     func startDeviceMotionUpdates(to queue: OperationQueue, withHandler handler: CoreMotion.CMDeviceMotionHandler)     func startDeviceMotionUpdates(using referenceFrame: CMAttitudeReferenceFrame)     func startDeviceMotionUpdates(using referenceFrame: CMAttitudeReferenceFrame, to queue: OperationQueue, withHandler handler: CoreMotion.CMDeviceMotionHandler)     func stopDeviceMotionUpdates()     var showsDeviceMovementDisplay: Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CMMotionManager : CVarArg { } extension CMMotionManager : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CMMotionManager.accelerometerUpdateInterval](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616135-accelerometerupdateinterval)

|  | Declaration |
| --- | --- |
| From | ``` var accelerometerUpdateInterval: NSTimeInterval ``` |
| To | ``` var accelerometerUpdateInterval: TimeInterval ``` |

Modified [CMMotionManager.deviceMotionUpdateInterval](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616065-devicemotionupdateinterval)

|  | Declaration |
| --- | --- |
| From | ``` var deviceMotionUpdateInterval: NSTimeInterval ``` |
| To | ``` var deviceMotionUpdateInterval: TimeInterval ``` |

Modified [CMMotionManager.gyroUpdateInterval](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616160-gyroupdateinterval)

|  | Declaration |
| --- | --- |
| From | ``` var gyroUpdateInterval: NSTimeInterval ``` |
| To | ``` var gyroUpdateInterval: TimeInterval ``` |

Modified [CMMotionManager.isAccelerometerActive](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1615990-isaccelerometeractive)

|  | Declaration |
| --- | --- |
| From | ``` var accelerometerActive: Bool { get } ``` |
| To | ``` var isAccelerometerActive: Bool { get } ``` |

Modified [CMMotionManager.isAccelerometerAvailable](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616057-isaccelerometeravailable)

|  | Declaration |
| --- | --- |
| From | ``` var accelerometerAvailable: Bool { get } ``` |
| To | ``` var isAccelerometerAvailable: Bool { get } ``` |

Modified [CMMotionManager.isDeviceMotionActive](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616158-devicemotionactive)

|  | Declaration |
| --- | --- |
| From | ``` var deviceMotionActive: Bool { get } ``` |
| To | ``` var isDeviceMotionActive: Bool { get } ``` |

Modified [CMMotionManager.isDeviceMotionAvailable](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616094-devicemotionavailable)

|  | Declaration |
| --- | --- |
| From | ``` var deviceMotionAvailable: Bool { get } ``` |
| To | ``` var isDeviceMotionAvailable: Bool { get } ``` |

Modified [CMMotionManager.isGyroActive](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616153-isgyroactive)

|  | Declaration |
| --- | --- |
| From | ``` var gyroActive: Bool { get } ``` |
| To | ``` var isGyroActive: Bool { get } ``` |

Modified [CMMotionManager.isGyroAvailable](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1615951-isgyroavailable)

|  | Declaration |
| --- | --- |
| From | ``` var gyroAvailable: Bool { get } ``` |
| To | ``` var isGyroAvailable: Bool { get } ``` |

Modified [CMMotionManager.isMagnetometerActive](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1615977-magnetometeractive)

|  | Declaration |
| --- | --- |
| From | ``` var magnetometerActive: Bool { get } ``` |
| To | ``` var isMagnetometerActive: Bool { get } ``` |

Modified [CMMotionManager.isMagnetometerAvailable](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616143-magnetometeravailable)

|  | Declaration |
| --- | --- |
| From | ``` var magnetometerAvailable: Bool { get } ``` |
| To | ``` var isMagnetometerAvailable: Bool { get } ``` |

Modified [CMMotionManager.magnetometerUpdateInterval](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616089-magnetometerupdateinterval)

|  | Declaration |
| --- | --- |
| From | ``` var magnetometerUpdateInterval: NSTimeInterval ``` |
| To | ``` var magnetometerUpdateInterval: TimeInterval ``` |

Modified [CMMotionManager.startAccelerometerUpdates(to: OperationQueue, withHandler: CoreMotion.CMAccelerometerHandler)](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616148-startaccelerometerupdates)

|  | Declaration |
| --- | --- |
| From | ``` func startAccelerometerUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMAccelerometerHandler) ``` |
| To | ``` func startAccelerometerUpdates(to queue: OperationQueue, withHandler handler: CoreMotion.CMAccelerometerHandler) ``` |

Modified [CMMotionManager.startDeviceMotionUpdates(to: OperationQueue, withHandler: CoreMotion.CMDeviceMotionHandler)](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616048-startdevicemotionupdates)

|  | Declaration |
| --- | --- |
| From | ``` func startDeviceMotionUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMDeviceMotionHandler) ``` |
| To | ``` func startDeviceMotionUpdates(to queue: OperationQueue, withHandler handler: CoreMotion.CMDeviceMotionHandler) ``` |

Modified [CMMotionManager.startDeviceMotionUpdates(using: CMAttitudeReferenceFrame)](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616107-startdevicemotionupdates)

|  | Declaration |
| --- | --- |
| From | ``` func startDeviceMotionUpdatesUsingReferenceFrame(_ referenceFrame: CMAttitudeReferenceFrame) ``` |
| To | ``` func startDeviceMotionUpdates(using referenceFrame: CMAttitudeReferenceFrame) ``` |

Modified [CMMotionManager.startDeviceMotionUpdates(using: CMAttitudeReferenceFrame, to: OperationQueue, withHandler: CoreMotion.CMDeviceMotionHandler)](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616176-startdevicemotionupdates)

|  | Declaration |
| --- | --- |
| From | ``` func startDeviceMotionUpdatesUsingReferenceFrame(_ referenceFrame: CMAttitudeReferenceFrame, toQueue queue: NSOperationQueue, withHandler handler: CMDeviceMotionHandler) ``` |
| To | ``` func startDeviceMotionUpdates(using referenceFrame: CMAttitudeReferenceFrame, to queue: OperationQueue, withHandler handler: CoreMotion.CMDeviceMotionHandler) ``` |

Modified [CMMotionManager.startGyroUpdates(to: OperationQueue, withHandler: CoreMotion.CMGyroHandler)](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616104-startgyroupdates)

|  | Declaration |
| --- | --- |
| From | ``` func startGyroUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMGyroHandler) ``` |
| To | ``` func startGyroUpdates(to queue: OperationQueue, withHandler handler: CoreMotion.CMGyroHandler) ``` |

Modified [CMMotionManager.startMagnetometerUpdates(to: OperationQueue, withHandler: CoreMotion.CMMagnetometerHandler)](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1615968-startmagnetometerupdates)

|  | Declaration |
| --- | --- |
| From | ``` func startMagnetometerUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMMagnetometerHandler) ``` |
| To | ``` func startMagnetometerUpdates(to queue: OperationQueue, withHandler handler: CoreMotion.CMMagnetometerHandler) ``` |

Modified [CMPedometer](https://developer.apple.com/documentation/coremotion/cmpedometer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CMPedometer : NSObject {     class func isStepCountingAvailable() -> Bool     class func isDistanceAvailable() -> Bool     class func isFloorCountingAvailable() -> Bool     class func isPaceAvailable() -> Bool     class func isCadenceAvailable() -> Bool     func queryPedometerDataFromDate(_ start: NSDate, toDate end: NSDate, withHandler handler: CMPedometerHandler)     func startPedometerUpdatesFromDate(_ start: NSDate, withHandler handler: CMPedometerHandler)     func stopPedometerUpdates() } ``` | -- |
| To | ``` class CMPedometer : NSObject {     class func isStepCountingAvailable() -> Bool     class func isDistanceAvailable() -> Bool     class func isFloorCountingAvailable() -> Bool     class func isPaceAvailable() -> Bool     class func isCadenceAvailable() -> Bool     class func isPedometerEventTrackingAvailable() -> Bool     func queryPedometerData(from start: Date, to end: Date, withHandler handler: CoreMotion.CMPedometerHandler)     func startUpdates(from start: Date, withHandler handler: CoreMotion.CMPedometerHandler)     func stopUpdates()     func startEventUpdates(handler handler: CoreMotion.CMPedometerEventHandler)     func stopEventUpdates()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CMPedometer : CVarArg { } extension CMPedometer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CMPedometer.queryPedometerData(from: Date, to: Date, withHandler: CoreMotion.CMPedometerHandler)](https://developer.apple.com/documentation/coremotion/cmpedometer/1613946-querypedometerdata)

|  | Declaration |
| --- | --- |
| From | ``` func queryPedometerDataFromDate(_ start: NSDate, toDate end: NSDate, withHandler handler: CMPedometerHandler) ``` |
| To | ``` func queryPedometerData(from start: Date, to end: Date, withHandler handler: CoreMotion.CMPedometerHandler) ``` |

Modified [CMPedometer.startUpdates(from: Date, withHandler: CoreMotion.CMPedometerHandler)](https://developer.apple.com/documentation/coremotion/cmpedometer/1613950-startpedometerupdatesfromdate)

|  | Declaration |
| --- | --- |
| From | ``` func startPedometerUpdatesFromDate(_ start: NSDate, withHandler handler: CMPedometerHandler) ``` |
| To | ``` func startUpdates(from start: Date, withHandler handler: CoreMotion.CMPedometerHandler) ``` |

Modified [CMPedometer.stopUpdates()](https://developer.apple.com/documentation/coremotion/cmpedometer/1613973-stoppedometerupdates)

|  | Declaration |
| --- | --- |
| From | ``` func stopPedometerUpdates() ``` |
| To | ``` func stopUpdates() ``` |

Modified [CMPedometerData](https://developer.apple.com/documentation/coremotion/cmpedometerdata)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CMPedometerData : NSObject, NSSecureCoding, NSCopying {     var startDate: NSDate { get }     var endDate: NSDate { get }     var numberOfSteps: NSNumber { get }     var distance: NSNumber? { get }     var floorsAscended: NSNumber? { get }     var floorsDescended: NSNumber? { get }     var currentPace: NSNumber? { get }     var currentCadence: NSNumber? { get } } ``` | NSCopying, NSSecureCoding |
| To | ``` class CMPedometerData : NSObject, NSSecureCoding, NSCopying {     var startDate: Date { get }     var endDate: Date { get }     var numberOfSteps: NSNumber { get }     var distance: NSNumber? { get }     var floorsAscended: NSNumber? { get }     var floorsDescended: NSNumber? { get }     var currentPace: NSNumber? { get }     var currentCadence: NSNumber? { get }     var averageActivePace: NSNumber? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CMPedometerData : CVarArg { } extension CMPedometerData : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CMPedometerData.endDate](https://developer.apple.com/documentation/coremotion/cmpedometerdata/1613952-enddate)

|  | Declaration |
| --- | --- |
| From | ``` var endDate: NSDate { get } ``` |
| To | ``` var endDate: Date { get } ``` |

Modified [CMPedometerData.startDate](https://developer.apple.com/documentation/coremotion/cmpedometerdata/1613942-startdate)

|  | Declaration |
| --- | --- |
| From | ``` var startDate: NSDate { get } ``` |
| To | ``` var startDate: Date { get } ``` |

Modified [CMRecordedAccelerometerData](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata)

|  | Declaration |
| --- | --- |
| From | ``` class CMRecordedAccelerometerData : CMAccelerometerData {     var identifier: UInt64 { get }     var startDate: NSDate { get } } ``` |
| To | ``` class CMRecordedAccelerometerData : CMAccelerometerData {     var identifier: UInt64 { get }     var startDate: Date { get } } ``` |

Modified [CMRecordedAccelerometerData.startDate](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata/1616130-startdate)

|  | Declaration |
| --- | --- |
| From | ``` var startDate: NSDate { get } ``` |
| To | ``` var startDate: Date { get } ``` |

Modified [CMSensorDataList](https://developer.apple.com/documentation/coremotion/cmsensordatalist)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CMSensorDataList : NSObject, NSFastEnumeration { } ``` | NSFastEnumeration |
| To | ``` class CMSensorDataList : NSObject, NSFastEnumeration {     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CMSensorDataList : CVarArg { } extension CMSensorDataList : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSFastEnumeration |

Modified [CMSensorRecorder](https://developer.apple.com/documentation/coremotion/cmsensorrecorder)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CMSensorRecorder : NSObject {     class func isAccelerometerRecordingAvailable() -> Bool     class func isAuthorizedForRecording() -> Bool     func accelerometerDataFromDate(_ fromDate: NSDate, toDate toDate: NSDate) -> CMSensorDataList?     func recordAccelerometerForDuration(_ duration: NSTimeInterval) } ``` | -- |
| To | ``` class CMSensorRecorder : NSObject {     class func isAccelerometerRecordingAvailable() -> Bool     class func isAuthorizedForRecording() -> Bool     func accelerometerData(from fromDate: Date, to toDate: Date) -> CMSensorDataList?     func recordAccelerometer(forDuration duration: TimeInterval)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CMSensorRecorder : CVarArg { } extension CMSensorRecorder : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CMSensorRecorder.accelerometerData(from: Date, to: Date) -> CMSensorDataList?](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/1615937-accelerometerdata)

|  | Declaration |
| --- | --- |
| From | ``` func accelerometerDataFromDate(_ fromDate: NSDate, toDate toDate: NSDate) -> CMSensorDataList? ``` |
| To | ``` func accelerometerData(from fromDate: Date, to toDate: Date) -> CMSensorDataList? ``` |

Modified [CMSensorRecorder.recordAccelerometer(forDuration: TimeInterval)](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/1615987-recordaccelerometer)

|  | Declaration |
| --- | --- |
| From | ``` func recordAccelerometerForDuration(_ duration: NSTimeInterval) ``` |
| To | ``` func recordAccelerometer(forDuration duration: TimeInterval) ``` |

Modified [CMStepCounter](https://developer.apple.com/documentation/coremotion/cmstepcounter)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CMStepCounter : NSObject {     class func isStepCountingAvailable() -> Bool     func queryStepCountStartingFrom(_ start: NSDate, to end: NSDate, toQueue queue: NSOperationQueue, withHandler handler: CMStepQueryHandler)     func startStepCountingUpdatesToQueue(_ queue: NSOperationQueue, updateOn stepCounts: Int, withHandler handler: CMStepUpdateHandler)     func stopStepCountingUpdates() } ``` | -- |
| To | ``` class CMStepCounter : NSObject {     class func isStepCountingAvailable() -> Bool     func queryStepCountStarting(from start: Date, to end: Date, to queue: OperationQueue, withHandler handler: CoreMotion.CMStepQueryHandler)     func startStepCountingUpdates(to queue: OperationQueue, updateOn stepCounts: Int, withHandler handler: CoreMotion.CMStepUpdateHandler)     func stopStepCountingUpdates()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CMStepCounter : CVarArg { } extension CMStepCounter : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CMStepCounter.queryStepCountStarting(from: Date, to: Date, to: OperationQueue, withHandler: CoreMotion.CMStepQueryHandler)](https://developer.apple.com/documentation/coremotion/cmstepcounter/1616166-querystepcountstartingfrom)

|  | Declaration |
| --- | --- |
| From | ``` func queryStepCountStartingFrom(_ start: NSDate, to end: NSDate, toQueue queue: NSOperationQueue, withHandler handler: CMStepQueryHandler) ``` |
| To | ``` func queryStepCountStarting(from start: Date, to end: Date, to queue: OperationQueue, withHandler handler: CoreMotion.CMStepQueryHandler) ``` |

Modified [CMStepCounter.startStepCountingUpdates(to: OperationQueue, updateOn: Int, withHandler: CoreMotion.CMStepUpdateHandler)](https://developer.apple.com/documentation/coremotion/cmstepcounter/1616151-startstepcountingupdatestoqueue)

|  | Declaration |
| --- | --- |
| From | ``` func startStepCountingUpdatesToQueue(_ queue: NSOperationQueue, updateOn stepCounts: Int, withHandler handler: CMStepUpdateHandler) ``` |
| To | ``` func startStepCountingUpdates(to queue: OperationQueue, updateOn stepCounts: Int, withHandler handler: CoreMotion.CMStepUpdateHandler) ``` |

Modified [CMAccelerometerHandler](https://developer.apple.com/documentation/coremotion/cmaccelerometerhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMAccelerometerHandler = (CMAccelerometerData?, NSError?) -> Void ``` |
| To | ``` typealias CMAccelerometerHandler = (CMAccelerometerData?, Error?) -> Swift.Void ``` |

Modified [CMAltitudeHandler](https://developer.apple.com/documentation/coremotion/cmaltitudehandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMAltitudeHandler = (CMAltitudeData?, NSError?) -> Void ``` |
| To | ``` typealias CMAltitudeHandler = (CMAltitudeData?, Error?) -> Swift.Void ``` |

Modified [CMDeviceMotionHandler](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMDeviceMotionHandler = (CMDeviceMotion?, NSError?) -> Void ``` |
| To | ``` typealias CMDeviceMotionHandler = (CMDeviceMotion?, Error?) -> Swift.Void ``` |

Modified [CMGyroHandler](https://developer.apple.com/documentation/coremotion/cmgyrohandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMGyroHandler = (CMGyroData?, NSError?) -> Void ``` |
| To | ``` typealias CMGyroHandler = (CMGyroData?, Error?) -> Swift.Void ``` |

Modified [CMMagnetometerHandler](https://developer.apple.com/documentation/coremotion/cmmagnetometerhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMMagnetometerHandler = (CMMagnetometerData?, NSError?) -> Void ``` |
| To | ``` typealias CMMagnetometerHandler = (CMMagnetometerData?, Error?) -> Swift.Void ``` |

Modified [CMMotionActivityHandler](https://developer.apple.com/documentation/coremotion/cmmotionactivityhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMMotionActivityHandler = (CMMotionActivity?) -> Void ``` |
| To | ``` typealias CMMotionActivityHandler = (CMMotionActivity?) -> Swift.Void ``` |

Modified [CMMotionActivityQueryHandler](https://developer.apple.com/documentation/coremotion/cmmotionactivityqueryhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMMotionActivityQueryHandler = ([CMMotionActivity]?, NSError?) -> Void ``` |
| To | ``` typealias CMMotionActivityQueryHandler = ([CMMotionActivity]?, Error?) -> Swift.Void ``` |

Modified [CMPedometerHandler](https://developer.apple.com/documentation/coremotion/cmpedometerhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMPedometerHandler = (CMPedometerData?, NSError?) -> Void ``` |
| To | ``` typealias CMPedometerHandler = (CMPedometerData?, Error?) -> Swift.Void ``` |

Modified [CMStepQueryHandler](https://developer.apple.com/documentation/coremotion/cmstepqueryhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMStepQueryHandler = (Int, NSError?) -> Void ``` |
| To | ``` typealias CMStepQueryHandler = (Int, Error?) -> Swift.Void ``` |

Modified [CMStepUpdateHandler](https://developer.apple.com/documentation/coremotion/cmstepupdatehandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMStepUpdateHandler = (Int, NSDate, NSError?) -> Void ``` |
| To | ``` typealias CMStepUpdateHandler = (Int, Date, Error?) -> Swift.Void ``` |

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
