---
title: mediaTypes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/mediatypes
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/mediatypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/mediatypes.json'
content_hash: 'sha256:66361a4c1f7b8af9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# mediaTypes

<sub>Instance Property</sub>

An array that indicates the media types to access by the media picker controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var mediaTypes: [String] { get set }
```

## Discussion

Depending on the media types you assign to this property, the picker displays a dedicated interface for still images or movies, or a selection control that lets the user choose the picker interface. Before setting this property, check which media types are available by calling the [+ availableMediaTypesForSourceType:](<availablemediatypes(for_).md>) class method.

If you set this property to an empty array, or to an array in which none of the media types is available for the current source, the system throws an exception.

When capturing media, the value of this property determines the camera interface to display. When browsing saved media, this property determines the types of media presented in the interface.

By default, the value of this property is the [image](../../uniformtypeidentifiers/uttype-swift.struct/image.md) (Swift) or `kUTTypeImage` (Objective-C) identifier, which designates the still camera interface when capturing media, and specifies that only still images should be displayed in the media picker when browsing saved media. The following example shows how to designate the movie capture interface, or to indicate that only movies should be displayed when browsing saved media:

**Swift**

```swift
myImagePickerController.mediaTypes = [ UTType.movie.identifier ]
```

**Objective-C**

```objc
myImagePickerController.mediaTypes =
    [[NSArray alloc] initWithObjects: (NSString *) kUTTypeMovie, nil];
```

> [!note] Note
> If you want to display a Live Photo rendered as a Loop or a Bounce, you must include the [movie](../../uniformtypeidentifiers/uttype-swift.struct/movie.md) (Swift) or `kUTTypeMovie` (Objective-C) identifier.

To designate all available media types for a source, use a statement like this:

**Swift**

```swift
if let mediaTypes = UIImagePickerController.availableMediaTypes(for: .camera) {
    myImagePickerController.mediaTypes = mediaTypes
}
```

**Objective-C**

```objc
myImagePickerController.mediaTypes =
    [UIImagePickerController availableMediaTypesForSourceType:
        UIImagePickerControllerSourceTypeCamera];
```

## See Also

### Configuring the picker

- [allowsEditing](allowsediting.md) — A Boolean value that indicates whether the user is allowed to edit a selected still image or movie.
