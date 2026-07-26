---
title: nextModel
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nscustommigrationstage/nextmodel
source_url: 'https://developer.apple.com/documentation/coredata/nscustommigrationstage/nextmodel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nscustommigrationstage/nextmodel.json'
content_hash: 'sha256:3813f7d4f8c9cf64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSCustomMigrationStage](../nscustommigrationstage.md)

# nextModel

<sub>Instance Property</sub>

The reference that represents the migration’s destination model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nextModel: NSManagedObjectModelReference { get }
```

## Discussion

Core Data sets this property to the `nextModel` parameter you specify when creating the migration stage.

## See Also

### Accessing model references

- [currentModel](currentmodel.md) — The reference that represents the migration’s source model.
