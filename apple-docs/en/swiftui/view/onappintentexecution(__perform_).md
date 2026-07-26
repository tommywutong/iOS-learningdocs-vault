---
title: 'onAppIntentExecution(_:perform:)'
framework: AppIntents
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onappintentexecution(_:perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onappintentexecution(_:perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onappintentexecution%28_%3Aperform%3A%29.json'
content_hash: 'sha256:07b22e8a31379dea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onAppIntentExecution(_:perform:)

<sub>Instance Method</sub>

Registers a handler to invoke in response to the specified app intent that your app receives.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated func onAppIntentExecution<I>(_ intent: I.Type = I.self, perform action: @escaping @MainActor (I) -> Void) -> some View where I : TargetContentProvidingIntent

```

## Parameters

- `intent` — The type of App Intent that the `action` closure handles.

- `action` — A closure that SwiftUI calls when the specified app intent is being performed. The closure takes the app intent instance as an input parameter.

## Return Value

A view that handles the specified app intent’s perform

## Discussion

Use this view modifier to receive instances in a particular scene within your app. The scene that SwiftUI routes the incoming user activity to depends on the structure of your app, what scenes are active, and other configuration. For more information, see [handlesExternalEvents(matching:)](<../scene/handlesexternalevents(matching_).md>).

The action closure is called before the app is foregrounded. If the app intent implements a perform() method, it will be called after the action closure. This can be useful if your app intent supports running in the background via the AppIntent.IntentModes API.

> [!note] Note
> Usage of the app intent instance provided to the action closure is limited to inspecting parameter values, interactive requests like [requestValue(_:)](<../../appintents/intentparameter/requestvalue(__)-592nd.md>) or [needsValueError(_:)](<../../appintents/intentparameter/needsvalueerror(__).md>) doesn’t work.

## See Also

### App intents

- [appEntityIdentifier(_:)](<appentityidentifier(__).md>) — Associates a SwiftUI view with an app entity to make its content discoverable by Apple Intelligence and Siri.
- [appEntityIdentifier(forSelectionType:identifier:)](<appentityidentifier(forselectiontype_identifier_).md>) — Associates the items in a SwiftUI list view with app entities to make them discoverable by Apple Intelligence and Siri.
- [appEntityUIElements(_:)](<appentityuielements(__).md>) — Provides the system with additional context to make a custom view’s content discoverable by Apple Intelligence and Siri.
- [shortcutsLinkStyle(_:)](<shortcutslinkstyle(__).md>) — Sets the given style for ShortcutsLinks within the view hierarchy
- [siriTipViewStyle(_:)](<siritipviewstyle(__).md>) — Sets the given style for SiriTipView within the view hierarchy
