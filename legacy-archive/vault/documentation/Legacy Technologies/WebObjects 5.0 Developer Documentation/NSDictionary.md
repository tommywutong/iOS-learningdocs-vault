---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSDictionary.html
archived_at: '2026-07-15T08:13:55.927626Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSDictionary

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : Cloneable: java.io.Serializable: NSCoding: NSKeyValueCoding: NSKeyValueCodingAdditions

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

The NSDictionary class declares the programmatic interface to objects that manage immutable associations of keys and values. Use this class, or its subclass NSMutableDictionary when you need a convenient and efficient way to retrieve data associated with an arbitrary key. (For convenience, we use the term __dictionary__ to refer to any instance of one of these classes without specifying its exact class membership.)

A key-value pair within a dictionary is called an entry. Each entry consists of one object that represents the key, and a second object which is that key's value. Within a dictionary, the keys are unique. That is, no two keys in a single dictionary are equal (as determined by __equals__).

An instance of NSDictionary is an immutable dictionary: you establish its entries when it's created, and cannot modify them afterwards. An instance of NSMutableDictionary is a mutable dictionary: you can add or delete entries at any time, and the object automatically allocates memory as needed.

Internally, a dictionary uses a hash table to organize its storage and to provide rapid access to a value given the corresponding key. However, the methods defined in this class insulate you from the complexities of working with hash tables, hashing functions, or the hashed value of keys. The methods described below take keys directly, not their hashed form.

Methods that add entries to dictionaries-whether during construction (for all dictionaries) or modification (for mutable dictionaries)-add each value object to the dictionary directly. These methods also add each key object directly to the dictionary, which means that you must ensure that the keys do not change. If you expect your keys to change for any reason, you should make copies of the keys and add the copies to the dictionary.

