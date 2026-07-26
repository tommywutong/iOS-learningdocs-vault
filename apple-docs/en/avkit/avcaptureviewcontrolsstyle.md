---
title: AVCaptureViewControlsStyle
framework: AVKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcaptureviewcontrolsstyle
source_url: 'https://developer.apple.com/documentation/avkit/avcaptureviewcontrolsstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcaptureviewcontrolsstyle.json'
content_hash: 'sha256:723442789b74873a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVCaptureViewControlsStyle

<sub>Enumeration</sub>

Constants that describe the capture view’s supported controls styles.

<sub>macOS</sub>

```swift
enum AVCaptureViewControlsStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a controls style

- [init(rawValue:)](<avcaptureviewcontrolsstyle/init(rawvalue_).md>)

### Controls Styles

- [AVCaptureViewControlsStyleInline](avcaptureviewcontrolsstyle/inline.md) — The view’s inline controls style.
- [AVCaptureViewControlsStyleFloating](avcaptureviewcontrolsstyle/floating.md) — The view’s floating controls style, which matches the user interface of QuickTime Player.
- [AVCaptureViewControlsStyleInlineDeviceSelection](avcaptureviewcontrolsstyle/inlinedeviceselection.md) — The view’s inline device selection style.
- [AVCaptureViewControlsStyleDefault](avcaptureviewcontrolsstyle/default.md) — The view’s default controls style.

## See Also

### Customizing the View

- [controlsStyle](avcaptureview/controlsstyle.md) — The style of the capture controls presented by the view.
- [videoGravity](avcaptureview/videogravity.md) — A string value that defines how the capture view displays video within its bounds.
