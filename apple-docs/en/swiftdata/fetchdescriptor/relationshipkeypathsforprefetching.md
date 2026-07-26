---
title: relationshipKeyPathsForPrefetching
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/fetchdescriptor/relationshipkeypathsforprefetching
source_url: 'https://developer.apple.com/documentation/swiftdata/fetchdescriptor/relationshipkeypathsforprefetching'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/fetchdescriptor/relationshipkeypathsforprefetching.json'
content_hash: 'sha256:0d4c79d5c69bdc1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [FetchDescriptor](../fetchdescriptor.md)

# relationshipKeyPathsForPrefetching

<sub>Instance Property</sub>

The key paths that identify any related models to include as part of the fetch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var relationshipKeyPathsForPrefetching: [PartialKeyPath<T>]
```

## Discussion

Prefetching enables SwiftData to obtain any related models in a single fetch, instead of incurring subsequent access to the persistent storage as you access each related model.

For example, given an `Employee` model with a relationship to a `Department` model, and suppose you fetch all employees as you want to display both their name and the name of the department where they work. In such a scenario, the model context may need to perform additional fetches for each individual department, resulting in significant overhead. You can avoid this by prefetching the department relationship as part of the employee fetch.

The default value is an empty array.

## See Also

### Specifying the fetched attributes

- [propertiesToFetch](propertiestofetch.md) — The specific subset of attributes to fetch if you don’t require them all.
