---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/EOSortOrderingComparison.html
archived_at: '2026-07-18T01:28:41.744928Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOQualifierComparison.md)
[!](EOValidation-3.md)

---

# EOSortOrderingComparison

---

#### (informal protocol)

__Category Of:__ NSObject

__Declared in:__ EOControl/EOSortOrdering.h

## Protocol Description

The EOSortOrderingComparison informal protocol defines methods for comparing values. These methods are used for sorting value objects. Though declared for NSObject, most of these methods work properly only with value classes: NSString, NSDate, NSNumber, NSDecimalNumber, and EONull

**Sorting value objects**

**- compareAscending:

**- compareCaseInsensitiveAscending:

**- compareCaseInsensitiveDescending:

**- compareDescending:********

---

#### compareAscending:

- (NSComparisonResult)__compareAscending:__ (id)_anObject_

Returns NSOrderedAscending if _anObject_ is naturally ordered after the receiver, NSOrderedDescending if it's naturally ordered before the receiver, and NSOrderedSame if they're equivalent for ordering purposes. NSObject's implementation of this method simply invokes __compare:__ .

__See also:__ - __compareDescending:__ , - __compareCaseInsensitiveAscending:__ , - __compareCaseInsensitiveDescending:__

---

#### compareCaseInsensitiveAscending:

- (NSComparisonResult)__compareCaseInsensitiveAscending:__ (id)_anObject_

Returns NSOrderedAscending if _anObject_ is naturally ordered-ignoring case-after the receiver, NSOrderedDescending if it's naturally ordered before the receiver, and NSOrderedSame if they're equivalent for ordering purposes. NSObject's implementation of this method invokes __compare:__ , while NSString's invokes __caseInsensitiveCompare:__ .

__See also:__ - __compareCaseInsensitiveDescending:__ , - __compareAscending:__ , - __compareDescending:__

---

#### compareCaseInsensitiveDescending:

- (NSComparisonResult)__compareCaseInsensitiveDescending:__ (id)_anObject_

Returns NSOrderedAscending if _anObject_ is naturally ordered-ignoring case-_before_ the receiver, NSOrderedDescending if it's naturally ordered _after_ the receiver, and NSOrderedSame if they're equivalent for ordering purposes. NSObject's implementation of this method invokes __compare:__ and inverts the result, while NSString's invokes __caseInsensitiveCompare:__ and inverts the result.

__See also:__ - __compareCaseInsensitiveAscending:__ , - __compareDescending:__ , - __compareAscending:__

---

#### compareDescending:

- (NSComparisonResult)__compareDescending:__ (id)_anObject_

Returns NSOrderedAscending if _anObject_ is naturally ordered _before_ the receiver, NSOrderedDescending if it's naturally ordered _after_ the receiver, and NSOrderedSame if they're equivalent for ordering purposes. NSObject's implementation of this method simply invokes __compare:__ and inverts the result.

__See also:__ - __compareAscending:__ , - __compareCaseInsensitiveDescending:__ , - __compareCaseInsensitiveAscending:__

---

[!](EOQualifierComparison.md)
[!](EOValidation-3.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
