---
title: Uniform Type Identifiers and Custom Document Type Resources
apple_id: DTS40014116
resource_type: QA
platform: iOS|macOS
topic: Data Management
technology: null
published: '2014-01-29'
source_url: https://developer.apple.com/library/archive/qa/qa1796/_index.html
archived_at: '2026-07-18T02:34:45.561710Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1796

# Uniform Type Identifiers and Custom Document Type Resources

## Q:  Where can I find resources about Uniform Type Identifiers and related technologies?

A: There are a number of documents available about Uniform Type Identifiers (UTIs) in the reference library. This Q&A is a starting point to aid developers in locating documents that describe what UTIs are and how they are used. It contains three sections:

- UTI Definition
- UTI Resources
- Classes and Technologies

A uniform type identifier (UTI) is a string that identifies a class of entities with a type. UTIs are typically used to identify the format for files or in-memory data types and to identify the hierarchical layout of directories, volumes or packages. UTIs are used either to declare the format of existing data or to declare formats that your application accepts. For example, applications use UTIs to declare the format for data they place on a pasteboard. Apps also use UTIs to declare the types of files that they are able to open.

- [Cocoa Core Competencies -- Uniform Type Identifier](https://developer.apple.com/library/ios/documentation/general/conceptual/DevPedia-CocoaCore/UniformTypeIdentifier.html)

  This document provides a high-level view of what Uniform Type Identifiers are, how they work and what they are used for. This document is an excellent starting point for learning about UTIs.
- [Uniform Type Identifiers Overview](https://developer.apple.com/library/ios/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_intro/understand_utis_intro.html#//apple_ref/doc/uid/TP40001319)

  Describes UTIs and how to use them.

  This document includes the following chapters:

  - [Uniform Type Identifier Concepts](https://developer.apple.com/library/ios/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_conc/understand_utis_conc.html#//apple_ref/doc/uid/TP40001319-CH202-CHDHIJDE)

    Describes the syntax and usage of UTIs.
  - [Adopting Uniform Type Identifiers](https://developer.apple.com/library/ios/documentation/FileManagement/Conceptual/understanding_utis/understand_utis.tasks/understand_utis_tasks.html#//apple_ref/doc/uid/TP40001319-CH203-BABHCIAC)

    Describes how to adopt UTIs in your applications.
  - [Declaring New Uniform Type Identifiers](https://developer.apple.com/library/ios/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_declare/understand_utis_declare.html#//apple_ref/doc/uid/TP40001319-CH204-SW1)

    Describes how to declare new UTIs in your applications.
- [Uniform Type Identifiers Reference](https://developer.apple.com/library/ios/documentation/Miscellaneous/Reference/UTIRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009257)

  This document is for OS X and iOS application developers that need to create or otherwise manipulate data that may be exchanged with other applications or services. For example, applications often need to be aware of the type of data they handle when:

  - Displaying, or manipulating, files, bundles, or folders
  - Accessing streaming data
  - Copying and pasting between documents or applications
  - Dragging and dropping between applications
- [System-Declared Uniform Type Identifiers](https://developer.apple.com/library/ios/documentation/Miscellaneous/Reference/UTIRef/Articles/System-DeclaredUniformTypeIdentifiers.html#//apple_ref/doc/uid/TP40009259-SW1)

  Provides a list of UTIs that are defined on OS X.
- [UTType Reference](https://developer.apple.com/library/ios/documentation/MobileCoreServices/Reference/UTTypeRef/Reference/reference.html#//apple_ref/doc/uid/TP40008771)

  This document provides information about the C methods that can be used to manipulate UTIs on iOS.
- [Technical Q&A QA1587](https://developer.apple.com/library/ios/qa/qa1587/_index.html#//apple_ref/doc/uid/DTS40012659)

  Provides a set of step-by-step instructions for adding a custom document type and new UTI to an iOS app.

There are technologies that use UTIs as part of their underlying technologies. These include pasteboards and drag-and-drop for example. Below is a list of related documents:

- [UIPasteboard Class Reference](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIPasteboard_Class/Reference.html#//apple_ref/doc/uid/TP40008243)

  The class reference for UIPasteboard.
- [Pasteboard Programming Guide](https://developer.apple.com/library/mac/documentation/cocoa/Conceptual/PasteboardGuide106/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008099)

  This document provides information about pasteboard programming on OS X.
- [NSPasteboard Class Reference](https://developer.apple.com/library/mac/documentation/cocoa/reference/applicationkit/Classes/NSPasteboard_Class/Reference/Reference.html)

  The class reference for NSPasteboard on OS X.
- [NSPasteboardItem Class Reference](https://developer.apple.com/library/mac/documentation/cocoa/Reference/NSPasteboardItem_Class/Reference/Reference.html#//apple_ref/occ/cl/NSPasteboardItem)

  The class reference for NSPasteboardItem on OS X.
- [Drag and Drop Programming Topics](https://developer.apple.com/library/mac/documentation/cocoa/Conceptual/DragandDrop/DragandDrop.html#//apple_ref/doc/uid/10000069i)

  This document provides information about drag and drop programming on OS X.
- [NSDraggingDestination Protocol Reference](https://developer.apple.com/library/mac/documentation/cocoa/Reference/ApplicationKit/Protocols/NSDraggingDestination_Protocol/Reference/Reference.html#//apple_ref/occ/intf/NSDraggingDestination)

  This document provides information about the NSDragDestination protocol available on OS X.
- [NSDraggingInfo Protocol Reference](https://developer.apple.com/library/mac/documentation/cocoa/Reference/ApplicationKit/Protocols/NSDraggingInfo_Protocol/Reference/Reference.html#//apple_ref/occ/intf/NSDraggingInfo)

  This document provides information about the NSDraggingInfo protocol available on OS X.
- [NSDraggingSource Protocol Reference](https://developer.apple.com/library/mac/documentation/cocoa/Reference/ApplicationKit/Protocols/NSDraggingSource_Protocol/Reference/Reference.html#//apple_ref/occ/intf/NSDraggingSource)

  This document provides information about the NSDraggingSource protocol available on OS X.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-01-29 | New document that this document presents a list of resources about Uniform Type Identifiers and custom document type creation. |

