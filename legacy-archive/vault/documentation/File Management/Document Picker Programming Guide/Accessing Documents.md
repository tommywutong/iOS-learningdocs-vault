---
title: Document Picker Programming Guide
apple_id: TP40014451
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: UIKit
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/DocumentPickerProgrammingGuide/AccessingDocuments/AccessingDocuments.html
archived_at: '2026-07-15T07:31:54.726386Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Document Picker Programming Guide](About%20the%20Document%20Picker.md)


[Next](Creating%20an%20Outstanding%20User%20Experience.md)[Previous](About%20the%20Document%20Picker.md)

# Accessing Documents

Use a document picker view controller to access files from a variety of external sources. iOS 8.0 provides a single, built-in source—iCloud Drive. This source grants access to documents inside either the public iCloud container or another app’s iCloud container.

Third-party developers can also create their own sources using the Document Provider extension. These extensions grant limited access to a group container shared by the extension and its containing app.

The document picker provides four basic operations: _import_, _export_, _open_, and _move_. Each operation has its own unique set of features, and it’s important to pick the correct operation for the task at hand. You can divide these operations based on the direction you are moving the documents. The import and open operations let the user select an external file and bring it into your app. The export and move operations take local files and send them to an external source.

Alternatively, you can divide these operations based on how the system handles the files. For import and export operations, the document picker copies the original file into its destination; the original file remains unchanged. For open and move operations, the file can be accessed directly from the source’s container, letting the user edit the file in place.

No matter which of the four operations you use, there are two ways to present the document picker.

The document menu provides a list of relevant Document Provider extensions enabled on the device. Users can control which Document Provider extensions are shown on this menu, turning them on or off as desired. When the user selects an extension, the system presents a document picker view controller containing the selected document provider.

You can also add optional items to either the top or bottom of this list by calling the [addOptionWithTitle:image:order:handler:](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/1614193-addoption) method. If the user selects one of these items, the system calls its handler.

To present the document menu, instantiate a copy of the [UIDocumentMenuViewController](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller) class, set its delegate, add any optional items you want, and present it to the user. For step-by-step instructions, see [Setting up an Import Operation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dinjrfvbuqmrnknlte).

![../Art/Document Menu_2x.png](../Art/Document Menu_2x.png)

Instead of presenting a document menu, you can present a document picker view controller directly. This direct approach opens a document picker view controller for the most recently used document provider. Users can then switch to a different document provider, if they want.

To present the document picker view controller, instantiate a copy of the [UIDocumentPickerViewController](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller) class, set its delegate, and present it to the user. For step-by-step instructions, see [Setting up an Import Operation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dinjrfvbuqmrnknlte).

![../Art/Document Picker_2x.png](../Art/Document Picker_2x.png)

Use the import and export operations to copy files into or out of your app’s sandbox. In many ways, this behavior is similar to the way the [UIDocumentInteractionController](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller) class’s “Open in” menu behaves. But whereas the document interaction controller forced users to leave your app, find a file, and then transfer it back to your app; the import operation lets users transfer files without ever leaving your app. This leads to a workflow that is both more convenient and easier to understand. The import and export operations also let users access files from any Document Provider extensions they have installed on their devices. In the case of iCloud Drive, this means that users can import and export from the iCloud container of any app that has enabled access to its iCloud document storage.

This sharing model is very simple and straightforward. In fact, its main advantage comes from its simplicity. You always work with a separate, local copy of the data; therefore, you don’t need to use file coordination or security-scoped URLs. However, because each app uses its own copy of the document, this approach consumes extra storage space and makes it difficult to process a single document with multiple apps. Copying may still be preferred when working with aggregate documents, for example a richly-formatted text document that can include images or videos. Often, you want to import these assets, giving your aggregate document its own, private copy of the resource files.

To set up an import operation, use one of the processes described next.

__To display the document menu__

