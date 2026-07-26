---
title: 'init(reflecting:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/init(reflecting:)'
source_url: 'https://developer.apple.com/documentation/swift/string/init(reflecting:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28reflecting%3A%29.json'
content_hash: 'sha256:cb39af452ef456bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(reflecting:)

<sub>Initializer</sub>

Creates a string with a detailed representation of the given value, suitable for debugging.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Subject>(reflecting subject: Subject)
```

## Discussion

Use this initializer to convert an instance of any type to its custom debugging representation. The initializer creates the string representation of `instance` in one of the following ways, depending on its protocol conformance:

- If `subject` conforms to the `CustomDebugStringConvertible` protocol, the result is `subject.debugDescription`.
- If `subject` conforms to the `CustomStringConvertible` protocol, the result is `subject.description`.
- If `subject` conforms to the `TextOutputStreamable` protocol, the result is obtained by calling `subject.write(to: s)` on an empty string `s`.
- An unspecified result is supplied automatically by the Swift standard library.

For example, this custom `Point` struct uses the default representation supplied by the standard library.

```swift
struct Point {
    let x: Int, y: Int
}

let p = Point(x: 21, y: 30)
print(String(reflecting: p))
// Prints "p: Point = {
//           x = 21
//           y = 30
//         }"
```

After adding `CustomDebugStringConvertible` conformance by implementing the `debugDescription` property, `Point` provides its own custom debugging representation.

```swift
extension Point: CustomDebugStringConvertible {
    var debugDescription: String {
        return "Point(x: \(x), y: \(y))"
    }
}

print(String(reflecting: p))
// Prints "Point(x: 21, y: 30)"
```

## See Also

### Converting Other Types to Strings

- [init(_:)](<init(__)-1ywfq.md>) — Creates an instance from the description of a given `LosslessStringConvertible` instance.
- [init(describing:)](<init(describing_)-588wb.md>) — Creates a string representing the given value.
- [init(describing:)](<init(describing_)-hsqw.md>) — Creates a string representing the given value.
- [init(describing:)](<init(describing_)-6ttci.md>) — Creates a string representing the given value.
- [init(describing:)](<init(describing_)-67ncf.md>) — Creates a string representing the given value.
