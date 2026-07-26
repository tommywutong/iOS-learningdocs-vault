---
title: usesProVideoStorage
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/usesprovideostorage
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/usesprovideostorage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/usesprovideostorage.json'
content_hash: 'sha256:0c27c10b6a554cb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# usesProVideoStorage

<sub>Instance Property</sub>

Indicates whether to use pre-allocated storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var usesProVideoStorage: Bool { get set }
```

## Discussion

The default value is `NO`. See more detailed description of ProVideoStorage in `AVProVideoStorage.h`.

An exception will be thrown if clients try to set `YES` if the value of the `proVideoStorageSupported` property is `NO`.

An exception will be thrown if clients try to set this property after `-startWriting` has been called on the receiver.
