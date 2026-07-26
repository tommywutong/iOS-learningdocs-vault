---
title: 'end(using:dismissalPolicy:)'
framework: ActivityKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.1+（16.2 起废弃）, iPadOS 16.1+（16.2 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/activitykit/activity/end(using:dismissalpolicy:)'
source_url: 'https://developer.apple.com/documentation/activitykit/activity/end(using:dismissalpolicy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/end%28using%3Adismissalpolicy%3A%29.json'
content_hash: 'sha256:2a05797230a32c98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# end(using:dismissalPolicy:)

<sub>Instance Method</sub>

Ends an active Live Activity.

> [!warning] Deprecated
> Use end(content:dismissalPolicy:) instead

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func end(using contentState: Activity<Attributes>.ContentState? = nil, dismissalPolicy: ActivityUIDismissalPolicy = .default) async
```

## Parameters

- `contentState` — The latest and final dynamic content for the Live Activity that ended. The size of the encoded content can’t exceed 4KB in size.

- `dismissalPolicy` — Describes how and when the system should dismiss a Live Activity and and remove it from the Lock Screen.

## Discussion

End an active Live Activity while your app is in the foreground or while it’s in the background — for example, by using [Background Tasks](../../backgroundtasks.md).

Include updated data in the `contentState` parameter to ensure the Live Activity shows the latest and final content update after it ends. This is important because the Live Activity remains visible until the system or the person removes it.

## See Also

### Deprecated

- [request(attributes:contentState:pushType:)](<request(attributes_contentstate_pushtype_).md>) — Requests and starts a Live Activity. _(deprecated)_
- [update(using:)](<update(using_).md>) — Updates the dynamic content of the Live Activity. _(deprecated)_
- [update(using:alertConfiguration:)](<update(using_alertconfiguration_).md>) — Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update. _(deprecated)_
- [contentState](contentstate-swift.property.md) — The dynamic content of a Live Activity. _(deprecated)_
- [contentStateUpdates](contentstateupdates-swift.property.md) — An asynchronous sequence you use to observe changes to the dynamic content of a Live Activity. _(deprecated)_
- [ContentStateUpdates](contentstateupdates-swift.struct.md) — A structure that offers functionality to observe changes to the dynamic content of a Live Activity. _(deprecated)_
