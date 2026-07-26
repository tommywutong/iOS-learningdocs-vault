---
title: layoutManager
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.1+, macOS 10.5+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caconstraintlayoutmanager/layoutmanager
source_url: 'https://developer.apple.com/documentation/quartzcore/caconstraintlayoutmanager/layoutmanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caconstraintlayoutmanager/layoutmanager.json'
content_hash: 'sha256:41f752fca7fbc4e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAConstraintLayoutManager](../caconstraintlayoutmanager.md)

# layoutManager

<sub>Type Method</sub>

Returns the shared layout manager object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) layoutManager;
```

## Return Value

The shared layout manager object.

## Discussion

You can assign the returned object to any layers that manage layout using constraints.

## See Also

### Related Documentation

- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
