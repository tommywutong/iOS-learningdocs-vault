---
title: interactively
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrolldismisseskeyboardmode/interactively
source_url: 'https://developer.apple.com/documentation/swiftui/scrolldismisseskeyboardmode/interactively'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolldismisseskeyboardmode/interactively.json'
content_hash: 'sha256:fa5bc0c0538a4388'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollDismissesKeyboardMode](../scrolldismisseskeyboardmode.md)

# interactively

<sub>Type Property</sub>

Enable people to interactively dismiss the keyboard as part of the scroll operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
static var interactively: ScrollDismissesKeyboardMode { get }
```

## Discussion

The software keyboard’s position tracks the gesture that drives the scroll operation if the gesture crosses into the keyboard’s area of the display. People can dismiss the keyboard by scrolling it off the display, or reverse the direction of the scroll to cancel the dismissal.

## See Also

### Getting modes

- [automatic](automatic.md) — Determine the mode automatically based on the surrounding context.
- [immediately](immediately.md) — Dismiss the keyboard as soon as scrolling starts.
- [never](never.md) — Never dismiss the keyboard automatically as a result of scrolling.
