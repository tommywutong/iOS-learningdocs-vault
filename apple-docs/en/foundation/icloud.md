---
title: iCloud
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/icloud
source_url: 'https://developer.apple.com/documentation/foundation/icloud'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/icloud.json'
content_hash: 'sha256:2c0724457c1f3ec4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# iCloud

<sub>API Collection</sub>

Manage files and key-value data that automatically synchronize among a user’s iCloud devices.

## Topics

### iCloud Storage

- [FileManager](filemanager.md) — A convenient interface to the contents of the file system, and the primary means of interacting with it.
- [FileManagerDelegate](filemanagerdelegate.md) — The interface a file manager’s delegate uses to intervene during operations or if an error occurs.

### App Preferences

- [Synchronizing App Preferences with iCloud](synchronizing-app-preferences-with-icloud.md) — Store app preferences in iCloud and share them among instances of your app running on a user’s connected devices.
- [NSUbiquitousKeyValueStore](nsubiquitouskeyvaluestore.md) — An iCloud-based container of key-value pairs you share among instances of your app running on a person’s devices.

### File Search

- [NSMetadataQuery](nsmetadataquery.md) — A query that you perform against Spotlight metadata.
- [NSMetadataQueryDelegate](nsmetadataquerydelegate.md) — An interface that enables the delegate of a metadata query to provide substitute results or attributes.
- [NSMetadataItem](nsmetadataitem.md) — The metadata associated with a file.

### Entitlements

- [com.apple.developer.icloud-container-development-container-identifiers](../bundleresources/entitlements/com.apple.developer.icloud-container-development-container-identifiers.md) — The container identifiers for the iCloud development environment.
- [com.apple.developer.icloud-container-environment](../bundleresources/entitlements/com.apple.developer.icloud-container-environment.md) — The development or production environment to use for the iCloud containers.
- [iCloud Container Identifiers Entitlement](../bundleresources/entitlements/com.apple.developer.icloud-container-identifiers.md) — The container identifiers for the iCloud production environment.
- [iCloud Services Entitlement](../bundleresources/entitlements/com.apple.developer.icloud-services.md) — The iCloud services used by the app.
- [iCloud Key-Value Store Entitlement](../bundleresources/entitlements/com.apple.developer.ubiquity-kvstore-identifier.md) — The container identifier to use for iCloud key-value storage.

### Errors

- [iCloud Error Codes](icloud-error-codes.md) — Error codes to expect when an iCloud-related error occurs.

## See Also

### Files and Data Persistence

- [File System](file-system.md) — Create, read, write, and examine files and folders in the file system.
- [Archives and Serialization](archives-and-serialization.md) — Convert objects and values to and from property list, JSON, and other flat binary representations.
- [Settings](settings.md) — Configure your app using data you store persistently on the local disk or in iCloud.
- [Spotlight](spotlight.md) — Search for files and other items on the local device, and index your app’s content for searching.
- [Optimizing Your App’s Data for iCloud Backup](optimizing-your-app-s-data-for-icloud-backup.md) — Minimize the space and time that backups take to create by excluding purgeable and nonpurgeable data from backups.
