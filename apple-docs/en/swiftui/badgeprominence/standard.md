---
title: standard
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/badgeprominence/standard
source_url: 'https://developer.apple.com/documentation/swiftui/badgeprominence/standard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/badgeprominence/standard.json'
content_hash: 'sha256:263b1607cf68e1f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [BadgeProminence](../badgeprominence.md)

# standard

<sub>Type Property</sub>

The standard level of prominence for a badge.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let standard: BadgeProminence
```

## Discussion

This level of prominence should be used for badges that display a value that suggests user action, such as a count of unread messages or new invitations.

In lists on macOS, this results in a badge label on a grayscale platter; and in lists on iOS, this prominence of badge has no platter.

```swift
List(mailboxes) { mailbox in
    Text(mailbox.name)
        .badge(mailbox.numberOfUnreadMessages)
}
.badgeProminence(.standard)
```

## See Also

### Getting background prominence

- [increased](increased.md) — The highest level of prominence for a badge.
- [decreased](decreased.md) — The lowest level of prominence for a badge.
