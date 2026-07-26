---
title: 'init(migratingFrom:to:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+, Swift 5.8+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nscustommigrationstage/init(migratingfrom:to:)'
source_url: 'https://developer.apple.com/documentation/coredata/nscustommigrationstage/init(migratingfrom:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nscustommigrationstage/init%28migratingfrom%3Ato%3A%29.json'
content_hash: 'sha256:eb33ad975833618d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSCustomMigrationStage](../nscustommigrationstage.md)

# init(migratingFrom:to:)

<sub>Initializer</sub>

Creates a custom migration stage with the specified source and destination model references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(migratingFrom currentModel: NSManagedObjectModelReference, to nextModel: NSManagedObjectModelReference)
```

## Parameters

- `currentModel` — The reference that represents the migration’s source model.

- `nextModel` — The reference that represents the migration’s destination model.

## See Also

### Creating a custom migration stage

- [NSManagedObjectModelReference](../nsmanagedobjectmodelreference.md) — An object that describes a specific version of an object model.
