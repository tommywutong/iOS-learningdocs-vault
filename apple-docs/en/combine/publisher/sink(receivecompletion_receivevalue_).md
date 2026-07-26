---
title: 'sink(receiveCompletion:receiveValue:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/sink(receivecompletion:receivevalue:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/sink(receivecompletion:receivevalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/sink%28receivecompletion%3Areceivevalue%3A%29.json'
content_hash: 'sha256:36784c1d1a8c8452'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# sink(receiveCompletion:receiveValue:)

<sub>Instance Method</sub>

Attaches a subscriber with closure-based behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sink(receiveCompletion: @escaping (Subscribers.Completion<Self.Failure>) -> Void, receiveValue: @escaping (Self.Output) -> Void) -> AnyCancellable
```

## Parameters

- `receiveValue` — The closure to execute on receipt of a value.

## Return Value

A cancellable instance, which you use when you end assignment of the received value. Deallocation of the result will tear down the subscription stream.

## Discussion

Use [sink(receiveCompletion:receiveValue:)](<sink(receivecompletion_receivevalue_).md>) to observe values received by the publisher and process them using a closure you specify.

In this example, a [Range](../../swift/range.md) publisher publishes integers to a [sink(receiveCompletion:receiveValue:)](<sink(receivecompletion_receivevalue_).md>) operator’s `receiveValue` closure that prints them to the console. Upon completion the [sink(receiveCompletion:receiveValue:)](<sink(receivecompletion_receivevalue_).md>) operator’s `receiveCompletion` closure indicates the successful termination of the stream.

```swift
let myRange = (0...3)
cancellable = myRange.publisher
    .sink(receiveCompletion: { print ("completion: \($0)") },
          receiveValue: { print ("value: \($0)") })

// Prints:
//  value: 0
//  value: 1
//  value: 2
//  value: 3
//  completion: finished
```

This method creates the subscriber and immediately requests an unlimited number of values, prior to returning the subscriber. The return value should be held, otherwise the stream will be canceled.

## See Also

### Connecting simple subscribers

- [assign(to:on:)](<assign(to_on_).md>) — Assigns each element from a publisher to a property on an object.
- [assign(to:)](<assign(to_).md>) — Republishes elements received from a publisher, by assigning them to a property marked as a publisher.
- [sink(receiveValue:)](<sink(receivevalue_).md>) — Attaches a subscriber with closure-based behavior to a publisher that never fails.
