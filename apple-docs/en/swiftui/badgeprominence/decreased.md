---
title: decreased
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/badgeprominence/decreased
source_url: 'https://developer.apple.com/documentation/swiftui/badgeprominence/decreased'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/badgeprominence/decreased.json'
content_hash: 'sha256:7425d507d230ee2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [BadgeProminence](../badgeprominence.md)

# decreased

<sub>Type Property</sub>

The lowest level of prominence for a badge.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let decreased: BadgeProminence
```

## Discussion

This level or prominence should be used for badges that display a value of passive information that requires no user action, such as total number of messages or content.

In lists on iOS and macOS, this results in badge labels being displayed without any extra decoration. On iOS, this looks the same as `.standard`.

```swift
List(folders) { folder in
    Text(folder.name)
        .badge(folder.numberOfItems)
}
.badgeProminence(.decreased)
```

## See Also

### Getting background prominence

- [standard](standard.md) — The standard level of prominence for a badge.
- [increased](increased.md) — The highest level of prominence for a badge.
