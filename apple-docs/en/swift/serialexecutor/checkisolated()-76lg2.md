---
title: checkIsolated()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/serialexecutor/checkisolated()-76lg2
source_url: 'https://developer.apple.com/documentation/swift/serialexecutor/checkisolated()-76lg2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/serialexecutor/checkisolated%28%29-76lg2.json'
content_hash: 'sha256:97531ac6e1199a63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SerialExecutor](../serialexecutor.md)

# checkIsolated()

<sub>Instance Method</sub>

Last resort “fallback” isolation check, called when the concurrency runtime is comparing executors e.g. during `assumeIsolated()` and is unable to prove serial equivalence between the expected (this object), and the current executor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func checkIsolated()
```

## Discussion

During executor comparison, the Swift concurrency runtime attempts to compare current and expected executors in a few ways (including “complex” equality between executors (see [isSameExclusiveExecutionContext(other:)](<issameexclusiveexecutioncontext(other_).md>)), and if all those checks fail, this method is invoked on the expected executor.

This method MUST crash if it is unable to prove that the current execution context belongs to this executor. At this point usual executor comparison would have already failed, though the executor may have some external tracking of threads it owns, and may be able to prove isolation nevertheless.

A default implementation is provided that unconditionally crashes the program, and prevents calling code from proceeding with potentially not thread-safe execution.

> [!warning] Warning
> This method must crash and halt program execution if unable to prove the isolation of the calling context.
