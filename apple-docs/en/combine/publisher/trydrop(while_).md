---
title: 'tryDrop(while:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/trydrop(while:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/trydrop(while:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/trydrop%28while%3A%29.json'
content_hash: 'sha256:f823731b02f5247f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# tryDrop(while:)

<sub>Instance Method</sub>

Omits elements from the upstream publisher until an error-throwing closure returns false, before republishing all remaining elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryDrop(while predicate: @escaping (Self.Output) throws -> Bool) -> Publishers.TryDropWhile<Self>
```

## Parameters

- `predicate` — A closure that takes an element as a parameter and returns a Boolean value indicating whether to drop the element from the publisher’s output.

## Return Value

A publisher that skips over elements until the provided closure returns `false`, and then republishes all remaining elements. If the predicate closure throws, the publisher fails with an error.

## Discussion

Use [tryDrop(while:)](<trydrop(while_).md>) to omit elements from an upstream until an error-throwing closure you provide returns false, after which the remaining items in the stream are published. If the closure throws, no elements are emitted and the publisher fails with an error.

In the example below, elements are ignored until `-1` is encountered in the stream and the closure returns `false`. The publisher then republishes the remaining elements and finishes normally. Conversely, if the `guard` value in the closure had been encountered, the closure would throw and the publisher would fail with an error.

```swift
struct RangeError: Error {}
var numbers = [1, 2, 3, 4, 5, 6, -1, 7, 8, 9, 10]
let range: CountableClosedRange<Int> = (1...100)
cancellable = numbers.publisher
    .tryDrop {
        guard $0 != 0 else { throw RangeError() }
        return range.contains($0)
    }
    .sink(
        receiveCompletion: { print ("completion: \($0)") },
        receiveValue: { print ("value: \($0)") }
    )

// Prints: "-1 7 8 9 10 completion: finished"
// If instead numbers was [1, 2, 3, 4, 5, 6, 0, -1, 7, 8, 9, 10], tryDrop(while:) would fail with a RangeError.
```

## See Also

### Applying sequence operations to elements

- [drop(untilOutputFrom:)](<drop(untiloutputfrom_).md>) — Ignores elements from the upstream publisher until it receives an element from a second publisher.
- [dropFirst(_:)](<dropfirst(__).md>) — Omits the specified number of elements before republishing subsequent elements.
- [drop(while:)](<drop(while_).md>) — Omits elements from the upstream publisher until a given closure returns false, before republishing all remaining elements.
- [append(_:)](<append(__)-1qb8d.md>) — Appends a publisher’s output with the specified elements.
- [append(_:)](<append(__)-69sdn.md>) — Appends a publisher’s output with the specified sequence.
- [append(_:)](<append(__)-5yh02.md>) — Appends the output of this publisher with the elements emitted by the given publisher.
- [prepend(_:)](<prepend(__)-7wk5l.md>) — Prefixes a publisher’s output with the specified values.
- [prepend(_:)](<prepend(__)-v9sb.md>) — Prefixes a publisher’s output with the specified sequence.
- [prepend(_:)](<prepend(__)-5dj9c.md>) — Prefixes the output of this publisher with the elements emitted by the given publisher.
- [prefix(_:)](<prefix(__).md>) — Republishes elements up to the specified maximum count.
- [prefix(while:)](<prefix(while_).md>) — Republishes elements while a predicate closure indicates publishing should continue.
- [tryPrefix(while:)](<tryprefix(while_).md>) — Republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [prefix(untilOutputFrom:)](<prefix(untiloutputfrom_).md>) — Republishes elements until another publisher emits an element.
