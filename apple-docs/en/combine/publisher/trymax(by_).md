---
title: 'tryMax(by:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/trymax(by:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/trymax(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/trymax%28by%3A%29.json'
content_hash: 'sha256:b6f7314d213609cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# tryMax(by:)

<sub>Instance Method</sub>

Publishes the maximum value received from the upstream publisher, using the provided error-throwing closure to order the items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryMax(by areInIncreasingOrder: @escaping (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>
```

## Parameters

- `areInIncreasingOrder` — A throwing closure that receives two elements and returns `true` if they’re in increasing order. If this closure throws, the publisher terminates with a [Subscribers.Completion.failure(_:)](<../subscribers/completion/failure(__).md>).

## Return Value

A publisher that publishes the maximum value received from the upstream publisher, after the upstream publisher finishes.

## Discussion

Use [tryMax(by:)](<trymax(by_).md>) to determine the maximum value of elements received from the upstream publisher using an error-throwing closure you specify.

In the example below, an array publishes elements. The [tryMax(by:)](<trymax(by_).md>) operator executes the error-throwing closure that throws when the `first` element is an odd number, terminating the publisher.

```swift
struct IllegalValueError: Error {}

let numbers: [Int]  = [0, 10, 6, 13, 22, 22]
cancellable = numbers.publisher
    .tryMax { first, second -> Bool in
        if (first % 2 != 0) {
            throw IllegalValueError()
        }
        return first > second
    }
    .sink(
        receiveCompletion: { print ("completion: \($0)") },
        receiveValue: { print ("value: \($0)") }
    )

// Prints: completion: failure(IllegalValueError())
```

After this publisher receives a request for more than 0 items, it requests unlimited items from its upstream publisher.

## See Also

### Applying mathematical operations on elements

- [count()](<count().md>) — Publishes the number of elements received from the upstream publisher.
- [max()](<max().md>) — Publishes the maximum value received from the upstream publisher, after it finishes.
- [max(by:)](<max(by_).md>) — Publishes the maximum value received from the upstream publisher, using the provided ordering closure.
- [min()](<min().md>) — Publishes the minimum value received from the upstream publisher, after it finishes.
- [min(by:)](<min(by_).md>) — Publishes the minimum value received from the upstream publisher, after it finishes.
- [tryMin(by:)](<trymin(by_).md>) — Publishes the minimum value received from the upstream publisher, using the provided error-throwing closure to order the items.
