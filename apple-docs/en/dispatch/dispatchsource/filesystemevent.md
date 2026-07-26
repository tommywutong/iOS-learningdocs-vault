---
title: DispatchSource.FileSystemEvent
framework: Dispatch
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsource/filesystemevent
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsource/filesystemevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsource/filesystemevent.json'
content_hash: 'sha256:42f2d06639ede338'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSource](../dispatchsource.md)

# DispatchSource.FileSystemEvent

<sub>Structure</sub>

Events involving a change to a file system object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FileSystemEvent
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### File System Event Flags

- [all](filesystemevent/all.md) — All changes related to the file system object.
- [attrib](filesystemevent/attrib.md) — Changes to the metadata of the file system object.
- [delete](filesystemevent/delete.md) — The deletion of the file system object.
- [extend](filesystemevent/extend.md) — Changes to the size of the file system object.
- [funlock](filesystemevent/funlock.md) — The unlocking of the file system object.
- [link](filesystemevent/link.md) — Changes to the link count of the file system object.
- [rename](filesystemevent/rename.md) — Changes to the name of the file system object.
- [revoke](filesystemevent/revoke.md) — The revocation of the file system object.
- [write](filesystemevent/write.md) — The writing of data to the file system object.

## See Also

### Creating a File System Source

- [makeReadSource(fileDescriptor:queue:)](<makereadsource(filedescriptor_queue_).md>) — Creates a new dispatch source object for reading bytes from the specified file.
- [makeWriteSource(fileDescriptor:queue:)](<makewritesource(filedescriptor_queue_).md>) — Creates a new dispatch source object for writing data to the specified file.
- [makeFileSystemObjectSource(fileDescriptor:eventMask:queue:)](<makefilesystemobjectsource(filedescriptor_eventmask_queue_).md>) — Creates a new dispatch source object for monitoring file-system events.
- [DispatchSourceRead](../dispatchsourceread.md) — A dispatch source object for reading data from a file descriptor.
- [DispatchSourceWrite](../dispatchsourcewrite.md) — A dispatch source object for writing data to a file descriptor.
- [DispatchSourceFileSystemObject](../dispatchsourcefilesystemobject.md) — A dispatch source that monitors events associated with a file descriptor.
