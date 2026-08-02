---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOApplicationRef/Java/Classes/EOComponentController.html
archived_at: '2026-07-15T08:13:42.639583Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# EOComponentController

> **__Inherits from:__**
> : [EOController](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33oorzg63dmmvza): Object

> **__Implements:__**
> : NSDisposable: (Inherited from EOController): com.webobjects.eocontrol.EOKeyValueCodingAdditions (Inherited from EOController): EOAction.Enabling (Inherited from EOController): com.webobjects.eocontrol.EOKeyValueCoding (Inherited from EOKeyValueCodingAdditions): com.webobjects.foundation.NSKeyValueCoding (Inherited from EOKeyValueCoding)

> **__Package:__**
> : com.webobjects.eoapplication

---

## Class Description

---

The EOComponentController class provides behavior for controllers that manage user interface components. A component controller has a __component__, that represents the user interface for the controller itself (not for its subcontrollers), a __subcontroller area__ for displaying the user interfaces for its subcontrollers, and an __integration component__-a component that represents the controller when its shown in its supercontrollers user interface.

By default, a controller's integration component is simply the controller's component. In other words, a supercontroller adds its subcontrollers' components to the subcontroller area of its component. However, the integration component can be a completely separate component. For example, the integration component for a window controller is a button that, when pushed, opens the window controller's window.

Also by default, a controller's subcontroller area is simply the controller's component. In the simplest case, a component controller doesn't have its own user interface, but only serves to display the user interfaces of its subcontrollers. For example, EOComponentController's component is simply an EOView. It puts nothing in the view except its subcontrollers' user interfaces. Thus, the subcontroller area is the controller's component-the EOView. However, the subcontroller area can be a subcomponent of the controller's component. For example, an EOBoxController's component contains a border (etched or bezel, for example) which is the box controller's user interface. Its subcontroller area is a component located inside the border. This is where the box controller displays its subcontrollers.

## Managing the Component

To access a component controller's component, use the method [component](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpmnxw24dpnzsw45a). If the component hasn't yet been created, __component__ creates it by invoking [prepareComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpobzgk4dbojsug33nobxw4zlooq). And __prepareComponent__, in turn, invokes [generateComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpm5sw4zlsmf2gkq3pnvyg63tfnz2a) to dynamically create the component. Subclasses should override __generateComponent__.

To see if a controller's component has been created, use the method [isComponentPrepared](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpnfzug33nobxw4zloorihezlqmfzgkza). Sometimes you need to know if a component has been created, because you can't configure its behavior after its creation. For example, if you want to set a component's alignment behavior, you have to set it with the EOComponentController method [setAlignsComponents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponsxiqlmnftw442dn5wxa33omvxhi4y) before the component controller creates its component.

## Visibility

A component controller is visible when its component is visible on screen. When a controller becomes visible, it ensures that it's connected to its supercontroller. However, a controller that's connected to its supercontroller isn't necessarily visible. For example, you might connect an invisible controller when you need to prepare it with data before making it visible.

Similarly, a controller can be "shown" or "hidden" in its supercontroller without changing the controller's visibility. The method [showInSupercontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponug652jnzjxk4dfojrw63tuojxwy3dfoi) ensures that the receiver's integration component is displayed in its supercontroller's component. This doesn't necessarily change the visibility of the controller. For example, a tab switch controller might switch to another view, but if the switch controller isn't visible when the change occurs, the subcontroller doesn't become visible.

## Component Appearance

A component controller's component can have an icon and a label. The component can be represented in the user interface with icon only, label only, or with both icon and label. A component specifies which representation it prefers. A controller can _prefer_ to be represented with an icon only, but can't require it. This is because the controller might not have an icon. If the controller prefers icon only and has an icon, then the controller is represented with the icon only. If the controller doesn't prefer icon only and has an icon, then the controller is represented with its icon and label. If the controller doesn't have an icon, the controller is represented with the label only.

A controller always has a label. If the controller's label hasn't been explicitly set, the controller derives one from its subcontrollers.

## Layout

Subclasses of EOComponentController have complete control over how they lay out their subcontrollers. EOComponentController's implementation can lay out subcontrollers in a row or a column (the default). To change the layout direction, the method [setUsesHorizontalLayout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponsxivltmvzuq33snf5g63tumfweyylzn52xi).

