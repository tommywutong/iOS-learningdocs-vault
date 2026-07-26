---
title: updateConfiguration()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/updateconfiguration()
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/updateconfiguration()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/updateconfiguration%28%29.json'
content_hash: 'sha256:bf4e42d9de36e7ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# updateConfiguration()

<sub>Instance Method</sub>

Updates the button configuration in response to a button state change.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func updateConfiguration()
```

## Discussion

Override this method in your subclass to respond changes to the button’s state. Make any necessary changes and update the button’s configuration.

Don’t call this method directly. Call [- setNeedsUpdateConfiguration](<setneedsupdateconfiguration().md>) to request an update to your button.

In iOS 18 and later, UIKit supports automatic trait tracking inside this method for traits from this button’s `traitCollection`. For more information, see [Automatic trait tracking](../automatic-trait-tracking.md).

This method supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md).

## See Also

### Observing data in buttons

- [configurationUpdateHandler](configurationupdatehandler-swift.property.md) — A closure that executes when the button state changes.
