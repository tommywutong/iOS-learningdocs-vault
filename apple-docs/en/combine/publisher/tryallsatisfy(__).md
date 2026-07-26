---
title: 'tryAllSatisfy(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/tryallsatisfy(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/tryallsatisfy(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/tryallsatisfy%28_%3A%29.json'
content_hash: 'sha256:c9253a901032f201'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# tryAllSatisfy(_:)

<sub>Instance Method</sub>

Publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryAllSatisfy(_ predicate: @escaping (Self.Output) throws -> Bool) -> Publishers.TryAllSatisfy<Self>
```

## Parameters

- `predicate` — A closure that evaluates each received element. Return `true` to continue, or `false` to cancel the upstream and complete. The closure may throw an error, in which case the publisher cancels the upstream publisher and fails with the thrown error.

## Return Value

A publisher that publishes a Boolean value that indicates whether all received elements pass a given predicate.

## Discussion

Use the [tryAllSatisfy(_:)](<tryallsatisfy(__).md>) operator to determine if all elements in a stream satisfy a criteria in an error-throwing predicate you provide. When this publisher receives an element, it runs the predicate against the element. If the predicate returns `false`, the publisher produces a `false` value and finishes. If the upstream publisher finishes normally, this publisher produces a `true` value and finishes. If the predicate throws an error, the publisher fails and passes the error to its downstream subscriber.

In the example below, an error-throwing predicate tests if each of an integer array publisher’s elements fall into the `targetRange`; the predicate throws an error if an element is zero and terminates the stream.

```swift
let targetRange = (-1...100)
let numbers = [-1, 10, 5, 0]

numbers.publisher
    .tryAllSatisfy { anInt in
        guard anInt != 0 else { throw RangeError() }
        return targetRange.contains(anInt)
    }
    .sink(
        receiveCompletion: { print ("completion: \($0)") },
        receiveValue: { print ("value: \($0)") }
    )

// Prints: "completion: failure(RangeError())"
```

With operators similar to [reduce(_:_:)](<reduce(____).md>), this publisher produces at most one value.

> [!note] Note
> Upon receiving any request greater than zero, this publisher requests unlimited elements from the upstream publisher.

## See Also

### Applying matching criteria to elements

- [contains(_:)](<contains(__).md>) — Publishes a Boolean value upon receiving an element equal to the argument.
- [contains(where:)](<contains(where_).md>) — Publishes a Boolean value upon receiving an element that satisfies the predicate closure.
- [tryContains(where:)](<trycontains(where_).md>) — Publishes a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [allSatisfy(_:)](<allsatisfy(__).md>) — Publishes a single Boolean value that indicates whether all received elements pass a given predicate.
