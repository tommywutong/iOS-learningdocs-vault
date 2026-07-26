---
title: DispatchSpecificKey
framework: Dispatch
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchspecifickey
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchspecifickey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchspecifickey.json'
content_hash: 'sha256:943de8e83ec98642'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchSpecificKey

<sub>Class</sub>

A key associated with a specific contextual value on a dispatch queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class DispatchSpecificKey<T>
```

## Overview

Access the value of a key using the [setSpecific(key:value:)](<dispatchqueue/setspecific(key_value_).md>) and [getSpecific(key:)](<dispatchqueue/getspecific(key_)-swift.method.md>) methods.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Key

- [init()](<dispatchspecifickey/init().md>)

## See Also

### Getting and Setting Contextual Data

- [setSpecific(key:value:)](<dispatchqueue/setspecific(key_value_).md>) — Sets the key/value data for the specified dispatch queue.
- [getSpecific(key:)](<dispatchqueue/getspecific(key_)-swift.method.md>) — Returns the value for the key associated with this dispatch queue.
- [getSpecific(key:)](<dispatchqueue/getspecific(key_)-swift.type.method.md>) — Returns the value for the key associated with the current execution context.
