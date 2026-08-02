---
title: Printing Programming Guide for Mac
apple_id: 10000083i
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: null
published: '2012-12-20'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Printing/osxp_printinfo/osxp_printinfo.html
archived_at: '2026-07-15T07:17:46.358037Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Printing Programming Guide for Mac](About%20Printing%20on%20the%20Mac.md)


[Next](Managing%20Page%20Layout%20Objects.md)[Previous](Managing%20and%20Extending%20the%20Print%20Panel.md)

# Managing Print Information Objects

An `NSPrintInfo` object contains a dictionary that stores the attributes that describe a print job. The dictionary keys are described in the “Constants” section of [NSPrintInfo](https://developer.apple.com/documentation/appkit/nsprintinfo).

You can set your instance of `NSPrintInfo` as the shared instance using the method `setSharedPrintInfo:`. You get the shared `NSPrintInfo` object using the `sharedPrintInfo` class method.

To reuse the print settings used the last time your app ran, record the print info object as an app preference each time the user prints something and then restore those settings when the app launches.

However, because the dictionary that stores an `NSPrintInfo` object’s print settings includes non-property list values, it is not a proper property list object. Therefore, it cannot be converted to a plist format and saved directly as a preference value. Instead, you need to use the `NSKeyedArchiver` (or `NSArchiver`) class method `archivedDataWithRootObject:` to encode the `NSPrintInfo` object as an `NSData` object, which can be stored in a property list or saved to a file.

To restore the `NSPrintInfo` object, reload the NSData object and then use the `NSKeyedUnarchiver` (or `NSUnarchiver`) class method `unarchiveObjectWithData:` to decode the `NSPrintInfo` information.

In a document-based app, each `NSDocument` instance has its own print info object, which you can obtain by calling the `printInfo` method of `NSDocument`. The document initially uses a copy of the app’s shared print info object (unless you set one yourself). When the user makes changes in the Page Setup panel, the document’s print info object is automatically updated with the new print settings.

Because print settings are often document specific, you might want to save them. For example, a user may print a wide spreadsheet in landscape mode. That setting should be remembered each time the document is printed but should not be used for any other documents, which the user may prefer to print in portrait mode.Therefore, each document should have its own print info object that is saved with the document and used each time that particular document is printed. As before, you should encode the `NSPrintInfo` object into an `NSData` object. Then, you should write the data to the document’s file.

[Next](Managing%20Page%20Layout%20Objects.md)[Previous](Managing%20and%20Extending%20the%20Print%20Panel.md)

