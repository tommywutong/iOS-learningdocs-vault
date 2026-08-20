---
title: Markup Formatting Reference
apple_id: TP40016497
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2017-06-05'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_markup_formatting_ref/Headings.html
archived_at: '2026-07-18T02:24:59.017371Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Markup Formatting Reference](index.md)



## Headings

Display a line of text formatted as a heading.

Works with:

- ✓ Playgrounds
- ✓ Symbol documentation

### Syntax

Use number signs (`#`) to specify up to three levels of heading. There is at least one space between the number sign and the title string.

- ```
  # Heading 1 String
  ```
- ```
  ## Heading 2 String
  ```
- ```
  ### Heading 3 String
  ```

Alternatively, create level 1 and level 2 headings with an underline string.

- ```
  Heading 1 String
  ```
- ```
  =…
  ```

Underline heading 1 text with at least one equals sign (`=`).

- ```
  Heading 2 String
  ```
- ```
  -…
  ```

Underline heading 2 text with at least one equals sign (`–`).

### Example 1

Create a heading using a number sign.

### Playground Markup

1. `` //: ## Level 2 Heading Using Number Signs (`#`) ``

![image: ../Art/MFR_heading_eg_1_2x.png](attachments/Art/MFR_heading_eg_1_2x.png)

### Quick Help Markup

1. `/**`
2. `` An example of using a number sign (`#`) for a *heading* ``
4. `## This is a Heading 2`
5. `*/`

![image: ../Art/MFR_symbol_heading1_2x.png](attachments/Art/MFR_symbol_heading1_2x.png)

### Example 2

Create a heading using the equals sign for level 1, or the hyphen for sign for level 2. This example uses the same number of equal signs the number of characters in the heading string. Only one equals sign is required.

### Playground Markup

1. `//: Level 1 Heading Using Equals Sign ('=')`
2. `//: =`

![image: ../Art/MFR_heading_eg_2_2x.png](attachments/Art/MFR_heading_eg_2_2x.png)

### Quick Help Markup

1. `/**`
2. `An example of using a character underline for a *heading*`
4. `This is a Heading 1`
5. `===================`
6. `*/`

![image: ../Art/MFR_symbol_heading2_2x.png](attachments/Art/MFR_symbol_heading2_2x.png)

[Block Comment](ComentBlock.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmjqgmwvgvzr)

[Horizontal Rules](HorizontalRules.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmjtfvjvomi)
