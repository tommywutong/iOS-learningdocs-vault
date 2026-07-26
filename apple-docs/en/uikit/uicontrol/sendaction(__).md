---
title: 'sendAction(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontrol/sendaction(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/sendaction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/sendaction%28_%3A%29.json'
content_hash: 'sha256:ac79929a5ba37146'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# sendAction(_:)

<sub>Instance Method</sub>

Like -sendAction:to:forEvent:, this method is called by -sendActionsForControlEvents:. You may override this method to observe or modify behavior. If you override this method, you should call super precisely once to dispatch the action, or not call super to suppress sending that action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func sendAction(_ action: UIAction)
```

## See Also

### Triggering actions

- [- performPrimaryAction](<performprimaryaction().md>) — Calls the method associated with the control’s primary action.
- [- sendAction:to:forEvent:](<sendaction(__to_for_).md>) — Calls the specified action method.
- [- sendActionsForControlEvents:](<sendactions(for_).md>) — Calls the action methods associated with the specified events.
