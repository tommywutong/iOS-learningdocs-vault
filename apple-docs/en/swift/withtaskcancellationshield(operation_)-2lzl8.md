---
title: 'withTaskCancellationShield(operation:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/withtaskcancellationshield(operation:)-2lzl8'
source_url: 'https://developer.apple.com/documentation/swift/withtaskcancellationshield(operation:)-2lzl8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/withtaskcancellationshield%28operation%3A%29-2lzl8.json'
content_hash: 'sha256:658421b414ca1fe2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# withTaskCancellationShield(operation:)

<sub>Function</sub>

Enters a scope in which a task cancellation shield is active.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withTaskCancellationShield<Value, Failure>(operation: () throws(Failure) -> Value) throws(Failure) -> Value where Failure : Error
```

## Discussion

Cancellation shields are primarily used to ensure some cleanup code will definitely run, even if the context in which the cleanup functions are called from is a cancelled task, and the functions may otherwise return early (due to observing the cancellation of the current task).

For example, a resource cleanup function might internally check for cancellation, which could cause it to skip important cleanup work:

```swift
let resource = await makeResource()
defer {
  await withTaskCancellationShield {
    await resource.finish() // runs to completion, even if task was cancelled earlier
  }
}

struct Resource {
  func finish() {
    guard !Task.isCancelled() else { return } // returns early if task was cancelled!
    // real work happens here
  }
```

While inside a cancellation shield, `Task.isCancelled` returns `false` and `Task.checkCancellation()` does not throw, even if the surrounding task has been cancelled. Similarly task cancellation handlers do not trigger while executing in a shielded block of code.

Once the shield scope exits, the task’s actual cancellation status becomes observable again. Cancellation shields to not prevent the task from becoming cancelled, but only prevent observing the cancellation while executing inside a shielded scope.

Cancellation shields also prevent cancellation from propagating to child tasks created within the shielded scope:

```swift
let task = Task {
  withUnsafeCurrentTask { $0?.cancel() } // cancel the task

  await withTaskCancellationShield {
    // Child tasks created here do NOT observe the parent's cancellation
    // and therefore start as not cancelled. They can be individually cancelled though.
    await withTaskGroup(of: Void.self) { group in
      group.addTask {
        print(Task.isCancelled) // false
      }
      for await _ in group {}

      group.cancelAll() // explicitly cancelling the group does cancel child tasks of the group
      group.addTask {
        print(Task.isCancelled) // true
      }
    }
  }
}
```

Note that shielding the `addTask` call itself does not shield the child task:

```swift
await withTaskGroup(of: Void.self) { group in
  group.cancelAll()
  withTaskCancellationShield {
    group.addTask { print(Task.isCancelled) } // true - child IS cancelled
  }
  group.addTask {
    withTaskCancellationShield { print(Task.isCancelled) } // false - shielded inside child
  }
}
```

## See Also

### Shielding Tasks from Cancellation

- [withTaskCancellationShield(operation:)](<withtaskcancellationshield(operation_)-8zlgh.md>) — Enters a scope in which a task cancellation shield is active. _(beta)_
