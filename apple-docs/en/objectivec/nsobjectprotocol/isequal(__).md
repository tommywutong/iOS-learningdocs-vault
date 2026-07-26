---
title: 'isEqual(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobjectprotocol/isequal(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/isequal(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/isequal%28_%3A%29.json'
content_hash: 'sha256:76da95a58aac7d42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# isEqual(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the receiver and a given object are equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isEqual(_ object: Any?) -> Bool
```

## Parameters

- `object` — The object to be compared to the receiver. May be `nil`, in which case this method returns [NO](../no.md).

## Return Value

[YES](../yes.md) if the receiver and `anObject` are equal, otherwise [NO](../no.md).

## Discussion

This method defines what it means for instances to be equal. For example, a container object might define two containers as equal if their corresponding objects all respond [YES](../yes.md) to an [- isEqual:](<isequal(__).md>) request. See the [NSData](../../foundation/nsdata.md), [NSDictionary](../../foundation/nsdictionary.md), [NSArray](../../foundation/nsarray.md), and [NSString](../../foundation/nsstring.md) class specifications for examples of the use of this method.

If two objects are equal, they must have the same hash value. This last point is particularly important if you define [- isEqual:](<isequal(__).md>) in a subclass and intend to put instances of that subclass into a collection. Make sure you also define [hash](hash.md) in your subclass.

## See Also

### Identifying and Comparing Objects

- [hash](hash.md) — Returns an integer that can be used as a table address in a hash table structure.
- [- self](<self().md>) — Returns the receiver.
