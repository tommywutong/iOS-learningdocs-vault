---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOApplicationRef/Java/Interfaces/EOAction.Enabling.html
archived_at: '2026-07-15T08:13:43.155743Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# EOAction.Enabling

> __Implemented by:__ : EOController

> **__Package:__**
> : com.webobjects.eoapplication

---

## Interface Description

---

The EOAction.Enabling interface defines a method, [canPerformActionNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpifrxi2lpnyxek3tbmjwgs3thf5rwc3sqmvzgm33snvawg5djn5xe4ylnmvsa), which allows you to tell if an action (an EOAction object) is enabled for the receiver.

## Instance Methods

---

### canPerformActionNamed

`public abstract boolean canPerformActionNamed(String actionName)`

Returns `true` if the receiver can perform an action (an EOAction object) named _actionName_, `false` otherwise. An EOController's implementation of this method generally returns `false` if the receiver doesn't have an action named _actionName_ or if the _actionName_ action is disabled.

__See Also:__ [isActionNamedEnabled](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5uxgqldoruw63somfwwkzcfnzqwe3dfmq) ( [EOController](EOController.md#apple-inceqrshirauc))

---

© 2001 Apple Computer, Inc. (Last Published April 14, 2001)

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
