---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Protocols/ErrorPageInterface.html
archived_at: '2026-07-15T08:12:46.109189Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

# ErrorPageInterface

> **__Implemented by:__**
> : [D2WErrorPage](D2WErrorPage.md)

> **__Package:__**
> : com.webobjects.directtoweb

---

## Interface Description

---

This interface is the return value for the D2W `errorPage` methods that create error pages. The methods defined by this interface initialize the newly created page.

## Method Types

---

> **Managing the Next Page Parameters**
> : [setNextPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rlsojxxeudbm5sus3tumvzgmyldmuxxgzlujzsxq5cqmftwkl3wn5uwilzik5hug33nobxw4zlooquq)

> **Setting the Message**
> : [setMessage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rlsojxxeudbm5sus3tumvzgmyldmuxxgzlujvsxg43bm5ss65tpnfsc6kctorzgs3thfe)

## Methods

---

### setMessage

public abstract void setMessage(String message)

Sets the message displayed by the receiver.

---

### setNextPage

abstract public void setNextPage(WOComponent nextPage)

Sets the page that displayed when the user clicks Return in the error page.

---

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
