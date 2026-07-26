---
title: tabs
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/pickerstyle/tabs
source_url: 'https://developer.apple.com/documentation/swiftui/pickerstyle/tabs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pickerstyle/tabs.json'
content_hash: 'sha256:6d327911b30a7dd5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PickerStyle](../pickerstyle.md)

# tabs

<sub>Type Property</sub>

A picker style that presents options as segmented tabs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@export(implementation) static var tabs: TabsPickerStyle { get }
```

## Discussion

On macOS, this style produces a segmented picker with a visual treatment that distinguishes tab navigation from value selection. On iOS, tvOS, and visionOS, the visual appearance matches that of the standard standard `.segmented` style. On all supported platforms, VoiceOver announces options as tabs.

```swift
Picker("View", selection: $view) {
    Text("Events").tag(Views.events)
    Text("Reminders").tag(Views.reminders)
}
.pickerStyle(.tabs)
```

To apply this style to a picker, or to a view that contains pickers, use the [pickerStyle(_:)](<../view/pickerstyle(__).md>) modifier.

## See Also

### Getting built-in picker styles

- [automatic](automatic.md) — The default picker style, based on the picker’s context.
- [inline](inline.md) — A `PickerStyle` where each option is displayed inline with other views in the current container.
- [menu](menu.md) — A picker style that presents the options as a menu when the user presses a button, or as a submenu when nested within a larger menu.
- [navigationLink](navigationlink.md) — A picker style represented by a navigation link that presents the options by pushing a List-style picker view.
- [palette](palette.md) — A picker style that presents the options as a row of compact elements.
- [radioGroup](radiogroup.md) — A picker style that presents the options as a group of radio buttons.
- [segmented](segmented.md) — A picker style that presents the options in a segmented control.
- [wheel](wheel.md) — A picker style that presents the options in a scrollable wheel that shows the selected option and a few neighboring options.
