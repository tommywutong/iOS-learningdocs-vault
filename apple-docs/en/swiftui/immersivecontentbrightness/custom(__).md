---
title: 'custom(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/immersivecontentbrightness/custom(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/immersivecontentbrightness/custom(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersivecontentbrightness/custom%28_%3A%29.json'
content_hash: 'sha256:3cdd6e47e17aabe1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImmersiveContentBrightness](../immersivecontentbrightness.md)

# custom(_:)

<sub>Type Method</sub>

Creates a content brightness with a custom value.

<sub>visionOS</sub>

```swift
static func custom(_ value: Double) -> ImmersiveContentBrightness
```

## Parameters

- `value` — The value of the brightness. Provide a value between 0 and 1. Larger values correspond to a brighter environment.

## See Also

### Getting brightness levels

- [automatic](automatic.md) — The default content brightness.
- [dark](dark.md) — A dark content brightness.
- [dim](dim.md) — A dimmed content brightness.
- [bright](bright.md) — A bright content brightness.
