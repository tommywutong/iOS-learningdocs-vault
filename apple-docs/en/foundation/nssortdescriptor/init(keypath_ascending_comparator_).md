---
title: 'init(keyPath:ascending:comparator:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nssortdescriptor/init(keypath:ascending:comparator:)'
source_url: 'https://developer.apple.com/documentation/foundation/nssortdescriptor/init(keypath:ascending:comparator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssortdescriptor/init%28keypath%3Aascending%3Acomparator%3A%29.json'
content_hash: 'sha256:dad1fc4935cdc6b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSortDescriptor](../nssortdescriptor.md)

# init(keyPath:ascending:comparator:)

<sub>Initializer</sub>

Creates a sort descriptor with a specified key path and ordering, and a comparator block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init<Root, Value>(keyPath: KeyPath<Root, Value>, ascending: Bool, comparator cmptr: @escaping Comparator)
```

## Parameters

- `keyPath` — The key path to the property to compare.

- `ascending` — If `true`, the sort descriptor compares using the [SortOrder.forward](../sortorder/forward.md) sort order; otherwise, it uses [SortOrder.reverse](../sortorder/reverse.md).

- `cmptr` — A comparator block.

## See Also

### Creating a Sort Descriptor

- [- initWithKey:ascending:](<init(key_ascending_).md>) — Creates a sort descriptor with a specified string key path and sort order.
- [- initWithKey:ascending:selector:](<init(key_ascending_selector_).md>) — Creates a sort descriptor with a specified string key path, ordering, and comparison selector.
- [init(keyPath:ascending:)](<init(keypath_ascending_).md>) — Creates a sort descriptor with a specified key path and ordering.
- [- initWithKey:ascending:comparator:](<init(key_ascending_comparator_).md>) — Creates a sort descriptor with a specified string key path and ordering, and a comparator block.
- [- initWithCoder:](<init(coder_).md>) — Creates a sort descriptor by decoding from the coder you specify.
- [init(_:)](<init(__)-7qf91.md>) — Creates a sort descriptor using a sort descriptor you specify. _(deprecated)_
