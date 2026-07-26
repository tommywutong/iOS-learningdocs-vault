---
title: ubiquitousItemDownloadingStatusKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresourcekey/ubiquitousitemdownloadingstatuskey
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcekey/ubiquitousitemdownloadingstatuskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcekey/ubiquitousitemdownloadingstatuskey.json'
content_hash: 'sha256:24556b7523bac86d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceKey](../urlresourcekey.md)

# ubiquitousItemDownloadingStatusKey

<sub>Type Property</sub>

The key for the current download state for the item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let ubiquitousItemDownloadingStatusKey: URLResourceKey
```

## Discussion

The value indicates whether a local copy exists and whether that copy is the most current version of the item. See [URLUbiquitousItemDownloadingStatus](../urlubiquitousitemdownloadingstatus.md) for values for this key.

## See Also

### Ubiquitous keys

- [NSURLIsUbiquitousItemKey](isubiquitousitemkey.md) — The key for a Boolean value that indicates whether the item is in iCloud storage.
- [NSURLUbiquitousSharedItemMostRecentEditorNameComponentsKey](ubiquitousshareditemmostrecenteditornamecomponentskey.md) — The key for the name components of the most recent editor.
- [NSURLUbiquitousItemDownloadRequestedKey](ubiquitousitemdownloadrequestedkey.md) — The key for a Boolean value that indicates whether the system has already made a call [- startDownloadingUbiquitousItemAtURL:error:](<../filemanager/startdownloadingubiquitousitem(at_).md>) to download the item.
- [NSURLUbiquitousItemIsDownloadingKey](ubiquitousitemisdownloadingkey.md) — The key for a Boolean value that indicates whether the system is downloading the item from iCloud.
- [NSURLUbiquitousItemDownloadingErrorKey](ubiquitousitemdownloadingerrorkey.md) — The key for an error object that indicates why downloading the item from iCloud fails.
- [URLUbiquitousItemDownloadingStatus](../urlubiquitousitemdownloadingstatus.md) — Values that describe the iCloud storage state of a file.
- [NSURLUbiquitousItemIsExcludedFromSyncKey](ubiquitousitemisexcludedfromsynckey.md) — The key of a Boolean value that indicates whether the system excludes the item from syncing.
- [NSURLUbiquitousItemIsUploadedKey](ubiquitousitemisuploadedkey.md) — The key for a Boolean value that indicates whether the system uploads the item’s data to iCloud storage.
- [NSURLUbiquitousItemIsUploadingKey](ubiquitousitemisuploadingkey.md) — The key for a Boolean value that indicates whether the system is uploading the item to iCloud.
- [NSURLUbiquitousItemUploadingErrorKey](ubiquitousitemuploadingerrorkey.md) — The key for an error object that indicates why uploading the item to iCloud fails.
- [NSURLUbiquitousItemHasUnresolvedConflictsKey](ubiquitousitemhasunresolvedconflictskey.md) — The key for a Boolean value that indicates whether this item has outstanding conflicts.
- [NSURLUbiquitousItemContainerDisplayNameKey](ubiquitousitemcontainerdisplaynamekey.md) — The key for a string that contains the name of the item’s container as it appears to the user.
- [NSURLUbiquitousSharedItemOwnerNameComponentsKey](ubiquitousshareditemownernamecomponentskey.md) — The key for the name components of the item’s owner.
- [NSURLUbiquitousSharedItemCurrentUserPermissionsKey](ubiquitousshareditemcurrentuserpermissionskey.md) — The key for the current user’s permissions.
- [NSURLUbiquitousSharedItemCurrentUserRoleKey](ubiquitousshareditemcurrentuserrolekey.md) — The key for the role of the current user.
