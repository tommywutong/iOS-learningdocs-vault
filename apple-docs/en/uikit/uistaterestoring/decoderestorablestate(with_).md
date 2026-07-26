---
title: 'decodeRestorableState(with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uistaterestoring/decoderestorablestate(with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uistaterestoring/decoderestorablestate(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistaterestoring/decoderestorablestate%28with%3A%29.json'
content_hash: 'sha256:69027a216e44ca41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStateRestoring](../uistaterestoring.md)

# decodeRestorableState(with:)

<sub>Instance Method</sub>

Decodes and restores state-related information for the object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func decodeRestorableState(with coder: NSCoder)
```

## Parameters

- `coder` — The coder object to use to decode the state of the view.

## Discussion

If your app supports state restoration, you can implement this method on any object for which you also overrode the [- encodeRestorableStateWithCoder:](<encoderestorablestate(with_).md>) method. Your implementation of this method should read any saved state information from the archive and use it to restore the object to its previous configuration. If your [- encodeRestorableStateWithCoder:](<encoderestorablestate(with_).md>) method called `super`, this method should similarly call `super` at some point in its implementation.

## See Also

### Encoding and decoding the object

- [- encodeRestorableStateWithCoder:](<encoderestorablestate(with_).md>) — Encodes state-related information for the object.
- [- applicationFinishedRestoringState](<applicationfinishedrestoringstate().md>) — Called after all objects have had a chance to decode their state.
