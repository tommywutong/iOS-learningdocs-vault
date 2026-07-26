---
title: 'widgetURL(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/widgeturl(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/widgeturl(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/widgeturl%28_%3A%29.json'
content_hash: 'sha256:702c4b1bc45feab9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# widgetURL(_:)

<sub>Instance Method</sub>

Sets the URL to open in the containing app when the user clicks the widget.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func widgetURL(_ url: URL?) -> some View

```

## Parameters

- `url` — The URL to open in the containing app.

## Return Value

A view that opens the specified URL when the user clicks the widget.

## Discussion

Widgets support one `widgetURL` modifier in their view hierarchy. If multiple views have `widgetURL` modifiers, the behavior is undefined.

## See Also

### URLs

- [onOpenURL(perform:)](<onopenurl(perform_).md>) — Registers a handler to invoke in response to a URL that your app receives.
- [onOpenURL(prefersInApp:)](<onopenurl(prefersinapp_).md>) — Sets an `OpenURLAction` that prefers opening URL with an in-app browser. The `handler` closure takes a URL as input, and returns a `OpenURLAction.Result` that indicates the outcome of the action.
