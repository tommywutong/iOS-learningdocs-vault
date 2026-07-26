---
title: AnyKeyPath
framework: Swift
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/anykeypath
source_url: 'https://developer.apple.com/documentation/swift/anykeypath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anykeypath.json'
content_hash: 'sha256:42867864387feaf1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# AnyKeyPath

<sub>Class</sub>

A type-erased key path, from any root type to any resulting value type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AnyKeyPath
```

## Relationships

- **Inherited By**: [PartialKeyPath](partialkeypath.md)

- **Conforms To**: [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [Equatable](equatable.md), [Escapable](escapable.md), [Hashable](hashable.md)

## Topics

### Type Properties

- [rootType](anykeypath/roottype.md) — The root type for this key path.
- [valueType](anykeypath/valuetype.md) — The value type for this key path.

### Default Implementations

- [CustomDebugStringConvertible Implementations](anykeypath/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](anykeypath/equatable-implementations.md)
- [Hashable Implementations](anykeypath/hashable-implementations.md)

## See Also

### Key Paths

- [KeyPath](keypath.md) — A key path from a specific root type to a specific resulting value type.
- [PartialKeyPath](partialkeypath.md) — A partially type-erased key path, from a concrete root type to any resulting value type.
