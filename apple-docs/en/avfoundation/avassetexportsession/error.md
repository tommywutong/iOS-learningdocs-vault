---
title: error
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（18.0 起废弃）, iPadOS 4.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetexportsession/error
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/error.json'
content_hash: 'sha256:e5aaebd954e27c44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# error

<sub>Instance Property</sub>

An optional error object.

> [!warning] Deprecated
> Use `export(to:as:)` instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var error: (any Error)? { get }
```

## Discussion

The default value of this property is `nil`. The export session sets it to an error object if its status changes to [AVAssetExportSessionStatusFailed](status-swift.enum/failed.md) or [AVAssetExportSessionStatusCancelled](status-swift.enum/cancelled.md).
