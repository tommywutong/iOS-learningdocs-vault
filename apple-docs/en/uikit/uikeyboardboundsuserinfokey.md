---
title: UIKeyboardBoundsUserInfoKey
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+（3.2 起废弃）, iPadOS 2.0+（3.2 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uikeyboardboundsuserinfokey
source_url: 'https://developer.apple.com/documentation/uikit/uikeyboardboundsuserinfokey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeyboardboundsuserinfokey.json'
content_hash: 'sha256:a0c1a159c9e7dbf8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIKeyboardBoundsUserInfoKey

<sub>Global Variable</sub>

A user info key to retrieve the bounds of the keyboard.

> [!warning] Deprecated
> Use [UIKeyboardFrameBeginUserInfoKey](uiresponder/keyboardframebeginuserinfokey.md) or [UIKeyboardFrameEndUserInfoKey](uiresponder/keyboardframeenduserinfokey.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSString * const UIKeyboardBoundsUserInfoKey;
```

## Discussion

The value for this key is an [NSValue](../foundation/nsvalue.md) object containing a [CGRect](../corefoundation/cgrect.md) that identifies the bounds rectangle of the keyboard in the window coordinate space. This value is sufficient for obtaining the size of the keyboard. If you want to get the origin of the keyboard on the screen (before or after animation), use the values obtained from the user info dictionary through the [UIKeyboardCenterBeginUserInfoKey](uikeyboardcenterbeginuserinfokey.md) or [UIKeyboardCenterEndUserInfoKey](uikeyboardcenterenduserinfokey.md) constants.

## See Also

### Deprecated

- [UIKeyboardCenterBeginUserInfoKey](uikeyboardcenterbeginuserinfokey.md) — A user info key to retrieve the center point of the keyboard before its animation begins. _(deprecated)_
- [UIKeyboardCenterEndUserInfoKey](uikeyboardcenterenduserinfokey.md) — A user info key to retrieve the center point of the keyboard after its animation completes. _(deprecated)_
