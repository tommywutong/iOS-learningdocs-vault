---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/Foundation/FoundationIntro.html
archived_at: '2026-07-15T07:51:39.710305Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](FoundationTOC.md) [!Previous Section](FoundationTOC.md)

# Foundation Objects

This section provides an overview of some of the topics, techniques, and conventions you use when programming with Foundation objects.

## Representing Objects as Strings

You can obtain a human-readable string representation of any object by sending it a __description__ message. This method is particularly useful for debugging. In some cases, the string returned from __description__ contains only the class name of the object that received the message (the _receiver_). Most objects, however, provide more information. For class-specific details, see the __description__ method descriptions later in this chapter.

## Mutable and Immutable Objects

Some objects are immutable; that is, once they are created, they can't be modified. Other objects are mutable. They can be modified at any time. When you create an object, you can often choose to create it as either immutable or mutable. Three kinds of objects discussed in this chapter-strings, arrays, and dictionaries-have both immutable and mutable versions.
It's best to use immutable objects whenever possible. Use a mutable object only if you need to modify its contents after you create it.

## Determining Equality

You can determine if two objects are equal using the __isEqual:__ method. This method returns YES if the receiver of the message and the specified object are equal, and NO otherwise. The definition of equality depends on the object's type. For example, array objects define two arrays as equal if they contain the same contents. For more information, see the __isEqual:__ method descriptions later in this chapter.

## Writing to and Reading From Files

Strings, arrays, and dictionaries-three of the classes discussed in this chapter-provide methods for writing to and reading from files. The method __writeToFile:atomically:__ writes a textual description of the receiver's contents to a specified path name, and corresponding class-specific creation methods-__stringWithContentsOfFile:__, __arrayWithContentsOfFile:__, and __dictionaryWithContentsOfFile:__-create an object from the contents of a specified file.
For example, the following code excerpt reads the contents of an error log stored in a file, appends a new error to the log, and saves the updated log to the same file:

```
    id errorLog = [NSString stringWithContentsOfFile:errorPath];
    id newErrorLog = [errorLog stringByAppendingFormat:@"%@: %@.\n",
        timeStamp, @"premature end of file."];
    [newErrorLog writeToFile:errorPath atomically:YES];
```


### Writing to Files

To write to a file, use the method __writeToFile:atomically:__. It uses the __description__ method to obtain a human-readable string representation of the receiver and then writes the string to the specified file. The resulting file is suitable for use with _className___WithContentsOfFile:__ methods. This method returns YES if the file is written successfully, and NO otherwise.
If the argument for __atomically:__is YES, the string representation is first written to an auxiliary file. Then the auxiliary file is renamed to the specified filename. If the argument is NO, the object is written directly to the specified file. The YES option guarantees that the specified file, if it exists at all, won't be corrupted even if the system should crash during writing.
When __writeToFile:atomically:__ fails, it returns NO. If this happens, check the permissions on the specified file and its directory. The most common cause of write failures is that the process owner doesn't have the necessary permissions to write to the file or its directory. If the argument for __atomically:__ is NO, it's sufficient to grant write permissions only on the file.
__Note:__  The configuration of your HTTP server determines the user who owns autostarted applications.

### Reading From Files

The string, array, and dictionary classes provide methods of the form _className___WithContentsOfFile:__. These methods create a new object and initialize it with the contents of a specified file, which can be specified with a full or relative pathname.

[!Table of Contents](FoundationTOC.md) [!Next Section](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/Foundation/StringIntro.html)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
