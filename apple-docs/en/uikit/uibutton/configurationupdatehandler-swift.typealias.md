---
title: UIButton.ConfigurationUpdateHandler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configurationupdatehandler-swift.typealias
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configurationupdatehandler-swift.typealias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configurationupdatehandler-swift.typealias.json'
content_hash: 'sha256:d0a31999689e86a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# UIButton.ConfigurationUpdateHandler

<sub>Type Alias</sub>

A closure to update the configuration of a button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias ConfigurationUpdateHandler = (UIButton) -> Void
```

## Parameters

- `button` — The button to update.

## See Also

### Managing the appearance with a configuration object

- [configuration](configuration-5rlyb.md) — The configuration for the button’s appearance.
- [automaticallyUpdatesConfiguration](automaticallyupdatesconfiguration.md) — A Boolean value that determines whether the button configuration changes when button’s state changes.
- [- setNeedsUpdateConfiguration](<setneedsupdateconfiguration().md>) — Requests the system update the button configuration.
- [- updateConfiguration](<updateconfiguration().md>) — Updates the button configuration in response to a button state change.
- [configurationUpdateHandler](configurationupdatehandler-swift.property.md) — A closure that executes when the button state changes.
