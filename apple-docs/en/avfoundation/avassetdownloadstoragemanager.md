---
title: AVAssetDownloadStorageManager
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetdownloadstoragemanager
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadstoragemanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadstoragemanager.json'
content_hash: 'sha256:1b64373cee1e8a55'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetDownloadStorageManager

<sub>Class</sub>

An object that manages policies to automatically purge downloaded assets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class AVAssetDownloadStorageManager
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the shared manager

- [+ sharedDownloadStorageManager](<avassetdownloadstoragemanager/shared().md>) — Returns the shared storage manager instance.

### Setting the storage policy

- [- storageManagementPolicyForURL:](<avassetdownloadstoragemanager/storagemanagementpolicy(for_).md>) — Returns the storage management policy for a downloaded asset.
- [- setStorageManagementPolicy:forURL:](<avassetdownloadstoragemanager/setstoragemanagementpolicy(__for_).md>) — Sets a storage policy for the downloaded asset.

## See Also

### Offline storage management

- [AVAssetDownloadStorageManagementPolicy](avassetdownloadstoragemanagementpolicy.md) — An object that defines a policy to automatically manage the storage of downloaded assets.
- [AVMutableAssetDownloadStorageManagementPolicy](avmutableassetdownloadstoragemanagementpolicy.md) — A mutable object that you use to create a new storage management policy.
