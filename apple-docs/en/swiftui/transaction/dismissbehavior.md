---
title: dismissBehavior
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/transaction/dismissbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/transaction/dismissbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transaction/dismissbehavior.json'
content_hash: 'sha256:86fa6fc2178cba1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Transaction](../transaction.md)

# dismissBehavior

<sub>Instance Property</sub>

The behavior for how windows will dismiss programmatically when used in conjunction with [DismissWindowAction](../dismisswindowaction.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var dismissBehavior: DismissBehavior { get set }
```

## Discussion

The default value is `.interactive`.

You can use this property to dismiss windows which may be showing a modal presentation by using the `.destructive` value:

```swift
struct DismissWindowButton: View {
    @Environment(\.dismissWindow) private var dismissWindow

    var body: some View {
        Button("Close Auxiliary Window") {
            withTransaction(\.dismissBehavior, .destructive) {
                dismissWindow(id: "auxiliary")
            }
        }
    }
}
```
