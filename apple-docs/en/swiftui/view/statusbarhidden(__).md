---
title: 'statusBarHidden(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/statusbarhidden(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/statusbarhidden(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/statusbarhidden%28_%3A%29.json'
content_hash: 'sha256:0c3789228ff96163'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# statusBarHidden(_:)

<sub>Instance Method</sub>

Sets the visibility of the status bar.

> [!warning] Deprecated
> Use .toolbarVisibility(_, for: .statusBar) instead

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@export(implementation) nonisolated func statusBarHidden(_ hidden: Bool = true) -> some View

```

## Parameters

- `hidden` — A Boolean value that indicates whether to hide the status bar.

## See Also

### Hiding system elements

- [labelsHidden()](<labelshidden().md>) — Hides the labels of any controls contained within this view.
- [labelsVisibility(_:)](<labelsvisibility(__).md>) — Controls the visibility of labels of any controls contained within this view.
- [labelsVisibility](../environmentvalues/labelsvisibility.md) — The labels visibility set by [labelsVisibility(_:)](<labelsvisibility(__).md>).
- [menuIndicator(_:)](<menuindicator(__).md>) — Sets the menu indicator visibility for controls within this view.
- [persistentSystemOverlays(_:)](<persistentsystemoverlays(__).md>) — Sets the preferred visibility of the non-transient system views overlaying the app.
- [Visibility](../visibility.md) — The visibility of a UI element, chosen automatically based on the platform, current context, and other factors.
