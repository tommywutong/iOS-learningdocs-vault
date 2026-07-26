---
title: launchPath
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+（27.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/process/launchpath
source_url: 'https://developer.apple.com/documentation/foundation/process/launchpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/process/launchpath.json'
content_hash: 'sha256:80fe09888f201a65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Process](../process.md)

# launchPath

<sub>Instance Property</sub>

Sets the receiver’s executable.

> [!warning] Deprecated
> Use [executableURL](executableurl.md) instead.

<sub>macOS</sub>

```swift
var launchPath: String? { get set }
```

## Parameters

- `path` — The path to the executable.

## See Also

### Deprecated

- [+ launchedTaskWithLaunchPath:arguments:](<launchedprocess(launchpath_arguments_).md>) — Creates and launches a task with a specified executable and arguments. _(deprecated)_
- [currentDirectoryPath](currentdirectorypath.md) — Sets the current directory for the receiver. _(deprecated)_
- [- launch](<launch().md>) — Launches the task represented by the receiver. _(deprecated)_
