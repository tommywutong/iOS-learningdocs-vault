---
title: 'callAsFunction(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/openurlaction/callasfunction(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/openurlaction/callasfunction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/openurlaction/callasfunction%28_%3A%29.json'
content_hash: 'sha256:945242b802839681'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [OpenURLAction](../openurlaction.md)

# callAsFunction(_:)

<sub>Instance Method</sub>

Opens a URL, following system conventions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func callAsFunction(_ url: URL)
```

## Parameters

- `url` — The URL to open.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the [OpenURLAction](../openurlaction.md) structure that you get from the [Environment](../environment.md), using a URL as an argument:

```swift
struct OpenURLExample: View {
    @Environment(\.openURL) private var openURL

    var body: some View {
        Button {
            if let url = URL(string: "https://www.example.com") {
                openURL(url) // Implicitly calls openURL.callAsFunction(url)
            }
        } label: {
            Label("Get Help", systemImage: "person.fill.questionmark")
        }
    }
}
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in _The Swift Programming Language_.

## See Also

### Calling the action

- [callAsFunction(_:completion:)](<callasfunction(__completion_).md>) — Asynchronously opens a URL, following system conventions.
