---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Concepts/ChangingMainKeyWindow.html
archived_at: '2026-07-15T07:21:08.355553Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](Window%20Layers%20and%20Levels.md)[Previous](Opening%20and%20Closing%20Windows.md)

# Window Layering and Types of Windows

Each window is placed on the screen by a particular application, and each application typically owns a variety of windows. Windows have numerous characteristics. They can be located onscreen or offscreen. Onscreen windows are placed on the screen in levels managed by the window server.

Windows onscreen are ordered from front to back. Like sheets of paper loosely stacked together, windows in front can overlap, or even completely cover, those behind them. Each window has a unique position in the order. When two windows are placed side-by-side, one is still technically in front of the other.

If any window could be in front of any other window, then small but important windows—like menus and tool palettes—might get lost behind larger ones. Windows that require user action, like attention panels and pop-up lists, might disappear behind another window and go unnoticed. To prevent this, all the windows onscreen are organized into levels.

When two windows belong to the same level, either one can be in front. When two windows belong to different levels, however, the one in the higher level will always be above the other.

Onscreen windows can also carry a status: _main_ or _key_. Offscreen windows are hidden or minimized on Dock, and do not carry either status. Onscreen windows that are neither main nor key are inactive.

Each application and document window exists in its own layer, so documents from different applications can be interleaved. Clicking a window to bring it to the front doesn’t disturb the layering order of any other window.

A window’s depth in the layers is determined by when the window was last accessed. When a user clicks an inactive document or chooses it from the Window menu, only that document, and any open utility windows, should be brought to the front. Users can bring all windows of an application forward by clicking its icon in the Dock or by choosing Bring All to Front in the application’s Window menu. These actions should bring forward all of the application’s open windows, maintaining their onscreen location, size, and layering order within the application. For more information, see UI Element Guidelines: Menus in _OS X Human Interface Guidelines_.

Utility windows are always in the same layer: the top layer. They are visible only when their application is active.

Windows have different looks based on how the user is interacting with them. The foremost document or application window that is the focus of the user’s attention is referred to as the _main_ window. Each application also has only one main window at a given time. This main window often has _key_ status, as well. The main window is the principal focus of user actions for an application. Often, user actions in a modal key window (typically a panel such as the Font window or an Info window) have a direct effect on the main window.

Main and key windows are both active windows. Active windows are visually distinct from inactive windows in that their controls have color, while the controls in inactive windows do not have color. Inactive windows are windows the user has open but that are not in the foreground. Main and key windows are always in the foreground and their controls always have color. If the main and key window are different windows, they are distinguished from one another by the look of their title bars. Note the visual distinctions between main, key, and inactive windows in Figure 1.

__Figure 1__  Main, key, and inactive windows

!

A good example of the difference between key and main windows can be seen in most well-behaved Mac apps. Selecting “Save As...” in a text document, for example, displays a panel with a field to type the document’s name and a pull-down menu of locations to save it. The panel represents the _key_ window. It will accept your keyboard input (the file name), but will directly affect the _main_ window under it (by saving it to the location you specified). Once you save the document, the save panel disappears, the main window becomes key again, and will accept keyboard input once more.

The _key window_ responds to user input, whether from the keyboard, mouse, or alternative input devices, for an application and is the primary recipient of messages from menus and panels. Usually, a window is made key when the user clicks it. Each application can have only one key window at a given time.

Users expect to see their actions on the keyboard and mouse take effect not only in a particular application, but also in a particular window of that application. Each user action is associated with a window by the window server and AppKit. Before acting, the user needs to know which window will be affected; there should be no surprises.

Since the mouse controls the pointer, it's quite easy for the user to determine which window a mouse action is associated with. It's whatever window the pointer is over. But the keyboard doesn’t have a pointer, so there’s no natural way to determine where typed characters will appear.

To mark the key window for users, AppKit highlights its title bar. You can think of the highlighting as a kind of pointer for the keyboard. It shifts from window to window as the key window changes. Key-window status also moves from application to application as the active application changes. Only one window on the screen is marked at a time, and it is in the active application. There’s just one key window on the Desktop. Even a system that has two screens, but only one keyboard, has at most one key window.

Since the key window belongs to the active application, its highlighted title bar has the secondary effect of helping to show which application is currently active. The key window is the most prominently marked window in the active application, making it “key” in a second sense: it’s the main focus of the user’s attention on the screen.

The _main window_ is the standard window where the user is currently working. The main window is not always the key window. There are times when a window other than the main window takes the focus of the input device, while the main window still remains the focus of the user’s attention and of user actions carried out in panels and menus. For example, when a person is using an inspector, a Find dialog, or the Fonts or Colors windows, the document is the main window and the other window is the key window. The Find panel requires the user to supply information by typing it. Since the panel is the destination of the user’s keystrokes, it’s marked as the key window. But the panel is just an instrument through which users can do work in another window—the main window. In a document-based application, the main window is the window for the current document.

Whenever a standard window becomes the key window, it also becomes the main window. When key-window status shifts from a standard window to a panel, main-window status remains with the standard window.

So that users can pick out the main window when it’s not the key window, the Application Kit highlights its title bar and colors the window buttons. If the main window is also the key window, it has only the highlighting of the key window. A menu command might affect either the key window or the main window, depending on the command. For example, the Paste command can be used to enter text in a Find panel. But the Save command saves the document displayed in the main window, and the Bold command turns the current selection in the main window bold. For this reason, user actions in a panel or menu are associated with both the key window and the main window:

- An action is first associated with the key window.
- If the key window is a panel and it can’t handle the action, the action is next associated with the main window.

Note that this order of precedence is reflected in the way windows are highlighted: The key window is always marked, but the main window is marked only when it’s not the key window. The main window is always in the same application as the key window, the active application.

Windows that are already onscreen automatically change their status as the key or main window based on the user’s actions with the mouse and on how clicked views handle those mouse events. You can also set the key and main windows programmatically by sending the relevant windows a [makeKeyWindow](https://developer.apple.com/documentation/appkit/nswindow/1419368-makekey) or [makeMainWindow](https://developer.apple.com/documentation/appkit/nswindow/1419271-makemain) message. Setting the key and main windows programmatically is particularly useful when creating a new window. Because making a window key is often combined with ordering the window to the front of the screen, the `NSWindow` class defines a convenience method, [makeKeyAndOrderFront:](https://developer.apple.com/documentation/appkit/nswindow/1419208-makekeyandorderfront), that performs both operations.

Not all windows are suitable as key or main windows. For example, a window that merely displays information and contains no objects that need to respond to events or action messages can completely forgo ever becoming the key window. Similarly, a window that acts as a floating palette of items that are only dragged out by mouse actions never needs to be the key window. Such a window can be defined as a subclass of `NSWindow` that overrides the methods [canBecomeKeyWindow](https://developer.apple.com/documentation/appkit/nswindow/1419543-canbecomekeywindow) and [canBecomeMainWindow](https://developer.apple.com/documentation/appkit/nswindow/1419162-canbecomemain) to return `NO` instead of the default of `YES`. Defining a window this way prevents it from ever becoming the key or main window. Although the `NSWindow` class defines these methods, only subclasses of `NSPanel` typically refuse to accept key or main window status.

[Next](Window%20Layers%20and%20Levels.md)[Previous](Opening%20and%20Closing%20Windows.md)

