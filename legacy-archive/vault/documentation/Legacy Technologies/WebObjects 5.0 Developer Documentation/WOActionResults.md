---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsRef/Java/Protocols/WOActionResults.html
archived_at: '2026-07-15T08:15:15.989081Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# WOActionResults

> __Implemented by:__ : WOComponent: WOResponse:

> **__Package:__**
> : com.webobjects.appserver

---

## Interface Description

---

The WOActionResults interface is the return type for direct actions. As a convenience, direct actions can return either WOComponent objects or WOResponse objects; both of which implement the WOActionResults protocol. This interface implements only one method: [generateResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6v2pifrxi2lpnzjgk43vnr2hgl3hmvxgk4tborsvezltobxw443f).

If you want to return any other class from a direct action, then that class must implement this protocol.

## Instance Methods

---

### generateResponse

`public abstract WOResponse generateResponse()`

Returns a response object. WOResponse's implementation of this method returns the receiver. WOComponent's implementation of this method calls appendToResponse on itself and all children components in its template and returns the result as a WOResponse object. If you want to return any other class from a direct action, then that class must implement this method.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
