---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/JavaScriptCore.html
archived_at: '2026-07-15T07:34:46.343178Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# JavaScriptCore Changes

## JavaScriptCore

JSContext.hRemoved [-[JSContext JSGlobalContextRef]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451338-jsglobalcontextref)Removed [-[JSContext globalObject]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451436-globalobject)Added [JSContext.JSGlobalContextRef](https://developer.apple.com/documentation/javascriptcore/jscontext/1451338-jsglobalcontextref)Added [+[JSContext currentCallee]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451762-currentcallee)Added [-[JSContext evaluateScript:withSourceURL:]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451384-evaluatescript)Added [JSContext.globalObject](https://developer.apple.com/documentation/javascriptcore/jscontext/1451436-globalobject)Added [JSContext.name](https://developer.apple.com/documentation/javascriptcore/jscontext/1451399-name)Modified [JSContext.exception](https://developer.apple.com/documentation/javascriptcore/jscontext/1451499-exception)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) JSValue *exception ``` |
| To | ``` @property(strong) JSValue *exception ``` |

Modified [-[JSContext init]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451742-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

Modified [-[JSContext initWithVirtualMachine:]](https://developer.apple.com/documentation/javascriptcore/jscontext/1451554-initwithvirtualmachine)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithVirtualMachine:(JSVirtualMachine *)virtualMachine ``` |
| To | ``` - (instancetype)initWithVirtualMachine:(JSVirtualMachine *)virtualMachine ``` |

Modified [JSContext.virtualMachine](https://developer.apple.com/documentation/javascriptcore/jscontext/1451510-virtualmachine)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) JSVirtualMachine *virtualMachine ``` |
| To | ``` @property(readonly, strong) JSVirtualMachine *virtualMachine ``` |

JSContextRef.hAdded [JSContextGetGlobalContext()](https://developer.apple.com/documentation/javascriptcore/1451674-jscontextgetglobalcontext)Added [JSGlobalContextCopyName()](https://developer.apple.com/documentation/javascriptcore/1451356-jsglobalcontextcopyname)Added [JSGlobalContextSetName()](https://developer.apple.com/documentation/javascriptcore/1451703-jsglobalcontextsetname)JSManagedValue.hRemoved [-[JSManagedValue value]](https://developer.apple.com/documentation/javascriptcore/jsmanagedvalue/1451448-value)Added [+[JSManagedValue managedValueWithValue:andOwner:]](https://developer.apple.com/documentation/javascriptcore/jsmanagedvalue/1451607-managedvaluewithvalue)Added [JSManagedValue.value](https://developer.apple.com/documentation/javascriptcore/jsmanagedvalue/1451448-value)Modified [-[JSManagedValue initWithValue:]](https://developer.apple.com/documentation/javascriptcore/jsmanagedvalue/1451420-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithValue:(JSValue *)value ``` |
| To | ``` - (instancetype)initWithValue:(JSValue *)value ``` |

JSValue.hRemoved [-[JSValue JSValueRef]](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451639-jsvalueref)Added [JSValue.JSValueRef](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451639-jsvalueref)Modified [JSValue.context](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451518-context)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) JSContext *context ``` |
| To | ``` @property(readonly, strong) JSContext *context ``` |

JSVirtualMachine.hModified [-[JSVirtualMachine init]](https://developer.apple.com/documentation/javascriptcore/jsvirtualmachine/1451568-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

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
