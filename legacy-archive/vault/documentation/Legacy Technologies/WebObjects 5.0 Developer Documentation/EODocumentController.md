---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOApplicationRef/Java/Classes/EODocumentController.html
archived_at: '2026-07-15T08:13:42.799155Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# EODocumentController

> **__Inherits from:__**
> : [EOEntityController](EOEntityController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuk3tunf2hsq3pnz2he33mnrsxe): [EOComponentController](EOComponentController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33nobxw4zloorbw63tuojxwy3dfoi): [EOController](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33oorzg63dmmvza)

> **__Implements:__**
> : EODocument: EOEditable: EOAssociationConnector (Inherited from EOEntityController): EOComponentController.EndEditing (Inherited from EOEntityController): EOObserving (Inherited from EOEntityController): EOObjectDisplay (Inherited from EOEntityController): NSInlineObservable (Inherited from EOController): NSDisposable (Inherited from EOController): EOKeyValueCodingAdditions (Inherited from EOController): EOAction.Enabling (Inherited from EOController): EOKeyValueCoding (Inherited from EOKeyValueCodingAdditions): NSKeyValueCoding (Inherited from EOKeyValueCoding)

> **__Package:__**
> : com.webobjects.eoapplication

---

## Class Description

---

The EODocumentController class provides behavior for displaying and editing enterprise objects in a user interface. EODocumentController's API is mostly specified by the interfaces [EODocument](EODocument.md#apple-ijbesskjifdeg) and [EOEditable](EOEditable.md#apple-inducskdinbeg). Additionally, much of the way that EODocumentController works is set up by its superclass, [EOEntityController](EOEntityController.md#apple-ijbesskgjjeug). Since EOEntityControllers use EOEditingContexts and EODisplayGroups to manage and display a set of enterprise objects; EODocumentControllers use them as well. However, in addition to displaying enterprise objects, document controllers can also edit their objects. You can insert, update, and delete enterprise objects; undo and redo unsaved changes; and save and revert.

EODocumentController provides several methods that interact with a user. For example, the methods [revert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3smv3gk4tu) and [saveIfUserConfirms](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3tmf3gkslgkvzwk4sdn5xgm2lsnvzq) open dialogs to confirm that a user wants to revert or save before performing the action. Also, many of the methods open dialogs when an error occurs, telling the user what happened.

## Root Document Controller Responsibilities

EODocumentController defines the concept of a root document controller. A document controller is the root if none of its ancestors are EODocuments. A root document controller usually provides the editing context for all its descendent document controllers-they typically don't have their own. Consequently, the root document controller has responsibilities that non-root document controllers don't have. For example, only the root document controller provides save and revert behavior.

## Rule System and XML Description

