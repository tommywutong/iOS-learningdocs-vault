---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOApplication.framework/Java/Classes/EOAction.html
archived_at: '2026-07-15T08:11:36.130843Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOApplication Reference

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

# EOAction

> **__Inherits
> from:__**
> : javax.swing.AbstractAction

> **__Package:__**
> : com.apple.client.eoapplication

---

## Class Description

---

EOAction objects are
abstract representations of operations the user can invoke from
the user interface. An action does not specify how it appears in
the user interface-it can appear as a button, a menu item, or
both.

Each action defines a method called the action name, that
is invoked when the action triggers. An action also has a description
path, which describes the category of the action and its name. For
example, a Quit action's description path might be `"Document/Quit"`.
In addition, the action can have a short description that differs
from the last element of the description path, for example, `"Quit
the Application"`.

Actions can have icons for buttons in the application and
small icons for minor buttons in the user interface. To allow users
to trigger actions with "hot-keys," each action has a menu accelerator,
a javax.swing.KeyStroke the user can type
on the keyboard.

Actions often appear in groups in the user interface: buttons
in the same group are rendered close together and menu items in
the group are rendered in separate menus like the Document, Edit,
Tools, or Window menus. To group actions, EOAction defines
a category priority. All actions in the same group have the same
category priority. An additional parameter, the action priority
defines the order in which actions appear within a group (for example,
the order menu items appear within a menu).

An action triggers when the user clicks the corresponding
user interface widget. In most cases, the action's method is dispatched
to the subcontrollers of the controller that displays the action.
Methods whose names end with __...ForControllerHierarchy__ return
such actions. In some cases, the action's method is dispatched
to the active widget, like the text field containing the cursor.
Methods whose names end with __...ForFocusComponent__ return
such actions. In other cases, the action's method is dispatched
to a particular object, usually the EOApplication at
the root of the controller hierarchy.

EOAction defines methods to create actions, access an action's
parameters, manage groups of actions, and accessing shared actions
used in Direct to Java Client applications.

## Method Types

---

