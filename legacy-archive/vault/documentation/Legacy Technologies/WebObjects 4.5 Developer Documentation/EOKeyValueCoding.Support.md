---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOKeyValueCodingSupport.html
archived_at: '2026-07-15T08:11:37.730680Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOKeyValueCoding.Support

> **__Inherits
> from:__**
> : Object

> **__Package:__**
> : com.apple.client.eocontrol

---

## Class Description

---

EOKeyValueCoding.Support provides default
implementations of the EOKeyValueCoding interface.

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.yellow.eocontrol package. |

An EOCustomObject uses EOKeyValueCoding.Support's default
implementations. Typically your custom enterprise object classes
inherit from EOCustomObject and inherit the default implementations.
EOKeyValueCoding.Support also enables you to put non-enterprise
objects into the interface layer by declaring that your class conforms
to key-value coding.

The methods in the Support class are just like the methods
defined by the EOKeyValueCoding interface, except they are all static
methods and they take an extra argument-the enterprise object
on which the default implementation should operate. For example,
suppose you want to implement an Employee enterprise object class
that doesn't inherit from EOCustomObject but that uses Support's default
implementations. Employee's [valueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe) method would look like
this:

> ```
> public Object valueForKey(String key)
>     return EOKeyValueCoding.Support.valueForKey(this, key);
> }
> ```

## Method Types

---

> **Accessing values**
> : [storedValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6s3fpflgc3dvmvbw6zdjnzts4u3vobyg64tuf5zxi33smvsfmylmovsum33sjnsxs)
> : [takeStoredValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6s3fpflgc3dvmvbw6zdjnzts4u3vobyg64tuf52gc23fkn2g64tfmrlgc3dvmvdg64slmv4q)
> : [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6s3fpflgc3dvmvbw6zdjnzts4u3vobyg64tuf52gc23fkzqwy5lfizxxes3fpe)
> : [valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6s3fpflgc3dvmvbw6zdjnzts4u3vobyg64tuf53gc3dvmvdg64slmv4q)
>
> **Handling error conditions**
> : [handleQueryWithUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6s3fpflgc3dvmvbw6zdjnzts4u3vobyg64tuf5ugc3tenrsvc5lfoj4vo2lunbkw4ytpovxgis3fpe)
> : [handleTakeValueForUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6s3fpflgc3dvmvbw6zdjnzts4u3vobyg64tuf5ugc3tenrsviyllmvlgc3dvmvdg64svnzrg65lomrfwk6i)
> : [unableToSetNullForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6s3fpflgc3dvmvbw6zdjnzts4u3vobyg64tuf52w4ylcnrsvi32tmv2e45lmnrdg64slmv4q)

## Static Methods

---

### handleQueryWithUnboundKey

`public static Object handleQueryWithUnboundKey(
Object anObject,
String key)`

Throws an IllegalArgumentException.

__See
Also:__  [handleQueryWithUnboundKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpnbqw4zdmmvixkzlspflws5dikvxge33vnzsewzlz) (EOKeyValueCoding)

---

### handleTakeValueForUnboundKey

`public static void handleTakeValueForUnboundKey(
Object anObject,
Object value,
String key)`

Throws an IllegalArgumentException.

__See
Also:__  [handleTakeValueForUnboundKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpnbqw4zdmmvkgc23fkzqwy5lfizxxevlomjxxk3tejnsxs) (EOKeyValueCoding)

---

### storedValueForKey

`public static Object storedValueForKey(
Object anObject,
String key)`

Returns _anObject_'s
property identified by _key._ Similar
to the implementation of [valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6s3fpflgc3dvmvbw6zdjnzts4u3vobyg64tuf53gc3dvmvdg64slmv4q),
but `storedValueForKey` resolves _key_ with
a different method-instance variable search order:

1. Searches
   for a private accessor method based on _key_ (a
   method preceded by an underbar). For example, with a key of "lastName", `storedValueForKey` looks
   for a method named _getLastName or _lastName.
2. If a private accessor isn't found, searches for an instance
   variable based on _key_ and returns
   its value directly. For example, with a key of "lastName", `storedValueForKey` looks
   for an instance variable named `_lastName` or `lastName`.
3. If neither a private accessor or an instance variable is found, `storedValueForKey` searches
   for a public accessor method based on _key._
   For the key "lastName", this would be getLastName or lastName.

