---
title: ExpressibleByDictionaryLiteral
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/expressiblebydictionaryliteral
source_url: 'https://developer.apple.com/documentation/swift/expressiblebydictionaryliteral'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/expressiblebydictionaryliteral.json'
content_hash: 'sha256:b89b617343c167b1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ExpressibleByDictionaryLiteral

<sub>Protocol</sub>

A type that can be initialized using a dictionary literal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ExpressibleByDictionaryLiteral
```

## Overview

A dictionary literal is a simple way of writing a list of key-value pairs. You write each key-value pair with a colon (`:`) separating the key and the value. The dictionary literal is made up of one or more key-value pairs, separated by commas and surrounded with square brackets.

To declare a dictionary, assign a dictionary literal to a variable or constant:

```swift
let countryCodes = ["BR": "Brazil", "GH": "Ghana",
                    "JP": "Japan", "US": "United States"]
// 'countryCodes' has type '[String: String]'

print(countryCodes["BR"]!)
// Prints "Brazil"
```

When the context provides enough type information, you can use a special form of the dictionary literal, square brackets surrounding a single colon, to initialize an empty dictionary.

```swift
var frequencies: [String: Int] = [:]
print(frequencies.count)
// Prints "0"
```

> [!note] Note
> A dictionary literal is _not_ the same as an instance of `Dictionary`. You can’t initialize a type that conforms to `ExpressibleByDictionaryLiteral` simply by assigning an instance of `Dictionary`, `KeyValuePairs`, or similar.

## Conforming to the ExpressibleByDictionaryLiteral Protocol

To add the capability to be initialized with a dictionary literal to your own custom types, declare an `init(dictionaryLiteral:)` initializer. The following example shows the dictionary literal initializer for a hypothetical `CountedSet` type, which uses setlike semantics while keeping track of the count for duplicate elements:

```swift
struct CountedSet<Element: Hashable>: Collection, SetAlgebra {
    // implementation details

    /// Updates the count stored in the set for the given element,
    /// adding the element if necessary.
    ///
    /// - Parameter n: The new count for `element`. `n` must be greater
    ///   than or equal to zero.
    /// - Parameter element: The element to set the new count on.
    mutating func updateCount(_ n: Int, for element: Element)
}

extension CountedSet: ExpressibleByDictionaryLiteral {
    init(dictionaryLiteral elements: (Element, Int)...) {
        self.init()
        for (element, count) in elements {
            self.updateCount(count, for: element)
        }
    }
}
```

## Relationships

- **Conforming Types**: [Dictionary](dictionary.md), [KeyValuePairs](keyvaluepairs.md)

## Topics

### Associated Types

- [Key](expressiblebydictionaryliteral/key.md) — The key type of a dictionary literal.
- [Value](expressiblebydictionaryliteral/value.md) — The value type of a dictionary literal.

### Initializers

- [init(dictionaryLiteral:)](<expressiblebydictionaryliteral/init(dictionaryliteral_).md>) — Creates an instance initialized with the given key-value pairs.

## See Also

### Collection Literals

- [ExpressibleByArrayLiteral](expressiblebyarrayliteral.md) — A type that can be initialized using an array literal.
