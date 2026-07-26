---
title: Visibility.visible
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/visibility/visible
source_url: 'https://developer.apple.com/documentation/swiftui/visibility/visible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visibility/visible.json'
content_hash: 'sha256:60014be3958c6d91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Visibility](../visibility.md)

# Visibility.visible

<sub>Case</sub>

The element may be visible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case visible
```

## Discussion

Some APIs may use this value to represent a hint or preference, rather than a mandatory assertion. For example, setting list row separator visibility to `visible` using the [listRowSeparator(_:edges:)](<../view/listrowseparator(__edges_).md>) modifier may not always result in any visible separators, especially for list styles that do not include separators as part of their design.

## See Also

### Getting visibility options

- [Visibility.automatic](automatic.md) — The element may be visible or hidden depending on the policies of the component accepting the visibility configuration.
- [Visibility.hidden](hidden.md) — The element may be hidden.
