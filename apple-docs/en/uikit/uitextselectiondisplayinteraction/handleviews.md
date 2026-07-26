---
title: handleViews
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextselectiondisplayinteraction/handleviews
source_url: 'https://developer.apple.com/documentation/uikit/uitextselectiondisplayinteraction/handleviews'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextselectiondisplayinteraction/handleviews.json'
content_hash: 'sha256:d70396c26edb1af1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSelectionDisplayInteraction](../uitextselectiondisplayinteraction.md)

# handleViews

<sub>Instance Property</sub>

The view that draws the selection handles for the selected text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var handleViews: [any UIView & UITextSelectionHandleView] { get set }
```

## Discussion

When you install the interaction on your text input view, the system installs two views in this property that provide the standard system appearance for the selection handles. You can replace these views with custom ones you provide to change the appearance of the selection handles.

> [!important] Important
> When assigning a value to this property, you must provide exactly two views. One view provides the leading selection handle and the other provides the trailing selection handle.

## See Also

### Getting the system selection views

- [highlightView](highlightview.md) — The view that draws the selection highlight behind the rendered text.
- [cursorView](cursorview.md) — The view that draws the caret at the text insertion point.
