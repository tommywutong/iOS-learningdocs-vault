---
title: PHLocalIdentifierNotFound
framework: Photos
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.13+（12.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/photos/phlocalidentifiernotfound
source_url: 'https://developer.apple.com/documentation/photos/phlocalidentifiernotfound'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlocalidentifiernotfound.json'
content_hash: 'sha256:1760f920ef638224'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHLocalIdentifierNotFound

<sub>Global Variable</sub>

A constant value that indicates that the system can’t resolve a local object from a global identifier.

> [!warning] Deprecated
> Use [PHLocalIdentifierMapping](phlocalidentifiermapping.md) instead.

<sub>macOS</sub>

```swift
let PHLocalIdentifierNotFound: String
```

## See Also

### Converting Between Local and iCloud Identifiers

- [cloudIdentifierMappings(forLocalIdentifiers:)](<phphotolibrary/cloudidentifiermappings(forlocalidentifiers_).md>) — Retrieves the cloud identifier mappings for the list of local identifiers.
- [localIdentifierMappings(for:)](<phphotolibrary/localidentifiermappings(for_).md>) — Retrieves the local identifier mappings for the list of cloud identifiers.
- [PHCloudIdentifier](phcloudidentifier.md) — An object that identifies an asset or collection that syncs through iCloud Photos.
- [- cloudIdentifiersForLocalIdentifiers:](<phphotolibrary/cloudidentifiers(forlocalidentifiers_).md>) — Retrieves the equivalent iCloud identifiers for the list of local identifiers. _(deprecated)_
- [- localIdentifiersForCloudIdentifiers:](<phphotolibrary/localidentifiers(for_).md>) — Retrieves the equivalent local identifiers for the list of iCloud identifiers. _(deprecated)_
