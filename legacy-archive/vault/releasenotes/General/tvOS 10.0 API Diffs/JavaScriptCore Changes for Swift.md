---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Swift/JavaScriptCore.html
archived_at: '2026-07-18T02:57:50.094075Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# JavaScriptCore Changes for Swift

### JavaScriptCore

Removed JSClassDefinition.init(version: Int32, attributes: JSClassAttributes, className: UnsafePointer<Int8>, parentClass: JSClassRef, staticValues: UnsafePointer<JSStaticValue>, staticFunctions: UnsafePointer<JSStaticFunction>, initialize: JSObjectInitializeCallback!, finalize: JSObjectFinalizeCallback!, hasProperty: JSObjectHasPropertyCallback!, getProperty: JSObjectGetPropertyCallback!, setProperty: JSObjectSetPropertyCallback!, deleteProperty: JSObjectDeletePropertyCallback!, getPropertyNames: JSObjectGetPropertyNamesCallback!, callAsFunction: JSObjectCallAsFunctionCallback!, callAsConstructor: JSObjectCallAsConstructorCallback!, hasInstance: JSObjectHasInstanceCallback!, convertToType: JSObjectConvertToTypeCallback!)Removed JSStaticFunction.init(name: UnsafePointer<Int8>, callAsFunction: JSObjectCallAsFunctionCallback!, attributes: JSPropertyAttributes)Removed JSStaticValue.init(name: UnsafePointer<Int8>, getProperty: JSObjectGetPropertyCallback!, setProperty: JSObjectSetPropertyCallback!, attributes: JSPropertyAttributes)Added [JSClassDefinition.init(version: Int32, attributes: JSClassAttributes, className: UnsafePointer<Int8>!, parentClass: JSClassRef!, staticValues: UnsafePointer<JSStaticValue>!, staticFunctions: UnsafePointer<JSStaticFunction>!, initialize: JavaScriptCore.JSObjectInitializeCallback!, finalize: JavaScriptCore.JSObjectFinalizeCallback!, hasProperty: JavaScriptCore.JSObjectHasPropertyCallback!, getProperty: JavaScriptCore.JSObjectGetPropertyCallback!, setProperty: JavaScriptCore.JSObjectSetPropertyCallback!, deleteProperty: JavaScriptCore.JSObjectDeletePropertyCallback!, getPropertyNames: JavaScriptCore.JSObjectGetPropertyNamesCallback!, callAsFunction: JavaScriptCore.JSObjectCallAsFunctionCallback!, callAsConstructor: JavaScriptCore.JSObjectCallAsConstructorCallback!, hasInstance: JavaScriptCore.JSObjectHasInstanceCallback!, convertToType: JavaScriptCore.JSObjectConvertToTypeCallback!)](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1779586-init)Added [JSStaticFunction.init(name: UnsafePointer<Int8>!, callAsFunction: JavaScriptCore.JSObjectCallAsFunctionCallback!, attributes: JSPropertyAttributes)](https://developer.apple.com/documentation/javascriptcore/jsstaticfunction/1779585-init)Added [JSStaticValue.init(name: UnsafePointer<Int8>!, getProperty: JavaScriptCore.JSObjectGetPropertyCallback!, setProperty: JavaScriptCore.JSObjectSetPropertyCallback!, attributes: JSPropertyAttributes)](https://developer.apple.com/documentation/javascriptcore/jsstaticvalue/1779584-init)Added [JSTypedArrayType [struct]](https://developer.apple.com/documentation/javascriptcore/jstypedarraytype)Added [JSTypedArrayType.init(_: UInt32)](https://developer.apple.com/documentation/javascriptcore/jstypedarraytype/1645837-init)Added [JSTypedArrayType.init(rawValue: UInt32)](https://developer.apple.com/documentation/javascriptcore/jstypedarraytype/1645838-init)Added [JSTypedArrayType.rawValue](https://developer.apple.com/documentation/javascriptcore/jstypedarraytype/1645836-rawvalue)Added [JSObjectGetArrayBufferByteLength(_: JSContextRef!, _: JSObjectRef!, _: UnsafeMutablePointer<JSValueRef?>!) -> Int](https://developer.apple.com/documentation/javascriptcore/1644609-jsobjectgetarraybufferbytelength)Added [JSObjectGetArrayBufferBytesPtr(_: JSContextRef!, _: JSObjectRef!, _: UnsafeMutablePointer<JSValueRef?>!) -> UnsafeMutableRawPointer!](https://developer.apple.com/documentation/javascriptcore/1644605-jsobjectgetarraybufferbytesptr)Added [JSObjectGetTypedArrayBuffer(_: JSContextRef!, _: JSObjectRef!, _: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](https://developer.apple.com/documentation/javascriptcore/1644604-jsobjectgettypedarraybuffer)Added [JSObjectGetTypedArrayByteLength(_: JSContextRef!, _: JSObjectRef!, _: UnsafeMutablePointer<JSValueRef?>!) -> Int](https://developer.apple.com/documentation/javascriptcore/1644600-jsobjectgettypedarraybytelength)Added [JSObjectGetTypedArrayByteOffset(_: JSContextRef!, _: JSObjectRef!, _: UnsafeMutablePointer<JSValueRef?>!) -> Int](https://developer.apple.com/documentation/javascriptcore/1644608-jsobjectgettypedarraybyteoffset)Added [JSObjectGetTypedArrayBytesPtr(_: JSContextRef!, _: JSObjectRef!, _: UnsafeMutablePointer<JSValueRef?>!) -> UnsafeMutableRawPointer!](https://developer.apple.com/documentation/javascriptcore/1644602-jsobjectgettypedarraybytesptr)Added [JSObjectGetTypedArrayLength(_: JSContextRef!, _: JSObjectRef!, _: UnsafeMutablePointer<JSValueRef?>!) -> Int](https://developer.apple.com/documentation/javascriptcore/1644601-jsobjectgettypedarraylength)Added [JSObjectMakeArrayBufferWithBytesNoCopy(_: JSContextRef!, _: UnsafeMutableRawPointer!, _: Int, _: JavaScriptCore.JSTypedArrayBytesDeallocator!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](https://developer.apple.com/documentation/javascriptcore/1644606-jsobjectmakearraybufferwithbytes)Added [JSObjectMakeTypedArray(_: JSContextRef!, _: JSTypedArrayType, _: Int, _: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](https://developer.apple.com/documentation/javascriptcore/1644597-jsobjectmaketypedarray)Added [JSObjectMakeTypedArrayWithArrayBuffer(_: JSContextRef!, _: JSTypedArrayType, _: JSObjectRef!, _: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](https://developer.apple.com/documentation/javascriptcore/1644598-jsobjectmaketypedarraywitharrayb)Added [JSObjectMakeTypedArrayWithArrayBufferAndOffset(_: JSContextRef!, _: JSTypedArrayType, _: JSObjectRef!, _: Int, _: Int, _: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](https://developer.apple.com/documentation/javascriptcore/1644599-jsobjectmaketypedarraywitharrayb)Added [JSObjectMakeTypedArrayWithBytesNoCopy(_: JSContextRef!, _: JSTypedArrayType, _: UnsafeMutableRawPointer!, _: Int, _: JavaScriptCore.JSTypedArrayBytesDeallocator!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](https://developer.apple.com/documentation/javascriptcore/1644607-jsobjectmaketypedarraywithbytesn)Added [JSTypedArrayBytesDeallocator](https://developer.apple.com/documentation/javascriptcore/jstypedarraybytesdeallocator)Added [JSValueGetTypedArrayType(_: JSContextRef!, _: JSValueRef!, _: UnsafeMutablePointer<JSValueRef?>!) -> JSTypedArrayType](https://developer.apple.com/documentation/javascriptcore/1644616-jsvaluegettypedarraytype)Added [kJSTypedArrayTypeArrayBuffer](https://developer.apple.com/documentation/javascriptcore/jstypedarraytype/kjstypedarraytypearraybuffer)Added [kJSTypedArrayTypeFloat32Array](https://developer.apple.com/documentation/javascriptcore/kjstypedarraytypefloat32array)Added [kJSTypedArrayTypeFloat64Array](https://developer.apple.com/documentation/javascriptcore/kjstypedarraytypefloat64array)Added [kJSTypedArrayTypeInt16Array](https://developer.apple.com/documentation/javascriptcore/kjstypedarraytypeint16array)Added [kJSTypedArrayTypeInt32Array](https://developer.apple.com/documentation/javascriptcore/jstypedarraytype/kjstypedarraytypeint32array)Added [kJSTypedArrayTypeInt8Array](https://developer.apple.com/documentation/javascriptcore/kjstypedarraytypeint8array)Added [kJSTypedArrayTypeNone](https://developer.apple.com/documentation/javascriptcore/jstypedarraytype/kjstypedarraytypenone)Added [kJSTypedArrayTypeUint16Array](https://developer.apple.com/documentation/javascriptcore/kjstypedarraytypeuint16array)Added [kJSTypedArrayTypeUint32Array](https://developer.apple.com/documentation/javascriptcore/kjstypedarraytypeuint32array)Added [kJSTypedArrayTypeUint8Array](https://developer.apple.com/documentation/javascriptcore/kjstypedarraytypeuint8array)Added [kJSTypedArrayTypeUint8ClampedArray](https://developer.apple.com/documentation/javascriptcore/jstypedarraytype/kjstypedarraytypeuint8clampedarray)Modified [JSClassDefinition [struct]](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition)

|  | Declaration |
| --- | --- |
| From | ``` struct JSClassDefinition {     var version: Int32     var attributes: JSClassAttributes     var className: UnsafePointer<Int8>     var parentClass: JSClassRef     var staticValues: UnsafePointer<JSStaticValue>     var staticFunctions: UnsafePointer<JSStaticFunction>     var initialize: JSObjectInitializeCallback!     var finalize: JSObjectFinalizeCallback!     var hasProperty: JSObjectHasPropertyCallback!     var getProperty: JSObjectGetPropertyCallback!     var setProperty: JSObjectSetPropertyCallback!     var deleteProperty: JSObjectDeletePropertyCallback!     var getPropertyNames: JSObjectGetPropertyNamesCallback!     var callAsFunction: JSObjectCallAsFunctionCallback!     var callAsConstructor: JSObjectCallAsConstructorCallback!     var hasInstance: JSObjectHasInstanceCallback!     var convertToType: JSObjectConvertToTypeCallback!     init()     init(version version: Int32, attributes attributes: JSClassAttributes, className className: UnsafePointer<Int8>, parentClass parentClass: JSClassRef, staticValues staticValues: UnsafePointer<JSStaticValue>, staticFunctions staticFunctions: UnsafePointer<JSStaticFunction>, initialize initialize: JSObjectInitializeCallback!, finalize finalize: JSObjectFinalizeCallback!, hasProperty hasProperty: JSObjectHasPropertyCallback!, getProperty getProperty: JSObjectGetPropertyCallback!, setProperty setProperty: JSObjectSetPropertyCallback!, deleteProperty deleteProperty: JSObjectDeletePropertyCallback!, getPropertyNames getPropertyNames: JSObjectGetPropertyNamesCallback!, callAsFunction callAsFunction: JSObjectCallAsFunctionCallback!, callAsConstructor callAsConstructor: JSObjectCallAsConstructorCallback!, hasInstance hasInstance: JSObjectHasInstanceCallback!, convertToType convertToType: JSObjectConvertToTypeCallback!) } ``` |
| To | ``` struct JSClassDefinition {     var version: Int32     var attributes: JSClassAttributes     var className: UnsafePointer<Int8>!     var parentClass: JSClassRef!     var staticValues: UnsafePointer<JSStaticValue>!     var staticFunctions: UnsafePointer<JSStaticFunction>!     var initialize: JavaScriptCore.JSObjectInitializeCallback!     var finalize: JavaScriptCore.JSObjectFinalizeCallback!     var hasProperty: JavaScriptCore.JSObjectHasPropertyCallback!     var getProperty: JavaScriptCore.JSObjectGetPropertyCallback!     var setProperty: JavaScriptCore.JSObjectSetPropertyCallback!     var deleteProperty: JavaScriptCore.JSObjectDeletePropertyCallback!     var getPropertyNames: JavaScriptCore.JSObjectGetPropertyNamesCallback!     var callAsFunction: JavaScriptCore.JSObjectCallAsFunctionCallback!     var callAsConstructor: JavaScriptCore.JSObjectCallAsConstructorCallback!     var hasInstance: JavaScriptCore.JSObjectHasInstanceCallback!     var convertToType: JavaScriptCore.JSObjectConvertToTypeCallback!     init()     init(version version: Int32, attributes attributes: JSClassAttributes, className className: UnsafePointer<Int8>!, parentClass parentClass: JSClassRef!, staticValues staticValues: UnsafePointer<JSStaticValue>!, staticFunctions staticFunctions: UnsafePointer<JSStaticFunction>!, initialize initialize: JavaScriptCore.JSObjectInitializeCallback!, finalize finalize: JavaScriptCore.JSObjectFinalizeCallback!, hasProperty hasProperty: JavaScriptCore.JSObjectHasPropertyCallback!, getProperty getProperty: JavaScriptCore.JSObjectGetPropertyCallback!, setProperty setProperty: JavaScriptCore.JSObjectSetPropertyCallback!, deleteProperty deleteProperty: JavaScriptCore.JSObjectDeletePropertyCallback!, getPropertyNames getPropertyNames: JavaScriptCore.JSObjectGetPropertyNamesCallback!, callAsFunction callAsFunction: JavaScriptCore.JSObjectCallAsFunctionCallback!, callAsConstructor callAsConstructor: JavaScriptCore.JSObjectCallAsConstructorCallback!, hasInstance hasInstance: JavaScriptCore.JSObjectHasInstanceCallback!, convertToType convertToType: JavaScriptCore.JSObjectConvertToTypeCallback!) } ``` |

Modified [JSClassDefinition.callAsConstructor](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451577-callasconstructor)

|  | Declaration |
| --- | --- |
| From | ``` var callAsConstructor: JSObjectCallAsConstructorCallback! ``` |
| To | ``` var callAsConstructor: JavaScriptCore.JSObjectCallAsConstructorCallback! ``` |

Modified [JSClassDefinition.callAsFunction](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451450-callasfunction)

|  | Declaration |
| --- | --- |
| From | ``` var callAsFunction: JSObjectCallAsFunctionCallback! ``` |
| To | ``` var callAsFunction: JavaScriptCore.JSObjectCallAsFunctionCallback! ``` |

Modified [JSClassDefinition.className](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451709-classname)

|  | Declaration |
| --- | --- |
| From | ``` var className: UnsafePointer<Int8> ``` |
| To | ``` var className: UnsafePointer<Int8>! ``` |

Modified [JSClassDefinition.convertToType](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451772-converttotype)

|  | Declaration |
| --- | --- |
| From | ``` var convertToType: JSObjectConvertToTypeCallback! ``` |
| To | ``` var convertToType: JavaScriptCore.JSObjectConvertToTypeCallback! ``` |

Modified [JSClassDefinition.deleteProperty](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451506-deleteproperty)

|  | Declaration |
| --- | --- |
| From | ``` var deleteProperty: JSObjectDeletePropertyCallback! ``` |
| To | ``` var deleteProperty: JavaScriptCore.JSObjectDeletePropertyCallback! ``` |

Modified [JSClassDefinition.finalize](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451680-finalize)

|  | Declaration |
| --- | --- |
| From | ``` var finalize: JSObjectFinalizeCallback! ``` |
| To | ``` var finalize: JavaScriptCore.JSObjectFinalizeCallback! ``` |

Modified [JSClassDefinition.getProperty](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451740-getproperty)

|  | Declaration |
| --- | --- |
| From | ``` var getProperty: JSObjectGetPropertyCallback! ``` |
| To | ``` var getProperty: JavaScriptCore.JSObjectGetPropertyCallback! ``` |

Modified [JSClassDefinition.getPropertyNames](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451611-getpropertynames)

|  | Declaration |
| --- | --- |
| From | ``` var getPropertyNames: JSObjectGetPropertyNamesCallback! ``` |
| To | ``` var getPropertyNames: JavaScriptCore.JSObjectGetPropertyNamesCallback! ``` |

Modified [JSClassDefinition.hasInstance](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451413-hasinstance)

|  | Declaration |
| --- | --- |
| From | ``` var hasInstance: JSObjectHasInstanceCallback! ``` |
| To | ``` var hasInstance: JavaScriptCore.JSObjectHasInstanceCallback! ``` |

Modified [JSClassDefinition.hasProperty](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451425-hasproperty)

|  | Declaration |
| --- | --- |
| From | ``` var hasProperty: JSObjectHasPropertyCallback! ``` |
| To | ``` var hasProperty: JavaScriptCore.JSObjectHasPropertyCallback! ``` |

Modified [JSClassDefinition.initialize](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451397-initialize)

|  | Declaration |
| --- | --- |
| From | ``` var initialize: JSObjectInitializeCallback! ``` |
| To | ``` var initialize: JavaScriptCore.JSObjectInitializeCallback! ``` |

Modified [JSClassDefinition.parentClass](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451741-parentclass)

|  | Declaration |
| --- | --- |
| From | ``` var parentClass: JSClassRef ``` |
| To | ``` var parentClass: JSClassRef! ``` |

Modified [JSClassDefinition.setProperty](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451705-setproperty)

|  | Declaration |
| --- | --- |
| From | ``` var setProperty: JSObjectSetPropertyCallback! ``` |
| To | ``` var setProperty: JavaScriptCore.JSObjectSetPropertyCallback! ``` |

Modified [JSClassDefinition.staticFunctions](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451685-staticfunctions)

|  | Declaration |
| --- | --- |
| From | ``` var staticFunctions: UnsafePointer<JSStaticFunction> ``` |
| To | ``` var staticFunctions: UnsafePointer<JSStaticFunction>! ``` |

Modified [JSClassDefinition.staticValues](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451484-staticvalues)

|  | Declaration |
| --- | --- |
| From | ``` var staticValues: UnsafePointer<JSStaticValue> ``` |
| To | ``` var staticValues: UnsafePointer<JSStaticValue>! ``` |

Modified [JSContext](https://developer.apple.com/documentation/javascriptcore/jscontext)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class JSContext : NSObject {     init!()     init!(virtualMachine virtualMachine: JSVirtualMachine!)     func evaluateScript(_ script: String!) -> JSValue!     func evaluateScript(_ script: String!, withSourceURL sourceURL: NSURL!) -> JSValue!     class func currentContext() -> JSContext!     class func currentCallee() -> JSValue!     class func currentThis() -> JSValue!     class func currentArguments() -> [AnyObject]!     var globalObject: JSValue! { get }     var exception: JSValue!     var exceptionHandler: ((JSContext!, JSValue!) -> Void)!     var virtualMachine: JSVirtualMachine! { get }     var name: String! } extension JSContext {     func objectForKeyedSubscript(_ key: AnyObject!) -> JSValue!     func setObject(_ object: AnyObject!, forKeyedSubscript key: protocol<NSCopying, NSObjectProtocol>!) } extension JSContext {      init!(JSGlobalContextRef jsGlobalContextRef: JSGlobalContextRef)     class func contextWithJSGlobalContextRef(_ jsGlobalContextRef: JSGlobalContextRef) -> JSContext!     var JSGlobalContextRef: JSGlobalContextRef { get } } ``` | -- |
| To | ``` class JSContext : NSObject {     init!()     init!(virtualMachine virtualMachine: JSVirtualMachine!)     func evaluateScript(_ script: String!) -> JSValue!     func evaluateScript(_ script: String!, withSourceURL sourceURL: URL!) -> JSValue!     class func current() -> JSContext!     class func currentCallee() -> JSValue!     class func currentThis() -> JSValue!     class func currentArguments() -> [Any]!     var globalObject: JSValue! { get }     var exception: JSValue!     var exceptionHandler: ((JSContext?, JSValue?) -> Swift.Void)!     var virtualMachine: JSVirtualMachine! { get }     var name: String!      init!(jsGlobalContextRef jsGlobalContextRef: JSGlobalContextRef!)     class func withJSGlobalContextRef(_ jsGlobalContextRef: JSGlobalContextRef!) -> JSContext!     var jsGlobalContextRef: JSGlobalContextRef! { get }     func objectForKeyedSubscript(_ key: Any!) -> JSValue!     func setObject(_ object: Any!, forKeyedSubscript key: (NSCopying & NSObjectProtocol)!)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension JSContext : CVarArg { } extension JSContext : Equatable, Hashable {     var hashValue: Int { get } } extension JSContext {     func objectForKeyedSubscript(_ key: Any!) -> JSValue!     func setObject(_ object: Any!, forKeyedSubscript key: (NSCopying & NSObjectProtocol)!) } extension JSContext {      init!(jsGlobalContextRef jsGlobalContextRef: JSGlobalContextRef!)     class func withJSGlobalContextRef(_ jsGlobalContextRef: JSGlobalContextRef!) -> JSContext!     var jsGlobalContextRef: JSGlobalContextRef! { get } } ``` | CVarArg, Equatable, Hashable |

Modified [JSContext.current() -> JSContext! [class]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451545-currentcontext)

|  | Declaration |
| --- | --- |
| From | ``` class func currentContext() -> JSContext! ``` |
| To | ``` class func current() -> JSContext! ``` |

Modified [JSContext.currentArguments() -> [Any]! [class]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451650-currentarguments)

|  | Declaration |
| --- | --- |
| From | ``` class func currentArguments() -> [AnyObject]! ``` |
| To | ``` class func currentArguments() -> [Any]! ``` |

Modified [JSContext.evaluateScript(_: String!, withSourceURL: URL!) -> JSValue!](https://developer.apple.com/documentation/javascriptcore/jscontext/1451384-evaluatescript)

|  | Declaration |
| --- | --- |
| From | ``` func evaluateScript(_ script: String!, withSourceURL sourceURL: NSURL!) -> JSValue! ``` |
| To | ``` func evaluateScript(_ script: String!, withSourceURL sourceURL: URL!) -> JSValue! ``` |

Modified [JSContext.exceptionHandler](https://developer.apple.com/documentation/javascriptcore/jscontext/1451731-exceptionhandler)

|  | Declaration |
| --- | --- |
| From | ``` var exceptionHandler: ((JSContext!, JSValue!) -> Void)! ``` |
| To | ``` var exceptionHandler: ((JSContext?, JSValue?) -> Swift.Void)! ``` |

Modified [JSContext.init(jsGlobalContextRef: JSGlobalContextRef!)](https://developer.apple.com/documentation/javascriptcore/jscontext/1451491-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(JSGlobalContextRef jsGlobalContextRef: JSGlobalContextRef) ``` |
| To | ``` init!(jsGlobalContextRef jsGlobalContextRef: JSGlobalContextRef!) ``` |

Modified [JSContext.jsGlobalContextRef](https://developer.apple.com/documentation/javascriptcore/jscontext/1451338-jsglobalcontextref)

|  | Declaration |
| --- | --- |
| From | ``` var JSGlobalContextRef: JSGlobalContextRef { get } ``` |
| To | ``` var jsGlobalContextRef: JSGlobalContextRef! { get } ``` |

Modified [JSContext.objectForKeyedSubscript(_: Any!) -> JSValue!](https://developer.apple.com/documentation/javascriptcore/jscontext/1451771-objectforkeyedsubscript)

|  | Declaration |
| --- | --- |
| From | ``` func objectForKeyedSubscript(_ key: AnyObject!) -> JSValue! ``` |
| To | ``` func objectForKeyedSubscript(_ key: Any!) -> JSValue! ``` |

Modified [JSContext.setObject(_: Any!, forKeyedSubscript: (NSCopying & NSObjectProtocol)!)](https://developer.apple.com/documentation/javascriptcore/jscontext/1451416-setobject)

|  | Declaration |
| --- | --- |
| From | ``` func setObject(_ object: AnyObject!, forKeyedSubscript key: protocol<NSCopying, NSObjectProtocol>!) ``` |
| To | ``` func setObject(_ object: Any!, forKeyedSubscript key: (NSCopying & NSObjectProtocol)!) ``` |

Modified [JSManagedValue](https://developer.apple.com/documentation/javascriptcore/jsmanagedvalue)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class JSManagedValue : NSObject {      init!(value value: JSValue!)     class func managedValueWithValue(_ value: JSValue!) -> JSManagedValue!      init!(value value: JSValue!, andOwner owner: AnyObject!)     class func managedValueWithValue(_ value: JSValue!, andOwner owner: AnyObject!) -> JSManagedValue!     init!(value value: JSValue!)     var value: JSValue! { get } } ``` | -- |
| To | ``` class JSManagedValue : NSObject {      init!(value value: JSValue!)     class func withValue(_ value: JSValue!) -> JSManagedValue!      init!(value value: JSValue!, andOwner owner: Any!)     class func withValue(_ value: JSValue!, andOwner owner: Any!) -> JSManagedValue!     init!(value value: JSValue!)     var value: JSValue! { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension JSManagedValue : CVarArg { } extension JSManagedValue : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [JSManagedValue.init(value: JSValue!, andOwner: Any!)](https://developer.apple.com/documentation/javascriptcore/jsmanagedvalue/1451607-managedvaluewithvalue)

|  | Declaration |
| --- | --- |
| From | ``` init!(value value: JSValue!, andOwner owner: AnyObject!) ``` |
| To | ``` init!(value value: JSValue!, andOwner owner: Any!) ``` |

Modified [JSStaticFunction [struct]](https://developer.apple.com/documentation/javascriptcore/jsstaticfunction)

|  | Declaration |
| --- | --- |
| From | ``` struct JSStaticFunction {     var name: UnsafePointer<Int8>     var callAsFunction: JSObjectCallAsFunctionCallback!     var attributes: JSPropertyAttributes     init()     init(name name: UnsafePointer<Int8>, callAsFunction callAsFunction: JSObjectCallAsFunctionCallback!, attributes attributes: JSPropertyAttributes) } ``` |
| To | ``` struct JSStaticFunction {     var name: UnsafePointer<Int8>!     var callAsFunction: JavaScriptCore.JSObjectCallAsFunctionCallback!     var attributes: JSPropertyAttributes     init()     init(name name: UnsafePointer<Int8>!, callAsFunction callAsFunction: JavaScriptCore.JSObjectCallAsFunctionCallback!, attributes attributes: JSPropertyAttributes) } ``` |

Modified [JSStaticFunction.callAsFunction](https://developer.apple.com/documentation/javascriptcore/jsstaticfunction/1451749-callasfunction)

|  | Declaration |
| --- | --- |
| From | ``` var callAsFunction: JSObjectCallAsFunctionCallback! ``` |
| To | ``` var callAsFunction: JavaScriptCore.JSObjectCallAsFunctionCallback! ``` |

Modified [JSStaticFunction.name](https://developer.apple.com/documentation/javascriptcore/jsstaticfunction/1451657-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: UnsafePointer<Int8> ``` |
| To | ``` var name: UnsafePointer<Int8>! ``` |

Modified [JSStaticValue [struct]](https://developer.apple.com/documentation/javascriptcore/jsstaticvalue)

|  | Declaration |
| --- | --- |
| From | ``` struct JSStaticValue {     var name: UnsafePointer<Int8>     var getProperty: JSObjectGetPropertyCallback!     var setProperty: JSObjectSetPropertyCallback!     var attributes: JSPropertyAttributes     init()     init(name name: UnsafePointer<Int8>, getProperty getProperty: JSObjectGetPropertyCallback!, setProperty setProperty: JSObjectSetPropertyCallback!, attributes attributes: JSPropertyAttributes) } ``` |
| To | ``` struct JSStaticValue {     var name: UnsafePointer<Int8>!     var getProperty: JavaScriptCore.JSObjectGetPropertyCallback!     var setProperty: JavaScriptCore.JSObjectSetPropertyCallback!     var attributes: JSPropertyAttributes     init()     init(name name: UnsafePointer<Int8>!, getProperty getProperty: JavaScriptCore.JSObjectGetPropertyCallback!, setProperty setProperty: JavaScriptCore.JSObjectSetPropertyCallback!, attributes attributes: JSPropertyAttributes) } ``` |

Modified [JSStaticValue.getProperty](https://developer.apple.com/documentation/javascriptcore/jsstaticvalue/1451527-getproperty)

|  | Declaration |
| --- | --- |
| From | ``` var getProperty: JSObjectGetPropertyCallback! ``` |
| To | ``` var getProperty: JavaScriptCore.JSObjectGetPropertyCallback! ``` |

Modified [JSStaticValue.name](https://developer.apple.com/documentation/javascriptcore/jsstaticvalue/1451701-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: UnsafePointer<Int8> ``` |
| To | ``` var name: UnsafePointer<Int8>! ``` |

Modified [JSStaticValue.setProperty](https://developer.apple.com/documentation/javascriptcore/jsstaticvalue/1451455-setproperty)

|  | Declaration |
| --- | --- |
| From | ``` var setProperty: JSObjectSetPropertyCallback! ``` |
| To | ``` var setProperty: JavaScriptCore.JSObjectSetPropertyCallback! ``` |

Modified [JSValue](https://developer.apple.com/documentation/javascriptcore/jsvalue)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class JSValue : NSObject {     var context: JSContext! { get }      init!(object value: AnyObject!, inContext context: JSContext!)     class func valueWithObject(_ value: AnyObject!, inContext context: JSContext!) -> JSValue!      init!(bool value: Bool, inContext context: JSContext!)     class func valueWithBool(_ value: Bool, inContext context: JSContext!) -> JSValue!      init!(double value: Double, inContext context: JSContext!)     class func valueWithDouble(_ value: Double, inContext context: JSContext!) -> JSValue!      init!(int32 value: Int32, inContext context: JSContext!)     class func valueWithInt32(_ value: Int32, inContext context: JSContext!) -> JSValue!      init!(UInt32 value: UInt32, inContext context: JSContext!)     class func valueWithUInt32(_ value: UInt32, inContext context: JSContext!) -> JSValue!      init!(newObjectInContext context: JSContext!)     class func valueWithNewObjectInContext(_ context: JSContext!) -> JSValue!      init!(newArrayInContext context: JSContext!)     class func valueWithNewArrayInContext(_ context: JSContext!) -> JSValue!      init!(newRegularExpressionFromPattern pattern: String!, flags flags: String!, inContext context: JSContext!)     class func valueWithNewRegularExpressionFromPattern(_ pattern: String!, flags flags: String!, inContext context: JSContext!) -> JSValue!      init!(newErrorFromMessage message: String!, inContext context: JSContext!)     class func valueWithNewErrorFromMessage(_ message: String!, inContext context: JSContext!) -> JSValue!      init!(nullInContext context: JSContext!)     class func valueWithNullInContext(_ context: JSContext!) -> JSValue!      init!(undefinedInContext context: JSContext!)     class func valueWithUndefinedInContext(_ context: JSContext!) -> JSValue!     func toObject() -> AnyObject!     func toObjectOfClass(_ expectedClass: AnyClass!) -> AnyObject!     func toBool() -> Bool     func toDouble() -> Double     func toInt32() -> Int32     func toUInt32() -> UInt32     func toNumber() -> NSNumber!     func toString() -> String!     func toDate() -> NSDate!     func toArray() -> [AnyObject]!     func toDictionary() -> [NSObject : AnyObject]!     func valueForProperty(_ property: String!) -> JSValue!     func setValue(_ value: AnyObject!, forProperty property: String!)     func deleteProperty(_ property: String!) -> Bool     func hasProperty(_ property: String!) -> Bool     func defineProperty(_ property: String!, descriptor descriptor: AnyObject!)     func valueAtIndex(_ index: Int) -> JSValue!     func setValue(_ value: AnyObject!, atIndex index: Int)     var isUndefined: Bool { get }     var isNull: Bool { get }     var isBoolean: Bool { get }     var isNumber: Bool { get }     var isString: Bool { get }     var isObject: Bool { get }     var isArray: Bool { get }     var isDate: Bool { get }     func isEqualToObject(_ value: AnyObject!) -> Bool     func isEqualWithTypeCoercionToObject(_ value: AnyObject!) -> Bool     func isInstanceOf(_ value: AnyObject!) -> Bool     func callWithArguments(_ arguments: [AnyObject]!) -> JSValue!     func constructWithArguments(_ arguments: [AnyObject]!) -> JSValue!     func invokeMethod(_ method: String!, withArguments arguments: [AnyObject]!) -> JSValue! } extension JSValue {      init!(point point: CGPoint, inContext context: JSContext!)     class func valueWithPoint(_ point: CGPoint, inContext context: JSContext!) -> JSValue!      init!(range range: NSRange, inContext context: JSContext!)     class func valueWithRange(_ range: NSRange, inContext context: JSContext!) -> JSValue!      init!(rect rect: CGRect, inContext context: JSContext!)     class func valueWithRect(_ rect: CGRect, inContext context: JSContext!) -> JSValue!      init!(size size: CGSize, inContext context: JSContext!)     class func valueWithSize(_ size: CGSize, inContext context: JSContext!) -> JSValue!     func toPoint() -> CGPoint     func toRange() -> NSRange     func toRect() -> CGRect     func toSize() -> CGSize } extension JSValue {     func objectForKeyedSubscript(_ key: AnyObject!) -> JSValue!     func objectAtIndexedSubscript(_ index: Int) -> JSValue!     func setObject(_ object: AnyObject!, forKeyedSubscript key: protocol<NSCopying, NSObjectProtocol>!)     func setObject(_ object: AnyObject!, atIndexedSubscript index: Int) } extension JSValue {      init!(JSValueRef value: JSValueRef, inContext context: JSContext!)     class func valueWithJSValueRef(_ value: JSValueRef, inContext context: JSContext!) -> JSValue!     var JSValueRef: JSValueRef { get } } ``` | -- |
| To | ``` class JSValue : NSObject {     var context: JSContext! { get }      init!(object value: Any!, in context: JSContext!)     class func withObject(_ value: Any!, in context: JSContext!) -> JSValue!      init!(bool value: Bool, in context: JSContext!)     class func withBool(_ value: Bool, in context: JSContext!) -> JSValue!      init!(double value: Double, in context: JSContext!)     class func withDouble(_ value: Double, in context: JSContext!) -> JSValue!      init!(int32 value: Int32, in context: JSContext!)     class func withInt32(_ value: Int32, in context: JSContext!) -> JSValue!      init!(uInt32 value: UInt32, in context: JSContext!)     class func withUInt32(_ value: UInt32, in context: JSContext!) -> JSValue!      init!(newObjectIn context: JSContext!)     class func withNewObject(in context: JSContext!) -> JSValue!      init!(newArrayIn context: JSContext!)     class func withNewArray(in context: JSContext!) -> JSValue!      init!(newRegularExpressionFromPattern pattern: String!, flags flags: String!, in context: JSContext!)     class func withNewRegularExpression(fromPattern pattern: String!, flags flags: String!, in context: JSContext!) -> JSValue!      init!(newErrorFromMessage message: String!, in context: JSContext!)     class func withNewError(fromMessage message: String!, in context: JSContext!) -> JSValue!      init!(nullIn context: JSContext!)     class func withNullIn(_ context: JSContext!) -> JSValue!      init!(undefinedIn context: JSContext!)     class func withUndefinedIn(_ context: JSContext!) -> JSValue!     func toObject() -> Any!     func toObjectOf(_ expectedClass: Swift.AnyClass!) -> Any!     func toBool() -> Bool     func toDouble() -> Double     func toInt32() -> Int32     func toUInt32() -> UInt32     func toNumber() -> NSNumber!     func toString() -> String!     func toDate() -> Date!     func toArray() -> [Any]!     func toDictionary() -> [AnyHashable : Any]!     func forProperty(_ property: String!) -> JSValue!     func setValue(_ value: Any!, forProperty property: String!)     func deleteProperty(_ property: String!) -> Bool     func hasProperty(_ property: String!) -> Bool     func defineProperty(_ property: String!, descriptor descriptor: Any!)     func atIndex(_ index: Int) -> JSValue!     func setValue(_ value: Any!, at index: Int)     var isUndefined: Bool { get }     var isNull: Bool { get }     var isBoolean: Bool { get }     var isNumber: Bool { get }     var isString: Bool { get }     var isObject: Bool { get }     var isArray: Bool { get }     var isDate: Bool { get }     func isEqual(to value: Any!) -> Bool     func isEqualWithTypeCoercion(to value: Any!) -> Bool     func isInstance(of value: Any!) -> Bool     func call(withArguments arguments: [Any]!) -> JSValue!     func construct(withArguments arguments: [Any]!) -> JSValue!     func invokeMethod(_ method: String!, withArguments arguments: [Any]!) -> JSValue!      init!(jsValueRef value: JSValueRef!, in context: JSContext!)     class func withJSValueRef(_ value: JSValueRef!, in context: JSContext!) -> JSValue!     var jsValueRef: JSValueRef! { get }     func objectForKeyedSubscript(_ key: Any!) -> JSValue!     func objectAtIndexedSubscript(_ index: Int) -> JSValue!     func setObject(_ object: Any!, forKeyedSubscript key: (NSCopying & NSObjectProtocol)!)     func setObject(_ object: Any!, atIndexedSubscript index: Int)      init!(point point: CGPoint, in context: JSContext!)     class func withPoint(_ point: CGPoint, in context: JSContext!) -> JSValue!      init!(range range: NSRange, in context: JSContext!)     class func withRange(_ range: NSRange, in context: JSContext!) -> JSValue!      init!(rect rect: CGRect, in context: JSContext!)     class func withRect(_ rect: CGRect, in context: JSContext!) -> JSValue!      init!(size size: CGSize, in context: JSContext!)     class func withSize(_ size: CGSize, in context: JSContext!) -> JSValue!     func toPoint() -> CGPoint     func toRange() -> NSRange     func toRect() -> CGRect     func toSize() -> CGSize     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension JSValue : CVarArg { } extension JSValue : Equatable, Hashable {     var hashValue: Int { get } } extension JSValue {      init!(point point: CGPoint, in context: JSContext!)     class func withPoint(_ point: CGPoint, in context: JSContext!) -> JSValue!      init!(range range: NSRange, in context: JSContext!)     class func withRange(_ range: NSRange, in context: JSContext!) -> JSValue!      init!(rect rect: CGRect, in context: JSContext!)     class func withRect(_ rect: CGRect, in context: JSContext!) -> JSValue!      init!(size size: CGSize, in context: JSContext!)     class func withSize(_ size: CGSize, in context: JSContext!) -> JSValue!     func toPoint() -> CGPoint     func toRange() -> NSRange     func toRect() -> CGRect     func toSize() -> CGSize } extension JSValue {     func objectForKeyedSubscript(_ key: Any!) -> JSValue!     func objectAtIndexedSubscript(_ index: Int) -> JSValue!     func setObject(_ object: Any!, forKeyedSubscript key: (NSCopying & NSObjectProtocol)!)     func setObject(_ object: Any!, atIndexedSubscript index: Int) } extension JSValue {      init!(jsValueRef value: JSValueRef!, in context: JSContext!)     class func withJSValueRef(_ value: JSValueRef!, in context: JSContext!) -> JSValue!     var jsValueRef: JSValueRef! { get } } ``` | CVarArg, Equatable, Hashable |

Modified [JSValue.atIndex(_: Int) -> JSValue!](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451602-atindex)

|  | Declaration |
| --- | --- |
| From | ``` func valueAtIndex(_ index: Int) -> JSValue! ``` |
| To | ``` func atIndex(_ index: Int) -> JSValue! ``` |

Modified [JSValue.call(withArguments: [Any]!) -> JSValue!](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451648-call)

|  | Declaration |
| --- | --- |
| From | ``` func callWithArguments(_ arguments: [AnyObject]!) -> JSValue! ``` |
| To | ``` func call(withArguments arguments: [Any]!) -> JSValue! ``` |

Modified [JSValue.construct(withArguments: [Any]!) -> JSValue!](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451480-constructwitharguments)

|  | Declaration |
| --- | --- |
| From | ``` func constructWithArguments(_ arguments: [AnyObject]!) -> JSValue! ``` |
| To | ``` func construct(withArguments arguments: [Any]!) -> JSValue! ``` |

Modified [JSValue.defineProperty(_: String!, descriptor: Any!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451542-defineproperty)

|  | Declaration |
| --- | --- |
| From | ``` func defineProperty(_ property: String!, descriptor descriptor: AnyObject!) ``` |
| To | ``` func defineProperty(_ property: String!, descriptor descriptor: Any!) ``` |

Modified [JSValue.forProperty(_: String!) -> JSValue!](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451438-forproperty)

|  | Declaration |
| --- | --- |
| From | ``` func valueForProperty(_ property: String!) -> JSValue! ``` |
| To | ``` func forProperty(_ property: String!) -> JSValue! ``` |

Modified [JSValue.init(bool: Bool, in: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451616-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(bool value: Bool, inContext context: JSContext!) ``` |
| To | ``` init!(bool value: Bool, in context: JSContext!) ``` |

Modified [JSValue.init(double: Double, in: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451482-valuewithdouble)

|  | Declaration |
| --- | --- |
| From | ``` init!(double value: Double, inContext context: JSContext!) ``` |
| To | ``` init!(double value: Double, in context: JSContext!) ``` |

Modified [JSValue.init(int32: Int32, in: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451434-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(int32 value: Int32, inContext context: JSContext!) ``` |
| To | ``` init!(int32 value: Int32, in context: JSContext!) ``` |

Modified [JSValue.init(jsValueRef: JSValueRef!, in: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451641-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(JSValueRef value: JSValueRef, inContext context: JSContext!) ``` |
| To | ``` init!(jsValueRef value: JSValueRef!, in context: JSContext!) ``` |

Modified [JSValue.init(newArrayIn: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451473-valuewithnewarrayincontext)

|  | Declaration |
| --- | --- |
| From | ``` init!(newArrayInContext context: JSContext!) ``` |
| To | ``` init!(newArrayIn context: JSContext!) ``` |

Modified [JSValue.init(newErrorFromMessage: String!, in: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451630-valuewithnewerrorfrommessage)

|  | Declaration |
| --- | --- |
| From | ``` init!(newErrorFromMessage message: String!, inContext context: JSContext!) ``` |
| To | ``` init!(newErrorFromMessage message: String!, in context: JSContext!) ``` |

Modified [JSValue.init(newObjectIn: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451751-valuewithnewobjectincontext)

|  | Declaration |
| --- | --- |
| From | ``` init!(newObjectInContext context: JSContext!) ``` |
| To | ``` init!(newObjectIn context: JSContext!) ``` |

Modified [JSValue.init(newRegularExpressionFromPattern: String!, flags: String!, in: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451539-valuewithnewregularexpressionfro)

|  | Declaration |
| --- | --- |
| From | ``` init!(newRegularExpressionFromPattern pattern: String!, flags flags: String!, inContext context: JSContext!) ``` |
| To | ``` init!(newRegularExpressionFromPattern pattern: String!, flags flags: String!, in context: JSContext!) ``` |

Modified [JSValue.init(nullIn: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451463-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(nullInContext context: JSContext!) ``` |
| To | ``` init!(nullIn context: JSContext!) ``` |

Modified [JSValue.init(object: Any!, in: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451694-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(object value: AnyObject!, inContext context: JSContext!) ``` |
| To | ``` init!(object value: Any!, in context: JSContext!) ``` |

Modified [JSValue.init(point: CGPoint, in: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451382-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(point point: CGPoint, inContext context: JSContext!) ``` |
| To | ``` init!(point point: CGPoint, in context: JSContext!) ``` |

Modified [JSValue.init(range: NSRange, in: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451628-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(range range: NSRange, inContext context: JSContext!) ``` |
| To | ``` init!(range range: NSRange, in context: JSContext!) ``` |

Modified [JSValue.init(rect: CGRect, in: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451664-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(rect rect: CGRect, inContext context: JSContext!) ``` |
| To | ``` init!(rect rect: CGRect, in context: JSContext!) ``` |

Modified [JSValue.init(size: CGSize, in: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451715-valuewithsize)

|  | Declaration |
| --- | --- |
| From | ``` init!(size size: CGSize, inContext context: JSContext!) ``` |
| To | ``` init!(size size: CGSize, in context: JSContext!) ``` |

Modified [JSValue.init(uInt32: UInt32, in: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451402-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(UInt32 value: UInt32, inContext context: JSContext!) ``` |
| To | ``` init!(uInt32 value: UInt32, in context: JSContext!) ``` |

Modified [JSValue.init(undefinedIn: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451387-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(undefinedInContext context: JSContext!) ``` |
| To | ``` init!(undefinedIn context: JSContext!) ``` |

Modified [JSValue.invokeMethod(_: String!, withArguments: [Any]!) -> JSValue!](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451666-invokemethod)

|  | Declaration |
| --- | --- |
| From | ``` func invokeMethod(_ method: String!, withArguments arguments: [AnyObject]!) -> JSValue! ``` |
| To | ``` func invokeMethod(_ method: String!, withArguments arguments: [Any]!) -> JSValue! ``` |

Modified [JSValue.isEqual(to: Any!) -> Bool](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451504-isequal)

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToObject(_ value: AnyObject!) -> Bool ``` |
| To | ``` func isEqual(to value: Any!) -> Bool ``` |

Modified [JSValue.isEqualWithTypeCoercion(to: Any!) -> Bool](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451765-isequalwithtypecoercion)

|  | Declaration |
| --- | --- |
| From | ``` func isEqualWithTypeCoercionToObject(_ value: AnyObject!) -> Bool ``` |
| To | ``` func isEqualWithTypeCoercion(to value: Any!) -> Bool ``` |

Modified [JSValue.isInstance(of: Any!) -> Bool](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451691-isinstanceof)

|  | Declaration |
| --- | --- |
| From | ``` func isInstanceOf(_ value: AnyObject!) -> Bool ``` |
| To | ``` func isInstance(of value: Any!) -> Bool ``` |

Modified [JSValue.jsValueRef](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451639-jsvalueref)

|  | Declaration |
| --- | --- |
| From | ``` var JSValueRef: JSValueRef { get } ``` |
| To | ``` var jsValueRef: JSValueRef! { get } ``` |

Modified [JSValue.objectForKeyedSubscript(_: Any!) -> JSValue!](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451371-objectforkeyedsubscript)

|  | Declaration |
| --- | --- |
| From | ``` func objectForKeyedSubscript(_ key: AnyObject!) -> JSValue! ``` |
| To | ``` func objectForKeyedSubscript(_ key: Any!) -> JSValue! ``` |

Modified [JSValue.setObject(_: Any!, atIndexedSubscript: Int)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451583-setobject)

|  | Declaration |
| --- | --- |
| From | ``` func setObject(_ object: AnyObject!, atIndexedSubscript index: Int) ``` |
| To | ``` func setObject(_ object: Any!, atIndexedSubscript index: Int) ``` |

Modified [JSValue.setObject(_: Any!, forKeyedSubscript: (NSCopying & NSObjectProtocol)!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451672-setobject)

|  | Declaration |
| --- | --- |
| From | ``` func setObject(_ object: AnyObject!, forKeyedSubscript key: protocol<NSCopying, NSObjectProtocol>!) ``` |
| To | ``` func setObject(_ object: Any!, forKeyedSubscript key: (NSCopying & NSObjectProtocol)!) ``` |

Modified [JSValue.setValue(_: Any!, at: Int)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451533-setvalue)

|  | Declaration |
| --- | --- |
| From | ``` func setValue(_ value: AnyObject!, atIndex index: Int) ``` |
| To | ``` func setValue(_ value: Any!, at index: Int) ``` |

Modified [JSValue.setValue(_: Any!, forProperty: String!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451676-setvalue)

|  | Declaration |
| --- | --- |
| From | ``` func setValue(_ value: AnyObject!, forProperty property: String!) ``` |
| To | ``` func setValue(_ value: Any!, forProperty property: String!) ``` |

Modified [JSValue.toArray() -> [Any]!](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451465-toarray)

|  | Declaration |
| --- | --- |
| From | ``` func toArray() -> [AnyObject]! ``` |
| To | ``` func toArray() -> [Any]! ``` |

Modified [JSValue.toDate() -> Date!](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451753-todate)

|  | Declaration |
| --- | --- |
| From | ``` func toDate() -> NSDate! ``` |
| To | ``` func toDate() -> Date! ``` |

Modified [JSValue.toDictionary() -> [AnyHashable : Any]!](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451728-todictionary)

|  | Declaration |
| --- | --- |
| From | ``` func toDictionary() -> [NSObject : AnyObject]! ``` |
| To | ``` func toDictionary() -> [AnyHashable : Any]! ``` |

Modified [JSValue.toObject() -> Any!](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451725-toobject)

|  | Declaration |
| --- | --- |
| From | ``` func toObject() -> AnyObject! ``` |
| To | ``` func toObject() -> Any! ``` |

Modified [JSValue.toObjectOf(_: Swift.AnyClass!) -> Any!](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451760-toobjectof)

|  | Declaration |
| --- | --- |
| From | ``` func toObjectOfClass(_ expectedClass: AnyClass!) -> AnyObject! ``` |
| To | ``` func toObjectOf(_ expectedClass: Swift.AnyClass!) -> Any! ``` |

Modified [JSVirtualMachine](https://developer.apple.com/documentation/javascriptcore/jsvirtualmachine)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class JSVirtualMachine : NSObject {     init!()     func addManagedReference(_ object: AnyObject!, withOwner owner: AnyObject!)     func removeManagedReference(_ object: AnyObject!, withOwner owner: AnyObject!) } ``` | -- |
| To | ``` class JSVirtualMachine : NSObject {     init!()     func addManagedReference(_ object: Any!, withOwner owner: Any!)     func removeManagedReference(_ object: Any!, withOwner owner: Any!)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension JSVirtualMachine : CVarArg { } extension JSVirtualMachine : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [JSVirtualMachine.addManagedReference(_: Any!, withOwner: Any!)](https://developer.apple.com/documentation/javascriptcore/jsvirtualmachine/1451354-addmanagedreference)

|  | Declaration |
| --- | --- |
| From | ``` func addManagedReference(_ object: AnyObject!, withOwner owner: AnyObject!) ``` |
| To | ``` func addManagedReference(_ object: Any!, withOwner owner: Any!) ``` |

Modified [JSVirtualMachine.removeManagedReference(_: Any!, withOwner: Any!)](https://developer.apple.com/documentation/javascriptcore/jsvirtualmachine/1451452-removemanagedreference)

|  | Declaration |
| --- | --- |
| From | ``` func removeManagedReference(_ object: AnyObject!, withOwner owner: AnyObject!) ``` |
| To | ``` func removeManagedReference(_ object: Any!, withOwner owner: Any!) ``` |

Modified [JSCheckScriptSyntax(_: JSContextRef!, _: JSStringRef!, _: JSStringRef!, _: Int32, _: UnsafeMutablePointer<JSValueRef?>!) -> Bool](https://developer.apple.com/documentation/javascriptcore/1451547-jscheckscriptsyntax)

|  | Declaration |
| --- | --- |
| From | ``` func JSCheckScriptSyntax(_ ctx: JSContextRef, _ script: JSStringRef, _ sourceURL: JSStringRef, _ startingLineNumber: Int32, _ exception: UnsafeMutablePointer<JSValueRef>) -> Bool ``` |
| To | ``` func JSCheckScriptSyntax(_ ctx: JSContextRef!, _ script: JSStringRef!, _ sourceURL: JSStringRef!, _ startingLineNumber: Int32, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> Bool ``` |

Modified [JSClassCreate(_: UnsafePointer<JSClassDefinition>!) -> JSClassRef!](https://developer.apple.com/documentation/javascriptcore/1451678-jsclasscreate)

|  | Declaration |
| --- | --- |
| From | ``` func JSClassCreate(_ definition: UnsafePointer<JSClassDefinition>) -> JSClassRef ``` |
| To | ``` func JSClassCreate(_ definition: UnsafePointer<JSClassDefinition>!) -> JSClassRef! ``` |

Modified [JSClassRef](https://developer.apple.com/documentation/javascriptcore/jsclassref)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSClassRef = COpaquePointer ``` |
| To | ``` typealias JSClassRef = OpaquePointer ``` |

Modified [JSClassRelease(_: JSClassRef!)](https://developer.apple.com/documentation/javascriptcore/1451508-jsclassrelease)

|  | Declaration |
| --- | --- |
| From | ``` func JSClassRelease(_ jsClass: JSClassRef) ``` |
| To | ``` func JSClassRelease(_ jsClass: JSClassRef!) ``` |

Modified [JSClassRetain(_: JSClassRef!) -> JSClassRef!](https://developer.apple.com/documentation/javascriptcore/1451344-jsclassretain)

|  | Declaration |
| --- | --- |
| From | ``` func JSClassRetain(_ jsClass: JSClassRef) -> JSClassRef ``` |
| To | ``` func JSClassRetain(_ jsClass: JSClassRef!) -> JSClassRef! ``` |

Modified [JSContextGetGlobalContext(_: JSContextRef!) -> JSGlobalContextRef!](https://developer.apple.com/documentation/javascriptcore/1451674-jscontextgetglobalcontext)

|  | Declaration |
| --- | --- |
| From | ``` func JSContextGetGlobalContext(_ ctx: JSContextRef) -> JSGlobalContextRef ``` |
| To | ``` func JSContextGetGlobalContext(_ ctx: JSContextRef!) -> JSGlobalContextRef! ``` |

Modified [JSContextGetGlobalObject(_: JSContextRef!) -> JSObjectRef!](https://developer.apple.com/documentation/javascriptcore/1451440-jscontextgetglobalobject)

|  | Declaration |
| --- | --- |
| From | ``` func JSContextGetGlobalObject(_ ctx: JSContextRef) -> JSObjectRef ``` |
| To | ``` func JSContextGetGlobalObject(_ ctx: JSContextRef!) -> JSObjectRef! ``` |

Modified [JSContextGetGroup(_: JSContextRef!) -> JSContextGroupRef!](https://developer.apple.com/documentation/javascriptcore/1451429-jscontextgetgroup)

|  | Declaration |
| --- | --- |
| From | ``` func JSContextGetGroup(_ ctx: JSContextRef) -> JSContextGroupRef ``` |
| To | ``` func JSContextGetGroup(_ ctx: JSContextRef!) -> JSContextGroupRef! ``` |

Modified [JSContextGroupCreate() -> JSContextGroupRef!](https://developer.apple.com/documentation/javascriptcore/1451632-jscontextgroupcreate)

|  | Declaration |
| --- | --- |
| From | ``` func JSContextGroupCreate() -> JSContextGroupRef ``` |
| To | ``` func JSContextGroupCreate() -> JSContextGroupRef! ``` |

Modified [JSContextGroupRef](https://developer.apple.com/documentation/javascriptcore/jscontextgroupref)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSContextGroupRef = COpaquePointer ``` |
| To | ``` typealias JSContextGroupRef = OpaquePointer ``` |

Modified [JSContextGroupRelease(_: JSContextGroupRef!)](https://developer.apple.com/documentation/javascriptcore/1451520-jscontextgrouprelease)

|  | Declaration |
| --- | --- |
| From | ``` func JSContextGroupRelease(_ group: JSContextGroupRef) ``` |
| To | ``` func JSContextGroupRelease(_ group: JSContextGroupRef!) ``` |

Modified [JSContextGroupRetain(_: JSContextGroupRef!) -> JSContextGroupRef!](https://developer.apple.com/documentation/javascriptcore/1451564-jscontextgroupretain)

|  | Declaration |
| --- | --- |
| From | ``` func JSContextGroupRetain(_ group: JSContextGroupRef) -> JSContextGroupRef ``` |
| To | ``` func JSContextGroupRetain(_ group: JSContextGroupRef!) -> JSContextGroupRef! ``` |

Modified [JSContextRef](https://developer.apple.com/documentation/javascriptcore/jscontextref)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSContextRef = COpaquePointer ``` |
| To | ``` typealias JSContextRef = OpaquePointer ``` |

Modified [JSEvaluateScript(_: JSContextRef!, _: JSStringRef!, _: JSObjectRef!, _: JSStringRef!, _: Int32, _: UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef!](https://developer.apple.com/documentation/javascriptcore/1451589-jsevaluatescript)

|  | Declaration |
| --- | --- |
| From | ``` func JSEvaluateScript(_ ctx: JSContextRef, _ script: JSStringRef, _ thisObject: JSObjectRef, _ sourceURL: JSStringRef, _ startingLineNumber: Int32, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSValueRef ``` |
| To | ``` func JSEvaluateScript(_ ctx: JSContextRef!, _ script: JSStringRef!, _ thisObject: JSObjectRef!, _ sourceURL: JSStringRef!, _ startingLineNumber: Int32, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef! ``` |

Modified [JSGarbageCollect(_: JSContextRef!)](https://developer.apple.com/documentation/javascriptcore/1451393-jsgarbagecollect)

|  | Declaration |
| --- | --- |
| From | ``` func JSGarbageCollect(_ ctx: JSContextRef) ``` |
| To | ``` func JSGarbageCollect(_ ctx: JSContextRef!) ``` |

Modified [JSGlobalContextCopyName(_: JSGlobalContextRef!) -> JSStringRef!](https://developer.apple.com/documentation/javascriptcore/1451356-jsglobalcontextcopyname)

|  | Declaration |
| --- | --- |
| From | ``` func JSGlobalContextCopyName(_ ctx: JSGlobalContextRef) -> JSStringRef ``` |
| To | ``` func JSGlobalContextCopyName(_ ctx: JSGlobalContextRef!) -> JSStringRef! ``` |

Modified [JSGlobalContextCreate(_: JSClassRef!) -> JSGlobalContextRef!](https://developer.apple.com/documentation/javascriptcore/1451585-jsglobalcontextcreate)

|  | Declaration |
| --- | --- |
| From | ``` func JSGlobalContextCreate(_ globalObjectClass: JSClassRef) -> JSGlobalContextRef ``` |
| To | ``` func JSGlobalContextCreate(_ globalObjectClass: JSClassRef!) -> JSGlobalContextRef! ``` |

Modified [JSGlobalContextCreateInGroup(_: JSContextGroupRef!, _: JSClassRef!) -> JSGlobalContextRef!](https://developer.apple.com/documentation/javascriptcore/1451710-jsglobalcontextcreateingroup)

|  | Declaration |
| --- | --- |
| From | ``` func JSGlobalContextCreateInGroup(_ group: JSContextGroupRef, _ globalObjectClass: JSClassRef) -> JSGlobalContextRef ``` |
| To | ``` func JSGlobalContextCreateInGroup(_ group: JSContextGroupRef!, _ globalObjectClass: JSClassRef!) -> JSGlobalContextRef! ``` |

Modified [JSGlobalContextRef](https://developer.apple.com/documentation/javascriptcore/jsglobalcontextref)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSGlobalContextRef = COpaquePointer ``` |
| To | ``` typealias JSGlobalContextRef = OpaquePointer ``` |

Modified [JSGlobalContextRelease(_: JSGlobalContextRef!)](https://developer.apple.com/documentation/javascriptcore/1451599-jsglobalcontextrelease)

|  | Declaration |
| --- | --- |
| From | ``` func JSGlobalContextRelease(_ ctx: JSGlobalContextRef) ``` |
| To | ``` func JSGlobalContextRelease(_ ctx: JSGlobalContextRef!) ``` |

Modified [JSGlobalContextRetain(_: JSGlobalContextRef!) -> JSGlobalContextRef!](https://developer.apple.com/documentation/javascriptcore/1451719-jsglobalcontextretain)

|  | Declaration |
| --- | --- |
| From | ``` func JSGlobalContextRetain(_ ctx: JSGlobalContextRef) -> JSGlobalContextRef ``` |
| To | ``` func JSGlobalContextRetain(_ ctx: JSGlobalContextRef!) -> JSGlobalContextRef! ``` |

Modified [JSGlobalContextSetName(_: JSGlobalContextRef!, _: JSStringRef!)](https://developer.apple.com/documentation/javascriptcore/1451703-jsglobalcontextsetname)

|  | Declaration |
| --- | --- |
| From | ``` func JSGlobalContextSetName(_ ctx: JSGlobalContextRef, _ name: JSStringRef) ``` |
| To | ``` func JSGlobalContextSetName(_ ctx: JSGlobalContextRef!, _ name: JSStringRef!) ``` |

Modified [JSObjectCallAsConstructor(_: JSContextRef!, _: JSObjectRef!, _: Int, _: UnsafePointer<JSValueRef?>!, _: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](https://developer.apple.com/documentation/javascriptcore/1451445-jsobjectcallasconstructor)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectCallAsConstructor(_ ctx: JSContextRef, _ object: JSObjectRef, _ argumentCount: Int, _ arguments: UnsafePointer<JSValueRef>, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSObjectRef ``` |
| To | ``` func JSObjectCallAsConstructor(_ ctx: JSContextRef!, _ object: JSObjectRef!, _ argumentCount: Int, _ arguments: UnsafePointer<JSValueRef?>!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef! ``` |

Modified [JSObjectCallAsConstructorCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectcallasconstructorcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectCallAsConstructorCallback = (JSContextRef, JSObjectRef, Int, UnsafePointer<JSValueRef>, UnsafeMutablePointer<JSValueRef>) -> JSObjectRef ``` |
| To | ``` typealias JSObjectCallAsConstructorCallback = (JSContextRef?, JSObjectRef?, Int, UnsafePointer<JSValueRef?>?, UnsafeMutablePointer<JSValueRef?>?) -> JSObjectRef? ``` |

Modified [JSObjectCallAsFunction(_: JSContextRef!, _: JSObjectRef!, _: JSObjectRef!, _: Int, _: UnsafePointer<JSValueRef?>!, _: UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef!](https://developer.apple.com/documentation/javascriptcore/1451407-jsobjectcallasfunction)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectCallAsFunction(_ ctx: JSContextRef, _ object: JSObjectRef, _ thisObject: JSObjectRef, _ argumentCount: Int, _ arguments: UnsafePointer<JSValueRef>, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSValueRef ``` |
| To | ``` func JSObjectCallAsFunction(_ ctx: JSContextRef!, _ object: JSObjectRef!, _ thisObject: JSObjectRef!, _ argumentCount: Int, _ arguments: UnsafePointer<JSValueRef?>!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef! ``` |

Modified [JSObjectCallAsFunctionCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectcallasfunctioncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectCallAsFunctionCallback = (JSContextRef, JSObjectRef, JSObjectRef, Int, UnsafePointer<JSValueRef>, UnsafeMutablePointer<JSValueRef>) -> JSValueRef ``` |
| To | ``` typealias JSObjectCallAsFunctionCallback = (JSContextRef?, JSObjectRef?, JSObjectRef?, Int, UnsafePointer<JSValueRef?>?, UnsafeMutablePointer<JSValueRef?>?) -> JSValueRef? ``` |

Modified [JSObjectConvertToTypeCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectconverttotypecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectConvertToTypeCallback = (JSContextRef, JSObjectRef, JSType, UnsafeMutablePointer<JSValueRef>) -> JSValueRef ``` |
| To | ``` typealias JSObjectConvertToTypeCallback = (JSContextRef?, JSObjectRef?, JSType, UnsafeMutablePointer<JSValueRef?>?) -> JSValueRef? ``` |

Modified [JSObjectCopyPropertyNames(_: JSContextRef!, _: JSObjectRef!) -> JSPropertyNameArrayRef!](https://developer.apple.com/documentation/javascriptcore/1451560-jsobjectcopypropertynames)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectCopyPropertyNames(_ ctx: JSContextRef, _ object: JSObjectRef) -> JSPropertyNameArrayRef ``` |
| To | ``` func JSObjectCopyPropertyNames(_ ctx: JSContextRef!, _ object: JSObjectRef!) -> JSPropertyNameArrayRef! ``` |

Modified [JSObjectDeleteProperty(_: JSContextRef!, _: JSObjectRef!, _: JSStringRef!, _: UnsafeMutablePointer<JSValueRef?>!) -> Bool](https://developer.apple.com/documentation/javascriptcore/1451595-jsobjectdeleteproperty)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectDeleteProperty(_ ctx: JSContextRef, _ object: JSObjectRef, _ propertyName: JSStringRef, _ exception: UnsafeMutablePointer<JSValueRef>) -> Bool ``` |
| To | ``` func JSObjectDeleteProperty(_ ctx: JSContextRef!, _ object: JSObjectRef!, _ propertyName: JSStringRef!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> Bool ``` |

Modified [JSObjectDeletePropertyCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectdeletepropertycallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectDeletePropertyCallback = (JSContextRef, JSObjectRef, JSStringRef, UnsafeMutablePointer<JSValueRef>) -> Bool ``` |
| To | ``` typealias JSObjectDeletePropertyCallback = (JSContextRef?, JSObjectRef?, JSStringRef?, UnsafeMutablePointer<JSValueRef?>?) -> Bool ``` |

Modified [JSObjectFinalizeCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectfinalizecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectFinalizeCallback = (JSObjectRef) -> Void ``` |
| To | ``` typealias JSObjectFinalizeCallback = (JSObjectRef?) -> Swift.Void ``` |

Modified [JSObjectGetPrivate(_: JSObjectRef!) -> UnsafeMutableRawPointer!](https://developer.apple.com/documentation/javascriptcore/1451515-jsobjectgetprivate)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectGetPrivate(_ object: JSObjectRef) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func JSObjectGetPrivate(_ object: JSObjectRef!) -> UnsafeMutableRawPointer! ``` |

Modified [JSObjectGetProperty(_: JSContextRef!, _: JSObjectRef!, _: JSStringRef!, _: UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef!](https://developer.apple.com/documentation/javascriptcore/1451619-jsobjectgetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectGetProperty(_ ctx: JSContextRef, _ object: JSObjectRef, _ propertyName: JSStringRef, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSValueRef ``` |
| To | ``` func JSObjectGetProperty(_ ctx: JSContextRef!, _ object: JSObjectRef!, _ propertyName: JSStringRef!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef! ``` |

Modified [JSObjectGetPropertyAtIndex(_: JSContextRef!, _: JSObjectRef!, _: UInt32, _: UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef!](https://developer.apple.com/documentation/javascriptcore/1451717-jsobjectgetpropertyatindex)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectGetPropertyAtIndex(_ ctx: JSContextRef, _ object: JSObjectRef, _ propertyIndex: UInt32, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSValueRef ``` |
| To | ``` func JSObjectGetPropertyAtIndex(_ ctx: JSContextRef!, _ object: JSObjectRef!, _ propertyIndex: UInt32, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef! ``` |

Modified [JSObjectGetPropertyCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectgetpropertycallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectGetPropertyCallback = (JSContextRef, JSObjectRef, JSStringRef, UnsafeMutablePointer<JSValueRef>) -> JSValueRef ``` |
| To | ``` typealias JSObjectGetPropertyCallback = (JSContextRef?, JSObjectRef?, JSStringRef?, UnsafeMutablePointer<JSValueRef?>?) -> JSValueRef? ``` |

Modified [JSObjectGetPropertyNamesCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectgetpropertynamescallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectGetPropertyNamesCallback = (JSContextRef, JSObjectRef, JSPropertyNameAccumulatorRef) -> Void ``` |
| To | ``` typealias JSObjectGetPropertyNamesCallback = (JSContextRef?, JSObjectRef?, JSPropertyNameAccumulatorRef?) -> Swift.Void ``` |

Modified [JSObjectGetPrototype(_: JSContextRef!, _: JSObjectRef!) -> JSValueRef!](https://developer.apple.com/documentation/javascriptcore/1451342-jsobjectgetprototype)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectGetPrototype(_ ctx: JSContextRef, _ object: JSObjectRef) -> JSValueRef ``` |
| To | ``` func JSObjectGetPrototype(_ ctx: JSContextRef!, _ object: JSObjectRef!) -> JSValueRef! ``` |

Modified [JSObjectHasInstanceCallback](https://developer.apple.com/documentation/javascriptcore/jsobjecthasinstancecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectHasInstanceCallback = (JSContextRef, JSObjectRef, JSValueRef, UnsafeMutablePointer<JSValueRef>) -> Bool ``` |
| To | ``` typealias JSObjectHasInstanceCallback = (JSContextRef?, JSObjectRef?, JSValueRef?, UnsafeMutablePointer<JSValueRef?>?) -> Bool ``` |

Modified [JSObjectHasProperty(_: JSContextRef!, _: JSObjectRef!, _: JSStringRef!) -> Bool](https://developer.apple.com/documentation/javascriptcore/1451558-jsobjecthasproperty)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectHasProperty(_ ctx: JSContextRef, _ object: JSObjectRef, _ propertyName: JSStringRef) -> Bool ``` |
| To | ``` func JSObjectHasProperty(_ ctx: JSContextRef!, _ object: JSObjectRef!, _ propertyName: JSStringRef!) -> Bool ``` |

Modified [JSObjectHasPropertyCallback](https://developer.apple.com/documentation/javascriptcore/jsobjecthaspropertycallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectHasPropertyCallback = (JSContextRef, JSObjectRef, JSStringRef) -> Bool ``` |
| To | ``` typealias JSObjectHasPropertyCallback = (JSContextRef?, JSObjectRef?, JSStringRef?) -> Bool ``` |

Modified [JSObjectInitializeCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectinitializecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectInitializeCallback = (JSContextRef, JSObjectRef) -> Void ``` |
| To | ``` typealias JSObjectInitializeCallback = (JSContextRef?, JSObjectRef?) -> Swift.Void ``` |

Modified [JSObjectIsConstructor(_: JSContextRef!, _: JSObjectRef!) -> Bool](https://developer.apple.com/documentation/javascriptcore/1451486-jsobjectisconstructor)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectIsConstructor(_ ctx: JSContextRef, _ object: JSObjectRef) -> Bool ``` |
| To | ``` func JSObjectIsConstructor(_ ctx: JSContextRef!, _ object: JSObjectRef!) -> Bool ``` |

Modified [JSObjectIsFunction(_: JSContextRef!, _: JSObjectRef!) -> Bool](https://developer.apple.com/documentation/javascriptcore/1451769-jsobjectisfunction)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectIsFunction(_ ctx: JSContextRef, _ object: JSObjectRef) -> Bool ``` |
| To | ``` func JSObjectIsFunction(_ ctx: JSContextRef!, _ object: JSObjectRef!) -> Bool ``` |

Modified [JSObjectMake(_: JSContextRef!, _: JSClassRef!, _: UnsafeMutableRawPointer!) -> JSObjectRef!](https://developer.apple.com/documentation/javascriptcore/1451624-jsobjectmake)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectMake(_ ctx: JSContextRef, _ jsClass: JSClassRef, _ data: UnsafeMutablePointer<Void>) -> JSObjectRef ``` |
| To | ``` func JSObjectMake(_ ctx: JSContextRef!, _ jsClass: JSClassRef!, _ data: UnsafeMutableRawPointer!) -> JSObjectRef! ``` |

Modified [JSObjectMakeArray(_: JSContextRef!, _: Int, _: UnsafePointer<JSValueRef?>!, _: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](https://developer.apple.com/documentation/javascriptcore/1451661-jsobjectmakearray)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectMakeArray(_ ctx: JSContextRef, _ argumentCount: Int, _ arguments: UnsafePointer<JSValueRef>, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSObjectRef ``` |
| To | ``` func JSObjectMakeArray(_ ctx: JSContextRef!, _ argumentCount: Int, _ arguments: UnsafePointer<JSValueRef?>!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef! ``` |

Modified [JSObjectMakeConstructor(_: JSContextRef!, _: JSClassRef!, _: JavaScriptCore.JSObjectCallAsConstructorCallback!) -> JSObjectRef!](https://developer.apple.com/documentation/javascriptcore/1451566-jsobjectmakeconstructor)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectMakeConstructor(_ ctx: JSContextRef, _ jsClass: JSClassRef, _ callAsConstructor: JSObjectCallAsConstructorCallback!) -> JSObjectRef ``` |
| To | ``` func JSObjectMakeConstructor(_ ctx: JSContextRef!, _ jsClass: JSClassRef!, _ callAsConstructor: JavaScriptCore.JSObjectCallAsConstructorCallback!) -> JSObjectRef! ``` |

Modified [JSObjectMakeDate(_: JSContextRef!, _: Int, _: UnsafePointer<JSValueRef?>!, _: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](https://developer.apple.com/documentation/javascriptcore/1451745-jsobjectmakedate)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectMakeDate(_ ctx: JSContextRef, _ argumentCount: Int, _ arguments: UnsafePointer<JSValueRef>, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSObjectRef ``` |
| To | ``` func JSObjectMakeDate(_ ctx: JSContextRef!, _ argumentCount: Int, _ arguments: UnsafePointer<JSValueRef?>!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef! ``` |

Modified [JSObjectMakeError(_: JSContextRef!, _: Int, _: UnsafePointer<JSValueRef?>!, _: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](https://developer.apple.com/documentation/javascriptcore/1451375-jsobjectmakeerror)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectMakeError(_ ctx: JSContextRef, _ argumentCount: Int, _ arguments: UnsafePointer<JSValueRef>, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSObjectRef ``` |
| To | ``` func JSObjectMakeError(_ ctx: JSContextRef!, _ argumentCount: Int, _ arguments: UnsafePointer<JSValueRef?>!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef! ``` |

Modified [JSObjectMakeFunction(_: JSContextRef!, _: JSStringRef!, _: UInt32, _: UnsafePointer<JSStringRef?>!, _: JSStringRef!, _: JSStringRef!, _: Int32, _: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](https://developer.apple.com/documentation/javascriptcore/1451478-jsobjectmakefunction)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectMakeFunction(_ ctx: JSContextRef, _ name: JSStringRef, _ parameterCount: UInt32, _ parameterNames: UnsafePointer<JSStringRef>, _ body: JSStringRef, _ sourceURL: JSStringRef, _ startingLineNumber: Int32, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSObjectRef ``` |
| To | ``` func JSObjectMakeFunction(_ ctx: JSContextRef!, _ name: JSStringRef!, _ parameterCount: UInt32, _ parameterNames: UnsafePointer<JSStringRef?>!, _ body: JSStringRef!, _ sourceURL: JSStringRef!, _ startingLineNumber: Int32, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef! ``` |

Modified [JSObjectMakeFunctionWithCallback(_: JSContextRef!, _: JSStringRef!, _: JavaScriptCore.JSObjectCallAsFunctionCallback!) -> JSObjectRef!](https://developer.apple.com/documentation/javascriptcore/1451336-jsobjectmakefunctionwithcallback)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectMakeFunctionWithCallback(_ ctx: JSContextRef, _ name: JSStringRef, _ callAsFunction: JSObjectCallAsFunctionCallback!) -> JSObjectRef ``` |
| To | ``` func JSObjectMakeFunctionWithCallback(_ ctx: JSContextRef!, _ name: JSStringRef!, _ callAsFunction: JavaScriptCore.JSObjectCallAsFunctionCallback!) -> JSObjectRef! ``` |

Modified [JSObjectMakeRegExp(_: JSContextRef!, _: Int, _: UnsafePointer<JSValueRef?>!, _: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](https://developer.apple.com/documentation/javascriptcore/1451530-jsobjectmakeregexp)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectMakeRegExp(_ ctx: JSContextRef, _ argumentCount: Int, _ arguments: UnsafePointer<JSValueRef>, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSObjectRef ``` |
| To | ``` func JSObjectMakeRegExp(_ ctx: JSContextRef!, _ argumentCount: Int, _ arguments: UnsafePointer<JSValueRef?>!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef! ``` |

Modified [JSObjectRef](https://developer.apple.com/documentation/javascriptcore/jsobjectref)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectRef = COpaquePointer ``` |
| To | ``` typealias JSObjectRef = OpaquePointer ``` |

Modified [JSObjectSetPrivate(_: JSObjectRef!, _: UnsafeMutableRawPointer!) -> Bool](https://developer.apple.com/documentation/javascriptcore/1451626-jsobjectsetprivate)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectSetPrivate(_ object: JSObjectRef, _ data: UnsafeMutablePointer<Void>) -> Bool ``` |
| To | ``` func JSObjectSetPrivate(_ object: JSObjectRef!, _ data: UnsafeMutableRawPointer!) -> Bool ``` |

Modified [JSObjectSetProperty(_: JSContextRef!, _: JSObjectRef!, _: JSStringRef!, _: JSValueRef!, _: JSPropertyAttributes, _: UnsafeMutablePointer<JSValueRef?>!)](https://developer.apple.com/documentation/javascriptcore/1451687-jsobjectsetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectSetProperty(_ ctx: JSContextRef, _ object: JSObjectRef, _ propertyName: JSStringRef, _ value: JSValueRef, _ attributes: JSPropertyAttributes, _ exception: UnsafeMutablePointer<JSValueRef>) ``` |
| To | ``` func JSObjectSetProperty(_ ctx: JSContextRef!, _ object: JSObjectRef!, _ propertyName: JSStringRef!, _ value: JSValueRef!, _ attributes: JSPropertyAttributes, _ exception: UnsafeMutablePointer<JSValueRef?>!) ``` |

Modified [JSObjectSetPropertyAtIndex(_: JSContextRef!, _: JSObjectRef!, _: UInt32, _: JSValueRef!, _: UnsafeMutablePointer<JSValueRef?>!)](https://developer.apple.com/documentation/javascriptcore/1451744-jsobjectsetpropertyatindex)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectSetPropertyAtIndex(_ ctx: JSContextRef, _ object: JSObjectRef, _ propertyIndex: UInt32, _ value: JSValueRef, _ exception: UnsafeMutablePointer<JSValueRef>) ``` |
| To | ``` func JSObjectSetPropertyAtIndex(_ ctx: JSContextRef!, _ object: JSObjectRef!, _ propertyIndex: UInt32, _ value: JSValueRef!, _ exception: UnsafeMutablePointer<JSValueRef?>!) ``` |

Modified [JSObjectSetPropertyCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectsetpropertycallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectSetPropertyCallback = (JSContextRef, JSObjectRef, JSStringRef, JSValueRef, UnsafeMutablePointer<JSValueRef>) -> Bool ``` |
| To | ``` typealias JSObjectSetPropertyCallback = (JSContextRef?, JSObjectRef?, JSStringRef?, JSValueRef?, UnsafeMutablePointer<JSValueRef?>?) -> Bool ``` |

Modified [JSObjectSetPrototype(_: JSContextRef!, _: JSObjectRef!, _: JSValueRef!)](https://developer.apple.com/documentation/javascriptcore/1451747-jsobjectsetprototype)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectSetPrototype(_ ctx: JSContextRef, _ object: JSObjectRef, _ value: JSValueRef) ``` |
| To | ``` func JSObjectSetPrototype(_ ctx: JSContextRef!, _ object: JSObjectRef!, _ value: JSValueRef!) ``` |

Modified [JSPropertyNameAccumulatorAddName(_: JSPropertyNameAccumulatorRef!, _: JSStringRef!)](https://developer.apple.com/documentation/javascriptcore/1451395-jspropertynameaccumulatoraddname)

|  | Declaration |
| --- | --- |
| From | ``` func JSPropertyNameAccumulatorAddName(_ accumulator: JSPropertyNameAccumulatorRef, _ propertyName: JSStringRef) ``` |
| To | ``` func JSPropertyNameAccumulatorAddName(_ accumulator: JSPropertyNameAccumulatorRef!, _ propertyName: JSStringRef!) ``` |

Modified [JSPropertyNameAccumulatorRef](https://developer.apple.com/documentation/javascriptcore/jspropertynameaccumulatorref)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSPropertyNameAccumulatorRef = COpaquePointer ``` |
| To | ``` typealias JSPropertyNameAccumulatorRef = OpaquePointer ``` |

Modified [JSPropertyNameArrayGetCount(_: JSPropertyNameArrayRef!) -> Int](https://developer.apple.com/documentation/javascriptcore/1451573-jspropertynamearraygetcount)

|  | Declaration |
| --- | --- |
| From | ``` func JSPropertyNameArrayGetCount(_ array: JSPropertyNameArrayRef) -> Int ``` |
| To | ``` func JSPropertyNameArrayGetCount(_ array: JSPropertyNameArrayRef!) -> Int ``` |

Modified [JSPropertyNameArrayGetNameAtIndex(_: JSPropertyNameArrayRef!, _: Int) -> JSStringRef!](https://developer.apple.com/documentation/javascriptcore/1451592-jspropertynamearraygetnameatinde)

|  | Declaration |
| --- | --- |
| From | ``` func JSPropertyNameArrayGetNameAtIndex(_ array: JSPropertyNameArrayRef, _ index: Int) -> JSStringRef ``` |
| To | ``` func JSPropertyNameArrayGetNameAtIndex(_ array: JSPropertyNameArrayRef!, _ index: Int) -> JSStringRef! ``` |

Modified [JSPropertyNameArrayRef](https://developer.apple.com/documentation/javascriptcore/jspropertynamearrayref)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSPropertyNameArrayRef = COpaquePointer ``` |
| To | ``` typealias JSPropertyNameArrayRef = OpaquePointer ``` |

Modified [JSPropertyNameArrayRelease(_: JSPropertyNameArrayRef!)](https://developer.apple.com/documentation/javascriptcore/1451569-jspropertynamearrayrelease)

|  | Declaration |
| --- | --- |
| From | ``` func JSPropertyNameArrayRelease(_ array: JSPropertyNameArrayRef) ``` |
| To | ``` func JSPropertyNameArrayRelease(_ array: JSPropertyNameArrayRef!) ``` |

Modified [JSPropertyNameArrayRetain(_: JSPropertyNameArrayRef!) -> JSPropertyNameArrayRef!](https://developer.apple.com/documentation/javascriptcore/1451352-jspropertynamearrayretain)

|  | Declaration |
| --- | --- |
| From | ``` func JSPropertyNameArrayRetain(_ array: JSPropertyNameArrayRef) -> JSPropertyNameArrayRef ``` |
| To | ``` func JSPropertyNameArrayRetain(_ array: JSPropertyNameArrayRef!) -> JSPropertyNameArrayRef! ``` |

Modified [JSStringCopyCFString(_: CFAllocator!, _: JSStringRef!) -> CFString!](https://developer.apple.com/documentation/javascriptcore/1451659-jsstringcopycfstring)

|  | Declaration |
| --- | --- |
| From | ``` func JSStringCopyCFString(_ alloc: CFAllocator!, _ string: JSStringRef) -> CFString! ``` |
| To | ``` func JSStringCopyCFString(_ alloc: CFAllocator!, _ string: JSStringRef!) -> CFString! ``` |

Modified [JSStringCreateWithCFString(_: CFString!) -> JSStringRef!](https://developer.apple.com/documentation/javascriptcore/1451524-jsstringcreatewithcfstring)

|  | Declaration |
| --- | --- |
| From | ``` func JSStringCreateWithCFString(_ string: CFString!) -> JSStringRef ``` |
| To | ``` func JSStringCreateWithCFString(_ string: CFString!) -> JSStringRef! ``` |

Modified [JSStringCreateWithCharacters(_: UnsafePointer<JSChar>!, _: Int) -> JSStringRef!](https://developer.apple.com/documentation/javascriptcore/1412810-jsstringcreatewithcharacters)

|  | Declaration |
| --- | --- |
| From | ``` func JSStringCreateWithCharacters(_ chars: UnsafePointer<JSChar>, _ numChars: Int) -> JSStringRef ``` |
| To | ``` func JSStringCreateWithCharacters(_ chars: UnsafePointer<JSChar>!, _ numChars: Int) -> JSStringRef! ``` |

Modified [JSStringCreateWithUTF8CString(_: UnsafePointer<Int8>!) -> JSStringRef!](https://developer.apple.com/documentation/javascriptcore/1412806-jsstringcreatewithutf8cstring)

|  | Declaration |
| --- | --- |
| From | ``` func JSStringCreateWithUTF8CString(_ string: UnsafePointer<Int8>) -> JSStringRef ``` |
| To | ``` func JSStringCreateWithUTF8CString(_ string: UnsafePointer<Int8>!) -> JSStringRef! ``` |

Modified [JSStringGetCharactersPtr(_: JSStringRef!) -> UnsafePointer<JSChar>!](https://developer.apple.com/documentation/javascriptcore/1412796-jsstringgetcharactersptr)

|  | Declaration |
| --- | --- |
| From | ``` func JSStringGetCharactersPtr(_ string: JSStringRef) -> UnsafePointer<JSChar> ``` |
| To | ``` func JSStringGetCharactersPtr(_ string: JSStringRef!) -> UnsafePointer<JSChar>! ``` |

Modified [JSStringGetLength(_: JSStringRef!) -> Int](https://developer.apple.com/documentation/javascriptcore/1412802-jsstringgetlength)

|  | Declaration |
| --- | --- |
| From | ``` func JSStringGetLength(_ string: JSStringRef) -> Int ``` |
| To | ``` func JSStringGetLength(_ string: JSStringRef!) -> Int ``` |

Modified [JSStringGetMaximumUTF8CStringSize(_: JSStringRef!) -> Int](https://developer.apple.com/documentation/javascriptcore/1412800-jsstringgetmaximumutf8cstringsiz)

|  | Declaration |
| --- | --- |
| From | ``` func JSStringGetMaximumUTF8CStringSize(_ string: JSStringRef) -> Int ``` |
| To | ``` func JSStringGetMaximumUTF8CStringSize(_ string: JSStringRef!) -> Int ``` |

Modified [JSStringGetUTF8CString(_: JSStringRef!, _: UnsafeMutablePointer<Int8>!, _: Int) -> Int](https://developer.apple.com/documentation/javascriptcore/1412812-jsstringgetutf8cstring)

|  | Declaration |
| --- | --- |
| From | ``` func JSStringGetUTF8CString(_ string: JSStringRef, _ buffer: UnsafeMutablePointer<Int8>, _ bufferSize: Int) -> Int ``` |
| To | ``` func JSStringGetUTF8CString(_ string: JSStringRef!, _ buffer: UnsafeMutablePointer<Int8>!, _ bufferSize: Int) -> Int ``` |

Modified [JSStringIsEqual(_: JSStringRef!, _: JSStringRef!) -> Bool](https://developer.apple.com/documentation/javascriptcore/1412804-jsstringisequal)

|  | Declaration |
| --- | --- |
| From | ``` func JSStringIsEqual(_ a: JSStringRef, _ b: JSStringRef) -> Bool ``` |
| To | ``` func JSStringIsEqual(_ a: JSStringRef!, _ b: JSStringRef!) -> Bool ``` |

Modified [JSStringIsEqualToUTF8CString(_: JSStringRef!, _: UnsafePointer<Int8>!) -> Bool](https://developer.apple.com/documentation/javascriptcore/1412792-jsstringisequaltoutf8cstring)

|  | Declaration |
| --- | --- |
| From | ``` func JSStringIsEqualToUTF8CString(_ a: JSStringRef, _ b: UnsafePointer<Int8>) -> Bool ``` |
| To | ``` func JSStringIsEqualToUTF8CString(_ a: JSStringRef!, _ b: UnsafePointer<Int8>!) -> Bool ``` |

Modified [JSStringRef](https://developer.apple.com/documentation/javascriptcore/jsstringref)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSStringRef = COpaquePointer ``` |
| To | ``` typealias JSStringRef = OpaquePointer ``` |

Modified [JSStringRelease(_: JSStringRef!)](https://developer.apple.com/documentation/javascriptcore/1412814-jsstringrelease)

|  | Declaration |
| --- | --- |
| From | ``` func JSStringRelease(_ string: JSStringRef) ``` |
| To | ``` func JSStringRelease(_ string: JSStringRef!) ``` |

Modified [JSStringRetain(_: JSStringRef!) -> JSStringRef!](https://developer.apple.com/documentation/javascriptcore/1412794-jsstringretain)

|  | Declaration |
| --- | --- |
| From | ``` func JSStringRetain(_ string: JSStringRef) -> JSStringRef ``` |
| To | ``` func JSStringRetain(_ string: JSStringRef!) -> JSStringRef! ``` |

Modified [JSValueCreateJSONString(_: JSContextRef!, _: JSValueRef!, _: UInt32, _: UnsafeMutablePointer<JSValueRef?>!) -> JSStringRef!](https://developer.apple.com/documentation/javascriptcore/1395934-jsvaluecreatejsonstring)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueCreateJSONString(_ ctx: JSContextRef, _ value: JSValueRef, _ indent: UInt32, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSStringRef ``` |
| To | ``` func JSValueCreateJSONString(_ ctx: JSContextRef!, _ value: JSValueRef!, _ indent: UInt32, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSStringRef! ``` |

Modified [JSValueGetType(_: JSContextRef!, _: JSValueRef!) -> JSType](https://developer.apple.com/documentation/javascriptcore/1395918-jsvaluegettype)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueGetType(_ ctx: JSContextRef, _ _: JSValueRef) -> JSType ``` |
| To | ``` func JSValueGetType(_ ctx: JSContextRef!, _ _: JSValueRef!) -> JSType ``` |

Modified [JSValueIsArray(_: JSContextRef!, _: JSValueRef!) -> Bool](https://developer.apple.com/documentation/javascriptcore/1395924-jsvalueisarray)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueIsArray(_ ctx: JSContextRef, _ value: JSValueRef) -> Bool ``` |
| To | ``` func JSValueIsArray(_ ctx: JSContextRef!, _ value: JSValueRef!) -> Bool ``` |

Modified [JSValueIsBoolean(_: JSContextRef!, _: JSValueRef!) -> Bool](https://developer.apple.com/documentation/javascriptcore/1395970-jsvalueisboolean)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueIsBoolean(_ ctx: JSContextRef, _ value: JSValueRef) -> Bool ``` |
| To | ``` func JSValueIsBoolean(_ ctx: JSContextRef!, _ value: JSValueRef!) -> Bool ``` |

Modified [JSValueIsDate(_: JSContextRef!, _: JSValueRef!) -> Bool](https://developer.apple.com/documentation/javascriptcore/1395926-jsvalueisdate)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueIsDate(_ ctx: JSContextRef, _ value: JSValueRef) -> Bool ``` |
| To | ``` func JSValueIsDate(_ ctx: JSContextRef!, _ value: JSValueRef!) -> Bool ``` |

Modified [JSValueIsEqual(_: JSContextRef!, _: JSValueRef!, _: JSValueRef!, _: UnsafeMutablePointer<JSValueRef?>!) -> Bool](https://developer.apple.com/documentation/javascriptcore/1395960-jsvalueisequal)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueIsEqual(_ ctx: JSContextRef, _ a: JSValueRef, _ b: JSValueRef, _ exception: UnsafeMutablePointer<JSValueRef>) -> Bool ``` |
| To | ``` func JSValueIsEqual(_ ctx: JSContextRef!, _ a: JSValueRef!, _ b: JSValueRef!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> Bool ``` |

Modified [JSValueIsInstanceOfConstructor(_: JSContextRef!, _: JSValueRef!, _: JSObjectRef!, _: UnsafeMutablePointer<JSValueRef?>!) -> Bool](https://developer.apple.com/documentation/javascriptcore/1395944-jsvalueisinstanceofconstructor)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueIsInstanceOfConstructor(_ ctx: JSContextRef, _ value: JSValueRef, _ constructor: JSObjectRef, _ exception: UnsafeMutablePointer<JSValueRef>) -> Bool ``` |
| To | ``` func JSValueIsInstanceOfConstructor(_ ctx: JSContextRef!, _ value: JSValueRef!, _ constructor: JSObjectRef!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> Bool ``` |

Modified [JSValueIsNull(_: JSContextRef!, _: JSValueRef!) -> Bool](https://developer.apple.com/documentation/javascriptcore/1395966-jsvalueisnull)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueIsNull(_ ctx: JSContextRef, _ value: JSValueRef) -> Bool ``` |
| To | ``` func JSValueIsNull(_ ctx: JSContextRef!, _ value: JSValueRef!) -> Bool ``` |

Modified [JSValueIsNumber(_: JSContextRef!, _: JSValueRef!) -> Bool](https://developer.apple.com/documentation/javascriptcore/1395958-jsvalueisnumber)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueIsNumber(_ ctx: JSContextRef, _ value: JSValueRef) -> Bool ``` |
| To | ``` func JSValueIsNumber(_ ctx: JSContextRef!, _ value: JSValueRef!) -> Bool ``` |

Modified [JSValueIsObject(_: JSContextRef!, _: JSValueRef!) -> Bool](https://developer.apple.com/documentation/javascriptcore/1395954-jsvalueisobject)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueIsObject(_ ctx: JSContextRef, _ value: JSValueRef) -> Bool ``` |
| To | ``` func JSValueIsObject(_ ctx: JSContextRef!, _ value: JSValueRef!) -> Bool ``` |

Modified [JSValueIsObjectOfClass(_: JSContextRef!, _: JSValueRef!, _: JSClassRef!) -> Bool](https://developer.apple.com/documentation/javascriptcore/1395932-jsvalueisobjectofclass)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueIsObjectOfClass(_ ctx: JSContextRef, _ value: JSValueRef, _ jsClass: JSClassRef) -> Bool ``` |
| To | ``` func JSValueIsObjectOfClass(_ ctx: JSContextRef!, _ value: JSValueRef!, _ jsClass: JSClassRef!) -> Bool ``` |

Modified [JSValueIsStrictEqual(_: JSContextRef!, _: JSValueRef!, _: JSValueRef!) -> Bool](https://developer.apple.com/documentation/javascriptcore/1395920-jsvalueisstrictequal)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueIsStrictEqual(_ ctx: JSContextRef, _ a: JSValueRef, _ b: JSValueRef) -> Bool ``` |
| To | ``` func JSValueIsStrictEqual(_ ctx: JSContextRef!, _ a: JSValueRef!, _ b: JSValueRef!) -> Bool ``` |

Modified [JSValueIsString(_: JSContextRef!, _: JSValueRef!) -> Bool](https://developer.apple.com/documentation/javascriptcore/1395940-jsvalueisstring)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueIsString(_ ctx: JSContextRef, _ value: JSValueRef) -> Bool ``` |
| To | ``` func JSValueIsString(_ ctx: JSContextRef!, _ value: JSValueRef!) -> Bool ``` |

Modified [JSValueIsUndefined(_: JSContextRef!, _: JSValueRef!) -> Bool](https://developer.apple.com/documentation/javascriptcore/1395964-jsvalueisundefined)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueIsUndefined(_ ctx: JSContextRef, _ value: JSValueRef) -> Bool ``` |
| To | ``` func JSValueIsUndefined(_ ctx: JSContextRef!, _ value: JSValueRef!) -> Bool ``` |

Modified [JSValueMakeBoolean(_: JSContextRef!, _: Bool) -> JSValueRef!](https://developer.apple.com/documentation/javascriptcore/1395946-jsvaluemakeboolean)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueMakeBoolean(_ ctx: JSContextRef, _ boolean: Bool) -> JSValueRef ``` |
| To | ``` func JSValueMakeBoolean(_ ctx: JSContextRef!, _ boolean: Bool) -> JSValueRef! ``` |

Modified [JSValueMakeFromJSONString(_: JSContextRef!, _: JSStringRef!) -> JSValueRef!](https://developer.apple.com/documentation/javascriptcore/1395928-jsvaluemakefromjsonstring)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueMakeFromJSONString(_ ctx: JSContextRef, _ string: JSStringRef) -> JSValueRef ``` |
| To | ``` func JSValueMakeFromJSONString(_ ctx: JSContextRef!, _ string: JSStringRef!) -> JSValueRef! ``` |

Modified [JSValueMakeNull(_: JSContextRef!) -> JSValueRef!](https://developer.apple.com/documentation/javascriptcore/1395942-jsvaluemakenull)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueMakeNull(_ ctx: JSContextRef) -> JSValueRef ``` |
| To | ``` func JSValueMakeNull(_ ctx: JSContextRef!) -> JSValueRef! ``` |

Modified [JSValueMakeNumber(_: JSContextRef!, _: Double) -> JSValueRef!](https://developer.apple.com/documentation/javascriptcore/1395952-jsvaluemakenumber)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueMakeNumber(_ ctx: JSContextRef, _ number: Double) -> JSValueRef ``` |
| To | ``` func JSValueMakeNumber(_ ctx: JSContextRef!, _ number: Double) -> JSValueRef! ``` |

Modified [JSValueMakeString(_: JSContextRef!, _: JSStringRef!) -> JSValueRef!](https://developer.apple.com/documentation/javascriptcore/1395980-jsvaluemakestring)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueMakeString(_ ctx: JSContextRef, _ string: JSStringRef) -> JSValueRef ``` |
| To | ``` func JSValueMakeString(_ ctx: JSContextRef!, _ string: JSStringRef!) -> JSValueRef! ``` |

Modified [JSValueMakeUndefined(_: JSContextRef!) -> JSValueRef!](https://developer.apple.com/documentation/javascriptcore/1395974-jsvaluemakeundefined)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueMakeUndefined(_ ctx: JSContextRef) -> JSValueRef ``` |
| To | ``` func JSValueMakeUndefined(_ ctx: JSContextRef!) -> JSValueRef! ``` |

Modified [JSValueProtect(_: JSContextRef!, _: JSValueRef!)](https://developer.apple.com/documentation/javascriptcore/1395978-jsvalueprotect)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueProtect(_ ctx: JSContextRef, _ value: JSValueRef) ``` |
| To | ``` func JSValueProtect(_ ctx: JSContextRef!, _ value: JSValueRef!) ``` |

Modified [JSValueRef](https://developer.apple.com/documentation/javascriptcore/jsvalueref)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSValueRef = COpaquePointer ``` |
| To | ``` typealias JSValueRef = OpaquePointer ``` |

Modified [JSValueToBoolean(_: JSContextRef!, _: JSValueRef!) -> Bool](https://developer.apple.com/documentation/javascriptcore/1395930-jsvaluetoboolean)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueToBoolean(_ ctx: JSContextRef, _ value: JSValueRef) -> Bool ``` |
| To | ``` func JSValueToBoolean(_ ctx: JSContextRef!, _ value: JSValueRef!) -> Bool ``` |

Modified [JSValueToNumber(_: JSContextRef!, _: JSValueRef!, _: UnsafeMutablePointer<JSValueRef?>!) -> Double](https://developer.apple.com/documentation/javascriptcore/1395968-jsvaluetonumber)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueToNumber(_ ctx: JSContextRef, _ value: JSValueRef, _ exception: UnsafeMutablePointer<JSValueRef>) -> Double ``` |
| To | ``` func JSValueToNumber(_ ctx: JSContextRef!, _ value: JSValueRef!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> Double ``` |

Modified [JSValueToObject(_: JSContextRef!, _: JSValueRef!, _: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](https://developer.apple.com/documentation/javascriptcore/1395950-jsvaluetoobject)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueToObject(_ ctx: JSContextRef, _ value: JSValueRef, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSObjectRef ``` |
| To | ``` func JSValueToObject(_ ctx: JSContextRef!, _ value: JSValueRef!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef! ``` |

Modified [JSValueToStringCopy(_: JSContextRef!, _: JSValueRef!, _: UnsafeMutablePointer<JSValueRef?>!) -> JSStringRef!](https://developer.apple.com/documentation/javascriptcore/1395972-jsvaluetostringcopy)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueToStringCopy(_ ctx: JSContextRef, _ value: JSValueRef, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSStringRef ``` |
| To | ``` func JSValueToStringCopy(_ ctx: JSContextRef!, _ value: JSValueRef!, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSStringRef! ``` |

Modified [JSValueUnprotect(_: JSContextRef!, _: JSValueRef!)](https://developer.apple.com/documentation/javascriptcore/1395922-jsvalueunprotect)

|  | Declaration |
| --- | --- |
| From | ``` func JSValueUnprotect(_ ctx: JSContextRef, _ value: JSValueRef) ``` |
| To | ``` func JSValueUnprotect(_ ctx: JSContextRef!, _ value: JSValueRef!) ``` |

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
