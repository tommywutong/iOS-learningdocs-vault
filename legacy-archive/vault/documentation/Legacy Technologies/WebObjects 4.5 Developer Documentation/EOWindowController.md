---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOApplication.framework/Java/Classes/EOWindowController.html
archived_at: '2026-07-15T08:11:36.729729Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOApplication Reference

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

# EOWindowController

> **__Inherits
> from:__**
> : [EOComponentController](EOComponentController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33nobxw4zloorbw63tuojxwy3dfoi) : [EOController](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33oorzg63dmmvza) : Object

> **__Implements:__**
> : ActionListener
> : (java.awt.event package)
> : EOComponentController.Activation

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
> : [EOWindowController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixukt2xnfxgi33xinxw45dsn5wgyzls)
> : [generateBorderSizeForRootPaneContainerClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6v3jnzsg652dn5xhi4tpnrwgk4rpm5sw4zlsmf2gkqtpojsgk4stnf5gkrtpojjg633ukbqw4zkdn5xhiyljnzsxeq3mmfzxg)
> : [actionPerformed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixwcy3unfxw4udfojtg64tnmvsa)
> : [activate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixwcy3unf3gc5df)
> : [activateWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixwcy3unf3gc5dfk5uw4zdpo4)
> : [borderSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixwe33smrsxeu3jpjsq)
> : [borderedSizeForComponentSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixwe33smrsxezleknuxuzkgn5zeg33nobxw4zloorjws6tf)
> : [componentDidBecomeInvisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixwg33nobxw4zloorcgszccmvrw63lfjfxhm2ltnfrgyzi)
> : [componentShouldBeResizable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixwg33nobxw4zloorjwq33vnrseezksmvzws6tbmjwgk)
> : [componentSizeForBorderedSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixwg33nobxw4zloorjws6tfizxxeqtpojsgk4tfmrjws6tf)
> : [defaultActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixwizlgmf2wy5cbmn2gs33oom)
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixwi2ltobxxgzi)
> : [generateBorderSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixwozlomvzgc5dfijxxezdfojjws6tf)
> : [generateComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixwozlomvzgc5dfinxw24dpnzsw45a)
> : [integrationComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixws3tumvtxeylunfxw4q3pnvyg63tfnz2a)
> : [minimumIntegrationComponentSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixw22lonfwxk3kjnz2gkz3smf2gs33oinxw24dpnzsw45ctnf5gk)
> : [removeTransientSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixxezlnn53gkvdsmfxhg2lfnz2fg5lcmnxw45dsn5wgyzls)
> : [setUsesActivationAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixxgzlukvzwk42bmn2gs5tboruw63sbmn2gs33o)
> : [setUsesActivationButton](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixxgzlukvzwk42bmn2gs5tboruw63scov2hi33o)
> : [setUsesUserDefaultsWindowLocation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixxgzlukvzwk42vonsxerdfmzqxk3duonlws3ten53uy33dmf2gs33o)
> : [setUsesUserDefaultsWindowSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixxgzlukvzwk42vonsxerdfmzqxk3duonlws3ten53vg2l2mu)
> : [setWindowPosition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixxgzluk5uw4zdpo5ig643joruw63q)
> : [usesActivationAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixxk43fonawg5djozqxi2lpnzawg5djn5xa)
> : [usesActivationButton](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixxk43fonawg5djozqxi2lpnzbhk5dun5xa)
> : [usesUserDefaultsWindowLocation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixxk43fonkxgzlsirswmylvnr2hgv3jnzsg652mn5rwc5djn5xa)
> : [usesUserDefaultsWindowSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixxk43fonkxgzlsirswmylvnr2hgv3jnzsg652tnf5gk)
> : [windowPosition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpk5uw4zdpo5bw63tuojxwy3dfoixxo2lomrxxoudponuxi2lpny)

## Constructors

---

### EOWindowController

`public EOWindowController(EOXMLUnarchiver anEOXMLUnarchiver)`

---

## Static Methods

---

### generateBorderSizeForRootPaneContainerClass

`protected static java.awt.Dimension generateBorderSizeForRootPaneContainerClass(
Class aClass,
boolean aBoolean)`

---

## Instance Methods

---

### actionPerformed

`public void actionPerformed(java.awt.event.ActionEvent anActionEvent)`

---

### activate

`public boolean activate()`

---

### activateWindow

`public abstract void activateWindow()`

---

### borderSize

`public java.awt.Dimension borderSize()`

---

### borderedSizeForComponentSize

`public java.awt.Dimension borderedSizeForComponentSize(java.awt.Dimension aDimension)`

---

### componentDidBecomeInvisible

`protected void componentDidBecomeInvisible()`

---

### componentShouldBeResizable

`protected boolean componentShouldBeResizable(javax.swing.JComponent aJComponent)`

---

### componentSizeForBorderedSize

`public java.awt.Dimension componentSizeForBorderedSize(java.awt.Dimension aDimension)`

---

### defaultActions

`protected NSArray defaultActions()`

---

### dispose

`public void dispose()`

---

### generateBorderSize

`protected java.awt.Dimension generateBorderSize()`

---

### generateComponent

`protected void generateComponent()`

---

### integrationComponent

`public javax.swing.JComponent integrationComponent()`

---

### minimumIntegrationComponentSize

`public java.awt.Dimension minimumIntegrationComponentSize()`

---

### removeTransientSubcontroller

`protected boolean removeTransientSubcontroller(EOController anEOController)`

---

### setUsesActivationAction

`public void setUsesActivationAction(boolean aBoolean)`

---

### setUsesActivationButton

`public void setUsesActivationButton(boolean aBoolean)`

---

### setUsesUserDefaultsWindowLocation

`public void setUsesUserDefaultsWindowLocation(boolean aBoolean)`

---

### setUsesUserDefaultsWindowSize

`public void setUsesUserDefaultsWindowSize(boolean aBoolean)`

---

### setWindowPosition

`public void setWindowPosition(int anInt)`

---

### usesActivationAction

`public boolean usesActivationAction()`

---

### usesActivationButton

`public boolean usesActivationButton()`

---

### usesUserDefaultsWindowLocation

`public boolean usesUserDefaultsWindowLocation()`

---

### usesUserDefaultsWindowSize

`public boolean usesUserDefaultsWindowSize()`

---

### windowPosition

`public int windowPosition()`

---

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

__DRAFT__
