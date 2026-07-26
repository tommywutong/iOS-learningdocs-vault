---
title: init()
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturescreeninput/init()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturescreeninput/init%28%29.json'
content_hash: 'sha256:c3678768ad0a9b99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureScreenInput](../avcapturescreeninput.md)

# init()

<sub>Initializer</sub>

Initializes a capture screen input that provides media data from the main screen.

<sub>macOS</sub>

```swift
init()
```

## Discussion

Using this initializer is equivalent to calling [- initWithDisplayID:](<init(displayid_).md>) with the result of the [CGMainDisplayID()](<../../coregraphics/cgmaindisplayid().md>) function.

## See Also

### Initializing a capture screen input

- [- initWithDisplayID:](<init(displayid_).md>) — Initializes a capture screen input that provides media data from the specified display.
