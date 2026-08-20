---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOTemporaryGlobalID.html
archived_at: '2026-07-15T08:13:47.429692Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOTemporaryGlobalID

> **__Inherits from:__**
> : [EOGlobalID](EOGlobalID.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuo3dpmjqwyske)

> **__Implements:__**
> : NSCoding

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

An EOTemporaryGlobalID object identifies a newly created enterprise object before it's saved to an external store. When the object is saved, the temporary ID is converted to a permanent one, as described in the EOGlobalID class specification.

## Constants

---

EOTemporaryGlobalID defines the following `int` constant to specify the length (in bytes) of a global ID:

- UniqueBinaryKeyLength

## Interfaces Implemented

---

> : NSCoding: [classForCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsw24dpojqxe6khnrxweylmjfcc6y3mmfzxgrtpojbw6zdfoi): [decodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vdfnvyg64tboj4uo3dpmjqwyskef5sgky3pmrsu6ytkmvrxi): [encodeWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsw24dpojqxe6khnrxweylmjfcc6zlomnxwizkxnf2gqq3pmrsxe):

## Constructors

---

### EOTemporaryGlobalID

`public EOTemporaryGlobalID()`

Creates and returns an EOTemporaryGlobalID as a unique instance. The returned object contains a byte string that's guaranteed to be unique network-wide. As a result, EOTemporaryGlobalIDs can be safely passed between processes and machines while still preserving global uniqueness. The returned byte string has the format:
> ```
> < Sequence [2], ProcessID [2] , Time [4], IP Addr [4] >
> ```

`protected EOTemporaryGlobalID(byte[] globallyUniqueBytes)`

Description forthcoming.

---

## Static Methods

---

### assignGloballyUniqueBytes

`public static void assignGloballyUniqueBytes(byte[] uniqueBytes)`

Description forthcoming.

---

### decodeObject

`public static Object decodeObject(NSCoder coder)`

Conformance to NSCoding.

---

## Instance Methods

---

### classForCoder

`public Class classForCoder()`

Conformance to NSCoding.

---

### encodeWithCoder

`public void encodeWithCoder(NSCoder coder)`

Conformance to NSCoding.

---

### __equals__

`public boolean equals(Object anObject)`

Description forthcoming.

---

### __hashCode__

`public int hashCode()`

Description forthcoming.

---

### isTemporary

`public boolean isTemporary()`

Returns true.

---

### __toString__

`public String toString()`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
