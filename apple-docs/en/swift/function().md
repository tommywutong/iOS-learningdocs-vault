---
title: function()
framework: Swift
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/function()
source_url: 'https://developer.apple.com/documentation/swift/function()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/function%28%29.json'
content_hash: 'sha256:8b5e59ca96a06503'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# function()

<sub>Macro</sub>

Produces the name of the declaration in which it appears.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@freestanding(expression) macro function<T>() -> T where T : ExpressibleByStringLiteral
```

## Overview

Inside a function, the value `#function` produces is the name of that function, inside a method it’s the name of that method, inside a property getter or setter it’s the name of that property, inside special members like `init` or `subscript` it’s the name of that keyword, and at the top level of a file it’s the name of the current module.

When used as the default value of a function or method parameter, this macro’s value is determined when the default value expression is evaluated at the call site. For example:

```swift
func logFunctionName(string: String = #function) {
    print(string)
}
func myFunction() {
    logFunctionName() // Prints "myFunction()".
}
```

## See Also

### Getting Source Location Information

- [file()](<file().md>) — Produces the path to the file in which it appears.
- [fileID()](<fileid().md>) — Produces a unique identifier for the source file in which the macro appears.
- [filePath()](<filepath().md>) — Produces the complete path to the file in which the macro appears.
- [line()](<line().md>) — Produces the line number on which it appears.
- [column()](<column().md>) — Produces the column number in which the macro begins.
