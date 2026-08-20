---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOSortOrderingComprsnSppt.html
archived_at: '2026-07-18T01:28:27.459377Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOSortOrdering.md)
[!](EOTemporaryGlobalID.md)

---

# EOSortOrdering.ComparisonSupport

__Inherits From:__
java.lang.Object

__Package:__
com.apple.client.eocontrol (Siva)

## Class Description

Siva's class EOSortOrdering.ComparisonSupport provides default implementations of the EOSortOrderingComparison interface. It is for use in client-side enterprise object classes only; there is no equivalent Yellow Box class for server-side enterprise objects.

Siva's EOCustomObject uses EOSortOrdering.ComparisonSupport's default implementations. Typically your custom enterprise object classes inherit from EOCustomObject and inherit the default implementations. If your custom enterprise object class doesn't inherit from EOCustomObject, you should implement the EOSortOrderingComparison interface directly.

## Method Types

**Setting up automatic support**

**[setSupportForClass](#apple-gq3demy)

**[supportForClass](#apple-gq3deny)****

**Comparing two objects**

**[compareValues](#apple-gq3dcoi)**

**EOSortOrderingComparison methods**

**[compareAscending](#apple-gq3dgnq)

**[compareCaseInsensitiveAscending](#apple-gq3dima)

**[compareCaseInsensitiveDescending](#apple-gq3dina)

**[compareDescending](#apple-gq3dioa)********

## Static Methods

---

#### compareValues

public static int __compareValues__ (java.lang.Object _anObject_, java.lang.Object _anotherObject_, com.apple.client.foundation.NSSelector _selector_)

Compares the two objects using _selector_. You should use this method to compare value objects instead of calling _selector_ directly. This method is the entry point for the comparison support, and calls methods in support classes if appropriate.

__See also:__
[__setSupportForClass__](#apple-gq3demy), [__supportForClass__](#apple-gq3deny)

---

#### setSupportForClass

public static void __setSupportForClass__ (EOSortOrdering. ComparisonSupport _supportClass_, java.lang.Class _aClass_)

Sets _supportClass_ as the support class to be used for comparing instances of _aClass_. When [__compareValues__](#apple-gq3dcoi) is called, the methods in _supportClass_ will be used to do the comparison for instances of _aClass_.

__See also:__
[__compareValues__](#apple-gq3dcoi)

---

#### supportForClass

public static EOSortOrdering. ComparisonSupport __supportForClass__ (java.lang.Class _aClass_)

Returns the support class used for doing sort ordering comparisons for instances of _aClass_.

__See also:__
[__compareValues__](#apple-gq3dcoi), [__setSupportForClass__](#apple-gq3demy)

## Instance Methods

---

#### compareAscending

public int __compareAscending__ (java.lang.Object _receiver_, java.lang.Object _anObject_)

Returns NSOrderedAscending if _anObject_ is naturally ordered after _receiver_, NSOrderedDescending if it's naturally ordered before _receiver_, and NSOrderedSame if they're equivalent for ordering purposes. NSObject's implementation of this method simply invokes __compare:__ .

__See also:__
[__compareDescending__](#apple-gq3dioa), [__compareCaseInsensitiveAscending__](#apple-gq3dima),
[__compareCaseInsensitiveDescending__](#apple-gq3dina)

---

#### compareCaseInsensitiveAscending

public int __compareCaseInsensitiveAscending__ (java.lang.Object _receiver_, java.lang.Object _anObject_)

Returns NSOrderedAscending if _anObject_ is naturally ordered-ignoring case-after _receiver_, NSOrderedDescending if it's naturally ordered before _receiver_, and NSOrderedSame if they're equivalent for ordering purposes. NSObject's implementation of this method invokes __compare:__ , while NSString's invokes __caseInsensitiveCompare:__ .

__See also:__
[__compareCaseInsensitiveDescending__](#apple-gq3dina), [__compareAscending__](#apple-gq3dgnq), [__compareDescending__](#apple-gq3dioa)

---

#### compareCaseInsensitiveDescending

public int __compareCaseInsensitiveDescending__ (java.lang.Object _receiver_, java.lang.Object _anObject_)

Returns NSOrderedAscending if _anObject_ is naturally ordered-ignoring case-before _receiver_, NSOrderedDescending if it's naturally ordered after _receiver_, and NSOrderedSame if they're equivalent for ordering purposes. NSObject's implementation of this method invokes __compare:__  and inverts the result, while NSString's invokes __caseInsensitiveCompare:__  and inverts the result.

__See also:__
[__compareCaseInsensitiveDescending__](#apple-gq3dina), [__compareDescending__](#apple-gq3dioa), [__compareAscending__](#apple-gq3dgnq)

---

#### compareDescending

public int __compareDescending__ (java.lang.Object _anObject_, java.lang.Object _anObject_)

Returns NSOrderedAscending if _anObject_ is naturally ordered before _receiver_, NSOrderedDescending if it's naturally ordered after _receiver_, and NSOrderedSame if they're equivalent for ordering purposes. NSObject's implementation of this method simply invokes __compare:__  and inverts the result.

__See also:__
[__compareAscending__](#apple-gq3dgnq), [__compareCaseInsensitiveDescending__](#apple-gq3dina), [__compareCaseInsensitiveAscending__](#apple-gq3dima)

---

[!](EOSortOrdering.md)
[!](EOTemporaryGlobalID.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
