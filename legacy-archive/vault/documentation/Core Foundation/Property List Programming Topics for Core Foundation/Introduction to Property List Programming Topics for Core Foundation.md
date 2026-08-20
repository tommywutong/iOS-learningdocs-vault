---
title: Property List Programming Topics for Core Foundation
apple_id: 10000130i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html
archived_at: '2026-07-15T07:22:47.543583Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Property%20List%20Structure%20and%20Contents.md)

# Introduction to Property List Programming Topics for Core Foundation

Many applications require a mechanism for storing information that will be needed at a later time. For situations where you need to store small amounts of persistent data, less than a few hundred kilobytes, Core Foundation provides property lists. Property lists—frequently referred to as “plists”—offer a uniform and architecture-independent means of organizing, storing, and accessing data for Mac apps.

Property lists organize data into named values and lists of values using several Core Foundation types: CFString, CFNumber, CFBoolean, CFDate, CFData, CFArray, and CFDictionary. These types give you the means to produce data that is meaningfully structured, transportable, storable, and accessible, but still as efficient as possible. The property list programming interface allows you to convert hierarchically structured combinations of these basic types to and from standard XML. The XML data can be saved to disk and later used to reconstruct the original Core Foundation objects. Note that property lists should be used for data that consists primarily of strings and numbers because they are very inefficient when used with large blocks of binary data.

Property lists are used frequently in OS X. For example, the OS X Finder—through bundles—uses property lists to store file and directory attributes. Core Foundation bundles and URL objects use property lists as well. User and application preferences also use property lists, however, you should not use the CFPropertyList API to read and modify preferences. Core Foundation provides a programming interface specifically for this purpose—see _[Preferences Programming Topics for Core Foundation](../Preferences%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20Preferences%20Programming%20Topics%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezds2i)_ for more information.

This document describes the property list structure, and use of XML tags and specifics about numbers, and contains examples on creating, saving, and restoring property lists.

- [Property List Structure and Contents](Property%20List%20Structure%20and%20Contents.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3tclkdjjbeksscjbea)
- [Creating Property Lists](Creating%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3tilkdjjbekscbifdq)
- [Saving and Restoring Property Lists](Saving%20and%20Restoring%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3tklkdjjbekscbifdq)
- [Using Numbers in Property Lists](Using%20Numbers%20in%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3tglkdjjbeksscjbea)
- [Property List XML Tags](Property%20List%20XML%20Tags.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3telkdjjbeksscjbea)

[Next](Property%20List%20Structure%20and%20Contents.md)

