---
title: Markup Formatting Reference
apple_id: TP40016497
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2017-06-05'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_markup_formatting_ref/Copyright.html
archived_at: '2026-07-18T02:24:48.011811Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Markup Formatting Reference](index.md)



## Copyright

Add a `Copyright` callout to the Quick Help for a symbol using the Copyright delimiter. Multiple `Copyright` callouts appear in the description section in the same order as they do in the markup.

Use the callout to display copyright information for a symbol.

Works with:

- Playgrounds
- ✓ Symbol documentation

### Syntax

- ```
  * | + | - Copyright: description
  ```
- ```
  optional continuation of description
  ```

The description displayed in Quick Help for the copyright callout is created as described in [Parameters Section](SymbolDocumentation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnjrfvjvoni).

### Example

1. `/**`
2. `An example of using the copyright field`
4. `- Copyright: Copyright © 1215`
5. `by The Group of Barrons`
6. `*/`

![image: ../Art/MFR_symbol_field_copyright_2x.png](attachments/Art/MFR_symbol_field_copyright_2x.png)

[Complexity](Complexity.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmztfvjvomi)

[Custom Callout](CustomCallouts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnjzfvjvomi)
