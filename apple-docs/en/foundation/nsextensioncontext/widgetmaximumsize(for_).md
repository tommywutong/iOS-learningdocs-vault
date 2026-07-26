---
title: 'widgetMaximumSize(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+（14.0 起废弃）, iPadOS 10.0+（14.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsextensioncontext/widgetmaximumsize(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsextensioncontext/widgetmaximumsize(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensioncontext/widgetmaximumsize%28for%3A%29.json'
content_hash: 'sha256:d07608017b65d4aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExtensionContext](../nsextensioncontext.md)

# widgetMaximumSize(for:)

<sub>Instance Method</sub>

Returns the maximum size for the specified widget display mode.

> [!warning] Deprecated
> Use [WidgetKit](../../widgetkit.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func widgetMaximumSize(for displayMode: NCWidgetDisplayMode) -> CGSize
```

## Parameters

- `displayMode` — The active display mode of the widget. For possible values, see [NCWidgetDisplayMode](../../notificationcenter/ncwidgetdisplaymode.md).

## See Also

### Deprecated

- [- completeRequestWithBroadcastURL:broadcastConfiguration:setupInfo:](<completerequest(withbroadcast_broadcastconfiguration_setupinfo_).md>) — Tells the host app to complete the app extension request with the specified broadcast information. _(deprecated)_
- [widgetActiveDisplayMode](widgetactivedisplaymode.md) — The active display mode of the widget. _(deprecated)_
- [widgetLargestAvailableDisplayMode](widgetlargestavailabledisplaymode.md) — The largest display mode the widget supports. _(deprecated)_
