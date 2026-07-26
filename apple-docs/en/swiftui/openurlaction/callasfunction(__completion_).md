---
title: 'callAsFunction(_:completion:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/openurlaction/callasfunction(_:completion:)'
source_url: 'https://developer.apple.com/documentation/swiftui/openurlaction/callasfunction(_:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/openurlaction/callasfunction%28_%3Acompletion%3A%29.json'
content_hash: 'sha256:3b6039e13607baef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [OpenURLAction](../openurlaction.md)

# callAsFunction(_:completion:)

<sub>Instance Method</sub>

Asynchronously opens a URL, following system conventions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func callAsFunction(_ url: URL, completion: @escaping (Bool) -> Void)
```

## Parameters

- `url` — The URL to open.

- `completion` — A closure the method calls after determining if it can open the URL, but possibly before fully opening the URL. The closure takes a Boolean value that indicates whether the method can open the URL.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the [OpenURLAction](../openurlaction.md) structure that you get from the [Environment](../environment.md), using a URL and a completion handler as arguments:

```swift
struct OpenURLExample: View {
    @Environment(\.openURL) private var openURL

    var body: some View {
        Button {
            if let url = URL(string: "https://www.example.com") {
                // Implicitly calls openURL.callAsFunction(url) { ... }
                openURL(url) { accepted in
                    print(accepted ? "Success" : "Failure")
                }
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

- [callAsFunction(_:)](<callasfunction(__).md>) — Opens a URL, following system conventions.
