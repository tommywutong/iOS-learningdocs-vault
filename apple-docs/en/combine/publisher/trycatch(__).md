---
title: 'tryCatch(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/trycatch(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/trycatch(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/trycatch%28_%3A%29.json'
content_hash: 'sha256:429298a368dd960f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# tryCatch(_:)

<sub>Instance Method</sub>

Handles errors from an upstream publisher by either replacing it with another publisher or throwing a new error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryCatch<P>(_ handler: @escaping (Self.Failure) throws -> P) -> Publishers.TryCatch<Self, P> where P : Publisher, Self.Output == P.Output
```

## Parameters

- `handler` — A throwing closure that accepts the upstream failure as input. This closure can either replace the upstream publisher with a new one, or throw a new error to the downstream subscriber.

## Return Value

A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher, or an error.

## Discussion

Use [tryCatch(_:)](<trycatch(__).md>) to decide how to handle from an upstream publisher by either replacing the publisher with a new publisher, or throwing a new error.

In the example below, an array publisher emits values that a [tryMap(_:)](<trymap(__).md>) operator evaluates to ensure the values are greater than zero. If the values aren’t greater than zero, the operator throws an error to the downstream subscriber to let it know there was a problem. The subscriber, [tryCatch(_:)](<trycatch(__).md>), replaces the error with a new publisher using [Just](../just.md) to publish a final value before the stream ends normally.

```swift
enum SimpleError: Error { case error }
var numbers = [5, 4, 3, 2, 1, -1, 7, 8, 9, 10]

cancellable = numbers.publisher
   .tryMap { v in
        if v > 0 {
            return v
        } else {
            throw SimpleError.error
        }
}
  .tryCatch { error in
      Just(0) // Send a final value before completing normally.
              // Alternatively, throw a new error to terminate the stream.
}
  .sink(receiveCompletion: { print ("Completion: \($0).") },
        receiveValue: { print ("Received \($0).") }
  )
//    Received 5.
//    Received 4.
//    Received 3.
//    Received 2.
//    Received 1.
//    Received 0.
//    Completion: finished.
```

## See Also

### Handling errors

- [assertNoFailure(_:file:line:)](<assertnofailure(__file_line_).md>) — Raises a fatal error when its upstream publisher fails, and otherwise republishes all received input.
- [catch(_:)](<catch(__).md>) — Handles errors from an upstream publisher by replacing it with another publisher.
- [retry(_:)](<retry(__).md>) — Attempts to recreate a failed subscription with the upstream publisher up to the number of times you specify.
