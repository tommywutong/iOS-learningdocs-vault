---
title: 'contains(where:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/contains(where:)'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/contains(where:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/contains%28where%3A%29.json'
content_hash: 'sha256:e46d3023ddceaf05'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# contains(where:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(where predicate: (Self.Element) throws -> Bool) rethrows -> Bool
```

## Parameters

- `predicate` — A closure that takes an element of the sequence as its argument and returns a Boolean value that indicates whether the passed element represents a match.

## Return Value

`true` if the sequence contains an element that satisfies `predicate`; otherwise, `false`.

## Discussion

You can use the predicate to check for an element of a type that doesn’t conform to the `Equatable` protocol, such as the `HTTPResponse` enumeration in this example.

```swift
enum HTTPResponse {
    case ok
    case error(Int)
}

let lastThreeResponses: [HTTPResponse] = [.ok, .ok, .error(404)]
let hadError = lastThreeResponses.contains { element in
    if case .error = element {
        return true
    } else {
        return false
    }
}
// 'hadError' == true
```

Alternatively, a predicate can be satisfied by a range of `Equatable` elements or a general condition. This example shows how you can check an array for an expense greater than $100.

```swift
let expenses = [21.37, 55.21, 9.32, 10.18, 388.77, 11.41]
let hasBigPurchase = expenses.contains { $0 > 100 }
// 'hasBigPurchase' == true
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the sequence.

## See Also

### Finding Elements

- [allSatisfy(_:)](<allsatisfy(__).md>) — Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [first(where:)](<first(where_).md>) — Returns the first element of the sequence that satisfies the given predicate.
- [firstIndex(where:)](<firstindex(where_).md>) — Returns the first index in which an element of the collection satisfies the given predicate.
- [min(by:)](<min(by_).md>) — Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [max(by:)](<max(by_).md>) — Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