In addition to horizontal/vertical layout behavior, a component can align its components or not. For example, consider a controller that uses vertical layout and contains several EOTextFieldControllers. If the controller aligns components, it left aligns the text fields. The default alignment behavior aligns components by making their corresponding labels identically sized. The width of the labels is known as the __alignment width__.

To specify a component's alignment behavior, use the method [setAlignsComponents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponsxiqlmnftw442dn5wxa33omvxhi4y). To set the alignment width, use [setAlignmentWidth](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponsxiqlmnftw43lfnz2fo2leorua).

## Resizing

EOComponentController implements complex resizing behavior. For example, if a controller's component changes in a way that might affect its minimum size, the controller's supercontroller is notified and the supercontroller ensures that its subcontroller area is at least as big as the minimum size required to show all its subcontrollers.

Using the default behavior, the user interface doesn't automatically shrink. EOComponentController only resizes up to meet the minimum requirements. As much as possible it resizes components to fill the available space. A component controller can specify both horizontal and vertical resizing behavior for its component to accommodate this scheme.

## Rule System and XML Description

The following tables identify the `controllerType`, XML tag, and XML attributes used by the rule system and EOXMLUnarchiver to generate a controller hierarchy. For more information, see the section ["Rule System and XML Description" (page 8)](The%20eoapplication%20Package.md#apple-ijaucrsgijduu) in the package introduction.

|  |
| --- |
| __Default Rule System Controller Type__ |
| `groupingController` |

|  |
| --- |
| __XML Tag__ |
| `COMPONENTCONTROLLER` |

|  |  |  |
| --- | --- | --- |
| __XML Attribute__ | __Value__ | __Description__ |
| `alignmentWidth` | integer | See ["Layout" (page 97)](#apple-inceqskjiffeq). |
| `alignsComponents` | "true" or "false" | See ["Layout" (page 97)](#apple-inceqskjiffeq). |
| `horizontallyResizable` | "true" or "false" | See ["Resizing" (page 97)](#apple-inceqsshjffes). |
| `iconName` | string | The filename of the component's icon. Uses standard resource location behavior to find the icon by name. See ["Component Appearance" (page 97)](#apple-inceqrccinbui) for more information. |
| `iconURL` | string | The URL from which the icon is downloaded. See ["Component Appearance" (page 97)](#apple-inceqrccinbui) for more information. |
| `label` | string | See ["Component Appearance" (page 97)](#apple-inceqrccinbui). |
| `minimumHeight` | integer | The minimum height of the controller's component, not including its subcontroller area. |
| `minimumWidth` | integer | The minimum width of the controller's component, not including its subcontroller area. |
| `prefersIconOnly` | "true" or "false" | See ["Component Appearance" (page 97)](#apple-inceqrccinbui). |
| `usesHorizontalLayout` | "true" or "false" | See ["Layout" (page 97)](#apple-inceqskjiffeq). |
| `verticallyResizable` | "true" or "false" | See ["Resizing" (page 97)](#apple-inceqsshjffes). |

## Constants

---

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| Bottom | Description forthcoming. |
| BottomLeft | Description forthcoming. |
| BottomRight | Description forthcoming. |
| Center | Description forthcoming. |
| Left | Description forthcoming. |
| Right | Description forthcoming. |
| Top | Description forthcoming. |
| TopLeft | Description forthcoming. |
| TopRight | Description forthcoming. |

## Interfaces Implemented

---

> : NSDisposable (Inherited from EOController): [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpmruxg4dponsq): : EOKeyValueCodingAdditions (Inherited from EOController): : EOAction.Enabling (Inherited from EOController): : EOKeyValueCoding (Inherited from EOKeyValueCodingAdditions): [handleQueryWithUnboundKey](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5ugc3tenrsvc5lfoj4vo2lunbkw4ytpovxgis3fpe): [handleTakeValueForUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpnbqw4zdmmvkgc23fkzqwy5lfizxxevlomjxxk3tejnsxs): [unableToSetNullForKey](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf52w4ylcnrsvi32tmv2e45lmnrdg64slmv4q): : NSKeyValueCoding (Inherited from EOKeyValueCoding):

## Method Types

---

> **Constructors**
> : [EOComponentController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpivhug33nobxw4zloorbw63tuojxwy3dfoi)
>
> **Managing the component**
> : [generateComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpm5sw4zlsmf2gkq3pnvyg63tfnz2a): [prepareComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpobzgk4dbojsug33nobxw4zlooq): [setComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponsxiq3pnvyg63tfnz2a): [component](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpmnxw24dpnzsw45a): [isComponentPrepared](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpnfzug33nobxw4zloorihezlqmfzgkza)
>
> **Managing the integration component**
> : [integration ComponentDidBecomeInvisible](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOApplicationRef/Java/Classes/EOComponentController.html#//apple_ref/java/instm/EOComponentController/integration): [integrationComponentDidBecomeVisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpnfxhizlhojqxi2lpnzbw63lqn5xgk3tuiruwiqtfmnxw2zkwnfzwsytmmu): [integrationComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpnfxhizlhojqxi2lpnzbw63lqn5xgk3tu)
>
> **Managing the subcontroller area**
> : [setSubcontrollerArea](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponsxiu3vmjrw63tuojxwy3dfojaxezlb): [subcontrollerArea](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpon2wey3pnz2he33mnrsxeqlsmvqq): [addComponentOfSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpmfsgiq3pnvyg63tfnz2e6zstovrgg33oorzg63dmmvza): [removeComponentOfSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpojsw233wmvbw63lqn5xgk3tuj5tfg5lcmnxw45dsn5wgyzls)
>
> **Managing component visibility**
> : [showInSupercontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponug652jnzjxk4dfojrw63tuojxwy3dfoi): [makeVisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpnvqwwzkwnfzwsytmmu): [componentDidBecomeVisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpmnxw24dpnzsw45cenfseezldn5wwkvtjonuwe3df): [showSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponug652tovrgg33oorzg63dmmvza): [hideInSupercontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpnbuwizkjnzjxk4dfojrw63tuojxwy3dfoi): [makeInvisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpnvqwwzkjnz3gs43jmjwgk): [componentDidBecomeInvisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpmnxw24dpnzsw45cenfseezldn5wwksloozuxg2lcnrsq): [hideSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpnbuwizktovrgg33oorzg63dmmvza): [setVisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponsxivtjonuwe3df): [isVisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpnfzvm2ltnfrgyzi)
>
> **Setting component appearance**
> : [setPrefersIconOnly](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponsxiudsmvtgk4ttjfrw63spnzwhs): [prefersIconOnly](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpobzgkztfojzusy3pnzhw43dz): [setIcon](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponsxisldn5xa): [icon](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpnfrw63q): [setLabel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponsxitdbmjswy): [label](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpnrqwezlm)
>
> **Layout behavior**
> : [setUsesHorizontalLayout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponsxivltmvzuq33snf5g63tumfweyylzn52xi): [usesHorizontalLayout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpovzwk42in5zgs6tpnz2gc3cmmf4w65lu): [setAlignsComponents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponsxiqlmnftw442dn5wxa33omvxhi4y): [alignsComponents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpmfwgsz3oonbw63lqn5xgk3tuom): [setAlignmentWidth](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponsxiqlmnftw43lfnz2fo2leorua): [alignmentWidth](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpmfwgsz3onvsw45cxnfshi2a)
>
> **Resizing behavior**
> : [setCanResizeHorizontally](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponsxiq3bnzjgk43jpjsuq33snf5g63tumfwgy6i): [canResizeHorizontally](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpmnqw4utfonuxuzkin5zgs6tpnz2gc3dmpe): [setCanResizeVertically](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponsxiq3bnzjgk43jpjsvmzlsoruwgylmnr4q): [canResizeVertically](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpmnqw4utfonuxuzkwmvzhi2ldmfwgy6i)
>
> **Configuring user interface sizes**
> : [setDefaultComponentSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponsxirdfmzqxk3duinxw24dpnzsw45ctnf5gk): [defaultComponentSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpmrswmylvnr2eg33nobxw4zloorjws6tf): [ensureMinimumComponentSizeWithoutSubcontrollers](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpmvxhg5lsmvgws3tjnv2w2q3pnvyg63tfnz2fg2l2mvlws5din52xiu3vmjrw63tuojxwy3dfojzq): [ensureMinimumSubcontrollerAreaSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpmvxhg5lsmvgws3tjnv2w2u3vmjrw63tuojxwy3dfojaxezlbknuxuzi): [subcontrollerMinimumSizeDidChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpon2wey3pnz2he33mnrsxetljnzuw25lnknuxuzkenfseg2dbnztwk): [minimumComponentSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpnvuw42lnovwug33nobxw4zloorjws6tf): [minimumComponentSizeWithoutSubcontrollers](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpnvuw42lnovwug33nobxw4zloorjws6tfk5uxi2dpov2fg5lcmnxw45dsn5wgyzlsom): [minimumIntegrationComponentSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpnvuw42lnovwus3tumvtxeylunfxw4q3pnvyg63tfnz2fg2l2mu): [minimumSubcontrollerAreaSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpnvuw42lnovwvg5lcmnxw45dsn5wgyzlsifzgkyktnf5gk)
>
> **Determining the root component controller**
> : [isRootComponentController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpnfzve33porbw63lqn5xgk3tuinxw45dsn5wgyzls)
>
> **Methods inherited from EOController**
> : [canBeTransient](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpmnqw4qtfkrzgc3ttnfsw45a): [removeTransientSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpojsw233wmvkheyloonuwk3tukn2wey3pnz2he33mnrsxe): [subcontrollerWasAdded](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpon2wey3pnz2he33mnrsxev3bonawizdfmq): [subcontrollerWasRemoved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpon2wey3pnz2he33mnrsxev3bonjgk3lpozswi)
>
> **Methods inherited from Object**
> : [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rporxvg5dsnfxgo)

## Constructors

---

### EOComponentController

`public EOComponentController(EOXMLUnarchiver unarchiver)`

Creates a new component controller. For information on how these constructors are used and on what they do, see the method description for the [EOController](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5cu6q3pnz2he33mnrsxe) constructors in the EOController class specification.

`public EOComponentController()`

Description forthcoming.

---

## Instance Methods

---

### addComponentOfSubcontroller

`protected void addComponentOfSubcontroller(EOComponentController controller)`

Adds the integration component for the receiver's subcontroller, _controller_, to the user interface for the receiver.

---

### alignmentWidth

`public int alignmentWidth()`

Returns the receiver's alignment width.

__See Also:__ ["Layout" (page 97)](#apple-inceqskjiffeq)

---

### alignsComponents

`public boolean alignsComponents()`

Returns `true` if the receiver aligns its components, `false` otherwise.

__See Also:__ ["Layout" (page 97)](#apple-inceqskjiffeq)

---

### canBeTransient

`public boolean canBeTransient()`

Returns `true` if the controller can be transient, `false` otherwise. By default, a component controller is transient only if it's an instance of EOComponentController, not an instance of a subclass.

__See Also:__ [canBeTransient](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rwc3scmvkheyloonuwk3tu) (EOController)

---

### canResizeHorizontally

`public boolean canResizeHorizontally()`

Returns `true` if the receiver can resize its component horizontally, or `false` otherwise.

__See Also:__ ["Resizing" (page 97)](#apple-inceqsshjffes)

---

### canResizeVertically

`public boolean canResizeVertically()`

Returns `true` if the receiver can resize its component vertically, or `false` otherwise.

__See Also:__ ["Resizing" (page 97)](#apple-inceqsshjffes)

---

### component

`public javax.swing.JComponent component()`

Returns the receiver's component, creating and preparing it first if it doesn't already exist.

__See Also:__ ["Managing the Component" (page 96)](#apple-inceqqskifeuq), [prepareComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpobzgk4dbojsug33nobxw4zlooq), [generateComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpm5sw4zlsmf2gkq3pnvyg63tfnz2a)

---

### componentDidBecomeInvisible

`protected void componentDidBecomeInvisible()`

Invoked by the receiver's supercontroller when the receiver's component becomes invisible, giving the receiver a chance to respond. EOComponentController's implementation invokes [breakConnection](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rhezlbnnbw63tomvrxi2lpny) to break the receiver's connection to the controller hierarchy.

---

### componentDidBecomeVisible

`protected void componentDidBecomeVisible()`

Invoked by the receiver's supercontroller when the receiver's component becomes visible, giving the receiver a chance to respond. EOComponentController's implementation invokes [establishConnection](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5sxg5dbmjwgs43iinxw43tfmn2gs33o) to ensure the receiver is connected to the controller hierarchy.

---

### defaultComponentSize

`public java.awt.Dimension defaultComponentSize()`

Returns the default size for the receiver's component. This is the size the component is set to when it's created.

__See Also:__ ["Resizing" (page 97)](#apple-inceqsshjffes)

---

### dispose

`public void dispose()`

Conformance to NSDisposable. See the method description of __dispose__ in the interface specification for NSDisposable.

---

### ensureMinimumComponentSizeWithoutSubcontrollers

`public void ensureMinimumComponentSizeWithoutSubcontrollers( int width, int height)`

Ensures that the size of the receiver's component, not including the subcontroller area, is at least as large as the area specified by _width_ and _height_. If it isn't, the receiver resizes its component to _width_ and _height_. This method is invoked by the receiver itself when its component is changed in a way that might affect the component's minimum size. For example, suppose a label is changed and requires a larger space.

__See Also:__ ["Resizing" (page 97)](#apple-inceqsshjffes)

---

### ensureMinimumSubcontrollerAreaSize

`public void ensureMinimumSubcontrollerAreaSize( int width, int height)`

Ensures that the size of the receiver's subcontroller area is at least as large as the area specified by _width_ and _height_. If it isn't, the receiver resizes its subcontroller area to _width_ and _height_. This method is invoked when a subcontroller's component changes in a way that might affect its minimum size.

__See Also:__ ["Resizing" (page 97)](#apple-inceqsshjffes)

---

### generateComponent

`protected void generateComponent()`

Creates the receiver's component, including setting up the subcontroller area. Implementations of these methods usually invoke [setComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponsxiq3pnvyg63tfnz2a) and if necessary [setSubcontrollerArea](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponsxiu3vmjrw63tuojxwy3dfojaxezlb). EOComponentController creates an EOView.

__See Also:__ ["Managing the Component" (page 96)](#apple-inceqqskifeuq)

---

### handleTakeValueForUnboundKey

`public void handleTakeValueForUnboundKey( Object value, String key)`

Conformance to EOKeyValueCoding. See the method description of __handleTakeValueForUnboundKey__ in the interface specification for EOKeyValueCoding.

---

### hideInSupercontroller

`public boolean hideInSupercontroller()`

Invokes [hideSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpnbuwizktovrgg33oorzg63dmmvza) on the receiver's supercontroller to hide the receiver's component if the component (or integration component) appears in the supercontroller's user interface. Returns `true` on success, `false` otherwise. If the receiver doesn't have a supercontroller, then this method simply makes the receiver invisible. For example, a window controller which is the root component controller simply closes.

This method is invoked automatically (for example, from [makeInvisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpnvqwwzkjnz3gs43jmjwgk)). You should never need to invoke it yourself.

__See Also:__ ["Visibility" (page 96)](#apple-inceqqsfinauq)

---

### hideSubcontroller

`protected boolean hideSubcontroller(EOComponentController controller)`

Hides _controller_'s user interface in the interface of the receiver. Returns `true` if the subcontroller was successfully hidden, `false` otherwise. EOComponentController's implementation simply returns `false`. This is because most controllers can't hide their subcontrollers. Examples of controllers that can hide their subcontrollers are tab view controllers, which hide a subcontroller by making another subcontroller visible. Don't invoke this method directly; invoke __hideInSupercontroller__ instead.

__See Also:__ ["Visibility" (page 96)](#apple-inceqqsfinauq)

---

### icon

`public javax.swing.Icon icon()`

Returns the receiver's icon, or `null` if it has none.

__See Also:__ ["Component Appearance" (page 97)](#apple-inceqrccinbui)

---

### integrationComponent

`public javax.swing.JComponent integrationComponent()`

Returns the component used as the integration component in the receiver's supercontroller to represent the receiver. EOComponentController returns its component by default.

__See Also:__ ["Class Description" (page 96)](#apple-inceqqsdirbes)

---

### integration ComponentDidBecomeInvisible

`protected void integrationComponentDidBecomeInvisible()`

Invoked by the receiver's supercontroller when the receiver's integration component becomes invisible, giving the receiver a chance to respond. EOComponentController's implementation sets the receiver's visibility to be `false`, because by default the integration component is identical to the component.

---

### integrationComponentDidBecomeVisible

`protected void integrationComponentDidBecomeVisible()`

Invoked by the receiver's supercontroller when the receiver's integration component becomes visible, giving the receiver a chance to respond. EOComponentController's implementation sets the receiver's visibility to be `true`, because by default the integration component is identical to the component.

---

### isComponentPrepared

`protected boolean isComponentPrepared()`

Returns `true` if the receiver is prepared, `false` otherwise.

__See Also:__ ["Managing the Component" (page 96)](#apple-inceqqskifeuq)

---

### isRootComponentController

`public boolean isRootComponentController()`

Returns `true` if the receiver is a root component controller, `false` otherwise. A component controller is the root component controller if its supercontroller is not an instance of EOComponentController.

---

### isVisible

`public boolean isVisible()`

Returns `true` if the receiver is visible, `false` otherwise. A component controller is visible if its component is on the screen. Note, showing a subcontroller in its supercontroller doesn't necessarily mean that it is visible. For example, you can show a component in a tab view, but the component won't be visible unless the tab view is visible.

__See Also:__ ["Visibility" (page 96)](#apple-inceqqsfinauq)

---

### label

`public String label()`

Returns the receiver's label. If the label is not explicitly set, EOComponentController's implementation attempts to derive a label from it's subcontrollers.

__See Also:__ ["Component Appearance" (page 97)](#apple-inceqrccinbui)

---

### makeInvisible

`public boolean makeInvisible()`

Makes the receiver's user interface invisible. If the receiver's supercontroller is a component controller, makes the receiver invisible by making the receiver's supercontroller invisible. Otherwise, invokes [hideInSupercontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpnbuwizkjnzjxk4dfojrw63tuojxwy3dfoi). Returns `true` if the method succeeds in making the receiver invisible, `false` otherwise.

---

### makeVisible

`public boolean makeVisible()`

Makes the receiver's user interface visible. Establishes the receiver's connection to its supercontrollers and invokes [showInSupercontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponug652jnzjxk4dfojrw63tuojxwy3dfoi). If the receiver's supercontroller is a component controller, it also attempts to make the supercontroller visible. Returns `true` if the method succeeds in making the receiver visible, `false` otherwise.

__See Also:__ ["Visibility" (page 96)](#apple-inceqqsfinauq)

---

### minimumComponentSize

`public java.awt.Dimension minimumComponentSize()`

Returns the current minimum size required to display the receiver's component, including the size required for its subcontroller area.

__See Also:__ ["Resizing" (page 97)](#apple-inceqsshjffes)

---

### minimumComponentSizeWithoutSubcontrollers

`public java.awt.Dimension minimumComponentSizeWithoutSubcontrollers()`

Returns the current minimum size required to display the receiver's component, excluding the subcontroller area.

__See Also:__ ["Resizing" (page 97)](#apple-inceqsshjffes)

---

### minimumIntegrationComponentSize

`public java.awt.Dimension minimumIntegrationComponentSize()`

Returns the minimum size required to display the receiver's integration component.

__See Also:__ ["Resizing" (page 97)](#apple-inceqsshjffes)

---

### minimumSubcontrollerAreaSize

`public java.awt.Dimension minimumSubcontrollerAreaSize()`

Returns the minimum size of the subcontroller area to display the receiver's subcontrollers.

__See Also:__ ["Resizing" (page 97)](#apple-inceqsshjffes)

---

### prefersIconOnly

`public boolean prefersIconOnly()`

Returns `true` if the receiver prefers to represent itself with only an icon, `false` otherwise.

__See Also:__ ["Component Appearance" (page 97)](#apple-inceqrccinbui)

---

### prepareComponent

`protected void prepareComponent()`

If the receiver's component is not already prepared, it generates the component.

__See Also:__ ["Managing the Component" (page 96)](#apple-inceqqskifeuq)

---

### removeComponentOfSubcontroller

`protected void removeComponentOfSubcontroller(EOComponentController controller)`

Removes the user interface for the specified subcontroller, _controller_, from the receiver's user interface and informs _controller_ that its integration component became invisible.

---

### removeTransientSubcontroller

`protected boolean removeTransientSubcontroller(EOController controller)`

See the method description for [removeTransientSubcontroller](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zgk3lpozsvi4tbnzzwszloorjxkytdn5xhi4tpnrwgk4q) in the EOController class specification.

---

### setAlignmentWidth

`public void setAlignmentWidth(int alignmentWidgth)`

Sets the receiver's alignment width to _alignmentWidth_. Throws an IllegalStateException if the receiver is already prepared. In other words, you can only set the alignment width before the component is generated.

__See Also:__ ["Layout" (page 97)](#apple-inceqskjiffeq)

---

### setAlignsComponents

`public void setAlignsComponents(boolean flag)`

Sets according to _flag_ whether the receiver aligns the components in its user interface. Throws an IllegalStateException if the receiver is already prepared. In other words, you can only set the alignment behavior before the component is generated.

__See Also:__ ["Layout" (page 97)](#apple-inceqskjiffeq)

---

### setCanResizeHorizontally

`public void setCanResizeHorizontally(boolean flag)`

Sets according to _flag_ whether the receiver's component can resize horizontally. Throws an IllegalStateException if the receiver is already prepared. In other words, you can only set the horizontal resizing behavior before the component is generated.

__See Also:__ ["Resizing" (page 97)](#apple-inceqsshjffes)

---

### setCanResizeVertically

`public void setCanResizeVertically(boolean flag)`

Sets according to _flag_ whether the receiver's component can resize vertically. Throws an IllegalStateException if the receiver is already prepared. In other words, you can only set the vertical resizing behavior before the component is generated.

__See Also:__ ["Resizing" (page 97)](#apple-inceqsshjffes)

---

### setComponent

`public void setComponent(java.awt.Component component)`

Sets the receiver's component to _component_.

__See Also:__ ["Managing the Component" (page 96)](#apple-inceqqskifeuq)

---

### setDefaultComponentSize

`public void setDefaultComponentSize(java.awt.Dimension dimension)`

Sets the default size of the receiver's component to _dimension_.

__See Also:__ ["Resizing" (page 97)](#apple-inceqsshjffes)

---

### setIcon

`public void setIcon(javax.swing.Icon icon)`

Sets the receiver's icon to _icon_.

__See Also:__ ["Component Appearance" (page 97)](#apple-inceqrccinbui)

---

### setLabel

`public void setLabel(String label)`

Sets the receiver's label to _label_.

__See Also:__ ["Component Appearance" (page 97)](#apple-inceqrccinbui)

---

### setPrefersIconOnly

`public void setPrefersIconOnly(boolean flag)`

Sets according to _flag_ whether the receiver prefers to represent itself with only an icon or with an icon and a label.

__See Also:__ ["Component Appearance" (page 97)](#apple-inceqrccinbui)

---

### setSubcontrollerArea

`public void setSubcontrollerArea(javax.swing.JComponent component)`

Sets the component that holds the user interface for the receiver's subcontrollers to _component_.

__See Also:__ ["Class Description" (page 96)](#apple-inceqqsdirbes)

---

### setUsesHorizontalLayout

`public void setUsesHorizontalLayout(boolean flag)`

Sets according to _flag_ whether the receiver uses horizontal layout. Throws an IllegalStateException if the receiver is already prepared. In other words, you can only set the layout direction before the component is generated.

__See Also:__ ["Layout" (page 97)](#apple-inceqskjiffeq)

---

### setVisible

`public void setVisible(boolean flag)`

Sets the visibility of the receiver according to _flag_. Invokes [componentDidBecomeVisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpmnxw24dpnzsw45cenfseezldn5wwkvtjonuwe3df) or [componentDidBecomeInvisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpmnxw24dpnzsw45cenfseezldn5wwksloozuxg2lcnrsq) to notify the receiver that its visibility changed and to give the receiver the opportunity to respond appropriately. Also notifies the receiver's ancestors that a subcontroller's visibility has changed, giving the supercontrollers the opportunity to respond.

If _flag_ is `true`, this method disposes of transient receivers after making them visible.

__See Also:__ ["Visibility" (page 96)](#apple-inceqqsfinauq)

---

### showInSupercontroller

`public boolean showInSupercontroller()`

Invokes [showSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rponug652tovrgg33oorzg63dmmvza) to add the receiver's user interface to its supercontroller's receiver. Returns `true` on success, `false` otherwise. If the supercontroller is `null`, this method also makes the receiver visible.

|  |
| --- |
| __Note:__ Invoking this method doesn't necessarily change the visibility of the receiver. For example, a switch controller might switch the component it displays, but if the switch controller isn't visible, the subcontroller doesn't become visible when it's shown. |

This method is invoked automatically (for example, from [makeVisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpnvqwwzkwnfzwsytmmu)). You should never need to invoke it yourself.

__See Also:__ ["Visibility" (page 96)](#apple-inceqqsfinauq)

---

### showSubcontroller

`protected boolean showSubcontroller(EOComponentController controller)`

Adds _controller_'s user interface to the interface of the receiver. Returns `true` if the subcontroller was successfully shown, `false` otherwise. EOComponentController's implementation simply returns `true`: Since the integration components for subcontrollers are added to a controller's user interface automatically, the subcontrollers are already shown. EOTabSwitchController is an example of a subclass that overrides this method in a meaningful way. To show one subcontroller, the tab switch controller hides another.

__See Also:__ ["Visibility" (page 96)](#apple-inceqqsfinauq)

---

### subcontrollerArea

`public javax.swing.JComponent subcontrollerArea()`

Returns the component that holds the user interface for the receiver's subcontrollers.

__See Also:__ ["Class Description" (page 96)](#apple-inceqqsdirbes)

---

### subcontrollerMinimumSizeDidChange

`public void subcontrollerMinimumSizeDidChange( EOComponentController controller, javax.swing.JComponent component, java.awt.Dimension dimension)`

Updates the receiver's user interface to accommodate a change to the subcontroller's minimum size. This method is invoked by subcontrollers when they change in a way that might affect their component's minimum size. A subcontroller sends this method with itself, its integration component, and its new minimum size as the arguments. The expectation is that the supercontroller will make space for the subcontroller if it needs to.

__See Also:__ ["Resizing" (page 97)](#apple-inceqsshjffes)

---

### subcontrollerWasAdded

`protected void subcontrollerWasAdded(EOController controller)`

Invokes [addComponentOfSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpmfsgiq3pnvyg63tfnz2e6zstovrgg33oorzg63dmmvza) to add the integration component (if any) for the receiver's subcontroller, _controller_, to the receiver's user interface. Invoked from [addSubcontroller](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5qwizctovrgg33oorzg63dmmvza) to notify the receiver that its subcontroller _controller_ has been added to the controller hierarchy.

---

### subcontrollerWasRemoved

`protected void subcontrollerWasRemoved(EOController controller)`

Invokes [removeComponentOfSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw24dpnzsw45cdn5xhi4tpnrwgk4rpojsw233wmvbw63lqn5xgk3tuj5tfg5lcmnxw45dsn5wgyzls) to remove the integration component (if any) for the receiver's subcontroller, _controller_, from the receiver's user interface. Invoked from [removeSubcontroller](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zgk3lpozsvg5lcmnxw45dsn5wgyzls) to notify the receiver that its subcontroller _controller_ has been removed from the controller hierarchy.

---

### toString

`public String toString()`

Returns the receiver as a string that states the receiver's class name and type name, whether the receiver is connected, the number of subcontrollers, whether or not the receiver has been prepared, whether or not the receiver is visible, information about widget sizing and alignment behavior, and so on.

---

### usesHorizontalLayout

`public boolean usesHorizontalLayout()`

Returns `true` if the receiver uses a horizontal layout, `false` otherwise.

__See Also:__ ["Layout" (page 97)](#apple-inceqskjiffeq)

---

© 2001 Apple Computer, Inc. (Last Published April 14, 2001)

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
