---
title: AVCaptureScreenInput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturescreeninput
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturescreeninput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturescreeninput.json'
content_hash: 'sha256:4b3515aa631d4b98'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureScreenInput

<sub>Class</sub>

A capture input for recording from a screen in macOS.

<sub>macOS</sub>

```swift
class AVCaptureScreenInput
```

## Overview

> [!important] Important
> Starting in macOS 12.3, use the [ScreenCaptureKit](../screencapturekit.md) framework for screen recording instead.

This class is a concrete capture input subclass that provides an interface to capture media from a screen or a portion of a screen.

Use instances of this class as input sources for [AVCaptureSession](avcapturesession.md) objects that provide media data from one of the screens connected to the system, represented by [CGDirectDisplayID](../coregraphics/cgdirectdisplayid.md).

## Relationships

- **Inherits From**: [AVCaptureInput](avcaptureinput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing a capture screen input

- [- initWithDisplayID:](<avcapturescreeninput/init(displayid_).md>) — Initializes a capture screen input that provides media data from the specified display.
- [- init](<avcapturescreeninput/init().md>) — Initializes a capture screen input that provides media data from the main screen.

### Setting video capture options

- [minFrameDuration](avcapturescreeninput/minframeduration.md) — The screen input’s minimum frame duration.
- [cropRect](avcapturescreeninput/croprect.md) — Indicates the bounding rectangle of the screen area to be captured, in pixels.
- [scaleFactor](avcapturescreeninput/scalefactor.md) — Indicates the factor by which video buffers captured from the screen are to be scaled.

### Capturing mouse activity

- [capturesCursor](avcapturescreeninput/capturescursor.md) — A Boolean value that specifies whether the mouse cursor appears in the captured output.
- [capturesMouseClicks](avcapturescreeninput/capturesmouseclicks.md) — A Boolean value that specifies whether mouse clicks appear highlighted in the captured output.

### Deprecated

- [removesDuplicateFrames](avcapturescreeninput/removesduplicateframes.md) — A Boolean value that specifies whether the capture input skips duplicate frames. _(deprecated)_
