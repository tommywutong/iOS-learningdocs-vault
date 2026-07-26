---
title: nextFocusedView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusupdatecontext/nextfocusedview
source_url: 'https://developer.apple.com/documentation/uikit/uifocusupdatecontext/nextfocusedview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusupdatecontext/nextfocusedview.json'
content_hash: 'sha256:9b2325d3c4bd52d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusUpdateContext](../uifocusupdatecontext.md)

# nextFocusedView

<sub>Instance Property</sub>

The view that takes the focus after the focus update.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var nextFocusedView: UIView? { get }
```

## Discussion

If your app targets tvOS 10 and later, use [nextFocusedItem](nextfocuseditem.md) instead.

This property returns `nil` if no view will be focused after the update.

## See Also

### Locating focus direction

- [previouslyFocusedView](previouslyfocusedview.md) — The view that was focused before the focus update.
- [focusHeading](focusheading.md) — The heading in which the focus update is occurring.
- [UIFocusHeading](../uifocusheading.md) — The general type of an event.
