---
title: preferredTransform
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasset/preferredtransform
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/preferredtransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/preferredtransform.json'
content_hash: 'sha256:5e7860db974d810e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# preferredTransform

<sub>Instance Property</sub>

The asset’s transform preference to apply to its visual content during presentation or processing.

> [!warning] Deprecated
> Load the value of [preferredTransform](../avpartialasyncproperty/preferredtransform-80d13.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var preferredTransform: CGAffineTransform { get }
```

## Discussion

The value is typically, but not always, the identity transform.
