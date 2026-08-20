---
title: Ruler and Paragraph Style Programming Topics
apple_id: 10000089i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2007-09-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Rulers/Tasks/UserManipMarker.html
archived_at: '2026-07-15T07:18:47.894497Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Ruler and Paragraph Style Programming Topics](Introduction%20to%20Rulers%20and%20Paragraph%20Styles.md)


[Next](Updating%20the%20Ruler%20View.md)[Previous](Using%20a%20Ruler%20View%E2%80%99s%20Client.md)

# Letting Users Manipulate Markers

While a ruler’s client view must perform the work of determining marker locations and placing them on the ruler, the ruler itself handles all the work of tracking user manipulations of the markers, sending messages to the client view that inform it of the changes before they begin, as they occur, and after they finish. The client view can use these messages to update its own state. The following sections describe the individual processes of moving, removing, and adding markers, along with a special method for handling mouse events in the ruler area.

When the user presses the mouse button over a ruler marker, NSRulerView sends the marker a `trackMouse:adding:` message. If the marker isn’t movable this method does nothing and immediately returns `NO`. If it is movable, then it sends the client a series of messages allowing it to determine how the user can move the marker around on the ruler.

The first of these messages is `rulerView:shouldMoveMarker`, which allows the client view to prevent an otherwise movable marker from being moved. Normally, whether a marker can be moved should be set on the marker itself, but there are situations, such as where items can be locked in place, where this is more properly tracked by the client view instead. If the client view returns `YES`, allowing the movement, then it receives a series of `rulerView:willMoveMarker:toLocation:` messages as the user drags the marker around. Each message identifies the marker being moved and its proposed new location in the client view’s coordinate system. The client view can return an altered location to restrict the marker’s movement, or update its display to reflect the new location. Finally, when the user releases the mouse button, the client receives `rulerView:didMoveMarker:`, on which it can update its state and clean up any information it may have used while tracking the marker’s movements.

Removal of markers is handled by a similar set of messages. However, these are always sent during a movement operation, as the user must first be dragging a marker within the ruler to be able to drag it off the ruler. If a marker isn’t set to be removable, the user simply can’t drag it off. If the marker is removable, then when the user drags the mouse far enough away from the ruler’s baseline, it sends the client view a `rulerView:shouldRemoveMarker:` message, allowing the client to approve or veto the removal. No messages are necessary for new locations, of course, but if the user returns the marker to the ruler then it resumes sending `rulerView:willMoveMarker:toLocation:` messages as before. If the user releases the mouse with the marker dragged away from the ruler, the marker sends the client view a `rulerView:didRemoveMarker:` message, so the user can delete the item or attribute represented by the marker.

When the user wants to add a marker, the addition must be initiated by the application, of course, since there is no marker yet for the ruler to track. The first step in adding a marker, then, is to create one, using the NSRulerMarker`initWithRulerView:markerLocation:image:imageOrigin:` method. Once the new marker is created, you instruct the ruler view to handle dragging it onto itself by sending it a `trackMarker:withMouseEvent:` message. One means of doing this is to use the mouse event from the client view method `rulerView:handleMouseDown:`, as described in [Handling Mouse Events in the Ruler Area](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha3tqljrgaztoojwhe). Another is to create a custom view object—which typically resides in the ruler’s accessory view—that displays prototype markers, and that handles a mouse-down event by creating a new marker for the ruler and invoking `trackMarker:withMouseEvent:` with the new marker and that mouse-down event.

Once you’ve initiated the addition process, things proceed in the same manner as for moving a marker. The ruler view sends the new marker a `trackMouse:adding:` message, with `YES` as the second argument to indicate that the marker isn’t merely being moved. The marker being added then sends the client view a `rulerView:shouldAddMarker:` message, and if the client approves, then it repeatedly sends `rulerView:willAddMarker:atLocation:` messages as the user moves the marker around on the ruler. The user can drag the marker away to avoid adding it, or release the mouse button over the ruler, in which case the client receives a `rulerView:didAddMarker:` message.

As with moving a marker, you should consider enabling and disabling in a more immediate fashion than by the client view method if possible. If the user shouldn’t be able to drag a marker from the accessory view, for example, the view containing the prototype marker should disable itself and indicate this in its appearance, rather than allowing the user to drag a marker out only to discover that the ruler won’t accept it.

In addition to handling user manipulation of markers, a ruler informs its client view when the user presses the mouse button while the mouse is inside the ruler area (where hash marks are drawn) by sending it a `rulerView:handleMouseDown:` message. This information allows the client view to take some special action, such as adding a new marker to the ruler, as described in [Adding Markers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha3tqljrgaztoojqgi). This approach works well when it’s quite clear what kind of marker will be created. The client view can also use this message as a cue to change its display in some way—for example, to add or remove a guideline that assists the user in laying out and aligning items in the view.

[Next](Updating%20the%20Ruler%20View.md)[Previous](Using%20a%20Ruler%20View%E2%80%99s%20Client.md)

