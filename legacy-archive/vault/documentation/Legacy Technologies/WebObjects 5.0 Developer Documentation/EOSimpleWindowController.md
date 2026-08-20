---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOApplicationRef/Java/Classes/EOSimpleWindowController.html
archived_at: '2026-07-15T08:13:42.957245Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md)

# EOSimpleWindowController

> **__Inherits from:__**
> : [EOWindowController](EOWindowController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvo2lomrxxoq3pnz2he33mnrsxe): [EOComponentController](EOComponentController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33nobxw4zloorbw63tuojxwy3dfoi): [EOController](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33oorzg63dmmvza): Object

> **__Implements:__**
> : WindowListener: (java.awt.event package): ComponentListener (java.awt.event package): EOComponentController.ResetUserInterface

> **__Package:__**
> : com.webobjects.eoapplication

---

## Class Description

---

Documentation for this class is forthcoming. For information on using this class, see the book _Getting Started with Direct to Java Client_.

|  |  |
| --- | --- |
| __XML Tag__ | __Default Rule System Controller Type__ |
| None (abstract class) | `windowController` |

## Method Types

---

> **All methods**
> : [EOSimpleWindowController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvza): [activateWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6yldoruxmylumvlws3ten53q): [addComponentOfSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6ylemrbw63lqn5xgk3tuj5tfg5lcmnxw45dsn5wgyzls): [closeWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6y3mn5zwkv3jnzsg65y): [componentDidBecomeInvisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6y3pnvyg63tfnz2ei2leijswg33nmvew45tjonuwe3df): [componentDidBecomeVisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6y3pnvyg63tfnz2ei2leijswg33nmvlgs43jmjwgk): [componentHidden](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6y3pnvyg63tfnz2eq2lemrsw4): [componentMoved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6y3pnvyg63tfnz2e233wmvsa): [componentResized](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6y3pnvyg63tfnz2fezltnf5gkza): [componentShown](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6y3pnvyg63tfnz2fg2dpo5xa): [deactivateWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6zdfmfrxi2lwmf2gkv3jnzsg65y): [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6zdjonyg643f): [disposeIfDeactivated](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6zdjonyg643fjfteizlbmn2gs5tborswi): [integrationComponentDidBecomeInvisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc62loorswo4tboruw63sdn5wxa33omvxhirdjmrbgky3pnvsus3twnfzwsytmmu): [integrationComponentDidBecomeVisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc62loorswo4tboruw63sdn5wxa33omvxhirdjmrbgky3pnvsvm2ltnfrgyzi): [makeVisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc63lbnnsvm2ltnfrgyzi): [newWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc63tfo5lws3ten53q): [newWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc63tfo5lws3ten53q): [resetUserInterface](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc64tfonsxivltmvzes3tumvzgmyldmu): [setDisposeIfDeactivated](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc643forcgs43qn5zwkslgirswcy3unf3gc5dfmq): [setLabel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc643forggcytfnq): [setWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc643forlws3ten53q): [setWindowResizable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc643forlws3ten53vezltnf5gcytmmu): [setWindowTitle](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc643forlws3ten53vi2lunrsq): [startListeningToWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc643umfzhitdjon2gk3tjnztvi32xnfxgi33x): [stopListeningToWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc643un5yey2ltorsw42lom5kg6v3jnzsg65y): [subcontrollerEditedDidChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc643vmjrw63tuojxwy3dfojcwi2lumvsei2leinugc3thmu): [subcontrollerMinimumSizeDidChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc643vmjrw63tuojxwy3dfojgws3tjnv2w2u3jpjsui2leinugc3thmu): [verifyContentMinimumSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc65tfojuwm6kdn5xhizloorgws3tjnv2w2u3jpjsq): [window](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc653jnzsg65y): [windowActivated](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc653jnzsg652bmn2gs5tborswi): [windowClosed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc653jnzsg652dnrxxgzle): [windowClosing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc653jnzsg652dnrxxg2lom4): [windowDeactivated](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc653jnzsg652emvqwg5djozqxizle): [windowDeiconified](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc653jnzsg652emvuwg33onftgszle): [windowIconified](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc653jnzsg652jmnxw42lgnfswi): [windowOpened](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc653jnzsg652pobsw4zle)

