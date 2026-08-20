---
title: Markup Formatting Reference
apple_id: TP40016497
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2017-06-05'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_markup_formatting_ref/Version.html
archived_at: '2026-07-18T02:26:27.593704Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Markup Formatting Reference](index.md)



## Version

Add a `Version` callout to the Quick Help for a symbol using the Version delimiter. Multiple `Version` callouts appear in the description section in the same order as they do in the markup.

Works with:

- Playgrounds
- ✓ Symbol documentation

### Syntax

- ```
  * | + | - Version: description
  ```
- ```
  optional continuation of description
  ```

The description of the for the version callout is created as described in [Parameters Section](SymbolDocumentation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnjrfvjvoni).

### Example

1. `/**`
2. `An example of using the version field`
4. `- Version: 0.1 (61A329)`
5. `*/`

![image: ../Art/MFR_symbol_field_version_2x.png](attachments/Art/MFR_symbol_field_version_2x.png)

[To Do](Todo.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnbxfvjvomi)

[Warning](Warning.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnbzfvjvomi)
