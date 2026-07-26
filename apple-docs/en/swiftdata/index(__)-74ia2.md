---
title: 'Index(_:)'
framework: SwiftData
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/index(_:)-74ia2'
source_url: 'https://developer.apple.com/documentation/swiftdata/index(_:)-74ia2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/index%28_%3A%29-74ia2.json'
content_hash: 'sha256:040f249430e123f9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# Index(_:)

<sub>Macro</sub>

Specifies the key-paths that SwiftData uses to create one or more binary indices for the associated model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@freestanding(declaration) macro Index<T>(_ indices: [PartialKeyPath<T>]...) where T : PersistentModel
```

## See Also

### Model definition

- [Model()](<model().md>) — Converts a Swift class into a stored model that’s managed by SwiftData.
- [Attribute(_:originalName:hashModifier:)](<attribute(__originalname_hashmodifier_).md>) — Specifies the custom behavior that SwiftData applies to the annotated property when managing the owning class.
- [Unique(_:)](<unique(__).md>) — Specifies the key-paths that SwiftData uses to enforce the uniqueness of model instances.
- [Index(_:)](<index(__)-7d4z0.md>) — Specifies the key-paths that SwiftData uses to create one or more indicies for the associated model, where each index is either binary or R-tree.
- [Defining data relationships with enumerations and model classes](defining-data-relationships-with-enumerations-and-model-classes.md) — Create relationships for static and dynamic data stored in your app.
- [Relationship(_:deleteRule:minimumModelCount:maximumModelCount:originalName:inverse:hashModifier:)](<relationship(__deleterule_minimummodelcount_maximummodelcount_originalname_inverse_hashmodifier_).md>) — Specifies the options that SwiftData needs to manage the annotated property as a relationship between two models.
- [Transient()](<transient().md>) — Tells SwiftData not to persist the annotated property when managing the owning class.
