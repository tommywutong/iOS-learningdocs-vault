---
title: segmented
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/pickerstyle/segmented
source_url: 'https://developer.apple.com/documentation/swiftui/pickerstyle/segmented'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pickerstyle/segmented.json'
content_hash: 'sha256:71b5bf3fbce337a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PickerStyle](../pickerstyle.md)

# segmented

<sub>Type Property</sub>

A picker style that presents the options in a segmented control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@export(implementation) static var segmented: SegmentedPickerStyle { get }
```

## Discussion

Use this style when there are two to five options. Consider using [menu](menu.md) when there are more than five options.

For each option’s label, use sentence-style capitalization without ending punctuation, like a period or colon.

To apply this style to a picker, or to a view that contains pickers, use the [pickerStyle(_:)](<../view/pickerstyle(__).md>) modifier.

## See Also

### Getting built-in picker styles

- [automatic](automatic.md) — The default picker style, based on the picker’s context.
- [inline](inline.md) — A `PickerStyle` where each option is displayed inline with other views in the current container.
- [menu](menu.md) — A picker style that presents the options as a menu when the user presses a button, or as a submenu when nested within a larger menu.
- [navigationLink](navigationlink.md) — A picker style represented by a navigation link that presents the options by pushing a List-style picker view.
- [palette](palette.md) — A picker style that presents the options as a row of compact elements.
- [radioGroup](radiogroup.md) — A picker style that presents the options as a group of radio buttons.
- [tabs](tabs.md) — A picker style that presents options as segmented tabs. _(beta)_
- [wheel](wheel.md) — A picker style that presents the options in a scrollable wheel that shows the selected option and a few neighboring options.