> **Accessing action parameters**
> : [actionName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4ttbnvsq)
> : [actionPriority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4udsnfxxe2lupe)
> : [actionTitle](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4vdjorwgk)
> : [categoryPriority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwgylumvtw64tzkbzgs33snf2hs)
> : [descriptionPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwizltmnzgs4dunfxw4udborua)
> : [descriptionPathComponents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwizltmnzgs4dunfxw4udborueg33nobxw4zloorzq)
> : [icon](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwsy3pny)
> : [menuAccelerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxw2zloovawgy3fnrsxeylun5za)
> : [setActionName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxgzluifrxi2lpnzhgc3lf)
> : [setActionPriority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxgzluifrxi2lpnzihe2lpojuxi6i)
> : [setCategoryPriority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxgzluinqxizlhn5zhsudsnfxxe2lupe)
> : [setDescriptionPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxgzluirsxgy3snfyhi2lpnzigc5di)
> : [setIcon](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxgzlujfrw63q)
> : [setMenuAccelerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxgzlujvsw45kbmnrwk3dfojqxi33s)
> : [setShortDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxgzluknug64tuirsxgy3snfyhi2lpny)
> : [setSmallIcon](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxgzluknwwc3dmjfrw63q)
> : [shortDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxg2dpoj2eizltmnzgs4dunfxw4)
> : [smallIcon](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxg3lbnrwesy3pny)
>
> **Creating actions**
> : [EOAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxukt2bmn2gs33o)
> : [actionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpmfrxi2lpnzdg64sdn5xhi4tpnrwgk4sinfsxeylsmnuhs)
> : [actionForFocusComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpmfrxi2lpnzdg64sgn5rxk42dn5wxa33omvxhi)
> : [actionForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpmfrxi2lpnzdg64spmjvgky3u)
> : [standardActionForFocusComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgiqldoruw63sgn5zem33dovzug33nobxw4zlooq)
> : [standardDocumentActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgirdpmn2w2zloorawg5djn5xem33sinxw45dsn5wgyzlsjbuwk4tbojrwq6i)
> : [standardDocumentActionForApplication](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgirdpmn2w2zloorawg5djn5xem33sifyha3djmnqxi2lpny)
> : [standardDocumentActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgirdpmn2w2zloorawg5djn5xem33sinxw45dsn5wgyzlsjbuwk4tbojrwq6i)
> : [standardEditActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgirlenf2ecy3unfxw4rtpojbw63tuojxwy3dfojegszlsmfzgg2dz)
>
> **Creating menu accelerators**
> : [keyStrokeWithKeyCode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpnnsxsu3uojxwwzkxnf2gqs3fpfbw6zdf)
> : [keyStrokeWithKeyCodeAndModifiers](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpnnsxsu3uojxwwzkxnf2gqs3fpfbw6zdfifxgitlpmruwm2lfojzq)
> : [keyStrokeWithKeyCodeAndShiftModifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpnnsxsu3uojxwwzkxnf2gqs3fpfbw6zdfifxgiu3infthitlpmruwm2lfoi)
> : [keyStrokeWithString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpnnsxsu3uojxwwzkxnf2gqu3uojuw4zy)
>
> **Accessing specific shared
> actions**
> : [standardActivatePreviousWindowActionForApplication](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgiqldoruxmylumvihezlwnfxxk42xnfxgi33xifrxi2lpnzdg64sbobygy2ldmf2gs33o)
> : [standardAddActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgiqlemrawg5djn5xem33sinxw45dsn5wgyzlsjbuwk4tbojrwq6i)
> : [standardAppendActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgiqlqobsw4zcbmn2gs33oizxxeq3pnz2he33mnrsxesdjmvzgc4tdnb4q)
> : [standardCancelActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgiq3bnzrwk3cbmn2gs33oizxxeq3pnz2he33mnrsxesdjmvzgc4tdnb4q)
> : [standardClearActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgiq3mmvqxeqldoruw63sgn5zeg33oorzg63dmmvzeq2lfojqxey3ipe)
> : [standardCloseWindowActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgiq3mn5zwkv3jnzsg652bmn2gs33oizxxeq3pnz2he33mnrsxesdjmvzgc4tdnb4q)
> : [standardDeleteActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgirdfnrsxizkbmn2gs33oizxxeq3pnz2he33mnrsxesdjmvzgc4tdnb4q)
> : [standardDeselectActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgirdfonswyzldorawg5djn5xem33sinxw45dsn5wgyzlsjbuwk4tbojrwq6i)
> : [standardEditActionsForFocusComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgirlenf2ecy3unfxw442gn5zem33dovzug33nobxw4zlooq)
> : [standardFindActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgirtjnzsecy3unfxw4rtpojbw63tuojxwy3dfojegszlsmfzgg2dz)
> : [standardInsertActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgisloonsxe5cbmn2gs33oizxxeq3pnz2he33mnrsxesdjmvzgc4tdnb4q)
> : [standardInsertWithTaskActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgisloonsxe5cxnf2gqvdbonvucy3unfxw4rtpojbw63tuojxwy3dfojegszlsmfzgg2dz)
> : [standardOkActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgit3lifrxi2lpnzdg64sdn5xhi4tpnrwgk4sinfsxeylsmnuhs)
> : [standardOkAndSaveActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgit3lifxgiu3bozsucy3unfxw4rtpojbw63tuojxwy3dfojegszlsmfzgg2dz)
> : [standardOpenWithTaskActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgit3qmvxfo2lunbkgc43lifrxi2lpnzdg64sdn5xhi4tpnrwgk4sinfsxeylsmnuhs)
> : [standardQuitActionForApplication](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgiulvnf2ecy3unfxw4rtpojaxa4dmnfrwc5djn5xa)
> : [standardRedoActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgiutfmrxucy3unfxw4rtpojbw63tuojxwy3dfojegszlsmfzgg2dz)
> : [standardRefreshActionForApplication](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgiutfmzzgk43iifrxi2lpnzdg64sbobygy2ldmf2gs33o)
> : [standardRemoveActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgiutfnvxxmzkbmn2gs33oizxxeq3pnz2he33mnrsxesdjmvzgc4tdnb4q)
> : [standardRevertActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgiutfozsxe5cbmn2gs33oizxxeq3pnz2he33mnrsxesdjmvzgc4tdnb4q)
> : [standardSaveActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgiu3bozsucy3unfxw4rtpojbw63tuojxwy3dfojegszlsmfzgg2dz)
> : [standardSaveAllActionForApplication](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgiu3bozsuc3dmifrxi2lpnzdg64sbobygy2ldmf2gs33o)
> : [standardSelectActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgiu3fnrswg5cbmn2gs33oizxxeq3pnz2he33mnrsxesdjmvzgc4tdnb4q)
> : [standardUndoActionForControllerHierarchy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpon2gc3temfzgivlomrxucy3unfxw4rtpojbw63tuojxwy3dfojegszlsmfzgg2dz)
>
> **Managing actions**
> : [actionCanBePerformedInContextOfController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4q3bnzbgkudfojtg64tnmvses3sdn5xhizlyorhwmq3pnz2he33mnrsxe)
> : [actionPerformed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4udfojtg64tnmvsa)
> : [mergedActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpnvsxez3fmrawg5djn5xhg)
> : [sortedActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rponxxe5dfmrawg5djn5xhg)
>
> **Managing the property
> change listener**
> : [addPropertyChangeListener](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwczdekbzg64dfoj2hsq3imfxgozkmnfzxizlomvza)
> : [firePropertyChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwm2lsmvihe33qmvzhi6kdnbqw4z3f)
> : [removePropertyChangeListener](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxezlnn53gkudsn5ygk4tupfbwqylom5suy2ltorsw4zls)
>
> **Methods inherited from
> Object**
> : [equals](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwk4lvmfwhg)
> : [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxi32torzgs3th)

