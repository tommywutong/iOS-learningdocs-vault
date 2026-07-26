---
title: 已废弃符号
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutmanager-deprecated-symbols
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager-deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager-deprecated-symbols.json'
content_hash: 'sha256:d4d1056292b44fc7'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [TextKit](textkit.md) · [NSLayoutManager](nslayoutmanager.md)

# 已废弃符号

<sub>API 集合</sub>

查看不再受支持的符号及其替代方案。

## 主题

### Methods

- [- showCGGlyphs:positions:count:font:matrix:attributes:inContext:](<nslayoutmanager/showcgglyphs(__positions_count_font_matrix_attributes_in_).md>) — 使用指定的属性，在指定的位置渲染字符图元（glyph）。_(已废弃)_
- [invalidateGlyphs(onLayoutInvalidationForGlyphRange:)](<../appkit/nslayoutmanager/invalidateglyphs(onlayoutinvalidationforglyphrange_).md>) — 明确指定字符图元流的哪些部分依赖于布局。_(已废弃)_
- [invalidateLayout(forCharacterRange:isSoft:actualCharacterRange:)](<../appkit/nslayoutmanager/invalidatelayout(forcharacterrange_issoft_actualcharacterrange_).md>) — 使映射到给定字符范围的字符图元的布局信息失效。_(已废弃)_
- [textStorage(_:edited:range:changeInLength:invalidatedRange:)](<../appkit/nslayoutmanager/textstorage(__edited_range_changeinlength_invalidatedrange_).md>) — 使给定文本存储对象中某部分文本的字符图元和布局信息失效。_(已废弃)_
- [insertGlyph(_:atGlyphIndex:characterIndex:)](<../appkit/nslayoutmanager/insertglyph(__atglyphindex_characterindex_).md>) — 在给定索引处向字符图元流中插入单个字符图元，并将其映射到给定字符索引处的字符。_(已废弃)_
- [insertGlyphs(_:length:forStartingGlyphAt:characterIndex:)](<../appkit/nslayoutmanager/insertglyphs(__length_forstartingglyphat_characterindex_).md>) — 在给定索引处向字符图元缓存中插入给定的字符图元，并将它们映射到从给定字符索引开始的字符。_(已废弃)_
- [- glyphAtIndex:](<nslayoutmanager/glyph(at_).md>) — 返回指定索引处的字符图元。_(已废弃)_
- [- glyphAtIndex:isValidIndex:](<nslayoutmanager/glyph(at_isvalidindex_).md>) — 返回指定索引处的字符图元，并可选地返回一个标志，表示所请求的索引是否有效。_(已废弃)_
- [replaceGlyph(at:withGlyph:)](<../appkit/nslayoutmanager/replaceglyph(at_withglyph_).md>) — 用新的字符图元替换给定索引处的字符图元。_(已废弃)_
- [getGlyphs(_:range:)](<../appkit/nslayoutmanager/getglyphs(__range_).md>) — 用一串字符图元填充传入的缓冲区。_(已废弃)_
- [getGlyphs(in:glyphs:characterIndexes:glyphInscriptions:elasticBits:)](<../appkit/nslayoutmanager/getglyphs(in_glyphs_characterindexes_glyphinscriptions_elasticbits_).md>) — 返回对给定字符图元范围执行布局所需的字符图元和信息。_(已废弃)_
- [getGlyphs(in:glyphs:characterIndexes:glyphInscriptions:elasticBits:bidiLevels:)](<../appkit/nslayoutmanager/getglyphs(in_glyphs_characterindexes_glyphinscriptions_elasticbits_bidilevels_).md>) — 返回对给定字符图元范围执行布局所需的字符图元和信息。_(已废弃)_
- [deleteGlyphs(in:)](<../appkit/nslayoutmanager/deleteglyphs(in_).md>) — 从接收者的字符图元存储中删除给定范围内的字符图元。_(已废弃)_
- [setCharacterIndex(_:forGlyphAt:)](<../appkit/nslayoutmanager/setcharacterindex(__forglyphat_).md>) — 设置与给定字符图元索引处的字符图元相对应的字符索引。_(已废弃)_
- [intAttribute(_:forGlyphAt:)](<../appkit/nslayoutmanager/intattribute(__forglyphat_).md>) — 返回给定索引处的字符图元中，由给定属性标签所标识的属性值。_(已废弃)_
- [setIntAttribute(_:value:forGlyphAt:)](<../appkit/nslayoutmanager/setintattribute(__value_forglyphat_).md>) — 为给定的字符图元设置自定属性值。_(已废弃)_
- [setLocations(_:startingGlyphIndexes:count:forGlyphRange:)](<../appkit/nslayoutmanager/setlocations(__startingglyphindexes_count_forglyphrange_).md>) — 一次性为多个字符图元范围设置位置。_(已废弃)_
- [rectArray(forCharacterRange:withinSelectedCharacterRange:in:rectCount:)](<../appkit/nslayoutmanager/rectarray(forcharacterrange_withinselectedcharacterrange_in_rectcount_).md>) — 返回一个矩形数组，并通过引用返回此类矩形的数量，这些矩形定义了给定容器中围住给定字符范围的区域。
- [rectArray(forGlyphRange:withinSelectedGlyphRange:in:rectCount:)](<../appkit/nslayoutmanager/rectarray(forglyphrange_withinselectedglyphrange_in_rectcount_).md>) — 返回一个矩形数组，并通过引用返回此类矩形的数量，这些矩形定义了给定容器中围住给定字符图元范围的区域。
- [substituteFont(for:)](<../appkit/nslayoutmanager/substitutefont(for_).md>) — 如果有合适的屏幕字体可用，用其替换指定的字体。_(已废弃)_

### Properties

- [hyphenationFactor](nslayoutmanager/hyphenationfactor.md) — 控制何时执行断字的阈值。_(已废弃)_
- [attributedString](nslayoutmanager-attributedstring.md) — `NSGlyphGenerator` 对象据以获取字符、用于生成字符图元的文本存储对象。
- [layoutOptions](nslayoutmanager-layoutoptions.md) — 布局管理器当前的布局选项。
- [usesScreenFonts](../appkit/nslayoutmanager/usesscreenfonts.md) — 一个布尔值，控制是否使用屏幕字体来计算布局和显示文本。_(已废弃)_

### Types

- [Glyph Attributes](../appkit/glyph-attributes.md) — 仅在字符图元生成机制内部使用、但也必须在各组件之间共享的属性。
