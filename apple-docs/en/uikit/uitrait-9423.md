---
title: UITrait
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitrait-9423
source_url: 'https://developer.apple.com/documentation/uikit/uitrait-9423'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitrait-9423.json'
content_hash: 'sha256:e9a2b26698ad1e1a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITrait

<sub>Type Alias</sub>

A type representing a trait in a trait collection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias UITrait = any UITraitDefinition.Type
```

## Discussion

The type of a trait serves as a key to uniquely identify a trait in a trait collection. The [subscript(_:)](<uitraitcollection/subscript(__)-96v58.md>) method of [UITraitCollection](uitraitcollection.md) and [registerForTraitChanges(_:handler:)](<uitraitchangeobservable-67e94/registerfortraitchanges(__handler_).md>) are two examples that take trait types to identify traits in the collection.

## See Also

### Custom traits

- [Providing data to the view hierarchy with custom traits](providing-data-to-the-view-hierarchy-with-custom-traits.md) — Share data that needs to flow hierarchically across multiple levels of your view hierarchy.
- [UIMutableTraits](uimutabletraits-13ja5.md) — A mutable container of traits.
- [UITraitDefinition](uitraitdefinition-64c15.md) — A type representing a trait in a trait collection.
