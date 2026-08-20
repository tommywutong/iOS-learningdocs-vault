---
title: Xcode 4 Transition Guide
apple_id: TP40009984
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-08-10'
source_url: https://developer.apple.com/library/archive/documentation/IDEs/Conceptual/Xcode4TransitionGuide/Refactoring/Refactoring.html
archived_at: '2026-07-15T07:42:15.174758Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 4 Transition Guide](About%20the%20Transition%20to%20Xcode%204.md)


[Next](Repositories%2C%20Snapshots%2C%20and%20Archives.md)[Previous](Debugging%20and%20Analyzing%20Your%20Code.md)

# Replacing Text and Refactoring

Like Xcode 3, Xcode 4 enables you to replace text throughout your project and to make other global changes to your code, such as converting the code to Objective-C 2.0 or creating a superclass from a class. These facilities are referred to as _search and replace_ and _factoring_.

To replace text in your source files, choose Replace from the pop-up menu in the search navigator (Figure 6-1). Type the text you want to find in the top text field and press Return, then type the replacement text in the lower text field (Figure 6-2). Note that Xcode does not search for the text if you don’t press Return while the cursor is in the upper text field, so if you get no results after typing your replacement text, put your cursor in the upper text field and press Return. The activity viewer in the workspace toolbar indicates the find operation is in progress (Figure 6-3).

__Figure 6-1__  Find/Replace pop-up menu

!

__Figure 6-2__  Find/Replace results

!

__Figure 6-3__  Activity viewer during a Find operation

!

Click Replace All to replace every occurrence of the searched-for text with the replacement text. To replace a single result, click that result to select it and press Replace. To replace a subset of the occurrences found, use Shift-click or Command-click to make your selection and press Replace.

By default, Xcode creates a snapshot of your project before making the changes; see [Take a Snapshot of Your Workspace](Repositories%2C%20Snapshots%2C%20and%20Archives.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsobufvbuqnznknlts)). To change this preference, select the Snapshots pane in the File > Project Settings dialog. You can also make a manual snapshot before clicking the Replace button (choose File > Manual Snapshot).

To see what your changes will look like in your source code before deciding which occurrences to replace, click the Preview button below the Replace text box ([Figure 6-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsobufvbuqobnknlte)). The preview dialog is shown in Figure 6-4.

__Figure 6-4__  Replacement preview

!

To select an individual occurrence of the Find text for replacement, click the checkbox for that occurrence in the left pane of the dialog, or click the sliding switch in the center of the right pane. Alternatively, you can select as many occurrences as you wish in the left pane using Shift-click or Command-click, and then press the Space bar to select them. If you decide to replace all the occurrences, click Cancel and then click the Replace All button.

A refactoring operation is one that improves the structure of source code without changing its behavior. You might do this to make it easier to maintain, or as a first step in making further changes to the code. Refactoring in Xcode 4 works much as it does in Xcode 3. Before you can choose a refactoring operation (also called a _transformation_) from Edit > Refactor or from the shortcut menu in the source editor, you have to select the source code that you want to refactor. Only the refactoring operations appropriate for the selected text are available in the menu.

Once you’ve selected the text and the refactoring operation, Xcode presents a dialog to let you select options and specify symbol names where necessary.

You also have the opportunity to preview the changes and decide which files to include before applying the changes (Figure 6-5). Uncheck a file in the navigator pane to leave it out of the refactoring operation. You can edit your source code directly in the Preview dialog. Any such edits are shown in the preview and included in the refactoring operation.

__Figure 6-5__  Refactor preview dialog

!

Possible refactoring operations include:

- __Rename__ changes the name of the selected item throughout your project files; select any symbol except except the declaration of a method inside a protocol interface. If you’re renaming a class and you have files that use that class in the file name, check the Rename related files checkbox to rename the files as part of the refactoring operation.
- __Extract__ creates a function or method from the selected code; select code or code and comments within a function or method implementation.
- __Encapsulate__ creates accessors (Get and Set methods) for the selected item and changes code that directly accesses the item to use the accessor methods instead; select a symbol that is an instance variable (“ivar”) or a member of a struct or union.
- __Create Superclass__ creates a superclass from the selected class; select a symbol that is a class defined in your project.
- __Move Up__ Moves the declaration and definition of the selected item into the superclass of the class where they currently reside, removing them from their former location; select a symbol that is a method or instance variable in a class, not a category, where the class and superclass are defined in your project.
- __Move Down__ moves the declaration and definition of the refactoring item to one or more of the subclasses of the class that declares and defines the item; select a symbol that is an instance variable in a class, not a category, where the class is defined in your project and one or more subclasses already exist.

Refactoring works only with C and Objective-C files.

Before you’ve saved your updated files, you can use the Edit > Undo operation on a per-file basis to back out changes, or you can close the project without saving changes to revert to your original files.

[Next](Repositories%2C%20Snapshots%2C%20and%20Archives.md)[Previous](Debugging%20and%20Analyzing%20Your%20Code.md)