The following tables identify the `controllerType`, XML tag, and XML attributes used by the rule system and EOXMLUnarchiver to generate a controller hierarchy. For more information, see the section ["Rule System and XML Description" (page 8)](The%20eoapplication%20Package.md#apple-ijaucrsgijduu) in the package introduction.

|  |
| --- |
| __Default Rule System Controller Type__ |
| `entityController` |

|  |
| --- |
| __XML Tag__ |
| `DOCUMENTCONTROLLER` |

|  |  |  |
| --- | --- | --- |
| __XML Attribute__ | __Value__ | __Description__ |
| `editability` | string | One of "Never", "Always", or "IfSupercontroller". See the __EOEditable__ interface specification for more information on these settings. |

## Interfaces Implemented

---

> : EODocument: [isDocumentForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3joncg6y3vnvsw45cgn5zeo3dpmjqwyske): [isEdited](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3joncwi2lumvsa): [save](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3tmf3gk): [saveIfUserConfirms](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3tmf3gkslgkvzwk4sdn5xgm2lsnvzq): [setEdited](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3tmv2ekzdjorswi): : EOEditable: [editability](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3fmruxiylcnfwgs5dz): [isEditable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3joncwi2lumfrgyzi): [setEditability](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3tmv2ekzdjorqwe2lmnf2hs): [supercontrollerEditabilityDidChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3tovygk4tdn5xhi4tpnrwgk4sfmruxiylcnfwgs5dziruwiq3imfxgozi): [takeResponsibilityForEditabilityOfAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3umfvwkutfonyg63ttnfrgs3djor4um33sivsgs5dbmjuwy2lupfhwmqltonxwg2lboruw63q): : EOAssociationConnector (Inherited from EOEntityController): : EOComponentController.EndEditing (Inherited from EOEntityController): : EOObserving (Inherited from EOEntityController): : EOObjectDisplay (Inherited from EOEntityController): : NSInlineObservable (Inherited from EOController): : NSDisposable (Inherited from EOController): [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3enfzxa33tmu): : EOKeyValueCodingAdditions (Inherited from EOController): : EOAction.Enabling (Inherited from EOController): [canPerformActionNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3dmfxfazlsmzxxe3kbmn2gs33ojzqw2zle): : EOKeyValueCoding (Inherited from EOKeyValueCodingAdditions): : NSKeyValueCoding (Inherited from EOKeyValueCoding):

## Method Types

---

> **Constructors**
> : [EODocumentController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel2fj5cg6y3vnvsw45cdn5xhi4tpnrwgk4q)
>
> **Inserting, updating, and deleting**
> : [insertObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3jnzzwk4tuj5rguzldoq): [deleteSelectedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3emvwgk5dfknswyzldorswit3cnjswg5dt): [wasEdited](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3xmfzukzdjorswi)
>
> **Saving**
> : [canSave](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3dmfxfgylwmu): [saveChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3tmf3gkq3imfxgozlt): [saveAndMakeInvisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3tmf3gkqlomrgwc23fjfxhm2ltnfrgyzi): [saveIfUserConfirms](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3tmf3gkslgkvzwk4sdn5xgm2lsnvzq): [saveIfUserConfirmsAndMakeInvisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3tmf3gkslgkvzwk4sdn5xgm2lsnvzuc3tejvqwwzkjnz3gs43jmjwgk): [saveIfUserConfirmsAndMakeInvisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3tmf3gkslgkvzwk4sdn5xgm2lsnvzuc3tejvqwwzkjnz3gs43jmjwgk): [saveFailed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3tmf3gkrtbnfwgkza)
>
> **Reverting**
> : [canRevert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3dmfxfezlwmvzhi): [revert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3smv3gk4tu): [revertAndMakeInvisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3smv3gk4tuifxgitlbnnsus3twnfzwsytmmu): [revertChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3smv3gk4tuinugc3thmvzq): [revertFailed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3smv3gk4tuizqws3dfmq)
>
> **Undoing and Redoing**
> : [canUndo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3dmfxfk3ten4): [undo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3vnzsg6): [canRedo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3dmfxfezlen4): [redo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3smvsg6)
>
> **Determining the root document controller**
> : [isRootDocumentController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3jonjg633uirxwg5lnmvxhiq3pnz2he33mnrsxe)
>
> **Methods inherited from EOEntityController**
> : [handleEditingContextNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3imfxgi3dfivsgs5djnztug33oorsxq5con52gsztjmnqxi2lpny)
>
> **Methods inherited from EOController**
> : [connectionWasEstablished](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3dn5xg4zldoruw63sxmfzuk43umfrgy2ltnbswi): [defaultActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3emvtgc5lmorawg5djn5xhg): [prepareForNewTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3qojsxaylsmvdg64somv3viyltnm)
>
> **Methods inherited from Object**
> : [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3un5jxi4tjnztq)

## Constructors

---

### EODocumentController

`public EODocumentController()`

`public EODocumentController(EOXMLUnarchiver unarchiver)`

Creates a new document controller. For information on how these constructors are used and on what they do, see the method description for the [EOController](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5cu6q3pnz2he33mnrsxe) constructors in the EOController class specification.

---

## Instance Methods

---

### canPerformActionNamed

`public boolean canPerformActionNamed(String actionName)`

Conformance to [EOAction.Enabling](EOAction.Enabling.md#apple-ijauissii5eum). EODocumentController's implementation uses the methods [canRedo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3dmfxfezlen4), [canRevert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3dmfxfezlwmvzhi), [canSave](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3dmfxfgylwmu), and [canUndo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3dmfxfk3ten4) to determine the enabling state of the corresponding actions.

__See Also:__ [canPerformActionNamed](EOAction.Enabling.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpifrxi2lpnyxek3tbmjwgs3thf5rwc3sqmvzgm33snvawg5djn5xe4ylnmvsa) (EOAction.Enabling)

---

### canRedo

`public boolean canRedo()`

Returns `true` if the receiver can redo, `false` otherwise. A document controller can redo as long as its editing context's undo manager can redo and as long as it (or one of its subcontrollers) is editable.

---

### canRevert

`public boolean canRevert()`

Returns `true` if the receiver can revert, `false` otherwise. A document controller can revert only if it's been edited and only if it's the root document controller.

---

### canSave

`public boolean canSave()`

Returns `true` if the receiver can save, `false` otherwise. A document controller can save only if it's been edited and only if it's the root document controller.

---

### canUndo

`public boolean canUndo()`

Returns `true` if the receiver can undo, `false` otherwise. A document controller can undo as long as its editing context's undo manager can undo and as long as it (or one of its subcontrollers) is editable.

---

### connectionWasEstablished

`protected void connectionWasEstablished()`

See the method description for [connectionWasEstablished](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tomvrxi2lpnzlwc42fon2gcytmnfzwqzle) in the EOController class specification. EODocumentController's implementation additionally updates its editability.

---

### defaultActions

`protected NSArray defaultActions()`

Adds actions for handling editing to the default actions defined by the superclass, [EOEntityController](EOEntityController.md#apple-ijbesskgjjeug). More specifically, it adds save and revert actions. However, note that __defaultActions__ only adds save and revert if the receiver is the root document controller, if it's editable, and if it's not modal.

---

### deleteSelectedObjects

`public void deleteSelectedObjects()`

Deletes the objects selected in the receiver's display group and then sets the receiver's edited state to `true`.

---

### dispose

`public void dispose()`

Conformance to NSDisposable. See the method description of __dispose__ in the interface specification for NSDisposable.

---

### editability

`public int editability()`

Conformance to [EOEditable](EOEditable.md#apple-inducskdinbeg). See the method description of [editability](EOEditable.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivsgs5dbmjwgkl3fmruxiylcnfwgs5dz) in the interface specification for EOEditable.

---

### handleEditingContextNotification

`public void handleEditingContextNotification(NSNotification notification)`

See the method description for [handleEditingContextNotification](EOEntityController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupfbw63tuojxwy3dfoixwqylomrwgkrlenf2gs3thinxw45dfpb2e433unftgsy3boruw63q) in the EOEntityController class specification. EODocumentController's implementation additionally updates its edited state if the receiver is a root document controller.

---

### insertObject

`public void insertObject()`

Creates a new enterprise object, inserts it into the receiver's display group, and sets the receiver's edited status to `true`.

---

### isDocumentForGlobalID

`public boolean isDocumentForGlobalID( com.webobjects.eocontrol.EOGlobalID globalID, String entityName)`

Conformance to [EODocument](EODocument.md#apple-ijbesskjifdeg). See the method description of [isDocumentForGlobalID](EODocument.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpirxwg5lnmvxhil3joncg6y3vnvsw45cgn5zeo3dpmjqwyske) in the interface specification for EODocument.

---

### isEditable

`public boolean isEditable()`

Conformance to [EOEditable](EOEditable.md#apple-inducskdinbeg). See the method description of [isEditable](EOEditable.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivsgs5dbmjwgkl3joncwi2lumfrgyzi) in the interface specification for EOEditable.

---

### isEdited

`public boolean isEdited()`

Conformance to [EODocument](EODocument.md#apple-ijbesskjifdeg). See the method description of [isEdited](EODocument.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpirxwg5lnmvxhil3joncwi2lumvsa) in the interface specification for EODocument.

---

### isRootDocumentController

`public boolean isRootDocumentController()`

Returns `true` if none of the supercontrollers are [EODocument](EODocument.md#apple-ijbesskjifdeg)s, `false` otherwise.

---

### prepareForNewTask

`public void prepareForNewTask(boolean flag)`

See the method description for [prepareForNewTask](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5yhezlqmfzgkrtpojhgk52umfzww) in the EOController class specification. EODocumentController's implementation additionally sets its edited state to `false`.

---

### redo

`public void redo()`

Tells the receiver's editing context to redo.

---

### revert

`public boolean revert()`

Reverts the receiver's unsaved changes upon user confirmation. If the receiver has been edited, opens a dialog to verify that the user wants to revert. Upon confirmation, invokes [revertChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3smv3gk4tuinugc3thmvzq) requesting an error dialog upon failure. Returns `true` on success, `false` upon failure or if the user cancels the revert.

---

### revertAndMakeInvisible

`public boolean revertAndMakeInvisible()`

Reverts the receiver's unsaved changes and makes the receiver invisible. Reverts by invoking [revertChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3smv3gk4tuinugc3thmvzq), requesting an error dialog upon failure Returns `true` if changes are successfully reverted, `false` if the receiver can't be reverted or if the revert fails.

---

### revertChanges

`public boolean revertChanges(boolean showErrorDialog)`

Tells the receiver's editing context to revert, refetches if necessary, and sets the receiver's editing state to `false`. If the revert fails, catches the exception and, if _showErrorDialog_ is true, invokes __revertFailed__ to show the reason for failure. Returns `true` if the revert succeeds, `false` otherwise.

---

### revertFailed

`protected void revertFailed( Exception exception, boolean showErrorDialog)`

If _showErrorDialog_ is `true`, brings the receiver's user interface to the front and opens a dialog displaying _exception_'s class name and exception message. Invoked from [revertChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3smv3gk4tuinugc3thmvzq).

---

### save

`public boolean save()`

Saves the receiver's changes. Saves by invoking __saveChanges__, requesting an error dialog upon failure Returns `true` if changes are successfully saved, `false` if the receiver can't save or if the save fails.

---

### saveAndMakeInvisible

`public boolean saveAndMakeInvisible()`

Saves the receiver's changes and makes the receiver invisible. Saves by invoking [saveChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3tmf3gkq3imfxgozlt), requesting an error dialog upon failure Returns `true` if changes are successfully reverted, `false` if the receiver can't be reverted or if the revert fails.

---

### saveChanges

`public boolean saveChanges( boolean showErrorDialog, String saveOperationTitle)`

Tells the receiver's editing context to save changes and sets the receiver's editing state to `false`. If the save fails, catches the exception and, if _showErrorDialog_ is true, invokes __saveFailed__ to show the reason for failure. Returns `true` if the save succeeds, `false` otherwise.

---

### saveFailed

`protected void saveFailed( Exception showErrorDialog, boolean showErrorDialog, String saveOperationTitle)`

If _showErrorDialog_ is `true`, brings the receiver's user interface to the front and opens a dialog displaying _exception_'s class name and exception message. Invoked from __saveChanges__.

---

### saveIfUserConfirms

`public boolean saveIfUserConfirms( String operationTitle, String message)`

`public boolean saveIfUserConfirms()`

Saves the receiver's unsaved changes upon user confirmation. If the receiver has been edited, opens a dialog to verify that the user wants to save. If _operationTitle_ and _message_ are provided, they are used as the dialog title and message; otherwise, "Save" and "Save Changes?" are used. Upon confirmation, invokes __saveChanges__ requesting an error dialog upon failure. Returns `true` on success, `false` upon failure or if the user cancels the save.

---

### saveIfUserConfirmsAndMakeInvisible

`public boolean saveIfUserConfirmsAndMakeInvisible( String operationTitle, String message)`

`public boolean saveIfUserConfirmsAndMakeInvisible()`

Saves the receiver's unsaved changes upon user confirmation and makes the receiver invisible. Saves by invoking __saveIfUserConfirms__, requesting an error dialog upon failure. The arguments _operationTitle_ and _message_ are used as the title and message of the confirmation panel. "Save" and "Save changes?" are substituted for `null`. If the no-argument form of this method is invoked, then the title of the confirmation dialog is "Close" and the dialog has no message. Returns `true` if changes are successfully saved, `false` if the receiver can't be saved or if the save fails.

---

### setEditability

`public void setEditability(int editability)`

Conformance to [EOEditable](EOEditable.md#apple-inducskdinbeg). See the method description of [setEditability](EOEditable.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivsgs5dbmjwgkl3tmv2ekzdjorqwe2lmnf2hs) in the interface specification for EOEditable.

---

### setEdited

`public void setEdited(boolean flag)`

Conformance to [EODocument](EODocument.md#apple-ijbesskjifdeg). See the method description of [setEdited](EODocument.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpirxwg5lnmvxhil3tmv2ekzdjorswi) in the interface specification for EODocument.

---

### supercontrollerEditabilityDidChange

`public void supercontrollerEditabilityDidChange()`

Conformance to [EOEditable](EOEditable.md#apple-inducskdinbeg). See the method description of [supercontrollerEditabilityDidChange](EOEditable.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivsgs5dbmjwgkl3tovygk4tdn5xhi4tpnrwgk4sfmruxiylcnfwgs5dziruwiq3imfxgozi) in the interface specification for EOEditable. EODocumentController's implementation updates the receiver's editability and resets its actions.

---

### takeResponsibilityForEditabilityOfAssociation

`public void takeResponsibilityForEditabilityOfAssociation( com.webobjects.eointerface.EOAssociation association)`

Conformance to [EOEditable](EOEditable.md#apple-inducskdinbeg). See the method description of [takeResponsibilityForEditabilityOfAssociation](EOEditable.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivsgs5dbmjwgkl3umfvwkutfonyg63ttnfrgs3djor4um33sivsgs5dbmjuwy2lupfhwmqltonxwg2lboruw63q) in the interface specification for EOEditable.

---

### toString

`public String toString()`

Returns the receiver as a string, including the receiver's editability and whether or not it has unsaved edits.

---

### undo

`public void undo()`

Tells the receiver's editing context to redo.

---

### wasEdited

`protected void wasEdited()`

Invoked from [setEdited](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirxwg5lnmvxhiq3pnz2he33mnrsxel3tmv2ekzdjorswi) to notify the receiver that edited status has changed, giving the receiver the opportunity to respond.

---

© 2001 Apple Computer, Inc. (Last Published April 14, 2001)

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
