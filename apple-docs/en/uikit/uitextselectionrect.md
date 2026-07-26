---
title: UITextSelectionRect
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextselectionrect
source_url: 'https://developer.apple.com/documentation/uikit/uitextselectionrect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextselectionrect.json'
content_hash: 'sha256:5b0ec70f54327914'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextSelectionRect

<sub>Class</sub>

An encapsulation of information about a selected range of text in a document.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UITextSelectionRect
```

## Overview

This class is an abstract class and must be subclassed to be used. The system text input views provide their own concrete implementations of this class.

### Subclassing Notes

If you are implementing a custom text input view, you can subclass and use your custom class to return selection-related information. When subclassing, you should override and reimplement all properties. In your custom implementations, do not call `super`.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Accessing the Selection Rectangle

- [rect](uitextselectionrect/rect.md) — The rectangle that encloses the text selection rectangle’s text range.

### Accessing Text-Related Attributes

- [writingDirection](uitextselectionrect/writingdirection.md) — The writing direction of text in the text selection rectangle’s text range.
- [isVertical](uitextselectionrect/isvertical.md) — A Boolean value that indicates whether the text is vertical.

### Determining the Selection Status

- [containsStart](uitextselectionrect/containsstart.md) — A Boolean value that indicates whether the rectangle contains the start of the selection.
- [containsEnd](uitextselectionrect/containsend.md) — A Boolean value that indicates whether the rectangle contains the end of the selection.

### Instance Properties

- [transform](uitextselectionrect/transform.md) — Custom transform for highlight rects. This transform is assumed to be in the `textInputView` coordinate space. Default is CGAffineTransformIdentity (no transform applied).

## See Also

### Metrics

- [UITextPosition](uitextposition.md) — A position in a text container—that is, an index into the backing string in a text-display view.
- [UITextRange](uitextrange.md) — A range of characters in a text container with a starting index and an ending index in string backing a text-entry object.
