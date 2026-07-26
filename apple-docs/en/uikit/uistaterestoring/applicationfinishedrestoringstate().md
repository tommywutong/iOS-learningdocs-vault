---
title: applicationFinishedRestoringState()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistaterestoring/applicationfinishedrestoringstate()
source_url: 'https://developer.apple.com/documentation/uikit/uistaterestoring/applicationfinishedrestoringstate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistaterestoring/applicationfinishedrestoringstate%28%29.json'
content_hash: 'sha256:916e902303323f24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStateRestoring](../uistaterestoring.md)

# applicationFinishedRestoringState()

<sub>Instance Method</sub>

Called after all objects have had a chance to decode their state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func applicationFinishedRestoringState()
```

## Discussion

Implement this method, as needed, to perform additional configuration of the restored object. This method is called toward the end of the restoration process when all objects have been decoded. You might use this method to restore state that exists between multiple objects or in cases where you have dependencies that make decoding those objects in a specific order difficult.

The order in which this method is called on decoded objects is not guaranteed.

## See Also

### Encoding and decoding the object

- [- encodeRestorableStateWithCoder:](<encoderestorablestate(with_).md>) — Encodes state-related information for the object.
- [- decodeRestorableStateWithCoder:](<decoderestorablestate(with_).md>) — Decodes and restores state-related information for the object.
