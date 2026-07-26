---
title: Finding and replacing content in a project
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/finding-and-replacing-content-in-a-project
source_url: 'https://developer.apple.com/documentation/xcode/finding-and-replacing-content-in-a-project'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/finding-and-replacing-content-in-a-project.json'
content_hash: 'sha256:5d96b8994492d18c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Projects and workspaces](projects-and-workspaces.md)

# Finding and replacing content in a project

<sub>Article</sub>

Search some or all of your project for text strings or symbol names, and perform advanced searches using regular expressions.

## Overview

Xcode offers sophisticated search and replace capabilities in the Find navigator, which you access from the navigator area of your project. Use the Find navigator to search for text and symbols across your entire project. To perform advanced searches, use regular expressions or use the navigator’s controls to narrow the scope of the search operations.

To display the Find navigator, click the magnifying glass icon in the navigator area of your project.

![Perform advanced searches using the Find navigator.](../../../attachments/6c5ce8aa8d50cf3d3c1a7f4f3d1ee027/find-navigator-overview@2x.png)

### Find text strings

To search for text in your project:

1. In the search criteria bar, select Find \> Text.
2. Select a search criteria: Containing, Matching, Starting with, or Ending with.
3. Enter text into the search field.
4. Select a case-sensitivity option from the pop-up menu.
5. Press Return.

Xcode displays the results of the search. When you select a result, Xcode displays the result in the editor area. To quickly navigate to the next or previous item, choose Find \> Find Next in Project or Find \> Find Previous in Project.

> [!tip] Tip
> To quickly populate the search field, select some text in the editor and choose Find \> Find in Project. Xcode copies the selected text to the search field.

### Find symbol references and definitions

Xcode offers two ways to search for symbols:

- Use Find \> References to search your code for the specified symbol name.
- Use Find \> Definitions to search for the source file that contains the definition of the specified symbol.

When you execute the search, the search results contain only places where your code refers to the symbol. The results don’t include references to the symbol in code comments or other project files. To refine your results, change the matching behavior and case sensitivity options of your search.

### Replace instances of found text

To search for text and replace it with another string:

1. In the search criteria bar, select Replace \> Text.
2. Select a search criteria: Containing, Matching, Starting with, or Ending with.
3. Enter text into the search field.
4. Select a case-sensitivity option from the pop-up menu.
5. Enter text in the replacement field.
6. Press Return.

Xcode displays the results of the search, but it doesn’t automatically replace the text. To replace the text for a single result, select it and click the Replace button. To replace the text for all results, click Replace All.

### Filter the list of search results

After any search, you can narrow the search results further by entering a secondary string into the filter bar. The Find navigator temporarily removes results that don’t also contain the string you type into the filter bar. To restore the original results, clear the text from the filter bar.

### Limit the scope of a find or replace operation

When you execute a search, Xcode searches all files in your project by default. To search only a subset of files, click Scope and choose from the options that appear.

- Click a project or group to restrict searches to the designated part of your Xcode project.
- Create a custom scope to restrict searches to files in specific locations or files with a specific name, path, extension, type, or source-control status.

![Create a custom scope in the Find navigator to limit where Xcode searches.](../../../attachments/214ec1c6561b93f6b768c9a98174ee4c/find-scope-search@2x.png)

### Refine searches to match predefined pattern strings

Pattern tokens help you match strings that contain variable content. For example, you might use a pattern token to represent an email address in a string.

To add a pattern to your search string, click the magnifying glass in the search field and choose Insert Pattern from the pop-up menu.

![Insert a pattern in the search field of the Find navigator.](../../../attachments/8fe20fb0a7b58fede042ce50ab83e7cc/find-insert-pattern@2x.png)

Select the pattern you want from the pop-up menu to add it to your search field. Xcode defines pattern tokens for white space, URLs, hexadecimal digits, and other specific character sets. Include one or more tokens plus literal text to perform complex pattern matching.

![Select search patterns from the pop-up menu to add them to the search field of the Find navigator.](../../../attachments/c89d561cfbf4e8657898de8c495ca41f/find-pattern-menu@2x.png)

### Find or replace using a regular expression

Regular expressions let you define your own custom pattern strings to use during matches. The [NSRegularExpression](../foundation/nsregularexpression.md) class in the Foundation framework defines the syntax that you use for Xcode regular expressions.

To find or replace text using a regular expression:

1. In the search criteria bar, select Find \> Regular Expression or Replace \> Regular Expression.
2. Select a search criteria: Containing, Matching, Starting with, or Ending with.
3. Enter the regular expression into the Find or Replace search field.
4. Select a case-sensitivity option from the pop-up menu.
5. Press Return.

![Search using a regular expression to more precisely match specific patterns.](../../../attachments/f0837dede7b64a2c6c8bbf2c8e1e6550/find-regular-expression@2x.png)

## See Also

### Navigation

- [Configuring the Xcode project window](configuring-the-xcode-project-window.md) — Customize the Xcode project window and editor area to view and edit project files in a configuration you prefer.
