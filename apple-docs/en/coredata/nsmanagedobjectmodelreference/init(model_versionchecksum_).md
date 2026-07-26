---
title: 'init(model:versionChecksum:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectmodelreference/init(model:versionchecksum:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodelreference/init(model:versionchecksum:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodelreference/init%28model%3Aversionchecksum%3A%29.json'
content_hash: 'sha256:ba4c9a74c5d8e771'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectModelReference](../nsmanagedobjectmodelreference.md)

# init(model:versionChecksum:)

<sub>Initializer</sub>

Creates an object model reference for the specified model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(model: NSManagedObjectModel, versionChecksum: String)
```

## Parameters

- `model` — The managed object model.

- `versionChecksum` — The checksum of the object model’s version.

## Discussion

To determine an object model’s version checksum, use its [versionChecksum](../nsmanagedobjectmodel/versionchecksum.md) property. Alternatively, you can find the checksum in the versioned model’s `VersionInfo.plist` file or in Xcode’s build log.

## See Also

### Creating a reference

- [- initWithFileURL:versionChecksum:](<init(fileurl_versionchecksum_).md>) — Creates an object model reference for the model at the specified file URL.
- [- initWithName:inBundle:versionChecksum:](<init(name_in_versionchecksum_).md>) — Creates an object model reference for the named model in the specified bundle.
- [- initWithEntityVersionHashes:inBundle:versionChecksum:](<init(entityversionhashes_in_versionchecksum_).md>) — Creates an object model reference with the entities corresponding to the specified entity version hashes.
