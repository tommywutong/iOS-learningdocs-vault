---
title: setNeedsTouchBarUpdate()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/setneedstouchbarupdate()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedstouchbarupdate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/setneedstouchbarupdate%28%29.json'
content_hash: 'sha256:ef955589a399b1d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# setNeedsTouchBarUpdate()

<sub>Instance Method</sub>

Tells the system to update the Touch Bar.

<sub>Mac Catalyst</sub>

```swift
func setNeedsTouchBarUpdate()
```

## Discussion

Call this method when the value from [childViewControllerForTouchBar](childviewcontrollerfortouchbar.md) changes.

## See Also

### Managing the Touch Bar

- [childViewControllerForTouchBar](childviewcontrollerfortouchbar.md) — The child view controller that the system uses to display content in the Touch Bar.
