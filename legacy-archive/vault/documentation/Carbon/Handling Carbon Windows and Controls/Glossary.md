---
title: Handling Carbon Windows and Controls
apple_id: TP30001004
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-07-07'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/HandlingWindowsControls/glossary/wind_cont_glossary.html
archived_at: '2026-07-15T05:22:46.938041Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Handling Carbon Windows and Controls](Introduction%20to%20Handling%20Carbon%20Windows%20and%20Controls.md)


[Previous](Document%20Revision%20History.md)

# Glossary

- __active control__

  A control that can respond to user input. Typically controls are active when their owning window is active.

- __active window__

  The window in which the user is currently working. The active window as an opaque title bar and all its controls have color. The active window is typically the frontmost nonfloating window.

- __application-modal__

  A window state where the user cannot do anything else within the application until the window is dismissed. Compare. [document-modal](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqhewueq2jizbegrcc);[system modal](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqhewueq2jjfceur2e).

- __best size__

  The optimum size for displaying the contents of a window.

- __click-through__

  A control state where the control responds to user input even if the owning window is inactive.

- __close button__

  The red button in a window’s title bar that closes the window.

- __content region__

  The portion of the window below the title bar. The content region can contain document content or controls.

- __control reference__

  A pointer to an opaque data structure that describes a control’s properties. You manipulate a control by means of its control reference.

- __default button__

  The button in a dialog that is activated when the user clicks the Return or Enter key. The default button is identified by its pulsing blue animation.

- __desktop__

  The background on top of which all windows appear to rest onscreen;the working environment displayed on Macintosh computers.

- __dialog__

  A window that is specifically designed to interact with the user.

- __document-modal__

  A window state where the user cannot do anything else within a particular document until the window is dismissed. Sheets are document-modal windows. Compare [application-modal](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqhewueq2jirbueq2g); [system modal](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqhewueq2jjfceur2e).

- __drag area__

  The portion of the window that users can “grab” to move it around the desktop.

- __enabled control__

  A control state where the control appears normally (that is, not grayed out) and responds to user input when active.

- __focus ring__

  A colored halo that appears around the control that currently has keyboard focus.

- __frame region__

  The portion of the window that is not the content region. The frame region is so named because earlier versions of Mac OS windows included thin borders around the content region.

- __global coordinates__

  The coordinate system where the origin is set at the top left corner of the main viewing screen. Compare [local coordinates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqhewueq2jizauorcb).

- __graphics port__

  A drawing environment that describes how to translate bits in memory to an image. Graphics ports are typically associated with windows (every window has one), but graphics ports also exist for printing.

- __indicator__

  The part of a control that visually represents its value. For example, on a scroll bar control, the scroller is the indicator.

- __keyboard focus__

  The state in which a window or control receives keystrokes. Keyboard input is directed to one window (and one control within the window) at a time.

- __local coordinates__

  The coordinate system for each window, where the origin is set at the upper left corner of the window’s content region. Compare [global coordinates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqhewueq2ji5cukqke).

- __minimize button__

  The yellow button in a window’s title bar that shrinks the window into the Dock.

- __nib file__

  A special file created by Interface Builder that contains information required to create user interface objects (windows, controls, and menus).

- __proxy icon__

  An icon that appears in a window’s title bar. The user can manipulate the proxy icon just as if it were the actual document or folder icon in the Finder.

- __resize control__

  A control that appears in the lower right corner of a window that allows the user to resize the window. Sometimes referred to as a _resize tab_.

- __resource__

  A special data structure that was historically stored in the resource fork of a file. Resources are accessed and interpreted by resource type and ID.

- __resource fork__

  The part of a file that historically held an application’s resources. Use of the resource fork is discouraged in Mac OS X, but you can store resources in the data fork.

- __root control__

  An invisible control within which all other controls for window are embedded.

- __scroller__

  The movable indicator in a scroll bar.

- __scroll arrows__

  Small buttons that appear on the scroll control that let the user incrementally advance the scrollers without dragging.

- __scroll bar__

  A special control that lets the user select which portion of a document is visible in a window.

- __scroller__

  The movable portion of the scroll control.

- __structure region__

  The entire area taken up by the window onscreen.

- __system modal__

  A window state where the user cannot do anything else until the window is dismissed. You should avoid using the system-modal state if at all possible. Compare [application-modal](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqhewueq2jirbueq2g); [document-modal](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqhewueq2jizbegrcc).

- __title bar__

  The bar at the top of the window that displays its name. The title bar can also contain controls and a proxy icon.

- __toolbar button__

  A clear oblong button at the right end of a window’s title bar that shows and hides the toolbar (if one exists).

- __toolbox object class__

  A collection of event handlers and data that defines a custom object such as a control or window.

- __update region__

  A region maintained by the Window Manager that includes the parts of a window’s content region that need updating.

- __user size__

  The window size determined by the user.

- __visible region__

  The portion of a window’s content region that is visible to the user.

- __window__

  The primary means of displaying screen information on Macintosh computers.

- __window layering__

  The layering of windows according to the window class hierarchy. Compare [window ordering](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqhewueq2jijfecrkh).

- __window ordering__

  The layering of windows within a specific window class. Compare _window layering._

- __window reference__

  A pointer to an opaque data structure that defines a window. All access to a window or its attributes is through the window reference.

- __zoom button__

  The green button in a window’s title bar that toggles its size between the user size and the best size.

[Previous](Document%20Revision%20History.md)

