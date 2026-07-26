---
title: currentDirectory()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/currentdirectory()
source_url: 'https://developer.apple.com/documentation/foundation/url/currentdirectory()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/currentdirectory%28%29.json'
content_hash: 'sha256:92f8bbedf653ba78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# currentDirectory()

<sub>Type Method</sub>

Returns the working directory of the current process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func currentDirectory() -> URL
```

## Return Value

Calling this method issues a `getcwd` system call. This method’s return value can change between calls because any thread can change the process’s current working directory at any time. Take precautions when reasoning about the current directory in a multithreaded environment.

## See Also

### Accessing home and user directories

- [homeDirectory](homedirectory.md) — The home directory for the current user.
- [homeDirectory(forUser:)](<homedirectory(foruser_).md>) — Returns the home directory for the specified user.
