---
title: NSMetadataQueryUbiquitousDocumentsScope
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataqueryubiquitousdocumentsscope
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataqueryubiquitousdocumentsscope'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataqueryubiquitousdocumentsscope.json'
content_hash: 'sha256:2d339de7326e7823'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMetadataQueryUbiquitousDocumentsScope

<sub>Global Variable</sub>

Search all files in the `Documents` directories of the app’s iCloud container directories.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSMetadataQueryUbiquitousDocumentsScope: String
```

## See Also

### Constants

- [NSMetadataQueryUserHomeScope](nsmetadataqueryuserhomescope.md) — Search the user’s home directory.
- [NSMetadataQueryLocalComputerScope](nsmetadataquerylocalcomputerscope.md) — Search all local mounted volumes, including the user home directory. The user’s home directory is searched even if it is a remote volume.
- [NSMetadataQueryNetworkScope](nsmetadataquerynetworkscope.md) — Search all user-mounted remote volumes.
- [NSMetadataQueryUbiquitousDataScope](nsmetadataqueryubiquitousdatascope.md) — Search all files not in the `Documents` directories of the app’s iCloud container directories.
- [NSMetadataQueryAccessibleUbiquitousExternalDocumentsScope](nsmetadataqueryaccessibleubiquitousexternaldocumentsscope.md) — Search for documents outside the app’s container. This search can locate iCloud documents that the user previously opened using a document picker view controller. This lets your app access the documents again without requiring direct user interaction. The result’s [NSMetadataItemURLKey](nsmetadataitemurlkey.md) attributes return security-scoped NSURLs. For more information on working with security-scoped URLs, see [Security-Scoped URLs](nsurl.md#Security-Scoped-URLs) in [NSURL](nsurl.md).
- [NSMetadataQueryIndexedLocalComputerScope](nsmetadataqueryindexedlocalcomputerscope.md) — Search all indexed local mounted volumes including the current user’s home directory (even if the home directory is remote).
- [NSMetadataQueryIndexedNetworkScope](nsmetadataqueryindexednetworkscope.md) — Search all indexed user-mounted remote volumes.
