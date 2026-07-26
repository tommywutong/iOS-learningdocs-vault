---
title: 'init(_:textRange:prepare:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/accessibilityrotorentry/init(_:textrange:prepare:)'
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilityrotorentry/init(_:textrange:prepare:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilityrotorentry/init%28_%3Atextrange%3Aprepare%3A%29.json'
content_hash: 'sha256:0160c6da045eee59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AccessibilityRotorEntry](../accessibilityrotorentry.md)

# init(_:textRange:prepare:)

<sub>Initializer</sub>

Create a Rotor entry with a specific label and range. This Rotor entry will be associated with the Accessibility element that owns the Rotor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) init(_ label: LocalizedStringResource, textRange: Range<String.Index>, prepare: @escaping () -> Void = {}) where ID == Never
```

## Parameters

- `label` — Localized string used to show this Rotor entry to users. If no label is specified, the Rotor entry will be labeled based on the text at that range.

- `prepare` — Optional closure to run before a Rotor entry is navigated to, to prepare the UI as needed. This can be used to bring the UI element or text on-screen if it isn’t already, and SwiftUI not able to automatically scroll to it.

## See Also

### Creating a rotor entry

- [init(_:id:textRange:prepare:)](<init(__id_textrange_prepare_).md>) — Create a Rotor entry with a specific label and identifier, with an optional range.
