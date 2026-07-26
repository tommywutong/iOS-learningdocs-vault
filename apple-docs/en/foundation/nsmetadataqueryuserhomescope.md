---
title: NSMetadataQueryUserHomeScope
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataqueryuserhomescope
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataqueryuserhomescope'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataqueryuserhomescope.json'
content_hash: 'sha256:17176ea2111f38df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMetadataQueryUserHomeScope

<sub>Global Variable</sub>

Search the user’s home directory.

<sub>macOS</sub>

```swift
let NSMetadataQueryUserHomeScope: String
```

## See Also

### Constants

- [NSMetadataQueryLocalComputerScope](nsmetadataquerylocalcomputerscope.md) — Search all local mounted volumes, including the user home directory. The user’s home directory is searched even if it is a remote volume.
- [NSMetadataQueryNetworkScope](nsmetadataquerynetworkscope.md) — Search all user-mounted remote volumes.
- [NSMetadataQueryUbiquitousDocumentsScope](nsmetadataqueryubiquitousdocumentsscope.md) — Search all files in the `Documents` directories of the app’s iCloud container directories.
- [NSMetadataQueryUbiquitousDataScope](nsmetadataqueryubiquitousdatascope.md) — Search all files not in the `Documents` directories of the app’s iCloud container directories.
- [NSMetadataQueryAccessibleUbiquitousExternalDocumentsScope](nsmetadataqueryaccessibleubiquitousexternaldocumentsscope.md) — Search for documents outside the app’s container. This search can locate iCloud documents that the user previously opened using a document picker view controller. This lets your app access the documents again without requiring direct user interaction. The result’s [NSMetadataItemURLKey](nsmetadataitemurlkey.md) attributes return security-scoped NSURLs. For more information on working with security-scoped URLs, see [Security-Scoped URLs](nsurl.md#Security-Scoped-URLs) in [NSURL](nsurl.md).
- [NSMetadataQueryIndexedLocalComputerScope](nsmetadataqueryindexedlocalcomputerscope.md) — Search all indexed local mounted volumes including the current user’s home directory (even if the home directory is remote).
- [NSMetadataQueryIndexedNetworkScope](nsmetadataqueryindexednetworkscope.md) — Search all indexed user-mounted remote volumes.
