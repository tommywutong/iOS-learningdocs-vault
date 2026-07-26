---
title: Setting up a document browser app
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/setting-up-a-document-browser-app
source_url: 'https://developer.apple.com/documentation/uikit/setting-up-a-document-browser-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/setting-up-a-document-browser-app.json'
content_hash: 'sha256:35e198f0273b7bf5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [View controllers](view-controllers.md) · [Adding a document browser to your app](adding-a-document-browser-to-your-app.md)

# Setting up a document browser app

<sub>Article</sub>

Add a document browser view controller to your app.

## Overview

Setting up the document browser is a three-step process:

1. Set the browser as your app’s root view controller.
2. Declare document browser support for your app.
3. Define the type of documents that the document browser can open.

The simplest way to do all three is to create a new project using the Document Based App template.

### Create a new document-based app

To create a new document-based app, open Xcode and choose File \> New \> Project. In the template chooser, under Application, choose the Document Based App template, and click Next.

![](../../../attachments/b91b785d9ee2e57577d2f373cd4a9ad8/setting-up-a-document-browser-app-1@2x.png)

<sub>A screenshot of Xcode's project template pane, that shows both the iOS tab and the Document App icon in a selected state.</sub>

Continue following the prompts to create a document-based project. The following items appear in your new project:

- `Main.storyboard` contains a document browser view controller as its initial view controller. This storyboard sets the document browser as your app’s root view controller, ensuring that the browser remains in memory throughout your app’s lifetime.
- In your app’s `Info.plist` file, the [UISupportsDocumentBrowser](../bundleresources/information-property-list/uisupportsdocumentbrowser.md) key is set to `YES`, declaring document browser support for your app. Specifically, this key lets other apps open and edit the files stored in your app’s Documents directory. It also lets people set the app’s default save location in Settings.
- The app declares that it supports `public.image` document types. People can then select image files in the document browser and share image files from other apps.

Use most of these default values as-is; however, unless you’re making an image-based app, you probably need to update the supported document types.

### Set the supported document types

For each document type your app supports, follow these steps in the project editor’s Info pane:

1. Click the Document Types disclosure triangle, and click the Add button (+) to add a new document type or open an existing document type.
2. Set the document type’s name and its uniform type identifier (UTI).
3. Click the “Additional document type properties” disclosure triangle.
4. Add the [LSHandlerRank](../bundleresources/information-property-list/cfbundledocumenttypes/lshandlerrank.md) key, and set its value to `Owner` or `Alternate`.
5. Optionally, set the other document type properties.

For example, for an app that edits text files, use the settings shown in the following image:

![](../../../attachments/ea5401762124692ecd5dbc3c7620b258/setting-up-a-document-browser-app-2@2x.png)

<sub>A screenshot showing the document type settings for text files. The file type is set to public.plain-text, and the handler rank is set to Alternate.</sub>

These entries set the [CFBundleDocumentTypes](../bundleresources/information-property-list/cfbundledocumenttypes.md) key in your app’s `Info.plist` file as shown here:

```xml
<key>CFBundleDocumentTypes</key>
<array>
    <dict>
        <key>CFBundleTypeIconFiles</key>
        <array/>
        <key>CFBundleTypeName</key>
        <string>Text</string>
        <key>LSHandlerRank</key>
        <string>Alternate</string>
        <key>LSItemContentTypes</key>
        <array>
            <string>public.plain-text</string>
        </array>
    </dict>
</array>
```

For more information, see [Set supported document types](http://help.apple.com/xcode/mac/current/#/devddd273fdd).

## See Also

### Configuration

- [Presenting selected documents](presenting-selected-documents.md) — Display user-selected documents over your browser view controller.
- [Enabling document sharing](enabling-document-sharing.md) — Give users the ability to import and export documents from your app.
