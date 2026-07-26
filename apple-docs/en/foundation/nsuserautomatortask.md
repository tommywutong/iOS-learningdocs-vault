---
title: NSUserAutomatorTask
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuserautomatortask
source_url: 'https://developer.apple.com/documentation/foundation/nsuserautomatortask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuserautomatortask.json'
content_hash: 'sha256:41a2a60a50dc52bf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUserAutomatorTask

<sub>Class</sub>

An object that executes Automator workflows.

<sub>macOS</sub>

```swift
class NSUserAutomatorTask
```

## Overview

The [NSUserAutomatorTask](nsuserautomatortask.md) class is intended to run Automator workflows from your application. It is intended to execute user-supplied workflows, and will execute them outside of the application’s sandbox, if any.

The class is not intended to execute scripts built into an application; for that, use one of the [Process](process.md) or [AMWorkflow](../automator/amworkflow.md) classes.  If the application is sandboxed, then the script must be in the [NSApplicationScriptsDirectory](filemanager/searchpathdirectory/applicationscriptsdirectory.md) folder.  A sandboxed application may read from, but not write to, this folder.

If you simply need to execute scripts without regard to input or output, use [NSUserScriptTask](nsuserscripttask.md), which can execute any of the specific types.  If you need specific control over the input to or output from the workflow, use this class.

## Relationships

- **Inherits From**: [NSUserScriptTask](nsuserscripttask.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Executing Automator Tasks

- [- executeWithInput:completionHandler:](<nsuserautomatortask/execute(withinput_completionhandler_).md>) — Execute the Automator workflow by providing it as securely coded input.
- [variables](nsuserautomatortask/variables.md) — The variables required by the Automator workflow.

### Constants

- [CompletionHandler](nsuserautomatortask/completionhandler.md) — Implement this block to retrieve the output of the Automator workflow executed by [- executeWithInput:completionHandler:](<nsuserautomatortask/execute(withinput_completionhandler_).md>).

## See Also

### Scripts and External Tasks

- [Process](process.md) — An object that represents a subprocess of the current process.
- [NSUserScriptTask](nsuserscripttask.md) — An object that executes scripts.
- [NSUserAppleScriptTask](nsuserapplescripttask.md) — An object that executes AppleScript scripts.
- [NSUserUnixTask](nsuserunixtask.md) — An object that executes unix applications.
