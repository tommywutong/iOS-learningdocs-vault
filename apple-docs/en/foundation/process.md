---
title: Process
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/process
source_url: 'https://developer.apple.com/documentation/foundation/process'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/process.json'
content_hash: 'sha256:fa773705ce564549'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Process

<sub>Class</sub>

An object that represents a subprocess of the current process.

<sub>Mac Catalyst, macOS</sub>

```swift
class Process
```

## Overview

Using this class, your program can run another program as a subprocess and monitor that program’s execution. Unlike [Thread](thread.md), it doesn’t share memory space with the process that creates it.

A process operates within an environment defined by the current values for several items: the current directory, standard input, standard output, standard error, and the values of any environment variables, inheriting its environment from the process that launches it. If there are any environment variables that should be different for the subprocess (for example, if the current directory needs to change), change it in the instance after initialization, before your app launches it. Your app can’t change a process’s environment while it’s running.

You can only run the subprocess once per instance. Subsequent attempts raise an error.

> [!important] Important
> In a sandboxed app, child processes you create with this class inherit the sandbox of the parent app. Instead, write helper apps as XPC Services because it allows you to specify different sandbox entitlements for helper apps. For more information, see [Daemons and Services Programming Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html#//apple_ref/doc/uid/10000172i) and [XPC](../xpc.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating and initializing a process

- [+ launchedTaskWithExecutableURL:arguments:error:terminationHandler:](<process/run(__arguments_terminationhandler_).md>) — Creates and runs a task with a specified executable and arguments.
- [- init](<process/init().md>) — Returns an initialized process object with the environment of the current process.

### Returning information

- [processIdentifier](process/processidentifier.md) — The receiver’s process identifier.

### Running and stopping

- [- launchAndReturnError:](<process/run().md>) — Runs the process with the current environment.
- [- interrupt](<process/interrupt().md>) — Sends an interrupt signal to the receiver and all of its subtasks.
- [- resume](<process/resume().md>) — Resumes execution of a suspended task.
- [- suspend](<process/suspend().md>) — Suspends execution of the receiver task.
- [- terminate](<process/terminate().md>) — Sends a terminate signal to the receiver and all of its subtasks.
- [- waitUntilExit](<process/waituntilexit().md>) — Blocks the process until the receiver is finished.

### Querying the process state

- [running](process/isrunning.md) — A status that indicates whether the receiver is still running.
- [terminationStatus](process/terminationstatus.md) — The exit status the receiver’s executable returns.
- [terminationReason](process/terminationreason-swift.property.md) — The reason the system terminated the task.

### Configuring a process

- [arguments](process/arguments.md) — The command arguments that the system uses to launch the executable.
- [currentDirectoryURL](process/currentdirectoryurl.md) — The current directory for the receiver.
- [environment](process/environment.md) — The environment for the receiver.
- [executableURL](process/executableurl.md) — The receiver’s executable.
- [qualityOfService](process/qualityofservice.md) — The default quality of service level the system applies to operations the task executes.
- [standardError](process/standarderror.md) — The standard error for the receiver.
- [standardInput](process/standardinput.md) — The standard input for the receiver.
- [standardOutput](process/standardoutput.md) — The standard output for the receiver.

### Working with termination handlers

- [terminationHandler](process/terminationhandler.md) — A completion block the system invokes when the task completes.

### Working with constants

- [TerminationReason](process/terminationreason-swift.enum.md) — Constants that specify the termination reason values that the system returns.
- [QualityOfService](qualityofservice.md) — Constants that indicate the nature and importance of work to the system.

### Working with notifications

- [NSTaskDidTerminateNotification](process/didterminatenotification.md) — Posted when the task has stopped execution.

### Working with notification messages

- [DidTerminateMessage](process/didterminatemessage.md) — A message the system sends when a task stops operation.

### Deprecated

- [+ launchedTaskWithLaunchPath:arguments:](<process/launchedprocess(launchpath_arguments_).md>) — Creates and launches a task with a specified executable and arguments. _(deprecated)_
- [currentDirectoryPath](process/currentdirectorypath.md) — Sets the current directory for the receiver. _(deprecated)_
- [launchPath](process/launchpath.md) — Sets the receiver’s executable. _(deprecated)_
- [- launch](<process/launch().md>) — Launches the task represented by the receiver. _(deprecated)_

### Instance Properties

- [launchRequirement](process/launchrequirement.md)
- [launchRequirementData](process/launchrequirementdata.md) — The launch requirement data for the receiver.

## See Also

### Scripts and External Tasks

- [NSUserScriptTask](nsuserscripttask.md) — An object that executes scripts.
- [NSUserAppleScriptTask](nsuserapplescripttask.md) — An object that executes AppleScript scripts.
- [NSUserAutomatorTask](nsuserautomatortask.md) — An object that executes Automator workflows.
- [NSUserUnixTask](nsuserunixtask.md) — An object that executes unix applications.
