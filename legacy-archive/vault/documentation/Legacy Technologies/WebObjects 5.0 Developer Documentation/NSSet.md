---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSSet.html
archived_at: '2026-07-15T08:13:56.525806Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSSet

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : Cloneable: java.io.Serializable: NSCoding

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

The NSSet and NSMutableSet classes declare the programmatic interface to an object that manages a set of objects. NSSet provides support for the mathematical concept of a set. A set, both in its mathematical sense and in the implementation of NSSet, is an unordered collection of distinct elements. The NSMutableSet class is provided for sets whose contents may be altered.

NSSet declares the programmatic interface for static sets of objects. You establish a static set's entries when it's created, and thereafter the entries can't be modified. NSMutableSet, on the other hand, declares a programmatic interface for dynamic sets of objects. A dynamic-or mutable-set allows the addition and deletion of entries at any time, automatically allocating memory as needed.

Use sets as an alternative to arrays when the order of elements isn't important and performance in testing whether an object is contained in the set is a consideration-while arrays are ordered, testing for membership is slower than with sets. When testing for set membership, the __equals__ method is invoked only once.

Methods that add entries to sets-whether during construction (for all sets) or modification (for mutable sets)-add each member to the set directly. This means that you must ensure that the members do not change. If you expect your members to change for any reason, you should make copies of them and add the copies to the set.

