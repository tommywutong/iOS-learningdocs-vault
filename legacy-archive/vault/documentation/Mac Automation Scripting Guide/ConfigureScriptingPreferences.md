---
title: Mac Automation Scripting Guide
apple_id: TP40016239
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/ConfigureScriptingPreferences.html
archived_at: '2026-07-15T07:45:20.918259Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Mac Automation Scripting Guide](index.md)



## Configuring Scripting Preferences

Script Editor preferences allows you to configure a variety of aspects of scripting behavior.

### General Preferences

In the General pane of Script Editor preferences (Figure 9-1), you can configure settings such as the following.

__Figure 9-1__General pane of Script Editor preferences
![image: ../Art/script-editor_preferences_window_general_pane_2x.png](attachments/Art/script-editor_preferences_window_general_pane_2x.png)

__Default Language__—The default scripting language when you create new Script Editor documents.

__Show “tell” application menu__—This setting can be enabled to add a tell application menu to the navigation bar. Selecting an app in this menu allows you to direct script execution to the chosen app. In Figure 9-2, the tell application menu is set to the Finder. As a result, the script itself doesn’t need to include a `tell application "Finder"` statement. It automatically understands the Finder’s terminology and sends events to the Finder.

__Figure 9-2__The tell application menu in a Script Editor document
![image: ../Art/scripteditor_tellappmenu_2x.png](attachments/Art/scripteditor_tellappmenu_2x.png)

In addition, the current application object—which refers to the application currently executing the script—reflects the selected application, rather than Script Editor. See Listing 9-1 and Listing 9-2.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=name%20of%20current%20application)

__Listing 9-1__AppleScript: Targeting the current application object after setting the tell application menu in Script Editor to Finder

1. `name of current application`
2. `--> Result: "Finder"`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=Application.currentApplication%28%29.name%28%29)

__Listing 9-2__JavaScript: Targeting the current application object after setting the tell application menu in Script Editor to Finder

1. `Application.currentApplication().name()`
2. `// Result: "Finder"`

__Show inherited items__—This setting can be enabled to display inherited object properties in the dictionary viewer. For example, in the Finder, a `file` object inherits the attributes of an `item` object. Without this setting enabled, the dictionary entry for `file` simply provide a a pointer to the `item` entry to view the `item` attributes. See Figure 9-3. With this option enabled, the `file` entry in the Finder’s scripting dictionary includes the attributes of an `item`. See Figure 9-4.

__Figure 9-3__Dictionary entry without inherited items
![image: ../Art/scripteditor_dictionary_entrywithoutinheriteditems_2x.png](attachments/Art/scripteditor_dictionary_entrywithoutinheriteditems_2x.png)

__Figure 9-4__Dictionary entry with inherited items
![image: ../Art/scripteditor_dictionary_entrywithinheriteditems_2x.png](attachments/Art/scripteditor_dictionary_entrywithinheriteditems_2x.png)

__Script Menu__—These settings allow you to enable and configure a systemwide script menu (Figure 9-5). This menu can be used to organize your scripts and provide access to them in any app.

__Figure 9-5__The systemwide script menu
![image: ../Art/scriptmenu_2x.png](attachments/Art/scriptmenu_2x.png)

### Editing Preferences

In the Editing pane of Script Editor preferences, shown in Figure 9-6, you can configure settings such as the following.

__Figure 9-6__Editing pane of Script Editor preferences
![image: ../Art/script-editor_preferences_window_editing_pane_2x.png](attachments/Art/script-editor_preferences_window_editing_pane_2x.png)

__Code completion__—When this option is enabled, Script Editor suggest code completions as you type a script (Figure 9-7).

__Figure 9-7__Code completion in Script Editor
![image: ../Art/scripteditor_codecompletion1_2x.png](attachments/Art/scripteditor_codecompletion1_2x.png)

To accept and insert a code completion suggestion, press the F5 key or the Esc (Escape) key. If multiple code completion choices are available, a code completion dialog appears, allowing you to select a suggestion (see Figure 9-8).

__Figure 9-8__The code completion dialog in Script Editor
![image: ../Art/scripteditor_codecompletion2_2x.png](attachments/Art/scripteditor_codecompletion2_2x.png)

__Tab width and line wrapping__—Adjust how indentation and line wrapping occurs in the editor pane of Script Editor documents.

__Escape tabs and line breaks in strings__—This setting only affects AppleScripts. When this option is disabled, tabs and line breaks appear normally in a text string, as shown in Figure 9-9.

__Figure 9-9__A string containing normal tabs and line breaks
![image: ../Art/scripteditor_nonescapedtabsandlinebreaks_example_2x.png](attachments/Art/scripteditor_nonescapedtabsandlinebreaks_example_2x.png)

When this option is enabled, tabs and line breaks are replaced with escaped character equivalents—`/t` for a tab, and `/r` for a line break. See Figure 9-10.

__Figure 9-10__A string containing escaped tabs and line breaks
![image: ../Art/scripteditor_escapedtabsandlinebreaks_example_2x.png](attachments/Art/scripteditor_escapedtabsandlinebreaks_example_2x.png)

### Formatting Preferences

In the Formatting pane of Script Editor window (Figure 9-11), you can configure the style—font, point size, and color—of various script attributes, including new text, language keywords, comments, and variables. Formatting options are language-specific. Select a language from the Language popup menu to view that language’s formatting settings.

__Figure 9-11__Formatting pane of Script Editor preferences
![image: ../Art/script-editor_preferences_window_formatting_pane_2x.png](attachments/Art/script-editor_preferences_window_formatting_pane_2x.png)

### History Preferences

In the History pane of Script Editor preferences (Figure 9-12), you can enable or disable the log history, adjust the quantity of log history entries, and enable logging only when the log is visible.

__Figure 9-12__History pane of Script Editor preferences
![image: ../Art/script-editor_preferences_window_history_pane_2x.png](attachments/Art/script-editor_preferences_window_history_pane_2x.png)

### Plug-ins Preferences

The Plug-ins pane of Script Editor preferences (Figure 9-13) lists any installed Script Editor plug-ins.

__Figure 9-13__Plug-ins pane of Script Editor preferences
![image: ../Art/script-editor_preferences_window_plugins_pane_2x.png](attachments/Art/script-editor_preferences_window_plugins_pane_2x.png)

[Running a Script](RunaScript.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqmjufvjvomi)

[About Scripting Terminology](AboutScriptingTerminology.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqnzvfvjvomq)
