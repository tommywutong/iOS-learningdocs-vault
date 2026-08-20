---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOQualifierComparisonSppt.html
archived_at: '2026-07-18T01:28:27.315241Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOQualifier-2.md)
[!](EOSortOrdering.md)

---

# EOQualifier.ComparisonSupport

__Inherits From:__
java.lang.Object

__Package:__
com.apple.client.eocontrol (Siva)

## Class Description

Siva's class EOQualifier.ComparisonSupport provides default implementations of the EOQualifierComparison interface. It is for use in client-side enterprise object classes only; there is no equivalent Yellow Box class for server-side enterprise objects.

Siva's EOCustomObject uses EOQualifier.ComparisonSupport's default implementations. Typically your custom enterprise object classes inherit from EOCustomObject and inherit the default implementations. If your custom enterprise object class doesn't inherit from EOCustomObject, you should implement the EOQualifierComparison interface directly.

## Method Types

**Setting up automatic support**

**[setSupportForClass](#apple-gq3deni)

**[supportForClass](#apple-gq3dgnq)****

**Comparing two objects**

**[compareValues](#apple-gq3dcna)**

**EOQualifierComparison methods**

**[compareValues](#apple-gq3dcna)

**[setSupportForClass](#apple-gq3deni)

**[supportForClass](#apple-gq3dgnq)

**EOQualifier.ComparisonSupport

**[doesContain](#apple-gqzdmma)

**[isCaseInsensitiveLike](#apple-gqzdmna)

**[isEqualTo](#apple-gqzdmoa)

**[isGreaterThan](#apple-gqzdomq)

**[isGreaterThanOrEqualTo](#apple-gqzdonq)

**[isLessThan](#apple-gqzdqma)

**[isLessThanOrEqualTo](#apple-gqzdqna)

**[isLike](#apple-gqzdqoa)

**[isNotEqualTo](#apple-gqzdsmq)**************************

## Static Methods

---

#### compareValues

public static int __compareValues__ (java.lang.Object _anObject_, java.lang.Object _anotherObject_, com.apple.client.foundation.NSSelector _selector_)

Compares the two objects using _selector_. You should use this method to compare value objects instead of calling _selector_ directly. This method is the entry point for the comparison support, and calls methods in support classes if appropriate.

__See also:__
[__setSupportForClass__](#apple-gq3deni), [__supportForClass__](#apple-gq3dgnq)

---

#### setSupportForClass

public static void __setSupportForClass__ (EOSortOrdering. ComparisonSupport _supportClass_, java.lang.Class _aClass_)

Sets _supportClass_ as the support class to be used for comparing instances of _aClass_. When [__compareValues__](#apple-gq3dcna) is called, the methods in _supportClass_ will be used to do the comparison for instances of _aClass_.

__See also:__
[__compareValues__](#apple-gq3dcna)

---

#### supportForClass

public static EOSortOrdering. ComparisonSupport __supportForClass__ (java.lang.Class _aClass_)

Returns the support class used for doing sort ordering comparisons for instances of _aClass_.

__See also:__
[__compareValues__](#apple-gq3dcna), [__setSupportForClass__](#apple-gq3deni)

## Instance Methods

---

#### doesContain

public boolean __doesContain__ (java.lang.Object _receiver_, java.lang.Object _anObject_)

Returns YES if _receiver_ contains _anObject_, NO if it doesn't. NSObject's implementation of this method returns YES only if _receiver_ is a kind of NSArray and contains _anObject_. In all other cases it returns NO. This method is used in the Framework only by EOQualifier for in-memory evaluation.

---

#### isCaseInsensitiveLike

public boolean __isCaseInsensitiveLike__ (java.lang.Object _receiver_, java.lang.Object _anObject_)

Returns YES if _receiver_ is a case-insensitive match for _aStrin__g_, NO if it isn't. See "Using Wildcards" in the EOQualifier class specification for the wildcard characters allowed. NSObject's implementation returns NO; NSString's performs a proper case-insensitive comparison. This method is used in the Framework only by EOQualifier for in-memory evaluation.

__See also:__
[__isLike__](#apple-gqzdqoa), [__doesContain__](#apple-gqzdmma), [__isEqualTo__](#apple-gqzdmoa), [__isGreaterThan__](#apple-gqzdomq), [__isGreaterThanOrEqualTo__](#apple-gqzdonq), [__isLessThan__](#apple-gqzdqma),
[__isLessThanOrEqualTo__](#apple-gqzdqna),[__isNotEqualTo__](#apple-gqzdsmq)

---

#### isEqualTo

public boolean __isEqualTo__ (java.lang.Object _receiver_, java.lang.Object _anObject_)

Invokes __isEqual:__  and returns the result. This method is used in the Framework only by EOQualifier for in-memory evaluation.

__See also:__
[__doesContain__](#apple-gqzdmma), [__isGreaterThan__](#apple-gqzdomq), [__isGreaterThanOrEqualTo__](#apple-gqzdonq), [__isLessThan__](#apple-gqzdqma),
[__isLessThanOrEqualTo__](#apple-gqzdqna), [__isLike__](#apple-gqzdqoa), [__isCaseInsensitiveLike__](#apple-gqzdmna), [__isNotEqualTo__](#apple-gqzdsmq)

---

#### isGreaterThan

public boolean __isGreaterThan__ (java.lang.Object _receiver_, java.lang.Object _anObject_)

Invokes __compare:__  and returns YES if the result is NSOrderedDescending. This method is used in the Framework only by EOQualifier for in-memory evaluation.

__See also:__
[__doesContain__](#apple-gqzdmma), [__isEqualTo__](#apple-gqzdmoa), [__isGreaterThanOrEqualTo__](#apple-gqzdonq), [__isLessThan__](#apple-gqzdqma), [__isLessThanOrEqualTo__](#apple-gqzdqna),
[__isLike__](#apple-gqzdqoa), [__isCaseInsensitiveLike__](#apple-gqzdmna), [__isNotEqualTo__](#apple-gqzdsmq)

---

#### isGreaterThanOrEqualTo

public boolean __isGreaterThanOrEqualTo__ (java.lang.Object _receiver_, java.lang.Object _anObject_)

Invokes __compare:__  and returns YES if the result is NSOrderedDescending or NSOrderedSame. This method is used in the Framework only by EOQualifier for in-memory evaluation.

__See also:__
[__doesContain__](#apple-gqzdmma), [__isEqualTo__](#apple-gqzdmoa), [__isGreaterThan__](#apple-gqzdomq), [__isLessThan__](#apple-gqzdqma), [__isLessThanOrEqualTo__](#apple-gqzdqna), [__isLike__](#apple-gqzdqoa),
[__isCaseInsensitiveLike__](#apple-gqzdmna), [__isNotEqualTo__](#apple-gqzdsmq)

---

#### isLessThan

public boolean __isLessThan__ (java.lang.Object _receiver_, java.lang.Object _anObject_)

Invokes `compare:` and returns YES if the result is NSOrderedAscending. This method is used in the Framework only by EOQualifier for in-memory evaluation.

__See also:__
[__doesContain__](#apple-gqzdmma), [__isEqualTo__](#apple-gqzdmoa), [__isGreaterThan__](#apple-gqzdomq), [__isGreaterThanOrEqualTo__](#apple-gqzdonq), [__isLessThanOrEqualTo__](#apple-gqzdqna),
[__isLike__](#apple-gqzdqoa), [__isCaseInsensitiveLike__](#apple-gqzdmna), [__isNotEqualTo__](#apple-gqzdsmq)

---

#### isLessThanOrEqualTo

public boolean __isLessThanOrEqualTo__ (java.lang.Object _receiver_, java.lang.Object _anObject_)

Invokes `compare:` and returns YES if the result is NSOrderedAscending or NSOrderedSame. This method is used in the Framework only by EOQualifier for in-memory evaluation.

__See also:__
[__doesContain__](#apple-gqzdmma), [__isEqualTo__](#apple-gqzdmoa), [__isGreaterThan__](#apple-gqzdomq), [__isGreaterThanOrEqualTo__](#apple-gqzdonq), [__isLessThan__](#apple-gqzdqma), [__isLike__](#apple-gqzdqoa),
[__isCaseInsensitiveLike__](#apple-gqzdmna), [__isNotEqualTo__](#apple-gqzdsmq)

---

#### isLike

public boolean __isLike__ (java.lang.Object _receiver_, java.lang.Object _anObject_)

Returns YES if _receiver_ matches _aString_ according to the semantics of the SQL __like__  comparison operator, NO if it doesn't. See "Using Wildcards" in the EOQualifier class specification for the wildcard characters allowed. NSObject's implementation returns NO; NSString's performs a proper comparison. This method is used in the Framework only by EOQualifier for in-memory evaluation.

__See also:__
[__isCaseInsensitiveLike__](#apple-gqzdmna), [__doesContain__](#apple-gqzdmma), [__isEqualTo__](#apple-gqzdmoa), [__isGreaterThan__](#apple-gqzdomq), [__isGreaterThanOrEqualTo__](#apple-gqzdonq),
[__isLessThan__](#apple-gqzdqma), [__isLessThanOrEqualTo__](#apple-gqzdqna), [__isNotEqualTo__](#apple-gqzdsmq)

---

#### isNotEqualTo

public boolean __isNotEqualTo__ (java.lang.Object _receiver_, java.lang.Object _anObject_)

Invokes __isEqual:__ , inverts the result, and returns it. This method is used in the Framework only by EOQualifier for in-memory evaluation.

__See also:__
[__doesContain__](#apple-gqzdmma), [__isEqualTo__](#apple-gqzdmoa), [__isGreaterThan__](#apple-gqzdomq), [__isGreaterThanOrEqualTo__](#apple-gqzdonq), [__isLessThan__](#apple-gqzdqma),
[__isLessThanOrEqualTo__](#apple-gqzdqna), [__isLike__](#apple-gqzdqoa), [__isCaseInsensitiveLike__](#apple-gqzdmna)

---

[!](EOQualifier-2.md)
[!](EOSortOrdering.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
