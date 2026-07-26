---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollbouncebehavior/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/scrollbouncebehavior/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollbouncebehavior/automatic.json'
content_hash: 'sha256:bf08b4c513a916e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollBounceBehavior](../scrollbouncebehavior.md)

# automatic

<sub>Type Property</sub>

The automatic behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var automatic: ScrollBounceBehavior { get }
```

## Discussion

The scrollable view automatically chooses whether content bounces when people scroll to the end of the view’s content. By default, scrollable views use the [always](always.md) behavior.

## See Also

### Bounce behaviors

- [always](always.md) — The scrollable view always bounces.
- [basedOnSize](basedonsize.md) — The scrollable view bounces when its content is large enough to require scrolling.
