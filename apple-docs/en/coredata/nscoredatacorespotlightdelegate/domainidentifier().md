---
title: domainIdentifier()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nscoredatacorespotlightdelegate/domainidentifier()
source_url: 'https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/domainidentifier()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nscoredatacorespotlightdelegate/domainidentifier%28%29.json'
content_hash: 'sha256:03f6e73fc70a3c54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSCoreDataCoreSpotlightDelegate](../nscoredatacorespotlightdelegate.md)

# domainIdentifier()

<sub>Instance Method</sub>

Returns the domain identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func domainIdentifier() -> String
```

## Discussion

The default value is the persistent store’s identifier.

## See Also

### Configuring the Index

- [indexingEnabled](isindexingenabled.md) — A Boolean value that indicates whether Core Data is currently updating the Core Spotlight index with the persistent store’s entities.
- [- indexName](<indexname().md>) — Returns the index’s name.
