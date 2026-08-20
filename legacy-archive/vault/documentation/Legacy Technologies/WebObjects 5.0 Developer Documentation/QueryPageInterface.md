---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Protocols/QueryPageInterface.html
archived_at: '2026-07-15T08:12:46.223573Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

# QueryPageInterface

> **__Implemented by:__**
> : [D2WQueryPage](D2WQueryPage.md)
> : [QueryAllPageInterface](QueryAllPageInterface.md)

> **__Package:__**
> : com.webobjects.directtoweb

---

## Interface Description

---

This interface is the return value for the D2W `queryPageForEntityNamed` method that creates a query page. The methods defined by this interface initialize the newly created page.

## Method Types

---

> **Managing the Data Source**
> : [queryDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6ulvmvzhsudbm5sus3tumvzgmyldmuxxc5lfoj4uiylumfjw65lsmnss6rkpirqxiyktn52xey3ff4ucs)

> **Managing the Next Page Parameters**
> : [setNextPageDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6ulvmvzhsudbm5sus3tumvzgmyldmuxxgzlujzsxq5cqmftwkrdfnrswoylumuxxm33jmqxsqttfpb2faylhmvcgk3dfm5qxizjj)

## Methods

---

### queryDataSource

abstract public EODataSource queryDataSource()

Returns the receiver's EODataSource (defined in the EOControl Framework) containing the objects matching the query.

---

### setNextPageDelegate

abstract public void setNextPageDelegate(NextPageDelegate nextPageDelegate)

__See Also:__[NextPageDelegate](NextPageDelegate.md)

---

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
