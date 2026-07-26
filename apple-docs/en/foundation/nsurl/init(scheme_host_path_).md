---
title: 'init(scheme:host:path:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.11 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurl/init(scheme:host:path:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/init(scheme:host:path:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/init%28scheme%3Ahost%3Apath%3A%29.json'
content_hash: 'sha256:153aef2dae07728e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# init(scheme:host:path:)

<sub>Initializer</sub>

Initializes a newly created NSURL with a specified scheme, host, and path.

> [!warning] Deprecated
> Use NSURLComponents instead, which lets you create a valid URL with any valid combination of URL components and subcomponents (not just scheme, host and path), and lets you set components and subcomponents with either percent-encoded or un-percent-encoded strings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(scheme: String, host: String?, path: String)
```

## Parameters

- `scheme` — The scheme for the NSURL object. For example, in the URL `http://www.example.com/index.html`, the scheme is `http`.

- `host` — The host for the NSURL object (for example, `www.example.com`). May be the empty string.

- `path` — The path for the NSURL object (for example, `/index.html`). If the path begins with a tilde, you must first expand it by calling [stringByExpandingTildeInPath](../nsstring/expandingtildeinpath.md).

## Return Value

The newly initialized NSURL object.

## Discussion

This method automatically uses percent encoding to escape the `path` and `host` parameters.

## See Also

### Related Documentation

- [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672)
- [URL Loading System](../url-loading-system.md) — Interact with URLs and communicate with servers using standard Internet protocols.
