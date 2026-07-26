---
title: NSUserUnixTask
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuserunixtask
source_url: 'https://developer.apple.com/documentation/foundation/nsuserunixtask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuserunixtask.json'
content_hash: 'sha256:0b0fbca2a0ec5a33'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUserUnixTask

<sub>Class</sub>

An object that executes unix applications.

<sub>macOS</sub>

```swift
class NSUserUnixTask
```

## Overview

The [NSUserUnixTask](nsuserunixtask.md) class is intended to run unix applications, typically a shell script, from your application. It is intended to execute user-supplied scripts, and will execute them outside of the application’s sandbox, if any.

The class is not intended to execute scripts built into an application; for that, use one of the [Process](process.md), [NSAppleScript](nsapplescript.md), or [AMWorkflow](../automator/amworkflow.md) classes.  If the application is sandboxed, then the script must be in the [NSApplicationScriptsDirectory](filemanager/searchpathdirectory/applicationscriptsdirectory.md) folder.  A sandboxed application may read from, but not write to, this folder.

If you simply need to execute unix scripts without regard to input or output, use [NSUserScriptTask](nsuserscripttask.md), which can execute any of the specific types.  If you need specific control over the input to, or output from, or the error stream of the script, use this class.

## Relationships

- **Inherits From**: [NSUserScriptTask](nsuserscripttask.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Executing the Unix Script

- [- executeWithArguments:completionHandler:](<nsuserunixtask/execute(witharguments_completionhandler_).md>) — Execute the unix script with the specified arguments.

### Standard Unix Streams

- [standardError](nsuserunixtask/standarderror.md) — The standard error stream.
- [standardInput](nsuserunixtask/standardinput.md) — The standard input stream.
- [standardOutput](nsuserunixtask/standardoutput.md) — The standard output stream.

### Constants

- [CompletionHandler](nsuserunixtask/completionhandler.md) — Implement this block to retrieve an error from the Unix scripted executed by [- executeWithArguments:completionHandler:](<nsuserunixtask/execute(witharguments_completionhandler_).md>).

## See Also

### Scripts and External Tasks

- [Process](process.md) — An object that represents a subprocess of the current process.
- [NSUserScriptTask](nsuserscripttask.md) — An object that executes scripts.
- [NSUserAppleScriptTask](nsuserapplescripttask.md) — An object that executes AppleScript scripts.
- [NSUserAutomatorTask](nsuserautomatortask.md) — An object that executes Automator workflows.
