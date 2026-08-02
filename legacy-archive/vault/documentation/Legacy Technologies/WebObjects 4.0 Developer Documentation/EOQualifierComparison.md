---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/EOQualifierComparison.html
archived_at: '2026-07-18T01:28:41.534941Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EORelationshipManipulation-2.md)
[!](EOSortOrderingComparison.md)

---

# EOQualifierComparison

---

#### (informal protocol)

__Category Of:__ NSObject

__Declared in:__ EOControl/EOQualifier.h

## Protocol Description

The EOQualifierComparison informal protocol defines methods for comparing values. These methods are used for evaluating qualifiers in memory. Though declared for NSObject, most of these methods work properly only with value classes: NSString, NSDate, NSNumber, NSDecimalNumber, and EONull

**Testing value objects**

**- doesContain:

**- isEqualTo:

**- isGreaterThan:

**- isGreaterThanOrEqualTo:

**- isLessThan:

**- isLessThanOrEqualTo:

**- isLike:

**- isCaseInsensitiveLike:

**- isNotEqualTo:******************

---

#### doesContain:

- (BOOL)__doesContain:__ (id)_anObject_

Returns YES if the receiver contains _anObject_, NO if it doesn't. NSObject's implementation of this method returns YES only if the receiver is a kind of NSArray and contains _anObject_. In all other cases it returns NO.

---

#### isCaseInsensitiveLike:

- (BOOL)`isCaseInsensitiveLike:`(NSString \*)_anObject_

Returns YES if the receiver is a case-insensitive match for _aStrin__g_, NO if it isn't. See "Using Wildcards" in the EOQualifier class specification for the wildcard characters allowed. NSObject's implementation returns NO; NSString's performs a proper case-insensitive comparison.

__See also:__ - __isLike:__ , - __doesContain:__ , - __isEqualTo:__ , - __isGreaterThan:__ , - __isGreaterThanOrEqualTo:__ , - __isLessThan:__ , - __isLessThanOrEqualTo:__ ,- __isNotEqualTo:__

---

#### isEqualTo:

- (BOOL)__isEqualTo:__ (id)_anObject_

Returns YES if the receiver is equal to _anObject_, NO if it isn't. NSObject's implementation invokes __isEqual:__ and returns the result.

__See also:__ - __doesContain:__ , - __isGreaterThan:__ , - __isGreaterThanOrEqualTo:__ , - __isLessThan:__ , - __isLessThanOrEqualTo:__ , - __isLike:__ , - __isCaseInsensitiveLike:__ , - __isNotEqualTo:__

---

#### isGreaterThan:

- (BOOL)__isGreaterThan:__ (id)_anObject_

Returns YES if the receiver is greater than _anObject_, NO if it isn't. NSObject's implementation invokes __compare:__ and returns YES if the result is NSOrderedDescending.

__See also:__ - __doesContain:__ , - __isEqualTo:__ , - __isGreaterThanOrEqualTo:__ , - __isLessThan:__ , - __isLessThanOrEqualTo:__ , - __isLike:__ , - __isCaseInsensitiveLike:__ , - __isNotEqualTo:__

---

#### isGreaterThanOrEqualTo:

- (BOOL)__isGreaterThanOrEqualTo:__ (id)_anObject_

Returns YES if the receiver is greater than or equal to _anObject_, NO if it isn't. NSObject's implementation invokes `compare:` and returns YES if the result is NSOrderedAscending.

__See also:__ - __doesContain:__ , - __isEqualTo:__ , - __isGreaterThan:__ , - __isLessThan:__ , - __isLessThanOrEqualTo:__ , - __isLike:__ , - __isCaseInsensitiveLike:__ , - __isNotEqualTo:__

---

#### isLessThan:

- (BOOL)__isLessThan:__ (id)_anObject_

Returns YES if the receiver is less than _anObject_, NO if it isn't. NSObject's implementation invokes `compare:` and returns YES if the result is NSOrderedAscending.

__See also:__ - __doesContain:__ , - __isEqualTo:__ , - __isGreaterThan:__ , - __isGreaterThanOrEqualTo:__ , - __isLessThanOrEqualTo:__ , - __isLike:__ , - __isCaseInsensitiveLike:__ , - __isNotEqualTo:__

---

#### isLessThanOrEqualTo:

- (BOOL)__isLessThanOrEqualTo:__ (id)_anObject_

Returns YES if the receiver is less than or equal to _anObject_, NO if it isn't. NSObject's implementation invokes `compare:` and returns YES if the result is NSOrderedAscending or NSOrderedSame.

__See also:__ - __doesContain:__ , - __isEqualTo:__ , - __isGreaterThan:__ , - __isGreaterThanOrEqualTo:__ , - __isLessThan:__ , - __isLike:__ , - __isCaseInsensitiveLike:__ , - __isNotEqualTo:__

---

#### isLike:

- (BOOL)__isLike:__ (NSString \*)_aString_

Returns YES if the receiver matches _aString_ according to the semantics of the SQL __like__ comparison operator, NO if it doesn't. See "Using Wildcards" in the EOQualifier class specification for the wildcard characters allowed. NSObject's implementation returns NO; NSString's performs a proper comparison.

__See also:__ - __isCaseInsensitiveLike:__ , - __doesContain:__ , - __isEqualTo:__ , - __isGreaterThan:__ , - __isGreaterThanOrEqualTo:__ , - __isLessThan:__ , - __isLessThanOrEqualTo:__ , - __isNotEqualTo:__

---

#### isNotEqualTo:

- (BOOL)__isNotEqualTo:__ (id)_anObject_

Returns YES if the receiver is not equal to _anObject_, NO if it is. NSObject's implementation invokes __isEqual:__ , inverts the result, and returns it.

__See also:__ - __doesContain:__ , - __isEqualTo:__ , - __isGreaterThan:__ , - __isGreaterThanOrEqualTo:__ , - __isLessThan:__ , - __isLessThanOrEqualTo:__ , - __isLike:__ , - __isCaseInsensitiveLike:__

---

[!](EORelationshipManipulation-2.md)
[!](EOSortOrderingComparison.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
