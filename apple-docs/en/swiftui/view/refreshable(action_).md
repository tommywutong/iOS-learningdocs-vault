---
title: 'refreshable(action:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/refreshable(action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/refreshable(action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/refreshable%28action%3A%29.json'
content_hash: 'sha256:2c551ddc393ae5c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# refreshable(action:)

<sub>Instance Method</sub>

Adds an asynchronous handler that can update the data the view displays when a person initiates a request, such as by pulling to refresh.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func refreshable(action: @escaping @Sendable () async -> Void) -> some View

```

## Parameters

- `action` — An asynchronous handler that SwiftUI executes when a person requests a refresh. Use this handler to initiate an update of model data displayed in the modified view. Use `await` in front of any asynchronous calls inside the handler.

## Return Value

A view with a new refresh action in its environment.

## Discussion

Apply this modifier to a view to set the [refresh](../environmentvalues/refresh.md) value in the view’s environment to a [RefreshAction](../refreshaction.md) instance that uses the specified `action` as its handler. Views that detect the presence of the instance can change their appearance to provide a way for a person to execute the handler.

For example, when you apply this modifier on iOS and iPadOS to a [List](../list.md), the list enables a standard pull-to-refresh gesture that refreshes the list contents. When a person drags the top of the scrollable area downward, the view reveals a progress indicator and executes the specified handler. The indicator remains visible for the duration of the refresh, which runs asynchronously:

```swift
List(mailbox.conversations) { conversation in
    ConversationCell(conversation)
}
.refreshable {
    await mailbox.fetch()
}
```

You can add refresh capability to your own views as well. For information on how to do that, see [RefreshAction](../refreshaction.md).

## See Also

### Refreshing a list’s content

- [refresh](../environmentvalues/refresh.md) — A refresh action stored in a view’s environment.
- [RefreshAction](../refreshaction.md) — An action that initiates a refresh operation.
