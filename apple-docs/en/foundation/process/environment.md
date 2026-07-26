---
title: environment
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/process/environment
source_url: 'https://developer.apple.com/documentation/foundation/process/environment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/process/environment.json'
content_hash: 'sha256:56656a1677c0b573'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Process](../process.md)

# environment

<sub>Instance Property</sub>

The environment for the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
var environment: [String : String]? { get set }
```

## Parameters

- `environmentDictionary` — A dictionary of environment variable values whose keys are the variable names.

## Discussion

If this method isn’t used, the environment is inherited from the process that created the receiver. This method raises an `NSInvalidArgumentException` if the system has launched the receiver.

## See Also

### Configuring a process

- [arguments](arguments.md) — The command arguments that the system uses to launch the executable.
- [currentDirectoryURL](currentdirectoryurl.md) — The current directory for the receiver.
- [executableURL](executableurl.md) — The receiver’s executable.
- [qualityOfService](qualityofservice.md) — The default quality of service level the system applies to operations the task executes.
- [standardError](standarderror.md) — The standard error for the receiver.
- [standardInput](standardinput.md) — The standard input for the receiver.
- [standardOutput](standardoutput.md) — The standard output for the receiver.
