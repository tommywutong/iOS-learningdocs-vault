---
title: NSCloseCommand
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsclosecommand
source_url: 'https://developer.apple.com/documentation/foundation/nsclosecommand'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsclosecommand.json'
content_hash: 'sha256:4c74c9124452b196'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCloseCommand

<sub>Class</sub>

A command that closes one or more scriptable objects.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSCloseCommand
```

## Overview

An instance of `NSCloseCommand` closes the specified scriptable object or objects—typically a document or window (and its associated document, if any). The command may optionally specify a location to save in and how to handle modified documents (by automatically saving changes, not saving them, or asking the user).

`NSCloseCommand` is part of Cocoa’s built-in scripting support. It works automatically to support the `close` command through key-value coding. Most applications don’t need to subclass `NSCloseCommand` or call its methods.

## Relationships

- **Inherits From**: [NSScriptCommand](nsscriptcommand.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing save options

- [saveOptions](nsclosecommand/saveoptions.md) — Returns a constant indicating how to deal with closing any modified documents.

### Constants

- [NSSaveOptions](nssaveoptions.md) — The [saveOptions](nsclosecommand/saveoptions.md) method returns one of the following constants to indicate how to deal with saving any modified documents:

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
- [NSCloneCommand](nsclonecommand.md) — A command that clones one or more scriptable objects.
- [NSCountCommand](nscountcommand.md) — A command that counts the number of objects of a specified class in the specified object container.
