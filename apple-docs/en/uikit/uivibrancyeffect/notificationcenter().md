---
title: notificationCenter()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uivibrancyeffect/notificationcenter()
source_url: 'https://developer.apple.com/documentation/uikit/uivibrancyeffect/notificationcenter()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uivibrancyeffect/notificationcenter%28%29.json'
content_hash: 'sha256:7c477fab9fa221c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIVibrancyEffect](../uivibrancyeffect.md)

# notificationCenter()

<sub>Type Method</sub>

Creates a vibrancy effect for use in Notification Center.

> [!warning] Deprecated
> Use [+ widgetPrimaryVibrancyEffect](<widgetprimary().md>) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class func notificationCenter() -> UIVibrancyEffect
```

## Return Value

The vibrancy effect that’s appropriate for use in Today widgets in Notification Center. To learn more about Today widgets, see [Today](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/Today.html#//apple_ref/doc/uid/TP40014214-CH11).

## See Also

### Deprecated

- [+ widgetPrimaryVibrancyEffect](<widgetprimary().md>) — Creates a vibrancy effect suitable for use with certain supporting text and template images within a widget. _(deprecated)_
- [+ widgetSecondaryVibrancyEffect](<widgetsecondary().md>) — Creates a vibrancy effect suitable for indicating the secondary importance or relevance of supporting text and template images within a widget. _(deprecated)_
- [+ widgetEffectForVibrancyStyle:](<widgeteffect(forvibrancystyle_).md>) — Creates a vibrancy effect for the specified style. _(deprecated)_
