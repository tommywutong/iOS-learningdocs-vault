---
title: difference
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdiffabledatasourcesectiontransaction-c.class/difference
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectiontransaction-c.class/difference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesectiontransaction-c.class/difference.json'
content_hash: 'sha256:9b6d848350fd0742'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSectionTransaction](../nsdiffabledatasourcesectiontransaction-c.class.md)

# difference

<sub>Instance Property</sub>

A collection of insertions and removals that describe the difference between initial and final section snapshots.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) NSOrderedCollectionDifference<id> * difference;
```

## See Also

### Accessing a transaction’s information

- [sectionIdentifier](sectionidentifier.md) — The identifier of the section for the transaction.
- [initialSnapshot](initialsnapshot.md) — The section snapshot before the transaction occured.
- [finalSnapshot](finalsnapshot.md) — The section snapshot after the transaction occured.
