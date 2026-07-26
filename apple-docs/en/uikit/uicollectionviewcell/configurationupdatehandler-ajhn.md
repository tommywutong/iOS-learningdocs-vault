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
doc_path: /documentation/uikit/uicollectionviewcell/configurationupdatehandler-ajhn
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcell/configurationupdatehandler-ajhn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcell/configurationupdatehandler-ajhn.json'
content_hash: 'sha256:154c850a8b98b802'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewCell](../uicollectionviewcell.md)

# configurationUpdateHandler

<sub>Instance Property</sub>

A block for handling updates to the cell’s configuration using the current state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nullable) UICollectionViewCellConfigurationUpdateHandler configurationUpdateHandler;
```

## Discussion

A configuration update handler provides an alternative approach to overriding [updateConfigurationUsingState:](updateconfigurationusingstate_.md) in a subclass. Set a configuration update handler to update the cell’s configuration using the new state in response to a configuration state change:

```objc
[cell setConfigurationUpdateHandler:^(UICollectionViewCell *cell, UICellConfigurationState *state) {
    UIListContentConfiguration *content = [[UIListContentConfiguration cellConfiguration] updatedConfigurationForState:state];
    [content setText: @"Hello world!"];
    if (state.isDisabled) {
        [content.textProperties setColor:[UIColor systemGrayColor]];
    }
    [cell setContentConfiguration:content];
}];
```

Setting the value of this property calls [- setNeedsUpdateConfiguration](<setneedsupdateconfiguration().md>). The system calls this handler after calling [updateConfigurationUsingState:](updateconfigurationusingstate_.md).

In iOS 18 and later, UIKit supports automatic trait tracking inside this block for traits from this cell’s `traitCollection`. For more information, see [Automatic trait tracking](../automatic-trait-tracking.md).

This closure supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md).
