---
title: AVCaptionRenderer
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 26.4+, visionOS 26.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionrenderer
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionrenderer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionrenderer.json'
content_hash: 'sha256:46bb154e9f9c2b36'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptionRenderer

<sub>Class</sub>

An object that renders captions for display at a particular time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVCaptionRenderer
```

## Overview

This object renders a caption scene for a given time from a collection of captions. If there aren’t any captions to display at the specified time, the renderer draws an empty flood fill with a zero alpha or a color.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the renderer

- [captions](avcaptionrenderer/captions.md) — The captions to render.
- [bounds](avcaptionrenderer/bounds.md) — The drawing bounds of caption scenes.

### Determining scene changes

- [- captionSceneChangesInRange:](<avcaptionrenderer/captionscenechanges(in_).md>) — Determine render time ranges within an enclosing time range to account for visual changes among captions.
- [Scene](avcaptionrenderer/scene.md) — An object that holds a time range and an associated state which indicates when the renderer draws output.

### Rendering a caption

- [- renderInContext:forTime:](<avcaptionrenderer/render(in_for_).md>) — Draw the captions for the time you specify.

### Initializers

- [- init](<avcaptionrenderer/init().md>)

### Type Methods

- [+ captionPreviewForProfileID:extendedLanguageTag:renderSize:](<avcaptionrenderer/captionpreview(forprofileid_extendedlanguagetag_rendersize_).md>) — Generate a caption preview attributed string for the specified profile ID.
