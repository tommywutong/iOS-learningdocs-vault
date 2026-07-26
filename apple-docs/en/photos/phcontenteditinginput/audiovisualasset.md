---
title: audiovisualAsset
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcontenteditinginput/audiovisualasset
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditinginput/audiovisualasset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditinginput/audiovisualasset.json'
content_hash: 'sha256:47c10d3400c4364e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHContentEditingInput](../phcontenteditinginput.md)

# audiovisualAsset

<sub>Instance Property</sub>

The video asset, as an `AVAsset` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var audiovisualAsset: AVAsset? { get }
```

## Discussion

This object provides access to the video asset as a collection of tracks and metadata. For details on working with [AVAsset](../../avfoundation/avasset.md) objects, see [AVFoundation Programming Guide](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/AVFoundationPG/Articles/00_Introduction.html#//apple_ref/doc/uid/TP40010188).

## See Also

### Working with Video Assets

- [avAsset](avasset.md) — The video asset, as an `AVAsset` object. _(deprecated)_
