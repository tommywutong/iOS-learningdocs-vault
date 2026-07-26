---
title: UIKeyboardCenterBeginUserInfoKey
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+（3.2 起废弃）, iPadOS 2.0+（3.2 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uikeyboardcenterbeginuserinfokey
source_url: 'https://developer.apple.com/documentation/uikit/uikeyboardcenterbeginuserinfokey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeyboardcenterbeginuserinfokey.json'
content_hash: 'sha256:b643dbda4894d26e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIKeyboardCenterBeginUserInfoKey

<sub>Global Variable</sub>

A user info key to retrieve the center point of the keyboard before its animation begins.

> [!warning] Deprecated
> Use [UIKeyboardFrameBeginUserInfoKey](uiresponder/keyboardframebeginuserinfokey.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSString * const UIKeyboardCenterBeginUserInfoKey;
```

## Discussion

The value for this key is an [NSValue](../foundation/nsvalue.md) object containing a [CGPoint](../corefoundation/cgpoint.md) that identifies the keyboard’s center point, in the window’s coordinate space, before its animation begins. These coordinates take into account any rotation factors applied to the window’s contents as a result of interface orientation changes. Thus, the center point of the keyboard is different in portrait versus landscape orientations.

## See Also

### Deprecated

- [UIKeyboardCenterEndUserInfoKey](uikeyboardcenterenduserinfokey.md) — A user info key to retrieve the center point of the keyboard after its animation completes. _(deprecated)_
- [UIKeyboardBoundsUserInfoKey](uikeyboardboundsuserinfokey.md) — A user info key to retrieve the bounds of the keyboard. _(deprecated)_
