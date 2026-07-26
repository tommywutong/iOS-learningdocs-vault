---
title: configurationUpdateHandler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewheaderfooterview/configurationupdatehandler-3oji2
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/configurationupdatehandler-3oji2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewheaderfooterview/configurationupdatehandler-3oji2.json'
content_hash: 'sha256:49a7ab03dccada85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md)

# configurationUpdateHandler

<sub>Instance Property</sub>

A block for handling updates to the view’s configuration using the current state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nullable) UITableViewHeaderFooterViewConfigurationUpdateHandler configurationUpdateHandler;
```

## Discussion

A configuration update handler provides an alternative approach to overriding [updateConfigurationUsingState:](updateconfigurationusingstate_.md) in a subclass. Set a configuration update handler to update the header footer view’s configuration using the new state in response to a configuration state change.

Setting the value of this property calls [- setNeedsUpdateConfiguration](<setneedsupdateconfiguration().md>). The system calls this handler after calling [updateConfigurationUsingState:](updateconfigurationusingstate_.md).

In iOS 18 and later, UIKit supports automatic trait tracking inside this block for traits from this view’s `traitCollection`. For more information, see [Automatic trait tracking](../automatic-trait-tracking.md).

This closure supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md).
