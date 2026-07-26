---
title: standardInput
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/process/standardinput
source_url: 'https://developer.apple.com/documentation/foundation/process/standardinput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/process/standardinput.json'
content_hash: 'sha256:938c5f634ff43d06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Process](../process.md)

# standardInput

<sub>Instance Property</sub>

The standard input for the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
var standardInput: Any? { get set }
```

## Parameters

- `file` — The standard input for the receiver, which can be either an [FileHandle](../filehandle.md) or an [Pipe](../pipe.md) object.

## Discussion

If `file` is an `NSPipe` object, launching the receiver automatically closes the read end of the pipe in the current task. Don’t create a handle for the pipe and pass that as the argument, or the read end of the pipe won’t be closed automatically.

If this method isn’t used, the standard input is inherited from the process that created the receiver. This method raises an `NSInvalidArgumentException` if the system has lauched the receiver.

## See Also

### Configuring a process

- [arguments](arguments.md) — The command arguments that the system uses to launch the executable.
- [currentDirectoryURL](currentdirectoryurl.md) — The current directory for the receiver.
- [environment](environment.md) — The environment for the receiver.
- [executableURL](executableurl.md) — The receiver’s executable.
- [qualityOfService](qualityofservice.md) — The default quality of service level the system applies to operations the task executes.
- [standardError](standarderror.md) — The standard error for the receiver.
- [standardOutput](standardoutput.md) — The standard output for the receiver.
