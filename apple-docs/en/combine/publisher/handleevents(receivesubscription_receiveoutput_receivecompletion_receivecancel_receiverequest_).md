---
title: 'handleEvents(receiveSubscription:receiveOutput:receiveCompletion:receiveCancel:receiveRequest:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/handleevents(receivesubscription:receiveoutput:receivecompletion:receivecancel:receiverequest:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/handleevents(receivesubscription:receiveoutput:receivecompletion:receivecancel:receiverequest:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/handleevents%28receivesubscription%3Areceiveoutput%3Areceivecompletion%3Areceivecancel%3Areceiverequest%3A%29.json'
content_hash: 'sha256:9726673a3f20aa84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# handleEvents(receiveSubscription:receiveOutput:receiveCompletion:receiveCancel:receiveRequest:)

<sub>Instance Method</sub>

Performs the specified closures when publisher events occur.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func handleEvents(receiveSubscription: ((any Subscription) -> Void)? = nil, receiveOutput: ((Self.Output) -> Void)? = nil, receiveCompletion: ((Subscribers.Completion<Self.Failure>) -> Void)? = nil, receiveCancel: (() -> Void)? = nil, receiveRequest: ((Subscribers.Demand) -> Void)? = nil) -> Publishers.HandleEvents<Self>
```

## Parameters

- `receiveSubscription` — An optional closure that executes when the publisher receives the subscription from the upstream publisher. This value defaults to `nil`.

- `receiveOutput` — An optional closure that executes when the publisher receives a value from the upstream publisher. This value defaults to `nil`.

- `receiveCompletion` — An optional closure that executes when the upstream publisher finishes normally or terminates with an error. This value defaults to `nil`.

- `receiveCancel` — An optional closure that executes when the downstream receiver cancels publishing. This value defaults to `nil`.

- `receiveRequest` — An optional closure that executes when the publisher receives a request for more elements. This value defaults to `nil`.

## Return Value

A publisher that performs the specified closures when publisher events occur.

## Discussion

Use [handleEvents(receiveSubscription:receiveOutput:receiveCompletion:receiveCancel:receiveRequest:)](<handleevents(receivesubscription_receiveoutput_receivecompletion_receivecancel_receiverequest_).md>) when you want to examine elements as they progress through the stages of the publisher’s lifecycle.

In the example below, a publisher of integers shows the effect of printing debugging information at each stage of the element-processing lifecycle:

```swift
let integers = (0...2)
cancellable = integers.publisher
    .handleEvents(receiveSubscription: { subs in
        print("Subscription: \(subs.combineIdentifier)")
    }, receiveOutput: { anInt in
        print("in output handler, received \(anInt)")
    }, receiveCompletion: { _ in
        print("in completion handler")
    }, receiveCancel: {
        print("received cancel")
    }, receiveRequest: { (demand) in
        print("received demand: \(demand.description)")
    })
    .sink { _ in return }

// Prints:
//   received demand: unlimited
//   Subscription: 0x7f81284734c0
//   in output handler, received 0
//   in output handler, received 1
//   in output handler, received 2
//   in completion handler
```

## See Also

### Debugging

- [breakpoint(receiveSubscription:receiveOutput:receiveCompletion:)](<breakpoint(receivesubscription_receiveoutput_receivecompletion_).md>) — Raises a debugger signal when a provided closure needs to stop the process in the debugger.
- [breakpointOnError()](<breakpointonerror().md>) — Raises a debugger signal upon receiving a failure.
- [print(_:to:)](<print(__to_).md>) — Prints log messages for all publishing events.
