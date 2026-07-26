---
title: NSCreateCommand
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscreatecommand
source_url: 'https://developer.apple.com/documentation/foundation/nscreatecommand'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscreatecommand.json'
content_hash: 'sha256:f655f01be715ca95'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCreateCommand

<sub>Class</sub>

A command that creates a scriptable object.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSCreateCommand
```

## Overview

An instance of `NSCreateCommand` creates the specified scriptable object (such as a document), optionally supplying the new object with the specified attributes. This command corresponds to AppleScript’s `make` command.

`NSCreateCommand` is part of Cocoa’s built-in scripting support. Most applications don’t need to subclass `NSCreateCommand` or invoke its methods.

When an instance of `NSCreateCommand` is executed, it creates a new object using `[[theClassToBeCreated allocWithZone:NULL] init]` (where `theClassToBeCreated` is the class of the object to be created), unless the command has a `with data` argument. In the latter case, the new object is created by invoking `[[NSScriptCoercionHandler sharedCoercionHandler] coerceValue:theDataAsAnObject toClass:theClassToBeCreated]`.  Any properties specified by a `with properties` argument are then set in the new object using `-setScriptingProperties:`.

If an `NSCreateCommand` object with no argument corresponding to the `at` parameter is executed (for example, `tell application "Mail" to make new mailbox with properties {name:"testFolder"}`), and the receiver of the command (not necessarily the application object) has a to-many relationship to objects of the class to be instantiated, and the class description for the receiving class returns [false](../swift/false.md) when sent an `isLocationRequiredToCreateForKey:` message, the `NSCreateCommand` object creates a new object and sends the receiver an [insertValue(_:at:inPropertyWithKey:)](<../objectivec/nsobject-swift.class/insertvalue(__at_inpropertywithkey_).md>) message to place the new object in the container. This is part of Cocoa’s scripting support for inserting newly-created objects into containers without explicitly specifying a location.

## Relationships

- **Inherits From**: [NSScriptCommand](nsscriptcommand.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting information about a create command

- [createClassDescription](nscreatecommand/createclassdescription.md) — Returns the class description for the class that is to be created.
- [resolvedKeyDictionary](nscreatecommand/resolvedkeydictionary.md) — Returns a dictionary that contains the properties that were specified in the `make` Apple event command that has been converted to this `NSCreateCommand` object.

## See Also

### Script Commands

- [NSScriptCommand](nsscriptcommand.md) — A self-contained scripting statement.
- [NSQuitCommand](nsquitcommand.md) — A command that quits the specified app.
- [NSSetCommand](nssetcommand.md) — A command that sets one or more attributes or relationships to one or more values.
- [NSMoveCommand](nsmovecommand.md) — A command that moves one or more scriptable objects.
- [NSDeleteCommand](nsdeletecommand.md) — A command that deletes a scriptable object.
- [NSExistsCommand](nsexistscommand.md) — A command that determines whether a scriptable object exists.
- [NSGetCommand](nsgetcommand.md) — A command that retrieves a value or object from a scriptable object.
- [NSCloneCommand](nsclonecommand.md) — A command that clones one or more scriptable objects.
- [NSCountCommand](nscountcommand.md) — A command that counts the number of objects of a specified class in the specified object container.
- [NSCloseCommand](nsclosecommand.md) — A command that closes one or more scriptable objects.
