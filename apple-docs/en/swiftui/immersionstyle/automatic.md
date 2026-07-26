---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 26.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/immersionstyle/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/immersionstyle/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersionstyle/automatic.json'
content_hash: 'sha256:b759c0f55da85b76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImmersionStyle](../immersionstyle.md)

# automatic

<sub>Type Property</sub>

The default immersion style.

<sub>macOS, visionOS</sub>

```swift
@export(implementation) static var automatic: AutomaticImmersionStyle { get }
```

## Discussion

The system uses this style for an [ImmersiveSpace](../immersivespace.md) if you don’t provide an [immersionStyle(selection:in:)](<../scene/immersionstyle(selection_in_).md>) scene modifier. You don’t typically specify the `automatic` style explicitly.

By default, on visionOS, the system uses the [mixed](mixed.md) immersion style as the `automatic` style and for macOS the [full](full.md) immersion style as the `automatic` style.

## See Also

### Getting built-in styles

- [full](full.md) — An immersion style that displays unbounded content that completely replaces passthrough video.
- [mixed](mixed.md) — An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.
- [progressive](progressive.md) — An immersion style that displays unbounded content that partially replaces passthrough video.
