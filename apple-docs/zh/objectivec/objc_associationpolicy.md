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
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_AssociationPolicy

<sub>枚举</sub>

用于指定关联行为的类型。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum objc_AssociationPolicy
```

## 关系

- **符合**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md)

## 主题

### 枚举 case

- [OBJC_ASSOCIATION_ASSIGN](objc_associationpolicy/objc_association_assign.md) — 指定对关联对象的不安全非保留引用。
- [OBJC_ASSOCIATION_COPY](objc_associationpolicy/objc_association_copy.md) — 指定关联对象被拷贝，且关联以原子方式建立。
- [OBJC_ASSOCIATION_COPY_NONATOMIC](objc_associationpolicy/objc_association_copy_nonatomic.md) — 指定关联对象被拷贝，且关联不以原子方式建立。
- [OBJC_ASSOCIATION_RETAIN](objc_associationpolicy/objc_association_retain.md) — 指定对关联对象的强引用，且关联以原子方式建立。
- [OBJC_ASSOCIATION_RETAIN_NONATOMIC](objc_associationpolicy/objc_association_retain_nonatomic.md) — 指定对关联对象的强引用，且关联不以原子方式建立。

### 初始化方法

- [init(rawValue:)](<objc_associationpolicy/init(rawvalue_).md>)
