---
title: 'colorScheme(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/colorscheme(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/colorscheme(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/colorscheme%28_%3A%29.json'
content_hash: 'sha256:5db1342b58a94512'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# colorScheme(_:)

<sub>Instance Method</sub>

Sets this view’s color scheme.

> [!warning] Deprecated
> Use [preferredColorScheme(_:)](<preferredcolorscheme(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func colorScheme(_ colorScheme: ColorScheme) -> some View

```

## Parameters

- `colorScheme` — The color scheme for this view.

## Return Value

A view that sets this view’s color scheme.

## Discussion

Use `colorScheme(_:)` to set the color scheme for the view to which you apply it and any subviews.

## See Also

### Appearance modifiers

- [listRowPlatterColor(_:)](<listrowplattercolor(__).md>) — Sets the color that the system applies to the row background when this view is placed in a list. _(deprecated)_
- [background(_:alignment:)](<background(__alignment_).md>) — Layers the given view behind this view. _(deprecated)_
- [overlay(_:alignment:)](<overlay(__alignment_).md>) — Layers a secondary view in front of this view. _(deprecated)_
- [foregroundColor(_:)](<foregroundcolor(__).md>) — Sets the color of the foreground elements displayed by this view. _(deprecated)_
- [complicationForeground()](<complicationforeground().md>) — Promotes this view to the foreground in a complication. _(deprecated)_
