---
title: UITableViewCell.StateMask
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/statemask
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/statemask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/statemask.json'
content_hash: 'sha256:c4342898516e1031'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# UITableViewCell.StateMask

<sub>Structure</sub>

Constants used to determine the new state of a cell as it transitions between states.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct StateMask
```

## Overview

The methods that use these constants are [- didTransitionToState:](<didtransition(to_).md>) and [- willTransitionToState:](<willtransition(to_).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [UITableViewCellStateShowingEditControlMask](statemask/showingeditcontrol.md) — The state of a table view cell when the table view is in editing mode.
- [UITableViewCellStateShowingDeleteConfirmationMask](statemask/showingdeleteconfirmation.md) — The state of a table view cell that shows a button requesting confirmation of a delete gesture.

### Initializers

- [init(rawValue:)](<statemask/init(rawvalue_).md>) — Creates a state mask with the specified raw value.

## See Also

### Adjusting to state transitions

- [- willTransitionToState:](<willtransition(to_).md>) — Notifies the cell that it’s about to transition to a new cell state.
- [- didTransitionToState:](<didtransition(to_).md>) — Notifies the cell that it transitioned to a new cell state.
