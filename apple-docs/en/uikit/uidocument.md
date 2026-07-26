---
title: UIDocument
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument
source_url: 'https://developer.apple.com/documentation/uikit/uidocument'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument.json'
content_hash: 'sha256:ade4e0cb71397626'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDocument

<sub>Class</sub>

An abstract base class for managing discrete portions of your app’s data.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated class UIDocument
```

## Overview

Apps that make use of [UIDocument](uidocument.md) and its underlying architecture get many benefits for their documents:

- Asynchronous reading and writing of data on a background queue, meaning your app’s responsiveness is unaffected while reading and writing operations take place
- Coordinated reading and writing of document files automatically integrated with cloud services
- Support for discovering conflicts between different versions of a document
- Safe-saving of document data by writing data first to a temporary file and then replacing the current document file with it
- Automatic saving of document data at opportune moments and support for dealing with suspend behaviors

In the Model-View-Controller design pattern, a [UIDocument](uidocument.md) object is a model object or model-controller object — it manages the data of a document or the aggregate model objects that together constitute the document’s data. You typically pair it with a view controller that manages the view presenting the document’s contents. [UIDocument](uidocument.md) provides no direct support for managing document views, but view controllers that subclass [UIDocumentViewController](uidocumentviewcontroller.md) can present a `UIDocument`, and view controllers that subclass [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) can organize and display `UIDocument` collections.

Document-based apps include those that can generate multiple documents, each with its own file-system location. A document-based app must create a subclass of [UIDocument](uidocument.md) for its documents.

> [!note] Note
> If you’re using a database to store document data, create a subclass of the [UIManagedDocument](uimanageddocument.md) class instead of [UIDocument](uidocument.md); [UIManagedDocument](uimanageddocument.md) is a subclass of [UIDocument](uidocument.md).

The primary attribute of a document in the [UIDocument](uidocument.md) architecture is its file URL. When you initialize an instance of your document subclass by calling [- initWithFileURL:](<uidocument/init(fileurl_).md>), you must pass a file URL locating the document file in the app sandbox. [UIDocument](uidocument.md) determines the file type (the Uniform Type Identifier associated with the file extension) and the document name (the filename component) from the file URL. You can override the accessor methods of the [fileType](uidocument/filetype.md) and [localizedName](uidocument/localizedname.md) properties to supply different values.

The following outlines the life cycle of a typical document:

1. You create a new document or open an existing document.

    - To create a new document, allocate and initialize an instance of your subclass and then call [- saveToURL:forSaveOperation:completionHandler:](<uidocument/save(to_for_completionhandler_).md>) on the instance.
    - To open an existing document (selected by the user), allocate and initialize an instance of your subclass and then call [- openWithCompletionHandler:](<uidocument/open(completionhandler_).md>) on the instance.
2. The user edits the document. As the user edits, track changes to the document. [UIDocument](uidocument.md) periodically notes when there are unsaved changes and writes the document data to its file.
3. The user requests that the document be integrated with cloud services (optional). You must enable the document for cloud storage. You must also resolve any conflicts between different versions of the same document.
4. The user closes the document. Call [- closeWithCompletionHandler:](<uidocument/close(completionhandler_).md>) on the document instance. [UIDocument](uidocument.md) saves the document if there are any unsaved changes.

A typical document-based app calls [- openWithCompletionHandler:](<uidocument/open(completionhandler_).md>), [- closeWithCompletionHandler:](<uidocument/close(completionhandler_).md>), and [- saveToURL:forSaveOperation:completionHandler:](<uidocument/save(to_for_completionhandler_).md>) on the main thread. When the read or save operation kicked off by these methods concludes, the system executes the completion-handler block on the same dispatch queue as the system used to invoke the method, allowing you to complete any tasks contingent on the read or save operation. If the operation isn’t successful, the system passes [false](../swift/false.md) to the completion-handler block.

### Implement the NSFilePresenter protocol

The [UIDocument](uidocument.md) class adopts the [NSFilePresenter](../foundation/nsfilepresenter.md) protocol. When another client attempts to read the document of a [UIDocument](uidocument.md)-based app, the system suspends reading until the system provides the [UIDocument](uidocument.md) object an opportunity to save any changes made to the document.

Although some implementations do nothing, [UIDocument](uidocument.md) implements all [NSFilePresenter](../foundation/nsfilepresenter.md) methods. Specifically, [UIDocument](uidocument.md):

- Implements [relinquishPresentedItem(toReader:)](<../foundation/nsfilepresenter/relinquishpresenteditem(toreader_).md>) to forward the incoming block to [- performAsynchronousFileAccessUsingBlock:](<uidocument/performasynchronousfileaccess(__).md>)
- Implements [relinquishPresentedItem(toWriter:)](<../foundation/nsfilepresenter/relinquishpresenteditem(towriter_).md>) to check if the file-modification date changed; if the file is newer than before, it calls [- revertToContentsOfURL:completionHandler:](<uidocument/revert(tocontentsof_completionhandler_).md>) with the value of the [fileURL](uidocument/fileurl.md) as the URL parameter
- Implements [presentedItemDidMove(to:)](<../foundation/nsfilepresenter/presenteditemdidmove(to_).md>) to update the document’s file URL ([fileURL](uidocument/fileurl.md))

In your [UIDocument](uidocument.md) subclass, if you override a [NSFilePresenter](../foundation/nsfilepresenter.md) method, you can always invoke the superclass implementation (`super`).

### Create a subclass

Each document-based app must create a subclass of [UIDocument](uidocument.md) whose instances represent its documents. The subclassing requirements for most apps are simple:

- For writing operations, implement the [- contentsForType:error:](<uidocument/contents(fortype_).md>) method to provide a snapshot of document data. The data must be in the form of an [NSData](../foundation/nsdata.md) object (for flat files) or an [FileWrapper](../foundation/filewrapper.md) object (for file packages). Writing operations are usually initiated through the autosave feature.
- For reading operations, implement the [- loadFromContents:ofType:error:](<uidocument/load(fromcontents_oftype_).md>) method to receive an [NSData](../foundation/nsdata.md) or [FileWrapper](../foundation/filewrapper.md) object and initialize the app’s data structures with it.
- Implement change tracking to enable the autosaving feature. See [Track changes](uidocument.md#Track-changes) for details.
- When cloud services are enabled for a document, resolve conflicts between different versions of a document. See [Resolve conflicts and handle errors](uidocument.md#Resolve-conflicts-and-handle-errors) for details.

  The system typically calls the [- contentsForType:error:](<uidocument/contents(fortype_).md>) and [- loadFromContents:ofType:error:](<uidocument/load(fromcontents_oftype_).md>) methods on the main queue. More specifically:
- The system calls the [- contentsForType:error:](<uidocument/contents(fortype_).md>) method on the queue that the system called the [- saveToURL:forSaveOperation:completionHandler:](<uidocument/save(to_for_completionhandler_).md>) method on; writing of data takes place on a background thread.
- The system calls the [- loadFromContents:ofType:error:](<uidocument/load(fromcontents_oftype_).md>) method on the queue that the system called the [- openWithCompletionHandler:](<uidocument/open(completionhandler_).md>) method on.

If you have special requirements for reading and writing document data for which the [- contentsForType:error:](<uidocument/contents(fortype_).md>) and [- loadFromContents:ofType:error:](<uidocument/load(fromcontents_oftype_).md>) methods won’t suffice, you can override other methods of the [UIDocument](uidocument.md) class. See [Override input and output methods](uidocument.md#Override-input-and-output-methods) for a discussion of these requirements and methods.

#### Track changes

To enable the autosaving feature of [UIDocument](uidocument.md), you must notify it when users make changes to a document. [UIDocument](uidocument.md) periodically checks whether the [hasUnsavedChanges](uidocument/hasunsavedchanges.md) method returns [true](../swift/true.md); if it does, it initiates the save operation for the document.

There are two primary ways to implement change tracking in your [UIDocument](uidocument.md) subclass:

- Call the methods of the [UndoManager](../foundation/undomanager.md) class to implement undo and redo for the document. You can access the default [UndoManager](../foundation/undomanager.md) object from the [undoManager](uidocument/undomanager.md) property. This is the preferred approach, especially for existing apps that already support undo and redo.
- Call the [- updateChangeCount:](<uidocument/updatechangecount(__).md>) method at the appropriate junctures in your code.

#### Resolve conflicts and handle errors

A [UIDocument](uidocument.md) object has a specific state at any moment in its life cycle. You can check the current state by querying the [documentState](uidocument/documentstate.md) property, and get notified about changes by observing the [UIDocumentStateChangedNotification](uidocument/statechangednotification.md) notification.

If the owner enables a document for iCloud, it’s important to check for conflicting versions and to attempt to resolve conflicts. Listen for the [UIDocumentStateChangedNotification](uidocument/statechangednotification.md) notification and then checking if the document state is [UIDocumentStateInConflict](uidocument/state/inconflict.md). This state indicates that there are conflicting versions of the document, which you can access by calling the [NSFileVersion](../foundation/nsfileversion.md) class method [unresolvedConflictVersionsOfItem(at:)](<../foundation/nsfileversion/unresolvedconflictversionsofitem(at_).md>), passing in the document’s file URL. If you can resolve a conflict correctly without user interaction, do so. Otherwise, discretely notify the user that a conflict exists and let them choose how to resolve it. Possible approaches include:

- Display the conflicting versions, from which a user can pick one or both versions to keep.
- Display a merged version and giving the user an option to pick it.
- Display the file modification dates and giving the user the option to choose one or both.

Document state, in addition to indicating an inter-file conflict, can indicate errors. For example, [UIDocumentStateClosed](uidocument/state/closed.md) indicates an error in reading, and [UIDocumentStateSavingError](uidocument/state/savingerror.md) indicates an error in saving or reverting a document. The system notifies your app of reading and writing errors through the `success` parameter passed into the completion handlers of the [- openWithCompletionHandler:](<uidocument/open(completionhandler_).md>), [- closeWithCompletionHandler:](<uidocument/close(completionhandler_).md>), [- revertToContentsOfURL:completionHandler:](<uidocument/revert(tocontentsof_completionhandler_).md>), and [- saveToURL:forSaveOperation:completionHandler:](<uidocument/save(to_for_completionhandler_).md>) methods.

You can handle errors by calling or implementing the [- handleError:userInteractionPermitted:](<uidocument/handleerror(__userinteractionpermitted_).md>) method; the default implementations of the [- openWithCompletionHandler:](<uidocument/open(completionhandler_).md>) and [- saveToURL:forSaveOperation:completionHandler:](<uidocument/save(to_for_completionhandler_).md>) methods call `handleError(_:userInteractionPermitted:)` when a [UIDocument](uidocument.md) object encounters a reading or writing error, respectively. You can handle read, save, and reversion errors by informing the user and, if the situation permits, trying to recover from the error.

Be sure to read the description for the [- contentsForType:error:](<uidocument/contents(fortype_).md>) method for its guidance on handling errors encountered during document saving.

#### Override input and output methods

If you app has special requirements for reading or writing document data, it can override methods of [UIDocument](uidocument.md) other than [- loadFromContents:ofType:error:](<uidocument/load(fromcontents_oftype_).md>) and [- contentsForType:error:](<uidocument/contents(fortype_).md>). These requirements often include the following:

- Incremental reading and writing of large data files

  Override the [- readFromURL:error:](<uidocument/read(from_).md>) and [- writeContents:toURL:forSaveOperation:originalContentsURL:error:](<uidocument/writecontents(__to_for_originalcontentsurl_).md>) methods, respectively.
- Custom representations of document data (that is, not an [NSData](../foundation/nsdata.md) or [FileWrapper](../foundation/filewrapper.md) object)

  Override the [- readFromURL:error:](<uidocument/read(from_).md>) method when reading document data and the [- writeContents:toURL:forSaveOperation:originalContentsURL:error:](<uidocument/writecontents(__to_for_originalcontentsurl_).md>) method when writing document data.
- Performing actions before or after reading or writing data

  Override [- openWithCompletionHandler:](<uidocument/open(completionhandler_).md>) and [- saveToURL:forSaveOperation:completionHandler:](<uidocument/save(to_for_completionhandler_).md>).
- A custom approach to safe-saving

  Override the [- writeContents:andAttributes:safelyToURL:forSaveOperation:error:](<uidocument/writecontents(__andattributes_safelyto_for_).md>) method.
- Changing the file type of a document before it’s saved

  Override the [savingFileType](uidocument/savingfiletype.md) method to return a file type other than the default ([fileType](uidocument/filetype.md)). An example of this is an RTF document which, after a user adds an image to it, should be saved as an RTFD document.

If you override these methods, be aware that all reading and writing of document data must be done on a background queue and must be coordinated with other attempts to read from and write to the same document file. Because of this, you usually call the superclass implementation (`super`) as part of your override, and if you call other `UIDocument` methods, you usually invoke them in the block passed into a call of the [- performAsynchronousFileAccessUsingBlock:](<uidocument/performasynchronousfileaccess(__).md>) method. Read the method descriptions for details.

#### Access document attributes

If you override any of the document-attribute properties (listed under [Accessing document attributes](uidocument.md#Accessing-document-attributes)) by overriding the related accessor methods, be aware that the UIKit framework can call these accessor methods on a background thread. Thus your overriding implementation must be thread safe.

### Rename documents

`UIDocument` provides support for changing the document’s title. Security considerations require that clients can’t programmatically rename a file on the file system, and that the system confirms that a person intends to rename their file. To satisfy these restrictions, the system, instead of your app, presents a renaming user interface using a process outside your app. The external process renames the underlying file and reports the new location back to the client.

To support this external process, `UIDocument` conforms to [UINavigationItemRenameDelegate](uinavigationitemrenamedelegate-96g5t.md) and handles the rename request internally when a person invokes renaming from the title menu. If you’re using [UIDocumentViewController](uidocumentviewcontroller.md), it automatically configures renaming for you. Otherwise, you manually assign the document as the navigation item’s [renameDelegate](uinavigationitem/renamedelegate-o32h.md).

```swift
init(document: MyDocument) {
    self.document = document
    super.init(nibName:nil, bundle: nil)
    self.navigationItem.renameDelegate = document
}
```

The Rename action appears in the title menu as one of the system-suggested actions. When a person taps the Rename action, the system shows an inline text field for changing the navigation item’s `title`. Upon renaming the item, the system changes the file name in storage as though the person renamed the file in another application.

Prior to iOS 17, to enable the system rename user interface, a client view controller adopts the `UINavigationItemRenameDelegate` protocol and assigns itself as the navigation item’s `renameDelegate`. It’s the client’s responsibility to implement callbacks such as [navigationItem(_:didEndRenamingWith:)](<uinavigationitemrenamedelegate-5j4ws/navigationitem(__didendrenamingwith_).md>) (Swift) or [navigationItem:didEndRenamingWithTitle:](uinavigationitemrenamedelegate-96g5t/navigationitem_didendrenamingwithtitle_.md) (Objective-C) to explicitly move the file in storage.

```swift
class EditorViewController: UIViewController,
        UINavigationItemRenameDelegate {

    override func viewDidLoad() {
        super.viewDidLoad()
        navigationItem.renameDelegate = self
    }

    func navigationItem(_ navigationItem: UINavigationItem, didEndRenamingWith: title: String) {
        // Move the file, update the model, and so on.
    }
}
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UIManagedDocument](uimanageddocument.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSFilePresenter](../foundation/nsfilepresenter.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [ProgressReporting](../foundation/progressreporting.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Initializing a document object

- [- initWithFileURL:](<uidocument/init(fileurl_).md>) — Returns a document object initialized with its file-system location.

### Accessing document attributes

- [fileURL](uidocument/fileurl.md) — The file URL you use to initialize the document.
- [localizedName](uidocument/localizedname.md) — The localized name of the document.
- [fileType](uidocument/filetype.md) — The file type of the document.
- [fileModificationDate](uidocument/filemodificationdate.md) — The date and time your app last modified the document file.
- [documentState](uidocument/documentstate.md) — The current state of the document.
- [progress](uidocument/progress.md) — The upload or download progress of a document.

### Writing document data

- [- closeWithCompletionHandler:](<uidocument/close(completionhandler_).md>) — Asynchronously closes the document after saving any changes.
- [- contentsForType:error:](<uidocument/contents(fortype_).md>) — Returns the document data to be saved.
- [- saveToURL:forSaveOperation:completionHandler:](<uidocument/save(to_for_completionhandler_).md>) — Saves document data to the specified location in the application sandbox.
- [- writeContents:andAttributes:safelyToURL:forSaveOperation:error:](<uidocument/writecontents(__andattributes_safelyto_for_).md>) — Ensures that document data is written safely to a specified location in the application sandbox.
- [- writeContents:toURL:forSaveOperation:originalContentsURL:error:](<uidocument/writecontents(__to_for_originalcontentsurl_).md>) — Writes the document data to disk at the sandbox location indicated by a file URL.
- [savingFileType](uidocument/savingfiletype.md) — Returns the file type to use for saving a document.
- [- fileAttributesToWriteToURL:forSaveOperation:error:](<uidocument/fileattributestowrite(to_for_).md>) — Returns a dictionary of file attributes to associate with the document file when writing or updating it.
- [- fileNameExtensionForType:saveOperation:](<uidocument/filenameextension(fortype_saveoperation_).md>) — Returns a file extension to append to the file URL of the document file being written.

### Reading document data

- [- openWithCompletionHandler:](<uidocument/open(completionhandler_).md>) — Opens a document asynchronously.
- [- loadFromContents:ofType:error:](<uidocument/load(fromcontents_oftype_).md>) — Loads the document data into the app’s data model.
- [- readFromURL:error:](<uidocument/read(from_).md>) — Reads the document data in a file at a specified location in the application sandbox.

### Creating new documents

- [CreationIntent](uidocument/creationintent.md) — An app intent that creates new documents for your app.

### Accessing document files asynchronously

- [- performAsynchronousFileAccessUsingBlock:](<uidocument/performasynchronousfileaccess(__).md>) — Schedules a document-reading or document-writing operation on a concurrent background queue.

### Reverting a document

- [- revertToContentsOfURL:completionHandler:](<uidocument/revert(tocontentsof_completionhandler_).md>) — Reverts a document to the most recent document data stored on-disk.

### Disabling and enabling editing

- [- disableEditing](<uidocument/disableediting().md>) — Disables editing when it’s unsafe to make changes to a document.
- [- enableEditing](<uidocument/enableediting().md>) — Enables editing when it’s safe again to make changes to a document.

### Tracking changes and autosaving

- [hasUnsavedChanges](uidocument/hasunsavedchanges.md) — A Boolean value that indicates whether the document has any unsaved changes.
- [- updateChangeCount:](<uidocument/updatechangecount(__).md>) — Updates the change counter by indicating the kind of change.
- [undoManager](uidocument/undomanager.md) — The undo manager for the document.
- [- changeCountTokenForSaveOperation:](<uidocument/changecounttoken(for_).md>) — Returns a change token for a specific save operation.
- [- updateChangeCountWithToken:forSaveOperation:](<uidocument/updatechangecount(withtoken_for_).md>) — Updates the change count with reference to a change-count token passed in by UIKit.
- [- autosaveWithCompletionHandler:](<uidocument/autosave(completionhandler_).md>) — Initiates automatic saving of documents with unsaved changes.

### Supporting user activities

- [userActivity](uidocument/useractivity.md) — An object encapsulating a user activity supported by this document.
- [- restoreUserActivityState:](<uidocument/restoreuseractivitystate(__).md>) — Restores the state needed to continue the given user activity.
- [- updateUserActivityState:](<uidocument/updateuseractivitystate(__).md>) — Updates the state of the given user activity.

### Resolving conflicts and handling errors

- [- handleError:userInteractionPermitted:](<uidocument/handleerror(__userinteractionpermitted_).md>) — Handles an error that occurs during an attempt to read, save, or revert a document.
- [- finishedHandlingError:recovered:](<uidocument/finishedhandlingerror(__recovered_).md>) — Tells UIKit that you finished handling the error.
- [- userInteractionNoLongerPermittedForError:](<uidocument/userinteractionnolongerpermitted(forerror_).md>) — Indicates when it’s no longer safe to proceed without immediately handling the error.

### Constants

- [ChangeKind](uidocument/changekind.md) — Constants that specify the kind of change to a document.
- [SaveOperation](uidocument/saveoperation.md) — Constants that specify the type of save operation.
- [State](uidocument/state.md) — Constants that specify the document state.
- [NSUserActivityDocumentURLKey](uidocument/useractivityurlkey.md) — The key that identifies the document associated with a user activity.

### Notifications

- [UIDocumentStateChangedNotification](uidocument/statechangednotification.md) — A notification the document object posts when there’s a change in the state of the document.

### Structures

- [DidMoveToWritableLocationMessage](uidocument/didmovetowritablelocationmessage.md)
- [StateChangedMessage](uidocument/statechangedmessage.md)

### Type Properties

- [UIDocumentDidMoveToWritableLocationNotification](uidocument/didmovetowritablelocationnotification.md) — A notification that the document posts when copying the file from a readonly location in order to write changes. This notification will be posted on the file presenter queue.
- [UIDocumentDidMoveToWritableLocationOldURLKey](uidocument/didmovetowritablelocationoldurlkey.md) — The key in a `UIDocumentDidMoveToWritableLocationNotification`’s `userInfo` dictionary that contains the previous readonly file URL.

## See Also

### Documents

- [UIManagedDocument](uimanageddocument.md) — A managed document object that integrates with Core Data.
- [Synchronizing documents in the iCloud environment](synchronizing-documents-in-the-icloud-environment.md) — Manage documents across multiple devices to create a seamless editing and collaboration experience.
