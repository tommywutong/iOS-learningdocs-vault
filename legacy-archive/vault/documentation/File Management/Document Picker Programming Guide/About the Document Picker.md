---
title: Document Picker Programming Guide
apple_id: TP40014451
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: UIKit
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/DocumentPickerProgrammingGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:31:55.721671Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Accessing%20Documents.md)

# About the Document Picker

The document picker feature lets users select documents from outside your app’s sandbox. These include documents stored in iCloud Drive and documents provided by a third-party extension. Users can open these documents directly, editing them in place. This access simplifies sharing documents between apps and enables more complex workflows. For example, users can easily edit a single document using multiple apps.

![../Art/Document Picker_2x.png](../Art/Document Picker_2x.png)

The document picker feature give users an unprecedented amount of freedom when it comes to accessing and sharing their documents.

### The Document Picker Enables Sharing Documents Between Apps

The document menu view controller displays a list of document providers available on the device. Each provider grants access to a container outside your app’s sandbox. For example, iCloud Drive lets users reach into the public iCloud container or into another app’s iCloud container and access the files stored there.

The document picker view controller lets your app _import_ or _open_ files from a particular document provider, uploading and downloading local copies as needed. Apps can also _export_ or _move_ their own documents into these external storage areas.

### Sharing Documents Introduces Added Complexity that Your App Must Handle

Many of these sharing operations let users interact with their documents in radically new ways. As a result, users have greater flexibility when it comes to working with their documents. Because this flexibility also introduces additional complexity, your app needs to be able to handle these additional complications with grace and poise.

### Enabling iCloud Drive Support Provides Access to Your Documents

If you want to let other apps access files stored in your iCloud container, you must enable iCloud Drive support. To learn how to do this, see [Enabling Document Storage in iCloud Drive](../../General/iCloud%20Design%20Guide/Designing%20for%20Documents%20in%20iCloud.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaojufvbuqmrnknltema).

Before your app can use the document picker, you must turn on the iCloud Documents capabilities in Xcode. For more information about iCloud Documents, see [Designing for Documents in iCloud](https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/DesigningForDocumentsIniCloud.html#//apple_ref/doc/uid/TP40012094-CH2).

![../Art/Enabling iCloud Documents_2x.png](../Art/Enabling iCloud Documents_2x.png)

_Import_ and _export_ operations simply make copies of existing files. They are relatively easy to use and require only standard app development skills: working with the file system, reading and writing documents, and presenting view controllers.

In contrast, _open_ and _move_ operations introduce a considerable amount of complexity. These operations allow you to access resources outside your app’s sandbox, and more than one process may attempt to read or write to these files concurrently. Before implementing one of these options, familiarize yourself with file coordinators, file presenters, and security-scoped URLs.

For more information about security-scoped URLs, see Bookmarks, Security Scope, and Start/Stop Semantics.

For more information about file coordinators and file presenters, see [The Role of File Coordinators and Presenters](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileCoordinators/FileCoordinators.html#//apple_ref/doc/uid/TP40010672-CH11) in _[File System Programming Guide](../File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_.

If you would like additional information on creating your own Document Provider extensions, see [Document Provider](../../General/App%20Extension%20Programming%20Guide/FileProvider.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjufvbuqmjy) in _[App Extension Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214)_

[Next](Accessing%20Documents.md)

