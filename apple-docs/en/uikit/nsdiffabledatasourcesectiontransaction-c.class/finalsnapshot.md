---
title: finalSnapshot
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdiffabledatasourcesectiontransaction-c.class/finalsnapshot
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectiontransaction-c.class/finalsnapshot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesectiontransaction-c.class/finalsnapshot.json'
content_hash: 'sha256:a2d269a59032d9a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSectionTransaction](../nsdiffabledatasourcesectiontransaction-c.class.md)

# finalSnapshot

<sub>Instance Property</sub>

The section snapshot after the transaction occured.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) NSDiffableDataSourceSectionSnapshot<id> * finalSnapshot;
```

## See Also

### Accessing a transaction’s information

- [sectionIdentifier](sectionidentifier.md) — The identifier of the section for the transaction.
- [initialSnapshot](initialsnapshot.md) — The section snapshot before the transaction occured.
- [difference](difference.md) — A collection of insertions and removals that describe the difference between initial and final section snapshots.
