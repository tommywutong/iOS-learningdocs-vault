---
title: currentDirectoryPath
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+（27.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/process/currentdirectorypath
source_url: 'https://developer.apple.com/documentation/foundation/process/currentdirectorypath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/process/currentdirectorypath.json'
content_hash: 'sha256:4ac1fe109a94c53c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Process](../process.md)

# currentDirectoryPath

<sub>Instance Property</sub>

Sets the current directory for the receiver.

> [!warning] Deprecated
> Use [currentDirectoryURL](currentdirectoryurl.md) instead.

<sub>macOS</sub>

```swift
var currentDirectoryPath: String { get set }
```

## Parameters

- `path` — The current directory for the task.

## Discussion

If this method isn’t used, the current directory is inherited from the process that created the receiver. This method raises an `NSInvalidArgumentException` if the receiver has already been launched.

## See Also

### Deprecated

- [+ launchedTaskWithLaunchPath:arguments:](<launchedprocess(launchpath_arguments_).md>) — Creates and launches a task with a specified executable and arguments. _(deprecated)_
- [launchPath](launchpath.md) — Sets the receiver’s executable. _(deprecated)_
- [- launch](<launch().md>) — Launches the task represented by the receiver. _(deprecated)_
