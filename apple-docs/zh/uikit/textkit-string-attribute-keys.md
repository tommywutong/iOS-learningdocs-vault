---
title: TextKit 字符串属性键
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/textkit-string-attribute-keys
source_url: 'https://developer.apple.com/documentation/uikit/textkit-string-attribute-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/textkit-string-attribute-keys.json'
content_hash: 'sha256:0a58a318d377a00c'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [TextKit](textkit.md) · [TextKit string attributes](textkit-string-attributes.md)

# TextKit 字符串属性键

<sub>API 集合</sub>

用于为属性字符串中的字符范围应用属性的 UIKit 专属键。

## 概述

UIKit 定义了这些属性键，供你在 [NSAttributedString](../foundation/nsattributedstring.md) 和 [NSMutableAttributedString](../foundation/nsmutableattributedstring.md) 中指定属性值时使用。

## 主题

### Getting rendering attribute keys

- [NSBackgroundColorAttributeName](nsbackgroundcolorattributename.md) — 文本背后背景的颜色。
- [NSBaselineOffsetAttributeName](nsbaselineoffsetattributename.md) — 文本位置的垂直偏移量。
- [NSFontAttributeName](nsfontattributename.md) — 文本的字体。
- [NSForegroundColorAttributeName](nsforegroundcolorattributename.md) — 文本的颜色。
- [NSKernAttributeName](nskernattributename.md) — 文本的字距调整。
- [NSLigatureAttributeName](nsligatureattributename.md) — 文本的连字。
- [NSParagraphStyleAttributeName](nsparagraphstyleattributename.md) — 文本的段落样式。
- [NSStrikethroughColorAttributeName](nsstrikethroughcolorattributename.md) — 删除线的颜色。
- [NSStrikethroughStyleAttributeName](nsstrikethroughstyleattributename.md) — 文本的删除线样式。
- [NSStrokeColorAttributeName](nsstrokecolorattributename.md) — 描边的颜色。
- [NSStrokeWidthAttributeName](nsstrokewidthattributename.md) — 描边的宽度。
- [NSTrackingAttributeName](nstrackingattributename.md) — 修改默认字符间距的量。
- [NSUnderlineColorAttributeName](nsunderlinecolorattributename.md) — 下划线的颜色。
- [NSUnderlineStyleAttributeName](nsunderlinestyleattributename.md) — 文本的下划线样式。
- [NSWritingDirectionAttributeName](nswritingdirectionattributename.md) — 文本的书写方向。

### Getting text attribute keys

- [NSLinkAttributeName](nslinkattributename.md) — 文本的链接。
- [NSShadowAttributeName](nsshadowattributename.md) — 文本的阴影。
- [NSTextEffectAttributeName](nstexteffectattributename.md) — 一个用于为文本应用文本效果的属性。
- [NSTextHighlightColorSchemeAttributeName](nstexthighlightcolorschemeattributename.md) — 要应用于文本的自定义高亮颜色。
- [NSTextHighlightStyleAttributeName](nstexthighlightstyleattributename.md) — 一个用于为文本添加高亮颜色以强调该文本的属性。
- [UITextItemTagAttributeName](uitextitemtagattributename.md) — 与某个文本项关联的自定义标记的名称。
- [NSWritingToolsExclusionAttributeName](nswritingtoolsexclusionattributename.md)

### Getting attachment attribute keys

- [NSAdaptiveImageGlyphAttributeName](nsadaptiveimageglyphattributename.md) — 文本的自适应图像字形。
- [NSAttachmentAttributeName](nsattachmentattributename.md) — 文本的附件。

### Getting accessibility attribute keys

- [UIAccessibilitySpeechAttributeAnnouncementPriority](uiaccessibilityspeechattributeannouncementpriority.md)
- [UIAccessibilitySpeechAttributeIPANotation](uiaccessibilityspeechattributeipanotation.md) — 一个键，指示特定单词或短语（例如专有名称）的发音方式。
- [UIAccessibilitySpeechAttributeLanguage](uiaccessibilityspeechattributelanguage.md) — 一个键，指示朗读字符串时使用的语言。
- [UIAccessibilitySpeechAttributePitch](uiaccessibilityspeechattributepitch.md) — 一个键，指示应用于朗读内容的音高。
- [UIAccessibilitySpeechAttributePunctuation](uiaccessibilityspeechattributepunctuation.md) — 一个键，指示是否朗读标点符号。
- [UIAccessibilitySpeechAttributeQueueAnnouncement](uiaccessibilityspeechattributequeueannouncement.md) — 一个键，指示某条播报是排在现有语音之后，还是打断现有语音。
- [UIAccessibilitySpeechAttributeSpellOut](uiaccessibilityspeechattributespellout.md)
- [UIAccessibilityTextAttributeCustom](uiaccessibilitytextattributecustom.md) — 用于指定要应用到文本上的自定义属性的键。
- [UIAccessibilityTextAttributeHeadingLevel](uiaccessibilitytextattributeheadinglevel.md) — 用于指定文本标题级别的键。
- [UIAccessibilityTextAttributeContext](uiaccessibilitytextattributecontext.md)

### Deprecated keys

- [NSExpansionAttributeName](nsexpansionattributename.md) — 文本的扩展因子。_(已废弃)_
- [NSObliquenessAttributeName](nsobliquenessattributename.md) — 文本的倾斜度。_(已废弃)_
- [NSVerticalGlyphFormAttributeName](nsverticalglyphformattributename.md) — 文本的竖排字形形式。_(已废弃)_

## 另请参阅

### Getting text content attributes

- [NSTextHighlightStyle](nstexthighlightstyle.md) — 指定要应用于文本的高亮类型的常量。
- [NSTextHighlightColorScheme](nstexthighlightcolorscheme.md) — 指定要用于文本的高亮颜色的常量。
- [NSTextEffectStyle](nstexteffectstyle.md) — 指定要应用于文本的效果类型的常量。
- [NSUnderlineStyle](nsunderlinestyle.md) — 用于下划线样式和删除线样式属性键的常量。
- [NSWritingDirectionFormatType](nswritingdirectionformattype.md) — 用于书写方向属性键的常量。
