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
doc_path: '/documentation/combine/publisher/prepend(_:)-v9sb'
source_url: 'https://developer.apple.com/documentation/combine/publisher/prepend(_:)-v9sb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/prepend%28_%3A%29-v9sb.json'
content_hash: 'sha256:04dbf39940d53f41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# prepend(_:)

<sub>Instance Method</sub>

Prefixes a publisher’s output with the specified sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prepend<S>(_ elements: S) -> Publishers.Concatenate<Publishers.Sequence<S, Self.Failure>, Self> where S : Sequence, Self.Output == S.Element
```

## Parameters

- `elements` — A sequence of elements to publish before this publisher’s elements.

## Return Value

A publisher that prefixes the sequence of elements prior to this publisher’s elements.

## Discussion

Use [prepend(_:)](<prepend(__)-v9sb.md>) to publish values from two publishers when you need to prepend one publisher’s elements to another.

In this example the [prepend(_:)](<prepend(__)-v9sb.md>) operator publishes the provided sequence before republishing all elements from `dataElements`:

```swift
let prefixValues = [0, 1, 255]
let dataElements = (0...10)
cancellable = dataElements.publisher
    .prepend(prefixValues)
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
- [prepend(_:)](<prepend(__)-7wk5l.md>) — Prefixes a publisher’s output with the specified values.
- [prepend(_:)](<prepend(__)-5dj9c.md>) — Prefixes the output of this publisher with the elements emitted by the given publisher.
- [prefix(_:)](<prefix(__).md>) — Republishes elements up to the specified maximum count.
- [prefix(while:)](<prefix(while_).md>) — Republishes elements while a predicate closure indicates publishing should continue.
- [tryPrefix(while:)](<tryprefix(while_).md>) — Republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [prefix(untilOutputFrom:)](<prefix(untiloutputfrom_).md>) — Republishes elements until another publisher emits an element.
