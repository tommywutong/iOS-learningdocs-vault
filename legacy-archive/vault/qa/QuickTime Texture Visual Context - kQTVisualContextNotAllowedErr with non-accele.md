---
title: QuickTime Texture Visual Context - kQTVisualContextNotAllowedErr with non-accelerated
  graphics cards
apple_id: DTS10004429
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2007-09-18'
source_url: https://developer.apple.com/library/archive/qa/qa1542/_index.html
archived_at: '2026-07-18T02:32:15.745081Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1542

# QuickTime Texture Visual Context - kQTVisualContextNotAllowedErr with non-accelerated graphics cards

## Q:  I'm working with QTCoreVideo101 but it never returns a VisualContextRef. Calling `QTOpenGLTextureContextCreate` always fails with error -9459. I have a Mac Pro system with a third party video card for Final Cut Pro. How can I create a QuickTime OpenGL Texture Visual Context?

A: I'm working with QTCoreVideo101 but it never returns a VisualContextRef. Calling `QTOpenGLTextureContextCreate` always fails with error -9459. I have a Mac Pro system with a third party video card for Final Cut Pro. How can I create a QuickTime OpenGL Texture Visual Context?

The most likely reason for the -9459 (`kQTVisualContextNotAllowedErr`) error is the third party video card. If the card presents itself as a video device but does not support accelerated surfaces `QTOpenGLTextureContextCreate` will fail.

To successfully create a QuickTime OpenGL Texture Visual Context, the non-accelerated display(s) may be masked out by creating a display mask (simply a bitmask used to specify a set of attached displays) that only identifies the displays supporting accelerated surfaces. This can be done using Quartz Display Services APIs such as `CGDisplayUsesOpenGLAcceleration` and `CGDisplayIDToOpenGLDisplayMask`.

This display mask (with the non-accelerated display(s) masked out) is then used when creating the OpenGL Pixel Format object. This Pixel Format object is used when creating the OpenGL Context and when calling `QTOpenGLTextureContextCreate`.

Listing 1 demonstrates how to build the display mask, while listing 2 demonstrates how to use the returned display mask when creating the `NSOpenGLPixelFormat` object.

__Listing 1__  Return the Accelerated Display Mask.

```
static CGOpenGLDisplayMask GetTheAcceleratedDisplayMask(void) {      const CGDisplayCount maxDisplays = sizeof(CGOpenGLDisplayMask) * 8; // the number of displays      CGDirectDisplayID displays[maxDisplays]; // represents the unique identifier for an attached display     CGDisplayCount display, displayCount;     CGOpenGLDisplayMask displayMask = 0; // bitmask used in OpenGL to specify a set of attached displays      // get the list of displays that are active (or drawable)     if (CGGetActiveDisplayList(maxDisplays, displays, &displayCount) == kCGErrorSuccess) {          // does the display support acceleration         for (display = 0; display < displayCount; display++) {              if (CGDisplayUsesOpenGLAcceleration(displays[display])) {                 // it does, so get the OpenGL display mask for the display and update our display mask                 displayMask |= CGDisplayIDToOpenGLDisplayMask(displays[display]);             }         }     }      // return our display mask that now has all the non-accelerated displays filtered out     return displayMask; }
```

In listing 1, we need the __active__ display list. An active display is connected, __awake__ and available for drawing, while a display is considered online simply when the frame buffer is connected to a monitor.

In a hardware mirroring set, only the primary display is active.

__Listing 2__  Using the Display Mask by Subclassing NSOpenGLView

```objc
@interface MyOpenGLView : NSOpenGLView {     ...      QTVisualContextRef mQTOpenGLTextureVisualContext; }     ...  - (QTVisualContextRef)visualContext; - (void) setVisualContextRef:(QTVisualContextRef)inVisualContext;      ... @end  @implementation MyOpenGLView  + (NSOpenGLPixelFormat *)defaultPixelFormat {     // create an NSOpenGLPixelFormat object with the appropriate display mask     CGOpenGLDisplayMask myDisplayMask = GetTheAcceleratedDisplayMask();      if (0 != myDisplayMask) {         NSOpenGLPixelFormatAttribute attributes[] =         {             NSOpenGLPFADoubleBuffer, // double buffered pixel format             NSOpenGLPFAAccelerated,  // hardware accelerated renderer             NSOpenGLPFANoRecovery,   // disable all failure recovery systems             //** bit mask of supported physical screens **//             NSOpenGLPFAScreenMask, (NSOpenGLPixelFormatAttribute)myDisplayMask,             (NSOpenGLPixelFormatAttribute)0         };          return [[(NSOpenGLPixelFormat*)[NSOpenGLPixelFormat alloc]                                                             initWithAttributes:attributes] autorelease];     } else {         return [super defaultPixelFormat];     } }  - (id)initWithFrame:(NSRect)frameRect {     return [super initWithFrame:frameRect pixelFormat:[MyOpenGLView defaultPixelFormat]]; }  - (void)prepareOpenGL {     ...      if (nil != [self openGLContext]) {         long swapInterval = 1;         // sync with screen refresh to avoid tearing        [[self openGLContext] setValues:&swapInterval forParameter:NSOpenGLCPSwapInterval];     }      ...      // create the QuickTime Texture Visual Context for rendering to my custom NSOpenGLView     if (NULL == [self visualContextRef]) {         QTVisualContextRef aQTOpenGLTextureContext;          OSStatus status = QTOpenGLTextureContextCreate(kCFAllocatorDefault,                                          [[self openGLContext] CGLContextObj],                                          (CGLPixelFormatObj)[[self pixelFormat] CGLPixelFormatObj],                                          NULL, &aQTOpenGLTextureContext);         if (noErr == status) {             [self setVisualContextRef:aQTOpenGLTextureContext];              ...          } else {             [self setVisualContextRef:NULL];         }     }      ...  }     ...  - (QTVisualContextRef)visualContext {     return mQTOpenGLTextureVisualContext; }  - (void)setVisualContextRef:(QTVisualContextRef)inVisualContext {     mQTOpenGLTextureVisualContext = inVisualContext; }     ...
```


- [Introduction to Quartz Display Services Programming Topics](https://developer.apple.com/documentation/GraphicsImaging/Conceptual/QuartzDisplayServicesConceptual/Introduction/Introduction.html)
- [Introduction to OpenGL Programming Guide for Mac OS X](https://developer.apple.com/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/opengl_intro/chapter_1_section_1.html#//apple_ref/doc/uid/TP40001987-CH207-TP9)
- [What's New in QuickTime 7](https://developer.apple.com/documentation/QuickTime/Conceptual/QT7UpdateGuide/Chapter02/chapter_2_section_1.html#//apple_ref/doc/uid/TP40001163-CH313-DontLinkElementID_161)
- [Technical Q&A QA1218, 'How do I tell if a particular display is being hardware accelerated by Quartz Extreme?'](https://developer.apple.com/qa/qa2001/qa1218.html)
- [Sample Code 'QTCoreVideo101'](https://developer.apple.com/samplecode/QTCoreVideo101/index.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-09-18 | New document that discusses how to create a display mask and avoid a kQTVisualContextNotAllowedErr when using a non-accelerated graphics card. |

