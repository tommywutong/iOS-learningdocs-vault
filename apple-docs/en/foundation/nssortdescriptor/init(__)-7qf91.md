---
title: 'init(_:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+（17.0 起废弃）, iPadOS 15.0+（17.0 起废弃）, Mac Catalyst 15.0+（17.0 起废弃）, macOS 12.0+（14.0 起废弃）, tvOS 15.0+（17.0 起废弃）, visionOS 1.0+, watchOS 8.0+（10.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nssortdescriptor/init(_:)-7qf91'
source_url: 'https://developer.apple.com/documentation/foundation/nssortdescriptor/init(_:)-7qf91'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssortdescriptor/init%28_%3A%29-7qf91.json'
content_hash: 'sha256:a0d317043e654941'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSortDescriptor](../nssortdescriptor.md)

# init(_:)

<sub>Initializer</sub>

Creates a sort descriptor using a sort descriptor you specify.

> [!warning] Deprecated
> Use `init(_:) where Compared: NSObject` instead. Attempt to convert SortDescriptor with Compared being non-NSObject will result in a fatalError at runtime.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init<Compared>(_ sortDescriptor: SortDescriptor<Compared>)
```

## Parameters

- `sortDescriptor` — A sort descriptor.

## See Also

### Creating a Sort Descriptor

- [- initWithKey:ascending:](<init(key_ascending_).md>) — Creates a sort descriptor with a specified string key path and sort order.
- [- initWithKey:ascending:selector:](<init(key_ascending_selector_).md>) — Creates a sort descriptor with a specified string key path, ordering, and comparison selector.
- [init(keyPath:ascending:)](<init(keypath_ascending_).md>) — Creates a sort descriptor with a specified key path and ordering.
- [- initWithKey:ascending:comparator:](<init(key_ascending_comparator_).md>) — Creates a sort descriptor with a specified string key path and ordering, and a comparator block.
- [init(keyPath:ascending:comparator:)](<init(keypath_ascending_comparator_).md>) — Creates a sort descriptor with a specified key path and ordering, and a comparator block.
- [- initWithCoder:](<init(coder_).md>) — Creates a sort descriptor by decoding from the coder you specify.
