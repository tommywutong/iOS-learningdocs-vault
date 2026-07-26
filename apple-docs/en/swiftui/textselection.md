---
title: TextSelection
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textselection
source_url: 'https://developer.apple.com/documentation/swiftui/textselection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textselection.json'
content_hash: 'sha256:1a83dc114974fa38'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TextSelection

<sub>Structure</sub>

Represents a selection of text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TextSelection
```

## Overview

A selection is either an insertion point (e.g. a cursor in the text), a selection over a range of text or on macOS, multiple selections.

This is frequently used to represent selection of text in a `TextField` or `TextEditor`. The following example shows a text editor that leverages text selection to offer live suggestions based on the current selection.

```swift
struct SuggestionTextEditor: View {
    @State var text: String = ""
    @State var selection: TextSelection? = nil

    var body: some View {
        VStack {
            TextEditor(text: $text, selection: $selection)
            // A helper view that offers live suggestions based on selection.
            SuggestionsView(
                substrings: getSubstrings(text: text, indices: selection?.indices))
        }
    }

    private func getSubstrings(
        text: String, indices: TextSelection.Indices?
    ) -> [Substring] {
        // Resolve substrings representing the current selection...
    }
}

struct SuggestionsView: View { ... }
```

You can also use the [textSelectionAffinity(_:)](<view/textselectionaffinity(__).md>) modifier to specify a selection affinity on the given hierarchy:

```swift
struct SuggestionTextEditor: View {
    @State var text: String = ""
    @State var selection: TextSelection? = nil

    var body: some View {
        VStack {
            TextEditor(text: $text, selection: $selection)
            // A helper view that offers live suggestions based on selection.
            SuggestionsView(
                substrings: getSubstrings(text: text, indices: selection?.indices))
        }
        .textSelectionAffinity(.upstream)
    }

    private func getSubstrings(
        text: String, indices: TextSelection.Indices?
    ) -> [Substring] {
        // Resolve substrings representing the current selection...
    }
}

struct SuggestionsView: View { ... }
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Initializers

- [init(insertionPoint:)](<textselection/init(insertionpoint_).md>) — Create a selection at a given insertion point.
- [init(range:)](<textselection/init(range_).md>) — Create a single selection with a given range.
- [init(ranges:)](<textselection/init(ranges_).md>) — Create multiple selections with a given range-set.

### Instance Properties

- [affinity](textselection/affinity.md) — Return the selection affinity of the selection.
- [indices](textselection/indices-swift.property.md) — Return the current text selection indices.
- [isInsertion](textselection/isinsertion.md) — Return `true` if the selection is an insertion point.

### Enumerations

- [Indices](textselection/indices-swift.enum.md) — The indices of the current selection.

## See Also

### Selecting text

- [textSelection(_:)](<view/textselection(__).md>) — Controls whether people can select text within this view.
- [TextSelectability](textselectability.md) — A type that describes the ability to select text.
- [textSelectionAffinity(_:)](<view/textselectionaffinity(__).md>) — Sets the direction of a selection or cursor relative to a text character.
- [textSelectionAffinity](environmentvalues/textselectionaffinity.md) — A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [TextSelectionAffinity](textselectionaffinity.md) — A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [AttributedTextSelection](attributedtextselection.md) — Represents a selection of attributed text.
