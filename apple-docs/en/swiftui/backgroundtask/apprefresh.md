---
title: appRefresh
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [watchOS 9.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/backgroundtask/apprefresh
source_url: 'https://developer.apple.com/documentation/swiftui/backgroundtask/apprefresh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/backgroundtask/apprefresh.json'
content_hash: 'sha256:05b34083166cc8b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [BackgroundTask](../backgroundtask.md)

# appRefresh

<sub>Type Property</sub>

A task that updates your app’s state in the background.

> [!warning] Deprecated
> Use appRefresh(_ identifier: String)

<sub>watchOS</sub>

```swift
static var appRefresh: BackgroundTask<String?, Void> { get }
```

## See Also

### Deprecated symbols

- [snapshot](snapshot.md) — A background task used to update your app’s user interface in preparation for a snapshot.
