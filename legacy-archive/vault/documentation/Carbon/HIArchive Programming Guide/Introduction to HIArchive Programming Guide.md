---
title: HIArchive Programming Guide
apple_id: TP40002481
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-08-11'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/HIArchiveProgrammingGuide/HIArchive_intro/HIArchive_intro.html
archived_at: '2026-07-15T05:22:33.457766Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Archiving%20and%20Unarchiving%20Objects.md)

# Introduction to HIArchive Programming Guide

HIArchive provides a convenient and standardized
mechanism for flattening data objects so they can be stored in memory
or on disk. Applications can use these archives whenever they need
to package complex data. For example, you can use archives to:

- Store document
  data
- Transfer data using pasteboards, drag and drop, streams, or
  Apple events
- Store localization strings and user interface elements in
  the same package

HIArchive encodes archives in the binary property list format.
You can convert archives to a text XML format using the `plutil` property
list tool accessible from Terminal. You can also examine archives
using the Property List Editor tool in `/Developer/Applications/Utilities`.

This document is for Carbon developers who want to use, create,
or manipulate HIArchives, whether to store and access proprietary
data, or to edit archived data obtained from other sources. You
should also read this document if you want to support the archiving
of your custom HIObjects.

HIArchive is comparable to (and uses the same underlying mechanism
as) the Cocoa NSKeyedArchiver/Unarchiver classes.

HIArchive is available in Mac OS X version 10.4 and later.

This document is organized into the following chapters:

- [Archiving and Unarchiving Objects](Archiving%20and%20Unarchiving%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiobrfvbuqmrqgiwueqsdi5bugrsf) describes the basics of using HIArchives.
- [Making HIObjects Archivable](Making%20HIObjects%20Archivable.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiobrfvbuqmrqguwueqsdi5bugrsf) describes
  how to make your custom HIObjects support archiving.

In addition to this document, you may find the following documents
useful:

- For a complete
  description of the HIArchive API, see _HIArchive Reference_.
- If you are not familiar with using HIViews and HIObjects,
  you should read _[HIView Programming Guide](../HIView%20Programming%20Guide/Introduction%20to%20HIView%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrt)_.
[Next](Archiving%20and%20Unarchiving%20Objects.md)

