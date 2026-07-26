---
title: contentStateUpdates
framework: ActivityKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.1+（16.2 起废弃）, iPadOS 16.1+（16.2 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/activitykit/activity/contentstateupdates-swift.property
source_url: 'https://developer.apple.com/documentation/activitykit/activity/contentstateupdates-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/contentstateupdates-swift.property.json'
content_hash: 'sha256:3c6f84a999c8ed60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# contentStateUpdates

<sub>Instance Property</sub>

An asynchronous sequence you use to observe changes to the dynamic content of a Live Activity.

> [!warning] Deprecated
> Use contentUpdates instead

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var contentStateUpdates: Activity<Attributes>.ContentStateUpdates { get }
```

## See Also

### Deprecated

- [request(attributes:contentState:pushType:)](<request(attributes_contentstate_pushtype_).md>) — Requests and starts a Live Activity. _(deprecated)_
- [update(using:)](<update(using_).md>) — Updates the dynamic content of the Live Activity. _(deprecated)_
- [update(using:alertConfiguration:)](<update(using_alertconfiguration_).md>) — Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update. _(deprecated)_
- [end(using:dismissalPolicy:)](<end(using_dismissalpolicy_).md>) — Ends an active Live Activity. _(deprecated)_
- [contentState](contentstate-swift.property.md) — The dynamic content of a Live Activity. _(deprecated)_
- [ContentStateUpdates](contentstateupdates-swift.struct.md) — A structure that offers functionality to observe changes to the dynamic content of a Live Activity. _(deprecated)_
