---
title: Localizing your app using agents
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/localizing-your-app-using-agents
source_url: 'https://developer.apple.com/documentation/xcode/localizing-your-app-using-agents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/localizing-your-app-using-agents.json'
content_hash: 'sha256:0f0e1910c6808573'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Coding intelligence](coding-intelligence.md)

# Localizing your app using agents

<sub>Article</sub>

Use agentic coding tools to translate the strings in your app into multiple languages and regions.

## Overview

Agents simplify the localization of your app by performing tasks for you, such as adding languages, updating string catalogs, translating strings, and even adding language-specific plural variants when needed. Xcode gives the right context and language-specific style guidance to agents so they make the best translations for your app.

Before you begin, enable an agent in Intelligence settings and choose that agent in the coding assistant. For more information, see [Setting up coding intelligence](setting-up-coding-intelligence.md).

## Add languages and translations

In the coding assistant, enter a prompt in the message text field, such as:

- _Translate my app into Italian._

Xcode prepares your project for translation by adding the language. It then builds all the targets in your project to add all localizable strings to string catalogs. Xcode also localizes human-readable text in the information property list file.

If you have a large project, you can organize the strings into multiple string catalogs. If you pass string catalog names using the `tableName` or `table` parameter to localizable APIs, Xcode adds the strings to string catalogs with that name. Otherwise, it uses the default `Localizable.xcstrings` filename.

During the translation, Xcode:

- Provides context about where strings appear in your code
- Identifies plural and device variations for strings
- Identifies similar strings to stay consistent with your existing terminology
- Adheres to any requests for custom styles, such as language appropriate for children or formal business tone

You can watch the progress of translations in the transcript and see files that Xcode changes in the artifacts pane.

![](../../../attachments/f5b3c4f11810ad3ba6cfc0310719f7ba/localizing-using-agents-in-progress@2x.png)

<sub>A screenshot that shows the conversation sidebar, a localization transcript in the middle, and changes to a string catalog in the artifacts pane on the right. The transcript shows the “Translate my app into Italian” prompt in progress with one translation batch in progress and two translation batches complete. The artifacts pane shows the Localizable string catalog translated into Italian.</sub>

After the agent completes the translations, Xcode shows a summary of the changes in the transcript. The summary of changes includes the details of the added or changed files in the artifacts area. You can move the files that Xcode creates to other locations in your project.

To differentiate agentic translations from those that you provide, Xcode sets the state of translations to Machine Translated in the string catalog editor. If you export your localizations to XML Localization Interchange File Format (XLIFF), Xcode sets the `state-qualifier` property to `leveraged-mt` as well.

## Use localizable APIs

If Xcode omits some user-facing strings when updating string catalogs, make sure you’re using localizable APIs in your code.

If your app uses [SwiftUI](../swiftui.md), the views that the framework provides treat user-facing strings as localizable, so Xcode automatically finds them. However, other Swift code that creates human-readable strings, must explicitly use the [init(localized:)](<../swift/string/init(localized_).md>) initializer to be localizable.

```swift
String(localized: "Hello, world!")
```

Update your Swift code to use the initializer and build your app again to update the string catalogs.

For additional initializer options, see [Creating a Localized String](../swift/string.md#Creating-a-Localized-String). For UIKit and AppKit, make sure you use similar localizable APIs. For more information, see [Preparing your app’s text for translation](preparing-your-apps-text-for-translation.md).

## Generate translations in the string catalog editor

You can also generate specific translations in the string catalog editor. Use the Generate Translations button in the editor toolbar to add translations to languages and strings:

- To generate missing translations for all languages, select the source localization in the sidebar and click Generate Translations.
- To generate missing translations for a specific language, select the language in the sidebar and click Generate Translations.
- To generate translations for specific strings in a language, select the language, select the strings in the editor area, and click Generate Translations.

You can also Control-click a language in the sidebar or string in the editor and choose Generate Translations from the contextual menu.

![](../../../attachments/f0df909ff12580234dd7a2b081a92b1b/string-catalog-editor-generate-translations-button@2x.png)

<sub>A screenshot that shows the Project navigator on the left and the string catalog editor on the right. The string catalog editor shows German added with zero percent translation in the sidebar, a string selected in the detail area, and the Generate Translations button in the toolbar.</sub>

## Test machine translations

You can immediately test the translations in a preview or by running your app on a simulated or physical device.

Before you run your app in Device Hub, set a language and region in the Run scheme. Then make sure that all the text fits when you change the language. For example, use Dynamic Type so words and letters don’t clip in languages that require more height.

![](../../../attachments/24ce5ab541dca08062c640b716a01b70/previewing-localizations-in-the-canvas@2x.png)

<sub>A screenshot that shows the Project navigator on the left with a source file selected, the source editor in the middle showing code for a preview, and the canvas on the right showing the preview localized in Italian.</sub>

Also, verify that right-to-left languages have enough space. For more information, see [Previewing localizations](previewing-localizations.md) and [Testing localizations when running your app](testing-localizations-when-running-your-app.md).

Get feedback from people who speak the languages and live in the regions you support. For distribution options, including using TestFlight, see [Distributing your app to registered devices](distributing-your-app-to-registered-devices.md) and [Distributing your app for beta testing and releases](distributing-your-app-for-beta-testing-and-releases.md).

## Provide translation guidance

You can add translation guidance to configuration files, such as the `AGENTS.md` or `CLAUDE.md` files, that agents automatically read. For example, in your agent configuration file, refer to your translation guidance that you store in a separate `TRANSLATION.md` file in your project. You can include a glossary of terms your app uses or a list of strings that the agent shouldn’t translate.

To share configuration files between all your Xcode projects, see [Customize agent environments](extending-and-customizing-agents.md#Customize-agent-environments).

## See Also

### Related Documentation

- [Localizing and varying text with a string catalog](localizing-and-varying-text-with-a-string-catalog.md) — Use string catalogs to manage localizable strings, add languages, translate text, handle plurals, and vary text by device.
