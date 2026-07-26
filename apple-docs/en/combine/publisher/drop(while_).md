---
title: 'drop(while:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/drop(while:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/drop(while:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/drop%28while%3A%29.json'
content_hash: 'sha256:320e71aebc7ab36c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# drop(while:)

<sub>Instance Method</sub>

Omits elements from the upstream publisher until a given closure returns false, before republishing all remaining elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func drop(while predicate: @escaping (Self.Output) -> Bool) -> Publishers.DropWhile<Self>
```

## Parameters

- `predicate` — A closure that takes an element as a parameter and returns a Boolean value indicating whether to drop the element from the publisher’s output.

## Return Value

A publisher that skips over elements until the provided closure returns `false`.

## Discussion

Use [drop(while:)](<drop(while_).md>) to omit elements from an upstream publisher until the element received meets a condition you specify.

In the example below, the operator omits all elements in the stream until the first element arrives that’s a positive integer, after which the operator publishes all remaining elements:

```swift
let numbers = [-62, -1, 0, 10, 0, 22, 41, -1, 5]
cancellable = numbers.publisher
    .drop { $0 <= 0 }
    .sink { print("\($0)") }

// Prints: "10 0, 22 41 -1 5"
```

## See Also

### Applying sequence operations to elements

- [drop(untilOutputFrom:)](<drop(untiloutputfrom_).md>) — Ignores elements from the upstream publisher until it receives an element from a second publisher.
- [dropFirst(_:)](<dropfirst(__).md>) — Omits the specified number of elements before republishing subsequent elements.
- [tryDrop(while:)](<trydrop(while_).md>) — Omits elements from the upstream publisher until an error-throwing closure returns false, before republishing all remaining elements.
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
