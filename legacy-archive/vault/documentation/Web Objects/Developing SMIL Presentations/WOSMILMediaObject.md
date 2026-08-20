---
title: Developing SMIL Presentations
apple_id: TP40000999
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-03-29'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/Reference/WOSMILMediaObject.html
archived_at: '2026-07-18T02:20:18.405402Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Developing SMIL Presentations](toc.md)


[!](WOSMILSwitch.md) [!](WOSMILSeq.md)

## WOSMILMediaObject

This element allows you to include media objects in a presentation.
It corresponds to the following tags: `<ref>`, `<animation>`, `<audio>`, `<img>`, `<video>`, `<text>`,
and `<textstream>`. [Table 4-10](#apple-ijbegrsgjbdeo) and [Table 4-11](#apple-ijbegqsdivfei) describe
this element's bindings.

__Table
4-10 Basic bindings of the WOSMILMediaObject
element__

| Binding | Description |
| `alt` | Alternate text to display when the player cannot display the object this element references. |
| `data` | Allows you to embed a media object inside your SMIL component. It's useful for embedding small objects, especially text. |
| `filename` | Filename of the media object to render. Use with `framework`. `filename` and `href` are mutually exclusive. |
| `fill` | Determines the effective end of the media object. Value: `"remove"` or `"freeze"`. See [http://www.w3.org/TR/REC-smil/](http://www.w3.org/TR/REC-smil/) for more information on SMIL's time model. |
| `framework` | Logical location of the media object indicated by `filename`. Value: `"app"`, `"JavaJDBCAdaptor"`, `"JavaWOExtensions"`, or `"JavaWebObjects"`. |
| `href` | URL of the media object to render. `href` and `filename` are mutually exclusive. |
| `mediaAbstract` | Brief description of the media element. |
| `mediaObjectName` | Value: `"ref"`, `"animation"`, `"audio"`, `"img"`, `"video"`, `"text"`, or `"textstream"`. |
| `mimeType` | MIME type of the media object. |
| `regionID` | Name of the region in which the media object this element refers to is rendered. |

__Table
4-11 Additional bindings of the WOSMILMediaObject
element__

| Binding | Description |
| `author` | Name of the author of the object referenced by this element. |
| `begin` | When the object is to be displayed. |
| `clipBegin` | The beginning of a clip of the object referenced by this element. |
| `clipEnd` | The end of a clip of the object referenced by this element. |
| `copyright` | Copyright notice for the object referenced by this element. |
| `dur` | Duration of the element. |
| `end` | End of the element. |
| `elementID` | Name of the element. |
| `longdesc` | A link to a detailed description of the object that this element references. |
| `title` | Meaningful description for this element. |
| _system attribute_ | See ["System-Attribute Bindings"](System_Attribute_Bindings.md#apple-ijbegr2djjeui). |

[!](WOSMILSwitch.md) [!](WOSMILSeq.md)

---

© 2002 Apple Computer, Inc. (Last Updated March 29, 2002)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
