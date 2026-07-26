---
title: 'init(frame:primaryAction:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibutton/init(frame:primaryaction:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/init(frame:primaryaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/init%28frame%3Aprimaryaction%3A%29.json'
content_hash: 'sha256:9c80246143916509'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# init(frame:primaryAction:)

<sub>Initializer</sub>

Creates a new button with the specified frame, registers the primary action event, and sets the title and image to the action’s title and image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(frame: CGRect, primaryAction: UIAction?)
```

## Parameters

- `frame` — The frame rectangle for the view, measured in points.

- `primaryAction` — The action to perform when the button is selected. The button registers this action for the [UIControlEventPrimaryActionTriggered](../uicontrol/event/primaryactiontriggered.md) control event and sets the title and image properties to the action’s title and image.

## See Also

### Creating buttons

- [- initWithFrame:](<init(frame_).md>) — Creates a new button with the specified frame.
- [- initWithCoder:](<init(coder_).md>) — Creates a new button with data in an unarchiver.
