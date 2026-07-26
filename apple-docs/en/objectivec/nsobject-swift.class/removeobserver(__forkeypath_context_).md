---
title: 'removeObserver(_:forKeyPath:context:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/removeobserver(_:forkeypath:context:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/removeobserver(_:forkeypath:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/removeobserver%28_%3Aforkeypath%3Acontext%3A%29.json'
content_hash: 'sha256:197362223cfe6e3d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# removeObserver(_:forKeyPath:context:)

<sub>Instance Method</sub>

Stops the observer object from receiving change notifications for the property specified by the key path relative to the object receiving this message, given the context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context: UnsafeMutableRawPointer?)
```

## Parameters

- `observer` — The object to remove as an observer.

- `keyPath` — A key-path, relative to the observed object, for which `observer` is registered to receive KVO change notifications.

- `context` — Arbitrary data that more specifically identifies the observer to be removed.

## Discussion

Examining the value in `context` you are able to determine precisely which [- addObserver:forKeyPath:options:context:](<addobserver(__forkeypath_options_context_).md>) invocation was used to create the observation relationship. When the same observer is registered for the same key-path multiple times, but with different context pointers, an application can determine specifically which object to stop observing. It is an error to call [- removeObserver:forKeyPath:context:](<removeobserver(__forkeypath_context_).md>) if the object has not been registered as an observer.

Be sure to invoke this method (or [- removeObserver:forKeyPath:](<removeobserver(__forkeypath_).md>)) before any object specified in [- addObserver:forKeyPath:options:context:](<addobserver(__forkeypath_options_context_).md>) is deallocated.

## See Also

### Registering for Observation

- [- addObserver:forKeyPath:options:context:](<addobserver(__forkeypath_options_context_).md>) — Registers the observer object to receive KVO notifications for the key path relative to the object receiving this message.
- [- removeObserver:forKeyPath:](<removeobserver(__forkeypath_).md>) — Stops the observer object from receiving change notifications for the property specified by the key path relative to the object receiving this message.
