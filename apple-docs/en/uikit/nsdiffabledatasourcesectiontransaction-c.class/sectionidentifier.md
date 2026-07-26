---
title: sectionIdentifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdiffabledatasourcesectiontransaction-c.class/sectionidentifier
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectiontransaction-c.class/sectionidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesectiontransaction-c.class/sectionidentifier.json'
content_hash: 'sha256:3bc21b0ae418f032'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSectionTransaction](../nsdiffabledatasourcesectiontransaction-c.class.md)

# sectionIdentifier

<sub>Instance Property</sub>

The identifier of the section for the transaction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) SectionIdentifierType sectionIdentifier;
```

## See Also

### Accessing a transaction’s information

- [initialSnapshot](initialsnapshot.md) — The section snapshot before the transaction occured.
- [finalSnapshot](finalsnapshot.md) — The section snapshot after the transaction occured.
- [difference](difference.md) — A collection of insertions and removals that describe the difference between initial and final section snapshots.
