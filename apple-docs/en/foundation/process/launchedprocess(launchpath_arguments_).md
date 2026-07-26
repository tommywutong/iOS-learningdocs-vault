---
title: 'launchedProcess(launchPath:arguments:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.0+（27.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/process/launchedprocess(launchpath:arguments:)'
source_url: 'https://developer.apple.com/documentation/foundation/process/launchedprocess(launchpath:arguments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/process/launchedprocess%28launchpath%3Aarguments%3A%29.json'
content_hash: 'sha256:f24f9abae3ebe33a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Process](../process.md)

# launchedProcess(launchPath:arguments:)

<sub>Type Method</sub>

Creates and launches a task with a specified executable and arguments.

> [!warning] Deprecated
> Use [+ launchedTaskWithExecutableURL:arguments:error:terminationHandler:](<run(__arguments_terminationhandler_).md>) instead.

<sub>macOS</sub>

```swift
class func launchedProcess(launchPath path: String, arguments: [String]) -> Process
```

## Parameters

- `path` — The path to the executable.

- `arguments` — An array of `NSString` objects that supplies the arguments to the task. If `arguments` is `nil`, an `NSInvalidArgumentException` is raised.

## Return Value

An initialized `NSTask` object with the supplied `arguments`.

## Discussion

The task inherits its environment from the process that invokes this method.

The `NSTask` object converts both `path` and the strings in `arguments` to appropriate C-style strings (using [fileSystemRepresentation](../nsstring/filesystemrepresentation.md)) before passing them to the task via `argv[])` . The strings in `arguments` don’t undergo shell expansion, so you don’t need to do special quoting, and shell variables, such as `$PWD`, aren’t resolved.

## See Also

### Related Documentation

- [- init](<init().md>) — Returns an initialized process object with the environment of the current process.

### Deprecated

- [currentDirectoryPath](currentdirectorypath.md) — Sets the current directory for the receiver. _(deprecated)_
- [launchPath](launchpath.md) — Sets the receiver’s executable. _(deprecated)_
- [- launch](<launch().md>) — Launches the task represented by the receiver. _(deprecated)_
