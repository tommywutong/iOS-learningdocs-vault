---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/delegate.json'
content_hash: 'sha256:004dd300a6f449a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# delegate

<sub>Instance Property</sub>

The delegate of the app object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
unowned(unsafe) var delegate: (any UIApplicationDelegate)? { get set }
```

## Discussion

Every app must have an app delegate object to respond to app-related messages. For example, the app notifies its delegate when the app finishes launching and when its foreground or background execution status changes. Similarly, app-related messages coming from the system are often routed to the app delegate for handling. Xcode provides an initial app delegate for every app and you should not need to change this delegate later.

The delegate must adopt the [UIApplicationDelegate](../uiapplicationdelegate.md) formal protocol.

## See Also

### Configuring your app’s behavior

- [UIApplicationDelegate](../uiapplicationdelegate.md) — A set of methods to manage shared behaviors for your app.
