---
title: supertypes
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/supertypes
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/supertypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/supertypes.json'
content_hash: 'sha256:a18bc6dacf910c9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# supertypes

<sub>Instance Property</sub>

The set of types the type directly or indirectly conforms to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var supertypes: Set<UTType> { get }
```

## See Also

### Checking a type’s relationship to another type

- [conforms(to:)](<conforms(to_).md>) — Returns a Boolean value that indicates whether a type conforms to the type.
- [isSubtype(of:)](<issubtype(of_).md>) — Returns a Boolean value that indicates whether a type is higher in a hierarchy than the type.
- [isSupertype(of:)](<issupertype(of_).md>) — Returns a Boolean value that indicates whether a type is lower in a hierarchy than the type.
- [Navigating Hierarchical Data Using Outline and Split Views](../../appkit/navigating-hierarchical-data-using-outline-and-split-views.md) — Build a structured user interface that simplifies navigation in your app.
