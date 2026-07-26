---
title: cursorView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextselectiondisplayinteraction/cursorview
source_url: 'https://developer.apple.com/documentation/uikit/uitextselectiondisplayinteraction/cursorview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextselectiondisplayinteraction/cursorview.json'
content_hash: 'sha256:5c19b1253ed8ac62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSelectionDisplayInteraction](../uitextselectiondisplayinteraction.md)

# cursorView

<sub>Instance Property</sub>

The view that draws the caret at the text insertion point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var cursorView: any UIView & UITextCursorView { get set }
```

## Discussion

When you install the interaction on your text input view, the system installs a view in this property that provides the standard system appearance for the caret at the insertion point. You can replace this view with a custom one you provide to change the appearance of the caret.

## See Also

### Getting the system selection views

- [highlightView](highlightview.md) — The view that draws the selection highlight behind the rendered text.
- [handleViews](handleviews.md) — The view that draws the selection handles for the selected text.
