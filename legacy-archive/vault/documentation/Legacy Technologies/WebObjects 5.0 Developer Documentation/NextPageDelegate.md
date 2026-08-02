---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Protocols/NextPageDelegate.html
archived_at: '2026-07-15T08:12:46.169686Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

# NextPageDelegate

> **__Package:__**
> : com.webobjects.directtoweb

---

## Interface Description

---

This interface defines the `nextPage` method that a Direct to Web template can invoke in its next page delegate. See the "Customizing a Direct to Web Application" chapter of _Developing WebObjects Applications With Direct to Web_ for more information about using the next page delegate.

## Method Types

---

> ****
> : [nextPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6ttfpb2faylhmvcgk3dfm5qxizjpnzsxq5cqmftwkl2xj5bw63lqn5xgk3tuf4ufot2dn5wxa33omvxhiki)

## Methods

---

### nextPage

abstract public WOComponent nextPage(WOComponent sender)

This action method is invoked when the user leaves a Direct to Web page. It returns the next page (a WOComponent object) to display. The `sender` argument contains the Direct to Web template instance that invokes the method. If this method is not implemented, the `sender` is redisplayed.

---

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
