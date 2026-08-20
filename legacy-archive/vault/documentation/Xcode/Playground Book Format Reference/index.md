---
title: Playground Book Format Reference
apple_id: TP40017343
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2018-04-30'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/swift_playgrounds_doc_format/index.html
archived_at: '2026-07-27T06:57:10.607746Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)



## Playground Book Package

> [!IMPORTANT]

With the playground book package format, you can create a document that includes features such as playground pages, live views containing iOS views, and animated cutscenes. Figure 1-1 shows a screenshot from Learn to Code 1.

__Figure 1-1__Learn to Code 1
（原归档配图获取待重试：`SP_learn_to_code_2x.png`）

### Content Hierarchy

A playground book is a _package_—a type of document with a file and folder structure. The parts of a book package form a nested hierarchy of folders. At the top is the book, then the chapters, and finally the individual pages and their content. The books, chapters, and pages include manifest information and optional items shared between the book, chapter, or page. Figure 1-2 shows the general hierarchy of files and folders for the playground book package format.

__Figure 1-2__Package folder hierarchy
（原归档配图获取待重试：`SP_package_format_2x.png`）

The package format uses a combination of folder name extensions, specially named folders, and specially named files. Manifest files for a book, and for each chapter and page, contain configuration information such as the order of chapters or the name of a page.

### Folder Name Extensions

The book package, chapters, and pages use folder name extensions to indicate their type. Table 1-1 describes the folder name extensions and lists their locations in the hierarchy.

__Table 1-1__Folder name extensions

| Extension | Level | Description |
| --- | --- | --- |
| `.playgroundbook` | Book | The top-level folder for the playground book |
| `.playgroundchapter` | Chapter | A chapter in the book |
| `.playgroundpage` | Page | An individual page containing a playground and an optional, always-on live view |
| `.cutscenepage` | Page | An individual page containing a cutscene |

### Folders in the Package Structure

The package structure consists of specially named folders with no folder name extensions. These folders contain the book, the chapters in the book, and the pages in each chapter. Table 1-2 describes the folders in the package structure and lists the containing folder for each.

__Table 1-2__Package structure folder names

| Folder name | Containing folder | Description |
| --- | --- | --- |
| `Contents` | The top-level `.playgroundbook` folder | Contains all the other files and folders for the playground book |
| `Chapters` | `Contents` | Contains all the chapter folders for the book |
| `Pages` | `.playgroundchapter` | Contains all the page folders for the chapter |

### Shared Code Folders

Shared code is stored in folders named `Sources`. The contents of the folders are shared by the level in the hierarchy at which they are defined and all levels below that. For example, code in the `Sources` folder at the book level is available to all chapters and pages, whereas code in the `Sources` folder at the chapter level is available to all pages in that chapter but not to any other chapter.

Table 1-3 describes the shared code folder names and lists their containing folders.

__Table 1-3__Shared code folder names

| Folder name | Containing folders | Description |
| --- | --- | --- |
| `Sources` | `Contents`  `.playgroundchapter`  `.playgroundpage` | A folder containing shared Swift code |

### Public and Private Resources Folders

Resources, such as images, sounds, and text files, are stored in specially named folders with no folder name extensions. Any resources that you want users to be able to access from the file picker or image picker go in a `PublicResources` folder. Any resources that you don’t want users to access, such as localization or hints files, go in a `PrivateResources` folder.

Like shared code folders, the contents of resource folders are shared by the level in the hierarchy at which they are defined and all levels below that. When page content references a resource by name, it consults the `PublicResources` and `PrivateResources` folders at the page, chapter, and book levels, resolving in the following ways:

- If a page, chapter, or book has a resource with the same name in both the `PublicResources` and the `PrivateResources` folders, the resource in the `PublicResources` folder is used.
- If a page has a resource with the same name as its containing chapter, or a chapter has a resource with the same name as its containing book, the resource associated with the higher level is used.

Table 1-3 describes the resources folder names and lists their containing folders.

__Table 1-4__Public and private resources folder names

| Folder name | Containing folders | Description |
| --- | --- | --- |
| `PublicResources` | `Contents`  `.playgroundchapter`  `.playgroundpage`  `.cutscenepage` | A folder containing public resources, such as images and text files |
| `PrivateResources` | `Contents`  `.playgroundchapter`  `.playgroundpage`  `.cutscenepage` | A folder containing private resources, such as images, text files, hints, and localization files |

### Localized Resources Folders

Localized resources are stored in folders named with a locale identifier and the `.lproj` folder name extension. For example, resources for English-speaking users go in `en.lproj` folders, and resources for French-speaking users go in `fr.lproj` folders.

> [!NOTE]
>
> For more information, see [Language and Locale IDs](../../Mac%20OSX/Internationalization%20and%20Localization%20Guide/Language%20and%20Locale%20IDs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2jninedcni) in _[Internationalization and Localization Guide](../../Mac%20OSX/Internationalization%20and%20Localization%20Guide/About%20Internationalization%20and%20Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2i)_.

Table 1-5 describes the folder name extension and lists its locations in the hierarchy.

__Table 1-5__Localized resources folder extensions

| Extension | Containing folders | Description |
| --- | --- | --- |
| `.lproj` | `PublicResources`  `PrivateResources` | A folder containing localized assets for the specified locale |

### Specially Named Files

Configuration information, playground contents, and the source code for always-on live views are in specially named files.

Table 1-6 describes the specially named files and lists their containing folders.

__Table 1-6__Specially named files

| File name | Containing folders | Description |
| --- | --- | --- |
| `Manifest.plist` | `Contents`  `.playgroundchapter`  `.playgroundpage`  `.cutscenepage` | A property list that defines the attributes for a book, chapter, or page |
| `Contents.swift` | `.playgroundpage` | A required file with the initial contents of the playground page |
| `LiveView.swift` | `.playgroundpage` | An optional file used to specify an always-on live view; the code in this file is executed when the page is opened |

### Creating Playground Books

You need to use both a Mac running Xcode and an iPad to create a playground book. The first step in development is creating a skeleton structure for the book. A simple approach is to start with an existing playground book, which you can get by downloading _[StarterPlaygroundBook: A simple Swift Playground Book](../../../samplecode/StarterPlaygroundBook-%20A%20simple%20Swift%20Playground%20Book/StarterPlaygroundBook-%20A%20simple%20Swift%20Playground%20Book.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tgnbu)_. If your playground book uses APIs specific to Swift Playgrounds, or if you need to debug a page’s live view, download the Swift Playgrounds Author Template from [Downloads for Apple Developers](https://developer.apple.com/download/more/?=Swift%20Playgrounds%20Author%20Template).

Any changes to a book, such as adding a new page, require modifying content files, manifest files, and the folder structure. Changes made to a book in Swift Playgrounds, such as entering code into an editable text field, do not change the underlying pages. The suggested workflow is:

1. Make targeted changes to the book’s content and structure in Xcode
2. Transfer the updated book into Swift Playgrounds using iCloud or AirDrop
3. Open the updated book and test the changes
4. Note any additional changes that are needed, and return to step 1

[Book Manifest](https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/swift_playgrounds_doc_format/BookManifest.html#//apple_ref/doc/uid/TP40017343-CH63-SW8)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2018-04-30](https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/swift_playgrounds_doc_format/RevisionHistory.html#//apple_ref/doc/uid/TP40017343-CH99-SW1)