## Constructors

---

### EOSimpleWindowController

`public EOSimpleWindowController(EOXMLUnarchiver anEOXMLUnarchiver)`

Description forthcoming.

`public EOSimpleWindowController()`

Description forthcoming.

---

## Instance Methods

---

### activateWindow

`public void activateWindow()`

Description forthcoming.

---

### addComponentOfSubcontroller

`protected void addComponentOfSubcontroller(EOComponentController anEOComponentController)`

Description forthcoming.

---

### closeWindow

`public boolean closeWindow()`

Description forthcoming.

---

### componentDidBecomeInvisible

`protected void componentDidBecomeInvisible()`

Description forthcoming.

---

### componentDidBecomeVisible

`protected void componentDidBecomeVisible()`

Description forthcoming.

---

### componentHidden

`public void componentHidden(java.awt.event.ComponentEvent aComponentEvent)`

Description forthcoming.

---

### componentMoved

`public void componentMoved(java.awt.event.ComponentEvent aComponentEvent)`

Description forthcoming.

---

### componentResized

`public void componentResized(java.awt.event.ComponentEvent aComponentEvent)`

Description forthcoming.

---

### componentShown

`public void componentShown(java.awt.event.ComponentEvent aComponentEvent)`

Description forthcoming.

---

### deactivateWindow

`public void deactivateWindow()`

Description forthcoming.

---

### dispose

`public void dispose()`

Description forthcoming.

---

### disposeIfDeactivated

`public boolean disposeIfDeactivated()`

Description forthcoming.

---

### integrationComponentDidBecomeInvisible

`protected void integrationComponentDidBecomeInvisible()`

Description forthcoming.

---

### integrationComponentDidBecomeVisible

`protected void integrationComponentDidBecomeVisible()`

Description forthcoming.

---

### makeVisible

`public boolean makeVisible()`

Description forthcoming.

---

### newWindow

`protected abstract java.awt.Window newWindow(javax.swing.JComponent aJComponent)`

Description forthcoming.

---

### newWindow

`protected java.awt.Window newWindow()`

Description forthcoming.

---

### resetUserInterface

`public void resetUserInterface()`

Description forthcoming.

---

### setDisposeIfDeactivated

`public void setDisposeIfDeactivated(boolean aBoolean)`

Description forthcoming.

---

### setLabel

`public void setLabel(String aString)`

Description forthcoming.

---

### setWindow

`public void setWindow(java.awt.Window aWindow)`

Description forthcoming.

---

### setWindowResizable

`protected abstract void setWindowResizable( java.awt.Window aWindow, boolean aBoolean)`

Description forthcoming.

---

### setWindowTitle

`protected abstract void setWindowTitle( java.awt.Window aWindow, String aString)`

Description forthcoming.

---

### startListeningToWindow

`protected void startListeningToWindow()`

Description forthcoming.

---

### stopListeningToWindow

`protected void stopListeningToWindow()`

Description forthcoming.

---

### subcontrollerEditedDidChange

`public void subcontrollerEditedDidChange(EOController anEOController)`

Description forthcoming.

---

### subcontrollerMinimumSizeDidChange

`public void subcontrollerMinimumSizeDidChange( EOComponentController anEOComponentController, javax.swing.JComponent aJComponent, java.awt.Dimension aDimension)`

Description forthcoming.

---

### verifyContentMinimumSize

`protected java.awt.Dimension verifyContentMinimumSize( java.awt.Window aWindow, java.awt.Dimension aDimension)`

Description forthcoming.

---

### window

`public java.awt.Window window()`

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
