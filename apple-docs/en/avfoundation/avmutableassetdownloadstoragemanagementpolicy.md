---
title: AVMutableAssetDownloadStorageManagementPolicy
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutableassetdownloadstoragemanagementpolicy
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutableassetdownloadstoragemanagementpolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutableassetdownloadstoragemanagementpolicy.json'
content_hash: 'sha256:b49333c1805551dc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMutableAssetDownloadStorageManagementPolicy

<sub>Class</sub>

A mutable object that you use to create a new storage management policy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class AVMutableAssetDownloadStorageManagementPolicy
```

## Relationships

- **Inherits From**: [AVAssetDownloadStorageManagementPolicy](avassetdownloadstoragemanagementpolicy.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Managing storage

- [expirationDate](avmutableassetdownloadstoragemanagementpolicy/expirationdate.md) — The expiration date for an asset.
- [priority](avmutableassetdownloadstoragemanagementpolicy/priority.md) — The eviction priority for a downloaded asset.
- [AVAssetDownloadedAssetEvictionPriority](avassetdownloadedassetevictionpriority.md) — Constants that define eviction priorities for a storage management policy.

## See Also

### Offline storage management

- [AVAssetDownloadStorageManager](avassetdownloadstoragemanager.md) — An object that manages policies to automatically purge downloaded assets.
- [AVAssetDownloadStorageManagementPolicy](avassetdownloadstoragemanagementpolicy.md) — An object that defines a policy to automatically manage the storage of downloaded assets.
