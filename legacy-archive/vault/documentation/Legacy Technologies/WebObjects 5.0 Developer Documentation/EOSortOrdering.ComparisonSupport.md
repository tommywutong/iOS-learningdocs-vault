---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOSortOrderingComparisonS.html
archived_at: '2026-07-15T08:13:47.405169Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOSortOrdering.ComparisonSupport

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

The Java Client EOSortOrdering.ComparisonSupport class provides default implementations of the EOSortOrderingComparison interface.

The Java Client EOCustomObject uses EOSortOrdering.ComparisonSupport's default implementations. Typically your custom enterprise object classes inherit from EOCustomObject and inherit the default implementations. If your custom enterprise object class doesn't inherit from EOCustomObject, you should implement the EOSortOrderingComparison interface directly.

## Method Types

---

> **Setting up automatic support**
> : [setSupportForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3poj2e64temvzgs3thfzbw63lqmfzgs43pnzjxk4dqn5zhil3tmv2fg5lqobxxe5cgn5zeg3dbonzq): [supportForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3poj2e64temvzgs3thfzbw63lqmfzgs43pnzjxk4dqn5zhil3tovyha33sordg64sdnrqxg4y)
>
> **Comparing two objects**
> : [compareValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3poj2e64temvzgs3thfzbw63lqmfzgs43pnzjxk4dqn5zhil3dn5wxaylsmvlgc3dvmvzq)
>
> **EOSortOrderingComparison methods**
> : [compareAscending](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts4q3pnvygc4tjonxw4u3vobyg64tuf5rw63lqmfzgkqltmnsw4zdjnztq): [compareCaseInsensitiveAscending](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts4q3pnvygc4tjonxw4u3vobyg64tuf5rw63lqmfzgkq3bonsus3ttmvxhg2lunf3gkqltmnsw4zdjnztq): [compareCaseInsensitiveDescending](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts4q3pnvygc4tjonxw4u3vobyg64tuf5rw63lqmfzgkq3bonsus3ttmvxhg2lunf3gkrdfonrwk3tenfxgo): [compareDescending](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknxxe5cpojsgk4tjnzts4q3pnvygc4tjonxw4u3vobyg64tuf5rw63lqmfzgkrdfonrwk3tenfxgo)

## Static Methods

---

### compareValues

`public static int compareValues( Object anObject, Object anotherObject, NSSelector selector)`

Compares the two objects using _selector_. You should use this method to compare value objects instead of calling _selector_ directly. This method is the entry point for the comparison support, and calls methods in support classes if appropriate.

---

### setSupportForClass

`public static void setSupportForClass( EOSortOrdering.ComparisonSupport supportClass, Class aClass)`

Sets _supportClass_ as the support class to be used for comparing instances of _aClass_. When [compareValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3poj2e64temvzgs3thfzbw63lqmfzgs43pnzjxk4dqn5zhil3dn5wxaylsmvlgc3dvmvzq) is called, the methods in _supportClass_ will be used to do the comparison for instances of _aClass_.

---

### supportForClass

`public static EOSortOrdering.ComparisonSupport supportForClass(Class aClass)`

Returns the support class used for doing sort ordering comparisons for instances of _aClass_.

---

## Instance Methods

---

### compareAscending

`public int compareAscending( Object receiver, Object anObject)`

Returns `NSComparator.OrderedAscending` if _anObject_ is naturally ordered after _receiver_, `NSComparator.OrderedDescending` if it's naturally ordered before _receiver_, and `NSComparator.OrderedSame` if they're equivalent for ordering purposes.

---

### compareCaseInsensitiveAscending

`public int compareCaseInsensitiveAscending( Object receiver, Object anObject)`

Returns `NSComparator.OrderedAscending` if _anObject_ is naturally ordered-ignoring case-after _receiver_, `NSComparator.OrderedDescending` if it's naturally ordered before _receiver_, and `NSComparator.OrderedSame` if they're equivalent for ordering purposes.

---

### compareCaseInsensitiveDescending

`public int compareCaseInsensitiveDescending( Object receiver, Object anObject)`

Returns `NSComparator.OrderedAscending` if _anObject_ is naturally ordered-ignoring case-before _receiver_, `NSComparator.OrderedDescending` if it's naturally ordered after _receiver_, and `NSComparator.OrderedSame` if they're equivalent for ordering purposes.

---

### compareDescending

`public int compareDescending( Object anObject, Object anObject)`

Returns `NSComparator.OrderedAscending` if _anObject_ is naturally ordered before _receiver_, `NSComparator.OrderedDescending` if it's naturally ordered after _receiver_, and `NSComparator.OrderedSame` if they're equivalent for ordering purposes.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
