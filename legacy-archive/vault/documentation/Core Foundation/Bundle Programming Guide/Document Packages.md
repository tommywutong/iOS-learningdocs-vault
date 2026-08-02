---
title: Bundle Programming Guide
apple_id: 10000123i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/DocumentPackages/DocumentPackages.html
archived_at: '2026-07-15T07:22:12.200427Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Bundle Programming Guide](Introduction.md)


[Next](Glossary.md)[Previous](Accessing%20a%20Bundle%E2%80%99s%20Contents.md)

# Document Packages

If your document file formats are getting too complex to manage because of several disparate types of data, you might consider adopting a package format for your documents. Document packages give the illusion of a single document to users but provide you with flexibility in how you store the document data internally. Especially if you use several different types of standard data formats, such as JPEG, GIF, or XML, document packages make accessing and managing that data much easier.

Apple does not prescribe any specific structure for document packages. The contents and organization of the package directory are left to you. You are encouraged, however, to create either a flat directory structure or use the framework bundle structure, which involves placing your files in a top-level `Resources` subdirectory. (For more information about the bundle structure of frameworks, see [Framework Bundles](Bundle%20Structures.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2jninedcmbrfvjvomrw).)

To register a document as a package, you must modify the document type information in your application’s [information property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44) (`Info.plist`) file. The `CFBundleDocumentTypes` key stores information about the document types your application supports. For each document package type, include the `LSTypeIsPackage` key with an appropriate value. The presence of this key tells the Finder and Launch Services to treat directories with the given file extension as a package. For more information about `Info.plist` keys, see _[Information Property List Key Reference](../../General/Information%20Property%20List%20Key%20Reference/About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbx)_.

Document packages should always have an extension to identify them—even though that extension may be hidden by the user. The extension allows the Finder to identify your document directory and treat it as a package. You should never associate a document package with a MIME type or 4-byte OS type.

When it is time for your application to create a new document, it can do so in one of two ways:

- Use an [NSFileWrapper](https://developer.apple.com/documentation/foundation/filewrapper) object to create the document package.
- Create the document package manually.

If you are creating a Cocoa application, the `NSFileWrapper` class is the preferred way to create document packages because it ties in with the existing support in [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) for reading and writing your document contents. (The `NSFileWrapper` class is also available in iOS 4.0 and later as part of the Foundation framework.) For information on how to use this class, see _[NSFileWrapper Class Reference](https://developer.apple.com/documentation/foundation/nsfilewrapper)_.

If you are writing a command-line tool or other type of application that does not use the higher-level Objective-C [frameworks](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56) (such as AppKit or UIKit), you can still create document packages manually. The important thing to remember about creating a document package is that it is just a directory. As long as the type of the document package is registered (as described in [Registering Your Document Type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2jninedcmbwfvjvomy)), all you have to do is create a directory with the appropriate filename extension. (The Finder uses the filename extension as its cue to treat the directory as a package.) You can create the directory (and create any files you want to put inside that directory) using the standard BSD file system routines or using the [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager) class in the Foundation framework.

There are several ways to access the contents of a document package. Because a document package is a directory, you can access the document's contents using any appropriate file-system routines. If you use a bundle structure for your document package, you can also use the [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) or [CFBundleRef](https://developer.apple.com/documentation/corefoundation/cfbundle) routines. Use of a bundle structure is especially appropriate for documents that store multiple localizations.

If your document package uses a flat directory structure or contains a fixed set of content files, you might find using file-system routines faster and easier than using `NSBundle` or `CFBundleRef`. However, if the contents of your document can fluctuate, you should consider using a bundle structure and `NSBundle` or `CFBundleRef` to simplify the dynamic discovery of files inside your document.

If you are creating a Cocoa application, you must also remember to customize the way your `NSDocument` subclass loads the contents of the document package. The traditional technique of using the [readFromData:ofType:error:](https://developer.apple.com/documentation/appkit/nsdocument/1515198-readfromdata) and [dataOfType:error:](https://developer.apple.com/documentation/appkit/nsdocument/1515205-data) methods to read and write data are intended for a single file document. To handle a document package, you must use the [readFromFileWrapper:ofType:error:](https://developer.apple.com/documentation/appkit/nsdocument/1515044-readfromfilewrapper) and [fileWrapperOfType:error:](https://developer.apple.com/documentation/appkit/nsdocument/1515089-filewrapperoftype) methods instead. For information about reading and writing document data from your `NSDocument` subclass, see _Document-Based Applications Overview_.

[Next](Glossary.md)[Previous](Accessing%20a%20Bundle%E2%80%99s%20Contents.md)

