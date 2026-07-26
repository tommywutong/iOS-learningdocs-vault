---
title: loadMetadata()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsincrementalstore/loadmetadata()
source_url: 'https://developer.apple.com/documentation/coredata/nsincrementalstore/loadmetadata()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsincrementalstore/loadmetadata%28%29.json'
content_hash: 'sha256:0f9f576e2b3efcf9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSIncrementalStore](../nsincrementalstore.md)

# loadMetadata()

<sub>Instance Method</sub>

Loads the metadata for the store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadMetadata() throws
```

## Discussion

In your implementation of this method, you must validate that the URL used to create the store is usable (the location exists and if necessary is writable, the schema is compatible, and so on) and return an error if there is an issue.

Any subclass of `NSIncrementalStore` which is file-based must be able to handle being initialized with a URL pointing to a zero-length file. This serves as an indicator that a new store is to be constructed at the specified location and allows applications using the store to securely create reservation files in known locations.

## See Also

### Related Documentation

- [Incremental Store Programming Guide](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/IncrementalStorePG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010706)

### Accessing Metadata

- [+ identifierForNewStoreAtURL:](<identifierfornewstore(at_).md>) — Returns the identifier for the store at a given URL.
