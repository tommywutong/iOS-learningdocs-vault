---
title: 'init(asset:timebase:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 10.10+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avsamplebuffergenerator/init(asset:timebase:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffergenerator/init(asset:timebase:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffergenerator/init%28asset%3Atimebase%3A%29.json'
content_hash: 'sha256:1e870f06b4b8ea2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferGenerator](../avsamplebuffergenerator.md)

# init(asset:timebase:)

<sub>Initializer</sub>

Creates a new sample buffer generator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(asset: AVAsset, timebase: CMTimebase?)
```

## Parameters

- `asset` — The asset.

- `timebase` — If `NULL`, requests will be handled synchronously.

## Return Value

An initialized `AVSampleBufferGenerator` instance.
