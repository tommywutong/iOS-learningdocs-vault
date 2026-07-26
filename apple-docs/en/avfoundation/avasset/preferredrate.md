---
title: preferredRate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasset/preferredrate
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/preferredrate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/preferredrate.json'
content_hash: 'sha256:18f293c3e2dc72e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# preferredRate

<sub>Instance Property</sub>

The asset’s rate preference for playing its media.

> [!warning] Deprecated
> Load the value of [preferredRate](../avpartialasyncproperty/preferredrate.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var preferredRate: Float { get }
```

## Discussion

This value is typically, but not always, 1.0.
