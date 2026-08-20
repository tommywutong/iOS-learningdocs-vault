---
title: Shark User Guide
apple_id: TP40005233
resource_type: Guide
platform: iOS|macOS
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SharkUserGuide/CommandReference/CommandReference.html
archived_at: '2026-07-15T07:25:57.334480Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Shark User Guide](Introduction.md)


[Next](Miscellaneous%20Topics.md)[Previous](Hardware%20Counter%20Configuration.md)

# Command Reference

This section summarizes Shark’s commands, arranged by menu.

This menu contains the usual application-menu commands.

| Command | Shortcut | Description | Where Described |
| --- | --- | --- | --- |
| About Shark... |  | See revision information for Shark. |  |
| Preferences... | Cmd-, | Edit some global Shark parameters. | [Shark Preferences](Getting%20Started%20with%20Shark.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmrnknltk) |
| Hide Shark | Cmd-H | Hides Shark's window(s) and switches to the next-frontmost application. |  |
| Hide Others | Opt-Cmd-H | Hides all other applications' windows. |  |
| Show All |  | Restores all windows hidden with the previous two commands. |  |
| Quit Shark | Cmd-Q | Quits Shark. |  |

This menu contains commands that control the processing of Shark’s session files. Most are fairly standard File operations, but there are a few commands here that are unique to Shark and described further in the sections noted below.

| Command | Shortcut | Description | Where Described |
| --- | --- | --- | --- |
| Open | Cmd-O | Open a saved session. |  |
| Open Recent ► |  | Contains a list of recently used saved sessions — choose one to open it. |  |
| Close | Cmd-W | Close the frontmost window. If the frontmost window is the main control window, this will quit Shark. |  |
| Close All | Opt-Cmd-W | Close all session windows. |  |
| Save | Cmd-S | Save the frontmost session. | [Session Files](Getting%20Started%20with%20Shark.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmrnknltm) |
| Save As... | Shift-Cmd-S | Save the frontmost session to a new location. | [Session Files](Getting%20Started%20with%20Shark.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmrnknltm) |
| Mail This Session |  | Attach a copy of the frontmost session to a new email in your default email program. | [Session Files](Getting%20Started%20with%20Shark.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmrnknltm) |
| Compare... | Opt-Cmd-C | Compare two saved sessions. | [Comparing Sessions](Advanced%20Session%20Management%20and%20Data%20Mining.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqnznknltina) |
| Merge... | Opt-Cmd-M | Merge two saved sessions. | [Merging Sessions](Advanced%20Session%20Management%20and%20Data%20Mining.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqnznknltini) |
| Get Info | Cmd-I | Opens the Info sheet for the frontmost session. | [Session Information Sheet](Getting%20Started%20with%20Shark.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmrnknltcmi) |
| Symbolicate... | Opt-Cmd-S | Add symbols to the frontmost session from a symbol-rich copy of the target application on disk. | [Manual Session Symbolication](Advanced%20Session%20Management%20and%20Data%20Mining.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqnznknltg) |
| Generate Report... | Cmd-J | Create a plain text summary of highlights from the frontmost session. | [Session Report](Getting%20Started%20with%20Shark.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmrnknltcmq) |
| Page Setup... | Shift-Cmd-P | Configure printers and print settings. |  |
| Print... | Cmd-P | Print the frontmost window. |  |

All items in this menu are standard text editing items. They work generally as expected when you are editing or examining text in Shark, and the cut/copy/paste commands will also work with some higher-level objects.

| Command | Shortcut | Description |
| --- | --- | --- |
| Undo | Cmd-Z | Undo the previous action. |
| Redo | Shift-Cmd-Z | Redo the next action. |
| Cut | Cmd-X | Cut the selected text, placing it on the clipboard. |
| Copy | Cmd-C | Copy the selected text to the clipboard. |
| Paste | Cmd-V | Paste the contents of the clipboard. |
| Paste and Match Style | Opt-Shift-Cmd-V | Paste the contents of the clipboard using the same style as existing text. |
| Select All | Cmd-A | Select all of whatever was most recently selected (samples, text, etc.). |
| Find ► |  |  |
| Find... | Cmd-F | Open the Find text window. |
| Find Next | Cmd-G | Find the next occurrence of the text search pattern. |
| Find Previous | Shift-Cmd-G | Find the previous occurrence of the text search pattern. |
| Spelling ► |  |  |
| Show Spelling and Grammar | Cmd-: | Open the Spelling and Grammar palette. |
| Check Spelling | Cmd-; | Check the spelling within the current text field, opening the Spelling and Grammar palette to highlight suspected errors. |
| Check Spelling while Typing |  | If ticked, spelling is checked as it is typed. Suspected errors are underlined. |
| Speech ► |  |  |
| Start Speaking |  | Start speaking the selected text, if any, or else the contents of the current text field. |
| Stop Speaking |  | Stop speaking. |
| Special Characters... | Opt-Cmd-T | Open the character palette, to access special characters and symbols. |

