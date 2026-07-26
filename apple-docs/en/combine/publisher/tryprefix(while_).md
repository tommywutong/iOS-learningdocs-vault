---
title: 'tryPrefix(while:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/tryprefix(while:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/tryprefix(while:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/tryprefix%28while%3A%29.json'
content_hash: 'sha256:f5644ba190424db1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# tryPrefix(while:)

<sub>Instance Method</sub>

Republishes elements while an error-throwing predicate closure indicates publishing should continue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryPrefix(while predicate: @escaping (Self.Output) throws -> Bool) -> Publishers.TryPrefixWhile<Self>
```

## Parameters

- `predicate` — A closure that takes an element as its parameter and returns a Boolean value indicating whether publishing should continue.

## Return Value

A publisher that passes through elements until the predicate throws or indicates publishing should finish.

## Discussion

Use [tryPrefix(while:)](<tryprefix(while_).md>) to emit values from the upstream publisher that meet a condition you specify in an error-throwing closure. The publisher finishes when the closure returns `false`. If the closure throws an error, the publisher fails with that error.

```swift
struct OutOfRangeError: Error {}

let numbers = (0...10).reversed()
cancellable = numbers.publisher
    .tryPrefix {
        guard $0 != 0 else {throw OutOfRangeError()}
        return $0 <= numbers.max()!
    }
    .sink(
        receiveCompletion: { print ("completion: \($0)", terminator: " ") },
        receiveValue: { print ("\($0)", terminator: " ") }
    )

// Prints: "10 9 8 7 6 5 4 3 2 1 completion: failure(OutOfRangeError()) "
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
- [prefix(while:)](<prefix(while_).md>) — Republishes elements while a predicate closure indicates publishing should continue.
- [prefix(untilOutputFrom:)](<prefix(untiloutputfrom_).md>) — Republishes elements until another publisher emits an element.
