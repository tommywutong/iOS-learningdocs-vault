---
title: 'encodeRestorableState(with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/encoderestorablestate(with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/encoderestorablestate(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/encoderestorablestate%28with%3A%29.json'
content_hash: 'sha256:4bd986b787e20a61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# encodeRestorableState(with:)

<sub>Instance Method</sub>

Encodes state-related information for the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func encodeRestorableState(with coder: NSCoder)
```

## Parameters

- `coder` — The coder object to use to encode the state of the view.

## Discussion

If your app supports state preservation, you can override this method for any views that have state information that should be saved between launches of your app. You should save only the data required to return the view to its current configuration. Do not save the view object itself and do not save any data that could be determined by other means at launch time.

Few views should need to save state information. Most views should just be configured using the data from their view controller. However, this method is available for those views that have user-configurable state that would be otherwise lost between app launches.

Your implementation of this method can encode other restorable view and view controller objects that it needs to reference. Encoding a restorable view or view controller writes that object’s restoration identifier to the coder. (That identifier is used during the decode process to locate the new version of the object.) If the view or view controller defines its own version of this method, that method is also called at some point so that the object can encode its own state.

Apart from views and view controllers, other objects follow the normal serialization process and must adopt the [NSCoding](../../foundation/nscoding.md) protocol before they can be encoded. Encoding such objects embeds the object’s contents in the archive directly. During the decode process, a new object is created and initialized with the data from the archive.

It is recommended that you call `super` at some point during your implementation to give parent classes an opportunity to save their state information.

## See Also

### Preserving and restoring state

- [restorationIdentifier](restorationidentifier.md) — The identifier that determines whether the view supports state restoration.
- [- decodeRestorableStateWithCoder:](<decoderestorablestate(with_).md>) — Decodes and restores state-related information for the view.
