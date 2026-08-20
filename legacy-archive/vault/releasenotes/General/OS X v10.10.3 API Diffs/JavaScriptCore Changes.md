---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/JavaScriptCore.html
archived_at: '2026-07-18T02:52:32.727686Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# JavaScriptCore Changes

## JavaScriptCore

Added JSClassDefinition.init()Added JSClassDefinition.init(version: Int32, attributes: JSClassAttributes, className: UnsafePointer<Int8>, parentClass: JSClassRef, staticValues: UnsafePointer<JSStaticValue>, staticFunctions: UnsafePointer<JSStaticFunction>, initialize: JSObjectInitializeCallback, finalize: JSObjectFinalizeCallback, hasProperty: JSObjectHasPropertyCallback, getProperty: JSObjectGetPropertyCallback, setProperty: JSObjectSetPropertyCallback, deleteProperty: JSObjectDeletePropertyCallback, getPropertyNames: JSObjectGetPropertyNamesCallback, callAsFunction: JSObjectCallAsFunctionCallback, callAsConstructor: JSObjectCallAsConstructorCallback, hasInstance: JSObjectHasInstanceCallback, convertToType: JSObjectConvertToTypeCallback)Added JSStaticFunction.init()Added JSStaticFunction.init(name: UnsafePointer<Int8>, callAsFunction: JSObjectCallAsFunctionCallback, attributes: JSPropertyAttributes)Added JSStaticValue.init()Added JSStaticValue.init(name: UnsafePointer<Int8>, getProperty: JSObjectGetPropertyCallback, setProperty: JSObjectSetPropertyCallback, attributes: JSPropertyAttributes)Added JSClassRelease(JSClassRef)Added JSClassRetain(JSClassRef) -> JSClassRefAdded JSContextGroupRelease(JSContextGroupRef)Added JSContextGroupRetain(JSContextGroupRef) -> JSContextGroupRefAdded JSGlobalContextRelease(JSGlobalContextRef)Added JSGlobalContextRetain(JSGlobalContextRef) -> JSGlobalContextRefAdded JSPropertyNameArrayRelease(JSPropertyNameArrayRef)Added JSPropertyNameArrayRetain(JSPropertyNameArrayRef) -> JSPropertyNameArrayRefAdded JSStringRelease(JSStringRef)Added JSStringRetain(JSStringRef) -> JSStringRefModified JSClassDefinition [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct JSClassDefinition {     var version: Int32     var attributes: JSClassAttributes     var className: ConstUnsafePointer<Int8>     var parentClass: Unmanaged<JSClass>!     var staticValues: ConstUnsafePointer<JSStaticValue>     var staticFunctions: ConstUnsafePointer<JSStaticFunction>     var initialize: JSObjectInitializeCallback     var finalize: JSObjectFinalizeCallback     var hasProperty: JSObjectHasPropertyCallback     var getProperty: JSObjectGetPropertyCallback     var setProperty: JSObjectSetPropertyCallback     var deleteProperty: JSObjectDeletePropertyCallback     var getPropertyNames: JSObjectGetPropertyNamesCallback     var callAsFunction: JSObjectCallAsFunctionCallback     var callAsConstructor: JSObjectCallAsConstructorCallback     var hasInstance: JSObjectHasInstanceCallback     var convertToType: JSObjectConvertToTypeCallback } ``` |
| To | ``` struct JSClassDefinition {     var version: Int32     var attributes: JSClassAttributes     var className: UnsafePointer<Int8>     var parentClass: JSClassRef     var staticValues: UnsafePointer<JSStaticValue>     var staticFunctions: UnsafePointer<JSStaticFunction>     var initialize: JSObjectInitializeCallback     var finalize: JSObjectFinalizeCallback     var hasProperty: JSObjectHasPropertyCallback     var getProperty: JSObjectGetPropertyCallback     var setProperty: JSObjectSetPropertyCallback     var deleteProperty: JSObjectDeletePropertyCallback     var getPropertyNames: JSObjectGetPropertyNamesCallback     var callAsFunction: JSObjectCallAsFunctionCallback     var callAsConstructor: JSObjectCallAsConstructorCallback     var hasInstance: JSObjectHasInstanceCallback     var convertToType: JSObjectConvertToTypeCallback     init()     init(version version: Int32, attributes attributes: JSClassAttributes, className className: UnsafePointer<Int8>, parentClass parentClass: JSClassRef, staticValues staticValues: UnsafePointer<JSStaticValue>, staticFunctions staticFunctions: UnsafePointer<JSStaticFunction>, initialize initialize: JSObjectInitializeCallback, finalize finalize: JSObjectFinalizeCallback, hasProperty hasProperty: JSObjectHasPropertyCallback, getProperty getProperty: JSObjectGetPropertyCallback, setProperty setProperty: JSObjectSetPropertyCallback, deleteProperty deleteProperty: JSObjectDeletePropertyCallback, getPropertyNames getPropertyNames: JSObjectGetPropertyNamesCallback, callAsFunction callAsFunction: JSObjectCallAsFunctionCallback, callAsConstructor callAsConstructor: JSObjectCallAsConstructorCallback, hasInstance hasInstance: JSObjectHasInstanceCallback, convertToType convertToType: JSObjectConvertToTypeCallback) } ``` |

Modified JSClassDefinition.className

|  | Declaration |
| --- | --- |
| From | ``` var className: ConstUnsafePointer<Int8> ``` |
| To | ``` var className: UnsafePointer<Int8> ``` |

Modified JSClassDefinition.parentClass

|  | Declaration |
| --- | --- |
| From | ``` var parentClass: Unmanaged<JSClass>! ``` |
| To | ``` var parentClass: JSClassRef ``` |

Modified JSClassDefinition.staticFunctions

|  | Declaration |
| --- | --- |
| From | ``` var staticFunctions: ConstUnsafePointer<JSStaticFunction> ``` |
| To | ``` var staticFunctions: UnsafePointer<JSStaticFunction> ``` |

Modified JSClassDefinition.staticValues

|  | Declaration |
| --- | --- |
| From | ``` var staticValues: ConstUnsafePointer<JSStaticValue> ``` |
| To | ``` var staticValues: UnsafePointer<JSStaticValue> ``` |

Modified JSContext

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified JSContext.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified JSContext.JSGlobalContextRef

|  | Declaration |
| --- | --- |
| From | ``` var JSGlobalContextRef: JSGlobalContext! { get } ``` |
| To | ``` var JSGlobalContextRef: JSGlobalContextRef { get } ``` |

Modified JSContext.init(JSGlobalContextRef: JSGlobalContextRef)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(JSGlobalContextRef jsGlobalContextRef: JSGlobalContext!) -> JSContext ``` | OS X 10.10 |
| To | ``` init!(JSGlobalContextRef jsGlobalContextRef: JSGlobalContextRef) -> JSContext ``` | OS X 10.10.3 |

Modified JSContext.init(virtualMachine: JSVirtualMachine!)

|  | Declaration |
| --- | --- |
| From | ``` init(virtualMachine virtualMachine: JSVirtualMachine!) ``` |
| To | ``` init!(virtualMachine virtualMachine: JSVirtualMachine!) ``` |

Modified JSManagedValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified JSManagedValue.init(value: JSValue!)

|  | Declaration |
| --- | --- |
| From | ``` init(value value: JSValue!) ``` |
| To | ``` init!(value value: JSValue!) ``` |

Modified JSManagedValue.init(value: JSValue!, andOwner: AnyObject!)

|  | Declaration |
| --- | --- |
| From | ``` init(value value: JSValue!, andOwner owner: AnyObject!) -> JSManagedValue ``` |
| To | ``` init!(value value: JSValue!, andOwner owner: AnyObject!) -> JSManagedValue ``` |

Modified JSStaticFunction [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct JSStaticFunction {     var name: ConstUnsafePointer<Int8>     var callAsFunction: JSObjectCallAsFunctionCallback     var attributes: JSPropertyAttributes } ``` |
| To | ``` struct JSStaticFunction {     var name: UnsafePointer<Int8>     var callAsFunction: JSObjectCallAsFunctionCallback     var attributes: JSPropertyAttributes     init()     init(name name: UnsafePointer<Int8>, callAsFunction callAsFunction: JSObjectCallAsFunctionCallback, attributes attributes: JSPropertyAttributes) } ``` |

Modified JSStaticFunction.name

|  | Declaration |
| --- | --- |
| From | ``` var name: ConstUnsafePointer<Int8> ``` |
| To | ``` var name: UnsafePointer<Int8> ``` |

Modified JSStaticValue [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct JSStaticValue {     var name: ConstUnsafePointer<Int8>     var getProperty: JSObjectGetPropertyCallback     var setProperty: JSObjectSetPropertyCallback     var attributes: JSPropertyAttributes } ``` |
| To | ``` struct JSStaticValue {     var name: UnsafePointer<Int8>     var getProperty: JSObjectGetPropertyCallback     var setProperty: JSObjectSetPropertyCallback     var attributes: JSPropertyAttributes     init()     init(name name: UnsafePointer<Int8>, getProperty getProperty: JSObjectGetPropertyCallback, setProperty setProperty: JSObjectSetPropertyCallback, attributes attributes: JSPropertyAttributes) } ``` |

Modified JSStaticValue.name

|  | Declaration |
| --- | --- |
| From | ``` var name: ConstUnsafePointer<Int8> ``` |
| To | ``` var name: UnsafePointer<Int8> ``` |

Modified JSValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified JSValue.JSValueRef

|  | Declaration |
| --- | --- |
| From | ``` var JSValueRef: JSValue! { get } ``` |
| To | ``` var JSValueRef: JSValueRef { get } ``` |

Modified JSValue.init(JSValueRef: JSValueRef, inContext: JSContext!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(JSValueRef value: JSValue!, inContext context: JSContext!) -> JSValue ``` | OS X 10.10 |
| To | ``` init!(JSValueRef value: JSValueRef, inContext context: JSContext!) -> JSValue ``` | OS X 10.10.3 |

Modified JSValue.init(UInt32: UInt32, inContext: JSContext!)

|  | Declaration |
| --- | --- |
| From | ``` init(UInt32 value: UInt32, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(UInt32 value: UInt32, inContext context: JSContext!) -> JSValue ``` |

Modified JSValue.init(bool: Bool, inContext: JSContext!)

|  | Declaration |
| --- | --- |
| From | ``` init(bool value: Bool, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(bool value: Bool, inContext context: JSContext!) -> JSValue ``` |

Modified JSValue.init(double: Double, inContext: JSContext!)

|  | Declaration |
| --- | --- |
| From | ``` init(double value: Double, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(double value: Double, inContext context: JSContext!) -> JSValue ``` |

Modified JSValue.init(int32: Int32, inContext: JSContext!)

|  | Declaration |
| --- | --- |
| From | ``` init(int32 value: Int32, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(int32 value: Int32, inContext context: JSContext!) -> JSValue ``` |

Modified JSValue.init(newArrayInContext: JSContext!)

|  | Declaration |
| --- | --- |
| From | ``` init(newArrayInContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(newArrayInContext context: JSContext!) -> JSValue ``` |

Modified JSValue.init(newErrorFromMessage: String!, inContext: JSContext!)

|  | Declaration |
| --- | --- |
| From | ``` init(newErrorFromMessage message: String!, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(newErrorFromMessage message: String!, inContext context: JSContext!) -> JSValue ``` |

Modified JSValue.init(newObjectInContext: JSContext!)

|  | Declaration |
| --- | --- |
| From | ``` init(newObjectInContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(newObjectInContext context: JSContext!) -> JSValue ``` |

Modified JSValue.init(newRegularExpressionFromPattern: String!, flags: String!, inContext: JSContext!)

|  | Declaration |
| --- | --- |
| From | ``` init(newRegularExpressionFromPattern pattern: String!, flags flags: String!, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(newRegularExpressionFromPattern pattern: String!, flags flags: String!, inContext context: JSContext!) -> JSValue ``` |

Modified JSValue.init(nullInContext: JSContext!)

|  | Declaration |
| --- | --- |
| From | ``` init(nullInContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(nullInContext context: JSContext!) -> JSValue ``` |

Modified JSValue.init(object: AnyObject!, inContext: JSContext!)

|  | Declaration |
| --- | --- |
| From | ``` init(object value: AnyObject!, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(object value: AnyObject!, inContext context: JSContext!) -> JSValue ``` |

Modified JSValue.init(point: CGPoint, inContext: JSContext!)

|  | Declaration |
| --- | --- |
| From | ``` init(point point: CGPoint, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(point point: CGPoint, inContext context: JSContext!) -> JSValue ``` |

Modified JSValue.init(range: NSRange, inContext: JSContext!)

|  | Declaration |
| --- | --- |
| From | ``` init(range range: NSRange, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(range range: NSRange, inContext context: JSContext!) -> JSValue ``` |

Modified JSValue.init(rect: CGRect, inContext: JSContext!)

|  | Declaration |
| --- | --- |
| From | ``` init(rect rect: CGRect, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(rect rect: CGRect, inContext context: JSContext!) -> JSValue ``` |

Modified JSValue.init(size: CGSize, inContext: JSContext!)

|  | Declaration |
| --- | --- |
| From | ``` init(size size: CGSize, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(size size: CGSize, inContext context: JSContext!) -> JSValue ``` |

Modified JSValue.init(undefinedInContext: JSContext!)

|  | Declaration |
| --- | --- |
| From | ``` init(undefinedInContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(undefinedInContext context: JSContext!) -> JSValue ``` |

Modified JSVirtualMachine

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified JSVirtualMachine.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified JSCheckScriptSyntax(JSContextRef, JSStringRef, JSStringRef, Int32, UnsafeMutablePointer<JSValueRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSCheckScriptSyntax(_ ctx: JSContext!, _ script: JSString!, _ sourceURL: JSString!, _ startingLineNumber: Int32, _ exception: UnsafePointer<Unmanaged<JSValue>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func JSCheckScriptSyntax(_ ctx: JSContextRef, _ script: JSStringRef, _ sourceURL: JSStringRef, _ startingLineNumber: Int32, _ exception: UnsafeMutablePointer<JSValueRef>) -> Bool ``` | OS X 10.10.3 |

Modified JSClassCreate(UnsafePointer<JSClassDefinition>) -> JSClassRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSClassCreate(_ definition: ConstUnsafePointer<JSClassDefinition>) -> Unmanaged<JSClass>! ``` | OS X 10.10 |
| To | ``` func JSClassCreate(_ definition: UnsafePointer<JSClassDefinition>) -> JSClassRef ``` | OS X 10.10.3 |

Modified JSClassRef

|  | Declaration |
| --- | --- |
| From | ``` typealias JSClassRef = JSClass ``` |
| To | ``` typealias JSClassRef = COpaquePointer ``` |

Modified JSContextGetGlobalContext(JSContextRef) -> JSGlobalContextRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSContextGetGlobalContext(_ ctx: JSContext!) -> Unmanaged<JSGlobalContext>! ``` | OS X 10.10 |
| To | ``` func JSContextGetGlobalContext(_ ctx: JSContextRef) -> JSGlobalContextRef ``` | OS X 10.7 |

Modified JSContextGetGlobalObject(JSContextRef) -> JSObjectRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSContextGetGlobalObject(_ ctx: JSContext!) -> Unmanaged<JSObject>! ``` | OS X 10.10 |
| To | ``` func JSContextGetGlobalObject(_ ctx: JSContextRef) -> JSObjectRef ``` | OS X 10.10.3 |

Modified JSContextGetGroup(JSContextRef) -> JSContextGroupRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSContextGetGroup(_ ctx: JSContext!) -> Unmanaged<JSContextGroup>! ``` | OS X 10.10 |
| To | ``` func JSContextGetGroup(_ ctx: JSContextRef) -> JSContextGroupRef ``` | OS X 10.6 |

Modified JSContextGroupCreate() -> JSContextGroupRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSContextGroupCreate() -> Unmanaged<JSContextGroup>! ``` | OS X 10.10 |
| To | ``` func JSContextGroupCreate() -> JSContextGroupRef ``` | OS X 10.6 |

Modified JSContextGroupRef

|  | Declaration |
| --- | --- |
| From | ``` typealias JSContextGroupRef = JSContextGroup ``` |
| To | ``` typealias JSContextGroupRef = COpaquePointer ``` |

Modified JSContextRef

|  | Declaration |
| --- | --- |
| From | ``` typealias JSContextRef = JSContext ``` |
| To | ``` typealias JSContextRef = COpaquePointer ``` |

Modified JSEvaluateScript(JSContextRef, JSStringRef, JSObjectRef, JSStringRef, Int32, UnsafeMutablePointer<JSValueRef>) -> JSValueRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSEvaluateScript(_ ctx: JSContext!, _ script: JSString!, _ thisObject: JSObject!, _ sourceURL: JSString!, _ startingLineNumber: Int32, _ exception: UnsafePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSValue>! ``` | OS X 10.10 |
| To | ``` func JSEvaluateScript(_ ctx: JSContextRef, _ script: JSStringRef, _ thisObject: JSObjectRef, _ sourceURL: JSStringRef, _ startingLineNumber: Int32, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSValueRef ``` | OS X 10.10.3 |

Modified JSGarbageCollect(JSContextRef)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSGarbageCollect(_ ctx: JSContext!) ``` | OS X 10.10 |
| To | ``` func JSGarbageCollect(_ ctx: JSContextRef) ``` | OS X 10.10.3 |

Modified JSGlobalContextCopyName(JSGlobalContextRef) -> JSStringRef

|  | Declaration |
| --- | --- |
| From | ``` func JSGlobalContextCopyName(_ ctx: JSGlobalContext!) -> Unmanaged<JSString>! ``` |
| To | ``` func JSGlobalContextCopyName(_ ctx: JSGlobalContextRef) -> JSStringRef ``` |

Modified JSGlobalContextCreate(JSClassRef) -> JSGlobalContextRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSGlobalContextCreate(_ globalObjectClass: JSClass!) -> Unmanaged<JSGlobalContext>! ``` | OS X 10.10 |
| To | ``` func JSGlobalContextCreate(_ globalObjectClass: JSClassRef) -> JSGlobalContextRef ``` | OS X 10.5 |

Modified JSGlobalContextCreateInGroup(JSContextGroupRef, JSClassRef) -> JSGlobalContextRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSGlobalContextCreateInGroup(_ group: JSContextGroup!, _ globalObjectClass: JSClass!) -> Unmanaged<JSGlobalContext>! ``` | OS X 10.10 |
| To | ``` func JSGlobalContextCreateInGroup(_ group: JSContextGroupRef, _ globalObjectClass: JSClassRef) -> JSGlobalContextRef ``` | OS X 10.6 |

Modified JSGlobalContextRef

|  | Declaration |
| --- | --- |
| From | ``` typealias JSGlobalContextRef = JSGlobalContext ``` |
| To | ``` typealias JSGlobalContextRef = COpaquePointer ``` |

Modified JSGlobalContextSetName(JSGlobalContextRef, JSStringRef)

|  | Declaration |
| --- | --- |
| From | ``` func JSGlobalContextSetName(_ ctx: JSGlobalContext!, _ name: JSString!) ``` |
| To | ``` func JSGlobalContextSetName(_ ctx: JSGlobalContextRef, _ name: JSStringRef) ``` |

Modified JSObjectCallAsConstructor(JSContextRef, JSObjectRef, Int, UnsafePointer<JSValueRef>, UnsafeMutablePointer<JSValueRef>) -> JSObjectRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectCallAsConstructor(_ ctx: JSContext!, _ object: JSObject!, _ argumentCount: UInt, _ arguments: ConstUnsafePointer<Unmanaged<JSValue>?>, _ exception: UnsafePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSObject>! ``` | OS X 10.10 |
| To | ``` func JSObjectCallAsConstructor(_ ctx: JSContextRef, _ object: JSObjectRef, _ argumentCount: Int, _ arguments: UnsafePointer<JSValueRef>, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSObjectRef ``` | OS X 10.10.3 |

Modified JSObjectCallAsConstructorCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectCallAsConstructorCallback = CFunctionPointer<((JSContext!, JSObject!, UInt, ConstUnsafePointer<Unmanaged<JSValue>?>, UnsafePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSObject>!)> ``` |
| To | ``` typealias JSObjectCallAsConstructorCallback = CFunctionPointer<((JSContextRef, JSObjectRef, Int, UnsafePointer<JSValueRef>, UnsafeMutablePointer<JSValueRef>) -> JSObjectRef)> ``` |

Modified JSObjectCallAsFunction(JSContextRef, JSObjectRef, JSObjectRef, Int, UnsafePointer<JSValueRef>, UnsafeMutablePointer<JSValueRef>) -> JSValueRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectCallAsFunction(_ ctx: JSContext!, _ object: JSObject!, _ thisObject: JSObject!, _ argumentCount: UInt, _ arguments: ConstUnsafePointer<Unmanaged<JSValue>?>, _ exception: UnsafePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSValue>! ``` | OS X 10.10 |
| To | ``` func JSObjectCallAsFunction(_ ctx: JSContextRef, _ object: JSObjectRef, _ thisObject: JSObjectRef, _ argumentCount: Int, _ arguments: UnsafePointer<JSValueRef>, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSValueRef ``` | OS X 10.10.3 |

Modified JSObjectCallAsFunctionCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectCallAsFunctionCallback = CFunctionPointer<((JSContext!, JSObject!, JSObject!, UInt, ConstUnsafePointer<Unmanaged<JSValue>?>, UnsafePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSValue>!)> ``` |
| To | ``` typealias JSObjectCallAsFunctionCallback = CFunctionPointer<((JSContextRef, JSObjectRef, JSObjectRef, Int, UnsafePointer<JSValueRef>, UnsafeMutablePointer<JSValueRef>) -> JSValueRef)> ``` |

Modified JSObjectConvertToTypeCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectConvertToTypeCallback = CFunctionPointer<((JSContext!, JSObject!, JSType, UnsafePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSValue>!)> ``` |
| To | ``` typealias JSObjectConvertToTypeCallback = CFunctionPointer<((JSContextRef, JSObjectRef, JSType, UnsafeMutablePointer<JSValueRef>) -> JSValueRef)> ``` |

Modified JSObjectCopyPropertyNames(JSContextRef, JSObjectRef) -> JSPropertyNameArrayRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectCopyPropertyNames(_ ctx: JSContext!, _ object: JSObject!) -> Unmanaged<JSPropertyNameArray>! ``` | OS X 10.10 |
| To | ``` func JSObjectCopyPropertyNames(_ ctx: JSContextRef, _ object: JSObjectRef) -> JSPropertyNameArrayRef ``` | OS X 10.10.3 |

Modified JSObjectDeleteProperty(JSContextRef, JSObjectRef, JSStringRef, UnsafeMutablePointer<JSValueRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectDeleteProperty(_ ctx: JSContext!, _ object: JSObject!, _ propertyName: JSString!, _ exception: UnsafePointer<Unmanaged<JSValue>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func JSObjectDeleteProperty(_ ctx: JSContextRef, _ object: JSObjectRef, _ propertyName: JSStringRef, _ exception: UnsafeMutablePointer<JSValueRef>) -> Bool ``` | OS X 10.10.3 |

Modified JSObjectDeletePropertyCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectDeletePropertyCallback = CFunctionPointer<((JSContext!, JSObject!, JSString!, UnsafePointer<Unmanaged<JSValue>?>) -> Bool)> ``` |
| To | ``` typealias JSObjectDeletePropertyCallback = CFunctionPointer<((JSContextRef, JSObjectRef, JSStringRef, UnsafeMutablePointer<JSValueRef>) -> Bool)> ``` |

Modified JSObjectFinalizeCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectFinalizeCallback = CFunctionPointer<((JSObject!) -> Void)> ``` |
| To | ``` typealias JSObjectFinalizeCallback = CFunctionPointer<((JSObjectRef) -> Void)> ``` |

Modified JSObjectGetPrivate(JSObjectRef) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectGetPrivate(_ object: JSObject!) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func JSObjectGetPrivate(_ object: JSObjectRef) -> UnsafeMutablePointer<Void> ``` | OS X 10.10.3 |

Modified JSObjectGetProperty(JSContextRef, JSObjectRef, JSStringRef, UnsafeMutablePointer<JSValueRef>) -> JSValueRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectGetProperty(_ ctx: JSContext!, _ object: JSObject!, _ propertyName: JSString!, _ exception: UnsafePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSValue>! ``` | OS X 10.10 |
| To | ``` func JSObjectGetProperty(_ ctx: JSContextRef, _ object: JSObjectRef, _ propertyName: JSStringRef, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSValueRef ``` | OS X 10.10.3 |

Modified JSObjectGetPropertyAtIndex(JSContextRef, JSObjectRef, UInt32, UnsafeMutablePointer<JSValueRef>) -> JSValueRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectGetPropertyAtIndex(_ ctx: JSContext!, _ object: JSObject!, _ propertyIndex: UInt32, _ exception: UnsafePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSValue>! ``` | OS X 10.10 |
| To | ``` func JSObjectGetPropertyAtIndex(_ ctx: JSContextRef, _ object: JSObjectRef, _ propertyIndex: UInt32, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSValueRef ``` | OS X 10.10.3 |

Modified JSObjectGetPropertyCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectGetPropertyCallback = CFunctionPointer<((JSContext!, JSObject!, JSString!, UnsafePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSValue>!)> ``` |
| To | ``` typealias JSObjectGetPropertyCallback = CFunctionPointer<((JSContextRef, JSObjectRef, JSStringRef, UnsafeMutablePointer<JSValueRef>) -> JSValueRef)> ``` |

Modified JSObjectGetPropertyNamesCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectGetPropertyNamesCallback = CFunctionPointer<((JSContext!, JSObject!, JSPropertyNameAccumulator!) -> Void)> ``` |
| To | ``` typealias JSObjectGetPropertyNamesCallback = CFunctionPointer<((JSContextRef, JSObjectRef, JSPropertyNameAccumulatorRef) -> Void)> ``` |

Modified JSObjectGetPrototype(JSContextRef, JSObjectRef) -> JSValueRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectGetPrototype(_ ctx: JSContext!, _ object: JSObject!) -> Unmanaged<JSValue>! ``` | OS X 10.10 |
| To | ``` func JSObjectGetPrototype(_ ctx: JSContextRef, _ object: JSObjectRef) -> JSValueRef ``` | OS X 10.10.3 |

Modified JSObjectHasInstanceCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectHasInstanceCallback = CFunctionPointer<((JSContext!, JSObject!, JSValue!, UnsafePointer<Unmanaged<JSValue>?>) -> Bool)> ``` |
| To | ``` typealias JSObjectHasInstanceCallback = CFunctionPointer<((JSContextRef, JSObjectRef, JSValueRef, UnsafeMutablePointer<JSValueRef>) -> Bool)> ``` |

Modified JSObjectHasProperty(JSContextRef, JSObjectRef, JSStringRef) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectHasProperty(_ ctx: JSContext!, _ object: JSObject!, _ propertyName: JSString!) -> Bool ``` | OS X 10.10 |
| To | ``` func JSObjectHasProperty(_ ctx: JSContextRef, _ object: JSObjectRef, _ propertyName: JSStringRef) -> Bool ``` | OS X 10.10.3 |

Modified JSObjectHasPropertyCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectHasPropertyCallback = CFunctionPointer<((JSContext!, JSObject!, JSString!) -> Bool)> ``` |
| To | ``` typealias JSObjectHasPropertyCallback = CFunctionPointer<((JSContextRef, JSObjectRef, JSStringRef) -> Bool)> ``` |

Modified JSObjectInitializeCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectInitializeCallback = CFunctionPointer<((JSContext!, JSObject!) -> Void)> ``` |
| To | ``` typealias JSObjectInitializeCallback = CFunctionPointer<((JSContextRef, JSObjectRef) -> Void)> ``` |

Modified JSObjectIsConstructor(JSContextRef, JSObjectRef) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectIsConstructor(_ ctx: JSContext!, _ object: JSObject!) -> Bool ``` | OS X 10.10 |
| To | ``` func JSObjectIsConstructor(_ ctx: JSContextRef, _ object: JSObjectRef) -> Bool ``` | OS X 10.10.3 |

Modified JSObjectIsFunction(JSContextRef, JSObjectRef) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectIsFunction(_ ctx: JSContext!, _ object: JSObject!) -> Bool ``` | OS X 10.10 |
| To | ``` func JSObjectIsFunction(_ ctx: JSContextRef, _ object: JSObjectRef) -> Bool ``` | OS X 10.10.3 |

Modified JSObjectMake(JSContextRef, JSClassRef, UnsafeMutablePointer<Void>) -> JSObjectRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectMake(_ ctx: JSContext!, _ jsClass: JSClass!, _ data: UnsafePointer<()>) -> Unmanaged<JSObject>! ``` | OS X 10.10 |
| To | ``` func JSObjectMake(_ ctx: JSContextRef, _ jsClass: JSClassRef, _ data: UnsafeMutablePointer<Void>) -> JSObjectRef ``` | OS X 10.10.3 |

Modified JSObjectMakeArray(JSContextRef, Int, UnsafePointer<JSValueRef>, UnsafeMutablePointer<JSValueRef>) -> JSObjectRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectMakeArray(_ ctx: JSContext!, _ argumentCount: UInt, _ arguments: ConstUnsafePointer<Unmanaged<JSValue>?>, _ exception: UnsafePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSObject>! ``` | OS X 10.10 |
| To | ``` func JSObjectMakeArray(_ ctx: JSContextRef, _ argumentCount: Int, _ arguments: UnsafePointer<JSValueRef>, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSObjectRef ``` | OS X 10.6 |

Modified JSObjectMakeConstructor(JSContextRef, JSClassRef, JSObjectCallAsConstructorCallback) -> JSObjectRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectMakeConstructor(_ ctx: JSContext!, _ jsClass: JSClass!, _ callAsConstructor: JSObjectCallAsConstructorCallback) -> Unmanaged<JSObject>! ``` | OS X 10.10 |
| To | ``` func JSObjectMakeConstructor(_ ctx: JSContextRef, _ jsClass: JSClassRef, _ callAsConstructor: JSObjectCallAsConstructorCallback) -> JSObjectRef ``` | OS X 10.10.3 |

Modified JSObjectMakeDate(JSContextRef, Int, UnsafePointer<JSValueRef>, UnsafeMutablePointer<JSValueRef>) -> JSObjectRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectMakeDate(_ ctx: JSContext!, _ argumentCount: UInt, _ arguments: ConstUnsafePointer<Unmanaged<JSValue>?>, _ exception: UnsafePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSObject>! ``` | OS X 10.10 |
| To | ``` func JSObjectMakeDate(_ ctx: JSContextRef, _ argumentCount: Int, _ arguments: UnsafePointer<JSValueRef>, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSObjectRef ``` | OS X 10.6 |

Modified JSObjectMakeError(JSContextRef, Int, UnsafePointer<JSValueRef>, UnsafeMutablePointer<JSValueRef>) -> JSObjectRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectMakeError(_ ctx: JSContext!, _ argumentCount: UInt, _ arguments: ConstUnsafePointer<Unmanaged<JSValue>?>, _ exception: UnsafePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSObject>! ``` | OS X 10.10 |
| To | ``` func JSObjectMakeError(_ ctx: JSContextRef, _ argumentCount: Int, _ arguments: UnsafePointer<JSValueRef>, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSObjectRef ``` | OS X 10.6 |

Modified JSObjectMakeFunction(JSContextRef, JSStringRef, UInt32, UnsafePointer<JSStringRef>, JSStringRef, JSStringRef, Int32, UnsafeMutablePointer<JSValueRef>) -> JSObjectRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectMakeFunction(_ ctx: JSContext!, _ name: JSString!, _ parameterCount: UInt32, _ parameterNames: ConstUnsafePointer<Unmanaged<JSString>?>, _ body: JSString!, _ sourceURL: JSString!, _ startingLineNumber: Int32, _ exception: UnsafePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSObject>! ``` | OS X 10.10 |
| To | ``` func JSObjectMakeFunction(_ ctx: JSContextRef, _ name: JSStringRef, _ parameterCount: UInt32, _ parameterNames: UnsafePointer<JSStringRef>, _ body: JSStringRef, _ sourceURL: JSStringRef, _ startingLineNumber: Int32, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSObjectRef ``` | OS X 10.10.3 |

Modified JSObjectMakeFunctionWithCallback(JSContextRef, JSStringRef, JSObjectCallAsFunctionCallback) -> JSObjectRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectMakeFunctionWithCallback(_ ctx: JSContext!, _ name: JSString!, _ callAsFunction: JSObjectCallAsFunctionCallback) -> Unmanaged<JSObject>! ``` | OS X 10.10 |
| To | ``` func JSObjectMakeFunctionWithCallback(_ ctx: JSContextRef, _ name: JSStringRef, _ callAsFunction: JSObjectCallAsFunctionCallback) -> JSObjectRef ``` | OS X 10.10.3 |

Modified JSObjectMakeRegExp(JSContextRef, Int, UnsafePointer<JSValueRef>, UnsafeMutablePointer<JSValueRef>) -> JSObjectRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectMakeRegExp(_ ctx: JSContext!, _ argumentCount: UInt, _ arguments: ConstUnsafePointer<Unmanaged<JSValue>?>, _ exception: UnsafePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSObject>! ``` | OS X 10.10 |
| To | ``` func JSObjectMakeRegExp(_ ctx: JSContextRef, _ argumentCount: Int, _ arguments: UnsafePointer<JSValueRef>, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSObjectRef ``` | OS X 10.6 |

Modified JSObjectRef

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectRef = JSObject ``` |
| To | ``` typealias JSObjectRef = COpaquePointer ``` |

Modified JSObjectSetPrivate(JSObjectRef, UnsafeMutablePointer<Void>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectSetPrivate(_ object: JSObject!, _ data: UnsafePointer<()>) -> Bool ``` | OS X 10.10 |
| To | ``` func JSObjectSetPrivate(_ object: JSObjectRef, _ data: UnsafeMutablePointer<Void>) -> Bool ``` | OS X 10.10.3 |

Modified JSObjectSetProperty(JSContextRef, JSObjectRef, JSStringRef, JSValueRef, JSPropertyAttributes, UnsafeMutablePointer<JSValueRef>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectSetProperty(_ ctx: JSContext!, _ object: JSObject!, _ propertyName: JSString!, _ value: JSValue!, _ attributes: JSPropertyAttributes, _ exception: UnsafePointer<Unmanaged<JSValue>?>) ``` | OS X 10.10 |
| To | ``` func JSObjectSetProperty(_ ctx: JSContextRef, _ object: JSObjectRef, _ propertyName: JSStringRef, _ value: JSValueRef, _ attributes: JSPropertyAttributes, _ exception: UnsafeMutablePointer<JSValueRef>) ``` | OS X 10.10.3 |

Modified JSObjectSetPropertyAtIndex(JSContextRef, JSObjectRef, UInt32, JSValueRef, UnsafeMutablePointer<JSValueRef>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectSetPropertyAtIndex(_ ctx: JSContext!, _ object: JSObject!, _ propertyIndex: UInt32, _ value: JSValue!, _ exception: UnsafePointer<Unmanaged<JSValue>?>) ``` | OS X 10.10 |
| To | ``` func JSObjectSetPropertyAtIndex(_ ctx: JSContextRef, _ object: JSObjectRef, _ propertyIndex: UInt32, _ value: JSValueRef, _ exception: UnsafeMutablePointer<JSValueRef>) ``` | OS X 10.10.3 |

Modified JSObjectSetPropertyCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectSetPropertyCallback = CFunctionPointer<((JSContext!, JSObject!, JSString!, JSValue!, UnsafePointer<Unmanaged<JSValue>?>) -> Bool)> ``` |
| To | ``` typealias JSObjectSetPropertyCallback = CFunctionPointer<((JSContextRef, JSObjectRef, JSStringRef, JSValueRef, UnsafeMutablePointer<JSValueRef>) -> Bool)> ``` |

Modified JSObjectSetPrototype(JSContextRef, JSObjectRef, JSValueRef)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSObjectSetPrototype(_ ctx: JSContext!, _ object: JSObject!, _ value: JSValue!) ``` | OS X 10.10 |
| To | ``` func JSObjectSetPrototype(_ ctx: JSContextRef, _ object: JSObjectRef, _ value: JSValueRef) ``` | OS X 10.10.3 |

Modified JSPropertyDescriptorConfigurableKey

|  | Declaration |
| --- | --- |
| From | ``` let JSPropertyDescriptorConfigurableKey: NSString! ``` |
| To | ``` let JSPropertyDescriptorConfigurableKey: String ``` |

Modified JSPropertyDescriptorEnumerableKey

|  | Declaration |
| --- | --- |
| From | ``` let JSPropertyDescriptorEnumerableKey: NSString! ``` |
| To | ``` let JSPropertyDescriptorEnumerableKey: String ``` |

Modified JSPropertyDescriptorGetKey

|  | Declaration |
| --- | --- |
| From | ``` let JSPropertyDescriptorGetKey: NSString! ``` |
| To | ``` let JSPropertyDescriptorGetKey: String ``` |

Modified JSPropertyDescriptorSetKey

|  | Declaration |
| --- | --- |
| From | ``` let JSPropertyDescriptorSetKey: NSString! ``` |
| To | ``` let JSPropertyDescriptorSetKey: String ``` |

Modified JSPropertyDescriptorValueKey

|  | Declaration |
| --- | --- |
| From | ``` let JSPropertyDescriptorValueKey: NSString! ``` |
| To | ``` let JSPropertyDescriptorValueKey: String ``` |

Modified JSPropertyDescriptorWritableKey

|  | Declaration |
| --- | --- |
| From | ``` let JSPropertyDescriptorWritableKey: NSString! ``` |
| To | ``` let JSPropertyDescriptorWritableKey: String ``` |

Modified JSPropertyNameAccumulatorAddName(JSPropertyNameAccumulatorRef, JSStringRef)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSPropertyNameAccumulatorAddName(_ accumulator: JSPropertyNameAccumulator!, _ propertyName: JSString!) ``` | OS X 10.10 |
| To | ``` func JSPropertyNameAccumulatorAddName(_ accumulator: JSPropertyNameAccumulatorRef, _ propertyName: JSStringRef) ``` | OS X 10.10.3 |

Modified JSPropertyNameAccumulatorRef

|  | Declaration |
| --- | --- |
| From | ``` typealias JSPropertyNameAccumulatorRef = JSPropertyNameAccumulator ``` |
| To | ``` typealias JSPropertyNameAccumulatorRef = COpaquePointer ``` |

Modified JSPropertyNameArrayGetCount(JSPropertyNameArrayRef) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSPropertyNameArrayGetCount(_ array: JSPropertyNameArray!) -> UInt ``` | OS X 10.10 |
| To | ``` func JSPropertyNameArrayGetCount(_ array: JSPropertyNameArrayRef) -> Int ``` | OS X 10.10.3 |

Modified JSPropertyNameArrayGetNameAtIndex(JSPropertyNameArrayRef, Int) -> JSStringRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSPropertyNameArrayGetNameAtIndex(_ array: JSPropertyNameArray!, _ index: UInt) -> Unmanaged<JSString>! ``` | OS X 10.10 |
| To | ``` func JSPropertyNameArrayGetNameAtIndex(_ array: JSPropertyNameArrayRef, _ index: Int) -> JSStringRef ``` | OS X 10.10.3 |

Modified JSPropertyNameArrayRef

|  | Declaration |
| --- | --- |
| From | ``` typealias JSPropertyNameArrayRef = JSPropertyNameArray ``` |
| To | ``` typealias JSPropertyNameArrayRef = COpaquePointer ``` |

Modified JSStringCopyCFString(CFAllocator!, JSStringRef) -> CFString!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSStringCopyCFString(_ alloc: CFAllocator!, _ string: JSString!) -> CFString! ``` | OS X 10.10 |
| To | ``` func JSStringCopyCFString(_ alloc: CFAllocator!, _ string: JSStringRef) -> CFString! ``` | OS X 10.10.3 |

Modified JSStringCreateWithCFString(CFString!) -> JSStringRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSStringCreateWithCFString(_ string: CFString!) -> Unmanaged<JSString>! ``` | OS X 10.10 |
| To | ``` func JSStringCreateWithCFString(_ string: CFString!) -> JSStringRef ``` | OS X 10.10.3 |

Modified JSStringCreateWithCharacters(UnsafePointer<JSChar>, Int) -> JSStringRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSStringCreateWithCharacters(_ chars: ConstUnsafePointer<JSChar>, _ numChars: UInt) -> Unmanaged<JSString>! ``` | OS X 10.10 |
| To | ``` func JSStringCreateWithCharacters(_ chars: UnsafePointer<JSChar>, _ numChars: Int) -> JSStringRef ``` | OS X 10.10.3 |

Modified JSStringCreateWithUTF8CString(UnsafePointer<Int8>) -> JSStringRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSStringCreateWithUTF8CString(_ string: ConstUnsafePointer<Int8>) -> Unmanaged<JSString>! ``` | OS X 10.10 |
| To | ``` func JSStringCreateWithUTF8CString(_ string: UnsafePointer<Int8>) -> JSStringRef ``` | OS X 10.10.3 |

Modified JSStringGetCharactersPtr(JSStringRef) -> UnsafePointer<JSChar>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSStringGetCharactersPtr(_ string: JSString!) -> ConstUnsafePointer<JSChar> ``` | OS X 10.10 |
| To | ``` func JSStringGetCharactersPtr(_ string: JSStringRef) -> UnsafePointer<JSChar> ``` | OS X 10.10.3 |

Modified JSStringGetLength(JSStringRef) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSStringGetLength(_ string: JSString!) -> UInt ``` | OS X 10.10 |
| To | ``` func JSStringGetLength(_ string: JSStringRef) -> Int ``` | OS X 10.10.3 |

Modified JSStringGetMaximumUTF8CStringSize(JSStringRef) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSStringGetMaximumUTF8CStringSize(_ string: JSString!) -> UInt ``` | OS X 10.10 |
| To | ``` func JSStringGetMaximumUTF8CStringSize(_ string: JSStringRef) -> Int ``` | OS X 10.10.3 |

Modified JSStringGetUTF8CString(JSStringRef, UnsafeMutablePointer<Int8>, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSStringGetUTF8CString(_ string: JSString!, _ buffer: UnsafePointer<Int8>, _ bufferSize: UInt) -> UInt ``` | OS X 10.10 |
| To | ``` func JSStringGetUTF8CString(_ string: JSStringRef, _ buffer: UnsafeMutablePointer<Int8>, _ bufferSize: Int) -> Int ``` | OS X 10.10.3 |

Modified JSStringIsEqual(JSStringRef, JSStringRef) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSStringIsEqual(_ a: JSString!, _ b: JSString!) -> Bool ``` | OS X 10.10 |
| To | ``` func JSStringIsEqual(_ a: JSStringRef, _ b: JSStringRef) -> Bool ``` | OS X 10.10.3 |

Modified JSStringIsEqualToUTF8CString(JSStringRef, UnsafePointer<Int8>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSStringIsEqualToUTF8CString(_ a: JSString!, _ b: ConstUnsafePointer<Int8>) -> Bool ``` | OS X 10.10 |
| To | ``` func JSStringIsEqualToUTF8CString(_ a: JSStringRef, _ b: UnsafePointer<Int8>) -> Bool ``` | OS X 10.10.3 |

Modified JSStringRef

|  | Declaration |
| --- | --- |
| From | ``` typealias JSStringRef = JSString ``` |
| To | ``` typealias JSStringRef = COpaquePointer ``` |

Modified JSValueCreateJSONString(JSContextRef, JSValueRef, UInt32, UnsafeMutablePointer<JSValueRef>) -> JSStringRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueCreateJSONString(_ ctx: JSContext!, _ value: JSValue!, _ indent: UInt32, _ exception: UnsafePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSString>! ``` | OS X 10.10 |
| To | ``` func JSValueCreateJSONString(_ ctx: JSContextRef, _ value: JSValueRef, _ indent: UInt32, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSStringRef ``` | OS X 10.7 |

Modified JSValueGetType(JSContextRef, JSValueRef) -> JSType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueGetType(_ ctx: JSContext!, _ _: JSValue!) -> JSType ``` | OS X 10.10 |
| To | ``` func JSValueGetType(_ ctx: JSContextRef, _ _: JSValueRef) -> JSType ``` | OS X 10.10.3 |

Modified JSValueIsBoolean(JSContextRef, JSValueRef) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueIsBoolean(_ ctx: JSContext!, _ value: JSValue!) -> Bool ``` | OS X 10.10 |
| To | ``` func JSValueIsBoolean(_ ctx: JSContextRef, _ value: JSValueRef) -> Bool ``` | OS X 10.10.3 |

Modified JSValueIsEqual(JSContextRef, JSValueRef, JSValueRef, UnsafeMutablePointer<JSValueRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueIsEqual(_ ctx: JSContext!, _ a: JSValue!, _ b: JSValue!, _ exception: UnsafePointer<Unmanaged<JSValue>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func JSValueIsEqual(_ ctx: JSContextRef, _ a: JSValueRef, _ b: JSValueRef, _ exception: UnsafeMutablePointer<JSValueRef>) -> Bool ``` | OS X 10.10.3 |

Modified JSValueIsInstanceOfConstructor(JSContextRef, JSValueRef, JSObjectRef, UnsafeMutablePointer<JSValueRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueIsInstanceOfConstructor(_ ctx: JSContext!, _ value: JSValue!, _ constructor: JSObject!, _ exception: UnsafePointer<Unmanaged<JSValue>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func JSValueIsInstanceOfConstructor(_ ctx: JSContextRef, _ value: JSValueRef, _ constructor: JSObjectRef, _ exception: UnsafeMutablePointer<JSValueRef>) -> Bool ``` | OS X 10.10.3 |

Modified JSValueIsNull(JSContextRef, JSValueRef) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueIsNull(_ ctx: JSContext!, _ value: JSValue!) -> Bool ``` | OS X 10.10 |
| To | ``` func JSValueIsNull(_ ctx: JSContextRef, _ value: JSValueRef) -> Bool ``` | OS X 10.10.3 |

Modified JSValueIsNumber(JSContextRef, JSValueRef) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueIsNumber(_ ctx: JSContext!, _ value: JSValue!) -> Bool ``` | OS X 10.10 |
| To | ``` func JSValueIsNumber(_ ctx: JSContextRef, _ value: JSValueRef) -> Bool ``` | OS X 10.10.3 |

Modified JSValueIsObject(JSContextRef, JSValueRef) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueIsObject(_ ctx: JSContext!, _ value: JSValue!) -> Bool ``` | OS X 10.10 |
| To | ``` func JSValueIsObject(_ ctx: JSContextRef, _ value: JSValueRef) -> Bool ``` | OS X 10.10.3 |

Modified JSValueIsObjectOfClass(JSContextRef, JSValueRef, JSClassRef) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueIsObjectOfClass(_ ctx: JSContext!, _ value: JSValue!, _ jsClass: JSClass!) -> Bool ``` | OS X 10.10 |
| To | ``` func JSValueIsObjectOfClass(_ ctx: JSContextRef, _ value: JSValueRef, _ jsClass: JSClassRef) -> Bool ``` | OS X 10.10.3 |

Modified JSValueIsStrictEqual(JSContextRef, JSValueRef, JSValueRef) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueIsStrictEqual(_ ctx: JSContext!, _ a: JSValue!, _ b: JSValue!) -> Bool ``` | OS X 10.10 |
| To | ``` func JSValueIsStrictEqual(_ ctx: JSContextRef, _ a: JSValueRef, _ b: JSValueRef) -> Bool ``` | OS X 10.10.3 |

Modified JSValueIsString(JSContextRef, JSValueRef) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueIsString(_ ctx: JSContext!, _ value: JSValue!) -> Bool ``` | OS X 10.10 |
| To | ``` func JSValueIsString(_ ctx: JSContextRef, _ value: JSValueRef) -> Bool ``` | OS X 10.10.3 |

Modified JSValueIsUndefined(JSContextRef, JSValueRef) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueIsUndefined(_ ctx: JSContext!, _ value: JSValue!) -> Bool ``` | OS X 10.10 |
| To | ``` func JSValueIsUndefined(_ ctx: JSContextRef, _ value: JSValueRef) -> Bool ``` | OS X 10.10.3 |

Modified JSValueMakeBoolean(JSContextRef, Bool) -> JSValueRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueMakeBoolean(_ ctx: JSContext!, _ boolean: Bool) -> Unmanaged<JSValue>! ``` | OS X 10.10 |
| To | ``` func JSValueMakeBoolean(_ ctx: JSContextRef, _ boolean: Bool) -> JSValueRef ``` | OS X 10.10.3 |

Modified JSValueMakeFromJSONString(JSContextRef, JSStringRef) -> JSValueRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueMakeFromJSONString(_ ctx: JSContext!, _ string: JSString!) -> Unmanaged<JSValue>! ``` | OS X 10.10 |
| To | ``` func JSValueMakeFromJSONString(_ ctx: JSContextRef, _ string: JSStringRef) -> JSValueRef ``` | OS X 10.7 |

Modified JSValueMakeNull(JSContextRef) -> JSValueRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueMakeNull(_ ctx: JSContext!) -> Unmanaged<JSValue>! ``` | OS X 10.10 |
| To | ``` func JSValueMakeNull(_ ctx: JSContextRef) -> JSValueRef ``` | OS X 10.10.3 |

Modified JSValueMakeNumber(JSContextRef, Double) -> JSValueRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueMakeNumber(_ ctx: JSContext!, _ number: Double) -> Unmanaged<JSValue>! ``` | OS X 10.10 |
| To | ``` func JSValueMakeNumber(_ ctx: JSContextRef, _ number: Double) -> JSValueRef ``` | OS X 10.10.3 |

Modified JSValueMakeString(JSContextRef, JSStringRef) -> JSValueRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueMakeString(_ ctx: JSContext!, _ string: JSString!) -> Unmanaged<JSValue>! ``` | OS X 10.10 |
| To | ``` func JSValueMakeString(_ ctx: JSContextRef, _ string: JSStringRef) -> JSValueRef ``` | OS X 10.10.3 |

Modified JSValueMakeUndefined(JSContextRef) -> JSValueRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueMakeUndefined(_ ctx: JSContext!) -> Unmanaged<JSValue>! ``` | OS X 10.10 |
| To | ``` func JSValueMakeUndefined(_ ctx: JSContextRef) -> JSValueRef ``` | OS X 10.10.3 |

Modified JSValueProtect(JSContextRef, JSValueRef)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueProtect(_ ctx: JSContext!, _ value: JSValue!) ``` | OS X 10.10 |
| To | ``` func JSValueProtect(_ ctx: JSContextRef, _ value: JSValueRef) ``` | OS X 10.10.3 |

Modified JSValueRef

|  | Declaration |
| --- | --- |
| From | ``` typealias JSValueRef = JSValue ``` |
| To | ``` typealias JSValueRef = COpaquePointer ``` |

Modified JSValueToBoolean(JSContextRef, JSValueRef) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueToBoolean(_ ctx: JSContext!, _ value: JSValue!) -> Bool ``` | OS X 10.10 |
| To | ``` func JSValueToBoolean(_ ctx: JSContextRef, _ value: JSValueRef) -> Bool ``` | OS X 10.10.3 |

Modified JSValueToNumber(JSContextRef, JSValueRef, UnsafeMutablePointer<JSValueRef>) -> Double

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueToNumber(_ ctx: JSContext!, _ value: JSValue!, _ exception: UnsafePointer<Unmanaged<JSValue>?>) -> Double ``` | OS X 10.10 |
| To | ``` func JSValueToNumber(_ ctx: JSContextRef, _ value: JSValueRef, _ exception: UnsafeMutablePointer<JSValueRef>) -> Double ``` | OS X 10.10.3 |

Modified JSValueToObject(JSContextRef, JSValueRef, UnsafeMutablePointer<JSValueRef>) -> JSObjectRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueToObject(_ ctx: JSContext!, _ value: JSValue!, _ exception: UnsafePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSObject>! ``` | OS X 10.10 |
| To | ``` func JSValueToObject(_ ctx: JSContextRef, _ value: JSValueRef, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSObjectRef ``` | OS X 10.10.3 |

Modified JSValueToStringCopy(JSContextRef, JSValueRef, UnsafeMutablePointer<JSValueRef>) -> JSStringRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueToStringCopy(_ ctx: JSContext!, _ value: JSValue!, _ exception: UnsafePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSString>! ``` | OS X 10.10 |
| To | ``` func JSValueToStringCopy(_ ctx: JSContextRef, _ value: JSValueRef, _ exception: UnsafeMutablePointer<JSValueRef>) -> JSStringRef ``` | OS X 10.10.3 |

Modified JSValueUnprotect(JSContextRef, JSValueRef)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func JSValueUnprotect(_ ctx: JSContext!, _ value: JSValue!) ``` | OS X 10.10 |
| To | ``` func JSValueUnprotect(_ ctx: JSContextRef, _ value: JSValueRef) ``` | OS X 10.10.3 |

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
