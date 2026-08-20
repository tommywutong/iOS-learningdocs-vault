---
title: 资源编程指南
apple_id: 10000051i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/ImageSoundResources/ImageSoundResources.html
archived_at: '2026-07-15T07:16:32.533200Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [资源编程指南](About%20Resources.md)


[下一页](Data%20Resource%20Files.md)[上一页](String%20Resources.md)

# 图像、声音和视频资源

OS X 和 iOS 平台在设计之初就致力于提供丰富的多媒体体验。为了支撑这种体验，两个平台都为在应用程序中加载和使用图像、声音和视频资源提供了充分的支持。图像资源常用于绘制应用程序用户界面的各个部分。声音和视频资源使用得相对较少，但同样能提升应用程序的整体观感和吸引力。以下各节介绍在应用程序中处理图像、声音和视频资源时可以使用的支持。

借助 Xcode，你可以在 nib 文件中引用应用程序的声音和图像文件。这样做可以把这些图像或声音与视图或控件的不同属性关联起来。例如，你可以设置图像视图默认显示的图像，或者设置按钮要显示的图像。在 nib 文件中建立这样的连接，省去了以后加载 nib 文件时再去建立连接的麻烦。

要让图像和声音资源在 nib 文件中可用，你只需把它们添加到 Xcode 工程中；Xcode 随后会在库面板里列出它们。当你与某个资源文件建立连接时，Xcode 会在 nib 文件中记录下这个连接。加载时，nib 加载代码会在工程 bundle 中查找该资源——Xcode 在构建时应该已经把它放到了那里。

