---
title: NSSetCommand
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nssetcommand
source_url: 'https://developer.apple.com/documentation/foundation/nssetcommand'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssetcommand.json'
content_hash: 'sha256:1a85aaea6a552b26'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSSetCommand

<sub>Class</sub>

A command that sets one or more attributes or relationships to one or more values.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSSetCommand
```

## Overview

An instance of `NSSetCommand` sets one or more attributes or relationships to one or more values; for example, it may set the (x, y) coordinates for a window’s position or set the name of a document.

`NSSetCommand` is part of Cocoa’s built-in scripting support. It works automatically to support the `set` command through key-value coding. Most applications don’t need to subclass `NSSetCommand` or call its methods.

`NSSetCommand` uses available scripting class descriptions to determine whether it should set a value for an attribute (or property), or set a value for all elements (to-many objects). For the latter, it invokes [replaceValue(at:inPropertyWithKey:withValue:)](<../objectivec/nsobject-swift.class/replacevalue(at_inpropertywithkey_withvalue_).md>); for the former, it invokes [setValue(_:forKey:)](<../objectivec/nsobject-swift.class/setvalue(__forkey_).md>) (or, if the receiver overrides [takeValue(_:forKey:)](<../objectivec/nsobject-swift.class/takevalue(__forkey_).md>), it invokes that method, to support backward binary compatibility.)

For information on working with `set` commands, see [Getting and Setting Properties and Elements](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_get_set/SAppsGetSet.html#//apple_ref/doc/uid/TP40002164-CH18) in [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164).

## Relationships

- **Inherits From**: [NSScriptCommand](nsscriptcommand.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Working with specifiers

- [keySpecifier](nssetcommand/keyspecifier.md) — Returns a specifier that identifies the attribute or relationship that is to be set for the receiver of the `set` AppleScript command.
- [- setReceiversSpecifier:](<nssetcommand/setreceiversspecifier(__).md>) — Sets the receiver’s object specifier.

## See Also

### Script Commands

- [NSScriptCommand](nsscriptcommand.md) — A self-contained scripting statement.
- [NSQuitCommand](nsquitcommand.md) — A command that quits the specified app.
- [NSMoveCommand](nsmovecommand.md) — A command that moves one or more scriptable objects.
- [NSCreateCommand](nscreatecommand.md) — A command that creates a scriptable object.
- [NSDeleteCommand](nsdeletecommand.md) — A command that deletes a scriptable object.
- [NSExistsCommand](nsexistscommand.md) — A command that determines whether a scriptable object exists.
- [NSGetCommand](nsgetcommand.md) — A command that retrieves a value or object from a scriptable object.
- [NSCloneCommand](nsclonecommand.md) — A command that clones one or more scriptable objects.
- [NSCountCommand](nscountcommand.md) — A command that counts the number of objects of a specified class in the specified object container.
- [NSCloseCommand](nsclosecommand.md) — A command that closes one or more scriptable objects.
