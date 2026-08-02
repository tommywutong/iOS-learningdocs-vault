---
title: Mac Automation Scripting Guide
apple_id: TP40016239
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/UsetheSystem-WideScriptMenu.html
archived_at: '2026-07-15T07:46:26.687783Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Mac Automation Scripting Guide](index.md)



## Using the Systemwide Script Menu

The OS X script menu provides quick access to your collection of scripts. Simply select a script in the menu at any time to run it instantly. Within the script menu, scripts can be organized into subfolders and by application. See Figure 41-1.

__Figure 41-1__The OS X script menu
![image: ../Art/scriptmenu_2x.png](attachments/Art/scriptmenu_2x.png)

> [!NOTE]
> 

### Enabling the Script Menu

The script menu is disabled by default in OS X.

__To enable the script menu__

1. Launch Script Editor, located in `/Applications/Utilities/`.
2. Select Script Editor > Preferences, or press Command-Comma (,), to open the preferences window.
3. Click General in the toolbar.
4. Enable the “Show Script menu in menu bar” checkbox.
5. Choose whether application scripts—scripts that appear only when a corresponding app is in the front—should appear at the top or bottom of the script menu.

   ![image: ../Art/scripteditor_scriptmenu_preferences_2x.png](attachments/Art/scripteditor_scriptmenu_preferences_2x.png)

> [!TIP]
> 

### Adding User-Level Scripts to the Script Menu

User-level scripts are scripts that only you can see and use. They aren’t available to other users on your Mac.

To add user-level scripts to the script menu, save them into the `~/Library/Scripts/` folder of your user directory. For quick access to this folder, select Open Scripts Folder > Open User Scripts Folder from the script menu. When you do this, the folder is automatically created if it doesn’t already exist.

### Adding Computer-Level Scripts to the Script Menu

Computer-level scripts are scripts that any user on your Mac can see and use.

To add computer-level scripts to the script menu, save them into the `/Library/Scripts/` folder on your Mac. For quick access to this folder, select Open Scripts Folder > Open Computer Scripts Folder from the script menu. When you do this, the folder is automatically created if it doesn’t already exist.

### Adding Application-Specific Scripts to the Script Menu

Application-specific scripts are only visible in the script menu when a specific app is in the front.

To add application-specific scripts to the script menu, save them into the `~/Library/Scripts/Applications/«ApplicationName»` folder in your user directory or the `/Library/Scripts/Applications/«ApplicationName»` folder on your Mac. For quick access to this folder, bring the app to the front, then select Open Scripts Folder > Open «ApplicationName» Scripts Folder from the script menu. When you do this, a folder for the application is automatically created if it doesn’t already exist.

### Running Scripts in the Script Menu

Select a script from the script menu to run it. If the script is an application, it launches and runs normally. If the script is a compiled script, a progress indicator appears in the menu bar. See Figure 41-2.

__Figure 41-2__Script menu progress
![image: ../Art/scriptmenu_progress_2x.png](attachments/Art/scriptmenu_progress_2x.png)

> [!NOTE]
> 

[Making a Systemwide Service](MakeaSystem-WideService.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqnbwfvjvomi)

[Using Dictation to Run Scripts](UseDictationtoRunScripts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqobxfvjvomi)
