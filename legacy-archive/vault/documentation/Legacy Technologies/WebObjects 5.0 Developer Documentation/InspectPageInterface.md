---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Protocols/InspectPageInterface.html
archived_at: '2026-07-15T08:12:46.128755Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

# InspectPageInterface

> **__Implemented by:__**
> : [EditPageInterface](EditPageInterface.md)
> : [D2WInspectPage](D2WInspectPage.md)

> **__Package:__**
> : com.webobjects.directtoweb

---

## Interface Description

---

This interface is the return value for the D2W `inspectPageForEntityNamed` method that creates an inspect page. The methods defined by this interface initialize the newly created page.

## Method Types

---

> **Managing the Next Page Parameters**
> : [setNextPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6sloonygky3ukbqwozkjnz2gk4tgmfrwkl3tmv2e4zlyorigcz3ff53g62lef4ufot2dn5wxa33omvxhiki)
> : [setNextPageDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6sloonygky3ukbqwozkjnz2gk4tgmfrwkl3tmv2e4zlyorigcz3firswyzlhmf2gkl3wn5uwilzijzsxq5cqmftwkrdfnrswoylumuuq)

> **Setting the Object**
> : [setObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6sloonygky3ukbqwozkjnz2gk4tgmfrwkl3tmv2e6ytkmvrxil3wn5uwilziivhuk3tumvzha4tjonsu6ytkmvrxiki)

## Methods

---

### setNextPage

abstract public void setNextPage(WOComponent nextPage)

Sets the page that is displayed when the user clicks Return in the inspect page. If the new page needs to be initialized, set the next page delegate instead.

__See Also:__[setNextPageDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6sloonygky3ukbqwozkjnz2gk4tgmfrwkl3tmv2e4zlyorigcz3firswyzlhmf2gkl3wn5uwilzijzsxq5cqmftwkrdfnrswoylumuuq)

---

### setNextPageDelegate

public abstract void setNextPageDelegate(NextPageDelegate nextPageDelegate)

Sets the receiver's next page delegate to `nextPageDelegate`. When the user clicks Return in the inspect page, Direct to Web invokes the `nextPage` method on the next page delegate.

__See Also:__[NextPageDelegate](NextPageDelegate.md)

---

### setObject

abstract public void setObject(EOEnterpriseObject anObject)

Sets the object displayed by the inspect page.

---

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
