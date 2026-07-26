---
title: 'map(_:_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/map(_:_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/map(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/map%28_%3A_%3A%29.json'
content_hash: 'sha256:b76b6ce6b814f120'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# map(_:_:)

<sub>Instance Method</sub>

Publishes the values of two key paths as a tuple.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func map<T0, T1>(_ keyPath0: KeyPath<Self.Output, T0>, _ keyPath1: KeyPath<Self.Output, T1>) -> Publishers.MapKeyPath2<Self, T0, T1>
```

## Parameters

- `keyPath0` — The key path of a property on `Output`.

- `keyPath1` — The key path of another property on `Output`.

## Return Value

A publisher that publishes the values of two key paths as a tuple.

## Discussion

In the following example, the [map(_:_:)](<map(____).md>) operator uses the Swift key path syntax to access the `die1` and `die2` members of the `DiceRoll` structure published by the [Just](../just.md) publisher.

The downstream sink subscriber receives only these two values (as an `(Int, Int)` tuple), not the entire `DiceRoll`.

```swift
struct DiceRoll {
    let die1: Int
    let die2: Int
}

cancellable = Just(DiceRoll(die1:Int.random(in:1...6),
                            die2: Int.random(in:1...6)))
    .map(\.die1, \.die2)
    .sink { values in
        print ("Rolled: \(values.0), \(values.1) (total: \(values.0 + values.1))")
    }
// Prints "Rolled: 6, 4 (total: 10)" (or other random values).
```

## See Also

### Identifying properties with key paths

- [map(_:)](<map(__)-6sm0a.md>) — Publishes the value of a key path.
- [map(_:_:_:)](<map(______).md>) — Publishes the values of three key paths as a tuple.
