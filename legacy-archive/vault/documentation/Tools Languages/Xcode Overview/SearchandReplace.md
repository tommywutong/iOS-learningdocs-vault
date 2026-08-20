---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/SearchandReplace.html
archived_at: '2026-07-27T06:57:07.956949Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](WorkingwithSymbols.md)[Previous](EditingSourceCode.md)

## Search and Replace

Xcode offers several approaches to making changes that apply to multiple lines of text.

### Searching in a File

Change instances of a text string in a single file by choosing Find > Find and Replace.

（原归档配图获取待重试：`FindReplaceFile_2x.png`）

### Editing All Symbols

You can simultaneously modify all the occurrences of a symbol, such as the name of a local variable or parameter, within a scope. Place the insertion point in the symbol you want to edit. When the disclosure triangle appears, click it to display the menu, and choose Edit All in Scope. Edit the symbol. As you type new text, all instances of the symbol change simultaneously.

（原归档配图获取待重试：`EditInScope_2x.png`）

### Searching the Project

Change instances of a text string in your project or workspace by choosing Find > Find and Replace in Project. This command displays the find navigator. You can customize the operation—for example, to limit the scope of the search or to match the case of letters in the string. The find navigator provides a preview that allows you to replace all instances of the string or to accept or reject individual replacements.

（原归档配图未能恢复：`SearchReplaceProject_2x.png`）

### Using Wildcards

You can use wildcard string patterns in the search field. To enter a component of a pattern, click the disclosure triangle on the left of the find string field and choose Insert Pattern. Choose a component from the pop-up menu of patterns. Xcode inserts the wildcard at the current location of the cursor in the find string.

（原归档配图获取待重试：`WildcardSearchStrings.png`）

### Refactoring Code

You can refactor your code to improve its structure, readability, and maintainability without changing its behavior. A refactoring operation (also called a _transformation_) is applied to a code fragment or a symbol that you select in the source editor. You can rename symbols, extract code into methods, create superclasses, move items up to the superclasses or down to their subclasses, and encapsulate variables throughout your project files.

After selecting the code fragment or symbol you want to refactor, choose Edit > Refactor and then choose the appropriate refactoring command. A preview pane shows you how each change will appear when applied. Deselect a file in the leftmost pane of the preview dialog to leave it out of the refactoring operation. You can edit your source code directly in the preview. Any such edits are shown in the preview and are included in the refactoring operation.

（原归档配图获取待重试：`RefactorRename_2x.png`）

[Editing Source Code](EditingSourceCode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmzufvjvomi)

[Working with Symbols](WorkingwithSymbols.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmzxfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](WorkingwithSymbols.md)[Previous](EditingSourceCode.md)
