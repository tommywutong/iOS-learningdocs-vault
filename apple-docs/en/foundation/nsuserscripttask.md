---
title: NSUserScriptTask
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuserscripttask
source_url: 'https://developer.apple.com/documentation/foundation/nsuserscripttask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuserscripttask.json'
content_hash: 'sha256:00e5d66eb82dafb8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUserScriptTask

<sub>Class</sub>

An object that executes scripts.

<sub>macOS</sub>

```swift
class NSUserScriptTask
```

## Overview

The [NSUserScriptTask](nsuserscripttask.md) class is able to run all the scripts normally run by the one of its subclasses, however it ignores the results. It is intended to execute user-supplied scripts and will execute them outside of the application’s sandbox, if any.

If you need to execute scripts and get the input and output information use the [NSUserUnixTask](nsuserunixtask.md), [NSUserAppleScriptTask](nsuserapplescripttask.md), and [NSUserAutomatorTask](nsuserautomatortask.md) sub classes.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSUserAppleScriptTask](nsuserapplescripttask.md), [NSUserAutomatorTask](nsuserautomatortask.md), [NSUserUnixTask](nsuserunixtask.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Specifying the Script

- [- initWithURL:error:](<nsuserscripttask/init(url_)-2qgls.md>) — Return a user script task instance given a URL for a script file.
- [scriptURL](nsuserscripttask/scripturl.md) — The URL of the script file.

### Executing the User Script

- [- executeWithCompletionHandler:](<nsuserscripttask/execute(completionhandler_).md>) — Executes the script with no input and ignoring any result.

### Constants

- [CompletionHandler](nsuserscripttask/completionhandler.md) — Implement this block to retrieve the error of the script executed by [- executeWithCompletionHandler:](<nsuserscripttask/execute(completionhandler_).md>).

### Initializers

- [init(URL:)](<nsuserscripttask/init(url_)-3l6en.md>)

## See Also

### Scripts and External Tasks

- [Process](process.md) — An object that represents a subprocess of the current process.
- [NSUserAppleScriptTask](nsuserapplescripttask.md) — An object that executes AppleScript scripts.
- [NSUserAutomatorTask](nsuserautomatortask.md) — An object that executes Automator workflows.
- [NSUserUnixTask](nsuserunixtask.md) — An object that executes unix applications.
