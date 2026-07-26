---
title: 'drop(untilOutputFrom:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/drop(untiloutputfrom:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/drop(untiloutputfrom:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/drop%28untiloutputfrom%3A%29.json'
content_hash: 'sha256:6a7cb1148b3dc64d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# drop(untilOutputFrom:)

<sub>Instance Method</sub>

Ignores elements from the upstream publisher until it receives an element from a second publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func drop<P>(untilOutputFrom publisher: P) -> Publishers.DropUntilOutput<Self, P> where P : Publisher, Self.Failure == P.Failure
```

## Parameters

- `publisher` — A publisher to monitor for its first emitted element.

## Return Value

A publisher that drops elements from the upstream publisher until the `other` publisher produces a value.

## Discussion

Use [drop(untilOutputFrom:)](<drop(untiloutputfrom_).md>) to ignore elements from the upstream publisher until another, second, publisher delivers its first element. This publisher requests a single value from the second publisher, and it ignores (drops) all elements from the upstream publisher until the second publisher produces a value. After the second publisher produces an element, [drop(untilOutputFrom:)](<drop(untiloutputfrom_).md>) cancels its subscription to the second publisher, and allows events from the upstream publisher to pass through.

After this publisher receives a subscription from the upstream publisher, it passes through backpressure requests from downstream to the upstream publisher. If the upstream publisher acts on those requests before the other publisher produces an item, this publisher drops the elements it receives from the upstream publisher.

In the example below, the `pub1` publisher defers publishing its elements until the `pub2` publisher delivers its first element:

```swift
let upstream = PassthroughSubject<Int,Never>()
let second = PassthroughSubject<String,Never>()
cancellable = upstream
    .drop(untilOutputFrom: second)
    .sink { print("\($0)", terminator: " ") }

upstream.send(1)
upstream.send(2)
second.send("A")
upstream.send(3)
upstream.send(4)
// Prints "3 4"
```

## See Also

### Applying sequence operations to elements

- [dropFirst(_:)](<dropfirst(__).md>) — Omits the specified number of elements before republishing subsequent elements.
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
