---
title: 'onOpenURL(perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onopenurl(perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onopenurl(perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onopenurl%28perform%3A%29.json'
content_hash: 'sha256:d35d9c6200449109'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onOpenURL(perform:)

<sub>Instance Method</sub>

Registers a handler to invoke in response to a URL that your app receives.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func onOpenURL(perform action: @escaping (URL) -> ()) -> some View

```

## Parameters

- `action` — A closure that SwiftUI calls when your app receives a Universal Link or a custom [URL](../../foundation/url.md). The closure takes the URL as an input parameter.

## Return Value

A view that handles incoming URLs.

## Discussion

Use this view modifier to receive URLs in a particular scene within your app. The scene that SwiftUI routes the incoming URL to depends on the structure of your app, what scenes are active, and other configuration. For more information, see [handlesExternalEvents(matching:)](<../scene/handlesexternalevents(matching_).md>).

UI frameworks traditionally pass Universal Links to your app using an [NSUserActivity](../../foundation/nsuseractivity.md). However, SwiftUI passes a Universal Link to your app directly as a URL, which you receive using this modifier. To receive other user activities, like when your app participates in Handoff, use the [onContinueUserActivity(_:perform:)](<oncontinueuseractivity(__perform_).md>) modifier instead.

For more information about linking into your app, see [Allowing apps and websites to link to your content](../../xcode/allowing-apps-and-websites-to-link-to-your-content.md).

## See Also

### Sending and receiving URLs

- [openURL](../environmentvalues/openurl.md) — An action that opens a URL.
- [OpenURLAction](../openurlaction.md) — An action that opens a URL.
