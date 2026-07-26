---
title: widgetLargestAvailableDisplayMode
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+（14.0 起废弃）, iPadOS 10.0+（14.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsextensioncontext/widgetlargestavailabledisplaymode
source_url: 'https://developer.apple.com/documentation/foundation/nsextensioncontext/widgetlargestavailabledisplaymode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensioncontext/widgetlargestavailabledisplaymode.json'
content_hash: 'sha256:1e3ae145b616601d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExtensionContext](../nsextensioncontext.md)

# widgetLargestAvailableDisplayMode

<sub>Instance Property</sub>

The largest display mode the widget supports.

> [!warning] Deprecated
> Use [WidgetKit](../../widgetkit.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var widgetLargestAvailableDisplayMode: NCWidgetDisplayMode { get set }
```

## Discussion

The default value of this property is [NCWidgetDisplayMode.compact](../../notificationcenter/ncwidgetdisplaymode/compact.md). At any time, you can change the largest display mode your widget supports by changing the value of this property. For example, you can update the property value as more or less content is available to display in your widget.

## See Also

### Deprecated

- [- completeRequestWithBroadcastURL:broadcastConfiguration:setupInfo:](<completerequest(withbroadcast_broadcastconfiguration_setupinfo_).md>) — Tells the host app to complete the app extension request with the specified broadcast information. _(deprecated)_
- [widgetActiveDisplayMode](widgetactivedisplaymode.md) — The active display mode of the widget. _(deprecated)_
- [- widgetMaximumSizeForDisplayMode:](<widgetmaximumsize(for_).md>) — Returns the maximum size for the specified widget display mode. _(deprecated)_
