---
title: hash
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobjectprotocol/hash
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/hash'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/hash.json'
content_hash: 'sha256:ddacbf2bd8bd46f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# hash

<sub>Instance Property</sub>

Returns an integer that can be used as a table address in a hash table structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hash: Int { get }
```

## Return Value

An integer that can be used as a table address in a hash table structure.

## Discussion

If two objects are equal (as determined by the [- isEqual:](<isequal(__).md>) method), they must have the same hash value. This last point is particularly important if you define [hash](hash.md) in a subclass and intend to put instances of that subclass into a collection.

If a mutable object is added to a collection that uses hash values to determine the object’s position in the collection, the value returned by the [hash](hash.md) method of the object must not change while the object is in the collection. Therefore, either the [hash](hash.md) method must not rely on any of the object’s internal state information or you must make sure the object’s internal state information does not change while the object is in the collection. Thus, for example, a mutable dictionary can be put in a hash table but you must not change it while it is in there. (Note that it can be difficult to know whether or not a given object is in a collection.)

## See Also

### Identifying and Comparing Objects

- [- isEqual:](<isequal(__).md>) — Returns a Boolean value that indicates whether the receiver and a given object are equal.
- [- self](<self().md>) — Returns the receiver.
