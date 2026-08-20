---
title: Markup Formatting Reference
apple_id: TP40016497
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2017-06-05'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_markup_formatting_ref/Precondition.html
archived_at: '2026-07-18T02:25:44.931410Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Markup Formatting Reference](index.md)



## Precondition

Adds a `Precondition` callout to the Quick Help for a symbol. Multiple `Precondition` callouts appear in the description section in the same order as they do in the markup.

Use the callout to document any conditions that are held for the documented symbol to work.

Works with:

- Playgrounds
- ✓ Symbol documentation

### Syntax

- ```
  * | + | - Precondition: description
  ```
- ```
  optional continuation of description
  ```

The description displayed in Quick Help for the precondition callout is created as described in [Parameters Section](SymbolDocumentation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnjrfvjvoni).

### Example

1. `/**`
2. `An example of using the precondition field`
4. `` - Precondition: The `person` property must be non-nil. ``
5. `` - Precondition: `updatedAddress` must be a valid address. ``
6. `*/`

![image: ../Art/MFR_symbol_field_precondition_2x.png](attachments/Art/MFR_symbol_field_precondition_2x.png)

[Postcondition](Postcondition.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnbqfvjvomi)

[Remark](Remark.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnbsfvjvomi)
