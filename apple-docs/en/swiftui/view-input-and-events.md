---
title: Input and event modifiers
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-input-and-events
source_url: 'https://developer.apple.com/documentation/swiftui/view-input-and-events'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-input-and-events.json'
content_hash: 'sha256:185b040d871588d6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [View fundamentals](view-fundamentals.md) · [View](view.md)

# Input and event modifiers

<sub>API Collection</sub>

Supply actions for a view to perform in response to user input and system events.

## Overview

Use input and event modifiers to configure and provide handlers for a wide variety of user inputs or system events. For example, you can detect and control focus, respond to life cycle events like view appearance and disappearance, manage keyboard shortcuts, and much more.

## Topics

### Interactivity

- [disabled(_:)](<view/disabled(__).md>) — Adds a condition that controls whether users can interact with this view.
- [interactionActivityTrackingTag(_:)](<view/interactionactivitytrackingtag(__).md>) — Sets a tag that you use for tracking interactivity.

### List controls

- [swipeActions(edge:allowsFullSwipe:content:)](<view/swipeactions(edge_allowsfullswipe_content_).md>) — Adds custom swipe actions to a row in a list.
- [refreshable(action:)](<view/refreshable(action_).md>) — Adds an asynchronous handler that can update the data the view displays when a person initiates a request, such as by pulling to refresh.
- [selectionDisabled(_:)](<view/selectiondisabled(__).md>) — Adds a condition that controls whether users can select this view.

### Container controls

- [swipeActions(edge:allowsFullSwipe:content:onPresentationChanged:)](<view/swipeactions(edge_allowsfullswipe_content_onpresentationchanged_).md>) — Adds custom swipe actions to a row in a list or container, notifying you when the actions are revealed or dismissed. _(beta)_
- [swipeActionsContainer()](<view/swipeactionscontainer().md>) — Coordinates swipe action dismissal and mutual exclusion across rows in a container. _(beta)_

### Scroll controls

- [scrollPosition(_:anchor:)](<view/scrollposition(__anchor_).md>) — Associates a binding to a scroll position with a scroll view within this view.
- [scrollPosition(id:anchor:)](<view/scrollposition(id_anchor_).md>) — Associates a binding to be updated when a scroll view within this view scrolls.
- [defaultScrollAnchor(_:)](<view/defaultscrollanchor(__).md>) — Associates an anchor to control which part of the scroll view’s content should be rendered by default.
- [defaultScrollAnchor(_:for:)](<view/defaultscrollanchor(__for_).md>) — Associates an anchor to control the position of a scroll view in a particular circumstance.
- [scrollTargetBehavior(_:)](<view/scrolltargetbehavior(__).md>) — Sets the scroll behavior of views scrollable in the provided axes.
- [scrollTargetLayout(isEnabled:)](<view/scrolltargetlayout(isenabled_).md>) — Configures the outermost layout as a scroll target layout.
- [scrollInputBehavior(_:for:)](<view/scrollinputbehavior(__for_).md>) — Enables or disables scrolling in scrollable views when using particular inputs.
- [scrollTransition(_:axis:transition:)](<view/scrolltransition(__axis_transition_).md>) — Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [scrollTransition(topLeading:bottomTrailing:axis:transition:)](<view/scrolltransition(topleading_bottomtrailing_axis_transition_).md>) — Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [onScrollGeometryChange(for:of:action:)](<view/onscrollgeometrychange(for_of_action_).md>) — Adds an action to be performed when a value, created from a scroll geometry, changes.
- [onScrollTargetVisibilityChange(idType:threshold:_:)](<view/onscrolltargetvisibilitychange(idtype_threshold___).md>) — Adds an action to be called with information about what views would be considered visible.
- [onScrollVisibilityChange(threshold:_:)](<view/onscrollvisibilitychange(threshold___).md>) — Adds an action to be called when the view crosses the threshold to be considered on/off screen.
- [onScrollPhaseChange(_:)](<view/onscrollphasechange(__).md>) — Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.

