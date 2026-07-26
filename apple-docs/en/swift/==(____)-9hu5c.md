---
title: '==(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/==(_:_:)-9hu5c'
source_url: 'https://developer.apple.com/documentation/swift/==(_:_:)-9hu5c'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/%3D%3D%28_%3A_%3A%29-9hu5c.json'
content_hash: 'sha256:28a2e3ca9c68f58f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ==(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether the two arguments are equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func == <T>(lhs: T, rhs: T) -> Bool where T : RawRepresentable, T.RawValue : Equatable
```

## Parameters

- `lhs` — A raw-representable instance.

- `rhs` — A second raw-representable instance.

## See Also

### Comparing Values

- [!=(_:_:)](<!=(____)-9wy5n.md>) — Returns a Boolean value indicating whether the two arguments are not equal.
- [!=(_:_:)](<!=(____)-8pggn.md>) — Returns a Boolean value indicating whether the two arguments are not equal.
