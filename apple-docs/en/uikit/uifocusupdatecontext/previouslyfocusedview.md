---
title: previouslyFocusedView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusupdatecontext/previouslyfocusedview
source_url: 'https://developer.apple.com/documentation/uikit/uifocusupdatecontext/previouslyfocusedview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusupdatecontext/previouslyfocusedview.json'
content_hash: 'sha256:24b91f84565acf0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusUpdateContext](../uifocusupdatecontext.md)

# previouslyFocusedView

<sub>Instance Property</sub>

The view that was focused before the focus update.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var previouslyFocusedView: UIView? { get }
```

## Discussion

If your app targets tvOS 10 and later, use [previouslyFocusedItem](previouslyfocuseditem.md) instead.

This property returns `nil` when no view was previously focused, such as when setting the initial focus.

## See Also

### Locating focus direction

- [nextFocusedView](nextfocusedview.md) — The view that takes the focus after the focus update.
- [focusHeading](focusheading.md) — The heading in which the focus update is occurring.
- [UIFocusHeading](../uifocusheading.md) — The general type of an event.
