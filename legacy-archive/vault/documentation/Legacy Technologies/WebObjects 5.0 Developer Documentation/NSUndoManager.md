---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSUndoManager.html
archived_at: '2026-07-15T08:13:56.639296Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSUndoManager

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : NSDisposable: Serializable

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

NSUndoManager is a general-purpose recorder of operations for undo and redo. You register an undo operation by specifying the object that's changing (or the owner of that object), along with a method to invoke to revert its state, and the arguments for that method. NSUndoManager groups all operations within a single cycle of the run loop, so that performing an undo reverts all changes that occurred during the loop. Also, when performing undo an NSUndoManager saves the operations reverted so that you can redo the undos.

NSUndoManager is implemented as a class of the Foundation framework because executables other than applications might want to revert changes to their states. For example, you might have an interactive command-line tool with undo and redo commands. However, users typically see undo and redo as application features. WebObjects applications can use NSUndoManagers to undo and redo user operations. Typically a session's editing context has an undo manager that provides undo and redo operations on enterprise objects. For more information, see the class specification for EOEditingContext (eocontrol package).

## Operations and Groups

An undo operation is a method for reverting a change to an object, along with the arguments needed to revert the change (for example, its state before the change). Undo operations are typically collected in undo groups, which represent whole revertible actions, and are stored on a stack. Redo operations and groups are simply undo operations stored on a separate stack (described below). When an NSUndoManager performs undo or redo, it's actually undoing or redoing an entire group of operations. For example, a user could change the first name and the last name of an employee. An application might package both operations as a group, so when the user chooses Undo, both the first and last names are reverted. To undo a single operation, the operation must be packaged alone in a group.

NSUndoManager normally creates undo groups automatically during the run loop. The first time it's asked to record an undo operation in the run loop, it creates a new group. Then, at the end of the loop, it closes the group. You can create additional, nested undo groups within these default groups using the [beginUndoGrouping](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwezlhnfxfk3ten5dxe33vobuw4zy) and [enableUndoRegistration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwk3tbmjwgkvlomrxvezlhnfzxi4tboruw63q) methods. You can also turn off the default grouping behavior using [setGroupsByEvent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxgzlui5zg65lqonbhsrlwmvxhi).

## The Undo and Redo Stacks

Undo groups are stored on a stack, with the oldest groups at the bottom and the newest at the top. The undo stack is unlimited by default, but you can restrict it to a maximum number of groups using the [setLevelsOfUndo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxgzlujrsxmzlmonhwmvlomrxq) method. When the stack exceeds the maximum, the oldest undo groups are dropped from the bottom.

Initially, both stacks are empty. Recording undo operations adds to the undo stack, but the redo stack remains empty until an undo is performed. Performing an undo causes the reverting operations in the latest group to be applied to their objects. Since these operations cause changes to the objects' states, the objects presumably register new operations with the NSUndoManager, this time in the reverse direction from the original operations. Since the NSUndoManager is in the process of performing undo, it records these operations as redo operations on the redo stack. Consecutive undos add to the redo stack. Subsequent redo operations pull the operations off the redo stack, apply them to the objects, and push them back onto the undo stack.

The redo stack's contents last as long as undo and redo are performed successively. However, because applying a new change to an object invalidates the previous changes, as soon as a new undo operation is registered, the redo stack is cleared. This prevents redo from returning objects to an inappropriate prior state. You can check for the ability to undo and redo with the [canUndo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwgylokvxgi3y) and [canRedo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwgylokjswi3y) methods.

## Registering Undo Operations

To add an undo operation to the undo stack, you must register it with the object that will perform the undo operation. To register the undo operation you specify a selector with a single object argument. When an object changes, the object itself (or another object acting on its behalf) records its attributes prior to the change in the argument object. (This argument is frequently an NSDictionary object, but it can be any object.) Performing the undo then involves resetting the object with these attributes.

To record a simple undo operation, you need only invoke [registerUndoWithTarget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxezlhnfzxizlskvxgi32xnf2gqvdbojtwk5a), giving the object to be sent the undo operation selector, the selector to invoke, and an argument to pass with that message. The target object is usually not the actual object whose state is changing; instead, it's the client object, a document or container that holds many undoable objects. The argument is an object that captures the state of the object before the change is made. If you have multiple arguments, use [registerUndoWithTargetAndArguments](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxezlhnfzxizlskvxgi32xnf2gqvdbojtwk5cbnzsec4thovwwk3tuom).

