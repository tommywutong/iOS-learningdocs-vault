---
title: close
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/buttonrole/close
source_url: 'https://developer.apple.com/documentation/swiftui/buttonrole/close'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/buttonrole/close.json'
content_hash: 'sha256:694803ba918916c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ButtonRole](../buttonrole.md)

# close

<sub>Type Property</sub>

A role that indicates a button that closes the current operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let close: ButtonRole
```

## Discussion

Unlike a cancel operation, a close operation doesn’t lose progress for a user.

The following view would display a close button in the toolbar.

```swift
struct NewContactSheet: View {
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            NewContactEditor()
                .toolbar {
                    Button(role: .close) {
                        dismiss()
                    }
                }
        }
    }
}
```
