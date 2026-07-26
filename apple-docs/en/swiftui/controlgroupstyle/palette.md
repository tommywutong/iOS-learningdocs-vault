---
title: palette
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/controlgroupstyle/palette
source_url: 'https://developer.apple.com/documentation/swiftui/controlgroupstyle/palette'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlgroupstyle/palette.json'
content_hash: 'sha256:e4332c9a38b6af4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ControlGroupStyle](../controlgroupstyle.md)

# palette

<sub>Type Property</sub>

A control group style that presents its content as a palette.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var palette: PaletteControlGroupStyle { get }
```

## Discussion

> [!note] Note
> When used outside of menus, this style is rendered as a segmented control.

Use this style to render a multi-select or a stateless palette. The following example creates a control group that contains both type of shelves:

```swift
Menu {
    // A multi select palette
    ControlGroup {
        ForEach(ColorTags.allCases) { colorTag in
            Toggle(isOn: $selectedColorTags[colorTag]) {
                Label(colorTag.name, systemImage: "circle")
            }
            .tint(colorTag.color)
        }
    }
    .controlGroupStyle(.palette)
    .paletteSelectionEffect(.symbolVariant(.fill))

    // A momentary / stateless palette
    ControlGroup {
        ForEach(Emotes.allCases) { emote in
            Button {
                sendEmote(emote)
            } label: {
                Label(emote.name, systemImage: emote.systemImage)
            }
        }
    }
    .controlGroupStyle(.palette)
}
```

To apply this style to a control group, or to a view that contains control groups, use the [controlGroupStyle(_:)](<../view/controlgroupstyle(__).md>) modifier.

## See Also

### Getting built-in control group styles

- [automatic](automatic.md) — The default control group style.
- [compactMenu](compactmenu.md) — A control group style that presents its content as a compact menu when the user presses the control, or as a submenu when nested within a larger menu.
- [menu](menu.md) — A control group style that presents its content as a menu when the user presses the control, or as a submenu when nested within a larger menu.
- [navigation](navigation.md) — The navigation control group style.
