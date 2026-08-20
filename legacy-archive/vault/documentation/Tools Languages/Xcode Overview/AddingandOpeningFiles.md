---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/AddingandOpeningFiles.html
archived_at: '2026-07-27T06:57:07.941079Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](EditingSourceCode.md)[Previous](AlternativeToolchains.md)

## Opening and Adding Files

To view and edit a source file, select it in the project navigator. The file’s contents appear in the editor area of the workspace window.

（原归档配图未能恢复：`Projects_2x.png`）

### Creating Source Files from Templates

Use file templates to add files to your project with minimum effort. To access the File Template library, click the File Template button (（原归档配图未能恢复：`XC_O_library_file_templates_button_2x.png`）) in the utilities area of the workspace window. Create a source file by dragging its template to the project navigator.

（原归档配图获取待重试：`FileTemplate_2x.png`）

Alternatively, choose File > New File or press Command-N. Xcode brings up the New File dialog, where you can choose a template for your file. After choosing a template and pressing Next, you name the file and add it to your project.

（原归档配图未能恢复：`Menu_New_File_1_Template.png`）

（原归档配图未能恢复：`Menu_New_File_2_Name.png`）

### Opening a File Quickly

Choose File > Open Quickly to locate files that define a specified symbol or whose filenames contain a specified string. Open Quickly searches are case insensitive and are limited to the current project and to the active software development kit (SDK). From the search results list, double-click the file you want to open.

（原归档配图获取待重试：`OpenQuickly_2x.png`）

To open the file in the assistant editor pane, hold down the Option key when you double-click. To open the file in a separate window, press Option-Shift. To see a dialog letting you specify where the file should open, press Option-Shift-click.

### Splitting the Editor to Display Related Content

Split the editor pane to see multiple views of the same file or to view multiple related files at once. For example, you can simultaneously view an implementation file and its header file counterpart. To split the source editor, open an assistant editor pane by clicking the Assistant Editor button (（原归档配图未能恢复：`XC_O_editor_buttons_assistant_2x.png`）) in the workspace toolbar. The split can be vertical or horizontal.

（原归档配图未能恢复：`VerticalSplit_2x.png`）

（原归档配图获取待重试：`HorizontalAssistant_2x.png`）

To change the orientation of the split, choose View > Assistant Editor, and then choose one of the menu options. In both of the screenshots above, the navigator and utilities areas are closed to maximize the viewing area of the source editor.

### Setting the Assistant Editor Mode

When you open an assistant editor pane, you can set it to either of two modes: manual or tracking. In manual mode, you select the file to display by navigating to it in the jump bar. The contents of the assistant editor do not change as you change the contents of the main editor.

In tracking mode, you select a criterion from a pop-up menu. Criteria include include groupings such as counterparts, superclasses, subclasses, and siblings. Once you choose a criterion, Xcode lists the appropriate files in a submenu. As you change the file in the main editor, Xcode updates the assistant editor based on the selected criterion.

To change the mode, select one from the Assistant pop-up menu. (The Assistant pop-up menu is the first item to the right of the back and forward arrows in the assistant editor jump bar.)

（原归档配图未能恢复：`AssistantBehavior_2x.png`）

You can further split the assistant editor pane by clicking the Add button (（原归档配图获取待重试：`OpenAssistantPaneControl_2x.png`）) in the top-right corner of the assistant editor pane. The nearby close button (（原归档配图未能恢复：`CloseAssistantPaneControl_2x.png`）) closes it again.

（原归档配图获取待重试：`SplitAssistant_2x.png`）

[Using Alternative Toolchains](AlternativeToolchains.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnzwfvjvomi)

[Editing Source Code](EditingSourceCode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmzufvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](EditingSourceCode.md)[Previous](AlternativeToolchains.md)
