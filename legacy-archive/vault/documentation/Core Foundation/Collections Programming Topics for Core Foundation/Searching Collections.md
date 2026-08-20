---
title: Collections Programming Topics for Core Foundation
apple_id: 10000124i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2011-01-18'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/Articles/searching.html
archived_at: '2026-07-15T07:22:15.641980Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Collections Programming Topics for Core Foundation](Introduction.md)


[Next](Working%20With%20Mutable%20Collections.md)[Previous](Getting%20the%20Values%20of%20Collections.md)

# Searching Collections

Core Foundation includes several programming interfaces for
finding values (and, in the case of CFDictionary, keys) in collection
objects. The `CF`_Type_`GetValueIfPresent` functions, described
in [Getting the Values of Collections](Getting%20the%20Values%20of%20Collections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeztglkdjjbekscbifdq), report on the existence
of values in dictionaries, sets, and bags. You can also use functions
with “Contains” in their names to determine whether a collection
holds a value or key. [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeztiljrgaydsojrfvbuqrceivceurq) illustrates how the `CFDictionaryContainsKey` function
might be used.

__Listing 1__  Searching
a CFDictionary object for a key

```
if (CFDictionaryContainsKey(mappingTable, (const void*)lowerCharsetName)) {
    result = (CFStringEncoding)CFDictionaryGetValue(mappingTable, (const void*)lowerCharsetName);
}
```

For CFArray objects, the `CFArrayBSearchValues` function
offers a more sophisticated search option. This function searches
for a specified value in a sorted array using a binary search algorithm.
If the value doesn’t exist in the collection, the function tells
you where it should go; the `CFArrayBSearchValues` function
thus helps you to keep a sorted mutable array sorted. [Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeztiljrgaytamzwfvbuqrcdjjfecsq) shows
how this function might be called.

__Listing 2__  Searching
for a value in a CFArray object

```
CFIndex position = CFArrayBSearchValues(aMutArray, CFRangeMake(0,CFArrayGetCount(anArray)), (const void *)CFSTR("String Three"), CFStringCompare, 0);
```

The fourth parameter of the `CFArrayBSearchValues` function
must be a pointer to a function that conforms to the `CFComparatorFunction` type.
This comparator function is supposed to know how to compare values
in the array. In the given example `CFStringCompare` is
used because it conforms to `CFComparatorFunction` and
it knows how to compare CFString values. There are other predefined
Core Foundation comparator functions that you can use, such as `CFNumberCompare` and `CFDateCompare`.

Upon return of the above call, the function’s `CFIndex` result
can indicate one of the following:

- If the value exists, its index in the array
- An index greater than or equal to the end point of the range
  if the specified value is greater than all the values in the rangeThe
  index of the value greater than the specified value if the value
  lies between two of (or less than all of) the values in the range.

You can use the `CFArrayContainsValue` to
determine whether the result is the first of the listed alternatives.

The CFTree type defines a different group of functions for
locating contained values (that is, subtrees). See [Creating and Copying Collections](Creating%20and%20Copying%20Collections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeztelkdjjbekscbifdq) for
more information.

[Next](Working%20With%20Mutable%20Collections.md)[Previous](Getting%20the%20Values%20of%20Collections.md)

