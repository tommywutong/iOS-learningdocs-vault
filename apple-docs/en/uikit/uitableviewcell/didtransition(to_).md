---
title: 'didTransition(to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewcell/didtransition(to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/didtransition(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/didtransition%28to%3A%29.json'
content_hash: 'sha256:3c58d74cec9a6cc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# didTransition(to:)

<sub>Instance Method</sub>

Notifies the cell that it transitioned to a new cell state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func didTransition(to state: UITableViewCell.StateMask)
```

## Parameters

- `state` — A bit mask indicating the state or combination of states the cell is transitioning to.

## Discussion

Subclasses of `UITableViewCell` can implement this method to animate additional changes to a cell when it is changing state. `UITableViewCell` calls this method whenever a cell transitions between states, such as from a normal state (the default) to editing mode. This method is called at the end of the animation block, which gives the custom cell a chance to clean up after the state change—for example, removing the edit and reorder controls after transitioning out of editing.  Subclasses must always call `super` when overriding this method.

Note that when the user swipes a cell to delete it, the cell transitions to the state identified by the [UITableViewCellStateShowingDeleteConfirmationMask](statemask/showingdeleteconfirmation.md) constant but the [UITableViewCellStateShowingEditControlMask](statemask/showingeditcontrol.md) is not set.

## See Also

### Related Documentation

- [editingAccessoryType](editingaccessorytype.md) — The type of standard accessory view for the cell to use in the table view’s editing state.
- [editingAccessoryView](editingaccessoryview.md) — The view to use on the right side of the cell, typically as a control, in the table view’s editing state.
- [accessoryView](accessoryview.md) — The view to use on the right side of the cell, typically as a control, in the table view’s normal state.
- [accessoryType](accessorytype-swift.property.md) — The type of standard accessory view for the cell to use in the table view’s normal state.

### Adjusting to state transitions

- [- willTransitionToState:](<willtransition(to_).md>) — Notifies the cell that it’s about to transition to a new cell state.
- [StateMask](statemask.md) — Constants used to determine the new state of a cell as it transitions between states.
