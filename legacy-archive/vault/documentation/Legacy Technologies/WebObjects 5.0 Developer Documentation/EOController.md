---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOApplicationRef/Java/Classes/EOController.html
archived_at: '2026-07-15T08:13:42.677868Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# EOController

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : NSDisposable: NSKeyValueCodingAdditions: EOAction.Enabling: NSKeyValueCoding.ErrorHandling: NSKeyValueCoding

> **__Package:__**
> : com.webobjects.eoapplication

---

## Class Description

---

The EOController class defines basic behavior for controller objects that are responsible for managing and sometimes generating the user interface for the client side of a Java Client application. An application's controllers are arranged in a hierarchy, which describes the complete functionality of an application.

The controller hierarchy mirrors the hierarchy of windows and widgets that make up the client application's user interface. The root of the hierarchy is an EOApplication object. The EOApplication's subcontrollers are usually window or applet controllers, which themselves have subcontrollers.

The most significant functionality provided by the EOController class is managing the controller hierarchy (building, connecting, and traversing the hierarchy) and handling actions.

## Building the Controller Hierarchy

EOController defines methods for building the controller hierarchy. You can add and remove controllers ( [addSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5qwizctovrgg33oorzg63dmmvza), [removeFromSupercontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zgk3lpozsum4tpnvjxk4dfojrw63tuojxwy3dfoi)), be notified when the controller hierarchy changes ( [subcontrollerWasAdded](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zxkytdn5xhi4tpnrwgk4sxmfzuczdemvsa) and [subcontrollerWasRemoved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zxkytdn5xhi4tpnrwgk4sxmfzvezlnn53gkza)), and inquire about the relationships controllers have to one another ( [subcontrollers](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zxkytdn5xhi4tpnrwgk4tt), [supercontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zxk4dfojrw63tuojxwy3dfoi), [isAncestorOfController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5uxgqlomnsxg5dpojhwmq3pnz2he33mnrsxe), and [isSupercontrollerOfController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5uxgu3vobsxey3pnz2he33mnrsxet3ginxw45dsn5wgyzls)).

You might need to directly invoke the methods __addSubcontroller__ and __removeFromSupercontroller__ to programmatically manipulate the controller hierarchy. The base implementations of these methods are sufficient for most subclasses. They set and unset a controller's supercontroller ( [setSupercontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zwk5ctovygk4tdn5xhi4tpnrwgk4q)) and notify that supercontroller that a subcontroller was added or removed.

If you write a custom controller and you need to do something special when a subcontroller is added to or removed from the controller hierarchy, override the methods [subcontrollerWasAdded](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zxkytdn5xhi4tpnrwgk4sxmfzuczdemvsa) and [subcontrollerWasRemoved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zxkytdn5xhi4tpnrwgk4sxmfzvezlnn53gkza) to put your customizations there. Taking this approach, you shouldn't have to override the add and remove methods.

## Traversing the Controller Hierarchy