All items in this menu are standard text processing commands. Since it is generally not possible to apply custom formats to most text within Shark, this menu is seldom used.

| Command | Shortcut | Description |
| --- | --- | --- |
| Font ► |  |  |
| Show Fonts | Cmd-T | Show the Font palette. |
| Bold | Cmd-B | Toggle the bold attribute of the selected text. |
| Italic |  | Toggle the italic attribute of the selected text. |
| Underline | Cmd-U | Toggle the underline attribute of the selected text. |
| Bigger | Cmd-+ | Increase the font size of the selected text. |
| Smaller | Cmd-- | Decrease the font size of the selected text. |
| Show Colors |  | Show the color picker palette. |
| Copy Style |  | Copy the style of the selected text to the clipboard. |
| Paste Style | Opt-Cmd-V | Apply the style information on the clipboard to the selected text. |
| Text ► |  |  |
| Align Left | Cmd-{ | Align the current line or selected text to the left margin. |
| Center | Cmd-| | Center the current line or selected text. |
| Justify |  | Align the current line or selected text justified across the page. |
| Align Right | Cmd-} | Align the current line or selected text to the right margin. |
| Show Ruler |  | Show the ruler and text editing tools for the current text view. |
| Copy Ruler | Ctrl-Cmd-C | Copy the current ruler configuration to the clipboard. |
| Paste Ruler | Ctrl-Cmd-V | Paste the current ruler configuration from the clipboard. |

This menu contains commands that allow you to adjust Shark’s built-in configurations to match your needs. These are described further in [Custom Configurations](Custom%20Configurations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqobnknltc) and [Hardware Counter Configuration](Hardware%20Counter%20Configuration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmjqfvjvomi), in the sections noted below.

| Command | Shortcut | Description | Where Described |
| --- | --- | --- | --- |
| Show/Hide Mini Config Editor | Shift-Cmd-C | Show/Hide the mini config editor attached to the main control window. | [Mini Configuration Editors](Getting%20Started%20with%20Shark.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmrnknltcma) |
| Edit... | Opt-Shift-Cmd-C | Edit the current configuration. | [The Config Editor](Custom%20Configurations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqobnknltcmy) |
| New... | Cmd-N | Create a new configuration. | [The Config Editor](Custom%20Configurations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqobnknltcmy) |
| Export... |  | Export the current configuration to a file. | [The Config Editor](Custom%20Configurations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqobnknltcmy) |
| Import... |  | Import a configuration from a file. | [The Config Editor](Custom%20Configurations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqobnknltcmy) |

This menu contains commands that modify when Shark starts and stops profiling and tracing operations. These are described further in [Advanced Profiling Control](Advanced%20Profiling%20Control.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmjtfvjvomjv), in the sections noted below.

| Command | Shortcut | Description | Where Described |
| --- | --- | --- | --- |
| Programmatic (Remote) | Shift-Cmd-R | Causes Shark to listen for programmatic start/stop commands. It will then take sessions using the currently selected configuration. | [Interprocess Remote Control](Advanced%20Profiling%20Control.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmjtfvjvomjx) |
| Unresponsive Applications | Shift-Cmd-A | Using the currently selected configuration, Shark automatically profiles all applications which become unresponsive. Automatically activates Batch Mode when used. | [Unresponsive Application Measurements](Advanced%20Profiling%20Control.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmjtfvjvomrq) |
| Batch Mode | Shift-Cmd-B | Toggles Batch mode, allowing the recording of multiple sessions before analysis begins. Automatically enabled when Unresponsive Applications is ticked. | [Batch Mode](Advanced%20Profiling%20Control.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmjtfvjvomq) |
| Network/iPhone Profiling... | Shift-Cmd-N | Enable Network Profiling of other computers or iPhones, instead of local profiling, or share this computer for others to profile. | [Network/iPhone Profiling](Advanced%20Profiling%20Control.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmjtfvjvomjz) |

This menu, which disappears when data mining is not possible, provides access to Shark’s powerful symbol-level data mining capabilities. These are described in more detail in [Data Mining](Advanced%20Session%20Management%20and%20Data%20Mining.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqnznknltc).

