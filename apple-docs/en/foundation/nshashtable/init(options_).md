---
title: 'init(options:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nshashtable/init(options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nshashtable/init(options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashtable/init%28options%3A%29.json'
content_hash: 'sha256:8f211f1259bde55f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSHashTable](../nshashtable.md)

# init(options:)

<sub>Initializer</sub>

Returns a hash table with given pointer functions options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(options: NSPointerFunctions.Options = [])
```

## Parameters

- `options` — A bit field that specifies the options for the elements in the hash table. For possible values, see [NSHashTableOptions](../nshashtableoptions.md).

## Return Value

A hash table with given pointer functions options.

## See Also

### Convenience Constructors

- [+ weakObjectsHashTable](<weakobjects().md>) — Returns a new hash table for storing weak references to its contents.
