---
title: ubiquitousItemIsExcludedFromSync
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 11.3+, tvOS 14.5+, visionOS 1.0+, watchOS 7.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresourcevalues/ubiquitousitemisexcludedfromsync
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcevalues/ubiquitousitemisexcludedfromsync'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcevalues/ubiquitousitemisexcludedfromsync.json'
content_hash: 'sha256:e41c7fcaf97e0409'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceValues](../urlresourcevalues.md)

# ubiquitousItemIsExcludedFromSync

<sub>Instance Property</sub>

A Boolean value that indicates the system excludes the item from syncing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var ubiquitousItemIsExcludedFromSync: Bool? { get set }
```

## Discussion

The item is locally on-disk, but isn’t available on the server.

## See Also

### Ubiquitous values

- [isUbiquitousItem](isubiquitousitem.md) — A Boolean value that indicates whether the item is in the iCloud storage.
- [ubiquitousItemIsShared](ubiquitousitemisshared.md) — A Boolean value that indicates a shared item.
- [ubiquitousSharedItemCurrentUserPermissions](ubiquitousshareditemcurrentuserpermissions.md) — The current user’s permissions for the shared item.
- [ubiquitousSharedItemCurrentUserRole](ubiquitousshareditemcurrentuserrole.md) — The current user’s role for the shared item.
- [ubiquitousSharedItemMostRecentEditorNameComponents](ubiquitousshareditemmostrecenteditornamecomponents.md) — The name components of the most recent editor of the shared item.
- [ubiquitousSharedItemOwnerNameComponents](ubiquitousshareditemownernamecomponents.md) — The name components of the owner of the shared item.
- [ubiquitousItemContainerDisplayName](ubiquitousitemcontainerdisplayname.md) — The name of the item’s container as the system displays it to users.
- [ubiquitousItemDownloadRequested](ubiquitousitemdownloadrequested.md) — A Boolean value that indicates whether the user or the system requests a download of the item.
- [ubiquitousItemDownloadingError](ubiquitousitemdownloadingerror.md) — The error when downloading the item from iCloud fails.
- [ubiquitousItemDownloadingStatus](ubiquitousitemdownloadingstatus.md) — The download status of the item.
- [ubiquitousItemHasUnresolvedConflicts](ubiquitousitemhasunresolvedconflicts.md) — A Boolean value that indicates whether the item has outstanding conflicts.
- [ubiquitousItemIsDownloading](ubiquitousitemisdownloading.md) — A Boolean value that indicates whether the system is downloading the item.
- [ubiquitousItemIsUploaded](ubiquitousitemisuploaded.md) — A Boolean value that indicates whether data is present in the cloud for the item.
- [ubiquitousItemIsUploading](ubiquitousitemisuploading.md) — A Boolean value that indicates whether the system is uploading the item.
- [ubiquitousItemUploadingError](ubiquitousitemuploadingerror.md) — The error when uploading the item to iCloud fails.
