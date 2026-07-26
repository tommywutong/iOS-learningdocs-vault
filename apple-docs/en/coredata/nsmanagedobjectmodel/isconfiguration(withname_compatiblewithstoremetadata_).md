---
title: 'isConfiguration(withName:compatibleWithStoreMetadata:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectmodel/isconfiguration(withname:compatiblewithstoremetadata:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/isconfiguration(withname:compatiblewithstoremetadata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodel/isconfiguration%28withname%3Acompatiblewithstoremetadata%3A%29.json'
content_hash: 'sha256:77e9c5c19bcf4b74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectModel](../nsmanagedobjectmodel.md)

# isConfiguration(withName:compatibleWithStoreMetadata:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether a given configuration in the model is compatible with given metadata from a persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isConfiguration(withName configuration: String?, compatibleWithStoreMetadata metadata: [String : Any]) -> Bool
```

## Parameters

- `configuration` — The name of a configuration in the receiver. Pass `nil` to specify no configuration.

- `metadata` — Metadata for a persistent store.

## Return Value

[true](../../swift/true.md) if the configuration in the receiver specified by `configuration` is compatible with the store metadata given by `metadata`, otherwise [false](../../swift/false.md).

## Discussion

This method compares the version information in the store metadata with the entity versions of a given configuration. For information on specific differences, use [entityVersionHashesByName](entityversionhashesbyname.md) and perform an entity-by-entity comparison.

## See Also

### Versioning and migrating entities

- [versionChecksum](versionchecksum.md) — The Base64-encoded 128-bit model version hash.
- [versionIdentifiers](versionidentifiers.md) — The set of developer-defined version identifiers for the object model.
- [entityVersionHashesByName](entityversionhashesbyname.md) — The dictionary of the model’s entity names and their corresponding version hashes.
