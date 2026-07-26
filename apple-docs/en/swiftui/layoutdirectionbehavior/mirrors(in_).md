---
title: 'LayoutDirectionBehavior.mirrors(in:)'
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/layoutdirectionbehavior/mirrors(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/layoutdirectionbehavior/mirrors(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layoutdirectionbehavior/mirrors%28in%3A%29.json'
content_hash: 'sha256:6066ed0f2161dd3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LayoutDirectionBehavior](../layoutdirectionbehavior.md)

# LayoutDirectionBehavior.mirrors(in:)

<sub>Case</sub>

A behavior that mirrors when the layout direction has the specified value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case mirrors(in: LayoutDirection)
```

## Discussion

If you develop your view or shape in an LTR context, you can use `.mirrors(in: .rightToLeft)` (which is equivalent to `.mirrors`) to mirror your content when the layout direction is RTL (and keep the original version in LTR). If you developer in an RTL context, you can use `.mirrors(in: .leftToRight)` to mirror your content when the layout direction is LTR (and keep the original version in RTL).

## See Also

### Getting behaviors

- [LayoutDirectionBehavior.fixed](fixed.md) — A behavior that doesn’t mirror when the layout direction changes.
- [mirrors](mirrors.md) — A behavior that mirrors when the layout direction is right-to-left.
