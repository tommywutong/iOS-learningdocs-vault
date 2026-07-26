---
title: NSManagedObjectModelReference
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectmodelreference
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodelreference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodelreference.json'
content_hash: 'sha256:6ab7d77397f12657'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSManagedObjectModelReference

<sub>Class</sub>

An object that describes a specific version of an object model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSManagedObjectModelReference
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a reference

- [- initWithModel:versionChecksum:](<nsmanagedobjectmodelreference/init(model_versionchecksum_).md>) — Creates an object model reference for the specified model.
- [- initWithFileURL:versionChecksum:](<nsmanagedobjectmodelreference/init(fileurl_versionchecksum_).md>) — Creates an object model reference for the model at the specified file URL.
- [- initWithName:inBundle:versionChecksum:](<nsmanagedobjectmodelreference/init(name_in_versionchecksum_).md>) — Creates an object model reference for the named model in the specified bundle.
- [- initWithEntityVersionHashes:inBundle:versionChecksum:](<nsmanagedobjectmodelreference/init(entityversionhashes_in_versionchecksum_).md>) — Creates an object model reference with the entities corresponding to the specified entity version hashes.

### Resolving the model object

- [resolvedModel](nsmanagedobjectmodelreference/resolvedmodel.md) — The resolved object model.
- [versionChecksum](nsmanagedobjectmodelreference/versionchecksum.md) — The version checksum of the resolved model.

### Initializers

- [init(entityVersionHashes:inBundle:versionChecksum:)](<nsmanagedobjectmodelreference/init(entityversionhashes_inbundle_versionchecksum_).md>)
- [init(name:inBundle:versionChecksum:)](<nsmanagedobjectmodelreference/init(name_inbundle_versionchecksum_).md>)

## See Also

### Creating a custom migration stage

- [init(migratingFrom:to:)](<nscustommigrationstage/init(migratingfrom_to_).md>) — Creates a custom migration stage with the specified source and destination model references.
