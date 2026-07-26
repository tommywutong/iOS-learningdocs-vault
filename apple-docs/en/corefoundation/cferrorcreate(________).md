---
title: 'CFErrorCreate(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cferrorcreate(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cferrorcreate(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cferrorcreate%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:fa08b37a8741d62b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFErrorCreate(_:_:_:_:)

<sub>Function</sub>

Creates a new CFError object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFErrorCreate(_ allocator: CFAllocator!, _ domain: CFErrorDomain!, _ code: CFIndex, _ userInfo: CFDictionary!) -> CFError!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `domain` — A CFString that identifies the error domain. If this reference is `NULL` or is otherwise not a valid CFString, the behavior is undefined.

- `code` — A CFIndex that identifies the error code. The code is interpreted within the context of the error domain.

- `userInfo` — A CFDictionary created with [kCFCopyStringDictionaryKeyCallBacks](kcfcopystringdictionarykeycallbacks.md) and [kCFTypeDictionaryValueCallBacks](kcftypedictionaryvaluecallbacks.md). The dictionary is copied with [CFDictionaryCreateCopy](<cfdictionarycreatecopy(____).md>). If you do not want the userInfo dictionary, you can pass `NULL`, in which case an empty dictionary will be assigned.

## Return Value

A new CFError object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a CFError

- [CFErrorCreateWithUserInfoKeysAndValues](<cferrorcreatewithuserinfokeysandvalues(____________).md>) — Creates a new CFError object using given keys and values to create the user info dictionary.
