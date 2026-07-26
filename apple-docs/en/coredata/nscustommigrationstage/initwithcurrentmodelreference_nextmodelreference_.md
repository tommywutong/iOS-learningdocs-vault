---
title: 'initWithCurrentModelReference:nextModelReference:'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nscustommigrationstage/initwithcurrentmodelreference:nextmodelreference:'
source_url: 'https://developer.apple.com/documentation/coredata/nscustommigrationstage/initwithcurrentmodelreference:nextmodelreference:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nscustommigrationstage/initwithcurrentmodelreference%3Anextmodelreference%3A.json'
content_hash: 'sha256:65ef09e56e88b910'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSCustomMigrationStage](../nscustommigrationstage.md)

# initWithCurrentModelReference:nextModelReference:

<sub>Instance Method</sub>

Creates a custom migration stage with the specified source and destination model references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithCurrentModelReference:(NSManagedObjectModelReference *) currentModel nextModelReference:(NSManagedObjectModelReference *) nextModel;
```

## Parameters

- `currentModel` — The reference that represents the migration’s source model.

- `nextModel` — The reference that represents the migration’s destination model.

## Return Value

An initialized custom migration stage, or `nil` if Core Data can’t create one.

## See Also

### Creating a custom migration stage

- [NSManagedObjectModelReference](../nsmanagedobjectmodelreference.md) — An object that describes a specific version of an object model.
