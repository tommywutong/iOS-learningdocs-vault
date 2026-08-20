---
title: Document-Based App Programming Guide for iOS
apple_id: TP40011149
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: UIKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/DocumentBasedAppPGiOS/DocumentImplPreflight/DocumentImplPreflight.html
archived_at: '2026-07-15T07:23:58.004425Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Document-Based App Programming Guide for iOS](About%20Document-Based%20Applications%20in%20iOS.md)


[Next](Creating%20a%20Custom%20Document%20Object.md)[Previous](Designing%20a%20Document-Based%20Application.md)

# Document-Based Application Preflight

For most developers, making a document-based application doesn’t require much more effort than making an application that isn’t document based. The basic difference is that you must create a custom subclass of [UIDocument](https://developer.apple.com/documentation/uikit/uidocument) and then manage a document through the phases of its runtime life, including its integration with iCloud storage. This chapter outlines those document-specific tasks performed by most applications and describes the general steps for creating and configuring a document-based application project in iOS.

To create a document-based application, you should complete the following tasks:

- Create a custom subclass of `UIDocument` that provides the UIKit framework with a snapshot of document data and that initializes the document’s model objects from the contents of the document file.

  [Creating a Custom Document Object](Creating%20a%20Custom%20Document%20Object.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqobnknltc) describes the required method overrides and, if document data is to be stored as a file package, explains how to go about using [NSFileWrapper](https://developer.apple.com/documentation/foundation/filewrapper) objects for document data.
- Allow users to create new documents and select and open existing ones. You should also implement the complementary tasks of closing documents and deleting selected documents.

  Note that the follow-on task to creating or opening a document is displaying the document’s content in a view.

  [Creating a New Document](Managing%20the%20Life%20Cycle%20of%20a%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqnbnknltg), [Opening and Closing a Document](Managing%20the%20Life%20Cycle%20of%20a%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqnbnknlte), and [Deleting a Document](Managing%20the%20Life%20Cycle%20of%20a%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqnbnknlti) describe the requirements and procedures for these tasks. These discussions also include examples of managing the display of document data.
- Implement undo management or change tracking to enable the automatic saving of document data (saveless model).

  See [Change Tracking and Undo Operations](Change%20Tracking%20and%20Undo%20Operations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqnjnknltc) for details.
- Put documents—typically those selected by users—into iCloud storage. Also remove documents from iCloud storage when users request this.

  [Moving Documents to and from iCloud Storage](Managing%20the%20Life%20Cycle%20of%20a%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqnbnknltk) discusses these procedures.
- Observe notifications of changes in document state and, if an error occurs, respond appropriately.

  [Monitoring Document-State Changes and Handling Errors](Managing%20the%20Life%20Cycle%20of%20a%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqnbnknltm) describes the general procedure for doing this.
- If conflicts between different versions of a document occur, notify the user and offer ways to resolve the conflicts.

  [Resolving Document Version Conflicts](Resolving%20Document%20Version%20Conflicts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqnrnknltc) describes how to notify users of version conflicts and discusses strategies for resolving these conflicts.

You can also add extra features to your document-based application, such as the capability for printing the document, spell-checking it, or emailing it to others.

If your application has advanced requirements—for example, incremental reading and writing of large document files or dealing with document-data formats other than the supported ones—see _[UIDocument Class Reference](https://developer.apple.com/documentation/uikit/uidocument)_. All of these advanced tasks involve overriding `UIDocument` methods.

When you create the Xcode project for your document-based application, choose a suitable template. (Note that there is no template specifically for document-based applications.) Generally, you want the first view of the application to be one in which users can choose existing documents and create new ones. Because the Master-Detail Xcode template is suitable for this purpose, it is used in the code examples throughout this document. This template gives you an initial table view for the iPhone and a split view for the iPad. Your project should use a storyboard, so be sure to select this option.

Based on the design for your application (see [Designing a Document-Based Application](Designing%20a%20Document-Based%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqmrnknlte)), create the view-controller subclasses that your application requires. All you need are minimally declared header and source files at this point. Then, create the user interface of your application in the project storyboard (or storyboards, if yours is a universal application); associate your custom view controllers with the view-controller placeholders in the storyboard.

Next, you need to configure the project for documents by specifying, in the Xcode target settings, the type or types of the documents that the application knows about.

The most important attribute of a document object in iOS is its file URL ([fileURL](https://developer.apple.com/documentation/uikit/uidocument/1619990-fileurl)). The file URL is important, among other reasons, because it tells iOS which applications understand the document’s format. The file URL ends with an extension (for example, `html`) and this extension is matched with a Uniform Type Identifier (for example, `public.html`). The Uniform Type Identifier (UTI) is the principal identifier of document type. Using the extension, `UIDocument` looks up the document-type UTI (as shown in Figure 2-1) and assigns it to the `fileType` property. Unlike document-based applications in OSX, those in iOS don’t need to associate the `UIDocument` subclass with the document type.

__Figure 2-1__  iOS looking up a document UTI from the extension of its file URL

!

A document-type UTI can be defined by the system; see [System-Declared Uniform Type Identifiers](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/UTIRef/Articles/System-DeclaredUniformTypeIdentifiers.html#//apple_ref/doc/uid/TP40009259) in _[Uniform Type Identifiers Reference](../../Miscellaneous/Uniform%20Type%20Identifiers%20Reference/Introduction%20to%20Uniform%20Type%20Identifiers%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjx)_ for a list of these common identifiers. A document-based application can also define its own proprietary UTI for its documents (and often does). If it does declare a custom UTI, it must also export that UTI to make the operating system aware of it.

To declare a document type in Xcode, start by clicking the Add button in the target’s Info settings and choose Add Document Type from the pop-up menu. Click the triangle next to Untitled to disclose the property fields and add the properties in Table 2-1.

__Table 2-1__  Properties for defining a document type (`CFBundleDocumentTypes`)

| Key | Xcode field | Value and comments |
| `LSItemContentTypes` | Types | An array of UTI strings. Only one is typically specified per document type. |
| `CFBundleTypeName` | Name | An optional name for the document type. |
| `CFBundleTypeIconFiles` | Icon | An array of paths to icon image files in the application bundle. |
| `CFBundleTypeExtensions` | In “Additional document type properties” table. | An array of filename extensions paired with the document UTI. |
| `LSHandlerRank` | In “Additional document type properties” table. | `Owner`, `Alternate`, `None`. (Typically `Owner`). |
| `LSTypeIsPackage` | In “Additional document type properties” table. | If document data is stored in a file package, set this property to `YES`. Otherwise omit. |

For more information about these keys, see [CFBundleDocumentTypes](../../General/Information%20Property%20List%20Key%20Reference/Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgaytmobv) in _[Information Property List Key Reference](../../General/Information%20Property%20List%20Key%20Reference/About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbx)_.

When you have finished entering the properties for a document type, The Document Types area of Xcode should look similar to the example in Figure 2-2.

__Figure 2-2__  Specification of a document type in Xcode

!

An application could have multiple types of documents—for example, a word-processing application could have a type for regular (blank) documents and another type for pre-formatted documents. For each type, you need to go through the procedure given above .

If you define a custom UTI for your documents, you must also export it. To export a document type in Xcode, start by clicking the Add button in the target’s Info settings and choose Add Exported UTI from the pop-up menu. Click the triangle next to Untitled to disclose the property fields and add the properties in Table 2-2.

__Table 2-2__  Properties for exporting a document UTI (`UTExportedTypeDeclarations`)

| Key | Xcode field | Value and comments |
| `UITypeIdentifier` | Identifier | The custom document UTI, a string. |
| `UTTypeConformsTo` | Conforms to | The UTI that the custom document UTI conforms to. If the data representation is a file package, specify `com.apple.package`. |
| `UTTypeDescription` | Description | Description of the exported type (optional). |
| `UTTypeTagSpecification` | In “Additional exported UTI properties” table. | Create an array named `public.filename-extension`. Then add as items all extensions of the document file. |

For more information about these keys, see [CFBundleDocumentTypes](../../General/Information%20Property%20List%20Key%20Reference/Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgaytmobv) in _[Information Property List Key Reference](../../General/Information%20Property%20List%20Key%20Reference/About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbx)_.

When you have finished entering the properties for a document type, The Exported UTIs area of Xcode should look similar to the example in Figure 2-3.

__Figure 2-3__  Exporting a custom document UTI in Xcode

!

[Next](Creating%20a%20Custom%20Document%20Object.md)[Previous](Designing%20a%20Document-Based%20Application.md)

