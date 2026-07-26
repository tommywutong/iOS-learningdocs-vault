---
title: 'init(path:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdistributedlock/init(path:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdistributedlock/init(path:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdistributedlock/init%28path%3A%29.json'
content_hash: 'sha256:6eac869b4532a7a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDistributedLock](../nsdistributedlock.md)

# init(path:)

<sub>Initializer</sub>

Initializes an `NSDistributedLock` object to use as the lock the file-system entry specified by a given path.

<sub>Mac Catalyst, macOS</sub>

```swift
init?(path: String)
```

## Parameters

- `path` — All of `path` up to the last component itself must exist. You can use [FileManager](../filemanager.md) to create (and set permissions) for any nonexistent intermediate directories.

## Return Value

An `NSDistributedLock` object initialized to use as the locking object the file-system entry specified by `path`.

## Discussion

For applications to use the lock, `path` must be accessible to—and writable by—all hosts on which the applications might be running.
