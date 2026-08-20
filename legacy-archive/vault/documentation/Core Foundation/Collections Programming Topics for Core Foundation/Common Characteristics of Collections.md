---
title: Collections Programming Topics for Core Foundation
apple_id: 10000124i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2011-01-18'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/Articles/common.html
archived_at: '2026-07-15T07:22:13.130887Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Collections Programming Topics for Core Foundation](Introduction.md)


[Next](Types%20of%20Collections.md)[Previous](Introduction.md)

# Common Characteristics of Collections

A collection object (or simply, a collection) is a container of discrete values, usually of the same type. A collection can contain other Core Foundation objects, custom data structures, and primitive data values. Contained Core Foundation objects can be of different types. Strictly speaking, “contain” is not an exact term (although it’s conceptually useful) because an element of data in a Core Foundation collection can be no larger than the size of a pointer, which varies by processor and compiler. But pointers afford a great deal of flexibility and thus collection objects permit references to Core Foundation objects and pointers to any chunk of data as well as primitive values (such as integers) that take up no more space than a pointer address.

All collection objects enable you to access a contained value that satisfies a particular external property. This property, generally referred to as a “key,” varies according to the organizing scheme enforced by the type of collection. For example, the key for an array is an integer that specifies position within the collection; on the other hand, a dictionary—for which the term “key” has a more of a conventional meaning—permits any arbitrary value to act as the key for retrieving a contained value. A Core Foundation object retrieved from a collection is not guaranteed to persist because the owning collection might free it, so if you want to hold onto it you should retain or copy it. See [Types of Collections](Types%20of%20Collections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgezdslkdjjbeksscjbea) for more on the keys of specific collection types.

Most collection objects have a set of call back functions that define fundamental operations performed on the elements of that collection. These callbacks are invoked to

- retain elements added to a collection
- release elements removed from a collection
- compare one element in a collection to another
- print debugging information about contained elements
- for sets, bags, and dictionary keys, compute a hash code

Default callbacks are provided for collections that hold Core Foundation objects.

Notice in particular that the callbacks affect the memory management semantics of collection objects. When you create a collection, you specify the callbacks that it should use when items are added to or removed from the collection. The default callbacks are appropriate for collections that contain CF types—they retain an object that is added to the collection, and release an object that is removed from the collection. If you have custom data, or if the default callbacks are insufficient for your purposes, you can define your own. See [Creating and Copying Collections](Creating%20and%20Copying%20Collections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeztelkdjjbekscbifdq) for more on this subject.

One type of function that is particularly interesting is the _applier function_. Most collection objects allow you to define a callback function. You then pass a pointer to this applier function in collection functions that have `ApplyFunction` embedded in their names. The behavior defined in the callback function is applied iteratively to each element in the collection. This behavior is essentially the same thing as a `for` loop enumerating a collection; the code within the loop is applied to each element in the collection.

Except for trees (which are not true containers of other objects), collections come in two “flavors” or variants: immutable and mutable. The values in immutable collections are set for the life of the collection; you cannot add values to them or remove values from them. Mutable collections, however, let you add values, reorder values, and remove values. Mutable collections have two sub-flavors, fixed-size and variable-size, as determined by the capacity parameter in the functions that create these objects. For fixed-size collections you set the maximum number of values that the collection can contain.

Variable-size collections, on the other hand, can hold an unlimited number of values (or rather, limited only by constraints external to the collection, like the amount of available memory). Fixed-size collections tend to be higher performing, but you must be able to put a definite limit on the number of values that can be contained.

Some collection functions operate on both mutable and immutable collections (for example, getting the number of data elements and accessing data) whereas others work only with mutable collection objects, performing such operations as appending, inserting, removing, and sorting elements. See [Working With Mutable Collections](Working%20With%20Mutable%20Collections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeztklkdjjbekscbifdq) for details on these kinds of operations.

[Next](Types%20of%20Collections.md)[Previous](Introduction.md)

