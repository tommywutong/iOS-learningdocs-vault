---
title: fileOutput
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcaptureview/fileoutput
source_url: 'https://developer.apple.com/documentation/avkit/avcaptureview/fileoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcaptureview/fileoutput.json'
content_hash: 'sha256:b02513482b04c716'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVCaptureView](../avcaptureview.md)

# fileOutput

<sub>Instance Property</sub>

The capture file output used to record media data.

<sub>macOS</sub>

```swift
var fileOutput: AVCaptureFileOutput? { get }
```

## Discussion

The value of this property is the first capture file output object contained in the session’s [outputs](../../avfoundation/avcapturesession/outputs.md) array, or `nil` if it has no outputs. In the latter case, the capture view disables the start recording button. However, it may still enable the controls for choosing input sources.
