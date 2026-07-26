---
title: 'viewID(type:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scrollposition/viewid(type:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scrollposition/viewid(type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollposition/viewid%28type%3A%29.json'
content_hash: 'sha256:c4afeed0527101cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollPosition](../scrollposition.md)

# viewID(type:)

<sub>Instance Method</sub>

The id of the view positioned in the scroll view if configured to be in that position or the user has scrolled past a view with an id of matching type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func viewID<T>(type: T.Type) -> T? where T : Hashable, T : Sendable
```
