---
title: callAsFunction()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dismissaction/callasfunction()
source_url: 'https://developer.apple.com/documentation/swiftui/dismissaction/callasfunction()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dismissaction/callasfunction%28%29.json'
content_hash: 'sha256:f4a32ac0ddb89668'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DismissAction](../dismissaction.md)

# callAsFunction()

<sub>Instance Method</sub>

Dismisses the view if it is currently presented.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func callAsFunction()
```

## Discussion

Don’t call this method directly. SwiftUI calls it for you when you call the [DismissAction](../dismissaction.md) structure that you get from the [Environment](../environment.md):

```swift
private struct SheetContents: View {
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        Button("Done") {
            dismiss() // Implicitly calls dismiss.callAsFunction()
        }
    }
}
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in _The Swift Programming Language_.
