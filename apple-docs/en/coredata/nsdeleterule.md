---
title: NSDeleteRule
framework: Core Data
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsdeleterule
source_url: 'https://developer.apple.com/documentation/coredata/nsdeleterule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsdeleterule.json'
content_hash: 'sha256:e10252813e1dcbe3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSDeleteRule

<sub>Enumeration</sub>

Constants that determine what happens when you delete a relationship’s owning managed object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NSDeleteRule
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Delete Rules

- [NSNoActionDeleteRule](nsdeleterule/noactiondeleterule.md) — A rule that prevents modification of the referenced managed objects.
- [NSNullifyDeleteRule](nsdeleterule/nullifydeleterule.md) — A rule that nullifies the inverse relationship of the referenced managed objects.
- [NSCascadeDeleteRule](nsdeleterule/cascadedeleterule.md) — A rule that deletes the referenced managed objects.
- [NSDenyDeleteRule](nsdeleterule/denydeleterule.md) — A rule that prevents the deletion of the owning managed object if the relationship has references to other objects.

### Initializers

- [init(rawValue:)](<nsdeleterule/init(rawvalue_).md>)

## See Also

### Configuring Delete Behavior

- [deleteRule](nsrelationshipdescription/deleterule.md) — The rule to apply when you delete the relationship’s owning managed object.
