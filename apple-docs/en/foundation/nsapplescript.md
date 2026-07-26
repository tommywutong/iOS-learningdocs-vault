---
title: NSAppleScript
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsapplescript
source_url: 'https://developer.apple.com/documentation/foundation/nsapplescript'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsapplescript.json'
content_hash: 'sha256:643279b8745f43ee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSAppleScript

<sub>Class</sub>

An object that provides the ability to load, compile, and execute scripts.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSAppleScript
```

## Overview

This class provides applications with the ability to

- load a script from a URL or from a text string
- compile or execute a script or an individual Apple event
- obtain an `NSAppleEventDescriptor` containing the reply from an executed script or event
- obtain an attributed string for a compiled script, suitable for display in a script editor
- obtain various kinds of information about any errors that may occur

> [!important] Important
> `NSAppleScript` provides the [- executeAppleEvent:error:](<nsapplescript/executeappleevent(__error_).md>) method so that you can send an Apple event to invoke a handler in a script. (In an AppleScript script, a handler is the equivalent of a function.) However, you cannot use this method to send Apple events to other applications.

When you create an instance of `NSAppleScript` object, you can use a URL to specify a script that can be in either text or compiled form, or you can supply the script as a string. Should an error occur when compiling or executing the script, several of the methods return a dictionary containing error information. The keys for obtaining error information, such as [NSAppleScriptErrorMessage](nsapplescript/errormessage.md), are described in the Constants section.

See also NSAppleScript Additions Reference in the Application Kit framework, which defines a method that returns the syntax-highlighted source code for a script.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing a Script

- [- initWithContentsOfURL:error:](<nsapplescript/init(contentsof_error_).md>) — Initializes a newly allocated script instance from the source identified by the passed URL.
- [- initWithSource:](<nsapplescript/init(source_).md>) — Initializes a newly allocated script instance from the passed source.

### Getting Information About a Script

- [compiled](nsapplescript/iscompiled.md) — A Boolean value that indicates whether the receiver’s script has been compiled.
- [source](nsapplescript/source.md) — The script source for the receiver.

### Compiling and Executing a Script

- [- compileAndReturnError:](<nsapplescript/compileandreturnerror(__).md>) — Compiles the receiver, if it is not already compiled.
- [- executeAndReturnError:](<nsapplescript/executeandreturnerror(__).md>) — Executes the receiver, compiling it first if it is not already compiled.
- [- executeAppleEvent:error:](<nsapplescript/executeappleevent(__error_).md>) — Executes an Apple event in the context of the receiver, as a means of allowing the application to invoke a handler in the script.

### Constants

- [Error Dictionary Keys](error-dictionary-keys.md) — If the result of [- initWithContentsOfURL:error:](<nsapplescript/init(contentsof_error_).md>), [- compileAndReturnError:](<nsapplescript/compileandreturnerror(__).md>), [- executeAndReturnError:](<nsapplescript/executeandreturnerror(__).md>), or [- executeAppleEvent:error:](<nsapplescript/executeappleevent(__error_).md>), signals failure (`nil`, [false](../swift/false.md), `nil`, or `nil`, respectively), a pointer to an autoreleased dictionary is put at the location pointed to by the error parameter. The error info dictionary may contain entries that use any combination of the following keys, including no entries at all.

### Instance Properties

- [richTextSource](nsapplescript/richtextsource.md) — Returns the syntax-highlighted source code of the receiver if the receiver has been compiled and its source code is available.

### Initializers

- [init(contentsOfURL:error:)](<nsapplescript/init(contentsofurl_error_).md>)
