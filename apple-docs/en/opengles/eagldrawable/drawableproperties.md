---
title: drawableProperties
framework: OpenGL ES
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（12.0 起废弃）, iPadOS 2.0+（12.0 起废弃）, Mac Catalyst 2.0+（12.0 起废弃）, tvOS 9.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/opengles/eagldrawable/drawableproperties
source_url: 'https://developer.apple.com/documentation/opengles/eagldrawable/drawableproperties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/opengles/eagldrawable/drawableproperties.json'
content_hash: 'sha256:6b4d22987fc5e63a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [OpenGL ES](../../opengles.md) · [EAGLDrawable](../eagldrawable.md)

# drawableProperties

<sub>Instance Property</sub>

A dictionary of values that specify the desired characteristics of the drawable surface.

> [!warning] Deprecated
> OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var drawableProperties: [String : Any]? { get set }
```

## Discussion

The `drawableProperties` dictionary specifies the properties that are used by this object when it is attached to an OpenGL ES renderbuffer. Your application should set these properties before passing this object into the `EAGLContext` method [- renderbufferStorage:fromDrawable:](<../eaglcontext/renderbufferstorage(__from_).md>). If you change the `drawableProperties` dictionary, your application must call [- renderbufferStorage:fromDrawable:](<../eaglcontext/renderbufferstorage(__from_).md>) again on the context for the new values to take effect.

## See Also

### Related Documentation

- [OpenGL ES Programming Guide](https://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/OpenGLES_ProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008793)
