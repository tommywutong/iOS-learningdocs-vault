---
title: 'listRowPlatterColor(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/listrowplattercolor(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/listrowplattercolor(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/listrowplattercolor%28_%3A%29.json'
content_hash: 'sha256:7758450c249d8e0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# listRowPlatterColor(_:)

<sub>Instance Method</sub>

Sets the color that the system applies to the row background when this view is placed in a list.

> [!warning] Deprecated
> Use [listItemTint(_:)](<listitemtint(__)-5ehdr.md>) instead.

<sub>watchOS</sub>

```swift
nonisolated func listRowPlatterColor(_ color: Color?) -> some View

```

## Parameters

- `color` — The [Color](../color.md) to apply to the system cell.

## Return Value

A view with the specified `color` applied to the system cell.

## Discussion

Use `listRowPlatterColor(_:)` to set the underlying row background color in a list.

In the example below, the `Flavor` enumeration provides content for list items. The SwiftUI [List](../list.md) builder iterates over the `Flavor` enumeration and extracts the raw value of each of its elements using the resulting text to create each list row item. After the list builder finishes, the `listRowPlatterColor(_:)` modifier sets the underlying row background color to the [Color](../color.md) you specify.

```swift
struct ContentView: View {
    enum Flavor: String, CaseIterable, Identifiable {
        var id: String { self.rawValue }
        case vanilla, chocolate, strawberry
    }

    var body: some View {
        List {
            ForEach(Flavor.allCases) {
                Text($0.rawValue)
                    .listRowPlatterColor(.green)
            }
        }
    }
}
```

## See Also

### Appearance modifiers

- [colorScheme(_:)](<colorscheme(__).md>) — Sets this view’s color scheme. _(deprecated)_
- [background(_:alignment:)](<background(__alignment_).md>) — Layers the given view behind this view. _(deprecated)_
- [overlay(_:alignment:)](<overlay(__alignment_).md>) — Layers a secondary view in front of this view. _(deprecated)_
- [foregroundColor(_:)](<foregroundcolor(__).md>) — Sets the color of the foreground elements displayed by this view. _(deprecated)_
- [complicationForeground()](<complicationforeground().md>) — Promotes this view to the foreground in a complication. _(deprecated)_
