---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/JavaScriptCore.html
archived_at: '2026-07-18T02:53:08.353261Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# JavaScriptCore Changes for Objective-C

### JavaScriptCore

#### JSBase.h

Removed #def WTF_EXPORT_PRIVATE

#### JSValue.h

Added [JSValue.isArray](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451575-isarray)Added [JSValue.isDate](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451668-isdate)Modified [JSValue.isBoolean](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451367-isboolean)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isBoolean ``` |
| To | ``` @property(readonly) BOOL isBoolean ``` |

Modified [JSValue.isNull](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451369-isnull)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isNull ``` |
| To | ``` @property(readonly) BOOL isNull ``` |

Modified [JSValue.isNumber](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451682-isnumber)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isNumber ``` |
| To | ``` @property(readonly) BOOL isNumber ``` |

Modified [JSValue.isObject](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451461-isobject)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isObject ``` |
| To | ``` @property(readonly) BOOL isObject ``` |

Modified [JSValue.isString](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451427-isstring)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isString ``` |
| To | ``` @property(readonly) BOOL isString ``` |

Modified [JSValue.isUndefined](https://developer.apple.com/documentation/javascriptcore/jsvalue/1451365-isundefined)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isUndefined ``` |
| To | ``` @property(readonly) BOOL isUndefined ``` |

#### JSValueRef.h

Added [JSValueIsArray()](https://developer.apple.com/documentation/javascriptcore/1395924-jsvalueisarray)Added [JSValueIsDate()](https://developer.apple.com/documentation/javascriptcore/1395926-jsvalueisdate)

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
