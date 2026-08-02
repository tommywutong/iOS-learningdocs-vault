---
title: Mac Automation Scripting Guide
apple_id: TP40016239
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/AutomatetheUserInterface.html
archived_at: '2026-07-15T07:45:17.916792Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Mac Automation Scripting Guide](index.md)



## Automating the User Interface

Unfortunately, not every Mac app has scripting support, and those that do may not always have scripting support for every task you want to automate. You can often work around such limitations, however, by writing a user interface script, commonly called a UI or GUI script. A user interface script simulates user interaction, such as mouse clicks and keystrokes, allowing the script to select menu items, push buttons, enter text into text fields, and more.

### Enabling User Interface Scripting

User interface scripting relies upon the OS X accessibility frameworks that provide alternative methods of querying and controlling the interfaces of apps and the system. By default, accessibility control of apps is disabled. For security and privacy reasons, the user must manually enable it on an app-by-app (including script apps) basis.

__To enable accessibility control for an app__

1. Launch System Preferences and click Security & Privacy.
2. Click the Privacy tab.
3. Click Accessibility.
4. Click the Add button (+).
5. Choose an app and click Open.
6. Select the checkbox to the left of the app.

   ![image: ../Art/systempreferences_security_accessibility_2x.png](attachments/Art/systempreferences_security_accessibility_2x.png)

When running an app that requires accessibility control for the first time, the system prompts you to enable it. See Figure 37-1.

__Figure 37-1__An accessibility control prompt
![image: ../Art/accessibility_alert1_2x.png](attachments/Art/accessibility_alert1_2x.png)

Attempting to run an app that has not been given permission to use accessibility features results in an error. See Figure 37-2.

__Figure 37-2__An accessibility control error
![image: ../Art/accessibility_alert2_2x.png](attachments/Art/accessibility_alert2_2x.png)

> [!NOTE]
> 

### Targeting an App

User interface scripting terminology is found in the Processes Suite of the System Events scripting dictionary. This suite includes terminology for interacting with most types of user interface elements, including windows, buttons, checkboxes, menus, radio buttons, text fields, and more. In System Events, the `process` class represents a running app. Listing 37-1 shows how to target an app using this class.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=tell%20application%20%22System%20Events%22%0A%20%20%20%20tell%20process%20%22Safari%22%0A%20%20%20%20%20%20%20%20--%20Perform%20user%20interface%20scripting%20tasks%0A%20%20%20%20end%20tell%0Aend%20tell)

__Listing 37-1__AppleScript: Targeting an app for user interface scripting

1. `tell application "System Events"`
2. `tell process "Safari"`
3. `-- Perform user interface scripting tasks`
4. `end tell`
5. `end tell`

To control the user interface of an app, you must first inspect the app and determine its element hierarchy. This can be done by querying the app. For example, Listing 37-2 asks Safari for a list of menus in the menu bar.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=tell%20application%20%22System%20Events%22%0A%20%20%20%20tell%20process%20%22Safari%22%0A%20%20%20%20%20%20%20%20name%20of%20every%20menu%20of%20menu%20bar%201%0A%20%20%20%20end%20tell%0Aend%20tell%0A--%3E%20Result%3A%20%7B%22Apple%22%2C%20%22Safari%22%2C%20%22File%22%2C%20%22Edit%22%2C%20%22View%22%2C%20%22History%22%2C%20%22Bookmarks%22%2C%20%22Develop%22%2C%20%22Window%22%2C%20%22Help%22%7D)

__Listing 37-2__AppleScript: Querying an app for user interface element information

1. `tell application "System Events"`
2. `tell process "Safari"`
3. `name of every menu of menu bar 1`
4. `end tell`
5. `end tell`
6. `--> Result: {"Apple", "Safari", "File", "Edit", "View", "History", "Bookmarks", "Develop", "Window", "Help"}`

Accessibility Inspector (Figure 37-3) makes it even easier to identify user interface element information. This app is included with Xcode. To use it, open Xcode and select Xcode > Open Developer Tool > Accessibility Inspector.

__Figure 37-3__Accessibility Inspector
![image: ../Art/accessibilityinspector_2x.png](attachments/Art/accessibilityinspector_2x.png)

Once you know how an element fits into an interface, you target it within that hierarchy. For example, `button X of window Y of process Z`.

### Clicking a Button

