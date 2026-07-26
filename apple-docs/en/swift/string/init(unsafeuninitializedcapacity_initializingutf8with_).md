---
title: 'init(unsafeUninitializedCapacity:initializingUTF8With:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/init(unsafeuninitializedcapacity:initializingutf8with:)'
source_url: 'https://developer.apple.com/documentation/swift/string/init(unsafeuninitializedcapacity:initializingutf8with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28unsafeuninitializedcapacity%3Ainitializingutf8with%3A%29.json'
content_hash: 'sha256:7c00ee1b04fbde89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(unsafeUninitializedCapacity:initializingUTF8With:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<E>(unsafeUninitializedCapacity capacity: Int, initializingUTF8With initializer: (UnsafeMutableBufferPointer<UInt8>) throws(E) -> Int) throws(E) where E : Error
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
- [init(repeating:count:)](<init(repeating_count_)-23xjt.md>) — Creates a new string representing the given string repeated the specified number of times.
- [init(repeating:count:)](<init(repeating_count_)-11bpi.md>) — Creates a string representing the given character repeated the specified number of times.
