---
title: 'init(configuration:primaryAction:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibutton/init(configuration:primaryaction:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/init(configuration:primaryaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/init%28configuration%3Aprimaryaction%3A%29.json'
content_hash: 'sha256:95879eb9259640f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# init(configuration:primaryAction:)

<sub>Initializer</sub>

Creates a new button with the specified configuration and registers the primary action event.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency convenience init(configuration: UIButton.Configuration, primaryAction: UIAction? = nil)
```

## Parameters

- `configuration` — The button configuration.

- `primaryAction` — The action to perform for the [UIControlEventPrimaryActionTriggered](../uicontrol/event/primaryactiontriggered.md) control event.

## Discussion

If the primary action contains a title or an image, this method copies them to the configuration and the button displays them.

## See Also

### Creating buttons from a configuration object

- [Configuration](configuration-swift.struct.md) — A configuration that specifies the appearance and behavior of a button and its contents.
