---
title: progress
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（27.0 起废弃）, iPadOS 4.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetexportsession/progress
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/progress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/progress.json'
content_hash: 'sha256:54e842d9f756481b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# progress

<sub>Instance Property</sub>

A value that indicates the progress of the export.

> [!warning] Deprecated
> Use `progressStates(updateInterval:)` instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var progress: Float { get }
```

## Discussion

The value of this property ranges from `0.0` to `1.0.`
