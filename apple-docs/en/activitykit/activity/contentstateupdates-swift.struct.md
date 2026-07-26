---
title: Activity.ContentStateUpdates
framework: ActivityKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.1+（16.2 起废弃）, iPadOS 16.1+（16.2 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/activitykit/activity/contentstateupdates-swift.struct
source_url: 'https://developer.apple.com/documentation/activitykit/activity/contentstateupdates-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/contentstateupdates-swift.struct.json'
content_hash: 'sha256:0442aa0c3fd73e2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# Activity.ContentStateUpdates

<sub>Structure</sub>

A structure that offers functionality to observe changes to the dynamic content of a Live Activity.

> [!warning] Deprecated
> Use `ContentUpdates` instead

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct ContentStateUpdates
```

## Relationships

- **Conforms To**: [AsyncSequence](../../swift/asyncsequence.md)

## Topics

### Creating an iterator

- [makeAsyncIterator()](<contentstateupdates-swift.struct/makeasynciterator().md>) — Creates the asynchronous iterator that produces results from this asynchronous sequence. _(deprecated)_
- [Iterator](contentstateupdates-swift.struct/iterator.md) — An iterator for accessing individual data entries from the series. _(deprecated)_
- [Element](contentstateupdates-swift.struct/element.md) — The type of element this asynchronous sequence produces. _(deprecated)_

## See Also

### Deprecated

- [request(attributes:contentState:pushType:)](<request(attributes_contentstate_pushtype_).md>) — Requests and starts a Live Activity. _(deprecated)_
- [update(using:)](<update(using_).md>) — Updates the dynamic content of the Live Activity. _(deprecated)_
- [update(using:alertConfiguration:)](<update(using_alertconfiguration_).md>) — Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update. _(deprecated)_
- [end(using:dismissalPolicy:)](<end(using_dismissalpolicy_).md>) — Ends an active Live Activity. _(deprecated)_
- [contentState](contentstate-swift.property.md) — The dynamic content of a Live Activity. _(deprecated)_
- [contentStateUpdates](contentstateupdates-swift.property.md) — An asynchronous sequence you use to observe changes to the dynamic content of a Live Activity. _(deprecated)_
