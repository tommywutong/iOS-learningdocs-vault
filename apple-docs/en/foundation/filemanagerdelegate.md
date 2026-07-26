---
title: FileManagerDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanagerdelegate
source_url: 'https://developer.apple.com/documentation/foundation/filemanagerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanagerdelegate.json'
content_hash: 'sha256:618c96baf3c98a68'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# FileManagerDelegate

<sub>Protocol</sub>

The interface a file manager’s delegate uses to intervene during operations or if an error occurs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol FileManagerDelegate : NSObjectProtocol
```

## Overview

The [FileManagerDelegate](filemanagerdelegate.md) protocol defines optional methods for managing operations involving the copying, moving, linking, or removal of files and directories. When you use an [FileManager](filemanager.md) object to initiate a copy, move, link, or remove operation, the file manager asks its delegate whether the operation should begin at all and whether it should proceed when an error occurs.

The methods of this protocol accept either [NSURL](nsurl.md) or [NSString](nsstring.md) objects. The file manager always prefers methods that take an [NSURL](nsurl.md) object over those that take an [NSString](nsstring.md) object.

You should associate your delegate with a unique instance of the [FileManager](filemanager.md) class, as opposed to the shared instance.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Moving  an Item

- [- fileManager:shouldMoveItemAtURL:toURL:](<filemanagerdelegate/filemanager(__shouldmoveitemat_to_).md>) — Asks the delegate if the file manager should move the specified item to the new URL.
- [- fileManager:shouldMoveItemAtPath:toPath:](<filemanagerdelegate/filemanager(__shouldmoveitematpath_topath_).md>) — Asks the delegate if the file manager should move the specified item to the new path.
- [- fileManager:shouldProceedAfterError:movingItemAtURL:toURL:](<filemanagerdelegate/filemanager(__shouldproceedaftererror_movingitemat_to_).md>) — Asks the delegate if the move operation should continue after an error occurs while moving the item at the specified URL.
- [- fileManager:shouldProceedAfterError:movingItemAtPath:toPath:](<filemanagerdelegate/filemanager(__shouldproceedaftererror_movingitematpath_topath_).md>) — Asks the delegate if the move operation should continue after an error occurs while moving the item at the specified path.

### Copying  an Item

- [- fileManager:shouldCopyItemAtURL:toURL:](<filemanagerdelegate/filemanager(__shouldcopyitemat_to_).md>) — Asks the delegate if the file manager should copy the specified item to the new URL.
- [- fileManager:shouldCopyItemAtPath:toPath:](<filemanagerdelegate/filemanager(__shouldcopyitematpath_topath_).md>) — Asks the delegate if the file manager should copy the specified item to the new path.
- [- fileManager:shouldProceedAfterError:copyingItemAtURL:toURL:](<filemanagerdelegate/filemanager(__shouldproceedaftererror_copyingitemat_to_).md>) — Asks the delegate if the move operation should continue after an error occurs while copying the item at the specified URL.
- [- fileManager:shouldProceedAfterError:copyingItemAtPath:toPath:](<filemanagerdelegate/filemanager(__shouldproceedaftererror_copyingitematpath_topath_).md>) — Asks the delegate if the move operation should continue after an error occurs while copying the item at the specified path.

### Removing an Item

- [- fileManager:shouldRemoveItemAtURL:](<filemanagerdelegate/filemanager(__shouldremoveitemat_).md>) — Asks the delegate whether the item at the specified URL should be deleted.
- [- fileManager:shouldRemoveItemAtPath:](<filemanagerdelegate/filemanager(__shouldremoveitematpath_).md>) — Asks the delegate whether the item at the specified path should be deleted.
- [- fileManager:shouldProceedAfterError:removingItemAtURL:](<filemanagerdelegate/filemanager(__shouldproceedaftererror_removingitemat_).md>) — Asks the delegate if the operation should continue after an error occurs while removing the item at the specified URL.
- [- fileManager:shouldProceedAfterError:removingItemAtPath:](<filemanagerdelegate/filemanager(__shouldproceedaftererror_removingitematpath_).md>) — Asks the delegate if the operation should continue after an error occurs while removing the item at the specified path.

### Linking an Item

- [- fileManager:shouldLinkItemAtURL:toURL:](<filemanagerdelegate/filemanager(__shouldlinkitemat_to_).md>) — Asks the delegate if a hard link should be created between the items at the two URLs.
- [- fileManager:shouldLinkItemAtPath:toPath:](<filemanagerdelegate/filemanager(__shouldlinkitematpath_topath_).md>) — Asks the delegate if a hard link should be created between the items at the two paths.
- [- fileManager:shouldProceedAfterError:linkingItemAtURL:toURL:](<filemanagerdelegate/filemanager(__shouldproceedaftererror_linkingitemat_to_).md>) — Asks the delegate if the operation should continue after an error occurs while linking to the item at the specified URL.
- [- fileManager:shouldProceedAfterError:linkingItemAtPath:toPath:](<filemanagerdelegate/filemanager(__shouldproceedaftererror_linkingitematpath_topath_).md>) — Asks the delegate if the operation should continue after an error occurs while linking to the item at the specified path.

## See Also

### File system operations

- [Improving performance and stability when accessing the file system](improving-performance-and-stability-when-accessing-the-file-system.md) — Prevent data loss and app crashes by interacting with the file system in a coordinated, asynchronous manner and by avoiding unnecessary disk I/O.
- [Using the file system effectively](using-the-file-system-effectively.md) — Gain access to benefits like automatic backup or purging by using purpose-built directories provided by the system.
- [FileManager](filemanager.md) — A convenient interface to the contents of the file system, and the primary means of interacting with it.
- [About Apple File System](about-apple-file-system.md) — Use high-level APIs to get the most out of Apple File System.
