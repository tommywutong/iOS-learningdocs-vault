---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/init(_:)-14lv5'
source_url: 'https://developer.apple.com/documentation/swift/string/init(_:)-14lv5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28_%3A%29-14lv5.json'
content_hash: 'sha256:8151fe64ce785221'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(_:)

<sub>Initializer</sub>

Creates a new string from the given substring.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ substring: Substring)
```

## Parameters

- `substring` — A substring to convert to a standalone `String` instance.

## Discussion

> [!abstract] Complexity
> O(_n_), where _n_ is the length of `substring`.

## See Also

### Creating a String

- [init(decoding:)](<init(decoding_)-nm7v.md>) — Creates a string by interpreting the file path’s content as UTF-8 on Unix and UTF-16 on Windows.
- [init()](<init().md>) — Creates an empty string.
- [init(_:)](<init(__)-8v3fo.md>) — Creates a string containing the given character.
- [init(_:)](<init(__)-8og6g.md>) — Creates a new string containing the characters in the given sequence.
- [init(_:)](<init(__)-1ip93.md>) — Creates a new instance of a collection containing the elements of a sequence.
- [init(_:)](<init(__)-50pwi.md>) — Creates a new string containing the characters in the given sequence.
- [init(repeating:count:)](<init(repeating_count_)-23xjt.md>) — Creates a new string representing the given string repeated the specified number of times.
- [init(repeating:count:)](<init(repeating_count_)-11bpi.md>) — Creates a string representing the given character repeated the specified number of times.
- [init(unsafeUninitializedCapacity:initializingUTF8With:)](<init(unsafeuninitializedcapacity_initializingutf8with_).md>)
