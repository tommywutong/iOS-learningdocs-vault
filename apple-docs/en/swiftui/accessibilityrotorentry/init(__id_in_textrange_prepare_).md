---
title: 'init(_:id:in:textRange:prepare:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/accessibilityrotorentry/init(_:id:in:textrange:prepare:)'
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilityrotorentry/init(_:id:in:textrange:prepare:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilityrotorentry/init%28_%3Aid%3Ain%3Atextrange%3Aprepare%3A%29.json'
content_hash: 'sha256:7e9645e061a78693'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AccessibilityRotorEntry](../accessibilityrotorentry.md)

# init(_:id:in:textRange:prepare:)

<sub>Initializer</sub>

Create a Rotor entry with a specific label, identifier and namespace, and with an optional range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) init(_ label: LocalizedStringResource, id: ID, in namespace: Namespace.ID, textRange: Range<String.Index>? = nil, prepare: @escaping () -> Void = {})
```

## Parameters

- `label` — Localized string used to show this Rotor entry to users.

- `id` — Used to find the UI element associated with this Rotor entry. This identifier and namespace should match a call to `accessibilityRotorEntry(id:in)`.

- `namespace` — Namespace for this identifier. Should match a call to `accessibilityRotorEntry(id:in)`.

- `textRange` — Optional range of text associated with this Rotor entry. This should be a range within text that is set as the accessibility label or accessibility value of the associated element.

- `prepare` — Optional closure to run before a Rotor entry is navigated to, to prepare the UI as needed. This should be used to bring the Accessibility element on-screen, if scrolling is needed to get to it.

## See Also

### Creating an identified rotor entry in a namespace

- [init(_:_:in:textRange:prepare:)](<init(____in_textrange_prepare_).md>) — Create a Rotor entry with a specific label, identifier and namespace, and with an optional range.
