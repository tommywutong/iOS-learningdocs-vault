---
title: 'open(_:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsextensioncontext/open(_:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsextensioncontext/open(_:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensioncontext/open%28_%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:7d87eaead1300cd7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExtensionContext](../nsextensioncontext.md)

# open(_:completionHandler:)

<sub>Instance Method</sub>

Asks the system to open a URL on behalf of the currently running app extension.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func open(_ URL: URL, completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func open(_ URL: URL) async -> Bool
```

## Parameters

- `URL` — The URL to open.

- `completionHandler` — A block/closure to be called when the URL has opened. The closure takes a single boolean parameter indicating whether the operation was successful.

## Discussion

Each extension point determines whether to support this method, or under which conditions to support this method. In iOS,  the Today and iMessage app extension points support this method. An iMessage app extension can use this method only to open its parent app, and only if the parent app is shown on the iOS home screen.

> [!important] Important
> You can use this method in a Today widget to open the widget’s containing app. If you use this method to open other apps from your Today widget, your App Store submission may require additional review. To learn more, see [App Store Review Guidelines](http://developer.apple.com/appstore/resources/approval/guidelines.html) and [iOS Human Interface Guidelines](https://developer.apple.com/ios/human-interface-guidelines/).
