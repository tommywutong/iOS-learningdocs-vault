---
title: 'dropFirst(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/dropfirst(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/dropfirst(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/dropfirst%28_%3A%29.json'
content_hash: 'sha256:30648b2bbadbf977'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# dropFirst(_:)

<sub>Instance Method</sub>

Omits the specified number of elements before republishing subsequent elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dropFirst(_ count: Int = 1) -> Publishers.Drop<Self>
```

## Parameters

- `count` — The number of elements to omit. The default is `1`.

## Return Value

A publisher that doesn’t republish the first `count` elements.

## Discussion

Use [dropFirst(_:)](<dropfirst(__).md>) when you want to drop the first `n` elements from the upstream publisher, and republish the remaining elements.

The example below drops the first five elements from the stream:

```swift
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cancellable = numbers.publisher
    .dropFirst(5)
    .sink { print("\($0)", terminator: " ") }

// Prints: "6 7 8 9 10 "
```

## See Also

### Applying sequence operations to elements

- [drop(untilOutputFrom:)](<drop(untiloutputfrom_).md>) — Ignores elements from the upstream publisher until it receives an element from a second publisher.
- [drop(while:)](<drop(while_).md>) — Omits elements from the upstream publisher until a given closure returns false, before republishing all remaining elements.
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
