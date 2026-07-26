---
title: 'init(displayID:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturescreeninput/init(displayid:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/init(displayid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturescreeninput/init%28displayid%3A%29.json'
content_hash: 'sha256:c7a0b71c9c6e6f5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureScreenInput](../avcapturescreeninput.md)

# init(displayID:)

<sub>Initializer</sub>

Initializes a capture screen input that provides media data from the specified display.

<sub>macOS</sub>

```swift
init?(displayID: CGDirectDisplayID)
```

## Parameters

- `displayID` — The ID of the display from which to capture video. `CGDirectDisplayID` is defined in `<CoreGraphics/CGDirectDisplay.h>`.

## Return Value

A capture screen input initialized to provide media data from a given display. If the display cannot be used (because it is not available on the system, for example), returns `nil`.

## See Also

### Initializing a capture screen input

- [- init](<init().md>) — Initializes a capture screen input that provides media data from the main screen.
