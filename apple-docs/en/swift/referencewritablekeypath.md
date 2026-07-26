---
title: ReferenceWritableKeyPath
framework: Swift
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/referencewritablekeypath
source_url: 'https://developer.apple.com/documentation/swift/referencewritablekeypath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/referencewritablekeypath.json'
content_hash: 'sha256:3df858f5369c5257'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ReferenceWritableKeyPath

<sub>Class</sub>

A key path that supports reading from and writing to the resulting value with reference semantics.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class ReferenceWritableKeyPath<Root, Value>
```

## Relationships

- **Inherits From**: [WritableKeyPath](writablekeypath.md)

- **Conforms To**: [CustomDebugStringConvertible](customdebugstringconvertible.md), [Equatable](equatable.md), [Hashable](hashable.md)

## See Also

### Writable Key Paths

- [WritableKeyPath](writablekeypath.md) — A key path that supports reading from and writing to the resulting value.
