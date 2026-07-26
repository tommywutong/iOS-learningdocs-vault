---
title: isComposable
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+（16.0 起废弃）, iPadOS 4.3+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasset/iscomposable
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/iscomposable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/iscomposable.json'
content_hash: 'sha256:dad4806d6c3b1f61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# isComposable

<sub>Instance Property</sub>

A Boolean value that indicates whether you can use the asset as a segment of a composition track.

> [!warning] Deprecated
> Load the value of [isComposable](../avpartialasyncproperty/iscomposable.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var isComposable: Bool { get }
```

## Discussion

This property value is [true](../../swift/true.md) you can use the asset as a segment within an [AVCompositionTrack](../avcompositiontrack.md) object.
