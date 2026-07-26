---
title: 'breakpoint(receiveSubscription:receiveOutput:receiveCompletion:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/breakpoint(receivesubscription:receiveoutput:receivecompletion:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/breakpoint(receivesubscription:receiveoutput:receivecompletion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/breakpoint%28receivesubscription%3Areceiveoutput%3Areceivecompletion%3A%29.json'
content_hash: 'sha256:77339b4f65848237'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# breakpoint(receiveSubscription:receiveOutput:receiveCompletion:)

<sub>Instance Method</sub>

Raises a debugger signal when a provided closure needs to stop the process in the debugger.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func breakpoint(receiveSubscription: ((any Subscription) -> Bool)? = nil, receiveOutput: ((Self.Output) -> Bool)? = nil, receiveCompletion: ((Subscribers.Completion<Self.Failure>) -> Bool)? = nil) -> Publishers.Breakpoint<Self>
```

## Parameters

- `receiveSubscription` — A closure that executes when the publisher receives a subscription. Return `true` from this closure to raise `SIGTRAP`, or false to continue.

- `receiveOutput` — A closure that executes when the publisher receives a value. Return `true` from this closure to raise `SIGTRAP`, or false to continue.

- `receiveCompletion` — A closure that executes when the publisher receives a completion. Return `true` from this closure to raise `SIGTRAP`, or false to continue.

## Return Value

A publisher that raises a debugger signal when one of the provided closures returns `true`.

## Discussion

Use [breakpoint(receiveSubscription:receiveOutput:receiveCompletion:)](<breakpoint(receivesubscription_receiveoutput_receivecompletion_).md>) to examine one or more stages of the subscribe/publish/completion process and stop in the debugger, based on conditions you specify. When any of the provided closures returns `true`, this operator raises the `SIGTRAP` signal to stop the process in the debugger. Otherwise, this publisher passes through values and completions as-is.

In the example below, a [PassthroughSubject](../passthroughsubject.md) publishes strings to a breakpoint republisher. When the breakpoint receives the string “`DEBUGGER`”, it returns `true`, which stops the app in the debugger.

```swift
let publisher = PassthroughSubject<String?, Never>()
cancellable = publisher
    .breakpoint(
        receiveOutput: { value in return value == "DEBUGGER" }
    )
    .sink { print("\(String(describing: $0))" , terminator: " ") }

publisher.send("DEBUGGER")

// Prints: "error: Execution was interrupted, reason: signal SIGTRAP."
// Depending on your specific environment, the console messages may
// also include stack trace information, which is not shown here.
```

## See Also

### Debugging

- [breakpointOnError()](<breakpointonerror().md>) — Raises a debugger signal upon receiving a failure.
- [handleEvents(receiveSubscription:receiveOutput:receiveCompletion:receiveCancel:receiveRequest:)](<handleevents(receivesubscription_receiveoutput_receivecompletion_receivecancel_receiverequest_).md>) — Performs the specified closures when publisher events occur.
- [print(_:to:)](<print(__to_).md>) — Prints log messages for all publishing events.
