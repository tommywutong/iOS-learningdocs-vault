---
title: 'makeUIViewController(context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uiviewcontrollerrepresentable/makeuiviewcontroller(context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uiviewcontrollerrepresentable/makeuiviewcontroller(context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uiviewcontrollerrepresentable/makeuiviewcontroller%28context%3A%29.json'
content_hash: 'sha256:fdac3fb85a2df8ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIViewControllerRepresentable](../uiviewcontrollerrepresentable.md)

# makeUIViewController(context:)

<sub>Instance Method</sub>

Creates the view controller object and configures its initial state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func makeUIViewController(context: Self.Context) -> Self.UIViewControllerType
```

## Parameters

- `context` — A context structure containing information about the current state of the system.

## Return Value

Your UIKit view controller configured with the provided information.

## Discussion

You must implement this method and use it to create your view controller object. Create the view controller using your app’s current data and contents of the `context` parameter. The system calls this method only once, when it creates your view controller for the first time. For all subsequent updates, the system calls the [updateUIViewController(_:context:)](<updateuiviewcontroller(__context_).md>) method.

## See Also

### Creating and updating the view controller

- [updateUIViewController(_:context:)](<updateuiviewcontroller(__context_).md>) — Updates the state of the specified view controller with new information from SwiftUI.
- [Context](context.md)
- [UIViewControllerType](uiviewcontrollertype.md) — The type of view controller to present.
