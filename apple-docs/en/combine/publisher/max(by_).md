---
title: 'max(by:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/max(by:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/max(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/max%28by%3A%29.json'
content_hash: 'sha256:afbb81fea94581d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# max(by:)

<sub>Instance Method</sub>

Publishes the maximum value received from the upstream publisher, using the provided ordering closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func max(by areInIncreasingOrder: @escaping (Self.Output, Self.Output) -> Bool) -> Publishers.Comparison<Self>
```

## Parameters

- `areInIncreasingOrder` — A closure that receives two elements and returns true if they’re in increasing order.

## Return Value

A publisher that publishes the maximum value received from the upstream publisher, after the upstream publisher finishes.

## Discussion

Use [max(by:)](<max(by_).md>) to determine the maximum value of elements received from the upstream publisher based on an ordering closure you specify.

In the example below, an array publishes enumeration elements representing playing card ranks. The [max(by:)](<max(by_).md>) operator compares the current and next elements using the `rawValue` property of each enumeration value in the user supplied closure and prints the maximum value found after publishing all of the elements.

```swift
enum Rank: Int {
    case ace = 1, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king
}

let cards: [Rank] = [.five, .queen, .ace, .eight, .jack]
cancellable = cards.publisher
    .max {
        return  $0.rawValue > $1.rawValue
    }
    .sink { print("\($0)") }

// Prints: "queen"
```

After this publisher receives a request for more than 0 items, it requests unlimited items from its upstream publisher.

## See Also

### Applying mathematical operations on elements

- [count()](<count().md>) — Publishes the number of elements received from the upstream publisher.
- [max()](<max().md>) — Publishes the maximum value received from the upstream publisher, after it finishes.
- [tryMax(by:)](<trymax(by_).md>) — Publishes the maximum value received from the upstream publisher, using the provided error-throwing closure to order the items.
- [min()](<min().md>) — Publishes the minimum value received from the upstream publisher, after it finishes.
- [min(by:)](<min(by_).md>) — Publishes the minimum value received from the upstream publisher, after it finishes.
- [tryMin(by:)](<trymin(by_).md>) — Publishes the minimum value received from the upstream publisher, using the provided error-throwing closure to order the items.
