---
title: CommandLine
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/commandline
source_url: 'https://developer.apple.com/documentation/swift/commandline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/commandline.json'
content_hash: 'sha256:de6b58bd1c7e4783'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# CommandLine

<sub>Enumeration</sub>

Command-line arguments for the current process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum CommandLine
```

## Relationships

- **Conforms To**: [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Accessing Arguments

- [arguments](commandline/arguments.md) — An array that provides access to this program’s command line arguments.

### Accessing Raw Argument Data

- [argc](commandline/argc.md) — Access to the raw argc value from C.
- [unsafeArgv](commandline/unsafeargv.md) — Access to the raw argv value from C.

## See Also

### Command Line Input

- [readLine(strippingNewline:)](<readline(strippingnewline_).md>) — Returns a string read from standard input through the end of the current line or until EOF is reached.
