---
title: 'encodeRestorableState(with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uistaterestoring/encoderestorablestate(with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uistaterestoring/encoderestorablestate(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistaterestoring/encoderestorablestate%28with%3A%29.json'
content_hash: 'sha256:45b86fe221e935bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStateRestoring](../uistaterestoring.md)

# encodeRestorableState(with:)

<sub>Instance Method</sub>

Encodes state-related information for the object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func encodeRestorableState(with coder: NSCoder)
```

## Parameters

- `coder` — The coder object to use to encode the state of the object.

## Discussion

You can implement this method for any object that has state information you want to preserve. When deciding what data to save, write the smallest amount of data needed to restore the object to its current configuration. The information you save should be data that you could not easily recreate. You can also save references to other objects, such as the view controller that was using the object.

> [!important] Important
> This method is not a substitute for saving your app’s data structures persistently to disk. You should continue to save your app’s actual data to iCloud or the local file system using existing techniques. This method is intended only for saving configuration state or other information related to your app’s user interface. You should consider any data you write to the coder as purgeable and be prepared for it to be unavailable during subsequent launches.

It is strongly recommended that you call `super` at some point during your implementation to give parent classes an opportunity to save information too.

## See Also

### Encoding and decoding the object

- [- decodeRestorableStateWithCoder:](<decoderestorablestate(with_).md>) — Decodes and restores state-related information for the object.
- [- applicationFinishedRestoringState](<applicationfinishedrestoringstate().md>) — Called after all objects have had a chance to decode their state.