In most applications a single instance of NSUndoManager belongs to an object that contains or manages other objects. This is particularly the case with document-based applications, where a single object is responsible for all undo and redo operations for a document. An object such as this is often called the NSUndoManager's client. Each client object has its own NSUndoManager. The client claims exclusive right to alter its undoable objects so that it can record undo operations for all changes. In the specific case of documents, this scheme keeps each pair of undo and redo stacks separate so that when an undo is performed, it applies to the focal document in the application (typically the one displayed in the key window). It also relieves the individual objects in a document from having to know the identity of their NSUndoManager or from having to track changes to themselves.

However, an object that is changed can have its own NSUndoManager and perform its own undo and redo operations. For example, you could have a custom view that displays images dragged into it; with each successful drag operation, it registers a new undo group. If the view is then selected (that is, made first responder) and the Undo command applied, the previously displayed image would be redisplayed.

## Performing Undo and Redo

Performing undo and redo is usually as simple as sending [undo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxk3ten4) and [redo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxezlen4) messages to the NSUndoManager. __undo__ closes the last open undo group and then applies all the undo operations in that group (recording any undo operations as redo operations instead). __redo__ likewise applies all the redo operations on the top redo group.

__undo__ is intended for undoing top-level groups, and shouldn't be used for nested undo groups. If any unclosed, nested undo groups are on the stack when __undo__ is invoked, it throws an exception. To undo nested groups, you must explicitly close the group with an [enableUndoRegistration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwk3tbmjwgkvlomrxvezlhnfzxi4tboruw63q) message, then use [undoNestedGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxk3ten5hgk43umvseo4tpovya) to undo it. Note also that if you turn off automatic grouping by event with [setGroupsByEvent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxgzlui5zg65lqonbhsrlwmvxhi), you must explicitly close the current undo group with [enableUndoRegistration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwk3tbmjwgkvlomrxvezlhnfzxi4tboruw63q) before invoking either undo method.

## Undo Notifications

