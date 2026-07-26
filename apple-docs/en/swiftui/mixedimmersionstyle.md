---
title: MixedImmersionStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/mixedimmersionstyle
source_url: 'https://developer.apple.com/documentation/swiftui/mixedimmersionstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/mixedimmersionstyle.json'
content_hash: 'sha256:d4e71441083a8a96'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# MixedImmersionStyle

<sub>Structure</sub>

An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.

<sub>visionOS</sub>

```swift
struct MixedImmersionStyle
```

## Overview

When this immersion style is selected, the immersion amount reported by the closure of [onImmersionChange(initial:_:)](<view/onimmersionchange(initial___).md>) is `0.0`.

Use [mixed](immersionstyle/mixed.md) with the [immersionStyle(selection:in:)](<scene/immersionstyle(selection_in_).md>)modifier to specify this style.

## Relationships

- **Conforms To**: [ImmersionStyle](immersionstyle.md)

## Topics

### Creating the immersion style

- [init()](<mixedimmersionstyle/init().md>)

## See Also

### Supporting types

- [AutomaticImmersionStyle](automaticimmersionstyle.md) — The default style of immersive spaces.
- [FullImmersionStyle](fullimmersionstyle.md) — An immersion style that displays unbounded content that completely replaces passthrough video.
- [ProgressiveImmersionStyle](progressiveimmersionstyle.md) — An immersion style that displays unbounded content that partially replaces passthrough video.
