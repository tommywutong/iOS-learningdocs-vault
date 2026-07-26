---
title: CFMutableBag
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfmutablebag
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmutablebag'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmutablebag.json'
content_hash: 'sha256:619ee36b9929938f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMutableBag

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFMutableBag
```

## Overview

CFMutableBag manages dynamic bags. The basic interface for managing bags is provided by [CFBag](cfbag.md). CFMutableBag adds functions to modify the contents of a bag.

You create a mutable bag object using either the [CFBagCreateMutable](<cfbagcreatemutable(______).md>) or [CFBagCreateMutableCopy](<cfbagcreatemutablecopy(______).md>) function.

CFMutableBag provides several functions for adding and removing values from a bag. The [CFBagAddValue](<cfbagaddvalue(____).md>) function adds a value to a bag and [CFBagRemoveValue](<cfbagremovevalue(____).md>) removes values from a bag.

## Relationships

- **Inherits From**: [CFBag](cfbag.md)

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Mutable Bag

- [CFBagCreateMutable](<cfbagcreatemutable(______).md>) — Creates a new empty mutable bag.
- [CFBagCreateMutableCopy](<cfbagcreatemutablecopy(______).md>) — Creates a new mutable bag with the values from another bag.

### Modifying a Mutable Bag

- [CFBagAddValue](<cfbagaddvalue(____).md>) — Adds a value to a mutable bag.
- [CFBagRemoveAllValues](<cfbagremoveallvalues(__).md>) — Removes all values from a mutable bag.
- [CFBagRemoveValue](<cfbagremovevalue(____).md>) — Removes a value from a mutable bag.
- [CFBagReplaceValue](<cfbagreplacevalue(____).md>) — Replaces a value in a mutable bag.
- [CFBagSetValue](<cfbagsetvalue(____).md>) — Sets a value in a mutable bag.

## See Also

### Related Documentation

- [Collections Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/CFCollections.html#//apple_ref/doc/uid/10000124i)

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
