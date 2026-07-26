---
title: NSMetadataQueryAccessibleUbiquitousExternalDocumentsScope
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataqueryaccessibleubiquitousexternaldocumentsscope
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataqueryaccessibleubiquitousexternaldocumentsscope'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataqueryaccessibleubiquitousexternaldocumentsscope.json'
content_hash: 'sha256:93badea8f02c91a1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMetadataQueryAccessibleUbiquitousExternalDocumentsScope

<sub>Global Variable</sub>

Search for documents outside the app’s container. This search can locate iCloud documents that the user previously opened using a document picker view controller. This lets your app access the documents again without requiring direct user interaction. The result’s [NSMetadataItemURLKey](nsmetadataitemurlkey.md) attributes return security-scoped NSURLs. For more information on working with security-scoped URLs, see [Security-Scoped URLs](nsurl.md#Security-Scoped-URLs) in [NSURL](nsurl.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSMetadataQueryAccessibleUbiquitousExternalDocumentsScope: String
```

## See Also

### Constants

- [NSMetadataQueryUserHomeScope](nsmetadataqueryuserhomescope.md) — Search the user’s home directory.
- [NSMetadataQueryLocalComputerScope](nsmetadataquerylocalcomputerscope.md) — Search all local mounted volumes, including the user home directory. The user’s home directory is searched even if it is a remote volume.
- [NSMetadataQueryNetworkScope](nsmetadataquerynetworkscope.md) — Search all user-mounted remote volumes.
- [NSMetadataQueryUbiquitousDocumentsScope](nsmetadataqueryubiquitousdocumentsscope.md) — Search all files in the `Documents` directories of the app’s iCloud container directories.
- [NSMetadataQueryUbiquitousDataScope](nsmetadataqueryubiquitousdatascope.md) — Search all files not in the `Documents` directories of the app’s iCloud container directories.
- [NSMetadataQueryIndexedLocalComputerScope](nsmetadataqueryindexedlocalcomputerscope.md) — Search all indexed local mounted volumes including the current user’s home directory (even if the home directory is remote).
- [NSMetadataQueryIndexedNetworkScope](nsmetadataqueryindexednetworkscope.md) — Search all indexed user-mounted remote volumes.
