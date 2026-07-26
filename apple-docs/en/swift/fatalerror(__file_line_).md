---
title: 'fatalError(_:file:line:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/fatalerror(_:file:line:)'
source_url: 'https://developer.apple.com/documentation/swift/fatalerror(_:file:line:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/fatalerror%28_%3Afile%3Aline%3A%29.json'
content_hash: 'sha256:1fe8011435cbae9a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# fatalError(_:file:line:)

<sub>Function</sub>

Unconditionally prints a given message and stops execution.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fatalError(_ message: @autoclosure () -> String = String(), file: StaticString = #file, line: UInt = #line) -> Never
```

## Parameters

- `message` — The string to print. The default is an empty string.

- `file` — The file name to print with `message`. The default is the file where `fatalError(_:file:line:)` is called.

- `line` — The line number to print along with `message`. The default is the line number where `fatalError(_:file:line:)` is called.

## See Also

### Exiting a Program

- [Never](never.md) — A type that has no values and can’t be constructed.
