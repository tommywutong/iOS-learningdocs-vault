---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/EOQualifierComparison.html
archived_at: '2026-07-18T01:28:33.196903Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOObserving.md)
[!](EOQualifierEvaluation.md)

---

# EOQualifier.Comparison

__Implemented By:__
NSObject (Yellow Box)

__Package:__
com.apple.client.eocontrol (Java Client)

## Interface Description

The EOQualifierComparison interface defines methods for comparing values. These methods are used for evaluating qualifiers in memory. Though declared for NSObject in Yellow Box, most of these methods work properly only with value classes: NSString, NSDate, NSNumber, NSDecimalNumber, and EONullValue. Yellow Box implements these methods as part of NSObject-there is no separate interface. In Java Client, support for these methods is provided for java.lang.String, java.lang.Number, and java.lang.Date using [EOQualifier.ComparisonSupport](EOQualifier.ComparisonSupport.md). You should implement this interface for any value classes you write that you want to be evaluated in memory by EOQualifier instances.

## Method Types

**Testing value objects**

**- doesContain

**- isEqualTo

**- isGreaterThan

**- isGreaterThanOrEqualTo

**- isLessThan

**- isLessThanOrEqualTo

**- isLike

**- isCaseInsensitiveLike

**- isNotEqualTo******************

## Instance Methods

---

#### doesContain

public abstract boolean __doesContain__ (java.lang.Object _anObject_)

Returns __true__ if the receiver contains _anObject_, __false__ if it doesn't. NSObject's implementation of this method returns __true__ only if the receiver is a kind of NSArray and contains _anObject_. In all other cases it returns __false__ .

---

#### isCaseInsensitiveLike

public abstract boolean __isCaseInsensitiveLike__ (java.lang.Object _anObject_)

Returns __true__ if the receiver is a case-insensitive match for _aStrin__g_, __false__ if it isn't. See "Using Wildcards" in the EOQualifier class specification for the wildcard characters allowed. NSObject's implementation returns __false__ ; NSString's performs a proper case-insensitive comparison.

__See also:__ - __isLike__ , - __doesContain__ , - __isEqualTo__ , - __isGreaterThan__ , - __isGreaterThanOrEqualTo__ , - __isLessThan__ , - __isLessThanOrEqualTo__ ,- __isNotEqualTo__

---

#### isEqualTo

public abstract boolean __isEqualTo__ (java.lang.Object _anObject_)

Returns __true__ if the receiver is equal to _anObject_, __false__ if it isn't. NSObject's implementation invokes __isEqual__ and returns the result.

__See also:__ - __doesContain__ , - __isGreaterThan__ , - __isGreaterThanOrEqualTo__ , - __isLessThan__ , - __isLessThanOrEqualTo__ , - __isLike__ , - __isCaseInsensitiveLike__ , - __isNotEqualTo__

---

#### isGreaterThan

public abstract boolean __isGreaterThan__ (java.lang.Object _anObject_)

Returns __true__ if the receiver is greater than _anObject_, __false__ if it isn't. NSObject's implementation invokes __compare:__ and returns __true__ if the result is NSOrderedDescending.

__See also:__ - __doesContain__ , - __isEqualTo__ , - __isGreaterThanOrEqualTo__ , - __isLessThan__ , - __isLessThanOrEqualTo__ , - __isLike__ , - __isCaseInsensitiveLike__ , - __isNotEqualTo__

---

#### isGreaterThanOrEqualTo

public abstract boolean __isGreaterThanOrEqualTo__ (java.lang.Object _anObject_)

Returns __true__ if the receiver is greater than or equal to _anObject_, __false__ if it isn't. NSObject's implementation invokes `compare:` and returns __true__ if the result is NSOrderedAscending.

__See also:__ - __doesContain__ , - __isEqualTo__ , - __isGreaterThan__ , - __isLessThan__ , - __isLessThanOrEqualTo__ , - __isLike__ , - __isCaseInsensitiveLike__ , - __isNotEqualTo__

---

#### isLessThan

public abstract boolean __isLessThan__ (java.lang.Object _anObject_)

Returns __true__ if the receiver is less than _anObject_, __false__ if it isn't. NSObject's implementation invokes `compare:` and returns __true__ if the result is NSOrderedAscending.

__See also:__ - __doesContain__ , - __isEqualTo__ , - __isGreaterThan__ , - __isGreaterThanOrEqualTo__ , - __isLessThanOrEqualTo__ , - __isLike__ , - __isCaseInsensitiveLike__ , - __isNotEqualTo__

---

#### isLessThanOrEqualTo

public abstract boolean __isLessThanOrEqualTo__ (java.lang.Object _anObject_)

Returns __true__ if the receiver is less than or equal to _anObject_, __false__ if it isn't. NSObject's implementation invokes `compare:` and returns __true__ if the result is NSOrderedAscending or NSOrderedSame.

__See also:__ - __doesContain__ , - __isEqualTo__ , - __isGreaterThan__ , - __isGreaterThanOrEqualTo__ , - __isLessThan__ , - __isLike__ , - __isCaseInsensitiveLike__ , - __isNotEqualTo__

---

#### isLike

public abstract boolean __isLike__ (java.lang.Object _anObject_)

Returns __true__ if the receiver matches _aString_ according to the semantics of the SQL __like__ comparison operator, __false__ if it doesn't. See "Using Wildcards" in the EOQualifier class specification for the wildcard characters allowed. NSObject's implementation returns __false__ ; NSString's performs a proper comparison.

__See also:__ - __isCaseInsensitiveLike__ , - __doesContain__ , - __isEqualTo__ , - __isGreaterThan__ , - __isGreaterThanOrEqualTo__ , - __isLessThan__ , - __isLessThanOrEqualTo__ , - __isNotEqualTo__

---

#### isNotEqualTo

public abstract boolean __isNotEqualTo__ (java.lang.Object _anObject_)

Returns __true__ if the receiver is not equal to _anObject_, __false__ if it is. NSObject's implementation invokes __isEqual__ , inverts the result, and returns it.

__See also:__ - __doesContain__ , - __isEqualTo__ , - __isGreaterThan__ , - __isGreaterThanOrEqualTo__ , - __isLessThan__ , - __isLessThanOrEqualTo__ , - __isLike__ , - __isCaseInsensitiveLike__

---

[!](EOObserving.md)
[!](EOQualifierEvaluation.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
