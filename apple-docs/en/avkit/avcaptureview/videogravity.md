---
title: videoGravity
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcaptureview/videogravity
source_url: 'https://developer.apple.com/documentation/avkit/avcaptureview/videogravity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcaptureview/videogravity.json'
content_hash: 'sha256:884ba45766fe38f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVCaptureView](../avcaptureview.md)

# videoGravity

<sub>Instance Property</sub>

A string value that defines how the capture view displays video within its bounds.

<sub>macOS</sub>

```swift
var videoGravity: AVLayerVideoGravity { get set }
```

## Discussion

See [AVLayerVideoGravity](../../avfoundation/avlayervideogravity.md) for supported values. The default value is [resizeAspect](../../avfoundation/avlayervideogravity/resizeaspect.md).

## See Also

### Customizing the View

- [controlsStyle](controlsstyle.md) — The style of the capture controls presented by the view.
- [AVCaptureViewControlsStyle](../avcaptureviewcontrolsstyle.md) — Constants that describe the capture view’s supported controls styles.
