---
title: init()
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/process/init()
source_url: 'https://developer.apple.com/documentation/foundation/process/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/process/init%28%29.json'
content_hash: 'sha256:49d5f166a9a01fa4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Process](../process.md)

# init()

<sub>Initializer</sub>

Returns an initialized process object with the environment of the current process.

<sub>Mac Catalyst, macOS</sub>

```swift
init()
```

## Return Value

An initialized process object with the environment of the current process.

## Discussion

If you need to modify the environment of a process, use alloc and init, and then set up the environment before launching the new process. Otherwise, just use the class method [+ launchedTaskWithExecutableURL:arguments:error:terminationHandler:](<run(__arguments_terminationhandler_).md>) to create and run the process.

## See Also

### Creating and initializing a process

- [+ launchedTaskWithExecutableURL:arguments:error:terminationHandler:](<run(__arguments_terminationhandler_).md>) — Creates and runs a task with a specified executable and arguments.
