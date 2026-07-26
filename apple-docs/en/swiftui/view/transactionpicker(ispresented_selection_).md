---
title: 'transactionPicker(isPresented:selection:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/transactionpicker(ispresented:selection:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/transactionpicker(ispresented:selection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/transactionpicker%28ispresented%3Aselection%3A%29.json'
content_hash: 'sha256:eede8c86d48e76c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# transactionPicker(isPresented:selection:)

<sub>Instance Method</sub>

Presents a picker that selects a collection of transactions.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency func transactionPicker(isPresented: Binding<Bool>, selection: Binding<[Transaction]>) -> some View

```

## Parameters

- `isPresented` — The binding to whether the transaction picker should be shown.

- `selection` — The selection of transactions from the transaction picker.
