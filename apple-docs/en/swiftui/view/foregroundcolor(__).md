---
title: 'foregroundColor(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/foregroundcolor(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/foregroundcolor(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/foregroundcolor%28_%3A%29.json'
content_hash: 'sha256:69cf9c24d9b7a16f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# foregroundColor(_:)

<sub>Instance Method</sub>

Sets the color of the foreground elements displayed by this view.

> [!warning] Deprecated
> Use [foregroundStyle(_:)](<foregroundstyle(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func foregroundColor(_ color: Color?) -> some View

```

## Parameters

- `color` — The foreground color to use when displaying this view. Pass `nil` to remove any custom foreground color and to allow the system or the container to provide its own foreground color. If a container-specific override doesn’t exist, the system uses the primary color.

## Return Value

A view that uses the foreground color you supply.

## See Also

### Appearance modifiers

- [colorScheme(_:)](<colorscheme(__).md>) — Sets this view’s color scheme. _(deprecated)_
- [listRowPlatterColor(_:)](<listrowplattercolor(__).md>) — Sets the color that the system applies to the row background when this view is placed in a list. _(deprecated)_
- [background(_:alignment:)](<background(__alignment_).md>) — Layers the given view behind this view. _(deprecated)_
- [overlay(_:alignment:)](<overlay(__alignment_).md>) — Layers a secondary view in front of this view. _(deprecated)_
- [complicationForeground()](<complicationforeground().md>) — Promotes this view to the foreground in a complication. _(deprecated)_
