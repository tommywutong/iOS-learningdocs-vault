---
title: NSQuitCommand
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsquitcommand
source_url: 'https://developer.apple.com/documentation/foundation/nsquitcommand'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsquitcommand.json'
content_hash: 'sha256:dae0a2114c81c972'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSQuitCommand

<sub>Class</sub>

A command that quits the specified app.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSQuitCommand
```

## Overview

The quit command may optionally specify how to handle modified documents (automatically save changes, don’t save them, or ask the user). For details, see the description for the `quit` command in “Apple Events Sent By the Mac OS” in [How Cocoa Applications Handle Apple Events](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_handle_AEs/SAppsHandleAEs.html#//apple_ref/doc/uid/20001239) in [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164).

`NSQuitCommand` is part of Cocoa’s built-in scripting support. Most applications don’t need to subclass `NSQuitCommand` or call its methods.

## Relationships

- **Inherits From**: [NSScriptCommand](nsscriptcommand.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing options

- [saveOptions](nsquitcommand/saveoptions.md) — Returns a constant indicating how to deal with closing any modified documents.

## See Also

### Script Commands

- [NSScriptCommand](nsscriptcommand.md) — A self-contained scripting statement.
- [NSSetCommand](nssetcommand.md) — A command that sets one or more attributes or relationships to one or more values.
- [NSMoveCommand](nsmovecommand.md) — A command that moves one or more scriptable objects.
- [NSCreateCommand](nscreatecommand.md) — A command that creates a scriptable object.
- [NSDeleteCommand](nsdeletecommand.md) — A command that deletes a scriptable object.
- [NSExistsCommand](nsexistscommand.md) — A command that determines whether a scriptable object exists.
- [NSGetCommand](nsgetcommand.md) — A command that retrieves a value or object from a scriptable object.
- [NSCloneCommand](nsclonecommand.md) — A command that clones one or more scriptable objects.
- [NSCountCommand](nscountcommand.md) — A command that counts the number of objects of a specified class in the specified object container.
- [NSCloseCommand](nsclosecommand.md) — A command that closes one or more scriptable objects.
