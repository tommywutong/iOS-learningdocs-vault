---
title: min()
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publisher/min()
source_url: 'https://developer.apple.com/documentation/combine/publisher/min()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/min%28%29.json'
content_hash: 'sha256:bad699a93c9bac52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# min()

<sub>Instance Method</sub>

Publishes the minimum value received from the upstream publisher, after it finishes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func min() -> Publishers.Comparison<Self>
```

## Return Value

A publisher that publishes the minimum value received from the upstream publisher, after the upstream publisher finishes.

## Discussion

Use [min(by:)](<min(by_).md>) to find the minimum value in a stream of elements from an upstream publisher.

In the example below, the [min(by:)](<min(by_).md>) operator emits a value when the publisher finishes, that value is the minimum of the values received from upstream, which is `-1`.

```swift
let numbers = [-1, 0, 10, 5]
numbers.publisher
    .min()
    .sink { print("\($0)") }

// Prints: "-1"
```

After this publisher receives a request for more than 0 items, it requests unlimited items from its upstream publisher.

## See Also

### Applying mathematical operations on elements

- [count()](<count().md>) — Publishes the number of elements received from the upstream publisher.
- [max()](<max().md>) — Publishes the maximum value received from the upstream publisher, after it finishes.
- [max(by:)](<max(by_).md>) — Publishes the maximum value received from the upstream publisher, using the provided ordering closure.
- [tryMax(by:)](<trymax(by_).md>) — Publishes the maximum value received from the upstream publisher, using the provided error-throwing closure to order the items.
- [min(by:)](<min(by_).md>) — Publishes the minimum value received from the upstream publisher, after it finishes.
- [tryMin(by:)](<trymin(by_).md>) — Publishes the minimum value received from the upstream publisher, using the provided error-throwing closure to order the items.
