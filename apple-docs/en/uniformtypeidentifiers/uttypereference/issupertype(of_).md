---
title: 'isSupertype(of:)'
framework: Uniform Type Identifiers
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uniformtypeidentifiers/uttypereference/issupertype(of:)'
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/issupertype(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypereference/issupertype%28of%3A%29.json'
content_hash: 'sha256:d768b54d88f6e4af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTTypeReference](../uttypereference.md)

# isSupertype(of:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether a type is lower in a hierarchy than the type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isSupertype(of type: UTType) -> Bool
```

## Parameters

- `type` — A [UTType](../uttype-swift.struct.md) instance.

## Return Value

[true](../../swift/true.md) if `type` directly or indirectly conforms to the type, but returns [false](../../swift/false.md) if it’s equal to the type.

## See Also

### Checking a type’s relationship to another type

- [supertypes](../uttype-swift.struct/supertypes.md) — The set of types the type directly or indirectly conforms to.
- [- conformsToType:](<conforms(to_).md>) — Returns a Boolean value that indicates whether a type conforms to the type.
- [- isSubtypeOfType:](<issubtype(of_).md>) — Returns a Boolean value that indicates whether a type is higher in a hierarchy than the type.
