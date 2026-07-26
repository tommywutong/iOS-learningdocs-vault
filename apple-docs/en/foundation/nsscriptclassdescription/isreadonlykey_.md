---
title: 'isReadOnlyKey:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.5 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsscriptclassdescription/isreadonlykey:'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptclassdescription/isreadonlykey:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptclassdescription/isreadonlykey%3A.json'
content_hash: 'sha256:5b5e8dd04a6b1e5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptClassDescription](../nsscriptclassdescription.md)

# isReadOnlyKey:

<sub>Instance Method</sub>

Returns a Boolean value indicating whether a specified property in the receiver is read-only.

> [!warning] Deprecated
> Use [- hasWritablePropertyForKey:](<haswritableproperty(forkey_).md>) instead.

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) isReadOnlyKey:(NSString *) key;
```

## Parameters

- `key` — The identifying key for a property of the receiver.

## Return Value

[true](../../swift/true.md) if the property specified by `key` exists in the receiver or in the `NSScriptClassDescription` for any superclass, and is read only; otherwise, [false](../../swift/false.md).

## Discussion

This method could return [false](../../swift/false.md) either because `key` is unrecognized or because writing to the property is not supported. Use [- hasWritablePropertyForKey:](<haswritableproperty(forkey_).md>) instead.

## See Also

### Getting attribute and relationship information

- [- hasOrderedToManyRelationshipForKey:](<hasorderedtomanyrelationship(forkey_).md>) — Returns a Boolean value indicating whether the described class has an ordered to-many relationship identified by the specified key.
- [- hasPropertyForKey:](<hasproperty(forkey_).md>) — Returns a Boolean value indicating whether the described class has a property identified by the specified key.
- [- hasReadablePropertyForKey:](<hasreadableproperty(forkey_).md>) — Returns a Boolean value indicating whether the described class has a readable property identified by the specified key.
- [- hasWritablePropertyForKey:](<haswritableproperty(forkey_).md>) — Returns a Boolean value indicating whether the described class has a writable property identified by the specified key.
- [- keyWithAppleEventCode:](<key(withappleeventcode_).md>) — Given an Apple event code that identifies a property or element class, returns the key for the corresponding attribute, one-to-one relationship, or one-to-many relationship.
- [- typeForKey:](<type(forkey_).md>) — Returns the name of the declared type of the attribute or relationship identified by the passed key.
