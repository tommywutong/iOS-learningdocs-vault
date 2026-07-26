---
title: UndoManager
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager
source_url: 'https://developer.apple.com/documentation/foundation/undomanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager.json'
content_hash: 'sha256:3cec814407cce483'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UndoManager

<sub>Class</sub>

A general-purpose recorder of operations that enables undo and redo.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor class UndoManager
```

## Overview

You register an undo operation by calling one of the methods described in Registering undo operations. You specify the name of the object that’s changing (or the owner of that object) and provide a closure, method, or invocation to revert its state.

After you register an undo operation, you can call [- undo](<undomanager/undo().md>) on the undo manager to revert to the state of the last undo operation. When undoing an action, [UndoManager](undomanager.md) saves the operations you revert to so that you can call [- redo](<undomanager/redo().md>) automatically.

Typically, apps with UI interactions work with [UndoManager](undomanager.md). For example, UIKit implements undo and redo in its text view object, making it easy for you to undo and redo actions in objects along the responder chain. [UndoManager](undomanager.md) also serves as a general-purpose state manager, which you can use to undo and redo many kinds of actions. For example, an interactive command-line utility can use this class to undo the last command run, or a networking library can undo a request by sending another request that invalidates the previous one.

> [!important] Important
> `UndoManager` is [MainActor](../swift/mainactor.md)-isolated in Swift, making it safe to use in UI frameworks like [AppKit](../appkit.md) and [UIKit](../uikit.md) that expect to execute code on the main thread, queue, or actor. When registering an undoable action with [registerUndo(withTarget:handler:)](<undomanager/registerundo(withtarget_handler_).md>), the `handler` closure is also [MainActor](../swift/mainactor.md)-isolated to ensure safety and simplify ergonomics.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Registering undo operations

- [registerUndo(withTarget:handler:)](<undomanager/registerundo(withtarget_handler_).md>) — Registers the specified closure to implement a single undo operation that the target receives.
- [- registerUndoWithTarget:selector:object:](<undomanager/registerundo(withtarget_selector_object_).md>) — Registers the selector of the specified target to implement a single undo operation that the target receives.
- [- prepareWithInvocationTarget:](<undomanager/prepare(withinvocationtarget_).md>) — Prepares the undo manager for invocation-based undo with the given target as the subject of the next undo operation.

### Checking undo ability

- [canUndo](undomanager/canundo.md) — A Boolean value that indicates whether the manager has any actions to undo.
- [canRedo](undomanager/canredo.md) — A Boolean value that indicates whether the manager has any actions to redo.

### Performing undo and redo

- [- undo](<undomanager/undo().md>) — Closes the top-level undo group if necessary, and then performs undo operations on the group.
- [- undoNestedGroup](<undomanager/undonestedgroup().md>) — Performs the undo operations in the last undo group (whether top-level or nested), recording the operations on the redo stack as a single group.
- [- redo](<undomanager/redo().md>) — Performs the operations in the last group on the redo stack, if there are any, recording them on the undo stack as a single group.

### Managing undo and redo stack depth

- [levelsOfUndo](undomanager/levelsofundo.md) — The maximum number of top-level undo groups the undo manager holds.
- [undoCount](undomanager/undocount.md) — The number of times you can invoke undo before there are no actions left to undo.
- [redoCount](undomanager/redocount.md) — The number of times you can invoke redo before there are no actions left to redo.

### Creating undo groups

- [- beginUndoGrouping](<undomanager/beginundogrouping().md>) — Marks the beginning of an undo group.
- [- endUndoGrouping](<undomanager/endundogrouping().md>) — Marks the end of an undo group.
- [groupsByEvent](undomanager/groupsbyevent.md) — A Boolean value that indicates whether the manager automatically creates undo groups around each pass of the run loop.
- [groupingLevel](undomanager/groupinglevel.md) — The number of nested undo groups (or redo groups, if redo is the most recent operation) in the current event loop.

### Enabling and disabling undo

- [- disableUndoRegistration](<undomanager/disableundoregistration().md>) — Disables the recording of undo operations.
- [- enableUndoRegistration](<undomanager/enableundoregistration().md>) — Enables the recording of undo operations.
- [undoRegistrationEnabled](undomanager/isundoregistrationenabled.md) — A Boolean value that indicates whether the recording of undo operations is enabled.

### Checking whether undo or redo is in process

- [undoing](undomanager/isundoing.md) — Returns a Boolean value that indicates whether the manager is in the process of performing an undo action.
- [redoing](undomanager/isredoing.md) — Returns a Boolean value that indicates whether the manager is in the process of performing a redo action.

### Clearing undo operations

- [- removeAllActions](<undomanager/removeallactions().md>) — Clears the undo and redo stacks and reenables the manager.
- [- removeAllActionsWithTarget:](<undomanager/removeallactions(withtarget_).md>) — Clears the undo and redo stacks of all operations involving the specified target as the recipient of the undo message.

### Managing the action name

- [undoActionName](undomanager/undoactionname.md) — The name identifying the undo action.
- [redoActionName](undomanager/redoactionname.md) — The name identifying the redo action.
- [setActionName(_:)](<undomanager/setactionname(__)-cci9.md>) — Sets the name of the action associated with the Undo or Redo command using a localized string resource.
- [- setActionName:](<undomanager/setactionname(__)-8lzip.md>) — Sets the name of the action associated with the Undo or Redo command.

### Getting and localizing the menu item title

- [undoMenuItemTitle](undomanager/undomenuitemtitle.md) — The title of the Undo menu command, such as Undo Paste.
- [redoMenuItemTitle](undomanager/redomenuitemtitle.md) — The title of the Redo menu command, such as Redo Paste.
- [- undoMenuTitleForUndoActionName:](<undomanager/undomenutitle(forundoactionname_).md>) — Returns the localized title of the Undo menu command for the identified action.
- [- redoMenuTitleForUndoActionName:](<undomanager/redomenutitle(forundoactionname_).md>) — Returns the localized title of the Redo menu command for the identified action.

### Working with user info

- [- setActionUserInfoValue:forKey:](<undomanager/setactionuserinfovalue(__forkey_).md>) — Sets a user info value for an undo or redo action.
- [- undoActionUserInfoValueForKey:](<undomanager/undoactionuserinfovalue(forkey_).md>) — Retrieves the undo action’s user info value for the given key.
- [- redoActionUserInfoValueForKey:](<undomanager/redoactionuserinfovalue(forkey_).md>) — Retrieves the redo action’s user info value for the given key.
- [UserInfoKey](undomanager/userinfokey.md) — An extensible namespace for undo and redo user info keys.

### Working with run loops

- [runLoopModes](undomanager/runloopmodes.md) — The modes governing the types of input to handle during a cycle of the run loop.
- [NSUndoCloseGroupingRunLoopOrdering](nsundoclosegroupingrunloopordering.md) — A priority to use when using a run loop to close an undo group.

### Using discardable undo and redo actions

- [- setActionIsDiscardable:](<undomanager/setactionisdiscardable(__).md>) — Sets whether the next undo or redo action is discardable.
- [undoActionIsDiscardable](undomanager/undoactionisdiscardable.md) — A Boolean value that indicates whether the next undo action is discardable.
- [redoActionIsDiscardable](undomanager/redoactionisdiscardable.md) — A Boolean value that indicates whether the next redo action is discardable.

### Working with notifications

- [NSUndoManagerWillUndoChangeNotification](nsnotification/name-swift.struct/nsundomanagerwillundochange.md) — Posted just before an undo manager performs an undo operation.
- [NSUndoManagerDidUndoChangeNotification](nsnotification/name-swift.struct/nsundomanagerdidundochange.md) — Posted just after an undo manager performs an undo operation.
- [NSUndoManagerWillRedoChangeNotification](nsnotification/name-swift.struct/nsundomanagerwillredochange.md) — Posted just before an undo manager performs a redo operation.
- [NSUndoManagerDidRedoChangeNotification](nsnotification/name-swift.struct/nsundomanagerdidredochange.md) — Posted just after an undo manager performs a redo operation.
- [NSUndoManagerCheckpointNotification](nsnotification/name-swift.struct/nsundomanagercheckpoint.md) — Posted whenever an undo manager opens or closes an undo group (except when it opens a top-level group) and when checking the redo stack.
- [NSUndoManagerDidOpenUndoGroupNotification](nsnotification/name-swift.struct/nsundomanagerdidopenundogroup.md) — Posted whenever an undo manager opens an undo group.
- [NSUndoManagerWillCloseUndoGroupNotification](nsnotification/name-swift.struct/nsundomanagerwillcloseundogroup.md) — Posted before an undo manager closes an undo group.
- [NSUndoManagerDidCloseUndoGroupNotification](nsnotification/name-swift.struct/nsundomanagerdidcloseundogroup.md) — Posted after an undo manager closes an undo group.
- [NSUndoManagerGroupIsDiscardableKey](nsundomanagergroupisdiscardablekey.md) — A key, used in a notification’s user info, that indicates the undo group contains only discardable actions.

### Working with notification messages

- [WillUndoChangeMessage](undomanager/willundochangemessage.md) — A message that an undo manager sends before undoing a change.
- [DidUndoChangeMessage](undomanager/didundochangemessage.md) — A message that an undo manager sends after undoing a change.
- [WillRedoChangeMessage](undomanager/willredochangemessage.md) — A message that an undo manager sends before redoing a change.
- [DidRedoChangeMessage](undomanager/didredochangemessage.md) — A message that an undo manager sends after redoing a change.
- [CheckpointMessage](undomanager/checkpointmessage.md) — A message that an undo manager sends at certain checkpoints.
- [DidOpenUndoGroupMessage](undomanager/didopenundogroupmessage.md) — A message that an undo manager sends after opening an undo group.
- [WillCloseUndoGroupMessage](undomanager/willcloseundogroupmessage.md) — A message that an undo manager sends before closing an undo group.
- [DidCloseUndoGroupMessage](undomanager/didcloseundogroupmessage.md) — A message that an undo manager sends after closing an undo group.
