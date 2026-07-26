---
title: objc_AssociationPolicy
framework: Objective-C Runtime
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_associationpolicy
source_url: 'https://developer.apple.com/documentation/objectivec/objc_associationpolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_associationpolicy.json'
content_hash: 'sha256:d4fa5a999bef6573'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_AssociationPolicy

<sub>Enumeration</sub>

Type to specify the behavior of an association.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum objc_AssociationPolicy
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md)

## Topics

### Enumeration Cases

- [OBJC_ASSOCIATION_ASSIGN](objc_associationpolicy/objc_association_assign.md) — Specifies an unsafe unretained reference to the associated object.
- [OBJC_ASSOCIATION_COPY](objc_associationpolicy/objc_association_copy.md) — Specifies that the associated object is copied, and that the association is made atomically.
- [OBJC_ASSOCIATION_COPY_NONATOMIC](objc_associationpolicy/objc_association_copy_nonatomic.md) — Specifies that the associated object is copied, and that the association is not made atomically.
- [OBJC_ASSOCIATION_RETAIN](objc_associationpolicy/objc_association_retain.md) — Specifies a strong reference to the associated object, and that the association is made atomically.
- [OBJC_ASSOCIATION_RETAIN_NONATOMIC](objc_associationpolicy/objc_association_retain_nonatomic.md) — Specifies a strong reference to the associated object, and that the association is not made atomically.

### Initializers

- [init(rawValue:)](<objc_associationpolicy/init(rawvalue_).md>)
