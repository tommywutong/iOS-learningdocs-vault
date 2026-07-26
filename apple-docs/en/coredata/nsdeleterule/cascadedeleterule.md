---
title: NSDeleteRule.cascadeDeleteRule
framework: Core Data
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsdeleterule/cascadedeleterule
source_url: 'https://developer.apple.com/documentation/coredata/nsdeleterule/cascadedeleterule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsdeleterule/cascadedeleterule.json'
content_hash: 'sha256:06eecdc43fad3890'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSDeleteRule](../nsdeleterule.md)

# NSDeleteRule.cascadeDeleteRule

<sub>Case</sub>

A rule that deletes the referenced managed objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case cascadeDeleteRule
```

## See Also

### Delete Rules

- [NSNoActionDeleteRule](noactiondeleterule.md) — A rule that prevents modification of the referenced managed objects.
- [NSNullifyDeleteRule](nullifydeleterule.md) — A rule that nullifies the inverse relationship of the referenced managed objects.
- [NSDenyDeleteRule](denydeleterule.md) — A rule that prevents the deletion of the owning managed object if the relationship has references to other objects.
