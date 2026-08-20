---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/Advanced/Limitations.html
archived_at: '2026-07-15T07:50:05.836095Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Advanced.book.md)
[!Previous Section](CreateReusableComponent.md)

 Reusable Component Limitations

|  |  |
| --- | --- |
|  | ---  Reusable Component Limitations When you create a reusable component in WebObjects Builder, there are some limitations:   - Reusable components stored on a [custom palette](CreatePalette.md) must use only lower-case letters in the names of exported variables. When you store a component on the palette, all of its exported variables are   stored on the palette along with it. The palette ignores case. When you drag the   component off of the palette, the exported variable names appear in the inspector in all lower-case letters and are written out in the parent component's __.wod__   file that way. (The __.wod__ file stores bindings.)  For example, the child component may have an exported variable __alertString__.   After the child component is dragged from the palette to the parent component,   the bindings inspector displays that variable as __alertstring__. The parent component then binds to an __alertstring__ attribute. At run time, WebObjects tries to bind   the parent component's script to the __alertstring__ variable in the child component   fails because alertstring does not exist. - Form elements are surrounded by <FORM> tags. When you drag an element from the Form Elements palette to a component,   WebObjects Builder inserts a <FORM> tag before that component and a   </FORM> tag immediately after it. If you create a reusable component in this   manner and intend to use it inside a parent component's form, it won't work   because of the extra <FORM> tags.   As a workaround, you can do the following:    1. Create the component in WebObjects Builder, and then save it.   2. Open the component's HTML file (_MyComponent___.wo/___MyComponent___.html__) in      a text editor.   3. Delete the <FORM> start and end tags, then save the file. If you're storing the component on a custom palette, do this before you add the   component to the palette.  --- |

[!Table of Contents](Advanced.book.md)
[!Next Section](CreatePalette.md)
