---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSMutableArray.html
archived_at: '2026-07-15T08:13:56.212952Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSMutableArray

> **__Inherits from:__**
> : [NSArray](NSArray.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpjzjuc4tsmf4q)

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

The NSMutableArray defines the programmatic interface for managing collections of objects called arrays. It adds insertion and deletion operations to the basic array-handling behavior inherited from its superclass, NSArray.

[Table 0-7](#apple-ijbuqskkincec) describes the NSMutableArray methods that provide the basis for all NSMutableArray's other methods; that is, all other methods are implemented in terms of these. If you create a subclass of NSMutableArray, you need only ensure that these base methods work properly. Having done so, you can be sure that all your subclass's inherited methods operate properly.

__Table 0-7 NSMutableArray's Base API__

| __Method__ | __Description__ |
| [addObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s6ylemrhwe2tfmn2a) | Adds an object to the array. |
| [addObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s6ylemrhwe2tfmn2hg) | Adds multiple objects to the array. |
| [insertObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s62loonsxe5cpmjvgky3uif2es3temv4a) | Inserts an object into the array at a specified index. |
| [removeAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s64tfnvxxmzkbnrwe6ytkmvrxi4y) | Empties the receiver of all its elements. |
| [removeObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s64tfnvxxmzkpmjvgky3uif2es3temv4a) | Removes the object at a specified index from the array. |
| `replaceObjectAtIndex(Object, int)` | Replaces the object at a specified index with another object. |
| [setArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s643foraxe4tbpe) | Sets an array's elements to the ones in another array. |
| [sortUsingComparator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s643poj2fk43jnztug33nobqxeylun5za) | Sorts the elements of the array. |

The other methods provide convenient ways of inserting an object into a specific slot in the array and removing an object based on its identity or position in the array.

## Method Types

---

> **Creating mutable arrays**
>
> : [NSMutableArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s6tstjv2xiylcnrsuc4tsmf4q): [immutableClone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s62lnnv2xiylcnrsug3dpnzsq): [clone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s6y3mn5xgk)
>
> **Adding and replacing objects**
>
> : [addObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s6ylemrhwe2tfmn2a): [addObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s6ylemrhwe2tfmn2hg): [addObjectsFromArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s6ylemrhwe2tfmn2hgrtsn5wuc4tsmf4q): [insertObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s62loonsxe5cpmjvgky3uif2es3temv4a): [replaceObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s64tfobwgcy3fj5rguzldoraxislomrsxq): [replaceObjectsInRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s64tfobwgcy3fj5rguzldorzus3ssmfxgozi): [setArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s643foraxe4tbpe)
>
> **Removing objects**
>
> : [removeAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s64tfnvxxmzkbnrwe6ytkmvrxi4y): [removeIdenticalObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s64tfnvxxmzkjmrsw45djmnqwyt3cnjswg5a): [removeLastObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s64tfnvxxmzkmmfzxit3cnjswg5a): [removeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s64tfnvxxmzkpmjvgky3u): [removeObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s64tfnvxxmzkpmjvgky3uif2es3temv4a): [removeObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s64tfnvxxmzkpmjvgky3uom): [removeObjectsInArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s64tfnvxxmzkpmjvgky3uonew4qlsojqxs): [removeObjectsInRange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s64tfnvxxmzkpmjvgky3uonew4utbnztwk)
>
> **Rearranging objects**
>
> : [sortUsingComparator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s643poj2fk43jnztug33nobqxeylun5za)

## Constructors

---

### NSMutableArray

`public NSMutableArray()`

Creates an empty mutable array.

`public NSMutableArray(int capacity)`

Creates an empty mutable array with enough allocated memory to hold the number of objects specified by _capacity_, a number greater than 0. NSMutableArrays expand as needed, so _capacity_ simply establishes the object's initial capacity.

`public NSMutableArray(NSArray anArray)`

Creates a mutable array containing the objects in _anArray_.

`public NSMutableArray(Object anObject)`

Creates a mutable array containing the single element _anObject_.

`public NSMutableArray(Object[] objects)`

Creates a mutable array containing _objects_.

`public NSMutableArray( Object[] objects, NSRange aRange)`

Creates a mutable array containing the objects from _objects_ in the range specified by aRange. After an immutable array has been initialized in this way, it can't be modified.

`public NSMutableArray( java.util.Vector aVector, NSRange aRange, boolean checkForNull)`

Creates a mutable array containing the objects from _aVector_ in the range specified by aRange. The _checkForNull_ argument controls the method's behavior when it encounters a `null` value in the vector: if _checkForNull_ is `true`, the null value is simply ignored. If _checkForNull_ is false, the method raises an IllegalArgumentException.

---

## Instance Methods

---

### addObject

`public void addObject(Object anObject)`

Inserts _anObject_ at the end of the receiver. If _anObject_ is `null`, an IllegalArgumentException is thrown.

---

### addObjects

`public void addObjects(Object[] otherArray)`

Adds the objects contained in _otherArray_ to the end of the receiver's array of objects. If any of the objects in _otherArray_ are `null`, an IllegalArgumentException is thrown.

---

### addObjectsFromArray

`public void addObjectsFromArray(NSArray anArray)`

Adds the objects contained in _anArray_ to the end of the receiver's array of objects.

---

### clone

`public Object clone()`

Creates a clone of the receiver. NSMutableArray's implementation simply creates a new NSMutableArray with the objects in the receiver.

---

### immutableClone

`public NSArray immutableClone()`

Returns a copy of the receiver as an immutable NSArray.

---

### insertObjectAtIndex

`public void insertObjectAtIndex( Object anObject, int index)`

Inserts _anObject_ into the receiver at _index_. If _index_ is already occupied, the objects at _index_ and beyond are shifted down one slot to make room. _index_ cannot be greater than the number of elements in the array. This method throws an IllegalArgumentException if _anObject_ is `null` or if _index_ is greater than the number of elements in the array.

Note that NSArrays are not like C arrays. That is, even though you might specify a size when you create an array, the specified size is regarded as a hint; the actual size of the array is still 0. Because of this, you can only insert new objects in ascending order-with no gaps. Once you add two objects, the array's size is 2, so you can add objects at indexes 0, 1, or 2. Index 3 is illegal and out of bounds; if you try to add an object at index 3 (when the size of the array is 2), NSMutableArray throws an exception.

---

### __mutableClone__

`public NSMutableArray mutableClone()`

Description forthcoming.

---

### removeAllObjects

`public void removeAllObjects()`

Empties the receiver of all its elements.

---

### removeIdenticalObject

`public void removeIdenticalObject(Object anObject)`

`public void removeIdenticalObject( Object anObject, NSRange aRange)`

Removes all occurrences of _anObject_ throughout the array; or if _aRange_ provided, removes all occurrences of _anObject_ in the specified range. These methods use the [indexOfIdenticalObject](NSArray.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5uw4zdfpbhwmslemvxhi2ldmfwe6ytkmvrxi) method to locate matches and remove them by using [removeObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s64tfnvxxmzkpmjvgky3uif2es3temv4a). Throws an IllegalArgumentException if _anObject_ is null or if _aRange_ is out of bounds.

---

### removeLastObject

`public void removeLastObject()`

Removes the receiver's element with the highest-valued index. Throws an IllegalArgumentException if there are no objects in the array.

---

### removeObject

`public void removeObject(Object anObject)`

`public void removeObject( Object anObject, NSRange aRange)`

Removes all occurrences of _anObject_ throughout the array; or if _aRange_ provided, removes all occurrences of _anObject_ in the specified range. These methods use the [indexOfObject](NSArray.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5uw4zdfpbhwmt3cnjswg5a) method to locate matches and remove them by using [removeObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s64tfnvxxmzkpmjvgky3uif2es3temv4a). Thus, matches are determined on the basis of an object's response to the __equals__ message. Throws an IllegalArgumentException if _anObject_ is null or if _aRange_ is out of bounds.

---

### removeObjectAtIndex

`public void removeObjectAtIndex(int index)`

Removes the object at _index_ and moves all elements beyond _index_ up one slot to fill the gap. This method throws a IllegalArgumentException if the array is empty or if _index_ is beyond the end of the array.

---

### removeObjects

`public void removeObjects(Object[] objects)`

This method is similar to [removeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s64tfnvxxmzkpmjvgky3u), but allows you to efficiently remove the set of objects in _objects_ with a single operation.

---

### removeObjectsInArray

`public void removeObjectsInArray(NSArray otherArray)`

This method is similar to [removeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s64tfnvxxmzkpmjvgky3u), but allows you to efficiently remove the set of objects in _otherArray_ with a single operation.

---

### removeObjectsInRange

`public void removeObjectsInRange(NSRange aRange)`

Removes each of the objects within the specified range in the receiver using [removeObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsuc4tsmf4s64tfnvxxmzkpmjvgky3uif2es3temv4a). Throws an IllegalArgumentException if _aRange_ is out of bounds.

---

### replaceObjectAtIndex

`public void replaceObjectAtIndex( Object anObject, int index)`

Replaces the object at _index_ with _anObject_. This method throws an IllegalArgumentException if _anObject_ is `null` or if _index_ is beyond the end of the array.

`public void replaceObjectAtIndex( int index, Object anObject)`

This method is deprecated. Use `replaceObjectAtIndex(Object, int)` instead.

---

### replaceObjectsInRange

`public void replaceObjectsInRange( NSRange aRange, NSArray otherArray, NSRange otherRange)`

Replaces the objects in the receiver specified by _aRange_ with the objects in _otherArray_ specified by _otherRange_. _aRange_ and _otherRange_ don't have to be equal; if _aRange_ is greater than _otherRange_, the extra objects in the receiver are removed. If _otherRange_ is greater than _aRange_, the extra objects from _otherArray_ are inserted into the receiver.

---

### setArray

`public void setArray(NSArray otherArray)`

Sets the receiver's elements to those in _otherArray_. Shortens the receiver, if necessary, so that it contains no more than the number of elements in _otherArray_. Replaces existing elements in the receiver with the elements in _otherArray_. If there are more elements in _otherArray_ than there are in the receiver, the additional items are added.

---

### sortUsingComparator

`public void sortUsingComparator(NSComparator aComparator) throws NSComparator.ComparisonException`

Sorts the receiver's elements, as determined by _aComparator_. Throws an NSComparator.Exception if _aComparator_ is null.

__See Also:__ [sortedArrayUsingComparator](NSArray.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstifzheylzf5zw64tumvsec4tsmf4vk43jnztug33nobqxeylun5za) (NSArray)

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
