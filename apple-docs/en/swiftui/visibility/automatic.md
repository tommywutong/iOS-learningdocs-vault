---
title: Visibility.automatic
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/visibility/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/visibility/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visibility/automatic.json'
content_hash: 'sha256:050246182415d910'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Visibility](../visibility.md)

# Visibility.automatic

<sub>Case</sub>

The element may be visible or hidden depending on the policies of the component accepting the visibility configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case automatic
```

## Discussion

For example, some components employ different automatic behavior depending on factors including the platform, the surrounding container, user settings, etc.

## See Also

### Getting visibility options

- [Visibility.visible](visible.md) — The element may be visible.
- [Visibility.hidden](hidden.md) — The element may be hidden.
