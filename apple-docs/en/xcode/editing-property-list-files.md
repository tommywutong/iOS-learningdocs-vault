---
title: Editing property list files
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/editing-property-list-files
source_url: 'https://developer.apple.com/documentation/xcode/editing-property-list-files'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/editing-property-list-files.json'
content_hash: 'sha256:17f8ed8270c3dbff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Bundles and frameworks](bundles-and-frameworks.md)

# Editing property list files

<sub>Article</sub>

Add, remove, and change keys and values in a structured file.

## Overview

You use property list files to provide the system with structured data about your apps and other code bundles. For example, every bundle contains an Xcode-managed [Information Property List](../bundleresources/information-property-list.md) that describes the bundle to the system. Additionally, many apps contain property lists that describe their [Entitlements](../bundleresources/entitlements.md), and [Privacy manifest files](../bundleresources/privacy-manifest-files.md) that describe the data they collect and how they use certain APIs.

By default, Xcode generates your bundle’s information property list file from values in your project’s build settings, which you manage using the Info pane in the project editor, and you don’t need to edit the file directly. If you need to, you can supply a file that you edit manually. For more information, see [Managing your app’s information property list values](../bundleresources/managing-your-app-s-information-property-list.md).

Similarly, Xcode manages your app or extension’s [Entitlements](../bundleresources/entitlements.md) file, based on [Capabilities](capabilities.md) you add to your target using the Signing & Capabilities pane in the target editor, and you typically don’t need to edit the entitlements property list file directly. For more information, see [Adding capabilities to your app](adding-capabilities-to-your-app.md).

When you manually create a property list file, use the Xcode property list editor to update the file’s content while ensuring that the structure is valid.

### Create a property list file

To create a property list file in Xcode, follow these steps:

1. Choose File \> New \> File from Template.
2. Select the Property List template from the Resource group.
3. Click Next.
4. Enter a name for the file, and click Create.

To create a privacy manifest file, select the App Privacy template from the Resource group instead. For more information, see [Privacy manifest files](../bundleresources/privacy-manifest-files.md#Create-a-privacy-manifest).

### Add a property to the file

To add a property to a property list file, open the file in the Xcode editor, hover over the title of the file, and click the Add button (+) that appears next to the title. Type the name of the key and press Enter, or click outside of the text field.

You can also add an entry at any level of the property list file by hovering over an existing entry and clicking on the Add button that appears.

![A screenshot of Xcode adding a key to a dictionary in a property list file.](../../../attachments/115cda3e3af9d20ac184d8316cbb5031/editing-property-list-files-1@2x.png)

If the existing entry’s value has a primitive type — for example, a string, number, or Boolean — then Xcode creates the new entry as a key at the same level in the file’s structure as the existing entry, or as a new element in the same array if the existing entry is an element in an array.

If the existing entry’s value has a collection type — a dictionary or an array — then the behavior depends on whether the value is disclosed or hidden. If the value is disclosed, Xcode creates the new entry as a key-value pair inside the value if it’s a dictionary, or a new element in the array if it’s an array. Otherwise, Xcode creates the new entry as a key-value pair at the same level in the file’s structure as the existing entry.

### Set the type and value for a property

Xcode tracks the schema for common property list files, including information property lists and privacy manifest files, and sets the correct type for a key when you add the key to the file. To change the type for a custom key, use the pop-up menu in the Type column of the property list editor to choose the new type.

Use the pop-up menu in the Value column of the editor to set the value for a Boolean key to `YES` or `NO`. Enter the value for another primitive type, such as a string or number, into the Value column of the editor. To add elements to dictionaries or arrays, see [Add a property to the file](editing-property-list-files.md#Add-a-property-to-the-file), above.

### Remove a property from the file

To remove a key from a property list file, or an element from an array, hover over the element and click the Remove button (-) that appears.

### View raw keys and values

By default, Xcode shows readable representations of keys and values in common property list files. To see the raw keys and values, Control-click in the property list editor and check Raw Keys and Values. To return to the readable representations, uncheck Raw Keys and Values.

## See Also

### Bundles

- [Placing content in a bundle](../bundleresources/placing-content-in-a-bundle.md) — Place bundle content in the correct location based on its type.
- [Managing your app’s information property list values](../bundleresources/managing-your-app-s-information-property-list.md) — Customize the information property list values for your app using Xcode.
- [Embedding nonstandard code structures in a bundle](embedding-nonstandard-code-structures-in-a-bundle.md) — Use code that’s structured in a nonstandard way while avoiding code signing and distribution problems.
