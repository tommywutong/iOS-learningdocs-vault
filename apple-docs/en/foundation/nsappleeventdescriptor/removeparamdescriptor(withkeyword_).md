---
title: 'removeParamDescriptor(withKeyword:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventdescriptor/removeparamdescriptor(withkeyword:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/removeparamdescriptor(withkeyword:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/removeparamdescriptor%28withkeyword%3A%29.json'
content_hash: 'sha256:c526440fcb0a0e79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# removeParamDescriptor(withKeyword:)

<sub>Instance Method</sub>

Removes the receiver’s parameter descriptor identified by the specified keyword.

<sub>Mac Catalyst, macOS</sub>

```swift
func removeParamDescriptor(withKeyword keyword: AEKeyword)
```

## Parameters

- `keyword` — A keyword (a four-character code) that identifies the parameter descriptor to remove. Currently provides no indication if an error occurs.

## Discussion

The receiver must be an Apple event or Apple event record, both of which can contain parameters.

## See Also

### Working With Apple Event Descriptors

- [- attributeDescriptorForKeyword:](<attributedescriptor(forkeyword_).md>) — Returns a descriptor for the receiver’s Apple event attribute identified by the specified keyword.
- [eventClass](eventclass.md) — The event class for the receiver.
- [eventID](eventid.md) — The event ID for the receiver.
- [- paramDescriptorForKeyword:](<paramdescriptor(forkeyword_).md>) — Returns a descriptor for the receiver’s Apple event parameter identified by the specified keyword.
- [returnID](returnid.md) — The receiver’s return ID (the ID for a reply Apple event).
- [- setAttributeDescriptor:forKeyword:](<setattribute(__forkeyword_).md>) — Adds a descriptor to the receiver as an attribute identified by the specified keyword.
- [- setParamDescriptor:forKeyword:](<setparam(__forkeyword_).md>) — Adds a descriptor to the receiver as an Apple event parameter identified by the specified keyword.
- [transactionID](transactionid.md) — The receiver’s transaction ID, if any.
