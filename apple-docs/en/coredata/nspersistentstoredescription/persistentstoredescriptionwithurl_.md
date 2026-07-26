---
title: 'persistentStoreDescriptionWithURL:'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstoredescription/persistentstoredescriptionwithurl:'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoredescription/persistentstoredescriptionwithurl:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoredescription/persistentstoredescriptionwithurl%3A.json'
content_hash: 'sha256:03cd222110b0cf7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreDescription](../nspersistentstoredescription.md)

# persistentStoreDescriptionWithURL:

<sub>Type Method</sub>

Initializes and returns a persistent store description with the given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) persistentStoreDescriptionWithURL:(NSURL *) URL;
```

## Parameters

- `URL` — Location for the store.

## Return Value

Initialized [NSPersistentStoreDescription](../nspersistentstoredescription.md) configured with the given URL.

## Discussion

This method is a convenience for creating a new [NSPersistentStoreDescription](../nspersistentstoredescription.md) configured with a given URL.

## See Also

### Creating a Persistent Store Description

- [- initWithURL:](<init(url_)-ko0l.md>) — Initializes the receiver with a URL for the store.
