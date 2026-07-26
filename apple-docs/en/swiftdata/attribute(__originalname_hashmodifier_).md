---
title: 'Attribute(_:originalName:hashModifier:)'
framework: SwiftData
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/attribute(_:originalname:hashmodifier:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/attribute(_:originalname:hashmodifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/attribute%28_%3Aoriginalname%3Ahashmodifier%3A%29.json'
content_hash: 'sha256:ab03203969bb028a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# Attribute(_:originalName:hashModifier:)

<sub>Macro</sub>

Specifies the custom behavior that SwiftData applies to the annotated property when managing the owning class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@attached(peer) macro Attribute(_ options: Schema.Attribute.Option..., originalName: String? = nil, hashModifier: String? = nil)
```

## Parameters

- `options` — A list of options to apply to the attached property to customize its behavior. For possible values, see [Option](schema/attribute/option.md).

- `originalName` — The previous name of the attribute, if it’s different to the one in the current schema version. The default value is `nil`.

- `hashModifier` — A unique hash value that represents the most recent version of the attached property. The default value is `nil`.

## Overview

The framework’s default behavior for managing a model class’s stored properties is suitable for most use cases. However, if you need to alter the persistence behavior of a particular property, annotate it with the `@Attribute` macro. For example, you may want to avoid conflicts in your model data by specifying that an attribute’s value is unique across all instances of that model.

```swift
@Model
class RemoteImage {
    @Attribute(.unique) var sourceURL: URL
    var data: Data
    
    init(sourceURL: URL, data: Data = Data()) {
        self.sourceURL = sourceURL
        self.data = data
    }
}
```

## See Also

### Model definition

- [Model()](<model().md>) — Converts a Swift class into a stored model that’s managed by SwiftData.
- [Unique(_:)](<unique(__).md>) — Specifies the key-paths that SwiftData uses to enforce the uniqueness of model instances.
- [Index(_:)](<index(__)-74ia2.md>) — Specifies the key-paths that SwiftData uses to create one or more binary indices for the associated model.
- [Index(_:)](<index(__)-7d4z0.md>) — Specifies the key-paths that SwiftData uses to create one or more indicies for the associated model, where each index is either binary or R-tree.
- [Defining data relationships with enumerations and model classes](defining-data-relationships-with-enumerations-and-model-classes.md) — Create relationships for static and dynamic data stored in your app.
- [Relationship(_:deleteRule:minimumModelCount:maximumModelCount:originalName:inverse:hashModifier:)](<relationship(__deleterule_minimummodelcount_maximummodelcount_originalname_inverse_hashmodifier_).md>) — Specifies the options that SwiftData needs to manage the annotated property as a relationship between two models.
- [Transient()](<transient().md>) — Tells SwiftData not to persist the annotated property when managing the owning class.
