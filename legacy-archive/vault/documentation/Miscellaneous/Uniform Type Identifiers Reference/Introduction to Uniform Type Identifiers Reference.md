---
title: Uniform Type Identifiers Reference
apple_id: TP40009257
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreServices
published: '2009-11-17'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/UTIRef/Introduction/Introduction.html
archived_at: '2026-07-15T08:17:10.489561Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](System-Declared%20Uniform%20Type%20Identifiers.md)

# Introduction to Uniform Type Identifiers Reference

One of the challenges facing application developers is the proliferation of methods to identify types of data. For example, some text files may be assigned a `'TEXT'` file type (as originally designed for Mac OS 9 and earlier), while others may simply have a `.txt` filename extension. Some may have the `.text` extension instead. In addition, some file types might be subsets of other types; an application that opens all `.txt` files should probably also be able to open those with a `.html` extension. Determining all the possible files an application could read could become impossible. The user experience then suffers, with users not understanding why an application can open one text file but not another.

To solve this problem, Apple has defined a syntax for special data identifiers called _uniform type identifiers_. Each UTI provides a unique identifier for a particular file type, data type, directory or bundle type, and so on. In addition, other type identifier namespaces for a particular type can be grouped under one UTI, with utility functions available to translate from one format to another.

This document is for OS X and iOS application developers that need to create or otherwise manipulate data that may be exchanged with other applications or services. For example, applications often need to be aware of the type of data they handle when:

- Displaying, or manipulating, files, bundles, or folders
- Accessing streaming data
- Copying and pasting between documents or applications
- Dragging and dropping between applications

Support for uniform type identifiers is available in OS X v10.3 and later and iOS 3.0 and later.

This document is organized into the following chapters:

- [System-Declared Uniform Type Identifiers](System-Declared%20Uniform%20Type%20Identifiers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjzfvjvomi) describes UTIs defined by Apple.

_[Uniform Type Identifiers Overview](../../File%20Management/Uniform%20Type%20Identifiers%20Overview/Introduction%20to%20Uniform%20Type%20Identifiers%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmjz)_ describes UTIs and how to use them.

_[UTType Reference](https://developer.apple.com/documentation/mobilecoreservices/uttype)_ describes the functions used to manipulate UTIs.

[Next](System-Declared%20Uniform%20Type%20Identifiers.md)