## Constructors

---

### EOAction

`public EOAction(
String actionName,
String descriptionPath,
String shortDescription,
javax.swing.Icon icon,
javax.swing.Icon smallIcon,
javax.swing.KeyStroke menuAccelerator,
int categoryPriority,
int actionPriority)`

Returns a
new action (an EOAction object) as specified
by the arguments.

__See Also:__  [actionName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4ttbnvsq), [descriptionPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwizltmnzgs4dunfxw4udborua), [shortDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxg2dpoj2eizltmnzgs4dunfxw4), [icon](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwsy3pny), [smallIcon](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxg3lbnrwesy3pny), [menuAccelerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxw2zloovawgy3fnrsxeylun5za), [categoryPriority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwgylumvtw64tzkbzgs33snf2hs), and [actionPriority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4udsnfxxe2lupe).

---

## Static Methods

---

### actionForControllerHierarchy

`public static EOAction actionForControllerHierarchy(
String actionName,
String descriptionPath,
String shortDescription,
javax.swing.Icon icon,
javax.swing.Icon smallIcon,
javax.swing.KeyStroke menuAccelerator,
int categoryPriority,
int actionPriority,
boolean sendsActionToAllControllers)`

Returns a
new action (an EOAction object) as specified
by the arguments. When this action triggers, it is dispatched to
the subcontrollers of the controller that displays it. If _sendsActionToAllControllers_ is `true`,
the action is dispatched to the subcontrollers of the controller
that displays the action. Otherwise, the action is dispatched to
the first subcontroller that responds to it.

__See
Also:__  [EOAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxukt2bmn2gs33o), [actionName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4ttbnvsq), [descriptionPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwizltmnzgs4dunfxw4udborua), [shortDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxg2dpoj2eizltmnzgs4dunfxw4), [icon](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwsy3pny), [smallIcon](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxg3lbnrwesy3pny), [menuAccelerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxw2zloovawgy3fnrsxeylun5za), [categoryPriority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwgylumvtw64tzkbzgs33snf2hs), and [actionPriority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4udsnfxxe2lupe).

---

### actionForFocusComponent

`public static EOAction actionForFocusComponent(
String actionName,
String descriptionPath,
String shortDescription,
javax.swing.Icon icon,
javax.swing.Icon smallIcon,
javax.swing.KeyStroke menuAccelerator,
int categoryPriority,
int actionPriority)`