当你加载一个包含图像和声音资源引用的 nib 文件时，nib 加载代码会尽可能缓存这些资源，以便后续取用。例如，加载 nib 文件之后，你可以用 [NSImage](https://developer.apple.com/documentation/appkit/nsimage) 或 [UIImage](https://developer.apple.com/documentation/uikit/uiimage)（取决于你所在的平台）的 `imageNamed:` 方法取回与该 nib 文件关联的图像。在 OS X 中，你可以用 [NSSound](https://developer.apple.com/documentation/appkit/nssound) 的 [soundNamed:](https://developer.apple.com/documentation/appkit/nssound/1477318-soundnamed) 方法取回缓存的声音资源。

图像资源在大多数应用程序中都很常用。即使是非常简单的应用程序，也会用图像为控件和视图打造自定义外观。OS X 和 iOS 为使用 Objective-C 对象操作图像数据提供了广泛的支持。这些对象让使用图像变得极其简单，通常只需要几行代码就能加载并绘制图像。如果你不想使用 Objective-C 对象，也可以用 Quartz 通过基于 C 的接口来加载图像。以下各节分别介绍用每一种可用技术加载图像资源文件的过程。

要在 [Objective-C](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectiveC.html#//apple_ref/doc/uid/TP40008195-CH43) 中加载图像，你需要根据当前平台使用 [NSImage](https://developer.apple.com/documentation/appkit/nsimage) 或 [UIImage](https://developer.apple.com/documentation/uikit/uiimage) 对象。用 AppKit 框架为 OS X 构建的应用程序使用 `NSImage` 对象来加载并绘制图像，为 iOS 构建的应用程序则使用 `UIImage` 对象。在加载已有图像资源方面，这两个对象提供的行为几乎完全相同。你把应用程序 bundle 中图像文件的指针传给该对象来[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)它，图像对象会处理好加载图像数据的各种细节。

清单 3-1 展示了在 OS X 中如何使用 `NSImage` 类加载图像资源。定位到图像资源之后（本例中它位于应用程序 bundle 里），你只需用这个路径来初始化图像对象。初始化之后，你就可以用 `NSImage` 的方法绘制该图像，或者把这个对象传给其他能使用它的方法。要在 iOS 中完成完全相同的任务，你只需把代码中对 `NSImage` 的引用改成 `UIImage` 即可。

__清单 3-1__  加载图像资源

```objc
NSString* imageName = [[NSBundle mainBundle] pathForResource:@"image1" ofType:@"png"];
NSImage* imageObj = [[NSImage alloc] initWithContentsOfFile:imageName];
```

你可以用图像对象打开目标平台支持的任何类型的图像。每个对象通常都是更高级图像处理代码的轻量级包装。要在当前图形上下文中绘制图像，只需使用它的某个绘制相关方法即可。`NSImage` 和 `UIImage` 都提供了以几种不同方式绘制图像的方法。`NSImage` 类还为操作你所加载的图像提供了额外的支持。

关于 `NSImage` 和 `UIImage` 类的方法的信息，请参阅 _[NSImage Class Reference](https://developer.apple.com/documentation/appkit/nsimage)_ 和 _[UIImage Class Reference](https://developer.apple.com/documentation/uikit/uiimage)_。关于 `NSImage` 类附加特性的更详细信息，请参阅 _[Cocoa Drawing Guide](../Cocoa%20Drawing%20Guide/Introduction%20to%20Cocoa%20Drawing%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojq)_ 中的 [Images](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Images/Images.html#//apple_ref/doc/uid/TP40003290-CH208)。

如果你编写的是基于 C 的代码，可以结合使用 Core Foundation 和 Quartz 的调用把图像资源加载到应用程序中。Core Foundation 提供了定位图像资源并把相应图像数据加载到内存中的基础支持。Quartz 则把你加载到内存中的图像数据转换成可用的 [CGImageRef](https://developer.apple.com/documentation/coregraphics/cgimageref)，你的代码随后就能用它来绘制图像。

用 Quartz 加载图像有两种方式：数据提供者（data provider）和图像源（image source）对象。数据提供者在 iOS 和 OS X 中都可用。图像源对象只在 OS X v10.4 及更高版本中可用，但它借助 Image I/O 框架增强了数据提供者的基本图像处理能力。就加载和显示图像资源而言，这两种技术都很胜任。只有当你想更多地访问图像相关数据时，才可能更倾向于选择图像源而不是数据提供者。

清单 3-2 展示了如何用数据提供者加载一张 JPEG 图像。这个方法利用 Core Foundation 的 [bundle](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Bundle.html#//apple_ref/doc/uid/TP40008195-CH4) 支持在应用程序的主 bundle 中定位图像并获取指向它的 URL，然后用这个 URL 创建数据提供者对象，再为相应的 JPEG 数据创建一个 [CGImageRef](https://developer.apple.com/documentation/coregraphics/cgimageref)。（为简洁起见，本例省略了所有错误处理代码。你自己的代码应当确保所引用的数据结构都是有效的。）

__清单 3-2__  使用数据提供者加载图像资源

```c
CGImageRef MyCreateJPEGImageRef (const char *imageName);
{
    CGImageRef image;
    CGDataProviderRef provider;
    CFStringRef name;
    CFURLRef url;
    CFBundleRef mainBundle = CFBundleGetMainBundle();

    // 获取指向该 bundle 资源的 URL。
    name = CFStringCreateWithCString (NULL, imageName, kCFStringEncodingUTF8);
    url = CFBundleCopyResourceURL(mainBundle, name, CFSTR("jpg"), NULL);
    CFRelease(name);

    // 创建数据提供者对象
    provider = CGDataProviderCreateWithURL (url);
    CFRelease (url);

    // 用该提供者创建图像对象。
    image = CGImageCreateWithJPEGDataProvider (provider, NULL, true,
                                    kCGRenderingIntentDefault);
    CGDataProviderRelease (provider);

    return (image);
}
```

关于处理 Quartz 图像的详细信息，请参阅 _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_。关于数据提供者的参考信息，请参阅 _Quartz 2D Reference Collection_（OS X）或 _Core Graphics Framework Reference_（iOS）。

iOS 应用应当包含其图像资源的高分辨率版本。当应用运行在配备高分辨率屏幕的设备上时，高分辨率图像能提供更多细节，看起来也更好，因为它们无需缩放就能适配相应空间。你应当为应用程序 bundle 中的每个图像资源提供高分辨率版本，包括图标和启动图像。

要指定图像的高分辨率版本，请创建一个宽度和高度（以像素计）都是原图两倍的版本。多出来的像素用于提供更多细节。保存图像时，使用相同的基本名称，但在基本文件名和文件扩展名之间加上字符串 `@2x`。例如，如果你有一张名为 `MyImage.png` 的图像，其高分辨率版本的名称就是 `MyImage@2x.png`。请把图像的高分辨率版本和原始版本放在应用程序 bundle 中的同一位置。

当底层设备配备高分辨率屏幕时，bundle 加载例程和图像加载例程会自动查找带 `@2x` 字符串的图像文件。如果你把 `@2x` 字符串与其他修饰符组合使用，`@2x` 字符串应当位于所有设备修饰符之前，但位于其他所有修饰符（例如启动方向或 URL scheme 修饰符）之后。例如：

- `MyImage.png` - 图像资源的默认版本。
- `MyImage@2x.png` - 面向配备 Retina 显示屏的设备的图像资源高分辨率版本。
- `MyImage~iphone.png` - 面向 iPhone 和 iPod touch 的图像版本。
- `MyImage@2x~iphone.png` - 面向配备 Retina 显示屏的 iPhone 和 iPod touch 设备的图像高分辨率版本。

当你要加载图像时，在代码中指定图像名称时不要包含 `@2x` 或任何设备修饰符。例如，如果你的应用程序 bundle 包含了前面列表中的那些图像文件，你应该请求名为 `MyImage.png` 的图像。系统会自动判断哪个版本的图像最合适并加载它。同样，在使用或绘制该图像时，你也不需要知道它是原始分辨率版本还是高分辨率版本。图像绘制例程会根据实际加载到的图像自动调整。不过，如果你仍然想知道某张图像是原始版本还是高分辨率版本，可以检查它的缩放因子。如果图像是高分辨率版本，它的缩放因子会被设置为 `1.0` 以外的值。

关于如何支持高分辨率设备的更多信息，请参阅 [Supporting High-Resolution Screens In Views](https://developer.apple.com/library/archive/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/SupportingHiResScreensInViews/SupportingHiResScreensInViews.html#//apple_ref/doc/uid/TP40010156-CH15)。

[下一页](Data%20Resource%20Files.md)[上一页](String%20Resources.md)

