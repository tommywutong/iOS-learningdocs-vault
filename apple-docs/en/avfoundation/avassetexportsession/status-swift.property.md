---
title: status
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（18.0 起废弃）, iPadOS 4.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetexportsession/status-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/status-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/status-swift.property.json'
content_hash: 'sha256:f2318ba31c075f12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# status

<sub>Instance Property</sub>

The status of the export session.

> [!warning] Deprecated
> Use [states(updateInterval:)](<states(updateinterval_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var status: AVAssetExportSession.Status { get }
```

## Discussion

For possible values, see [Status](status-swift.enum.md).

This value is key-value observable.
