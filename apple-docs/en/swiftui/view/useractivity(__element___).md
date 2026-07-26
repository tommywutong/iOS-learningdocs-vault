---
title: 'userActivity(_:element:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/useractivity(_:element:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/useractivity(_:element:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/useractivity%28_%3Aelement%3A_%3A%29.json'
content_hash: 'sha256:447e15932554beca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# userActivity(_:element:_:)

<sub>Instance Method</sub>

Advertises a user activity type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func userActivity<P>(_ activityType: String, element: P?, _ update: @escaping (P, NSUserActivity) -> ()) -> some View

```

## Parameters

- `activityType` — The type of activity to advertise.

- `element` — If the element is `nil`, the handler will not be associated with the activity (and if there are no handlers, no activity is advertised). The method passes the non-`nil` element to the handler as a convenience so the handlers don’t all need to implement an early exit with `guard element = element else { return }`.

- `update` — A function that modifies the passed-in activity for advertisement.

## Discussion

The scope of the activity applies only to the scene or window the view is in.

## See Also

### Sending and receiving user activities

- [Restoring your app’s state with SwiftUI](../restoring-your-app-s-state-with-swiftui.md) — Provide app continuity for users by preserving their current activities.
- [userActivity(_:isActive:_:)](<useractivity(__isactive___).md>) — Advertises a user activity type.
- [onContinueUserActivity(_:perform:)](<oncontinueuseractivity(__perform_).md>) — Registers a handler to invoke in response to a user activity that your app receives.
