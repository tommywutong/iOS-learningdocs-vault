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
doc_path: /documentation/uikit/uitableviewheaderfooterview/setneedsupdateconfiguration()
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/setneedsupdateconfiguration()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewheaderfooterview/setneedsupdateconfiguration%28%29.json'
content_hash: 'sha256:a55caac51d60428b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md)

# setNeedsUpdateConfiguration()

<sub>Instance Method</sub>

Informs the view to update its configuration for its current state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setNeedsUpdateConfiguration()
```

## Discussion

You call this method when you need the view to update its configuration according to the current configuration state. The system calls this method automatically when the view’s [configurationState](configurationstate-7xj7r.md) changes, as well as in other circumstances that may require an update. The system might combine multiple requests into a single update.

If you add custom states to the view’s configuration state, make sure to call this method every time those custom states change.

## See Also

### Managing the state

- [configurationState](configurationstate-7xj7r.md) — The current configuration state of the view.
- [updateConfiguration(using:)](<updateconfiguration(using_).md>) — Updates the view’s configuration using the current state.
- [configurationUpdateHandler](configurationupdatehandler-49slo.md) — A block for handling updates to the view’s configuration using the current state.
- [ConfigurationUpdateHandler](configurationupdatehandler-swift.typealias.md) — The type of block for handling updates to the view’s configuration using the current state.
