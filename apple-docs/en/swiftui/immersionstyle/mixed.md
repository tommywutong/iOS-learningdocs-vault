---
title: mixed
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/immersionstyle/mixed
source_url: 'https://developer.apple.com/documentation/swiftui/immersionstyle/mixed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersionstyle/mixed.json'
content_hash: 'sha256:fe783896b917783e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImmersionStyle](../immersionstyle.md)

# mixed

<sub>Type Property</sub>

An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.

<sub>visionOS</sub>

```swift
@export(implementation) static var mixed: MixedImmersionStyle { get }
```

## Discussion

When this immersion style is selected, the immersion amount reported by the closure of [onImmersionChange(initial:_:)](<../view/onimmersionchange(initial___).md>) is `0.0`.

Use the [immersionStyle(selection:in:)](<../scene/immersionstyle(selection_in_).md>) scene modifier to specify this style for an [ImmersiveSpace](../immersivespace.md). However, this is the default immersion style if you don’t specify one.

The immersion style affects how windows interact with virtual objects in the environment. In `mixed` immersion, a virtual object obscures part or all of a window that’s behind the object. Similarly, a window obscures a virtual object that’s behind the window.

## See Also

### Getting built-in styles

- [automatic](automatic.md) — The default immersion style.
- [full](full.md) — An immersion style that displays unbounded content that completely replaces passthrough video.
- [progressive](progressive.md) — An immersion style that displays unbounded content that partially replaces passthrough video.
