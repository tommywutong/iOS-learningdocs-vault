---
title: increased
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/badgeprominence/increased
source_url: 'https://developer.apple.com/documentation/swiftui/badgeprominence/increased'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/badgeprominence/increased.json'
content_hash: 'sha256:2fe4d3c574316382'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [BadgeProminence](../badgeprominence.md)

# increased

<sub>Type Property</sub>

The highest level of prominence for a badge.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let increased: BadgeProminence
```

## Discussion

This level of prominence should be used for badges that display a value that requires user action, such as number of updates or account errors.

In lists on iOS and macOS, this results in badge labels being displayed on a red platter.

```swift
ForEach(accounts) { account in
    Text(account.userName)
        .badge(account.setupErrors)
        .badgeProminence(.increased)
}
```

## See Also

### Getting background prominence

- [standard](standard.md) — The standard level of prominence for a badge.
- [decreased](decreased.md) — The lowest level of prominence for a badge.
