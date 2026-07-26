---
title: NSURLHandle
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlhandle
source_url: 'https://developer.apple.com/documentation/foundation/nsurlhandle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlhandle.json'
content_hash: 'sha256:a9f6c1bd81234ad9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLHandle

<sub>Class</sub>

An object that accesses and manages resource data indicated by a URL.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSURLHandle
```

## Overview

> [!important] Important
> [NSURLHandle](nsurlhandle.md) is deprecated in macOS 10.4 and later. Use [URLSession](urlsession.md) instead.

A single [NSURLHandle](nsurlhandle.md) can service multiple equivalent [NSURL](nsurl.md) objects, but only if these URLs map to the same resource.

### Overview

Cocoa provides private concrete subclasses to handle HTTP and file URL schemes. If you want to implement support for additional URL schemes, you would do so by creating a subclass of `NSURLHandle`. You can use `NSURL` and `NSURLHandle` to download from FTP sites without subclassing.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Loading resource data

- [Status](nsurlhandle/status-swift.enum.md) — These following constants are defined by `NSURLHandle` and are returned by [status](nsurlhandle/status-c.method.md).
