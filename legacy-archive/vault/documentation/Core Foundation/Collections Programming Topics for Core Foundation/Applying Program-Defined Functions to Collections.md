---
title: Collections Programming Topics for Core Foundation
apple_id: 10000124i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2011-01-18'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/Articles/applying.html
archived_at: '2026-07-15T07:22:12.639847Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Collections Programming Topics for Core Foundation](Introduction.md)


[Next](Creating%20and%20Using%20Tree%20Structures.md)[Previous](Working%20With%20Mutable%20Collections.md)

# Applying Program-Defined Functions to Collections

A particularly useful feature of collections is the capability
for applying a program-defined function to each value in a collection
object. This applier function must conform to a prototype defined
for each collection type. You must specify a pointer to this function
in the collection functions (of the form `CF`_Type_`ApplyFunction`)
that invokes it on each contained value.

[Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeztmljrgaydsojsfvbuqrcdindesqq) provides a simple example that applies a character-counting
function to the CFString objects stored in a CFArray object. This
function is of the type `CFArrayApplierFunction`.
This prototype has two parameters: the first is a value in the array (or
a pointer to that value) and the second is some program-defined
value (or a pointer to that value).

__Listing 1__  Applying
a function to an array

```
void countCharacters(const void *val, void *context) {
    CFStringRef str = (CFStringRef)val;
    CFIndex *cnt = (CFIndex *)context;
    CFIndex numchars = CFStringGetLength(str);
    *cnt += numchars;
}

void countCharsInArray() {
    CFStringRef strs[3];
    CFArrayRef anArray;
    CFIndex count=0;

    strs[0] = CFSTR("String One");
    strs[1] = CFSTR("String Two");
    strs[2] = CFSTR("String Three");

    anArray = CFArrayCreate(NULL, (void *)strs, 3, &kCFTypeArrayCallBacks);
    CFArrayApplyFunction(anArray, CFRangeMake(0,CFArrayGetCount(anArray)), countCharacters, &count);
    printf("The number of characters in the array is %d", count);
    CFRelease(anArray);
}
```

Often an applier function is used to iterate over a mutable
collection in order to remove objects matching certain criteria.
It is never safe to mutate a collection while an applier function
is iterating over it. However, there are some safe ways to use an
applier function to mutate a collection:

- Mutate after iterating. Use the applied function
  to record where changes are needed in the collection, and then mutate
  the collection after an applier function finishes executing.
- Mutate the original. If the collection is mutable, make a
  copy of the collection and use an applier function to iterate over
  the copy and mutate the original.

Which approach is easier depends on the situation. If the
original collection is immutable, then you can use a variation:

- Mutate a copy. Make a mutable copy of the collection
  and use an applier function to iterate over the original and mutate
  the copy.

[Next](Creating%20and%20Using%20Tree%20Structures.md)[Previous](Working%20With%20Mutable%20Collections.md)

