---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSMutableSet.html
archived_at: '2026-07-15T08:13:56.300102Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

# NSMutableSet

> **__Inherits from:__**
> : [NSSet](NSSet.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpjzjvgzlu): Object

> **__Implements:__**
> : Cloneable: java.io.Serializable: NSCoding

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

The NSMutableSet class declares the programmatic interface to an object that manages a mutable set of objects. NSMutableSet provides support for the mathematical concept of a set. A set, both in its mathematical sense, and in the NSMutableSet implementation, is an unordered collection of distinct elements. The NSSet class supports creating and managing immutable sets.

[Table 0-11](#apple-ijbuqskkincec) describes the NSMutableSet methods that provide the basis for all NSMutableSet's other methods; that is, all other methods are implemented in terms of these five. If you create a subclass of NSMutableSet, you need only ensure that these base methods work properly. Having done so, you can be sure that all your subclass's inherited methods operate properly.

__Table 0-11 NSMutableSet's Base API__

| __Method__ | __Description__ |
| [count](NSSet.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3dn52w45a) | Returns the number of members in the set. |
| [member](NSSet.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3nmvwwezls) | Returns the object in the set that is equal to the specified object. |
| [objectsNoCopy](NSSet.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3pmjvgky3uonhg6q3pob4q) | Returns the actual array of objects in the set. |
| [removeAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5zgk3lpozsuc3dmj5rguzldorzq) | Empties the set of all its members. |
| [removeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5zgk3lpozsu6ytkmvrxi) | Removes the specified object from the set. |

Objects are removed from an NSMutableSet using any of the methods [intersectSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5uw45dfojzwky3uknsxi), [removeAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5zgk3lpozsuc3dmj5rguzldorzq), [removeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5zgk3lpozsu6ytkmvrxi), or [subtractSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5zxkytuojqwg5ctmv2a).

Objects are added to an NSMutableSet with [addObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5qwizcpmjvgky3u), which adds a single object to the set; [addObjectsFromArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5qwizcpmjvgky3uondhe33nifzheylz), which adds all objects from a specified array to the set; or with [unionSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf52w42lpnzjwk5a), which adds all the objects from another set.

Methods that add entries to NSMutableSets-whether during construction or modification-add each member to the set directly. This means that you must ensure that the members do not change. If you expect your members to change for any reason, you should make copies of them and add the copies to the set.

## Interfaces Implemented

---

> : Cloneable
>
> : [clone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5rwy33omu)
>
> :
>
> : java.io.Serializable:
>
> : NSCoding
>
> : classForCoder: decodeObject: encodeWithCoder
>
> :

## Method Types

---

> **Constructors**
>
> : [NSMutableSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5hfgtlvorqwe3dfknsxi)
>
> **Adding and removing entries**
>
> : [addObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5qwizcpmjvgky3u): [addObjectsFromArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5qwizcpmjvgky3uondhe33nifzheylz): [removeAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5zgk3lpozsuc3dmj5rguzldorzq): [removeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5zgk3lpozsu6ytkmvrxi)
>
> **Combining and recombining sets**
>
> : [intersectSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5uw45dfojzwky3uknsxi): [setSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5zwk5ctmv2a): [subtractSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5zxkytuojqwg5ctmv2a): [unionSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf52w42lpnzjwk5a)
>
> **Copying the set**
>
> : [immutableClone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5uw23lvorqwe3dfinwg63tf)

## Constructors

---

### NSMutableSet

`public NSMutableSet()`

Creates an empty NSMutableSet.

`public NSMutableSet(NSArray anArray)`

Creates an NSMutableSet containing the objects in _anArray_.

|  |
| --- |
| __Note:__ NSMutableSet assumes that member objects are immutable. If your member objects are mutable, you should make copies of them and add the copies to the set. |

`public NSMutableSet(NSSet aSet)`

Creates an NSMutableSet containing the objects in _aSet_.

`public NSMutableSet(Object anObject)`

Creates an NSMutableSet containing a single object _anObject_.

|  |
| --- |
| __Note:__ NSMutableSet assumes that member objects are immutable. If your member objects are mutable, you should make copies of them and add the copies to the set. |

`public NSMutableSet(Object[] objects[])`

Creates an NSMutableSet containing the objects in the _objects_ language array.

|  |
| --- |
| __Note:__ NSMutableSet assumes that member objects are immutable. If your member objects are mutable, you should make copies of them and add the copies to the set. |

`public NSMutableSet(int capacity)`

Creates an NSMutableSet that can hold at least _capacity_ objects.

---

## Instance Methods

---

### addObject

`public void addObject(Object anObject)`

Adds the specified object to the receiver if it is not already a member. If _anObject_ is already present in the set, this method has no effect on either the set or on _anObject_.

|  |
| --- |
| __Note:__ NSMutableSet assumes that member objects are immutable. If your member objects are mutable, you should make copies of them and add the copies to the set. |

__See Also:__ [addObjectsFromArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5qwizcpmjvgky3uondhe33nifzheylz), [unionSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf52w42lpnzjwk5a)

---

### addObjectsFromArray

`public void addObjectsFromArray(NSArray anArray)`

Adds each object contained in _anArray_ to the receiver, if that object is not already a member. If a given element of the array is already present in the set, this method has no effect on either the set or on the array element.

|  |
| --- |
| __Note:__ NSMutableSet assumes that member objects are immutable. If your member objects are mutable, you should make copies of them and add the copies to the set. |

__See Also:__ [addObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5qwizcpmjvgky3u), [unionSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf52w42lpnzjwk5a)

---

### clone

`public Object clone()`

Creates a clone of the receiver. NSMutableSet's implementation simply creates a new NSMutableSet with the objects in the receiver.

---

### immutableClone

`public NSSet immutableClone()`

Creates an immutable copy (a NSSet) of the receiver.

---

### intersectSet

`public void intersectSet(NSSet otherSet)`

Removes from the receiver each object that isn't a member of _otherSet_.

__See Also:__ [removeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5zgk3lpozsu6ytkmvrxi), [removeAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5zgk3lpozsuc3dmj5rguzldorzq), [subtractSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5zxkytuojqwg5ctmv2a)

---

### __mutableClone__

`public NSMutableArray mutableClone()`

Description forthcoming.

---

### removeAllObjects

`public void removeAllObjects()`

Empties the set of all its members.

__See Also:__ [removeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5zgk3lpozsu6ytkmvrxi), [intersectSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5uw45dfojzwky3uknsxi), [subtractSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5zxkytuojqwg5ctmv2a)

---

### removeObject

`public void removeObject(Object anObject)`

Removes _anObject_ from the set.

__See Also:__ [removeAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5zgk3lpozsuc3dmj5rguzldorzq), [intersectSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5uw45dfojzwky3uknsxi), [subtractSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5zxkytuojqwg5ctmv2a)

---

### setSet

`public void setSet(NSSet otherSet)`

Empties the receiver, then adds each object contained in _otherSet_ to the receiver.

---

### subtractSet

`public void subtractSet(NSSet otherSet)`

Removes from the receiver each object contained in _otherSet_ that is also present in the receiver. If any member of _otherSet_ isn't present in the receiving set, this method has no effect on either the receiver or on the _otherSet_ member.

__See Also:__ [removeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5zgk3lpozsu6ytkmvrxi), [removeAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5zgk3lpozsuc3dmj5rguzldorzq), [intersectSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5uw45dfojzwky3uknsxi)

---

### unionSet

`public void unionSet(NSSet otherSet)`

Adds each object contained in _otherSet_ to the receiver, if that object is not already a member. If any member of _otherSet_ is already present in the receiver, this method has no effect on either the receiver or on the _otherSet_ member.

__See Also:__ [addObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5qwizcpmjvgky3u), [addObjectsFromArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsvgzluf5qwizcpmjvgky3uondhe33nifzheylz)

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
