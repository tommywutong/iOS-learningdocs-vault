---
title: 'addObserver(_:forKeyPath:options:context:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/addobserver(_:forkeypath:options:context:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/addobserver(_:forkeypath:options:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/addobserver%28_%3Aforkeypath%3Aoptions%3Acontext%3A%29.json'
content_hash: 'sha256:a9948135507c6d34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# addObserver(_:forKeyPath:options:context:)

<sub>Instance Method</sub>

Registers the observer object to receive KVO notifications for the key path relative to the object receiving this message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options: NSKeyValueObservingOptions = [], context: UnsafeMutableRawPointer?)
```

## Parameters

- `observer` — The object to register for KVO notifications. The observer must implement the key-value observing method [- observeValueForKeyPath:ofObject:change:context:](<observevalue(forkeypath_of_change_context_).md>).

- `keyPath` — The key path, relative to the object receiving this message, of the property to observe. This value must not be `nil`.

- `options` — A combination of the `NSKeyValueObservingOptions` values that specifies what is included in observation notifications. For possible values, see [NSKeyValueObservingOptions](../../foundation/nskeyvalueobservingoptions.md).

- `context` — Arbitrary data that is passed to `observer` in [- observeValueForKeyPath:ofObject:change:context:](<observevalue(forkeypath_of_change_context_).md>).

## Discussion

Neither the object receiving this message, nor `observer`, are retained. An object that calls this method must also eventually call either the [- removeObserver:forKeyPath:](<removeobserver(__forkeypath_).md>) or [- removeObserver:forKeyPath:context:](<removeobserver(__forkeypath_context_).md>) method to unregister the observer when participating in KVO.

## See Also

### Registering for Observation

- [- removeObserver:forKeyPath:](<removeobserver(__forkeypath_).md>) — Stops the observer object from receiving change notifications for the property specified by the key path relative to the object receiving this message.
- [- removeObserver:forKeyPath:context:](<removeobserver(__forkeypath_context_).md>) — Stops the observer object from receiving change notifications for the property specified by the key path relative to the object receiving this message, given the context.