Returns a new action (an EOAction object)
as specified by the arguments. When this action triggers, it is
dispatched to the active widget (for example, the text field containing
the cursor). The other parameters are identical to the EOAction constructor
parameters.

__See Also:__  [EOAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxukt2bmn2gs33o), [actionName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4ttbnvsq), [descriptionPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwizltmnzgs4dunfxw4udborua), [shortDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxg2dpoj2eizltmnzgs4dunfxw4), [icon](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwsy3pny), [smallIcon](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxg3lbnrwesy3pny), [menuAccelerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxw2zloovawgy3fnrsxeylun5za), [categoryPriority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwgylumvtw64tzkbzgs33snf2hs), and [actionPriority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4udsnfxxe2lupe).

---

### actionForObject

`public static EOAction actionForObject(
String actionName,
String descriptionPath,
String shortDescription,
javax.swing.Icon icon,
javax.swing.Icon smallIcon,
javax.swing.KeyStroke menuAccelerator,
int categoryPriority,
int actionPriority,
Object object)`

Returns a
new action (an EOAction object) as specified
by the arguments. When this action triggers, it is dispatched directly
to _object_. To create an action that
gets dispatched to the application, set _object_ to
the EOApplication at the top of the controller
hierarchy. The other parameters are identical to the EOAction constructor
parameters.

__See Also:__  [EOAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxukt2bmn2gs33o), [actionName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4ttbnvsq), [descriptionPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwizltmnzgs4dunfxw4udborua), [shortDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxg2dpoj2eizltmnzgs4dunfxw4), [icon](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwsy3pny), [smallIcon](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxg3lbnrwesy3pny), [menuAccelerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxw2zloovawgy3fnrsxeylun5za), [categoryPriority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwgylumvtw64tzkbzgs33snf2hs), and [actionPriority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4udsnfxxe2lupe).

---

### keyStrokeWithKeyCode

`public static javax.swing.KeyStroke keyStrokeWithKeyCode(int keyCode)`

Returns a KeyStroke given
the numerical key code _keyCode_ with
the appropriate modifier for the client operating system (usually `CTRL_MASK`).
See Sun's javax.swing.KeyStroke documentation
for more information.

---

### keyStrokeWithKeyCodeAndModifiers

`public static javax.swing.KeyStroke keyStrokeWithKeyCodeAndModifiers(
int keyCode,
int modifiers)`

Returns a KeyStroke given
the numerical key code _keyCode_ and
the modifier mask _modifiers_. This method
adds the appropriate modifier for the client operating system (usually `CTRL_MASK`).
See Sun's javax.swing.KeyStroke documentation
for more information.

---

### keyStrokeWithKeyCodeAndShiftModifier

`public static javax.swing.KeyStroke keyStrokeWithKeyCodeAndShiftModifier(int keyCode)`

Returns a KeyStroke given
the numerical key code _keyCode_ with
the SHIFT modifier. This method also adds the appropriate modifier
for the client operating system (usually `CTRL_MASK`).
See Sun's javax.swing.KeyStroke documentation
for more information.

---

### keyStrokeWithString

`public static javax.swing.KeyStroke keyStrokeWithString(String keyStrokeDescription)`

Returns a
KeyStroke for the String _keyStrokeDescription_.
This method adds the appropriate modifier for the client operating
system (usually `CTRL_MASK`).
See Sun's javax.swing.KeyStroke documentation
for more information.

---

### mergedActions

`public static NSArray mergedActions(
NSArray actionArray1,
NSArray actionArray2)`

Returns an
NSArray containing all of the actions in _actionArray1_ and _actionArray2_ with
duplicate actions removed.

---

### sortedActions

`public static NSArray sortedActions(NSArray actionArray)`

Returns a
sorted NSArray containing the actions in _actionArray_.
The actions are sorted first on the category priority, then on the
action priority, and finally on the description path.

__See
Also:__  [categoryPriority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwgylumvtw64tzkbzgs33snf2hs), [actionPriority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4udsnfxxe2lupe), and [descriptionPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwizltmnzgs4dunfxw4udborua).

---

### standardActionForFocusComponent

