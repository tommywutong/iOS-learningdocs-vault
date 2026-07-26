---
title: isReadable
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+（16.0 起废弃）, iPadOS 4.3+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasset/isreadable
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/isreadable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/isreadable.json'
content_hash: 'sha256:d15ed191127c541b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# isReadable

<sub>Instance Property</sub>

A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.

> [!warning] Deprecated
> Load the value of [isReadable](../avpartialasyncproperty/isreadable.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isReadable: Bool { get }
```

## Discussion

This property value is [true](../../swift/true.md) if you can use [AVAssetReader](../avassetreader.md) to extract the asset’s media data.
