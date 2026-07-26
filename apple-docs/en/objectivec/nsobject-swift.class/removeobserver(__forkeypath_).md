---
title: 'removeObserver(_:forKeyPath:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/removeobserver(_:forkeypath:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/removeobserver(_:forkeypath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/removeobserver%28_%3Aforkeypath%3A%29.json'
content_hash: 'sha256:99cb80f30604b824'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# removeObserver(_:forKeyPath:)

<sub>Instance Method</sub>

Stops the observer object from receiving change notifications for the property specified by the key path relative to the object receiving this message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)
```

## Parameters

- `observer` — The object to remove as an observer.

- `keyPath` — A key-path, relative to the object receiving this message, for which `observer` is registered to receive KVO change notifications.

## Discussion

It is an error to call [- removeObserver:forKeyPath:](<removeobserver(__forkeypath_).md>) for an `object` that has not previously been registered as an observer.

Be sure to invoke this method (or [- removeObserver:forKeyPath:context:](<removeobserver(__forkeypath_context_).md>)) before any object specified in [- addObserver:forKeyPath:options:context:](<addobserver(__forkeypath_options_context_).md>) is deallocated.

## See Also

### Registering for Observation

- [- addObserver:forKeyPath:options:context:](<addobserver(__forkeypath_options_context_).md>) — Registers the observer object to receive KVO notifications for the key path relative to the object receiving this message.
- [- removeObserver:forKeyPath:context:](<removeobserver(__forkeypath_context_).md>) — Stops the observer object from receiving change notifications for the property specified by the key path relative to the object receiving this message, given the context.
