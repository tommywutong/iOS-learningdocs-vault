---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/pickerstyle/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/pickerstyle/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pickerstyle/automatic.json'
content_hash: 'sha256:3a36aedca9e34d92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PickerStyle](../pickerstyle.md)

# automatic

<sub>Type Property</sub>

The default picker style, based on the picker’s context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static var automatic: DefaultPickerStyle { get }
```

## Discussion

How a picker using the default picker style appears largely depends on the platform and the view type in which it appears. For example, in a standard view, the default picker styles by platform are:

- On iOS and watchOS the default is a wheel.
- On macOS, the default is a pop-up button.
- On tvOS, the default is a segmented control.

The default picker style may also take into account other factors — like whether the picker appears in a container view — when setting the appearance of a picker.

You can override a picker’s style. To apply the default style to a picker, or to a view that contains pickers, use the [pickerStyle(_:)](<../view/pickerstyle(__).md>) modifier.

## See Also

### Getting built-in picker styles

- [inline](inline.md) — A `PickerStyle` where each option is displayed inline with other views in the current container.
- [menu](menu.md) — A picker style that presents the options as a menu when the user presses a button, or as a submenu when nested within a larger menu.
- [navigationLink](navigationlink.md) — A picker style represented by a navigation link that presents the options by pushing a List-style picker view.
- [palette](palette.md) — A picker style that presents the options as a row of compact elements.
- [radioGroup](radiogroup.md) — A picker style that presents the options as a group of radio buttons.
- [segmented](segmented.md) — A picker style that presents the options in a segmented control.
- [tabs](tabs.md) — A picker style that presents options as segmented tabs. _(beta)_
- [wheel](wheel.md) — A picker style that presents the options in a scrollable wheel that shows the selected option and a few neighboring options.