An NSUndoManager regularly posts checkpoint notifications to synchronize the inclusion of undo operations in undo groups. Objects sometimes delay performing changes, for various reasons. This means they may also delay registering undo operations for those changes. Because NSUndoManager collects individual operations into groups, it must be sure to synchronize its client with the creation of these groups so that operations are entered into the proper undo groups. To this end, whenever an NSUndoManager opens or closes a new undo group (except when it opens a top-level group), it posts an [CheckpointNotification](#apple-infeercdjbceo) so observers can apply their pending undo operations to the group in effect. The NSUndoManager's client should register itself as an observer for this notification and record undo operations for all pending changes upon receiving it.

NSUndoManager also posts a number of other notifications at specific intervals: when a group is created, when a group is closed, and just before and just after both undo and redo operations. For more on notifications, see ["Notifications" (page 335)](#apple-infeer2birbec).

## Constants

---

NSUndoManager provides the following constant to specify the priority of closing an undo group compared to other operations that take place after the current event ends. Undo groups are automatically closed at the end of the event. The priority specified by this constant is lower than the priority for an EOEditingContext to flush its changes.

|  |  |  |
| --- | --- | --- |
| __Constant__ | __Type__ | __Description__ |
| UndoCloseGroupingRunLoopOrdering | int | Specifies the priority for closing the current undo group compared to other operations in the delayed callback queue. |

## Interfaces Implemented

---

> : NSDisposable
>
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwi2ltobxxgzi)
>
> :

## Method Types

---

> **Registering undo operations**
>
> : [registerUndoWithTarget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxezlhnfzxizlskvxgi32xnf2gqvdbojtwk5a): [registerUndoWithTargetAndArguments](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxezlhnfzxizlskvxgi32xnf2gqvdbojtwk5cbnzsec4thovwwk3tuom)
>
> **Checking undo ability**
>
> : [canUndo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwgylokvxgi3y): [canRedo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwgylokjswi3y)
>
> **Performing undo and redo**
>
> : [undo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxk3ten4): [undoNestedGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxk3ten5hgk43umvseo4tpovya): [redo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxezlen4)
>
> **Limiting the undo stack**
>
> : [setLevelsOfUndo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxgzlujrsxmzlmonhwmvlomrxq): [levelsOfUndo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwyzlwmvwhgt3gkvxgi3y)
>
> **Creating undo groups**
>
> : [beginUndoGrouping](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwezlhnfxfk3ten5dxe33vobuw4zy): [endUndoGrouping](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwk3tekvxgi32hojxxk4djnztq): [setGroupsByEvent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxgzlui5zg65lqonbhsrlwmvxhi): [groupsByEvent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwo4tpovyhgqtziv3gk3tu): [groupingLevel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwo4tpovygs3thjrsxmzlm)
>
> **Disabling undo**
>
> : [disableUndoRegistration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwi2ltmfrgyzkvnzsg6utfm5uxg5dsmf2gs33o): [enableUndoRegistration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwk3tbmjwgkvlomrxvezlhnfzxi4tboruw63q): [isUndoRegistrationEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixws42vnzsg6utfm5uxg5dsmf2gs33oivxgcytmmvsa)
>
> **Checking whether undo or redo is being performed**
>
> : [isUndoing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixws42vnzsg62lom4): [isRedoing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixws42smvsg62lom4)
>
> **Clearing undo operations**
>
> : [removeAllActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxezlnn53gkqlmnrawg5djn5xhg): [removeAllActionsWithTarget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxezlnn53gkqlmnrawg5djn5xhgv3jorufiylsm5sxi)

## Constructors

---

### NSUndoManager

`public NSUndoManager()`

Creates an NSUndoManager object.

---

## Instance Methods

---

### beginUndoGrouping

`public void beginUndoGrouping()`

Marks the beginning of an undo group. All individual undo operations before a subsequent [endUndoGrouping](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwk3tekvxgi32hojxxk4djnztq) message are grouped together and reversed by a later [undo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxk3ten4) message. By default undo groups are begun automatically at the start of the event loop, but you can begin your own undo groups with this method, and nest them within other groups.

This method posts an [CheckpointNotification](#apple-infeercdjbceo) unless a top-level undo is in progress. It posts a [DidOpenUndoGroupNotification](#apple-infeer2fivbeu) if a new group was successfully created.

---

### canRedo

`public boolean canRedo()`

Returns `true` if the receiver has any actions to redo, `false` if it doesn't.

Because any undo operation registered clears the redo stack, this method posts an [CheckpointNotification](#apple-infeercdjbceo) to allow clients to apply their pending operations before testing the redo stack.

---

### canUndo

`public boolean canUndo()`

Returns `true` if the receiver has any actions to undo, `false` if it doesn't. This does not mean you can safely invoke [undo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxk3ten4) or [undoNestedGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxk3ten5hgk43umvseo4tpovya)-you may have to close open undo groups first.

__See Also:__ [enableUndoRegistration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwk3tbmjwgkvlomrxvezlhnfzxi4tboruw63q), [registerUndoWithTarget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxezlhnfzxizlskvxgi32xnf2gqvdbojtwk5a)

---

### disableUndoRegistration

`public void disableUndoRegistration()`

Disables the recording of undo operations, whether by [registerUndoWithTarget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxezlhnfzxizlskvxgi32xnf2gqvdbojtwk5a) or by invocation-based undo. This method can be invoked multiple times by multiple clients. [enableUndoRegistration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwk3tbmjwgkvlomrxvezlhnfzxi4tboruw63q) must be invoked an equal number of times to re-enable undo registration.

---

### dispose

`public void dispose()`

Conformance to [NSDisposable](NSDisposable.md#apple-ijbesq2gineuc). See the method description of [dispose](NSDisposable.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstiruxg4dponqwe3dff5sgs43qn5zwk) in the interface specification for NSDisposable.

---

### enableUndoRegistration

`public void enableUndoRegistration()`

Enables the recording of undo operations. Because undo registration is enabled by default, it is often used to balance a prior [disableUndoRegistration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwi2ltmfrgyzkvnzsg6utfm5uxg5dsmf2gs33o) message. Undo registration isn't actually re-enabled until an enable message balances the last disable message in effect. Throws an IllegalStateException if invoked while no [disableUndoRegistration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwi2ltmfrgyzkvnzsg6utfm5uxg5dsmf2gs33o) message is in effect.

---

### endUndoGrouping

`public void endUndoGrouping()`

Marks the end of an undo group. All individual undo operations back to the matching [beginUndoGrouping](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwezlhnfxfk3ten5dxe33vobuw4zy) message are grouped together and reversed by a later [undo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxk3ten4) or [undoNestedGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxk3ten5hgk43umvseo4tpovya) message. Undo groups can be nested, thus providing functionality similar to nested transactions. Throws an IllegalStateException if there's no __beginUndoGrouping__ message in effect.

This method posts an [CheckpointNotification](#apple-infeercdjbceo) and an [WillCloseUndoGroupNotification](#apple-infeerkijfcec) just before the group is closed.

__See Also:__ [levelsOfUndo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwyzlwmvwhgt3gkvxgi3y)

---

### groupingLevel

`public int groupingLevel()`

Returns the number of nested undo groups (or redo groups, if Redo was last invoked) in the current event loop. If zero is returned, there is no open undo or redo group.

__See Also:__ [levelsOfUndo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwyzlwmvwhgt3gkvxgi3y), [setLevelsOfUndo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxgzlujrsxmzlmonhwmvlomrxq)

---

### groupsByEvent

`public boolean groupsByEvent()`

Returns `true` if the receiver automatically creates undo groups around each pass of the run loop, `false` if it doesn't. The default is `true`.

__See Also:__ [beginUndoGrouping](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwezlhnfxfk3ten5dxe33vobuw4zy)

---

### isRedoing

`public boolean isRedoing()`

Returns `true` if the receiver is in the process of performing its [redo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxezlen4) method, `false` otherwise.

---

### isUndoRegistrationEnabled

`public boolean isUndoRegistrationEnabled()`

Returns whether the recording of undo operations is enabled. Undo registration is enabled by default.

__See Also:__ [disableUndoRegistration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwi2ltmfrgyzkvnzsg6utfm5uxg5dsmf2gs33o), [enableUndoRegistration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwk3tbmjwgkvlomrxvezlhnfzxi4tboruw63q)

---

### isUndoing

`public boolean isUndoing()`

Returns `true` if the receiver is in the process of performing an [undo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxk3ten4) or [undoNestedGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxk3ten5hgk43umvseo4tpovya), `false` otherwise.

---

### levelsOfUndo

`public int levelsOfUndo()`

Returns the maximum number of top-level undo groups the receiver will hold. If ending the current undo group will result in the number of groups exceeding this limit, the oldest groups are dropped from the stack. A limit of zero indicates no limit, so old undo groups are never dropped. The default is zero.

__See Also:__ [enableUndoRegistration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwk3tbmjwgkvlomrxvezlhnfzxi4tboruw63q), [setLevelsOfUndo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxgzlujrsxmzlmonhwmvlomrxq)

---

### redo

`public void redo()`

Performs the operations in the last group on the redo stack, if there are any, recording them on the undo stack as a single group. Throws an IllegalStateException if the method is invoked during an undo operation.

This method posts an [CheckpointNotification](#apple-infeercdjbceo) and [WillRedoChangeNotification](#apple-infeerkjjjcue) before it performs the redo operation, and it posts the [DidRedoChangeNotification](#apple-infeessfi5dei) after it performs the redo operation.

__See Also:__ [registerUndoWithTarget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxezlhnfzxizlskvxgi32xnf2gqvdbojtwk5a)

---

### registerUndoWithTarget

`public void registerUndoWithTarget( Object target, NSSelector aSelector, Object anObject)`

Records a single undo operation for _target_, so that when undo is performed it's sent _aSelector_ with _anObject_ as the sole argument. Also clears the redo stack. See ["Registering Undo Operations" (page 325)](#apple-ijeukq2jifbeq) in the class description for more information.

Throws an IllegalStateException if invoked when no undo group has been established using [beginUndoGrouping](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwezlhnfxfk3ten5dxe33vobuw4zy). Undo groups are normally set by default, so you should rarely need to begin a top-level undo group explicitly.

__See Also:__ [undoNestedGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxk3ten5hgk43umvseo4tpovya), [groupingLevel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwo4tpovygs3thjrsxmzlm)

---

### registerUndoWithTargetAndArguments

`public void registerUndoWithTargetAndArguments( Object target, NSSelector selector, Object[] parameters[])`

---

### removeAllActions

`public void removeAllActions()`

Clears the undo and redo stacks and reenables the receiver.

__See Also:__ [enableUndoRegistration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwk3tbmjwgkvlomrxvezlhnfzxi4tboruw63q), [removeAllActionsWithTarget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxezlnn53gkqlmnrawg5djn5xhgv3jorufiylsm5sxi)

---

### removeAllActionsWithTarget

`public void removeAllActionsWithTarget(Object target)`

Clears the undo and redo stacks of all operations involving _target_ as the recipient of the undo message. Doesn't re-enable the receiver if it's disabled. An object that shares an NSUndoManager with other clients should invoke this message in its implementation of __finalize__. <<True?>>

__See Also:__ [enableUndoRegistration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwk3tbmjwgkvlomrxvezlhnfzxi4tboruw63q), [removeAllActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxezlnn53gkqlmnrawg5djn5xhg)

---

### setGroupsByEvent

`public void setGroupsByEvent(boolean flag)`

Sets whether the receiver automatically groups undo operations during the run loop. If _flag_ is `true`, the receiver creates undo groups around each pass through the run loop; if flag is `false` it doesn't. The default is `true`.

If you turn automatic grouping off, you must close groups explicitly before invoking either [undo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxk3ten4) or [undoNestedGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxk3ten5hgk43umvseo4tpovya).

__See Also:__ [groupingLevel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwo4tpovygs3thjrsxmzlm), [groupsByEvent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwo4tpovyhgqtziv3gk3tu)

---

### setLevelsOfUndo

`public void setLevelsOfUndo(int levels)`

Sets the maximum number of top-level undo groups the receiver will hold to _levels_. When ending an undo group results in the number of groups exceeding this limit, the oldest groups are dropped from the stack. A limit of zero indicates no limit, so that old undo groups are never dropped. The default is zero.

If invoked with a limit below the prior limit, old undo groups are immediately dropped.

__See Also:__ [enableUndoRegistration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwk3tbmjwgkvlomrxvezlhnfzxi4tboruw63q), [levelsOfUndo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwyzlwmvwhgt3gkvxgi3y)

---

### undo

`public void undo()`

Closes the top-level undo group if necessary and invokes [undoNestedGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxk3ten5hgk43umvseo4tpovya). It also invokes [endUndoGrouping](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwk3tekvxgi32hojxxk4djnztq) if the nesting level is 1. Throws an InternalInconsistencyException if more than one undo group is open (that is, if the last group isn't at the top level).

This method posts an ["CheckpointNotification" (page 336)](#apple-infeercdjbceo).

__See Also:__ [enableUndoRegistration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwk3tbmjwgkvlomrxvezlhnfzxi4tboruw63q), [groupingLevel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwo4tpovygs3thjrsxmzlm)

---

### undoNestedGroup

`public void undoNestedGroup()`

Performs the undo operations in the last undo group (whether top-level or nested), recording the operations on the redo stack as a single group. Throws an InternalInconsistencyException if any undo operations have been registered since the last [enableUndoRegistration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwk3tbmjwgkvlomrxvezlhnfzxi4tboruw63q) message.

This method posts an ["CheckpointNotification" (page 336)](#apple-infeercdjbceo) and ["WillUndoChangeNotification" (page 338)](#apple-infeeskbivdee) before it performs the undo operation, and it posts the ["DidUndoChangeNotification" (page 337)](#apple-infeeschjjbug) after it performs the undo operation.

__See Also:__ [undo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxk3ten4)

---

## Notifications

---

### CheckpointNotification

`public static final String CheckpointNotification`

Posted whenever an NSUndoManager opens or closes an undo group (except when it opens a top-level group), and when an NSUndoManager checks the redo stack in [canRedo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwgylokjswi3y). The notification contains:

**notification object**
: The NSUndoManager

**_userInfo_**
: `null`

### DidOpenUndoGroupNotification

`public static final String DidOpenUndoGroupNotification`

Posted whenever an NSUndoManager opens an undo group, which occurs in an invocation of [beginUndoGrouping](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwezlhnfxfk3ten5dxe33vobuw4zy). The notification contains:

**notification object**
: The NSUndoManager

**_userInfo_**
: `null`

### DidRedoChangeNotification

`public static final String DidRedoChangeNotification`

Posted just after an NSUndoManager performs a redo operation ( [redo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxezlen4)). The notification contains:

**notification object**
: The NSUndoManager

**_userInfo_**
: `null`

### DidUndoChangeNotification

`public static final String DidUndoChangeNotification`

Posted just after an NSUndoManager performs an undo operation. If you invoke [undo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxk3ten4) or [undoNestedGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxk3ten5hgk43umvseo4tpovya), this notification will be posted. The notification contains:

**notification object**
: The NSUndoManager

**_userInfo_**
: `null`

### WillCloseUndoGroupNotification

`public static final String WillCloseUndoGroupNotification`

Posted whenever an NSUndoManager closes an undo group, which occurs in an invocation of [endUndoGrouping](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixwk3tekvxgi32hojxxk4djnztq). The notification contains:

**notification object**
: The NSUndoManager

**_userInfo_**
: `null`

### WillRedoChangeNotification

`public static final String WillRedoChangeNotification`

Posted just before an NSUndoManager performs a redo operation ( [redo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxezlen4)). The notification contains:

**notification object**
: The NSUndoManager

**_userInfo_**
: `null`

### WillUndoChangeNotification

`public static final String WillUndoChangeNotification`

Posted just before an NSUndoManager performs an undo operation. If you invoke [undo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxk3ten4) or [undoNestedGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkvxgi32nmfxgcz3foixxk3ten5hgk43umvseo4tpovya), this notification will be posted. The notification contains:

**notification object**
: The NSUndoManager

**_userInfo_**
: `null`

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
