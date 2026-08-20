---
title: File Metadata Search Programming Guide
apple_id: TP40001841
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreServices
published: '2011-09-28'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/SpotlightQuery/Concepts/Introduction.html
archived_at: '2026-07-15T05:24:41.691545Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Searching%20iCloud%20and%20the%20Desktop.md)

# About File Metadata Queries

File metadata provides several application programming interfaces that allow it application to search for files based on data that is part of the file or file system. The level of interaction your application requires with the search results will often dictate the API that you chose.

The simplest way to provide metadata support in your Mac app is to use the Spotlight search window. Using this API an application can display the standard Spotlight search window, optionally providing a search string. The search results are presented directly to the user and are not available to the application. This is a good choice if your application isn't search oriented, but you want to allow users to search for contextual terms using Spotlight.

For applications that need to create queries and interact with the results there are two APIs available. The Metadata framework provides a low-level query API, `MDQuery`, that allows an application to search for files based on metadata values. `MDQuery` is completely configurable, allowing you to run synchronous and asynchronous queries and provides fine-grain control of the frequency of results batching.

The Cocoa frameworks's `NSMetadataQuery` class provides a high-level Objective-C interface to the `MDQuery` API. This class allows you to construct queries using a subset of the `NSPredicate` classes, and execute the queries asynchronously. The `NSMetadataQuery` class allows an application to specify the grouping of the results into multiple subcategories. `NSMetadataQuery` does not support synchronous queries and provides minimal update notifications as data is collected. On OS X `NSMetadataQuery` supports Cocoa bindings, allowing you to display the results without writing any significant amount of glue code.

Spotlight is a fundamental feature of OS X, and all developers should be familiar with its capabilities. Many applications, at a minimum, should offer users the ability to search for selected text using the Spotlight search window.

The following articles cover key concepts in understanding how Spotlight can be used to query metadata:

- [Searching File Metadata with NSMetadataQuery](Searching%20File%20Metadata%20with%20NSMetadataQuery.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnbyfvbuuqsfjjbeqsa) provides a conceptual overview of searching for files using file metadata.
- [Displaying the Finder’s Spotlight Search Window](Displaying%20the%20Finder%E2%80%99s%20Spotlight%20Search%20Window.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjqfvbuuqsfjjbeqsa) describes how to present the standard Spotlight search window.
- [File Metadata Query Expression Syntax](File%20Metadata%20Query%20Expression%20Syntax.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnbzfvbuuqsfjjbeqsa) describes the metadata query language.

There are other technologies, not fully covered in this document, that are fundamental to integrating metadata into your applications. Refer to these documents for more details:

- _[Spotlight Overview](../Spotlight%20Overview/Introduction%20to%20Spotlight.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenry)_ covers the conceptual details surrounding Spotlight’s metadata usage.
- _[Spotlight Importer Programming Guide](../Spotlight%20Importer%20Programming%20Guide/About%20Spotlight%20Importers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrx)_ describes the plug-ins that extract metadata from document files.
- _[File Metadata Attributes Reference](../../File%20Metadata%20Attributes%20Reference/About%20the%20File%20Metadata%20Attributes%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmobz)_ describe the metadata attributes provided by Apple.

The following sample code is available that shows how to generate Spotlight queries.

- _[Spotlighter](../../../samplecode/Spotlighter/Spotlighter.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobrha)_ examples shows how to use Spotlight searches.
- _[PredicateEditorSample](../../../samplecode/PredicateEditorSample/PredicateEditorSample.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimjtha)_ shows how to use the rule editor and Spotlight.
- _[PhotoSearch](../../../samplecode/PhotoSearch/PhotoSearch.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojzgq)_ allows the search of images based on name. It allows multiple searches to run simultaneously.
[Next](Searching%20iCloud%20and%20the%20Desktop.md)

