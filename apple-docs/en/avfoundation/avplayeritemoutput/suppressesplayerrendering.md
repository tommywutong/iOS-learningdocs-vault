---
title: suppressesPlayerRendering
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemoutput/suppressesplayerrendering
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemoutput/suppressesplayerrendering'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemoutput/suppressesplayerrendering.json'
content_hash: 'sha256:1306a24db423e773'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemOutput](../avplayeritemoutput.md)

# suppressesPlayerRendering

<sub>Instance Property</sub>

A Boolean value that indicates whether the player object renders the receiver’s output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var suppressesPlayerRendering: Bool { get set }
```

## Discussion

When the value of this property is [false](../../swift/false.md) (the default), the player object handles the rendering of the receiver’s associated output. Change the value of this property to [true](../../swift/true.md) to suppress the rendering of the media data associated with this object.
