---
title: always
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollbouncebehavior/always
source_url: 'https://developer.apple.com/documentation/swiftui/scrollbouncebehavior/always'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollbouncebehavior/always.json'
content_hash: 'sha256:4c48e836b8dc02cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollBounceBehavior](../scrollbouncebehavior.md)

# always

<sub>Type Property</sub>

The scrollable view always bounces.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var always: ScrollBounceBehavior { get }
```

## Discussion

The scrollable view always bounces along the specified axis, regardless of the size of the content.

## See Also

### Bounce behaviors

- [automatic](automatic.md) — The automatic behavior.
- [basedOnSize](basedonsize.md) — The scrollable view bounces when its content is large enough to require scrolling.
