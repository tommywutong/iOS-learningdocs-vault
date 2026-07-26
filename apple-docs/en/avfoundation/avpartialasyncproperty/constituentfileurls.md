---
title: constituentFileURLs
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/constituentfileurls
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/constituentfileurls'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/constituentfileurls.json'
content_hash: 'sha256:001797cf504685f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# constituentFileURLs

<sub>Type Property</sub>

The list of file URLs used by the MediaExtension that constitute the asset. The list of file URLs that constitute the asset are returned only for QuickTime reference movies, or if the MediaExtension format reader implements this property [MEFileInfo setConstituentFileNames:].

<sub>macOS</sub>

```swift
static var constituentFileURLs: AVAsyncProperty<Root, [URL]> { get }
```
