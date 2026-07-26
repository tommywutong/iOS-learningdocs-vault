---
title: NSDeleteCommand
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdeletecommand
source_url: 'https://developer.apple.com/documentation/foundation/nsdeletecommand'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdeletecommand.json'
content_hash: 'sha256:398f4e217021bd93'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDeleteCommand

<sub>Class</sub>

A command that deletes a scriptable object.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSDeleteCommand
```

## Overview

An instance of `NSDeleteCommand` deletes the specified scriptable object or objects (such as words, paragraphs, and so on).

Suppose, for example, a user executes a script that sends the command `delete the third rectangle in the first document` to the Sketch sample application (located in `/Developer/Examples/AppKit`). Cocoa creates an `NSDeleteCommand` object to perform the operation. When the command is executed, it uses the key-value coding mechanism (by invoking `removeValueAtIndex:fromPropertyWithKey:`) to remove the specified object or objects from their container. See the description for [removeValue(at:fromPropertyWithKey:)](<../objectivec/nsobject-swift.class/removevalue(at_frompropertywithkey_).md>) for related information.

`NSDeleteCommand` is part of Cocoa’s built-in scripting support. Most applications don’t need to subclass `NSDeleteCommand` or call its methods.

## Relationships

- **Inherits From**: [NSScriptCommand](nsscriptcommand.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Working with specifiers

- [keySpecifier](nsdeletecommand/keyspecifier.md) — Returns a specifier for the object or objects to be deleted.
- [- setReceiversSpecifier:](<nsdeletecommand/setreceiversspecifier(__).md>) — Sets the receiver’s object specifier.

## See Also

### Script Commands

- [NSScriptCommand](nsscriptcommand.md) — A self-contained scripting statement.
- [NSQuitCommand](nsquitcommand.md) — A command that quits the specified app.
- [NSSetCommand](nssetcommand.md) — A command that sets one or more attributes or relationships to one or more values.
- [NSMoveCommand](nsmovecommand.md) — A command that moves one or more scriptable objects.
- [NSCreateCommand](nscreatecommand.md) — A command that creates a scriptable object.
- [NSExistsCommand](nsexistscommand.md) — A command that determines whether a scriptable object exists.
- [NSGetCommand](nsgetcommand.md) — A command that retrieves a value or object from a scriptable object.
- [NSCloneCommand](nsclonecommand.md) — A command that clones one or more scriptable objects.
- [NSCountCommand](nscountcommand.md) — A command that counts the number of objects of a specified class in the specified object container.
- [NSCloseCommand](nsclosecommand.md) — A command that closes one or more scriptable objects.
