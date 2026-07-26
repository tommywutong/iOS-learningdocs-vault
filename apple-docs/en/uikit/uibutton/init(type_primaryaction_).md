---
title: 'init(type:primaryAction:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibutton/init(type:primaryaction:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/init(type:primaryaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/init%28type%3Aprimaryaction%3A%29.json'
content_hash: 'sha256:2a4458816db81d3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# init(type:primaryAction:)

<sub>Initializer</sub>

Creates a new button with the specified type, registers the primary action event, and sets the title and image to the action’s title and image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency convenience init(type buttonType: UIButton.ButtonType = .system, primaryAction: UIAction?)
```

## Parameters

- `buttonType` — The type of button.

- `primaryAction` — The action to perform when the button is selected. The button registers this action for the [UIControlEventPrimaryActionTriggered](../uicontrol/event/primaryactiontriggered.md) control event and sets the title and image properties to the action’s title and image.

## See Also

### Creating buttons of a specific type

- [+ buttonWithType:](<init(type_).md>) — Creates and returns a new button of the specified type.
- [ButtonType](buttontype-swift.enum.md) — Specifies the style of a button.
