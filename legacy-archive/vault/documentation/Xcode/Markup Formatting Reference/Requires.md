---
title: Markup Formatting Reference
apple_id: TP40016497
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2017-06-05'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_markup_formatting_ref/Requires.html
archived_at: '2026-07-18T02:25:50.494623Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Markup Formatting Reference](index.md)



## Requires

Add a `Requires` callout to the Quick Help for a symbol using the Requires delimiter. See [Precondition](Precondition.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnbrfvjvomi) for usage.

Works with:

- Playgrounds
- ✓ Symbol documentation

### Syntax

- ```
  * | + | - Requires: description
  ```
- ```
  optional continuation of description
  ```

The description displayed in Quick Help for the requires callout is created as described in [Parameters Section](SymbolDocumentation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnjrfvjvoni).

### Example

1. `/**`
2. `An example of using the requires field`
4. `` - Requires: `start <= end`. ``
5. `` - Requires: `count > 0`. ``
6. `*/`

![image: ../Art/MFR_symbol_field_requires_2x.png](attachments/Art/MFR_symbol_field_requires_2x.png)

[Returns](Returns.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmrvfvjvomi)

[See Also](SeeAlso.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnbvfvjvomi)
