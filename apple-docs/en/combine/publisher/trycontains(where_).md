---
title: 'tryContains(where:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/trycontains(where:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/trycontains(where:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/trycontains%28where%3A%29.json'
content_hash: 'sha256:4e4820fef0bfcaf4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# tryContains(where:)

<sub>Instance Method</sub>

Publishes a Boolean value upon receiving an element that satisfies the throwing predicate closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryContains(where predicate: @escaping (Self.Output) throws -> Bool) -> Publishers.TryContainsWhere<Self>
```

## Parameters

- `predicate` — A closure that takes an element as its parameter and returns a Boolean value that indicates whether the element satisfies the closure’s comparison logic.

## Return Value

A publisher that emits the Boolean value `true` when the upstream publisher emits a matching value.

## Discussion

Use [tryContains(where:)](<trycontains(where_).md>) to find the first element in an upstream that satisfies the error-throwing closure you provide.

This operator consumes elements produced from the upstream publisher until the upstream publisher either:

- Produces a matching element, after which it emits `true` and the publisher finishes normally.
- Emits `false` if no matching element is found and the publisher finishes normally.

If the predicate throws an error, the publisher fails, passing the error to its downstream.

In the example below, the [tryContains(where:)](<trycontains(where_).md>) operator tests values to find an element less than `10`; when the closure finds an odd number, like `3`, the publisher terminates with an `IllegalValueError`.

```swift
struct IllegalValueError: Error {}

let numbers = [3, 2, 10, 5, 0, 9]
numbers.publisher
    .tryContains {
        if ($0 % 2 != 0) {
            throw IllegalValueError()
        }
       return $0 < 10
    }
    .sink(
        receiveCompletion: { print ("completion: \($0)") },
        receiveValue: { print ("value: \($0)") }
    )

// Prints: "completion: failure(IllegalValueError())"
```

## See Also

### Applying matching criteria to elements

- [contains(_:)](<contains(__).md>) — Publishes a Boolean value upon receiving an element equal to the argument.
- [contains(where:)](<contains(where_).md>) — Publishes a Boolean value upon receiving an element that satisfies the predicate closure.
- [allSatisfy(_:)](<allsatisfy(__).md>) — Publishes a single Boolean value that indicates whether all received elements pass a given predicate.
- [tryAllSatisfy(_:)](<tryallsatisfy(__).md>) — Publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.
