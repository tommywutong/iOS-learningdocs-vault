---
title: setNeedsUpdateConfiguration()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/setneedsupdateconfiguration()
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/setneedsupdateconfiguration()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/setneedsupdateconfiguration%28%29.json'
content_hash: 'sha256:e191f1eae74aa248'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# setNeedsUpdateConfiguration()

<sub>Instance Method</sub>

Informs the cell to update its configuration for its current state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setNeedsUpdateConfiguration()
```

## Discussion

You call this method when you need the cell to update its configuration according to the current configuration state. The system calls this method automatically when the cell’s [configurationState](configurationstate-4xwj0.md) changes, as well as in other circumstances that may require an update. The system might combine multiple requests into a single update.

If you add custom states to the cell’s configuration state, make sure to call this method every time those custom states change.

## See Also

### Managing the state

- [configurationState](configurationstate-4xwj0.md) — The current configuration state of the cell.
- [updateConfiguration(using:)](<updateconfiguration(using_).md>) — Updates the cell’s configuration using the current state.
- [configurationUpdateHandler](configurationupdatehandler-974.md) — A block for handling updates to the cell’s configuration using the current state.
- [ConfigurationUpdateHandler](configurationupdatehandler-swift.typealias.md) — The type of block for handling updates to the cell’s configuration using the current state.
