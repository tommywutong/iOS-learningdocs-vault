---
title: Configure document types for your iCloud container
apple_id: DTS40017664
resource_type: QA
platform: iOS
topic: Data Management
technology: UIKit
published: '2017-07-27'
source_url: https://developer.apple.com/library/archive/qa/qa1959/_index.html
archived_at: '2026-07-18T02:38:00.741731Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1959

# Configure document types for your iCloud container

## Q:  How to make my iCloud container ready to accept documents from `UIActivityViewController`?

A: On iOS, [UIActivityViewController](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller) allows an app to add a document to other apps' iCloud container by user interactions. When an app is ready to share a document, it wraps that document as a [UIActivityItemProvider](https://developer.apple.com/documentation/uikit/uiactivityitemprovider) object, then creates a `UIActivityViewController` object and presents it; users can then tap the `Add To iCloud Drive` button, and pick an iCloud container to add the document.

To accept a document from `UIActivityViewController`, your app needs to expose its iCloud container to iCloud Drive and declare that it can handle the document type. The detailed steps to expose an iCloud container is described in [QA1893](https://developer.apple.com/library/content/qa/qa1893/_index.html), and the document type declaration will be done by setting up a [CFBundleDocumentTypes](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-101685) entry in your app’s info.plist.

Listing 1 is a sample `CFBundleDocumentTypes` entry declaring that the app can handle the PDF file type and a document type created by its own. (The strings with the “Your_” prefix are placeholders that should be replaced with values appropriate for your app.)

__Listing 1__  A sample `CFBundleDocumentTypes` entry

```
 <key>CFBundleDocumentTypes</key>
    <array>
        <dict>
            <key>CFBundleTypeIconFiles</key>
            <array/>
            <key>CFBundleTypeName</key>
            <string>Adobe PDF</string>
            <key>CFBundleTypeRole</key>
            <string>Viewer</string>
            <key>LSHandlerRank</key>
            <string>Alternative</string>
            <key>LSItemContentTypes</key>
            <array>
                <string>com.adobe.pdf</string>
            </array>
        </dict>
        <dict>
            <key>CFBundleTypeIconFiles</key>
            <array/>
            <key>CFBundleTypeName</key>
            <string>Your_Type_Name</string>
            <key>CFBundleTypeRole</key>
            <string>Editor</string>
            <key>LSHandlerRank</key>
            <string>Owner</string>
            <key>LSItemContentTypes</key>
            <array>
                <string>com.Your_Company.Your_Type</string>
            </array>
        </dict>
    </array>
```

A new document type normally needs to be exported so as to be used by the other parties of the system. This can be done by adding a `UTExportedTypeDeclarations` entry in the info.plist. You can see Listing 2 for an example. The detailed discussion on this topic is covered in [Declaring New Uniform Type Identifiers](https://developer.apple.com/library/content/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_declare/understand_utis_declare.html) section.

__Listing 2__  A sample `UTExportedTypeDeclarations` entry

```
 <key>UTExportedTypeDeclarations</key>
    <array>
        <dict>
            <key>UTTypeConformsTo</key>
            <array>
                <string>public.content</string>
                <string>public.data</string>
            </array>
            <key>UTTypeDescription</key>
            <string>Your_Type_Description</string>
            <key>UTTypeIdentifier</key>
            <string>com.Your_Company.Your_Type</string>
            <key>UTTypeTagSpecification</key>
            <dict>
                <key>public.filename-extension</key>
                <array>
                    <string>Your_Extension_Name</string>
                </array>
                <key>public.mime-type</key>
                <string>Your_Mime-type</string>
            </dict>
        </dict>
    </array>
```

When exporting types, be sure to add a `UTTypeConformsTo` entry to declare the conformance to at least `public.content` and `public.data`. Having a container that can only contain types that don’t conform to `public.item` (which `public.data` does) will cause it to be disabled in `UIActivityViewController`.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-07-27 | New document that describes how to make your iCloud container ready to accept documents from UIActivityViewController. |

