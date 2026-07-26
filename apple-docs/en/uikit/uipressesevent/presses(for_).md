---
title: 'presses(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipressesevent/presses(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipressesevent/presses(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipressesevent/presses%28for%3A%29.json'
content_hash: 'sha256:fde5903915dbc25c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPressesEvent](../uipressesevent.md)

# presses(for:)

<sub>Instance Method</sub>

Returns the state of all physical buttons in the event that are associated with a particular gesture recognizer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func presses(for gesture: UIGestureRecognizer) -> Set<UIPress>
```

## Parameters

- `gesture` — A gesture recognizer.

## Return Value

The set of [UIPress](../uipress.md) instances that participated in this event that are associated with the gesture recognizer.

## See Also

### Reading the event button presses

- [allPresses](allpresses.md) — The state of all physical buttons in the event.
