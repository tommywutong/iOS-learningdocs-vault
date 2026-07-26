---
title: 'setObject:forKeyedSubscript:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledictionary/setobject:forkeyedsubscript:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledictionary/setobject:forkeyedsubscript:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledictionary/setobject%3Aforkeyedsubscript%3A.json'
content_hash: 'sha256:d00d5d558df7b054'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableDictionary](../nsmutabledictionary.md)

# setObject:forKeyedSubscript:

<sub>Instance Method</sub>

Adds a given key-value pair to the dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) setObject:(ObjectType) obj forKeyedSubscript:(id<NSCopying>) key;
```

## Parameters

- `obj` — The value for `key`. A strong reference to the object is maintained by the dictionary. Passing `nil` will cause any object corresponding to `key` to be removed from the dictionary.

- `key` — The key for `obj`. The key is copied (using [- copyWithZone:](<../nscopying/copy(with_).md>); keys must conform to the `NSCopying` protocol). If `key` already exists in the dictionary, `anObject` takes its place. > [!important] Important > Raises an [NSInvalidArgumentException](../nsexceptionname/invalidargumentexception.md) if `key` is `nil`.

## Discussion

This method has the same behavior as the [- setObject:forKey:](<setobject(__forkey_).md>) method.

You shouldn’t need to call this method directly. Instead, this method is called when setting an object for a key using subscripting.

```objc
id value = @"someValue";
mutableDictionary[@"someKey"] = value;
```

## See Also

### Related Documentation

- [- removeObjectForKey:](<removeobject(forkey_).md>) — Removes a given key and its associated value from the dictionary.
- [- objectForKeyedSubscript:](<../nsdictionary/subscript(__)-52n56.md>) — Returns the value associated with a given key.

### Adding Entries to a Mutable Dictionary

- [- setObject:forKey:](<setobject(__forkey_).md>) — Adds a given key-value pair to the dictionary.
- [- setValue:forKey:](<setvalue(__forkey_).md>) — Adds a given key-value pair to the dictionary.
- [- addEntriesFromDictionary:](<addentries(from_).md>) — Adds to the receiving dictionary the entries from another dictionary.
- [- setDictionary:](<setdictionary(__).md>) — Sets the contents of the receiving dictionary to entries in a given dictionary.
