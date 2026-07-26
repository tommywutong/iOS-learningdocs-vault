---
title: inputs
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/inputs
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/inputs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/inputs.json'
content_hash: 'sha256:8fccdca72c06ea69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# inputs

<sub>Instance Property</sub>

The inputs that provide media data to a capture session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var inputs: [AVCaptureInput] { get }
```

## Discussion

You add new inputs to a capture session by callings its [- addInput:](<addinput(__).md>) method.

## See Also

### Configuring inputs

- [- canAddInput:](<canaddinput(__).md>) — Determines whether you can add an input to a session.
- [- addInput:](<addinput(__).md>) — Adds a capture input to the session.
- [- removeInput:](<removeinput(__).md>) — Removes an input from the session.
