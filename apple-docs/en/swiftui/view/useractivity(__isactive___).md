---
title: 'userActivity(_:isActive:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/useractivity(_:isactive:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/useractivity(_:isactive:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/useractivity%28_%3Aisactive%3A_%3A%29.json'
content_hash: 'sha256:f014e2ffc82d72fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# userActivity(_:isActive:_:)

<sub>Instance Method</sub>

Advertises a user activity type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func userActivity(_ activityType: String, isActive: Bool = true, _ update: @escaping (NSUserActivity) -> ()) -> some View

```

## Parameters

- `activityType` — The type of activity to advertise.

- `isActive` — When `false`, avoids advertising the activity. Defaults to `true`.

- `update` — A function that modifies the passed-in activity for advertisement.

## Discussion

You can use `userActivity(_:isActive:_:)` to start, stop, or modify the advertisement of a specific type of user activity.

The scope of the activity applies only to the scene or window the view is in.

## See Also

### Sending and receiving user activities

- [Restoring your app’s state with SwiftUI](../restoring-your-app-s-state-with-swiftui.md) — Provide app continuity for users by preserving their current activities.
- [userActivity(_:element:_:)](<useractivity(__element___).md>) — Advertises a user activity type.
- [onContinueUserActivity(_:perform:)](<oncontinueuseractivity(__perform_).md>) — Registers a handler to invoke in response to a user activity that your app receives.
