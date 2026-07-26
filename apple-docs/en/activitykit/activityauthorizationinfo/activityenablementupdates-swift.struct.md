---
title: ActivityAuthorizationInfo.ActivityEnablementUpdates
framework: ActivityKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activityauthorizationinfo/activityenablementupdates-swift.struct
source_url: 'https://developer.apple.com/documentation/activitykit/activityauthorizationinfo/activityenablementupdates-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activityauthorizationinfo/activityenablementupdates-swift.struct.json'
content_hash: 'sha256:ca03f6a9d35d595f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [ActivityAuthorizationInfo](../activityauthorizationinfo.md)

# ActivityAuthorizationInfo.ActivityEnablementUpdates

<sub>Structure</sub>

A structure that offers functionality to observe whether your app can start a Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct ActivityEnablementUpdates
```

## Relationships

- **Conforms To**: [AsyncSequence](../../swift/asyncsequence.md)

## Topics

### Creating an iterator

- [makeAsyncIterator()](<activityenablementupdates-swift.struct/makeasynciterator().md>) — Creates the asynchronous iterator that produces results from this asynchronous sequence.
- [Iterator](activityenablementupdates-swift.struct/iterator.md) — An iterator for accessing individual data entries from the series.
- [Element](activityenablementupdates-swift.struct/element.md) — The type of element this asynchronous sequence produces.

## See Also

### Observing Live Activity permission changes

- [areActivitiesEnabled](areactivitiesenabled.md) — A Boolean value that indicates whether your app can start a Live Activity.
- [activityEnablementUpdates](activityenablementupdates-swift.property.md) — An asynchronous sequence you use to observe whether your app can start a Live Activity.
- [init()](<init().md>) — Creates an object you use to observe user authorizations for starting Live Activities and updating them with ActivityKit push notifications.
