---
title: NSCloneCommand
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsclonecommand
source_url: 'https://developer.apple.com/documentation/foundation/nsclonecommand'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsclonecommand.json'
content_hash: 'sha256:274990587e57bea1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCloneCommand

<sub>Class</sub>

A command that clones one or more scriptable objects.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSCloneCommand
```

## Overview

An instance of `NSCloneCommand` clones the specified scriptable object or objects (such as words, paragraphs, images, and so on) and inserts them in the specified location, or the default location if no location is specified. The cloned scriptable objects typically correspond to objects in the application, but aren’t required to. This command corresponds to AppleScript’s `duplicate` command.

`NSCloneCommand` is part of Cocoa’s built-in scripting support. It works automatically to support the `duplicate` command through key-value coding. Most applications don’t need to subclass `NSCloneCommand` or invoke its methods.

When an instance of `NSCloneCommand` is executed, it clones the specified objects by sending them [copyWithZone:](../objectivec/nsobject-swift.class/copywithzone_.md) messages.

## Relationships

- **Inherits From**: [NSScriptCommand](nsscriptcommand.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Working with specifiers

- [keySpecifier](nsclonecommand/keyspecifier.md) — Returns a specifier for the object or objects to be cloned.
- [- setReceiversSpecifier:](<nsclonecommand/setreceiversspecifier(__).md>) — Sets the receiver’s object specifier;.

## See Also

### Script Commands

- [NSScriptCommand](nsscriptcommand.md) — A self-contained scripting statement.
- [NSQuitCommand](nsquitcommand.md) — A command that quits the specified app.
- [NSSetCommand](nssetcommand.md) — A command that sets one or more attributes or relationships to one or more values.
- [NSMoveCommand](nsmovecommand.md) — A command that moves one or more scriptable objects.
- [NSCreateCommand](nscreatecommand.md) — A command that creates a scriptable object.
- [NSDeleteCommand](nsdeletecommand.md) — A command that deletes a scriptable object.
- [NSExistsCommand](nsexistscommand.md) — A command that determines whether a scriptable object exists.
- [NSGetCommand](nsgetcommand.md) — A command that retrieves a value or object from a scriptable object.
- [NSCountCommand](nscountcommand.md) — A command that counts the number of objects of a specified class in the specified object container.
- [NSCloseCommand](nsclosecommand.md) — A command that closes one or more scriptable objects.
