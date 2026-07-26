---
title: 'appEntityIdentifier(_:)'
framework: AppIntents
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.4+, iPadOS 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/appentityidentifier(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/appentityidentifier(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/appentityidentifier%28_%3A%29.json'
content_hash: 'sha256:030cf609ce833088'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# appEntityIdentifier(_:)

<sub>Instance Method</sub>

Associates a SwiftUI view with an app entity to make its content discoverable by Apple Intelligence and Siri.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func appEntityIdentifier(_ identifier: EntityIdentifier?) -> some View

```

## Parameters

- `identifier` — The fully qualified identifier of the app entity instance you associate with the view.

## Discussion

Use this modifier to make your app entity discoverable by Apple Intelligence and Siri and provide additional context to the system when the view appears onscreen. You can associate the view with one app entity. If you apply the modifier several times on one view, the system gives precedence to the innermost modifier and discards the other modifiers.

For example, this example associates `entityA` with the `Rectangle()` and `entityB` with `BarView`. The system ignores the modifier that associates `entityC` with the `BarView`:

```swift
struct FooView {
    let entityA: EntityA
    let entityB: EntityB
    let entityC: EntityC
    var body: some View {
        BarView {
            Rectangle()
                .appEntityIdentifier(EntityIdentifier(for: EntityA.self, identifier: entityA.id))
        }
        .appEntityIdentifier(EntityIdentifier(for: EntityB.self, identifier: entityB.id))
        .appEntityIdentifier(EntityIdentifier(for: EntityC.self, identifier: entityC.id))
    }
}
```

To remove the association, set `appEntityIdentifier` to `nil`.

For more information, refer to doc:providing-contextual-cues-to-Apple-Intelligence-and-Siri and [App Intents](../../appintents.md).

## See Also

### App intents

- [appEntityIdentifier(forSelectionType:identifier:)](<appentityidentifier(forselectiontype_identifier_).md>) — Associates the items in a SwiftUI list view with app entities to make them discoverable by Apple Intelligence and Siri.
- [appEntityUIElements(_:)](<appentityuielements(__).md>) — Provides the system with additional context to make a custom view’s content discoverable by Apple Intelligence and Siri.
- [onAppIntentExecution(_:perform:)](<onappintentexecution(__perform_).md>) — Registers a handler to invoke in response to the specified app intent that your app receives.
- [shortcutsLinkStyle(_:)](<shortcutslinkstyle(__).md>) — Sets the given style for ShortcutsLinks within the view hierarchy
- [siriTipViewStyle(_:)](<siritipviewstyle(__).md>) — Sets the given style for SiriTipView within the view hierarchy
