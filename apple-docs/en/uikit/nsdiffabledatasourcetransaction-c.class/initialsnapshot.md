---
title: initialSnapshot
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdiffabledatasourcetransaction-c.class/initialsnapshot
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcetransaction-c.class/initialsnapshot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcetransaction-c.class/initialsnapshot.json'
content_hash: 'sha256:ce45cdca96151a26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceTransaction](../nsdiffabledatasourcetransaction-c.class.md)

# initialSnapshot

<sub>Instance Property</sub>

The snapshot before the transaction occured.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) NSDiffableDataSourceSnapshot<id,id> * initialSnapshot;
```

## See Also

### Accessing a transaction’s information

- [sectionTransactions](sectiontransactions.md) — An array of section transactions for the transaction.
- [finalSnapshot](finalsnapshot.md) — The snapshot after the transaction occured.
- [difference](difference.md) — A collection of insertions and removals that describe the difference between initial and final snapshots.
