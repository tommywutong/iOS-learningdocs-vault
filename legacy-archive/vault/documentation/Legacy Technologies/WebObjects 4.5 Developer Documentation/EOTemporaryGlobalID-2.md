---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOTemporaryGlobalID.html
archived_at: '2026-07-15T08:11:40.057653Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOTemporaryGlobalID

> **__Inherits
> from:__**
> : [EOGlobalID](EOGlobalID-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5dwy33cmfwesra) : NSObject

> **__Conforms to:__**
> : NSCoding
> : NSCopying (EOGlobalID)
> : NSObject (NSObject)

> __Declared in:__ : EOControl/EOGlobalID.h

---

## Class Description

---

An EOTemporaryGlobalID object identifies a newly created enterprise
object before it's saved to an external store. When the object
is saved, the temporary ID is converted to a permanent one, as described in
the [EOGlobalID](EOGlobalID-2.md#apple-ivhuo3dpmjqwyske) class specification.

## Constants

---

In EOGlobalID.h, EOControl defines an
enumeration with the following constant to specify the length (in
bytes) of a global ID:

- EOUniqueBinaryKeyLength

## Adopted Protocols

---

> NSCoding: __- encodeWithCoder:__
> : __- initWithCoder:__

## Class Methods

---

### assignGloballyUniqueBytes:

`+ (void)assignGloballyUniqueBytes:(unsigned
char *)buffer`

Assigns a network-wide unique ID of the format:
> ```
> < Sequence [2], ProcessID [2] , Time [4], IP Addr [4] >
> ```

_buffer_ should
have space for EOUniqueBinaryKeyLength (12) bytes.

---

## Instance Methods

---

### init

`- (id)init`

Initializes a newly allocated EOTemporaryGlobalID
as a unique instance. The new temporary global ID contains a byte
string obtained from [assignGloballyUniqueBytes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvizlnobxxeylspfdwy33cmfwesrbpmfzxg2lhnzdwy33cmfwgy6kvnzuxc5lfij4xizlthi) that's
guaranteed to be unique network-wide. As a result, EOTemporaryGlobalIDs
can be safely passed between processes and machines while still
preserving global uniqueness.

---

### isTemporary

`- (BOOL)isTemporary`

Returns YES.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
