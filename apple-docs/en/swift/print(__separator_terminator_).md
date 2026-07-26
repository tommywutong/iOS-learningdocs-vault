---
title: 'print(_:separator:terminator:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/print(_:separator:terminator:)'
source_url: 'https://developer.apple.com/documentation/swift/print(_:separator:terminator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/print%28_%3Aseparator%3Aterminator%3A%29.json'
content_hash: 'sha256:e096c5d714c1f76b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# print(_:separator:terminator:)

<sub>Function</sub>

Writes the textual representations of the given items into the standard output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func print(_ items: Any..., separator: String = " ", terminator: String = "\n")
```

## Parameters

- `items` — Zero or more items to print.

- `separator` — A string to print between each item. The default is a single space (`" "`).

- `terminator` — The string to print after all items have been printed. The default is a newline (`"\n"`).

## Discussion

You can pass zero or more items to the `print(_:separator:terminator:)` function. The textual representation for each item is the same as that obtained by calling `String(describing: item)`. The following example prints a string, a closed range of integers, and a group of floating-point values to standard output:

```swift
print("One two three four five")
// Prints "One two three four five"

print(1...5)
// Prints "1...5"

print(1.0, 2.0, 3.0, 4.0, 5.0)
// Prints "1.0 2.0 3.0 4.0 5.0"
```

To print the items separated by something other than a space, pass a string as `separator`.

```swift
print(1.0, 2.0, 3.0, 4.0, 5.0, separator: " ... ")
// Prints "1.0 ... 2.0 ... 3.0 ... 4.0 ... 5.0"
```

The output from each call to `print(_:separator:terminator:)` includes a newline by default. To print the items without a trailing newline, pass an empty string as `terminator`.

```swift
for n in 1...5 {
    print(n, terminator: "")
}
// Prints "12345"
```

## See Also

### Printing and Dumping

- [print(_:separator:terminator:to:)](<print(__separator_terminator_to_).md>) — Writes the textual representations of the given items into the given output stream.
- [debugPrint(_:separator:terminator:)](<debugprint(__separator_terminator_).md>) — Writes the textual representations of the given items most suitable for debugging into the standard output.
- [debugPrint(_:separator:terminator:to:)](<debugprint(__separator_terminator_to_).md>) — Writes the textual representations of the given items most suitable for debugging into the given output stream.
- [dump(_:name:indent:maxDepth:maxItems:)](<dump(__name_indent_maxdepth_maxitems_).md>) — Dumps the given object’s contents using its mirror to standard output.
- [dump(_:to:name:indent:maxDepth:maxItems:)](<dump(__to_name_indent_maxdepth_maxitems_).md>) — Dumps the given object’s contents using its mirror to the specified output stream.
