---
title: homeDirectory
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/homedirectory
source_url: 'https://developer.apple.com/documentation/foundation/url/homedirectory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/homedirectory.json'
content_hash: 'sha256:7657bb392d26a44e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# homeDirectory

<sub>Type Property</sub>

The home directory for the current user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var homeDirectory: URL { get }
```

## Discussion

This URL is the equivalent of the shell value `~/`.

Complexity: `O(1)`.

## See Also

### Accessing home and user directories

- [currentDirectory()](<currentdirectory().md>) — Returns the working directory of the current process.
- [homeDirectory(forUser:)](<homedirectory(foruser_).md>) — Returns the home directory for the specified user.
