---
title: 'task(name:priority:file:line:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/task(name:priority:file:line:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/task(name:priority:file:line:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/task%28name%3Apriority%3Afile%3Aline%3A_%3A%29.json'
content_hash: 'sha256:e4f7c53300940dc5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# task(name:priority:file:line:_:)

<sub>Instance Method</sub>

Adds an asynchronous task to perform before this view appears.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func task(name: String? = nil, priority: TaskPriority = .userInitiated, file: String = #fileID, line: Int = #line, _ action: sending @escaping @isolated(any) () async -> Void) -> some View

```

## Parameters

- `name` — Human readable name for the task. A name will be generated if this argument is `nil`. This value is a no-op prior to iOS 26.4, macOS 26.4, watchOS 26.4, tvOS 26.4, and visionOS 26.4.

- `priority` — The task priority to use when creating the asynchronous task. The default priority is [userInitiated](../../swift/taskpriority/userinitiated.md).

- `file` — File name used in default task name. SwiftUI uses the callsite of .task by default. This value is a no-op prior to iOS 26.4, macOS 26.4, watchOS 26.4, tvOS 26.4, and visionOS 26.4.

- `line` — Line number used in default task name. SwiftUI uses the callsite of .task by default. This value is a no-op prior to iOS 26.4, macOS 26.4, watchOS 26.4, tvOS 26.4, and visionOS 26.4.

- `action` — A closure that SwiftUI calls as an asynchronous task before the view appears. SwiftUI will automatically cancel the task at some point after the view disappears before the action completes.

## Return Value

A view that runs the specified action asynchronously before the view appears.

## Discussion

Use this modifier to perform an asynchronous task with a lifetime that matches that of the modified view. If the task doesn’t finish before SwiftUI removes the view or the view changes identity, SwiftUI cancels the task.

Use the `await` keyword inside the task to wait for an asynchronous call to complete, or to wait on the values of an [AsyncSequence](../../swift/asyncsequence.md) instance. For example, you can modify a [Text](../text.md) view to start a task that loads content from a remote resource:

```swift
let url = URL(string: "https://example.com")!
@State private var message = "Loading..."

var body: some View {
    Text(message)
        .task {
            do {
                var receivedLines = [String]()
                for try await line in url.lines {
                    receivedLines.append(line)
                    message = "Received \(receivedLines.count) lines"
                }
            } catch {
                message = "Failed to load"
            }
        }
}
```

This example uses the [lines](../../foundation/url/lines.md) method to get the content stored at the specified [URL](../../foundation/url.md) as an asynchronous sequence of strings. When each new line arrives, the body of the `for`-`await`-`in` loop stores the line in an array of strings and updates the content of the text view to report the latest line count.

The task is created by `Task.immediate`. Its action begins execution synchronously until it suspends at the first `await`.

## See Also

### Assigning tasks

- [task(id:name:executorPreference:priority:file:line:_:)](<task(id_name_executorpreference_priority_file_line___).md>) — Adds a task to perform before this view appears or when a specified value changes.
- [task(id:name:priority:file:line:_:)](<task(id_name_priority_file_line___).md>) — Adds a task to perform before this view appears or when a specified value changes.
- [task(name:executorPreference:priority:file:line:action:)](<task(name_executorpreference_priority_file_line_action_).md>) — Adds an asynchronous task to perform before this view appears.
