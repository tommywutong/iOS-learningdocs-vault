---
title: layoutOptions
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutmanager-layoutoptions
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager-layoutoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager-layoutoptions.json'
content_hash: 'sha256:4637384f3b0bf0c3'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [TextKit](textkit.md) · [NSLayoutManager](nslayoutmanager.md) · [Deprecated symbols](nslayoutmanager-deprecated-symbols.md)

# layoutOptions

<sub>文章</sub>

布局管理器当前的布局选项。

## 概述

**Swift**

```swift
var layoutOptions: Int { get }
```

**Objective-C**

```objc
@property(readonly) NSUInteger layoutOptions
```

该属性是 `NSGlyphStorage` 协议的一部分，供字符图元生成器使用。它让字符图元生成器能够询问布局管理器请求了哪些选项。

## 另请参阅

### Properties

- [hyphenationFactor](nslayoutmanager/hyphenationfactor.md) — 控制何时执行断字的阈值。_(已废弃)_
- [attributedString](nslayoutmanager-attributedstring.md) — `NSGlyphGenerator` 对象据以获取字符、用于生成字符图元的文本存储对象。
- [usesScreenFonts](../appkit/nslayoutmanager/usesscreenfonts.md) — 一个布尔值，控制是否使用屏幕字体来计算布局和显示文本。_(已废弃)_
