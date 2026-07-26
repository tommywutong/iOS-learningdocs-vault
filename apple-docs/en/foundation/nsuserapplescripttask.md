---
title: NSUserAppleScriptTask
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuserapplescripttask
source_url: 'https://developer.apple.com/documentation/foundation/nsuserapplescripttask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuserapplescripttask.json'
content_hash: 'sha256:156ce7a09f4e4d21'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUserAppleScriptTask

<sub>Class</sub>

An object that executes AppleScript scripts.

<sub>macOS</sub>

```swift
class NSUserAppleScriptTask
```

## Overview

The [NSUserAppleScriptTask](nsuserapplescripttask.md) class is intended to run AppleScript scripts from your application. It is intended to execute user-supplied scripts and will execute them outside of the application’s sandbox, if any.

The class is not intended to execute scripts built into an application; for that, use one of the [Process](process.md) classes. If the application is sandboxed, then the script must be in the [NSApplicationScriptsDirectory](filemanager/searchpathdirectory/applicationscriptsdirectory.md) folder. A sandboxed application may read from, but not write to, this folder.

If you simply need to execute scripts without regard to input or output, use [NSUserScriptTask](nsuserscripttask.md), which can execute any of the specific types. If you need specific control over the input to or output from the script, use this class.

## Relationships

- **Inherits From**: [NSUserScriptTask](nsuserscripttask.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Executing an AppleScript Script

- [- executeWithAppleEvent:completionHandler:](<nsuserapplescripttask/execute(withappleevent_completionhandler_).md>) — Execute the AppleScript script by sending it the specified Apple event.

### Constants

- [CompletionHandler](nsuserapplescripttask/completionhandler.md) — Implement this block to retrieve the result of the AppleScript executed by [- executeWithAppleEvent:completionHandler:](<nsuserapplescripttask/execute(withappleevent_completionhandler_).md>).

## See Also

### Scripts and External Tasks

- [Process](process.md) — An object that represents a subprocess of the current process.
- [NSUserScriptTask](nsuserscripttask.md) — An object that executes scripts.
- [NSUserAutomatorTask](nsuserautomatortask.md) — An object that executes Automator workflows.
- [NSUserUnixTask](nsuserunixtask.md) — An object that executes unix applications.
