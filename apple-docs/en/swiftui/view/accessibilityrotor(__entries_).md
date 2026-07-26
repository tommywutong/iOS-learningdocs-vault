---
title: 'accessibilityRotor(_:entries:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityrotor(_:entries:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityrotor(_:entries:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityrotor%28_%3Aentries%3A%29.json'
content_hash: 'sha256:f96dc322f7f44921'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityRotor(_:entries:)

<sub>Instance Method</sub>

Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func accessibilityRotor<Content>(_ label: LocalizedStringResource, @ContentBuilder entries: @escaping () -> Content) -> some View where Content : AccessibilityRotorContent

```

## Parameters

- `label` — Localized label identifying this Rotor to the user.

- `entries` — Content used to generate Rotor entries. This can include AccessibilityRotorEntry structs, as well as constructs such as if and ForEach.

## Discussion

An Accessibility Rotor is a shortcut for Accessibility users to quickly navigate to specific elements of the user interface, and optionally specific ranges of text within those elements.

In the following example, a Message application creates a Rotor allowing users to navigate to specifically the messages originating from VIPs.

```swift
// `messages` is a list of `Identifiable` `Message`s.

ScrollView {
    LazyVStack {
        ForEach(messages) { message in
            MessageView(message)
        }
    }
}
.accessibilityElement(children: .contain)
.accessibilityRotor("VIPs") {
    // Not all the MessageViews are generated at once, the model
    // knows about all the messages.
    ForEach(messages) { message in
        // If the Message is from a VIP, make a Rotor entry for it.
        if message.isVIP {
            AccessibilityRotorEntry(message.subject, id: message.id)
        }
    }
}
```

## See Also

### Working with rotors

- [accessibilityRotor(_:entries:entryID:entryLabel:)](<accessibilityrotor(__entries_entryid_entrylabel_).md>) — Create an Accessibility Rotor with the specified user-visible label and entries.
- [accessibilityRotor(_:entries:entryLabel:)](<accessibilityrotor(__entries_entrylabel_).md>) — Create an Accessibility Rotor with the specified user-visible label and entries.
- [accessibilityRotor(_:textRanges:)](<accessibilityrotor(__textranges_).md>) — Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
