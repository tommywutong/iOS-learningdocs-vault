---
title: Supporting Multiple GPUs on Mac OS X
apple_id: DTS40008924
resource_type: Technical Note
platform: macOS
topic: Performance
technology: null
published: '2009-06-05'
source_url: https://developer.apple.com/library/archive/technotes/tn2229/_index.html
archived_at: '2026-07-26T19:54:09.639264Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2229

# Supporting Multiple GPUs on Mac OS X

Multiple GPU support has existed in Mac OS X for a long time, and with the introduction of the Late 2008 MacBook Pro brings the first Macintosh hardware that comes standard with 2 GPUs. This makes it more important than ever to ensure that your application works correctly with multiple GPUs. This document describes what you need to know for your OpenGL content to render correctly on all hardware.

[What you should know when supporting Multiple GPUs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqojsgqwugsbrfvjukq2ujfhu4mi)[Enabling usage of offline renderers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqojsgqwugsbrfvjukq2ujfhu4mq)[Using CGLQueryRendererInfo](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqojsgqwugsbrfvjvkqstivbviskpjyza)[Detecting Renderer Changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqojsgqwugsbrfvjukq2ujfhu4na)[Registering for Display Change notifications using Quartz Display Services](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqojsgqwugsbrfvjvkqstivbviskpjy2a)[Using NSOpenGLView](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqojsgqwugsbrfvjvkqstivbviskpjy2q)[PBuffers vs OpenGL Textures and Buffer Objects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqojsgqwugsbrfvjukq2ujfhu4ny)[Choosing the correct renderer for a PBuffer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqojsgqwugsbrfvjvkqstivbviskpjy3q)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqojsgqwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## What you should know when supporting Multiple GPUs

All OpenGL application developers should read and understand the concepts described in the documents below. Understanding these concepts will prevent subtle bugs and allow your application to better take advantage of the GPU resources available on a users system.

