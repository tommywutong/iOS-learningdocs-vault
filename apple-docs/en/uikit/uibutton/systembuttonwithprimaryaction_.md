---
title: 'systemButtonWithPrimaryAction:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibutton/systembuttonwithprimaryaction:'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/systembuttonwithprimaryaction:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/systembuttonwithprimaryaction%3A.json'
content_hash: 'sha256:2350e452957d1e2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# systemButtonWithPrimaryAction:

<sub>Type Method</sub>

Creates and returns a system type button, registers the primary action event, and sets the title and image to the action’s title and image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) systemButtonWithPrimaryAction:(UIAction *) primaryAction;
```

## Parameters

- `primaryAction` — The action to perform when the button is selected. The button registers this action for the [UIControlEventPrimaryActionTriggered](../uicontrol/event/primaryactiontriggered.md) control event and sets the title and image properties to the action’s title and image.

## See Also

### Creating system buttons

- [+ systemButtonWithImage:target:action:](<systembutton(with_target_action_).md>) — Creates and returns a system type button with specified image, target, and action.
