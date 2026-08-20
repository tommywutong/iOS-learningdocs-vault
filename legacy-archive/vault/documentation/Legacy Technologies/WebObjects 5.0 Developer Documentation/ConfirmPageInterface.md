---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Protocols/ConfirmPageInterface.html
archived_at: '2026-07-15T08:12:45.997256Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

# ConfirmPageInterface

> **__Implemented by:__**
> : [D2WConfirmPage](D2WConfirmPage.md)

> **__Package:__**
> : com.webobjects.directtoweb

---

## Interface Description

---

This interface is the return value for the D2W method `confirmPageForEntityNamed` that creates a confirm page. The methods defined by this interface initialize the newly created page.

## Method Types

---

> **Managing the Next Page Parameters**
> : [setCancelDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6q3pnztgs4tnkbqwozkjnz2gk4tgmfrwkl3tmv2egylomnswyrdfnrswoylumuxxm33jmqxsqttfpb2faylhmvcgk3dfm5qxizjj)
> : [setConfirmDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6q3pnztgs4tnkbqwozkjnz2gk4tgmfrwkl3tmv2eg33omzuxe3kemvwgkz3borss65tpnfsc6kcomv4hiudbm5suizlmmvtwc5dffe)

> **Setting the Message**
> : [setMessage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6q3pnztgs4tnkbqwozkjnz2gk4tgmfrwkl3tmv2e2zltonqwozjpozxwszbpfbjxi4tjnztss)

## Methods

---

### setCancelDelegate

public abstract void setCancelDelegate(NextPageDelegate cancelDelegate)

Sets the receiver's cancel delegate to `cancelDelegate`. When the user clicks No in the confirm page, Direct to Web invokes the `nextPage` method on the cancel delegate.

---

### setConfirmDelegate

abstract public void setConfirmDelegate(NextPageDelegate confirmDelegate)

Sets the receiver's confirm delegate to `confirmDelegate`. When the user clicks Yes in the confirm page, Direct to Web invokes the `nextPage` method on the confirm delegate.

---

### setMessage

public abstract void setMessage(String messageString)

Sets the message displayed by the confirm page.

---

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
