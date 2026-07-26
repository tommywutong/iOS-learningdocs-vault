---
title: FullImmersionStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 26.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/fullimmersionstyle
source_url: 'https://developer.apple.com/documentation/swiftui/fullimmersionstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/fullimmersionstyle.json'
content_hash: 'sha256:03cdc4e2a0170fe9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# FullImmersionStyle

<sub>Structure</sub>

An immersion style that displays unbounded content that completely replaces passthrough video.

<sub>macOS, visionOS</sub>

```swift
struct FullImmersionStyle
```

## Overview

When this immersion style is selected, the immersion amount reported by the closure of [onImmersionChange(initial:_:)](<view/onimmersionchange(initial___).md>) is `1.0`.

Use [full](immersionstyle/full.md) with the [immersionStyle(selection:in:)](<scene/immersionstyle(selection_in_).md>)modifier to specify this style.

## Relationships

- **Conforms To**: [ImmersionStyle](immersionstyle.md)

## Topics

### Creating the immersion style

- [init()](<fullimmersionstyle/init().md>)

## See Also

### Supporting types

- [AutomaticImmersionStyle](automaticimmersionstyle.md) — The default style of immersive spaces.
- [MixedImmersionStyle](mixedimmersionstyle.md) — An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.
- [ProgressiveImmersionStyle](progressiveimmersionstyle.md) — An immersion style that displays unbounded content that partially replaces passthrough video.
