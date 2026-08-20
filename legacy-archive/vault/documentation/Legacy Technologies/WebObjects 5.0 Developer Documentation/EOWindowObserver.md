---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOApplicationRef/Java/Classes/EOWindowObserver.html
archived_at: '2026-07-15T08:13:43.074271Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md)

# EOWindowObserver

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : WindowListener: (java.awt.event package): NSDisposable

> **__Package:__**
> : com.webobjects.eoapplication

---

## Class Description

---

Documentation for this class is forthcoming. For information on using this class, see the book _Getting Started with Direct to Java Client_.

## Method Types

---

> **All methods**
> : [activateBestWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpmfrxi2lwmf2gkqtfon2fo2lomrxxo): [activatePreviousWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpmfrxi2lwmf2gkudsmv3gs33vonlws3ten53q): [activeWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpmfrxi2lwmvlws3ten53q): [blockActiveWindowChangedNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpmjwg6y3lifrxi2lwmvlws3ten53ug2dbnztwkzcon52gsztjmnqxi2lpny): [controllerForActiveWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpmnxw45dsn5wgyzlsizxxeqldoruxmzkxnfxgi33x): [controllerForLatestDeactivatedWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpmnxw45dsn5wgyzlsizxxetdborsxg5cemvqwg5djozqxizlek5uw4zdpo4): [controllerForWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpmnxw45dsn5wgyzlsizxxev3jnzsg65y): [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpmruxg4dponsq): [latestDeactivatedWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpnrqxizltorcgkyldoruxmylumvsfo2lomrxxo): [previousWindowToActivate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpobzgk5tjn52xgv3jnzsg652un5awg5djozqxizi): [registerWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpojswo2ltorsxev3jnzsg65y): [registerWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpojswo2ltorsxev3jnzsg65y): [registeredWindows](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpojswo2ltorsxezlek5uw4zdpo5zq): [unblockActiveWindowChangedNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpovxge3dpmnvucy3unf3gkv3jnzsg652dnbqw4z3fmrhg65djmzuwgylunfxw4): [unregisterWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpovxhezlhnfzxizlsk5uw4zdpo4): [unregisterWindowOfController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpovxhezlhnfzxizlsk5uw4zdpo5hwmq3pnz2he33mnrsxe): [visibleWindows](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpozuxg2lcnrsvo2lomrxxo4y): [windowActivated](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5awg5djozqxizle): [windowClosed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5bwy33tmvsa): [windowClosing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5bwy33tnfxgo): [windowDeactivated](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5cgkyldoruxmylumvsa): [windowDeiconified](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5cgk2ldn5xgsztjmvsa): [windowDidBecomeActive](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5cgszccmvrw63lfifrxi2lwmu): [windowDidBecomeInactive](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5cgszccmvrw63lfjfxgcy3unf3gk): [windowDidBecomeInvisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5cgszccmvrw63lfjfxhm2ltnfrgyzi): [windowDidBecomeVisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5cgszccmvrw63lfkzuxg2lcnrsq): [windowForController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5dg64sdn5xhi4tpnrwgk4q): [windowIconified](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5ewg33onftgszle): [windowOpened](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5hwe43foj3gk4rpo5uw4zdpo5hxazlomvsa)

## Constructors

---

### EOWindowObserver

`protected EOWindowObserver()`

Description forthcoming.

---

## Instance Methods

---

### activateBestWindow

`public void activateBestWindow()`

Description forthcoming.

---

### activatePreviousWindow

`public void activatePreviousWindow()`

Description forthcoming.

---

### activeWindow

`public java.awt.Window activeWindow()`

Description forthcoming.

---

### blockActiveWindowChangedNotification

`public void blockActiveWindowChangedNotification()`

Description forthcoming.

---

### controllerForActiveWindow

`public EOController controllerForActiveWindow()`

Description forthcoming.

---

### controllerForLatestDeactivatedWindow

`public EOController controllerForLatestDeactivatedWindow()`

Description forthcoming.

---

### controllerForWindow

`public EOController controllerForWindow(java.awt.Window aWindow)`

Description forthcoming.

---

### dispose

`public void dispose()`

Description forthcoming.

---

### latestDeactivatedWindow

`public java.awt.Window latestDeactivatedWindow()`

Description forthcoming.

---

### previousWindowToActivate

`public java.awt.Window previousWindowToActivate()`

Description forthcoming.

---

### registerWindow

`public void registerWindow( java.awt.Window aWindow, EOController anEOController)`

Description forthcoming.

---

### registerWindow

`public void registerWindow(java.awt.Window aWindow)`

Description forthcoming.

---

### registeredWindows

`public NSArray registeredWindows()`

Description forthcoming.

---

### unblockActiveWindowChangedNotification

`public void unblockActiveWindowChangedNotification()`

Description forthcoming.

---

### unregisterWindow

`public void unregisterWindow(java.awt.Window aWindow)`

Description forthcoming.

---

### unregisterWindowOfController

`public void unregisterWindowOfController(EOController anEOController)`

Description forthcoming.

---

### visibleWindows

`public NSArray visibleWindows()`

Description forthcoming.

---

### windowActivated

`public void windowActivated(java.awt.event.WindowEvent aWindowEvent)`

Description forthcoming.

---

### windowClosed

`public void windowClosed(java.awt.event.WindowEvent aWindowEvent)`

Description forthcoming.

---

### windowClosing

`public void windowClosing(java.awt.event.WindowEvent aWindowEvent)`

Description forthcoming.

---

### windowDeactivated

`public void windowDeactivated(java.awt.event.WindowEvent aWindowEvent)`

Description forthcoming.

---

### windowDeiconified

`public void windowDeiconified(java.awt.event.WindowEvent aWindowEvent)`

Description forthcoming.

---

### windowDidBecomeActive

`protected void windowDidBecomeActive(java.awt.Window aWindow)`

Description forthcoming.

---

### windowDidBecomeInactive

`protected void windowDidBecomeInactive(java.awt.Window aWindow)`

Description forthcoming.

---

### windowDidBecomeInvisible

`protected void windowDidBecomeInvisible(java.awt.Window aWindow)`

Description forthcoming.

---

### windowDidBecomeVisible

`protected void windowDidBecomeVisible(java.awt.Window aWindow)`

Description forthcoming.

---

### windowForController

`public java.awt.Window windowForController(EOController anEOController)`

Description forthcoming.

---

### windowIconified

`public void windowIconified(java.awt.event.WindowEvent aWindowEvent)`

Description forthcoming.

---

### windowOpened

`public void windowOpened(java.awt.event.WindowEvent aWindowEvent)`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 14, 2001)

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
