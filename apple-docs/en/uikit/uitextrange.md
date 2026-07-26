---
title: UITextRange
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextrange
source_url: 'https://developer.apple.com/documentation/uikit/uitextrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextrange.json'
content_hash: 'sha256:d5dbf1b609aff14e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextRange

<sub>Class</sub>

A range of characters in a text container with a starting index and an ending index in string backing a text-entry object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UITextRange
```

## Overview

Classes that adopt the [UITextInput](uitextinput.md) protocol must create custom [UITextRange](uitextrange.md) objects for representing ranges within the text managed by the class. The starting and ending indexes of the range are represented by [UITextPosition](uitextposition.md) objects. The text system uses both [UITextRange](uitextrange.md) and [UITextPosition](uitextposition.md) objects for communicating text-layout information. There are two reasons for using objects for text ranges rather than primitive types such as [NSRange](../foundation/nsrange-c.struct.md):

- Some documents contain nested elements (for example, HTML tags and embedded objects) and you need to track both absolute position and position in the visible text.
- The WebKit framework requires that text indexes and offsets be represented by objects.

If you adopt the [UITextInput](uitextinput.md) protocol, you must create a custom [UITextRange](uitextrange.md) subclass as well as a custom [UITextPosition](uitextposition.md) subclass.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Defining Ranges of Text

- [start](uitextrange/start.md) — The start of a range of text.
- [end](uitextrange/end.md) — The end of the range of text.
- [empty](uitextrange/isempty.md) — A Boolean value that indicates whether the range of text represented by the receiver is zero-length.

## See Also

### Metrics

- [UITextPosition](uitextposition.md) — A position in a text container—that is, an index into the backing string in a text-display view.
- [UITextSelectionRect](uitextselectionrect.md) — An encapsulation of information about a selected range of text in a document.
