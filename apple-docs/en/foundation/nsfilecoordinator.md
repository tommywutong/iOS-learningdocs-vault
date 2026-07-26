---
title: NSFileCoordinator
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilecoordinator
source_url: 'https://developer.apple.com/documentation/foundation/nsfilecoordinator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilecoordinator.json'
content_hash: 'sha256:6665a30944028441'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSFileCoordinator

<sub>Class</sub>

An object that coordinates the reading and writing of files and directories among file presenters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSFileCoordinator
```

## Overview

The [NSFileCoordinator](nsfilecoordinator.md) class coordinates the reading and writing of files and directories among multiple processes and objects in the same process. You use instances of this class as is to read from, write to, modify the attributes of, change the location of, or delete a file or directory, but before your code to perform those actions executes, the file coordinator lets registered file presenter objects perform any tasks that they might require to ensure their own integrity. For example, if you want to change the location of a file, other objects interested in that file need to know where you intend to move it so that they can update their references.

Objects that adopt the [NSFilePresenter](nsfilepresenter.md) protocol must register themselves with the [NSFileCoordinator](nsfilecoordinator.md) class to be notified of any pending changes. They do this by calling the [+ addFilePresenter:](<nsfilecoordinator/addfilepresenter(__).md>) class method. A file presenter must balance calls to [+ addFilePresenter:](<nsfilecoordinator/addfilepresenter(__).md>) with a call to [+ removeFilePresenter:](<nsfilecoordinator/removefilepresenter(__).md>) before being released, even in a garbage-collected application. The file presenter class maintains a list of active file presenter objects in the current application and uses that list, plus the file coordinator classes in other processes, to deliver notifications to all of the objects interested in a particular item.

Instances of [NSFileCoordinator](nsfilecoordinator.md) are meant to be used on a per-file-operation basis, where a file operation is something like opening and reading the contents of a file or moving a batch of files and directories to a new location. There is no benefit to keeping a file coordinator object past the length of the planned operation. In fact, because file coordinators retain file presenter objects, keeping one around could prevent the file presenter objects from being released in a timely manner.

For information about implementing a file presenter object to receive file-related notifications, see [NSFilePresenter](nsfilepresenter.md).

### File Presenters and iOS

If your app or extension enters the background with an active file presenter, it may be terminated by the system in order to prevent deadlock on that file. To prevent this situation, call [+ removeFilePresenter:](<nsfilecoordinator/removefilepresenter(__).md>) to remove the file presenter in the [applicationDidEnterBackground(_:)](<../uikit/uiapplicationdelegate/applicationdidenterbackground(__).md>) method or in response to a [didEnterBackgroundNotification](../uikit/uiapplication/didenterbackgroundnotification.md) notification. Call [+ addFilePresenter:](<nsfilecoordinator/addfilepresenter(__).md>) to add the file presenter again in the [applicationWillEnterForeground(_:)](<../uikit/uiapplicationdelegate/applicationwillenterforeground(__).md>) method or in response to a [willEnterForegroundNotification](../uikit/uiapplication/willenterforegroundnotification.md) notification.

> [!note] Note
> The [UIDocument](../uikit/uidocument.md) class automatically removes itself when your app goes to the background. It automatically adds itself again when your app returns to the foreground.

### File Coordinators and iOS

A coordinated read or write will automatically begin a background task when granted, similar to one created with the [beginBackgroundTask(expirationHandler:)](<../uikit/uiapplication/beginbackgroundtask(expirationhandler_).md>) method. This helps ensure that your app or extension has sufficient time to finish the read or write operation if it’s suspended, without creating a deadlock on access to that file by other processes. If a process is suspended while waiting for a coordinated read or write to be granted, the request is canceled, and an `NSError` object with the code [NSUserCancelledError](nsusercancellederror-swift.var.md) is produced. If the background task expires, the process is terminated.

> [!note] Note
> The [UIDocument](../uikit/uidocument.md) class automatically requests additional background time and safely performs coordinated reads and writes when loading and saving the document.

### Threading Considerations

Each file coordinator object you create should be used on a single thread only. If you need to coordinate file operations across multiple objects in different threads, each object should create its own file coordinator.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing a File Coordinator

- [- initWithFilePresenter:](<nsfilecoordinator/init(filepresenter_).md>) — Initializes and returns a file coordinator object using the specified file presenter.

### Managing File Presenters

- [+ addFilePresenter:](<nsfilecoordinator/addfilepresenter(__).md>) — Registers the specified file presenter object so that it can receive notifications.
- [+ removeFilePresenter:](<nsfilecoordinator/removefilepresenter(__).md>) — Unregisters the specified file presenter object.
- [filePresenters](nsfilecoordinator/filepresenters.md) — Returns an array containing the currently registered file presenter objects.
- [purposeIdentifier](nsfilecoordinator/purposeidentifier.md) — A string that uniquely identifies the file access that was performed by this file coordinator.

### Coordinating File Operations Asynchronously

- [- coordinateAccessWithIntents:queue:byAccessor:](<nsfilecoordinator/coordinate(with_queue_byaccessor_).md>) — Performs a number of coordinated-read or -write operations asynchronously.

### Coordinating File Operations Synchronously

- [- coordinateReadingItemAtURL:options:error:byAccessor:](<nsfilecoordinator/coordinate(readingitemat_options_error_byaccessor_).md>) — Initiates a read operation on a single file or directory using the specified options.
- [- coordinateWritingItemAtURL:options:error:byAccessor:](<nsfilecoordinator/coordinate(writingitemat_options_error_byaccessor_).md>) — Initiates a write operation on a single file or directory using the specified options.
- [- coordinateReadingItemAtURL:options:writingItemAtURL:options:error:byAccessor:](<nsfilecoordinator/coordinate(readingitemat_options_writingitemat_options_error_byaccessor_).md>) — Initiates a read operation that contains a follow-up write operation.
- [- coordinateWritingItemAtURL:options:writingItemAtURL:options:error:byAccessor:](<nsfilecoordinator/coordinate(writingitemat_options_writingitemat_options_error_byaccessor_).md>) — Initiates a write operation that involves a secondary write operation.
- [- prepareForReadingItemsAtURLs:options:writingItemsAtURLs:options:error:byAccessor:](<nsfilecoordinator/prepare(forreadingitemsat_options_writingitemsat_options_error_byaccessor_).md>) — Prepare to read or write from multiple files in a single batch operation.
- [- itemAtURL:willMoveToURL:](<nsfilecoordinator/item(at_willmoveto_).md>) — Announces that your app is moving a file to a new URL.
- [- itemAtURL:didMoveToURL:](<nsfilecoordinator/item(at_didmoveto_).md>) — Notifies relevant file presenters that the location of a file or directory changed.
- [- cancel](<nsfilecoordinator/cancel().md>) — Cancels any active file coordination calls.

### Constants

- [ReadingOptions](nsfilecoordinator/readingoptions.md) — Options to use when reading the contents or attributes of a file or directory.
- [WritingOptions](nsfilecoordinator/writingoptions.md) — Options to use when changing the contents or attributes of a file or directory.

### Ubiquity Change Notifications

- [- itemAtURL:didChangeUbiquityAttributes:](<nsfilecoordinator/item(at_didchangeubiquityattributes_).md>) — Tells observing file providers that the item’s ubiquity attributes have changed.

## See Also

### Coordinated file access

- [NSFilePresenter](nsfilepresenter.md) — The interface a file coordinator uses to inform an object presenting a file about changes to that file made elsewhere in the system.
- [NSFileAccessIntent](nsfileaccessintent.md) — The details of a coordinated-read or coordinated-write operation.
