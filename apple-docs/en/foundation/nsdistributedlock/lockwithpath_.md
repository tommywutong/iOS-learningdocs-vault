---
title: 'lockWithPath:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdistributedlock/lockwithpath:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdistributedlock/lockwithpath:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdistributedlock/lockwithpath%3A.json'
content_hash: 'sha256:cdaeb71573d1a088'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDistributedLock](../nsdistributedlock.md)

# lockWithPath:

<sub>Type Method</sub>

Returns an `NSDistributedLock` object initialized to use as the locking object the file-system entry specified by a given path.

<sub>Mac Catalyst, macOS</sub>

```objc
+ (NSDistributedLock *) lockWithPath:(NSString *) path;
```

## Parameters

- `path` — All of `path` up to the last component itself must exist. You can use [FileManager](../filemanager.md) to create (and set permissions) for any nonexistent intermediate directories.

## Return Value

An `NSDistributedLock` object initialized to use as the locking object the file-system entry specified by `path`.

## Discussion

For applications to use the lock, `path` must be accessible to—and writable by—all hosts on which the applications might be running.

## See Also

### Related Documentation

- [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)

### Creating an NSDistributedLock

- [- initWithPath:](<init(path_).md>) — Initializes an `NSDistributedLock` object to use as the lock the file-system entry specified by a given path.
