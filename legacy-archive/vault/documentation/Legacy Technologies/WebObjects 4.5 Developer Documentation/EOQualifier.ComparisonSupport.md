---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOQualifierComparisonSup.html
archived_at: '2026-07-15T08:11:37.918915Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOQualifier.ComparisonSupport

> **__Inherits
> from:__**
> : Object

> **__Package:__**
> : com.apple.client.eocontrol

---

## Class Description

---

The com.apple.client.eocontrol EOQualifier.ComparisonSupport
class provides default implementations of the EOQualifierComparison
interface.

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.yellow.eocontrol package. |

The com.apple.client.eocontrol EOCustomObject uses EOQualifier.ComparisonSupport's
default implementations. Typically your custom enterprise object
classes inherit from EOCustomObject and inherit the default implementations.
If your custom enterprise object class doesn't inherit from EOCustomObject,
you should implement the EOQualifierComparison interface directly.

## Method Types

---

> **Setting up automatic
> support**
> : [setSupportForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzc4q3pnvygc4tjonxw4u3vobyg64tuf5zwk5ctovyha33sordg64sdnrqxg4y)
> : [supportForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzc4q3pnvygc4tjonxw4u3vobyg64tuf5zxk4dqn5zhirtpojbwyyltom)
>
> **Comparing two objects**
> : [compareValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzc4q3pnvygc4tjonxw4u3vobyg64tuf5rw63lqmfzgkvtbnr2wk4y)
>
> **EOQualifierComparison
> methods**
> : [doesContain](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33okn2xa4dpoj2c6zdpmvzug33oorqws3q)
> : [isCaseInsensitiveLike](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33okn2xa4dpoj2c62ltinqxgzkjnzzwk3ttnf2gs5tfjruwwzi)
> : [isEqualTo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33okn2xa4dpoj2c62ltivyxkylmkrxq)
> : [isGreaterThan](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33okn2xa4dpoj2c62lti5zgkylumvzfi2dbny)
> : [isGreaterThanOrEqualTo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33okn2xa4dpoj2c62lti5zgkylumvzfi2dbnzhxerlrovqwyvdp)
> : [isLessThan](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33okn2xa4dpoj2c62ltjrsxg42unbqw4)
> : [isLessThanOrEqualTo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33okn2xa4dpoj2c62ltjrsxg42unbqw4t3sivyxkylmkrxq)
> : [isLike](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33okn2xa4dpoj2c62ltjruwwzi)
> : [isNotEqualTo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4roinxw24dbojuxg33okn2xa4dpoj2c62ltjzxxirlrovqwyvdp)

## Static Methods

---

### compareValues

`public static int compareValues(
Object anObject,
Object anotherObject,
NSSelector selector)`

Compares the two objects using _selector._
You should use this method to compare value objects instead of calling _selector_ directly.
This method is the entry point for the comparison support, and calls methods
in support classes if appropriate.

---

### setSupportForClass

`public static void setSupportForClass(
EOSortOrdering.ComparisonSupport supportClass,
Class aClass)`

Sets _supportClass_ as
the support class to be used for comparing instances of _aClass._
When [compareValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzc4q3pnvygc4tjonxw4u3vobyg64tuf5rw63lqmfzgkvtbnr2wk4y) is
called, the methods in _supportClass_ are
used to do the comparison for instances of _aClass._

---

### supportForClass

`public static EOSortOrdering.ComparisonSupport supportForClass(Class aClass)`

Returns the support class used for doing sort
ordering comparisons for instances of _aClass._

---

## Instance Methods

---

### doesContain

`public boolean doesContain(
Object receiver,
Object anObject)`

Returns `true` if _receiver_ contains _anObject,_ `false` if
it doesn't. NSObject's implementation of this method returns `true` only
if _receiver_ is a kind of NSArray
and contains _anObject._ In all other
cases it returns `false`.
This method is used in the Framework only by EOQualifier for in-memory
evaluation.

---

### isCaseInsensitiveLike

`public boolean isCaseInsensitiveLike(
Object receiver,
Object anObject)`

Returns `true` if _receiver_ is
a case-insensitive match for _anObject,_ `false` if
it isn't. See ["Using Wildcards and the like Operator"](EOQualifier-2.md#apple-ijbesqsjijaue) for the wildcard characters allowed. This method
is used in the Framework only by EOQualifier for in-memory evaluation.

---

### isEqualTo

`public boolean isEqualTo(
Object receiver,
Object anObject)`

Invokes `equals` and
returns the result. This method is used in the Framework only by
EOQualifier for in-memory evaluation.

---

### isGreaterThan

`public boolean isGreaterThan(
Object receiver,
Object anObject)`

Invokes `compare` and
returns `true` if the result
is `NSComparitor.OrderedDescending`.
This method is used in the Framework only by EOQualifier for in-memory
evaluation.

---

### isGreaterThanOrEqualTo

`public boolean isGreaterThanOrEqualTo(
Object receiver,
Object anObject)`

Invokes `compare` and
returns `true` if the result
is `NSComparitor.OrderedDescending` or `NSComparitor.OrderedSame`.
This method is used in the Framework only by EOQualifier for in-memory
evaluation.

---

### isLessThan

`public boolean isLessThan(
Object receiver,
Object anObject)`

Invokes `compare` and
returns `true` if the result
is `NSComparator.OrderedAscending`.
This method is used in the Framework only by EOQualifier for in-memory
evaluation.

---

### isLessThanOrEqualTo

`public boolean isLessThanOrEqualTo(
Object receiver,
Object anObject)`

Invokes `compare` and
returns `true` if the result
is `NSComparator.OrderedAscending` or `NSComparator.OrderedSame`.
This method is used in the Framework only by EOQualifier for in-memory evaluation.

---

### isLike

`public boolean isLike(
Object receiver,
Object anObject)`

Returns `true` if _receiver_ matches _anObject_ according
to the semantics of the SQL `like` comparison operator, `false` if
it doesn't. See ["Using Wildcards and the like Operator"](EOQualifier-2.md#apple-ijbesqsjijaue) for the wildcard characters allowed. This method
is used in the Framework only by EOQualifier for in-memory evaluation.

---

### isNotEqualTo

`public boolean isNotEqualTo(
Object receiver,
Object anObject)`

Invokes `equals`, inverts
the result, and returns it. This method is used in the Framework
only by EOQualifier for in-memory evaluation.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
