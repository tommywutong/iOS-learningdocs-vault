---
title: 'prepend(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/prepend(_:)-7wk5l'
source_url: 'https://developer.apple.com/documentation/combine/publisher/prepend(_:)-7wk5l'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/prepend%28_%3A%29-7wk5l.json'
content_hash: 'sha256:4117391b1db2fb29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# prepend(_:)

<sub>Instance Method</sub>

Prefixes a publisher’s output with the specified values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prepend(_ elements: Self.Output...) -> Publishers.Concatenate<Publishers.Sequence<[Self.Output], Self.Failure>, Self>
```

## Parameters

- `elements` — The elements to publish before this publisher’s elements.

## Return Value

A publisher that prefixes the specified elements prior to this publisher’s elements.

## Discussion

Use [prepend(_:)](<prepend(__)-7wk5l.md>) when you need to prepend specific elements before the output of a publisher.

In the example below, the [prepend(_:)](<prepend(__)-7wk5l.md>) operator publishes the provided elements before republishing all elements from `dataElements`:

```swift
let dataElements = (0...10)
cancellable = dataElements.publisher
    .prepend(0, 1, 255)
    .sink { print("\($0)", terminator: " ") }

// Prints: "0 1 255 0 1 2 3 4 5 6 7 8 9 10"
```

## See Also

### Applying sequence operations to elements

- [drop(untilOutputFrom:)](<drop(untiloutputfrom_).md>) — Ignores elements from the upstream publisher until it receives an element from a second publisher.
- [dropFirst(_:)](<dropfirst(__).md>) — Omits the specified number of elements before republishing subsequent elements.
- [drop(while:)](<drop(while_).md>) — Omits elements from the upstream publisher until a given closure returns false, before republishing all remaining elements.
- [tryDrop(while:)](<trydrop(while_).md>) — Omits elements from the upstream publisher until an error-throwing closure returns false, before republishing all remaining elements.
- [append(_:)](<append(__)-1qb8d.md>) — Appends a publisher’s output with the specified elements.
- [append(_:)](<append(__)-69sdn.md>) — Appends a publisher’s output with the specified sequence.
- [append(_:)](<append(__)-5yh02.md>) — Appends the output of this publisher with the elements emitted by the given publisher.
- [prepend(_:)](<prepend(__)-v9sb.md>) — Prefixes a publisher’s output with the specified sequence.
- [prepend(_:)](<prepend(__)-5dj9c.md>) — Prefixes the output of this publisher with the elements emitted by the given publisher.
- [prefix(_:)](<prefix(__).md>) — Republishes elements up to the specified maximum count.
- [prefix(while:)](<prefix(while_).md>) — Republishes elements while a predicate closure indicates publishing should continue.
- [tryPrefix(while:)](<tryprefix(while_).md>) — Republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [prefix(untilOutputFrom:)](<prefix(untiloutputfrom_).md>) — Republishes elements until another publisher emits an element.
