---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOTemporaryGlobalID.html
archived_at: '2026-07-18T01:28:27.541698Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOSortOrdering.ComparisonSupport.md)
[!](EOClassDescription.ClassDelegate.md)

---

# EOTemporaryGlobalID

__Inherits From:__
[EOGlobalID](EOGlobalID.md) : NSObject

__Implements:__
java.lang.Cloneable (Java Client only)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (WebObjects and Yellow Box)

## Class Description

An EOTemporaryGlobalID object identifies a newly created enterprise object before it's saved to an external store. When the object is saved, the temporary ID is converted to a permanent one, as described in the [EOGlobalID](EOGlobalID.md) class specification.

## Constructors

---

#### EOTemporaryGlobalID

public __EOTemporaryGlobalID__ ()

Creates and returns an EOTemporaryGlobalID as a unique instance. The returned object contains a byte string that's guaranteed to be unique network-wide. As a result, EOTemporaryGlobalIDs can be safely passed between processes and machines while still preserving global uniqueness. The returned byte string has the format:

> ```
>
>     < Sequence [2], ProcessID [2] , Time [4], IP Addr [4] >
> ```

## Instance Methods

---

#### isTemporary

public boolean __isTemporary__ ()

Returns __true__ .

---

[!](EOSortOrdering.ComparisonSupport.md)
[!](EOClassDescription.ClassDelegate.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
