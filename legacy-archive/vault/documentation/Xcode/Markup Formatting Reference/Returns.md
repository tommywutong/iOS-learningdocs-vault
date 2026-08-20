---
title: Markup Formatting Reference
apple_id: TP40016497
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2017-06-05'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_markup_formatting_ref/Returns.html
archived_at: '2026-07-18T02:25:52.664092Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Markup Formatting Reference](index.md)



## Returns

Add the `Returns` section to Quick Help for a symbol using the Returns delimiter. Use the delimiter to document the item returned by a symbol.

> [!IMPORTANT]
> 

Works with:

- Playgrounds
- ✓ Symbol documentation

### Syntax

- ```
  * | + | - Returns: description
  ```
- ```
  optional continuation of description
  ```

The description displayed in Quick Help for the returns section is created as described in [Parameters Section](SymbolDocumentation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnjrfvjvoni).

### Example

1. `` /// - Returns: A random number between `min` and `max` ``

![image: ../Art/MFR_symbol_section_returns_2x.png](attachments/Art/MFR_symbol_section_returns_2x.png)

[Remark](Remark.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnbsfvjvomi)

[Requires](Requires.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnbufvjvomi)