`public static EOAction standardActionForFocusComponent(
String actionName,
javax.swing.KeyStroke menuAccelerator,
int actionPriority)`

Returns a
shared action as specified by the arguments. When the action triggers,
it is dispatched to the focus component (for example, a text field).
The action's category priority is the edit action priority so the
action is grouped with the other edit actions.

__See
Also:__  [actionName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4ttbnvsq), [menuAccelerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxw2zloovawgy3fnrsxeylun5za), and [actionPriority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4udsnfxxe2lupe).

---

### standardActivatePreviousWindowActionForApplication

`public static EOAction standardActivatePreviousWindowActionForApplication()`

Returns a
shared action (an EOAction object) for the __activatePreviousWindow__ method.
When this action triggers, it is dispatched to the EOApplication at
the top of the controller hierarchy. The action's category priority
is the window action priority so the action is grouped with the
other window actions. This action appears as the Activate Previous
Window item in the Window menu in Direct to Java Client applications.

---

### standardAddActionForControllerHierarchy

`public static EOAction standardAddActionForControllerHierarchy()`

Returns a shared action (an EOAction object)
for the __add__ method. When the action triggers,
it is dispatched to the subcontrollers of the controller that displays
it. The action's category priority is the document action priority
so the action is grouped with the other document actions.

---

### standardAppendActionForControllerHierarchy

`public static EOAction standardAppendActionForControllerHierarchy()`

Returns a
shared action (an EOAction object) for the __append__ method.
When the action triggers, it is dispatched to the subcontrollers
of the controller that displays it. The action's category priority
is the edit action priority so the action is grouped with the other
edit actions.

---

### standardCancelActionForControllerHierarchy

`public static EOAction standardCancelActionForControllerHierarchy()`

Returns a
shared action (an EOAction object) for the __cancel__ method.
When the action triggers, it is dispatched to the subcontrollers
of the controller that displays it. The action's category priority
is the modal dialog action priority so the action is grouped with
the other modal dialog actions.

---

### standardClearActionForControllerHierarchy

`public static EOAction standardClearActionForControllerHierarchy()`

Returns a
shared action (an EOAction object) for the __clear__ method.
When the action triggers, it is dispatched to the subcontrollers
of the controller that displays it. The action's category priority
is the edit action priority so the action is grouped with the other
edit actions.

---

### standardCloseWindowActionForControllerHierarchy

`public static EOAction standardCloseWindowActionForControllerHierarchy()`

Returns a
shared action (an EOAction object) for the __close__ method.
When the action triggers, it is dispatched to the subcontrollers
of the controller that displays it. The action's category priority
is the window action priority so the action is grouped with the
other window actions.

---

### standardDeleteActionForControllerHierarchy

`public static EOAction standardDeleteActionForControllerHierarchy()`

Returns a shared action (an EOAction object)
for the __delete__ method. When the action
triggers, it is dispatched to the subcontrollers of the controller
that displays it. The action's category priority is the document
action priority so the action is grouped with the other document
actions.

---

### standardDeselectActionForControllerHierarchy

`public static EOAction standardDeselectActionForControllerHierarchy()`

Returns a
shared action (an EOAction object) for the __deselect__ method.
When the action triggers, it is dispatched to the subcontrollers
of the controller that displays it. The action's category priority
is the document action priority so the action is grouped with the
other document actions.

---

### standardDocumentActionForApplication

`public static EOAction standardDocumentActionForApplication(
String actionName,
javax.swing.KeyStroke menuAccelerator,
int actionPriority)`

Returns a
shared action with the method name _actionName_,
menu accelerator _menuAccelerator_,
and action priority _actionPriority_.
When this action triggers, it is dispatched to the EOApplication at
the top of the controller hierarchy. The action's category priority
is the document action priority so the action is grouped with the
other document actions.

---

### standardDocumentActionForControllerHierarchy

`public static EOAction standardDocumentActionForControllerHierarchy(
String actionName,
javax.swing.KeyStroke menuAccelerator,
int actionPriority)`

Returns a
shared action with the method name _actionName_,
menu accelerator _menuAccelerator_,
and action priority _actionPriority_.
When the action triggers, it is dispatched to the subcontrollers
of the controller that displays it. The action's category priority
is the document action priority so the action is grouped with the
other document actions.

