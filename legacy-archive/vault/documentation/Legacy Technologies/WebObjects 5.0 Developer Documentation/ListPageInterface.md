---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Protocols/ListPageInterface.html
archived_at: '2026-07-15T08:12:46.147873Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

# ListPageInterface

> **__Implemented by:__**
> : [D2WListPage](D2WListPage.md)
> : [D2WMasterDetailPage](D2WMasterDetailPage.md)

> **__Package:__**
> : com.webobjects.directtoweb

---

## Interface Description

---

This interface is the return value for the D2W `listPageForEntityNamed` method that creates a list page. The methods defined by this interface initialize the newly created page.

## Method Types

---

> **Managing the Data Source**
> : [setDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tdjon2faylhmvew45dfojtgcy3ff5zwk5cemf2gcu3povzggzjpozxwszbpfbcu6rdborqvg33vojrwkki)

> **Managing the Next Page Parameters**
> : [setNextPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tdjon2faylhmvew45dfojtgcy3ff5zwk5comv4hiudbm5ss65tpnfsc6kcxj5bw63lqn5xgk3tufe)
> : [setNextPageDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tdjon2faylhmvew45dfojtgcy3ff5zwk5comv4hiudbm5suizlmmvtwc5dff53g62lef4ue4zlyorigcz3firswyzlhmf2gkki)

## Methods

---

### setDataSource

abstract public void setDataSource(EODataSource dataSource)

Sets the receiver's data source to `dataSource`. This data source contains the group of objects listed on the page.

---

### setNextPage

public abstract void setNextPage(WOComponent nextPage)

Sets the page that is displayed when the user clicks Return in the list page. If the new page needs to be initialized, set the next page delegate instead.

---

### setNextPageDelegate

public abstract void setNextPageDelegate(NextPageDelegate nextPageDelegate)

Sets the receiver's next page delegate to `nextPageDelegate`. When the user clicks Return in the list page, Direct to Web invokes the `nextPage` method on the next page delegate.

__See Also:__[NextPageDelegate](NextPageDelegate.md)

---

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
