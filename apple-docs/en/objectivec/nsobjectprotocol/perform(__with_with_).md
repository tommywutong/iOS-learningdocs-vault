---
title: 'perform(_:with:with:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 1.0+, iPadOS 1.0+, Mac Catalyst 1.0+, macOS 10.0+, tvOS 1.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobjectprotocol/perform(_:with:with:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/perform(_:with:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/perform%28_%3Awith%3Awith%3A%29.json'
content_hash: 'sha256:b0c617f5ba46e3da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# perform(_:with:with:)

<sub>Instance Method</sub>

Sends a message to the receiver with two objects as arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func perform(_ aSelector: Selector!, with object1: Any!, with object2: Any!) -> Unmanaged<AnyObject>!
```

## Parameters

- `aSelector` — A selector identifying the message to send. If `aSelector` is `NULL`, an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) is raised.

- `object1` — An object that is the first argument of the message.

- `object2` — An object that is the second argument of the message

## Return Value

An object that is the result of the message.

## Discussion

This method is the same as [- performSelector:](<perform(__).md>) except that you can supply two arguments for `aSelector`. `aSelector` should identify a method that can take two arguments of type id. For methods with other argument types and return values, use [NSInvocation](../../foundation/nsinvocation.md).

## See Also

### Related Documentation

- [- methodForSelector:](<../nsobject-swift.class/method(for_).md>) — Locates and returns the address of the receiver’s implementation of a method so it can be called as a function.

### Sending Messages

- [- performSelector:](<perform(__).md>) — Sends a specified message to the receiver and returns the result of the message.
- [- performSelector:withObject:](<perform(__with_).md>) — Sends a message to the receiver with an object as the argument.
