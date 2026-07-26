---
title: markdownSourcePosition
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributescopes/foundationattributes/markdownsourceposition
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/markdownsourceposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes/foundationattributes/markdownsourceposition.json'
content_hash: 'sha256:e0eee2048f0f4c72'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributeScopes](../../attributescopes.md) · [FoundationAttributes](../foundationattributes.md)

# markdownSourcePosition

<sub>Instance Property</sub>

A property for accessing a Markdown source position attribute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let markdownSourcePosition: AttributeScopes.FoundationAttributes.MarkdownSourcePositionAttribute
```

## Discussion

This attribute indicates the position in the Markdown source where a run of attributed text begins and ends, omitting markup characters in the source. For example, after parsing the source string `“This is *emphasized*.”`, the text `emphasized` has a Markdown source position that starts at column `10`. This index is the `“e”` character, not the `“*”` formatting character.

> [!tip] Tip
> [MarkdownSourcePosition](../../attributedstring/markdownsourceposition.md) uses `1`-based counting for its row and column properties. For columns, the value represents a UTF-8 index. With multi-byte characters, the column is therefore the first byte of the character.

An attributed string parsed from Markdown text includes this attribute only if the [appliesSourcePositionAttributes](../../attributedstring/markdownparsingoptions/appliessourcepositionattributes.md) value in the [MarkdownParsingOptions](../../attributedstring/markdownparsingoptions.md) provided to the [AttributedString](../../attributedstring.md) initializer is `true`.

In the following example, the `markdown` source string contains several forms of Markdown formatting supported by AttributedString, including the [NSInlinePresentationIntentStronglyEmphasized](../../inlinepresentationintent/stronglyemphasized.md) inline presentation intent applied with double asterisks. The example parses the source string, enabling the [appliesSourcePositionAttributes](../../attributedstring/markdownparsingoptions/appliessourcepositionattributes.md) option. Next, the example loops over the attributed string’s runs, looking for a run that contains both a [markdownSourcePosition](markdownsourceposition.md) attribute and an [inlinePresentationIntent](inlinepresentationintent.md) whose value is [NSInlinePresentationIntentStronglyEmphasized](../../inlinepresentationintent/stronglyemphasized.md). If it finds such a run, it prints the source position attribute and the attributed text.

```swift
let markdown = "Examples of *emphasis*, **strong emphasis**, and [link](https://example.com)."
let options = AttributedString.MarkdownParsingOptions(appliesSourcePositionAttributes: true)
if let attString = try? AttributedString(markdown: markdown, options: options) {
    for run in attString.runs {
        if let sourcePosition = run.markdownSourcePosition,
           let sourceRange = Range(sourcePosition, in: markdown),
           let presentationIntent = run.inlinePresentationIntent,
           presentationIntent.contains(.stronglyEmphasized) {
               print("Found strong emphasis: \(sourcePosition), text: '\(markdown[sourceRange])'")
        }
    }
}
// Prints: Found strong emphasis: MarkdownSourcePosition(startLine: 1, startColumn: 27, endLine: 1, endColumn: 41, startOffsets: Optional(Foundation.AttributedString.MarkdownSourcePosition.Offsets(utf8: 26, utf16: 26, utf8NextCodePoint: 27, utf16CurrentCodePointLength: 1)), endOffsets: Optional(Foundation.AttributedString.MarkdownSourcePosition.Offsets(utf8: 40, utf16: 40, utf8NextCodePoint: 41, utf16CurrentCodePointLength: 1))), text: 'strong emphasis'
```

This uses the [Range](../../../swift/range.md) convenience initializer [init(_:in:)](<../../../swift/range/init(__in_)-9vre5.md>), which creates a range from an [MarkdownSourcePosition](../../attributedstring/markdownsourceposition.md) and the Markdown source string. Working with a range may be more convenient than working with the start and end position properties in [MarkdownSourcePosition](../../attributedstring/markdownsourceposition.md).

## See Also

### Using Markdown source position attributes

- [MarkdownSourcePositionAttribute](markdownsourcepositionattribute.md) — A type for using a markdown source position as an attribute.
