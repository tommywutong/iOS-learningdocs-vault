---
title: NSFilePresenter
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilepresenter
source_url: 'https://developer.apple.com/documentation/foundation/nsfilepresenter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilepresenter.json'
content_hash: 'sha256:fec6d622dc723aac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSFilePresenter

<sub>Protocol</sub>

The interface a file coordinator uses to inform an object presenting a file about changes to that file made elsewhere in the system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSFilePresenter : NSObjectProtocol
```

## Overview

Objects that allow the user to view or edit the content of files or directories should adopt the [NSFilePresenter](nsfilepresenter.md) protocol. You use file presenters in conjunction with an [NSFileCoordinator](nsfilecoordinator.md) object to coordinate access to a file or directory among the objects of your application and between your application and other processes. When changes to an item occur, the system notifies objects that adopt this protocol and gives them a chance to respond appropriately.

Use the methods of this protocol to respond to actions about to be taken on the presented file or directory. When another object or process uses a file coordinator to begin reading or writing a file or directory, the file coordinator notifies all presented objects interested in the item first. It notifies the presenter objects by invoking one of the methods defined by this protocol on that object. The actual invocation of that method occurs on the operation queue in the [presentedItemOperationQueue](nsfilepresenter/presenteditemoperationqueue.md) property. Your file presenter must provide this queue. If your queue supports the concurrent execution of operations, the methods of your presenter object must be thread-safe and able to run in multiple queues simultaneously.

You can use file presenters to coordinate access to a file or directory among your application’s objects. If another process uses a file coordinator for the same file or directory, your presenter objects are similarly notified whenever the other process makes its changes. Your presenter objects are not notified about changes made directly using low-level read and write calls to the file. Only changes that go through a file coordinator result in notifications.

For information about how to use file presenters with a file coordinator object, see [NSFileCoordinator](nsfilecoordinator.md).

### File Presenters and iOS

If your app enters the background with an active file presenter, any other processes that perform a coordinated read or write on the presented file can deadlock. To prevent this situation, call the coordinator’s [+ removeFilePresenter:](<nsfilecoordinator/removefilepresenter(__).md>) type method to remove the file presenter in the [applicationDidEnterBackground(_:)](<../uikit/uiapplicationdelegate/applicationdidenterbackground(__).md>) method or in response to a [didEnterBackgroundNotification](../uikit/uiapplication/didenterbackgroundnotification.md) notification. Call [+ addFilePresenter:](<nsfilecoordinator/addfilepresenter(__).md>) to add the file presenter again in the [applicationWillEnterForeground(_:)](<../uikit/uiapplicationdelegate/applicationwillenterforeground(__).md>) method or in response to a [willEnterForegroundNotification](../uikit/uiapplication/willenterforegroundnotification.md) notification.

> [!note] Note
> The [UIDocument](../uikit/uidocument.md) class automatically removes itself when your app goes to the background. It automatically adds itself again when your app returns to the foreground.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing File Presenter Attributes

- [presentedItemURL](nsfilepresenter/presenteditemurl.md) — The URL of the presented file or directory.
- [presentedItemOperationQueue](nsfilepresenter/presenteditemoperationqueue.md) — The operation queue in which to execute presenter-related messages.
- [primaryPresentedItemURL](nsfilepresenter/primarypresenteditemurl.md) — The URL of a secondary item’s primary presented file or directory.

### Relinquishing Managed Files

- [- relinquishPresentedItemToReader:](<nsfilepresenter/relinquishpresenteditem(toreader_).md>) — Notifies your object that another object or process wants to read the presented file or directory.
- [- relinquishPresentedItemToWriter:](<nsfilepresenter/relinquishpresenteditem(towriter_).md>) — Notifies your object that another object or process wants to write to the presented file or directory.

### Handling Changes to Files

- [- savePresentedItemChangesWithCompletionHandler:](<nsfilepresenter/savepresenteditemchanges(completionhandler_).md>) — Tells your object to save any unsaved changes for the presented item.
- [- accommodatePresentedItemDeletionWithCompletionHandler:](<nsfilepresenter/accommodatepresenteditemdeletion(completionhandler_).md>) — Tells your object that its presented item is about to be deleted.
- [- presentedItemDidMoveToURL:](<nsfilepresenter/presenteditemdidmove(to_).md>) — Tells your object that the presented item moved or was renamed.
- [- presentedItemDidChange](<nsfilepresenter/presenteditemdidchange().md>) — Tells your object that the presented item’s contents or attributes changed.

### Responding to Version Changes

- [- presentedItemDidGainVersion:](<nsfilepresenter/presenteditemdidgain(__).md>) — Tells the delegate that a new version of the file or file package was added.
- [- presentedItemDidLoseVersion:](<nsfilepresenter/presenteditemdidlose(__).md>) — Tells the delegate that a version of the file or file package was removed.
- [- presentedItemDidResolveConflictVersion:](<nsfilepresenter/presenteditemdidresolveconflict(__).md>) — Tells the delegate that some other entity resolved a version conflict for the presenter’s file or file package.
- [- presentedSubitemAtURL:didGainVersion:](<nsfilepresenter/presentedsubitem(at_didgain_).md>) — Tells the delegate that the item inside the presented directory gained a new version.
- [- presentedSubitemAtURL:didLoseVersion:](<nsfilepresenter/presentedsubitem(at_didlose_).md>) — Tells the delegate that the item inside the presented directory lost an existing version.
- [- presentedSubitemAtURL:didResolveConflictVersion:](<nsfilepresenter/presentedsubitem(at_didresolve_).md>) — Tells the delegate that the item inside the presented directory had a version conflict resolved by an outside entity.

### Handling Changes to a Presented Directory

- [- accommodatePresentedSubitemDeletionAtURL:completionHandler:](<nsfilepresenter/accommodatepresentedsubitemdeletion(at_completionhandler_).md>) — Tells the delegate that some entity wants to delete an item that is inside of a presented directory.
- [- presentedSubitemDidAppearAtURL:](<nsfilepresenter/presentedsubitemdidappear(at_).md>) — Tells the delegate that an item was added to the presented directory.
- [- presentedSubitemAtURL:didMoveToURL:](<nsfilepresenter/presentedsubitem(at_didmoveto_).md>) — Tells the delegate that an item in the presented directory moved to a new location.
- [- presentedSubitemDidChangeAtURL:](<nsfilepresenter/presentedsubitemdidchange(at_).md>) — Tells the delegate that the contents or attributes of the specified item changed.

### Ubiquity Change Notifications

- [observedPresentedItemUbiquityAttributes](nsfilepresenter/observedpresenteditemubiquityattributes.md) — A list of ubiquity attributes used to generate and send notifications whenever an attribute in the list changes.
- [- presentedItemDidChangeUbiquityAttributes:](<nsfilepresenter/presenteditemdidchangeubiquityattributes(__).md>) — Tells your object that the file or file package’s ubiquity attributes have changed.

### Instance Methods

- [- accommodatePresentedItemEvictionWithCompletionHandler:](<nsfilepresenter/accommodatepresenteditemeviction(completionhandler_).md>) — Given that something in the system is waiting to evict the presented file or directory, do whatever it takes to ensure that the eviction will succeed and that the receiver’s application will behave properly when the eviction has happened, and then invoke the completion handler. This must include calling +[NSFileCoordinator removeFilePresenter:]. You may instead prevent eviction by passing the completion handler a meaningful error.

## See Also

### Coordinated file access

- [NSFileAccessIntent](nsfileaccessintent.md) — The details of a coordinated-read or coordinated-write operation.
- [NSFileCoordinator](nsfilecoordinator.md) — An object that coordinates the reading and writing of files and directories among file presenters.
