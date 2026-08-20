---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOQualifierComparisonSupp.html
archived_at: '2026-07-15T08:13:47.297952Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOQualifier.ComparisonSupport

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

The Java Client EOQualifier.ComparisonSupport class provides default implementations of the EOQualifierComparison interface.

The Java Client EOCustomObject uses EOQualifier.ComparisonSupport's default implementations. Typically your custom enterprise object classes inherit from EOCustomObject and inherit the default implementations. If your custom enterprise object class doesn't inherit from EOCustomObject, you should implement the EOQualifierComparison interface directly.

## Method Types

---

> **Setting up automatic support**
> : [setSupportForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzc4q3pnvygc4tjonxw4u3vobyg64tuf5zwk5ctovyha33sordg64sdnrqxg4y): [supportForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzc4q3pnvygc4tjonxw4u3vobyg64tuf5zxk4dqn5zhirtpojbwyyltom)
>
> **Comparing two objects**
> : [compareValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzc4q3pnvygc4tjonxw4u3vobyg64tuf5rw63lqmfzgkvtbnr2wk4y)
>
> **EOQualifierComparison methods**
> : [doesContain](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33okn2xa4dpoj2c6zdpmvzug33oorqws3q): [isCaseInsensitiveLike](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33okn2xa4dpoj2c62ltinqxgzkjnzzwk3ttnf2gs5tfjruwwzi): [isEqualTo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33okn2xa4dpoj2c62ltivyxkylmkrxq): [isGreaterThan](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33okn2xa4dpoj2c62lti5zgkylumvzfi2dbny): [isGreaterThanOrEqualTo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33okn2xa4dpoj2c62lti5zgkylumvzfi2dbnzhxerlrovqwyvdp): [isLessThan](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33okn2xa4dpoj2c62ltjrsxg42unbqw4): [isLessThanOrEqualTo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33okn2xa4dpoj2c62ltjrsxg42unbqw4t3sivyxkylmkrxq): [isLike](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33okn2xa4dpoj2c62ltjruwwzi): [isNotEqualTo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33okn2xa4dpoj2c62ltjzxxirlrovqwyvdp)

## Static Methods

---

### compareValues

`public static int compareValues( Object anObject, Object anotherObject, NSSelector selector)`

Compares the two objects using _selector_. You should use this method to compare value objects instead of calling _selector_ directly. This method is the entry point for the comparison support, and calls methods in support classes if appropriate.

---

### setSupportForClass

`public static void setSupportForClass( EOSortOrdering.ComparisonSupport supportClass, Class aClass)`

Sets _supportClass_ as the support class to be used for comparing instances of _aClass_. When [compareValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzc4q3pnvygc4tjonxw4u3vobyg64tuf5rw63lqmfzgkvtbnr2wk4y) is called, the methods in _supportClass_ are used to do the comparison for instances of _aClass_.

---

### supportForClass

`public static EOSortOrdering.ComparisonSupport supportForClass(Class aClass)`

Returns the support class used for doing sort ordering comparisons for instances of _aClass_.

---

## Instance Methods

---

### doesContain

`public boolean doesContain( Object receiver, Object anObject)`

Returns `true` if _receiver_ contains _anObject_, `false` if it doesn't. NSObject's implementation of this method returns `true` only if _receiver_ is a kind of NSArray and contains _anObject_. In all other cases it returns `false`. This method is used in the Framework only by EOQualifier for in-memory evaluation.

---

### isCaseInsensitiveLike

`public boolean isCaseInsensitiveLike( Object receiver, Object anObject)`

Returns `true` if _receiver_ is a case-insensitive match for _anObject_, `false` if it isn't. See "Using Wildcards and the like Operator" (page 99) for the wildcard characters allowed. This method is used in the Framework only by EOQualifier for in-memory evaluation.

---

### isEqualTo

`public boolean isEqualTo( Object receiver, Object anObject)`

Invokes __equals__ and returns the result. This method is used in the Framework only by EOQualifier for in-memory evaluation.

---

### isGreaterThan

`public boolean isGreaterThan( Object receiver, Object anObject)`

Invokes __compare__ and returns `true` if the result is `NSComparitor.OrderedDescending`. This method is used in the Framework only by EOQualifier for in-memory evaluation.

---

### isGreaterThanOrEqualTo

`public boolean isGreaterThanOrEqualTo( Object receiver, Object anObject)`

Invokes __compare__ and returns `true` if the result is `NSComparitor.OrderedDescending` or `NSComparitor.OrderedSame`. This method is used in the Framework only by EOQualifier for in-memory evaluation.

---

### isLessThan

`public boolean isLessThan( Object receiver, Object anObject)`

Invokes __compare__ and returns `true` if the result is `NSComparator.OrderedAscending`. This method is used in the Framework only by EOQualifier for in-memory evaluation.

---

### isLessThanOrEqualTo

`public boolean isLessThanOrEqualTo( Object receiver, Object anObject)`

Invokes __compare__ and returns `true` if the result is `NSComparator.OrderedAscending` or `NSComparator.OrderedSame`. This method is used in the Framework only by EOQualifier for in-memory evaluation.

---

### isLike

`public boolean isLike( Object receiver, Object anObject)`

Returns `true` if _receiver_ matches _anObject_ according to the semantics of the SQL __like__ comparison operator, `false` if it doesn't. See "Using Wildcards and the like Operator" (page 99) for the wildcard characters allowed. This method is used in the Framework only by EOQualifier for in-memory evaluation.

---

### isNotEqualTo

`public boolean isNotEqualTo( Object receiver, Object anObject)`

Invokes __equals__, inverts the result, and returns it. This method is used in the Framework only by EOQualifier for in-memory evaluation.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
