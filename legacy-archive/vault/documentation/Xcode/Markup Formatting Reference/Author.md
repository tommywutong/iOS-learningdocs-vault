---
title: Markup Formatting Reference
apple_id: TP40016497
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2017-06-05'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_markup_formatting_ref/Author.html
archived_at: '2026-07-18T02:24:34.831422Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Markup Formatting Reference](index.md)



## Author

Add an `Author` callout with a single name to the Quick Help for a symbol using the Author delimiter. Multiple `Author` callouts appear in the description section in the same order as they do in the markup

Use the callout to display the author of the code for a symbol.

Works with:

- Playgrounds
- ✓ Symbol documentation

### Syntax

- ```
  * | + | - Author: author name
  ```
- ```
  optional continuation of author name
  ```

The author name displayed in Quick Help is created as described in [Parameters Section](SymbolDocumentation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnjrfvjvoni).

### Example

1. `/**`
2. `An example of using the author field`
4. `- Author: William Shakespeare`
5. `*/`

![image: ../Art/MFR_symbol_field_author_2x.png](attachments/Art/MFR_symbol_field_author_2x.png)

### Alternative

Use the [Authors](Authors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmzrfvjvomi) delimiter to list multiple authors in one callout.

[Attention](Attention.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmrzfvjvomi)

[Authors](Authors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmzrfvjvomi)
