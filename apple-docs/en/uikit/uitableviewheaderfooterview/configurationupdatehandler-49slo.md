---
title: configurationUpdateHandler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewheaderfooterview/configurationupdatehandler-49slo
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/configurationupdatehandler-49slo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewheaderfooterview/configurationupdatehandler-49slo.json'
content_hash: 'sha256:108c7817d4e89e9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md)

# configurationUpdateHandler

<sub>Instance Property</sub>

A block for handling updates to the view’s configuration using the current state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var configurationUpdateHandler: UITableViewHeaderFooterView.ConfigurationUpdateHandler? { get set }
```

## Discussion

A configuration update handler provides an alternative approach to overriding [updateConfiguration(using:)](<../uicollectionviewcell/updateconfiguration(using_).md>) in a subclass. Set a configuration update handler to update the header footer view’s configuration using the new state in response to a configuration state change.

Setting the value of this property calls [- setNeedsUpdateConfiguration](<setneedsupdateconfiguration().md>). The system calls this handler after calling [updateConfiguration(using:)](<../uicollectionviewcell/updateconfiguration(using_).md>).

In iOS 18 and later, UIKit supports automatic trait tracking inside this closure for traits from this view’s `traitCollection`. For more information, see [Automatic trait tracking](../automatic-trait-tracking.md).

This closure supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md).

## See Also

### Observing data in table header and footer views

- [updateConfiguration(using:)](<updateconfiguration(using_).md>) — Updates the view’s configuration using the current state.
