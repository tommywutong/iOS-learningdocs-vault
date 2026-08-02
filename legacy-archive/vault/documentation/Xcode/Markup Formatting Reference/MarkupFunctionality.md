---
title: Markup Formatting Reference
apple_id: TP40016497
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2017-06-05'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_markup_formatting_ref/MarkupFunctionality.html
archived_at: '2026-07-18T02:25:24.019267Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Markup Formatting Reference](index.md)



## Markup Functionality

Markup uses simple character-based delimiters to mark formatted text in playgrounds and in Quick Help for Swift symbols.

The different delimiters include functionality for:

- Formatting a line of text such as a creating a heading
- Formatting multiple lines of text such as creating a bulleted list
- Formatting a span of characters such as adding emphasis to a string
- Inserting links to web based content
- Inserting assets such as images and videos
- Inserting callouts such as examples in playgrounds and parameters in Quick Help.
- Escaping special characters, including markup delimiters

Some of the delimiters are used for both rendered playground documentation and in Quick Help. Other delimiters are used with either playgrounds or with Quick Help. The documentation for each delimiter includes information on where it can be used. In addition, Table 2-1 gives an alphabetical overview of all the delimiters including a brief description.

For information on adding markup, see [Using Markup](AddingMarkup.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmznknltc).

__Table 2-1__Markup delimiters

| Delimiter name | Description | Playground | Quick Help |
| --- | --- | --- | --- |
| [Attention](Attention.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmrzfvjvomi) | Adds an `Attention` callout. |  | ✓ |
| [Author](Author.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmzqfvjvomi) | Adds an `Author` callout. |  | ✓ |
| [Authors](Authors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmzrfvjvomi) | Adds an `Authors` callout for multiple authors. |  | ✓ |
| [Block Comment](ComentBlock.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmjqgmwvgvzr) | The comment markers for opening and closing a block of markup. | ✓ | ✓ |
| [Bug](Bug.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmzsfvjvomi) | Adds a `Bug` callout. |  | ✓ |
| [Bulleted Lists](BulletedLists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqojnknltc) | Adds a bulleted list. | ✓ | ✓ |
| [Code Block](CodeBlocks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmjsfvjvomi) | Renders lines of text as a block of code. | ✓ | ✓ |
| [Code Voice](Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmjwfvjvomi) | Renders a span of text in the font used for displaying code. | ✓ | ✓ |
| [Complexity](Complexity.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmztfvjvomi) | Adds a `Complexity` callout. |  | ✓ |
| [Copyright](Copyright.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmzufvjvomi) | Adds a `Copyright` callout. |  | ✓ |
| [Custom Callout](CustomCallouts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnjzfvjvomi) | Adds a callout with custom text. | ✓ |  |
| [Date](Date.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmzvfvjvomi) | Adds a `Date` callout. |  | ✓ |
| [Emphasis (Italics)](Emphasis%28Italics%29.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmjufvjvomi) | Renders a span of text with emphasis. | ✓ | ✓ |
| [Escapes](SpecialCharacter.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmjzfvjvomi) | Disables any special behaviors for the following character. | ✓ | ✓ |
| [Example](Example.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnjyfvjvomi) | Adds an `Example` callout. | ✓ |  |
| [Experiment](Experiment.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmzwfvjvomi) | Adds an `Experiment` callout. | ✓ | ✓ |
| [Headings](Headings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqobnknltc) | Renders a line as a heading. | ✓ | ✓ |
| [Horizontal Rules](HorizontalRules.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmjtfvjvomi) | Adds a horizontal rule. | ✓ | ✓ |
| [Images](Images.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmjxfvjvomi) | Shows an image from the web or from a playground project. | ✓ | ✓ |
| [Important](Important.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmzxfvjvomi) | Adds an `Important` callout | ✓ | ✓ |
| [Invariant](Invariant.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmzyfvjvomi) | Adds an `Invariant` callout. |  | ✓ |
| [Link Reference](LinkReference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnjwfvjvomi) | Adds a named reference to a URL that can be used in multiple places. | ✓ | ✓ |
| [Links](Links.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmjyfvjvomi) | Adds a link to a text-based resource. | ✓ | ✓ |
| [Named Page](AnyPage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmrsfvjvomi) | Adds a link to a named playground page. | ✓ |  |
| [Next Page](NextPage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmrqfvjvomi) | Adds a link to the next playground page in the project. | ✓ |  |
| [Note](Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmzzfvjvomi) | Adds a `Note` callout. | ✓ | ✓ |
| [Numbered Lists](NumberedLists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmjqfvjvomi) | Adds a numbered list. | ✓ | ✓ |
| [Parameter](Parameter.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmryfvjvomi) | Adds a `Parameter` to the parameters section of Quick Help. |  | ✓ |
| [Parameters](Parameters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmrufvjvomi) | Adds multiple `Parameters` to the parameters section of Quick Help. |  | ✓ |
| [Postcondition](Postcondition.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnbqfvjvomi) | Adds a `Postcondition` callout. |  | ✓ |
| [Precondition](Precondition.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnbrfvjvomi) | Adds a `Precondition` callout. |  | ✓ |
| [Previous Page](PreviousPage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmrrfvjvomi) | Adds a link to the previous page in a playground project. | ✓ |  |
| [Remark](Remark.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnbsfvjvomi) | Adds a `Remark` callout. |  | ✓ |
| [Returns](Returns.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmrvfvjvomi) | Adds the `Returns` section to Quick Help. |  | ✓ |
| [Requires](Requires.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnbufvjvomi) | Adds a `Requires` callout. |  | ✓ |
| [See Also](SeeAlso.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnbvfvjvomi) | Adds a `See Also` callout. |  | ✓ |
| [Since](Since.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnbwfvjvomi) | Adds a `Since` callout. |  | ✓ |
| [Single Line Comment](SingleLineComment.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmjqgiwvgvzr) | The comment marker used for a single line of markup. | ✓ | ✓ |
| [Strong (Bold)](Strong%28Bold%29.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmjvfvjvomi) | Renders a span of text in bold. | ✓ | ✓ |
| [Throws](Throws.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmrwfvjvomi) | Adds the `Throws` section to Quick Help. |  | ✓ |
| [To Do](Todo.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnbxfvjvomi) | Adds a `To Do` callout. |  | ✓ |
| [Version](Version.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnbyfvjvomi) | Adds a `Version` callout. |  | ✓ |
| [Videos](InlineVideo.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqojyfvjvomi) | Adds a live video player. | ✓ |  |
| [Warning](Warning.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqnbzfvjvomi) | Adds a `Warning` callout. |  | ✓ |

[Markup Overview](index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmrnknltc)

[Adding Markup to Files](AddingMarkup.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqmjqgawvgvzr)
