---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Swift/QuartzCore.html
archived_at: '2026-07-18T02:57:54.331038Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# QuartzCore Changes for Swift

### QuartzCore

Removed [CADisplayLink.frameInterval](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1621231-frameinterval)Removed NSObject.actionForLayer(_: CALayer, forKey: String) -> CAAction?Removed NSObject.animationDidStart(_: CAAnimation)Removed NSObject.animationDidStop(_: CAAnimation, finished: Bool)Removed NSObject.displayLayer(_: CALayer)Removed NSObject.drawLayer(_: CALayer, inContext: CGContext)Removed NSObject.layoutSublayersOfLayer(_: CALayer)Added [CAAnimationDelegate](https://developer.apple.com/documentation/quartzcore/caanimationdelegate)Added [CAAnimationDelegate.animationDidStart(_: CAAnimation)](https://developer.apple.com/documentation/quartzcore/caanimationdelegate/2097265-animationdidstart)Added [CAAnimationDelegate.animationDidStop(_: CAAnimation, finished: Bool)](https://developer.apple.com/documentation/quartzcore/caanimationdelegate/2097259-animationdidstop)Added [CADisplayLink.preferredFramesPerSecond](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1648421-preferredframespersecond)Added [CADisplayLink.targetTimestamp](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1648422-targettimestamp)Added [CALayer.contentsFormat](https://developer.apple.com/documentation/quartzcore/calayer/1792104-contentsformat)Added [CALayerDelegate](https://developer.apple.com/documentation/quartzcore/calayerdelegate)Added [CALayerDelegate.action(for: CALayer, forKey: String) -> CAAction?](https://developer.apple.com/documentation/quartzcore/calayerdelegate/2097264-action)Added [CALayerDelegate.display(_: CALayer)](https://developer.apple.com/documentation/quartzcore/calayerdelegate/2097261-displaylayer)Added [CALayerDelegate.draw(_: CALayer, in: CGContext)](https://developer.apple.com/documentation/quartzcore/calayerdelegate/2097262-draw)Added [CALayerDelegate.layerWillDraw(_: CALayer)](https://developer.apple.com/documentation/quartzcore/calayerdelegate/2097263-layerwilldraw)Added [CALayerDelegate.layoutSublayers(of: CALayer)](https://developer.apple.com/documentation/quartzcore/calayerdelegate/2097257-layoutsublayersoflayer)Added [kCAContentsFormatGray8Uint](https://developer.apple.com/documentation/quartzcore/kcacontentsformatgray8uint)Added [kCAContentsFormatRGBA16Float](https://developer.apple.com/documentation/quartzcore/kcacontentsformatrgba16float)Added [kCAContentsFormatRGBA8Uint](https://developer.apple.com/documentation/quartzcore/kcacontentsformatrgba8uint)Added kCAEmitterBehaviorSimpleAttractorModified [CAAction](https://developer.apple.com/documentation/quartzcore/caaction)

|  | Declaration |
| --- | --- |
| From | ``` protocol CAAction {     func runActionForKey(_ event: String, object anObject: AnyObject, arguments dict: [NSObject : AnyObject]?) } ``` |
| To | ``` protocol CAAction {     func run(forKey event: String, object anObject: Any, arguments dict: [AnyHashable : Any]?) } ``` |

Modified [CAAction.run(forKey: String, object: Any, arguments: [AnyHashable : Any]?)](https://developer.apple.com/documentation/quartzcore/caaction/1410806-runactionforkey)

|  | Declaration |
| --- | --- |
| From | ``` func runActionForKey(_ event: String, object anObject: AnyObject, arguments dict: [NSObject : AnyObject]?) ``` |
| To | ``` func run(forKey event: String, object anObject: Any, arguments dict: [AnyHashable : Any]?) ``` |

Modified [CAAnimation](https://developer.apple.com/documentation/quartzcore/caanimation)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CAAnimation : NSObject, NSCoding, NSCopying, CAMediaTiming, CAAction {     convenience init()     class func animation() -> Self     class func defaultValueForKey(_ key: String) -> AnyObject?     func shouldArchiveValueForKey(_ key: String) -> Bool     var timingFunction: CAMediaTimingFunction?     var delegate: AnyObject?     var removedOnCompletion: Bool } extension CAAnimation {     var usesSceneTimeBase: Bool     var fadeInDuration: CGFloat     var fadeOutDuration: CGFloat     var animationEvents: [SCNAnimationEvent]? } ``` | CAAction, CAMediaTiming, NSCoding, NSCopying |
| To | ``` class CAAnimation : NSObject, NSCoding, NSCopying, CAMediaTiming, CAAction {     convenience init()     class func animation() -> Self     class func defaultValue(forKey key: String) -> Any?     func shouldArchiveValue(forKey key: String) -> Bool     var timingFunction: CAMediaTimingFunction?     var delegate: CAAnimationDelegate?     var isRemovedOnCompletion: Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CAAnimation : CVarArg { } extension CAAnimation : Equatable, Hashable {     var hashValue: Int { get } } extension CAAnimation {     var usesSceneTimeBase: Bool     var fadeInDuration: CGFloat     var fadeOutDuration: CGFloat     var animationEvents: [SCNAnimationEvent]? } ``` | CAAction, CAMediaTiming, CVarArg, Equatable, Hashable, NSCoding, NSCopying |

Modified [CAAnimation.defaultValue(forKey: String) -> Any? [class]](https://developer.apple.com/documentation/quartzcore/caanimation/1412530-defaultvalueforkey)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultValueForKey(_ key: String) -> AnyObject? ``` |
| To | ``` class func defaultValue(forKey key: String) -> Any? ``` |

Modified [CAAnimation.delegate](https://developer.apple.com/documentation/quartzcore/caanimation/1412490-delegate)

|  | Declaration |
| --- | --- |
| From | ``` var delegate: AnyObject? ``` |
| To | ``` var delegate: CAAnimationDelegate? ``` |

Modified [CAAnimation.isRemovedOnCompletion](https://developer.apple.com/documentation/quartzcore/caanimation/1412458-removedoncompletion)

|  | Declaration |
| --- | --- |
| From | ``` var removedOnCompletion: Bool ``` |
| To | ``` var isRemovedOnCompletion: Bool ``` |

Modified [CAAnimation.shouldArchiveValue(forKey: String) -> Bool](https://developer.apple.com/documentation/quartzcore/caanimation/1412525-shouldarchivevalueforkey)

|  | Declaration |
| --- | --- |
| From | ``` func shouldArchiveValueForKey(_ key: String) -> Bool ``` |
| To | ``` func shouldArchiveValue(forKey key: String) -> Bool ``` |

Modified [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation)

|  | Declaration |
| --- | --- |
| From | ``` class CABasicAnimation : CAPropertyAnimation {     var fromValue: AnyObject?     var toValue: AnyObject?     var byValue: AnyObject? } ``` |
| To | ``` class CABasicAnimation : CAPropertyAnimation {     var fromValue: Any?     var toValue: Any?     var byValue: Any? } ``` |

Modified [CABasicAnimation.byValue](https://developer.apple.com/documentation/quartzcore/cabasicanimation/1412445-byvalue)

|  | Declaration |
| --- | --- |
| From | ``` var byValue: AnyObject? ``` |
| To | ``` var byValue: Any? ``` |

Modified [CABasicAnimation.fromValue](https://developer.apple.com/documentation/quartzcore/cabasicanimation/1412519-fromvalue)

|  | Declaration |
| --- | --- |
| From | ``` var fromValue: AnyObject? ``` |
| To | ``` var fromValue: Any? ``` |

Modified [CABasicAnimation.toValue](https://developer.apple.com/documentation/quartzcore/cabasicanimation/1412523-tovalue)

|  | Declaration |
| --- | --- |
| From | ``` var toValue: AnyObject? ``` |
| To | ``` var toValue: Any? ``` |

Modified [CADisplayLink](https://developer.apple.com/documentation/quartzcore/cadisplaylink)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CADisplayLink : NSObject {      init(target target: AnyObject, selector sel: Selector)     class func displayLinkWithTarget(_ target: AnyObject, selector sel: Selector) -> CADisplayLink     func addToRunLoop(_ runloop: NSRunLoop, forMode mode: String)     func removeFromRunLoop(_ runloop: NSRunLoop, forMode mode: String)     func invalidate()     var timestamp: CFTimeInterval { get }     var duration: CFTimeInterval { get }     var paused: Bool     var frameInterval: Int } ``` | -- |
| To | ``` class CADisplayLink : NSObject {      init(target target: Any, selector sel: Selector)     class func withTarget(_ target: Any, selector sel: Selector) -> CADisplayLink     func add(to runloop: RunLoop, forMode mode: RunLoopMode)     func remove(from runloop: RunLoop, forMode mode: RunLoopMode)     func invalidate()     var timestamp: CFTimeInterval { get }     var duration: CFTimeInterval { get }     var targetTimestamp: CFTimeInterval { get }     var isPaused: Bool     var frameInterval: Int     var preferredFramesPerSecond: Int     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CADisplayLink : CVarArg { } extension CADisplayLink : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CADisplayLink.add(to: RunLoop, forMode: RunLoopMode)](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1621323-add)

|  | Declaration |
| --- | --- |
| From | ``` func addToRunLoop(_ runloop: NSRunLoop, forMode mode: String) ``` |
| To | ``` func add(to runloop: RunLoop, forMode mode: RunLoopMode) ``` |

Modified [CADisplayLink.init(target: Any, selector: Selector)](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1621228-init)

|  | Declaration |
| --- | --- |
| From | ``` init(target target: AnyObject, selector sel: Selector) ``` |
| To | ``` init(target target: Any, selector sel: Selector) ``` |

Modified [CADisplayLink.isPaused](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1621229-ispaused)

|  | Declaration |
| --- | --- |
| From | ``` var paused: Bool ``` |
| To | ``` var isPaused: Bool ``` |

Modified [CADisplayLink.remove(from: RunLoop, forMode: RunLoopMode)](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1621325-removefromrunloop)

|  | Declaration |
| --- | --- |
| From | ``` func removeFromRunLoop(_ runloop: NSRunLoop, forMode mode: String) ``` |
| To | ``` func remove(from runloop: RunLoop, forMode mode: RunLoopMode) ``` |

Modified [CAEAGLLayer](https://developer.apple.com/documentation/quartzcore/caeagllayer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CAEAGLLayer : CALayer, EAGLDrawable {     var presentsWithTransaction: Bool } ``` | EAGLDrawable |
| To | ``` class CAEAGLLayer : CALayer, EAGLDrawable {     var presentsWithTransaction: Bool     func scroll(_ p: CGPoint)     func scrollRectToVisible(_ r: CGRect)     var visibleRect: CGRect { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CAEAGLLayer : CVarArg { } extension CAEAGLLayer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, EAGLDrawable, Equatable, Hashable |

Modified [CAEdgeAntialiasingMask [struct]](https://developer.apple.com/documentation/quartzcore/caedgeantialiasingmask)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CAEdgeAntialiasingMask : OptionSetType {     init(rawValue rawValue: UInt32)     static var LayerLeftEdge: CAEdgeAntialiasingMask { get }     static var LayerRightEdge: CAEdgeAntialiasingMask { get }     static var LayerBottomEdge: CAEdgeAntialiasingMask { get }     static var LayerTopEdge: CAEdgeAntialiasingMask { get } } ``` | OptionSetType |
| To | ``` struct CAEdgeAntialiasingMask : OptionSet {     init(rawValue rawValue: UInt32)     static var layerLeftEdge: CAEdgeAntialiasingMask { get }     static var layerRightEdge: CAEdgeAntialiasingMask { get }     static var layerBottomEdge: CAEdgeAntialiasingMask { get }     static var layerTopEdge: CAEdgeAntialiasingMask { get }     func intersect(_ other: CAEdgeAntialiasingMask) -> CAEdgeAntialiasingMask     func exclusiveOr(_ other: CAEdgeAntialiasingMask) -> CAEdgeAntialiasingMask     mutating func unionInPlace(_ other: CAEdgeAntialiasingMask)     mutating func intersectInPlace(_ other: CAEdgeAntialiasingMask)     mutating func exclusiveOrInPlace(_ other: CAEdgeAntialiasingMask)     func isSubsetOf(_ other: CAEdgeAntialiasingMask) -> Bool     func isDisjointWith(_ other: CAEdgeAntialiasingMask) -> Bool     func isSupersetOf(_ other: CAEdgeAntialiasingMask) -> Bool     mutating func subtractInPlace(_ other: CAEdgeAntialiasingMask)     func isStrictSupersetOf(_ other: CAEdgeAntialiasingMask) -> Bool     func isStrictSubsetOf(_ other: CAEdgeAntialiasingMask) -> Bool } extension CAEdgeAntialiasingMask {     func union(_ other: CAEdgeAntialiasingMask) -> CAEdgeAntialiasingMask     func intersection(_ other: CAEdgeAntialiasingMask) -> CAEdgeAntialiasingMask     func symmetricDifference(_ other: CAEdgeAntialiasingMask) -> CAEdgeAntialiasingMask } extension CAEdgeAntialiasingMask {     func contains(_ member: CAEdgeAntialiasingMask) -> Bool     mutating func insert(_ newMember: CAEdgeAntialiasingMask) -> (inserted: Bool, memberAfterInsert: CAEdgeAntialiasingMask)     mutating func remove(_ member: CAEdgeAntialiasingMask) -> CAEdgeAntialiasingMask?     mutating func update(with newMember: CAEdgeAntialiasingMask) -> CAEdgeAntialiasingMask? } extension CAEdgeAntialiasingMask {     convenience init()     mutating func formUnion(_ other: CAEdgeAntialiasingMask)     mutating func formIntersection(_ other: CAEdgeAntialiasingMask)     mutating func formSymmetricDifference(_ other: CAEdgeAntialiasingMask) } extension CAEdgeAntialiasingMask {     convenience init<S : Sequence where S.Iterator.Element == CAEdgeAntialiasingMask>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CAEdgeAntialiasingMask...)     mutating func subtract(_ other: CAEdgeAntialiasingMask)     func isSubset(of other: CAEdgeAntialiasingMask) -> Bool     func isSuperset(of other: CAEdgeAntialiasingMask) -> Bool     func isDisjoint(with other: CAEdgeAntialiasingMask) -> Bool     func subtracting(_ other: CAEdgeAntialiasingMask) -> CAEdgeAntialiasingMask     var isEmpty: Bool { get }     func isStrictSuperset(of other: CAEdgeAntialiasingMask) -> Bool     func isStrictSubset(of other: CAEdgeAntialiasingMask) -> Bool } ``` | OptionSet |

Modified [CAEdgeAntialiasingMask.layerBottomEdge](https://developer.apple.com/documentation/quartzcore/caedgeantialiasingmask/kcalayerbottomedge)

|  | Declaration |
| --- | --- |
| From | ``` static var LayerBottomEdge: CAEdgeAntialiasingMask { get } ``` |
| To | ``` static var layerBottomEdge: CAEdgeAntialiasingMask { get } ``` |

Modified [CAEdgeAntialiasingMask.layerLeftEdge](https://developer.apple.com/documentation/quartzcore/caedgeantialiasingmask/1410870-layerleftedge)

|  | Declaration |
| --- | --- |
| From | ``` static var LayerLeftEdge: CAEdgeAntialiasingMask { get } ``` |
| To | ``` static var layerLeftEdge: CAEdgeAntialiasingMask { get } ``` |

Modified [CAEdgeAntialiasingMask.layerRightEdge](https://developer.apple.com/documentation/quartzcore/caedgeantialiasingmask/kcalayerrightedge)

|  | Declaration |
| --- | --- |
| From | ``` static var LayerRightEdge: CAEdgeAntialiasingMask { get } ``` |
| To | ``` static var layerRightEdge: CAEdgeAntialiasingMask { get } ``` |

Modified [CAEdgeAntialiasingMask.layerTopEdge](https://developer.apple.com/documentation/quartzcore/caedgeantialiasingmask/1410787-layertopedge)

|  | Declaration |
| --- | --- |
| From | ``` static var LayerTopEdge: CAEdgeAntialiasingMask { get } ``` |
| To | ``` static var layerTopEdge: CAEdgeAntialiasingMask { get } ``` |

Modified CAEmitterBehavior

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CAEmitterBehavior : NSObject, NSCoding {     class func behaviorTypes() -> [String]      init(type type: String)     class func behaviorWithType(_ type: String) -> CAEmitterBehavior     init(type type: String)     var type: String { get }     var name: String?     var enabled: Bool } ``` | NSCoding |
| To | ``` class CAEmitterBehavior : NSObject, NSCoding {     class func behaviorTypes() -> [String]      init(type type: String)     class func withType(_ type: String) -> CAEmitterBehavior     init(type type: String)     var type: String { get }     var name: String?     var isEnabled: Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CAEmitterBehavior : CVarArg { } extension CAEmitterBehavior : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding |

Modified CAEmitterBehavior.isEnabled

|  | Declaration |
| --- | --- |
| From | ``` var enabled: Bool ``` |
| To | ``` var isEnabled: Bool ``` |

Modified [CAEmitterCell](https://developer.apple.com/documentation/quartzcore/caemittercell)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CAEmitterCell : NSObject, NSCoding, CAMediaTiming {     convenience init()     class func emitterCell() -> Self     class func defaultValueForKey(_ key: String) -> AnyObject?     func shouldArchiveValueForKey(_ key: String) -> Bool     var name: String?     var enabled: Bool     var birthRate: Float     var lifetime: Float     var lifetimeRange: Float     var emissionLatitude: CGFloat     var emissionLongitude: CGFloat     var emissionRange: CGFloat     var velocity: CGFloat     var velocityRange: CGFloat     var xAcceleration: CGFloat     var yAcceleration: CGFloat     var zAcceleration: CGFloat     var scale: CGFloat     var scaleRange: CGFloat     var scaleSpeed: CGFloat     var spin: CGFloat     var spinRange: CGFloat     var color: CGColor?     var redRange: Float     var greenRange: Float     var blueRange: Float     var alphaRange: Float     var redSpeed: Float     var greenSpeed: Float     var blueSpeed: Float     var alphaSpeed: Float     var contents: AnyObject?     var contentsRect: CGRect     var contentsScale: CGFloat     var minificationFilter: String     var magnificationFilter: String     var minificationFilterBias: Float     var emitterCells: [CAEmitterCell]?     var style: [NSObject : AnyObject]? } ``` | CAMediaTiming, NSCoding |
| To | ``` class CAEmitterCell : NSObject, NSCoding, CAMediaTiming {     convenience init()     class func emitterCell() -> Self     class func defaultValue(forKey key: String) -> Any?     func shouldArchiveValue(forKey key: String) -> Bool     var name: String?     var isEnabled: Bool     var birthRate: Float     var lifetime: Float     var lifetimeRange: Float     var emissionLatitude: CGFloat     var emissionLongitude: CGFloat     var emissionRange: CGFloat     var velocity: CGFloat     var velocityRange: CGFloat     var xAcceleration: CGFloat     var yAcceleration: CGFloat     var zAcceleration: CGFloat     var scale: CGFloat     var scaleRange: CGFloat     var scaleSpeed: CGFloat     var spin: CGFloat     var spinRange: CGFloat     var color: CGColor?     var redRange: Float     var greenRange: Float     var blueRange: Float     var alphaRange: Float     var redSpeed: Float     var greenSpeed: Float     var blueSpeed: Float     var alphaSpeed: Float     var contents: Any?     var contentsRect: CGRect     var contentsScale: CGFloat     var minificationFilter: String     var magnificationFilter: String     var minificationFilterBias: Float     var emitterCells: [CAEmitterCell]?     var style: [AnyHashable : Any]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CAEmitterCell : CVarArg { } extension CAEmitterCell : Equatable, Hashable {     var hashValue: Int { get } } ``` | CAMediaTiming, CVarArg, Equatable, Hashable, NSCoding |

Modified [CAEmitterCell.contents](https://developer.apple.com/documentation/quartzcore/caemittercell/1522109-contents)

|  | Declaration |
| --- | --- |
| From | ``` var contents: AnyObject? ``` |
| To | ``` var contents: Any? ``` |

Modified [CAEmitterCell.defaultValue(forKey: String) -> Any? [class]](https://developer.apple.com/documentation/quartzcore/caemittercell/1521964-defaultvalue)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultValueForKey(_ key: String) -> AnyObject? ``` |
| To | ``` class func defaultValue(forKey key: String) -> Any? ``` |

Modified [CAEmitterCell.isEnabled](https://developer.apple.com/documentation/quartzcore/caemittercell/1521831-isenabled)

|  | Declaration |
| --- | --- |
| From | ``` var enabled: Bool ``` |
| To | ``` var isEnabled: Bool ``` |

Modified [CAEmitterCell.shouldArchiveValue(forKey: String) -> Bool](https://developer.apple.com/documentation/quartzcore/caemittercell/1522005-shouldarchivevalue)

|  | Declaration |
| --- | --- |
| From | ``` func shouldArchiveValueForKey(_ key: String) -> Bool ``` |
| To | ``` func shouldArchiveValue(forKey key: String) -> Bool ``` |

Modified [CAEmitterCell.style](https://developer.apple.com/documentation/quartzcore/caemittercell/1521925-style)

|  | Declaration |
| --- | --- |
| From | ``` var style: [NSObject : AnyObject]? ``` |
| To | ``` var style: [AnyHashable : Any]? ``` |

Modified [CAEmitterLayer](https://developer.apple.com/documentation/quartzcore/caemitterlayer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CAEmitterLayer : CALayer {     var emitterCells: [CAEmitterCell]?     var birthRate: Float     var lifetime: Float     var emitterPosition: CGPoint     var emitterZPosition: CGFloat     var emitterSize: CGSize     var emitterDepth: CGFloat     var emitterShape: String     var emitterMode: String     var renderMode: String     var preservesDepth: Bool     var velocity: Float     var scale: Float     var spin: Float     var seed: UInt32 } ``` | -- |
| To | ``` class CAEmitterLayer : CALayer {     var emitterCells: [CAEmitterCell]?     var birthRate: Float     var lifetime: Float     var emitterPosition: CGPoint     var emitterZPosition: CGFloat     var emitterSize: CGSize     var emitterDepth: CGFloat     var emitterShape: String     var emitterMode: String     var renderMode: String     var preservesDepth: Bool     var velocity: Float     var scale: Float     var spin: Float     var seed: UInt32     func scroll(_ p: CGPoint)     func scrollRectToVisible(_ r: CGRect)     var visibleRect: CGRect { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CAEmitterLayer : CVarArg { } extension CAEmitterLayer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CAGradientLayer](https://developer.apple.com/documentation/quartzcore/cagradientlayer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CAGradientLayer : CALayer {     var colors: [AnyObject]?     var locations: [NSNumber]?     var startPoint: CGPoint     var endPoint: CGPoint     var type: String } ``` | -- |
| To | ``` class CAGradientLayer : CALayer {     var colors: [Any]?     var locations: [NSNumber]?     var startPoint: CGPoint     var endPoint: CGPoint     var type: String     func scroll(_ p: CGPoint)     func scrollRectToVisible(_ r: CGRect)     var visibleRect: CGRect { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CAGradientLayer : CVarArg { } extension CAGradientLayer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CAGradientLayer.colors](https://developer.apple.com/documentation/quartzcore/cagradientlayer/1462403-colors)

|  | Declaration |
| --- | --- |
| From | ``` var colors: [AnyObject]? ``` |
| To | ``` var colors: [Any]? ``` |

Modified [CAKeyframeAnimation](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation)

|  | Declaration |
| --- | --- |
| From | ``` class CAKeyframeAnimation : CAPropertyAnimation {     var values: [AnyObject]?     var path: CGPath?     var keyTimes: [NSNumber]?     var timingFunctions: [CAMediaTimingFunction]?     var calculationMode: String     var tensionValues: [NSNumber]?     var continuityValues: [NSNumber]?     var biasValues: [NSNumber]?     var rotationMode: String? } ``` |
| To | ``` class CAKeyframeAnimation : CAPropertyAnimation {     var values: [Any]?     var path: CGPath?     var keyTimes: [NSNumber]?     var timingFunctions: [CAMediaTimingFunction]?     var calculationMode: String     var tensionValues: [NSNumber]?     var continuityValues: [NSNumber]?     var biasValues: [NSNumber]?     var rotationMode: String? } ``` |

Modified [CAKeyframeAnimation.values](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412498-values)

|  | Declaration |
| --- | --- |
| From | ``` var values: [AnyObject]? ``` |
| To | ``` var values: [Any]? ``` |

Modified [CALayer](https://developer.apple.com/documentation/quartzcore/calayer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CALayer : NSObject, NSCoding, CAMediaTiming {     convenience init()     class func layer() -> Self     init()     init(layer layer: AnyObject)     func presentationLayer() -> AnyObject?     func modelLayer() -> AnyObject     class func defaultValueForKey(_ key: String) -> AnyObject?     class func needsDisplayForKey(_ key: String) -> Bool     func shouldArchiveValueForKey(_ key: String) -> Bool     var bounds: CGRect     var position: CGPoint     var zPosition: CGFloat     var anchorPoint: CGPoint     var anchorPointZ: CGFloat     var transform: CATransform3D     func affineTransform() -> CGAffineTransform     func setAffineTransform(_ m: CGAffineTransform)     var frame: CGRect     var hidden: Bool     var doubleSided: Bool     var geometryFlipped: Bool     func contentsAreFlipped() -> Bool     var superlayer: CALayer? { get }     func removeFromSuperlayer()     var sublayers: [CALayer]?     func addSublayer(_ layer: CALayer)     func insertSublayer(_ layer: CALayer, atIndex idx: UInt32)     func insertSublayer(_ layer: CALayer, below sibling: CALayer?)     func insertSublayer(_ layer: CALayer, above sibling: CALayer?)     func replaceSublayer(_ layer: CALayer, with layer2: CALayer)     var sublayerTransform: CATransform3D     var mask: CALayer?     var masksToBounds: Bool     func convertPoint(_ p: CGPoint, fromLayer l: CALayer?) -> CGPoint     func convertPoint(_ p: CGPoint, toLayer l: CALayer?) -> CGPoint     func convertRect(_ r: CGRect, fromLayer l: CALayer?) -> CGRect     func convertRect(_ r: CGRect, toLayer l: CALayer?) -> CGRect     func convertTime(_ t: CFTimeInterval, fromLayer l: CALayer?) -> CFTimeInterval     func convertTime(_ t: CFTimeInterval, toLayer l: CALayer?) -> CFTimeInterval     func hitTest(_ p: CGPoint) -> CALayer?     func containsPoint(_ p: CGPoint) -> Bool     var contents: AnyObject?     var contentsRect: CGRect     var contentsGravity: String     var contentsScale: CGFloat     var contentsCenter: CGRect     var minificationFilter: String     var magnificationFilter: String     var minificationFilterBias: Float     var opaque: Bool     func display()     func setNeedsDisplay()     func setNeedsDisplayInRect(_ r: CGRect)     func needsDisplay() -> Bool     func displayIfNeeded()     var needsDisplayOnBoundsChange: Bool     var drawsAsynchronously: Bool     func drawInContext(_ ctx: CGContext)     func renderInContext(_ ctx: CGContext)     var edgeAntialiasingMask: CAEdgeAntialiasingMask     var allowsEdgeAntialiasing: Bool     var backgroundColor: CGColor?     var cornerRadius: CGFloat     var borderWidth: CGFloat     var borderColor: CGColor?     var opacity: Float     var allowsGroupOpacity: Bool     var compositingFilter: AnyObject?     var filters: [AnyObject]?     var backgroundFilters: [AnyObject]?     var shouldRasterize: Bool     var rasterizationScale: CGFloat     var shadowColor: CGColor?     var shadowOpacity: Float     var shadowOffset: CGSize     var shadowRadius: CGFloat     var shadowPath: CGPath?     func preferredFrameSize() -> CGSize     func setNeedsLayout()     func needsLayout() -> Bool     func layoutIfNeeded()     func layoutSublayers()     class func defaultActionForKey(_ event: String) -> CAAction?     func actionForKey(_ event: String) -> CAAction?     var actions: [String : CAAction]?     func addAnimation(_ anim: CAAnimation, forKey key: String?)     func removeAllAnimations()     func removeAnimationForKey(_ key: String)     func animationKeys() -> [String]?     func animationForKey(_ key: String) -> CAAnimation?     var name: String?     weak var delegate: AnyObject?     var style: [NSObject : AnyObject]? } extension CALayer {     func scrollPoint(_ p: CGPoint)     func scrollRectToVisible(_ r: CGRect)     var visibleRect: CGRect { get } } ``` | CAMediaTiming, NSCoding |
| To | ``` class CALayer : NSObject, NSCoding, CAMediaTiming {     convenience init()     class func layer() -> Self     init()     init(layer layer: Any)     func presentation() -> Self?     func model() -> Self     class func defaultValue(forKey key: String) -> Any?     class func needsDisplay(forKey key: String) -> Bool     func shouldArchiveValue(forKey key: String) -> Bool     var bounds: CGRect     var position: CGPoint     var zPosition: CGFloat     var anchorPoint: CGPoint     var anchorPointZ: CGFloat     var transform: CATransform3D     func affineTransform() -> CGAffineTransform     func setAffineTransform(_ m: CGAffineTransform)     var frame: CGRect     var isHidden: Bool     var isDoubleSided: Bool     var isGeometryFlipped: Bool     func contentsAreFlipped() -> Bool     var superlayer: CALayer? { get }     func removeFromSuperlayer()     var sublayers: [CALayer]?     func addSublayer(_ layer: CALayer)     func insertSublayer(_ layer: CALayer, at idx: UInt32)     func insertSublayer(_ layer: CALayer, below sibling: CALayer?)     func insertSublayer(_ layer: CALayer, above sibling: CALayer?)     func replaceSublayer(_ layer: CALayer, with layer2: CALayer)     var sublayerTransform: CATransform3D     var mask: CALayer?     var masksToBounds: Bool     func convert(_ p: CGPoint, from l: CALayer?) -> CGPoint     func convert(_ p: CGPoint, to l: CALayer?) -> CGPoint     func convert(_ r: CGRect, from l: CALayer?) -> CGRect     func convert(_ r: CGRect, to l: CALayer?) -> CGRect     func convertTime(_ t: CFTimeInterval, from l: CALayer?) -> CFTimeInterval     func convertTime(_ t: CFTimeInterval, to l: CALayer?) -> CFTimeInterval     func hitTest(_ p: CGPoint) -> CALayer?     func contains(_ p: CGPoint) -> Bool     var contents: Any?     var contentsRect: CGRect     var contentsGravity: String     var contentsScale: CGFloat     var contentsCenter: CGRect     var contentsFormat: String     var minificationFilter: String     var magnificationFilter: String     var minificationFilterBias: Float     var isOpaque: Bool     func display()     func setNeedsDisplay()     func setNeedsDisplayIn(_ r: CGRect)     func needsDisplay() -> Bool     func displayIfNeeded()     var needsDisplayOnBoundsChange: Bool     var drawsAsynchronously: Bool     func draw(in ctx: CGContext)     func render(in ctx: CGContext)     var edgeAntialiasingMask: CAEdgeAntialiasingMask     var allowsEdgeAntialiasing: Bool     var backgroundColor: CGColor?     var cornerRadius: CGFloat     var borderWidth: CGFloat     var borderColor: CGColor?     var opacity: Float     var allowsGroupOpacity: Bool     var compositingFilter: Any?     var filters: [Any]?     var backgroundFilters: [Any]?     var shouldRasterize: Bool     var rasterizationScale: CGFloat     var shadowColor: CGColor?     var shadowOpacity: Float     var shadowOffset: CGSize     var shadowRadius: CGFloat     var shadowPath: CGPath?     func preferredFrameSize() -> CGSize     func setNeedsLayout()     func needsLayout() -> Bool     func layoutIfNeeded()     func layoutSublayers()     class func defaultAction(forKey event: String) -> CAAction?     func action(forKey event: String) -> CAAction?     var actions: [String : CAAction]?     func add(_ anim: CAAnimation, forKey key: String?)     func removeAllAnimations()     func removeAnimation(forKey key: String)     func animationKeys() -> [String]?     func animation(forKey key: String) -> CAAnimation?     var name: String?     weak var delegate: CALayerDelegate?     var style: [AnyHashable : Any]?     func scroll(_ p: CGPoint)     func scrollRectToVisible(_ r: CGRect)     var visibleRect: CGRect { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CALayer : CVarArg { } extension CALayer : Equatable, Hashable {     var hashValue: Int { get } } extension CALayer {     func scroll(_ p: CGPoint)     func scrollRectToVisible(_ r: CGRect)     var visibleRect: CGRect { get } } ``` | CAMediaTiming, CVarArg, Equatable, Hashable, NSCoding |

Modified [CALayer.action(forKey: String) -> CAAction?](https://developer.apple.com/documentation/quartzcore/calayer/1410844-action)

|  | Declaration |
| --- | --- |
| From | ``` func actionForKey(_ event: String) -> CAAction? ``` |
| To | ``` func action(forKey event: String) -> CAAction? ``` |

Modified [CALayer.add(_: CAAnimation, forKey: String?)](https://developer.apple.com/documentation/quartzcore/calayer/1410848-addanimation)

|  | Declaration |
| --- | --- |
| From | ``` func addAnimation(_ anim: CAAnimation, forKey key: String?) ``` |
| To | ``` func add(_ anim: CAAnimation, forKey key: String?) ``` |

Modified [CALayer.animation(forKey: String) -> CAAnimation?](https://developer.apple.com/documentation/quartzcore/calayer/1410808-animation)

|  | Declaration |
| --- | --- |
| From | ``` func animationForKey(_ key: String) -> CAAnimation? ``` |
| To | ``` func animation(forKey key: String) -> CAAnimation? ``` |

Modified [CALayer.backgroundFilters](https://developer.apple.com/documentation/quartzcore/calayer/1410827-backgroundfilters)

|  | Declaration |
| --- | --- |
| From | ``` var backgroundFilters: [AnyObject]? ``` |
| To | ``` var backgroundFilters: [Any]? ``` |

Modified [CALayer.compositingFilter](https://developer.apple.com/documentation/quartzcore/calayer/1410748-compositingfilter)

|  | Declaration |
| --- | --- |
| From | ``` var compositingFilter: AnyObject? ``` |
| To | ``` var compositingFilter: Any? ``` |

Modified [CALayer.contains(_: CGPoint) -> Bool](https://developer.apple.com/documentation/quartzcore/calayer/1410857-containspoint)

|  | Declaration |
| --- | --- |
| From | ``` func containsPoint(_ p: CGPoint) -> Bool ``` |
| To | ``` func contains(_ p: CGPoint) -> Bool ``` |

Modified [CALayer.contents](https://developer.apple.com/documentation/quartzcore/calayer/1410773-contents)

|  | Declaration |
| --- | --- |
| From | ``` var contents: AnyObject? ``` |
| To | ``` var contents: Any? ``` |

Modified [CALayer.convert(_: CGRect, from: CALayer?) -> CGRect](https://developer.apple.com/documentation/quartzcore/calayer/1410948-convert)

|  | Declaration |
| --- | --- |
| From | ``` func convertRect(_ r: CGRect, fromLayer l: CALayer?) -> CGRect ``` |
| To | ``` func convert(_ r: CGRect, from l: CALayer?) -> CGRect ``` |

Modified [CALayer.convert(_: CGPoint, from: CALayer?) -> CGPoint](https://developer.apple.com/documentation/quartzcore/calayer/1410825-convert)

|  | Declaration |
| --- | --- |
| From | ``` func convertPoint(_ p: CGPoint, fromLayer l: CALayer?) -> CGPoint ``` |
| To | ``` func convert(_ p: CGPoint, from l: CALayer?) -> CGPoint ``` |

Modified [CALayer.convert(_: CGRect, to: CALayer?) -> CGRect](https://developer.apple.com/documentation/quartzcore/calayer/1410742-convertrect)

|  | Declaration |
| --- | --- |
| From | ``` func convertRect(_ r: CGRect, toLayer l: CALayer?) -> CGRect ``` |
| To | ``` func convert(_ r: CGRect, to l: CALayer?) -> CGRect ``` |

Modified [CALayer.convert(_: CGPoint, to: CALayer?) -> CGPoint](https://developer.apple.com/documentation/quartzcore/calayer/1410881-convertpoint)

|  | Declaration |
| --- | --- |
| From | ``` func convertPoint(_ p: CGPoint, toLayer l: CALayer?) -> CGPoint ``` |
| To | ``` func convert(_ p: CGPoint, to l: CALayer?) -> CGPoint ``` |

Modified [CALayer.convertTime(_: CFTimeInterval, from: CALayer?) -> CFTimeInterval](https://developer.apple.com/documentation/quartzcore/calayer/1410821-converttime)

|  | Declaration |
| --- | --- |
| From | ``` func convertTime(_ t: CFTimeInterval, fromLayer l: CALayer?) -> CFTimeInterval ``` |
| To | ``` func convertTime(_ t: CFTimeInterval, from l: CALayer?) -> CFTimeInterval ``` |

Modified [CALayer.convertTime(_: CFTimeInterval, to: CALayer?) -> CFTimeInterval](https://developer.apple.com/documentation/quartzcore/calayer/1410823-converttime)

|  | Declaration |
| --- | --- |
| From | ``` func convertTime(_ t: CFTimeInterval, toLayer l: CALayer?) -> CFTimeInterval ``` |
| To | ``` func convertTime(_ t: CFTimeInterval, to l: CALayer?) -> CFTimeInterval ``` |

Modified [CALayer.defaultAction(forKey: String) -> CAAction? [class]](https://developer.apple.com/documentation/quartzcore/calayer/1410954-defaultaction)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultActionForKey(_ event: String) -> CAAction? ``` |
| To | ``` class func defaultAction(forKey event: String) -> CAAction? ``` |

Modified [CALayer.defaultValue(forKey: String) -> Any? [class]](https://developer.apple.com/documentation/quartzcore/calayer/1410886-defaultvalueforkey)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultValueForKey(_ key: String) -> AnyObject? ``` |
| To | ``` class func defaultValue(forKey key: String) -> Any? ``` |

Modified [CALayer.delegate](https://developer.apple.com/documentation/quartzcore/calayer/1410984-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: AnyObject? ``` |
| To | ``` weak var delegate: CALayerDelegate? ``` |

Modified [CALayer.draw(in: CGContext)](https://developer.apple.com/documentation/quartzcore/calayer/1410757-drawincontext)

|  | Declaration |
| --- | --- |
| From | ``` func drawInContext(_ ctx: CGContext) ``` |
| To | ``` func draw(in ctx: CGContext) ``` |

Modified [CALayer.filters](https://developer.apple.com/documentation/quartzcore/calayer/1410901-filters)

|  | Declaration |
| --- | --- |
| From | ``` var filters: [AnyObject]? ``` |
| To | ``` var filters: [Any]? ``` |

Modified [CALayer.init(layer: Any)](https://developer.apple.com/documentation/quartzcore/calayer/1410842-init)

|  | Declaration |
| --- | --- |
| From | ``` init(layer layer: AnyObject) ``` |
| To | ``` init(layer layer: Any) ``` |

Modified [CALayer.insertSublayer(_: CALayer, at: UInt32)](https://developer.apple.com/documentation/quartzcore/calayer/1410944-insertsublayer)

|  | Declaration |
| --- | --- |
| From | ``` func insertSublayer(_ layer: CALayer, atIndex idx: UInt32) ``` |
| To | ``` func insertSublayer(_ layer: CALayer, at idx: UInt32) ``` |

Modified [CALayer.isDoubleSided](https://developer.apple.com/documentation/quartzcore/calayer/1410924-doublesided)

|  | Declaration |
| --- | --- |
| From | ``` var doubleSided: Bool ``` |
| To | ``` var isDoubleSided: Bool ``` |

Modified [CALayer.isGeometryFlipped](https://developer.apple.com/documentation/quartzcore/calayer/1410960-isgeometryflipped)

|  | Declaration |
| --- | --- |
| From | ``` var geometryFlipped: Bool ``` |
| To | ``` var isGeometryFlipped: Bool ``` |

Modified [CALayer.isHidden](https://developer.apple.com/documentation/quartzcore/calayer/1410838-hidden)

|  | Declaration |
| --- | --- |
| From | ``` var hidden: Bool ``` |
| To | ``` var isHidden: Bool ``` |

Modified [CALayer.isOpaque](https://developer.apple.com/documentation/quartzcore/calayer/1410763-isopaque)

|  | Declaration |
| --- | --- |
| From | ``` var opaque: Bool ``` |
| To | ``` var isOpaque: Bool ``` |

Modified [CALayer.model() -> Self](https://developer.apple.com/documentation/quartzcore/calayer/1410853-model)

|  | Declaration |
| --- | --- |
| From | ``` func modelLayer() -> AnyObject ``` |
| To | ``` func model() -> Self ``` |

Modified [CALayer.needsDisplay(forKey: String) -> Bool [class]](https://developer.apple.com/documentation/quartzcore/calayer/1410769-needsdisplay)

|  | Declaration |
| --- | --- |
| From | ``` class func needsDisplayForKey(_ key: String) -> Bool ``` |
| To | ``` class func needsDisplay(forKey key: String) -> Bool ``` |

Modified [CALayer.presentation() -> Self?](https://developer.apple.com/documentation/quartzcore/calayer/1410744-presentation)

|  | Declaration |
| --- | --- |
| From | ``` func presentationLayer() -> AnyObject? ``` |
| To | ``` func presentation() -> Self? ``` |

Modified [CALayer.removeAnimation(forKey: String)](https://developer.apple.com/documentation/quartzcore/calayer/1410939-removeanimationforkey)

|  | Declaration |
| --- | --- |
| From | ``` func removeAnimationForKey(_ key: String) ``` |
| To | ``` func removeAnimation(forKey key: String) ``` |

Modified [CALayer.render(in: CGContext)](https://developer.apple.com/documentation/quartzcore/calayer/1410909-render)

|  | Declaration |
| --- | --- |
| From | ``` func renderInContext(_ ctx: CGContext) ``` |
| To | ``` func render(in ctx: CGContext) ``` |

Modified [CALayer.scroll(_: CGPoint)](https://developer.apple.com/documentation/quartzcore/calayer/1522202-scroll)

|  | Declaration |
| --- | --- |
| From | ``` func scrollPoint(_ p: CGPoint) ``` |
| To | ``` func scroll(_ p: CGPoint) ``` |

Modified [CALayer.setNeedsDisplayIn(_: CGRect)](https://developer.apple.com/documentation/quartzcore/calayer/1410800-setneedsdisplay)

|  | Declaration |
| --- | --- |
| From | ``` func setNeedsDisplayInRect(_ r: CGRect) ``` |
| To | ``` func setNeedsDisplayIn(_ r: CGRect) ``` |

Modified [CALayer.shouldArchiveValue(forKey: String) -> Bool](https://developer.apple.com/documentation/quartzcore/calayer/1410753-shouldarchivevalue)

|  | Declaration |
| --- | --- |
| From | ``` func shouldArchiveValueForKey(_ key: String) -> Bool ``` |
| To | ``` func shouldArchiveValue(forKey key: String) -> Bool ``` |

Modified [CALayer.style](https://developer.apple.com/documentation/quartzcore/calayer/1410875-style)

|  | Declaration |
| --- | --- |
| From | ``` var style: [NSObject : AnyObject]? ``` |
| To | ``` var style: [AnyHashable : Any]? ``` |

Modified [CAMediaTimingFunction](https://developer.apple.com/documentation/quartzcore/camediatimingfunction)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CAMediaTimingFunction : NSObject, NSCoding {     convenience init(name name: String)     class func functionWithName(_ name: String) -> Self     convenience init(controlPoints c1x: Float, _ c1y: Float, _ c2x: Float, _ c2y: Float)     class func functionWithControlPoints(_ c1x: Float, _ c1y: Float, _ c2x: Float, _ c2y: Float) -> Self     init(controlPoints c1x: Float, _ c1y: Float, _ c2x: Float, _ c2y: Float)     func getControlPointAtIndex(_ idx: Int, values ptr: UnsafeMutablePointer<Float>) } ``` | NSCoding |
| To | ``` class CAMediaTimingFunction : NSObject, NSCoding {     convenience init(name name: String)     class func withName(_ name: String) -> Self     convenience init(controlPoints c1x: Float, _ c1y: Float, _ c2x: Float, _ c2y: Float)     class func withControlPoints(_ c1x: Float, _ c1y: Float, _ c2x: Float, _ c2y: Float) -> Self     init(controlPoints c1x: Float, _ c1y: Float, _ c2x: Float, _ c2y: Float)     func getControlPoint(at idx: Int, values ptr: UnsafeMutablePointer<Float>!)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CAMediaTimingFunction : CVarArg { } extension CAMediaTimingFunction : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding |

Modified [CAMediaTimingFunction.getControlPoint(at: Int, values: UnsafeMutablePointer<Float>!)](https://developer.apple.com/documentation/quartzcore/camediatimingfunction/1522057-getcontrolpoint)

|  | Declaration |
| --- | --- |
| From | ``` func getControlPointAtIndex(_ idx: Int, values ptr: UnsafeMutablePointer<Float>) ``` |
| To | ``` func getControlPoint(at idx: Int, values ptr: UnsafeMutablePointer<Float>!) ``` |

Modified [CAMetalLayer](https://developer.apple.com/documentation/quartzcore/cametallayer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CAMetalLayer : CALayer {     var device: MTLDevice?     var pixelFormat: MTLPixelFormat     var framebufferOnly: Bool     var drawableSize: CGSize     func nextDrawable() -> CAMetalDrawable?     var presentsWithTransaction: Bool } ``` | -- |
| To | ``` class CAMetalLayer : CALayer {     var device: MTLDevice?     var pixelFormat: MTLPixelFormat     var framebufferOnly: Bool     var drawableSize: CGSize     func nextDrawable() -> CAMetalDrawable?     var presentsWithTransaction: Bool     func scroll(_ p: CGPoint)     func scrollRectToVisible(_ r: CGRect)     var visibleRect: CGRect { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CAMetalLayer : CVarArg { } extension CAMetalLayer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CAPropertyAnimation](https://developer.apple.com/documentation/quartzcore/capropertyanimation)

|  | Declaration |
| --- | --- |
| From | ``` class CAPropertyAnimation : CAAnimation {     convenience init(keyPath path: String?)     class func animationWithKeyPath(_ path: String?) -> Self     var keyPath: String?     var additive: Bool     var cumulative: Bool     var valueFunction: CAValueFunction? } ``` |
| To | ``` class CAPropertyAnimation : CAAnimation {     convenience init(keyPath path: String?)     class func withKeyPath(_ path: String?) -> Self     var keyPath: String?     var isAdditive: Bool     var isCumulative: Bool     var valueFunction: CAValueFunction? } ``` |

Modified [CAPropertyAnimation.isAdditive](https://developer.apple.com/documentation/quartzcore/capropertyanimation/1412493-additive)

|  | Declaration |
| --- | --- |
| From | ``` var additive: Bool ``` |
| To | ``` var isAdditive: Bool ``` |

Modified [CAPropertyAnimation.isCumulative](https://developer.apple.com/documentation/quartzcore/capropertyanimation/1412538-iscumulative)

|  | Declaration |
| --- | --- |
| From | ``` var cumulative: Bool ``` |
| To | ``` var isCumulative: Bool ``` |

Modified [CAReplicatorLayer](https://developer.apple.com/documentation/quartzcore/careplicatorlayer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CAReplicatorLayer : CALayer {     var instanceCount: Int     var preservesDepth: Bool     var instanceDelay: CFTimeInterval     var instanceTransform: CATransform3D     var instanceColor: CGColor?     var instanceRedOffset: Float     var instanceGreenOffset: Float     var instanceBlueOffset: Float     var instanceAlphaOffset: Float } ``` | -- |
| To | ``` class CAReplicatorLayer : CALayer {     var instanceCount: Int     var preservesDepth: Bool     var instanceDelay: CFTimeInterval     var instanceTransform: CATransform3D     var instanceColor: CGColor?     var instanceRedOffset: Float     var instanceGreenOffset: Float     var instanceBlueOffset: Float     var instanceAlphaOffset: Float     func scroll(_ p: CGPoint)     func scrollRectToVisible(_ r: CGRect)     var visibleRect: CGRect { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CAReplicatorLayer : CVarArg { } extension CAReplicatorLayer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CAScrollLayer](https://developer.apple.com/documentation/quartzcore/cascrolllayer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CAScrollLayer : CALayer {     func scrollToPoint(_ p: CGPoint)     func scrollToRect(_ r: CGRect)     var scrollMode: String } ``` | -- |
| To | ``` class CAScrollLayer : CALayer {     func scroll(to p: CGPoint)     func scroll(to r: CGRect)     var scrollMode: String     func scroll(_ p: CGPoint)     func scrollRectToVisible(_ r: CGRect)     var visibleRect: CGRect { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CAScrollLayer : CVarArg { } extension CAScrollLayer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CAScrollLayer.scroll(to: CGPoint)](https://developer.apple.com/documentation/quartzcore/cascrolllayer/1522021-scrolltopoint)

|  | Declaration |
| --- | --- |
| From | ``` func scrollToPoint(_ p: CGPoint) ``` |
| To | ``` func scroll(to p: CGPoint) ``` |

Modified [CAScrollLayer.scroll(to: CGRect)](https://developer.apple.com/documentation/quartzcore/cascrolllayer/1522167-scroll)

|  | Declaration |
| --- | --- |
| From | ``` func scrollToRect(_ r: CGRect) ``` |
| To | ``` func scroll(to r: CGRect) ``` |

Modified [CAShapeLayer](https://developer.apple.com/documentation/quartzcore/cashapelayer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CAShapeLayer : CALayer {     var path: CGPath?     var fillColor: CGColor?     var fillRule: String     var strokeColor: CGColor?     var strokeStart: CGFloat     var strokeEnd: CGFloat     var lineWidth: CGFloat     var miterLimit: CGFloat     var lineCap: String     var lineJoin: String     var lineDashPhase: CGFloat     var lineDashPattern: [NSNumber]? } ``` | -- |
| To | ``` class CAShapeLayer : CALayer {     var path: CGPath?     var fillColor: CGColor?     var fillRule: String     var strokeColor: CGColor?     var strokeStart: CGFloat     var strokeEnd: CGFloat     var lineWidth: CGFloat     var miterLimit: CGFloat     var lineCap: String     var lineJoin: String     var lineDashPhase: CGFloat     var lineDashPattern: [NSNumber]?     func scroll(_ p: CGPoint)     func scrollRectToVisible(_ r: CGRect)     var visibleRect: CGRect { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CAShapeLayer : CVarArg { } extension CAShapeLayer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CATextLayer](https://developer.apple.com/documentation/quartzcore/catextlayer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CATextLayer : CALayer {     @NSCopying var string: AnyObject?     var font: AnyObject?     var fontSize: CGFloat     var foregroundColor: CGColor?     var wrapped: Bool     var truncationMode: String     var alignmentMode: String     var allowsFontSubpixelQuantization: Bool } ``` | -- |
| To | ``` class CATextLayer : CALayer {     var string: Any?     var font: CFTypeRef?     var fontSize: CGFloat     var foregroundColor: CGColor?     var isWrapped: Bool     var truncationMode: String     var alignmentMode: String     var allowsFontSubpixelQuantization: Bool     func scroll(_ p: CGPoint)     func scrollRectToVisible(_ r: CGRect)     var visibleRect: CGRect { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CATextLayer : CVarArg { } extension CATextLayer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CATextLayer.font](https://developer.apple.com/documentation/quartzcore/catextlayer/1515303-font)

|  | Declaration |
| --- | --- |
| From | ``` var font: AnyObject? ``` |
| To | ``` var font: CFTypeRef? ``` |

Modified [CATextLayer.isWrapped](https://developer.apple.com/documentation/quartzcore/catextlayer/1515302-wrapped)

|  | Declaration |
| --- | --- |
| From | ``` var wrapped: Bool ``` |
| To | ``` var isWrapped: Bool ``` |

Modified [CATextLayer.string](https://developer.apple.com/documentation/quartzcore/catextlayer/1515295-string)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var string: AnyObject? ``` |
| To | ``` var string: Any? ``` |

Modified [CATiledLayer](https://developer.apple.com/documentation/quartzcore/catiledlayer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CATiledLayer : CALayer {     class func fadeDuration() -> CFTimeInterval     var levelsOfDetail: Int     var levelsOfDetailBias: Int     var tileSize: CGSize } ``` | -- |
| To | ``` class CATiledLayer : CALayer {     class func fadeDuration() -> CFTimeInterval     var levelsOfDetail: Int     var levelsOfDetailBias: Int     var tileSize: CGSize     func scroll(_ p: CGPoint)     func scrollRectToVisible(_ r: CGRect)     var visibleRect: CGRect { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CATiledLayer : CVarArg { } extension CATiledLayer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CATransaction](https://developer.apple.com/documentation/quartzcore/catransaction)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CATransaction : NSObject {     class func begin()     class func commit()     class func flush()     class func lock()     class func unlock()     class func animationDuration() -> CFTimeInterval     class func setAnimationDuration(_ dur: CFTimeInterval)     class func animationTimingFunction() -> CAMediaTimingFunction?     class func setAnimationTimingFunction(_ function: CAMediaTimingFunction?)     class func disableActions() -> Bool     class func setDisableActions(_ flag: Bool)     class func completionBlock() -> (() -> Void)?     class func setCompletionBlock(_ block: (() -> Void)?)     class func valueForKey(_ key: String) -> AnyObject?     class func setValue(_ anObject: AnyObject?, forKey key: String) } ``` | -- |
| To | ``` class CATransaction : NSObject {     class func begin()     class func commit()     class func flush()     class func lock()     class func unlock()     class func animationDuration() -> CFTimeInterval     class func setAnimationDuration(_ dur: CFTimeInterval)     class func animationTimingFunction() -> CAMediaTimingFunction?     class func setAnimationTimingFunction(_ function: CAMediaTimingFunction?)     class func disableActions() -> Bool     class func setDisableActions(_ flag: Bool)     class func completionBlock() -> (() -> Swift.Void)?     class func setCompletionBlock(_ block: (@escaping () -> Swift.Void)?)     class func value(forKey key: String) -> Any?     class func setValue(_ anObject: Any?, forKey key: String)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CATransaction : CVarArg { } extension CATransaction : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CATransaction.completionBlock() -> (() -> Swift.Void)? [class]](https://developer.apple.com/documentation/quartzcore/catransaction/1448280-completionblock)

|  | Declaration |
| --- | --- |
| From | ``` class func completionBlock() -> (() -> Void)? ``` |
| To | ``` class func completionBlock() -> (() -> Swift.Void)? ``` |

Modified [CATransaction.setCompletionBlock(_: ( () -> Swift.Void)?) [class]](https://developer.apple.com/documentation/quartzcore/catransaction/1448281-setcompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` class func setCompletionBlock(_ block: (() -> Void)?) ``` |
| To | ``` class func setCompletionBlock(_ block: (@escaping () -> Swift.Void)?) ``` |

Modified [CATransaction.setValue(_: Any?, forKey: String) [class]](https://developer.apple.com/documentation/quartzcore/catransaction/1448278-setvalue)

|  | Declaration |
| --- | --- |
| From | ``` class func setValue(_ anObject: AnyObject?, forKey key: String) ``` |
| To | ``` class func setValue(_ anObject: Any?, forKey key: String) ``` |

Modified [CATransaction.value(forKey: String) -> Any? [class]](https://developer.apple.com/documentation/quartzcore/catransaction/1448259-value)

|  | Declaration |
| --- | --- |
| From | ``` class func valueForKey(_ key: String) -> AnyObject? ``` |
| To | ``` class func value(forKey key: String) -> Any? ``` |

Modified [CATransformLayer](https://developer.apple.com/documentation/quartzcore/catransformlayer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CATransformLayer : CALayer { } ``` | -- |
| To | ``` class CATransformLayer : CALayer {     func scroll(_ p: CGPoint)     func scrollRectToVisible(_ r: CGRect)     var visibleRect: CGRect { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CATransformLayer : CVarArg { } extension CATransformLayer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CATransition](https://developer.apple.com/documentation/quartzcore/catransition)

|  | Declaration |
| --- | --- |
| From | ``` class CATransition : CAAnimation {     var type: String     var subtype: String?     var startProgress: Float     var endProgress: Float     var filter: AnyObject? } ``` |
| To | ``` class CATransition : CAAnimation {     var type: String     var subtype: String?     var startProgress: Float     var endProgress: Float     var filter: Any? } ``` |

Modified [CATransition.filter](https://developer.apple.com/documentation/quartzcore/catransition/1412506-filter)

|  | Declaration |
| --- | --- |
| From | ``` var filter: AnyObject? ``` |
| To | ``` var filter: Any? ``` |

Modified [CAValueFunction](https://developer.apple.com/documentation/quartzcore/cavaluefunction)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CAValueFunction : NSObject, NSCoding {     convenience init?(name name: String)     class func functionWithName(_ name: String) -> Self?     var name: String { get } } ``` | NSCoding |
| To | ``` class CAValueFunction : NSObject, NSCoding {     convenience init?(name name: String)     class func withName(_ name: String) -> Self?     var name: String { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CAValueFunction : CVarArg { } extension CAValueFunction : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding |

Modified [NSValue.caTransform3DValue](https://developer.apple.com/documentation/foundation/nsvalue/1436572-catransform3dvalue)

|  | Declaration |
| --- | --- |
| From | ``` var CATransform3DValue: CATransform3D { get } ``` |
| To | ``` var caTransform3DValue: CATransform3D { get } ``` |

Modified [NSValue.init(caTransform3D: CATransform3D)](https://developer.apple.com/documentation/foundation/nsvalue/1436556-valuewithcatransform3d)

|  | Declaration |
| --- | --- |
| From | ``` init(CATransform3D t: CATransform3D) ``` |
| To | ``` init(caTransform3D t: CATransform3D) ``` |

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