---

### standardDocumentActionForControllerHierarchy

`public static EOAction standardDocumentActionForControllerHierarchy(
String actionName,
String baseTitle,
javax.swing.KeyStroke menuAccelerator,
int actionPriority)`

Returns a
shared action as specified by the arguments. The _baseTitle_ parameter
is the name of the action as it appears in the user interface and
is used for both the short description and the action title. When
the action triggers, it is dispatched to the subcontrollers of the
controller that displays it. The action's category priority is
the document action priority so the action is grouped with the other document
actions.

__See Also:__  [actionName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4ttbnvsq), [actionTitle](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4vdjorwgk), [shortDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxg2dpoj2eizltmnzgs4dunfxw4), [menuAccelerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxw2zloovawgy3fnrsxeylun5za), and [actionPriority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4udsnfxxe2lupe).

---

### standardEditActionForControllerHierarchy

`public static EOAction standardEditActionForControllerHierarchy(
String actionName,
javax.swing.KeyStroke menuAccelerator,
int actionPriority)`

Returns a
shared action as specified by the arguments. When the action triggers,
it is dispatched to the subcontrollers of the controller that displays
it. The action's category priority is the edit action priority so
the action is grouped with the other edit actions.

__See
Also:__  [actionName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4ttbnvsq), [menuAccelerator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxw2zloovawgy3fnrsxeylun5za), and [actionPriority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4udsnfxxe2lupe).

---

### standardEditActionsForFocusComponent

`public static NSArray standardEditActionsForFocusComponent()`

Returns an NSArray containing
shared actions for the __cut__, __copy__,
and __paste__ methods. When these actions trigger,
they are dispatched to the focus component. Sets the category priorities
for the actions to the edit category priority so the actions are
grouped with the other edit actions.

---

### standardFindActionForControllerHierarchy

`public static EOAction standardFindActionForControllerHierarchy()`

Returns a
shared action (an EOAction object) for the __find__ method.
When the action triggers, it is dispatched to the subcontrollers
of the controller that displays it. The action's category priority
is the edit action priority so the action is grouped with the other
edit actions.

---

### standardInsertActionForControllerHierarchy

`public static EOAction standardInsertActionForControllerHierarchy()`

Returns a
shared action (an EOAction object) for the __insertWithTask__ method.
When the action triggers, it is dispatched to the subcontrollers
of the controller that displays it. The action's category priority
is the document action priority so the action is grouped with the
other document actions.

---

### standardInsertWithTaskActionForControllerHierarchy

`public static EOAction standardInsertWithTaskActionForControllerHierarchy()`

Returns a
shared action (an EOAction object) for the __insertWithTask__ method.
When the action triggers, it is dispatched to the subcontrollers
of the controller that displays it. The action's category priority
is the document action priority so the action is grouped with the
other document actions.

---

### standardOkActionForControllerHierarchy

`public static EOAction standardOkActionForControllerHierarchy()`

Returns a
shared action (an EOAction object) for an
OK button in a modal dialog box. When the action triggers, it is
dispatched to the subcontrollers of the controller that displays
it. The action's category priority is the modal dialog action
priority so the action is grouped with the other modal dialog actions.

---

### standardOkAndSaveActionForControllerHierarchy

`public static EOAction standardOkAndSaveActionForControllerHierarchy()`

Returns a
shared action (an EOAction object) for an
OK and Save button in a modal dialog box. When the action triggers,
it is dispatched to the subcontrollers of the controller that displays
it. The action's category priority is the modal dialog action
priority so the action is grouped with the other modal dialog actions.

---

### standardOpenWithTaskActionForControllerHierarchy

`public static EOAction standardOpenWithTaskActionForControllerHierarchy()`

Returns a
shared action (an EOAction object) for the __openWithTask__ method.
When the action triggers, it is dispatched to the subcontrollers
of the controller that displays it. The action's category priority
is the document action priority so the action is grouped with the
other document actions.

---

### standardQuitActionForApplication

`public static EOAction standardQuitActionForApplication()`

