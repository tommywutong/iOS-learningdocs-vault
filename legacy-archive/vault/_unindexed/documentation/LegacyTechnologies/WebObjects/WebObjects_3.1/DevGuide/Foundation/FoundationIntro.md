---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Foundation/FoundationIntro.html
archived_at: '2026-07-15T07:46:47.203276Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Foundation.book.md) [!Previous Section](Foundation.book.md)

# Foundation Objects

This section provides an overview of some of the topics, techniques, and conventions you use when programming with Foundation objects.
It includes the following topics:

- [Types](#apple-gmzdm)
- [Sending Messages](#apple-gm2dq)
- [Mutable and Immutable Objects](#apple-gy3tg)
- [Determining Equality](#apple-gmztq)
- [Reading from and Writing to Files](#apple-gm2te)
- [Representing Objects as Strings](#apple-gmzts)

## Types

All the variables you create in WebScript are objects. Consequently, there is only one data type: __id__. For more information on the __id__ type, see "[The id Data Type](../WebScript/idDataType.md)" in the "Using WebScript" chapter.

## Sending Messages

To get an object to invoke one of its methods, you send it a message. For example, the following statement:

```
[colorArray removeAllObjects];
```


tells the object __colorArray__ to invoke its __removeAllObjects__ method. Message expressions are enclosed in square brackets:

```
[receiver message];
```


The receiver is an object, and the message is the method you want to invoke and any arguments passed to it. The following are examples of messages with arguments:

```
[colorArray addObject:newColor];
[colorArray writeToFile:fileName atomically:YES];
```


In the first statement, __newColor__ is an argument to the method __addObject:__. In the second statement, __fileName__ and __YES__ are both arguments to the method __writeToFile:atomically:__.
For more information on messages, see "[Messaging in WebScript](../WebScript/Messaging.md)" in the "Using WebScript" chapter.

## Representing Objects as Strings

You can get a human-readable string representation of any object by sending it a __description__ message. This method is particularly useful for debugging. In some cases, the string returned from __description__ only contains the name of the receiver's class, but most objects provide more information. For class-specific details, see the __description__ method descriptions later in this chapter.

## Mutable and Immutable Objects

Some objects are immutable; once they are created, they can't be modified. Other objects are mutable. They can be modified at any time. When you create an object, you can often choose to create it as either immutable or mutable. Three kinds of objects discussed in this chapter-strings, arrays, and dictionaries-have both immutable and mutable versions.
For clarity, it's best to use immutable objects wherever possible. Only use a mutable object if you need to modify its contents after you create it.

## Determining Equality

You can determine if two objects are equal using the __isEqual:__ method. __isEqual:__ returns YES if the receiver of the message and the specified object are equal, NO otherwise. Different types of objects determine equality in different ways. For example, array objects define two arrays as equal if they contain the same contents. For more information, see the __isEqual:__ method descriptions later in this chapter.

## Reading from and Writing to Files

Strings, arrays, and dictionaries-three of the classes discussed in this chapter-provide methods for writing to and reading from files. The method __writeToFile:atomically:__ writes a textual description of the receiver's contents to a specified path name, and corresponding class-specific creation methods-__stringWithContentsOfFile:__, __arrayWithContentsOfFile:__, and __dictionaryWithContentsOfFile:__-create an object from the contents of a specified file.
For example, the following code excerpt:

```
id errorLog = [NSString stringWithContentsOfFile:errorPath];
id newErrorLog = [errorLog stringByAppendingFormat:@"%@: %@.\n",
        timeStamp, @"premature end of file."];
[newErrorLog writeToFile:errorPath atomically:YES];
```


reads the contents of an error log stored in a file, appends a new error to the log, and saves the updated log to the same file.

### Writing to Files

The method __writeToFile:atomically:__ uses the __description__ method to obtain a human-readable string representation of the receiver. It then writes the string to the specified file. The resulting file is suitable for use with _className___WithContentsOfFile:__ methods. This method returns YES if the file is written successfully, and NO otherwise.
If the argument for __atomically:__is YES, the string representation is first written to an auxiliary file. Then the auxiliary file is renamed to the specified file name. If flag is NO, the object is written directly to the specified file. The YES option guarantees that the specified file, if it exists at all, won't be corrupted even if the system should crash during writing.
When __writeToFile:atomically:__ fails, it returns NO. If this happens, check the permissions on the specified file and its directory. The most common cause of write failures is that the process owner doesn't have the necessary permissions to write to the file or its directory. If the argument for __atomically:__ is NO, it's sufficient to grant write permissions only on the file.
__Note:__  The configuration of your HTTP server determines the user who owns autostarted applications.

### Reading from Files

The string, array, and dictionary classes provide methods of the form _className___WithContentsOfFile:__. These methods create a new object and initialize it with the contents of a specified file, which can be specified with a full or relative pathname.

[!Table of Contents](Foundation.book.md) [!Next Section](StringIntro.md)
