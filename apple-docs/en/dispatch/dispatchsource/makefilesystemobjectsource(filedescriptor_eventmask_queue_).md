---
title: 'makeFileSystemObjectSource(fileDescriptor:eventMask:queue:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchsource/makefilesystemobjectsource(filedescriptor:eventmask:queue:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsource/makefilesystemobjectsource(filedescriptor:eventmask:queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsource/makefilesystemobjectsource%28filedescriptor%3Aeventmask%3Aqueue%3A%29.json'
content_hash: 'sha256:ff175b2283a1c4df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSource](../dispatchsource.md)

# makeFileSystemObjectSource(fileDescriptor:eventMask:queue:)

<sub>Type Method</sub>

Creates a new dispatch source object for monitoring file-system events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func makeFileSystemObjectSource(fileDescriptor: Int32, eventMask: DispatchSource.FileSystemEvent, queue: DispatchQueue? = nil) -> any DispatchSourceFileSystemObject
```

## Parameters

- `fileDescriptor` — A file descriptor pointing to an open file or socket.

- `eventMask` — The set of events you want to monitor. For a list of possible values, see [FileSystemEvent](filesystemevent.md).

- `queue` — The dispatch queue to use when executing the installed handlers.

## Return Value

A dispatch source object that conforms to the [DispatchSourceFileSystemObject](../dispatchsourcefilesystemobject.md) protocol.

## Discussion

After creating the dispatch source, use the methods of the [DispatchSourceProtocol](../dispatchsourceprotocol.md) protocol to install the event handlers you need. The returned dispatch source is in the inactive state initially. When you are ready to begin processing events, call its [dispatch_activate](<../dispatchobject/activate().md>) method.

## See Also

### Creating a File System Source

- [makeReadSource(fileDescriptor:queue:)](<makereadsource(filedescriptor_queue_).md>) — Creates a new dispatch source object for reading bytes from the specified file.
- [makeWriteSource(fileDescriptor:queue:)](<makewritesource(filedescriptor_queue_).md>) — Creates a new dispatch source object for writing data to the specified file.
- [DispatchSourceRead](../dispatchsourceread.md) — A dispatch source object for reading data from a file descriptor.
- [DispatchSourceWrite](../dispatchsourcewrite.md) — A dispatch source object for writing data to a file descriptor.
- [DispatchSourceFileSystemObject](../dispatchsourcefilesystemobject.md) — A dispatch source that monitors events associated with a file descriptor.
- [FileSystemEvent](filesystemevent.md) — Events involving a change to a file system object.
