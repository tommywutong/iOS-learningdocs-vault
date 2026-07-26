---
title: KeyPath
framework: Swift
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/keypath
source_url: 'https://developer.apple.com/documentation/swift/keypath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keypath.json'
content_hash: 'sha256:6970197dd28967be'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# KeyPath

<sub>Class</sub>

A key path from a specific root type to a specific resulting value type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class KeyPath<Root, Value>
```

## Overview

The most common way to make an instance of this type is by using a key-path expression like `\SomeClass.someProperty`. For more information, see [Key-Path Expressions](https://docs.swift.org/swift-book/ReferenceManual/Expressions.html#ID563) in _[The Swift Programming Language](https://docs.swift.org/swift-book/)_.

## Relationships

- **Inherits From**: [PartialKeyPath](partialkeypath.md)

- **Inherited By**: [WritableKeyPath](writablekeypath.md)

- **Conforms To**: [CustomDebugStringConvertible](customdebugstringconvertible.md), [Equatable](equatable.md), [Hashable](hashable.md)

## See Also

### Key Paths

- [PartialKeyPath](partialkeypath.md) — A partially type-erased key path, from a concrete root type to any resulting value type.
- [AnyKeyPath](anykeypath.md) — A type-erased key path, from any root type to any resulting value type.
