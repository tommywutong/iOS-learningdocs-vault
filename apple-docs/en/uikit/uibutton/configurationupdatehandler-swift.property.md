---
title: configurationUpdateHandler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configurationupdatehandler-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configurationupdatehandler-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configurationupdatehandler-swift.property.json'
content_hash: 'sha256:b2a0a5d4f2c17aeb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# configurationUpdateHandler

<sub>Instance Property</sub>

A closure that executes when the button state changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var configurationUpdateHandler: UIButton.ConfigurationUpdateHandler? { get set }
```

## Discussion

Use this property as an alternative to overriding [- updateConfiguration](<updateconfiguration().md>). Set a closure to respond to button state changes by updating the button configuration.

In iOS 18 and later, UIKit supports automatic trait tracking inside this closure for traits from this button’s `traitCollection`. For more information, see [Automatic trait tracking](../automatic-trait-tracking.md).

This closure supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md).

## See Also

### Observing data in buttons

- [- updateConfiguration](<updateconfiguration().md>) — Updates the button configuration in response to a button state change.
