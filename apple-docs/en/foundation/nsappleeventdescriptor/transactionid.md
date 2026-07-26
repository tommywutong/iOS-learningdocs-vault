---
title: transactionID
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsappleeventdescriptor/transactionid
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/transactionid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/transactionid.json'
content_hash: 'sha256:08fcda285531a3d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# transactionID

<sub>Instance Property</sub>

The receiver’s transaction ID, if any.

<sub>Mac Catalyst, macOS</sub>

```swift
var transactionID: AETransactionID { get }
```

## Discussion

The receiver’s transaction ID (an integer value), or 0 if an error occurs.

The receiver must be an Apple event. Currently provides no indication if an error occurs. For more information on transactions, see the description for [+ appleEventWithEventClass:eventID:targetDescriptor:returnID:transactionID:](<appleevent(witheventclass_eventid_targetdescriptor_returnid_transactionid_).md>).

## See Also

### Working With Apple Event Descriptors

- [- attributeDescriptorForKeyword:](<attributedescriptor(forkeyword_).md>) — Returns a descriptor for the receiver’s Apple event attribute identified by the specified keyword.
- [eventClass](eventclass.md) — The event class for the receiver.
- [eventID](eventid.md) — The event ID for the receiver.
- [- paramDescriptorForKeyword:](<paramdescriptor(forkeyword_).md>) — Returns a descriptor for the receiver’s Apple event parameter identified by the specified keyword.
- [- removeParamDescriptorWithKeyword:](<removeparamdescriptor(withkeyword_).md>) — Removes the receiver’s parameter descriptor identified by the specified keyword.
- [returnID](returnid.md) — The receiver’s return ID (the ID for a reply Apple event).
- [- setAttributeDescriptor:forKeyword:](<setattribute(__forkeyword_).md>) — Adds a descriptor to the receiver as an attribute identified by the specified keyword.
- [- setParamDescriptor:forKeyword:](<setparam(__forkeyword_).md>) — Adds a descriptor to the receiver as an Apple event parameter identified by the specified keyword.
