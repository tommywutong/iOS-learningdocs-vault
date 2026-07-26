---
title: 'activityViewController(_:dataTypeIdentifierForActivityType:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiactivityitemsource/activityviewcontroller(_:datatypeidentifierforactivitytype:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemsource/activityviewcontroller(_:datatypeidentifierforactivitytype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemsource/activityviewcontroller%28_%3Adatatypeidentifierforactivitytype%3A%29.json'
content_hash: 'sha256:e6ab575b593ec7d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityItemSource](../uiactivityitemsource.md)

# activityViewController(_:dataTypeIdentifierForActivityType:)

<sub>Instance Method</sub>

For items that are provided as data, returns the UTI for the item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func activityViewController(_ activityViewController: UIActivityViewController, dataTypeIdentifierForActivityType activityType: UIActivity.ActivityType?) -> String
```

## Parameters

- `activityViewController` — The activity view controller object requesting information about the data item.

- `activityType` — The selected activity type; may be `nil`.

## Return Value

The UTI for the item.

## Discussion

Providing the UTI allows services to handle specific data types in appropriate ways, such as an email service formatting an image to display in-line. If you provide items as [NSData](../../foundation/nsdata.md) objects, implement this method to allow those services to better handle your data.

To ensure that Mail can handle an attachment that uses your exported UTI, include the [UTExportedTypeDeclarations](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/plist/info/UTExportedTypeDeclarations) key in your app’s `Info.plist` file, describing the UTI and providing the MIME type for it. The following example shows how `public.jpeg` might be defined as an exported type (only the required keys are shown):

```objc
<key>UTExportedTypeDeclarations</key>
        <array>
            <dict>
                <key>UTTypeIdentifier</key>
                <string>public.jpeg</string>
                <key>UTTypeConformsTo</key>
                <array>
                    <string>public.image</string>
                    <string>public.data</string>
                </array>
                <key>UTTypeTagSpecification</key>
                <dict>
                    <key>com.apple.ostype</key>
                    <string>JPEG</string>
                    <key>public.filename-extension</key>
                    <array>
                        <string>jpeg</string>
                        <string>jpg</string>
                    </array>
                    <key>public.mime-type</key>
                    <string>image/jpeg</string>
                </dict>
            </dict>
        </array>
```

## See Also

### Providing information about the data items

- [- activityViewController:subjectForActivityType:](<activityviewcontroller(__subjectforactivitytype_).md>) — For activities that support a subject field, returns the subject for the item.
- [- activityViewController:thumbnailImageForActivityType:suggestedSize:](<activityviewcontroller(__thumbnailimageforactivitytype_suggestedsize_).md>) — For activities that support a preview image, returns a thumbnail preview image for the item.
