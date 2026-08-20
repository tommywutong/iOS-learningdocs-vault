---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOApplication.framework/Java/Classes/EOWindowObserver.html
archived_at: '2026-07-15T08:11:36.770168Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOApplication Reference

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

# EOWindowObserver

> **__Inherits
> from:__**
> : Object

> **__Implements:__**
> : WindowListener
> : (java.awt.event package)
> : NSDisposable

> **__Package:__**
> : com.apple.client.eoapplication

---

## Class Description

---

Documentation for this class is forthcoming.
For information on using this class, see the book _Getting Started
with Direct to Java Client_.

## Method Types

---

> **All methods**
> : [activateBestWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpmfrxi2lwmf2gkqtfon2fo2lomrxxo)
> : [activatePreviousWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpmfrxi2lwmf2gkudsmv3gs33vonlws3ten53q)
> : [activeWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpmfrxi2lwmvlws3ten53q)
> : [blockActiveWindowChangedNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpmjwg6y3lifrxi2lwmvlws3ten53ug2dbnztwkzcon52gsztjmnqxi2lpny)
> : [controllerForActiveWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpmnxw45dsn5wgyzlsizxxeqldoruxmzkxnfxgi33x)
> : [controllerForLatestDeactivatedWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpmnxw45dsn5wgyzlsizxxetdborsxg5cemvqwg5djozqxizlek5uw4zdpo4)
> : [controllerForWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpmnxw45dsn5wgyzlsizxxev3jnzsg65y)
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpmruxg4dponsq)
> : [latestDeactivatedWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpnrqxizltorcgkyldoruxmylumvsfo2lomrxxo)
> : [previousWindowToActivate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpobzgk5tjn52xgv3jnzsg652un5awg5djozqxizi)
> : [registerWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpojswo2ltorsxev3jnzsg65y)
> : [registerWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpojswo2ltorsxev3jnzsg65y)
> : [registeredWindows](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpojswo2ltorsxezlek5uw4zdpo5zq)
> : [unblockActiveWindowChangedNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpovxge3dpmnvucy3unf3gkv3jnzsg652dnbqw4z3fmrhg65djmzuwgylunfxw4)
> : [unregisterWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpovxhezlhnfzxizlsk5uw4zdpo4)
> : [unregisterWindowOfController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpovxhezlhnfzxizlsk5uw4zdpo5hwmq3pnz2he33mnrsxe)
> : [visibleWindows](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpozuxg2lcnrsvo2lomrxxo4y)
> : [windowActivated](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5awg5djozqxizle)
> : [windowClosed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5bwy33tmvsa)
> : [windowClosing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5bwy33tnfxgo)
> : [windowDeactivated](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5cgkyldoruxmylumvsa)
> : [windowDeiconified](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5cgk2ldn5xgsztjmvsa)
> : [windowDidBecomeActive](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5cgszccmvrw63lfifrxi2lwmu)
> : [windowDidBecomeInactive](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5cgszccmvrw63lfjfxgcy3unf3gk)
> : [windowDidBecomeInvisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5cgszccmvrw63lfjfxhm2ltnfrgyzi)
> : [windowDidBecomeVisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5cgszccmvrw63lfkzuxg2lcnrsq)
> : [windowForController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5dg64sdn5xhi4tpnrwgk4q)
> : [windowIconified](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5ewg33onftgszle)
> : [windowOpened](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5hxazlomvsa)

## Instance Methods

---

### activateBestWindow

`public void activateBestWindow()`

---

### activatePreviousWindow

`public void activatePreviousWindow()`

---

### activeWindow

`public java.awt.Window activeWindow()`

---

### blockActiveWindowChangedNotification

`public void blockActiveWindowChangedNotification()`

---

### controllerForActiveWindow

`public EOController controllerForActiveWindow()`

---

### controllerForLatestDeactivatedWindow

`public EOController controllerForLatestDeactivatedWindow()`

---

### controllerForWindow

`public EOController controllerForWindow(java.awt.Window aWindow)`

---

### dispose

`public void dispose()`

---

### latestDeactivatedWindow

`public java.awt.Window latestDeactivatedWindow()`

---

### previousWindowToActivate

`public java.awt.Window previousWindowToActivate()`

---

### registerWindow

`public void registerWindow(
java.awt.Window aWindow,
EOController anEOController)`

---

### registerWindow

`public void registerWindow(java.awt.Window aWindow)`

---

### registeredWindows

`public NSArray registeredWindows()`

---

### unblockActiveWindowChangedNotification

`public void unblockActiveWindowChangedNotification()`

---

### unregisterWindow

`public void unregisterWindow(java.awt.Window aWindow)`

---

### unregisterWindowOfController

`public void unregisterWindowOfController(EOController anEOController)`

---

### visibleWindows

`public NSArray visibleWindows()`

---

### windowActivated

`public void windowActivated(java.awt.event.WindowEvent aWindowEvent)`

---

### windowClosed

`public void windowClosed(java.awt.event.WindowEvent aWindowEvent)`

---

### windowClosing

`public void windowClosing(java.awt.event.WindowEvent aWindowEvent)`

---

### windowDeactivated

`public void windowDeactivated(java.awt.event.WindowEvent aWindowEvent)`

---

### windowDeiconified

`public void windowDeiconified(java.awt.event.WindowEvent aWindowEvent)`

---

### windowDidBecomeActive

`protected void windowDidBecomeActive(java.awt.Window aWindow)`

---

### windowDidBecomeInactive

`protected void windowDidBecomeInactive(java.awt.Window aWindow)`

---

### windowDidBecomeInvisible

`protected void windowDidBecomeInvisible(java.awt.Window aWindow)`

---

### windowDidBecomeVisible

`protected void windowDidBecomeVisible(java.awt.Window aWindow)`

---

### windowForController

`public java.awt.Window windowForController(EOController anEOController)`

---

### windowIconified

`public void windowIconified(java.awt.event.WindowEvent aWindowEvent)`

---

### windowOpened

`public void windowOpened(java.awt.event.WindowEvent aWindowEvent)`

---

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

__DRAFT__
