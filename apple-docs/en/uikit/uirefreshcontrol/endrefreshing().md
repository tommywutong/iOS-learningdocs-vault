---
title: endRefreshing()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uirefreshcontrol/endrefreshing()
source_url: 'https://developer.apple.com/documentation/uikit/uirefreshcontrol/endrefreshing()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uirefreshcontrol/endrefreshing%28%29.json'
content_hash: 'sha256:7567894add4bf865'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIRefreshControl](../uirefreshcontrol.md)

# endRefreshing()

<sub>Instance Method</sub>

Tells the control that a refresh operation has ended.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func endRefreshing()
```

## Discussion

Call this method at the end of any refresh operation (whether it was initiated programmatically or by the user) to return the refresh control to its default state. If the refresh control is at least partially visible, calling this method also hides it. If animations are also enabled, the control is hidden using an animation.

## See Also

### Managing the refresh status

- [- beginRefreshing](<beginrefreshing().md>) — Tells the control that a refresh operation was started programmatically.
- [refreshing](isrefreshing.md) — A Boolean value indicating whether a refresh operation has been triggered and is in progress.
