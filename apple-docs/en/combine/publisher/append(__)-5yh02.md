---
title: 'append(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/append(_:)-5yh02'
source_url: 'https://developer.apple.com/documentation/combine/publisher/append(_:)-5yh02'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/append%28_%3A%29-5yh02.json'
content_hash: 'sha256:3c908a6c49ad128d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# append(_:)

<sub>Instance Method</sub>

Appends the output of this publisher with the elements emitted by the given publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func append<P>(_ publisher: P) -> Publishers.Concatenate<Self, P> where P : Publisher, Self.Failure == P.Failure, Self.Output == P.Output
```

## Parameters

- `publisher` — The appending publisher.

## Return Value

A publisher that appends the appending publisher’s elements after this publisher’s elements.

## Discussion

Use [append(_:)](<append(__)-5yh02.md>) to append the output of one publisher to another. The [append(_:)](<append(__)-5yh02.md>) operator produces no elements until this publisher finishes. It then produces this publisher’s elements, followed by the given publisher’s elements. If this publisher fails with an error, the given publishers elements aren’t published.

In the example below, the `append` publisher republishes all elements from the `numbers` publisher until it finishes, then publishes all elements from the `otherNumbers` publisher:

```swift
let numbers = (0...10)
let otherNumbers = (25...35)
cancellable = numbers.publisher
    .append(otherNumbers.publisher)
    .sink { print("\($0)", terminator: " ") }

// Prints: "0 1 2 3 4 5 6 7 8 9 10 25 26 27 28 29 30 31 32 33 34 35 "
```

## See Also

### Applying sequence operations to elements

- [drop(untilOutputFrom:)](<drop(untiloutputfrom_).md>) — Ignores elements from the upstream publisher until it receives an element from a second publisher.
- [dropFirst(_:)](<dropfirst(__).md>) — Omits the specified number of elements before republishing subsequent elements.
- [drop(while:)](<drop(while_).md>) — Omits elements from the upstream publisher until a given closure returns false, before republishing all remaining elements.
- [tryDrop(while:)](<trydrop(while_).md>) — Omits elements from the upstream publisher until an error-throwing closure returns false, before republishing all remaining elements.
- [append(_:)](<append(__)-1qb8d.md>) — Appends a publisher’s output with the specified elements.
- [append(_:)](<append(__)-69sdn.md>) — Appends a publisher’s output with the specified sequence.
- [prepend(_:)](<prepend(__)-7wk5l.md>) — Prefixes a publisher’s output with the specified values.
- [prepend(_:)](<prepend(__)-v9sb.md>) — Prefixes a publisher’s output with the specified sequence.
- [prepend(_:)](<prepend(__)-5dj9c.md>) — Prefixes the output of this publisher with the elements emitted by the given publisher.
- [prefix(_:)](<prefix(__).md>) — Republishes elements up to the specified maximum count.
- [prefix(while:)](<prefix(while_).md>) — Republishes elements while a predicate closure indicates publishing should continue.
- [tryPrefix(while:)](<tryprefix(while_).md>) — Republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [prefix(untilOutputFrom:)](<prefix(untiloutputfrom_).md>) — Republishes elements until another publisher emits an element.
