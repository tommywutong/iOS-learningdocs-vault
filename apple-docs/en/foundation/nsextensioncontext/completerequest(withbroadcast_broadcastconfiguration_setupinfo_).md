---
title: 'completeRequest(withBroadcast:broadcastConfiguration:setupInfo:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+（11.0 起废弃）, iPadOS 10.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 10.0+（11.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsextensioncontext/completerequest(withbroadcast:broadcastconfiguration:setupinfo:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsextensioncontext/completerequest(withbroadcast:broadcastconfiguration:setupinfo:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensioncontext/completerequest%28withbroadcast%3Abroadcastconfiguration%3Asetupinfo%3A%29.json'
content_hash: 'sha256:e834efe87ef9864a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExtensionContext](../nsextensioncontext.md)

# completeRequest(withBroadcast:broadcastConfiguration:setupInfo:)

<sub>Instance Method</sub>

Tells the host app to complete the app extension request with the specified broadcast information.

> [!warning] Deprecated
> Use [- completeRequestWithBroadcastURL:setupInfo:](<completerequest(withbroadcast_setupinfo_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func completeRequest(withBroadcast broadcastURL: URL, broadcastConfiguration: RPBroadcastConfiguration, setupInfo: [String : any NSCoding & NSObjectProtocol]?)
```

## See Also

### Deprecated

- [widgetActiveDisplayMode](widgetactivedisplaymode.md) — The active display mode of the widget. _(deprecated)_
- [widgetLargestAvailableDisplayMode](widgetlargestavailabledisplaymode.md) — The largest display mode the widget supports. _(deprecated)_
- [- widgetMaximumSizeForDisplayMode:](<widgetmaximumsize(for_).md>) — Returns the maximum size for the specified widget display mode. _(deprecated)_