Returns a
shared action (an EOAction object) for the __quit__ method.
When this action triggers, it is dispatched to the EOApplication at
the top of the controller hierarchy. The action's category priority
is the document action priority so the action is grouped with the
other document actions.

---

### standardRedoActionForControllerHierarchy

`public static EOAction standardRedoActionForControllerHierarchy()`

Returns a shared action (an EOAction object)
for the __redo__ method. When the action triggers,
it is dispatched to the subcontrollers of the controller that displays
it. The action's category priority is the edit action priority
so the action is grouped with the other edit actions.

---

### standardRefreshActionForApplication

`public static EOAction standardRefreshActionForApplication()`

Returns a
shared action (an EOAction object) for the __refresh__ method.
When this action triggers, it is dispatched to the EOApplication at
the top of the controller hierarchy. The action's category priority
is the document action priority so the action is grouped with the
other document actions.

---

### standardRemoveActionForControllerHierarchy

`public static EOAction standardRemoveActionForControllerHierarchy()`

The action's category priority
is the document action priority so the action is grouped with the
other document actions.Returns a shared action
(an EOAction object) for the __remove__ method.
When the action triggers, it is dispatched to the subcontrollers
of the controller that displays it.

---

### standardRevertActionForControllerHierarchy

`public static EOAction standardRevertActionForControllerHierarchy()`

Returns a shared action (an EOAction object)
for the __revert__ method. When the action
triggers, it is dispatched to the subcontrollers of the controller
that displays it. The action's category priority is the document
action priority so the action is grouped with the other document
actions.

---

### standardSaveActionForControllerHierarchy

`public static EOAction standardSaveActionForControllerHierarchy()`

Returns a
shared action (an EOAction object) for the __save__ method.
When the action triggers, it is dispatched to the subcontrollers
of the controller that displays it. The action's category priority
is the document action priority so the action is grouped with the
other document actions.

---

### standardSaveAllActionForApplication

`public static EOAction standardSaveAllActionForApplication()`

Returns a shared action (an EOAction object)
for the __saveAll__ method. When this action
triggers, it is dispatched to the EOApplication at
the top of the controller hierarchy. The action's category priority
is the document action priority so the action is grouped with the
other document actions.

---

### standardSelectActionForControllerHierarchy

`public static EOAction standardSelectActionForControllerHierarchy()`

Returns a shared action (an EOAction object)
for the __select__ method. When the action
triggers, it is dispatched to the subcontrollers of the controller
that displays it. The action's category priority is the document
action priority so the action is grouped with the other document
actions.

---

### standardUndoActionForControllerHierarchy

`public static EOAction standardUndoActionForControllerHierarchy()`

Returns a
shared action (an EOAction object) for the __undo__ method.
When the action triggers, it is dispatched to the subcontrollers
of the controller that displays it. The action's category priority
is the edit action priority so the action is grouped with the other
edit actions.

---

## Instance Methods

---

### actionCanBePerformedInContextOfController

`public boolean actionCanBePerformedInContextOfController(EOController controller)`

Returns whether
or not an action can trigger, which depends on the state of controllers
in the controller hierarchy. For example, a Save action for an unedited
document can not trigger.

---

### actionName

`public String actionName()`

Returns the
name of the method that executes when the receiver triggers.

---

### actionPerformed

`public void actionPerformed(java.awt.event.ActionEvent actionEvent)`

This method
is called when an action is triggered, that is, the user presses
the action's button or selects its menu item.

---

### actionPriority

`public int actionPriority()`

Returns the
receiver's action priority, which determines the order in which
its button or menu item appears within a category.

__See
Also:__  [categoryPriority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwgylumvtw64tzkbzgs33snf2hs)

---

### actionTitle

`public String actionTitle()`

Returns the
receiver's title, the last component of the receiver's description
path.

---

### addPropertyChangeListener

`public void addPropertyChangeListener(java.beans.PropertyChangeListener listener)`

See the method
description for __addPropertyChangeListener__ in
Sun's documentation for javax.swing.AbstractAction.

---

### categoryPriority

`public int categoryPriority()`

