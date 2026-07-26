---
title: 'inspectorColumnWidth(min:ideal:max:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/inspectorcolumnwidth(min:ideal:max:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/inspectorcolumnwidth(min:ideal:max:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/inspectorcolumnwidth%28min%3Aideal%3Amax%3A%29.json'
content_hash: 'sha256:1560ba43f6f403bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# inspectorColumnWidth(min:ideal:max:)

<sub>Instance Method</sub>

Sets a flexible, preferred width for the inspector in a trailing-column presentation.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
nonisolated func inspectorColumnWidth(min: CGFloat? = nil, ideal: CGFloat, max: CGFloat? = nil) -> some View

```

## Parameters

- `min` — The minimum allowed width for the trailing column inspector

- `ideal` — The initial width of the inspector in the absence of state restoration. `ideal` influences the resulting width on macOS when a user double-clicks the divider on the leading edge of the inspector. clicks a divider to readjust

- `max` — The maximum allowed width for the trailing column inspector

## Discussion

Apply this modifier on the content of a [inspector(isPresented:content:)](<inspector(ispresented_content_).md>) to specify a preferred flexible width for the column. Use [inspectorColumnWidth(_:)](<inspectorcolumnwidth(__).md>) if you need to specify a fixed width.

The following example shows an editor interface with an inspector, which when presented as a trailing-column, has a preferred width of 225 points, maximum of 400, and a minimum of 150 at which point it will collapse, if allowed.

```swift
MyEditorView()
    .inspector {
        TextTraitsInspectorView()
            .inspectorColumnWidth(min: 150, ideal: 225, max: 400)
    }
```

Only some platforms enable flexible inspector columns. If you specify a width that the current presentation environment doesn’t support, SwiftUI may use a different width for your column.

## See Also

### Presenting an inspector

- [inspector(isPresented:content:)](<inspector(ispresented_content_).md>) — Inserts an inspector at the applied position in the view hierarchy.
- [inspectorColumnWidth(_:)](<inspectorcolumnwidth(__).md>) — Sets a fixed, preferred width for the inspector containing this view when presented as a trailing column.
