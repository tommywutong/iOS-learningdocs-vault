---
title: NSMetadataQueryNetworkScope
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataquerynetworkscope
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataquerynetworkscope'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataquerynetworkscope.json'
content_hash: 'sha256:827c1e88608e97dc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMetadataQueryNetworkScope

<sub>Global Variable</sub>

Search all user-mounted remote volumes.

<sub>macOS</sub>

```swift
let NSMetadataQueryNetworkScope: String
```

## See Also

### Constants

- [NSMetadataQueryUserHomeScope](nsmetadataqueryuserhomescope.md) — Search the user’s home directory.
- [NSMetadataQueryLocalComputerScope](nsmetadataquerylocalcomputerscope.md) — Search all local mounted volumes, including the user home directory. The user’s home directory is searched even if it is a remote volume.
- [NSMetadataQueryUbiquitousDocumentsScope](nsmetadataqueryubiquitousdocumentsscope.md) — Search all files in the `Documents` directories of the app’s iCloud container directories.
- [NSMetadataQueryUbiquitousDataScope](nsmetadataqueryubiquitousdatascope.md) — Search all files not in the `Documents` directories of the app’s iCloud container directories.
- [NSMetadataQueryAccessibleUbiquitousExternalDocumentsScope](nsmetadataqueryaccessibleubiquitousexternaldocumentsscope.md) — Search for documents outside the app’s container. This search can locate iCloud documents that the user previously opened using a document picker view controller. This lets your app access the documents again without requiring direct user interaction. The result’s [NSMetadataItemURLKey](nsmetadataitemurlkey.md) attributes return security-scoped NSURLs. For more information on working with security-scoped URLs, see [Security-Scoped URLs](nsurl.md#Security-Scoped-URLs) in [NSURL](nsurl.md).
- [NSMetadataQueryIndexedLocalComputerScope](nsmetadataqueryindexedlocalcomputerscope.md) — Search all indexed local mounted volumes including the current user’s home directory (even if the home directory is remote).
- [NSMetadataQueryIndexedNetworkScope](nsmetadataqueryindexednetworkscope.md) — Search all indexed user-mounted remote volumes.
