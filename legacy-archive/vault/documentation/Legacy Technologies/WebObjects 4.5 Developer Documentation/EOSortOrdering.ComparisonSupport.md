---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOSortOrderingComparisonS.html
archived_at: '2026-07-15T08:11:37.989321Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOSortOrdering.ComparisonSupport

> **__Inherits
> from:__**
> : Object

> **__Package:__**
> : com.apple.client.eocontrol

---

## Class Description

---

The com.apple.client.eocontrol EOSortOrdering.ComparisonSupport
class provides default implementations of the [EOSortOrderingComparison](EOSortOrderingComparison.md#apple-mnxw24dbojsuizltmnsw4zdjnztv6) interface.

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.yellow.eocontrol package. |

The com.apple.client.eocontrol EOCustomObject uses EOSortOrdering.ComparisonSupport's
default implementations. Typically your custom enterprise object
classes inherit from EOCustomObject and inherit the default implementations.
If your custom enterprise object class doesn't inherit from EOCustomObject,
you should implement the [EOSortOrderingComparison](EOSortOrderingComparison.md#apple-mnxw24dbojsuizltmnsw4zdjnztv6) interface
directly.

## Method Types

---

> **Setting up automatic
> support**
> : [setSupportForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3poj2e64temvzgs3thfzbw63lqmfzgs43pnzjxk4dqn5zhil3tmv2fg5lqobxxe5cgn5zeg3dbonzq)
> : [supportForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3poj2e64temvzgs3thfzbw63lqmfzgs43pnzjxk4dqn5zhil3tovyha33sordg64sdnrqxg4y)
>
> **Comparing two objects**
> : [compareValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3poj2e64temvzgs3thfzbw63lqmfzgs43pnzjxk4dqn5zhil3dn5wxaylsmvlgc3dvmvzq)
>
> **EOSortOrderingComparison methods**
> : [compareAscending](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts4q3pnvygc4tjonxw4u3vobyg64tuf5rw63lqmfzgkqltmnsw4zdjnztq)
> : [compareCaseInsensitiveAscending](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts4q3pnvygc4tjonxw4u3vobyg64tuf5rw63lqmfzgkq3bonsus3ttmvxhg2lunf3gkqltmnsw4zdjnztq)
> : [compareCaseInsensitiveDescending](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts4q3pnvygc4tjonxw4u3vobyg64tuf5rw63lqmfzgkq3bonsus3ttmvxhg2lunf3gkrdfonrwk3tenfxgo)
> : [compareDescending](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts4q3pnvygc4tjonxw4u3vobyg64tuf5rw63lqmfzgkrdfonrwk3tenfxgo)

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
When [compareValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3poj2e64temvzgs3thfzbw63lqmfzgs43pnzjxk4dqn5zhil3dn5wxaylsmvlgc3dvmvzq) is
called, the methods in _supportClass_ will
be used to do the comparison for instances of _aClass._

---

### supportForClass

`public static EOSortOrdering.ComparisonSupport supportForClass(Class aClass)`

Returns the support class used for doing sort
ordering comparisons for instances of _aClass._

---

## Instance Methods

---

### compareAscending

`public int compareAscending(
Object receiver,
Object anObject)`

Returns `NSComparator.OrderedAscending` if _anObject_ is
naturally ordered after _receiver,_ `NSComparator.OrderedDescending` if
it's naturally ordered before _receiver,_
and `NSComparator.OrderedSame` if
they're equivalent for ordering purposes.

---

### compareCaseInsensitiveAscending

`public int compareCaseInsensitiveAscending(
Object receiver,
Object anObject)`

Returns `NSComparator.OrderedAscending` if _anObject_ is
naturally ordered-ignoring case-after _receiver,_ `NSComparator.OrderedDescending` if
it's naturally ordered before _receiver,_
and `NSComparator.OrderedSame` if
they're equivalent for ordering purposes.

---

### compareCaseInsensitiveDescending

`public int compareCaseInsensitiveDescending(
Object receiver,
Object anObject)`

Returns `NSComparator.OrderedAscending` if _anObject_ is
naturally ordered-ignoring case-before _receiver,_ `NSComparator.OrderedDescending` if
it's naturally ordered after _receiver,_
and `NSComparator.OrderedSame` if
they're equivalent for ordering purposes.

---

### compareDescending

`public int compareDescending(
Object anObject,
Object anObject)`

Returns `NSComparator.OrderedAscending` if _anObject_ is
naturally ordered before _receiver,_ `NSComparator.OrderedDescending` if
it's naturally ordered after _receiver,_
and `NSComparator.OrderedSame` if
they're equivalent for ordering purposes.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
