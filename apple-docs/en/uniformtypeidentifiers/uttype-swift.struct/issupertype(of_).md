---
title: 'isSupertype(of:)'
framework: Uniform Type Identifiers
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uniformtypeidentifiers/uttype-swift.struct/issupertype(of:)'
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/issupertype(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/issupertype%28of%3A%29.json'
content_hash: 'sha256:1b3d6fa847c69887'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

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

- [supertypes](supertypes.md) — The set of types the type directly or indirectly conforms to.
- [conforms(to:)](<conforms(to_).md>) — Returns a Boolean value that indicates whether a type conforms to the type.
- [isSubtype(of:)](<issubtype(of_).md>) — Returns a Boolean value that indicates whether a type is higher in a hierarchy than the type.
- [Navigating Hierarchical Data Using Outline and Split Views](../../appkit/navigating-hierarchical-data-using-outline-and-split-views.md) — Build a structured user interface that simplifies navigation in your app.
