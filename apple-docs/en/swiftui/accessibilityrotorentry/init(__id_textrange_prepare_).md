---
title: 'init(_:id:textRange:prepare:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/accessibilityrotorentry/init(_:id:textrange:prepare:)'
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilityrotorentry/init(_:id:textrange:prepare:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilityrotorentry/init%28_%3Aid%3Atextrange%3Aprepare%3A%29.json'
content_hash: 'sha256:245e4660bb387fde'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AccessibilityRotorEntry](../accessibilityrotorentry.md)

# init(_:id:textRange:prepare:)

<sub>Initializer</sub>

Create a Rotor entry with a specific label and identifier, with an optional range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) init(_ label: LocalizedStringResource, id: ID, textRange: Range<String.Index>? = nil, prepare: @escaping () -> Void = {})
```

## Parameters

- `label` — Localized string used to show this Rotor entry to users.

- `id` — Used to find the UI element associated with this Rotor entry. This identifier should be used within a `scrollView`, either in a `ForEach` or using an `id` call.

- `textRange` — Optional range of text associated with this Rotor entry. This should be a range within text that is set as the accessibility label or accessibility value of the associated element.

- `prepare` — Optional closure to run before a Rotor entry is navigated to, to prepare the UI as needed. This can be used to bring the UI element on-screen if it isn’t already, and SwiftUI is not able to automatically scroll to it.

## See Also

### Creating a rotor entry

- [init(_:textRange:prepare:)](<init(__textrange_prepare_).md>) — Create a Rotor entry with a specific label and range. This Rotor entry will be associated with the Accessibility element that owns the Rotor.
