---
title: 'task(id:name:priority:file:line:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/task(id:name:priority:file:line:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/task(id:name:priority:file:line:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/task%28id%3Aname%3Apriority%3Afile%3Aline%3A_%3A%29.json'
content_hash: 'sha256:bbae3f7df9d61b70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# task(id:name:priority:file:line:_:)

<sub>Instance Method</sub>

Adds a task to perform before this view appears or when a specified value changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func task<T>(id: T, name: String? = nil, priority: TaskPriority = .userInitiated, file: String = #fileID, line: Int = #line, _ action: sending @escaping @isolated(any) () async -> Void) -> some View where T : Equatable

```

## Parameters

- `id` — The value to observe for changes. The value must conform to the [Equatable](../../swift/equatable.md) protocol.

- `name` — Human readable name for the task. A name will be generated if this argument is `nil`. This value is a no-op prior to iOS 26.4, macOS 26.4, watchOS 26.4, tvOS 26.4, and visionOS 26.4.

- `priority` — The task priority to use when creating the asynchronous task. The default priority is [userInitiated](../../swift/taskpriority/userinitiated.md).

- `file` — File name used in default task name. SwiftUI uses the callsite of .task by default. This value is a no-op prior to iOS 26.4, macOS 26.4, watchOS 26.4, tvOS 26.4, and visionOS 26.4.

- `line` — Line number used in default task name. SwiftUI uses the callsite of .task by default. This value is a no-op prior to iOS 26.4, macOS 26.4, watchOS 26.4, tvOS 26.4, and visionOS 26.4.

- `action` — A closure that SwiftUI calls as an asynchronous task before the view appears. SwiftUI can automatically cancel the task after the view disappears before the action completes. If the `id` value changes, SwiftUI cancels and restarts the task.

## Return Value

A view that runs the specified action asynchronously before the view appears, or restarts the task when the `id` value changes.

## Discussion

This method behaves like `View/task(priority:_:)`, except that it also cancels and recreates the task when a specified value changes. To detect a change, the modifier tests whether a new value for the `id` parameter equals the previous value. For this to work, the value’s type must conform to the [Equatable](../../swift/equatable.md) protocol.

For example, if you define an equatable `Server` type that posts custom notifications whenever its state changes — for example, from _signed out_ to _signed in_ — you can use the task modifier to update the contents of a [Text](../text.md) view to reflect the state of the currently selected server:

```swift
Text(status ?? "Signed Out")
    .task(id: server) {
        let sequence = NotificationCenter.default.notifications(
            named: .didUpdateStatus,
            object: server
        ).compactMap {
            $0.userInfo?["status"] as? String
        }
        for await value in sequence {
            status = value
        }
    }
```

This example uses the [notifications(named:object:)](<../../foundation/notificationcenter/notifications(named_object_).md>) method to create an asynchronous sequence of notifications, given by an [AsyncSequence](../../swift/asyncsequence.md) instance. The example then maps the notification sequence to a sequence of strings that correspond to values stored with each notification.

Elsewhere, the server defines a custom `didUpdateStatus` notification:

```swift
extension NSNotification.Name {
    static var didUpdateStatus: NSNotification.Name {
        NSNotification.Name("didUpdateStatus")
    }
}
```

Whenever the server status changes, like after the user signs in, the server posts a notification of this custom type:

```swift
let notification = Notification(
    name: .didUpdateStatus,
    object: self,
    userInfo: ["status": "Signed In"])
NotificationCenter.default.post(notification)
```

The task attached to the [Text](../text.md) view gets and displays the status value from the notification’s user information dictionary. When the user chooses a different server, SwiftUI cancels the task and creates a new one, which then waits for notifications from the new server.

The task is created by `Task.immediate`. Its action begins execution synchronously until it suspends at the first `await`.

## See Also

### Assigning tasks

- [task(id:name:executorPreference:priority:file:line:_:)](<task(id_name_executorpreference_priority_file_line___).md>) — Adds a task to perform before this view appears or when a specified value changes.
- [task(name:executorPreference:priority:file:line:action:)](<task(name_executorpreference_priority_file_line_action_).md>) — Adds an asynchronous task to perform before this view appears.
- [task(name:priority:file:line:_:)](<task(name_priority_file_line___).md>) — Adds an asynchronous task to perform before this view appears.