Use the `click` command to click a button. Listing 37-3 clicks a button in the Safari toolbar to toggle the sidebar between open and closed.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=tell%20application%20%22System%20Events%22%0A%20%20%20%20tell%20process%20%22Safari%22%0A%20%20%20%20%20%20%20%20tell%20toolbar%20of%20window%201%0A%20%20%20%20%20%20%20%20%20%20%20%20click%20%28first%20button%20where%20its%20accessibility%20description%20%3D%20%22Sidebar%22%29%0A%20%20%20%20%20%20%20%20end%20tell%0A%20%20%20%20end%20tell%0Aend%20tell%0A--%3E%20Result%3A%20%7Bbutton%201%20of%20toolbar%201%20of%20window%20%22AppleScript%3A%20Graphic%20User%20Interface%20%28GUI%29%20Scripting%22%20of%20application%20process%20%22Safari%22%20of%20application%20%22System%20Events%22%7D)

__Listing 37-3__AppleScript: Clicking a button

1. `tell application "System Events"`
2. `tell process "Safari"`
3. `tell toolbar of window 1`
4. `click (first button where its accessibility description = "Sidebar")`
5. `end tell`
6. `end tell`
7. `end tell`
8. `--> Result: {button 1 of toolbar 1 of window "AppleScript: Graphic User Interface (GUI) Scripting" of application process "Safari" of application "System Events"}`

### Choosing a Menu Item

Menu items can have a fairly deep hierarchy within the interface of an app. A menu item generally resides within a menu, which resides within a menu bar. In scripting, they must be addressed as such. Listing 37-4 selects the Pin Tab menu item in the Window menu of Safari.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=tell%20application%20%22System%20Events%22%0A%20%20%20%20tell%20process%20%22Safari%22%0A%20%20%20%20%20%20%20%20set%20frontmost%20to%20true%0A%20%20%20%20%20%20%20%20click%20menu%20item%20%22Pin%20Tab%22%20of%20menu%20%22Window%22%20of%20menu%20bar%201%0A%20%20%20%20end%20tell%0Aend%20tell%0A--%3E%20Result%3A%20menu%20item%20%22Pin%20Tab%22%20of%20menu%20%22Window%22%20of%20menu%20bar%20item%20%22Window%22%20of%20menu%20bar%201%20of%20application%20process%20%22Safari%22%20of%20application%20%22System%20Events%22)

__Listing 37-4__AppleScript: Choosing a menu item

1. `tell application "System Events"`
2. `tell process "Safari"`
3. `set frontmost to true`
4. `click menu item "Pin Tab" of menu "Window" of menu bar 1`
5. `end tell`
6. `end tell`
7. `--> Result: menu item "Pin Tab" of menu "Window" of menu bar item "Window" of menu bar 1 of application process "Safari" of application "System Events"`

> [!NOTE]
> 

### Choosing a Submenu Item

Some menus contain other menus. In these cases, it may be necessary to select a menu item in a submenu of a menu. Listing 37-7 demonstrates how this would be done by selecting a submenu item in Safari.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=tell%20application%20%22System%20Events%22%0A%20%20%20%20tell%20process%20%22Safari%22%0A%20%20%20%20%20%20%20%20set%20frontmost%20to%20true%0A%20%20%20%20%20%20%20%20click%20menu%20item%20%22Email%20This%20Page%22%20of%20menu%20of%20menu%20item%20%22Share%22%20of%20menu%20%22File%22%20of%20menu%20bar%201%0A%20%20%20%20end%20tell%0Aend%20tell%0A--%3E%20Result%3A%20%7Bmenu%20item%20%22Email%20This%20Page%22%20of%20menu%20%22Share%22%20of%20menu%20item%20%22Share%22%20of%20menu%20%22File%22%20of%20menu%20bar%20item%20%22File%22%20of%20menu%20bar%201%20of%20application%20process%20%22Safari%22%20of%20application%20%22System%20Events%22%7D)

__Listing 37-7__AppleScript: Selecting a submenu item

1. `tell application "System Events"`
2. `tell process "Safari"`
3. `set frontmost to true`
4. `click menu item "Email This Page" of menu of menu item "Share" of menu "File" of menu bar 1`
5. `end tell`
6. `end tell`
7. `--> Result: {menu item "Email This Page" of menu "Share" of menu item "Share" of menu "File" of menu bar item "File" of menu bar 1 of application process "Safari" of application "System Events"}`

[Working with XML](WorkwithXML.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqnrxfvjvomi)

[Manipulating Images](ManipulateImages.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqmrqfvjvomi)
