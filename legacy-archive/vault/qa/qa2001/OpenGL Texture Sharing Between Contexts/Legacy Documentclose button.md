---
title: OpenGL Texture Sharing Between Contexts
apple_id: DTS10001583
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2001-05-01'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1031.html
archived_at: '2026-07-18T02:38:03.639097Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Graphics & Imaging > OpenGL](https://developer.apple.com/referencelibrary/GraphicsImaging/idxOpenGL-date.html)

|  |
| --- |
| Technical Q&A QA1031OpenGL Texture Sharing Between Contexts |

|  |  |  |
| --- | --- | --- |
| ---   Q: How does one share textures between mulitple OpenGL contexts?  A: Textures can be easily shared between OpenGL contexts on Mac OS X and Mac OS 9.     |  | | --- | | ```  // From the "Carbon SetupGL" sample code (Carbon SetupGL.c line 733): *paglContext = aglCreateContext (pcontextInfo->fmt, aglShareContext); if (aglShareContext == NULL)     aglShareContext = *paglContext; --- // From the "Carbon SetupGL" sample code (Carbon SetupGL Test.c line 576): // gTexture is the global texturing flag. // structWindowInfo contains the agl context for each window // (stored in the window's refcon) // LoadTextureRes just loads a buffer from a resource file long i = 0; GLbyte * pBuffer = NULL; short width = 0, height = 0; gTexture = 1 - gTexture; if (gTexture) {     if (gpWindowList[0] != NULL) // load the texture for the first window     {         structWindowInfoPtr pWindowInfo =                 (structWindowInfoPtr) GetWRefCon (gpWindowList [i]);         aglSetCurrentContext(pWindowInfo->aglContext);         glEnable (GL_TEXTURE_2D);         if (nameTexture)             glDeleteTextures (1, &nameTexture);         glGenTextures (1, &nameTexture);         glBindTexture(GL_TEXTURE_2D, nameTexture);         LoadTextureRes (1000, &pBuffer, &width, &height);         glTexImage2D (GL_TEXTURE_2D, 0, 3, width, height, 0,                       GL_RGB, GL_UNSIGNED_BYTE, pBuffer);     } } // enable texturing for all windows but do not load texture again for (i = 0; kMaxWindows > i; i++) {     if (gpWindowList[i] != NULL)     {         structWindowInfoPtr pWindowInfo =                 (structWindowInfoPtr) GetWRefCon (gpWindowList [i]);         aglSetCurrentContext(pWindowInfo->aglContext);         if (gTexture)         {             glEnable (GL_TEXTURE_2D);             glBindTexture(GL_TEXTURE_2D, nameTexture);         }         else             glDisable (GL_TEXTURE_2D);     } } if (pBuffer)     DisposePtr ((Ptr) pBuffer); ``` | | __Listing 1__. Creating shared contexts and textures |     First, create all contexts as shared contexts (see below). The requirement to create all contexts first maybe lifted in future versions of Mac OS X. Once all contexts are created, create the texture(s) and texture to any one context. All other contexts will share the texture that is current or one that you can bind via glBindTexture.  The specifics:  - Create shared contexts:  The first part of the code in listing 1 shows the creation of shared contexts. Where the global/static variable aglShareContext is the context to share. aglShareContext is initially set globally to NULL and then set to the first context created for all other contexts. This will, in effect, share all contexts.  - Load and share textures:  The second half of the code in listing 1 shows how to load a texture for the first context and then just bind this for use with the other contexts.  This technique is illustrated completely in the "Carbon SetupGL" sample on the sample code web site at <http://developer.apple.com/samplecode/>.   ---  [May 01 2001] |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
