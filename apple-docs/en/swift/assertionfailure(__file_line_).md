---
title: 'assertionFailure(_:file:line:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/assertionfailure(_:file:line:)'
source_url: 'https://developer.apple.com/documentation/swift/assertionfailure(_:file:line:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/assertionfailure%28_%3Afile%3Aline%3A%29.json'
content_hash: 'sha256:9d335bef4add5144'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# assertionFailure(_:file:line:)

<sub>Function</sub>

Indicates that an internal consistency check failed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func assertionFailure(_ message: @autoclosure () -> String = String(), file: StaticString = #file, line: UInt = #line)
```

## Parameters

- `message` — A string to print in a playground or `-Onone` build. The default is an empty string.

- `file` — The file name to print with `message`. The default is the file where `assertionFailure(_:file:line:)` is called.

- `line` — The line number to print along with `message`. The default is the line number where `assertionFailure(_:file:line:)` is called.

## Discussion

This function’s effect varies depending on the build flag used:

- In playgrounds and `-Onone` builds (the default for Xcode’s Debug configuration), stop program execution in a debuggable state after printing `message`.
- In `-O` builds, has no effect.
- In `-Ounchecked` builds, the optimizer may assume that this function is never called. Failure to satisfy that assumption is a serious programming error.

## See Also

### Testing

- [assert(_:_:file:line:)](<assert(____file_line_).md>) — Performs a traditional C-style assert with an optional message.
- [precondition(_:_:file:line:)](<precondition(____file_line_).md>) — Checks a necessary condition for making forward progress.
- [preconditionFailure(_:file:line:)](<preconditionfailure(__file_line_).md>) — Indicates that a precondition was violated.
