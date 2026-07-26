---
title: generateInitialTimecode()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecodegenerator/generateinitialtimecode()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/generateinitialtimecode()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecodegenerator/generateinitialtimecode%28%29.json'
content_hash: 'sha256:8e3bce095076a28a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md)

# generateInitialTimecode()

<sub>Instance Method</sub>

Generates an initial timecode intended to be the first in a sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func generateInitialTimecode() -> AVCaptureTimecode
```

## Return Value

A populated [AVCaptureTimecode](../avcapturetimecode.md) structure.
