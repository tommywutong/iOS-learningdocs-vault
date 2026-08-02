---
title: Xcode Keyboard Shortcuts and Gestures
apple_id: TP40010560
resource_type: Guide
platform: watchOS|Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-05-07'
source_url: https://developer.apple.com/library/archive/documentation/IDEs/Conceptual/xcode_help-command_shortcuts/SystemAndOther/SystemAndOther.html
archived_at: '2026-07-15T07:43:33.975405Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Keyboard Shortcuts and Gestures](About%20Xcode%20Gestures%20and%20Keyboard%20Shortcuts.md)


[Next](Document%20Revision%20History.md)[Previous](Text%20Commands%20%28By%20Type%29.md)

# Other System and Application Shortcuts

[Table 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknrqfvbuqnjnknlte) lists system-reserved and commonly used keyboard shortcuts.

Before you change keyboard shortcuts or implement them in your application, use this section to find:

- Key sequences reserved for use by OS X, indicated by an  icon.

  Users rely on these shortcuts to perform the specified actions regardless of which application is currently running (these include shortcuts reserved for accessibility purposes). _Do not override these shortcuts_.
- Key sequences recommended for common application tasks.

  Users expect these shortcuts to be consistent from application to application. If your application performs these tasks, you should provide the same shortcuts for those tasks.

  If your application does not perform the task associated with a recommended shortcut, think very carefully before you consider overriding it. Your users are likely to know and expect the original, established meaning.

For guidance on creating new keyboard shortcuts, see _Apple Human Interface Guidelines_.

__Table 3-1__  Common system and application shortcuts

