---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/EOSortOrderingComparison.html
archived_at: '2026-07-18T01:28:33.466375Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EORelationshipManipulation.md)
[!](EOValidation.md)

---

# EOSortOrdering.Comparison

__Implemented By:__
EONullValue (Java Client)
NSObject (Yellow Box)

__Package:__
com.apple.client.eocontrol (Java Client)

## Interface Description

The EOSortOrdering.Comparison interface defines methods for comparing values. These methods are used for sorting value objects. Though declared for NSObject in Yellow Box, most of these methods work properly only with value classes: NSString, NSDate, NSNumber, NSDecimalNumber, and EONullValue. Yellow Box implements these methods as part of NSObject-there is no separate interface. In Java Client, support for these methods is provided for java.lang.String, java.lang.Number, and java.lang.Date using [EOSortOrdering.ComparisonSupport](EOSortOrdering.ComparisonSupport.md). EONullValue implements the interface directly. You should implement this interface for any value classes you write that you want to be properly sorted by EOSortOrdering instances.

**Sorting value objects**

**- compareAscending

**- compareCaseInsensitiveAscending

**- compareCaseInsensitiveDescending

**- compareDescending********

## Instance Methods

---

#### compareAscending

public abstract int __compareAscending__ (java.lang.Object _anObject_)

Returns NSOrderedAscending if _anObject_ is naturally ordered after the receiver, NSOrderedDescending if it's naturally ordered before the receiver, and NSOrderedSame if they're equivalent for ordering purposes. NSObject's implementation of this method simply invokes __compare__ .

__See also:__ - __compareDescending__ , - __compareCaseInsensitiveAscending__ , - __compareCaseInsensitiveDescending__

---

#### compareCaseInsensitiveAscending

public abstract int __compareCaseInsensitiveAscending__ (java.lang.Object _anObject_)

Returns NSOrderedAscending if _anObject_ is naturally ordered-ignoring case-after the receiver, NSOrderedDescending if it's naturally ordered before the receiver, and NSOrderedSame if they're equivalent for ordering purposes. NSObject's implementation of this method invokes __compare__ , while NSString's invokes __caseInsensitiveCompare__ .

__See also:__ - __compareCaseInsensitiveDescending__ , - __compareAscending__ , - __compareDescending__

---

#### compareCaseInsensitiveDescending

public abstract int __compareCaseInsensitiveDescending__ (java.lang.Object _anObject_)

Returns NSOrderedAscending if _anObject_ is naturally ordered-ignoring case-_before_ the receiver, NSOrderedDescending if it's naturally ordered _after_ the receiver, and NSOrderedSame if they're equivalent for ordering purposes. NSObject's implementation of this method invokes __compare__ and inverts the result, while NSString's invokes __caseInsensitiveCompare__ and inverts the result.

__See also:__ - __compareCaseInsensitiveAscending__ , - __compareDescending__ , - __compareAscending__

---

#### compareDescending

public abstract int __compareDescending__ (java.lang.Object _anObject_)

Returns NSOrderedAscending if _anObject_ is naturally ordered _before_ the receiver, NSOrderedDescending if it's naturally ordered _after_ the receiver, and NSOrderedSame if they're equivalent for ordering purposes. NSObject's implementation of this method simply invokes __compare__ and inverts the result.

__See also:__ - __compareAscending__ , - __compareCaseInsensitiveDescending__ , - __compareCaseInsensitiveAscending__

---

[!](EORelationshipManipulation.md)
[!](EOValidation.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
