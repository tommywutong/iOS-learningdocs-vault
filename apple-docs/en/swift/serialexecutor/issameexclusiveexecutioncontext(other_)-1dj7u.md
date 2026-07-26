---
title: 'isSameExclusiveExecutionContext(other:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, tvOS 26.4+, visionOS 26.4+, watchOS 26.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/serialexecutor/issameexclusiveexecutioncontext(other:)-1dj7u'
source_url: 'https://developer.apple.com/documentation/swift/serialexecutor/issameexclusiveexecutioncontext(other:)-1dj7u'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/serialexecutor/issameexclusiveexecutioncontext%28other%3A%29-1dj7u.json'
content_hash: 'sha256:0b8bb294e977db4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SerialExecutor](../serialexecutor.md)

# isSameExclusiveExecutionContext(other:)

<sub>Instance Method</sub>

If this executor has complex equality semantics, and the runtime needs to compare two executors, it will first attempt the usual pointer-based equality / check, / and if it fails it will compare the types of both executors, if they are the same, / it will finally invoke this method, in an attempt to let the executor itself decide / if this and the `other` executor represent the same serial, exclusive, isolation context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isSameExclusiveExecutionContext(other: Self) -> Bool
```

## Parameters

- `other` — The executor to compare with.

## Return Value

`true`, if `self` and the `other` executor actually are mutually exclusive and it is safe–from a concurrency perspective–to execute code assuming one on the other.

## Discussion

This method must be implemented with great care, as wrongly returning `true` would allow / code from a different execution context (e.g. thread) to execute code which was intended to be isolated by another actor.

This check is not used when performing executor switching.

This check is used when performing `Actor/assertIsolated()`, `Actor/preconditionIsolated()`, `Actor/assumeIsolated()` and similar APIs which assert about the same “exclusive serial execution context”.
