---
title: RefreshAction
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/refreshaction
source_url: 'https://developer.apple.com/documentation/swiftui/refreshaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/refreshaction.json'
content_hash: 'sha256:b6c4c153528c3d64'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# RefreshAction

<sub>Structure</sub>

An action that initiates a refresh operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RefreshAction
```

## Overview

When the [refresh](environmentvalues/refresh.md) environment value contains an instance of this structure, certain built-in views in the corresponding [Environment](environment.md) begin offering a refresh capability. They apply the instance’s handler to any refresh operation that the user initiates. By default, the environment value is `nil`, but you can use the [refreshable(action:)](<view/refreshable(action_).md>) modifier to create and store a new refresh action that uses the handler that you specify:

```swift
List(mailbox.conversations) { conversation in
    ConversationCell(conversation)
}
.refreshable {
    await mailbox.fetch()
}
```

On iOS and iPadOS, the [List](list.md) in the example above offers a pull to refresh gesture because it detects the refresh action. When the user drags the list down and releases, the list calls the action’s handler. Because SwiftUI declares the handler as asynchronous, it can safely make long-running asynchronous calls, like fetching network data.

### Refreshing custom views

You can also offer refresh capability in your custom views. Read the [refresh](environmentvalues/refresh.md) environment value to get the `RefreshAction` instance for a given [Environment](environment.md). If you find a non-`nil` value, change your view’s appearance or behavior to offer the refresh to the user, and call the instance to conduct the refresh. You can call the refresh instance directly because it defines a [callAsFunction()](<refreshaction/callasfunction().md>) method that Swift calls when you call the instance:

```swift
struct RefreshableView: View {
    @Environment(\.refresh) private var refresh

    var body: some View {
        Button("Refresh") {
            Task {
                await refresh?()
            }
        }
        .disabled(refresh == nil)
    }
}
```

Be sure to call the handler asynchronously by preceding it with `await`. Because the call is asynchronous, you can use its lifetime to indicate progress to the user. For example, you might reveal an indeterminate [ProgressView](progressview.md) before calling the handler, and hide it when the handler completes.

If your code isn’t already in an asynchronous context, create a [Task](../swift/task.md) for the method to run in. If you do this, consider adding a way for the user to cancel the task. For more information, see [Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) in _The Swift Programming Language_.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Calling the action

- [callAsFunction()](<refreshaction/callasfunction().md>) — Initiates a refresh action.

## See Also

### Refreshing a list’s content

- [refreshable(action:)](<view/refreshable(action_).md>) — Adds an asynchronous handler that can update the data the view displays when a person initiates a request, such as by pulling to refresh.
- [refresh](environmentvalues/refresh.md) — A refresh action stored in a view’s environment.
