---
title: Collections Programming Topics for Core Foundation
apple_id: 10000124i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2011-01-18'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/Articles/mutable.html
archived_at: '2026-07-15T07:22:15.143404Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Collections Programming Topics for Core Foundation](Introduction.md)


[Next](Applying%20Program-Defined%20Functions%20to%20Collections.md)[Previous](Searching%20Collections.md)

# Working With Mutable Collections

The collection opaque types CFArray, CFDictionary, CFSet,
and CFBag offer similar sets of functions for manipulating the values
contained by mutable collections: adding values, removing values,
replacing values, and so on. There are some differences in behavior based
on whether the collection ensures the uniqueness of keys and values. Table 1 summaries
the behavior of the mutability functions. The Operation column identifies
the type of operation using the parameter found in a mutability
function, such as “Replace” in `CFDictionaryReplaceValue`.

__Table 1__  Semantics of mutable collection operations

| Operation | Collection Type | What it Means |
| Append | CFArray | Insert the value after all other values (index=count). |
| Insert | CFArray | Insert the value at the given index of the collection. |
| Add | all except CFArray | For CFDictionary and CFSet, add value if it is absent, do nothing if it is present. For CFBag, add value even if it is already present. |
| Replace | all | If the specified value is present, replace it with another value; otherwise, do nothing. |
| Set | all | Add the value if it is absent, replace it if it is present. |
| Remove | all | Remove the value if it is present, do nothing if it is absent. |

With fixed-size mutable collections, you must take care to
avoid adding beyond the capacity limit. A fixed-size collection
will let you add as many values as you want, but gives no notice
when you exceed the capacity. However, doing so will result in undefined behavior
that is most likely undesirable.

The CFArray type features one mutability operation that is
special to it. With the `CFArraySortValues` function
you can sort the values contained by the array. A comparator function,
which must conform to the `CFComparatorFunction` type,
is used to compare values. Listing 1 gives an example
of the use of the `CFArraySortValues` function.

__Listing 1__  Sorting
an array

```
CFMutableArrayRef createSortedArray(CFArrayRef anArray) {
    CFIndex count = CFArrayGetCount(anArray);
    CFMutableArrayRef marray = CFArrayCreateMutableCopy(NULL, count, anArray);
    CFArraySortValues(marray, CFRangeMake(0, count), (CFComparatorFunction)CFStringCompare, NULL);
    return marray;
}
```

Notice that the `CFStringCompare` function
is used, in this case, to compare CFString objects. Core Foundation
provides other comparator functions that are of the `CFComparatorFunction` type,
notably `CFDateCompare` and `CFNumberCompare`.
When an array holds Core Foundation objects, you can pass in an
appropriate predefined comparator function to the `CFArraySortValues` function
to sort those objects.

[Next](Applying%20Program-Defined%20Functions%20to%20Collections.md)[Previous](Searching%20Collections.md)

