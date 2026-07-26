---
title: 'sink(receiveValue:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/sink(receivevalue:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/sink(receivevalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/sink%28receivevalue%3A%29.json'
content_hash: 'sha256:6d44a54b6f69a2bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# sink(receiveValue:)

<sub>Instance Method</sub>

Attaches a subscriber with closure-based behavior to a publisher that never fails.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sink(receiveValue: @escaping (Self.Output) -> Void) -> AnyCancellable
```

## Parameters

- `receiveValue` — The closure to execute on receipt of a value.

## Return Value

A cancellable instance, which you use when you end assignment of the received value. Deallocation of the result will tear down the subscription stream.

## Discussion

Use [sink(receiveValue:)](<sink(receivevalue_).md>) to observe values received by the publisher and print them to the console. This operator can only be used when the stream doesn’t fail, that is, when the publisher’s [Failure](failure.md) type is [Never](../../swift/never.md).

In this example, a [Range](../../swift/range.md) publisher publishes integers to a [sink(receiveValue:)](<sink(receivevalue_).md>) operator’s `receiveValue` closure that prints them to the console:

```swift
let integers = (0...3)
integers.publisher
    .sink { print("Received \($0)") }

// Prints:
//  Received 0
//  Received 1
//  Received 2
//  Received 3
```

This method creates the subscriber and immediately requests an unlimited number of values, prior to returning the subscriber. The return value should be held, otherwise the stream will be canceled.

## See Also

### Connecting simple subscribers

- [assign(to:on:)](<assign(to_on_).md>) — Assigns each element from a publisher to a property on an object.
- [assign(to:)](<assign(to_).md>) — Republishes elements received from a publisher, by assigning them to a property marked as a publisher.
- [sink(receiveCompletion:receiveValue:)](<sink(receivecompletion_receivevalue_).md>) — Attaches a subscriber with closure-based behavior.
