---
title: invalidateDetents()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisheetpresentationcontroller/invalidatedetents()
source_url: 'https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/invalidatedetents()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisheetpresentationcontroller/invalidatedetents%28%29.json'
content_hash: 'sha256:b6e64be591064c59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISheetPresentationController](../uisheetpresentationcontroller.md)

# invalidateDetents()

<sub>Instance Method</sub>

Notifies the sheet to re-evaluate its detent value in the next layout pass.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func invalidateDetents()
```

## Discussion

When an external input (like a captured property) to a custom detent changes, call this method to notify the sheet to re-evaluate the detent.

To animate custom detents to their new heights, call this method within [- animateChanges:](<animatechanges(__).md>).

> [!note] Note
> You don’t need to call this method if [detents](detents.md) only contains system detents, or if your custom detents only use information from the passed-in context.
