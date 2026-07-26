---
title: 'buttonWithType:primaryAction:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibutton/buttonwithtype:primaryaction:'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/buttonwithtype:primaryaction:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/buttonwithtype%3Aprimaryaction%3A.json'
content_hash: 'sha256:23282c20f45905fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# buttonWithType:primaryAction:

<sub>Type Method</sub>

Creates a new button with the specified type, registers the primary action event, and sets the title and image to the action’s title and image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) buttonWithType:(UIButtonType) buttonType primaryAction:(UIAction *) primaryAction;
```

## Parameters

- `buttonType` — The type of button.

- `primaryAction` — The action to perform when the button is selected. The button registers this action for the [UIControlEventPrimaryActionTriggered](../uicontrol/event/primaryactiontriggered.md) control event and sets the title and image properties to the action’s title and image.

## See Also

### Creating buttons of a specific type

- [+ buttonWithType:](<init(type_).md>) — Creates and returns a new button of the specified type.
- [ButtonType](buttontype-swift.enum.md) — Specifies the style of a button.
