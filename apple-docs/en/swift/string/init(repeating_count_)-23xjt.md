---
title: 'init(repeating:count:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/init(repeating:count:)-23xjt'
source_url: 'https://developer.apple.com/documentation/swift/string/init(repeating:count:)-23xjt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28repeating%3Acount%3A%29-23xjt.json'
content_hash: 'sha256:b1659b8737aaab08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(repeating:count:)

<sub>Initializer</sub>

Creates a new string representing the given string repeated the specified number of times.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(repeating repeatedValue: String, count: Int)
```

## Parameters

- `repeatedValue` — The string to repeat.

- `count` — The number of times to repeat `repeatedValue` in the resulting string.

## Discussion

For example, you can use this initializer to create a string with ten `"ab"` strings in a row.

```swift
let s = String(repeating: "ab", count: 10)
print(s)
// Prints "abababababababababab"
```

## See Also

### Creating a String

- [init(decoding:)](<init(decoding_)-nm7v.md>) — Creates a string by interpreting the file path’s content as UTF-8 on Unix and UTF-16 on Windows.
- [init()](<init().md>) — Creates an empty string.
- [init(_:)](<init(__)-8v3fo.md>) — Creates a string containing the given character.
- [init(_:)](<init(__)-8og6g.md>) — Creates a new string containing the characters in the given sequence.
- [init(_:)](<init(__)-1ip93.md>) — Creates a new instance of a collection containing the elements of a sequence.
- [init(_:)](<init(__)-50pwi.md>) — Creates a new string containing the characters in the given sequence.
- [init(_:)](<init(__)-14lv5.md>) — Creates a new string from the given substring.
- [init(repeating:count:)](<init(repeating_count_)-11bpi.md>) — Creates a string representing the given character repeated the specified number of times.
- [init(unsafeUninitializedCapacity:initializingUTF8With:)](<init(unsafeuninitializedcapacity_initializingutf8with_).md>)
