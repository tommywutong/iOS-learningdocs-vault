---
title: 'dump(_:to:name:indent:maxDepth:maxItems:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dump(_:to:name:indent:maxdepth:maxitems:)'
source_url: 'https://developer.apple.com/documentation/swift/dump(_:to:name:indent:maxdepth:maxitems:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dump%28_%3Ato%3Aname%3Aindent%3Amaxdepth%3Amaxitems%3A%29.json'
content_hash: 'sha256:acf51e3d2926e931'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# dump(_:to:name:indent:maxDepth:maxItems:)

<sub>Function</sub>

Dumps the given object’s contents using its mirror to the specified output stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func dump<T, TargetStream>(_ value: T, to target: inout TargetStream, name: String? = nil, indent: Int = 0, maxDepth: Int = .max, maxItems: Int = .max) -> T where TargetStream : TextOutputStream
```

## Parameters

- `value` — The value to output to the `target` stream.

- `target` — The stream to use for writing the contents of `value`.

- `name` — A label to use when writing the contents of `value`. When `nil` is passed, the label is omitted. The default is `nil`.

- `indent` — The number of spaces to use as an indent for each line of the output. The default is `0`.

- `maxDepth` — The maximum depth to descend when writing the contents of a value that has nested components. The default is `Int.max`.

- `maxItems` — The maximum number of elements for which to write the full contents. The default is `Int.max`.

## Return Value

The instance passed as `value`.

## See Also

### Printing and Dumping

- [print(_:separator:terminator:)](<print(__separator_terminator_).md>) — Writes the textual representations of the given items into the standard output.
- [print(_:separator:terminator:to:)](<print(__separator_terminator_to_).md>) — Writes the textual representations of the given items into the given output stream.
- [debugPrint(_:separator:terminator:)](<debugprint(__separator_terminator_).md>) — Writes the textual representations of the given items most suitable for debugging into the standard output.
- [debugPrint(_:separator:terminator:to:)](<debugprint(__separator_terminator_to_).md>) — Writes the textual representations of the given items most suitable for debugging into the given output stream.
- [dump(_:name:indent:maxDepth:maxItems:)](<dump(__name_indent_maxdepth_maxitems_).md>) — Dumps the given object’s contents using its mirror to standard output.
