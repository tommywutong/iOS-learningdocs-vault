---
title: 'precondition(_:_:file:line:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/precondition(_:_:file:line:)'
source_url: 'https://developer.apple.com/documentation/swift/precondition(_:_:file:line:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/precondition%28_%3A_%3Afile%3Aline%3A%29.json'
content_hash: 'sha256:523feaa38f246ad8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# precondition(_:_:file:line:)

<sub>Function</sub>

Checks a necessary condition for making forward progress.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func precondition(_ condition: @autoclosure () -> Bool, _ message: @autoclosure () -> String = String(), file: StaticString = #file, line: UInt = #line)
```

## Parameters

- `condition` — The condition to test. `condition` is not evaluated in `-Ounchecked` builds.

- `message` — A string to print if `condition` is evaluated to `false` in a playground or `-Onone` build. The default is an empty string.

- `file` — The file name to print with `message` if the precondition fails. The default is the file where `precondition(_:_:file:line:)` is called.

- `line` — The line number to print along with `message` if the assertion fails. The default is the line number where `precondition(_:_:file:line:)` is called.

## Discussion

Use this function to detect conditions that must prevent the program from proceeding, even in shipping code.

- In playgrounds and `-Onone` builds (the default for Xcode’s Debug configuration): If `condition` evaluates to `false`, stop program execution in a debuggable state after printing `message`.
- In `-O` builds (the default for Xcode’s Release configuration): If `condition` evaluates to `false`, stop program execution.
- In `-Ounchecked` builds, `condition` is not evaluated, but the optimizer may assume that it _always_ evaluates to `true`. Failure to satisfy that assumption is a serious programming error.

## See Also

### Testing

- [assert(_:_:file:line:)](<assert(____file_line_).md>) — Performs a traditional C-style assert with an optional message.
- [assertionFailure(_:file:line:)](<assertionfailure(__file_line_).md>) — Indicates that an internal consistency check failed.
- [preconditionFailure(_:file:line:)](<preconditionfailure(__file_line_).md>) — Indicates that a precondition was violated.
