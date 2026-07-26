---
title: 'updateConfigurationUsingState:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewcell/updateconfigurationusingstate:'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/updateconfigurationusingstate:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/updateconfigurationusingstate%3A.json'
content_hash: 'sha256:bdeb989d77275634'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# updateConfigurationUsingState:

<sub>Instance Method</sub>

Updates the cell’s configuration using the current state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) updateConfigurationUsingState:(UICellConfigurationState *) state;
```

## Discussion

Avoid calling this method directly. Instead, use [- setNeedsUpdateConfiguration](<setneedsupdateconfiguration().md>) to request an update.

Override this method in a subclass to update the cell’s configuration using the provided state.

In iOS 18 and later, UIKit supports automatic trait tracking inside this method for traits from this cell’s `traitCollection`. For more information, see [Automatic trait tracking](../automatic-trait-tracking.md).

This method supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md).

## See Also

### Table view cells

- [configurationUpdateHandler](configurationupdatehandler-746ya.md) — A block for handling updates to the cell’s configuration using the current state.
