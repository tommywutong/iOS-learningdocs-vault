---
title: 'catch(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/catch(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/catch(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/catch%28_%3A%29.json'
content_hash: 'sha256:edea3ce96c8ec81e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# catch(_:)

<sub>Instance Method</sub>

Handles errors from an upstream publisher by replacing it with another publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func `catch`<P>(_ handler: @escaping (Self.Failure) -> P) -> Publishers.Catch<Self, P> where P : Publisher, Self.Output == P.Output
```

## Parameters

- `handler` — A closure that accepts the upstream failure as input and returns a publisher to replace the upstream publisher.

## Return Value

A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher.

## Discussion

Use `catch()` to replace an error from an upstream publisher with a new publisher.

In the example below, the `catch()` operator handles the `SimpleError` thrown by the upstream publisher by replacing the error with a `Just` publisher. This continues the stream by publishing a single value and completing normally.

```swift
struct SimpleError: Error {}
let numbers = [5, 4, 3, 2, 1, 0, 9, 8, 7, 6]
cancellable = numbers.publisher
    .tryLast(where: {
        guard $0 != 0 else {throw SimpleError()}
        return true
    })
    .catch({ (error) in
        Just(-1)
    })
    .sink { print("\($0)") }
    // Prints: -1
```

Backpressure note: This publisher passes through `request` and `cancel` to the upstream. After receiving an error, the publisher sends sends any unfulfilled demand to the new `Publisher`. SeeAlso: `replaceError`

## See Also

### Handling errors

- [assertNoFailure(_:file:line:)](<assertnofailure(__file_line_).md>) — Raises a fatal error when its upstream publisher fails, and otherwise republishes all received input.
- [tryCatch(_:)](<trycatch(__).md>) — Handles errors from an upstream publisher by either replacing it with another publisher or throwing a new error.
- [retry(_:)](<retry(__).md>) — Attempts to recreate a failed subscription with the upstream publisher up to the number of times you specify.
