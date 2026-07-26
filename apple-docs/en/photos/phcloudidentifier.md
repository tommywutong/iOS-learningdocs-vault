---
title: PHCloudIdentifier
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 10.13+, tvOS 15.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcloudidentifier
source_url: 'https://developer.apple.com/documentation/photos/phcloudidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcloudidentifier.json'
content_hash: 'sha256:1b0fc209a44a3a73'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHCloudIdentifier

<sub>Class</sub>

An object that identifies an asset or collection that syncs through iCloud Photos.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHCloudIdentifier
```

## Overview

A cloud identifier is a type of identifier that behaves like a local identifier. Use cloud identifiers to identify objects that sync across devices through iCloud Photos. You can store, sync, and use cloud identifiers with devices synced with an iCloud account. You’re also able to use secure coding to encode and decode cloud identifiers.

A local identifier is valid for referring to objects only in the context of a local device. These objects include [PHAsset](phasset.md), [PHAssetCollection](phassetcollection.md), and [PHCollectionList](phcollectionlist.md).

Because a cloud identifier is universal, you can use it on any iCloud-synced device. Convert the cloud identifier back to a local identifier and perform a fetch to find the equivalent object on that device. Perform batch lookups of identifiers using [localIdentifierMappingsForCloudIdentifiers:](phphotolibrary/localidentifiermappingsforcloudidentifiers_.md) and [cloudIdentifierMappingsForLocalIdentifiers:](phphotolibrary/cloudidentifiermappingsforlocalidentifiers_.md).

```swift
// Get the local identifier mappings for the cloud identifiers.
let identifierMappings = library.localIdentifierMappings(for: assetCloudIdentifiers)
```

Retrieving identifier mappings can be an expensive operation, so perform lookups sparingly. If a lookup fails, inspect the error property on [PHCloudIdentifierMapping](phcloudidentifiermapping.md) or [PHLocalIdentifierMapping](phlocalidentifiermapping.md) for details. See [Code](phphotoserror-swift.struct/code.md) for additional error details.

```swift
// Iterate over the cloud identifiers and add or handle missing local identifiers.
for cloudIdentifier in assetCloudIdentifiers {
    guard let identifierMapping = identifierMappings[cloudIdentifier] else {
        print("Failed to find a mapping for \(cloudIdentifier).")
        continue
    }

    // Track the local identifier if it exists.
    if let localIdentifier = identifierMapping.localIdentifier {
        localIdentifiers.append(localIdentifier)
    } else if let error = identifierMapping.error as? PHPhotosError {
        switch error.code {
        case .identifierNotFound:
            // Skip the missing or deleted assets.
            print("Failed to find the local identifier for \(cloudIdentifier). \(error.localizedDescription))")
        case .multipleIdentifiersFound:
            // Prompt the user to resolve the cloud identifier that matched multiple assets.
            print("Found multiple local identifiers for \(cloudIdentifier). \(error.localizedDescription)")
            if let selectedLocalIdentifier = promptUserForPotentialReplacement(with: error.userInfo[PHLocalIdentifiersErrorKey]) {
                localIdentifiers.append(selectedLocalIdentifier)
            }
        default:
            print("Encountered an unexpected error looking up the local identifier for \(cloudIdentifier). \(error.localizedDescription)")
        }
    }
}

// Fetch assets using the found identifiers.
let mappedAssets = PHAsset.fetchAssets(withLocalIdentifiers: localIdentifiers, 
                                       options: nil)
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Using Cloud Identifiers

- [- initWithStringValue:](<phcloudidentifier/init(stringvalue_).md>) — Deserializes a cloud identifier from its string value. _(deprecated)_
- [stringValue](phcloudidentifier/stringvalue.md) — A string version of the cloud identifier to use in serialization. _(deprecated)_
- [notFoundIdentifier](phcloudidentifier/notfound.md) — The global identifier used in an array slot for items that couldn’t be found. _(deprecated)_

### Initializers

- [- initWithArchivalStringValue:](<phcloudidentifier/init(archivalstringvalue_).md>) — Archival string can be used to serialize and deserialize the PHCloudIdentifier (Note the archival format is compatible with strings archived via the deprecated API `stringValue`)
- [init(coder:)](<phcloudidentifier/init(coder_).md>)

### Instance Properties

- [archivalStringValue](phcloudidentifier/archivalstringvalue.md)

## See Also

### Converting Between Local and iCloud Identifiers

- [cloudIdentifierMappings(forLocalIdentifiers:)](<phphotolibrary/cloudidentifiermappings(forlocalidentifiers_).md>) — Retrieves the cloud identifier mappings for the list of local identifiers.
- [localIdentifierMappings(for:)](<phphotolibrary/localidentifiermappings(for_).md>) — Retrieves the local identifier mappings for the list of cloud identifiers.
- [- cloudIdentifiersForLocalIdentifiers:](<phphotolibrary/cloudidentifiers(forlocalidentifiers_).md>) — Retrieves the equivalent iCloud identifiers for the list of local identifiers. _(deprecated)_
- [- localIdentifiersForCloudIdentifiers:](<phphotolibrary/localidentifiers(for_).md>) — Retrieves the equivalent local identifiers for the list of iCloud identifiers. _(deprecated)_
- [PHLocalIdentifierNotFound](phlocalidentifiernotfound.md) — A constant value that indicates that the system can’t resolve a local object from a global identifier. _(deprecated)_