| Command | Shortcut | Description |
| --- | --- | --- |
| Charge Symbol to Callers | Cmd-E | Add the cost of the selected symbol(s) to their caller(s), and hide the selected symbol(s). |
| Charge Library to Callers | Shift-Cmd-E | Add the cost of all calls to the selected library(ies) to their caller(s), and hide the selected library(ies). |
| Flatten Library | Shift-Cmd-F | Just hide the selected library(ies), without adding time to the callers. |
| Remove Callstacks with Symbol | Cmd-K | Hide all callstacks which contain the selected symbol(s). |
| Retain Callstacks with Symbol | Shift-Cmd-K | Keep visible all callstacks which contain the selected symbol(s). Callstacks retained in this way will not be hidden even if they contain symbols that are used with "Remove Callstacks with Symbol". |
| Restore All | Cmd-R | Show all symbols and libraries previously hidden by "Charge Symbol to Callers", "Charge Library to Callers" or "Remove Callstacks with Symbol", and restore original costs for all symbols. |
| Focus Symbol | Cmd-Y | Hide all except the selected symbol(s). |
| Focus Library | Shift-Cmd-Y | Hide all except the selected library(ies). |
| Focus Callers of Symbol | Opt-Cmd-Y | Hide all except the caller(s) of the selected symbol(s). |
| Focus Callers of Library | Opt-Shift-Cmd-Y | Hide all except the caller(s) of the selected library(ies). |
| Unfocus All |  | Show all symbols and libraries previously hidden by any of the Focus commands. |

Along with standard window control functionality, this contains the command to show or hide the _Advanced Settings_ drawer on the right side of each session window, as described in [Advanced Settings Drawer](Getting%20Started%20with%20Shark.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmrnknlts).

| Command | Shortcut | Description |
| --- | --- | --- |
| Minimize | Cmd-M | Minimise the frontmost window. |
| Minimize All |  | Minimise all Shark windows. |
| Zoom |  | Zoom the frontmost window. |
| Show Advanced Settings | Shift-Cmd-M | Toggle visibility of the advanced settings drawer of the frontmost session. |
| Bring All to Front |  | Bring all Shark windows to the front. |

This menu provides access to Shark’s online documentation, which is what you are reading! It also provides access to instruction reference manuals for PowerPC, 32-bit x86, and 64-bit x86 instructions, through the viewer described in [ISA Reference Window](Time%20Profiling.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmznknlto).

| Command | Shortcut | Description |
| --- | --- | --- |
| Shark Help | Cmd-? | Show the Shark User Guide (PDF). |
| PowerPC ISA Reference |  | Show the PowerPC Instruction Set Architecture Reference. |
| IA32 ISA Reference |  | Show the IA32 Instruction Set Architecture Reference. |
| EM64T ISA Reference |  | Show the EM64T Instruction Set Architecture Reference. |
| Acknowledgements |  | Show acknowledgements for open-source materials used in Shark. |

This section summarizes Shark’s unique commands, arranged alphabetically. Common text editing commands have been omitted from this table.

