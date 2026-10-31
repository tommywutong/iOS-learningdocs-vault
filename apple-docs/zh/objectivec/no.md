---
title: NO
framework: Objective-C Runtime
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/no
source_url: 'https://developer.apple.com/documentation/objectivec/no'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/no.json'
content_hash: 'sha256:46b659c21d3cd3e9'
translated: true
---


> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# NO

<sub>宏</sub>

将 `NO` 定义为 `0`。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define NO
```

## 讨论

Objective-C 中的 `NO` 宏会桥接到 Swift，成为值为 `false` 的 [ObjCBool](objcbool.md)。

## 另请参阅

### 常量

- [YES](yes.md) — Defines `YES` as `1`.
