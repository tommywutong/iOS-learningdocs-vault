---
title: currentModel
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nscustommigrationstage/currentmodel
source_url: 'https://developer.apple.com/documentation/coredata/nscustommigrationstage/currentmodel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nscustommigrationstage/currentmodel.json'
content_hash: 'sha256:00e8df0fb30b74bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSCustomMigrationStage](../nscustommigrationstage.md)

# currentModel

<sub>Instance Property</sub>

The reference that represents the migration’s source model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currentModel: NSManagedObjectModelReference { get }
```

## Discussion

Core Data sets this property to the `currentModel` parameter you specify when creating the migration stage.

## See Also

### Accessing model references

- [nextModel](nextmodel.md) — The reference that represents the migration’s destination model.
