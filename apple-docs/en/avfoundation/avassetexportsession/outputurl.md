---
title: outputURL
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（27.0 起废弃）, iPadOS 4.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetexportsession/outputurl
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/outputurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/outputurl.json'
content_hash: 'sha256:c5d9fbb0a672f6a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# outputURL

<sub>Instance Property</sub>

A URL where an asset export session writes its output.

> [!warning] Deprecated
> Use `export(to:as:isolation:)` instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var outputURL: URL? { get set }
```

## Discussion

This property value is key-value observable.
