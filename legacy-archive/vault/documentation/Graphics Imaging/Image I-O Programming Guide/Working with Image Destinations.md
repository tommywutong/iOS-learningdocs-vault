---
title: Image I/O Programming Guide
apple_id: TP40005462
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ImageIOGuide/ikpg_dest/ikpg_dest.html
archived_at: '2026-07-15T07:35:42.369438Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Image I/O Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Creating%20and%20Using%20Image%20Sources.md)

# Working with Image Destinations

An image destination abstracts the data-writing task and eliminates the need for you to manage data through a raw buffer. An image destination can represent a single image or multiple images. It can contain thumbnail images as well as properties for each image. After creating a CGImageDestination object for the appropriate destination (URL, CFData object, or Quartz data consumer), you can add image data and set image properties. When you are finished adding data, call the function [CGImageDestinationFinalize](https://developer.apple.com/documentation/imageio/1464968-cgimagedestinationfinalize).

The function [CGImageDestinationSetProperties](https://developer.apple.com/documentation/imageio/1464919-cgimagedestinationsetproperties) adds a dictionary ([CFDictionaryRef](https://developer.apple.com/documentation/corefoundation/cfdictionaryref)) of properties (key-value pairs) to the images in an image destination. Although setting properties is optional, there are many situations for which you will want to set them. For example, if your application allows users to add keywords to images or change saturation, exposure, or other values, you’ll want to save that information in the options dictionary.

Image I/O defines an extensive set of keys to specify such things as compression quality, background compositing color, Exif dictionary keys, color model values, GIF dictionary keys, Nikon and Canon camera keys, and many more. See _[CGImageProperties Reference](https://developer.apple.com/documentation/imageio/cgimageproperties)_.

When setting up the dictionary, you have two choices. You can either create a CFDictionary object or you can create an `NSDictionary` object, then cast it as a [CFDictionaryRef](https://developer.apple.com/documentation/corefoundation/cfdictionaryref) when you pass the options dictionary to the function [CGImageDestinationSetProperties](https://developer.apple.com/documentation/imageio/1464919-cgimagedestinationsetproperties). (CFDictionary and `NSDictionary` are interchangeable, or toll-free bridged.) Listing 3-1 shows a code fragment that assigns key-value pairs for three properties, then creates a dictionary that contains those properties. Because this is a code fragment, the necessary calls to release the CFNumber and CFDictionary objects created by the code are not shown. When you write your code, you need to call [CFRelease](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) when you no longer need each of these objects.

When you set up a key-value pair for a property, you need to consult the reference documentation (see _[CGImageDestination Reference](https://developer.apple.com/documentation/imageio/cgimagedestination)_ and _[CGImageProperties Reference](https://developer.apple.com/documentation/imageio/cgimageproperties)_) for the expected data type of the value. As you can see in Listing 3-1, numerical values typically need to be wrapped in a CFNumber object. When you use Core Foundation types for dictionary values, you can also supply the callback constants when you create the dictionary—[kCFTypeDictionaryKeyCallBacks](https://developer.apple.com/documentation/corefoundation/kcftypedictionarykeycallbacks) and [kCFTypeDictionaryValueCallBacks](https://developer.apple.com/documentation/corefoundation/kcftypedictionaryvaluecallbacks). (See _[CFDictionary Reference](https://developer.apple.com/documentation/corefoundation/cfdictionary)_.)

__Listing 3-1__  Setting the properties of an image destination

```
float compression = 1.0; // Lossless compression if available.
int orientation = 4; // Origin is at bottom, left.
CFStringRef myKeys[3];
CFTypeRef   myValues[3];
CFDictionaryRef myOptions = NULL;
myKeys[0] = kCGImagePropertyOrientation;
myValues[0] = CFNumberCreate(NULL, kCFNumberIntType, &orientation);
myKeys[1] = kCGImagePropertyHasAlpha;
myValues[1] = kCFBooleanTrue;
myKeys[2] = kCGImageDestinationLossyCompressionQuality;
myValues[2] = CFNumberCreate(NULL, kCFNumberFloatType, &compression);
myOptions = CFDictionaryCreate( NULL, (const void **)myKeys, (const void **)myValues, 3,
                      &kCFTypeDictionaryKeyCallBacks, &kCFTypeDictionaryValueCallBacks);
// Release the CFNumber and CFDictionary objects when you no longer need them.
```


To write an image to a destination, you first need to create an image destination object by calling the [CGImageDestinationCreateWithURL](https://developer.apple.com/documentation/imageio/1465361-cgimagedestinationcreatewithurl), [CGImageDestinationCreateWithData](https://developer.apple.com/documentation/imageio/1465133-cgimagedestinationcreatewithdata), or [CGImageDestinationCreateWithDataConsumer](https://developer.apple.com/documentation/imageio/1465231-cgimagedestinationcreatewithdata) functions. You need to supply the [UTI](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/UniformTypeIdentifier.html#//apple_ref/doc/uid/TP40008195-CH60) of the resulting image file. You can either supply a UTI or the equivalent constant, if one if available. See [Table 1-1](Basics%20of%20Using%20Image%20I-O.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrsfvbuqmrrgywvgvzt).

After you create an image destination, you can add an image to it by calling the [CGImageDestinationAddImage](https://developer.apple.com/documentation/imageio/1464962-cgimagedestinationaddimage) or [CGImageDestinationAddImageFromSource](https://developer.apple.com/documentation/imageio/1465143-cgimagedestinationaddimagefromso) functions. If the format of the image destination file supports multiple images, you can repeatedly add images. Calling the function [CGImageDestinationFinalize](https://developer.apple.com/documentation/imageio/1464968-cgimagedestinationfinalize) signals Image I/O that you are finished adding images. Once finalized, you cannot add any more data to the image destination.

Listing 3-2 shows how you might implement a method to write an image file. Although this listing shows how to use an image destination from within an Objective-C method, you can just as easily create and use an image destination in a procedural C function. The options parameter includes any properties you want to specify for the image, such as camera or compression settings.

__Listing 3-2__   A method that writes an image to a URL

```objc
- (void) writeCGImage: (CGImageRef) image toURL: (NSURL*) url withType: (CFStringRef) imageType andOptions: (CFDictionaryRef) options
{
   CGImageDestinationRef myImageDest = CGImageDestinationCreateWithURL((CFURLRef)url, imageType, 1, nil);
   CGImageDestinationAddImage(myImageDest, image, options);
   CGImageDestinationFinalize(myImageDest);
   CFRelease(myImageDest);
}
```


Image I/O can also be used to create animated images. When creating an animated image, you call [CGImageDestinationAddImage](https://developer.apple.com/documentation/imageio/1464962-cgimagedestinationaddimage) for each frame you want to add to the image. You must also specify other properties that control how the animation is performed.

Listing 3-3 shows how to create an animated PNG image. First it creates a pair of dictionaries to hold the animation properties. The first dictionary specifies the number of time the animated PNG should repeat its animation before stopping on the final frame. The second dictionary specifies the frame delay used by every frame in the sequence. After creating the image destination, the code sets the file properties for the destination image and then adds the frames, one at a time. Finally, the [CGImageDestinationFinalize](https://developer.apple.com/documentation/imageio/1464968-cgimagedestinationfinalize) method is called to complete the animated PNG.

__Listing 3-3__  Creating an animated PNG file

```swift
let loopCount = 1
let frameCount = 60

var fileProperties = NSMutableDictionary()
fileProperties.setObject(kCGImagePropertyPNGDictionary, forKey: NSDictionary(dictionary: [kCGImagePropertyAPNGLoopCount: frameCount]))

var frameProperties = NSMutableDictionary()
frameProperties.setObject(kCGImagePropertyPNGDictionary, forKey: NSDictionary(dictionary: [kCGImagePropertyAPNGDelayTime: 1.0 / Double(frameCount)]))

guard let destination = CGImageDestinationCreateWithURL(fileURL, kUTTypePNG, frameCount, nil) else {
    // Provide error handling here.
}

CGImageDestinationSetProperties(destination, fileProperties.copy() as? NSDictionary)

for i in 0..<frameCount {
    autoreleasepool {
        let radians = M_PI * 2.0 * Double(i) / Double(frameCount)
        guard let image = imageForFrame(size: CGSize(width: 300, height: 300)) else {
            return
        }

        CGImageDestinationAddImage(destination, image, frameProperties)
    }
}

if !CGImageDestinationFinalize(destination) {
    // Provide error handling here.
}
```

[Next](Document%20Revision%20History.md)[Previous](Creating%20and%20Using%20Image%20Sources.md)

