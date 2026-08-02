---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/ObjectiveC.html
archived_at: '2026-07-18T02:56:56.385939Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# ObjectiveC Changes for Swift

### ObjectiveC

Removed NSObject.alloc() -> Self [class]Removed NSObject.allocWithZone(_: NSZone) -> Self [class]Removed NSObject.new() -> Self [class]Removed NSZone.pointerRemoved objc_super.init(receiver: AnyObject!, super_class: AnyClass!)Removed ObjCBool.getMirror() -> MirrorTypeRemoved ObjCBool.init(_: Int8)Removed ObjCBool.valueRemoved Selector.getMirror() -> MirrorTypeRemoved Selector.ptrRemoved OBJC_ASSOCIATION_ASSIGNRemoved OBJC_ASSOCIATION_COPYRemoved OBJC_ASSOCIATION_COPY_NONATOMICRemoved OBJC_ASSOCIATION_RETAINRemoved OBJC_ASSOCIATION_RETAIN_NONATOMICRemoved objc_AssociationPolicyAdded [NSObject.hashValue](https://developer.apple.com/documentation/objectivec/nsobject/1418615-hashvalue)Added [NSObjectProtocol.performSelector(_: Selector) -> Unmanaged<AnyObject>!](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/1418867-perform)Added [NSObjectProtocol.performSelector(_: Selector, withObject: AnyObject!) -> Unmanaged<AnyObject>!](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/1418764-perform)Added [NSObjectProtocol.performSelector(_: Selector, withObject: AnyObject!, withObject: AnyObject!) -> Unmanaged<AnyObject>!](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1418667-performselector)Added [objc_AssociationPolicy [enum]](https://developer.apple.com/documentation/objectivec/objc_associationpolicy)Added [objc_AssociationPolicy.OBJC_ASSOCIATION_ASSIGN](https://developer.apple.com/documentation/objectivec/objc_associationpolicy/objc_association_assign)Added [objc_AssociationPolicy.OBJC_ASSOCIATION_COPY](https://developer.apple.com/documentation/objectivec/objc_associationpolicy/objc_association_copy)Added [objc_AssociationPolicy.OBJC_ASSOCIATION_COPY_NONATOMIC](https://developer.apple.com/documentation/objectivec/objc_associationpolicy/objc_association_copy_nonatomic)Added [objc_AssociationPolicy.OBJC_ASSOCIATION_RETAIN](https://developer.apple.com/documentation/objectivec/objc_associationpolicy/objc_association_retain)Added [objc_AssociationPolicy.OBJC_ASSOCIATION_RETAIN_NONATOMIC](https://developer.apple.com/documentation/objectivec/objc_associationpolicy/objc_association_retain_nonatomic)Added [objc_object.isa](https://developer.apple.com/documentation/objectivec/objc_object/1418809-isa)Added objc_super.init(receiver: Unmanaged<AnyObject>!, super_class: AnyClass!)Added ==(_: NSObject, _: NSObject) -> BoolAdded [NS_ENFORCE_NSOBJECT_DESIGNATED_INITIALIZER](https://developer.apple.com/documentation/objectivec/ns_enforce_nsobject_designated_initializer)Added [OBJC_BOOL_IS_CHAR](https://developer.apple.com/documentation/objectivec/objc_bool_is_char)Added objc_collect_if_needed(_: UInt)Added [OBJC_NO_GC_API](https://developer.apple.com/documentation/objectivec/objc_no_gc_api)Modified [NSObject](https://developer.apple.com/documentation/objectivec/nsobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSObject : NSObjectProtocol {     class func load()     class func initialize()     init()     class func new() -> Self     class func allocWithZone(_ zone: NSZone) -> Self     class func alloc() -> Self     func dealloc()     func finalize()     func copy() -> AnyObject     func mutableCopy() -> AnyObject     class func copyWithZone(_ zone: NSZone) -> AnyObject!     class func mutableCopyWithZone(_ zone: NSZone) -> AnyObject!     class func instancesRespondToSelector(_ aSelector: Selector) -> Bool     class func conformsToProtocol(_ `protocol`: Protocol) -> Bool     func methodForSelector(_ aSelector: Selector) -> IMP     class func instanceMethodForSelector(_ aSelector: Selector) -> IMP     func doesNotRecognizeSelector(_ aSelector: Selector)     func forwardingTargetForSelector(_ aSelector: Selector) -> AnyObject?     func forwardInvocation(_ anInvocation: NSInvocation!)     func methodSignatureForSelector(_ aSelector: Selector) -> NSMethodSignature!     class func instanceMethodSignatureForSelector(_ aSelector: Selector) -> NSMethodSignature!     func allowsWeakReference() -> Bool     func retainWeakReference() -> Bool     class func isSubclassOfClass(_ aClass: AnyClass) -> Bool     class func resolveClassMethod(_ sel: Selector) -> Bool     class func resolveInstanceMethod(_ sel: Selector) -> Bool     class func hash() -> Int     class func superclass() -> AnyClass?     class func `class`() -> AnyClass!     class func description() -> String     class func debugDescription() -> String } extension NSObject {     func attemptRecoveryFromError(_ error: NSError!, optionIndex recoveryOptionIndex: Int, delegate delegate: AnyObject!, didRecoverSelector didRecoverSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func attemptRecoveryFromError(_ error: NSError!, optionIndex recoveryOptionIndex: Int) -> Bool } extension NSObject {     func fileManager(_ fm: NSFileManager!, shouldProceedAfterError errorInfo: [NSObject : AnyObject]!) -> Bool     func fileManager(_ fm: NSFileManager!, willProcessPath path: String!) } extension NSObject {     class func accessInstanceVariablesDirectly() -> Bool     func valueForKey(_ key: String) -> AnyObject?     func setValue(_ value: AnyObject?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String, error outError: NSErrorPointer) -> Bool     func mutableArrayValueForKey(_ key: String) -> NSMutableArray     func mutableOrderedSetValueForKey(_ key: String) -> NSMutableOrderedSet     func mutableSetValueForKey(_ key: String) -> NSMutableSet     func valueForKeyPath(_ keyPath: String) -> AnyObject?     func setValue(_ value: AnyObject?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String, error outError: NSErrorPointer) -> Bool     func mutableArrayValueForKeyPath(_ keyPath: String) -> NSMutableArray     func mutableOrderedSetValueForKeyPath(_ keyPath: String) -> NSMutableOrderedSet     func mutableSetValueForKeyPath(_ keyPath: String) -> NSMutableSet     func valueForUndefinedKey(_ key: String) -> AnyObject?     func setValue(_ value: AnyObject?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValuesForKeys(_ keys: [AnyObject]) -> [NSObject : AnyObject]     func setValuesForKeysWithDictionary(_ keyedValues: [NSObject : AnyObject]) } extension NSObject {     func observeValueForKeyPath(_ keyPath: String, ofObject object: AnyObject, change change: [NSObject : AnyObject], context context: UnsafeMutablePointer<Void>) } extension NSObject {     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) } extension NSObject {     func willChangeValueForKey(_ key: String)     func didChangeValueForKey(_ key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAtIndexes indexes: NSIndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAtIndexes indexes: NSIndexSet, forKey key: String)     func willChangeValueForKey(_ key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, usingObjects objects: Set<NSObject>)     func didChangeValueForKey(_ key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, usingObjects objects: Set<NSObject>) } extension NSObject {     class func keyPathsForValuesAffectingValueForKey(_ key: String) -> Set<NSObject>     class func automaticallyNotifiesObserversForKey(_ key: String) -> Bool     var observationInfo: UnsafeMutablePointer<Void> } extension NSObject {     var classForKeyedArchiver: AnyClass? { get }     func replacementObjectForKeyedArchiver(_ archiver: NSKeyedArchiver) -> AnyObject?     class func classFallbacksForKeyedArchiver() -> [AnyObject] } extension NSObject {     class func classForKeyedUnarchiver() -> AnyClass } extension NSObject {     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObjectForCoder(_ aCoder: NSCoder) -> AnyObject?     func awakeAfterUsingCoder(_ aDecoder: NSCoder) -> AnyObject? } extension NSObject {     var autoContentAccessingProxy: AnyObject { get } } extension NSObject {     func performSelector(_ aSelector: Selector, withObject anArgument: AnyObject!, afterDelay delay: NSTimeInterval, inModes modes: [AnyObject]!)     func performSelector(_ aSelector: Selector, withObject anArgument: AnyObject!, afterDelay delay: NSTimeInterval)     class func cancelPreviousPerformRequestsWithTarget(_ aTarget: AnyObject, selector aSelector: Selector, object anArgument: AnyObject?)     class func cancelPreviousPerformRequestsWithTarget(_ aTarget: AnyObject) } extension NSObject {     func performSelectorOnMainThread(_ aSelector: Selector, withObject arg: AnyObject!, waitUntilDone wait: Bool, modes array: [AnyObject]!)     func performSelectorOnMainThread(_ aSelector: Selector, withObject arg: AnyObject!, waitUntilDone wait: Bool)     func performSelector(_ aSelector: Selector, onThread thr: NSThread!, withObject arg: AnyObject!, waitUntilDone wait: Bool, modes array: [AnyObject]!)     func performSelector(_ aSelector: Selector, onThread thr: NSThread!, withObject arg: AnyObject!, waitUntilDone wait: Bool)     func performSelectorInBackground(_ aSelector: Selector, withObject arg: AnyObject!) } extension NSObject : CVarArgType {     func encode() -> [Word] } extension NSObject : Printable { } extension NSObject : Equatable, Hashable {     var hashValue: Int { get } } extension NSObject {     func animationDidStart(_ anim: CAAnimation!)     func animationDidStop(_ anim: CAAnimation!, finished flag: Bool) } extension NSObject {     func displayLayer(_ layer: CALayer!)     func drawLayer(_ layer: CALayer!, inContext ctx: CGContext!)     func layoutSublayersOfLayer(_ layer: CALayer!)     func actionForLayer(_ layer: CALayer!, forKey event: String!) -> CAAction! } extension NSObject {     var isAccessibilityElement: Bool     var accessibilityLabel: String!     var accessibilityHint: String!     var accessibilityValue: String!     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath!     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String!     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle } extension NSObject {     func accessibilityElementCount() -> Int     func accessibilityElementAtIndex(_ index: Int) -> AnyObject!     func indexOfAccessibilityElement(_ element: AnyObject!) -> Int     var accessibilityElements: [AnyObject]! } extension NSObject {     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool } extension NSObject {     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [AnyObject]! } extension NSObject {     func awakeFromNib()     func prepareForInterfaceBuilder() } extension NSObject {     func cut(_ sender: AnyObject?)     func copy(_ sender: AnyObject?)     func paste(_ sender: AnyObject?)     func select(_ sender: AnyObject?)     func selectAll(_ sender: AnyObject?)     func delete(_ sender: AnyObject?)     func makeTextWritingDirectionLeftToRight(_ sender: AnyObject?)     func makeTextWritingDirectionRightToLeft(_ sender: AnyObject?)     func toggleBoldface(_ sender: AnyObject?)     func toggleItalics(_ sender: AnyObject?)     func toggleUnderline(_ sender: AnyObject?)     func increaseSize(_ sender: AnyObject?)     func decreaseSize(_ sender: AnyObject?) } ``` | AnyObject, CVarArgType, Equatable, Hashable, NSObjectProtocol, Printable |
| To | ``` class NSObject : NSObjectProtocol {     class func load()     class func initialize()     init()     class func new() -> Self     class func allocWithZone(_ zone: NSZone) -> Self     class func alloc() -> Self     func finalize()     func copy() -> AnyObject     func mutableCopy() -> AnyObject     class func copyWithZone(_ zone: NSZone) -> AnyObject!     class func mutableCopyWithZone(_ zone: NSZone) -> AnyObject!     class func instancesRespondToSelector(_ aSelector: Selector) -> Bool     class func conformsToProtocol(_ `protocol`: Protocol) -> Bool     func methodForSelector(_ aSelector: Selector) -> IMP     class func instanceMethodForSelector(_ aSelector: Selector) -> IMP     func doesNotRecognizeSelector(_ aSelector: Selector)     func forwardingTargetForSelector(_ aSelector: Selector) -> AnyObject?     func forwardInvocation(_ anInvocation: NSInvocation!)     func methodSignatureForSelector(_ aSelector: Selector) -> NSMethodSignature!     class func instanceMethodSignatureForSelector(_ aSelector: Selector) -> NSMethodSignature!     func allowsWeakReference() -> Bool     func retainWeakReference() -> Bool     class func isSubclassOfClass(_ aClass: AnyClass) -> Bool     class func resolveClassMethod(_ sel: Selector) -> Bool     class func resolveInstanceMethod(_ sel: Selector) -> Bool     class func hash() -> Int     class func superclass() -> AnyClass?     class func `class`() -> AnyClass!     class func description() -> String     class func debugDescription() -> String } extension NSObject {     func provideImageData(_ data: UnsafeMutablePointer<Void>, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: AnyObject?) } extension NSObject {     func attemptRecoveryFromError(_ error: NSError, optionIndex recoveryOptionIndex: Int, delegate delegate: AnyObject?, didRecoverSelector didRecoverSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func attemptRecoveryFromError(_ error: NSError, optionIndex recoveryOptionIndex: Int) -> Bool } extension NSObject {     func fileManager(_ fm: NSFileManager, shouldProceedAfterError errorInfo: [NSObject : AnyObject]) -> Bool     func fileManager(_ fm: NSFileManager, willProcessPath path: String) } extension NSObject {     class func accessInstanceVariablesDirectly() -> Bool     func valueForKey(_ key: String) -> AnyObject?     func setValue(_ value: AnyObject?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValueForKey(_ key: String) -> NSMutableArray     func mutableOrderedSetValueForKey(_ key: String) -> NSMutableOrderedSet     func mutableSetValueForKey(_ key: String) -> NSMutableSet     func valueForKeyPath(_ keyPath: String) -> AnyObject?     func setValue(_ value: AnyObject?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValueForKeyPath(_ keyPath: String) -> NSMutableArray     func mutableOrderedSetValueForKeyPath(_ keyPath: String) -> NSMutableOrderedSet     func mutableSetValueForKeyPath(_ keyPath: String) -> NSMutableSet     func valueForUndefinedKey(_ key: String) -> AnyObject?     func setValue(_ value: AnyObject?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValuesForKeys(_ keys: [String]) -> [String : AnyObject]     func setValuesForKeysWithDictionary(_ keyedValues: [String : AnyObject]) } extension NSObject {     func observeValueForKeyPath(_ keyPath: String?, ofObject object: AnyObject?, change change: [String : AnyObject]?, context context: UnsafeMutablePointer<Void>) } extension NSObject {     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) } extension NSObject {     func willChangeValueForKey(_ key: String)     func didChangeValueForKey(_ key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAtIndexes indexes: NSIndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAtIndexes indexes: NSIndexSet, forKey key: String)     func willChangeValueForKey(_ key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, usingObjects objects: Set<NSObject>)     func didChangeValueForKey(_ key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, usingObjects objects: Set<NSObject>) } extension NSObject {     class func keyPathsForValuesAffectingValueForKey(_ key: String) -> Set<String>     class func automaticallyNotifiesObserversForKey(_ key: String) -> Bool     var observationInfo: UnsafeMutablePointer<Void> } extension NSObject {     var classForKeyedArchiver: AnyClass? { get }     func replacementObjectForKeyedArchiver(_ archiver: NSKeyedArchiver) -> AnyObject?     class func classFallbacksForKeyedArchiver() -> [String] } extension NSObject {     class func classForKeyedUnarchiver() -> AnyClass } extension NSObject {     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObjectForCoder(_ aCoder: NSCoder) -> AnyObject?     func awakeAfterUsingCoder(_ aDecoder: NSCoder) -> AnyObject? } extension NSObject {     var autoContentAccessingProxy: AnyObject { get } } extension NSObject {     func performSelector(_ aSelector: Selector, withObject anArgument: AnyObject?, afterDelay delay: NSTimeInterval, inModes modes: [String])     func performSelector(_ aSelector: Selector, withObject anArgument: AnyObject?, afterDelay delay: NSTimeInterval)     class func cancelPreviousPerformRequestsWithTarget(_ aTarget: AnyObject, selector aSelector: Selector, object anArgument: AnyObject?)     class func cancelPreviousPerformRequestsWithTarget(_ aTarget: AnyObject) } extension NSObject {     func performSelectorOnMainThread(_ aSelector: Selector, withObject arg: AnyObject?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelectorOnMainThread(_ aSelector: Selector, withObject arg: AnyObject?, waitUntilDone wait: Bool)     func performSelector(_ aSelector: Selector, onThread thr: NSThread, withObject arg: AnyObject?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(_ aSelector: Selector, onThread thr: NSThread, withObject arg: AnyObject?, waitUntilDone wait: Bool)     func performSelectorInBackground(_ aSelector: Selector, withObject arg: AnyObject?) } extension NSObject : CustomStringConvertible { } extension NSObject : Equatable, Hashable {     var hashValue: Int { get } } extension NSObject : CVarArgType { } extension NSObject : Equatable, Hashable {     var hashValue: Int { get } } extension NSObject : CVarArgType { } extension NSObject {     func animationDidStart(_ anim: CAAnimation)     func animationDidStop(_ anim: CAAnimation, finished flag: Bool) } extension NSObject {     func displayLayer(_ layer: CALayer)     func drawLayer(_ layer: CALayer, inContext ctx: CGContext)     func layoutSublayersOfLayer(_ layer: CALayer)     func actionForLayer(_ layer: CALayer, forKey event: String) -> CAAction? } extension NSObject {     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle } extension NSObject {     func accessibilityElementCount() -> Int     func accessibilityElementAtIndex(_ index: Int) -> AnyObject?     func indexOfAccessibilityElement(_ element: AnyObject) -> Int     var accessibilityElements: [AnyObject]? } extension NSObject {     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>? } extension NSObject {     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]? } extension NSObject {     func awakeFromNib()     func prepareForInterfaceBuilder() } extension NSObject {     func cut(_ sender: AnyObject?)     func copy(_ sender: AnyObject?)     func paste(_ sender: AnyObject?)     func select(_ sender: AnyObject?)     func selectAll(_ sender: AnyObject?)     func delete(_ sender: AnyObject?)     func makeTextWritingDirectionLeftToRight(_ sender: AnyObject?)     func makeTextWritingDirectionRightToLeft(_ sender: AnyObject?)     func toggleBoldface(_ sender: AnyObject?)     func toggleItalics(_ sender: AnyObject?)     func toggleUnderline(_ sender: AnyObject?)     func increaseSize(_ sender: AnyObject?)     func decreaseSize(_ sender: AnyObject?) } ``` | AnyObject, CVarArgType, CustomStringConvertible, Equatable, Hashable, NSObjectProtocol |

Modified [NSObjectProtocol](https://developer.apple.com/documentation/objectivec/nsobjectprotocol)

|  | Declaration |
| --- | --- |
| From | ``` protocol NSObjectProtocol {     func isEqual(_ object: AnyObject?) -> Bool     var hash: Int { get }     var superclass: AnyClass? { get }     optional func `class`() -> AnyClass!     func `self`() -> Self     func performSelector(_ aSelector: Selector) -> AnyObject!     func performSelector(_ aSelector: Selector, withObject object: AnyObject!) -> AnyObject!     func performSelector(_ aSelector: Selector, withObject object1: AnyObject!, withObject object2: AnyObject!) -> AnyObject!     func isProxy() -> Bool     func isKindOfClass(_ aClass: AnyClass) -> Bool     func isMemberOfClass(_ aClass: AnyClass) -> Bool     func conformsToProtocol(_ aProtocol: Protocol) -> Bool     func respondsToSelector(_ aSelector: Selector) -> Bool     func retain() -> Self!     func release()     func autorelease() -> Self!     func retainCount() -> Int     func zone() -> NSZone     var description: String { get }     optional var debugDescription: String { get } } ``` |
| To | ``` protocol NSObjectProtocol {     func isEqual(_ object: AnyObject?) -> Bool     var hash: Int { get }     var superclass: AnyClass? { get }     func `class`() -> AnyClass!     func `self`() -> Self     func performSelector(_ aSelector: Selector) -> Unmanaged<AnyObject>!     func performSelector(_ aSelector: Selector, withObject object: AnyObject!) -> Unmanaged<AnyObject>!     func performSelector(_ aSelector: Selector, withObject object1: AnyObject!, withObject object2: AnyObject!) -> Unmanaged<AnyObject>!     func isProxy() -> Bool     func isKindOfClass(_ aClass: AnyClass) -> Bool     func isMemberOfClass(_ aClass: AnyClass) -> Bool     func conformsToProtocol(_ aProtocol: Protocol) -> Bool     func respondsToSelector(_ aSelector: Selector) -> Bool     func retain() -> Self!     func release()     func autorelease() -> Self!     func retainCount() -> Int     func zone() -> NSZone     var description: String { get }     optional var debugDescription: String { get } } ``` |

Modified [NSZone [struct]](https://developer.apple.com/documentation/objectivec/nszone)

|  | Declaration |
| --- | --- |
| From | ``` struct NSZone : NilLiteralConvertible {     var pointer: COpaquePointer     init()     init(nilLiteral nilLiteral: ()) } ``` |
| To | ``` struct NSZone : NilLiteralConvertible {     init()     init(nilLiteral nilLiteral: ()) } ``` |

Modified [objc_super [struct]](https://developer.apple.com/documentation/objectivec/objc_super)

|  | Declaration |
| --- | --- |
| From | ``` struct objc_super {     var receiver: AnyObject!     var super_class: AnyClass!     init()     init(receiver receiver: AnyObject!, super_class super_class: AnyClass!) } ``` |
| To | ``` struct objc_super {     var receiver: Unmanaged<AnyObject>!     var super_class: AnyClass!     init()     init(receiver receiver: Unmanaged<AnyObject>!, super_class super_class: AnyClass!) } ``` |

Modified [objc_super.receiver](https://developer.apple.com/documentation/objectivec/objc_super/1418543-receiver)

|  | Declaration |
| --- | --- |
| From | ``` var receiver: AnyObject! ``` |
| To | ``` var receiver: Unmanaged<AnyObject>! ``` |

Modified [ObjCBool [struct]](https://developer.apple.com/documentation/objectivec/objcbool)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ObjCBool : BooleanType, BooleanLiteralConvertible {     var value: Int8     init(_ value: Int8)     init(_ value: Bool)     var boolValue: Bool { get }     init(booleanLiteral value: Bool) } extension ObjCBool : Reflectable {     func getMirror() -> MirrorType } extension ObjCBool : Printable {     var description: String { get } } ``` | BooleanLiteralConvertible, BooleanType, Printable, Reflectable |
| To | ``` struct ObjCBool : BooleanType, BooleanLiteralConvertible {     init(_ value: Bool)     var boolValue: Bool { get }     init(booleanLiteral value: Bool) } extension ObjCBool : _Reflectable { } extension ObjCBool : CustomStringConvertible {     var description: String { get } } ``` | BooleanLiteralConvertible, BooleanType, CustomStringConvertible |

Modified [Selector [struct]](https://developer.apple.com/documentation/objectivec/selector)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Selector : StringLiteralConvertible, NilLiteralConvertible {     var ptr: COpaquePointer     init(_ str: String)     init(unicodeScalarLiteral value: String)     init(extendedGraphemeClusterLiteral value: String)     init(stringLiteral value: String)     init()     init(nilLiteral nilLiteral: ()) } extension Selector : Equatable, Hashable {     var hashValue: Int { get } } extension Selector : Printable {     var description: String { get } } extension Selector : Reflectable {     func getMirror() -> MirrorType } ``` | Equatable, Hashable, NilLiteralConvertible, Printable, Reflectable, StringLiteralConvertible |
| To | ``` struct Selector : StringLiteralConvertible, ExtendedGraphemeClusterLiteralConvertible, UnicodeScalarLiteralConvertible, NilLiteralConvertible {     init(_ str: String)     init(unicodeScalarLiteral value: String)     init(extendedGraphemeClusterLiteral value: String)     init(stringLiteral value: String)     init()     init(nilLiteral nilLiteral: ()) } extension Selector : Equatable, Hashable {     var hashValue: Int { get } } extension Selector : CustomStringConvertible {     var description: String { get } } extension Selector : _Reflectable { } ``` | CustomStringConvertible, Equatable, ExtendedGraphemeClusterLiteralConvertible, Hashable, NilLiteralConvertible, StringLiteralConvertible, UnicodeScalarLiteralConvertible |

Modified &&(_: T, _: () -> ObjCBool) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func &&<T : BooleanType>(_ lhs: T, _ rhs: @autoclosurerhs: @autoclosure () -> ObjCBool) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func &&<T : BooleanType>(_ lhs: T, @autoclosure _ rhs: () -> ObjCBool) -> Bool ``` | iOS 9.0 | ``` T : BooleanType ``` | T |

Modified ==(_: Selector, _: Selector) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ==(_ lhs: Selector, _ rhs: Selector) -> Bool ``` |
| To | ``` @warn_unused_result func ==(_ lhs: Selector, _ rhs: Selector) -> Bool ``` |

Modified autoreleasepool(_: () -> ())

|  | Declaration |
| --- | --- |
| From | ``` func autoreleasepool(_ code: @noescape () -> ()) ``` |
| To | ``` func autoreleasepool(@noescape _ code: () -> ()) ``` |

Modified objc_exception_handler

|  | Declaration |
| --- | --- |
| From | ``` typealias objc_exception_handler = CFunctionPointer<((AnyObject!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias objc_exception_handler = (AnyObject!, UnsafeMutablePointer<Void>) -> Void ``` |

Modified objc_exception_matcher

|  | Declaration |
| --- | --- |
| From | ``` typealias objc_exception_matcher = CFunctionPointer<((AnyClass!, AnyObject!) -> Int32)> ``` |
| To | ``` typealias objc_exception_matcher = (AnyClass!, AnyObject!) -> Int32 ``` |

Modified objc_exception_preprocessor

|  | Declaration |
| --- | --- |
| From | ``` typealias objc_exception_preprocessor = CFunctionPointer<((AnyObject!) -> AnyObject!)> ``` |
| To | ``` typealias objc_exception_preprocessor = (AnyObject!) -> AnyObject! ``` |

Modified [objc_setEnumerationMutationHandler(_: ((AnyObject!) -> Void)!)](https://developer.apple.com/documentation/objectivec/1418751-objc_setenumerationmutationhandl)

|  | Declaration |
| --- | --- |
| From | ``` func objc_setEnumerationMutationHandler(_ handler: CFunctionPointer<((AnyObject!) -> Void)>) ``` |
| To | ``` func objc_setEnumerationMutationHandler(_ handler: ((AnyObject!) -> Void)!) ``` |

Modified objc_setExceptionMatcher(_: objc_exception_matcher!) -> objc_exception_matcher!

|  | Declaration |
| --- | --- |
| From | ``` func objc_setExceptionMatcher(_ fn: objc_exception_matcher) -> objc_exception_matcher ``` |
| To | ``` func objc_setExceptionMatcher(_ fn: objc_exception_matcher!) -> objc_exception_matcher! ``` |

Modified objc_setExceptionPreprocessor(_: objc_exception_preprocessor!) -> objc_exception_preprocessor!

|  | Declaration |
| --- | --- |
| From | ``` func objc_setExceptionPreprocessor(_ fn: objc_exception_preprocessor) -> objc_exception_preprocessor ``` |
| To | ``` func objc_setExceptionPreprocessor(_ fn: objc_exception_preprocessor!) -> objc_exception_preprocessor! ``` |

Modified objc_setUncaughtExceptionHandler(_: objc_uncaught_exception_handler!) -> objc_uncaught_exception_handler!

|  | Declaration |
| --- | --- |
| From | ``` func objc_setUncaughtExceptionHandler(_ fn: objc_uncaught_exception_handler) -> objc_uncaught_exception_handler ``` |
| To | ``` func objc_setUncaughtExceptionHandler(_ fn: objc_uncaught_exception_handler!) -> objc_uncaught_exception_handler! ``` |

Modified objc_uncaught_exception_handler

|  | Declaration |
| --- | --- |
| From | ``` typealias objc_uncaught_exception_handler = CFunctionPointer<((AnyObject!) -> Void)> ``` |
| To | ``` typealias objc_uncaught_exception_handler = (AnyObject!) -> Void ``` |

Modified ||(_: T, _: () -> ObjCBool) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func ||<T : BooleanType>(_ lhs: T, _ rhs: @autoclosurerhs: @autoclosure () -> ObjCBool) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func ||<T : BooleanType>(_ lhs: T, @autoclosure _ rhs: () -> ObjCBool) -> Bool ``` | iOS 9.0 | ``` T : BooleanType ``` | T |

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
