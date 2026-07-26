---
title: 'instantiate(withOwner:options:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uinib/instantiate(withowner:options:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinib/instantiate(withowner:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinib/instantiate%28withowner%3Aoptions%3A%29.json'
content_hash: 'sha256:b8eae742eb49fdbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINib](../uinib.md)

# instantiate(withOwner:options:)

<sub>Instance Method</sub>

Unarchives and instantiates the in-memory contents of the nib object’s nib file, creating a distinct object tree and set of top-level objects.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func instantiate(withOwner ownerOrNil: Any?, options optionsOrNil: [UINib.OptionsKey : Any]? = nil) -> [Any]
```

## Parameters

- `ownerOrNil` — The object to use as the owner of the nib file. If the nib file has an owner, you must specify a valid object for this parameter.

- `optionsOrNil` — A dictionary containing the options to use when opening the nib file. For a list of available keys for this dictionary, see `NSBundle UIKit Additions`.

## Return Value

An autoreleased `NSArray` object containing the top-level objects from the nib file.

## Discussion

You can use this method to instantiate the objects in a nib and provide them to your code. This method unarchives each object, initializes it, sets its properties to their configured values, and reestablishes any connections to other objects. For detailed information about the nib-loading process, see [Resource Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Introduction/Introduction.html#//apple_ref/doc/uid/10000051i).

If the nib file contains any proxy objects beyond just the File’s Owner proxy object, you can specify the runtime replacement objects for those proxies using the options dictionary. In that dictionary, add the [UINibExternalObjects](optionskey/externalobjects.md) key and set its value to a dictionary containing the names of any proxy objects (the keys) and the real objects to use in their place. The proxy object’s name is the string you assign to it in the Name field of the Interface Builder inspector window.

## See Also

### Retrieving objects from the nib file

- [OptionsKey](optionskey.md) — Options that specify how to unarchive and instantiate the nib.
