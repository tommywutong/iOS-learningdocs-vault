---
title: 'decodeRestorableState(with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/decoderestorablestate(with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/decoderestorablestate(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/decoderestorablestate%28with%3A%29.json'
content_hash: 'sha256:c627040a7e840aaa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# decodeRestorableState(with:)

<sub>Instance Method</sub>

Decodes and restores state-related information for the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func decodeRestorableState(with coder: NSCoder)
```

## Parameters

- `coder` — The coder object to use to decode the state of the view.

## Discussion

If your app supports state restoration, you should override this method for any views for which you also overrode the [- encodeRestorableStateWithCoder:](<encoderestorablestate(with_).md>) method. Your implementation of this method should use any saved state information to restore the view to its previous configuration. If your [- encodeRestorableStateWithCoder:](<encoderestorablestate(with_).md>) method called `super`, this method should similarly call `super` at some point in its implementation.

## See Also

### Preserving and restoring state

- [restorationIdentifier](restorationidentifier.md) — The identifier that determines whether the view supports state restoration.
- [- encodeRestorableStateWithCoder:](<encoderestorablestate(with_).md>) — Encodes state-related information for the view.
