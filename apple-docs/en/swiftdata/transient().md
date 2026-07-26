---
title: Transient()
framework: SwiftData
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/transient()
source_url: 'https://developer.apple.com/documentation/swiftdata/transient()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/transient%28%29.json'
content_hash: 'sha256:4725591785e3c434'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# Transient()

<sub>Macro</sub>

Tells SwiftData not to persist the annotated property when managing the owning class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@attached(peer) macro Transient()
```

## Overview

If your model class has one or more stored properties that you want to omit from writes to the persistent storage, annotate each of those properties with the `@Transient` macro.

> [!note] Note
> By default, SwiftData considers any computed properties to be transient. You don’t need to explicitly annotate those properties.

```swift
@Model
class RemoteImage {
    var sourceURL: URL
    var data: Data
    
    @Transient
    var isDownloading = false
    
    init(sourceURL: URL, data: Data = Data(), isDownloading: Bool) {
        self.sourceURL = sourceURL
        self.data = data
        self.isDownloading = isDownloading
    }
}
```

Unless the type of the annotated property is an optional, the `@Transient` macro requires you to provide a default value. This constraint enables SwiftData to successfully materialize instances of the enclosing model class when running fetches.

## See Also

### Model definition

- [Model()](<model().md>) — Converts a Swift class into a stored model that’s managed by SwiftData.
- [Attribute(_:originalName:hashModifier:)](<attribute(__originalname_hashmodifier_).md>) — Specifies the custom behavior that SwiftData applies to the annotated property when managing the owning class.
- [Unique(_:)](<unique(__).md>) — Specifies the key-paths that SwiftData uses to enforce the uniqueness of model instances.
- [Index(_:)](<index(__)-74ia2.md>) — Specifies the key-paths that SwiftData uses to create one or more binary indices for the associated model.
- [Index(_:)](<index(__)-7d4z0.md>) — Specifies the key-paths that SwiftData uses to create one or more indicies for the associated model, where each index is either binary or R-tree.
- [Defining data relationships with enumerations and model classes](defining-data-relationships-with-enumerations-and-model-classes.md) — Create relationships for static and dynamic data stored in your app.
- [Relationship(_:deleteRule:minimumModelCount:maximumModelCount:originalName:inverse:hashModifier:)](<relationship(__deleterule_minimummodelcount_maximummodelcount_originalname_inverse_hashmodifier_).md>) — Specifies the options that SwiftData needs to manage the annotated property as a relationship between two models.
