---
title: Markup Formatting Reference
apple_id: TP40016497
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2017-06-05'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_markup_formatting_ref/Example.html
archived_at: '2026-07-18T02:24:55.246253Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Markup Formatting Reference](index.md)



## Example

Add an `Example` callout to a playground using the Example delimiter.

Works with:

- ✓ Playgrounds
- Symbol documentation

### Syntax

- ```
  * | + | - Example: description
  ```
- ```
  optional continuation of description
  ```

### Example

1. `/*:`
2. `` - Example: *A simple `for` loop.*\ ``
3. `` This example shows a `for` loop that prints the numbers 1 to 5.\ ``
4. `\`
5. `` `for index in 1...5 {`\ ``
6. `` `   print("index = \(index)")`\ ``
7. `` `}`} ``
8. `*/`

![image: Art/MFR_example_2x.png](attachments/Art/MFR_example_2x.png)

[Date](Date.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmzvfvjvomi)

[Experiment](Experiment.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmzwfvjvomi)
