---
title: UIApplication.State.inactive
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/state/inactive
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/state/inactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/state/inactive.json'
content_hash: 'sha256:9d547dff8bc9552e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIApplication](../../uiapplication.md) · [State](../state.md)

# UIApplication.State.inactive

<sub>Case</sub>

The app is running in the foreground but isn’t receiving events.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case inactive
```

## Discussion

This might happen as a result of an interruption or because the app is transitioning to or from the background.

## See Also

### Constants

- [UIApplicationStateActive](active.md) — The app is running in the foreground and currently receiving events.
- [UIApplicationStateBackground](background.md) — The app is running in the background.
