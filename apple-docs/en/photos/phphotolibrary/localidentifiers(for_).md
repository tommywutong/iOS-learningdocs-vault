---
title: 'localIdentifiers(for:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.13+（12.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/photos/phphotolibrary/localidentifiers(for:)'
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/localidentifiers(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/localidentifiers%28for%3A%29.json'
content_hash: 'sha256:8ced4f8dbb486442'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# localIdentifiers(for:)

<sub>Instance Method</sub>

Retrieves the equivalent local identifiers for the list of iCloud identifiers.

> [!warning] Deprecated
> Use [localIdentifierMappingsForCloudIdentifiers:](localidentifiermappingsforcloudidentifiers_.md) instead.

<sub>macOS</sub>

```swift
func localIdentifiers(for cloudIdentifiers: [PHCloudIdentifier]) -> [String]
```

## Parameters

- `cloudIdentifiers` — The iCloud identifiers for which to retrieve local identifier equivalents.

## Return Value

The array of corresponding iCloud identifiers.

## See Also

### Converting Between Local and iCloud Identifiers

- [cloudIdentifierMappings(forLocalIdentifiers:)](<cloudidentifiermappings(forlocalidentifiers_).md>) — Retrieves the cloud identifier mappings for the list of local identifiers.
- [localIdentifierMappings(for:)](<localidentifiermappings(for_).md>) — Retrieves the local identifier mappings for the list of cloud identifiers.
- [PHCloudIdentifier](../phcloudidentifier.md) — An object that identifies an asset or collection that syncs through iCloud Photos.
- [- cloudIdentifiersForLocalIdentifiers:](<cloudidentifiers(forlocalidentifiers_).md>) — Retrieves the equivalent iCloud identifiers for the list of local identifiers. _(deprecated)_
- [PHLocalIdentifierNotFound](../phlocalidentifiernotfound.md) — A constant value that indicates that the system can’t resolve a local object from a global identifier. _(deprecated)_
