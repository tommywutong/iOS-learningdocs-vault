---
title: 'selectionContainerViewBelowText(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextselectiondisplayinteractiondelegate/selectioncontainerviewbelowtext(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextselectiondisplayinteractiondelegate/selectioncontainerviewbelowtext(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextselectiondisplayinteractiondelegate/selectioncontainerviewbelowtext%28for%3A%29.json'
content_hash: 'sha256:733bf5b1799bf50b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSelectionDisplayInteractionDelegate](../uitextselectiondisplayinteractiondelegate.md)

# selectionContainerViewBelowText(for:)

<sub>Instance Method</sub>

Returns the container view to hold the selection-related highlight and detail views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func selectionContainerViewBelowText(for interaction: UITextSelectionDisplayInteraction) -> UIView?
```

## Parameters

- `interaction` — The interaction object that manages the highlight views.

## Return Value

The view in your interface you use to manage selection-related views.

## Discussion

Implement this delegate method if you use a view other than your text input view to display selection-related content and highlights. The container view you specify must sit below the text input view itself. The interaction object uses the view you provide as the parent for the views that display the selection highlight, selection handles, and caret.