Returns the
receiver's category priority, which determines the order in which
the group of buttons or menu items that contains the receiver appears.

---

### descriptionPath

`public String descriptionPath()`

Returns the
receiver's menu hierarchy path. For example, the Quit menu item
description path is `Document/Quit`.

---

### descriptionPathComponents

`public NSArray descriptionPathComponents()`

Returns an NSArray containing
the separate components of the receiver's menu hierarchy path.

---

### equals

`public boolean equals(Object anObject)`

Indicates
whether some object "is equal to" this one.

---

### firePropertyChange

`protected void firePropertyChange(
String propertyName,
Object oldValue,
Object newValue)`

See the method
description for __firePropertyChange__ in Sun's
documentation for javax.swing.AbstractAction.

---

### icon

`public javax.swing.Icon icon()`

Returns the
receiver's icon.

---

### menuAccelerator

`public javax.swing.KeyStroke menuAccelerator()`

Returns the
KeyStroke the user can type to invoke the receiver instead of selecting
it from the menu.

---

### removePropertyChangeListener

`public void removePropertyChangeListener(java.beans.PropertyChangeListener listener)`

See the method
description for __removePropertyChangeListener__ in
Sun's documentation for javax.swing.AbstractAction.

---

### setActionName

`public void setActionName(String actionName)`

Sets the
name of the method that executes when the receiver triggers.

---

### setActionPriority

`public void setActionPriority(int actionPriority)`

Sets the
receiver's action priority, which determines the order in which
its button or menu item appears within a category.

---

### setCategoryPriority

`public void setCategoryPriority(int categoryPriority)`

Returns the
receiver's category priority, which determines the order in which
the group of buttons or menu items containing the receiver appears.

---

### setDescriptionPath

`public void setDescriptionPath(String descriptionPath)`

Sets the
receiver's menu hierarchy path to _descriptionPath_.

---

### setIcon

`public void setIcon(javax.swing.Icon icon)`

Sets the
receiver's icon to _icon_.

---

### setMenuAccelerator

`public void setMenuAccelerator(javax.swing.KeyStroke menuAccelerator)`

Sets the
KeyStroke the user can type to invoke the receiver instead of selecting
it from a menu.

__See Also:__  [keyStrokeWithKeyCode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpnnsxsu3uojxwwzkxnf2gqs3fpfbw6zdf), [keyStrokeWithKeyCodeAndModifiers](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpnnsxsu3uojxwwzkxnf2gqs3fpfbw6zdfifxgitlpmruwm2lfojzq), [keyStrokeWithKeyCodeAndShiftModifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpnnsxsu3uojxwwzkxnf2gqs3fpfbw6zdfifxgiu3infthitlpmruwm2lfoi), and [keyStrokeWithString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qldoruw63rpnnsxsu3uojxwwzkxnf2gqu3uojuw4zy).

---

### setShortDescription

`public void setShortDescription(String shortDescription)`

Sets the action's short description to _shortDescription_.
The short description appears in buttons and menu items. If _shortDescription_ is `null`,
the receiver's title is displayed instead.

__See
Also:__  [actionTitle](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4vdjorwgk)

---

### setSmallIcon

`public void setSmallIcon(javax.swing.Icon anIcon)`

Sets the
receiver's small icon used for some small buttons in the user
interface (the Select button in a Form window's to-one relationship
editor is an example).

---

### shortDescription

`public String shortDescription()`

Returns the
receiver's short description, which is displayed in buttons and
menu items. If the short description is set to `null` or
has not been assigned, __shortDescription__ returns
the action's title.

__See Also:__  [actionTitle](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxwcy3unfxw4vdjorwgk)

---

### smallIcon

`public javax.swing.Icon smallIcon()`

Returns the
receiver's small icon used for some small buttons in the user
interface (the Select button in a Form window's to-one relationship
editor is an example). By default, the small icon is not displayed for
such buttons; the short description is displayed instead.

__See
Also:__  [shortDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnyxxg2dpoj2eizltmnzgs4dunfxw4)

---

### toString

`public String toString()`

Returns the receiver as a string that states
the receiver's method name, description path, category priority,
and action priority.

---

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

__DRAFT__
