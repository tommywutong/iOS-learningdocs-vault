---
title: Markup Formatting Reference
apple_id: TP40016497
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2017-06-05'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_markup_formatting_ref/Date.html
archived_at: '2026-07-18T02:24:51.825407Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Markup Formatting Reference](index.md)



## Date

Add a `Date` callout to the Quick Help for a symbol using the Date delimiter. Multiple `Date` callouts appear in the description section in the same order as they do in the markup.

Works with:

- Playgrounds
- ✓ Symbol documentation

### Syntax

- ```
  * | + | - Date: description
  ```
- ```
  optional continuation of description
  ```

The description displayed in Quick Help for the date callout is created as described in [Parameters Section](SymbolDocumentation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnjrfvjvoni).

### Example

1. `/**`
2. `An example of using the date field`
4. `Last date this example was changed`
5. `- Date: August 19, 2015`
7. `Days the method produces special results`
8. `- Date: 12/31`
9. `- Date: 03/17`
10. `*/`

![image: ../Art/MFR_symbol_field_date_2x.png](attachments/Art/MFR_symbol_field_date_2x.png)

[Custom Callout](CustomCallouts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnjzfvjvomi)

[Example](Example.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnjyfvjvomi)
