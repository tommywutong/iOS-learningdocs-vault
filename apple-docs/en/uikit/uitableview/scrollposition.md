---
title: UITableView.ScrollPosition
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/scrollposition
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/scrollposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/scrollposition.json'
content_hash: 'sha256:c7281ee9bc542a36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# UITableView.ScrollPosition

<sub>Enumeration</sub>

The position in the table view (top, middle, bottom) to scroll a specified row to.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum ScrollPosition
```

## Overview

You set the scroll position through a parameter of the [- selectRowAtIndexPath:animated:scrollPosition:](<selectrow(at_animated_scrollposition_).md>), [- scrollToNearestSelectedRowAtScrollPosition:animated:](<scrolltonearestselectedrow(at_animated_).md>), [- cellForRowAtIndexPath:](<cellforrow(at_).md>), and [indexPathForSelectedRow](indexpathforselectedrow.md) methods.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UITableViewScrollPositionNone](scrollposition/none.md) — The table view scrolls the row of interest to be fully visible with a minimum of movement.
- [UITableViewScrollPositionTop](scrollposition/top.md) — The table view scrolls the row of interest to the top of the visible table view.
- [UITableViewScrollPositionMiddle](scrollposition/middle.md) — The table view scrolls the row of interest to the middle of the visible table view.
- [UITableViewScrollPositionBottom](scrollposition/bottom.md) — The table view scrolls the row of interest to the bottom of the visible table view.

### Initializers

- [init(rawValue:)](<scrollposition/init(rawvalue_).md>)

## See Also

### Scrolling the table view

- [- scrollToRowAtIndexPath:atScrollPosition:animated:](<scrolltorow(at_at_animated_).md>) — Scrolls through the table view until a row that an index path identifies is at a particular location on the screen.
- [- scrollToNearestSelectedRowAtScrollPosition:animated:](<scrolltonearestselectedrow(at_animated_).md>) — Scrolls the table view so that the selected row nearest to a specified position in the table view is at that position.
