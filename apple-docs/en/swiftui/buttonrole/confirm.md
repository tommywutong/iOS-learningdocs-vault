---
title: confirm
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/buttonrole/confirm
source_url: 'https://developer.apple.com/documentation/swiftui/buttonrole/confirm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/buttonrole/confirm.json'
content_hash: 'sha256:6d312d73621502ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ButtonRole](../buttonrole.md)

# confirm

<sub>Type Property</sub>

A role that indicates a button that confirms an operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let confirm: ButtonRole
```

## Discussion

The following view would display a confirm button in the toolbar.

```swift
struct NewContactSheet: View {
    var body: some View {
        NavigationStack {
            NewContactEditor()
                .toolbar {
                    Button(role: .confirm) {
                        saveChanges()
                    }
                }
        }
    }
}
```
