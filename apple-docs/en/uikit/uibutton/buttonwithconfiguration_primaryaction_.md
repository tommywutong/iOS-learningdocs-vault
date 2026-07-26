---
title: 'buttonWithConfiguration:primaryAction:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibutton/buttonwithconfiguration:primaryaction:'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/buttonwithconfiguration:primaryaction:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/buttonwithconfiguration%3Aprimaryaction%3A.json'
content_hash: 'sha256:0e76c5e0135d9af1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# buttonWithConfiguration:primaryAction:

<sub>Type Method</sub>

Creates a new button with the specified configuration and registers the primary action event.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) buttonWithConfiguration:(UIButtonConfiguration *) configuration primaryAction:(UIAction *) primaryAction;
```

## Parameters

- `configuration` — The button configuration.

- `primaryAction` — The action to perform for the [UIControlEventPrimaryActionTriggered](../uicontrol/event/primaryactiontriggered.md) control event.

## Return Value

A new button.

## Discussion

If the primary action contains a title or an image, this method copies them to the configuration and the button displays them.

## See Also

### Creating buttons from a configuration object

- [UIButtonConfiguration](../uibuttonconfiguration.md) — A configuration that specifies the appearance and behavior of a button and its contents.
