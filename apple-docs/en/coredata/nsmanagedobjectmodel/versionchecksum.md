---
title: versionChecksum
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectmodel/versionchecksum
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/versionchecksum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodel/versionchecksum.json'
content_hash: 'sha256:b2f0355c1863d660'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectModel](../nsmanagedobjectmodel.md)

# versionChecksum

<sub>Instance Property</sub>

The Base64-encoded 128-bit model version hash.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var versionChecksum: String { get }
```

## Discussion

This value is also available in the versioned model’s `VersionInfo.plist` file and in Xcode’s build log.

## See Also

### Versioning and migrating entities

- [versionIdentifiers](versionidentifiers.md) — The set of developer-defined version identifiers for the object model.
- [entityVersionHashesByName](entityversionhashesbyname.md) — The dictionary of the model’s entity names and their corresponding version hashes.
- [- isConfiguration:compatibleWithStoreMetadata:](<isconfiguration(withname_compatiblewithstoremetadata_).md>) — Returns a Boolean value that indicates whether a given configuration in the model is compatible with given metadata from a persistent store.
