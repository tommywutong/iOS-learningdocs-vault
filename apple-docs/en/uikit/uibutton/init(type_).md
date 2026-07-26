---
title: 'init(type:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibutton/init(type:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/init(type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/init%28type%3A%29.json'
content_hash: 'sha256:b50f1cbfc3e7c67c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# init(type:)

<sub>Initializer</sub>

Creates and returns a new button of the specified type.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(type buttonType: UIButton.ButtonType)
```

## Parameters

- `buttonType` — The button type. See [ButtonType](buttontype-swift.enum.md) for the possible values.

## Return Value

A newly created button.

## Discussion

This method is a convenience constructor for creating button objects with specific configurations.

When creating a custom button — a button with the type [UIButtonTypeCustom](buttontype-swift.enum/custom.md) — the frame of the button is set to (`0`, `0`, `0`, `0`) initially. Before adding the button to your interface, you should update the frame to a more appropriate value.

## See Also

### Related Documentation

- [UIKit Catalog: Creating and customizing views and controls](../uikit-catalog-creating-and-customizing-views-and-controls.md) — Customize your app’s user interface with views and controls.

### Creating buttons of a specific type

- [init(type:primaryAction:)](<init(type_primaryaction_).md>) — Creates a new button with the specified type, registers the primary action event, and sets the title and image to the action’s title and image.
- [ButtonType](buttontype-swift.enum.md) — Specifies the style of a button.
