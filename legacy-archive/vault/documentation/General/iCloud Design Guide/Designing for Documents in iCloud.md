---
title: iCloud Design Guide
apple_id: TP40012094
resource_type: Guide
platform: tvOS|iOS|macOS
topic: General
technology: null
published: '2015-12-17'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/DesigningForDocumentsIniCloud.html
archived_at: '2026-07-15T07:34:35.966735Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iCloud Design Guide](About%20Incorporating%20iCloud%20into%20Your%20App.md)


[Next](https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/DesignForCoreDataIniCloud.html)[Previous](Designing%20for%20Key-Value%20Data%20in%20iCloud.md)

# Designing for Documents in iCloud

Adopting iCloud document storage makes your app’s documents available on all of a user’s devices. A _document_ (based on the [UIDocument](https://developer.apple.com/documentation/uikit/uidocument) class in iOS or the [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) class in OS X) is an assemblage of related data that can be written to disk as a single file or as a file package. A _file package_, in turn, is a directory presented to the user as a single file and made accessible to your app through an [NSFileWrapper](https://developer.apple.com/documentation/foundation/filewrapper) object.

Documents automatically implement most of the behavior expected of iCloud apps. Specifically, a document automatically ensures that local changes are safely coordinated with iCloud-originated changes. It does this by employing a file coordinator ([NSFileCoordinator](https://developer.apple.com/documentation/foundation/nsfilecoordinator)) object and by adopting the file presenter ([NSFilePresenter](https://developer.apple.com/documentation/foundation/nsfilepresenter)) protocol. In OS X v10.8 and later, documents automatically provide open/save/rename UI and functionality; in iOS your app must implement these things. The use of file coordinators and presenters is mandatory when working with iCloud documents.

When you write files and directories to iCloud document storage, the system transfers those items automatically to iCloud and to the user’s other devices. Using iCloud document storage is similar to using the local file system, except for the following requirements:

- Apps must request entitlements to access iCloud container directories, as explained in [Request Access to iCloud Using Xcode Capabilities](iCloud%20Fundamentals%20%28Key-Value%20and%20Document%20Storage%29.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaojufvbuqnrnknltcmy).
- Apps must use iCloud storage APIs to configure and access iCloud container directories and manage files.
- Apps must use file coordination to read and write the contents of files, as explained in `[Using File Coordination to Access Files and Directories](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaojufvbuqmrnknltcny)`.

To understand how iCloud document storage works, it helps to see it in action. Figure 3-1 shows a simplified representation of local storage on a device. In addition to the app’s local data directories, apps can also access any iCloud containers for which they have the proper entitlements. The iCloud containers themselves also live on the device but are in a different part of the file system and must be configured before they can be used. To configure an iCloud container for use, you call the [URLForUbiquityContainerIdentifier:](https://developer.apple.com/documentation/foundation/nsfilemanager/1411653-urlforubiquitycontaineridentifie) method of `NSFileManager` from a background thread (step 1), specifying the container that you want to access. The system configures the container (step 2) and returns the base URL of the container directory. You use that URL to build further URLs to specify files and directories, and you use the URL to create metadata queries to search the container (step 3).

__Figure 3-1__  Data and messaging interactions for iCloud apps

!

When accessing files and directories in a container, iCloud apps are required to use _file coordination_ to do so. File coordination uses _file coordinator_ and _file presenter_ objects to serialize access to files and directories in order to preserve data integrity. File presenters monitor a file and are notified whenever another thread or process takes action on it. All actions on a file must happen through a file coordinator, which coordinates those actions with any interested file presenters. For example, when moving a file from one location to another, the file coordinator notifies any interested file presenters of the new location. And when writing to a file, the file coordinator delays the write operation until all file presenters indicate that it is safe to do so.

Apps that use document objects ([UIDocument](https://developer.apple.com/documentation/uikit/uidocument) in iOS and `NSDocument` in OS X) get file coordination for free. Document objects implement the presenter ([NSFilePresenter](https://developer.apple.com/documentation/foundation/nsfilepresenter)) protocol and use its methods to manage the underlying file or file package. When reading or writing the file contents, document objects also use file coordinators (instances of the [NSFileCoordinator](https://developer.apple.com/documentation/foundation/nsfilecoordinator) class) automatically. If you are not using document objects to access files, you must handle the file coordination yourself. For more information about how to support file coordination in your own objects, see [The Role of File Coordinators and Presenters](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileCoordinators/FileCoordinators.html#//apple_ref/doc/uid/TP40010672-CH11) in _[File System Programming Guide](../../File%20Management/File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_.

The first time your app adds a document’s on-disk representation to an iCloud (ubiquity) container, the system transfers the entire file or file package to the iCloud server, as shown in Figure 3-2. The first step is to send the document’s metadata, which includes information such as the document name, modification date, file size, and file type. This metadata transfer takes place quickly. The second step is to send the document’s data. Sending the document metadata first lets iCloud know quickly that a new document exists. The iCloud server propagates new and changed metadata quickly to all other available devices attached to the same iCloud account. This lets the devices know that a new document is available.

__Figure 3-2__  Transferring a file to iCloud the first time

!!

After a document’s data is on the server, iCloud optimizes future transfers to and from devices. Instead of sending the entire file or file package each time it changes, iCloud sends only the metadata and the pieces that changed. Figure 3-3 shows a visual representation of this incremental upload. As before, the system sends the file metadata first so that iCloud can propagate it to other devices. After sending the metadata, the system uploads only the portions of the document that changed. This optimization reduces iCloud network traffic and reduces the amount of power consumed by the device. You can help this optimization by designing file formats that support incremental transfers, as described in [Design for Network Transfer Efficiency](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaojufvbuqmrnknlts).

__Figure 3-3__  Transferring just the file changes to iCloud

!!

When a new file appears in iCloud, that file must be downloaded to the user’s other devices, as shown in Figure 3-4. For each device, iCloud first sends that document’s metadata so that the device knows of the file’s existence. After that, the timing for retrieving the file data depends on the type of device. In iOS, apps must ask the system (either explicitly or implicitly) to download the file. You implicitly download a file by trying to access that file by using methods in the [NSFileCoordinator](https://developer.apple.com/documentation/foundation/nsfilecoordinator) class, or you explicitly download the file by invoking the [startDownloadingUbiquitousItemAtURL:error:](https://developer.apple.com/documentation/foundation/nsfilemanager/1410377-startdownloadingubiquitousitemat) method in the `NSFileManager` class. A Mac downloads files automatically as soon as it detects them on the server. For this reason, a Mac is sometimes referred to as a “greedy peer.” If your Mac app sees metadata for a new document but the document itself is not yet local, it is likely already being downloaded by the system on your app’s behalf.

__Figure 3-4__  Receiving a file from iCloud for the first time

!!

After downloading a file’s contents the first time, subsequent operations download only the portions of the file that changed, as shown in Figure 3-5. As with all transfers, the first step in the transfer process is to download the updated document metadata for the file. After receiving the metadata, devices automatically pull changes at appropriate times. On iOS devices, changes are pulled at appropriate times, such as when the app that owns the files comes to the foreground. In OS X, changes are pulled immediately.

__Figure 3-5__  Receiving changed data from iCloud

!!

To check the upload or download progress of a file, retrieve the value of the [NSURLUbiquitousItemDownloadingStatusKey](https://developer.apple.com/documentation/foundation/nsurlubiquitousitemdownloadingstatuskey) from the corresponding `NSURL` object. The value of that key tells you whether the file is already local to the device or in the process of being downloaded. You can receive more specific data about the download progress by getting other attributes of the `NSURL` object. For a list of relevant keys, see _[NSURL Class Reference](https://developer.apple.com/documentation/foundation/nsurl)_.

Changes to your app’s documents can arrive from iCloud at any time, so your app must be prepared to handle them. The [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) class in OS X does most of this work for you but in iOS there is more for you to handle explicitly. When implementing your iOS and OS X apps, do the following to make sure your apps handle iCloud changes appropriately:

- _Enable Auto Save._ Apps must enable Auto Save to participate with iCloud.

  In iOS, enable Auto Save by registering with the default [NSUndoManager](https://developer.apple.com/documentation/foundation/undomanager) object or by calling the [updateChangeCount:](https://developer.apple.com/documentation/uikit/uidocument/1619961-updatechangecount) method of [UIDocument](https://developer.apple.com/documentation/uikit/uidocument) at appropriate times. For example, you might call `updateChangeCount:` when a view moves off the screen or your app transitions to the background.

  In OS X, enable Auto Save by overriding the [autosavesInPlace](https://developer.apple.com/documentation/appkit/nsdocument/1515106-autosavesinplace) method of your [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) subclass and returning `YES`.
- __In iOS, actively track a document’s location in the file system.__ Each instance of your iOS app must be prepared for another instance to move, rename, or delete iCloud-based documents. If your app persistently stores a URL or path information to a file or file package, do not assume that the item will still be there the next time you attempt to access it.

  In iOS, employ an [NSMetadataQuery](https://developer.apple.com/documentation/foundation/nsmetadataquery) object, along with file coordination, to actively track the locations of your documents. Early in your app’s launch process, instantiate and configure a metadata query object, start it, and register for its [NSMetadataQueryDidUpdateNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1413406-nsmetadataquerydidupdate) notification. Implement the [presentedItemDidMoveToURL:](https://developer.apple.com/documentation/foundation/nsfilepresenter/1417861-presenteditemdidmove) method and the [presentedItemURL](https://developer.apple.com/documentation/foundation/nsfilepresenter/1414861-presenteditemurl) property to allow your app to respond to pushed changes from iCloud. Refresh your app’s model layer and update your app’s user interface elements as needed.

  For details on using metadata queries, see _[File Metadata Search Programming Guide](../../Carbon/File%20Metadata%20Search%20Programming%20Guide/About%20File%20Metadata%20Queries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnbr)_.
- _In OS X, do not actively track a document’s location in the file system._ The Open and Save dialogs in a document-based Mac app automatically track the locations of iCloud-based documents; you typically _do not_ need to use an `NSMetadataQuery` object. For example, if a user renames or moves a document while working on one device, instances of your app running on other devices automatically pick up those changes by way of the document architecture.
- _In iOS, actively download files when required._ Files in iOS are not automatically downloaded. The initial download of new iCloud-based documents requires your attention and careful design in your app. After you explicitly download such an item, the system automatically downloads changes when it can.

  Consider keeping track of file download status as part of your iOS app’s model layer. Having this information lets you provide a better user experience: you can design your app to not surprise users with long delays when they want to open a document that is not yet local. For each file (or file package) URL provided by your app’s metadata query, the value of the [NSURLUbiquitousItemDownloadingStatusKey](https://developer.apple.com/documentation/foundation/nsurlubiquitousitemdownloadingstatuskey) key tells you whether the file is up to date or whether it is being downloaded. To get the value of this key, call the [getResourceValue:forKey:error:](https://developer.apple.com/documentation/foundation/nsurl/1408874-getresourcevalue) method of `NSURL`. Reading a file that has not been downloaded can take a long time, because the coordinated read operation blocks until the file finishes downloading (or fails to download).

  For a file (or file package) that is not yet local, you can initiate a download explicitly when the user requests it or before if you can anticipate that the file is needed. If the number of files is small and each file is itself relatively small, you might consider actively downloading all files indicated by your metadata query. For each file (or file package) URL provided by the query, make the corresponding item local by calling the `NSFileManager` method [startDownloadingUbiquitousItemAtURL:error:](https://developer.apple.com/documentation/foundation/nsfilemanager/1410377-startdownloadingubiquitousitemat). If you pass this method a URL for an item that is already local, the method performs no work and returns `YES`.
- __In iOS, respond to, and resolve, document version conflicts as needed.__ A conflict arises when two instances of your iOS app, running on two different devices, attempt to change a document. This can happen, for example, if two devices are not connected to the network, a user makes changes on both of them, and then reconnects both devices to the network. Conflicts are reported to your app using [NSFileVersion](https://developer.apple.com/documentation/foundation/nsfileversion) objects. The iOS document architecture manages conflict resolution by nominating a winning `NSFileVersion` object, but it is your iOS app’s responsibility to accept the suggested version or specify a different one. You can rely on this automatic nomination most of the time; however, your app should be prepared to help as needed.

  When an iOS document’s state changes, it posts a [UIDocumentStateChangedNotification](https://developer.apple.com/documentation/uikit/uidocumentstatechangednotification) notification. On receiving this notification, query the document’s [documentState](https://developer.apple.com/documentation/uikit/uidocument/1619982-documentstate) property and check if the value is [UIDocumentStateInConflict](https://developer.apple.com/documentation/uikit/uidocumentstate/uidocumentstateinconflict). If you determine that explicit resolution is needed, resolve the conflict by using the [NSFileVersion](https://developer.apple.com/documentation/foundation/nsfileversion) class. Enlist the user’s help, if necessary; but when possible, resolve conflicts without user involvement. Keep in mind that another instance of your app, running on another device attached to the same iCloud account, might resolve the conflict before the local instance does.

  When done resolving a conflict, be sure to delete any out-of-date document versions; if you don’t, you needlessly consume capacity in the user’s iCloud storage.
- _In OS X, rely on the system to resolve document conflicts._ OS X manages conflict resolution for you when you use documents.
- _In OS X, avoid deadlocks resulting from modal UI elements._ It is possible for a document change to arrive from iCloud while your app is presenting a modal user interface element, such as a printing dialog, for the same document. If that incoming change requires its own modal interface, such as for conflict resolution, your app can deadlock.
- __Always use a file coordinator to access an iCloud file or file package.__ Document objects use file coordinators automatically, which is one of the great benefits of using documents when designing for iCloud.

  A document-based iOS app, however, must use a file coordinator explicitly when operating on a document’s underlying file; that is, when moving, renaming, duplicating, or deleting the file. For these operations, use methods from the [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager) class within the context of a file coordinator writing method. For more information, see [The Role of File Coordinators and Presenters](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileCoordinators/FileCoordinators.html#//apple_ref/doc/uid/TP40010672-CH11) in _[File System Programming Guide](../../File%20Management/File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_.

  Most document-based OS X apps should employ the built-in app-centric document viewing UI that appears when opening or saving documents. Even if your OS X app needs to present documents programmatically to the user, do not programmatically move, rename, or delete documents. It’s up to the user to perform those operations using the Finder, the built-in document renaming UI, or the built-in iCloud “move” menu items in the File menu.
- _Don’t let users unintentionally share information._ Unlike iOS users, OS X users have direct access to the file system. As a result, users can manipulate files and view their contents outside of the confines of your app. When designing your file formats, carefully consider which information your users would not want to share—for example, in an emailed version of the document. Instead of placing such information in your file or file package, store it outside of the `Documents` subdirectory in the iCloud container (see [Figure 1-2](iCloud%20Fundamentals%20%28Key-Value%20and%20Document%20Storage%29.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaojufvbuqnrnknlto)).
- __Make your documents user-manageable, when appropriate.__ Place files in the `Documents` subdirectory of an iCloud container to make them visible to the user and make it possible for the user to delete them individually. Files you place outside of the `Documents` subdirectory are grouped together as “data.” When a user visits System Preferences (OS X) or Settings (iOS), the user can delete content from iCloud. Files that you place outside of the `Documents` subdirectory can be deleted by the user only as a monolithic group.

  The choice of whether or not to use the `Documents` subdirectory depends on your app design. For example, if your app supports a user creating and naming a document, put the corresponding document file in the `Documents` subdirectory. If your app does not let users interact with files as discrete documents, it’s more appropriate to place them outside of the `Documents` subdirectory.

Choices you make in designing your document format can impact network transfer performance for your app’s documents. The most important choice is to be sure to use a file package for your document format.

If you provide versions of your app for iOS and Mac, design your document file format to be cross-platform compatible.

If your document data format consists of multiple distinct pieces, use a file package for your document file format. A _file package_, which you access by way of an [NSFileWrapper](https://developer.apple.com/documentation/foundation/filewrapper) object, lets you store the elements of a document as individual files and folders that can be read and written separately—while still appearing to the user as a single file. The iCloud upload and download machinery makes use of this factoring of content within a file package; only changed elements are uploaded or downloaded.

Register your document file format, and its associated filename extension, in your app’s `Info.plist` [property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/InfoPlist.html#//apple_ref/doc/uid/TP40008195-CH61) file in Xcode. Specifically, use the [CFBundleDocumentTypes](../Information%20Property%20List%20Key%20Reference/Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgaytmobv) key to specify the file formats that your app recognizes and is able to open. Specify both a filename extension and a uniform type identifier (UTI) corresponding to the file contents. The system uses this information to associate file packages to your app, and, in OS X, to display file packages to the user as though they are normal files.

Many document-based apps benefit from maintaining state on a per-document basis. For example, a user of a vector-based drawing app would want each document to remember which drawing tool was most recently used and which element of the drawing was selected.

There are two places you can store document-specific state:

- Within the file package (or flat-file format) for a document. This choice supports keeping the state together with the document if, for example, a user sends it by email.
- Associated with the document but outside of its file package (or file format). This choice supports cases in which a user would not want to share information. But, being outside of the data managed by your document objects, such state is not tracked by a document’s conflict resolution functionality. It is up to you to do so.

Whichever scheme you choose, take care, in an app that supports editing, to never save document state unless document content was edited. Otherwise, you invite trivial and unhelpful conflict scenarios that consume network bandwidth and battery power.

For example, imagine that a user had been editing a long text document on her iPad, working on page 1. A bit later, she opens the document on her iPhone and scrolls to the last page. This badly behaved example app aggressively saves the end-of-document scroll position—even though the user made no other changes. When the user later opens the document on her iPad to resume editing, there is a needless conflict due to scroll position data. The system has marked the document as in conflict ([UIDocumentStateInConflict](https://developer.apple.com/documentation/uikit/uidocumentstate/uidocumentstateinconflict)), and the newer version (automatically nominated as the conflict winner) is the one scrolled to the last page. To be a well-behaved iCloud app, this text editor should have ignored the change in scroll position on the iPhone because the user did not edit the content.

Think through various usage scenarios for your app, and design accordingly to improve user experience. Take care with state like:

- Document scroll position
- Element selection
- Last-opened timestamps
- Table sort order
- Window size (in OS X)

A strategy to consider is to save such state but only when the user has also made a change that deserves saving. In OS X, the built-in Resume feature provides all the state saving behavior that most document-based apps need. If you want additional control, you can take advantage of the [NSChangeDiscardable](https://developer.apple.com/documentation/appkit/nsdocumentchangetype/nschangediscardable) document change type.

Keep the following factors in mind when designing a document file format for iCloud:

- _Employ a cross-platform data representation._ Like-named classes—those whose prefixes are “UI” for iOS and “NS” for OS X—are not directly compatible. This is true for colors ([UIColor](https://developer.apple.com/documentation/uikit/uicolor) and [NSColor](https://developer.apple.com/documentation/appkit/nscolor)), images ([UIImage](https://developer.apple.com/documentation/uikit/uiimage) and [NSImage](https://developer.apple.com/documentation/appkit/nsimage)), and Bezier paths ([UIBezierPath](https://developer.apple.com/documentation/uikit/uibezierpath) and [NSBezierPath](https://developer.apple.com/documentation/appkit/nsbezierpath)), as well as for other classes.

  For example, an OS X `NSColor` object is defined in terms of a color space ([NSColorSpace](https://developer.apple.com/documentation/appkit/nscolorspace)), but there is no color space class in iOS.

  If you employ such a class in a document format property, you must devise an intermediate iCloud representation that you can faithfully reconstitute into the native representation on either platform, as depicted in Figure 3-6. When the [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) object saves its data to disk (step 1), it converts each platform-specific data type to an intermediate cross-platform representation. That cross-platform data is saved to iCloud and downloaded to the user’s other devices (steps 2 and 3). When the iOS version of your app extracts that data (step 4), it converts the data from the cross-platform representation into an iOS-specific version.

  __Figure 3-6__  Using a cross-platform data representation

  !

  When storing a document from your iOS app for later viewing on either platform, you’d reverse the process shown in Figure 3-6—starting by storing your iOS document using a cross-platform data representation.

  For each platform-specific data type you employ in your document format, check if there is an appropriate, lower-level data type shared by both platforms that you can use in the intermediate representation. For example, each color class (`UIColor` and `NSColor`) has an initialization method that lets you create a color object from a Core Image `CIColor` instance.

  When preparing data for writing to iCloud, convert _to_ the intermediate representation; when reading an iCloud-based file, convert _from_ the intermediate representation. If you call methods from [NSCoder](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCoder/Description.html#//apple_ref/occ/cl/NSCoder) or its concrete subclasses to encode and decode your document’s object graph, perform these conversions within those methods.
- _Take platform-specific coordinate systems into account._ The default [screen coordinate systems](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/CoordinateSystem.html#//apple_ref/doc/uid/TP40009071-CH8) in iOS and OS X are different, leading to differences in how you draw and in how you position views. Take this into account when storing and extracting screen coordinate information with your cross-platform representation. For more information, see [Coordinate Systems and Drawing in iOS](../../Drawing%20and%20Printing%20Guide%20for%20iOS/iOS%20Drawing%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjufvjvomju) in _[Drawing and Printing Guide for iOS](../../Drawing%20and%20Printing%20Guide%20for%20iOS/About%20Drawing%20and%20Printing%20in%20iOS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjw)_.
- _Always use case-insensitive filenames._ OS X, by default, and for nearly all users, employs a case-_insensitive_ file system. For example, the file `mydoc.txt` and the file `MyDoc.TXT` cannot both exist within the same directory in OS X. By contrast, iOS treats those filenames as being different.

  To make your document file format cross-platform compatible, you must read and write files in a case-insensitive manner.
- _Use a format version number._ Because you may want to change your document format in the future, design a format version numbering scheme and apply the version number as a property of the document format.

  Versioning your document format has always been a good idea, and with iCloud and cross-platform formats, it’s even more important. For example, an iCloud user is likely to have multiple devices on which to view content; but the user might not conscientiously update your app on all of her devices at once. So, for example, a user’s Mac might have the newest version of your OS X app but his iPad might have a year-old version of your iOS app.

  An early version of your app might be iOS-only; when you later distribute an OS X version, you’ll likely want to modify the document format. By embedding the format version within each document, your code can gracefully handle documents regardless of their version. You might, for example, make an old, iOS-only format read-only in OS X. Think through various scenarios involving multiple devices on each platform, each running a different version of your app. Make sure that you provide the best possible user experience for iCloud-based documents.

For more information about techniques for designing file formats, see [Choosing Types, Formats, and Strategies for Document Data](../../Data%20Management/Document-Based%20App%20Programming%20Guide%20for%20iOS/Designing%20a%20Document-Based%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqmrnknltcmi) in _[Document-Based App Programming Guide for iOS](../../Data%20Management/Document-Based%20App%20Programming%20Guide%20for%20iOS/About%20Document-Based%20Applications%20in%20iOS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbz)_ or [Handling a Shared Data Model in OS X and iOS](../../Data%20Management/Document-Based%20App%20Programming%20Guide%20for%20Mac/Designing%20a%20Document-Based%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzzfvbuqmrnknltcmi) in _[Document-Based App Programming Guide for Mac](../../Data%20Management/Document-Based%20App%20Programming%20Guide%20for%20Mac/About%20the%20Cocoa%20Document%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzz)_.

Table 3-1 lists some typical workflows for document-based apps. For each workflow, the table lists the primary classes you typically use, along with a brief description of the task.

__Table 3-1__  Typical document-based app workflows

| Workflow | Implementation | Description |
| Create a new standard document | [UIDocument](https://developer.apple.com/documentation/uikit/uidocument) (iOS)  [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) (OS X) | Use a document object to create and manage the data structures in your document format. The document classes automatically support saving new documents to an iCloud container or to local storage. |
| Create a new Core Data document | [UIManagedDocument](https://developer.apple.com/documentation/uikit/uimanageddocument) (iOS)  [NSPersistentDocument](https://developer.apple.com/documentation/appkit/nspersistentdocument) (OS X) | Use the Core Data document subclasses to create and manage your Core Data stores. For details, see [Designing for Core Data in iCloud](https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/DesignForCoreDataIniCloud.html#//apple_ref/doc/uid/TP40012094-CH3-SW1). |
| Obtain URLs to iCloud documents | [NSMetadataQuery](https://developer.apple.com/documentation/foundation/nsmetadataquery) (iOS)  Automatic (OS X) | In iOS, use a metadata query object to locate and obtain live-updated information on iCloud documents.  In OS X v10.8 or later, a document Open dialog uses a metadata query automatically. |
| Prompt the user to open a document. | Custom UI (iOS)  Automatic as part of the document architecture (OS X) | In iOS, your app is directly responsible for presenting a selection UI for user documents in a simple and clean way that fits well with the rest of the app design.  In OS X v10.8 or later, the Open command in a document-based app presents a dialog that lets the user select iCloud files. |
| Handle version conflicts | [UIDocument](https://developer.apple.com/documentation/uikit/uidocument), [NSFileVersion](https://developer.apple.com/documentation/foundation/nsfileversion) (iOS)  Automatic (OS X) | In iOS, documents detect and notify you about conflicts. Use `NSFileVersion` objects (one per revision of a document) to resolve them, as needed. |
| Move, duplicate, and delete iCloud-based documents | [NSFileCoordinator](https://developer.apple.com/documentation/foundation/nsfilecoordinator)  [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager) | Manipulate files on disk using the `NSFileManager` class, and always within the context of a file coordinator object. |

For details on how to perform the preceding workflows, look in the document-based programming guide for the platform you are targeting. For iOS, see _[Document-Based App Programming Guide for iOS](../../Data%20Management/Document-Based%20App%20Programming%20Guide%20for%20iOS/About%20Document-Based%20Applications%20in%20iOS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbz)_. For Mac, see _[Document-Based App Programming Guide for Mac](../../Data%20Management/Document-Based%20App%20Programming%20Guide%20for%20Mac/About%20the%20Cocoa%20Document%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzz)_.

To store your documents in iCloud Drive, enable iCloud in the Capabilities pane and add the `NSUbiquitousContainers` key to the `Info.plist` file.

To specify your app’s containers, set the `NSUbiquitousContainers` key to your app’s container IDs. Also, specify how you want to share each container using other `NSUbiquitous…` keys.

```
<key>NSUbiquitousContainers</key>
    <dict>
        <key>iCloud.com.example.MyApp</key>
        <dict>
            <key>NSUbiquitousContainerIsDocumentScopePublic</key>
            <true/>
            <key>NSUbiquitousContainerSupportedFolderLevels</key>
            <string>Any</string>
            <key>NSUbiquitousContainerName</key>
            <string>MyApp</string>
        </dict>
    </dict>
```

These settings allow iCloud Drive to provide public access to the files stored in your app’s container. iCloud Drive will create a folder for your app in the user’s iCloud Drive folder to store these documents. For a detailed description of `NSUbiquitous…` keys, see [Cocoa Keys](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251) in _[Information Property List Key Reference](../Information%20Property%20List%20Key%20Reference/About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbx)_.

[Next](https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/DesignForCoreDataIniCloud.html)[Previous](Designing%20for%20Key-Value%20Data%20in%20iCloud.md)

