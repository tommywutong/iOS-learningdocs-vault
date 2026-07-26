---
title: 'init(fromPasteboard:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurl/init(frompasteboard:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/init(frompasteboard:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/init%28frompasteboard%3A%29.json'
content_hash: 'sha256:ac515202e69072d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# init(fromPasteboard:)

<sub>Initializer</sub>

Reads an NSURL object off of the specified pasteboard.

<sub>macOS</sub>

```swift
init?(fromPasteboard pasteBoard: NSPasteboard)
```

<sub>macOS</sub>

```swift
init?(from pasteBoard: NSPasteboard)
```

## Parameters

- `pasteBoard` — The target pasteboard.

## Return Value

A `NSURL` object, or `nil` if the pasteboard does not contain `NSURLPboardType` data.

## See Also

### Working with Pasteboards

- [- writeToPasteboard:](<write(to_).md>) — Writes the URL to the specified pasteboard.