1. Instantiate a [UIDocumentMenuViewController](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller) object by calling [initWithDocumentTypes:inMode:](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/1614187-init). Pass in an array of UTIs representing the types of documents you want to import and the [UIDocumentPickerModeImport](https://developer.apple.com/documentation/uikit/uidocumentpickermode/import) mode.
2. Add any options by calling [addOptionWithTitle:image:order:handler:](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/1614193-addoption).

   The option’s completion handler runs when the user selects the option. While you can use these handlers to execute arbitrary code, the option should make sense within the context of importing documents. For example, you might use an option to create new documents. Or you might use an option to access files that are not available through existing Document Provider extensions (for example, importing files from system services such as Photos or iTunes).
3. Set the menu controller’s delegate.

   The menu view controller calls the delegate’s [documentMenu:didPickDocumentPicker:](https://developer.apple.com/documentation/uikit/uidocumentmenudelegate/1614188-documentmenu) method when the user selects a specific document picker. This method must set the provided document picker view controller’s delegate and present it. For more information see [Present the Most Recently Used Document Picker](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dinjrfvbuqmrnknlto).

   The menu view controller also calls the delegate’s [documentMenuWasCancelled:](https://developer.apple.com/documentation/uikit/uidocumentmenudelegate/1614190-documentmenuwascancelled) method when the user dismisses the menu.
4. Present the menu controller.

```
UIDocumentMenuViewController *importMenu =
[[UIDocumentMenuViewController alloc] initWithDocumentTypes:[self UTIs]
                                                     inMode:UIDocumentPickerModeImport];

importMenu.delegate = self;
[self presentViewController:importMenu animated:YES completion:nil];
```

```
let importMenu = UIDocumentMenuViewController(documentTypes: self.UTIs, inMode: .Import)
importMenu.delegate = self
self.presentViewController(importMenu, animated: true, completion: nil)
```

__To display a document picker directly__

1. Instantiate a [UIDocumentPickerViewController](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller) object by calling [initWithDocumentTypes:inMode:](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/1618678-initwithdocumenttypes). Pass in an array of UTIs representing the types of documents you want to import and the [UIDocumentPickerModeImport](https://developer.apple.com/documentation/uikit/uidocumentpickermode/import) mode.
2. Set the document picker controller’s delegate.

   The document picker calls the delegate’s [documentPicker:didPickDocumentAtURL:](https://developer.apple.com/documentation/uikit/uidocumentpickerdelegate/1618680-documentpicker) method when the user selects a file. The URL points to a temporary file in the app’s sandbox. The file remains available until the app closes.

   The document picker also calls the delegate’s [documentPickerWasCancelled:](https://developer.apple.com/documentation/uikit/uidocumentpickerdelegate/1618679-documentpickerwascancelled) method when the user dismisses the document picker.
3. Present the picker view controller.

```objc
-(void)documentMenu:(UIDocumentMenuViewController *)documentMenu didPickDocumentPicker:(UIDocumentPickerViewController *)documentPicker

{
    documentPicker.delegate = self;
    [self presentViewController:documentPicker animated:YES completion:nil];
}
```

```swift
func documentMenu(documentMenu: UIDocumentMenuViewController!,
                  didPickDocumentPicker documentPicker: UIDocumentPickerViewController!) {

    documentPicker.delegate = self
    self.presentViewController(documentPicker, animated: true, completion: nil)
}
```


The export operation uses the same basic setup as the import operation, with the following differences:

- To display a document menu, instantiate a [UIDocumentMenuViewController](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller) object using [initWithURL:inMode:](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/1614191-init). Pass in the URL of the file you want to export and the `UIDocumentPickerModeExportToService` mode.
- To display a document picker directly, instantiate a [UIDocumentPickerViewController](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller) object by calling [initWithURL:inMode:](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/1618684-init). Pass in the URL of the file you want to export and the `UIDocumentPickerModeExportToService` mode.
- The document picker calls the delegate’s [documentPicker:didPickDocumentAtURL:](https://developer.apple.com/documentation/uikit/uidocumentpickerdelegate/1618680-documentpicker) method when the user selects a destination outside your app’s sandbox. The system saves a copy of your document to the specified destination. The document picker provides the copy’s URL to indicate success; however, your app does not have access to the file referred to by this URL.

The open and move operations provide access to files outside your app’s sandbox. These operations let users modify the documents in-place, enabling a much deeper level of sharing between apps. This approach gives users a great amount of flexibility when it comes to working with their documents. For example, it lets users create a complex workflow, where a single document is processed using multiple apps.

However, these operations also represent a significant departure from traditional iOS document handling. The additional flexibility adds a layer of additional complexity. It also imposes a number of additional requirements.

Any app that accesses documents outside its sandbox must meet the following requirements:

- Your app must perform all file read and write operations using file coordination.
- If you display the contents of the document to the user, you must track the document’s state using a file presenter. If you’re only showing a list of files, a file presenter is not necessary.
- Do not save any URLs accessed through open or move operations. Always open the document using a document picker, a metadata query, or a security-scoped bookmark to the URL.
- These operations return security-scoped URLs. You must call [startAccessingSecurityScopedResource](https://developer.apple.com/documentation/foundation/nsurl/1417051-startaccessingsecurityscopedreso) before accessing the URL.
- If [startAccessingSecurityScopedResource](https://developer.apple.com/documentation/foundation/nsurl/1417051-startaccessingsecurityscopedreso) returns `YES`, call [stopAccessingSecurityScopedResource](https://developer.apple.com/documentation/foundation/nsurl/1413736-stopaccessingsecurityscopedresou) when you are done using the file.
- If you are using a UIDocument subclass, it will automatically consume the security-scoped URLs for you. There’s no need to call [startAccessingSecurityScopedResource](https://developer.apple.com/documentation/foundation/nsurl/1417051-startaccessingsecurityscopedreso) or [stopAccessingSecurityScopedResource](https://developer.apple.com/documentation/foundation/nsurl/1413736-stopaccessingsecurityscopedresou). UIDocument also acts as a file presenter and automatically handles file coordination. For these reasons, using a UIDocument subclass is highly recommended for all files outside your app’s sandbox.

The open operation uses the same basic setup as the import operation, with the following differences:

- To display a document menu, , instantiate a [UIDocumentMenuViewController](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller) object using [initWithDocumentTypes:inMode:](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/1614187-init). Pass in an array of UTIs representing the types of documents you want to import and the `UIDocumentPickerModeOpen` mode.
- To display a document picker directly, instantiate a [UIDocumentPickerViewController](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller) object by calling [initWithDocumentTypes:inMode:](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/1618678-initwithdocumenttypes). Pass in an array of UTIs representing the types of documents you want to import and the `UIDocumentPickerModeOpen` mode.
- The document picker calls the delegate’s [documentPicker:didPickDocumentAtURL:](https://developer.apple.com/documentation/uikit/uidocumentpickerdelegate/1618680-documentpicker) method when the user selects a document. You are given a security-scoped URL for that document. For more information on using security-scoped URLs, see [Requirements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dinjrfvbuqmrnknltg).

The move operation uses the same basic setup as the import operation, with the following differences:

- Instantiate a [UIDocumentMenuViewController](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller) object using [initWithURL:inMode:](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/1614191-init). Pass in the URL of the file you wish to exploit and the `UIDocumentPickerModeMoveToService` mode.
- Instantiate a [UIDocumentPickerViewController](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller) object by calling [initWithURL:inMode:](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/1618684-init). Pass in the URL of the file you wish to move and the `UIDocumentPickerModeMoveToService` mode.
- The document picker calls the delegate’s [documentPicker:didPickDocumentAtURL:](https://developer.apple.com/documentation/uikit/uidocumentpickerdelegate/1618680-documentpicker) method when the user selects a destination. The file is saved to this destination. The original file is also deleted from your app’s sandbox. You are then given a new security-scoped URL to access the new file. For more information on using security-scoped URLs, see [Requirements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dinjrfvbuqmrnknltg).

  This operation largely combines the export and open operations; however, the original file is also deleted.

[Next](Creating%20an%20Outstanding%20User%20Experience.md)[Previous](About%20the%20Document%20Picker.md)

