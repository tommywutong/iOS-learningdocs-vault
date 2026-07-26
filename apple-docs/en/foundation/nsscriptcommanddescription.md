---
title: NSScriptCommandDescription
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommanddescription
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommanddescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommanddescription.json'
content_hash: 'sha256:e250235848d3c669'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSScriptCommandDescription

<sub>Class</sub>

A script command that a macOS app supports.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSScriptCommandDescription
```

## Overview

A scriptable application provides scriptability information that describes the commands and objects scripters can use in scripts that target the application. An application’s scripting information is collected automatically by an instance of [NSScriptSuiteRegistry](nsscriptsuiteregistry.md), which creates an `NSScriptCommandDescription` for each command it finds, caches these objects in memory, and installs a command handler for each command.

A script command instance stores the name, class, argument types, and return type of a command. For example, commands in AppleScript’s Core suite include `clone`, `count`, `create`, `delete`, `exists`, and `move`.

The public methods of `NSScriptCommandDescription` are used primarily by Cocoa’s built-in scripting support in responding to Apple events that target the application. Although you can subclass the `NSScriptCommandDescription` class, it is unlikely that you would need to do so, or to create instances of it.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing a Script Command Description

- [- initWithSuiteName:commandName:dictionary:](<nsscriptcommanddescription/init(suitename_commandname_dictionary_).md>) — Initializes and returns a newly allocated instance of `NSScriptCommandDescription`.

### Getting Basic Information About the Command

- [appleEventClassCode](nsscriptcommanddescription/appleeventclasscode.md) — Returns the four-character code for the Apple event class of the receiver’s command.
- [appleEventCode](nsscriptcommanddescription/appleeventcode.md) — Returns the four-character code for the Apple event ID of the receiver’s command.
- [commandClassName](nsscriptcommanddescription/commandclassname.md) — Returns the name of the class that will be instantiated to handle the command.
- [commandName](nsscriptcommanddescription/commandname.md) — Returns the name of the command.
- [suiteName](nsscriptcommanddescription/suitename.md) — Returns the name of the suite that contains the command described by the receiver.

### Getting Command Argument Information

- [- appleEventCodeForArgumentWithName:](<nsscriptcommanddescription/appleeventcodeforargument(withname_).md>) — Returns the Apple event code for the specified command argument of the receiver.
- [argumentNames](nsscriptcommanddescription/argumentnames.md) — Returns the names (or keys) for all arguments of the receiver’s command.
- [- isOptionalArgumentWithName:](<nsscriptcommanddescription/isoptionalargument(withname_).md>) — Returns a Boolean value that indicates whether the command argument identified by the specified argument key is an optional argument.
- [- typeForArgumentWithName:](<nsscriptcommanddescription/typeforargument(withname_).md>) — Returns the type of the command argument identified by the specified key.

### Getting Command Return-Type Information

- [appleEventCodeForReturnType](nsscriptcommanddescription/appleeventcodeforreturntype.md) — Returns the Apple event code that identifies the command’s return type.
- [returnType](nsscriptcommanddescription/returntype.md) — Returns the return type of the command.

### Creating Commands

- [- createCommandInstance](<nsscriptcommanddescription/createcommandinstance().md>) — Creates and returns an instance of the command object described by the receiver.
- [- createCommandInstanceWithZone:](<nsscriptcommanddescription/createcommandinstance(with_).md>) — Creates and returns an instance of the command object described by the receiver in the specified memory zone.

### Initializers

- [- initWithCoder:](<nsscriptcommanddescription/init(coder_).md>)

## See Also

### Script Dictionary Description

- [NSScriptSuiteRegistry](nsscriptsuiteregistry.md) — The top-level repository of scriptability information for an app at runtime.
- [NSScriptClassDescription](nsscriptclassdescription.md) — A scriptable class that a macOS app supports.
- [NSClassDescription](nsclassdescription.md) — An abstract class that provides the interface for querying the relationships and properties of a class.
