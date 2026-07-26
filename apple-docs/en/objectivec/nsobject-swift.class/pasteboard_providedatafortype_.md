---
title: 'pasteboard:provideDataForType:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/pasteboard:providedatafortype:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/pasteboard:providedatafortype:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/pasteboard%3Aprovidedatafortype%3A.json'
content_hash: 'sha256:f77690d29f013d66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# pasteboard:provideDataForType:

<sub>Instance Method</sub>

Implemented by an owner object to provide promised data.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) pasteboard:(NSPasteboard *) sender provideDataForType:(NSPasteboardType) type;
```

## Parameters

- `sender` — The pasteboard that requires the specified data for a paste operation.

- `type` — The type of data the owner object must provide.

## Discussion

The receiver should have been previously declared in a [declareTypes(_:owner:)](<../../appkit/nspasteboard/declaretypes(__owner_).md>) message.

The requested data should be written to `sender` using the [setData(_:forType:)](<../../appkit/nspasteboard/setdata(__fortype_).md>), [setPropertyList(_:forType:)](<../../appkit/nspasteboard/setpropertylist(__fortype_).md>), or [setString(_:forType:)](<../../appkit/nspasteboard/setstring(__fortype_).md>) method. The [pasteboard:provideDataForType:](pasteboard_providedatafortype_.md) messages may also be sent to the owner when the application is shut down through an application’s [terminate(_:)](<../../appkit/nsapplication/terminate(__).md>) method. This is the method that is invoked in response to a Quit command. Thus the user can copy something to the pasteboard, quit the application, and still paste the data that was copied. A [pasteboard:provideDataForType:](pasteboard_providedatafortype_.md) message is sent only if the specified type of data has not already been supplied to the pasteboard. Instead of writing all data types when the cut or copy operation is done, an application can choose to implement this method to provide the data for certain types only when they are requested.

If an application writes data to the pasteboard in the richest, and therefore most preferred, type at the time of a cut or copy operation, its [pasteboard:provideDataForType:](pasteboard_providedatafortype_.md) method can simply read that data from the pasteboard, convert it to the requested type, and write it back to the pasteboard as the new type.

## See Also

### Related Documentation

- [Pasteboard Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PasteboardGuide106/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008099)
