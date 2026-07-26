---
title: NSMoveCommand
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmovecommand
source_url: 'https://developer.apple.com/documentation/foundation/nsmovecommand'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmovecommand.json'
content_hash: 'sha256:51795defcc41da1b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMoveCommand

<sub>Class</sub>

A command that moves one or more scriptable objects.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSMoveCommand
```

## Overview

An instance of `NSMoveCommand` moves the specified scriptable object or objects; for example, it may move words to a new location in a document or a file to a new directory.

`NSMoveCommand` is part of Cocoa’s built-in scripting support. It works automatically to support the `move` AppleScript command through key-value coding. Most applications don’t need to subclass `NSMoveCommand` or invoke its methods. However, for circumstances where you might choose to subclass this command, see “Modifying a Standard Command” in [Script Commands](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_script_cmds/SAppsScriptCmds.html#//apple_ref/doc/uid/20001242) in [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164).

When an instance of `NSMoveCommand` is executed, it does not make copies of moved objects. It removes objects from the source container or containers, then inserts them into the destination container.

## Relationships

- **Inherits From**: [NSScriptCommand](nsscriptcommand.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Working with specifiers

- [keySpecifier](nsmovecommand/keyspecifier.md) — Returns a specifier for the object or objects to be moved.
- [- setReceiversSpecifier:](<nsmovecommand/setreceiversspecifier(__).md>) — Sets the receiver’s object specifier.

## See Also

### Script Commands

- [NSScriptCommand](nsscriptcommand.md) — A self-contained scripting statement.
- [NSQuitCommand](nsquitcommand.md) — A command that quits the specified app.
- [NSSetCommand](nssetcommand.md) — A command that sets one or more attributes or relationships to one or more values.
- [NSCreateCommand](nscreatecommand.md) — A command that creates a scriptable object.
- [NSDeleteCommand](nsdeletecommand.md) — A command that deletes a scriptable object.
- [NSExistsCommand](nsexistscommand.md) — A command that determines whether a scriptable object exists.
- [NSGetCommand](nsgetcommand.md) — A command that retrieves a value or object from a scriptable object.
- [NSCloneCommand](nsclonecommand.md) — A command that clones one or more scriptable objects.
- [NSCountCommand](nscountcommand.md) — A command that counts the number of objects of a specified class in the specified object container.
- [NSCloseCommand](nsclosecommand.md) — A command that closes one or more scriptable objects.