__See
Also:__  [storedValueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpon2g64tfmrlgc3dvmvdg64slmv4q) (EOKeyValueCoding)

---

### takeStoredValueForKey

`public static void takeStoredValueForKey(
Object anObject,
Object value,
String key)`

Sets _anObject_'s
property identified by _key_ to _value._
Similar to the implementation of [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6s3fpflgc3dvmvbw6zdjnzts4u3vobyg64tuf52gc23fkzqwy5lfizxxes3fpe), but it resolves _key_ with
a different method-instance variable search order:

1. Searches
   for a private accessor method based on _key_ (a
   method preceded by an underbar). For example, with a key of "lastName", `takeStoredValueForKey` looks
   for a method named _setLastName.
2. If a private accessor isn't found, searches for an instance
   variable based on _key_ and sets its
   value directly. For example, with a key of "lastName", `takeStoredValueForKey` looks
   for an instance variable named `_lastName` or `lastName`.
3. If neither a private accessor or an instance variable is found, `takeStoredValueForKey` searches
   for a public accessor method based on _key._
   For the key "lastName", this would be setLastName.

__See
Also:__  [takeStoredValueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzktorxxezlekzqwy5lfizxxes3fpe) (EOKeyValueCoding)

---

### takeValueForKey

`public static void takeValueForKey(
Object anObject,
Object value,
String key)`

Sets _anObject_'s
property identified by _key_ to _value,_
invoking [handleTakeValueForUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6s3fpflgc3dvmvbw6zdjnzts4u3vobyg64tuf5ugc3tenrsviyllmvlgc3dvmvdg64svnzrg65lomrfwk6i) if
the receiver doesn't recognize _key_ and [unableToSetNullForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6s3fpflgc3dvmvbw6zdjnzts4u3vobyg64tuf52w4ylcnrsvi32tmv2e45lmnrdg64slmv4q) if _value_ is `null` and _key_ identifies
a scalar property. The default implementation works as follows:

1. Searches for a public accessor method of the form `set` _Key,_
   invoking it if there is one.
2. If a public accessor method isn't found, searches for a
   private accessor method of the form `_set` _Key,_ invoking
   it if there is one.
3. If an accessor method isn't found and the static method [accessInstanceVariablesDirectly](EOCustomObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3von2g63kpmjvgky3uf5qwgy3fonzus3ttorqw4y3fkzqxe2lbmjwgk42enfzgky3unr4q) in _anObject_'s
   class returns `true`, `takeValueForKey` searches
   for an instance variable based on _key_ and sets
   the value directly. For the key "lastName", this would be `_lastName` or `lastName`.

__See
Also:__  [takeValueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz) (EOKeyValueCoding)

---

### unableToSetNullForKey

`public static void unableToSetNullForKey(
Object anObject,
String key)`

Throws an IllegalArgumentException.

__See
Also:__  [unableToSetNullForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpovxgcytmmvkg6u3forhhk3dmizxxes3fpe) (EOKeyValueCoding)

---

### valueForKey

`public static Object valueForKey(
Object anObject,
String key)`

Returns the value for the property identified
by _key,_ invoking [handleQueryWithUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6s3fpflgc3dvmvbw6zdjnzts4u3vobyg64tuf5ugc3tenrsvc5lfoj4vo2lunbkw4ytpovxgis3fpe) if the
receiver doesn't recognize _key._
The default implementation works as follows:

1. Searches
   for a public accessor method based on _key._
   For example, with a key of "lastName", `valueForKey`looks
   for a method named getLastName or lastName.
2. If a public accessor method isn't found, searches for a
   private accessor method based on _key_ (a method
   preceded by an underbar). For example, with a key of "lastName", `valueForKey` looks
   for a method named _getLastName or _lastName.
3. If an accessor method isn't found and the static method [accessInstanceVariablesDirectly](EOCustomObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3von2g63kpmjvgky3uf5qwgy3fonzus3ttorqw4y3fkzqxe2lbmjwgk42enfzgky3unr4q) in _anObject_'s
   class returns `true`, `valueForKey` searches
   for an instance variable based on _key_ and
   returns its value directly. For the key "lastName", this would
   be _lastName or lastName.

__See
Also:__  [valueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe) (EOKeyValueCoding)

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
