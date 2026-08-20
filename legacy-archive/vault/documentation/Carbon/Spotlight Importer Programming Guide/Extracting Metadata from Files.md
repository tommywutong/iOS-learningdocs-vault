---
title: Spotlight Importer Programming Guide
apple_id: TP40001267
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreServices
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MDImporters/Concepts/Importers.html
archived_at: '2026-07-15T05:23:19.657860Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Spotlight Importer Programming Guide](About%20Spotlight%20Importers.md)


[Next](Assigning%20Values%20to%20Metadata%20Attributes.md)[Previous](About%20Spotlight%20Importers.md)

# Extracting Metadata from Files

Spotlight provides a powerful search capability by providing an application the means to save metadata about the file’s content. This metadata is searchable from OS X on disk based storage—both local and network.

For Spotlight searching to be possible, it has to have access to the file metadata. Although some file-system metadata (modification dates, display name, path name) is available for all files, most of the interesting data is embedded inside the file. To gather this embedded information into a searchable format, you must provide a Spotlight importer.

A Spotlight importer is a small plug-in bundle that you create to extract information from files created by your application.

Spotlight importers parse your file format for relevant information and assign that information to the appropriate metadata keys. Metadata keys provided by Apple (see _[File Metadata Attributes Reference](../../File%20Metadata%20Attributes%20Reference/About%20the%20File%20Metadata%20Attributes%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmobz)_) index the content in the file and facilitate searches using standard metadata keys. Xcode includes a Spotlight project template that provides the required CFPlugin support, as well as templates for the required schema file.

Spotlight importers typically are within your application’s bundle in the subdirectory `MyApp.app/Contents/Library/Spotlight`. Importers not related to a specific application can also be installed in `~/Library/Spotlight`, `/Library/Spotlight`, and `Framework/PlugIn`. Apple-provided importers reside in `/System/Library/Spotlight`.

Spotlight importers are associated with file types by specifying the uniform type identifiers (UTIs) from which they extract data. For more information on Uniform Type Identifiers see _[Uniform Type Identifiers Overview](../../File%20Management/Uniform%20Type%20Identifiers%20Overview/Introduction%20to%20Uniform%20Type%20Identifiers%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmjz)_.

The supported UTI types are specified in the importer’s `Info.plist` file, contained within the plug-in bundle. An importer can support a single file type or multiple file types. The function in the importer that is called for each file is passed the UTI type of the file and can adjust its extraction means as appropriate.

All critical metadata should be in the extracted from the data file. Consider the System store of metadata should be considered volatile.

Having to create intermediary cache files which were then processed by the Spotlight importer was a common work with Core Data-based applications, but it has been solved by Spotlight support for Core Data documents as described in _[Core Data Spotlight Integration Programming Guide](../../Cocoa/Core%20Data%20Spotlight%20Integration%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danrv)_.

A Spotlight importer must run entirely without interaction. You should not attempt to present any user interface or expect that the window server is running.

You should not expect your application to be running when your metadata importer is called. Importers can be called at any time to extract metadata from a file. Your metadata importer should be able to extract the information without any assistance from the application that created the file.

Keep security in mind when considering the metadata to write to a file. For example, writing a user’s account name or password to a metadata field (even a search-only field) is a bad idea.

[Next](Assigning%20Values%20to%20Metadata%20Attributes.md)[Previous](About%20Spotlight%20Importers.md)

