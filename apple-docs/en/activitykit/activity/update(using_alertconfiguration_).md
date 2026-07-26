---
title: 'update(using:alertConfiguration:)'
framework: ActivityKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.1+（16.2 起废弃）, iPadOS 16.1+（16.2 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/activitykit/activity/update(using:alertconfiguration:)'
source_url: 'https://developer.apple.com/documentation/activitykit/activity/update(using:alertconfiguration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/update%28using%3Aalertconfiguration%3A%29.json'
content_hash: 'sha256:536128c78c1b8d3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# update(using:alertConfiguration:)

<sub>Instance Method</sub>

Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.

> [!warning] Deprecated
> Use update(_:alertConfiguration:) instead

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func update(using contentState: Activity<Attributes>.ContentState, alertConfiguration: AlertConfiguration? = nil) async
```

## Parameters

- `contentState` — The updated dynamic content for the Live Activity. The size of the encoded content can’t exceed 4KB in size.

- `alertConfiguration` — The alert configuration you use to configure how the system notifies a person about the updated content of the Live Activity.

## Discussion

The system ignores updates to a Live Activity that’s in the [ActivityState.ended](../activitystate/ended.md) state.

## See Also

### Deprecated

- [request(attributes:contentState:pushType:)](<request(attributes_contentstate_pushtype_).md>) — Requests and starts a Live Activity. _(deprecated)_
- [update(using:)](<update(using_).md>) — Updates the dynamic content of the Live Activity. _(deprecated)_
- [end(using:dismissalPolicy:)](<end(using_dismissalpolicy_).md>) — Ends an active Live Activity. _(deprecated)_
- [contentState](contentstate-swift.property.md) — The dynamic content of a Live Activity. _(deprecated)_
- [contentStateUpdates](contentstateupdates-swift.property.md) — An asynchronous sequence you use to observe changes to the dynamic content of a Live Activity. _(deprecated)_
- [ContentStateUpdates](contentstateupdates-swift.struct.md) — A structure that offers functionality to observe changes to the dynamic content of a Live Activity. _(deprecated)_
