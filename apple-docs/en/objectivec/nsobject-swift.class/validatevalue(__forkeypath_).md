---
title: 'validateValue(_:forKeyPath:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/validatevalue(_:forkeypath:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/validatevalue(_:forkeypath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/validatevalue%28_%3Aforkeypath%3A%29.json'
content_hash: 'sha256:dba4241934236cb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# validateValue(_:forKeyPath:)

<sub>Instance Method</sub>

Indicates whether the value specified by a given pointer is not valid for a given key path relative to the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws
```

## Parameters

- `ioValue` — A pointer to a new value for the property identified by `inKeyPath`. This method may modify or replace the value in order to make it valid.

- `inKeyPath` — The name of one of the receiver’s properties. The key path must specify an attribute or a to-one relationship. The key path has the form `relationship``.``property` (with one or more relationships); for example `department.name` or `department.manager.lastName`.

## Discussion

In Swift, this method throws an error if the value isn’t valid.  In Objective-C, it returns a Boolean value.

The default implementation of this method gets the destination object for each relationship using [- valueForKey:](<value(forkey_).md>) and returns the result of calling the [- validateValue:forKey:error:](<validatevalue(__forkey_).md>) method for the property.

## See Also

### Validation

- [- validateValue:forKey:error:](<validatevalue(__forkey_).md>) — Indicates whether the value specified by a given pointer is valid, or can be made valid, for the property identified by a given key.
