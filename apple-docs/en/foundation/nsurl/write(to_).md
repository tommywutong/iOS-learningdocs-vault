---
title: 'write(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurl/write(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/write(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/write%28to%3A%29.json'
content_hash: 'sha256:ad84364077dcae5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# write(to:)

<sub>Instance Method</sub>

Writes the URL to the specified pasteboard.

<sub>macOS</sub>

```swift
func write(to pasteBoard: NSPasteboard)
```

## Parameters

- `pasteBoard` — The target pasteboard.

## Discussion

You must declare an `NSURLPboardType` data type for the pasteboard before invoking this method. Otherwise, the method returns without doing anything.

## See Also

### Related Documentation

- [declareTypes(_:owner:)](<../../appkit/nspasteboard/declaretypes(__owner_).md>) — Prepares the receiver for a change in its contents by declaring the new types of data it will contain and a new owner.

### Working with Pasteboards

- [+ URLFromPasteboard:](<init(frompasteboard_).md>) — Reads an NSURL object off of the specified pasteboard.
