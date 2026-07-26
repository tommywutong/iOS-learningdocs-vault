---
title: directTouch
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/gestureinputkinds/directtouch
source_url: 'https://developer.apple.com/documentation/swiftui/gestureinputkinds/directtouch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gestureinputkinds/directtouch.json'
content_hash: 'sha256:f231acbe5edf2050'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GestureInputKinds](../gestureinputkinds.md)

# directTouch

<sub>Type Property</sub>

A person is touching content directly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let directTouch: GestureInputKinds
```

## Discussion

Examples:

- touching a screen directly with fingers,
- directly touching or pinching content in visionOS,
- indirectly pinching content while looking at it in visionOS.

> [!note] Note
> In visionOS, you can further customize what hand motions your gesture recognizes using [handActivationBehavior(_:)](<../gesture/handactivationbehavior(__).md>).

## See Also

### Gesture input options

- [all](all.md) — All possible gesture input kinds, present and future. _(beta)_
- [indirectTouch](indirecttouch.md) — A person is touching content indirectly. _(beta)_
- [pencil](pencil.md) — A person is touching content directly with an Apple Pencil, or an other supported pencil device. _(beta)_
- [pointer](pointer.md) — A person is pressing a mouse or a trackpad button while the pointer is pointing at content. _(beta)_
