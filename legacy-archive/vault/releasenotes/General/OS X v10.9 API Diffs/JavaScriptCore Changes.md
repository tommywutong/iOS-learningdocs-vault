---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/JavaScriptCore.html
archived_at: '2026-07-18T02:54:14.595243Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# JavaScriptCore Changes

## JavaScriptCore

JSBase.hAdded [#def JSC_OBJC_API_ENABLED](https://developer.apple.com/documentation/javascriptcore/jsc_objc_api_enabled)JSContext.hAdded [JSContext](https://developer.apple.com/documentation/javascriptcore/jscontext)Added [-[JSContext JSGlobalContextRef]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451338-jsglobalcontextref)Added [+[JSContext contextWithJSGlobalContextRef:]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451491-init)Added [+[JSContext currentArguments]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451650-currentarguments)Added [+[JSContext currentContext]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451545-current)Added [+[JSContext currentThis]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451767-currentthis)Added [-[JSContext evaluateScript:]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451350-evaluatescript)Added [JSContext.exception](https://developer.apple.com/documentation/javascriptcore/jscontext/1451499-exception)Added [JSContext.exceptionHandler](https://developer.apple.com/documentation/javascriptcore/jscontext/1451731-exceptionhandler)Added [-[JSContext globalObject]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451436-globalobject)Added [-[JSContext init]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451742-init)Added [-[JSContext initWithVirtualMachine:]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451554-initwithvirtualmachine)Added [-[JSContext objectForKeyedSubscript:]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451771-objectforkeyedsubscript)Added [-[JSContext setObject:forKeyedSubscript:]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451416-setobject)Added [JSContext.virtualMachine](https://developer.apple.com/documentation/javascriptcore/jscontext/1451510-virtualmachine)Added JSContext(JSContextRefSupport)Added JSContext(SubscriptSupport)Added #def JSContext_hJSExport.hAdded [JSExport](https://developer.apple.com/documentation/javascriptcore/jsexport)Added #def JSExportAsJSManagedValue.hAdded [JSManagedValue](https://developer.apple.com/documentation/javascriptcore/jsmanagedvalue)Added [-[JSManagedValue initWithValue:]](https://developer.apple.com/documentation/javascriptcore/jsmanagedvalue/1451420-init)Added [+[JSManagedValue managedValueWithValue:]](https://developer.apple.com/documentation/javascriptcore/jsmanagedvalue/1501484-managedvaluewithvalue)Added [-[JSManagedValue value]](https://developer.apple.com/documentation/javascriptcore/jsmanagedvalue/1451448-value)Added #def JSManagedValue_hJSValue.hAdded [JSValue](https://developer.apple.com/documentation/javascriptcore/jsvalue)Added [-[JSValue JSValueRef]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451639-jsvalueref)Added [-[JSValue callWithArguments:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451648-call)Added [-[JSValue constructWithArguments:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451480-constructwitharguments)Added [JSValue.context](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451518-context)Added [-[JSValue defineProperty:descriptor:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451542-defineproperty)Added [-[JSValue deleteProperty:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451609-deleteproperty)Added [-[JSValue hasProperty:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451361-hasproperty)Added [-[JSValue invokeMethod:withArguments:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451666-invokemethod)Added [-[JSValue isBoolean]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451367-isboolean)Added [-[JSValue isEqualToObject:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451504-isequaltoobject)Added [-[JSValue isEqualWithTypeCoercionToObject:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451765-isequalwithtypecoerciontoobject)Added [-[JSValue isInstanceOf:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451691-isinstance)Added [-[JSValue isNull]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451369-isnull)Added [-[JSValue isNumber]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451682-isnumber)Added [-[JSValue isObject]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451461-isobject)Added [-[JSValue isString]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451427-isstring)Added [-[JSValue isUndefined]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451365-isundefined)Added [-[JSValue objectAtIndexedSubscript:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451549-objectatindexedsubscript)Added [-[JSValue objectForKeyedSubscript:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451371-objectforkeyedsubscript)Added [-[JSValue setObject:atIndexedSubscript:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451583-setobject)Added [-[JSValue setObject:forKeyedSubscript:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451672-setobject)Added [-[JSValue setValue:atIndex:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451533-setvalue)Added [-[JSValue setValue:forProperty:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451676-setvalue)Added [-[JSValue toArray]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451465-toarray)Added [-[JSValue toBool]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451373-tobool)Added [-[JSValue toDate]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451753-todate)Added [-[JSValue toDictionary]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451728-todictionary)Added [-[JSValue toDouble]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451581-todouble)Added [-[JSValue toInt32]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451493-toint32)Added [-[JSValue toNumber]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451459-tonumber)Added [-[JSValue toObject]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451725-toobject)Added [-[JSValue toObjectOfClass:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451760-toobjectof)Added [-[JSValue toPoint]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451591-topoint)Added [-[JSValue toRange]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451423-torange)Added [-[JSValue toRect]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451389-torect)Added [-[JSValue toSize]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451495-tosize)Added [-[JSValue toString]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451409-tostring)Added [-[JSValue toUInt32]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451739-touint32)Added [-[JSValue valueAtIndex:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451602-valueatindex)Added [-[JSValue valueForProperty:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451438-valueforproperty)Added [+[JSValue valueWithBool:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451616-init)Added [+[JSValue valueWithDouble:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451482-valuewithdouble)Added [+[JSValue valueWithInt32:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451434-init)Added [+[JSValue valueWithJSValueRef:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451641-init)Added [+[JSValue valueWithNewArrayInContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451473-init)Added [+[JSValue valueWithNewErrorFromMessage:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451630-valuewithnewerrorfrommessage)Added [+[JSValue valueWithNewObjectInContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451751-init)Added [+[JSValue valueWithNewRegularExpressionFromPattern:flags:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451539-valuewithnewregularexpressionfro)Added [+[JSValue valueWithNullInContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451463-valuewithnullincontext)Added [+[JSValue valueWithObject:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451694-valuewithobject)Added [+[JSValue valueWithPoint:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451382-valuewithpoint)Added [+[JSValue valueWithRange:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451628-valuewithrange)Added [+[JSValue valueWithRect:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451664-init)Added [+[JSValue valueWithSize:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451715-valuewithsize)Added [+[JSValue valueWithUInt32:inContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451402-init)Added [+[JSValue valueWithUndefinedInContext:]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451387-init)Added [JSPropertyDescriptorConfigurableKey](https://developer.apple.com/documentation/javascriptcore/jspropertydescriptorconfigurablekey)Added [JSPropertyDescriptorEnumerableKey](https://developer.apple.com/documentation/javascriptcore/jspropertydescriptorenumerablekey)Added [JSPropertyDescriptorGetKey](https://developer.apple.com/documentation/javascriptcore/jspropertydescriptorgetkey)Added [JSPropertyDescriptorSetKey](https://developer.apple.com/documentation/javascriptcore/jspropertydescriptorsetkey)Added [JSPropertyDescriptorValueKey](https://developer.apple.com/documentation/javascriptcore/jspropertydescriptorvaluekey)Added [JSPropertyDescriptorWritableKey](https://developer.apple.com/documentation/javascriptcore/jspropertydescriptorwritablekey)Added JSValue(JSValueRefSupport)Added JSValue(StructSupport)Added JSValue(SubscriptSupport)Added #def JSValue_hJSValueRef.hModified [JSValueGetType()](https://developer.apple.com/documentation/javascriptcore/1395918-jsvaluegettype)

|  | Declaration |
| --- | --- |
| From | JSType JSValueGetType ( JSContextRef ctx, JSValueRef value); |
| To | JSType JSValueGetType ( JSContextRef ctx, JSValueRef); |

JSVirtualMachine.hAdded [JSVirtualMachine](https://developer.apple.com/documentation/javascriptcore/jsvirtualmachine)Added [-[JSVirtualMachine addManagedReference:withOwner:]](https://developer.apple.com/documentation/javascriptcore/jsvirtualmachine/1451354-addmanagedreference)Added [-[JSVirtualMachine init]](https://developer.apple.com/documentation/javascriptcore/jsvirtualmachine/1451568-init)Added [-[JSVirtualMachine removeManagedReference:withOwner:]](https://developer.apple.com/documentation/javascriptcore/jsvirtualmachine/1451452-removemanagedreference)

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
