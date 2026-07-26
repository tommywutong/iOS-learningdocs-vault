---
title: Adding resources to localizations
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/adding-resources-to-localizations
source_url: 'https://developer.apple.com/documentation/xcode/adding-resources-to-localizations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/adding-resources-to-localizations.json'
content_hash: 'sha256:5f013726a53adf89'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Localization](localization.md)

# Adding resources to localizations

<sub>Article</sub>

Include more resources in the localizations you add to your project.

## Overview

As you add more resources to your project, you can also add them to your localizations. Perform this step before you export localizations so that placeholder resources appear in the localization export folders.

### Make resources localizable

In the Project navigator, select the resource. Then in the inspector, under Localization, click Localize. In the dialog that appears, choose the localizations to add to the resource from the pop-up menu, and click Localize.

![](../../../attachments/6fba471644f2c90709cd93c29bf907b3/adding-resources-to-localizations-1@2x.png)

<sub>Screenshot of the project editor with an image file resource selected and the Localize button visible in the lower right-hand corner.</sub>

In the inspector, under Localization, you can also select or deselect localizations for the resource. If you select multiple localizations, the resource becomes a group in the Project navigator localization-specific versions of the file.

> [!note] Note
> If you add a Settings Bundle or WatchKit Settings Bundle file to your project, it’s automatically localizable.

## See Also

### Resources and assets

- [Localizing assets in a catalog](localizing-assets-in-a-catalog.md) — Use asset catalogs to localize colors, images, symbols, watch complications, and more.
