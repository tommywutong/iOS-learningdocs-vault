---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/JavaScriptCore.html
archived_at: '2026-07-18T02:56:14.190565Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# JavaScriptCore Changes

## JavaScriptCore

Modified JSContext

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified JSContext.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified JSContext.init(JSGlobalContextRef: JSGlobalContext!)

|  | Declaration |
| --- | --- |
| From | ``` init(JSGlobalContextRef jsGlobalContextRef: JSGlobalContext!) -> JSContext ``` |
| To | ``` init!(JSGlobalContextRef jsGlobalContextRef: JSGlobalContext!) -> JSContext ``` |

Modified JSContext.init(virtualMachine: JSVirtualMachine!)

|  | Declaration |
| --- | --- |
| From | ``` init(virtualMachine virtualMachine: JSVirtualMachine!) ``` |
| To | ``` init!(virtualMachine virtualMachine: JSVirtualMachine!) ``` |

Modified JSManagedValue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

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

Modified JSValue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified JSValue.init(JSValueRef: JSValue!, inContext: JSContext!)

|  | Declaration |
| --- | --- |
| From | ``` init(JSValueRef value: JSValue!, inContext context: JSContext!) -> JSValue ``` |
| To | ``` init!(JSValueRef value: JSValue!, inContext context: JSContext!) -> JSValue ``` |

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
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified JSVirtualMachine.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified JSContextGetGlobalContext(JSContext!) -> Unmanaged<JSGlobalContext>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified JSContextGetGroup(JSContext!) -> Unmanaged<JSContextGroup>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified JSContextGroupCreate() -> Unmanaged<JSContextGroup>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified JSGlobalContextCreate(JSClass!) -> Unmanaged<JSGlobalContext>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified JSGlobalContextCreateInGroup(JSContextGroup!, JSClass!) -> Unmanaged<JSGlobalContext>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified JSObjectMakeArray(JSContext!, UInt, UnsafePointer<Unmanaged<JSValue>?>, UnsafeMutablePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSObject>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified JSObjectMakeDate(JSContext!, UInt, UnsafePointer<Unmanaged<JSValue>?>, UnsafeMutablePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSObject>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified JSObjectMakeError(JSContext!, UInt, UnsafePointer<Unmanaged<JSValue>?>, UnsafeMutablePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSObject>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified JSObjectMakeRegExp(JSContext!, UInt, UnsafePointer<Unmanaged<JSValue>?>, UnsafeMutablePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSObject>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified JSValueCreateJSONString(JSContext!, JSValue!, UInt32, UnsafeMutablePointer<Unmanaged<JSValue>?>) -> Unmanaged<JSString>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified JSValueMakeFromJSONString(JSContext!, JSString!) -> Unmanaged<JSValue>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

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
