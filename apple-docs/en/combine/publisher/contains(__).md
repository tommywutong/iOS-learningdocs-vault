---
title: 'contains(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/contains(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/contains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/contains%28_%3A%29.json'
content_hash: 'sha256:04b7492cfe294918'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# contains(_:)

<sub>Instance Method</sub>

Publishes a Boolean value upon receiving an element equal to the argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ output: Self.Output) -> Publishers.Contains<Self>
```

## Parameters

- `output` — An element to match against.

## Return Value

A publisher that emits the Boolean value `true` when the upstream publisher emits a matching value.

## Discussion

Use [contains(_:)](<contains(__).md>) to find the first element in an upstream that’s equal to the supplied argument. The contains publisher consumes all received elements until the upstream publisher produces a matching element. Upon finding the first match, it emits `true` and finishes normally. If the upstream finishes normally without producing a matching element, this publisher emits `false` and finishes.

In the example below, the [contains(_:)](<contains(__).md>) operator emits `true` the first time it receives the value `5` from the `numbers.publisher`, and then finishes normally.

```swift
let numbers = [-1, 5, 10, 5]
numbers.publisher
    .contains(5)
    .sink { print("\($0)") }

// Prints: "true"
```

## See Also

### Applying matching criteria to elements

- [contains(where:)](<contains(where_).md>) — Publishes a Boolean value upon receiving an element that satisfies the predicate closure.
- [tryContains(where:)](<trycontains(where_).md>) — Publishes a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [allSatisfy(_:)](<allsatisfy(__).md>) — Publishes a single Boolean value that indicates whether all received elements pass a given predicate.
- [tryAllSatisfy(_:)](<tryallsatisfy(__).md>) — Publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.
