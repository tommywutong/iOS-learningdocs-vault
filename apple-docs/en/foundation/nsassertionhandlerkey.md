---
title: NSAssertionHandlerKey
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsassertionhandlerkey
source_url: 'https://developer.apple.com/documentation/foundation/nsassertionhandlerkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsassertionhandlerkey.json'
content_hash: 'sha256:41f7cfc9b3d6d0da'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSAssertionHandlerKey

<sub>Global Variable</sub>

A key with a corresponding value in the thread dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSAssertionHandlerKey: String
```

## Discussion

If you need to customize the behavior of `NSAssertionHandler`, create a subclass, overriding [handleFailureInMethod:object:file:lineNumber:description:](nsassertionhandler/handlefailureinmethod_object_file_linenumber_description_.md) and [handleFailureInFunction:file:lineNumber:description:](nsassertionhandler/handlefailureinfunction_file_linenumber_description_.md), and install your instance into the current thread’s attributes dictionary with this key.

## See Also

### Working with Thread Properties

- [threadDictionary](thread/threaddictionary.md) — The thread object’s dictionary.
- [name](thread/name.md) — The name of the receiver.
- [stackSize](thread/stacksize.md) — The stack size of the receiver, in bytes.
