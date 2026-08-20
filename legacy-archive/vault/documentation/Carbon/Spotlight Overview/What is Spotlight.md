---
title: Spotlight Overview
apple_id: TP40001268
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreServices
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MetadataIntro/Concepts/WhatIsSpotlight.html
archived_at: '2026-07-15T05:23:34.826191Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Spotlight Overview](Introduction%20to%20Spotlight.md)


[Next](How%20Does%20Spotlight%20Work.md)[Previous](Introduction%20to%20Spotlight.md)

# What is Spotlight?

Organizing data on a computer is a difficult job, and in most cases is the sole responsibility of the user. However, even the most organized user may find it nearly impossible to arrange their files in a way that makes it easy to find information. Because the underlying file systems offer only one way of organizing information, users must resort to special tools to search for what they want. The problem is that most search tools can be slow and limited in how they do their search. Also, users may want to search more than files. Users may want to search their mail archives, address book contacts, or other digital assets embedded inside a file.

Spotlight provides a new way of organizing and accessing information in on your computer by using metadata. Metadata is data about a file, rather than the actual content stored in the file.

Metadata can include familiar information such as an asset’s author and modification date but it can also be keywords or other information that is custom to a particular asset. For example, an image file might have metadata describing the image’s dimensions and color model. Spotlight can use this information to allow a user to find all their high-resolution images using a CMYK colorspace.

For Spotlight searching to work, it has to have metadata. While some bits of metadata (modification dates, file type, path name) are easy to gather for a given file, most of the interesting data is embedded inside the file. To gather this embedded information you must provide a Spotlight importer.

A Spotlight importer is a small plug-in bundle that you create to extract information from files created by your application. Spotlight importers are used by the Spotlight server to gather information about new and existing files.

Apple provides importers for many standard file types that the system uses, including RTF, JPEG, Mail, PDF and MP3. However, if you define a custom document format, you must create a metadata importer for your own content.

The simplest way to provide Spotlight searching in your application is to display the standard Spotlight search window to users directly from your application using the `HISearchWindow` function, defined in the Carbon framework.

The Spotlight metadata framework provides a query API, `MDQuery`, that you can use in your application to search for files based on metadata values. Using this API, you initiate a query using the query expression syntax. You can sort the results based on different attributes and use those sorting criteria to organize the data before you present it to the user.

The Cocoa framework provides the `NSMetadataQuery` class that is an Objective-C interface to the `MDQuery` API. `NSMetadataQuery` uses the `NSPredicate` classes to construct queries rather than the Spotlight query expression syntax.

Spotlight is not only a means of searching for documents. Spotlight importers define metadata that Finder can display in its Get Info panel. This information provides more context and details about documents.

For example:

- Image files provide their dimensions, pixel depth and other color related information.
- QuickTime movies provide their duration.
- PDF files provide information on the authors, security, dimensions, encoding, and where they originated.

It is the richness of the metadata that you provide that will improve the user experience when using your custom files. See [Spotlight Importer Schema Format](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MDImporters/Concepts/SchemaRef.html#//apple_ref/doc/uid/TP40001832) for more information on displaying your attributes in Finder.

[Next](How%20Does%20Spotlight%20Work.md)[Previous](Introduction%20to%20Spotlight.md)

