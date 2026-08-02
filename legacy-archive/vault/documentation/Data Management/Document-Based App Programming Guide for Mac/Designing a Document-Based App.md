---
title: Document-Based App Programming Guide for Mac
apple_id: TP40011179
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/DocBasedAppProgrammingGuideForOSX/Designing/Designing.html
archived_at: '2026-07-15T07:23:51.679295Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Document-Based App Programming Guide for Mac](About%20the%20Cocoa%20Document%20Architecture.md)


[Next](The%20Classes%20That%20Support%20Document-Based%20Apps.md)[Previous](About%20the%20Cocoa%20Document%20Architecture.md)

# Designing a Document-Based App

Documents are containers for user data that can be stored in files locally and in iCloud. In a document-based design, the app enables users to create and manage documents containing their data. One app typically handles multiple documents, each in its own window, and often displays more than one document at a time. For example, a word processor provides commands to create new documents, it presents an editing environment in which the user enters text and embeds graphics into the document, it saves the document data to disk or iCloud, and it provides other document-related commands, such as printing and version management. In Cocoa, the document-based app design is enabled by a subsystem called the __document architecture__, which is part of of the AppKit [framework](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56).

There are several ways to think of a document. Conceptually, a document is a container for a body of information that can be named and stored in a file. In this sense, the document is an object in memory that owns and manages the document data. To users, the document is their information—such as text and graphics formatted on a page. In the context of Cocoa, a document is an instance of a custom `NSDocument` subclass that knows how to represent internally persistent data that it can display in a window. This document object knows how to read document data from a file and create an object graph in memory for the document [data model](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ModelObject.html#//apple_ref/doc/uid/TP40008195-CH31). It also knows how to modify that data model consistently and write the document data back out to disk. So, the document object mediates between different representations of document data, as shown in Figure 1-1.

__Figure 1-1__  Document file, object, and data model

!

Using iCloud, documents can be shared automatically among a user’s computers and iOS devices. The system synchronizes changes to the document data without user intervention. See [Storing Documents in iCloud](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzzfvbuqmrnknltm) for more information.

The document-based style of app is one design choice among several that you should consider when you design your app. Other choices include single-window utility apps, such as Calculator, and library-style “shoebox” apps, such as iPhoto. It’s important to choose the basic app style early in the design process because development takes quite different paths depending on that choice. If it makes sense for your users to create multiple discrete sets of data, each of which they can edit in a graphical environment and store in files, then you should plan to develop a document-based app.

The Cocoa document architecture provides a framework for document-based apps to do the following things:

- __Create new documents.__ The first time the user chooses to save a new document, it presents a dialog in which the user names and saves the document in a disk file in a user-chosen location.
- __Open existing documents stored in files.__ A document-based app specifies the types of document files it can read and write, as well as read-only and write-only types. It can represent the data of different document types internally and display the data appropriately.
- __Automatically save documents.__ Document-based apps can adopt autosaving in place, and its documents are automatically saved at appropriate times so that the data the user sees on screen is effectively the same as that saved on disk. Saving is done safely, so that an interrupted save operation does not leave data inconsistent. To avoid automatic saving of inadvertent changes, old files are locked from editing until explicitly unlocked by the user.
- __Asynchronously read and write document data.__ Reading and writing are done asynchronously on a background thread, so that lengthy operations do not make the app’s user interface unresponsive. In addition, reads and writes are coordinated using the `NSFilePresenter` [protocol](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45) and the `NSFileCoordinator` class to reduce version conflicts.
- __Manage multiple versions of documents.__ Autosave creates versions at regular intervals, and users can manually save a version whenever they wish. Users can browse versions and revert the document’s contents to a chosen version using a Time Machine–like interface. The version browser is also used to resolve version conflicts from simultaneous iCloud updates.
- __Print documents.__ Users can specify various page layouts in the print dialog and page setup dialog.
- __Track changes and set the document’s edited status.__ The document manages its edited status and implements multilevel undo and redo.
- __Validate menu items.__ The document enables or disables menu items automatically, depending on its edited status and the applicability of the associated action methods.
- __Handle app and window delegation.__ [Notifications](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Notification.html#//apple_ref/doc/uid/TP40008195-CH35) are sent and [delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) methods called at significant life cycle events, such as when the app terminates.

Cocoa’s document architecture implements most of its capabilities in three classes. These classes interoperate to provide an extensible app infrastructure that makes it easy for you to create document-based apps. Table 1-1 briefly describes these classes.

__Table 1-1__  Primary classes in the document architecture

| Class | Purpose |
| `NSDocument` | Creates, presents, and stores document data |
| `NSWindowController` | Manages a window in which a document is displayed |
| `NSDocumentController` | Manages all of the document objects in the app |

See [The Classes That Support Document-Based Apps](The%20Classes%20That%20Support%20Document-Based%20Apps.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzzfvbuqmznknlte) for more detailed information.

The iCloud storage technology enables you to share documents and other app data among multiple computers that run your document-based app. If you have a corresponding iOS version of your app, you can share your documents and app data with your iOS devices as well. Once your app sets up the proper connections, iCloud automatically pushes documents and changes to all the devices running an instance of your app with no explicit user intervention.

There are two kinds of storage in iCloud: document storage and key-value data storage. Document storage is designed for storing large amounts of data such as that in a document file. Key-value storage is designed for small amounts of app data such as configuration data. For example, you might store the text and illustrations for a book in document storage, and you might store the reader’s page location in key-value storage. That way, whenever the user opens the document on any device, the correct page is displayed.

Documents and key-value data designated for storage in iCloud are transferred to iCloud and to the user’s other computers as soon as possible. On iOS devices, only file metadata is transferred from iCloud to devices as soon as possible, while the file data itself is transferred on demand. Once data has been stored initially in iCloud, only changes are transferred thereafter, to make synchronization most efficient.

`NSDocument` implements file coordination, version management, and conflict resolution among documents, so it provides the easiest path to using iCloud. For details explaining how to handle document storage in iCloud, see [Moving Document Data to and from iCloud](Creating%20the%20Subclass%20of%20NSDocument.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzzfvbuqnbnknlte).

The document architecture helps document-based apps adopt App Sandbox, an access control technology that provides a last line of defense against stolen, corrupted, or deleted user data if malicious code exploits your app. The `NSDocument` class automatically works with Powerbox to make items available to your app when the user opens and saves documents or uses drag and drop. `NSDocument` also provides support for keeping documents within your sandbox if the user moves them using the Finder. For more information about App Sandbox, see _[App Sandbox Design Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183)_.

Your document data model is an object or graph of interconnected objects that contain the data displayed and manipulated by your document objects.

The Cocoa document architecture and many other technologies throughout Cocoa utilize the [Model-View-Controller](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MVC.html#//apple_ref/doc/uid/TP40008195-CH32) (MVC) design pattern. Model objects encapsulate the data specific to an app and manipulate and process that data. View objects display data from the app’s model objects and enable the editing of that data by users. Controller objects act as intermediaries between the app’s view objects and model objects. By separating these behaviors into discrete objects, your app code tends to be more reusable, the object interfaces are better defined, and your app is easier to maintain and extend. Perhaps most importantly, MVC-compliant app objects fit seamlessly into the document architecture.

A document object is a controller dedicated to managing the objects in the document’s data model. Each document object is a custom subclass of `NSDocument` designed specifically to handle a particular type of data model. Document-based apps are able to handle one or more types of documents, each with its own type of data model and corresponding `NSDocument` subclass. Apps use an information property list file, which is stored in the app’s [bundle](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Bundle.html#//apple_ref/doc/uid/TP40008195-CH4) and named, by default, `<appName>-Info.plist`, to specify information that can be used at runtime. Document-based apps use this property list to specify the document types the app can edit or view. For example, when the `NSDocumentController` object creates a new document or opens an existing document, it searches the property list for such items as the document class that handles a document type, the [uniform type identifier](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/UniformTypeIdentifier.html#//apple_ref/doc/uid/TP40008195-CH60) (UTI) for the type, and whether the app can edit or only view the type. For more information about creating a property list for types of documents, see [Complete the Information Property List](App%20Creation%20Process%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzzfvbuqnrnhe4tonrzhe).

Any objects that are part of the persistent state of a document should be considered part of that document’s model. For example, the Sketch sample app has a subclass of `NSDocument` named `SKTDocument`. Objects of this class have an array of `SKTGraphic` objects containing the data that defines the shapes Sketch can draw, so they form the data model of the document. Besides the actual `SKTGraphic` objects, however, the `SKTDocument` object contains some additional data that should technically be considered part of the model, such as the order of the graphics within the document’s array, which determines the front-to-back ordering of the `SKTGraphic` objects.

Like any document-based app, Sketch is able to write the data from its data model to a file and vice versa. The reading and writing are the responsibility of the `SKTDocument` object. Sketch implements the `NSDocument` data-based writing method that flattens its data model objects into an `NSData` object before writing it to a file. Conversely, it also implements the data-based `NSDocument` reading method to reconstitute its data model in memory from an `NSData` object it reads from one of its document files.

There are three ways you can implement data reading and writing capabilities in your document-based app:

- __Reading and writing native object types.__ `NSDocument` has methods that read and write `NSData` and `NSFileWrapper` objects natively. You must override at least one writing method to convert data from the document model’s internal data structures into an `NSData` object or `NSFileWrapper` object in preparation for writing to a file. Conversely, you must also override at least one reading method to convert data from an `NSData` or `NSFileWrapper` object into the document model’s internal data structures in preparation for displaying the data in a document window. See [Creating the Subclass of NSDocument](Creating%20the%20Subclass%20of%20NSDocument.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzzfvbuqnbnknltc) for more details about document reading and writing methods.
- __Using Core Data.__ If you have a large data set or require a managed object model, you may want to use `NSPersistentDocument` to create a document-based app that uses the Core Data framework. Core Data is a technology for [object graph](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectGraph.html#//apple_ref/doc/uid/TP40008195-CH54) management and persistence. One of the persistent stores provided by Core Data is based on SQLite. Although Core Data is an advanced technology requiring an understanding of Cocoa fundamental design patterns and programming paradigms, it brings many benefits to a document-based app, such as:

  - Incremental reading and writing of document data
  - Data compatibility for apps with iOS and OS X versions

  For more information, see _Core Data Starting Point_.
- __Custom object formats.__ If you need to read and write objects without using `NSData` and `NSFileWrapper`, you can override other `NSDocument` methods to do so, but your code needs to duplicate what `NSDocument` does for you. Naturally, this means your code will have greater complexity and a greater possibility of error.

Using iCloud, a document can be shared between document-based apps in OS X and iOS. However, there are differences between the platforms that you must take into consideration. For an app to edit the same document in iOS and OS X, the document-type information should be consistent. Other cross-platform considerations for document-data compatibility are:

- Some technologies are available on one platform but not the other. For example, if you use rich text format (RTF) as a document format in OS X, it won’t work in iOS because its text system doesn’t have built-in support for rich text format (although you can implement that support in your iOS app).
- The default coordinate system for each platform is different, which can affect how content is drawn. See “Default Coordinate Systems and Drawing in iOS” in _[Drawing and Printing Guide for iOS](../../Drawing%20and%20Printing%20Guide%20for%20iOS/About%20Drawing%20and%20Printing%20in%20iOS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjw)_ for a discussion of this topic.
- If you archive a document’s model object graph, you may need to perform suitable conversions using `NSCoder` methods when you encode and decode the model objects.
- Some corresponding classes are incompatible across the platforms. That is, there are significant differences between the classes representing colors (`UIColor` and `NSColor`), images (`UIImage` and `NSImage`), and Bezier paths (`UIBezierPath` and `NSBezierPath`). `NSColor` objects, for example, are defined in terms of a color space (`NSColorSpace`), but there is no color space class in UIKit.

These cross-platform issues affect the way you store document data in the file that is shared between OS X and iOS as an iCloud document. Both versions of your app must be able to reconstitute a usable in-memory data model that is appropriate to its platform, using the available technologies and classes, without losing any fidelity. And, of course, both versions must be able to convert their platform-specific data model structures into the shared file format.

One strategy you can use is to drop down to a lower-level framework that is shared by both platforms. For example, on the iOS side, `UIColor` defines a `CIColor` property holding a Core Image object representing the color; on the OS X side, your app can create an `NSColor` object from the `CIColor` object using the [colorWithCIColor:](https://developer.apple.com/documentation/appkit/nscolor/1525446-init) class method.

[Next](The%20Classes%20That%20Support%20Document-Based%20Apps.md)[Previous](About%20the%20Cocoa%20Document%20Architecture.md)

