---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Protocols/SelectPageInterface.html
archived_at: '2026-07-15T08:12:46.243520Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

# SelectPageInterface

> **__Implemented by:__**
> : [D2WListPage](D2WListPage.md)

> **__Package:__**
> : com.webobjects.directtoweb

---

## Interface Description

---

This interface is the return value for the D2W `selectPageForEntityNamed` method that creates a select page. The methods defined by this interface initialize the newly created page.

## Method Types

---

> **Managing the Data Source**
> : [setDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6u3fnrswg5cqmftwksloorsxeztbmnss643forcgc5dbknxxk4tdmuxxm33jmqxsqrkpirqxiyktn52xey3ffe)

> **Managing the Next Page Parameters**
> : [nextPageDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6u3fnrswg5cqmftwksloorsxeztbmnss63tfpb2faylhmvcgk3dfm5qxizjpjzsxq5cqmftwkrdfnrswoylumuxsqki)
> : [setNextPageDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6u3fnrswg5cqmftwksloorsxeztbmnss643forhgk6dukbqwozkemvwgkz3borss65tpnfsc6kcomv4hiudbm5suizlmmvtwc5dffe)

> **Managing the Selected Object**
> : [selectedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6u3fnrswg5cqmftwksloorsxeztbmnss643fnrswg5dfmrhwe2tfmn2c6rkpivxhizlsobzgs43fj5rguzldoqxsqki)
> : [setSelectedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6u3fnrswg5cqmftwksloorsxeztbmnss643forjwk3dfmn2gkzcpmjvgky3uf53g62lef4uekt2fnz2gk4tqojuxgzkpmjvgky3ufe)

## Methods

---

### nextPageDelegate

abstract public NextPageDelegate nextPageDelegate()

Returns the receiver's next page delegate.

__See Also:__[nextPageDelegate](D2WPage.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5xgk6dukbqwozkemvwgkz3borss6ttfpb2faylhmvcgk3dfm5qxizjpfauq) ([D2WPage](D2WPage.md))

---

### selectedObject

public abstract EOEnterpriseObject selectedObject()

Returns the object selected by the user.

---

### setDataSource

public abstract void setDataSource(EODataSource dataSource)

Sets the receiver's data source to `dataSource`. This data source contains the group of objects from which the user makes a selection.

---

### setNextPageDelegate

abstract public void setNextPageDelegate(NextPageDelegate nextPageDelegate)

Sets the receiver's next page delegate to `nextPageDelegate`. When the user selects an object on the select page, Direct to Web invokes the `nextPage` method on the next page delegate.

__See Also:__[NextPageDelegate](NextPageDelegate.md)

---

### setSelectedObject

public abstract void setSelectedObject(EOEnterpriseObject selectedObject)

Sets the receiver's selected object to `anObject`. This method can be used to set the default selected object.

---

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
