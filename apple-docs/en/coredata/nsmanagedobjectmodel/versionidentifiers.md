---
title: versionIdentifiers
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectmodel/versionidentifiers
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/versionidentifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodel/versionidentifiers.json'
content_hash: 'sha256:eaa5278f4afd4b31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectModel](../nsmanagedobjectmodel.md)

# versionIdentifiers

<sub>Instance Property</sub>

The set of developer-defined version identifiers for the object model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var versionIdentifiers: Set<AnyHashable> { get set }
```

## Discussion

Merged models return the combined collection of identifiers. The Core Data framework does not assign a default identifier to object models, nor does it depend on this value at runtime. For models you create in Xcode, set this value in the model inspector.

Use this value when debugging to help determine the models that Core Data merges to create the merged model.

## See Also

### Versioning and migrating entities

- [versionChecksum](versionchecksum.md) — The Base64-encoded 128-bit model version hash.
- [entityVersionHashesByName](entityversionhashesbyname.md) — The dictionary of the model’s entity names and their corresponding version hashes.
- [- isConfiguration:compatibleWithStoreMetadata:](<isconfiguration(withname_compatiblewithstoremetadata_).md>) — Returns a Boolean value that indicates whether a given configuration in the model is compatible with given metadata from a persistent store.