[Table 0-6](#apple-ijbuqskkincec) describes the NSDictionary methods that provide the basis for all NSDictionary's other methods; that is, all other methods are implemented in terms of these four. If you create a subclass of NSDictionary, you need only ensure that these base methods work properly. Having done so, you can be sure that all your subclass's inherited methods operate properly.

__Table 0-6 NSDictionary's Base API__

| __Method__ | __Description__ |
| [count](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5rw65looq) | Returns the number of entries in the dictionary. |
| [objectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5xwe2tfmn2em33sjnsxs) | Returns the value associated with a given key. |
| [keysNoCopy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5vwk6ltjzxug33qpe) | Returns a natural language array containing the keys in the dictionary. |
| [objectsNoCopy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5xwe2tfmn2hgttpinxxa6i) | Returns a natural language array containing the objects in the dictionary. |

The other methods declared here operate by invoking one or more of these primitives. The non-primitive methods provide convenient ways of accessing multiple entries at once.

## Constants

---

NSDictionary provides the following constant as a convenience; you can use it when you need an empty dictionary.

|  |  |  |
| --- | --- | --- |
| __Constant__ | __Type__ | __Description__ |
| EmptyDictionary | NSDictionary | A shared NSDictionary instance containing no entries. |

## Interfaces Implemented

---

> : Cloneable:
>
> : java.io.Serializable:
>
> : NSCoding
>
> : [classForCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5rwyyltondg64sdn5sgk4q): [decodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgrdjmn2gs33omfzhsl3emvrw6zdfj5rguzldoq): [encodeWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5sw4y3pmrsvo2lunbbw6zdfoi)
>
> :
>
> : NSKeyValueCoding
>
> : [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf52gc23fkzqwy5lfizxxes3fpe): [valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf53gc3dvmvdg64slmv4q)
>
> :
>
> : NSKeyValueCodingAdditions
>
> : [takeValueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf52gc23fkzqwy5lfizxxes3fpfigc5di): [valueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf53gc3dvmvdg64slmv4vayluna)
>
> :

## Method Types

---

> **Constructors**
>
> : [NSDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5hfgrdjmn2gs33omfzhs)
>
> **Accessing keys and values**
>
> : [allKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5qwy3clmv4xg): [allKeysForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5qwy3clmv4xgrtpojhwe2tfmn2a): [allValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5qwy3cwmfwhkzlt): [isEqualToDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5uxgrlrovqwyvdpiruwg5djn5xgc4tz): [keyEnumerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5vwk6kfnz2w2zlsmf2g64q): [keysNoCopy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5vwk6ltjzxug33qpe): [objectEnumerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5xwe2tfmn2ek3tvnvsxeylun5za): [objectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5xwe2tfmn2em33sjnsxs): [objectsForKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5xwe2tfmn2hgrtpojfwk6lt): [objectsNoCopy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5xwe2tfmn2hgttpinxxa6i)
>
> **Counting entries**
>
> : [count](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5rw65looq)
>
> **Creating hash tables**
>
> : [hashtable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5ugc43iorqwe3df)
>
> **Copying dictionaries**
>
> : [immutableClone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5uw23lvorqwe3dfinwg63tf): [mutableClone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5wxk5dbmjwgkq3mn5xgk)
>
> **Methods inherited from Object**
>
> : [clone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5rwy33omu): [equals](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5sxc5lbnrzq): [hashCode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5ugc43iinxwizi): [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf52g6u3uojuw4zy)

## Constructors

---

### NSDictionary

`public NSDictionary()`

Creates an empty dictionary. To improve performance, use the `EmptyDictionary` shared instance instead. See [Constants](#apple-indeeskgifaus).

`public NSDictionary( NSArray objectArray, NSArray keyArray)`

Creates a NSDictionary with entries from the contents of the _keyArray_ and _objectArray_ NSArrays. This method steps through _objectArray_ and _keyArray_, creating entries in the new dictionary as it goes. Each key object and its corresponding value object is added directly to the dictionary. An InvalidArgumentException is thrown if the _objectArray_ and _keyArray_ do not have the same number of elements.

|  |
| --- |
| __Note:__ NSDictionary assumes that key objects are immutable. If your key objects are mutable, you should make copies of them and add the copies to the dictionary. |

`public NSDictionary(NSDictionary dictionary)`

Creates a dictionary containing the keys and values found in _dictionary_.

`public NSDictionary( Object object, Object key)`

Creates a dictionary containing a single object _object_ for a single key _key_.

|  |
| --- |
| __Note:__ NSDictionary assumes that key objects are immutable. If your key objects are mutable, you should make copies of them and add the copies to the dictionary. |

`public NSDictionary( Object[] objects[], Object[] keys[])`

Creates a NSDictionary with entries from the contents of the _keys_ and _objects_ arrays. This method steps through _objects_ and _keys_, creating entries in the new dictionary as it goes. Each key object and its corresponding value object is added directly to the dictionary. An InvalidArgumentException is thrown if the _objects_ and _keys_ do not have the same number of elements.

|  |
| --- |
| __Note:__ NSDictionary assumes that key objects are immutable. If your key objects are mutable, you should make copies of them and add the copies to the dictionary. |

`public NSDictionary( java.util.Dictionary dictionary, boolean ignoreNull)`

Creates a dictionary containing the keys and values found in _dictionary_. If _ignoreNull_ is `false`, throws an InvalidArgumentException if any key or value in _dictionary_ is `null`.

---

## Static Methods

---

### decodeObject

`public static Object decodeObject(NSCoder coder)`

Creates an NSDictionary from the data in _coder_.

__See Also:__ [NSCoding](NSCoding.md#apple-ineucskcizbeq)

---

## Instance Methods

---

### allKeys

`public NSArray allKeys()`

Returns a new array containing the dictionary's keys or an empty array if the dictionary has no entries. The order of the elements in the array isn't defined.

__See Also:__ [allValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5qwy3cwmfwhkzlt), [allKeysForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5qwy3clmv4xgrtpojhwe2tfmn2a)

---

### allKeysForObject

`public NSArray allKeysForObject(Object anObject)`

Finds all occurrences of the value _anObject_ in the dictionary and returns a new array with the corresponding keys. Each object in the dictionary is sent an __equals__ message to determine if it's equal to _anObject_. If no object matching _anObject_ is found, this method returns `null`.

__See Also:__ [allKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5qwy3clmv4xg), [keyEnumerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5vwk6kfnz2w2zlsmf2g64q)

---

### allValues

`public NSArray allValues()`

Returns a new array containing the dictionary's values, or an empty array if the dictionary has no entries. The order of the values in the array isn't defined.

__See Also:__ [allKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5qwy3clmv4xg), [objectEnumerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5xwe2tfmn2ek3tvnvsxeylun5za)

---

### classForCoder

`public Class classForCoder()`

Conformance to [NSCoding](NSCoding.md#apple-ineucskcizbeq). See the method description of [classForCoder](NSCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstinxwi2lom4xwg3dbonzum33sinxwizls) in the interface specification for NSCoding.

---

### clone

`public Object clone()`

Returns a copy (an NSDictionary object) of the receiver. Since NSDictionaries are immutable, there's no need to make an actual copy.

---

### count

`public int count()`

Returns the number of entries in the dictionary.

---

### encodeWithCoder

`public void encodeWithCoder(NSCoder coder)`

Conformance to [NSCoding](NSCoding.md#apple-ineucskcizbeq). See the method description of [encodeWithCoder](NSCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstinxwi2lom4xwk3tdn5sgkv3jorueg33emvza) in the interface specification for NSCoding.

---

### equals

`public boolean equals(Object anObject)`

Compares the receiving dictionary to _anObject_. If _anObject_ is an NSDictionary and the contents of _anObject_ are equal to the contents of the receiver, this method returns `true`. If not, it returns `false`.

Two dictionaries have equal contents if they each hold the same number of entries and, for a given key, the corresponding value objects in each dictionary satisfy the __equals__ test.

---

### hashCode

`public int hashCode()`

Provide an appropriate hash code useful for storing the receiver in a hash-based data structure.

---

### hashtable

`public java.util.Hashtable hashtable()`

Returns a java.util.Hashtable containing the receiver's entries.

---

### immutableClone

`public NSDictionary immutableClone()`

Returns an immutable copy (an NSDictionary) of the receiver. Since NSDictionaries are immutable, there's no need to make an actual copy.

---

### isEqualToDictionary

`public boolean isEqualToDictionary(NSDictionary otherDictionary)`

Compares the receiving dictionary to _otherDictionary_. If the contents of _otherDictionary_ are equal to the contents of the receiver, this method returns `true`. If not, it returns `false`.

Two dictionaries have equal contents if they each hold the same number of entries and, for a given key, the corresponding value objects in each dictionary satisfy the __equals__ test.

---

### keyEnumerator

`public java.util.Enumeration keyEnumerator()`

Returns an Enumeration object that lets you access each key in the dictionary.
> ```
> java.util.Enumeration enumerator = myDict.keyEnumerator();
>
> while (enumerator.hasMoreElements()) {{
>     Object anObject = enumerator.nextElement();
>     /* code to act on each element */
> }
> ```

When this method is used with mutable subclasses of NSDictionary, your code shouldn't modify the entries during enumeration. If you intend to modify the entries, use the [allKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5qwy3clmv4xg) method to create a "snapshot" of the dictionary's keys. Then use this snapshot to traverse the entries, modifying them along the way.

Note that the [objectEnumerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5xwe2tfmn2ek3tvnvsxeylun5za) method provides a convenient way to access each value in the dictionary.

__See Also:__ [allKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5qwy3clmv4xg), [allKeysForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5qwy3clmv4xgrtpojhwe2tfmn2a), [objectEnumerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5xwe2tfmn2ek3tvnvsxeylun5za)

---

### keysNoCopy

`protected Object[] keysNoCopy()`

Returns an array containing the dictionary's values, or an empty array if the dictionary has no entries. The order of the values in the array isn't defined. This method is similar to [allKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5qwy3clmv4xg) except the keys are not copied.

__See Also:__ [objectsNoCopy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5xwe2tfmn2hgttpinxxa6i)

---

### mutableClone

`public NSMutableDictionary mutableClone()`

Returns a mutable dictionary (an NSMutableDictionary) with the same keys and value objects as the receiver.

---

### objectEnumerator

`public java.util.Enumeration objectEnumerator()`

Returns an enumerator object that lets you access each value in the dictionary.
> ```
> java.util.Enumeration enumerator = myDict.objectEnumerator();
>
> while (enumerator.hasMoreElements()) {{
>     Object anObject = enumerator.nextElement();
>     /* code to act on each element */
> }
> ```

When this method is used with mutable subclasses of NSDictionary, your code shouldn't modify the entries during enumeration. If you intend to modify the entries, use the [allValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5qwy3cwmfwhkzlt) method to create a "snapshot" of the dictionary's values. Work from this snapshot to modify the values.

__See Also:__ [keyEnumerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5vwk6kfnz2w2zlsmf2g64q)

---

### objectForKey

`public Object objectForKey(Object aKey)`

Returns an entry's value given its key, or `null` if no value is associated with _aKey_.

__See Also:__ [allKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5qwy3clmv4xg), [allValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5qwy3cwmfwhkzlt)

---

### objectsForKeys

`public NSArray objectsForKeys( NSArray keys, Object anObject)`

Returns the set of objects from the receiver that correspond to the specified _keys_ as an NSArray. The objects in the returned array and the _keys_ array have a one-for-one correspondence, so that the nth object in the returned array corresponds to the nth key in _keys_. If an object isn't found in the receiver to correspond to a given key, the marker object, specified by _anObject_, is placed in the corresponding element of the returned array.

---

### objectsNoCopy

`protected Object[] objectsNoCopy()`

Returns an array containing the dictionary's values, or an empty array if the dictionary has no entries. The order of the values in the array isn't defined. This method is similar to [allValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5qwy3cwmfwhkzlt) except the objects are not copied.

__See Also:__ [keysNoCopy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5vwk6ltjzxug33qpe)

---

### takeValueForKey

`public void takeValueForKey( Object object, String key)`

Conformance to [NSKeyValueCoding](NSKeyValueCoding.md#apple-ineucscjjjeeu). Since NSDictionaries are immutable, this method simply throws an IllegalStateException.

---

### takeValueForKeyPath

`public void takeValueForKeyPath( Object object, String key)`

Conformance to [NSKeyValueCodingAdditions](NSKeyValueCodingAdditions.md#apple-inbemssiinbek). See the method specification of [takeValueForKeyPath](NSKeyValueCodingAdditions.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4z2bmrsgs5djn5xhgl3umfvwkvtbnr2wkrtpojfwk6kqmf2gq) in the interface specification for NSKeyValueCodingAdditions.

---

### toString

`public String toString()`

Returns a string representation of the receiver containing a string representation of each key-value pair.

---

### valueForKey

`public Object valueForKey(String key)`

Conformance to [NSKeyValueCoding](NSKeyValueCoding.md#apple-ineucscjjjeeu). Equivalent to [objectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5xwe2tfmn2em33sjnsxs).

---

### valueForKeyPath

`public Object valueForKeyPath(String key)`

Conformance to [NSKeyValueCodingAdditions](NSKeyValueCodingAdditions.md#apple-inbemssiinbek). If the key exists in the dictionary, this method returns the corresponding object in the dictionary by invoking [objectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5xwe2tfmn2em33sjnsxs). Otherwise it invokes the default implementation of valueForKeyPath. See the method specification of [valueForKeyPath](NSKeyValueCodingAdditions.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjnsxsvtbnr2wkq3pmruw4z2bmrsgs5djn5xhgl3wmfwhkzkgn5zewzlzkbqxi2a) in the interface specification for NSKeyValueCodingAdditions.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
