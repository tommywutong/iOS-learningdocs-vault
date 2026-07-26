---
title: 'applicationDidFinishLaunching(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/applicationdidfinishlaunching(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationdidfinishlaunching(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/applicationdidfinishlaunching%28_%3A%29.json'
content_hash: 'sha256:92c2b7ab39772415'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# applicationDidFinishLaunching(_:)

<sub>Instance Method</sub>

Tells the delegate when the app has finished launching.

> [!warning] Deprecated
> Use [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func applicationDidFinishLaunching(_ application: UIApplication)
```

## Parameters

- `application` — The singleton app object.

## Discussion

Don’t use this method in your apps; instead, use the [- application:willFinishLaunchingWithOptions:](<application(__willfinishlaunchingwithoptions_).md>) and [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>) methods.

Your implementation of this method creates your app’s user interface and initializes the app’s data structures. If your app persists its state between launches, you would also use this method to restore your app to its previous state.

After calling this method, the app also posts a [UIApplicationDidFinishLaunchingNotification](../uiapplication/didfinishlaunchingnotification.md) notification to give interested objects a chance to respond to the initialization cycle.

## See Also

### Deprecated

- [Deprecated symbols](../uiapplicationdelegate-deprecated-symbols.md) — Symbols that are no longer supported.
