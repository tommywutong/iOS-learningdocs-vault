---
title: count()
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publisher/count()
source_url: 'https://developer.apple.com/documentation/combine/publisher/count()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/count%28%29.json'
content_hash: 'sha256:0e4a0a1283472c85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# count()

<sub>Instance Method</sub>

Publishes the number of elements received from the upstream publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func count() -> Publishers.Count<Self>
```

## Return Value

A publisher that consumes all elements until the upstream publisher finishes, then emits a single value with the total number of elements received.

## Discussion

Use [count()](<count().md>) to determine the number of elements received from the upstream publisher before it completes:

```swift
let numbers = (0...10)
cancellable = numbers.publisher
    .count()
    .sink { print("\($0)") }

// Prints: "11"
```

## See Also

### Applying mathematical operations on elements

- [max()](<max().md>) — Publishes the maximum value received from the upstream publisher, after it finishes.
- [max(by:)](<max(by_).md>) — Publishes the maximum value received from the upstream publisher, using the provided ordering closure.
- [tryMax(by:)](<trymax(by_).md>) — Publishes the maximum value received from the upstream publisher, using the provided error-throwing closure to order the items.
- [min()](<min().md>) — Publishes the minimum value received from the upstream publisher, after it finishes.
- [min(by:)](<min(by_).md>) — Publishes the minimum value received from the upstream publisher, after it finishes.
- [tryMin(by:)](<trymin(by_).md>) — Publishes the minimum value received from the upstream publisher, using the provided error-throwing closure to order the items.
