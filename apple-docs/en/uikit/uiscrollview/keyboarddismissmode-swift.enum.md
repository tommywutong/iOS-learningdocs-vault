---
title: UIScrollView.KeyboardDismissMode
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/keyboarddismissmode-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/keyboarddismissmode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/keyboarddismissmode-swift.enum.json'
content_hash: 'sha256:654da8caa8347e67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# UIScrollView.KeyboardDismissMode

<sub>Enumeration</sub>

Constants that determine how the system dismisses the keyboard when a drag begins in the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
enum KeyboardDismissMode
```

## Overview

You use these constants to set the value of the [keyboardDismissMode](keyboarddismissmode-swift.property.md) property.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIScrollViewKeyboardDismissModeNone](keyboarddismissmode-swift.enum/none.md) — A mode in which a drag doesn’t dismiss the keyboard.
- [UIScrollViewKeyboardDismissModeOnDrag](keyboarddismissmode-swift.enum/ondrag.md) — A mode in which the keyboard dismisses when a drag begins.
- [UIScrollViewKeyboardDismissModeInteractive](keyboarddismissmode-swift.enum/interactive.md) — A mode in which the keyboard follows the dragging touch offscreen, and can be pulled upward again to cancel the dismiss.
- [UIScrollViewKeyboardDismissModeOnDragWithAccessory](keyboarddismissmode-swift.enum/ondragwithaccessory.md) — A mode in which the keyboard and accessory view dismiss together when a drag begins.
- [UIScrollViewKeyboardDismissModeInteractiveWithAccessory](keyboarddismissmode-swift.enum/interactivewithaccessory.md) — A mode in which the keyboard and accessory view both follow the dragging touch offscreen, and can be pulled upward again to cancel the dismiss.

### Initializers

- [init(rawValue:)](<keyboarddismissmode-swift.enum/init(rawvalue_).md>)

## See Also

### Dismissing the keyboard

- [keyboardDismissMode](keyboarddismissmode-swift.property.md) — The manner in which the system dismisses the keyboard when a drag begins in the scroll view.
