---
title: AVAssetDownloadedAssetEvictionPriority
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetdownloadedassetevictionpriority
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadedassetevictionpriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadedassetevictionpriority.json'
content_hash: 'sha256:186287c3adb79cd5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetDownloadedAssetEvictionPriority

<sub>Structure</sub>

Constants that define eviction priorities for a storage management policy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct AVAssetDownloadedAssetEvictionPriority
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Eviction priorities

- [AVAssetDownloadedAssetEvictionPriorityDefault](avassetdownloadedassetevictionpriority/default.md) — The default eviction priority.
- [AVAssetDownloadedAssetEvictionPriorityImportant](avassetdownloadedassetevictionpriority/important.md) — An eviction priority that indicates that this asset is important and the system should evict lower-priority assets first.

### Initializers

- [init(rawValue:)](<avassetdownloadedassetevictionpriority/init(rawvalue_).md>) — Creates an eviction priority with a string.

## See Also

### Managing storage

- [expirationDate](avmutableassetdownloadstoragemanagementpolicy/expirationdate.md) — The expiration date for an asset.
- [priority](avmutableassetdownloadstoragemanagementpolicy/priority.md) — The eviction priority for a downloaded asset.
