---
title: 'print(_:separator:terminator:to:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/print(_:separator:terminator:to:)'
source_url: 'https://developer.apple.com/documentation/swift/print(_:separator:terminator:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/print%28_%3Aseparator%3Aterminator%3Ato%3A%29.json'
content_hash: 'sha256:2a0cc06cdbb83787'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# print(_:separator:terminator:to:)

<sub>Function</sub>

Writes the textual representations of the given items into the given output stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func print<Target>(_ items: Any..., separator: String = " ", terminator: String = "\n", to output: inout Target) where Target : TextOutputStream
```

## Parameters

- `items` — Zero or more items to print.

- `separator` — A string to print between each item. The default is a single space (`" "`).

- `terminator` — The string to print after all items have been printed. The default is a newline (`"\n"`).

- `output` — An output stream to receive the text representation of each item.

## Discussion

You can pass zero or more items to the `print(_:separator:terminator:to:)` function. The textual representation for each item is the same as that obtained by calling `String(describing: item)`. The following example prints a closed range of integers to a string:

```swift
var range = "My range: "
print(1...5, to: &range)
// range == "My range: 1...5\n"
```

To print the items separated by something other than a space, pass a string as `separator`.

```swift
var separated = ""
print(1.0, 2.0, 3.0, 4.0, 5.0, separator: " ... ", to: &separated)
// separated == "1.0 ... 2.0 ... 3.0 ... 4.0 ... 5.0\n"
```

The output from each call to `print(_:separator:terminator:to:)` includes a newline by default. To print the items without a trailing newline, pass an empty string as `terminator`.

```swift
var numbers = ""
for n in 1...5 {
    print(n, terminator: "", to: &numbers)
}
// numbers == "12345"
```

## See Also

### Printing and Dumping

- [print(_:separator:terminator:)](<print(__separator_terminator_).md>) — Writes the textual representations of the given items into the standard output.
- [debugPrint(_:separator:terminator:)](<debugprint(__separator_terminator_).md>) — Writes the textual representations of the given items most suitable for debugging into the standard output.
- [debugPrint(_:separator:terminator:to:)](<debugprint(__separator_terminator_to_).md>) — Writes the textual representations of the given items most suitable for debugging into the given output stream.
- [dump(_:name:indent:maxDepth:maxItems:)](<dump(__name_indent_maxdepth_maxitems_).md>) — Dumps the given object’s contents using its mirror to standard output.
- [dump(_:to:name:indent:maxDepth:maxItems:)](<dump(__to_name_indent_maxdepth_maxitems_).md>) — Dumps the given object’s contents using its mirror to the specified output stream.
