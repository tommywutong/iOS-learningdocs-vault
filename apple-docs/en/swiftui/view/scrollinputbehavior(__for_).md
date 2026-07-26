---
title: 'scrollInputBehavior(_:for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/scrollinputbehavior(_:for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/scrollinputbehavior(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/scrollinputbehavior%28_%3Afor%3A%29.json'
content_hash: 'sha256:1b8e20d6a7d0a0c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# scrollInputBehavior(_:for:)

<sub>Instance Method</sub>

Enables or disables scrolling in scrollable views when using particular inputs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func scrollInputBehavior(_ behavior: ScrollInputBehavior, for input: ScrollInputKind) -> some View

```

## Parameters

- `behavior` — Whether scrolling should be enabled or disabled for this input.

- `input` — The input for which to enable or disable scrolling.

## Discussion

In contrast to [scrollDisabled(_:)](<scrolldisabled(__).md>), this modifier will enable or disable scrolling only for particular inputs. The following, for instance, disables double-tap-to-scroll on watchOS while preserving the ability to scroll via touch and the Digital Crown:

```swift
ScrollView(...)
    .scrollInputBehavior(.disabled, for: .handGestureShortcut)
```

If `scrollDisabled(true)` has been applied to this view, scrolling will be disabled for all inputs and this modifier cannot be used to re-enable scrolling.

## See Also

### Managing scrolling for different inputs

- [ScrollInputKind](../scrollinputkind.md) — Inputs used to scroll views.
- [ScrollInputBehavior](../scrollinputbehavior.md) — A type that defines whether input should scroll a view.
