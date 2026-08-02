---
title: Using Interface Builder's NSOpenGLView or Custom View objects for an OpenGL
  application
apple_id: DTS10003419
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2004-10-28'
source_url: https://developer.apple.com/library/archive/qa/qa1167/_index.html
archived_at: '2026-07-18T02:30:11.830330Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1167

# Using Interface Builder's NSOpenGLView or Custom View objects for an OpenGL application

## Q:  Should I use Interface Builder's `NSOpenGLView` object or the Custom View object when I'm creating a window to draw into with OpenGL?

A: While either one can be used to draw with OpenGL, the Custom View offers greater flexibility for the application than the `NSOpenGLView` in the palette with a minor amount of additional setup. The current Interface Builder inspector for `NSOpenGLView` offers a limited set of pixel format attributes, so applications that require additional pixel format attributes should instead use the Custom View approach. For instance, double buffering is not currently available as a pixel format attribute in the `NSOpenGLView` inspector.

Note that if the view is created by dragging an `NSOpenGLView` out of the Graphics Views palette, the initialization routines `-initWithFrame:` and `-initWithFrame:` `pixelFormat:` are not called for the `NSOpenGLView`. In this case, setup and initialization code should go into the view's `-awakeFromNib` method, however any calls that require an active OpenGL context (such as most of the `gl...()` type calls) must be made after an OpenGL context has been created and made current. The first time through the `-drawRect:` method is a good place for this. It is also worth mentioning that with a dragged-in `NSOpenGLView`, the pixel format and other initialization items usually placed in `-initWithFrame:` and `-initWithFrame:` `pixelFormat:` have already been done and are loaded when the nib file itself is loaded.

__Listing 1__  Sample setup for an `NSOpenGLView`

```objc
@interface OpenGLView
{
    // Instance variable to control our initialization code
    BOOL readyToDraw;
}
@end


-(void)awakeFromNib
{
     // Do any other initialization code needed
     // in here.
     readyToDraw = NO;
}

-(void)drawRect:(NSRect)rect
{
     // Check to see if we're initialized
    if(!readyToDraw)
    {
       // ... do some setup code here
       // we have a valid OpenGL context at this point

       // Make sure we set this so we don't reinitialize next time
       readyToDraw = YES;
    }
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-10-28 | Edited out the capital 'I' in NSOpenGLPixelFormat, Edited code block for -awakeFromNib to be more accurate, Edited code block to add the @interface section to show an instance variable, Added additional descriptive information regarding a dragged-in NSOpenGLView, Added 'NOTE:' box for text following code listing |
| 2004-10-04 | New document that describes usage cases for both NSOpenGLViews and Custom Views for Cocoa OpenGL applications |

