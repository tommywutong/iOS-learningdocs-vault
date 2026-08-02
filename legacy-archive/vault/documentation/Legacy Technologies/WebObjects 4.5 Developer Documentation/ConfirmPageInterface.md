---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Protocols/ConfirmPageInterface.html
archived_at: '2026-07-15T08:11:31.229131Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

[![Table of Contents](attachments/images/up.gif)](../DirectToWebTOC.md)

# ConfirmPageInterface

> **__Implemented by:__**
> : [D2WConfirmPage](D2WConfirmPage.md)

> **__Package:__**
> : com.apple.yellow.directtoweb

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

[![Table of Contents](attachments/images/up.gif)](../DirectToWebTOC.md)
