---
title: arguments
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/process/arguments
source_url: 'https://developer.apple.com/documentation/foundation/process/arguments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/process/arguments.json'
content_hash: 'sha256:a95561f968b553ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Process](../process.md)

# arguments

<sub>Instance Property</sub>

The command arguments that the system uses to launch the executable.

<sub>Mac Catalyst, macOS</sub>

```swift
var arguments: [String]? { get set }
```

## Parameters

- `arguments` — An array of `NSString` objects that supplies the arguments to the task. If `arguments` is `nil`, the system raises an `NSInvalidArgumentException`.

## Discussion

The `NSTask` object converts both `path` and the strings in `arguments` to appropriate C-style strings (using [fileSystemRepresentation](../nsstring/filesystemrepresentation.md)) before passing them to the task through `argv[]`. The strings in `arguments` don’t undergo shell expansion, so you don’t need to do special quoting, and shell variables, such as `$PWD`, aren’t resolved.

## See Also

### Configuring a process

- [currentDirectoryURL](currentdirectoryurl.md) — The current directory for the receiver.
- [environment](environment.md) — The environment for the receiver.
- [executableURL](executableurl.md) — The receiver’s executable.
- [qualityOfService](qualityofservice.md) — The default quality of service level the system applies to operations the task executes.
- [standardError](standarderror.md) — The standard error for the receiver.
- [standardInput](standardinput.md) — The standard input for the receiver.
- [standardOutput](standardoutput.md) — The standard output for the receiver.