EOController defines numerous methods for traversing the controller hierarchy, but a single method provides the basic traversal functionality. The method [controllerEnumeration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojcw45lnmvzgc5djn5xa) creates and returns an enumeration that includes all the descendents of a controller (not including the controller), all the ancestors of a controller (not including the controller), or a controller and its descendants. You can further restrict the controllers included in an enumeration by specifying an interface the controllers must implement in order to be included. For more information, see the [EOController.Enumeration](EOController.Enumeration.md#apple-ijduosciijfek) interface specification and the method description for __controllerEnumeration__.

Other methods that traverse the controller hierarchy use a controller enumeration to perform the traversal. There are methods that return controllers in an enumeration that match one or more key-value pairs. Methods that use key-value coding on the controllers in an enumeration, returning the first controller that has a specified key or returning the value for that key. Also, there's a method ( [invokeMethod](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5uw45tpnnsu2zlunbxwi)) that invokes a particular method on the controllers in an enumeration.

## Connecting Controllers

A controller in the controller hierarchy can be connected to its supercontroller or not. Controllers are connected when they're performing their duties, and they are disconnected when they become idle. Generally controllers are connected only when their user interface is visible. For example, the controllers associated with a window are connected when the window is visible, and they're disconnected when the window becomes invisible.

When a controller _connects_ to its supercontroller, it gets from its supercontroller whatever resources or information it needs, and it prepares itself in whatever way necessary to perform its duties (for example, setting delegates). Similarly, when a controller breaks its connection to its supercontroller, it cleans up its resources for an idle period.

The EOController class defines methods for connecting controllers. There are methods for connecting and disconnecting a controller from its supercontroller ( [establishConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5sxg5dbmjwgs43iinxw43tfmn2gs33o) and [breakConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rhezlbnnbw63tomvrxi2lpny)), and also methods that make connections all the way up the controller hierarchy ( [establishConnectionToSupercontrollers](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5sxg5dbmjwgs43iinxw43tfmn2gs33okrxvg5lqmvzgg33oorzg63dmmvzhg)) and break connections all the way down ( [breakConnectionToSubcontrollers](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rhezlbnnbw63tomvrxi2lpnzkg6u3vmjrw63tuojxwy3dfojzq)). Generally you use the latter methods that connect or disconnect an entire branch of a tree. EOController's implementations of all these methods is generally sufficient for subclasses. They set the connection status of a controller ( [setConnected](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zwk5cdn5xg4zldorswi)), and notify the controller that its connection has been established or broken. You shouldn't have to override these methods.

If you do need to do something when a controller is connected or disconnected, you should override the methods [connectionWasEstablished](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tomvrxi2lpnzlwc42fon2gcytmnfzwqzle) and [connectionWasBroken](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tomvrxi2lpnzlwc42cojxwwzlo). These methods are invoked automatically by __establishConnection__ and __breakConnection__.

## Accessing and Enabling Actions

Controllers define actions that users can perform (such as quitting the application) and they know how to respond to those actions when they're performed. EOController defines methods that manage a controllers actions.

A controller has a set of actions. It also keeps track of which of those actions are enabled and which are disabled. For performance reasons, EOController's method implementations cache some of this information. Thus, whenever you do something that changes a controller's actions (such as adding a new subcontroller or enabling or disabling an action), the caches must be reset. Most of the time they're reset automatically, but subclasses might need to explicitly reset them with the method [resetActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zgk43forawg5djn5xhg).

To specify the actions a subclass understands, override the method [defaultActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5sgkztbovwhiqldoruw63tt). However, to find out what actions a controller understands, use [actions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5qwg5djn5xhg). This method simply manages and returns a cache of the methods returned by __defaultActions__. Some implementations of a __defaultActions__ method are potentially costly to invoke over and over again, because they dynamically build their collections of actions. The __actions__ method is simply an optimization. EOController's implementation of __actions__ should be sufficient for subclasses; you should never need to override it.

To find out what actions a controller can perform at a specific point in time, use the method [enabledActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5sw4ylcnrswiqldoruw63tt). This method returns only the controller's actions that aren't explicitly disabled. As with __actions__, __enabledActions__ manages and returns a cache of methods, and EOController's implemenation should be sufficient for subclasses.

## Transience

Some controllers are needed only to dynamically generate the user interface and don't serve any purpose after the user interface has been created and connected. For example, an EOTextFieldController creates a widget and a corresponding association and then is no longer needed. Controllers such as EOTextFieldController can be __transient__, because after their work is done, they can sometimes be removed from the controller hierarchy and disposed of (with [disposeIfTransient](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5sgs43qn5zwkslgkrzgc3ttnfsw45a)). This keeps the controller hierarchy simple, which makes user interface management more efficient.

Controllers specify whether or not they can be transient by overriding the method [canBeTransient](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rwc3scmvkheyloonuwk3tu). Some controllers can be transient sometimes and not other times, so not all implementations simply return `true` or `false`. For example, an EOTableController can be transient if the double click action is unassigned. If the action is assigned, however, the controller must listen for a double click and react when one occurs.

Subclasses that can be transient should invoke the method __disposeIfTransient__ as soon as their work is done and they can be disposed of. Sometimes a controller's supercontroller doesn't allow the controller to be disposed of. For example, the EOTabSwitchComponent doesn't allow its subcontrollers to be disposed of even if they're transient.

## Rule System and XML Description

The following tables identify the `controllerType`, XML tag, and XML attributes used by the rule system and EOXMLUnarchiver to generate a controller hierarchy. For more information, see the section ["Rule System and XML Description" (page 8)](The%20eoapplication%20Package.md#apple-ijaucrsgijduu) in the package introduction.

|  |
| --- |
| __Default Rule System Controller Type__ |
| None |

|  |
| --- |
| __XML Tag__ |
| None |

|  |  |  |
| --- | --- | --- |
| __XML Attribute__ | __Value__ | __Description__ |
| `className` | string | Name of a class to instantiate instead of the default class. |
| `disabledActionNames` | array of strings | Names of actions to explicitly disable. |
| `typeName` | string | This is usually a textual representation of the specification used to generate the controller, for example "question = window, task = query". The type name is used by the controller factory to identify which windows are the same so that it can reuse resources. The typeName is also used by the defaults system to specify per-window defaults. |

## Constants

---

EOController defines the following `int` constants to identify types of enumerations returned by the method [controllerEnumeration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojcw45lnmvzgc5djn5xa):

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| SubcontrollersEnumeration | An enumeration object that enumerates over a controller's subcontrollers, not including the controller itself. |
| SupercontrollersEnumeration | An enumeration object that enumerates over a controller's supercontrollers, not including the controller itself. |
| ControllerAndSubcontrollersEnumeration | An enumeration object that enumerates over a controller and its subcontrollers. |

## Interfaces Implemented

---

> : NSDisposable: [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5sgs43qn5zwk): : NSKeyValueCoding (Inherited from EOKeyValueCoding): [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf52gc23fkzqwy5lfizxxes3fpe): [valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf53gc3dvmvdg64slmv4q): : EOKeyValueCoding (Inherited from EOKeyValueCodingAdditions): [handleQueryWithUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5ugc3tenrsvc5lfoj4vo2lunbkw4ytpovxgis3fpe): [handleTakeValueForUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5ugc3tenrsviyllmvlgc3dvmvdg64svnzrg65lomrfwk6i): [unableToSetNullForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf52w4ylcnrsvi32tmv2e45lmnrdg64slmv4q): : EOKeyValueCodingAdditions: [takeValueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf52gc23fkzqwy5lfizxxes3fpfigc5di): [valueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf53gc3dvmvdg64slmv4vayluna): : EOAction.Enabling: [canPerformActionNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rwc3sqmvzgm33snvawg5djn5xe4ylnmvsa):

## Method Types

---

> **Constructors**
> : [EOController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5cu6q3pnz2he33mnrsxe)
>
> **Managing the controller hierarchy**
> : [addSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5qwizctovrgg33oorzg63dmmvza): [subcontrollerWasAdded](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zxkytdn5xhi4tpnrwgk4sxmfzuczdemvsa): [removeFromSupercontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zgk3lpozsum4tpnvjxk4dfojrw63tuojxwy3dfoi): [removeSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zgk3lpozsvg5lcmnxw45dsn5wgyzls): [subcontrollerWasRemoved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zxkytdn5xhi4tpnrwgk4sxmfzvezlnn53gkza): [setSupercontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zwk5ctovygk4tdn5xhi4tpnrwgk4q): [removeTransientSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zgk3lpozsvi4tbnzzwszloorjxkytdn5xhi4tpnrwgk4q): [canBeTransient](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rwc3scmvkheyloonuwk3tu): [subcontrollers](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zxkytdn5xhi4tpnrwgk4tt): [supercontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zxk4dfojrw63tuojxwy3dfoi): [isAncestorOfController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5uxgqlomnsxg5dpojhwmq3pnz2he33mnrsxe): [isSupercontrollerOfController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5uxgu3vobsxey3pnz2he33mnrsxet3ginxw45dsn5wgyzls)
>
> **Traversing the controller hierarchy**
> : [controllerEnumeration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojcw45lnmvzgc5djn5xa): [controllersInEnumeration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojzus3sfnz2w2zlsmf2gs33o): [controllerWithKeyValuePair](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojlws5dijnsxsvtbnr2wkudbnfza): [controllerWithKeyValuePairs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojlws5dijnsxsvtbnr2wkudbnfzhg): [controllersWithKeyValuePair](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojzvo2lunbfwk6kwmfwhkzkqmfuxe): [controllersWithKeyValuePairs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojzvo2lunbfwk6kwmfwhkzkqmfuxe4y): [hierarchicalControllerForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5ugszlsmfzgg2djmnqwyq3pnz2he33mnrsxertpojfwk6i): [hierarchicalValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5ugszlsmfzgg2djmnqwyvtbnr2wkrtpojfwk6i): [invokeMethod](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5uw45tpnnsu2zlunbxwi)
>
> **Connecting controllers**
> : [establishConnectionToSupercontrollers](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5sxg5dbmjwgs43iinxw43tfmn2gs33okrxvg5lqmvzgg33oorzg63dmmvzhg): [establishConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5sxg5dbmjwgs43iinxw43tfmn2gs33o): [connectionWasEstablished](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tomvrxi2lpnzlwc42fon2gcytmnfzwqzle): [breakConnectionToSubcontrollers](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rhezlbnnbw63tomvrxi2lpnzkg6u3vmjrw63tuojxwy3dfojzq): [breakConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rhezlbnnbw63tomvrxi2lpny): [connectionWasBroken](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tomvrxi2lpnzlwc42cojxwwzlo): [setConnected](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zwk5cdn5xg4zldorswi): [isConnected](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5uxgq3pnzxgky3umvsa)
>
> **Accessing and enabling actions**
> : [actions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5qwg5djn5xhg): [defaultActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5sgkztbovwhiqldoruw63tt): [enabledActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5sw4ylcnrswiqldoruw63tt): [actionWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5qwg5djn5xfo2lunbhgc3lf): [actionNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5qwg5djn5xe4ylnmvzq): [disableActionNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5sgs43bmjwgkqldoruw63somfwwkza): [enableActionNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5sw4ylcnrsucy3unfxw4ttbnvswi): [isActionNamedEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5uxgqldoruw63somfwwkzcfnzqwe3dfmq): [resetActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zgk43forawg5djn5xhg)
>
> **Reusing controllers**
> : [prepareForNewTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5yhezlqmfzgkrtpojhgk52umfzww)
>
> **Accessing the type name**
> : [typeName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf52hs4dfjzqw2zi): [setTypeName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zwk5cupfygkttbnvsq)
>
> **Accessing keys**
> : [canAccessFieldsDirectly](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3pnz2he33mnrsxel3dmfxecy3dmvzxgrtjmvwgi42enfzgky3unr4q)
>
> **Disposing**
> : [disposeIfTransient](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5sgs43qn5zwkslgkrzgc3ttnfsw45a): [disposableRegistry](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5sgs43qn5zwcytmmvjgkz3jon2he6i)
>
> **Methods inherited from Object**
> : [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf52g6u3uojuw4zy)

## Constructors

---

### EOController

`public EOController()`

Description forthcoming.

`public EOController(EOXMLUnarchiver unarchiver)`

Creates and returns a new controller. The no argument constructor is used when you create a controller programmatically, whereas the version taking an unarchiver is used in a Direct to Java Client applications to create controllers from an XML description. Controller subclasses should implement both constructors. Most commonly, controllers are created with the assistance of an unarchiver. For more information on this unarchiving, see the book _Getting Started with Direct to Java Client_.

---

## Static Methods

---

### canAccessFieldsDirectly

`public static boolean canAccessFieldsDirectly()`

Returns `true` if the receiver accesses its instance variables directly or `false` otherwise.By default, controllers don't access instance variables directly and return `false`.

__See Also:__ __accessInstanceVariablesDirectly__ (EOCustomObject)

---

## Instance Methods

---

### actionNames

`public NSArray actionNames()`

Returns an array of strings naming the actions the controller defines and responds to.

__See Also:__ ["Accessing and Enabling Actions" (page 121)](#apple-inceqqscireug)

---

### actionWithName

`public EOAction actionWithName(String actionName)`

If the receiver has an action named _actionName_, this method returns that action; otherwise, the method returns `null`.

__See Also:__ ["Accessing and Enabling Actions" (page 121)](#apple-inceqqscireug)

---

### actions

`public NSArray actions()`

Returns an array containing the receiver's actions. EOController's implementation caches the result of [defaultActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5sgkztbovwhiqldoruw63tt) and returns that. The cache is cleared with the method [resetActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zgk43forawg5djn5xhg).

__See Also:__ ["Accessing and Enabling Actions" (page 121)](#apple-inceqqscireug)

---

### addSubcontroller

`public void addSubcontroller(EOController subcontroller)`

Adds _controller_ as a subcontroller of the receiver and sets the receiver as _controller_'s supercontroller (first removing _controller_ from it's supercontroller if it already has one). Invoke this method to programmatically add a subcontroller to the hierarchy.

EOController's implementation sets _subcontroller_'s supercontroller and notifies the receiver that a subcontroller was added. It does nothing if _controller_ is a supercontroller of the receiver. The default implantation of this method should be sufficient for most subclasses; you shouldn't have to override it. If you need to do something special when a subcontroller is added, override [subcontrollerWasAdded](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zxkytdn5xhi4tpnrwgk4sxmfzuczdemvsa).

__See Also:__ ["Building the Controller Hierarchy" (page 120)](#apple-inceqssfizfem)

---

### breakConnection

`public void breakConnection()`

Breaks the receiver's connection to its supercontroller. Invokes [connectionWasBroken](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tomvrxi2lpnzlwc42cojxwwzlo) to give the receiver a chance to clean up, and informs all its ancestors that a subcontroller's connections have changed so the ancestors can respond appropriately. Use this method to programmatically disconnect a single controller (and not its subcontrollers).

EOController's implementation is sufficient for most subclasses, so you don't ordinarily override this method.

__See Also:__ ["Connecting Controllers" (page 121)](#apple-inceqrkcirdeu)

---

### breakConnectionToSubcontrollers

`public void breakConnectionToSubcontrollers()`

Breaks the connections the receiver's subcontrollers have to their subcontrollers, and then breaks the receiver's connections to its subcontrollers. This method is invoked recursively down the subcontroller chain until the receiver and all its subcontrollers are disconnected. Use this method to programmatically disconnect a branch of the controller hierarchy from a particular controller down.

EOController's implementation is sufficient for most subclasses, so you don't ordinarily override this method.

__See Also:__ ["Connecting Controllers" (page 121)](#apple-inceqrkcirdeu)

---

### canBeTransient

`public boolean canBeTransient()`

Returns `true` if the controller can be transient, `false` otherwise. EOController's implementation returns `false`.

__See Also:__ ["Transience" (page 122)](#apple-inceqskijfbek)

---

### canPerformActionNamed

`public boolean canPerformActionNamed(String actionName)`

Conformance to [EOAction.Enabling](EOAction.Enabling.md#apple-ijauissii5eum). See the method description of [canPerformActionNamed](EOAction.Enabling.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpifrxi2lpnyxek3tbmjwgs3thf5rwc3sqmvzgm33snvawg5djn5xe4ylnmvsa) in the interface specification for EOAction.Enabling.

__See Also:__ [isActionNamedEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5uxgqldoruw63somfwwkzcfnzqwe3dfmq), ["Accessing and Enabling Actions" (page 121)](#apple-inceqqscireug)

---

### connectionWasBroken

`protected void connectionWasBroken()`

Invoked from [breakConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rhezlbnnbw63tomvrxi2lpny) to notify the receiver that its connection to its supercontroller has been broken, giving the receiver the opportunity to clean up after its become idle.

__See Also:__ ["Connecting Controllers" (page 121)](#apple-inceqrkcirdeu)

---

### connectionWasEstablished

`protected void connectionWasEstablished()`

Invoked from [establishConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5sxg5dbmjwgs43iinxw43tfmn2gs33o) to notify the receiver that its connection to the controller hierarchy has been established, giving the receiver the opportunity to prepare itself (for example, setting delegates).

__See Also:__ ["Connecting Controllers" (page 121)](#apple-inceqrkcirdeu)

---

### controllerEnumeration

`public EOController.Enumeration controllerEnumeration( int enumerationType, Class controllerInterface)`

Returns an enumeration object of the specified type and interface. For example, invoking this method with `SubcontrollersEnumeration` as the _enumerationType_ and with `MyControllerInterface` as the _controllerInterface_ returns an enumeration object that returns the receiver's subcontrollers that implement the interface `MyControllerInterface`. The _enumerationType_ argument can be one of:

- [SubcontrollersEnumeration](#apple-inceqrckjjdeq)
- [SupercontrollersEnumeration](#apple-inceqrkgifduc)
- [ControllerAndSubcontrollersEnumeration](#apple-inceqskbjbdue)

The _controllerInterface_ argument can be the name of an interface or `null` to specify no interface, which returns all the controllers specified by _enumerationType_.

__See Also:__ ["Traversing the Controller Hierarchy" (page 120)](#apple-inceqrskjjaum), [EOController.Enumeration](EOController.Enumeration.md#apple-ijduosciijfek) interface specification

---

### controllersInEnumeration

`public NSArray controllersInEnumeration( int enumerationType, Class controllerInterface)`

Returns the controllers in an enumeration specified by _enumerationType_ and _controllerInterface_.

__See Also:__ [controllerEnumeration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojcw45lnmvzgc5djn5xa)

---

### controllersWithKeyValuePair

`public NSArray controllersWithKeyValuePair( int enumerationType, Class controllerInterface, String key, Object value)`

Traverses the controller hierarchy, and returns the controllers in the hierarchy whose values for _key_ match _value_. This method uses a controller enumeration specified by _enumerationType_ and _controllerInterface_ to find the controllers. The method tests the controllers returned by the enumeration for matches and returns them. Matches are determined with the method [valueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf53gc3dvmvdg64slmv4vayluna).

__See Also:__ ["Traversing the Controller Hierarchy" (page 120)](#apple-inceqrskjjaum), [controllerEnumeration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojcw45lnmvzgc5djn5xa)

---

### controllersWithKeyValuePairs

`public NSArray controllersWithKeyValuePairs( int enumerationType, Class controllerInterface, NSDictionary keyValuePairs)`

Traverses the controller hierarchy, and returns the controllers in the hierarchy whose key-value pairs match those specified in _keyValuePairs_. This method uses a controller enumeration specified by _enumerationType_ and _controllerInterface_ to find the controllers. The method tests the controllers returned by the enumeration for matches and returns them. Matches are determined with the method [valueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf53gc3dvmvdg64slmv4vayluna).

__See Also:__ ["Traversing the Controller Hierarchy" (page 120)](#apple-inceqrskjjaum), [controllerEnumeration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojcw45lnmvzgc5djn5xa)

---

### controllerWithKeyValuePair

`public EOController controllerWithKeyValuePair( int enumerationType, Class controllerInterface, String key, Object value)`

Traverses the controller hierarchy, and returns the first controller in the hierarchy whose value for _key_ matches _value_. This method uses a controller enumeration specified by _enumerationType_ and _controllerInterface_ to find the controller. The method tests the controllers returned by the enumeration for a match and returns the first that it matches. Matches are determined with the method [valueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf53gc3dvmvdg64slmv4vayluna).

__See Also:__ ["Traversing the Controller Hierarchy" (page 120)](#apple-inceqrskjjaum), [controllerEnumeration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojcw45lnmvzgc5djn5xa)

---

### controllerWithKeyValuePairs

`public EOController controllerWithKeyValuePairs( int enumerationType, Class controllerInterface, NSDictionary keyValuePairs)`

Traverses the controller hierarchy, and returns the first controller in the hierarchy whose key-value pairs match those specified in _keyValuePairs_. This method uses a controller enumeration specified by _enumerationType_ and _controllerInterface_ to find the controller. The method tests the controllers returned by the enumeration for a match and returns the first that it matches. Matches are determined with the method [valueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf53gc3dvmvdg64slmv4vayluna).

__See Also:__ ["Traversing the Controller Hierarchy" (page 120)](#apple-inceqrskjjaum), [controllerEnumeration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojcw45lnmvzgc5djn5xa)

---

### defaultActions

`protected NSArray defaultActions()`

Returns an array of the receiver's default actions (EOAction objects). A subclass of EOController should override this method to return the action it defines merged with the actions of its supercclass. Never invoke this method directly. Instead, invoke [actions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5qwg5djn5xhg), which caches the results of __defaultActions__ and is therefore more efficient.

__See Also:__ ["Accessing and Enabling Actions" (page 121)](#apple-inceqqscireug)

---

### disableActionNamed

`public void disableActionNamed(String actionName)`

Disables the action specified by the name _actionName_ and resets the receiver's actions.

__See Also:__ ["Accessing and Enabling Actions" (page 121)](#apple-inceqqscireug)

---

### disposableRegistry

`public NSDisposableRegistry disposableRegistry()`

Returns the receiver's disposable registry. This registry contains objects that will be disposed of together with the receiver. Subclasses can use the registry to register objects that should be disposed when their controller is disposed.

---

### dispose

`public void dispose()`

Conformance to NSDisposable. See the method description of __dispose__ in the interface specification for NSDisposable.

---

### disposeIfTransient

`protected boolean disposeIfTransient()`

Disposes the receiver if it's transient, first removing it from its supercontroller with [removeTransientSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zgk3lpozsvi4tbnzzwszloorjxkytdn5xhi4tpnrwgk4q). Returns `true` if the receiver is transient and has been disposed, `false` otherwise. If the receiver's supercontroller is non-`null`, this method also attempts to dispose of the supercontroller if it's transient.

__See Also:__ ["Transience" (page 122)](#apple-inceqskijfbek), [removeTransientSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zgk3lpozsvi4tbnzzwszloorjxkytdn5xhi4tpnrwgk4q)

---

### enableActionNamed

`public void enableActionNamed(String actionName)`

Enables the action named _actionName_ and resets the receiver's actions.

__See Also:__ ["Accessing and Enabling Actions" (page 121)](#apple-inceqqscireug)

---

### enabledActions

`public NSArray enabledActions()`

Returns an array of the receiver's enabled actions-those of the receiver's EOAction objects that aren't explicitly disabled. This method caches the enabled actions to enhance performance. The cache is cleared with the method [resetActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zgk43forawg5djn5xhg).

__See Also:__ ["Accessing and Enabling Actions" (page 121)](#apple-inceqqscireug)

---

### establishConnection

`public void establishConnection()`

Connects the receiver to the controller hierarchy. Invokes [connectionWasEstablished](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tomvrxi2lpnzlwc42fon2gcytmnfzwqzle) to give the receiver a chance to ready the user interface. After connecting the receiver, this method disposes of it if it's transient and is therefore no longer needed. Use this method to programmatically connect a single controller (and not its ancestors).

EOController's implementation is sufficient for most subclasses, so you don't ordinarily override this method.

__See Also:__ ["Connecting Controllers" (page 121)](#apple-inceqrkcirdeu)

---

### establishConnectionToSupercontrollers

`public void establishConnectionToSupercontrollers()`

Connects the receiver's supercontroller to the controller hierarchy, and then establishes the receiver's connection to the controller hierarchy. This method is invoked recursively up the supercontroller chain until the receiver and all its ancestors are connected. Use this method to programmatically prepare a branch of the controller hierarchy from a controller up to the root controller.

EOController's implementation is sufficient for most subclasses, so you don't ordinarily override this method.

__See Also:__ ["Connecting Controllers" (page 121)](#apple-inceqrkcirdeu)

---

### handleQueryWithUnboundKey

`public Object handleQueryWithUnboundKey(String key)`

Conformance to EOKeyValueCoding. See the method description of __handleQueryWithUnboundKey__ in the interface specification for EOKeyValueCoding.

---

### handleTakeValueForUnboundKey

`public void handleTakeValueForUnboundKey( Object value, String key)`

Conformance to EOKeyValueCoding. See the method description of __handleTakeValueForUnboundKey__ in the interface specification for EOKeyValueCoding.

---

### hierarchicalControllerForKey

`public EOController hierarchicalControllerForKey( Class controllerInterface, String key)`

Starting at the receiver, searches up the controller hierarchy for the first controller that implements _controllerInterface_ and has a non-`null` value for _key_. Returns that controller or `null` if none of the controllers have a non-`null` value for _key_.

__See Also:__ ["Traversing the Controller Hierarchy" (page 120)](#apple-inceqrskjjaum), [controllerEnumeration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojcw45lnmvzgc5djn5xa)

---

### hierarchicalValueForKey

`public Object hierarchicalValueForKey( Class controllerInterface, String key)`

Starting at the receiver, searches up the controller hierarchy for the first controller that implements _controllerInterface_ and has a non-`null` value for _key_. Returns the value or `null` if none of the controllers have a non-`null` value for _key_.

__See Also:__ ["Traversing the Controller Hierarchy" (page 120)](#apple-inceqrskjjaum), [controllerEnumeration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojcw45lnmvzgc5djn5xa)

---

### invokeMethod

`public void invokeMethod( int enumerationType, Class controllerInterface, String methodName, Class[] parameterTypes[], Object[] parameters[])`

Traverses the controller hierarchy, invoking the method specified by _methodName_ and _parameterTypes_ on the appropriate controllers. This method uses a controller enumeration specified by _enumerationType_ and _controllerInterface_ to find the controllers on which to invoke the specified method. For each controller in the enumeration, this method invokes the _methodName_ method with the values in _parameters_ as arguments to the method.

__See Also:__ ["Traversing the Controller Hierarchy" (page 120)](#apple-inceqrskjjaum), [controllerEnumeration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojcw45lnmvzgc5djn5xa)

---

### isActionNamedEnabled

`public boolean isActionNamedEnabled(String actionName)`

Returns `true` if the action specified by _actionName_ isn't specifically disabled, `false` otherwise.

__See Also:__ ["Accessing and Enabling Actions" (page 121)](#apple-inceqqscireug)

---

### isAncestorOfController

`public boolean isAncestorOfController(EOController controller)`

Returns `true` if _controller_ is a subcontroller of the receiver, of the receiver's subcontrollers, or their subcontrollers, and so on; `false` otherwise.

---

### isConnected

`public boolean isConnected()`

Returns `true` if the receiver is connected, `false` otherwise.

__See Also:__ ["Connecting Controllers" (page 121)](#apple-inceqrkcirdeu)

---

### isSupercontrollerOfController

`public boolean isSupercontrollerOfController(EOController controller)`

Returns `true` if _controller_ is an immediate subcontroller of the receiver, `false` otherwise.

---

### prepareForNewTask

`public void prepareForNewTask(boolean prepareSubcontrollersForNewTask)`

Prepares the receiver for performing a new task by resetting any data. If _prepareSubcontrollersForNewTask_ is `true`, this method also sends [prepareForNewTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5yhezlqmfzgkrtpojhgk52umfzww) to each of the receiver's subcontrollers. This method is invoked to prepare a branch of the controller hierarchy to be reused. Subclasses should override this method to get rid of data and perform any additional clean up.

---

### removeFromSupercontroller

`public void removeFromSupercontroller()`

Removes the receiver from its supercontroller's set of subcontrollers. Invoke this method when you need to programmatically remove a controller from the controller hierarchy.

EOController's implementation simply invokes [removeSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zgk3lpozsvg5lcmnxw45dsn5wgyzls) on the receiver's supercontroller. This method is a convenience so you don't have to look up a controller's supercontroller. The default implementation should be sufficient for subclasses; you shouldn't have to override it.

__See Also:__ ["Building the Controller Hierarchy" (page 120)](#apple-inceqssfizfem)

---

### removeSubcontroller

`protected void removeSubcontroller(EOController subcontroller)`

Removes _subcontroller_ from the controller hierarchy. EOController's implementation disconnects _subcontroller_ from the controller hierarchy, and invokes [subcontrollerWasRemoved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zxkytdn5xhi4tpnrwgk4sxmfzvezlnn53gkza) on the receiver to give the receiver a chance to respond appropriately. Never invoke this method directly; use __removeFromSupercontroller__ instead. The default implementation should be sufficient for subclasses; you shouldn't have to override it. If you need to do something when a subcontroller is removed, implement [subcontrollerWasRemoved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zxkytdn5xhi4tpnrwgk4sxmfzvezlnn53gkza).

__See Also:__ ["Building the Controller Hierarchy" (page 120)](#apple-inceqssfizfem)

---

### removeTransientSubcontroller

`protected boolean removeTransientSubcontroller(EOController subcontroller)`

Removes _subcontroller_ from the controller hierarchy if _subcontroller_ can be transient and if the receiver allows it. Returns `true` if the subcontroller could be removed, `false` otherwise. This method is invoked from [disposeIfTransient](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5sgs43qn5zwkslgkrzgc3ttnfsw45a), which is invoked in various situations to remove controllers as soon as they can become transient.

__See Also:__ ["Transience" (page 122)](#apple-inceqskijfbek)

---

### resetActions

`public void resetActions()`

Destroys the receiver's cache of actions and enabled actions, and destroys the action caches of the receiver's supercontrollers. This method is generally invoked automatically when the receiver's set of actions changes or when an action's enabled state is changed, but you can invoke it yourself to clear the caches as needed. EOController's implementation of this method is sufficient for most subclasses. You shouldn't have to override it.

__See Also:__ ["Accessing and Enabling Actions" (page 121)](#apple-inceqqscireug)

---

### setConnected

`protected void setConnected(boolean flag)`

Sets the receiver's connected status according to _flag_. EOController's implementation is sufficient for most subclasses; you don't normally override this method. Nor should you ever need to invoke it; [establishConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5sxg5dbmjwgs43iinxw43tfmn2gs33o) and [breakConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rhezlbnnbw63tomvrxi2lpny) set the controller's connection status automatically.

__See Also:__ ["Connecting Controllers" (page 121)](#apple-inceqrkcirdeu)

---

### setSupercontroller

`protected boolean setSupercontroller(EOController controller)`

Sets the receiver's supercontroller to _controller_ and resets the receiver's actions. Returns `true` on success or `false` otherwise. It fails if _controller_ is unacceptable as the receiver's supercontroller. Also, _controller_ can be `null` to unset the receiver's supercontroller.

EOController's implementation is sufficient for most subclasses; you don't normally override this method. Nor should you ever need to invoke it; [addSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5qwizctovrgg33oorzg63dmmvza) sets the supercontroller automatically.

__See Also:__ ["Building the Controller Hierarchy" (page 120)](#apple-inceqssfizfem)

---

### setTypeName

`public void setTypeName(String typeName)`

Sets the receiver's type name to _typeName_.

__See Also:__ ["Rule System and XML Description" (page 122)](#apple-inceqrcfjbfek)

---

### subcontrollers

`public NSArray subcontrollers()`

Returns the receiver's immediate subcontrollers. Use [controllerEnumeration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojcw45lnmvzgc5djn5xa) of [controllersInEnumeration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojzus3sfnz2w2zlsmf2gs33o) to return all the controllers in the hierarchy under the receiver.

---

### subcontrollerWasAdded

`protected void subcontrollerWasAdded(EOController subcontroller)`

Invoked from [addSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5qwizctovrgg33oorzg63dmmvza) to notify the receiver that its subcontroller _subcontroller_ has been added to the controller hierarchy, giving the receiver the opportunity to prepare the subcontroller for use.

__See Also:__ ["Building the Controller Hierarchy" (page 120)](#apple-inceqssfizfem)

---

### subcontrollerWasRemoved

`protected void subcontrollerWasRemoved(EOController subcontroller)`

Invoked from [removeSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5zgk3lpozsvg5lcmnxw45dsn5wgyzls) to notify the receiver that its subcontroller _subcontroller_ has been removed from the controller hierarchy, giving the receiver the opportunity to perform any necessary clean up.

__See Also:__ ["Building the Controller Hierarchy" (page 120)](#apple-inceqssfizfem)

---

### supercontroller

`public EOController supercontroller()`

Returns the receiver's supercontroller, or `null` if the receiver has no supercontroller.

`public EOController supercontroller(Class controllerInterface)`

Searching from the receiver's immediate supercontroller, returns the first supercontroller that implements the interface _controllerInterface_. Returns `null` if the receiver has no supercontroller or if none of the supercontrollers implement _controllerInterface_. Returns the receiver's immediate supercontroller if controllerInterface is `null`.

---

### takeValueForKey

`public void takeValueForKey( Object value, String key)`

Conformance to NSKeyValueCoding. See the method description of __valueForKey__ in the interface specification for NSKeyValueCoding.

---

### takeValueForKeyPath

`public void takeValueForKeyPath( Object value, String keyPath)`

Conformance to EOKeyValueCodingAdditions (com.webobjects.eocontrol). See the method description of __takeValueForKeyPath__ in the interface specification for EOKeyValueCodingAdditions.

---

### toString

`public String toString()`

Returns the receiver as a string that states the receiver's class name and type name, whether the receiver is connected, and the number of subcontrollers.

---

### typeName

`public String typeName()`

Returns the receiver's type name-a string that uniquely identifies the receiver as a node in the controller hierarchy. EOController's implementation returns `null`. The type name is used to identify controllers that have the same task. It is used to configure a controller with user defaults and also to reuse controllers when possible.

__See Also:__ ["Rule System and XML Description" (page 122)](#apple-inceqrcfjbfek)

---

### unableToSetNullForKey

`public void unableToSetNullForKey(String key)`

Conformance to EOKeyValueCoding. See the method description of __unableToSetNullForKey__ in the interface specification for EOKeyValueCoding.

---

### valueForKey

`public Object valueForKey(String key)`

Conformance to NSKeyValueCoding. See the method description of __valueForKey__ in the interface specification for NSKeyValueCoding.

---

### valueForKeyPath

`public Object valueForKeyPath(String keyPath)`

Conformance to EOKeyValueCodingAdditions (com.webobjects.eocontrol). See the method description of __valueForKeyPath__ in the interface specification for EOKeyValueCodingAdditions.

---

© 2001 Apple Computer, Inc. (Last Published April 14, 2001)

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
