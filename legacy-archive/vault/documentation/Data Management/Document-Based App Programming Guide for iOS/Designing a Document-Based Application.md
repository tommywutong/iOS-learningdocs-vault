---
title: Document-Based App Programming Guide for iOS
apple_id: TP40011149
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: UIKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/DocumentBasedAppPGiOS/DocumentArchitectureiniOS/DocumentArchitectureiniOS.html
archived_at: '2026-07-15T07:23:57.163190Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Document-Based App Programming Guide for iOS](About%20Document-Based%20Applications%20in%20iOS.md)


[Next](Document-Based%20Application%20Preflight.md)[Previous](About%20Document-Based%20Applications%20in%20iOS.md)

# Designing a Document-Based Application

The [UIDocument](https://developer.apple.com/documentation/uikit/uidocument) class, introduced in iOS 5.0, plays the principal role in document-based applications for iOS. It is an abstract base class—meaning that for you to have something useful, you must create a subclass of it that is tailored to the needs of your application. The application-specific code that you add to the subclass augments what `UIDocument` makes possible: efficient behavior of documents in a mobile environment integrated with iCloud storage.

When you have an idea for any application and sit down to design it, you must evaluate a multitude of options. What style of application should you use (master-detail, page-based utility, OpenGL game, and so on)? Will the application do its own drawing, will it respond to gestures or touch events, and will it incorporate audiovisual assets? What will the data model be—for example, should the application use [Core Data](https://developer.apple.com/library/archive/documentation/DataManagement/Devpedia-CoreData/coreDataOverview.html#//apple_ref/doc/uid/TP40010398-CH28)? The decision whether to make your application document-based might seem to complicate that series of choices, but it really boils down to how you anticipate people will use your application.

Document-based applications are ideal, even necessary, when users expect to enter and edit content in a visual container and store that content under a name they specify. Each container of information—a document—is unique. You are no doubt familiar with several types of document-based applications found in both desktop and mobile systems. To name a few, there are word processors, spreadsheets, and drawing programs. With the iCloud technology, you have an even more compelling reason to make your application document-based. Your users, for example, could create a document using your application on a OS X desktop system and then later, without having to do any syncing or copying, edit that document on an iPad using the iOS version of your application. This feature gives them an additional incentive to buy your application.

When you adopt the `UIDocument` approach to document-based applications, your application gets a lot of behavior “for free” or with minimal coding effort on your part.

- __Integration with iCloud storage.__ The `UIDocument` object coordinates all reading and writing of document data from and to iCloud storage. It does this by adopting the [NSFilePresenter](https://developer.apple.com/documentation/foundation/nsfilepresenter) [protocol](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45) and by calling methods of the [NSFileCoordinator](https://developer.apple.com/documentation/foundation/nsfilecoordinator) and [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager) classes.
- __Background writing and reading of document data.__ If your application reads and writes a document synchronously, it can become momentarily unresponsive. The `UIDocument` object avoids this problem by reading and writing document data asynchronously on a background dispatch queue.
- __Saveless model.__ In the saveless model, a user of a document-based application rarely has to save documents explicitly; The `UIDocument` object saves document data automatically at intervals optimized for what the user is doing with the document. You make your document-based application “saveless” by implementing undo management or change tracking (see [Change Tracking and Undo Operations](Change%20Tracking%20and%20Undo%20Operations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqnjnknltc) for information).
- __Safe saving.__ The `UIDocument` object saves document data safely; consequently, if some external event interrupts a save operation, document data won’t be left in an inconsistent state. The object implements safe saving by first writing the newest version of a document to a temporary file and then replacing the current document file with it.
- __Support for handling errors and version conflicts.__ When the `UIDocument` object detects a conflict between different versions of a document, it notifies the application. The application can then attempt to resolve the conflict itself, or it can ask the user to pick the desired document version. The `UIDocument` object also notifies an application when a save operation does not succeed. [Managing the Life Cycle of a Document](Managing%20the%20Life%20Cycle%20of%20a%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqnbnknltc) describes how to observe these notifications; [Resolving Document Version Conflicts](Resolving%20Document%20Version%20Conflicts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqnrnknltc) discusses strategies for dealing with document-version conflicts.

Although the broad definition of a document is a “container of information,” that container can be viewed in several ways. To a user, a document is the text, images, shapes, and other forms of information that he or she creates, edits, and saves under a unique name. A document can also refer to a document file: the persistent, on-disk representation of document data. And a document can mean a `UIDocument` object that represents and manages the in-memory representation of that same data.

A document object also plays a key role in converting document data between its representation on disk to its representation in memory. It cooperates with the `UIDocument` class in the writing of document data to a file and the reading of that data. For writing, a document typically provides a snapshot of data that can be written to the document file; for reading, it receives data and [initializes](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21) the document’s model objects with it. A document, in a sense, is a conduit between data stored in a file and the internal representation of that data. Figure 1-1 illustrates these relationships.

__Figure 1-1__  Document file, document object, and model objects managed by the document object

!

In iCloud, files reside locally in a container directory that is associated with an application. That directory has an internal structure that includes, most importantly, a `Documents` subdirectory. In the iCloud scheme, files and file packages written to the `Documents` subdirectory are considered document files—even if they don’t originate from document-based applications. Files that are written to other locations in the container directory are considered data files.

Document objects are file presenters because the `UIDocument` class adopts the [NSFilePresenter](https://developer.apple.com/documentation/foundation/nsfilepresenter) [protocol](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45). A file presenter is used together with [NSFileCoordinator](https://developer.apple.com/documentation/foundation/nsfilecoordinator) objects to coordinate access to a file or directory among the objects of an application and between an application and other processes. A file presenter is involved in other clients’ access of the same presented file or directory.

When users ask to store document files in iCloud storage, a document-based application should save those files (including file packages) in the `Documents` subdirectory of the iCloud container directory. See [Managing the Life Cycle of a Document](Managing%20the%20Life%20Cycle%20of%20a%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqnbnknltc) for specifics. For more information about iCloud mobile containers, see _[iCloud Design Guide](../../General/iCloud%20Design%20Guide/About%20Incorporating%20iCloud%20into%20Your%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaoju)_.

A document object has several defining properties, most of which relate to its role as a manager of document data. These properties are declared by the `UIDocument` class.

- __File URL.__ A document must have a location where it can be stored, whether that location is in the local file system or in iCloud storage. The [fileURL](https://developer.apple.com/documentation/uikit/uidocument/1619990-fileurl) [property](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13) identifies this location. When you create a `UIDocument` object, you must specify a file URL as the parameter of the [initWithFileURL:](https://developer.apple.com/documentation/uikit/uidocument/1619979-initwithfileurl) initializer method of `UIDocument`.
- __Document name.__ A `UIDocument` object obtains a default document name from the filename component of the file URL and stores it in the [localizedName](https://developer.apple.com/documentation/uikit/uidocument/1619959-localizedname) property. You can override the [getter method](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/AccessorMethod.html#//apple_ref/doc/uid/TP40008195-CH2) of this property to provide a custom, localized document name.
- __File type.__ The file type is a [Uniform Type Identifier](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/UniformTypeIdentifier.html#//apple_ref/doc/uid/TP40008195-CH60) (UTI) derived from the extension of the file URL and assigned to the [fileType](https://developer.apple.com/documentation/uikit/uidocument/1619992-filetype) property. For more information, see [How iOS Identifies Your Application’s Documents](Document-Based%20Application%20Preflight.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqmznknltq).
- __Modification date.__ The date the document file was last modified. This value is stored in the [fileModificationDate](https://developer.apple.com/documentation/uikit/uidocument/1619952-filemodificationdate) property. It can be use for (among other things) resolving document-version conflicts.
- __Document state.__ A document is in one of several possible states during its runtime life. These states can indicate, for example, that there was an error in saving the document or that there are conflicting document versions. `UIDocument` stores the current document state in the [documentState](https://developer.apple.com/documentation/uikit/uidocument/1619982-documentstate) property. For information about observing changes in document state, see [Monitoring Document-State Changes and Handling Errors](Managing%20the%20Life%20Cycle%20of%20a%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqnbnknltm).

Before you write a line of code for your document-based application, it’s worth your while to think about a few design issues.

As with all applications, you should devise an overall design for the objects of your document-based application that is based on the [Model-View-Controller](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MVC.html#//apple_ref/doc/uid/TP40008195-CH32) design pattern (MVC). Although the following MVC design for documents is recommended, you are free to come up with your own object-relationship designs.

In MVC terms, a document is a model [controller](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11); it “owns” and manages the model objects that represent the document’s content. The document object itself is owned and managed by a view controller. The view controller, by definition, also manages a view that presents the content managed by the document object. It is thus a mediating controller in this network of relationships, obtaining the data it needs to present in the view from the document object and passing data entered or changed by users to the document object. Figure 1-2 depicts these object relationships.

__Figure 1-2__  A view controller manages both a document object and the view that presents document data

!

Just as a view controller embeds its view, a view controller might embed the document object as a [declared property](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13). When your application instantiates the view controller, it initializes it with the document object or with the document’s file URL (from which the view controller itself can create the document object).

Of course, a document-based application will have other view controllers (with their views) and possibly other model objects. To get an idea of what other view controllers might be required, see [Designing the User Interface](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqmrnknltc).

Neither UIKit nor the developer tools provide any support for the user interface of a document-based application. For instance, there is no `UIDocumentView` class or `UIDocumentViewController` class and there is no standard interface for selecting documents. Rather than regret the absence, take it as an opportunity to create a user interface for your document-based application that makes it stand out from the competition.

Nonetheless, all document-based applications should enable their users to do certain things that require user interface elements; these include the following:

- Viewing and editing a document
- Creating a new document
- Selecting a document from a list of documents owned by the application
- Opening, closing, and deleting a selected document
- Putting a selected document in iCloud storage (and removing a selected document from iCloud storage)
- Indicating error conditions, including document-version conflicts
- Undoing and redoing changes (recommended but not required)

When you design your application, be sure to include the view controllers, views, and controls that are necessary to implement these actions.

When designing the data model for your document-based application, it’s critical that you ask and answer the following questions:

__What is the type of my document?__

A document must have a document type, a collection of information that characterizes the document and associates it with an application. A document type has a name, an icon (optional), a handler rank, and a Uniform Type Identifier (UTI) that is paired with one or more filename extensions. For an application to edit the same document in iOS and in OS X, the document-type information should be consistent.

[Creating and Configuring the Project](Document-Based%20Application%20Preflight.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqmznknlte) explains how to specify document types in a document-based iOS application. See _[Uniform Type Identifiers Overview](../../File%20Management/Uniform%20Type%20Identifiers%20Overview/Introduction%20to%20Uniform%20Type%20Identifiers%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmjz)_ for a description of UTIs and _[Uniform Type Identifiers Reference](../../Miscellaneous/Uniform%20Type%20Identifiers%20Reference/Introduction%20to%20Uniform%20Type%20Identifiers%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjx)_ for descriptions of common Uniform Type Identifiers.

__How should I represent the document data that is written to a file?__

You have basically three choices:

- __Core Data (database).__ [Core Data](https://developer.apple.com/library/archive/documentation/DataManagement/Devpedia-CoreData/coreDataOverview.html#//apple_ref/doc/uid/TP40010398-CH28) is a technology and framework for [object-graph](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectGraph.html#//apple_ref/doc/uid/TP40008195-CH54) management and persistence. It can use the built-in SQLite data library as a database system. The [UIManagedDocument](https://developer.apple.com/documentation/uikit/uimanageddocument) class, a subclass of `UIDocument`, is intended for document-based applications that use Core Data.
- __Supported object formats.__ `UIDocument` supports the [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) and [NSFileWrapper](https://developer.apple.com/documentation/foundation/filewrapper) objects as native types for document-data representation. `NSData` is intended for flat files, and `NSFileWrapper` is intended for file packages, which are directories that iOS treats as a single file. If you give `UIDocument` one of these objects, it saves it to the file system without further involvement on your part.
- __Custom object formats.__ If you want the document data written to a file to be of a type other than `NSData` or `NSFileWrapper`, you can write it to the file yourself in an override of a specific `UIDocument` method. Keep in mind that your code will have to duplicate what `UIDocument` does for you, and so you must deal with greater complexity and a greater possibility of error. See _[UIDocument Class Reference](https://developer.apple.com/documentation/uikit/uidocument)_ for further information.

__Why would I want to store my document data in a database instead of a file?__

If the data set managed by your document object is primarily a large object graph but your application uses only a subsection of that graph at any time, then `UIManagedDocument` and Core Data are a good option. Core Data brings many benefits to a document-based application:

- Incremental reading and writing of document data
- Support for undo and redo operations
- Automatic support for resolving document-version conflicts
- Data compatibility for cross-platform applications

The “downside” to Core Data is that it is a complex technology; it takes time to become familiar with its concepts, classes, and techniques. To learn more, read _[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_ and _[UIManagedDocument Class Reference](https://developer.apple.com/documentation/uikit/uimanageddocument)_.

__Which of the supported object formats (NSData or NSFileWrapper) is best for my application?__

Whether you use an [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) or [NSFileWrapper](https://developer.apple.com/documentation/foundation/filewrapper) object for document data depends on how complex that data is and on whether part of your document’s model-object graph can be written out separately to a file. For example, if your document data is plain text and nothing else, then `NSData` is a suitable container for it. If, however, the data has multiple components—for example, text _and_ images—use `NSFileWrapper` methods to create a file package for the data.

File wrapper objects—and file packages which they represent—offer some advantages over binary data objects.

- File wrappers support incremental saving. In contrast with a single binary data object, if a file wrapper contains your document data—for example, text and an image—and the text changes, only the file containing the text has to be written out to disk. This capability results in better performance.
- File wrappers (and file packages) make it easier to version documents. A file package, for example, can contain a property list file that holds version information and other metadata about a document.

[Storing Document Data in a File Package](Creating%20a%20Custom%20Document%20Object.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqobnknlte) discusses (and illustrates) how you use an `NSFileWrapper` object to represent document data in a form that can be written out as a file package.

__Can I archive my model-object graph and have that NSData object written to the document file?__

Yes, that is possible, but some of the caveats previously mentioned apply. If any part of your document’s model-object graph can be written to a separate file, don’t archive that part. Instead, store the `NSData` archive and the partitioned-out items as separate components of a file package.

__What if my document file is very large?__

If the data stored in a document file can be large, you might have to write and read the data incrementally to ensure a good user experience. There are a few approaches you might take:

- Use `UIManagedDocument`. Remember, Core Data gives you incremental reading and writing “for free.”
- Store the separable components of your document data in a file package.
- Override lower-level methods of `UIDocument` and do the incremental reading and writing of data yourself. (See _[UIDocument Class Reference](https://developer.apple.com/documentation/uikit/uidocument)_ for particulars.) You should always use an API for incremental reading and writing that is appropriate to the data type; for example, the AV Foundation framework has methods for incremental reading of large multimedia files.

__What should I be thinking about if I want my documents to be editable on both platforms?__

Your application will have a competitive advantage if your users can create and edit documents both on iOS mobile devices (iPhone, iPad, and iPad touch) and on OS X desktop systems. But for this to be possible, the format of the document data on both platforms should be compatible. Some important considerations for document-data compatibility are:

- Some technologies are available on one platform but not the other. For example, if you’re using RTF as a document format in OS X, that format won’t work in iOS because its text system doesn’t support rich text.
- The corresponding classes in each platform are not compatible. This is especially true with colors ([UIColor](https://developer.apple.com/documentation/uikit/uicolor) and [NSColor](https://developer.apple.com/documentation/appkit/nscolor)), images ([UIImage](https://developer.apple.com/documentation/uikit/uiimage) and [NSImage](https://developer.apple.com/documentation/appkit/nsimage)), and Bezier paths ([UIBezierPath](https://developer.apple.com/documentation/uikit/uibezierpath) and [NSBezierPath](https://developer.apple.com/documentation/appkit/nsbezierpath)). `NSColor` objects, for example, are defined in terms of a color space ([NSColorSpace](https://developer.apple.com/documentation/appkit/nscolorspace)), but there is no color space class in UIKit.

  If you define a document property with one of these classes, you must devise a way (when preparing the document data for writing) to convert the property into a form that can be accurately reconstituted on the other platform. One way to do this is to “drop down” to a lower-level framework that is shared by both platforms. For example, `UIColor` defines a `CIColor` property holding a Core Image object representing the color; on the OS X side, your application can create an `NSColor` object from the [CIColor](https://developer.apple.com/documentation/uikit/uicolor/1621951-cicolor) object using the [colorWithCIColor:](https://developer.apple.com/documentation/appkit/nscolor/1525446-init) class method.
- The default coordinate system for each platform is different, and this difference can affect how content is drawn. (See [Coordinate Systems and Drawing in iOS](../../Drawing%20and%20Printing%20Guide%20for%20iOS/iOS%20Drawing%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjufvjvomju) in _[Drawing and Printing Guide for iOS](../../Drawing%20and%20Printing%20Guide%20for%20iOS/About%20Drawing%20and%20Printing%20in%20iOS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjw)_ for a discussion of this topic).
- If you archive a document’s model-object graph, partially or entirely, then you might have to perform platform-sensitive conversions using [NSCoder](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCoder/Description.html#//apple_ref/occ/cl/NSCoder) methods when you encode and decode the model objects.

[Next](Document-Based%20Application%20Preflight.md)[Previous](About%20Document-Based%20Applications%20in%20iOS.md)

