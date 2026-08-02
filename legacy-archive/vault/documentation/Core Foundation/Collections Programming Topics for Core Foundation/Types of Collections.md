---
title: Collections Programming Topics for Core Foundation
apple_id: 10000124i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2011-01-18'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/Articles/types.html
archived_at: '2026-07-15T07:22:16.146577Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Collections Programming Topics for Core Foundation](Introduction.md)


[Next](Collection%20Customization.md)[Previous](Common%20Characteristics%20of%20Collections.md)

# Types of Collections

Although the major collection types of Core Foundation—arrays, dictionaries, sets, bags, and trees—have characteristics in common, they each have distinct ways of organizing the data elements they contain and, in some cases, restricting which elements they contain.

A Core Foundation array—an object of opaque type CFArray—is an ordered, compact container of values. The values are in sequential order and the key for accessing these values is their _index_, an integer specifying a value’s position in the sequence. The range of indexes is from 0 to _n_-1 where _n_ is the number of values in the array. An index of 0 identifies the first value in the array. You can think of arrays as numbered slots.

Arrays are ideal for programmatic situations where sequential position is significant, such as lists whose items are ranked according to some scheme (priority, for example) or where there is a mapping between values in the array and items in list-type controls such as menus. However, you can use arrays as general-purpose containers for holding and iterating over collected values.

An array is said to be compact because, with mutable arrays, deleting a value does not leave a gap in the array. The values with higher-numbered indexes have their indexes decremented by 1. If you insert a value, all subsequent elements have their keys incremented by 1. Because of this behavior, the key for accessing a particular object may change over time as values are inserted into and deleted from an array. But the set of valid indexes is always between 0 and _n_-1.

The access time for a value in the array is guaranteed to be at worst `O(log N)` for any implementation, current and future, but will often be `O(1)` (that is, constant time). Linear search operations similarly have a worst-case complexity of `O(N*log N)`, though typically the bounds will be tighter. Insertion or deletion operations are typically linear in the number of objects in the array, but may be `O(N*log N)` clearly in the worst case in some implementations. There are no favored positions within the array for performance; for example, it is not necessarily faster to access values with low indexes or to insert or delete values with high indices.

A dictionary—an object of the CFDictionary type—is a hashing-based collection whose keys for accessing its values are arbitrary, program-defined pieces of data (or pointers to data). Although the key is usually a string (or, in Core Foundation, a CFString object), it can be anything that can fit into the size of a pointer—an integer, a reference to a Core Foundation object, even a pointer to a data structure (unlikely as that might be). The keys of dictionaries are unlike the keys of the other collection objects in that, conceptually, they are also contained by the collection along with the values. Dictionaries are primarily useful for holding and organizing data that can be labeled, such as values extracted from text fields in the user interface.

In Core Foundation, a dictionary differs from an array in that the key used to access a particular value in the dictionary remains the same as values are added to or removed from the dictionary—that is, until a value associated with a particular key is replaced or removed. In an array, the key (that is, the index) that is used to retrieve a particular value can change over time as values are added to or deleted from the array. Also, unlike an array, a dictionary does not put its values in any order. To enable later retrieval of a value, the key of the key-value pair should be constant (or be treated as constant); if the key changes after being used to put a value in the dictionary, the value might not be retrievable. The keys of a dictionary form a set; in other words, keys are guaranteed to be unique in a dictionary.

Although a customization of the CFDictionary type might not use hashing and a hash table for storage of the values, the keys require both a function that generates hash codes and a function that tests for equality of two keys based on their hash codes. These two functions together must maintain the invariant that

```
if equal(X,Y) then
    hash(X) == hash(Y)
```

Although the converse of this logic is not generally true, the contra positive is required by Boolean logic:

```
if hash(X) != hash(Y),
    then !equal(X,Y)
```

If the `hash` and `equal` key
callbacks are `NULL`, the
key is used as a pointer-sized integer and pointer equality is used. For best performance, you should try to provide a `hash` callback that computes sufficiently dispersed hash codes for the key set.

The access time for a value in a CFDictionary object is guaranteed to be at worst `O(log N)` for any implementation, but is often `O(1)` (constant time). Insertion or deletion operations are typically in constant time as well, but are `O(N*log N)` in the worst cases. It is faster to access values through a key than accessing them directly. Dictionaries tend to use significantly more memory than an array with the same number of values.

Sets and bags are related types of collections. What they have in common is that the key for accessing a value in the collection is the value itself. The difference between sets and bags is the membership “rule” for values. With sets, if the value already exists in the collection, an identical value cannot be added to the set; conversely, you can add any value to a bag even if the bag already holds that value.

This “uniquing” functionality (or lack thereof) can have many uses. Say, for example, that your program is searching the Internet and you want to keep all qualifying URLs but don’t want duplicates; a set would work nicely for this purpose. A bag could be useful for statistical sampling; you could put all collected values in it and after you finish collecting data, you could query it for the frequency of each value.

Equality of key value and contained value is determined by a callback function that you can define. This function could set any criterion for equality. For example, the values of a set or bag could be custom structures representing a customer record; the function could decide that the external (key) and contained values are the same if the value of the account-number field in both structures is the same. (As with all collections, you can also specify default callback functions when Core Foundation objects are the values in a set or bag.) For sets (as with dictionaries), the `equal` callback function also decides which values can legally be added to the collection.

You use trees—objects of the CFTree type—to represent nodes in hierarchically organized structures, such as a file system with its files and directories. Each node in this tree structure is a tree object, and that object has relationships to other tree objects. Conceptually, objects of the CFTree type are significantly different from other Core Foundation collection objects. Arrays, dictionaries, sets, and bags are containers of (typically) multiple values, but tree objects have a one-to-one relationship with their data. In other words, a tree object is associated with only one pointer-size value (although that value can be, for instance, a pointer to a structure with multiple members or even a reference to a collection object). However, the essential characteristic of a tree object is that it keeps references to multiple subtrees, each with its own chunk of data, and in that sense a interlinked group of tree objects—the tree structure—can be considered a collection.

The parent-child paradigm is useful for understanding tree objects. As stated above, these objects stand in a hierarchical relationship to each other, and at the top of the hierarchy is the “root” tree. This tree is not a subtree of any other tree—that is, it has no parent tree—but it has one or more subtrees, or child trees. And these child trees can be the parents of other trees.

Tree objects have certain rules governing their relationships. When you add children to a tree, the parent retains them, but the children do not retain their parent. Additionally, a tree may not have as one of its child trees a tree of which it is itself a child; no cycles are allowed in the traversal of a tree and its subtrees. Two trees with the same parent tree are called “siblings” of each other. Conceptually, siblings are in sequential order, as in a linked list. Operations performed on the children of a tree apply only to those direct descendants; in other words, they do not recursively affect any subtrees of those children.

Unlike the other collection objects, a tree has no need for callbacks that operate on contained values because, structurally, these values can be only of the type CFTree. However, to be useful a tree object must have some data associated with it, and this data can determine its relationships with other trees. When you create a Core Foundation tree object, you must define a “context” for the tree. The context identifies the associated data and defines callbacks that are invoked to perform necessary operations on the data, such as retaining, releasing, comparing, and describing it.

[Next](Collection%20Customization.md)[Previous](Common%20Characteristics%20of%20Collections.md)

