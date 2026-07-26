---
title: 'cloudIdentifiers(forLocalIdentifiers:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.13+（12.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/photos/phphotolibrary/cloudidentifiers(forlocalidentifiers:)'
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/cloudidentifiers(forlocalidentifiers:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/cloudidentifiers%28forlocalidentifiers%3A%29.json'
content_hash: 'sha256:d1ee0de7c117df40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# cloudIdentifiers(forLocalIdentifiers:)

<sub>Instance Method</sub>

Retrieves the equivalent iCloud identifiers for the list of local identifiers.

> [!warning] Deprecated
> Use [cloudIdentifierMappingsForLocalIdentifiers:](cloudidentifiermappingsforlocalidentifiers_.md) instead.

<sub>macOS</sub>

```swift
func cloudIdentifiers(forLocalIdentifiers localIdentifiers: [String]) -> [PHCloudIdentifier]
```

## Parameters

- `localIdentifiers` — The local identifiers for which to retrieve iCloud identifier equivalents.

## Return Value

The array of corresponding iCloud identifiers.

## Discussion

Retrieving iCloud identifiers can be an expensive operation, so you should perform this lookup sparingly. Instead, work with local identifiers and retrieve their iCloud identifier equivalents only once: either after loading from or before saving to persistent storage.

## See Also

### Converting Between Local and iCloud Identifiers

- [cloudIdentifierMappings(forLocalIdentifiers:)](<cloudidentifiermappings(forlocalidentifiers_).md>) — Retrieves the cloud identifier mappings for the list of local identifiers.
- [localIdentifierMappings(for:)](<localidentifiermappings(for_).md>) — Retrieves the local identifier mappings for the list of cloud identifiers.
- [PHCloudIdentifier](../phcloudidentifier.md) — An object that identifies an asset or collection that syncs through iCloud Photos.
- [- localIdentifiersForCloudIdentifiers:](<localidentifiers(for_).md>) — Retrieves the equivalent local identifiers for the list of iCloud identifiers. _(deprecated)_
- [PHLocalIdentifierNotFound](../phlocalidentifiernotfound.md) — A constant value that indicates that the system can’t resolve a local object from a global identifier. _(deprecated)_
