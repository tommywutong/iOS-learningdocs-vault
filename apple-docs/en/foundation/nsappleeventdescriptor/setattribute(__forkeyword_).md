---
title: 'setAttribute(_:forKeyword:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventdescriptor/setattribute(_:forkeyword:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/setattribute(_:forkeyword:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/setattribute%28_%3Aforkeyword%3A%29.json'
content_hash: 'sha256:1550eb1e15dba825'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# setAttribute(_:forKeyword:)

<sub>Instance Method</sub>

Adds a descriptor to the receiver as an attribute identified by the specified keyword.

<sub>Mac Catalyst, macOS</sub>

```swift
func setAttribute(_ descriptor: NSAppleEventDescriptor, forKeyword keyword: AEKeyword)
```

## Parameters

- `descriptor` — The attribute descriptor to add to the receiver.

- `keyword` — A keyword (a four-character code) that identifies the attribute descriptor to add. If a descriptor with that keyword already exists in the receiver, it is replaced.

## Discussion

The receiver must be an Apple event. Currently provides no indication if an error occurs.

## See Also

### Working With Apple Event Descriptors

- [- attributeDescriptorForKeyword:](<attributedescriptor(forkeyword_).md>) — Returns a descriptor for the receiver’s Apple event attribute identified by the specified keyword.
- [eventClass](eventclass.md) — The event class for the receiver.
- [eventID](eventid.md) — The event ID for the receiver.
- [- paramDescriptorForKeyword:](<paramdescriptor(forkeyword_).md>) — Returns a descriptor for the receiver’s Apple event parameter identified by the specified keyword.
- [- removeParamDescriptorWithKeyword:](<removeparamdescriptor(withkeyword_).md>) — Removes the receiver’s parameter descriptor identified by the specified keyword.
- [returnID](returnid.md) — The receiver’s return ID (the ID for a reply Apple event).
- [- setParamDescriptor:forKeyword:](<setparam(__forkeyword_).md>) — Adds a descriptor to the receiver as an Apple event parameter identified by the specified keyword.
- [transactionID](transactionid.md) — The receiver’s transaction ID, if any.
