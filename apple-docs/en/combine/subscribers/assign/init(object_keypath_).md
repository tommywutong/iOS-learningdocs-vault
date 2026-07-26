---
title: 'init(object:keyPath:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/subscribers/assign/init(object:keypath:)'
source_url: 'https://developer.apple.com/documentation/combine/subscribers/assign/init(object:keypath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscribers/assign/init%28object%3Akeypath%3A%29.json'
content_hash: 'sha256:1741657480739c08'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Subscribers](../../subscribers.md) · [Assign](../assign.md)

# init(object:keyPath:)

<sub>Initializer</sub>

Creates a subscriber to assign the value of a property indicated by a key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(object: Root, keyPath: ReferenceWritableKeyPath<Root, Input>)
```

## Parameters

- `object` — The object that contains the property. The subscriber assigns the object’s property every time it receives a new value.

- `keyPath` — A key path that indicates the property to assign. See [Key-Path Expression](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/Expressions.html#//apple_ref/doc/uid/TP40014097-CH32-ID563) in _The Swift Programming Language_ to learn how to use key paths to specify a property of an object.
