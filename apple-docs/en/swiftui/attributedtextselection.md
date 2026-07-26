---
title: AttributedTextSelection
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/attributedtextselection
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextselection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextselection.json'
content_hash: 'sha256:12ddfc40b3d76f62'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AttributedTextSelection

<sub>Structure</sub>

Represents a selection of attributed text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AttributedTextSelection
```

## Overview

A selection is either an insertion point (e.g. a cursor in the text), or spans over a range of characters. While that range is always visually contiguous, it may not be logically contiguous in the text storage. Specifically, a single selection value cannot represent multiple cursors.

This is frequently used to represent selection of text in a `TextEditor`. The following example shows a text editor that leverages text selection to offer live suggestions based on the current selection.

```swift
struct SuggestionTextEditor: View {
    @State var text: AttributedString = ""
    @State var selection = AttributedTextSelection()

    var body: some View {
        VStack {
            TextEditor(text: $text, selection: $selection)
            // A helper view that offers live suggestions based on selection.
            SuggestionsView(substrings: getSubstrings(
                text: text, indices: selection.indices(in: text))
        }
    }

    private func getSubstrings(
        text: String, indices: AttributedTextSelection.Indices
    ) -> [Substring] {
        // Resolve substrings representing the current selection...
    }
}

struct SuggestionsView: View { ... }
```

You can also use the [textSelectionAffinity(_:)](<view/textselectionaffinity(__).md>) modifier to specify a selection affinity on the given hierarchy:

```swift
struct SuggestionTextEditor: View {
    @State var text: AttributedString = ""
    @State var selection = AttributedTextSelection()

    var body: some View {
        VStack {
            TextEditor(text: $text, selection: $selection)
            // A helper view that offers live suggestions based on selection.
            SuggestionsView(substrings: getSubstrings(
                text: text, indices: selection.indices(in: text))
        }
        .textSelectionAffinity(.upstream)
    }

    private func getSubstrings(
        text: String, indices: AttributedTextSelection.Indices
    ) -> [Substring] {
        // Resolve substrings representing the current selection...
    }
}

struct SuggestionsView: View { ... }
```

> [!info] See Also
> [TextSelectionAffinity](textselectionaffinity.md), [TextEditor](texteditor.md)

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Structures

- [Attributes](attributedtextselection/attributes.md) — A sequence of all attribute values a selection has in a certain text.

### Initializers

- [init()](<attributedtextselection/init().md>) — Initialize the default selection for a new text editor.
- [init(insertionPoint:typingAttributes:)](<attributedtextselection/init(insertionpoint_typingattributes_).md>) — Initialize a selection to a single insertion point.
- [init(range:)](<attributedtextselection/init(range_).md>) — Initialize a selection to a character range.
- [init(ranges:)](<attributedtextselection/init(ranges_).md>) — Initialize a selection to character ranges.

### Instance Methods

- [affinity(in:)](<attributedtextselection/affinity(in_).md>) — Return the selection affinity of the selection.
- [attributes(in:)](<attributedtextselection/attributes(in_).md>) — Obtain a lazy sequence of all attribute values the selection has in a given text.
- [indices(in:)](<attributedtextselection/indices(in_).md>) — The current text selection indices.
- [typingAttributes(in:)](<attributedtextselection/typingattributes(in_).md>) — Returns the typing attributes for a corresponding text.

### Enumerations

- [Indices](attributedtextselection/indices.md) — The indices of the current selection.

## See Also

### Selecting text

- [textSelection(_:)](<view/textselection(__).md>) — Controls whether people can select text within this view.
- [TextSelectability](textselectability.md) — A type that describes the ability to select text.
- [TextSelection](textselection.md) — Represents a selection of text.
- [textSelectionAffinity(_:)](<view/textselectionaffinity(__).md>) — Sets the direction of a selection or cursor relative to a text character.
- [textSelectionAffinity](environmentvalues/textselectionaffinity.md) — A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [TextSelectionAffinity](textselectionaffinity.md) — A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
