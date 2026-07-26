---
title: didFinishLaunchingNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/didfinishlaunchingnotification
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/didfinishlaunchingnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/didfinishlaunchingnotification.json'
content_hash: 'sha256:5260d77539f1a38e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# didFinishLaunchingNotification

<sub>Type Property</sub>

A notification that posts immediately after the app finishes launching.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let didFinishLaunchingNotification: NSNotification.Name
```

## Discussion

If the app was launched as a result of in remote notification targeted at it or because another app opened a URL resource claimed the posting app (the notification `object`), this notification contains a `userInfo` dictionary. You can access the contents of the dictionary using the [UIApplicationLaunchOptionsURLKey](launchoptionskey/url.md) and [UIApplicationLaunchOptionsSourceApplicationKey](launchoptionskey/sourceapplication.md) constants (for URLs), the [UIApplicationLaunchOptionsRemoteNotificationKey](launchoptionskey/remotenotification.md) constant (for remote notifications), and the [UIApplicationLaunchOptionsLocalNotificationKey](launchoptionskey/localnotification.md) constant (for local notifications). If the notification was posted for a normal app launch, there is no `userInfo` dictionary.

## See Also

### Initializing the app

- [- application:willFinishLaunchingWithOptions:](<../uiapplicationdelegate/application(__willfinishlaunchingwithoptions_).md>) — Tells the delegate that the launch process has begun.
- [- application:didFinishLaunchingWithOptions:](<../uiapplicationdelegate/application(__didfinishlaunchingwithoptions_).md>) — Tells the delegate that the launch process is almost done and the app is almost ready to run.
- [LaunchOptionsKey](launchoptionskey.md) — The keys you use to access values in the launch options dictionary that the system passes to your app at initialization.
