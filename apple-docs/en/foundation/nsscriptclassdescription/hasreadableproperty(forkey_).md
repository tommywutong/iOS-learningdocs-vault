---
title: 'hasReadableProperty(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptclassdescription/hasreadableproperty(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptclassdescription/hasreadableproperty(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptclassdescription/hasreadableproperty%28forkey%3A%29.json'
content_hash: 'sha256:c77335fcf462a67b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptClassDescription](../nsscriptclassdescription.md)

# hasReadableProperty(forKey:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the described class has a readable property identified by the specified key.

<sub>macOS</sub>

```swift
func hasReadableProperty(forKey key: String) -> Bool
```

## Parameters

- `key` — The identifying key for a property of the receiver.

## Return Value

[true](../../swift/true.md) if the described class has a readable property identified by the specified key; otherwise, [false](../../swift/false.md).

## Discussion

To determine if a property is read-only, invoke [- hasWritablePropertyForKey:](<haswritableproperty(forkey_).md>)/

## See Also

### Getting attribute and relationship information

- [- hasOrderedToManyRelationshipForKey:](<hasorderedtomanyrelationship(forkey_).md>) — Returns a Boolean value indicating whether the described class has an ordered to-many relationship identified by the specified key.
- [- hasPropertyForKey:](<hasproperty(forkey_).md>) — Returns a Boolean value indicating whether the described class has a property identified by the specified key.
- [- hasWritablePropertyForKey:](<haswritableproperty(forkey_).md>) — Returns a Boolean value indicating whether the described class has a writable property identified by the specified key.
- [- keyWithAppleEventCode:](<key(withappleeventcode_).md>) — Given an Apple event code that identifies a property or element class, returns the key for the corresponding attribute, one-to-one relationship, or one-to-many relationship.
- [- typeForKey:](<type(forkey_).md>) — Returns the name of the declared type of the attribute or relationship identified by the passed key.
