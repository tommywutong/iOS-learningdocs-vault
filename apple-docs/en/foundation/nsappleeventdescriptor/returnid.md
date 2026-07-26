---
title: returnID
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsappleeventdescriptor/returnid
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/returnid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/returnid.json'
content_hash: 'sha256:5b84caf850df279b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# returnID

<sub>Instance Property</sub>

The receiver’s return ID (the ID for a reply Apple event).

<sub>Mac Catalyst, macOS</sub>

```swift
var returnID: AEReturnID { get }
```

## Discussion

The receiver’s return ID (an integer value), or 0 if an error occurs.

The receiver must be an Apple event.

## See Also

### Working With Apple Event Descriptors

- [- attributeDescriptorForKeyword:](<attributedescriptor(forkeyword_).md>) — Returns a descriptor for the receiver’s Apple event attribute identified by the specified keyword.
- [eventClass](eventclass.md) — The event class for the receiver.
- [eventID](eventid.md) — The event ID for the receiver.
- [- paramDescriptorForKeyword:](<paramdescriptor(forkeyword_).md>) — Returns a descriptor for the receiver’s Apple event parameter identified by the specified keyword.
- [- removeParamDescriptorWithKeyword:](<removeparamdescriptor(withkeyword_).md>) — Removes the receiver’s parameter descriptor identified by the specified keyword.
- [- setAttributeDescriptor:forKeyword:](<setattribute(__forkeyword_).md>) — Adds a descriptor to the receiver as an attribute identified by the specified keyword.
- [- setParamDescriptor:forKeyword:](<setparam(__forkeyword_).md>) — Adds a descriptor to the receiver as an Apple event parameter identified by the specified keyword.
- [transactionID](transactionid.md) — The receiver’s transaction ID, if any.
