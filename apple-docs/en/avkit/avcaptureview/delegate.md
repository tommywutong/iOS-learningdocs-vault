---
title: delegate
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcaptureview/delegate
source_url: 'https://developer.apple.com/documentation/avkit/avcaptureview/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcaptureview/delegate.json'
content_hash: 'sha256:8edd7801dc135a96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVCaptureView](../avcaptureview.md)

# delegate

<sub>Instance Property</sub>

The capture view’s delegate object.

<sub>macOS</sub>

```swift
weak var delegate: (any AVCaptureViewDelegate)? { get set }
```

## Discussion

The capture view disables the start recording button if you don’t provide a delegate object.

## See Also

### Configuring the Delegate

- [AVCaptureViewDelegate](../avcaptureviewdelegate.md) — The protocol that defines the methods you can implement to respond to capture view events.
