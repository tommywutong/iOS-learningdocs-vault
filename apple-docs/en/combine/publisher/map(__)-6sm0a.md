---
title: 'map(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/map(_:)-6sm0a'
source_url: 'https://developer.apple.com/documentation/combine/publisher/map(_:)-6sm0a'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/map%28_%3A%29-6sm0a.json'
content_hash: 'sha256:c904e8d6b6f0f9de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# map(_:)

<sub>Instance Method</sub>

Publishes the value of a key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func map<T>(_ keyPath: KeyPath<Self.Output, T>) -> Publishers.MapKeyPath<Self, T>
```

## Parameters

- `keyPath` — The key path of a property on `Output`.

## Return Value

A publisher that publishes the value of the key path.

## Discussion

In the following example, the [map(_:)](<map(__)-6sm0a.md>) operator uses the Swift key path syntax to access the `die` member of the `DiceRoll` structure published by the [Just](../just.md) publisher.

The downstream sink subscriber receives only the value of this `Int`, not the entire `DiceRoll`.

```swift
struct DiceRoll {
    let die: Int
}

cancellable = Just(DiceRoll(die:Int.random(in:1...6)))
    .map(\.die)
    .sink {
        print ("Rolled: \($0)")
    }
// Prints "Rolled: 3" (or some other random value).
```

## See Also

### Identifying properties with key paths

- [map(_:_:)](<map(____).md>) — Publishes the values of two key paths as a tuple.
- [map(_:_:_:)](<map(______).md>) — Publishes the values of three key paths as a tuple.
