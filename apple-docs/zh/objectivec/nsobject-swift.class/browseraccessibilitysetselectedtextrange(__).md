---
title: 'browserAccessibilitySetSelectedTextRange(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, macOS, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/browseraccessibilitysetselectedtextrange(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/browseraccessibilitysetselectedtextrange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/browseraccessibilitysetselectedtextrange%28_%3A%29.json'
content_hash: 'sha256:2e6ad7f7bcad24e4'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# browserAccessibilitySetSelectedTextRange(_:)

<sub>实例方法</sub>

更新元素的选中文本。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func browserAccessibilitySetSelectedTextRange(_ range: NSRange)
```

## 参数

- `range` — 元素文本中要选择的范围。

## 另请参阅

### 改进浏览器辅助功能

- [- browserAccessibilityAttributedValueInRange:](<browseraccessibilityattributedvalue(in_).md>) — 以归因字符串形式返回此元素在给定范围内的值。
- [- browserAccessibilityDeleteTextAtCursor:](<browseraccessibilitydeletetextatcursor(numberofcharacters_).md>) — 从元素的当前光标位置删除文本。
- [- browserAccessibilityInsertTextAtCursor:](<browseraccessibilityinserttextatcursor(text_).md>) — 在元素的当前光标位置插入文本。
- [- browserAccessibilitySelectedTextRange](<browseraccessibilityselectedtextrange().md>) — 返回元素中选中文本的范围。
- [- browserAccessibilityValueInRange:](<browseraccessibilityvalue(in_).md>) — 返回此元素在给定范围内的值。
- [browserAccessibilityContainerType](browseraccessibilitycontainertype.md) — 包含此元素的容器种类。
- [browserAccessibilityCurrentStatus](browseraccessibilitycurrentstatus.md) — 作为元素 aria-current 值的字符串。
- [browserAccessibilityHasDOMFocus](browseraccessibilityhasdomfocus.md) — 一个布尔值，指示元素在浏览器文档对象模型中是否具有原生焦点。
- [browserAccessibilityIsRequired](browseraccessibilityisrequired.md) — 作为元素 aria-required 值的布尔值。
- [browserAccessibilityPressedState](browseraccessibilitypressedstate.md) — 元素的 aria-pressed 值。
- [browserAccessibilityRoleDescription](browseraccessibilityroledescription.md) — 描述元素对辅助技术角色的字符串。
- [browserAccessibilitySortDirection](browseraccessibilitysortdirection.md) — 作为元素 aria-sort 值的字符串。
