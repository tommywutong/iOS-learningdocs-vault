---
title: File System Programming Guide
apple_id: TP40010672
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:32:00.364634Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](File%20System%20Basics.md)

# About Files and Directories

The file system is an important part of any operating system. After all, it’s where users keep their stuff. The organization of the file system plays an important role in helping the user find files. The organization also makes it easier for apps and the system itself to find and access the resources they need to support the user.

This document is intended for developers who are writing software for macOS, iOS, and iCloud. It shows you how to use the system interfaces to access files and directories and how to move files to and from iCloud. This document also provides guidance on how best to work with files, and it shows you where you should be placing any new files you create.

To effectively use the file system, you must know what to expect from the file system and which technologies are available for accessing it.

### The File System Imposes a Specific Organization

The file systems in iOS and macOS are structured to help keep files organized, both for the user and for apps. From the perspective of your code, a well-organized file system makes it easier to locate files your app needs. Of course, you also need to know where you should put any files you create.

### Access Files Safely

On a multiuser system like macOS, it is possible that more than one app may attempt to read or write a file at the same time as another app is using it. The `NSFileCoordinator` and `NSFilePresenter` classes allow you to maintain file integrity and ensure that if files are made available to other apps (for example, emailing the current TextEdit document) that the most current version is sent.

### How You Access a File Depends on the File Type

Different files require different treatments by your code. For file formats defined by your app, you might read the contents as a binary stream of bytes. For more common file formats, though, iOS and macOS provide higher-level support that make reading and writing those files easier.

### System Interfaces Help You Locate and Manage Your Files

Hard-coded pathnames are fragile and liable to break over time, so the system provides interfaces that search for files in well-known locations. Using these interfaces makes your code more robust and future proof, ensuring that regardless of where files move to, you can still find them.

### Users Interact with Files Using the Standard System Panels

For files that the user creates and manages, your code can use the standard Open and Save panels to ask for the locations of those files. The standard panels present the user with a navigable version of the file system that matches what the Finder presents. You can use these panels without customization, modify the default behavior, or augment them with your own custom content. Even sandboxed apps can use the panels to access files because they work with the underlying security layer to allow exceptions for files outside of your sandbox that the user explicitly chooses.

### Read and Write Files Asynchronously

Because file operations require accessing a disk or network server, you should always access files from a secondary thread of your app. Some of the technologies for reading and writing files run asynchronously without you having to do anything, while others require you to provide your own execution context. All of the technologies do essentially the same thing but offer different levels of simplicity and flexibility.

As you read and write files, you should also use file coordinators to ensure that any actions you take on a file do not cause problems for other apps that care about the file.

### Move, Copy, Delete, and Manage Files Like the Finder

The system interfaces support all of the same types of behaviors that the Finder supports and many more. You can move, copy, create, and delete files and directories just like the user can. Using the programmatic interfaces, you can also iterate through the contents of directories and work with invisible files much more efficiently. More importantly, most of the work can be done asynchronously to avoid blocking your app’s main thread.

### Optimize Your File-Related Operations

The file system is one of the slowest parts of a computer so writing efficient code is important. Optimizing your file-system code is about minimizing the work you do and making sure that the operations you do perform are done efficiently.

For information about more advanced file-system tasks that you can perform, see _[File System Advanced Programming Topics](../File%20System%20Advanced%20Programming%20Topics/About%20Advanced%20File%20System%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydonrv)_.

[Next](File%20System%20Basics.md)

