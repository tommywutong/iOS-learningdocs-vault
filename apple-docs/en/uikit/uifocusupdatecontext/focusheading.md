---
title: focusHeading
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusupdatecontext/focusheading
source_url: 'https://developer.apple.com/documentation/uikit/uifocusupdatecontext/focusheading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusupdatecontext/focusheading.json'
content_hash: 'sha256:d0a8accce7dec4dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusUpdateContext](../uifocusupdatecontext.md)

# focusHeading

<sub>Instance Property</sub>

The heading in which the focus update is occurring.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var focusHeading: UIFocusHeading { get }
```

## Discussion

To view all the possible focus heading directions, see the [UIFocusHeading](../uifocusheading.md) data type.

## See Also

### Locating focus direction

- [previouslyFocusedView](previouslyfocusedview.md) — The view that was focused before the focus update.
- [nextFocusedView](nextfocusedview.md) — The view that takes the focus after the focus update.
- [UIFocusHeading](../uifocusheading.md) — The general type of an event.
