---
title: How to fix OpenGL ES application crashes when moving to the background
apple_id: DTS40012186
resource_type: QA
platform: iOS
topic: Graphics & Animation
technology: OpenGLES
published: '2012-04-09'
source_url: https://developer.apple.com/library/archive/qa/qa1766/_index.html
archived_at: '2026-07-27T07:25:59.558070Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1766

# How to fix OpenGL ES application crashes when moving to the background

## Q:  My OpenGL ES application crashes when moving to the background. How do I fix it?

A: If your OpenGL ES application crashes when moving to the background, and you get a crash report that contains a stack trace ending with `libGPUSupportMercury.dylib: gpus_ReturnNotPermittedKillClient + 0` as shown in __Listing 1__, it indicates that the application has attempted to do rendering with OpenGL ES in the background.

__Listing 1__  Stack trace

```
Thread 0 name: Dispatch queue: com.apple.main-thread
Thread 0 Crashed:
0   libGPUSupportMercury.dylib    	0x30570094 gpus_ReturnNotPermittedKillClient + 0
1   libGPUSupportMercury.dylib    	0x305700ae gpus_KillClient ( )
2   libGPUSupportMercury.dylib    	0x305705ba gpusSubmitDMABuffers ( )
3   IMGSGX535GLDriver             	0x34bd29b8 SubmitPacketsIfAny ( )
4   IMGSGX535GLDriver             	0x34bd2ad0 glrFlushContextToken ( )
5   GLEngine                      	0x37719c4a gliPresentViewES ( )
6   OpenGLES                      	0x323df6b4 -[EAGLContext presentRenderbuffer:] ( )
...
...
```

An OpenGL ES application will be terminated if it attempts to execute OpenGL ES commands in the background. Your application must ensure that all previously submitted commands have been finished and then stop rendering prior to moving into the background. See details about how to achieve this in the [Implementing a Multitasking-aware OpenGL ES Application](https://developer.apple.com/library/ios/#documentation/3DDrawing/Conceptual/OpenGLES_ProgrammingGuide/ImplementingaMultitasking-awareOpenGLESApplication/ImplementingaMultitasking-awareOpenGLESApplication.html#//apple_ref/doc/uid/TP40008793-CH5-SW1) chapter of the OpenGL ES Programming Guide for iOS.

See [Debugging Deployed iOS Apps](https://developer.apple.com/library/ios/#qa/qa1747/_index.html%23//apple_ref/doc/uid/DTS40011341) for information about how to get a crash report.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-04-09 | New document that describes how to fix OpenGL ES application crashes when moving to the background. |
