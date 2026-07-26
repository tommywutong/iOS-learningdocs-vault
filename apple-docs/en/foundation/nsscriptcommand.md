---
title: NSScriptCommand
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommand
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommand'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommand.json'
content_hash: 'sha256:59c7c2c22b16e996'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSScriptCommand

<sub>Class</sub>

A self-contained scripting statement.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSScriptCommand
```

## Overview

An instance of [NSScriptCommand](nsscriptcommand.md) represents a scripting statement, such as `set word 5 of the front document to word 1 of the second document`, and contains the information needed to perform the operation specified by the statement.

When an Apple event reaches a Cocoa application, Cocoa’s built-in scripting support transforms it into a script command (that is, an instance of `NSScriptCommand` or one of the subclasses provided by Cocoa scripting or by your application) and executes the command in the context of the application. Executing a command means either invoking the selector associated with the command on the object or objects designated to receive the command, or having the command perform its default implementation method ([- performDefaultImplementation](<nsscriptcommand/performdefaultimplementation().md>)).

Your application most likely calls methods of `NSScriptCommand` to extract the command arguments. You do this either in the `performDefaultImplementation` method of a command subclass you have created, or in an object method designated as the selector to handle a particular command.

As part of Cocoa’s standard scripting implementation, `NSScriptCommand` and its subclasses can handle the default command set for AppleScript’s Standard suite for most applications without any subclassing. The Standard suite includes commands such as `copy`, `count`, `create`, `delete`, `exists`, and `move`, as well as common object classes such as `application`, `document`, and `window`.

For more information on working with script commands, see [Script Commands](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_script_cmds/SAppsScriptCmds.html#//apple_ref/doc/uid/20001242) in [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSCloneCommand](nsclonecommand.md), [NSCloseCommand](nsclosecommand.md), [NSCountCommand](nscountcommand.md), [NSCreateCommand](nscreatecommand.md), [NSDeleteCommand](nsdeletecommand.md), [NSExistsCommand](nsexistscommand.md), [NSGetCommand](nsgetcommand.md), [NSMoveCommand](nsmovecommand.md), [NSQuitCommand](nsquitcommand.md), [NSSetCommand](nssetcommand.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing a script command

- [- initWithCommandDescription:](<nsscriptcommand/init(commanddescription_).md>) — Returns an a script command object initialized from the passed command description.

### Getting the current command

- [+ currentCommand](<nsscriptcommand/current().md>) — If a command is being executed in the current thread by Cocoa scripting’s built-in Apple event handling, return the command.

### Getting the Apple event

- [appleEvent](nsscriptcommand/appleevent.md) — If the receiver was constructed by Cocoa scripting’s built-in Apple event handling, returns the Apple event descriptor from which it was constructed.

### Executing the command

- [- executeCommand](<nsscriptcommand/execute().md>) — Executes the command if it is valid and returns the result, if any.
- [- performDefaultImplementation](<nsscriptcommand/performdefaultimplementation().md>) — Overridden by subclasses to provide a default implementation for the command represented by the receiver.

### Accessing receivers

- [evaluatedReceivers](nsscriptcommand/evaluatedreceivers.md) — Returns the object or objects to which the command is to be sent (called both the “receivers” or “targets” of script commands).
- [receiversSpecifier](nsscriptcommand/receiversspecifier.md) — Sets the object specifier to `receiversSpec` that, when evaluated, indicates the receiver or receivers of the command.

### Accessing arguments

- [arguments](nsscriptcommand/arguments.md) — Sets the arguments of the command to `args`.
- [evaluatedArguments](nsscriptcommand/evaluatedarguments.md) — Returns a dictionary containing the arguments of the command, evaluated from object specifiers to objects if necessary. The keys in the dictionary are the argument names.

### Accessing the direct parameter

- [directParameter](nsscriptcommand/directparameter.md) — Sets the object that corresponds to the direct parameter of the Apple event from which the receiver derives.

### Getting command information

- [commandDescription](nsscriptcommand/commanddescription.md) — Returns the command description for the command.
- [wellFormed](nsscriptcommand/iswellformed.md) — Returns a Boolean value indicating whether the receiver is well formed according to its command description.

### Handling script execution errors

- [scriptErrorExpectedTypeDescriptor](nsscriptcommand/scripterrorexpectedtypedescriptor.md) — Sets a descriptor for the expected type that will be put in the reply Apple event if the sender requested a reply, execution of the receiver completes, and an error number was set.
- [scriptErrorNumber](nsscriptcommand/scripterrornumber.md) — Sets a script error number that is associated with the execution of the command and is returned in the reply Apple event, if a reply was requested by the sender.
- [scriptErrorOffendingObjectDescriptor](nsscriptcommand/scripterroroffendingobjectdescriptor.md) — Sets a descriptor for an object that will be put in the reply Apple event if the sender requested a reply, execution of the receiver completes, and an error number was set.
- [scriptErrorString](nsscriptcommand/scripterrorstring.md) — Sets a script error string that is associated with execution of the command.

### Suspending and resuming commands

- [- suspendExecution](<nsscriptcommand/suspendexecution().md>) — Suspends the execution of the receiver.
- [- resumeExecutionWithResult:](<nsscriptcommand/resumeexecution(withresult_).md>) — If a successful, unmatched, invocation of [- suspendExecution](<nsscriptcommand/suspendexecution().md>) has been made, resume the execution of the command.

### Constants

- [NSScriptCommand—General Command Execution Errors](general-command-execution-errors.md) — `NSScriptCommand` uses the following error codes for general command execution problems:

### Initializers

- [- initWithCoder:](<nsscriptcommand/init(coder_).md>)

## See Also

### Script Commands

- [NSQuitCommand](nsquitcommand.md) — A command that quits the specified app.
- [NSSetCommand](nssetcommand.md) — A command that sets one or more attributes or relationships to one or more values.
- [NSMoveCommand](nsmovecommand.md) — A command that moves one or more scriptable objects.
- [NSCreateCommand](nscreatecommand.md) — A command that creates a scriptable object.
- [NSDeleteCommand](nsdeletecommand.md) — A command that deletes a scriptable object.
- [NSExistsCommand](nsexistscommand.md) — A command that determines whether a scriptable object exists.
- [NSGetCommand](nsgetcommand.md) — A command that retrieves a value or object from a scriptable object.
- [NSCloneCommand](nsclonecommand.md) — A command that clones one or more scriptable objects.
- [NSCountCommand](nscountcommand.md) — A command that counts the number of objects of a specified class in the specified object container.
- [NSCloseCommand](nsclosecommand.md) — A command that closes one or more scriptable objects.