| Primary Key | Key sequence |  | Associated action |
| __Space bar__ | ⌘ __Space__ |  | Show or hide the Spotlight search field (when multiple languages are installed, may rotate through enabled script systems). |
| __Space bar__ | ⇧ ⌘ __Space__ |  | Apple reserved. |
| __Space bar__ | ⌥ ⌘ __Space__ |  | Show the Spotlight search results window (when multiple languages are installed, may rotate through keyboard layouts and input methods within a script). |
| __Space bar__ | ⌃ ⌘ __Space__ |  | Apple reserved. |
| __Tab__ | ⇧ __Tab__ |  | Navigate through controls in a reverse direction. |
| __Tab__ | ⌘ __Tab__ |  | Move forward to the next most recently used application in a list of open applications. |
| __Tab__ | ⇧ ⌘ __Tab__ |  | Move backward through a list of open applications (sorted by recent use). |
| __Tab__ | ⌃ __Tab__ |  | Move focus to the next grouping of controls in a dialog or the next table (when Tab moves to the next cell). |
| __Tab__ | ⇧ ⌃ __Tab__ |  | Move focus to the previous grouping of controls. |
| __Esc__ | ⌘ __Esc__ |  | Open Front Row. |
| __Esc__ | ⌥ ⌘ __Esc__ |  | Open the Force Quit dialog. |
| __Eject__ | ⌃ ⌘ __Eject__ |  | Quit all applications (after giving the user a chance to save changes to open documents) and restart the computer. |
| __Eject__ | ⌃ ⌥ ⌘ __Eject__ |  | Quit all applications (after giving the user a chance to save changes to open documents) and shut the computer down. |
| __F1__ | ⌃ __F1__ |  | Toggle full keyboard access on or off. |
| __F2__ | ⌃ __F2__ |  | Move focus to the menu bar. |
| __F3__ | ⌃ __F3__ |  | Move focus to the Dock. |
| __F4__ | ⌃ __F4__ |  | Move focus to the active (or next) window. |
| __F4__ | ⇧ ⌃  __F4__ |  | Move focus to the previously active window. |
| __F5__ | ⌃ __F5__ |  | Move focus to the toolbar. |
| __F5__ | ⌘  __F5__ |  | Turn VoiceOver on or off. |
| __F6__ | ⌃  __F6__ |  | Move focus to the first (or next) panel. |
| __F6__ | ⇧ ⌃ __F6__ |  | Move focus to the previous panel. |
| __F7__ | ⌃ __F7__ |  | Temporarily override the current keyboard access mode in windows and dialogs. |
| __F8__ |  |  | Tile or untile all enabled spaces. |
| __F9__ |  |  | Tile or untile all open windows. |
| __F10__ |  |  | Tile or untile all open windows in the currently active application. |
| __F11__ |  |  | Hide or show all open windows. |
| __F12__ |  |  | Hide or display Dashboard. |
| __`__(grave accent) | ⌘ __`__ |  | Activate the next open window in the frontmost application. |
| __`__(grave accent) | ⇧ ⌘ __`__ |  | Activate the previous open window in the frontmost application. |
| __`__(grave accent) | ⌥ ⌘ __`__ |  | Move focus to the window drawer. |
| __-__ (hyphen) | ⌘ __-__ |  | Decrease the size of the selected item (equivalent to the Smaller command). |
| __-__ (hyphen) | ⌥ ⌘ __-__ |  | Zoom out when screen zooming is on. |
| __{__ (left bracket) | ⌘ __{__ |  | Left-align a selection (equivalent to the Align Left command). |
| __}__ (right bracket) | ⌘ __}__ |  | Right-align a selection (equivalent to the Align Right command). |
| __|__ (pipe) | ⌘ __|__ |  | Center-align a selection (equivalent to the Align Center command). |
| __:__ (colon) | ⌘ __:__ |  | Display the Spelling window (equivalent to the Spelling command). |
| __;__ (semicolon) | ⌘ __;__ |  | Find misspelled words in the document (equivalent to the Check Spelling command). |
| __,__ (comma) | ⌘ __,__ |  | Open the application's preferences window (equivalent to the Preferences command). |
| __,__ (comma) | ⌥ ⌃ ⌘ __,__ |  | Decrease screen contrast. |
| __.__ (period) | ⌥ ⌃ ⌘ __.__ |  | Increase screen contrast. |
| __?__ (question mark) | ⌘ __?__ |  | Open the application's help in Help Viewer. |
| __/__ (forward slash) | ⌥ ⌘ __/__ |  | Turn font smoothing on or off. |
| __=__ (equal sign) | ⇧ ⌘ __=__ |  | Increase the size of the selected item (equivalent to the Bigger command). |
| __=__ (equal sign) | ⌥ ⌘ __=__ |  | Zoom in when screen zooming is on. |
| __3__ | ⇧ ⌘ __3__ |  | Capture the screen to a file. |
| __3__ | ⇧ ⌃ ⌘ __3__ |  | Capture the screen to the Clipboard. |
| __4__ | ⇧ ⌘ __4__ |  | Capture a selection to a file. |
| __4__ | ⇧ ⌃ ⌘ __4__ |  | Capture a selection to the Clipboard. |
| __8__ | ⌥ ⌘ __8__ |  | Turn screen zooming on or off. |
| __8__ | ⌥ ⌃ ⌘ __8__ |  | Invert the screen colors. |
| __A__ | ⌘ __A__ |  | Highlight every item in a document or window, or all characters in a text field (equivalent to the Select All command). |
| __B__ | ⌘ __B__ |  | Boldface the selected text or toggle boldfaced text on and off (equivalent to the Bold command). |
| __C__ | ⌘ __C__ |  | Duplicate the selected data and store on the Clipboard (equivalent to the Copy command). |
| __C__ | ⇧ ⌘ __C__ |  | Display the Colors window (equivalent to the Show Colors command). |
| __C__ | ⌥ ⌘ __C__ |  | Copy the style of the selected text (equivalent to the Copy Style command). |
| __C__ | ⌃ ⌘ __C__ |  | Copy the formatting settings of the selected item and store on the Clipboard (equivalent to the Copy Ruler command). |
| __D__ | ⌥ ⌘ __D__ |  | Show or hide the Dock. |
| __D__ | ⌘ ⌃ __D__ |  | Display the definition of the selected word in the Dictionary application. |
| __E__ | ⌘ __E__ |  | Use the selection for a find operation. |
| __F__ | ⌘ __F__ |  | Open a Find window (equivalent to the Find command). |
| __F__ | ⌥ ⌘ __F__ |  | Jump to the search field control. |
| __G__ | ⌘ __G__ |  | Find the next occurrence of the selection (equivalent to the Find Next command). |
| __G__ | ⇧ ⌘ __G__ |  | Find the previous occurrence of the selection (equivalent to the Find Previous command). |
| __H__ | ⌘ __H__ |  | Hide the windows of the currently running application (equivalent to the Hide _ApplicationName_ command). |
| __H__ | ⌥ ⌘ __H__ |  | Hide the windows of all other running applications (equivalent to the Hide Others command). |
| __I__ | ⌘ __I__ |  | Italicize the selected text or toggle italic text on or off (equivalent to the Italic command). |
| __I__ | ⌘ __I__ |  | Display an Info window. |
| __I__ | ⌥ ⌘ __I__ |  | Display an inspector window. |
| __J__ | ⌘ __J__ |  | Scroll to a selection. |
| __M__ | ⌘ __M__ |  | Minimize the active window to the Dock (equivalent to the Minimize command). |
| __M__ | ⌥ ⌘ __M__ |  | Minimize all windows of the active application to the Dock (equivalent to the Minimize All command). |
| __N__ | ⌘ __N__ |  | Open a new document (equivalent to the New command). |
| __O__ | ⌘ __O__ |  | Display a dialog for choosing a document to open (equivalent to the Open command). |
| __P__ | ⌘ __P__ |  | Display the Print dialog (equivalent to the Print command). |
| __P__ | ⇧ ⌘ __P__ |  | Display a dialog for specifying printing parameters (equivalent to the Page Setup command). |
| __Q__ | ⌘ __Q__ |  | Quit the application (equivalent to the Quit command). |
| __Q__ | ⇧ ⌘ __Q__ |  | Log out the current user (equivalent to the Log Out command). |
| __Q__ | ⇧ ⌥ ⌘ __Q__ |  | Log out the current user without confirmation. |
| __S__ | ⌘ __S__ |  | Save the active document (equivalent to the Save command). |
| __S__ | ⇧ ⌘ __S__ |  | Display the Save dialog (equivalent to the Save As command). |
| __T__ | ⌘ __T__ |  | Display the Fonts window (equivalent to the Show Fonts command). |
| __T__ | ⌥ ⌘ __T__ |  | Show or hide a toolbar (equivalent to the Show/Hide Toolbar command). |
| __U__ | ⌘ __U__ |  | Underline the selected text or turn underlining on or off (equivalent to the Underline command). |
| __V__ | ⌘ __V__ |  | Insert the Clipboard contents at the insertion point (equivalent to the Paste command). |
| __V__ | ⌥ ⌘ __V__ |  | Apply the style of one object to the selected object (equivalent to the Paste Style command). |
| __V__ | ⌥ ⌘ ⌘ __V__ |  | Apply the style of the surrounding text to the inserted object (equivalent to the Paste and Match Style command). |
| __V__ | ⌃ ⌘ __V__ |  | Apply formatting settings to the selected object (equivalent to the Paste Ruler command). |
| __W__ | ⌘ __W__ |  | Close the active window (equivalent to the Close command). |
| __W__ | ⇧ ⌘ __W__ |  | Close a file and its associated windows (equivalent to the Close File command). |
| __W__ | ⌥ ⌘ __W__ |  | Close all windows in the application (equivalent to the Close All command). |
| __X__ | ⌘ __X__ |  | Remove the selection and store on the Clipboard (equivalent to the Cut command). |
| __Z__ | ⌘ __Z__ |  | Reverse the effect of the user's previous operation (equivalent to the Undo command). |
| __Z__ | ⇧ ⌘ __Z__ |  | Reverse the effect of the last Undo command (equivalent to the Redo command). |
| ⇢ (right arrow) | ⌘ ⇢ |  | Change the keyboard layout to current layout of Roman script. |
| ⇢ (right arrow) | ⇧ ⌘ ⇢ |  | Extend selection to the next semantic unit, typically the end of the current line. |
| ⇢ (right arrow) | ⇧ ⇢ |  | Extend selection one character to the right. |
| ⇢ (right arrow) | ⇧ ⌥ ⇢ |  | Extend selection to the end of the current word, then to the end of the next word. |
| ⇢ (right arrow) | ⌃ ⇢ |  | Move focus to another value or cell within a view, such as a table. |
| ⇠  (left arrow) | ⌘ ⇠ |  | Change the keyboard layout to current layout of system script. |
| ⇠  (left arrow) | ⇧ ⌘ ⇠ |  | Extend selection to the previous semantic unit, typically the beginning of the current line. |
| ⇠  (left arrow) | ⇧ ⇠ |  | Extend selection one character to the left. |
| ⇠  (left arrow) | ⇧ ⌥ ⇠ |  | Extend selection to the beginning of the current word, then to the beginning of the previous word. |
| ⇠  (left arrow) | ⌃ ⇠ |  | Move focus to another value or cell within a view, such as a table. |
| ⇡  (up arrow) | ⇧ ⌘ ⇡ |  | Extend selection upward in the next semantic unit, typically the beginning of the document. |
| ⇡  (up arrow) | ⇧ ⇡ |  | Extend selection to the line above, to the nearest character boundary at the same horizontal location. |
| ⇡  (up arrow) | ⇧ ⌥ ⇡ |  | Extend selection to the beginning of the current paragraph, then to the beginning of the next paragraph. |
| ⇡  (up arrow) | ⌃ ⇡ |  | Move focus to another value or cell within a view, such as a table. |
| ⇣  (down arrow) | ⇧ ⌘ ⇣ |  | Extend selection downward in the next semantic unit, typically the end of the document. |
| ⇣  (down arrow) | ⇧ ⇣ |  | Extend selection to the line below, to the nearest character boundary at the same horizontal location. |
| ⇣  (down arrow) | ⇧ ⌥ ⇣ |  | Extend selection to the end of the current paragraph, then to the end of the next paragraph (include the paragraph terminator, such as Return, in cut, copy, and paste operations). |
| ⇣  (down arrow) | ⌃ ⇣ |  | Move focus to another value or cell within a view, such as a table. |

[Next](Document%20Revision%20History.md)[Previous](Text%20Commands%20%28By%20Type%29.md)

