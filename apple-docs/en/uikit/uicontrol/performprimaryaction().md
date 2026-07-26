---
title: performPrimaryAction()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, tvOS 17.4+, visionOS 1.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontrol/performprimaryaction()
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/performprimaryaction()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/performprimaryaction%28%29.json'
content_hash: 'sha256:e803c9870fdf1692'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# performPrimaryAction()

<sub>Instance Method</sub>

Calls the method associated with the control’s primary action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func performPrimaryAction()
```

## Discussion

This method invokes the primary action for the control, whether it’s a direct action, for example, a button tap, or presents further UI, for example, a contextual menu.

## See Also

### Triggering actions

- [- sendAction:](<sendaction(__).md>) — Like -sendAction:to:forEvent:, this method is called by -sendActionsForControlEvents:. You may override this method to observe or modify behavior. If you override this method, you should call super precisely once to dispatch the action, or not call super to suppress sending that action.
- [- sendAction:to:forEvent:](<sendaction(__to_for_).md>) — Calls the specified action method.
- [- sendActionsForControlEvents:](<sendactions(for_).md>) — Calls the action methods associated with the specified events.
