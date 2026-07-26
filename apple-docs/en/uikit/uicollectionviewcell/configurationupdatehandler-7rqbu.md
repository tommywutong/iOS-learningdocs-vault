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
doc_path: /documentation/uikit/uicollectionviewcell/configurationupdatehandler-7rqbu
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcell/configurationupdatehandler-7rqbu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcell/configurationupdatehandler-7rqbu.json'
content_hash: 'sha256:4ddb4d75b412122e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewCell](../uicollectionviewcell.md)

# configurationUpdateHandler

<sub>Instance Property</sub>

A block for handling updates to the cell’s configuration using the current state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var configurationUpdateHandler: UICollectionViewCell.ConfigurationUpdateHandler? { get set }
```

## Discussion

A configuration update handler provides an alternative approach to overriding [updateConfiguration(using:)](<updateconfiguration(using_).md>) in a subclass. Set a configuration update handler to update the cell’s configuration using the new state in response to a configuration state change:

```swift
cell.configurationUpdateHandler = { cell, state in
    var content = UIListContentConfiguration.cell().updated(for: state)
    content.text = "Hello world!"
    if state.isDisabled {
        content.textProperties.color = .systemGray
    }
    cell.contentConfiguration = content
}
```

Setting the value of this property calls [- setNeedsUpdateConfiguration](<setneedsupdateconfiguration().md>). The system calls this handler after calling [updateConfiguration(using:)](<updateconfiguration(using_).md>).

In iOS 18 and later, UIKit supports automatic trait tracking inside this closure for traits from this cell’s `traitCollection`. For more information, see [Automatic trait tracking](../automatic-trait-tracking.md).

This closure supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md).

## See Also

### Observing data in collection view cells

- [updateConfiguration(using:)](<updateconfiguration(using_).md>) — Updates the cell’s configuration using the current state.
