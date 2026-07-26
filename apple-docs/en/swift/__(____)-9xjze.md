---
title: '??(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/__(_:_:)-9xjze'
source_url: 'https://developer.apple.com/documentation/swift/__(_:_:)-9xjze'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/__%28_%3A_%3A%29-9xjze.json'
content_hash: 'sha256:fd6dc10bb26d62ce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ??(_:_:)

<sub>Operator</sub>

Performs a nil-coalescing operation, returning the wrapped value of an `Optional` instance or a default value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func ?? <T>(optional: consuming T?, defaultValue: @autoclosure () throws -> T) rethrows -> T where T : ~Copyable
```

## Parameters

- `optional` — An optional value.

- `defaultValue` — A value to use as a default. `defaultValue` is the same type as the `Wrapped` type of `optional`.

## Discussion

A nil-coalescing operation unwraps the left-hand side if it has a value, or it returns the right-hand side as a default. The result of this operation will have the non-optional type of the left-hand side’s `Wrapped` type.

This operator uses short-circuit evaluation: `optional` is checked first, and `defaultValue` is evaluated only if `optional` is `nil`. For example:

```swift
func getDefault() -> Int {
    print("Calculating default...")
    return 42
}

let goodNumber = Int("100") ?? getDefault()
// goodNumber == 100

let notSoGoodNumber = Int("invalid-input") ?? getDefault()
// Prints "Calculating default..."
// notSoGoodNumber == 42
```

In this example, `goodNumber` is assigned a value of `100` because `Int("100")` succeeded in returning a non-`nil` result. When `notSoGoodNumber` is initialized, `Int("invalid-input")` fails and returns `nil`, and so the `getDefault()` method is called to supply a default value.

## See Also

### Coalescing Nil Values

- [??(_:_:)](<__(____)-1fjjj.md>) — Performs a nil-coalescing operation, returning the wrapped value of an `Optional` instance or a default `Optional` value.
