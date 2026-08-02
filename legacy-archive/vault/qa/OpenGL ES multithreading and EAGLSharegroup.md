---
title: OpenGL ES multithreading and EAGLSharegroup
apple_id: DTS40009659
resource_type: QA
platform: iOS
topic: Graphics & Animation
technology: OpenGLES
published: '2010-03-09'
source_url: https://developer.apple.com/library/archive/qa/qa1612/_index.html
archived_at: '2026-07-18T02:32:42.201221Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1612

# OpenGL ES multithreading and EAGLSharegroup

## Q:  In my multithreading OpenGL ES application, I load textures (or vertices) on a secondary thread then draw them onto screen on the main thread. Occasionally I see blank images or application freezes. What could be causing this?

A: In my multithreading OpenGL ES application, I load textures (or vertices) on a secondary thread then draw them onto screen on the main thread. Occasionally I see blank images or application freezes. What could be causing this?

It is very likely that the main and background threads are accessing the same OpenGL ES context simultaneously.

OpenGL ES commands for a specific context are not reentrant. You should never have more than one thread accessing a single context at the same time. It is highly recommended that you use only one thread per context.

__Listing 1__ demonstrates how to create and make current a context `contextB` using the `sharegroup` property (an `EAGLSharegroup` object) obtained from another already-allocated context `contextA`. Such contexts that belong to the same sharegroup can share resources, for example, textures, FBOs, etc. So you may use `contextB` on the secondary thread to create textures, and `contextA` on the main thread to draw the textures onto screen.

__Listing 1__  Creating a context belonging to the same sharegroup

```
contextB = [[EAGLContext alloc] initWithAPI:kEAGLRenderingAPIOpenGLES1                                   sharegroup:contextA.sharegroup]; if (!contextB || ![EAGLContext setCurrentContext:contextB]) {        // Handle errors here }
```

When you want to modify a resource on one context, you must first make sure it is not currently in use on another, even if you are accessing them from different threads. Once you modify it, its state is undefined until flushing and binding the object have been completed. You should never use an undefined object, whether you access it from a different context or not.

Take a texture as an example. __Listing 2__ shows the correct way to deal with multiple contexts. Any other ordering will not ensure consistent and correct behavior. It may result in data corruption, leaks, or crashes otherwise.

__Listing 2__  Modifying a texture on context B prior to using it on context A

```
// 1. Ensure context A is not bound to the texture [EAGLContext setCurrentContext:contextA]; glBindTexture(GL_TEXTURE_2D, 0);  // 2. Call flush on context A  glFlush();   // 3. Modify the texture on context B [EAGLContext setCurrentContext:contextB]; glBindTexture(GL_TEXTURE_2D, texId); // // Modify the texture data here //  // 4. Call flush on context B glFlush();   // 5. Rebind the texture on context A [EAGLContext setCurrentContext:contextA]; glBindTexture(GL_TEXTURE_2D, texId);  // 6. Use the texture as normal on context A
```

For more information on the `EAGLContext/-initWithAPI:sharegroup:` API and the `sharegroup` property, see the [EAGLContext Class Reference](https://developer.apple.com/iphone/library/documentation/OpenGLES/Reference/EAGLContext_ClassRef/Reference/EAGLContext.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-03-09 | New document that discusses best practices for developing multithreading OpenGL ES applications with the EAGLSharegroup class. |

