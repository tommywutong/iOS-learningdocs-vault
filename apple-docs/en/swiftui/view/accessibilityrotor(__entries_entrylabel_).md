---
title: 'accessibilityRotor(_:entries:entryLabel:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityrotor(_:entries:entrylabel:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityrotor(_:entries:entrylabel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityrotor%28_%3Aentries%3Aentrylabel%3A%29.json'
content_hash: 'sha256:bf58b8c4032bcb78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityRotor(_:entries:entryLabel:)

<sub>Instance Method</sub>

Create an Accessibility Rotor with the specified user-visible label and entries.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func accessibilityRotor<EntryModel>(_ rotorLabelResource: LocalizedStringResource, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View where EntryModel : Identifiable

```

## Parameters

- `rotorLabelResource` — Localized label identifying this Rotor to the user.

- `entries` — An array of identifiable values that will be used to generate the entries of the Rotor. The identifiers of the `Identifiable` values must match up with identifiers in a `ForEach` or explicit `id` calls within the `ScrollView`. When the user navigates to entries from this Rotor, SwiftUI will automatically scroll them into place as needed.

- `entryLabel` — Key path on the `Identifiable` type that can be used to get a user-visible label for every Rotor entry. This is used on macOS when the user opens the list of entries for the Rotor.

## Discussion

An Accessibility Rotor is a shortcut for Accessibility users to quickly navigate to specific elements of the user interface, and optionally specific ranges of text within those elements.

Using this modifier requires that the Rotor be attached to a `ScrollView`, or an Accessibility Element directly within a `ScrollView`, such as a `ForEach`.

In the following example, a Message application creates a Rotor allowing users to navigate to specifically the messages originating from VIPs.

```swift
// `messages` is a list of `Identifiable` `Message`s that have a
// `subject`.
// `vipMessages` is a filtered version of that list containing only
// messages from VIPs.

ScrollView {
    LazyVStack {
        ForEach(messages) { message in
            MessageView(message)
        }
    }
}
.accessibilityElement(children: .contain)
.accessibilityRotor("VIPs", entries: vipMessages,
    entryLabel: \.subject)
```

## See Also

### Working with rotors

- [accessibilityRotor(_:entries:)](<accessibilityrotor(__entries_).md>) — Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [accessibilityRotor(_:entries:entryID:entryLabel:)](<accessibilityrotor(__entries_entryid_entrylabel_).md>) — Create an Accessibility Rotor with the specified user-visible label and entries.
- [accessibilityRotor(_:textRanges:)](<accessibilityrotor(__textranges_).md>) — Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