[Technical Q&A QA1248: Context Sharing Tips](https://developer.apple.com/qa/qa2001/qa1248.html) describes what context sharing is, how its used and what is shared. These concepts are important whenever working with multiple OpenGL contexts, and should be well understood before attempting to work with multiple GPUs. You should note that Fullscreen contexts only support one GPU at a time, thus making sharing more complex. If you need to cover multiple displays with OpenGL content, then you can simply create a normal context that covers the entire display instead.

[Technical Note TN2080: Understanding and Detecting OpenGL Functionality](https://developer.apple.com/technotes/tn2002/tn2080.html) describes how you can detect changes in OpenGL functionality when the active hardware renderer changes. Properly detecting OpenGL functionality and changing your rendering paths to accommodate is vital to rendering correctly.

The _[Quartz Display Services Programming Topics](../documentation/Graphics%20Imaging/Quartz%20Display%20Services%20Programming%20Topics/Notification%20of%20Configuration%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2demzv)_ chapter of _[Quartz Display Services Programming Topics](../documentation/Graphics%20Imaging/Quartz%20Display%20Services%20Programming%20Topics/Introduction%20to%20Quartz%20Display%20Services%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denbv)_ describes how your application can detect screen configuration changes, which is necessary to know when you need to requery OpenGL capabilities and is especially vital if you are using PBuffers.

The [Introduction to OpenGL Programming Guide for Mac OS X](../documentation/Graphics%20Imaging/OpenGL%20Programming%20Guide%20for%20Mac/About%20OpenGL%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqmrqg4) describes many key concepts for using OpenGL on Mac OS X, including the concept of virtual screens, a core concept when working with OpenGL on Mac OS X in general. In particular you will want to be certain you are familiar with the techniques in the [Updating a Rendering Context](../documentation/Graphics%20Imaging/OpenGL%20Programming%20Guide%20for%20Mac/Working%20with%20Rendering%20Contexts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqmrrgywvgvzv) section.

The most important thing to remember is that applications that plan to take maximum advantage of OpenGL hardware should have already implemented most of what this document describes. The primary changes this document describes are for understanding these same concepts in the context of working with hardware that has multiple GPUs installed.

In any configuration where there are more GPUs than displays then at least 1 of these GPUs is considered to be "offline". Offline GPUs typically do not participate in hardware renderer selection, as this hardware has no means of displaying content, yet it is still sometimes useful to be able to take advantage of this hardware. On the other hand, the default behavior of OpenGL is designed to ensure that rendering typically occurs on GPUs that are capable of displaying that content. This document describes what you need to do to both take advantage of offline GPUs and ensure that your final rendering always occurs to an online GPU.

In order to do this, you must inform the OpenGL implementation that your application understands how to work correctly with both online and offline GPUs (described in Enabling usage of offline renderers). Once you've informed the implementation of this, then you need to arrange to receive notifications of GPU status changes (see Detecting Renderer Changes). When GPU status changes occur, you need to re-query the renderer capabilities in order to ensure that your rendering continues correctly, as the online renderer you wish to draw to may have changed. Finally, while all OpenGL objects (textures, buffer objects, etc) will retain their contents, display backing stores and PBuffers will need to be updated to ensure their contents remain valid (see PBuffers vs OpenGL Textures and Buffer Objects).

__Important:__ Apple recommends for best performance and convenience that your application always use Framebuffer Objects in preference to PBuffers.

[Back to Top](#)

## Enabling usage of offline renderers

Any Macintosh system configuration that includes more GPUs than displays will have both online and offline GPUs. Online GPUs are those that are connected to a display (such as an LCD panel or projector) while offline GPUs are those that have no such output hardware attached. One example of this is a Mac Pro configured with 2 video cards, but with displays only connected to one of those cards.

In these configurations you may wish to take advantage of the hardware that is not connected to a display, or to be able to start rendering on this hardware should a display be connected at a future date without having to reconfigure and reupload all of your OpenGL content. In order to enable this behavior you must add the appropriate attribute to your pixel format. For `NSOpenGL` you add `NSOpenGLPFAAllowOfflineRenderers`, for `CGL` add `kCGLPFAAllowOfflineRenderers` and for `AGL` add `AGL_ALLOW_OFFLINE_RENDERERS` to the attribute list you use to create your pixel format. To support Mac OS X 10.4 or earlier, you will need to remove this attribute from your attribute list, as otherwise pixel format creation will fail. Examples using `NSOpenGL` (Listing 1), `CGL` (Listing 2) and `AGL` (Listing 3) follow.

__Note:__ Instead of checking for an error when creating your OpenGL Context, you can instead check that the version of Mac OS X that your application is running on is at least Mac OS X 10.5. Additionally if you cannot use the Mac OS X 10.5 (or later) SDK then you will need to define the Allow Offline Renderer attribute yourself with a value of 96.

__Listing 1__  Creating an offline renderer aware Pixel Format with `NSOpenGL`.

```
NSOpenGLPixelFormatAttribute attribs[] = {     NSOpenGLPFAColorSize, 24,     NSOpenGLPFADoubleBuffer,     NSOpenGLPFAAllowOfflineRenderers, // lets OpenGL know this context is offline renderer aware     (NSOpenGLPixelFormatAttribute)0 }; pixFmt = [[NSOpenGLPixelFormat alloc] initWithAttributes:attribs];  #if MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_5 if(pixFmt == nil) {     // NSOpenGLPFAAllowOfflineRenderers is not supported on this OS version     attribs[3] = (NSOpenGLPixelFormatAttribute)0;     pixFmt = [[NSOpenGLPixelFormat alloc] initWithAttributes:attribs]; } #endif
```

__Listing 2__  Creating an offline renderer aware Pixel Format with `CGL`.

```
CGLPixelFormatAttribute attribs[] = {     kCGLPFAColorBits, 24,     kCGLPFADoubleBuffer,     kCGLPFAAllowOfflineRenderers, // lets OpenGL know this context is offline renderer aware     (CGLPixelFormatAttribute)0 }; CGLPixelFormatObj pixelFormatObj; GLint numPixelFormats; CGLError err;  err = CGLChoosePixelFormat(attribs, &pixelFormatObj, &numPixelFormats);  #if MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_5 if(err == kCGLBadAttribute) {     // kCGLPFAAllowOfflineRenderers is not supported on this OS version     attribs[3] = (CGLPixelFormatAttribute)0;     err = CGLChoosePixelFormat(attribs, &pixelFormatObj, &numPixelFormats); } #endif
```

__Listing 3__  Creating an offline renderer aware Pixel Format with `AGL`.

```
GLint attribs[] = {     AGL_COLOR_BITS, 24,     AGL_DOUBLE_BUFFER,     AGL_ALLOW_OFFLINE_RENDERERS, // lets OpenGL know this context is offline renderer aware     AGL_NONE }; AGLPixelFormat pixelFormatObj = aglChoosePixelFormat(NULL, 0, attribs); GLenum err = aglGetError();  #if MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_5 if(err == AGL_BAD_ATTRIBUTE || pixelFormatObj == NULL) {     // AGL_ALLOW_OFFLINE_RENDERERS is not supported on this OS version     attribs[3] = AGL_NONE;     pixelFormatObj = aglChoosePixelFormat(NULL, 0, attribs); } #endif
```

### Using CGLQueryRendererInfo

If your application links against the Mac OS X 10.4u SDK, then `CGLQueryRendererInfo`() won't return information about offline renderers, even when running on Mac OS X 10.5 or later. Apple recommends that you link against the Mac OS X 10.5 (or later) SDK and use the appropriate deployment target if your software needs to operate on 10.4 or earlier. If this is not possible then please contact [dts@apple.com](mailto:dts@apple.com)for assistance.

[Back to Top](#)

## Detecting Renderer Changes

Once your OpenGL context is configured to allow the hardware renderer to change, you will need to detect these changes by responding to Quartz Display Notifications (if you are not using `NSOpenGLView`) or by overriding `-update` (if you are using an `NSOpenGLView` subclass) in order to properly detect functionality changes. If you do not, then your OpenGL drawing may fail in various potentially catastrophic ways. Whenever the virtual screen changes, the capabilities of the video card you are currently rendering to can change, so you must re-query those capabilities and adjust your drawing paths as necessary to support the newly active GPU.

### Registering for Display Change notifications using Quartz Display Services

Using Quartz Display Services is appropriate if your application is not based on `NSOpenGLView`, regardless of if your application is windowed or fullscreen. You can register for display change notifications using `CGDisplayRegisterReconfigurationCallback` and request to stop receiving such notifications with `CGDisplayRemoveReconfigurationCallback`. Listing 4 demonstrates how to register for these notifications.

__Listing 4__  Detecting virtual screen changes with Quartz Display Services.

```
void MyDisplayReconfigurationCallBack(CGDirectDisplayID display, CGDisplayChangeSummaryFlags flags, void *userInfo);  // When the application has finished launching, // this message is sent to the Application Delegate // We use it to register for display reconfiguration notices. - (void)applicationDidFinishLaunching:(NSNotification *)aNotification {     CGDisplayRegisterReconfigurationCallback(MyDisplayReconfigurationCallBack, self); }  // Before the application terminates we'll remove our registration callback. // This isn't strictly necessary, but we demonstrate this here in case you have // more complex logic for removing the configuration callback // (for example, you might remove the callback when you have no windows open). - (void)applicationWillTerminate:(NSNotification *)aNotification {     CGDisplayRemoveReconfigurationCallback(MyDisplayReconfigurationCallBack, self); }  // When displays are reconfigured our callback will be called. You can take this opportunity // to do further processing or pass the notification on to an object for further handling. // In this example we've passed 'self' for the userInfo pointer, // so you can cast it to an appropriate object type and forward the message onwards. void MyDisplayReconfigurationCallBack(     CGDirectDisplayID display,     CGDisplayChangeSummaryFlags flags,     void *userInfo) {     if (flags & kCGDisplaySetModeFlag)     {         // Display has been reconfigured.         // Adapt to any changes in capabilities         // (such as max texture size, extensions and hardware capabilities such as the amount of VRAM).     } }
```

### Using NSOpenGLView

If you are using `NSOpenGLView` it automatically registers for notification of changes to the display configuration for you and calls its own `-update` method in response to those changes. You can then override `-update` to provide additional handling as shown in Listing 5.

__Listing 5__  Detecting virtual screen changes with an `NSOpenGLView`.

```objc
-(void) update {     [super update];     GLint newVirtualScreen = [[self openGLContext] currentVirtualScreen];     if (currentVirtualScreen != newVirtualScreen)     {         currentVirtualScreen = newVirtualScreen;         // Adapt to any changes in capabilities         // (such as max texture size and hardware capabilities).     } }
```

[Back to Top](#)

## PBuffers vs OpenGL Textures and Buffer Objects

It is highly recommended that you use Framebuffer Objects over PBuffers whenever possible. If you must work with PBuffers you need to ensure that the virtual screen of the PBuffer uses the same device of the context that you wish to draw its contents into. When the virtual screen of a PBuffer changes, its conents will be lost, so you need to update the PBuffer's contents at that time. Examples for `AGL` (Listing 6) and `CGL` (Listing 7) follow.

__Warning:__ An OpenGL context will not have had a virtual screen assigned to it until after you've shaped the context at least once, as these processes cause the context to be assigned to a device. Checking for the virtual screen of a context before it is assigned to a device will not produce a meaningful result.

__Listing 6__  Updating a PBuffer with `AGL`.

```
void MyAGLPBufferDraw(     AGLContext targetCtx,     AGLContext pbufferCtx,     AGLPbuffer pbuffer,     GLint *pbVS) {     // make PBuffer context current (as we are drawing into the PBuffer with it)     GLboolean success = aglSetCurrentContext(pbufferCtx);      GLint targetVS = aglGetVirtualScreen(targetCtx);     if(*pbVS != targetVS)     {         *pbVS = targetVS;         success = aglSetPBuffer(pbufferCtx, pbuffer, 0, 0, targetVS);          // re-query capabilities, including VRAM, if needed         // rebuild assets only as needed such as with max texture size shrinking         // set any state needed to make next draw use proper rendering paths     }      // ...     // Do drawing into PBuffer here     // ...      // make available to the target context - use glFlushRenderAPPLE for single buffered contexts     glFlushRenderAPPLE();       aglSetCurrentContext(NULL); // ensure we are not still drawing to PBuffer }
```

__Listing 7__  Updating a PBuffer with `CGL`.

```
void MyCGLPBufferDraw(     CGLContext targetCtx,     CGLContext pbufferCtx,     CGLPBufferObj pbuffer,     GLint *pbVS) {     CGLError err;      // make PBuffer context current (as we are drawing into the PBuffer with it)     err = CGLSetCurrentContext(pbufferCtx);      GLint targetVS;     err = CGLGetVirtualScreen(targetCtx, &targetVS);     if(*pbVS != targetVS)     {         *pbVS = targetVS;         err = CGLSetPBuffer(pbufferCtx, pbuffer, 0, 0, targetVS);          // re-query capabilities, including VRAM, if needed         // rebuild assets only as needed such as with max texture size shrinking         // set any state needed to make next draw use proper rendering paths     }      // ...     // Do drawing into PBuffer here     // ...      // make available to the target context - use glFlushRenderAPPLE for single buffered contexts     glFlushRenderAPPLE();       CGLSetCurrentContext(NULL); // ensure we are not still drawing to PBuffer }
```

### Choosing the correct renderer for a PBuffer

If you have a PBuffer whose contents are never displayed via OpenGL (such as might be the case if you use a PBuffer for GPGPU work) then you will need to determine a device for the PBuffer based on some onscreen element. Assuming that you don't have any onscreen OpenGL contexts that you can use for this assignment, the simplest way to do so is to use a pixel format attribute to assign the PBuffer to a device capable of rendering to the main screen. See Listing 8

__Listing 8__  Determining a virtual screen from an NSWindow

```
NSOpenGLPixelFormat *CreatePixelFormat() {     // Create pixel format     NSOpenGLPixelFormatAttribute attributes[] =     {         NSOpenGLPFADoubleBuffer,         NSOpenGLPFANoRecovery,         NSOpenGLPFAAccelerated,         // If this attribute is used on an OS that doesn't understand it         // then pixel format creation will fail. You can use one of the         // techniques described above to verify if the         // NSOpenGLPFAAllowOfflineRenderers pixel format attribute         // is supported.         NSOpenGLPFAAllowOfflineRenderers,         (NSOpenGLPixelFormatAttribute)0,     };     return [[NSOpenGLPixelFormat alloc] initWithAttributes:attributes]; }  GLint VirtualScreenForWindow(NSWindow *window) {     // If we're passed nil, then use the menu bar screen.     NSScreen *screen = (window != nil) ? [window screen] : [[NSScreen screens] objectAtIndex:0];      CGDirectDisplayID displayID = (CGDirectDisplayID)[[[screen deviceDescription]         objectForKey:@"NSScreenNumber"] unsignedIntValue];     if (displayID == 0)     {         // This is an error case because NSScreen does not have the necessary key.         // This should never happen.         return -1; // Error case     }      CGOpenGLDisplayMask currentDisplaymask = CGDisplayIDToOpenGLDisplayMask(displayID);     if(currentDisplaymask == 0)     {         // The display ID is unknown and not mappable to an OpenGL context         // This should never happen.         return -1; // Error case     }      // create pixel format     NSOpenGLPixelFormat *pixelFormat = CreatePixelFormat();      // find virtual screen     GLint virtualScreen = 0;     GLint numberOfVirtualScreen = [pixelFormat numberOfVirtualScreens];     GLint i;     for(i = 0; i < numberOfVirtualScreen; i++)     {         GLint mask;         [pixelFormat getValues:&mask             forAttribute:NSOpenGLPFAScreenMask forVirtualScreen:i];         if(mask & currentDisplaymask)         {             virtualScreen = i;             break;         }     }     [pixelFormat release];      return virtualScreen; }
```

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-06-05 | New document that describes what you need to know to take maximum advantage of multiple GPU configurations. |

