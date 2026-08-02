---
title: Markup Formatting Reference
apple_id: TP40016497
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2017-06-05'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_markup_formatting_ref/Parameter.html
archived_at: '2026-07-18T02:25:39.863976Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Markup Formatting Reference](index.md)



## Parameter

Add the name and description for a single parameter to the `Parameters` section of Quick Help. The parameters are added to Quick Help in the order that they appear in the markup.

The `Parameters` section is only added to Quick Help if there is at least one [Parameters](Parameters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmrufvjvomi) or Parameter delimiter in the markup for a symbol. The section contains entries for all the [Parameters](Parameters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmrufvjvomi) delimiters followed by entries for all the Parameter delimiters.

Works with:

- Playgrounds
- ✓ Symbol documentation

### Syntax

- ```
  * | + | - Parameter parameter name: description
  ```
- ```
  optional continuation of description
  ```
- ```

  ```
- ```
      optional paragraph
  ```
- ```
  …
  ```

Add paragraphs to the description of a symbol by adding an empty line and indenting the text for the paragraph by a tab or by four spaces.

The description displayed in Quick Help for the parameter is created as described in [Parameters Section](SymbolDocumentation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnjrfvjvoni).

### Example

1. `/// - Parameter llamaCount: The number of llamas in the managed herd.`

![image: ../Art/MFR_symbol_section_parameter_2x.png](attachments/Art/MFR_symbol_section_parameter_2x.png)

### Alternative

Use the [Parameters](Parameters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmrufvjvomi) delimiter to add multiple parameters.

[Note](Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmzzfvjvomi)

[Parameters](Parameters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmrufvjvomi)
