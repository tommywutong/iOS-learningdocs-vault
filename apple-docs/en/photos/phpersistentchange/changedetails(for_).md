---
title: 'changeDetails(for:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phpersistentchange/changedetails(for:)'
source_url: 'https://developer.apple.com/documentation/photos/phpersistentchange/changedetails(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phpersistentchange/changedetails%28for%3A%29.json'
content_hash: 'sha256:64abb3ca53d1990d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPersistentChange](../phpersistentchange.md)

# changeDetails(for:)

<sub>Instance Method</sub>

Returns the change history that contains the local identifiers for object inserts, updates, and deletes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func changeDetails(for objectType: PHObjectType) throws -> PHPersistentObjectChangeDetails
```

## Parameters

- `objectType` — The type of object to request change details for.

## Return Value

An object that represents the change details.

## See Also

### Getting the Change History

- [PHPersistentObjectChangeDetails](../phpersistentobjectchangedetails.md) — An object that represents the local identifiers that change between requests using a change token.