| Command | Shortcut | Description | Where Described | Menu |
| --- | --- | --- | --- | --- |
| Batch Mode | Shift-Cmd-B | Toggles Batch mode, allowing the recording of multiple sessions before analysis begins. Automatically enabled when Unresponsive Applications is ticked. | [Batch Mode](Advanced%20Profiling%20Control.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmjtfvjvomq) | Sampling |
| Charge Library to Callers | Shift-Cmd-E | Add the cost of all calls to the selected library(ies) to their caller(s), and hide the selected library(ies). | [Data Mining](Advanced%20Session%20Management%20and%20Data%20Mining.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqnznknltc) | Data Mining |
| Charge Symbol to Callers | Cmd-E | Add the cost of the selected symbol(s) to their caller(s), and hide the selected symbol(s). | [Data Mining](Advanced%20Session%20Management%20and%20Data%20Mining.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqnznknltc) | Data Mining |
| Compare... | Opt-Cmd-C | Compare two saved sessions. | [Comparing Sessions](Advanced%20Session%20Management%20and%20Data%20Mining.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqnznknltina) | File |
| Edit... | Opt-Shift-Cmd-C | Edit the current configuration. | [The Config Editor](Custom%20Configurations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqobnknltcmy) | Config |
| EM64T ISA Reference |  | Show the EM64T Instruction Set Architecture Reference. | [ISA Reference Window](Time%20Profiling.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmznknlto) | Help |
| Export... |  | Export the current configuration to a file. | [The Config Editor](Custom%20Configurations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqobnknltcmy) | Config |
| Flatten Library | Shift-Cmd-F | Just hide the selected library(ies), without adding time to the callers. | [Data Mining](Advanced%20Session%20Management%20and%20Data%20Mining.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqnznknltc) | Data Mining |
| Focus Callers of Library | Opt-Shift-Cmd-Y | Hide all except the caller(s) of the selected library(ies). | [Data Mining](Advanced%20Session%20Management%20and%20Data%20Mining.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqnznknltc) | Data Mining |
| Focus Callers of Symbol | Opt-Cmd-Y | Hide all except the caller(s) of the selected symbol(s). | [Data Mining](Advanced%20Session%20Management%20and%20Data%20Mining.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqnznknltc) | Data Mining |
| Focus Library | Shift-Cmd-Y | Hide all except the selected library(ies). | [Data Mining](Advanced%20Session%20Management%20and%20Data%20Mining.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqnznknltc) | Data Mining |
| Focus Symbol | Cmd-Y | Hide all except the selected symbol(s). | [Data Mining](Advanced%20Session%20Management%20and%20Data%20Mining.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqnznknltc) | Data Mining |
| Generate Report... | Cmd-J | Create a plain text summary of highlights from the frontmost session. | [Session Report](Getting%20Started%20with%20Shark.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmrnknltcmq) | File |
| Get Info | Cmd-I | Opens the Info sheet for the frontmost session. | [Session Information Sheet](Getting%20Started%20with%20Shark.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmrnknltcmi) | File |
| IA32 ISA Reference |  | Show the IA32 Instruction Set Architecture Reference. | [ISA Reference Window](Time%20Profiling.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmznknlto) | Help |
| Import... |  | Import a configuration from a file. | [The Config Editor](Custom%20Configurations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqobnknltcmy) | Config |
| Mail This Session |  | Attach a copy of the frontmost session to a new email in your default email program. | [Session Files](Getting%20Started%20with%20Shark.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmrnknltm) | File |
| Merge... | Opt-Cmd-M | Merge two saved sessions. | [Merging Sessions](Advanced%20Session%20Management%20and%20Data%20Mining.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqnznknltini) | File |
| Network/iPhone Profiling... | Shift-Cmd-N | Enable Network Profiling of other computers or iPhones, instead of local profiling, or share this computer for others to profile. | [Network/iPhone Profiling](Advanced%20Profiling%20Control.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmjtfvjvomjz) | Sampling |
| New... | Cmd-N | Create a new configuration. | [The Config Editor](Custom%20Configurations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqobnknltcmy) | Config |
| PowerPC ISA Reference |  | Show the PowerPC Instruction Set Architecture Reference. | [ISA Reference Window](Time%20Profiling.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmznknlto) | Help |
| Preferences... | Cmd-, | Edit some global Shark parameters. | [Shark Preferences](Getting%20Started%20with%20Shark.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmrnknltk) | Shark |
| Programmatic (Remote) | Shift-Cmd-R | Causes Shark to listen for programmatic start/stop commands. It will then take sessions using the currently selected configuration. | [Interprocess Remote Control](Advanced%20Profiling%20Control.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmjtfvjvomjx) | Sampling |
| Remove Callstacks with Symbol | Cmd-K | Hide all callstacks which contain the selected symbol(s). | [Data Mining](Advanced%20Session%20Management%20and%20Data%20Mining.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqnznknltc) | Data Mining |
| Restore All | Cmd-R | Show all symbols and libraries previously hidden by "Charge Symbol to Callers", "Charge Library to Callers" or "Remove Callstacks with Symbol", and restore original costs for all symbols. | [Data Mining](Advanced%20Session%20Management%20and%20Data%20Mining.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqnznknltc) | Data Mining |
| Retain Callstacks with Symbol | Shift-Cmd-K | Keep visible all callstacks which contain the selected symbol(s). Callstacks retained in this way will not be hidden even if they contain symbols that are used with "Remove Callstacks with Symbol". | [Data Mining](Advanced%20Session%20Management%20and%20Data%20Mining.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqnznknltc) | Data Mining |
| Shark Help | Cmd-? | Show the Shark User Guide (PDF). |  | Help |
| Show Advanced Settings | Shift-Cmd-M | Toggle visibility of the advanced settings drawer of the frontmost session. | [Advanced Settings Drawer](Getting%20Started%20with%20Shark.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmrnknlts) | Window |
| Show/Hide Mini Config Editor | Shift-Cmd-C | Show/Hide the mini config editor attached to the main control window. | [Mini Configuration Editors](Getting%20Started%20with%20Shark.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmrnknltcma) | Config |
| Symbolicate... | Opt-Cmd-S | Add symbols to the frontmost session from a symbol-rich copy of the target application on disk. | [Manual Session Symbolication](Advanced%20Session%20Management%20and%20Data%20Mining.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqnznknltg) | File |
| Unfocus All |  | Show all symbols and libraries previously hidden by any of the Focus commands. | [Data Mining](Advanced%20Session%20Management%20and%20Data%20Mining.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqnznknltc) | Data Mining |

[Next](Miscellaneous%20Topics.md)[Previous](Hardware%20Counter%20Configuration.md)

