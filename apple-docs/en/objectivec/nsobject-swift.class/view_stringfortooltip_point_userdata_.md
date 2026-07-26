---
title: 'view:stringForToolTip:point:userData:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/view:stringfortooltip:point:userdata:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/view:stringfortooltip:point:userdata:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/view%3Astringfortooltip%3Apoint%3Auserdata%3A.json'
content_hash: 'sha256:4884f49d9e02288c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# view:stringForToolTip:point:userData:

<sub>Instance Method</sub>

Returns the tool tip string to be displayed due to the cursor pausing at location `point` within the tool tip rectangle identified by `tag` in the view `view`.

<sub>Mac Catalyst, macOS</sub>

```objc
- (NSString *) view:(NSView *) view stringForToolTip:(NSToolTipTag) tag point:(NSPoint) point userData:(void *) data;
```

## Discussion

`userData` is additional information provided by the creator of the tool tip rectangle.

## See Also

### Related Documentation

- [Online Help](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OnlineHelp/OnlineHelp.html#//apple_ref/doc/uid/10000009i)
- [addToolTip(_:owner:userData:)](<../../appkit/nsview/addtooltip(__owner_userdata_).md>) — Creates a tooltip for a defined area in the view and returns a tag that identifies the tooltip rectangle.
