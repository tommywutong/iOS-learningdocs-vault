---
title: Mac Automation Scripting Guide
apple_id: TP40016239
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/TypesofScripts.html
archived_at: '2026-07-15T07:46:18.169244Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Mac Automation Scripting Guide](index.md)



## Types of Scripts

There are many different types of scripts on the Mac.

![image: ../Art/icon_applet_48_2x.png](attachments/Art/icon_applet_48_2x.png)

__Applets__—A script that’s been saved as an app. It behaves like other apps. Double-click it to launch and run it. When an applet is launched, any code in its `run` handler executes. If a script doesn’t contain an explicit `run` handler, then the top level of the script is treated as an implicit `run` handler and any code there executes.

![image: ../Art/icon_droplet_48_2x.png](attachments/Art/icon_droplet_48_2x.png)

__Droplets__—A script applet that has been configured to accept dropped files and folders. Double-click it to launch and run it—execute its `run` handler. Or, drag and drop files and folders onto it to process them. In a droplet, dropped files and folders are passed directly to an AppleScript `open` handler or JavaScript `openDocuments` function for processing.

![image: ../Art/icon_compiled_48_2x.png](attachments/Art/icon_compiled_48_2x.png)

__Scripts__—A script document file. Double-click it to open it for editing. Some apps and processes can load and run scripts. For example, Mail rules can execute scripts to process messages matching specific criteria. Scripts are sometimes referred to as _compiled scripts_.

![image: ../Art/icon_compiled_48_2x.png](attachments/Art/icon_compiled_48_2x.png)

__Script bundles__—A script document that’s been saved in _bundle_ format. A bundle is a directory with a standardized, hierarchical structure that holds executable code and the resources used by that code.

![image: ../Art/icon_applet_48_2x.png](attachments/Art/icon_applet_48_2x.png)

__Stay-open scripts__—By default, applets and droplets run and quit after launch. When configured as stay-open, however, they remain open until explicitly ordered to quit. Often, stay-open scripts include an `idle` handler, which initiates periodic actions.

For detailed information about `run`, `open`, and `idle` handlers in AppleScript, see [Handlers in Script Applications](../Apple%20Script/AppleScript%20Language%20Guide/About%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqgywvgvzrgq) in _[AppleScript Language Guide](../Apple%20Script/AppleScript%20Language%20Guide/Introduction%20to%20AppleScript%20Language%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobt)_. For information about `run`, `openDocuments`, and `idle` functions in JavaScript, see [Applets](../../releasenotes/JavaScript%20for%20Automation%20Release%20Notes/OS%20X%2010.10%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dkmbyfvbuqmjqhewvgvzrgu) in _[JavaScript for Automation Release Notes](../../releasenotes/JavaScript%20for%20Automation%20Release%20Notes/Introduction%20to%20JavaScript%20for%20Automation%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dkmby)_. For information about bundles, see _[Bundle Programming Guide](../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_.

[How Mac Scripting Works](HowMacScriptingWorks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqnztfvjvomi)

[About this Guide](AboutthisGuide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqnzrfvjvomi)
