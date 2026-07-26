---
title: 'storageManagementPolicy(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetdownloadstoragemanager/storagemanagementpolicy(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadstoragemanager/storagemanagementpolicy(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadstoragemanager/storagemanagementpolicy%28for%3A%29.json'
content_hash: 'sha256:60ce8d40f1ec23d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadStorageManager](../avassetdownloadstoragemanager.md)

# storageManagementPolicy(for:)

<sub>Instance Method</sub>

Returns the storage management policy for a downloaded asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func storageManagementPolicy(for downloadStorageURL: URL) -> AVAssetDownloadStorageManagementPolicy?
```

## Parameters

- `downloadStorageURL` — The location of the downloaded asset.

## Return Value

The storage management policy for the asset, or `nil` if one isn’t set.

## See Also

### Setting the storage policy

- [- setStorageManagementPolicy:forURL:](<setstoragemanagementpolicy(__for_).md>) — Sets a storage policy for the downloaded asset.
