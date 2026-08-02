---
title: Mac Automation Scripting Guide
apple_id: TP40016239
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/CreateaScript.html
archived_at: '2026-07-15T07:45:28.479915Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Mac Automation Scripting Guide](index.md)



## Creating a Script

Generally, most scripts are written in Script Editor documents. Scripts can also be written in Xcode, but this is typically for scripts that require advanced user interfaces.

__To write a script in Script Editor__

1. Launch Script Editor in `/Applications/Utilities/`.
2. Press Command-N or select File > New.
3. If the script isn’t configured for the correct language, choose the language in the navigation bar.

   ![image: ../Art/script-editor_langage_selector_2x.png](attachments/Art/script-editor_langage_selector_2x.png)

   > [!TIP]
   > 
4. Write your script code in the editing area. Newly written code is uncompiled and formatted as new text.

   ![image: ../Art/scripteditor_uncompiledscript_2x.png](attachments/Art/scripteditor_uncompiledscript_2x.png)
5. Click the Compile button (![image: ../Art/icon_compilescript_2x.png](attachments/Art/icon_compilescript_2x.png)) to compile the script and check for syntax errors.

   If a syntax error occurs, an alert is displayed.

   ![image: ../Art/scripteditor_syntaxerror_2x.png](attachments/Art/scripteditor_syntaxerror_2x.png)

   If the script compiles, code formatting is applied at this time.

   ![image: ../Art/scripteditor_compiledscript_2x.png](attachments/Art/scripteditor_compiledscript_2x.png)

> [!TIP]
> 

### Using an AppleScript Template

Script Editor includes a number of built-in templates for creating common types of AppleScripts, including droplets, Mail rule scripts, and Messages handler scripts.

> [!NOTE]
> 

__To create a template-based script__

1. Launch Script Editor in `/Applications/Utilities/`.
2. Choose File > New from Template.

   ![image: ../Art/scripteditor_newtemplate_menu_2x.png](attachments/Art/scripteditor_newtemplate_menu_2x.png)
3. Select a script template.

   A new Script Editor document window opens containing prewritten code and preconfigured settings. The following screenshot shows an example of a script created using a template.

   ![image: ../Art/scripteditor_asoc_template_2x.png](attachments/Art/scripteditor_asoc_template_2x.png)
4. Customize the script.

[Getting to Know Script Editor](GettoKnowScriptEditor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqnjnknltc)

[Saving a Script](SaveaScript.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqmjtfvjvomi)
