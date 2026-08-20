---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/WorkingwithSymbols.html
archived_at: '2026-07-27T06:57:07.964311Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](AnalyzingYourCode.md)[Previous](SearchandReplace.md)

## Working with Symbols

### Display the Definition of a Symbol

Place the pointer over a symbol and Command-click to display the symbol definition. The source editor navigates to the symbol definition and highlights it. If the definition is in a separate file, the source editor displays that file. (Alternatively, place the pointer over a symbol and choose Navigate > Jump to Definition.)

Place the pointer over a symbol, and Option-Command-click to display its definition in the assistant editor pane, as illustrated for the `APALoadFramesFromAtlas` function in the screenshot. This approach lets you keep the symbol in view as you inspect its definition.

（原归档配图获取待重试：`OptionCommandClickforAssistant_2x.png`）

### Look Up Documentation for a Symbol

Find concise reference documentation for a symbol, such as a method or property, by placing the insertion point in the symbol. Click the Quick Help button (（原归档配图获取待重试：`QuickHelp_2x.png`）) in the inspector pane toolbar. If the inspector pane is not open, in the main toolbar click the button to show the navigator in the workspace configuration button set. Quick Help for that symbol appears in the utilities area.

The information includes links to complete reference documentation for the symbol, the header file where the symbol is declared, related programming guides, and related sample code. (To view summary information in a pop-up window—the declaration, a description of the symbol, any return value, its release availability, header file, and a link to its related reference document—Option-click the symbol.)

（原归档配图获取待重试：`QuickHelpArea_2x.png`）

Click a link in Quick Help, and Xcode opens a separate Xcode document viewer window. The Xcode document viewer provides access to information without taking your focus away from the file you’re editing.

（原归档配图获取待重试：`APIRefWithMetaData_2x.png`）

The document viewer delivers in-depth programming guides, tutorials, sample code, and video presentations by Apple engineers, in addition to detailed framework API references. From a class reference, click “More related items” near the top of the viewer for links to additional documents relevant to your programming task.

（原归档配图未能恢复：`RelatedItems_2x.png`）

Use the search field in the toolbar to locate additional information about the API or programming concept.

（原归档配图获取待重试：`DocViewer_2x.png`）

To include a link to the document in a message, click the Share button (（原归档配图获取待重试：`ShareButtonIcon_2x.png`）) and choose Email Link or Message. You can open the document in Safari in HTML or PDF format from this menu. For a sample code project, click Open Project at the top of the window to download the project and open it in Xcode.

（原归档配图获取待重试：`ShareButton_2x.png`）

[Search and Replace](SearchandReplace.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmzwfvjvomi)

[Analyzing Your Code](AnalyzingYourCode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmzyfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](AnalyzingYourCode.md)[Previous](SearchandReplace.md)