[Table 0-13](#apple-ijbuqskkincec) describes the NSSet methods that provide the basis for all NSSet's other methods; that is, all other methods are implemented in terms of these three. If you create a subclass of NSSet, you need only ensure that these base methods work properly. Having done so, you can be sure that all your subclass's inherited methods operate properly.

__Table 0-13 NSSet's Base API__

| __Method__ | __Description__ |
| [count](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3dn52w45a) | Returns the number of members in the set. |
| [member](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3nmvwwezls) | Returns the object in the set that is equal to the specified object. |
| [objectsNoCopy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3pmjvgky3uonhg6q3pob4q) | Returns the actual array of objects in the set. |

NSSet provides methods for querying the elements of the set. The [allObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3bnrwe6ytkmvrxi4y) method returns an array containing the objects in a set. The [anyObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3bnz4u6ytkmvrxi) method returns some object in the set. Additionally, [intersectsSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3jnz2gk4ttmvrxi42tmv2a) tests for set intersection, [isEqualToSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3joncxc5lbnrkg6u3foq) tests for set equality, and [isSubsetOfSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3jonjxkyttmv2e6zstmv2a) tests for one set being a subset of another.The [objectEnumerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3pmjvgky3uivxhk3lfojqxi33s) method provides for traversing elements of the set one by one.

## Constants

---

NSSet provides the following constant as a convenience; you can use it when you need an empty set.

|  |  |  |
| --- | --- | --- |
| __Constant__ | __Type__ | __Description__ |
| EmptySet | NSSet | A shared NSSet instance containing no members. |

## Interfaces Implemented

---

> : Cloneable
>
> : [clone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3dnrxw4zi)
>
> :
>
> : java.io.Serializable:
>
> : NSCoding
>
> : [classForCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3dnrqxg42gn5zeg33emvza): [decodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgu3foqxwizldn5sgkt3cnjswg5a): [encodeWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3fnzrw6zdfk5uxi2cdn5sgk4q)
>
> :

## Method Types

---

> **Constructors**
>
> : [NSSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil2oknjwk5a)
>
> **Counting entries**
>
> : [count](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3dn52w45a)
>
> **Accessing the members**
>
> : [allObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3bnrwe6ytkmvrxi4y): [anyObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3bnz4u6ytkmvrxi): [containsObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3dn5xhiyljnzzu6ytkmvrxi): [member](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3nmvwwezls): [objectEnumerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3pmjvgky3uivxhk3lfojqxi33s): [objectsNoCopy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3pmjvgky3uonhg6q3pob4q)
>
> **Comparing sets**
>
> : [intersectsSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3jnz2gk4ttmvrxi42tmv2a): [isEqualToSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3joncxc5lbnrkg6u3foq): [isSubsetOfSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3jonjxkyttmv2e6zstmv2a)
>
> **Joining sets**
>
> : [setByIntersectingSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3tmv2ee6kjnz2gk4ttmvrxi2lom5jwk5a): [setBySubtractingSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3tmv2ee6ktovrhi4tbmn2gs3thknsxi): [setByUnioningSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3tmv2ee6kvnzuw63tjnztvgzlu)
>
> **Methods inherited from Object**
>
> : [equals](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3fof2wc3dt): [hashCode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3imfzwqq3pmrsq): [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3un5jxi4tjnztq)
>
> **Copying sets**
>
> : [immutableClone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3jnvwxk5dbmjwgkq3mn5xgk): [mutableClone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3nov2gcytmmvbwy33omu)

## Constructors

---

### NSSet

`public NSSet()`

Creates an empty NSSet. To improve performance, use the EmptySet shared instance. See [Constants](#apple-ijeeiskkizauk).

`public NSSet(NSArray anArray)`

Creates an NSSet containing the objects in _anArray_.

|  |
| --- |
| __Note:__ NSSet assumes that the member objects are immutable. If your member objects are mutable, you should make copies of them and add the copies to the set. |

`public NSSet(NSSet aSet)`

Creates an NSSet containing the objects in _aSet_.

`public NSSet(Object object)`

Creates an NSSet containing the single object _object_.

|  |
| --- |
| __Note:__ NSSet assumes that member objects are immutable. If your member objects are mutable, you should make copies of them and add the copies to the set. |

`public NSSet(Object[] objects[])`

Creates an NSSet containing the objects in the _objects_ language array.

|  |
| --- |
| __Note:__ NSSet assumes that member objects are immutable. If your member objects are mutable, you should make copies of them and add the copies to the set. |

---

## Static Methods

---

### decodeObject

`public static Object decodeObject(NSCoder coder)`

Creates an NSSet from the data in _coder_.

__See Also:__ [NSCoding](NSCoding.md#apple-ineucskcizbeq)

---

## Instance Methods

---

### allObjects

`public NSArray allObjects()`

Returns an array containing the receiver's members, or an empty array if the receiver has no members. The order of the objects in the array isn't defined.

__See Also:__ [anyObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3bnz4u6ytkmvrxi), [objectEnumerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3pmjvgky3uivxhk3lfojqxi33s)

---

### anyObject

`public Object anyObject()`

Returns one of the objects in the set (essentially chosen at random), or null if the set contains no objects.

__See Also:__ [allObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3bnrwe6ytkmvrxi4y), [objectEnumerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3pmjvgky3uivxhk3lfojqxi33s)

---

### classForCoder

`public Class classForCoder()`

Conformance with [NSCoding](NSCoding.md#apple-ineucskcizbeq). Please see the method description of [classForCoder](NSCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstinxwi2lom4xwg3dbonzum33sinxwizls) in the interface specification for NSCoding.

---

### clone

`public Object clone()`

Returns a copy (a NSSet object) of the receiver. Since NSSets are immutable, there's no need to make an actual copy.

---

### containsObject

`public boolean containsObject(Object anObject)`

Returns true if _anObject_ is present in the set, false otherwise.

__See Also:__ [member](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3nmvwwezls)

---

### count

`public int count()`

Returns the number of members in the set.

---

### encodeWithCoder

`public void encodeWithCoder(NSCoder aNSCoder)`

Conformance with [NSCoding](NSCoding.md#apple-ineucskcizbeq). Please see the method description of [encodeWithCoder](NSCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstinxwi2lom4xwk3tdn5sgkv3jorueg33emvza) in the interface specification for NSCoding.

---

### equals

`public boolean equals(Object anObject)`

Compares the receiving set to _anObject_. If _anObject_ is an NSSet and the contents of _anObject_ are equal to the contents of the receiver, this method returns `true`. If not, it returns `false`.

---

### hashCode

`public int hashCode()`

Provide an appropriate hash code useful for storing the receiver in a hash-based data structure. This value is the number of objects in the set.

---

### immutableClone

`public NSSet immutableClone()`

Returns an immutable copy (an NSSet) of the receiver. Since the NSSets are immutable, there's no need to make an actual copy.

---

### intersectsSet

`public boolean intersectsSet(NSSet otherSet)`

Returns true if at least one object in the receiver is also present in _otherSet_, `false` otherwise. The result of this method corresponds to the mathematical concept of disjoint sets: if the sets are not disjoint, __intersectsSet__ returns `true`, otherwise it returns `false`.

__See Also:__ [isEqualToSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3joncxc5lbnrkg6u3foq), [isSubsetOfSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3jonjxkyttmv2e6zstmv2a)

---

### isEqualToSet

`public boolean isEqualToSet(NSSet otherSet)`

Compares the receiving set to _otherSet_. If the contents of _otherSet_ are equal to the contents of the receiver, this method returns true. If not, it returns false.

Two sets have equal contents if they each have the same number of members and if each member matches a member in the other set (as determined by __equals__).

__See Also:__ [intersectsSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3jnz2gk4ttmvrxi42tmv2a), [isSubsetOfSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3jonjxkyttmv2e6zstmv2a)

---

### isSubsetOfSet

`public boolean isSubsetOfSet(NSSet otherSet)`

Returns true if every object in the receiver is also present in _otherSet_, false otherwise.

__See Also:__ [intersectsSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3jnz2gk4ttmvrxi42tmv2a), [isEqualToSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3joncxc5lbnrkg6u3foq)

---

### member

`public Object member(Object anObject)`

If _anObject_ is present in the set (as determined by __equals__), the object in the set is returned. Otherwise returns null.

---

### mutableClone

`public NSMutableSet mutableClone()`

Returns a mutable set (an NSMutableSet) with the same members as the receiver.

---

### objectEnumerator

`public java.util.Enumeration objectEnumerator()`

Returns an enumerator object that lets you access each object in the set
> ```
> java.util.Enumeration enumerator = mySet.objectEnumerator();
>
> while (enumerator.hasMoreElements()) {{
>     Object anObject = enumerator.nextElement();
>     /* code to act on each element */
> }
> ```

When this method is used with mutable subclasses of NSSet, your code shouldn't modify the set during enumeration. If you intend to modify the set, use the [allObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3bnrwe6ytkmvrxi4y) method to create a "snapshot" of the set's members. Enumerate the snapshot, but make your modifications to the original set.

---

### objectsNoCopy

`protected Object[] objectsNoCopy()`

Returns the actual array of objects contained in the set.

---

### setByIntersectingSet

`public NSSet setByIntersectingSet(NSSet otherSet)`

Returns a set of objects that are in both the receiver and _otherSet_.

__See Also:__ [intersectsSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3jnz2gk4ttmvrxi42tmv2a), [isSubsetOfSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3jonjxkyttmv2e6zstmv2a), [isEqualToSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3joncxc5lbnrkg6u3foq), [setBySubtractingSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3tmv2ee6ktovrhi4tbmn2gs3thknsxi), [setByUnioningSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3tmv2ee6kvnzuw63tjnztvgzlu)

---

### setBySubtractingSet

`public NSSet setBySubtractingSet(NSSet otherSet)`

Returns a set of objects that are in the receiver but not in _otherSet_.

__See Also:__ [intersectsSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3jnz2gk4ttmvrxi42tmv2a), [isSubsetOfSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3jonjxkyttmv2e6zstmv2a), [isEqualToSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3joncxc5lbnrkg6u3foq), [setByIntersectingSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3tmv2ee6kjnz2gk4ttmvrxi2lom5jwk5a), [setByUnioningSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3tmv2ee6kvnzuw63tjnztvgzlu)

---

### setByUnioningSet

`public NSSet setByUnioningSet(NSSet otherSet)`

Returns a set of objects that are either in the receiver or in _otherSet_ or both. If an object is in both, the resulting set contains it only once.

__See Also:__ [intersectsSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3jnz2gk4ttmvrxi42tmv2a), [isSubsetOfSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3jonjxkyttmv2e6zstmv2a), [isEqualToSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3joncxc5lbnrkg6u3foq), [setByIntersectingSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3tmv2ee6kjnz2gk4ttmvrxi2lom5jwk5a), [setBySubtractingSet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstknsxil3tmv2ee6ktovrhi4tbmn2gs3thknsxi)

---

### toString

`public String toString()`

Returns a string representation of the receiver. The string has the form "(object1, object2, ...)".

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
