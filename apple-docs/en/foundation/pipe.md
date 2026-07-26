---
title: Pipe
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/pipe
source_url: 'https://developer.apple.com/documentation/foundation/pipe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/pipe.json'
content_hash: 'sha256:0b267bba9878351c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Pipe

<sub>Class</sub>

A one-way communications channel between related processes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Pipe
```

## Overview

[Pipe](pipe.md) objects provide an object-oriented interface for accessing pipes. An [Pipe](pipe.md) object represents both ends of a pipe and enables communication through the pipe. A pipe is a one-way communications channel between related processes; one process writes data, while the other process reads that data. The data that passes through the pipe is buffered; the size of the buffer is determined by the underlying operating system. [Pipe](pipe.md) is an abstract class, the public interface of a class cluster.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the File Handles for a Pipe

- [fileHandleForReading](pipe/filehandleforreading.md) — The receiver’s read file handle.
- [fileHandleForWriting](pipe/filehandleforwriting.md) — The receiver’s write file handle.

## See Also

### Tasks and Pipes

- [Process](process.md) — An object that represents a subprocess of the current process.
