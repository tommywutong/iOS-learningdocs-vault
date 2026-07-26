---
title: 'setStorageManagementPolicy(_:for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetdownloadstoragemanager/setstoragemanagementpolicy(_:for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadstoragemanager/setstoragemanagementpolicy(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadstoragemanager/setstoragemanagementpolicy%28_%3Afor%3A%29.json'
content_hash: 'sha256:ee6f34c1adf18e8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadStorageManager](../avassetdownloadstoragemanager.md)

# setStorageManagementPolicy(_:for:)

<sub>Instance Method</sub>

Sets a storage policy for the downloaded asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func setStorageManagementPolicy(_ storageManagementPolicy: AVAssetDownloadStorageManagementPolicy, for downloadStorageURL: URL)
```

## Parameters

- `storageManagementPolicy` — The policy to set for the downloaded asset.

- `downloadStorageURL` — The location of the downloaded asset.

## See Also

### Setting the storage policy

- [- storageManagementPolicyForURL:](<storagemanagementpolicy(for_).md>) — Returns the storage management policy for a downloaded asset.
