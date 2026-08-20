---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/JavaScriptCore.html
archived_at: '2026-07-18T02:50:40.099906Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# JavaScriptCore Changes for Objective-C

### JavaScriptCore

#### JSBase.h

Added [JSTypedArrayBytesDeallocator](https://developer.apple.com/documentation/javascriptcore/jstypedarraybytesdeallocator)

#### JSTypedArray.h (Added)

Added [JSObjectGetArrayBufferByteLength()](https://developer.apple.com/documentation/javascriptcore/1644609-jsobjectgetarraybufferbytelength)Added [JSObjectGetArrayBufferBytesPtr()](https://developer.apple.com/documentation/javascriptcore/1644605-jsobjectgetarraybufferbytesptr)Added [JSObjectGetTypedArrayBuffer()](https://developer.apple.com/documentation/javascriptcore/1644604-jsobjectgettypedarraybuffer)Added [JSObjectGetTypedArrayByteLength()](https://developer.apple.com/documentation/javascriptcore/1644600-jsobjectgettypedarraybytelength)Added [JSObjectGetTypedArrayByteOffset()](https://developer.apple.com/documentation/javascriptcore/1644608-jsobjectgettypedarraybyteoffset)Added [JSObjectGetTypedArrayBytesPtr()](https://developer.apple.com/documentation/javascriptcore/1644602-jsobjectgettypedarraybytesptr)Added [JSObjectGetTypedArrayLength()](https://developer.apple.com/documentation/javascriptcore/1644601-jsobjectgettypedarraylength)Added [JSObjectMakeArrayBufferWithBytesNoCopy()](https://developer.apple.com/documentation/javascriptcore/1644606-jsobjectmakearraybufferwithbytes)Added [JSObjectMakeTypedArray()](https://developer.apple.com/documentation/javascriptcore/1644597-jsobjectmaketypedarray)Added [JSObjectMakeTypedArrayWithArrayBuffer()](https://developer.apple.com/documentation/javascriptcore/1644598-jsobjectmaketypedarraywitharrayb)Added [JSObjectMakeTypedArrayWithArrayBufferAndOffset()](https://developer.apple.com/documentation/javascriptcore/1644599-jsobjectmaketypedarraywitharrayb)Added [JSObjectMakeTypedArrayWithBytesNoCopy()](https://developer.apple.com/documentation/javascriptcore/1644607-jsobjectmaketypedarraywithbytesn)Added #def JSTypedArray_h

#### JSValueRef.h

Added [JSTypedArrayType](https://developer.apple.com/documentation/javascriptcore/jstypedarraytype)Added [JSValueGetTypedArrayType()](https://developer.apple.com/documentation/javascriptcore/1644616-jsvaluegettypedarraytype)Added [kJSTypedArrayTypeArrayBuffer](https://developer.apple.com/documentation/javascriptcore/kjstypedarraytypearraybuffer)Added [kJSTypedArrayTypeFloat32Array](https://developer.apple.com/documentation/javascriptcore/jstypedarraytype/kjstypedarraytypefloat32array)Added [kJSTypedArrayTypeFloat64Array](https://developer.apple.com/documentation/javascriptcore/kjstypedarraytypefloat64array)Added [kJSTypedArrayTypeInt16Array](https://developer.apple.com/documentation/javascriptcore/jstypedarraytype/kjstypedarraytypeint16array)Added [kJSTypedArrayTypeInt32Array](https://developer.apple.com/documentation/javascriptcore/jstypedarraytype/kjstypedarraytypeint32array)Added [kJSTypedArrayTypeInt8Array](https://developer.apple.com/documentation/javascriptcore/jstypedarraytype/kjstypedarraytypeint8array)Added [kJSTypedArrayTypeNone](https://developer.apple.com/documentation/javascriptcore/kjstypedarraytypenone)Added [kJSTypedArrayTypeUint16Array](https://developer.apple.com/documentation/javascriptcore/jstypedarraytype/kjstypedarraytypeuint16array)Added [kJSTypedArrayTypeUint32Array](https://developer.apple.com/documentation/javascriptcore/kjstypedarraytypeuint32array)Added [kJSTypedArrayTypeUint8Array](https://developer.apple.com/documentation/javascriptcore/jstypedarraytype/kjstypedarraytypeuint8array)Added [kJSTypedArrayTypeUint8ClampedArray](https://developer.apple.com/documentation/javascriptcore/kjstypedarraytypeuint8clampedarray)

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
