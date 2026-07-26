---
title: Metadata Query Search Scopes
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/metadata-query-search-scopes
source_url: 'https://developer.apple.com/documentation/foundation/metadata-query-search-scopes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/metadata-query-search-scopes.json'
content_hash: 'sha256:cdfbdbb6c75c4cfb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [iCloud](icloud.md) · [NSMetadataQuery](nsmetadataquery.md)

# Metadata Query Search Scopes

<sub>API Collection</sub>

Constants for the predefined search scopes used by [searchScopes](nsmetadataquery/searchscopes.md).

## Topics

### Constants

- [NSMetadataQueryUserHomeScope](nsmetadataqueryuserhomescope.md) — Search the user’s home directory.
- [NSMetadataQueryLocalComputerScope](nsmetadataquerylocalcomputerscope.md) — Search all local mounted volumes, including the user home directory. The user’s home directory is searched even if it is a remote volume.
- [NSMetadataQueryNetworkScope](nsmetadataquerynetworkscope.md) — Search all user-mounted remote volumes.
- [NSMetadataQueryUbiquitousDocumentsScope](nsmetadataqueryubiquitousdocumentsscope.md) — Search all files in the `Documents` directories of the app’s iCloud container directories.
- [NSMetadataQueryUbiquitousDataScope](nsmetadataqueryubiquitousdatascope.md) — Search all files not in the `Documents` directories of the app’s iCloud container directories.
- [NSMetadataQueryAccessibleUbiquitousExternalDocumentsScope](nsmetadataqueryaccessibleubiquitousexternaldocumentsscope.md) — Search for documents outside the app’s container. This search can locate iCloud documents that the user previously opened using a document picker view controller. This lets your app access the documents again without requiring direct user interaction. The result’s [NSMetadataItemURLKey](nsmetadataitemurlkey.md) attributes return security-scoped NSURLs. For more information on working with security-scoped URLs, see [Security-Scoped URLs](nsurl.md#Security-Scoped-URLs) in [NSURL](nsurl.md).
- [NSMetadataQueryIndexedLocalComputerScope](nsmetadataqueryindexedlocalcomputerscope.md) — Search all indexed local mounted volumes including the current user’s home directory (even if the home directory is remote).
- [NSMetadataQueryIndexedNetworkScope](nsmetadataqueryindexednetworkscope.md) — Search all indexed user-mounted remote volumes.

## See Also

### Constants

- [Content Relevance](content-relevance.md) — In addition to including the requested metadata attributes, a query result also includes content relevance, accessed with the following key.
- [Keys for Use with a Notification Info Dictionary](keys-for-use-with-a-notification-info-dictionary.md) — Constants for keys to retrieve the collection of changed items from a notification’s user info dictionary.
