---
title: isIsolatingCurrentContext()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/serialexecutor/isisolatingcurrentcontext()
source_url: 'https://developer.apple.com/documentation/swift/serialexecutor/isisolatingcurrentcontext()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/serialexecutor/isisolatingcurrentcontext%28%29.json'
content_hash: 'sha256:a3aa15cd4041742c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SerialExecutor](../serialexecutor.md)

# isIsolatingCurrentContext()

<sub>Instance Method</sub>

Checks if the current execution context is isolated by this executor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isIsolatingCurrentContext() -> Bool?
```

## Discussion

This function can be called by the runtime in order to perform assertions, or attempt to issue warnings about unexpected isolation.

This method will be invoked _before_ `checkIsolated` and may also be invoked when crashing is not an acceptable outcome of a check (e.g. when attempting to issue isolation _warnings_).

Implementations should prefer to implement this method rather than `checkIsolated()` since it can often result in more tailored error messages. It is allowed, and useful for backwards compatibility with old runtimes which are not able to invoke `isIsolatingCurrentContext()` to implement `checkIsolated()`, even if an implementation is able to implement this method. Often times an implementation of `checkIsolated()`, would then invoke `isIsolatingCurrentContext()` and crash if the returned value was `false`.

The default implementation returns `nil` is used to indicate that it is “unknown” if the current context is isolated by this serial executor. The runtime then _may_ proceed to invoke `checkIsolated()` as a last-resort attempt to verify the isolation of the current context.

## Default Implementations

### SerialExecutor Implementations

- [isIsolatingCurrentContext()](<isisolatingcurrentcontext()-65ht9.md>) — Checks if the current execution context is isolated by this executor.
