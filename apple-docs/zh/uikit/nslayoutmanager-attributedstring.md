---
title: attributedString
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutmanager-attributedstring
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager-attributedstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager-attributedstring.json'
content_hash: 'sha256:9b44b0eedf1c089a'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [TextKit](textkit.md) · [NSLayoutManager](nslayoutmanager.md) · [已废弃符号](nslayoutmanager-deprecated-symbols.md)

# attributedString

<sub>文章</sub>

`NSGlyphGenerator` 对象从中获取字符以生成字形的文本存储对象。

## 概述

**Swift**

```swift
var attributedString: NSAttributedString? { get }
```

**Objective-C**

```objc
@property(readonly, strong) NSAttributedString *attributedString
```

此属性属于 `NSGlyphStorage` 协议，供字形生成器使用。对于 `NSLayoutManager`，属性字符串等同于文本存储。

## 另请参阅

### 属性

- [hyphenationFactor](nslayoutmanager/hyphenationfactor.md) — 控制何时进行连字符处理的阈值。_(已废弃)_
- [layoutOptions](nslayoutmanager-layoutoptions.md) — 布局管理器当前的布局选项。
- [usesScreenFonts](../appkit/nslayoutmanager/usesscreenfonts.md) — 控制是否使用屏幕字体来计算布局和显示文本的布尔值。_(已废弃)_
