---
title: hasLocalContents
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfileversion/haslocalcontents
source_url: 'https://developer.apple.com/documentation/foundation/nsfileversion/haslocalcontents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileversion/haslocalcontents.json'
content_hash: 'sha256:6dd35ca80e254faa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileVersion](../nsfileversion.md)

# hasLocalContents

<sub>Instance Property</sub>

Whether the version has local contents. Versions that are returned by +getNonlocalVersionsOfItemAtURL:completionHandler: do not initially have local contents. You can only access their contents, either directly via the URL or by invoking -replaceItemAtURL:options:error:, from within a coordinated read on the NSFileVersion’s URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hasLocalContents: Bool { get }
```
