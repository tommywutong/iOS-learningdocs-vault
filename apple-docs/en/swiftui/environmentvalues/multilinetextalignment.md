---
title: multilineTextAlignment
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/multilinetextalignment
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/multilinetextalignment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/multilinetextalignment.json'
content_hash: 'sha256:d77050c5b599d955'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# multilineTextAlignment

<sub>Instance Property</sub>

An environment value that indicates how a text view aligns its lines when the content wraps or contains newlines.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var multilineTextAlignment: TextAlignment { get set }
```

## Discussion

Set this value for a view hierarchy by applying the [multilineTextAlignment(_:)](<../view/multilinetextalignment(__).md>) view modifier. Views in the hierarchy that display text, like [Text](../text.md) or [TextEditor](../texteditor.md), read the value from the environment and adjust their text alignment accordingly.

This value has no effect on a [Text](../text.md) view that contains only one line of text, because a text view has a width that exactly matches the width of its widest line. If you want to align an entire text view rather than its contents, set the aligment of its container, like a [VStack](../vstack.md) or a frame that you create with the [frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)](<../view/frame(minwidth_idealwidth_maxwidth_minheight_idealheight_maxheight_alignment_).md>) modifier.

> [!note] Note
> You can use this value to control the alignment of a [Text](../text.md) view that you create with the [init(_:style:)](<../text/init(__style_).md>) initializer to display localized dates and times, including when the view uses only a single line, but only when that view appears in a widget.

## See Also

### Formatting multiline text

- [lineSpacing(_:)](<../view/linespacing(__).md>) — Sets the amount of space between lines of text in this view.
- [lineSpacing](linespacing.md) — The distance in points between the bottom of one line fragment and the top of the next.
- [multilineTextAlignment(_:)](<../view/multilinetextalignment(__).md>) — Sets the alignment of a text view that contains multiple lines of text.
