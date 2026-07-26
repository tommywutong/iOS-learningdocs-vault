---
title: AVAssetDownloadStorageManagementPolicy
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetdownloadstoragemanagementpolicy
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadstoragemanagementpolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadstoragemanagementpolicy.json'
content_hash: 'sha256:846feefe0d2150d6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetDownloadStorageManagementPolicy

<sub>Class</sub>

An object that defines a policy to automatically manage the storage of downloaded assets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class AVAssetDownloadStorageManagementPolicy
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVMutableAssetDownloadStorageManagementPolicy](avmutableassetdownloadstoragemanagementpolicy.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Inspecting a policy

- [expirationDate](avassetdownloadstoragemanagementpolicy/expirationdate.md) — The expiration date for an asset.
- [priority](avassetdownloadstoragemanagementpolicy/priority.md) — The eviction priority for an asset.

## See Also

### Offline storage management

- [AVAssetDownloadStorageManager](avassetdownloadstoragemanager.md) — An object that manages policies to automatically purge downloaded assets.
- [AVMutableAssetDownloadStorageManagementPolicy](avmutableassetdownloadstoragemanagementpolicy.md) — A mutable object that you use to create a new storage management policy.
