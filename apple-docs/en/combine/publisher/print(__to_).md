---
title: 'print(_:to:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/print(_:to:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/print(_:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/print%28_%3Ato%3A%29.json'
content_hash: 'sha256:bdce907a8ed9edc7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# print(_:to:)

<sub>Instance Method</sub>

Prints log messages for all publishing events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func print(_ prefix: String = "", to stream: (any TextOutputStream)? = nil) -> Publishers.Print<Self>
```

## Parameters

- `prefix` — A string —- which defaults to empty -— with which to prefix all log messages.

- `stream` — A stream for text output that receives messages, and which directs output to the console by default.  A custom stream can be used to log messages to other destinations.

## Return Value

A publisher that prints log messages for all publishing events.

## Discussion

Use [print(_:to:)](<print(__to_).md>) to log messages the console.

In the example below, log messages are printed on the console:

```swift
let integers = (1...2)
cancellable = integers.publisher
   .print("Logged a message", to: nil)
   .sink { _ in }

// Prints:
//  Logged a message: receive subscription: (1..<2)
//  Logged a message: request unlimited
//  Logged a message: receive value: (1)
//  Logged a message: receive finished
```

## See Also

### Debugging

- [breakpoint(receiveSubscription:receiveOutput:receiveCompletion:)](<breakpoint(receivesubscription_receiveoutput_receivecompletion_).md>) — Raises a debugger signal when a provided closure needs to stop the process in the debugger.
- [breakpointOnError()](<breakpointonerror().md>) — Raises a debugger signal upon receiving a failure.
- [handleEvents(receiveSubscription:receiveOutput:receiveCompletion:receiveCancel:receiveRequest:)](<handleevents(receivesubscription_receiveoutput_receivecompletion_receivecancel_receiverequest_).md>) — Performs the specified closures when publisher events occur.
