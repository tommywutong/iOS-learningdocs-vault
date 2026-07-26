---
title: 'updateUIViewController(_:context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uiviewcontrollerrepresentable/updateuiviewcontroller(_:context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uiviewcontrollerrepresentable/updateuiviewcontroller(_:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uiviewcontrollerrepresentable/updateuiviewcontroller%28_%3Acontext%3A%29.json'
content_hash: 'sha256:1a42a8c1454ebdc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIViewControllerRepresentable](../uiviewcontrollerrepresentable.md)

# updateUIViewController(_:context:)

<sub>Instance Method</sub>

Updates the state of the specified view controller with new information from SwiftUI.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func updateUIViewController(_ uiViewController: Self.UIViewControllerType, context: Self.Context)
```

## Parameters

- `uiViewController` — Your custom view controller object.

- `context` — A context structure containing information about the current state of the system.

## Discussion

When the state of your app changes, SwiftUI updates the portions of your interface affected by those changes. SwiftUI calls this method for any changes affecting the corresponding UIKit view controller. Use this method to update the configuration of your view controller to match the new state information provided in the `context` parameter.

## See Also

### Creating and updating the view controller

- [makeUIViewController(context:)](<makeuiviewcontroller(context_).md>) — Creates the view controller object and configures its initial state.
- [Context](context.md)
- [UIViewControllerType](uiviewcontrollertype.md) — The type of view controller to present.
