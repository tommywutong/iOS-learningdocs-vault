---
title: 'type(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptclassdescription/type(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptclassdescription/type(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptclassdescription/type%28forkey%3A%29.json'
content_hash: 'sha256:c19249bd75388fa3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptClassDescription](../nsscriptclassdescription.md)

# type(forKey:)

<sub>Instance Method</sub>

Returns the name of the declared type of the attribute or relationship identified by the passed key.

<sub>Mac Catalyst, macOS</sub>

```swift
func type(forKey key: String) -> String?
```

## Parameters

- `key` — The identifying key for an attribute, one-to-one relationship, or one-to-many relationship of the receiver.

## Return Value

The name of the declared type of the attribute or relationship identified by `key`; for example, “NSString”. Searches in the receiver first, then in any superclass. Returns `nil` if no match is found.

## See Also

### Getting attribute and relationship information

- [- hasOrderedToManyRelationshipForKey:](<hasorderedtomanyrelationship(forkey_).md>) — Returns a Boolean value indicating whether the described class has an ordered to-many relationship identified by the specified key.
- [- hasPropertyForKey:](<hasproperty(forkey_).md>) — Returns a Boolean value indicating whether the described class has a property identified by the specified key.
- [- hasReadablePropertyForKey:](<hasreadableproperty(forkey_).md>) — Returns a Boolean value indicating whether the described class has a readable property identified by the specified key.
- [- hasWritablePropertyForKey:](<haswritableproperty(forkey_).md>) — Returns a Boolean value indicating whether the described class has a writable property identified by the specified key.
- [- keyWithAppleEventCode:](<key(withappleeventcode_).md>) — Given an Apple event code that identifies a property or element class, returns the key for the corresponding attribute, one-to-one relationship, or one-to-many relationship.
