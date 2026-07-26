---
title: configuration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-7gz60
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-7gz60'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-7gz60.json'
content_hash: 'sha256:5efa5c276b9f8a7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# configuration

<sub>Instance Property</sub>

The configuration for the button’s appearance.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, readwrite, nullable) UIButtonConfiguration * configuration;
```

## Discussion

Setting a configuration opts the button into a configuration system based on [UIButtonConfiguration](../uibuttonconfiguration.md). This configuration supports several options and behaviors unavailable with other configuration methods. Features include subtitle labels, extended control over background appearance, ways to transform the button configuration when the button changes state, and integration with macOS when building with Mac Catalyst.

When using a configuration, the button ignores deprecated methods and properties of [UIButton](../uibutton.md). You can combine most other methods and properties of [UIButton](../uibutton.md) with a configuration. If you have existing code to configure a button, you can set this property to take advantage of additional configuration features.

If the configuration is `nil`, other supported properties and methods of [UIButton](../uibutton.md), such as [- setTitle:forState:](<settitle(__for_).md>) , control the appearance of the button.

## See Also

### Managing the appearance with a configuration object

- [automaticallyUpdatesConfiguration](automaticallyupdatesconfiguration.md) — A Boolean value that determines whether the button configuration changes when button’s state changes.
- [- setNeedsUpdateConfiguration](<setneedsupdateconfiguration().md>) — Requests the system update the button configuration.
- [- updateConfiguration](<updateconfiguration().md>) — Updates the button configuration in response to a button state change.
- [configurationUpdateHandler](configurationupdatehandler-swift.property.md) — A closure that executes when the button state changes.
- [ConfigurationUpdateHandler](configurationupdatehandler-swift.typealias.md) — A closure to update the configuration of a button.
