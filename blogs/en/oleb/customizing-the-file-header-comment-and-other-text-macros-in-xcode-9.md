---
title: Customizing the file header comment and other text macros in Xcode 9
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/07/xcode-9-text-macros/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:812fb0a6eb5aefee'
translated: false
---

> 原文：[Customizing the file header comment and other text macros in Xcode 9](https://oleb.net/blog/2017/07/xcode-9-text-macros/)　·　Ole Begemann

# Customizing the file header comment and other text macros in Xcode 9

[I’m not a fan of the default file header comment](https://twitter.com/olebegemann/status/845263246949011457) Xcode adds to new source files. I’d argue that most of the information in the file header is either irrelevant or better tracked through source control. Moreover, these comments can quickly become outdated as files and projects get renamed.

[![Commentary on Xcode’s default file header comment](https://oleb.net/media/xcode-file-header-comment.png)](https://oleb.net/media/xcode-file-header-comment.png)

In my personal projects, my first step after creating a new file is always to delete this header comment.

Until now, that is, because Xcode 9 allows you to customize the file header and other so-called text macros using a plist file. The process is described in [Xcode Help](https://help.apple.com/xcode/mac/9.0/index.html) on a page titled [_Customize text macros_](https://help.apple.com/xcode/mac/9.0/index.html?localePath=en.lproj#/dev91a7a31fc):

[![The Customize Text Macros page in Xcode Help](https://oleb.net/media/xcode-help-customize-text-macros.png)](https://oleb.net/media/xcode-help-customize-text-macros.png)

1. **Create a property list file named `IDETemplateMacros.plist`.**
2. **For every text macro you want to customize, add a new key to the plist’s dictionary.** For example, to change the default file header, add an entry with the key `FILEHEADER`.

  [![Editing the IDETemplateMacros.plist file in Xcode’s property list editor](https://oleb.net/media/xcode-plist-editor-IDETemplateMacros-plist.png)](https://oleb.net/media/xcode-plist-editor-IDETemplateMacros-plist.png)

  <sub>Editing the `IDETemplateMacros.plist` file in Xcode’s plist editor.</sub>

  Xcode’s plist editor only displays a single line for the value, but you can insert newlines with Option + Return.

  See [_Text macros reference_ below](#text-macros-reference) for a full list of available macros. You can use other text macros in a macro’s value by wrapping them with three underscores, such as `___DATE___`. Some macros can also be customized with a `:modifier` syntax. See [_Text macro format reference_ below](#text-macro-format-reference) for more on this.
3. **Copy the file to one of the following locations. The directory specifies in which context the customized text macros should be applied:**

    - For a single project and user:  
       `<ProjectName>.xcodeproj/xcuserdata/[username].xcuserdatad/IDETemplateMacros.plist`
    - For all team members in a single project:  
       `<ProjectName>.xcodeproj/xcshareddata/IDETemplateMacros.plist`
    - For all projects in a workspace for a single user:  
       `<WorkspaceName>.xcworkspace/xcuserdata/[username].xcuserdatad/IDETemplateMacros.plist`
    - For all projects in a workspace for all team members:  
       `<WorkspaceName>.xcworkspace/xcshareddata/IDETemplateMacros.plist`
    - For everything you work on, regardless of project:  
       `~/Library/Developer/Xcode/UserData/IDETemplateMacros.plist`

When you now create a new file, it looks like this:

[![A new file in Xcode with a custom file header comment](https://oleb.net/media/xcode-new-file-after-customizing-text-macros.png)](https://oleb.net/media/xcode-new-file-after-customizing-text-macros.png)

<sub>The newly created file after customizing the `FILEHEADER` text macro.</sub>

Note that for the `FILEHEADER` macro, Xcode currently (Xcode 9 beta 3) adds comment markers (`//`, with no space) to the first line but not to subsequent lines. You’ll need to include those manually in the macro text. I’m not sure if this is the intended behavior or a bug (it looks like a bug to me).

Unfortunately, this also means that you can’t make the file header comment go away completely — even if you set it to an empty string in the plist, new files will begin with an empty comment line. I hope this gets fixed in a future version. I filed a bug at rdar://33451838.

---

# Text macros reference

_Here’s a list of all available text macros in Xcode 9. I copied this almost verbatim from the [_Text macros reference_](https://help.apple.com/xcode/mac/9.0/index.html?localePath=en.lproj#/dev7fe737ce0) page in Xcode Help._

[![The Text Macros Reference page in Xcode Help](https://oleb.net/media/xcode-help-text-macros-reference.png)](https://oleb.net/media/xcode-help-text-macros-reference.png)

> COPYRIGHT Xcode’s default copyright string that uses the organization name you’ve set in your project, e.g. "Copyright © 2017 MyCompany. All rights reserved." DATE The current date. DEFAULTTOOLCHAINSWIFTVERSION The version of Swift used for the default toolchain. FILEBASENAME The name of the current file without any extension. FILEBASENAMEASIDENTIFIER The name of the current file encoded as a C identifier. FILEHEADER The text placed at the top of every new text file. FILENAME The full name of the current file. FULLUSERNAME The full name of the current macOS user. NSHUMANREADABLECOPYRIGHTPLIST  The entry for the human readable copyright string in the Info.plist file of a macOS app target. For example, a valid value is: `<key>NSHumanReadableCopyright</key>
> <string>Copyright © 2017 Apple, Inc. All rights reserved.</string>
> ` Notice that the value includes a newline.  ORGANIZATIONNAME The company name for the team used for the provisioning profile. PACKAGENAME The name of the package built by the current scheme. PACKAGENAMEASIDENTIFIER A C-identifier encoded version of the package name built by the current scheme. PRODUCTNAME The app name of the product built by the current scheme. PROJECTNAME The name of the current project. RUNNINGMACOSVERSION The version of macOS that is running Xcode. TARGETNAME The name of the current target. TIME The current time. USERNAME The login name for the current macOS user. UUID  Return a unique ID. The first time the macro is used, it will generate the ID before returning it. You can use the macro to create multiple unique IDs by using a modifier. Each modifier returns the an ID that is unique for that modifier. For example, the first time `UUID:firstPurpose` it will generate and return a unique ID for that macro and modifier combination. Subsequent uses of `UUID:firstPurpose` return the same ID. Adding `UUID:secondPurpose` will generate and return a different ID that will be unique to `UUID:secondPurpose`, and different from the ID for `UUID:firstPurpose`.  WORKSPACENAME The name of the current workspace. If there is only one project open, then the name of the current project. YEAR The current year as a four-digit number.

---

# Text macro format reference

_Copied from the [_Text macro format reference_](https://help.apple.com/xcode/mac/9.0/index.html?localePath=en.lproj#/devc8a500cb9) page in Xcode Help._

[![The Text Macro Format Reference page in Xcode Help](https://oleb.net/media/xcode-help-text-macro-format-reference.png)](https://oleb.net/media/xcode-help-text-macro-format-reference.png)

> A text macro can contain any valid unicode text. It can also contain other text macros.
> 
> ## Including other text macros
> 
> To include another text macro, add three underscore (_) characters before and after the macro name:
> 
> ```
> ___<MacroName>___
> ```
> 
> ## Modifying text macro expansion
> 
> You can modify the final expansion of the text macro by adding one or more modifiers. Add a modifier to a text macro by placing a colon (:) at the end of the macro followed by the modifier. Add multiple modifiers by separating each one with a comma (,).
> 
> ```
> <MACRO>:<modifier>[,<modifier>]…
> ```
> 
> For example, the following macro will remove the path extension from the `FILENAME` macro:
> 
> ```
> FILENAME:deletingPathExtension
> ```
> 
> To turn the modified macro above into a valid C identifier, add the identifier macro:
> 
> ```
> FILENAME:deletingPathExtension,identifier
> ```
> 
> ## Modifiers
> 
> bundleIdentifier Replaces any non-bundle identifier characters with a hyphen (-). deletingLastPathComponent Removes the last path component from the expansion string. deletingPathExtension Removes any path extension from the expansion string. deletingTrailingDot Removes any trailing dots (.). identifier Replaces any non-C identifier characters with an underscore (_). lastPathComponent Returns just the last path component of the expansion string. pathExtension Returns the path extension of the expansion string. rfc1034Identifier Replaces any non-rfc1034 identifier characters with a hyphen (-). xml  Replaces special xml characters with the corresponding escape string. For example, less-than (`<`) is replaced with `&lt;`
