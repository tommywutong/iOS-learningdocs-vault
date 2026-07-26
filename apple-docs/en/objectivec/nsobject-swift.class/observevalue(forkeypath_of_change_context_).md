---
title: 'observeValue(forKeyPath:of:change:context:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/observevalue(forkeypath:of:change:context:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/observevalue(forkeypath:of:change:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/observevalue%28forkeypath%3Aof%3Achange%3Acontext%3A%29.json'
content_hash: 'sha256:5d8bbe549114a7fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# observeValue(forKeyPath:of:change:context:)

<sub>Instance Method</sub>

Informs the observing object when the value at the specified key path relative to the observed object has changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func observeValue(forKeyPath keyPath: String?, of object: Any?, change: [NSKeyValueChangeKey : Any]?, context: UnsafeMutableRawPointer?)
```

## Parameters

- `keyPath` — The key path, relative to `object`, to the value that has changed.

- `object` — The source object of the key path `keyPath`.

- `change` — A dictionary that describes the changes that have been made to the value of the property at the key path `keyPath` relative to `object`. Entries are described in `Change Dictionary Keys`.

- `context` — The value that was provided when the observer was registered to receive key-value observation notifications.

## Discussion

For an `object` to begin sending change notification messages for the value at `keyPath`, you send it an [- addObserver:forKeyPath:options:context:](<addobserver(__forkeypath_options_context_).md>) message, naming the observing object that should receive the messages. When you are done observing, and in particular before the observing object is deallocated, you send the observed object a [- removeObserver:forKeyPath:](<removeobserver(__forkeypath_).md>) or [- removeObserver:forKeyPath:context:](<removeobserver(__forkeypath_context_).md>) message to unregister the observer, and stop sending change notification messages.
