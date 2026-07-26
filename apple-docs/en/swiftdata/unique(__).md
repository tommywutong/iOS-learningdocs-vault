---
title: 'Unique(_:)'
framework: SwiftData
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/unique(_:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/unique(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/unique%28_%3A%29.json'
content_hash: 'sha256:e339127001467006'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# Unique(_:)

<sub>Macro</sub>

Specifies the key-paths that SwiftData uses to enforce the uniqueness of model instances.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@freestanding(declaration) macro Unique<T>(_ constraints: [PartialKeyPath<T>]...) where T : PersistentModel
```

## Parameters

- `constraints` — Arrays of model key-paths that form the unique constraints to apply to the enclosing model.

## Overview

If a model class contains attributes that you require to be unique across all persisted instances of that model, add the `Unique` macro to that model’s definition. You can specify a constraint on a single attribute, a compound constraint across multiple attributes, or any combination of the two.

> [!important] Important
> For relationship attributes, SwiftData only supports unique constraints on those that reference a single persistent model, rather than an array of persistent models.

The following example declares that every instance of `Person` has a unique `id`, and that no two instances of `Person` have the same `givenName` and `familyName`:

```swift
@Model
final class Person {
    // Declare any unique constraints as part of the model definition.
    #Unique<Person>([\.id], [\.givenName, \.familyName])

    var id: UUID
    var givenName: String
    var familyName: String

    init(id: UUID, givenName: String, familyName: String) {
        self.id = id
        self.givenName = givenName
        self.familyName = familyName
    }
}
```

## See Also

### Model definition

- [Model()](<model().md>) — Converts a Swift class into a stored model that’s managed by SwiftData.
- [Attribute(_:originalName:hashModifier:)](<attribute(__originalname_hashmodifier_).md>) — Specifies the custom behavior that SwiftData applies to the annotated property when managing the owning class.
- [Index(_:)](<index(__)-74ia2.md>) — Specifies the key-paths that SwiftData uses to create one or more binary indices for the associated model.
- [Index(_:)](<index(__)-7d4z0.md>) — Specifies the key-paths that SwiftData uses to create one or more indicies for the associated model, where each index is either binary or R-tree.
- [Defining data relationships with enumerations and model classes](defining-data-relationships-with-enumerations-and-model-classes.md) — Create relationships for static and dynamic data stored in your app.
- [Relationship(_:deleteRule:minimumModelCount:maximumModelCount:originalName:inverse:hashModifier:)](<relationship(__deleterule_minimummodelcount_maximummodelcount_originalname_inverse_hashmodifier_).md>) — Specifies the options that SwiftData needs to manage the annotated property as a relationship between two models.
- [Transient()](<transient().md>) — Tells SwiftData not to persist the annotated property when managing the owning class.
