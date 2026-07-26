---
title: automaticallyUpdatesConfiguration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/automaticallyupdatesconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/automaticallyupdatesconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/automaticallyupdatesconfiguration.json'
content_hash: 'sha256:e941b47bb7a9009a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# automaticallyUpdatesConfiguration

<sub>Instance Property</sub>

A Boolean value that determines whether the button configuration changes when button’s state changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var automaticallyUpdatesConfiguration: Bool { get set }
```

## Discussion

Set this property to [true](../../swift/true.md) to have the button call [updated(for:)](<configuration-swift.struct/updated(for_).md>) (Swift) or [updatedConfigurationForButton:](../uibuttonconfiguration/updatedconfigurationforbutton_.md) (Objective-C) when the button state changes and apply the changes to the button. The default value is [true](../../swift/true.md).

## See Also

### Managing the appearance with a configuration object

- [configuration](configuration-5rlyb.md) — The configuration for the button’s appearance.
- [- setNeedsUpdateConfiguration](<setneedsupdateconfiguration().md>) — Requests the system update the button configuration.
- [- updateConfiguration](<updateconfiguration().md>) — Updates the button configuration in response to a button state change.
- [configurationUpdateHandler](configurationupdatehandler-swift.property.md) — A closure that executes when the button state changes.
- [ConfigurationUpdateHandler](configurationupdatehandler-swift.typealias.md) — A closure to update the configuration of a button.
