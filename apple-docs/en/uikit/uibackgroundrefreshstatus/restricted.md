---
title: UIBackgroundRefreshStatus.restricted
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibackgroundrefreshstatus/restricted
source_url: 'https://developer.apple.com/documentation/uikit/uibackgroundrefreshstatus/restricted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibackgroundrefreshstatus/restricted.json'
content_hash: 'sha256:8fea249e1c6485c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBackgroundRefreshStatus](../uibackgroundrefreshstatus.md)

# UIBackgroundRefreshStatus.restricted

<sub>Case</sub>

Background updates are unavailable and the user cannot enable them again.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case restricted
```

## Discussion

For example, this status can occur when parental controls are in effect for the current user.

## See Also

### Constants

- [UIBackgroundRefreshStatusDenied](denied.md) — The user explicitly disabled background behavior for this app or for the whole system.
- [UIBackgroundRefreshStatusAvailable](available.md) — Background updates are available for the app.
