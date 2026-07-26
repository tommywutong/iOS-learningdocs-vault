---
title: NSGetCommand
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsgetcommand
source_url: 'https://developer.apple.com/documentation/foundation/nsgetcommand'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsgetcommand.json'
content_hash: 'sha256:e8fa4a7b28273f17'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSGetCommand

<sub>Class</sub>

A command that retrieves a value or object from a scriptable object.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSGetCommand
```

## Overview

An instance of `NSGetCommand` gets the specified value or object from the specified scriptable object: for example, the words from a paragraph or the name of a document.

When an instance of `NSGetCommand` is executed, it evaluates the specified receivers, gathers the specified data, if any, and packages it in a return Apple event.

`NSGetCommand` is part of Cocoa’s built-in scripting support. It works automatically to support the `get` command through key-value coding. Most applications don’t need to subclass `NSGetCommand` or call its methods.

For information on working with `get` commands, see [Getting and Setting Properties and Elements](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_get_set/SAppsGetSet.html#//apple_ref/doc/uid/TP40002164-CH18) in [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164).

## Relationships

- **Inherits From**: [NSScriptCommand](nsscriptcommand.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

### Script Commands

- [NSScriptCommand](nsscriptcommand.md) — A self-contained scripting statement.
- [NSQuitCommand](nsquitcommand.md) — A command that quits the specified app.
- [NSSetCommand](nssetcommand.md) — A command that sets one or more attributes or relationships to one or more values.
- [NSMoveCommand](nsmovecommand.md) — A command that moves one or more scriptable objects.
- [NSCreateCommand](nscreatecommand.md) — A command that creates a scriptable object.
- [NSDeleteCommand](nsdeletecommand.md) — A command that deletes a scriptable object.
- [NSExistsCommand](nsexistscommand.md) — A command that determines whether a scriptable object exists.
- [NSCloneCommand](nsclonecommand.md) — A command that clones one or more scriptable objects.
- [NSCountCommand](nscountcommand.md) — A command that counts the number of objects of a specified class in the specified object container.
- [NSCloseCommand](nsclosecommand.md) — A command that closes one or more scriptable objects.
