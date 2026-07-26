---
title: URLUbiquitousItemDownloadingStatus
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlubiquitousitemdownloadingstatus
source_url: 'https://developer.apple.com/documentation/foundation/urlubiquitousitemdownloadingstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlubiquitousitemdownloadingstatus.json'
content_hash: 'sha256:9a195c751f7ec254'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLUbiquitousItemDownloadingStatus

<sub>Structure</sub>

Values that describe the iCloud storage state of a file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct URLUbiquitousItemDownloadingStatus
```

## Discussion

These constants are possible values for the [NSURLUbiquitousItemDownloadingStatusKey](urlresourcekey/ubiquitousitemdownloadingstatuskey.md) key.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Download Status Instance

- [init(rawValue:)](<urlubiquitousitemdownloadingstatus/init(rawvalue_).md>) — Creates a download status instance from the provided constant string.

### Constants

- [NSURLUbiquitousItemDownloadingStatusCurrent](urlubiquitousitemdownloadingstatus/current.md) — A local copy of this item exists and is the most up-to-date version known to the device.
- [NSURLUbiquitousItemDownloadingStatusDownloaded](urlubiquitousitemdownloadingstatus/downloaded.md) — A local copy of this item exists, but it is stale. The most recent version will be downloaded as soon as possible.
- [NSURLUbiquitousItemDownloadingStatusNotDownloaded](urlubiquitousitemdownloadingstatus/notdownloaded.md) — This item has not been downloaded yet. Use [- startDownloadingUbiquitousItemAtURL:error:](<filemanager/startdownloadingubiquitousitem(at_).md>) to download it.

## See Also

### Ubiquitous keys

- [NSURLIsUbiquitousItemKey](urlresourcekey/isubiquitousitemkey.md) — The key for a Boolean value that indicates whether the item is in iCloud storage.
- [NSURLUbiquitousSharedItemMostRecentEditorNameComponentsKey](urlresourcekey/ubiquitousshareditemmostrecenteditornamecomponentskey.md) — The key for the name components of the most recent editor.
- [NSURLUbiquitousItemDownloadRequestedKey](urlresourcekey/ubiquitousitemdownloadrequestedkey.md) — The key for a Boolean value that indicates whether the system has already made a call [- startDownloadingUbiquitousItemAtURL:error:](<filemanager/startdownloadingubiquitousitem(at_).md>) to download the item.
- [NSURLUbiquitousItemIsDownloadingKey](urlresourcekey/ubiquitousitemisdownloadingkey.md) — The key for a Boolean value that indicates whether the system is downloading the item from iCloud.
- [NSURLUbiquitousItemDownloadingErrorKey](urlresourcekey/ubiquitousitemdownloadingerrorkey.md) — The key for an error object that indicates why downloading the item from iCloud fails.
- [NSURLUbiquitousItemDownloadingStatusKey](urlresourcekey/ubiquitousitemdownloadingstatuskey.md) — The key for the current download state for the item.
- [NSURLUbiquitousItemIsExcludedFromSyncKey](urlresourcekey/ubiquitousitemisexcludedfromsynckey.md) — The key of a Boolean value that indicates whether the system excludes the item from syncing.
- [NSURLUbiquitousItemIsUploadedKey](urlresourcekey/ubiquitousitemisuploadedkey.md) — The key for a Boolean value that indicates whether the system uploads the item’s data to iCloud storage.
- [NSURLUbiquitousItemIsUploadingKey](urlresourcekey/ubiquitousitemisuploadingkey.md) — The key for a Boolean value that indicates whether the system is uploading the item to iCloud.
- [NSURLUbiquitousItemUploadingErrorKey](urlresourcekey/ubiquitousitemuploadingerrorkey.md) — The key for an error object that indicates why uploading the item to iCloud fails.
- [NSURLUbiquitousItemHasUnresolvedConflictsKey](urlresourcekey/ubiquitousitemhasunresolvedconflictskey.md) — The key for a Boolean value that indicates whether this item has outstanding conflicts.
- [NSURLUbiquitousItemContainerDisplayNameKey](urlresourcekey/ubiquitousitemcontainerdisplaynamekey.md) — The key for a string that contains the name of the item’s container as it appears to the user.
- [NSURLUbiquitousSharedItemOwnerNameComponentsKey](urlresourcekey/ubiquitousshareditemownernamecomponentskey.md) — The key for the name components of the item’s owner.
- [NSURLUbiquitousSharedItemCurrentUserPermissionsKey](urlresourcekey/ubiquitousshareditemcurrentuserpermissionskey.md) — The key for the current user’s permissions.
- [NSURLUbiquitousSharedItemCurrentUserRoleKey](urlresourcekey/ubiquitousshareditemcurrentuserrolekey.md) — The key for the role of the current user.
