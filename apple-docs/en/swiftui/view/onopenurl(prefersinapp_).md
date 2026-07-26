---
title: 'onOpenURL(prefersInApp:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onopenurl(prefersinapp:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onopenurl(prefersinapp:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onopenurl%28prefersinapp%3A%29.json'
content_hash: 'sha256:2855187f043accf7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onOpenURL(prefersInApp:)

<sub>Instance Method</sub>

Sets an `OpenURLAction` that prefers opening URL with an in-app browser. The `handler` closure takes a URL as input, and returns a `OpenURLAction.Result` that indicates the outcome of the action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func onOpenURL(prefersInApp: Bool) -> some View

```

## Parameters

- `prefersInApp` — A boolean value that specifies whether to prefer to open the URL with an in-app browser or not.

## Discussion

It’s equivalent to calling `.onOpenURL(_:)`

```swift
.onOpenURL { _ in
    .systemAction(prefersInApp: prefersInApp)
}
```

## See Also

### URLs

- [onOpenURL(perform:)](<onopenurl(perform_).md>) — Registers a handler to invoke in response to a URL that your app receives.
- [widgetURL(_:)](<widgeturl(__).md>) — Sets the URL to open in the containing app when the user clicks the widget.
