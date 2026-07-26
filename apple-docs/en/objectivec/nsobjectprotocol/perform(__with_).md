---
title: 'perform(_:with:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 1.0+, iPadOS 1.0+, Mac Catalyst 1.0+, macOS 10.0+, tvOS 1.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobjectprotocol/perform(_:with:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/perform(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/perform%28_%3Awith%3A%29.json'
content_hash: 'sha256:c40989070eb12d20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# perform(_:with:)

<sub>Instance Method</sub>

Sends a message to the receiver with an object as the argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func perform(_ aSelector: Selector!, with object: Any!) -> Unmanaged<AnyObject>!
```

## Parameters

- `aSelector` — A selector identifying the message to send. If `aSelector` is `NULL`, an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) is raised.

- `object` — An object that is the sole argument of the message.

## Return Value

An object that is the result of the message.

## Discussion

This method is the same as [- performSelector:](<perform(__).md>) except that you can supply an argument for `aSelector`. `aSelector` should identify a method that takes a single argument of type id. For methods with other argument types and return values, use [NSInvocation](../../foundation/nsinvocation.md).

## See Also

### Related Documentation

- [- methodForSelector:](<../nsobject-swift.class/method(for_).md>) — Locates and returns the address of the receiver’s implementation of a method so it can be called as a function.

### Sending Messages

- [- performSelector:](<perform(__).md>) — Sends a specified message to the receiver and returns the result of the message.
- [- performSelector:withObject:withObject:](<perform(__with_with_).md>) — Sends a message to the receiver with two objects as arguments.
