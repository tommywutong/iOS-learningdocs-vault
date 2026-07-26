---
title: basedOnSize
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollbouncebehavior/basedonsize
source_url: 'https://developer.apple.com/documentation/swiftui/scrollbouncebehavior/basedonsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollbouncebehavior/basedonsize.json'
content_hash: 'sha256:777139ec11006168'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollBounceBehavior](../scrollbouncebehavior.md)

# basedOnSize

<sub>Type Property</sub>

The scrollable view bounces when its content is large enough to require scrolling.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var basedOnSize: ScrollBounceBehavior { get }
```

## Discussion

The scrollable view bounces along the specified axis if the size of the content exceeeds the size of the scrollable view in that axis.

## See Also

### Bounce behaviors

- [automatic](automatic.md) — The automatic behavior.
- [always](always.md) — The scrollable view always bounces.
