---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOApplication.framework/Java/Classes/EOSimpleWindowController.html
archived_at: '2026-07-15T08:11:36.631302Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOApplication Reference

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

# EOSimpleWindowController

> **__Inherits
> from:__**
> : [EOWindowController](EOWindowController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvo2lomrxxoq3pnz2he33mnrsxe) : [EOComponentController](EOComponentController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33nobxw4zloorbw63tuojxwy3dfoi) : [EOController](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33oorzg63dmmvza) :
> Object

> **__Implements:__**
> : WindowListener
> : (java.awt.event package)
> : ComponentListener (java.awt.event package)
> : EOComponentController.ResetUserInterface

> **__Package:__**
> : com.apple.client.eoapplication

---

## Class Description

---

Documentation for this class is forthcoming.
For information on using this class, see the book _Getting Started
with Direct to Java Client_.

|  |  |
| --- | --- |
| __XML Tag__ | __Default Rule System Controller Type__ |
| None (abstract class) | `windowController` |

## Method Types

---

> **All methods**
> : [EOSimpleWindowController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvza)
> : [activateWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6yldoruxmylumvlws3ten53q)
> : [addComponentOfSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6ylemrbw63lqn5xgk3tuj5tfg5lcmnxw45dsn5wgyzls)
> : [closeWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6y3mn5zwkv3jnzsg65y)
> : [componentDidBecomeInvisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6y3pnvyg63tfnz2ei2leijswg33nmvew45tjonuwe3df)
> : [componentDidBecomeVisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6y3pnvyg63tfnz2ei2leijswg33nmvlgs43jmjwgk)
> : [componentHidden](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6y3pnvyg63tfnz2eq2lemrsw4)
> : [componentMoved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6y3pnvyg63tfnz2e233wmvsa)
> : [componentResized](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6y3pnvyg63tfnz2fezltnf5gkza)
> : [componentShown](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6y3pnvyg63tfnz2fg2dpo5xa)
> : [deactivateWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6zdfmfrxi2lwmf2gkv3jnzsg65y)
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6zdjonyg643f)
> : [disposeIfDeactivated](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc6zdjonyg643fjfteizlbmn2gs5tborswi)
> : [integrationComponentDidBecomeInvisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc62loorswo4tboruw63sdn5wxa33omvxhirdjmrbgky3pnvsus3twnfzwsytmmu)
> : [integrationComponentDidBecomeVisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc62loorswo4tboruw63sdn5wxa33omvxhirdjmrbgky3pnvsvm2ltnfrgyzi)
> : [makeVisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc63lbnnsvm2ltnfrgyzi)
> : [newWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc63tfo5lws3ten53q)
> : [newWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc63tfo5lws3ten53q)
> : [resetUserInterface](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc64tfonsxivltmvzes3tumvzgmyldmu)
> : [setDisposeIfDeactivated](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc643forcgs43qn5zwkslgirswcy3unf3gc5dfmq)
> : [setLabel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc643forggcytfnq)
> : [setWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc643forlws3ten53q)
> : [setWindowResizable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc643forlws3ten53vezltnf5gcytmmu)
> : [setWindowTitle](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc643forlws3ten53vi2lunrsq)
> : [startListeningToWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc643umfzhitdjon2gk3tjnztvi32xnfxgi33x)
> : [stopListeningToWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc643un5yey2ltorsw42lom5kg6v3jnzsg65y)
> : [subcontrollerEditedDidChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc643vmjrw63tuojxwy3dfojcwi2lumvsei2leinugc3thmu)
> : [subcontrollerMinimumSizeDidChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc643vmjrw63tuojxwy3dfojgws3tjnv2w2u3jpjsui2leinugc3thmu)
> : [verifyContentMinimumSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc65tfojuwm6kdn5xhizloorgws3tjnv2w2u3jpjsq)
> : [window](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc653jnzsg65y)
> : [windowActivated](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc653jnzsg652bmn2gs5tborswi)
> : [windowClosed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc653jnzsg652dnrxxgzle)
> : [windowClosing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc653jnzsg652dnrxxg2lom4)
> : [windowDeactivated](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc653jnzsg652emvqwg5djozqxizle)
> : [windowDeiconified](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc653jnzsg652emvuwg33onftgszle)
> : [windowIconified](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc653jnzsg652jmnxw42lgnfswi)
> : [windowOpened](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpknuw24dmmvlws3ten53ug33oorzg63dmmvzc653jnzsg652pobsw4zle)

## Constructors

---

### EOSimpleWindowController

`public EOSimpleWindowController(EOXMLUnarchiver anEOXMLUnarchiver)`

---

## Instance Methods

---

### activateWindow

`public void activateWindow()`

---

### addComponentOfSubcontroller

`protected void addComponentOfSubcontroller(EOComponentController anEOComponentController)`

---

### closeWindow

`public boolean closeWindow()`

---

### componentDidBecomeInvisible

`protected void componentDidBecomeInvisible()`

---

### componentDidBecomeVisible

`protected void componentDidBecomeVisible()`

---

### componentHidden

`public void componentHidden(java.awt.event.ComponentEvent aComponentEvent)`

---

### componentMoved

`public void componentMoved(java.awt.event.ComponentEvent aComponentEvent)`

---

### componentResized

`public void componentResized(java.awt.event.ComponentEvent aComponentEvent)`

---

### componentShown

`public void componentShown(java.awt.event.ComponentEvent aComponentEvent)`

---

### deactivateWindow

`public void deactivateWindow()`

---

### dispose

`public void dispose()`

---

### disposeIfDeactivated

`public boolean disposeIfDeactivated()`

---

### integrationComponentDidBecomeInvisible

`protected void integrationComponentDidBecomeInvisible()`

---

### integrationComponentDidBecomeVisible

`protected void integrationComponentDidBecomeVisible()`

---

### makeVisible

`public boolean makeVisible()`

---

### newWindow

`protected abstract java.awt.Window newWindow(javax.swing.JComponent aJComponent)`

---

### newWindow

`protected java.awt.Window newWindow()`

---

### resetUserInterface

`public void resetUserInterface()`

---

### setDisposeIfDeactivated

`public void setDisposeIfDeactivated(boolean aBoolean)`

---

### setLabel

`public void setLabel(String aString)`

---

### setWindow

`public void setWindow(java.awt.Window aWindow)`

---

### setWindowResizable

`protected abstract void setWindowResizable(
java.awt.Window aWindow,
boolean aBoolean)`

---

### setWindowTitle

`protected abstract void setWindowTitle(
java.awt.Window aWindow,
String aString)`

---

### startListeningToWindow

`protected void startListeningToWindow()`

---

### stopListeningToWindow

`protected void stopListeningToWindow()`

---

### subcontrollerEditedDidChange

`public void subcontrollerEditedDidChange(EOController anEOController)`

---

### subcontrollerMinimumSizeDidChange

`public void subcontrollerMinimumSizeDidChange(
EOComponentController anEOComponentController,
javax.swing.JComponent aJComponent,
java.awt.Dimension aDimension)`

---

### verifyContentMinimumSize

`protected java.awt.Dimension verifyContentMinimumSize(
java.awt.Window aWindow,
java.awt.Dimension aDimension)`

---

### window

`public java.awt.Window window()`

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

### windowIconified

`public void windowIconified(java.awt.event.WindowEvent aWindowEvent)`

---

### windowOpened

`public void windowOpened(java.awt.event.WindowEvent aWindowEvent)`

---

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

__DRAFT__
