---
title: 'init(fromDictionaryRepresentation:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avdepthdata/init(fromdictionaryrepresentation:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avdepthdata/init(fromdictionaryrepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdepthdata/init%28fromdictionaryrepresentation%3A%29.json'
content_hash: 'sha256:cc6f9d4bc29c1035'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDepthData](../avdepthdata.md)

# init(fromDictionaryRepresentation:)

<sub>Initializer</sub>

Creates a depth data object from depth information such as that found in an image file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(fromDictionaryRepresentation imageSourceAuxDataInfoDictionary: [AnyHashable : Any]) throws
```

## Parameters

- `imageSourceAuxDataInfoDictionary` — A dictionary of primitive depth-related information, in the format provided by the  [CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)](<../../imageio/cgimagesourcecopyauxiliarydatainfoatindex(______).md>) function.

## Discussion

When using `CGImageSource` functions to read from a HEIF, JPEG, or DNG file containing depth data (as well as image data), you can use the  [CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)](<../../imageio/cgimagesourcecopyauxiliarydatainfoatindex(______).md>) function to load primitive depth map information, then use this initializer to create an [AVDepthData](../avdepthdata.md) object, as shown below.

```swift
- (nullable AVDepthData *)depthDataFromImageData:(nonnull NSData *)imageData {
	AVDepthData *depthData = nil;

    CGImageSourceRef imageSource = CGImageSourceCreateWithData((CFDataRef)imageData, NULL);
	if (imageSource) {
		NSDictionary *auxDataDictionary = (__bridge NSDictionary *)CGImageSourceCopyAuxiliaryDataInfoAtIndex(imageSource, 0, kCGImageAuxiliaryDataTypeDisparity);
		if (auxDataDictionary) {
			depthData = [AVDepthData depthDataFromDictionaryRepresentation:auxDataDictionary error:NULL];
		}

		CFRelease(imageSource);
	}

    return depthData;
}
```

## See Also

### Creating depth data

- [- dictionaryRepresentationForAuxiliaryDataType:](<dictionaryrepresentation(forauxiliarydatatype_).md>) — Returns a dictionary representation of the depth data suitable for writing into an image file.
