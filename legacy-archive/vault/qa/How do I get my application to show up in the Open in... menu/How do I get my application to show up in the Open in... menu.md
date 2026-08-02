---
title: How do I get my application to show up in the Open in... menu.
apple_id: DTS40012659
resource_type: QA
platform: iOS
topic: Data Management
technology: UIKit
published: '2016-11-16'
source_url: https://developer.apple.com/library/archive/qa/qa1587/_index.html
archived_at: '2026-07-18T02:32:20.091437Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1587

# How do I get my application to show up in the Open in... menu.

## Q:  How do I get my application to show up in the “Open in...” menu on iOS for a specific document type?

A: You need to register the document types that your application can open with iOS. To do this you need to add a document type to your app’s Info.plist for each document type that your app can open. Additionally if any of the document types are not known by iOS, you will need to provide an Uniform Type Identifier (UTI) for that document type.

To add the document type do the following:

1. In your Xcode project, select the target you want to add the document type to.
2. Select the Info tab.
3. Click on the disclosure button for Document Types to open the document types.
4. Click the “+” button.
5. In the newly created document type :
6. - Type the name of the document type.
   - In the “Types” section fill in the UTI for the new type.
   - Provide an icon for the document.
7. Click the disclosure triangle to open Additional document type properties.
8. Click in the table to add a new key and value.
9. - For the key value type: CFBundleTypeRole.
   - For the value type: Editor.
10. Click the + button to add another key/value pair.
11. - For the key value type: LSHandlerRank.
    - For the value type: Owner.

If the document type you are adding is a custom document type, or a document type that iOS does not already know about, you will need to define the UTI for the document type. To add a new UTI do the following:

1. In your Xcode project select the target you want to add the new UTI to.
2. Select the Info tab.
3. Click on the disclosure button for Exported UTIs.
4. Click the “+” button.
5. Select “Add Exported UTI”.
6. - In the Description field, fill in a description of the UTI.
   - In the Identifier field, fill in the identifier for the UTI.
   - In the Conforms To field fill in the list of UTIs that this new UTI conforms to.
7. Toggle the “Additional exported UTI properties” disclosure triangle to open up a table where you can add some additional information.
8. Click in the empty table and a list of items that can be added to the table will be displayed.
9. Type in “UTTypeTagSpecification”.
10. Set the type to Dictionary.
11. Click the disclosure triangle to open it, and click the + button in the table row to add an entry.
12. For the “New item” change the name to “public.filename-extension”.
13. For the type of the item change it to “Array”.
14. Toggle open the item you just added and click the + button in the table row.
15. For item 0 change the “value” to the file extension of your document. For example, txt, pdf, docx, etc.

Here is a concrete example of a custom document type and exported UTI. Let’s say you were adding a new document type of cat information. If the document had the file extension 'catinfo' then when you were finished with the steps shown above, your information would look like this:

__Figure 1__  Example settings for a cat info document type.

!!

The easiest way to test your custom document type is to email your custom file to your iOS device. Navigate to the email and ensure that the attachment is there. Tap and hold the document attachment icon. This should open a popover on the iPad, or an action sheet on the iPhone, that shows all of the apps that open your document type. Your app should show up in the list. Tap your app icon and your app should launch and receive the document from the email.

If your property list is not set up correctly then attempting to open your custom document from mail may not work. Symptoms are that your custom app shows up in the list of apps for your custom document type but the attachment is never handed off to your app. Compare your custom document type to the one shown in Figure 1 of this Q&A. Carefully comparing your document type field by field to the example frequently reveals errors.

Here are a few things you should check when things are not working as expected:

- The public.filename-extension key is spelled correctly.
- The public.filename-extension key/value is defined as an array not a string.
- Each item in the public.filename-extension array is a string that does not start with a dot. For example, txt not .txt.
- The type in the document type and the identifier in the exported (or imported) UTI are exactly the same. Copying and pasting this value is the easiest way to ensure that the values are identical.

[Uniform Type Identifiers Overview](https://developer.apple.com/library/ios/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_intro/understand_utis_intro.html#//apple_ref/doc/uid/TP40001319)

[Uniform Type Identifiers Reference](https://developer.apple.com/library/ios/documentation/Miscellaneous/Reference/UTIRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009257)

[Information Property List Key Reference: Core Foundation Keys](https://developer.apple.com/library/ios/#documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/TP40009249-SW1)

[System-Declared Uniform Type Identifiers](https://developer.apple.com/library/ios/documentation/Miscellaneous/Reference/UTIRef/Articles/System-DeclaredUniformTypeIdentifiers.html#//apple_ref/doc/uid/TP40009259-SW1)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-11-16 | Fixed a typographic error. |
| 2014-04-14 | Updated screen shot. |
| 2013-08-26 | Editorial update. |
| 2013-07-18 | Added sections on how to test your custom document type and troubleshooting tips. |
| 2012-08-14 | New document that describes how to add document types to iOS applications so they can be opened from the Open in... menu. |

