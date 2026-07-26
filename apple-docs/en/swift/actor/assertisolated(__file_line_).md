---
title: 'assertIsolated(_:file:line:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/actor/assertisolated(_:file:line:)'
source_url: 'https://developer.apple.com/documentation/swift/actor/assertisolated(_:file:line:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/actor/assertisolated%28_%3Afile%3Aline%3A%29.json'
content_hash: 'sha256:5774a37c73d39467'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Actor](../actor.md)

# assertIsolated(_:file:line:)

<sub>Instance Method</sub>

Stops program execution if the current task is not executing on this actor’s serial executor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: macOS 14.0, iOS 17.0, watchOS 10.0, tvOS 17.0)
nonisolated func assertIsolated(_ message: @autoclosure () -> String = String(), file: StaticString = #fileID, line: UInt = #line)
```

## Parameters

- `message` — The message to print if the assertion fails.

- `file` — The file name to print if the assertion fails. The default is where this method was called.

- `line` — The line number to print if the assertion fails The default is where this method was called.

## Discussion

This function’s effect varies depending on the build flag used:

- In playgrounds and `-Onone` builds (the default for Xcode’s Debug configuration), stops program execution in a debuggable state after printing `message`.
- In `-O` builds (the default for Xcode’s Release configuration), the isolation check is not performed and there are no effects.

> [!note] Note
> This check is performed against the actor’s serial executor, meaning that / if another actor uses the same serial executor–by using that actor’s serial executor as its own [unownedExecutor](unownedexecutor.md)–this check will succeed , as from a concurrency safety perspective, the serial executor guarantees mutual exclusion of those two actors.
