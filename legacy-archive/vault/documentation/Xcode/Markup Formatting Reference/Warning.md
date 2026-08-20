---
title: Markup Formatting Reference
apple_id: TP40016497
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2017-06-05'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_markup_formatting_ref/Warning.html
archived_at: '2026-07-18T02:26:29.083850Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Markup Formatting Reference](index.md)



## Warning

Add a `Warning` callout to the Quick Help for a symbol using the Warning delimiter. Multiple `Warning` callouts appear in the description section in the same order as they do in the markup.

Works with:

- Playgrounds
- ✓ Symbol documentation

### Syntax

- ```
  * | + | - Warning: description
  ```
- ```
  optional continuation of description
  ```

The description displayed in Quick Help for the warning callout is created as described in [Parameters Section](SymbolDocumentation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnjrfvjvoni).

### Example

1. `/**`
2. `An example of using the warning field`
4. `- Warning:`
5. `Not all code paths for this method have been tested`
6. `*/`

![image: ../Art/MFR_symbol_field_warning_2x.png](attachments/Art/MFR_symbol_field_warning_2x.png)

[Version](Version.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnbyfvjvomi)

[Escapes](SpecialCharacter.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmjzfvjvomi)
