---
title: Property List Programming Topics for Core Foundation
apple_id: 10000130i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/Articles/XMLTags.html
archived_at: '2026-07-15T07:22:47.536075Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Property List Programming Topics for Core Foundation](Introduction%20to%20Property%20List%20Programming%20Topics%20for%20Core%20Foundation.md)


[Next](Document%20Revision%20History.md)[Previous](Using%20Numbers%20in%20Property%20Lists.md)

# Property List XML Tags

When property lists convert a collection of Core Foundation objects into an XML property list, it wraps the property list using the document type tag `<plist>`. The other tags used for the Core Foundation data types are listed in [Table 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3teljrgazdomjzfvbeeq2hjffessa).

The XML data format is documented here strictly for help in understanding property lists and as a debugging aid. These tags may change in future releases so you shouldn’t rely on them directly.

When encoding the contents of a CFDictionary object, each member is encoded by placing the dictionary key in a `<key>` tag and immediately following it with the corresponding value in the appropriate tag from Table 1. See [Saving and Restoring Property Lists](Saving%20and%20Restoring%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3tklkdjjbekscbifdq) for an example XML data generated from a property list.

__Table 1__  Core Foundation Types with XML Equivalents

| CF type | XML tag |
| CFString | `<string>` |
| CFNumber | `<real> or <integer>` |
| CFDate | `<date>` |
| CFBoolean | `<true/> or <false/>` |
| CFData | `<data>` |
| CFArray | `<array>` |
| CFDictionary | `<dict>` |

[Next](Document%20Revision%20History.md)[Previous](Using%20Numbers%20in%20Property%20Lists.md)

