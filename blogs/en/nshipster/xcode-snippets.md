---
title: Xcode Snippets
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/xcode-snippets/'
original_language: en
published: 2013-09-02
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:22f88389a334d311'
translated: false
---

> 原文：[Xcode Snippets](https://nshipster.com/xcode-snippets/)　·　NSHipster (Mattt)

# [Xcode Snippets](https://nshipster.com/xcode-snippets/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  September 2^nd, 2013

iOS development all but requires the use of Xcode. To its credit, Xcode has improved pretty consistently over the last couple of years. Sure, [it still has its… quirks](http://www.textfromxcode.com), but hey—things could be [much, much worse](http://www.eclipse.org).

Working in an IDE may not be as cool as working in your favorite [decades-old editor](https://en.wikipedia.org/wiki/Vim_(text_editor)) (or [that other one](https://en.wikipedia.org/wiki/Emacs)), but you know what is cool? [Autocompletion](http://www.textfromxcode.com/post/24542673087). Not to mention [Build & Analyze](http://clang-analyzer.llvm.org/xcode.html), [Breakpoints](https://developer.apple.com/library/ios/recipes/xcode_help-source_editor/Creating,Disabling,andDeletingBreakpoints/Creating,Disabling,andDeletingBreakpoints.html), and [Instruments](https://developer.apple.com/library/ios/DOCUMENTATION/DeveloperTools/Conceptual/InstrumentsUserGuide/InstrumentsQuickStart/InstrumentsQuickStart.html).

This is all to say: if we’re resigned to use an IDE in our development workflow, we might as well make the most of it, right? So this week on NSHipster, we’re going to talk about one of the more powerful yet underused features of Xcode: **Code Snippets**.

---

From `@interface` declarations to `if (!self) return nil;` incantations, there is a lot of avoidable typing in Objective-C. Xcode snippets allow these common patterns and boilerplate code to be extracted for quick reuse.

## Using Xcode Snippets

To see the available code snippets, show the Utilities panel, to the right of your editor. On the bottom half the Utilities panel, there will be a horizontal divider with 4 icons.

![Utilities Divider](https://nshipster.com/assets/xcode-snippet-utilities-divider-57f2b5a1248fcc20d0e522879d7047cb7df70a021e363066c73e9c1f79f94ad3d2397d6d8d42a31594da898c1bcb2095744ab4a36a16bec2670948cdbf16dbf9.png)

Click the `{ }` icon to show the Code Snippets Library.

![Utilities Panel](https://nshipster.com/assets/xcode-snippet-utilties-panel-f63234371118ad036faf36978515bf074776a29ce1d3c55afad487a51de5f708a023f93edd89a623a34568724314fe5f1f79d2315c48012c0fc09bffc51b7b64.png)

There are two ways to insert a snippet into your code:

You can drag and drop from the code snippets library into your editor:

![Drag-and-Drop](https://nshipster.com/assets/xcode-snippet-drag-and-drop-93e45e9b973d52fb2b39688d7a6d6ecc469697380a7d2d74328257b7a86ac35959b7bfbc7469e404c9e4eeddc182e6fc26a00e52e9fac3e83e1c85bebf0e38a9.gif)

…or for snippets that include a text completion shortcut, you can start typing that:

![Text Completion Shortcut](https://nshipster.com/assets/xcode-snippet-text-completion-shortcut-01511df9c37bc2af414049007a2c90a706438127d39cdb9a434fecc3ce30d6d92e7ddc22632ab96a3d32c659e5556f3f5b97d72a22900d6d59954718d7bf67e8.gif)

To get a sense of what you can do with snippets, here’s an overview of the ones built-in to Xcode:

- C `typedef` declarations for `enum`, `struct``union`, and blocks
- C control flow statements like `if`, `if`…`else`, and `switch`
- C loops, such as `for`, `while`, and `do`…`while`
- C inline block variable declaration
- Objective-C declarations for `@interface` (including for class extensions and categories), `@implementation`, `@protocol`
- Objective-C boilerplate for KVO, including the relatively obscure `keyPathsForValuesAffecting<Key>`, used for [registering dependent keys](https://developer.apple.com/library/ios/DOCUMENTATION/Cocoa/Conceptual/KeyValueObserving/Articles/KVODependentKeys.html)
- Objective-C boilerplate for Core Data fetches, property accessors, and property validation
- Objective-C idioms for enumerating [`NSIndexSet`](https://nshipster.com/nsindexset/)
- Objective-C incantation for `init`, `initWithCoder:` and `initWithFrame:` method implementations
- Objective-C `@try` / `@catch` / `@finally` and `@autorelease` blocks
- GCD idioms for `dispatch_once` and `dispatch_after`

## Creating Xcode Snippets

Of course, what really makes snippets such a powerful feature is the ability to create your own.

The process of creating a snippet is actually pretty unintuitive and difficult to explain. It uses an obscure OS X system feature that allows users to create a “Text Clipping” by dragging and dropping selected text. Much easier to just show it in action:

![Text Completion Shortcut](https://nshipster.com/assets/xcode-snippet-create-53c59b570772f0a247a85b234a0822c73b87e61c3e4fb244bb3bdb2ade1604d5e21af0dae5e7cdeec3bb07c9a63859a2d4113e8494826a938b6d88e5d9b2ca47.gif)

After being added to the code snippet library, a user-defined snippet can be edited by double-clicking its listing:

![Text Completion Shortcut](https://nshipster.com/assets/xcode-snippet-editor-2a16b4074860349489d7acd4770785007266e17e6d83bf7333c6d2500962f47a2ab793e7239b21bd02daeae92f464bea49c92c4eae1a6130be9935c33de386cf.png)

Each snippet has the following fields:

- **Title** - The name of the snippet (appears in text completion and in snippet library listing)
- **Summary** - A brief description of what it does (appears only in snippet library listing)
- **Platform** - Limits the snippet visibility for text completion to the specified platform. OS X, iOS, or both (“All”)
- **Language** - Limits the snippet visibility for text completion to the specified language. Most commonly C, Objective-C, C++, or Objective-C++.
- **Completion Shortcut** - The text completion shortcut. For commonly-used snippets, this should be relatively short. Xcode does not warn about conflicting / overlapping shortcuts, so make sure yours doesn’t overlap with an existing one.
- **Completion Scopes** - Limits the snippet visibility for text completion to the specified scopes. For example, an `if` / `else` statement should only be auto-completed from within a method or function implementation. Any combination of the following:

    - All
    - Class Implementation
    - Class Interface Methods
    - Class Interface Variables
    - Code Expression
    - Function or Method
    - Preprocessor Directive
    - String or Comment
    - Top Level

> Each Xcode snippet has a file representation in `~/Library/Developer/Xcode/UserData/CodeSnippets/`

### Placeholder Tokens

Something you may have noticed in using other Xcode snippets are placeholder tokens:

![Placeholder Token](https://nshipster.com/assets/xcode-snippet-token-c8bfc19597e11f3112fb20fe017cbefde56063860cba42d70455092ee8591c0b3b4c4e3e2b8744e26c82accb761eba744009c2b4a7c462bf43046b48f568241d.png)

In Xcode, placeholder tokens are delimited by `<#` and `#>`, with the placeholder text in the middle. Go ahead—try typing that into Xcode, and watch as the text between the octothorp tags magically transforms right in front of your eyes.

Include placeholder tags to add a dash of dynamism in your own snippets!

### Third-Party Xcode Snippets

A list of generally useful code snippets can be found [in this GitHub project](https://github.com/mattt/Xcode-Snippets) (pull requests welcome!). If nothing else, this also serves as an example of what’s possible.

---

Programming isn’t about being an expert typist, so don’t make it any more difficult for yourself than it needs to be. If you find yourself groaning while typing some inane, rote-memorized code idiom, take a minute to create a snippet for it instead!
