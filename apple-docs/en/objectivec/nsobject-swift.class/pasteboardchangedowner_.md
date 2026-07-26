---
title: 'pasteboardChangedOwner:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/pasteboardchangedowner:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/pasteboardchangedowner:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/pasteboardchangedowner%3A.json'
content_hash: 'sha256:9dca6cd25de03cb3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# pasteboardChangedOwner:

<sub>Instance Method</sub>

Notifies a prior owner of the specified pasteboard (and owners of representations on the pasteboard) that the pasteboard has changed owners.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) pasteboardChangedOwner:(NSPasteboard *) sender;
```

## Parameters

- `sender` — The pasteboard object whose owner changed.

## Discussion

Pasteboard owners only need to implement this method if they need to know when they have lost ownership.

The owner is not able to read the contents of the pasteboard when responding to this method. The owner should be prepared to receive this method at any time, even from within the [declareTypes(_:owner:)](<../../appkit/nspasteboard/declaretypes(__owner_).md>) method used to declare ownership.

Once an owner has provided all of its data for declared types, it will not receive a `pasteboardChangedOwner:` message. If, therefore, you are maintaining an object just for the purpose of providing data lazily, rather than relying solely on receipt of a `pasteboardChangedOwner:` message you need to keep track of what types were promised and what types have been provided. When all the types have been provided, you may release the owner.

## See Also

### Related Documentation

- [changeCount](../../appkit/nspasteboard/changecount.md) — The receiver’s change count.
- [declareTypes(_:owner:)](<../../appkit/nspasteboard/declaretypes(__owner_).md>) — Prepares the receiver for a change in its contents by declaring the new types of data it will contain and a new owner.
