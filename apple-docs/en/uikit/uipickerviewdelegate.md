---
title: UIPickerViewDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipickerviewdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uipickerviewdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerviewdelegate.json'
content_hash: 'sha256:1ed3b65bdfeb9f6f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPickerViewDelegate

<sub>Protocol</sub>

The interface for a picker view’s delegate.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIPickerViewDelegate : NSObjectProtocol
```

## Overview

The delegate of a [UIPickerView](uipickerview.md) object must adopt this protocol and implement at least some of its methods to provide the picker view with the data it needs to construct itself.

The delegate implements the required methods of this protocol to return height, width, row title, and the view content for the rows in each component. It must also provide the content for each component’s row, either as a string or a view. Typically the delegate implements other optional methods to respond to new selections or deselections of component rows.

See [UIPickerView](uipickerview.md) for a discussion of components, rows, row content, and row selection.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [UIPickerViewAccessibilityDelegate](uipickerviewaccessibilitydelegate.md)

## Topics

### Setting the dimensions of the picker view

- [- pickerView:rowHeightForComponent:](<uipickerviewdelegate/pickerview(__rowheightforcomponent_).md>) — Called by the picker view when it needs the row height to use for drawing row content.
- [- pickerView:widthForComponent:](<uipickerviewdelegate/pickerview(__widthforcomponent_).md>) — Called by the picker view when it needs the row width to use for drawing row content.

### Setting the content of component rows

- [- pickerView:titleForRow:forComponent:](<uipickerviewdelegate/pickerview(__titleforrow_forcomponent_).md>) — Called by the picker view when it needs the title to use for a given row in a given component.
- [- pickerView:attributedTitleForRow:forComponent:](<uipickerviewdelegate/pickerview(__attributedtitleforrow_forcomponent_).md>) — Called by the picker view when it needs the styled title to use for a given row in a given component.
- [- pickerView:viewForRow:forComponent:reusingView:](<uipickerviewdelegate/pickerview(__viewforrow_forcomponent_reusing_).md>) — Called by the picker view when it needs the view to use for a given row in a given component.

### Responding to row selection

- [- pickerView:didSelectRow:inComponent:](<uipickerviewdelegate/pickerview(__didselectrow_incomponent_).md>) — Called by the picker view when the user selects a row in a component.

## See Also

### Customizing the picker behavior

- [delegate](uipickerview/delegate.md) — The delegate for the picker view.
