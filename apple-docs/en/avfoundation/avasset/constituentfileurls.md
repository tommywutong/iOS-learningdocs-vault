---
title: constituentFileURLs
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avasset/constituentfileurls
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/constituentfileurls'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/constituentfileurls.json'
content_hash: 'sha256:5c904f90462272e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# constituentFileURLs

<sub>Instance Property</sub>

The list of file URLs that collectively represent the media asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) NSArray<NSURL *> * constituentFileURLs;
```

## Discussion

The list of file URLs that constitute the asset are returned only for QuickTime reference movies, or if the MediaExtension format reader implements this property [MEFileInfo setConstituentFileNames:].
