---
title: updateFocusIfNeeded()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocussystem/updatefocusifneeded()
source_url: 'https://developer.apple.com/documentation/uikit/uifocussystem/updatefocusifneeded()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocussystem/updatefocusifneeded%28%29.json'
content_hash: 'sha256:eaa91f530a1d93fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusSystem](../uifocussystem.md)

# updateFocusIfNeeded()

<sub>Instance Method</sub>

Forces the system to act on a pending focus update for the current environment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func updateFocusIfNeeded()
```

## Discussion

If the current environment has a pending focus update, calling this method forces the system to update the focus information immediately instead of waiting for the next run loop cycle. If no focus update is pending, this method does nothing.

You create a pending focus update using the [- requestFocusUpdateToEnvironment:](<requestfocusupdate(to_).md>) method. The system may also schedule focus updates in response to interface-related events.

## See Also

### Managing focus updates

- [- requestFocusUpdateToEnvironment:](<requestfocusupdate(to_).md>) — Submits a request to update the focus state of the specified object.
