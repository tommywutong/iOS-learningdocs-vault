---
title: ubiquitousItemIsSyncPausedKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresourcekey/ubiquitousitemissyncpausedkey
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcekey/ubiquitousitemissyncpausedkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcekey/ubiquitousitemissyncpausedkey.json'
content_hash: 'sha256:b314e9de528a5ad5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceKey](../urlresourcekey.md)

# ubiquitousItemIsSyncPausedKey

<sub>Type Property</sub>

A Boolean value that indicates whether sync is paused for this item (value type boolean `NSNumber`).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let ubiquitousItemIsSyncPausedKey: URLResourceKey
```

## See Also

### Ubiquitous keys

- [NSURLIsUbiquitousItemKey](isubiquitousitemkey.md) — The key for a Boolean value that indicates whether the item is in iCloud storage.
- [NSURLUbiquitousSharedItemMostRecentEditorNameComponentsKey](ubiquitousshareditemmostrecenteditornamecomponentskey.md) — The key for the name components of the most recent editor.
- [NSURLUbiquitousItemDownloadRequestedKey](ubiquitousitemdownloadrequestedkey.md) — The key for a Boolean value that indicates whether the system has already made a call [- startDownloadingUbiquitousItemAtURL:error:](<../filemanager/startdownloadingubiquitousitem(at_).md>) to download the item.
- [NSURLUbiquitousItemIsDownloadingKey](ubiquitousitemisdownloadingkey.md) — The key for a Boolean value that indicates whether the system is downloading the item from iCloud.
- [NSURLUbiquitousItemDownloadingErrorKey](ubiquitousitemdownloadingerrorkey.md) — The key for an error object that indicates why downloading the item from iCloud fails.
- [NSURLUbiquitousItemDownloadingStatusKey](ubiquitousitemdownloadingstatuskey.md) — The key for the current download state for the item.
- [URLUbiquitousItemDownloadingStatus](../urlubiquitousitemdownloadingstatus.md) — Values that describe the iCloud storage state of a file.
- [NSURLUbiquitousItemIsExcludedFromSyncKey](ubiquitousitemisexcludedfromsynckey.md) — The key of a Boolean value that indicates whether the system excludes the item from syncing.
- [NSURLUbiquitousItemIsUploadedKey](ubiquitousitemisuploadedkey.md) — The key for a Boolean value that indicates whether the system uploads the item’s data to iCloud storage.
- [NSURLUbiquitousItemIsUploadingKey](ubiquitousitemisuploadingkey.md) — The key for a Boolean value that indicates whether the system is uploading the item to iCloud.
- [NSURLUbiquitousItemUploadingErrorKey](ubiquitousitemuploadingerrorkey.md) — The key for an error object that indicates why uploading the item to iCloud fails.
- [NSURLUbiquitousItemHasUnresolvedConflictsKey](ubiquitousitemhasunresolvedconflictskey.md) — The key for a Boolean value that indicates whether this item has outstanding conflicts.
- [NSURLUbiquitousItemContainerDisplayNameKey](ubiquitousitemcontainerdisplaynamekey.md) — The key for a string that contains the name of the item’s container as it appears to the user.
- [NSURLUbiquitousSharedItemOwnerNameComponentsKey](ubiquitousshareditemownernamecomponentskey.md) — The key for the name components of the item’s owner.
- [NSURLUbiquitousSharedItemCurrentUserPermissionsKey](ubiquitousshareditemcurrentuserpermissionskey.md) — The key for the current user’s permissions.
