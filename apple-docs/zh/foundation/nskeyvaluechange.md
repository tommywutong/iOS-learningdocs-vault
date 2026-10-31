---
title: NSKeyValueChange
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyvaluechange
source_url: 'https://developer.apple.com/documentation/foundation/nskeyvaluechange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyvaluechange.json'
content_hash: 'sha256:19740c3c2a8f624a'
translated: true
---

> 导航： [技术](../technologies.md) · [Foundation](../foundation.md)

# NSKeyValueChange

<sub>枚举</sub>

可以被观察到的变化种类。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NSKeyValueChange
```

## 概述

这些常量作为传递给 [observeValue(forKeyPath:of:change:context:)](<../objectivec/nsobject-swift.class/observevalue(forkeypath_of_change_context_).md>) 的变化字典中 [NSKeyValueChangeKindKey](nskeyvaluechangekey/kindkey.md) 键的值返回，用于指示所做变化的类型。

## 关系

- **遵循**：[BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## 主题

### 常量

- [NSKeyValueChangeSetting](nskeyvaluechange/setting.md) — 表示被观察键路径的值已设置为新值。这种变化可在观察对象的属性时发生，也可在观察指定一对一和一对多关系的属性时发生。
- [NSKeyValueChangeInsertion](nskeyvaluechange/insertion.md) — 表示某个对象已插入到正在观察的一对多关系中。
- [NSKeyValueChangeRemoval](nskeyvaluechange/removal.md) — 表示某个对象已从正在观察的一对多关系中移除。
- [NSKeyValueChangeReplacement](nskeyvaluechange/replacement.md) — 表示正在观察的一对多关系中的某个对象已被替换。

### 初始化方法

- [init(rawValue:)](<nskeyvaluechange/init(rawvalue_).md>)

## 另请参阅

### 枚举

- [NSGrammaticalCase](nsgrammaticalcase.md)
- [NSGrammaticalDefiniteness](nsgrammaticaldefiniteness.md)
- [NSGrammaticalDetermination](nsgrammaticaldetermination.md)
- [NSGrammaticalPerson](nsgrammaticalperson.md)
- [NSGrammaticalPronounType](nsgrammaticalpronountype.md)
- [NSKeyValueObservingOptions](nskeyvalueobservingoptions.md) — 可在变化字典中返回的值。
- [NSKeyValueSetMutationKind](nskeyvaluesetmutationkind.md)
