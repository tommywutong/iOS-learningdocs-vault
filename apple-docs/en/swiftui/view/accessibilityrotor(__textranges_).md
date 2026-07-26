---
title: 'accessibilityRotor(_:textRanges:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityrotor(_:textranges:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityrotor(_:textranges:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityrotor%28_%3Atextranges%3A%29.json'
content_hash: 'sha256:24a7d44d5ecd859f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityRotor(_:textRanges:)

<sub>Instance Method</sub>

Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func accessibilityRotor(_ label: LocalizedStringResource, textRanges: [Range<String.Index>]) -> some View

```

## Parameters

- `label` — Localized label identifying this Rotor to the user.

- `textRanges` — An array of ranges that will be used to generate the entries of the Rotor.

## Discussion

An Accessibility Rotor is a shortcut for Accessibility users to quickly navigate to specific elements of the user interface, and optionally specific ranges of text within those elements.

In the following example, a Message application adds a Rotor allowing the user to navigate through all the ranges of text containing email addresses.

```swift
extension Message {
    // Ranges of special areas in the `content` text. Calculated
    // when `content` is set and then cached so that we don't have
    // to re-compute them.
    var emailAddressRanges: [Range<String.Index>]
}

struct MessageContentView: View {
    TextEditor(.constant(message.content))
        .accessibilityRotor("Email Addresses",
            textRanges: message.emailAddressRanges)
}
```

## See Also

### Working with rotors

- [accessibilityRotor(_:entries:)](<accessibilityrotor(__entries_).md>) — Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [accessibilityRotor(_:entries:entryID:entryLabel:)](<accessibilityrotor(__entries_entryid_entrylabel_).md>) — Create an Accessibility Rotor with the specified user-visible label and entries.
- [accessibilityRotor(_:entries:entryLabel:)](<accessibilityrotor(__entries_entrylabel_).md>) — Create an Accessibility Rotor with the specified user-visible label and entries.
