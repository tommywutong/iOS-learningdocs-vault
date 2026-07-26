---
title: entityVersionHashesByName
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectmodel/entityversionhashesbyname
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/entityversionhashesbyname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodel/entityversionhashesbyname.json'
content_hash: 'sha256:5c91871db355921e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectModel](../nsmanagedobjectmodel.md)

# entityVersionHashesByName

<sub>Instance Property</sub>

The dictionary of the model’s entity names and their corresponding version hashes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var entityVersionHashesByName: [String : Data] { get }
```

## Discussion

Core Data use the dictionary of version hash information is to determine schema compatibility.

## See Also

### Versioning and migrating entities

- [versionChecksum](versionchecksum.md) — The Base64-encoded 128-bit model version hash.
- [versionIdentifiers](versionidentifiers.md) — The set of developer-defined version identifiers for the object model.
- [- isConfiguration:compatibleWithStoreMetadata:](<isconfiguration(withname_compatiblewithstoremetadata_).md>) — Returns a Boolean value that indicates whether a given configuration in the model is compatible with given metadata from a persistent store.
