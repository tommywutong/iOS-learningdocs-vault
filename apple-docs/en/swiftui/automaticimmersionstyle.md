---
title: AutomaticImmersionStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 26.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/automaticimmersionstyle
source_url: 'https://developer.apple.com/documentation/swiftui/automaticimmersionstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/automaticimmersionstyle.json'
content_hash: 'sha256:33675e5197540c17'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AutomaticImmersionStyle

<sub>Structure</sub>

The default style of immersive spaces.

<sub>macOS, visionOS</sub>

```swift
struct AutomaticImmersionStyle
```

## Overview

You don’t typically use this style explicitly, but if you need to, use [automatic](immersionstyle/automatic.md) with the [immersionStyle(selection:in:)](<scene/immersionstyle(selection_in_).md>)modifier to specify this style.

## Relationships

- **Conforms To**: [ImmersionStyle](immersionstyle.md)

## Topics

### Creating the immersion style

- [init()](<automaticimmersionstyle/init().md>)

## See Also

### Supporting types

- [FullImmersionStyle](fullimmersionstyle.md) — An immersion style that displays unbounded content that completely replaces passthrough video.
- [MixedImmersionStyle](mixedimmersionstyle.md) — An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.
- [ProgressiveImmersionStyle](progressiveimmersionstyle.md) — An immersion style that displays unbounded content that partially replaces passthrough video.
