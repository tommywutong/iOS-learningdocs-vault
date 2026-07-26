---
title: capturesMouseClicks
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturescreeninput/capturesmouseclicks
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/capturesmouseclicks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturescreeninput/capturesmouseclicks.json'
content_hash: 'sha256:a40c551479ad1362'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureScreenInput](../avcapturescreeninput.md)

# capturesMouseClicks

<sub>Instance Property</sub>

A Boolean value that specifies whether mouse clicks appear highlighted in the captured output.

<sub>macOS</sub>

```swift
var capturesMouseClicks: Bool { get set }
```

## Discussion

By default, `AVCaptureScreenInput` does not highlight mouse clicks in its captured output.

If you set this property is set to [true](../../swift/true.md), mouse clicks are highlighted (a circle is drawn around the mouse for the duration of the click) in the captured output.

## See Also

### Capturing mouse activity

- [capturesCursor](capturescursor.md) — A Boolean value that specifies whether the mouse cursor appears in the captured output.