### Geometry

- [onGeometryChange(for:of:action:)](<view/ongeometrychange(for_of_action_).md>) — Adds an action to be performed when a value, created from a geometry proxy, changes.
- [onGeometryChange3D(for:of:action:)](<view/ongeometrychange3d(for_of_action_).md>) — Returns a new view that arranges to call `action(value)` whenever the value computed by `transform(proxy)` changes, where `proxy` provides access to the view’s 3D geometry properties.
- [onInteractiveResizeChange(_:)](<view/oninteractiveresizechange(__).md>) — Adds an action to perform when the enclosing window is being interactively resized.

### Taps and gestures

- [onTapGesture(count:perform:)](<view/ontapgesture(count_perform_).md>) — Adds an action to perform when this view recognizes a tap gesture.
- [onTapGesture(count:coordinateSpace:perform:)](<view/ontapgesture(count_coordinatespace_perform_).md>) — Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [onTapGesture(count:coordinateSpace:inputKinds:perform:)](<view/ontapgesture(count_coordinatespace_inputkinds_perform_).md>) — Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction. _(beta)_
- [onLongPressGesture(minimumDuration:maximumDistance:perform:onPressingChanged:)](<view/onlongpressgesture(minimumduration_maximumdistance_perform_onpressingchanged_).md>) — Adds an action to perform when this view recognizes a long press gesture.
- [onLongPressGesture(minimumDuration:maximumDistance:inputKinds:perform:onPressingChanged:)](<view/onlongpressgesture(minimumduration_maximumdistance_inputkinds_perform_onpressingchanged_).md>) — Adds an action to perform when this view recognizes a long press gesture. _(beta)_
- [onLongPressGesture(minimumDuration:perform:onPressingChanged:)](<view/onlongpressgesture(minimumduration_perform_onpressingchanged_).md>) — Adds an action to perform when this view recognizes a long press gesture.
- [onLongTouchGesture(minimumDuration:perform:onTouchingChanged:)](<view/onlongtouchgesture(minimumduration_perform_ontouchingchanged_).md>) — Adds an action to perform when this view recognizes a remote long touch gesture. A long touch gesture is when the finger is on the remote touch surface without actually pressing.
- [gesture(_:)](<view/gesture(__).md>) — Attaches an [NSGestureRecognizerRepresentable](nsgesturerecognizerrepresentable.md) to the view.
- [gesture(_:isEnabled:)](<view/gesture(__isenabled_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:name:isEnabled:)](<view/gesture(__name_isenabled_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:including:)](<view/gesture(__including_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [highPriorityGesture(_:including:)](<view/highprioritygesture(__including_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:isEnabled:)](<view/highprioritygesture(__isenabled_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:name:isEnabled:)](<view/highprioritygesture(__name_isenabled_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [simultaneousGesture(_:including:)](<view/simultaneousgesture(__including_).md>) — Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [simultaneousGesture(_:isEnabled:)](<view/simultaneousgesture(__isenabled_).md>) — Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [simultaneousGesture(_:name:isEnabled:)](<view/simultaneousgesture(__name_isenabled_).md>) — Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [defersSystemGestures(on:)](<view/deferssystemgestures(on_).md>) — Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [onPencilDoubleTap(perform:)](<view/onpencildoubletap(perform_).md>) — Adds an action to perform after the user double-taps their Apple Pencil.
- [onPencilSqueeze(perform:)](<view/onpencilsqueeze(perform_).md>) — Adds an action to perform when the user squeezes their Apple Pencil.
- [allowsWindowActivationEvents()](<view/allowswindowactivationevents().md>) — Configures gestures in this view hierarchy to handle events that activate the containing window.
- [allowsWindowActivationEvents(_:)](<view/allowswindowactivationevents(__).md>) — Configures whether gestures in this view hierarchy can handle events that activate the containing window.

### Keyboard input

- [onKeyPress(_:action:)](<view/onkeypress(__action_).md>) — Performs an action if the user presses a key on a hardware keyboard while the view has focus.
- [onKeyPress(phases:action:)](<view/onkeypress(phases_action_).md>) — Performs an action if the user presses any key on a hardware keyboard while the view has focus.
- [onKeyPress(_:phases:action:)](<view/onkeypress(__phases_action_).md>) — Performs an action if the user presses a key on a hardware keyboard while the view has focus.
- [onKeyPress(characters:phases:action:)](<view/onkeypress(characters_phases_action_).md>) — Performs an action if the user presses one or more keys on a hardware keyboard while the view has focus.
- [onKeyPress(keys:phases:action:)](<view/onkeypress(keys_phases_action_).md>) — Performs an action if the user presses one or more keys on a hardware keyboard while the view has focus.
- [onModifierKeysChanged(mask:initial:_:)](<view/onmodifierkeyschanged(mask_initial___).md>) — Performs an action whenever the user presses or releases a hardware modifier key.

### Keyboard shortcuts

- [keyboardShortcut(_:)](<view/keyboardshortcut(__).md>) — Assigns a keyboard shortcut to the modified control.
- [keyboardShortcut(_:modifiers:)](<view/keyboardshortcut(__modifiers_).md>) — Defines a keyboard shortcut and assigns it to the modified control.
- [keyboardShortcut(_:modifiers:localization:)](<view/keyboardshortcut(__modifiers_localization_).md>) — Defines a keyboard shortcut and assigns it to the modified control.
- [modifierKeyAlternate(_:_:)](<view/modifierkeyalternate(____).md>) — Builds a view to use in place of the modified view when the user presses the modifier key(s) indicated by the given set.

### Hand interactions

- [handGestureShortcut(_:isEnabled:)](<view/handgestureshortcut(__isenabled_).md>) — Assigns a hand gesture shortcut to the modified control.
- [handPointerBehavior(_:)](<view/handpointerbehavior(__).md>) — Sets the behavior of the hand pointer while the user is interacting with the view.
- [manipulable(coordinateSpace:operations:inertia:isEnabled:onChanged:)](<view/manipulable(coordinatespace_operations_inertia_isenabled_onchanged_).md>) — Allows this view to be manipulated using common hand gestures.
- [manipulable(transform:coordinateSpace:operations:inertia:isEnabled:onChanged:)](<view/manipulable(transform_coordinatespace_operations_inertia_isenabled_onchanged_).md>) — Applies the given 3D affine transform to the view and allows it to be manipulated using common hand gestures.
- [manipulable(using:)](<view/manipulable(using_).md>) — Allows the view to be manipulated using a manipulation gesture attached to a different view.
- [manipulationGesture(updating:coordinateSpace:operations:inertia:isEnabled:onChanged:)](<view/manipulationgesture(updating_coordinatespace_operations_inertia_isenabled_onchanged_).md>) — Adds a manipulation gesture to this view without allowing this view to be manipulable itself.

### Hover

- [onHover(perform:)](<view/onhover(perform_).md>) — Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [onContinuousHover(coordinateSpace:perform:)](<view/oncontinuoushover(coordinatespace_perform_).md>) — Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
- [hoverEffect(_:)](<view/hovereffect(__).md>) — Applies a hover effect to this view.
- [hoverEffect(_:isEnabled:)](<view/hovereffect(__isenabled_).md>) — Applies a hover effect to this view.
- [hoverEffect(_:in:isEnabled:)](<view/hovereffect(__in_isenabled_).md>) — Applies a hover effect to this view, optionally adding it to a [HoverEffectGroup](hovereffectgroup.md).
- [hoverEffect(in:isEnabled:body:)](<view/hovereffect(in_isenabled_body_).md>) — Applies a hover effect to this view described by the given closure.
- [hoverEffectGroup()](<view/hovereffectgroup().md>) — Adds an implicit [HoverEffectGroup](hovereffectgroup.md) to all effects defined on descendant views, so that all effects added to subviews activate as a group whenever this view or any descendant views are hovered.
- [hoverEffectGroup(_:)](<view/hovereffectgroup(__).md>) — Adds a [HoverEffectGroup](hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [hoverEffectGroup(id:in:behavior:)](<view/hovereffectgroup(id_in_behavior_).md>) — Adds a [HoverEffectGroup](hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [hoverEffectDisabled(_:)](<view/hovereffectdisabled(__).md>) — Adds a condition that controls whether this view can display hover effects.
- [defaultHoverEffect(_:)](<view/defaulthovereffect(__).md>) — Sets the default hover effect to use for views within this view.
- [listRowHoverEffect(_:)](<view/listrowhovereffect(__).md>) — Requests that the containing list row use the provided hover effect.
- [listRowHoverEffectDisabled(_:)](<view/listrowhovereffectdisabled(__).md>) — Requests that the containing list row have its hover effect disabled.

### Pointer

- [pointerVisibility(_:)](<view/pointervisibility(__).md>) — Sets the visibility of the pointer when it’s over the view.
- [pointerStyle(_:)](<view/pointerstyle(__).md>) — Sets the pointer style to display when the pointer is over the view.

### Focus

- [focused(_:equals:)](<view/focused(__equals_).md>) — Modifies this view by binding its focus state to the given state value.
- [focused(_:)](<view/focused(__).md>) — Modifies this view by binding its focus state to the given Boolean state value.
- [focusedValue(_:)](<view/focusedvalue(__).md>) — Sets the focused value for the given object type.
- [focusedValue(_:_:)](<view/focusedvalue(____).md>) — Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused view hierarchy.
- [focusedSceneValue(_:)](<view/focusedscenevalue(__).md>) — Sets the focused value for the given object type at a scene-wide scope.
- [focusedSceneValue(_:_:)](<view/focusedscenevalue(____).md>) — Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused scene.
- [focusedObject(_:)](<view/focusedobject(__).md>) — Creates a new view that exposes the provided object to other views whose whose state depends on the focused view hierarchy.
- [focusedSceneObject(_:)](<view/focusedsceneobject(__).md>) — Creates a new view that exposes the provided object to other views whose whose state depends on the active scene.
- [prefersDefaultFocus(_:in:)](<view/prefersdefaultfocus(__in_).md>) — Indicates that the view should receive focus by default for a given namespace.
- [focusScope(_:)](<view/focusscope(__).md>) — Creates a focus scope that SwiftUI uses to limit default focus preferences.
- [focusSection()](<view/focussection().md>) — Indicates that the view’s frame and cohort of focusable descendants should be used to guide focus movement.
- [focusable(_:)](<view/focusable(__).md>) — Specifies if the view is focusable.
- [focusable(_:interactions:)](<view/focusable(__interactions_).md>) — Specifies if the view is focusable, and if so, what focus-driven interactions it supports.
- [focusEffectDisabled(_:)](<view/focuseffectdisabled(__).md>) — Adds a condition that controls whether this view can display focus effects, such as a default focus ring or hover effect.
- [defaultFocus(_:_:priority:)](<view/defaultfocus(____priority_).md>) — Defines a region of the window in which default focus is evaluated by assigning a value to a given focus state binding.
- [searchFocused(_:)](<view/searchfocused(__).md>) — Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.
- [searchFocused(_:equals:)](<view/searchfocused(__equals_).md>) — Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.

### Copy and paste

- [copyable(_:)](<view/copyable(__).md>) — Specifies a list of items to copy in response to the system’s Copy command.
- [cuttable(for:action:)](<view/cuttable(for_action_).md>) — Specifies an action that moves items to the Clipboard in response to the system’s Cut command.
- [pasteDestination(for:action:validator:)](<view/pastedestination(for_action_validator_).md>) — Specifies an action that adds validated items to a view in response to the system’s Paste command.
- [onCopyCommand(perform:)](<view/oncopycommand(perform_).md>) — Adds an action to perform in response to the system’s Copy command.
- [onCutCommand(perform:)](<view/oncutcommand(perform_).md>) — Adds an action to perform in response to the system’s Cut command.
- [onPasteCommand(of:perform:)](<view/onpastecommand(of_perform_).md>) — Adds an action to perform in response to the system’s Paste command.
- [onPasteCommand(of:validator:perform:)](<view/onpastecommand(of_validator_perform_).md>) — Adds an action to perform in response to the system’s Paste command with items that you validate.

### Drag and drop

- [dragConfiguration(_:)](<view/dragconfiguration(__).md>) — Configures a drag session.
- [dragContainer(for:in:_:)](<view/dragcontainer(for_in___).md>) — A container with draggable views where the drag payload is based on multiple identifiers of dragged items.
- [dragContainer(for:itemID:in:_:)](<view/dragcontainer(for_itemid_in___).md>) — A container with draggable views.
- [dragContainerSelection(_:containerNamespace:)](<view/dragcontainerselection(__containernamespace_).md>) — Provides multiple item selection support for drag containers.
- [dragPreviewsFormation(_:)](<view/dragpreviewsformation(__).md>) — Describes the way dragged previews are visually composed.
- [draggable(_:)](<view/draggable(__).md>) — Activates this view as the source of a drag and drop operation.
- [draggable(_:preview:)](<view/draggable(__preview_).md>) — Activates this view as the source of a drag and drop operation.
- [draggable(_:containerNamespace:_:)](<view/draggable(__containernamespace___).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [draggable(_:id:containerNamespace:_:)](<view/draggable(__id_containernamespace___).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [draggable(_:id:item:containerNamespace:)](<view/draggable(__id_item_containernamespace_).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [draggable(_:item:containerNamespace:)](<view/draggable(__item_containernamespace_).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [draggable(containerItemID:containerNamespace:)](<view/draggable(containeritemid_containernamespace_).md>) — Inside a drag container, activates this view as the source of a drag and drop operation. Supports lazy drag containers.
- [dropConfiguration(_:)](<view/dropconfiguration(__).md>) — Configures a drop session.
- [dropDestination(for:isEnabled:action:)](<view/dropdestination(for_isenabled_action_).md>) — Defines the destination of a drag and drop operation that provides a drop operation proposal and handles the dropped content with a closure that you specify.
- [dropPreviewsFormation(_:)](<view/droppreviewsformation(__).md>) — Describes the way previews for a drop are composed.
- [itemProvider(_:)](<view/itemprovider(__).md>) — Provides a closure that vends the drag representation to be used for a particular data element.
- [onDrag(_:preview:)](<view/ondrag(__preview_).md>) — Activates this view as the source of a drag and drop operation.
- [onDrag(_:)](<view/ondrag(__).md>) — Activates this view as the source of a drag and drop operation.
- [onDragSessionUpdated(_:)](<view/ondragsessionupdated(__).md>) — Specifies an action to perform on each update of an ongoing dragging operation activated by `draggable(_:)` or anther drag modifiers.
- [onDrop(of:isTargeted:perform:)](<view/ondrop(of_istargeted_perform_).md>) — Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [onDrop(of:delegate:)](<view/ondrop(of_delegate_).md>) — Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [onDropSessionUpdated(_:)](<view/ondropsessionupdated(__).md>) — Specifies an action to perform on each update of an ongoing drop operation activated by `dropDestination(_:)` or other drop modifiers.
- [springLoadingBehavior(_:)](<view/springloadingbehavior(__).md>) — Sets the spring loading behavior this view.

### Reordering

- [reorderContainer(for:isEnabled:move:)](<view/reordercontainer(for_isenabled_move_).md>) — Defines a container of reorderable views. _(beta)_
- [reorderContainer(for:in:isEnabled:move:)](<view/reordercontainer(for_in_isenabled_move_).md>) — Defines a container of reorderable views, with a type you specify to identify sections. _(beta)_
- [reorderContainer(for:itemID:isEnabled:move:)](<view/reordercontainer(for_itemid_isenabled_move_).md>) — Defines a container of reorderable views, with a type and keypath you specify to identify items. _(beta)_
- [reorderContainer(for:itemID:in:isEnabled:move:)](<view/reordercontainer(for_itemid_in_isenabled_move_).md>) — Defines a container of reorderable views, with a type and keypath you use to identify items and a type you use to identify collections. _(beta)_

### Submission

- [onAssignedDocumentDidSubmit(_:)](<view/onassigneddocumentdidsubmit(__).md>) — Adds an action to perform after submitting an assigned document.
- [onAssignedDocumentDidWithdraw(_:)](<view/onassigneddocumentdidwithdraw(__).md>) — Adds an action to perform after an assigned document submission has been withdrawn.
- [onAssignedDocumentWillSubmit(_:)](<view/onassigneddocumentwillsubmit(__).md>) — Adds an action to perform before submitting an assigned document.
- [onAssignedDocumentWillWithdraw(_:)](<view/onassigneddocumentwillwithdraw(__).md>) — Adds an action to perform before withdrawing an assigned document submission.
- [onSubmit(of:_:)](<view/onsubmit(of___).md>) — Adds an action to perform when the user submits a value to this view.
- [submitScope(_:)](<view/submitscope(__).md>) — Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.
- [submitLabel(_:)](<view/submitlabel(__).md>) — Sets the submit label for this view.

### Movement

- [onMoveCommand(perform:)](<view/onmovecommand(perform_).md>) — Adds an action to perform in response to a move command, like when the user presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote when controlling an Apple TV.
- [moveDisabled(_:)](<view/movedisabled(__).md>) — Adds a condition for whether the view’s view hierarchy is movable.

### Deletion

- [onDeleteCommand(perform:)](<view/ondeletecommand(perform_).md>) — Adds an action to perform in response to the system’s Delete command, or pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view has focus.
- [deleteDisabled(_:)](<view/deletedisabled(__).md>) — Adds a condition for whether the view’s view hierarchy is deletable.

### Commands

- [pageCommand(value:in:step:)](<view/pagecommand(value_in_step_).md>) — Steps a value through a range in response to page up or page down commands.
- [onExitCommand(perform:)](<view/onexitcommand(perform_).md>) — Sets up an action that triggers in response to receiving the exit command while the view has focus.
- [onPlayPauseCommand(perform:)](<view/onplaypausecommand(perform_).md>) — Adds an action to perform in response to the system’s Play/Pause command.
- [onCommand(_:perform:)](<view/oncommand(__perform_).md>) — Adds an action to perform in response to the given selector.

### Digital crown

- [digitalCrownAccessory(_:)](<view/digitalcrownaccessory(__).md>) — Specifies the visibility of Digital Crown accessory Views on Apple Watch.
- [digitalCrownAccessory(content:)](<view/digitalcrownaccessory(content_).md>) — Places an accessory View next to the Digital Crown on Apple Watch.
- [digitalCrownRotation(_:from:through:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)](<view/digitalcrownrotation(__from_through_sensitivity_iscontinuous_ishapticfeedbackenabled_onchange_onidle_).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(_:onChange:onIdle:)](<view/digitalcrownrotation(__onchange_onidle_).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)](<view/digitalcrownrotation(detent_from_through_by_sensitivity_iscontinuous_ishapticfeedbackenabled_onchange_onidle_).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(_:)](<view/digitalcrownrotation(__).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(_:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:)](<view/digitalcrownrotation(__from_through_by_sensitivity_iscontinuous_ishapticfeedbackenabled_).md>) — Tracks Digital Crown rotations by updating the specified binding.

### Game controller

- [handlesGameControllerEvents(matching:)](<view/handlesgamecontrollerevents(matching_).md>) — Specifies the game controllers events which should be delivered through the GameController framework when the view, or one of its descendants has focus.
- [handlesGameControllerEvents(matching:withOptions:)](<view/handlesgamecontrollerevents(matching_withoptions_).md>) — Specifies the game controllers events which should be delivered through the GameController framework when the view or one of its descendants has focus.

### Immersive spaces

- [onImmersionChange(initial:_:)](<view/onimmersionchange(initial___).md>) — Performs an action when the immersion state of your app changes.
- [onWorldRecenter(action:)](<view/onworldrecenter(action_).md>) — Adds an action to perform when recentering the view with the digital crown.
- [immersiveEnvironmentPicker(content:)](<view/immersiveenvironmentpicker(content_).md>) — Add menu items to open immersive spaces from a media player’s environment picker.

### Volumes

- [onVolumeViewpointChange(updateStrategy:initial:_:)](<view/onvolumeviewpointchange(updatestrategy_initial___).md>) — Adds an action to perform when the viewpoint of the volume changes.
- [supportedVolumeViewpoints(_:)](<view/supportedvolumeviewpoints(__).md>) — Specifies which viewpoints are supported for the window bar and ornaments in a volume.

### User activities

- [userActivity(_:element:_:)](<view/useractivity(__element___).md>) — Advertises a user activity type.
- [userActivity(_:isActive:_:)](<view/useractivity(__isactive___).md>) — Advertises a user activity type.
- [onContinueUserActivity(_:perform:)](<view/oncontinueuseractivity(__perform_).md>) — Registers a handler to invoke in response to a user activity that your app receives.
- [handlesExternalEvents(preferring:allowing:)](<view/handlesexternalevents(preferring_allowing_).md>) — Specifies the external events that the view’s scene handles if the scene is already open.

### View life cycle

- [onAppear(perform:)](<view/onappear(perform_).md>) — Adds an action to perform before this view appears.
- [onDisappear(perform:)](<view/ondisappear(perform_).md>) — Adds an action to perform after this view disappears.
- [onChange(of:initial:_:)](<view/onchange(of_initial___).md>) — Adds a modifier for this view that fires an action when a specific value changes.
- [task(id:name:executorPreference:priority:file:line:_:)](<view/task(id_name_executorpreference_priority_file_line___).md>) — Adds a task to perform before this view appears or when a specified value changes.
- [task(id:name:priority:file:line:_:)](<view/task(id_name_priority_file_line___).md>) — Adds a task to perform before this view appears or when a specified value changes.
- [task(name:executorPreference:priority:file:line:action:)](<view/task(name_executorpreference_priority_file_line_action_).md>) — Adds an asynchronous task to perform before this view appears.
- [task(name:priority:file:line:_:)](<view/task(name_priority_file_line___).md>) — Adds an asynchronous task to perform before this view appears.

### File renaming

- [renameAction(_:)](<view/renameaction(__).md>) — Sets a closure to run for the rename action.

### URLs

- [onOpenURL(perform:)](<view/onopenurl(perform_).md>) — Registers a handler to invoke in response to a URL that your app receives.
- [onOpenURL(prefersInApp:)](<view/onopenurl(prefersinapp_).md>) — Sets an `OpenURLAction` that prefers opening URL with an in-app browser. The `handler` closure takes a URL as input, and returns a `OpenURLAction.Result` that indicates the outcome of the action.
- [widgetURL(_:)](<view/widgeturl(__).md>) — Sets the URL to open in the containing app when the user clicks the widget.

### Asynchronous image loading

- [asyncImageURLSession(_:)](<view/asyncimageurlsession(__).md>) — A modifier that adds a URL session for asynchronous images contained in the view to use when fetching image data. _(beta)_

### Publisher events

- [onReceive(_:perform:)](<view/onreceive(__perform_).md>) — Adds an action to perform when this view detects data emitted by the given publisher.

### Hit testing

- [allowsHitTesting(_:)](<view/allowshittesting(__).md>) — Configures whether this view participates in hit test operations.

### Content shape

- [contentShape(_:eoFill:)](<view/contentshape(__eofill_).md>) — Defines the content shape for hit testing.
- [contentShape(_:_:eoFill:)](<view/contentshape(____eofill_).md>) — Sets the content shape for this view.

### Import and export

- [exportsItemProviders(_:onExport:)](<view/exportsitemproviders(__onexport_).md>) — Exports a read-only item provider for consumption by shortcuts, quick actions, and services.
- [exportsItemProviders(_:onExport:onEdit:)](<view/exportsitemproviders(__onexport_onedit_).md>) — Exports a read-write item provider for consumption by shortcuts, quick actions, and services.
- [importsItemProviders(_:onImport:)](<view/importsitemproviders(__onimport_).md>) — Enables importing item providers from services, such as Continuity Camera on macOS.
- [exportableToServices(_:)](<view/exportabletoservices(__).md>) — Exports items for consumption by shortcuts, quick actions, and services.
- [exportableToServices(_:onEdit:)](<view/exportabletoservices(__onedit_).md>) — Exports read-write items for consumption by shortcuts, quick actions, and services.
- [importableFromServices(for:action:)](<view/importablefromservices(for_action_).md>) — Enables importing items from services, such as Continuity Camera on macOS.

### App intents

- [appEntityIdentifier(_:)](<view/appentityidentifier(__).md>) — Associates a SwiftUI view with an app entity to make its content discoverable by Apple Intelligence and Siri.
- [appEntityIdentifier(forSelectionType:identifier:)](<view/appentityidentifier(forselectiontype_identifier_).md>) — Associates the items in a SwiftUI list view with app entities to make them discoverable by Apple Intelligence and Siri.
- [appEntityUIElements(_:)](<view/appentityuielements(__).md>) — Provides the system with additional context to make a custom view’s content discoverable by Apple Intelligence and Siri.
- [onAppIntentExecution(_:perform:)](<view/onappintentexecution(__perform_).md>) — Registers a handler to invoke in response to the specified app intent that your app receives.
- [shortcutsLinkStyle(_:)](<view/shortcutslinkstyle(__).md>) — Sets the given style for ShortcutsLinks within the view hierarchy
- [siriTipViewStyle(_:)](<view/siritipviewstyle(__).md>) — Sets the given style for SiriTipView within the view hierarchy

### Camera

- [onCameraCaptureEvent(isEnabled:action:)](<view/oncameracaptureevent(isenabled_action_).md>) — Used to register an action triggered by system capture events.
- [onCameraCaptureEvent(isEnabled:defaultSoundDisabled:action:)](<view/oncameracaptureevent(isenabled_defaultsounddisabled_action_).md>) — Used to register an action triggered by system capture events.
- [onCameraCaptureEvent(isEnabled:defaultSoundDisabled:primaryAction:secondaryAction:)](<view/oncameracaptureevent(isenabled_defaultsounddisabled_primaryaction_secondaryaction_).md>) — Used to register actions triggered by system capture events.
- [onCameraCaptureEvent(isEnabled:primaryAction:secondaryAction:)](<view/oncameracaptureevent(isenabled_primaryaction_secondaryaction_).md>) — Used to register actions triggered by system capture events.
- [cameraAnchor(isActive:)](<view/cameraanchor(isactive_).md>) — Specifies the view that should act as the virtual camera for Apple Vision Pro 2D Persona stream.

## See Also

### Providing interactivity

- [Search modifiers](view-search.md) — Enable people to search for content in your app.
- [Presentation modifiers](view-presentation.md) — Define additional views for the view to present under specified conditions.
- [State modifiers](view-state.md) — Access storage and provide child views with configuration data.
