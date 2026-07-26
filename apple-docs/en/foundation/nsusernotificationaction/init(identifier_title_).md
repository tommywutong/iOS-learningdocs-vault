---
title: 'init(identifier:title:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.10+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsusernotificationaction/init(identifier:title:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsusernotificationaction/init(identifier:title:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsusernotificationaction/init%28identifier%3Atitle%3A%29.json'
content_hash: 'sha256:a65db0bd0d2b0292'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserNotificationAction](../nsusernotificationaction.md)

# init(identifier:title:)

<sub>Initializer</sub>

Creates a user notification action with a specified identifier and title.

> [!warning] Deprecated
> All NSUserNotifications API should be replaced with UserNotifications.frameworks API

<sub>macOS</sub>

```swift
convenience init(identifier: String?, title: String?)
```

## Parameters

- `identifier` — The identifier for the action.

- `title` — A localized string suitable for display to the user.
