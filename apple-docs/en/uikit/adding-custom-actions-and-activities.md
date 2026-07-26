---
title: Adding custom actions and activities
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/adding-custom-actions-and-activities
source_url: 'https://developer.apple.com/documentation/uikit/adding-custom-actions-and-activities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/adding-custom-actions-and-activities.json'
content_hash: 'sha256:5125e344701ce3fd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [View controllers](view-controllers.md) · [Adding a document browser to your app](adding-a-document-browser-to-your-app.md)

# Adding custom actions and activities

<sub>Article</sub>

Add custom document browser actions, activities, and bar items.

## Overview

There are three different ways to add custom actions to the document browser:

- Add document browser actions to the navigation bar or Edit Menu.
- Add activities to the activity view.
- Add bar items to the navigation bar.

### Add document browser actions

By default, the system provides standard actions such as copy, move, rename, delete, and share. To add custom actions, assign an array of [UIDocumentBrowserAction](uidocumentbrowseraction.md) objects to the browser’s [customActions](uidocumentbrowserviewcontroller/customactions.md) property.

Document browser actions can be accessed in two ways:

- _Navigation bar_ actions appear in the navigation bar when someone places the browser in Select mode.
- _Edit Menu_ actions appear when someone long presses on a document or folder.

When someone initiates one of these actions, the actions receive the URLs of the currently selected items.

### Add activities

The browser displays an activity view when someone taps the Share button (for example, when someone long presses on a document or folder and selects Share from the Edit Menu).

To add custom activities to the activity view, implement your [UIDocumentBrowserViewControllerDelegate](uidocumentbrowserviewcontrollerdelegate.md) object’s [- documentBrowser:applicationActivitiesForDocumentURLs:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__applicationactivitiesfordocumenturls_).md>) method and return an array of custom [UIActivity](uiactivity.md) objects.

Your delegate object receives an array of URLs for the currently selected items. You can store and use these URLs in your [UIActivity](uiactivity.md) subclass.

For design guidance, see Human Interface Guidelines \>  [Collaboration and sharing](../design/human-interface-guidelines/collaboration-and-sharing.md).

### Add bar button items

Use the [additionalLeadingNavigationBarButtonItems](uidocumentbrowserviewcontroller/additionalleadingnavigationbarbuttonitems.md) and [additionalTrailingNavigationBarButtonItems](uidocumentbrowserviewcontroller/additionaltrailingnavigationbarbuttonitems.md) properties to add buttons to the navigation bar.

Actions that these buttons initiate don’t have access to the browser’s content or to the URLs of selected items. Use bar button items for actions that don’t affect a specific document or folder.

## See Also

### Customization

- [Customizing the document browser](customizing-the-browser.md) — Customize the document browser’s look and behavior.
