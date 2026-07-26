---
title: FileHandle
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle
source_url: 'https://developer.apple.com/documentation/foundation/filehandle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle.json'
content_hash: 'sha256:63368d5127189232'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# FileHandle

<sub>Class</sub>

An object-oriented wrapper for a file descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class FileHandle
```

## Overview

You use file handle objects to access data associated with files, sockets, pipes, and devices. For files, you can read, write, and seek within the file. For sockets, pipes, and devices, you can use a file handle object to monitor the device and process data asynchronously.

Most creation methods for [FileHandle](filehandle.md) cause the file handle object to take ownership of the associated file descriptor. This means that the file handle object both creates the file descriptor and is responsible for closing it later, usually when the system deallocates the file handle object. If you want to use a file handle object with a file descriptor that you created, use the [- initWithFileDescriptor:](<filehandle/init(filedescriptor_).md>) method or use the [- initWithFileDescriptor:closeOnDealloc:](<filehandle/init(filedescriptor_closeondealloc_).md>) method and pass [false](../swift/false.md) for the `flag` parameter.

### Run Loop Considerations

When using a file handle object to communicate asynchronously with a socket, you must initiate the corresponding operations from a thread with an active run loop. Although the read, accept, and wait operations themselves are performed asynchronously on background threads, the file handle uses a run loop source to monitor the operations and notify your code appropriately. Therefore, you must call those methods from your application’s main thread or from any thread where you’ve configured a run loop and are using it to process events.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a file handle

- [- initWithFileDescriptor:](<filehandle/init(filedescriptor_).md>) — Creates and returns a file handle object associated with the specified file descriptor.
- [- initWithFileDescriptor:closeOnDealloc:](<filehandle/init(filedescriptor_closeondealloc_).md>) — Creates and returns a file handle object associated with the specified file descriptor and deallocation policy.
- [+ fileHandleForReadingAtPath:](<filehandle/init(forreadingatpath_).md>) — Returns a file handle initialized for reading the file, device, or named socket at the specified path.
- [init(forReadingFromURL:)](<filehandle/init(forreadingfromurl_).md>) — Returns a file handle initialized for reading the file, device, or named socket at the specified URL.
- [+ fileHandleForWritingAtPath:](<filehandle/init(forwritingatpath_).md>) — Returns a file handle initialized for writing to the file, device, or named socket at the specified path.
- [init(forWritingToURL:)](<filehandle/init(forwritingtourl_).md>) — Returns a file handle initialized for writing to the file, device, or named socket at the specified URL.
- [+ fileHandleForUpdatingAtPath:](<filehandle/init(forupdatingatpath_).md>) — Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified path.
- [init(forUpdatingURL:)](<filehandle/init(forupdatingurl_).md>) — Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified URL.
- [- initWithCoder:](<filehandle/init(coder_).md>) — Returns a file handle initialized from data in an unarchiver.

### Getting a file handle

- [fileHandleWithStandardError](filehandle/standarderror.md) — The file handle associated with the standard error file.
- [fileHandleWithStandardInput](filehandle/standardinput.md) — The file handle associated with the standard input file.
- [fileHandleWithStandardOutput](filehandle/standardoutput.md) — The file handle associated with the standard output file.
- [fileHandleWithNullDevice](filehandle/nulldevice.md) — The file handle associated with a null device.

### Getting a file descriptor

- [fileDescriptor](filehandle/filedescriptor.md) — The POSIX file descriptor associated with the receiver.

### Reading from a file handle asynchronously

- [bytes](filehandle/bytes.md) — The file’s contents, as an asynchronous sequence of bytes.
- [AsyncBytes](filehandle/asyncbytes.md) — An asynchronous sequence of bytes.

### Reading from a file handle synchronously

- [availableData](filehandle/availabledata.md) — The data currently available in the receiver.
- [readToEnd()](<filehandle/readtoend().md>) — Reads the available data synchronously up to the end of file or maximum number of bytes.
- [read(upToCount:)](<filehandle/read(uptocount_).md>) — Reads data synchronously up to the specified number of bytes.

### Reading asynchronously with notifications

- [- acceptConnectionInBackgroundAndNotify](<filehandle/acceptconnectioninbackgroundandnotify().md>) — Accepts a socket connection (for stream-type sockets only) in the background and creates a file handle for the “near” (client) end of the communications channel.
- [- acceptConnectionInBackgroundAndNotifyForModes:](<filehandle/acceptconnectioninbackgroundandnotify(formodes_).md>) — Accepts a socket connection (for stream-type sockets only) in the background and creates a file handle for the “near” (client) end of the communications channel.
- [- readInBackgroundAndNotify](<filehandle/readinbackgroundandnotify().md>) — Reads from the file or communications channel in the background and posts a notification when finished.
- [- readInBackgroundAndNotifyForModes:](<filehandle/readinbackgroundandnotify(formodes_).md>) — Reads from the file or communications channel in the background and posts a notification when finished.
- [- readToEndOfFileInBackgroundAndNotify](<filehandle/readtoendoffileinbackgroundandnotify().md>) — Reads to the end of file from the file or communications channel in the background and posts a notification when finished.
- [- readToEndOfFileInBackgroundAndNotifyForModes:](<filehandle/readtoendoffileinbackgroundandnotify(formodes_).md>) — Reads to the end of file from the file or communications channel in the background and posts a notification when finished.
- [- waitForDataInBackgroundAndNotify](<filehandle/waitfordatainbackgroundandnotify().md>) — Asynchronously checks to see if data is available.
- [- waitForDataInBackgroundAndNotifyForModes:](<filehandle/waitfordatainbackgroundandnotify(formodes_).md>) — Asynchronously checks to see if data is available.

### Writing to a file handle

- [write(contentsOf:)](<filehandle/write(contentsof_).md>) — Writes the specified data synchronously to the file handle.

### Seeking within a file

- [offset()](<filehandle/offset().md>) — Gets the position of the file pointer within the file.
- [seekToEnd()](<filehandle/seektoend().md>) — Places the file pointer at the end of the file referenced by the file handle and returns the new file offset.
- [- seekToOffset:error:](<filehandle/seek(tooffset_).md>) — Moves the file pointer to the specified offset within the file.

### Operating on a file

- [- closeAndReturnError:](<filehandle/close().md>) — Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing.
- [- synchronizeAndReturnError:](<filehandle/synchronize().md>) — Causes all in-memory data and attributes of the file represented by the file handle to write to permanent storage.
- [- truncateAtOffset:error:](<filehandle/truncate(atoffset_).md>) — Truncates or extends the file represented by the file handle to a specified offset within the file and puts the file pointer at that position.

### Monitoring for readability and writability

- [readabilityHandler](filehandle/readabilityhandler.md) — The block to use for reading the contents of the file handle asynchronously.
- [writeabilityHandler](filehandle/writeabilityhandler.md) — The block to use for writing the contents of the file handle asynchronously.

### Working with constants

- [Keys for Notification UserInfo Dictionary](keys-for-notification-userinfo-dictionary.md) — Strings that the system uses as keys in a userinfo dictionary during a file handle notification.
- [Exception Names](exception-names.md) — Constant that defines the name of a file operation exception.

### Working with notifications

- [NSFileHandleConnectionAcceptedNotification](nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md) — Posted when a file handle object establishes a socket connection between two processes, creates a file handle object for one end of the connection, and makes this object available to observers.
- [NSFileHandleDataAvailableNotification](nsnotification/name-swift.struct/nsfilehandledataavailable.md) — Posted when the file handle determines that data is currently available for reading in a file or at a communications channel.
- [NSFileHandleReadCompletionNotification](filehandle/readcompletionnotification.md) — Posted when the file handle reads the data currently available in a file or at a communications channel.
- [NSFileHandleReadToEndOfFileCompletionNotification](nsnotification/name-swift.struct/nsfilehandlereadtoendoffilecompletion.md) — Posted when the file handle reads all data in the file or, in a communications channel, until the other process signals the end of data.

### Working with notification messages

- [ConnectionAcceptedMessage](filehandle/connectionacceptedmessage.md) — A message a file handle sends when it creates a socket connection between two processes and creates a file handle for one end of the connection.
- [DataAvailableMessage](filehandle/dataavailablemessage.md) — A message a file handle sends when it determines data is available for reading from a file or communications channel.
- [ReadCompletionMessage](filehandle/readcompletionmessage.md) — A message a file handle sends when it reads the data currently available in a file or a communication channel.
- [ReadToEndOfFileCompletionMessage](filehandle/readtoendoffilecompletionmessage.md) — A message a file handle sends when it reads all data in a file, or another process in a communication channel signals the end of the data.

### Deprecated

- [- readDataToEndOfFile](<filehandle/readdatatoendoffile().md>) — Reads the available data synchronously up to the end of file or maximum number of bytes. _(deprecated)_
- [- readDataOfLength:](<filehandle/readdata(oflength_).md>) — Reads data synchronously up to the specified number of bytes. _(deprecated)_
- [- writeData:](<filehandle/write(__).md>) — Writes the specified data synchronously to the file handle. _(deprecated)_
- [offsetInFile](filehandle/offsetinfile.md) — The position of the file pointer within the file represented by the file handle. _(deprecated)_
- [- seekToEndOfFile](<filehandle/seektoendoffile().md>) — Places the file pointer at the end of the file referenced by the file handle and returns the new file offset. _(deprecated)_
- [- seekToFileOffset:](<filehandle/seek(tofileoffset_).md>) — Moves the file pointer to the specified offset within the file represented by the receiver. _(deprecated)_
- [- closeFile](<filehandle/closefile().md>) — Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing. _(deprecated)_
- [- synchronizeFile](<filehandle/synchronizefile().md>) — Causes all in-memory data and attributes of the file represented by the handle to write to permanent storage. _(deprecated)_
- [- truncateFileAtOffset:](<filehandle/truncatefile(atoffset_).md>) — Truncates or extends the file represented by the file handle to a specified offset within the file and puts the file pointer at that position. _(deprecated)_
- [NSFileHandleNotificationMonitorModes](nsfilehandlenotificationmonitormodes.md) — Currently unused. _(deprecated)_

### Initializers

- [+ fileHandleForReadingFromURL:error:](<filehandle/init(forreadingfrom_).md>) — Returns a file handle initialized for reading the file, device, or named socket at the specified URL.
- [+ fileHandleForUpdatingURL:error:](<filehandle/init(forupdating_).md>) — Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified URL.
- [+ fileHandleForWritingToURL:error:](<filehandle/init(forwritingto_).md>) — Returns a file handle initialized for writing to the file, device, or named socket at the specified URL.

### Default Implementations

- [FileHandle Implementations](filehandle/filehandle-implementations.md)

## See Also

### Managed file access

- [NSFileSecurity](nsfilesecurity.md) — A stub class that encapsulates security information about a file.
- [NSFileVersion](nsfileversion.md) — A snapshot of a file at a specific point in time.
- [FileWrapper](filewrapper.md) — A representation of a node (a file, directory, or symbolic link) in the file system.
