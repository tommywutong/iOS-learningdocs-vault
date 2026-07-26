---
title: 'prefix(while:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/prefix(while:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/prefix(while:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/prefix%28while%3A%29.json'
content_hash: 'sha256:6ee4e741eeafbc98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# prefix(while:)

<sub>Instance Method</sub>

Republishes elements while a predicate closure indicates publishing should continue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prefix(while predicate: @escaping (Self.Output) -> Bool) -> Publishers.PrefixWhile<Self>
```

## Parameters

- `predicate` — A closure that takes an element as its parameter and returns a Boolean value that indicates whether publishing should continue.

## Return Value

A publisher that passes through elements until the predicate indicates publishing should finish.

## Discussion

Use [prefix(while:)](<prefix(while_).md>) to emit values while elements from the upstream publisher meet a condition you specify. The publisher finishes when the closure returns `false`.

In the example below, the [prefix(while:)](<prefix(while_).md>) operator emits values while the element it receives is less than five:

```swift
let numbers = (0...10)
numbers.publisher
    .prefix { $0 < 5 }
    .sink { print("\($0)", terminator: " ") }

// Prints: "0 1 2 3 4"
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
- [prepend(_:)](<prepend(__)-v9sb.md>) — Prefixes a publisher’s output with the specified sequence.
- [prepend(_:)](<prepend(__)-5dj9c.md>) — Prefixes the output of this publisher with the elements emitted by the given publisher.
- [prefix(_:)](<prefix(__).md>) — Republishes elements up to the specified maximum count.
- [tryPrefix(while:)](<tryprefix(while_).md>) — Republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [prefix(untilOutputFrom:)](<prefix(untiloutputfrom_).md>) — Republishes elements until another publisher emits an element.
