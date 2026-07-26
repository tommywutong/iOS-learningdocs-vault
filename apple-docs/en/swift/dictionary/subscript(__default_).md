---
title: 'subscript(_:default:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/subscript(_:default:)'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/subscript(_:default:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/subscript%28_%3Adefault%3A%29.json'
content_hash: 'sha256:35ca7de95b6fc60a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# subscript(_:default:)

<sub>Instance Subscript</sub>

Accesses the value with the given key, falling back to the given default value if the key isn’t found.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(key: Key, default defaultValue: @autoclosure () -> Value) -> Value { get set }
```

## Parameters

- `key` — The key the look up in the dictionary.

- `defaultValue` — The default value to use if `key` doesn’t exist in the dictionary.

## Return Value

The value associated with `key` in the dictionary; otherwise, `defaultValue`.

## Overview

Use this subscript when you want either the value for a particular key or, when that key is not present in the dictionary, a default value. This example uses the subscript with a message to use in case an HTTP response code isn’t recognized:

```swift
var responseMessages = [200: "OK",
                        403: "Access forbidden",
                        404: "File not found",
                        500: "Internal server error"]

let httpResponseCodes = [200, 403, 301]
for code in httpResponseCodes {
    let message = responseMessages[code, default: "Unknown response"]
    print("Response \(code): \(message)")
}
// Prints "Response 200: OK"
// Prints "Response 403: Access forbidden"
// Prints "Response 301: Unknown response"
```

When a dictionary’s `Value` type has value semantics, you can use this subscript to perform in-place operations on values in the dictionary. The following example uses this subscript while counting the occurrences of each letter in a string:

```swift
let message = "Hello, Elle!"
var letterCounts: [Character: Int] = [:]
for letter in message {
    letterCounts[letter, default: 0] += 1
}
// letterCounts == ["H": 1, "e": 2, "l": 4, "o": 1, ...]
```

When `letterCounts[letter, default: 0] += 1` is executed with a value of `letter` that isn’t already a key in `letterCounts`, the specified default value (`0`) is returned from the subscript, incremented, and then added to the dictionary under that key.

> [!note] Note
> Do not use this subscript to modify dictionary values if the dictionary’s `Value` type is a class. In that case, the default value and key are not written back to the dictionary after an operation.

## See Also

### Accessing Keys and Values

- [subscript(_:)](<subscript(__)-8rfql.md>) — Accesses the value associated with the given key for reading and writing.
- [index(forKey:)](<index(forkey_).md>) — Returns the index for the given key.
- [subscript(_:)](<subscript(__)-4bhoo.md>) — Accesses the key-value pair at the specified position.
- [keys](keys-swift.property.md) — A collection containing just the keys of the dictionary.
- [values](values-swift.property.md) — A collection containing just the values of the dictionary.
- [first](first.md) — The first element of the collection.
- [randomElement()](<randomelement().md>) — Returns a random element of the collection.
- [randomElement(using:)](<randomelement(using_).md>) — Returns a random element of the collection, using the given generator as a source for randomness.
