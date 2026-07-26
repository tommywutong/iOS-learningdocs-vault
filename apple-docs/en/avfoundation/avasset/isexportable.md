---
title: isExportable
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+（16.0 起废弃）, iPadOS 4.3+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasset/isexportable
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/isexportable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/isexportable.json'
content_hash: 'sha256:a09e57c9d6eed821'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# isExportable

<sub>Instance Property</sub>

A Boolean value that indicates whether you can export this asset using an export session.

> [!warning] Deprecated
> Load the value of [isExportable](../avpartialasyncproperty/isexportable.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isExportable: Bool { get }
```

## Discussion

This property value is [true](../../swift/true.md) if you can export the asset using [AVAssetExportSession](../avassetexportsession.md).
