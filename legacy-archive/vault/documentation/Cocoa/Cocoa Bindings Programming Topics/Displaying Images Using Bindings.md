---
title: Cocoa Bindings Programming Topics
apple_id: 10000167i
resource_type: Guide
platform: macOS
topic: General
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/Tasks/images.html
archived_at: '2026-07-15T07:12:17.049797Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Bindings Programming Topics](Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md)


[Next](Implementing%20To-One%20Relationships%20Using%20Pop-Up%20Menus.md)[Previous](Creating%20a%20Master-Detail%20Interface.md)

# Displaying Images Using Bindings

You typically display images using either an NSImageCell or an NSImageView. You might display images in table columns in a master interface, or an image view in a detail interface. Both of these components have similar bindings and therefore are both discussed in this article. When using these components, you also need to make similar decisions about how you want to store and access your images. The value bindings of these components support a variety of formats. You can specify the value binding using an NSImage, a file path or a URL.

The example presented in this article is an extension of those in [Creating a Master-Detail Interface](Creating%20a%20Master-Detail%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsga4talkcineugqkejbbq). Specifically, this article explains how to add an NSImageCell to a table column in the master interface (shown in Figure 1) and an NSImageView to the detail interface. This article also contains an example of a custom value transformer that converts image filenames to absolute paths.

See [Creating a Master-Detail Interface](Creating%20a%20Master-Detail%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsga4talkcineugqkejbbq) for the steps to create a basic master-detail interface.

__Figure 1__  Using an NSImageCell in an NSTableColumn

!

How you define image properties in your models depends on your application—it depends on how you want to store and access the images. If the images are stored on disk or in your project folder on the same computer, then you can access them via a file path. If the images are stored not on disk but on a remote server, then you can access them via a URL. If the images are stored in some data source, then you might load the images directly into memory. If you load them, you might define your image properties as simply NSImage objects. Fortunately, Cocoa bindings supports all these options.

In this example, the model uses an NSImage to represent the `image` property of a Media object as shown in [Figure 2](Creating%20a%20Master-Detail%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsga4taljrgiydcnrzfvbeeq2kirfegry) in [Creating a Master-Detail Interface](Creating%20a%20Master-Detail%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsga4talkcineugqkejbbq).

In the case of a file path or URL, you typically store only the filename in the model not the absolute path or URL (for example, you don’t want to update your models every time you move the image folder). However, the bindings expect an absolute path or URL. One solution is to implement a custom value transformer that takes an image filename and returns a file path or URL based on some variables you define. See [Using a Value Transformer to Convert Paths](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydaljrgi3dcmrw) to modify this example to use file paths instead of NSImage objects.

Next, you create the image views by either dragging an NSImageView to a window or an NSImageCell to the column that will display the images.

This example assumes you already have a working master-detail interface. Follow the steps in [Creating Controllers](Creating%20a%20Master-Detail%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsga4taljrge4tinrx) in Creating a Master-Detail Interface if you need to create an array controller.

Next, you bind the image views to the controllers. A subset of the value bindings of an NSImageView and an NSTableColumn (containing an NSImageCell) to choose from are:

- `value`—an NSImage object.
- `valuePath`—an absolute path to the image file.
- `valueURL`—a URL that returns the image file.

For example, you configure the `value` binding for the Image table column in [Figure 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydaljrgi4daobsfvbuuqsfjjcugqi) as follows:

1. Set `Bind to` to your array controller object. For example, `MediaAssetsController`.
2. Set `Controller Key` to `arrangedObjects` (the collection of objects being displayed).
3. Set `Model Key Path` to the NSImage property to display in that column. For example, in the media asset application, set the key path to `image`.

You configure the `value` binding for the NSImageView in the detail interface similarly, except that you set the `Controller Key` value to `selection` (that is, the currently selected object).

See [Using a Value Transformer to Convert Paths](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydaljrgi3dcmrw) for a variation of this example that uses the `valuePath` binding.

If you want to access your images using a file path, then you bind your views to your controllers using the `valuePath` binding instead. However, `valuePath` is expected to be an absolute file path. Typically, you do not store absolute paths in your models, just filenames or relative paths. You can convert a filename or relative path to an absolute path using a custom value transformer as follows.

First create a custom value transformer that takes the filename or relative path and converts it to an absolute path. You do this by subclassing NSValueTransformer and overriding the `transformedValueClass` and `allowsReverseTransformation` class methods, as shown in [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydaljrgi3timbzfvbeeq2iifaugsi).

You implement the `transformedValue:` method to perform the transformation. For example, the `transformedValue:` method implementation in Listing 1 assumes the images are located in the project `Resources` folder and uses NSBundle’s `resourcePath:` method to convert the filename to an absolute path. Note that you need to modify this example if you store the images somewhere else on the file system.

__Listing 1__  PathTransformer implementation file

```objc
#import "PathTransformer.h"

@implementation PathTransformer

+ (Class)transformedValueClass
{
    return [NSString self];
}

+ (BOOL)allowsReverseTransformation
{
    return NO;
}

- (id)transformedValue:(id)beforeObject
{
    if (beforeObject == nil) return nil;
    id resourcePath = [[NSBundle mainBundle] resourcePath];
    return [resourcePath stringByAppendingPathComponent:beforeObject];
}

@end
```


In order to use your custom value transformer, you must first register it with NSValueTransformer. Note that you register instances of a value transformer, not a subclass. You typically register value transformers in an `initialize` method or the application delegate’s `applicationDidFinishLaunching:` method. When you register a value transformer, you give it a logical name you can use later when configuring a bindings. For example, add the following code fragment to `applicationDidFinishLaunching:` to register an instance called `PathTransformer`:

```
id transformer = [[[PathTransformer alloc] init] autorelease];
[NSValueTransformer setValueTransformer:transformer forName:@"PathTransformer"];
```


Finally, you specify the value transformer when binding your views to your controllers using the `valuePath` binding. For example, you configure the `valuePath` binding for the Image table column as follows:

1. Set the `Bind to` aspect to your array controller object—for example, `MediaAssetsController`.
2. Set the `Controller Key` aspect to `arrangedObjects` (the collection of objects being displayed).
3. Set the `Model Key Path` aspect to the property containing the image filename. For example, in the media asset application, set the key path to `imagePath`.
4. Enter the transformer’s logical name, `PathTransformer` , in the Value Transformer text field.

Figure 2 shows the Bindings pane of an NSTableColumn in Interface Builder with the `valuePath` binding revealed and configured to use a custom value transformer.

__Figure 2__  Bindings pane of an NSTableColumn

!

To use the `valueURL` binding instead, implement a similar value transformer to convert filenames or relative paths to an appropriate NSURL object. Optionally, you can enhance the PathTransformer class to handle other types of filename transformations. In the latter case, register different instances using different names (for example, `PathTransformer` and `URLTransformer`) to handle each type of transformation.

[Next](Implementing%20To-One%20Relationships%20Using%20Pop-Up%20Menus.md)[Previous](Creating%20a%20Master-Detail%20Interface.md)

