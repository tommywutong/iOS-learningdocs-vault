---
title: 'onContinueUserActivity(_:perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/oncontinueuseractivity(_:perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/oncontinueuseractivity(_:perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/oncontinueuseractivity%28_%3Aperform%3A%29.json'
content_hash: 'sha256:f6441441ba86b34a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onContinueUserActivity(_:perform:)

<sub>Instance Method</sub>

Registers a handler to invoke in response to a user activity that your app receives.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func onContinueUserActivity(_ activityType: String, perform action: @escaping (NSUserActivity) -> ()) -> some View

```

## Parameters

- `activityType` — The type of activity that the `action` closure handles. Be sure that this string matches one of the values that you list in the [NSUserActivityTypes](../../bundleresources/information-property-list/nsuseractivitytypes.md) array in your app’s Information Property List.

- `action` — A closure that SwiftUI calls when your app receives a user activity of the specified type. The closure takes the activity as an input parameter.

## Return Value

A view that handles incoming user activities.

## Discussion

Use this view modifier to receive [NSUserActivity](../../foundation/nsuseractivity.md) instances in a particular scene within your app. The scene that SwiftUI routes the incoming user activity to depends on the structure of your app, what scenes are active, and other configuration. For more information, see [handlesExternalEvents(matching:)](<../scene/handlesexternalevents(matching_).md>).

UI frameworks traditionally pass Universal Links to your app using a user activity. However, SwiftUI passes a Universal Link to your app directly as a URL. To receive a Universal Link, use the [onOpenURL(perform:)](<onopenurl(perform_).md>) modifier instead.

## See Also

### Sending and receiving user activities

- [Restoring your app’s state with SwiftUI](../restoring-your-app-s-state-with-swiftui.md) — Provide app continuity for users by preserving their current activities.
- [userActivity(_:element:_:)](<useractivity(__element___).md>) — Advertises a user activity type.
- [userActivity(_:isActive:_:)](<useractivity(__isactive___).md>) — Advertises a user activity type.
