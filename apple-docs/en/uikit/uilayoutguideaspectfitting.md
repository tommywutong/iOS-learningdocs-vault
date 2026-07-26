---
title: UILayoutGuideAspectFitting
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilayoutguideaspectfitting
source_url: 'https://developer.apple.com/documentation/uikit/uilayoutguideaspectfitting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilayoutguideaspectfitting.json'
content_hash: 'sha256:d837f0dd8ef4f09b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UILayoutGuideAspectFitting

<sub>Protocol</sub>

The interface for a layout guide that supports a particular aspect ratio.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol UILayoutGuideAspectFitting : NSObjectProtocol
```

## Overview

The [safeAreaAspectFitLayoutGuide](uiwindow/safeareaaspectfitlayoutguide.md) property adopts this protocol to provide a layout guide for placing media content of a particular aspect ratio.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Specifying the aspect ratio

- [aspectRatio](uilayoutguideaspectfitting/aspectratio.md) — The content’s aspect ratio.

## See Also

### Working with layout guides

- [safeAreaAspectFitLayoutGuide](uiwindow/safeareaaspectfitlayoutguide.md) — A layout guide for placing content of a particular aspect ratio.
