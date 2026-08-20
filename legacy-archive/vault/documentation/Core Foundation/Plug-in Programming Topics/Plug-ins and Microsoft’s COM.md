---
title: Plug-in Programming Topics
apple_id: 10000128i
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2005-03-03'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPlugIns/Concepts/com.html
archived_at: '2026-07-15T07:22:37.862156Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Plug-in Programming Topics](Introduction%20to%20Plug-ins.md)


[Next](Anatomy%20of%20a%20Plug-in.md)[Previous](Plug-in%20Architecture.md)

# Plug-ins and Microsoft’s COM

The plug-in model is compatible with the basics of Microsoft’s COM (Component Object Model) architecture. This means that the plug-in interface is laid out according to the COM guidelines and that all interfaces must inherit from COM’s IUnknown interface. These are the only elements plug-ins share with COM. Other COM concepts such as the IClassFactory interface, aggregation, out-of-process servers, and Windows registry are not mapped. This document only minimally covers COM concepts as necessary to explain the way they are used in Core Foundation plug-ins. For additional information, you are encouraged to seek out the wealth of documentation already published about COM. A good place to start is the COM area of Microsoft’s web site, `http://www.microsoft.com/com/tech/com.asp`.

[Next](Anatomy%20of%20a%20Plug-in.md)[Previous](Plug-in%20Architecture.md)

