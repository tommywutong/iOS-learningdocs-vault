---
title: ProgressiveImmersionStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 26.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/progressiveimmersionstyle
source_url: 'https://developer.apple.com/documentation/swiftui/progressiveimmersionstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/progressiveimmersionstyle.json'
content_hash: 'sha256:510fa9489ca5bb34'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ProgressiveImmersionStyle

<sub>Structure</sub>

An immersion style that displays unbounded content that partially replaces passthrough video.

<sub>macOS, visionOS</sub>

```swift
struct ProgressiveImmersionStyle
```

## Overview

Use [progressive](immersionstyle/progressive.md) with the [immersionStyle(selection:in:)](<scene/immersionstyle(selection_in_).md>)modifier to specify this style.

## Relationships

- **Conforms To**: [ImmersionStyle](immersionstyle.md)

## Topics

### Creating the immersion style

- [init()](<progressiveimmersionstyle/init().md>) — An immersion style that displays unbounded content that partially replaces passthrough video.

### Initializers

- [init(immersion:initialAmount:)](<progressiveimmersionstyle/init(immersion_initialamount_).md>) — An immersion style that displays unbounded content that partially replaces passthrough video.

### Instance Properties

- [aspectRatio](progressiveimmersionstyle/aspectratio.md) — The aspect ratio used for this instance of the style.
- [initialImmersionAmount](progressiveimmersionstyle/initialimmersionamount.md) — The initial amount of immersion used for this instance of the style.
- [maximumImmersionAmount](progressiveimmersionstyle/maximumimmersionamount.md) — The maximum amount of immersion used for this instance of the style.
- [minimumImmersionAmount](progressiveimmersionstyle/minimumimmersionamount.md) — The minimum amount of immersion used for this instance of the style.

## See Also

### Supporting types

- [AutomaticImmersionStyle](automaticimmersionstyle.md) — The default style of immersive spaces.
- [FullImmersionStyle](fullimmersionstyle.md) — An immersion style that displays unbounded content that completely replaces passthrough video.
- [MixedImmersionStyle](mixedimmersionstyle.md) — An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.
