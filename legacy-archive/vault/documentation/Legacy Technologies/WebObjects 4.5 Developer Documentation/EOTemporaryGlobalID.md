---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOTemporaryGlobalID.html
archived_at: '2026-07-15T08:11:38.004535Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOTemporaryGlobalID

> **__Inherits
> from:__**
> : [(com.apple.client.eocontrol) EOGlobalID](EOGlobalID.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuo3dpmjqwyske) : Object
> (com.apple.yellow.eocontrol) EOGlobalID : NSObject

> **__Implements:__**
> : (com.apple.client.eocontrol only) Cloneable

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Class Description

---

An EOTemporaryGlobalID object identifies a newly created enterprise
object before it's saved to an external store. When the object
is saved, the temporary ID is converted to a permanent one, as described in
the [EOGlobalID](EOGlobalID.md#apple-ivhuo3dpmjqwyske) class specification.

## Constants

---

(com.apple.yellow.eocontrol only) EOTemporaryGlobalID defines
the following `int` constant
to specify the length (in bytes) of a global ID:

- UniqueBinaryKeyLength

## Constructors

---

### EOTemporaryGlobalID

`public EOTemporaryGlobalID()`

(com.apple.yellow.eocontrol only) Creates and
returns an EOTemporaryGlobalID as a unique instance. The returned
object contains a byte string that's guaranteed to be unique network-wide.
As a result, EOTemporaryGlobalIDs can be safely passed between processes
and machines while still preserving global uniqueness. The returned
byte string has the format:
> ```
> < Sequence [2], ProcessID [2], Time [4], IP Addr [4] >
> ```

---

## Instance Methods

---

### isTemporary

`public boolean isTemporary()`

Returns true.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
