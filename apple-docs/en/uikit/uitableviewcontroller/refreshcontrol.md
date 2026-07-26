---
title: refreshControl
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcontroller/refreshcontrol
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcontroller/refreshcontrol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcontroller/refreshcontrol.json'
content_hash: 'sha256:049ec6eca61ea7af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewController](../uitableviewcontroller.md)

# refreshControl

<sub>Instance Property</sub>

The refresh control used to update the table contents.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var refreshControl: UIRefreshControl? { get set }
```

## Discussion

The default value of this property is `nil`.

Assigning a refresh control to this property adds the control to the view controller’s associated interface. You don’t need to set the frame of the refresh control before associating it with the view controller. The view controller updates the control’s height and width and sets its position appropriately.

The table view controller doesn’t automatically update table’s contents in response to user interactions with the refresh control. When the user initiates a refresh operation, the control generates a [UIControlEventValueChanged](../uicontrol/event/valuechanged.md) event. You must associate a target and action method with this event and use them to refresh your table’s contents.
