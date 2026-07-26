---
title: complicationForeground()
framework: ClockKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [watchOS 7.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/view/complicationforeground()
source_url: 'https://developer.apple.com/documentation/swiftui/view/complicationforeground()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/complicationforeground%28%29.json'
content_hash: 'sha256:7e9973e877527f2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# complicationForeground()

<sub>Instance Method</sub>

Promotes this view to the foreground in a complication.

> [!warning] Deprecated
> On watchOS 9.0 or later, use WidgetKit instead

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency func complicationForeground() -> some View

```

## Return Value

A view that is in the complication foreground.

## Discussion

A view in the foreground will be tinted alongside other foreground views. The color for both the foreground and background layers is determined by the watch face.

## See Also

### Appearance modifiers

- [colorScheme(_:)](<colorscheme(__).md>) — Sets this view’s color scheme. _(deprecated)_
- [listRowPlatterColor(_:)](<listrowplattercolor(__).md>) — Sets the color that the system applies to the row background when this view is placed in a list. _(deprecated)_
- [background(_:alignment:)](<background(__alignment_).md>) — Layers the given view behind this view. _(deprecated)_
- [overlay(_:alignment:)](<overlay(__alignment_).md>) — Layers a secondary view in front of this view. _(deprecated)_
- [foregroundColor(_:)](<foregroundcolor(__).md>) — Sets the color of the foreground elements displayed by this view. _(deprecated)_
