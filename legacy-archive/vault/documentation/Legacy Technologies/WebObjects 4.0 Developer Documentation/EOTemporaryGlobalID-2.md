---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOTemporaryGlobalID.html
archived_at: '2026-07-18T01:28:37.433097Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOSortOrdering-2.md)
[!](EOUndoManager.md)

---

# EOTemporaryGlobalID

__Inherits From:__
[EOGlobalID](EOFaultHandler-2.md) : NSObject

__Conforms To:__ NSCoding
NSCopying (EOGlobalID)
NSObject (NSObject)

__Declared in:__ EOControl/EOGlobalID.h

An EOTemporaryGlobalID object identifies a newly created enterprise object before it's saved to an external store. When the object is saved, the temporary ID is converted to a permanent one, as described in the [EOGlobalID](EOFaultHandler-2.md) class specification.

---

## Adopted Protocols

**NSCoding**

**- encodeWithCoder:

**- initWithCoder:****

---

#### assignGloballyUniqueBytes:

+ (void)`assignGloballyUniqueBytes:`(unsigned char \*)_buffer_

Assigns a network-wide unique ID of the format:

> ```
> < Sequence [2], ProcessID [2] , Time [4], IP Addr [4] >
> ```

_buffer_ should have space for EOUniqueBinaryKeyLength (12) bytes.

---

#### init

- (id)__init__

Initializes a newly allocated EOTemporaryGlobalID as a unique instance. The new temporary global ID contains a byte string obtained from __assignGloballyUniqueBytes:__ that's guaranteed to be unique network-wide. As a result, EOTemporaryGlobalIDs can be safely passed between processes and machines while still preserving global uniqueness.

_buffer_ should have space for EOUniqueBinaryKeyLength (12) bytes.

---

#### isTemporary

- (BOOL)__isTemporary__

Returns YES.

---

[!](EOSortOrdering-2.md)
[!](EOUndoManager.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
