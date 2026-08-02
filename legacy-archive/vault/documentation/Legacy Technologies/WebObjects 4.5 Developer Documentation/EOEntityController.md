---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOApplication.framework/Java/Classes/EOEntityController.html
archived_at: '2026-07-15T08:11:36.511364Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOApplication Reference

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

# EOEntityController

> **__Inherits
> from:__**
> : [EOComponentController](EOComponentController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33nobxw4zloorbw63tuojxwy3dfoi) : [EOController](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33oorzg63dmmvza) : Object

> **__Implements:__**
> : EOObserving
> : EOObjectDisplay
> : EOAssociationConnector
> : EOComponentController.EndEditing
> : NSInlineObservable (Inherited from EOController)
> : NSDisposable (Inherited from EOController)
> : EOKeyValueCodingAdditions (Inherited from EOController)
> : EOAction.Enabling (Inherited from EOController)
> : EOKeyValueCoding (Inherited from EOKeyValueCodingAdditions)
> : NSKeyValueCoding (Inherited from EOKeyValueCoding)

> **__Package:__**
> : com.apple.client.eoapplication

---

## Class Description

---

The EOEntityController class provides behavior
for displaying enterprise objects in a user interface that can optionally
be loaded from an archive (a nib file). EOEntityController's most
basic API is specified by the interface [EOObjectDisplay](EOObjectDisplay.md#apple-inbecrckirfes), which
identifies an implementation strategy that uses EOEditingContexts
and EODisplayGroups to manage an entity controller's enterprise
objects. An entity controller has an entity name, which identifies
the kind of enterprise objects the controller works with. Additionally
it has an editing context that manages the controller's enterprise
objects, a display group that displays the enterprise objects and
manages a selection, and a controller display group that connects
controller methods to the user interface. For more information,
see the [EOObjectDisplay](EOObjectDisplay.md#apple-inbecrckirfes) interface
specification.

## User Interface Archive

As a subclass of EOComponentController, EOEntityController
manages a user interface component. However, whereas component controllers
dynamically generate their components, entity controllers have the
ability to load their components from an archive. An entity controller
has an archive name, which specifies the archive from which to load
the controller's component. If, however, a controller doesn't
have an archive name, the controller can fall back on dynamically
generating its component (an empty EOView).

## Managing the Editing Context

As mentioned earlier, EOEntityController uses an editing context
to manage its enterprise objects. By default, an entity controller
attempts to get its editing context from a supercontroller. An entity controller
looks up the controller hierarchy for the first EOObjectDisplay
ancestor that has an editing context. If it finds one, the entity
controller uses that supercontroller's editing context. If it
doesn't find one, it creates one.

You can change the way an entity controller gets its editing
context by specifying a __provider method__ with [setEditingContextProviderMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxgzluivsgs5djnztug33oorsxq5cqojxxm2lemvze2zlunbxwittbnvsq).
If an entity controller has an editing context provider method,
it gets its editing context by invoking that method.

The provider method name is a string, which can be a key path
or the name of an arbitrary class's static method. For an example
of setting the method name to a key path, consider a subclass of EOEntityController
that implements the method __customizedEditingContext__ to
return an editing context for the controller to use. In this case,
the provider method name could be set to "customizedEditingContext".

If the provider method name is the name of a static method,
the format of the string is "<class name>:<static method
name>". For example, suppose that you've written a subclass
of EOApplication that implements a static method, __customizedEditingContextForAllControllers__,
to return an editing context for all an application's controllers
to share. Then the editing context provider method name for all
entity controllers could be set to "CustomApplicationClass:customizedEditingContextForAllControllers".

EOEntityController provides two methods that you can use as
provider methods: [newEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixw4zlxivsgs5djnztug33oorsxq5a) and [nestedEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixw4zltorswirlenf2gs3thinxw45dfpb2a).
The former simply creates a new editing context and is a convenience
for setting the provider method. The latter attempts to create a
new editing context that's nested inside an ancestor's editing
context. If no ancestors provide an editing context to be a parent, __nestedEditingContext__ simply
creates a new editing context.

## Managing the Display Group

EOEntityController uses a display group to display its enterprise
objects. By default, an entity controller attempts to get its display
group from a supercontroller. An entity controller looks up the controller
hierarchy for the first EOObjectDisplay ancestor. If that supercontroller
has the same entity name and a display group, the entity controller
uses that supercontroller's display group. If it doesn't find
one, it invokes [loadArchive](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixwy33bmraxey3inf3gk) to see
if a display group is provided in the archive. If the controller
still doesn't have a display group, it simply creates one.

You can change the way an entity controller gets its display
group by specifying a __provider method__ with [setDisplayGroupProviderMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxgzluiruxg4dmmf4uo4tpovyfa4tpozuwizlsjvsxi2dpmrhgc3lf).
If an entity controller has a display group provider method, it
gets its display group by invoking that method. The display group
provider method name works the same way the editing context provider
method name works. For more information, see ["Managing the Editing Context"](#apple-ijbesskejbdum).

EOEntityController provides two methods that you can use as
provider methods: [newDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixw4zlxiruxg4dmmf4uo4tpovya) and [newDisplayGroupUsingOptimisticRefresh](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixw4zlxiruxg4dmmf4uo4tpovyfk43jnztu64dunfwws43unfrvezlgojsxg2a).
The simply create new display groups and are convenience methods
for setting the provider method.

## Rule System and XML Description

The following tables identify the `controllerType`,
XML tag, and XML attributes used by the rule system and EOXMLUnarchiver
to generate a controller hierarchy. For more information, see the
section ["Rule System and XML Description"](The%20eoapplication%20Package.md#apple-ijaucrsgijduu) in the package introduction.

|  |
| --- |
| __Default Rule System Controller Type__ |
| `entityController` |

|  |
| --- |
| __XML Tag__ |
| `ENTITYCONTROLLER` |

|  |  |  |
| --- | --- | --- |
| __XML Attribute__ | __Value__ | __Description__ |
| `archive` | string | The name of a nib file from which the controller loads its component (instead of dynamically creating it). |
| `displayGroupProviderMethodName` | string | A key path or string of the form "<class name>:<method name>" that names a method the controller uses to create its display group. |
| `editingContextProviderMethodName` | string | A key path or string of the form "<class name>:<method name>" that names a method the controller uses to create its editing context. |
| `entity` | string | Name of the controller's entity. |

## Interfaces Implemented

---

> EOObserving: [objectWillChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixw6ytkmvrxiv3jnrweg2dbnztwk)
>
> EOObjectDisplay: [controllerDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixwg33oorzg63dmmvzei2ltobwgc6khojxxk4a)
> : [displayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixwi2ltobwgc6khojxxk4a)
> : [editingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixwkzdjoruw4z2dn5xhizlyoq)
> : [entityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixwk3tunf2hsttbnvsq)
>
> EOAssociationConnector: [takeResposibilityForConnectionOfAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxiyllmvjgk43qn5zwsytjnruxi6kgn5zeg33onzswg5djn5xe6zsbonzw6y3jmf2gs33o)
>
> EOComponentController.EndEditing: [endEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixwk3teivsgs5djnztq)
>
> NSInlineObservable
> (Inherited from EOController)
>
> NSDisposable
> (Inherited from EOController): [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixwi2ltobxxgzi)
>
> EOKeyValueCodingAdditions
> (Inherited from EOController)
>
> EOAction.Enabling
> (Inherited from EOController)
>
> EOKeyValueCoding
> (Inherited from EOKeyValueCodingAdditions)
>
> NSKeyValueCoding
> (Inherited from EOKeyValueCoding)

## Method Types

---

> **Constructors**
> : [EOEntityController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixukt2fnz2gs5dzinxw45dsn5wgyzls)
>
> **Setting the entity**
> : [setEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxgzluivxhi2lupfhgc3lf)
>
> **Loading an archive**
> : [prepareComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxa4tfobqxezkdn5wxa33omvxhi)
> : [loadArchive](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixwy33bmraxey3inf3gk)
> : [controllerDidLoadArchive](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixwg33oorzg63dmmvzei2lejrxwczcbojrwq2lwmu)
> : [objectForOutletPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixw6ytkmvrxirtpojhxk5dmmv2fayluna)
> : [setArchiveName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxgzluifzgg2djozsu4ylnmu)
> : [archiveName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixwc4tdnbuxmzkomfwwk)
>
> **Managing the editing
> context**
> : [newEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixw4zlxivsgs5djnztug33oorsxq5a)
> : [setEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxgzluivsgs5djnztug33oorsxq5a)
> : [setEditingContextProviderMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxgzluivsgs5djnztug33oorsxq5cqojxxm2lemvze2zlunbxwittbnvsq)
> : [editingContextProviderMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixwkzdjoruw4z2dn5xhizlyorihe33wnfsgk4snmv2gq33ejzqw2zi)
> : [nestedEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixw4zltorswirlenf2gs3thinxw45dfpb2a)
> : [startListeningToEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxg5dboj2ey2ltorsw42lom5kg6rlenf2gs3thinxw45dfpb2a)
> : [stopListeningToEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxg5dpobggs43umvxgs3thkrxukzdjoruw4z2dn5xhizlyoq)
> : [handleEditingContextNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixwqylomrwgkrlenf2gs3thinxw45dfpb2e433unftgsy3boruw63q)
> : [setResetsEditingContextWhenPreparingForNewTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxgzlukjsxgzluoncwi2lunfxgoq3pnz2gk6duk5ugk3sqojsxaylsnfxgortpojhgk52umfzww)
> : [resetsEditingContextWhenPreparingForNewTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxezltmv2hgrlenf2gs3thinxw45dfpb2fo2dfnzihezlqmfzgs3thizxxettfo5kgc43l)
>
> **Managing the controller
> display group**
> : [setControllerDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxgzluinxw45dsn5wgyzlsiruxg4dmmf4uo4tpovya)
> : [hasControllerDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixwqyltinxw45dsn5wgyzlsiruxg4dmmf4uo4tpovya)
>
> **Managing the objects
> display group**
> : [newDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixw4zlxirqxiyktn52xey3f)
> : [newDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixw4zlxiruxg4dmmf4uo4tpovya)
> : [newDisplayGroupUsingOptimisticRefresh](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixw4zlxiruxg4dmmf4uo4tpovyfk43jnztu64dunfwws43unfrvezlgojsxg2a)
> : [setDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxgzluiruxg4dmmf4uo4tpovya)
> : [startListeningToDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxg5dboj2ey2ltorsw42lom5kg6rdjonygyylzi5zg65lq)
> : [stopListeningToDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxg5dpobggs43umvxgs3thkrxui2ltobwgc6khojxxk4a)
> : [setObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxgzluj5rguzldorlws5dii5wg6ytbnreui)
> : [setObjectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxgzluj5rguzldorzvo2lunbdgk5ddnbjxazldnftgsy3boruw63q)
> : [displayGroupSortOrderings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixwi2ltobwgc6khojxxk4ctn5zhit3smrsxe2lom5zq)
> : [setDisplayGroupProviderMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxgzluiruxg4dmmf4uo4tpovyfa4tpozuwizlsjvsxi2dpmrhgc3lf)
> : [displayGroupProviderMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixwi2ltobwgc6khojxxk4cqojxxm2lemvze2zlunbxwittbnvsq)
>
> **Accessing selected objects**
> : [selectedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxgzlmmvrxizlej5rguzldoq)
> : [selectedObjectGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxgzlmmvrxizlej5rguzldordwy33cmfwesra)
> : [selectedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxgzlmmvrxizlej5rguzldorzq)
> : [selectedObjectsGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxgzlmmvrxizlej5rguzldorzuo3dpmjqwyskeom)
>
> **Fetching**
> : [fetchesOnConnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixwmzlumnugk42pnzbw63tomvrxi)
> : [setFetchesOnConnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxgzluizsxiy3imvzu63sdn5xg4zldoq)
>
> **Determining the root
> document controller**
> : [isRootEntityController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixws42sn5xxirlooruxi6kdn5xhi4tpnrwgk4q)
>
> **Notifying observers of
> change**
> : [willChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxo2lmnrbwqylom5sq)
>
> **Methods inherited from
> EOController**
> : [connectionWasBroken](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixwg33onzswg5djn5xfoyltijzg623fny)
> : [connectionWasEstablished](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixwg33onzswg5djn5xfoyltivzxiylcnruxg2dfmq)
> : [establishConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixwk43umfrgy2ltnbbw63tomvrxi2lpny)
> : [prepareForNewTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxa4tfobqxezkgn5ze4zlxkrqxg2y)
>
> **Methods inherited from
> Object**
> : [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixxi32torzgs3th)

## Constructors

---

### EOEntityController

`public EOEntityController(EOXMLUnarchiver unarchiver)`

---

## Instance Methods

---

### archiveName

`public String archiveName()`

---

### connectionWasBroken

`protected void connectionWasBroken()`

---

### connectionWasEstablished

`protected void connectionWasEstablished()`

---

### controllerDidLoadArchive

`protected void controllerDidLoadArchive(NSDictionary aNSDictionary)`

---

### controllerDisplayGroup

`public com.apple.client.eointerface.EODisplayGroup controllerDisplayGroup()`

---

### displayGroup

`public com.apple.client.eointerface.EODisplayGroup displayGroup()`

---

### displayGroupProviderMethodName

`public String displayGroupProviderMethodName()`

---

### displayGroupSortOrderings

`protected NSArray displayGroupSortOrderings()`

---

### dispose

`public void dispose()`

---

### editingContext

`public com.apple.client.eocontrol.EOEditingContext editingContext()`

---

### editingContextProviderMethodName

`public String editingContextProviderMethodName()`

---

### endEditing

`public boolean endEditing()`

---

### entityName

`public String entityName()`

---

### establishConnection

`public void establishConnection()`

---

### fetchesOnConnect

`public boolean fetchesOnConnect()`

---

### handleEditingContextNotification

`public void handleEditingContextNotification(NSNotification aNSNotification)`

---

### hasControllerDisplayGroup

`public boolean hasControllerDisplayGroup()`

---

### isRootEntityController

`protected boolean isRootEntityController()`

---

### loadArchive

`protected boolean loadArchive()`

---

### nestedEditingContext

`public com.apple.client.eocontrol.EOEditingContext nestedEditingContext()`

---

### newDataSource

`protected com.apple.client.eocontrol.EODataSource newDataSource()`

---

### newDisplayGroup

`public com.apple.client.eointerface.EODisplayGroup newDisplayGroup()`

---

### newDisplayGroupUsingOptimisticRefresh

`public com.apple.client.eointerface.EODisplayGroup newDisplayGroupUsingOptimisticRefresh()`

---

### newEditingContext

`public com.apple.client.eocontrol.EOEditingContext newEditingContext()`

---

### objectForOutletPath

`public Object objectForOutletPath(
EOArchive anEOArchive,
String aString)`

---

### objectWillChange

`public void objectWillChange(Object anObject)`

---

### prepareComponent

`protected void prepareComponent()`

---

### prepareForNewTask

`public void prepareForNewTask(boolean aBoolean)`

---

### resetsEditingContextWhenPreparingForNewTask

`public boolean resetsEditingContextWhenPreparingForNewTask()`

---

### selectedObject

`public com.apple.client.eocontrol.EOEnterpriseObject selectedObject()`

---

### selectedObjectGlobalID

`public com.apple.client.eocontrol.EOGlobalID selectedObjectGlobalID()`

---

### selectedObjects

`public NSArray selectedObjects()`

---

### selectedObjectsGlobalIDs

`public NSArray selectedObjectsGlobalIDs()`

---

### setArchiveName

`public void setArchiveName(String aString)`

---

### setControllerDisplayGroup

`public void setControllerDisplayGroup(com.apple.client.eointerface.EODisplayGroup anEODisplayGroup)`

---

### setDisplayGroup

`public void setDisplayGroup(com.apple.client.eointerface.EODisplayGroup anEODisplayGroup)`

---

### setDisplayGroupProviderMethodName

`public void setDisplayGroupProviderMethodName(String aString)`

---

### setEditingContext

`public void setEditingContext(com.apple.client.eocontrol.EOEditingContext anEOEditingContext)`

---

### setEditingContextProviderMethodName

`public void setEditingContextProviderMethodName(String aString)`

---

### setEntityName

`public void setEntityName(String aString)`

---

### setFetchesOnConnect

`public void setFetchesOnConnect(boolean aBoolean)`

---

### setObjectWithGlobalID

`public void setObjectWithGlobalID(com.apple.client.eocontrol.EOGlobalID anEOGlobalID)`

---

### setObjectsWithFetchSpecification

`public void setObjectsWithFetchSpecification(com.apple.client.eocontrol.EOFetchSpecification anEOFetchSpecification)`

---

### setResetsEditingContextWhenPreparingForNewTask

`public void setResetsEditingContextWhenPreparingForNewTask(boolean aBoolean)`

---

### startListeningToDisplayGroup

`protected void startListeningToDisplayGroup()`

---

### startListeningToEditingContext

`protected void startListeningToEditingContext()`

---

### stopListeningToDisplayGroup

`protected void stopListeningToDisplayGroup()`

---

### stopListeningToEditingContext

`protected void stopListeningToEditingContext()`

---

### takeResposibilityForConnectionOfAssociation

`public void takeResposibilityForConnectionOfAssociation(com.apple.client.eointerface.EOAssociation anEOAssociation)`

---

### toString

`public String toString()`

---

### willChange

`public void willChange()`

---

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

__DRAFT__
