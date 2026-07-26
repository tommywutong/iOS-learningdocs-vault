---
title: beginRefreshing()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uirefreshcontrol/beginrefreshing()
source_url: 'https://developer.apple.com/documentation/uikit/uirefreshcontrol/beginrefreshing()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uirefreshcontrol/beginrefreshing%28%29.json'
content_hash: 'sha256:fafa3324106627f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIRefreshControl](../uirefreshcontrol.md)

# beginRefreshing()

<sub>Instance Method</sub>

Tells the control that a refresh operation was started programmatically.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func beginRefreshing()
```

## Discussion

Call this method when an external event source triggers a programmatic refresh of your scrolling view. In a table view, for example, if you use an instance of [Timer](../../foundation/timer.md) to refresh the contents of the table view periodically, you would call this method as part of your timer handler. This method updates the state of the refresh control to reflect the in-progress refresh operation. When the refresh operation ends, be sure to call the [- endRefreshing](<endrefreshing().md>) method to return the control to its default state.

## See Also

### Managing the refresh status

- [- endRefreshing](<endrefreshing().md>) — Tells the control that a refresh operation has ended.
- [refreshing](isrefreshing.md) — A Boolean value indicating whether a refresh operation has been triggered and is in progress.
