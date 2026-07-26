---
title: capturesCursor
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturescreeninput/capturescursor
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/capturescursor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturescreeninput/capturescursor.json'
content_hash: 'sha256:33e045c059900ac1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureScreenInput](../avcapturescreeninput.md)

# capturesCursor

<sub>Instance Property</sub>

A Boolean value that specifies whether the mouse cursor appears in the captured output.

<sub>macOS</sub>

```swift
var capturesCursor: Bool { get set }
```

## Discussion

When this property is true (the default), captured video frames include the mouse pointer. If you change this property to false, the captured output contains only the windows on the screen (that is, the mouse pointer is invisible in captured video).

> [!note] Note
> Even if you hide the mouse pointer in captured output, [CMSampleBuffer](../../coremedia/cmsamplebuffer.md) objects vended by the capture include metadata for the cursor position and mouse button state. See [kCMIOSampleBufferAttachmentKey_MouseAndKeyboardModifiers](../../coremediaio/kcmiosamplebufferattachmentkey_mouseandkeyboardmodifiers.md).

## See Also

### Capturing mouse activity

- [capturesMouseClicks](capturesmouseclicks.md) — A Boolean value that specifies whether mouse clicks appear highlighted in the captured output.
