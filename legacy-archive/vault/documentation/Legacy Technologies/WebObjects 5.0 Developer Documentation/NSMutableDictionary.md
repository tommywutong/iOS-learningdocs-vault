---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSMutableDictionary.html
archived_at: '2026-07-15T08:13:56.260109Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

# NSMutableDictionary

> **__Inherits from:__**
> : [NSDictionary](NSDictionary.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpjzjui2ldoruw63tboj4q): Object

> **__Implements:__**
> : Cloneable: java.io.Serializable: NSCoding: NSKeyValueCoding: NSKeyValueCodingAdditions

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

The NSMutableDictionary class declares the programmatic interface to objects that manage mutable associations of keys and values. This class adds modification operations to the basic operations it inherits from NSDictionary.

Methods that add entries to NSMutableDictionaries-whether during construction or modification-add each value object to the dictionary directly. These methods also add each key object directly to the dictionary, which means that you must ensure that the keys do not change. If you expect your keys to change for any reason, you should make copies of the keys and add the copies to the dictionary.

[Table 0-9](#apple-ijbuqskkincec) describes the NSMutableDictionary methods that provide the basis for all NSMutableDictionary's other methods; that is, all other methods are implemented in terms of these seven. If you create a subclass of NSMutableDictionary, you need only ensure that these base methods work properly. Having done so, you can be sure that all your subclass's inherited methods operate properly.

__Table 0-9 NSMutableDictionary's Base API__

| __Method__ | __Description__ |
| [count](NSDictionary.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5rw65looq) | Returns the number of entries in the dictionary. Inherited from [NSDictionary](NSDictionary.md#apple-incumskiiffeu). |
| [objectForKey](NSDictionary.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5xwe2tfmn2em33sjnsxs) | Returns the value associated with a given key. Inherited from NSDictionary. |
| [keysNoCopy](NSDictionary.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5vwk6ltjzxug33qpe) | Returns a natural language array containing the keys in the dictionary. Inherited from NSDictionary. |
| [objectsNoCopy](NSDictionary.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstiruwg5djn5xgc4tzf5xwe2tfmn2hgttpinxxa6i) | Returns a natural language array containing the objects in the dictionary. Inherited from NSDictionary. |
| [removeAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s64tfnvxxmzkbnrwe6ytkmvrxi4y) | Empties the dictionary of its entries. |
| [removeObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s64tfnvxxmzkpmjvgky3uizxxes3fpe) | Removes the specified key object and its associated value object from the dictionary. |
| [setObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s643forhwe2tfmn2em33sjnsxs) | Adds or replaces an entry to the receiver consisting of the specified key and value objects. |

The other methods declared here provide convenient ways of adding or removing multiple entries at a time.

## Interfaces Implemented

---

> : Cloneable
>
> : [clone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s6y3mn5xgk)
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
>
> : NSKeyValueCoding
>
> : [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s65dbnnsvmylmovsum33sjnsxs): valueForKey
>
> :
>
> : NSKeyValueCodingAdditions
>
> : takeValueForKeyPath: valueForKeyPath
>
> :

## Method Types

---

> **Constructors**
>
> : [NSMutableDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s6tstjv2xiylcnrsui2ldoruw63tboj4q)
>
> **Adding and removing entries**
>
> : [addEntriesFromDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s6ylemrcw45dsnfsxgrtsn5wui2ldoruw63tboj4q): [removeAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s64tfnvxxmzkbnrwe6ytkmvrxi4y): [removeObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s64tfnvxxmzkpmjvgky3uizxxes3fpe): [removeObjectsForKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s64tfnvxxmzkpmjvgky3uondg64slmv4xg): [setDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s643forcgsy3unfxw4ylspe): [setObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s643forhwe2tfmn2em33sjnsxs)
>
> **Copying the dictionary**
>
> : [immutableClone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s62lnnv2xiylcnrsug3dpnzsq)
>
> **Methods inherited from Object**
>
> : [clone](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s6y3mn5xgk)

## Constructors

---

### NSMutableDictionary

`public NSMutableDictionary()`

Creates an empty NSMutableDictionary.

`public NSMutableDictionary(int capacity)`

Creates an empty NSMutableDictionary prepared to hold at least _capacity_ entries.

`public NSMutableDictionary( NSArray objectArray, NSArray keyArray)`

Creates an NSMutableDictionary with entries from the contents of the _keyArray_ and _objectArray_ NSArrays. This method steps through _objectArray_ and _keyArray_, creating entries in the new dictionary as it goes. Each key object and its corresponding value object is added directly to the dictionary. An InvalidArgumentException is thrown if the _objectArray_ and _keyArray_ do not have the same number of elements.

|  |
| --- |
| __Note:__ NSMutableDictionary assumes that key objects are immutable. If your key objects are mutable, you should make copies of them and add the copies to the dictionary. |

`public NSMutableDictionary(NSDictionary dictionary)`

Creates an NSMutableDictionary containing the keys and values found in _dictionary_.

`public NSMutableDictionary( Object object, Object key)`

Creates an NSMutableDictionary containing a single object _object_ for a single key _key_.

|  |
| --- |
| __Note:__ NSMutableDictionary assumes that key objects are immutable. If your key objects are mutable, you should make copies of them and add the copies to the dictionary. |

`public NSMutableDictionary( Object[] objects, Object[] keys)`

Creates an NSMutableDictionary with entries from the contents of the _keys_ and _objects_ arrays. This method steps through _objects_ and _keys_, creating entries in the new dictionary as it goes. Each key object and its corresponding value object is added directly to the dictionary. An InvalidArgumentException is thrown if the _objects_ and _keys_ do not have the same number of elements.

|  |
| --- |
| __Note:__ NSMutableDictionary assumes that key objects are immutable. If your key objects are mutable, you should make copies of them and add the copies to the dictionary. |

`public NSMutableDictionary( java.util.Dictionary dictionary, boolean ignoreNull)`

Creates an NSMutableDictionary containing the keys and values found in _dictionary_. If _ignoreNull_ is `false`, throws an InvalidArgumentException if any key or value in _dictionary_ is `null`.

---

## Instance Methods

---

### addEntriesFromDictionary

`public void addEntriesFromDictionary(NSDictionary otherDictionary)`

Adds the entries from _otherDictionary_ to the receiver.

__See Also:__ [setObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s643forhwe2tfmn2em33sjnsxs)

---

### clone

`public Object clone()`

Returns a copy (a NSMutableDictionary object) of the receiver.

---

### immutableClone

`public NSDictionary immutableClone()`

Returns an immutable copy (an NSDictionary object) of the receiver.

---

### __mutableClone__

`public NSMutableArray mutableClone()`

Description forthcoming.

---

### removeAllObjects

`public void removeAllObjects()`

Empties the dictionary of its entries.

__See Also:__ [removeObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s64tfnvxxmzkpmjvgky3uizxxes3fpe), [removeObjectsForKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s64tfnvxxmzkpmjvgky3uondg64slmv4xg)

---

### removeObjectForKey

`public Object removeObjectForKey(Object key)`

Removes the dictionary entry identified by _key_ and returns the entry's value object. If no entry identified by _key_ exists, this method returns `null`.

__See Also:__ [removeObjectsForKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s64tfnvxxmzkpmjvgky3uondg64slmv4xg), [removeAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s64tfnvxxmzkbnrwe6ytkmvrxi4y)

---

### removeObjectsForKeys

`public void removeObjectsForKeys(NSArray keyArray)`

Removes one or more objects from the receiver. The entries are identified by the keys in _keyArray_. This method does not raise if the receiver does not contain entries for one or more of the keys.

__See Also:__ [removeObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s64tfnvxxmzkpmjvgky3uizxxes3fpe), [removeAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s64tfnvxxmzkbnrwe6ytkmvrxi4y)

---

### setDictionary

`public void setDictionary(NSDictionary otherDictionary)`

Sets the receiver to entries in _otherDictionary_. This method removes all entries from the receiver (with [removeAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s64tfnvxxmzkbnrwe6ytkmvrxi4y)) and adds each entry from _otherDictionary_ into the receiver.

---

### setObjectForKey

`public void setObjectForKey( Object anObject, Object aKey)`

Adds or replaces an entry to the receiver consisting of _aKey_ and its corresponding value object _anObject_. Throws an InvalidArgumentException if the key or value object is `null`.

|  |
| --- |
| __Note:__ NSMutableDictionary assumes that key objects are immutable. If your key objects are mutable, you should make copies of them and add the copies to the dictionary. |

__See Also:__ [removeObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s64tfnvxxmzkpmjvgky3uizxxes3fpe)

---

### takeValueForKey

`public void takeValueForKey( Object value, String key)`

Conformance to [NSKeyValueCoding](NSKeyValueCoding.md#apple-ineucscjjjeeu). Invokes [setObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s643forhwe2tfmn2em33sjnsxs) with the specified parameters if _value_ is not `null`. Otherwise invokes [removeObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2xiylcnrsui2ldoruw63tboj4s64tfnvxxmzkpmjvgky3uizxxes3fpe) for the specified key.

|  |
| --- |
| __Note:__ NSMutableDictionary assumes that key objects are immutable. If your key objects are mutable, you should make copies of them and add the copies to the dictionary. |

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
