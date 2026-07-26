---
title: 'forEach(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/foreach(_:)'
source_url: 'https://developer.apple.com/documentation/swift/string/foreach(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/foreach%28_%3A%29.json'
content_hash: 'sha256:162912b7e331c2c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# forEach(_:)

<sub>Instance Method</sub>

Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func forEach(_ body: (Self.Element) throws -> Void) rethrows
```

## Parameters

- `body` — A closure that takes an element of the sequence as a parameter.

## Discussion

The two loops in the following example produce the same output:

```swift
let numberWords = ["one", "two", "three"]
for word in numberWords {
    print(word)
}
// Prints "one"
// Prints "two"
// Prints "three"

numberWords.forEach { word in
    print(word)
}
// Same as above
```

Using the `forEach` method is distinct from a `for`-`in` loop in two important ways:

1. You cannot use a `break` or `continue` statement to exit the current call of the `body` closure or skip subsequent calls.
2. Using the `return` statement in the `body` closure will exit only from the current call to `body`, not from any outer scope, and won’t skip subsequent calls.

## See Also

### Iterating over a String’s Characters

- [enumerated()](<enumerated().md>) — Returns a sequence of pairs (_n_, _x_), where _n_ represents a consecutive integer starting at zero and _x_ represents an element of the sequence.
- [makeIterator()](<makeiterator().md>) — Returns an iterator over the elements of the collection.
- [underestimatedCount](underestimatedcount.md) — A value less than or equal to the number of elements in the collection.
