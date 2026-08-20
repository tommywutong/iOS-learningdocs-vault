---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/JavaScriptCore.html
archived_at: '2026-07-18T02:53:37.845060Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# JavaScriptCore Changes for Swift

### JavaScriptCore

Removed JSClassDefinition.init(version: Int32, attributes: JSClassAttributes, className: UnsafePointer<Int8>, parentClass: JSClassRef, staticValues: UnsafePointer<JSStaticValue>, staticFunctions: UnsafePointer<JSStaticFunction>, initialize: JSObjectInitializeCallback, finalize: JSObjectFinalizeCallback, hasProperty: JSObjectHasPropertyCallback, getProperty: JSObjectGetPropertyCallback, setProperty: JSObjectSetPropertyCallback, deleteProperty: JSObjectDeletePropertyCallback, getPropertyNames: JSObjectGetPropertyNamesCallback, callAsFunction: JSObjectCallAsFunctionCallback, callAsConstructor: JSObjectCallAsConstructorCallback, hasInstance: JSObjectHasInstanceCallback, convertToType: JSObjectConvertToTypeCallback)Removed JSStaticFunction.init(name: UnsafePointer<Int8>, callAsFunction: JSObjectCallAsFunctionCallback, attributes: JSPropertyAttributes)Removed JSStaticValue.init(name: UnsafePointer<Int8>, getProperty: JSObjectGetPropertyCallback, setProperty: JSObjectSetPropertyCallback, attributes: JSPropertyAttributes)Removed JSType.valueRemoved JSValue.isBoolean() -> BoolRemoved JSValue.isNull() -> BoolRemoved JSValue.isNumber() -> BoolRemoved JSValue.isObject() -> BoolRemoved JSValue.isString() -> BoolRemoved JSValue.isUndefined() -> BoolAdded JSClassDefinition.init(version: Int32, attributes: JSClassAttributes, className: UnsafePointer<Int8>, parentClass: JSClassRef, staticValues: UnsafePointer<JSStaticValue>, staticFunctions: UnsafePointer<JSStaticFunction>, initialize: JSObjectInitializeCallback!, finalize: JSObjectFinalizeCallback!, hasProperty: JSObjectHasPropertyCallback!, getProperty: JSObjectGetPropertyCallback!, setProperty: JSObjectSetPropertyCallback!, deleteProperty: JSObjectDeletePropertyCallback!, getPropertyNames: JSObjectGetPropertyNamesCallback!, callAsFunction: JSObjectCallAsFunctionCallback!, callAsConstructor: JSObjectCallAsConstructorCallback!, hasInstance: JSObjectHasInstanceCallback!, convertToType: JSObjectConvertToTypeCallback!)Added JSStaticFunction.init(name: UnsafePointer<Int8>, callAsFunction: JSObjectCallAsFunctionCallback!, attributes: JSPropertyAttributes)Added JSStaticValue.init(name: UnsafePointer<Int8>, getProperty: JSObjectGetPropertyCallback!, setProperty: JSObjectSetPropertyCallback!, attributes: JSPropertyAttributes)Added JSType.init(rawValue: UInt32)Added JSType.rawValueAdded [JSValue.isArray](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451575-isarray)Added [JSValue.isBoolean](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451367-isboolean)Added [JSValue.isDate](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451668-isdate)Added [JSValue.isNull](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451369-isnull)Added [JSValue.isNumber](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451682-isnumber)Added [JSValue.isObject](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451461-isobject)Added [JSValue.isString](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451427-isstring)Added [JSValue.isUndefined](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451365-isundefined)Added [JSValueIsArray(_: JSContextRef, _: JSValueRef) -> Bool](https://developer.apple.com/documentation/javascriptcore/1395924-jsvalueisarray)Added [JSValueIsDate(_: JSContextRef, _: JSValueRef) -> Bool](https://developer.apple.com/documentation/javascriptcore/1395926-jsvalueisdate)Modified [JSClassDefinition [struct]](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition)

|  | Declaration |
| --- | --- |
| From | ``` struct JSClassDefinition {     var version: Int32     var attributes: JSClassAttributes     var className: UnsafePointer<Int8>     var parentClass: JSClassRef     var staticValues: UnsafePointer<JSStaticValue>     var staticFunctions: UnsafePointer<JSStaticFunction>     var initialize: JSObjectInitializeCallback     var finalize: JSObjectFinalizeCallback     var hasProperty: JSObjectHasPropertyCallback     var getProperty: JSObjectGetPropertyCallback     var setProperty: JSObjectSetPropertyCallback     var deleteProperty: JSObjectDeletePropertyCallback     var getPropertyNames: JSObjectGetPropertyNamesCallback     var callAsFunction: JSObjectCallAsFunctionCallback     var callAsConstructor: JSObjectCallAsConstructorCallback     var hasInstance: JSObjectHasInstanceCallback     var convertToType: JSObjectConvertToTypeCallback     init()     init(version version: Int32, attributes attributes: JSClassAttributes, className className: UnsafePointer<Int8>, parentClass parentClass: JSClassRef, staticValues staticValues: UnsafePointer<JSStaticValue>, staticFunctions staticFunctions: UnsafePointer<JSStaticFunction>, initialize initialize: JSObjectInitializeCallback, finalize finalize: JSObjectFinalizeCallback, hasProperty hasProperty: JSObjectHasPropertyCallback, getProperty getProperty: JSObjectGetPropertyCallback, setProperty setProperty: JSObjectSetPropertyCallback, deleteProperty deleteProperty: JSObjectDeletePropertyCallback, getPropertyNames getPropertyNames: JSObjectGetPropertyNamesCallback, callAsFunction callAsFunction: JSObjectCallAsFunctionCallback, callAsConstructor callAsConstructor: JSObjectCallAsConstructorCallback, hasInstance hasInstance: JSObjectHasInstanceCallback, convertToType convertToType: JSObjectConvertToTypeCallback) } ``` |
| To | ``` struct JSClassDefinition {     var version: Int32     var attributes: JSClassAttributes     var className: UnsafePointer<Int8>     var parentClass: JSClassRef     var staticValues: UnsafePointer<JSStaticValue>     var staticFunctions: UnsafePointer<JSStaticFunction>     var initialize: JSObjectInitializeCallback!     var finalize: JSObjectFinalizeCallback!     var hasProperty: JSObjectHasPropertyCallback!     var getProperty: JSObjectGetPropertyCallback!     var setProperty: JSObjectSetPropertyCallback!     var deleteProperty: JSObjectDeletePropertyCallback!     var getPropertyNames: JSObjectGetPropertyNamesCallback!     var callAsFunction: JSObjectCallAsFunctionCallback!     var callAsConstructor: JSObjectCallAsConstructorCallback!     var hasInstance: JSObjectHasInstanceCallback!     var convertToType: JSObjectConvertToTypeCallback!     init()     init(version version: Int32, attributes attributes: JSClassAttributes, className className: UnsafePointer<Int8>, parentClass parentClass: JSClassRef, staticValues staticValues: UnsafePointer<JSStaticValue>, staticFunctions staticFunctions: UnsafePointer<JSStaticFunction>, initialize initialize: JSObjectInitializeCallback!, finalize finalize: JSObjectFinalizeCallback!, hasProperty hasProperty: JSObjectHasPropertyCallback!, getProperty getProperty: JSObjectGetPropertyCallback!, setProperty setProperty: JSObjectSetPropertyCallback!, deleteProperty deleteProperty: JSObjectDeletePropertyCallback!, getPropertyNames getPropertyNames: JSObjectGetPropertyNamesCallback!, callAsFunction callAsFunction: JSObjectCallAsFunctionCallback!, callAsConstructor callAsConstructor: JSObjectCallAsConstructorCallback!, hasInstance hasInstance: JSObjectHasInstanceCallback!, convertToType convertToType: JSObjectConvertToTypeCallback!) } ``` |

Modified [JSClassDefinition.callAsConstructor](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451577-callasconstructor)

|  | Declaration |
| --- | --- |
| From | ``` var callAsConstructor: JSObjectCallAsConstructorCallback ``` |
| To | ``` var callAsConstructor: JSObjectCallAsConstructorCallback! ``` |

Modified [JSClassDefinition.callAsFunction](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451450-callasfunction)

|  | Declaration |
| --- | --- |
| From | ``` var callAsFunction: JSObjectCallAsFunctionCallback ``` |
| To | ``` var callAsFunction: JSObjectCallAsFunctionCallback! ``` |

Modified [JSClassDefinition.convertToType](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451772-converttotype)

|  | Declaration |
| --- | --- |
| From | ``` var convertToType: JSObjectConvertToTypeCallback ``` |
| To | ``` var convertToType: JSObjectConvertToTypeCallback! ``` |

Modified [JSClassDefinition.deleteProperty](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451506-deleteproperty)

|  | Declaration |
| --- | --- |
| From | ``` var deleteProperty: JSObjectDeletePropertyCallback ``` |
| To | ``` var deleteProperty: JSObjectDeletePropertyCallback! ``` |

Modified [JSClassDefinition.finalize](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451680-finalize)

|  | Declaration |
| --- | --- |
| From | ``` var finalize: JSObjectFinalizeCallback ``` |
| To | ``` var finalize: JSObjectFinalizeCallback! ``` |

Modified [JSClassDefinition.getProperty](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451740-getproperty)

|  | Declaration |
| --- | --- |
| From | ``` var getProperty: JSObjectGetPropertyCallback ``` |
| To | ``` var getProperty: JSObjectGetPropertyCallback! ``` |

Modified [JSClassDefinition.getPropertyNames](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451611-getpropertynames)

|  | Declaration |
| --- | --- |
| From | ``` var getPropertyNames: JSObjectGetPropertyNamesCallback ``` |
| To | ``` var getPropertyNames: JSObjectGetPropertyNamesCallback! ``` |

Modified [JSClassDefinition.hasInstance](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451413-hasinstance)

|  | Declaration |
| --- | --- |
| From | ``` var hasInstance: JSObjectHasInstanceCallback ``` |
| To | ``` var hasInstance: JSObjectHasInstanceCallback! ``` |

Modified [JSClassDefinition.hasProperty](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451425-hasproperty)

|  | Declaration |
| --- | --- |
| From | ``` var hasProperty: JSObjectHasPropertyCallback ``` |
| To | ``` var hasProperty: JSObjectHasPropertyCallback! ``` |

Modified [JSClassDefinition.initialize](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451397-initialize)

|  | Declaration |
| --- | --- |
| From | ``` var initialize: JSObjectInitializeCallback ``` |
| To | ``` var initialize: JSObjectInitializeCallback! ``` |

Modified [JSClassDefinition.setProperty](https://developer.apple.com/documentation/javascriptcore/jsclassdefinition/1451705-setproperty)

|  | Declaration |
| --- | --- |
| From | ``` var setProperty: JSObjectSetPropertyCallback ``` |
| To | ``` var setProperty: JSObjectSetPropertyCallback! ``` |

Modified [JSContext](https://developer.apple.com/documentation/javascriptcore/jscontext)

|  | Declaration |
| --- | --- |
| From | ``` class JSContext : NSObject {     init!()     init!(virtualMachine virtualMachine: JSVirtualMachine!)     func evaluateScript(_ script: String!) -> JSValue!     func evaluateScript(_ script: String!, withSourceURL sourceURL: NSURL!) -> JSValue!     class func currentContext() -> JSContext!     class func currentCallee() -> JSValue!     class func currentThis() -> JSValue!     class func currentArguments() -> [AnyObject]!     var globalObject: JSValue! { get }     var exception: JSValue!     var exceptionHandler: ((JSContext!, JSValue!) -> Void)!     var virtualMachine: JSVirtualMachine! { get }     var name: String! } extension JSContext {     func objectForKeyedSubscript(_ key: AnyObject!) -> JSValue!     func setObject(_ object: AnyObject!, forKeyedSubscript key: NSObject!) } extension JSContext {     init!(JSGlobalContextRef jsGlobalContextRef: JSGlobalContextRef) -> JSContext     class func contextWithJSGlobalContextRef(_ jsGlobalContextRef: JSGlobalContextRef) -> JSContext!     var JSGlobalContextRef: JSGlobalContextRef { get } } ``` |
| To | ``` class JSContext : NSObject {     init!()     init!(virtualMachine virtualMachine: JSVirtualMachine!)     func evaluateScript(_ script: String!) -> JSValue!     func evaluateScript(_ script: String!, withSourceURL sourceURL: NSURL!) -> JSValue!     class func currentContext() -> JSContext!     class func currentCallee() -> JSValue!     class func currentThis() -> JSValue!     class func currentArguments() -> [AnyObject]!     var globalObject: JSValue! { get }     var exception: JSValue!     var exceptionHandler: ((JSContext!, JSValue!) -> Void)!     var virtualMachine: JSVirtualMachine! { get }     var name: String! } extension JSContext {     func objectForKeyedSubscript(_ key: AnyObject!) -> JSValue!     func setObject(_ object: AnyObject!, forKeyedSubscript key: protocol<NSCopying, NSObjectProtocol>!) } extension JSContext {      init!(JSGlobalContextRef jsGlobalContextRef: JSGlobalContextRef)     class func contextWithJSGlobalContextRef(_ jsGlobalContextRef: JSGlobalContextRef) -> JSContext!     var JSGlobalContextRef: JSGlobalContextRef { get } } ``` |

Modified [JSContext.init(JSGlobalContextRef: JSGlobalContextRef)](https://developer.apple.com/documentation/javascriptcore/jscontext/1451491-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(JSGlobalContextRef jsGlobalContextRef: JSGlobalContextRef) -> JSContext ``` |
| To | ``` init!(JSGlobalContextRef jsGlobalContextRef: JSGlobalContextRef) ``` |

Modified [JSContext.setObject(_: AnyObject!, forKeyedSubscript: protocol<NSCopying, NSObjectProtocol>!)](https://developer.apple.com/documentation/javascriptcore/jscontext/1451416-setobject)

|  | Declaration |
| --- | --- |
| From | ``` func setObject(_ object: AnyObject!, forKeyedSubscript key: NSObject!) ``` |
| To | ``` func setObject(_ object: AnyObject!, forKeyedSubscript key: protocol<NSCopying, NSObjectProtocol>!) ``` |

Modified [JSManagedValue](https://developer.apple.com/documentation/javascriptcore/jsmanagedvalue)

|  | Declaration |
| --- | --- |
| From | ``` class JSManagedValue : NSObject {     init!(value value: JSValue!) -> JSManagedValue     class func managedValueWithValue(_ value: JSValue!) -> JSManagedValue!     init!(value value: JSValue!, andOwner owner: AnyObject!) -> JSManagedValue     class func managedValueWithValue(_ value: JSValue!, andOwner owner: AnyObject!) -> JSManagedValue!     init!(value value: JSValue!)     var value: JSValue! { get } } ``` |
| To | ``` class JSManagedValue : NSObject {      init!(value value: JSValue!)     class func managedValueWithValue(_ value: JSValue!) -> JSManagedValue!      init!(value value: JSValue!, andOwner owner: AnyObject!)     class func managedValueWithValue(_ value: JSValue!, andOwner owner: AnyObject!) -> JSManagedValue!     init!(value value: JSValue!)     var value: JSValue! { get } } ``` |

Modified [JSManagedValue.init(value: JSValue!, andOwner: AnyObject!)](https://developer.apple.com/documentation/javascriptcore/jsmanagedvalue/1451607-managedvaluewithvalue)

|  | Declaration |
| --- | --- |
| From | ``` init!(value value: JSValue!, andOwner owner: AnyObject!) -> JSManagedValue ``` |
| To | ``` init!(value value: JSValue!, andOwner owner: AnyObject!) ``` |

Modified [JSStaticFunction [struct]](https://developer.apple.com/documentation/javascriptcore/jsstaticfunction)

|  | Declaration |
| --- | --- |
| From | ``` struct JSStaticFunction {     var name: UnsafePointer<Int8>     var callAsFunction: JSObjectCallAsFunctionCallback     var attributes: JSPropertyAttributes     init()     init(name name: UnsafePointer<Int8>, callAsFunction callAsFunction: JSObjectCallAsFunctionCallback, attributes attributes: JSPropertyAttributes) } ``` |
| To | ``` struct JSStaticFunction {     var name: UnsafePointer<Int8>     var callAsFunction: JSObjectCallAsFunctionCallback!     var attributes: JSPropertyAttributes     init()     init(name name: UnsafePointer<Int8>, callAsFunction callAsFunction: JSObjectCallAsFunctionCallback!, attributes attributes: JSPropertyAttributes) } ``` |

Modified [JSStaticFunction.callAsFunction](https://developer.apple.com/documentation/javascriptcore/jsstaticfunction/1451749-callasfunction)

|  | Declaration |
| --- | --- |
| From | ``` var callAsFunction: JSObjectCallAsFunctionCallback ``` |
| To | ``` var callAsFunction: JSObjectCallAsFunctionCallback! ``` |

Modified [JSStaticValue [struct]](https://developer.apple.com/documentation/javascriptcore/jsstaticvalue)

|  | Declaration |
| --- | --- |
| From | ``` struct JSStaticValue {     var name: UnsafePointer<Int8>     var getProperty: JSObjectGetPropertyCallback     var setProperty: JSObjectSetPropertyCallback     var attributes: JSPropertyAttributes     init()     init(name name: UnsafePointer<Int8>, getProperty getProperty: JSObjectGetPropertyCallback, setProperty setProperty: JSObjectSetPropertyCallback, attributes attributes: JSPropertyAttributes) } ``` |
| To | ``` struct JSStaticValue {     var name: UnsafePointer<Int8>     var getProperty: JSObjectGetPropertyCallback!     var setProperty: JSObjectSetPropertyCallback!     var attributes: JSPropertyAttributes     init()     init(name name: UnsafePointer<Int8>, getProperty getProperty: JSObjectGetPropertyCallback!, setProperty setProperty: JSObjectSetPropertyCallback!, attributes attributes: JSPropertyAttributes) } ``` |

Modified [JSStaticValue.getProperty](https://developer.apple.com/documentation/javascriptcore/jsstaticvalue/1451527-getproperty)

|  | Declaration |
| --- | --- |
| From | ``` var getProperty: JSObjectGetPropertyCallback ``` |
| To | ``` var getProperty: JSObjectGetPropertyCallback! ``` |

Modified [JSStaticValue.setProperty](https://developer.apple.com/documentation/javascriptcore/jsstaticvalue/1451455-setproperty)

|  | Declaration |
| --- | --- |
| From | ``` var setProperty: JSObjectSetPropertyCallback ``` |
| To | ``` var setProperty: JSObjectSetPropertyCallback! ``` |

Modified [JSType [struct]](https://developer.apple.com/documentation/javascriptcore/jstype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct JSType {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct JSType : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [JSValue](https://developer.apple.com/documentation/javascriptcore/jsvalue)

|  | Declaration |
| --- | --- |
| From | ``` class JSValue : NSObject {     var context: JSContext! { get }     init!(object value: AnyObject!, inContext context: JSContext!) -> JSValue     class func valueWithObject(_ value: AnyObject!, inContext context: JSContext!) -> JSValue!     init!(bool value: Bool, inContext context: JSContext!) -> JSValue     class func valueWithBool(_ value: Bool, inContext context: JSContext!) -> JSValue!     init!(double value: Double, inContext context: JSContext!) -> JSValue     class func valueWithDouble(_ value: Double, inContext context: JSContext!) -> JSValue!     init!(int32 value: Int32, inContext context: JSContext!) -> JSValue     class func valueWithInt32(_ value: Int32, inContext context: JSContext!) -> JSValue!     init!(UInt32 value: UInt32, inContext context: JSContext!) -> JSValue     class func valueWithUInt32(_ value: UInt32, inContext context: JSContext!) -> JSValue!     init!(newObjectInContext context: JSContext!) -> JSValue     class func valueWithNewObjectInContext(_ context: JSContext!) -> JSValue!     init!(newArrayInContext context: JSContext!) -> JSValue     class func valueWithNewArrayInContext(_ context: JSContext!) -> JSValue!     init!(newRegularExpressionFromPattern pattern: String!, flags flags: String!, inContext context: JSContext!) -> JSValue     class func valueWithNewRegularExpressionFromPattern(_ pattern: String!, flags flags: String!, inContext context: JSContext!) -> JSValue!     init!(newErrorFromMessage message: String!, inContext context: JSContext!) -> JSValue     class func valueWithNewErrorFromMessage(_ message: String!, inContext context: JSContext!) -> JSValue!     init!(nullInContext context: JSContext!) -> JSValue     class func valueWithNullInContext(_ context: JSContext!) -> JSValue!     init!(undefinedInContext context: JSContext!) -> JSValue     class func valueWithUndefinedInContext(_ context: JSContext!) -> JSValue!     func toObject() -> AnyObject!     func toObjectOfClass(_ expectedClass: AnyClass!) -> AnyObject!     func toBool() -> Bool     func toDouble() -> Double     func toInt32() -> Int32     func toUInt32() -> UInt32     func toNumber() -> NSNumber!     func toString() -> String!     func toDate() -> NSDate!     func toArray() -> [AnyObject]!     func toDictionary() -> [NSObject : AnyObject]!     func valueForProperty(_ property: String!) -> JSValue!     func setValue(_ value: AnyObject!, forProperty property: String!)     func deleteProperty(_ property: String!) -> Bool     func hasProperty(_ property: String!) -> Bool     func defineProperty(_ property: String!, descriptor descriptor: AnyObject!)     func valueAtIndex(_ index: Int) -> JSValue!     func setValue(_ value: AnyObject!, atIndex index: Int)     func isUndefined() -> Bool     func isNull() -> Bool     func isBoolean() -> Bool     func isNumber() -> Bool     func isString() -> Bool     func isObject() -> Bool     func isEqualToObject(_ value: AnyObject!) -> Bool     func isEqualWithTypeCoercionToObject(_ value: AnyObject!) -> Bool     func isInstanceOf(_ value: AnyObject!) -> Bool     func callWithArguments(_ arguments: [AnyObject]!) -> JSValue!     func constructWithArguments(_ arguments: [AnyObject]!) -> JSValue!     func invokeMethod(_ method: String!, withArguments arguments: [AnyObject]!) -> JSValue! } extension JSValue {     init!(point point: CGPoint, inContext context: JSContext!) -> JSValue     class func valueWithPoint(_ point: CGPoint, inContext context: JSContext!) -> JSValue!     init!(range range: NSRange, inContext context: JSContext!) -> JSValue     class func valueWithRange(_ range: NSRange, inContext context: JSContext!) -> JSValue!     init!(rect rect: CGRect, inContext context: JSContext!) -> JSValue     class func valueWithRect(_ rect: CGRect, inContext context: JSContext!) -> JSValue!     init!(size size: CGSize, inContext context: JSContext!) -> JSValue     class func valueWithSize(_ size: CGSize, inContext context: JSContext!) -> JSValue!     func toPoint() -> CGPoint     func toRange() -> NSRange     func toRect() -> CGRect     func toSize() -> CGSize } extension JSValue {     func objectForKeyedSubscript(_ key: AnyObject!) -> JSValue!     func objectAtIndexedSubscript(_ index: Int) -> JSValue!     func setObject(_ object: AnyObject!, forKeyedSubscript key: NSObject!)     func setObject(_ object: AnyObject!, atIndexedSubscript index: Int) } extension JSValue {     init!(JSValueRef value: JSValueRef, inContext context: JSContext!) -> JSValue     class func valueWithJSValueRef(_ value: JSValueRef, inContext context: JSContext!) -> JSValue!     var JSValueRef: JSValueRef { get } } ``` |
| To | ``` class JSValue : NSObject {     var context: JSContext! { get }      init!(object value: AnyObject!, inContext context: JSContext!)     class func valueWithObject(_ value: AnyObject!, inContext context: JSContext!) -> JSValue!      init!(bool value: Bool, inContext context: JSContext!)     class func valueWithBool(_ value: Bool, inContext context: JSContext!) -> JSValue!      init!(double value: Double, inContext context: JSContext!)     class func valueWithDouble(_ value: Double, inContext context: JSContext!) -> JSValue!      init!(int32 value: Int32, inContext context: JSContext!)     class func valueWithInt32(_ value: Int32, inContext context: JSContext!) -> JSValue!      init!(UInt32 value: UInt32, inContext context: JSContext!)     class func valueWithUInt32(_ value: UInt32, inContext context: JSContext!) -> JSValue!      init!(newObjectInContext context: JSContext!)     class func valueWithNewObjectInContext(_ context: JSContext!) -> JSValue!      init!(newArrayInContext context: JSContext!)     class func valueWithNewArrayInContext(_ context: JSContext!) -> JSValue!      init!(newRegularExpressionFromPattern pattern: String!, flags flags: String!, inContext context: JSContext!)     class func valueWithNewRegularExpressionFromPattern(_ pattern: String!, flags flags: String!, inContext context: JSContext!) -> JSValue!      init!(newErrorFromMessage message: String!, inContext context: JSContext!)     class func valueWithNewErrorFromMessage(_ message: String!, inContext context: JSContext!) -> JSValue!      init!(nullInContext context: JSContext!)     class func valueWithNullInContext(_ context: JSContext!) -> JSValue!      init!(undefinedInContext context: JSContext!)     class func valueWithUndefinedInContext(_ context: JSContext!) -> JSValue!     func toObject() -> AnyObject!     func toObjectOfClass(_ expectedClass: AnyClass!) -> AnyObject!     func toBool() -> Bool     func toDouble() -> Double     func toInt32() -> Int32     func toUInt32() -> UInt32     func toNumber() -> NSNumber!     func toString() -> String!     func toDate() -> NSDate!     func toArray() -> [AnyObject]!     func toDictionary() -> [NSObject : AnyObject]!     func valueForProperty(_ property: String!) -> JSValue!     func setValue(_ value: AnyObject!, forProperty property: String!)     func deleteProperty(_ property: String!) -> Bool     func hasProperty(_ property: String!) -> Bool     func defineProperty(_ property: String!, descriptor descriptor: AnyObject!)     func valueAtIndex(_ index: Int) -> JSValue!     func setValue(_ value: AnyObject!, atIndex index: Int)     var isUndefined: Bool { get }     var isNull: Bool { get }     var isBoolean: Bool { get }     var isNumber: Bool { get }     var isString: Bool { get }     var isObject: Bool { get }     var isArray: Bool { get }     var isDate: Bool { get }     func isEqualToObject(_ value: AnyObject!) -> Bool     func isEqualWithTypeCoercionToObject(_ value: AnyObject!) -> Bool     func isInstanceOf(_ value: AnyObject!) -> Bool     func callWithArguments(_ arguments: [AnyObject]!) -> JSValue!     func constructWithArguments(_ arguments: [AnyObject]!) -> JSValue!     func invokeMethod(_ method: String!, withArguments arguments: [AnyObject]!) -> JSValue! } extension JSValue {      init!(point point: CGPoint, inContext context: JSContext!)     class func valueWithPoint(_ point: CGPoint, inContext context: JSContext!) -> JSValue!      init!(range range: NSRange, inContext context: JSContext!)     class func valueWithRange(_ range: NSRange, inContext context: JSContext!) -> JSValue!      init!(rect rect: CGRect, inContext context: JSContext!)     class func valueWithRect(_ rect: CGRect, inContext context: JSContext!) -> JSValue!      init!(size size: CGSize, inContext context: JSContext!)     class func valueWithSize(_ size: CGSize, inContext context: JSContext!) -> JSValue!     func toPoint() -> CGPoint     func toRange() -> NSRange     func toRect() -> CGRect     func toSize() -> CGSize } extension JSValue {     func objectForKeyedSubscript(_ key: AnyObject!) -> JSValue!     func objectAtIndexedSubscript(_ index: Int) -> JSValue!     func setObject(_ object: AnyObject!, forKeyedSubscript key: protocol<NSCopying, NSObjectProtocol>!)     func setObject(_ object: AnyObject!, atIndexedSubscript index: Int) } extension JSValue {      init!(JSValueRef value: JSValueRef, inContext context: JSContext!)     class func valueWithJSValueRef(_ value: JSValueRef, inContext context: JSContext!) -> JSValue!     var JSValueRef: JSValueRef { get } } ``` |

Modified [JSValue.init(bool: Bool, inContext: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451616-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(bool value: Bool, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(bool value: Bool, inContext context: JSContext!) ``` |

Modified [JSValue.init(double: Double, inContext: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451482-valuewithdouble)

|  | Declaration |
| --- | --- |
| From | ``` init!(double value: Double, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(double value: Double, inContext context: JSContext!) ``` |

Modified [JSValue.init(int32: Int32, inContext: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451434-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(int32 value: Int32, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(int32 value: Int32, inContext context: JSContext!) ``` |

Modified [JSValue.init(JSValueRef: JSValueRef, inContext: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451641-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(JSValueRef value: JSValueRef, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(JSValueRef value: JSValueRef, inContext context: JSContext!) ``` |

Modified [JSValue.init(newArrayInContext: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451473-valuewithnewarrayincontext)

|  | Declaration |
| --- | --- |
| From | ``` init!(newArrayInContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(newArrayInContext context: JSContext!) ``` |

Modified [JSValue.init(newErrorFromMessage: String!, inContext: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451630-valuewithnewerrorfrommessage)

|  | Declaration |
| --- | --- |
| From | ``` init!(newErrorFromMessage message: String!, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(newErrorFromMessage message: String!, inContext context: JSContext!) ``` |

Modified [JSValue.init(newObjectInContext: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451751-valuewithnewobjectincontext)

|  | Declaration |
| --- | --- |
| From | ``` init!(newObjectInContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(newObjectInContext context: JSContext!) ``` |

Modified [JSValue.init(newRegularExpressionFromPattern: String!, flags: String!, inContext: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451539-valuewithnewregularexpressionfro)

|  | Declaration |
| --- | --- |
| From | ``` init!(newRegularExpressionFromPattern pattern: String!, flags flags: String!, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(newRegularExpressionFromPattern pattern: String!, flags flags: String!, inContext context: JSContext!) ``` |

Modified [JSValue.init(nullInContext: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451463-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(nullInContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(nullInContext context: JSContext!) ``` |

Modified [JSValue.init(object: AnyObject!, inContext: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451694-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(object value: AnyObject!, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(object value: AnyObject!, inContext context: JSContext!) ``` |

Modified [JSValue.init(point: CGPoint, inContext: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451382-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(point point: CGPoint, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(point point: CGPoint, inContext context: JSContext!) ``` |

Modified [JSValue.init(range: NSRange, inContext: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451628-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(range range: NSRange, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(range range: NSRange, inContext context: JSContext!) ``` |

Modified [JSValue.init(rect: CGRect, inContext: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451664-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(rect rect: CGRect, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(rect rect: CGRect, inContext context: JSContext!) ``` |

Modified [JSValue.init(size: CGSize, inContext: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451715-valuewithsize)

|  | Declaration |
| --- | --- |
| From | ``` init!(size size: CGSize, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(size size: CGSize, inContext context: JSContext!) ``` |

Modified [JSValue.init(UInt32: UInt32, inContext: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451402-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(UInt32 value: UInt32, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(UInt32 value: UInt32, inContext context: JSContext!) ``` |

Modified [JSValue.init(undefinedInContext: JSContext!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451387-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(undefinedInContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(undefinedInContext context: JSContext!) ``` |

Modified [JSValue.setObject(_: AnyObject!, forKeyedSubscript: protocol<NSCopying, NSObjectProtocol>!)](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451672-setobject)

|  | Declaration |
| --- | --- |
| From | ``` func setObject(_ object: AnyObject!, forKeyedSubscript key: NSObject!) ``` |
| To | ``` func setObject(_ object: AnyObject!, forKeyedSubscript key: protocol<NSCopying, NSObjectProtocol>!) ``` |

Modified [JSObjectCallAsConstructorCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectcallasconstructorcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectCallAsConstructorCallback = CFunctionPointer<((JSContextRef, JSObjectRef, Int, UnsafePointer<JSValueRef>, UnsafeMutablePointer<JSValueRef>) -> JSObjectRef)> ``` |
| To | ``` typealias JSObjectCallAsConstructorCallback = (JSContextRef, JSObjectRef, Int, UnsafePointer<JSValueRef>, UnsafeMutablePointer<JSValueRef>) -> JSObjectRef ``` |

Modified [JSObjectCallAsFunctionCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectcallasfunctioncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectCallAsFunctionCallback = CFunctionPointer<((JSContextRef, JSObjectRef, JSObjectRef, Int, UnsafePointer<JSValueRef>, UnsafeMutablePointer<JSValueRef>) -> JSValueRef)> ``` |
| To | ``` typealias JSObjectCallAsFunctionCallback = (JSContextRef, JSObjectRef, JSObjectRef, Int, UnsafePointer<JSValueRef>, UnsafeMutablePointer<JSValueRef>) -> JSValueRef ``` |

Modified [JSObjectConvertToTypeCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectconverttotypecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectConvertToTypeCallback = CFunctionPointer<((JSContextRef, JSObjectRef, JSType, UnsafeMutablePointer<JSValueRef>) -> JSValueRef)> ``` |
| To | ``` typealias JSObjectConvertToTypeCallback = (JSContextRef, JSObjectRef, JSType, UnsafeMutablePointer<JSValueRef>) -> JSValueRef ``` |

Modified [JSObjectDeletePropertyCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectdeletepropertycallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectDeletePropertyCallback = CFunctionPointer<((JSContextRef, JSObjectRef, JSStringRef, UnsafeMutablePointer<JSValueRef>) -> Bool)> ``` |
| To | ``` typealias JSObjectDeletePropertyCallback = (JSContextRef, JSObjectRef, JSStringRef, UnsafeMutablePointer<JSValueRef>) -> Bool ``` |

Modified [JSObjectFinalizeCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectfinalizecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectFinalizeCallback = CFunctionPointer<((JSObjectRef) -> Void)> ``` |
| To | ``` typealias JSObjectFinalizeCallback = (JSObjectRef) -> Void ``` |

Modified [JSObjectGetPropertyCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectgetpropertycallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectGetPropertyCallback = CFunctionPointer<((JSContextRef, JSObjectRef, JSStringRef, UnsafeMutablePointer<JSValueRef>) -> JSValueRef)> ``` |
| To | ``` typealias JSObjectGetPropertyCallback = (JSContextRef, JSObjectRef, JSStringRef, UnsafeMutablePointer<JSValueRef>) -> JSValueRef ``` |

Modified [JSObjectGetPropertyNamesCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectgetpropertynamescallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectGetPropertyNamesCallback = CFunctionPointer<((JSContextRef, JSObjectRef, JSPropertyNameAccumulatorRef) -> Void)> ``` |
| To | ``` typealias JSObjectGetPropertyNamesCallback = (JSContextRef, JSObjectRef, JSPropertyNameAccumulatorRef) -> Void ``` |

Modified [JSObjectHasInstanceCallback](https://developer.apple.com/documentation/javascriptcore/jsobjecthasinstancecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectHasInstanceCallback = CFunctionPointer<((JSContextRef, JSObjectRef, JSValueRef, UnsafeMutablePointer<JSValueRef>) -> Bool)> ``` |
| To | ``` typealias JSObjectHasInstanceCallback = (JSContextRef, JSObjectRef, JSValueRef, UnsafeMutablePointer<JSValueRef>) -> Bool ``` |

Modified [JSObjectHasPropertyCallback](https://developer.apple.com/documentation/javascriptcore/jsobjecthaspropertycallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectHasPropertyCallback = CFunctionPointer<((JSContextRef, JSObjectRef, JSStringRef) -> Bool)> ``` |
| To | ``` typealias JSObjectHasPropertyCallback = (JSContextRef, JSObjectRef, JSStringRef) -> Bool ``` |

Modified [JSObjectInitializeCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectinitializecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectInitializeCallback = CFunctionPointer<((JSContextRef, JSObjectRef) -> Void)> ``` |
| To | ``` typealias JSObjectInitializeCallback = (JSContextRef, JSObjectRef) -> Void ``` |

Modified [JSObjectMakeConstructor(_: JSContextRef, _: JSClassRef, _: JSObjectCallAsConstructorCallback!) -> JSObjectRef](https://developer.apple.com/documentation/javascriptcore/1451566-jsobjectmakeconstructor)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectMakeConstructor(_ ctx: JSContextRef, _ jsClass: JSClassRef, _ callAsConstructor: JSObjectCallAsConstructorCallback) -> JSObjectRef ``` |
| To | ``` func JSObjectMakeConstructor(_ ctx: JSContextRef, _ jsClass: JSClassRef, _ callAsConstructor: JSObjectCallAsConstructorCallback!) -> JSObjectRef ``` |

Modified [JSObjectMakeFunctionWithCallback(_: JSContextRef, _: JSStringRef, _: JSObjectCallAsFunctionCallback!) -> JSObjectRef](https://developer.apple.com/documentation/javascriptcore/1451336-jsobjectmakefunctionwithcallback)

|  | Declaration |
| --- | --- |
| From | ``` func JSObjectMakeFunctionWithCallback(_ ctx: JSContextRef, _ name: JSStringRef, _ callAsFunction: JSObjectCallAsFunctionCallback) -> JSObjectRef ``` |
| To | ``` func JSObjectMakeFunctionWithCallback(_ ctx: JSContextRef, _ name: JSStringRef, _ callAsFunction: JSObjectCallAsFunctionCallback!) -> JSObjectRef ``` |

Modified [JSObjectSetPropertyCallback](https://developer.apple.com/documentation/javascriptcore/jsobjectsetpropertycallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias JSObjectSetPropertyCallback = CFunctionPointer<((JSContextRef, JSObjectRef, JSStringRef, JSValueRef, UnsafeMutablePointer<JSValueRef>) -> Bool)> ``` |
| To | ``` typealias JSObjectSetPropertyCallback = (JSContextRef, JSObjectRef, JSStringRef, JSValueRef, UnsafeMutablePointer<JSValueRef>) -> Bool ``` |

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
