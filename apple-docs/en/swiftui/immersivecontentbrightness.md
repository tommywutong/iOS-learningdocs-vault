---
title: ImmersiveContentBrightness
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/immersivecontentbrightness
source_url: 'https://developer.apple.com/documentation/swiftui/immersivecontentbrightness'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersivecontentbrightness.json'
content_hash: 'sha256:26600cb0c8883e89'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ImmersiveContentBrightness

<sub>Structure</sub>

The content brightness of an immersive space.

<sub>visionOS</sub>

```swift
struct ImmersiveContentBrightness
```

## Overview

Use a value of this type as an input to the [immersiveContentBrightness(_:)](<scene/immersivecontentbrightness(__).md>) scene modifier to indicate the ambient content brightness of an [ImmersiveSpace](immersivespace.md).

When you do this to create an environment that’s suitable for video playback, use one of the standard brightness values like [bright](immersivecontentbrightness/bright.md), [dim](immersivecontentbrightness/dim.md), or [dark](immersivecontentbrightness/dark.md) to provide good results for most use cases. To optimize further, you can create a custom brightness using a normalized value that expresses the linear brightness ratio between a standard dynamic range white video frame and the background that surrounds the player window.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md)

## Topics

### Getting brightness levels

- [automatic](immersivecontentbrightness/automatic.md) — The default content brightness.
- [dark](immersivecontentbrightness/dark.md) — A dark content brightness.
- [dim](immersivecontentbrightness/dim.md) — A dimmed content brightness.
- [bright](immersivecontentbrightness/bright.md) — A bright content brightness.
- [custom(_:)](<immersivecontentbrightness/custom(__).md>) — Creates a content brightness with a custom value.

## See Also

### Adjusting content brightness

- [immersiveContentBrightness(_:)](<scene/immersivecontentbrightness(__).md>) — Sets the content brightness of an immersive space.
