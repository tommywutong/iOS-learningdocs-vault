---
title: WebKit DOM Programming Topics
apple_id: TP40001483
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: WebKit
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/DragAndDrop.html
archived_at: '2026-07-15T05:18:10.333801Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit DOM Programming Topics](index.md)



## Dragging and Dropping

Safari and WebKit-based applications include support for customizing the behavior of drag-and-drop operations within your HTML pages.

> [!NOTE]
> 

### About JavaScript Drag and Drop

Support for drag-and-drop operations is implemented in JavaScript and may be applied to individual elements of your HTML page. For drag operations, an element can handle the following JavaScript events:

- `ondragstart`
- `ondrag`
- `ondragend`

The `ondragstart` event initiates the drag operation. You can provide a handler for this event to initiate or cancel drag operations selectively. To cancel a drag operation, call the `preventDefault` method of the event object. To handle an event, assign a value to the `effectAllowed` property and put the data for the drag in the `dataTransfer` object, which you can get from the event object. See [Changing Drag Effects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgiztgljrg43tembw) for information on the `effectAllowed` property. See [Manipulating Dragged Data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgiztgljrg43tcmjz) for information on handling the drag data.

Once a drag is underway, the `ondrag` event is fired continuously at the element to give it a chance to perform any tasks it wants to while the drag is in progress. Upon completion of the operation, the element receives the `ondragend` event. If the drag was successful, the `ondrop` handler for the drop target element is also called (before the `ondragend` handler is called).

While a drag is in progress, events are sent to elements that are potential drop targets for the contents being dragged. Those elements can handle the following events:

- `ondragenter`
- `ondragover`
- `ondragleave`
- `ondrop`

The `ondragenter` and `ondragleave` events let the element know when the user’s mouse enters or leaves the boundaries of the element. You can use these events to change the cursor or provide feedback as to whether a drop can occur on an element. The `ondragover` event is sent continuously while the mouse is over the element to give it a chance to perform any needed tasks. If the user releases the mouse button, the element receives an `ondrop` event, which gives it a chance to incorporate the dropped content.

If you implement handlers for the `ondragenter` and `ondragover` events, you should call the `preventDefault` method of the event object. This method takes no parameters and notifies WebKit that your handler will act as the receiver of any incoming data. If you do not call this method, WebKit receives the data and incorporates it for you. You do not need to call `preventDefault` if you simply want to be notified when the events occur.

> [!NOTE]
> 

### Adding Handlers to Elements

You can add handlers for drag-and-drop events to any element in a webpage. When a drag or drop operation occurs, WebKit looks for the appropriate handler on the element that is the focus of the operation. If that element does not define a handler, WebKit walks up the list of parent elements until it finds one that does. If no element defines a handler, WebKit applies the default behavior. To demonstrate this process, suppose you have the following basic HTML in a webpage:

1. `<body ondragstart="BodyDragHandler()"`
2. `ondragend="BodyDragEndHandler()">`
3. `<span ondragstart="SpanDragHandler()">Drag this text.</span>`
4. `</body>`

If a user initiates a drag operation on the text in the `span` tag, WebKit calls `SpanDragHandler` to handle the event. When the drag operation finishes, WebKit calls the `BodyDragEndHandler` to handle the event.

### Making an Element Draggable

WebKit provides automatic support to let users drag common items, such as images, links, and selected text. You can extend this support to include specific elements on an HTML page. For example, you could mark a particular `div` or `span` tag as draggable.

To mark an arbitrary element as draggable, add the `-webkit-user-drag` attribute to the style definition of the element. Because `-webkit-user-drag` is a cascading style sheet (CSS) attribute, you can include it as part of a style definition, or as an inline style attribute on the element tag. The values for this attribute are listed in Table 4-1.

__Table 4-1__Values for -webkit-user-drag attribute

| Value | Description |
| --- | --- |
| `none` | Do not allow this element to be dragged. |
| `element` | Allow this element to be dragged. |
| `auto` | Use the default logic for determining whether the element should be dragged. (Images, links, and text selections are the only elements that can be dragged.) This is the default value. |

The following example shows how you might use this attribute in a `span` tag to permit the dragging of the entire tag. When the user clicks on the `span` text, WebKit identifies the span as being draggable and initiates the drag operation.

1. `<span style="color:rgb(22,255,22); -webkit-user-drag:element;">draggable text</span>`

### Manipulating Dragged Data

When an event occurs, your handler uses the `dataTransfer` object attached to the event to get and set the clipboard data. This object defines the `clearData`, `getData`, and `setData` methods to allow you to clear, get, and set the data on the dragging clipboard.

> [!NOTE]
> 

Unlike many other browsers, the WebKit drag-and-drop implementation supports data types beyond those that are found in HTML documents. When you call either `getData` or `setData`, you specify the MIME type of the target data. For types it recognizes, WebKit maps the type to a known clipboard type. However, you can also specify MIME types that correspond to any custom data formats your application understands. For most drag-and-drop operations, you will probably want to work with simple data types, such as plain text or a list of URIs.

Like applications, WebKit supports the ability to post the same data to the clipboard in multiple formats. To add another format, you simply call the `setData` method with a different MIME type and a string of data that conforms to that type.

To get a list of types currently available on the clipboard, you can use the `types` property of the `dataTransfer` object. This property contains an array of strings with the MIME types of the available data.

### Changing Drag Effects

When dragging content from one place to another, it might not always make sense to move that content permanently to the destination. You might want to copy the data or create a link between the source and destination documents instead. To handle these situations, you can use the `effectAllowed` and `dropEffect` properties of the `dataTransfer` object to specify how you want data to be handled.

The `effectAllowed` property tells WebKit what types of operation the source element supports. You would typically set this property in your `ondragstart` event handler. The value for this property is a string, whose value can be one of those listed in Table 4-2.

__Table 4-2__Options for dragging and dropping an element

| Value | Description |
| --- | --- |
| `none` | No drag operations are allowed on the element. |
| `copy` | The contents of the element should be copied to the destination only. |
| `link` | The contents of the element should be shared with the drop destination using a link back to the original. |
| `move` | The element should be moved to the destination only. |
| `copyLink` | The element can be copied or linked. |
| `copyMove` | The element can be copied or moved. This is the default value. |
| `linkMove` | The element can be linked or moved. |
| `all` | The element can be copied, moved, or linked. |

The `dropEffect` property specifies the single operation supported by the drop target (`copy`, `move`, `link`, or `none`). When an element receives an `ondragenter` event, you should set the value of this property to one of those values, preferably one that is also listed in the `effectAllowed` property. If you do not specify a value for this property, WebKit chooses one based on the available operations (as specified in `effectAllowed`). Copy operations have priority over move operations, which have priority over link operations.

When these properties are set by the source and target elements, WebKit displays feedback to the user about what type of operation will occur if the dragged element is dropped. For example, if the dragged element supports all operations but the drop target only supports copy operations, WebKit displays feedback indicating a copy operation would occur.

### Changing the Appearance of Dragged Elements

During a drag operation, WebKit provides feedback to the user by displaying an image of the dragged content under the mouse. The default image used by WebKit is a snapshot of the element being dragged, but you can change this image to suit your needs.

### Changing the Snapshot With CSS

The simplest way to change the drag image appearance is to use cascading style sheet entries for draggable elements. WebKit defines the `-webkit-drag` pseudoclass, which you can use to modify the style definitions for a particular class during a drag operation. To use this pseudoclass, create a new empty style sheet class entry with the name of the class you want to modify, followed by a a colon and the string `-webkit-drag`. In the style definition of this new class, change or add attributes to specify the differences in appearance between the original element and the element while it is being dragged.

The following example shows the style sheet definition for an element. During normal display, the appearance of the element is determined by the style sheet definition of the `divSrc4` class. When the element is dragged, WebKit changes the background color to match the color specified in the `divSrc4:-webkit-drag` pseudoclass.

1. `#divSrc4 {`
2. `display:inline-block;`
3. `margin:6;`
4. `position:relative;`
5. `top:20px;`
6. `width:100px;`
7. `height:50px;`
8. `background-color:rgb(202,232,255);`
9. `}`
11. `#divSrc4:-webkit-drag {`
12. `background-color:rgb(255,255,154)`
13. `}`

### Specifying a Custom Drag Image

Another way to change the drag image for an element is to specify a custom image. When a drag operation begins, you can use the `setDragImage` method of the `dataTransfer` object. This method has the following definition:

1. `function setDragImage(image, x, y)`

The `image` parameter can contain either a JavaScript Image object or another element. If you specify an Image object, WebKit uses that image as the drag image for the element. If you specify an element, WebKit takes a snapshot of the element you specify (including its child elements) and uses that snapshot as the drag image instead.

The `x` and `y` parameters of `setDragImage` specify the point of the image that should be placed directly under the mouse. This value is typically the location of the mouse click that initiated the drag, with respect to the upper-left corner of the element being manipulated.

Unfortunately, obtaining this information in a cross-browser fashion is easier said than done. There is no standard way to determine the position of the mouse relative to the document because different browsers implement the standard event values in subtly incompatible ways.

For the purposes of Safari and WebKit, `clientX` and `clientY` are document relative, as are `pageX` and `pageY` (which are thus always equal to `clientX` and `clientY`).

Obtaining the position of the element under the mouse is somewhat easier. QuirksMode has a page (with code samples) on the subject at [http://www.quirksmode.org/js/findpos.html](http://www.quirksmode.org/js/findpos.html).

### Drag-and-Drop Example

No description of drag-and-drop would be complete without a working example. Save this into an HTML file and open it in Safari. You should see a very simple set of boxes containing words. If you drag each word box into the blue “target” box, the box will disappear and the word will appear in its correct place to form the phrase “This is a test”.

1. `<!DOCTYPE html>`
2. `<html>`
3. `<head>`
4. `<title>Drag-and-Drop</title>`
6. `<script><!--`
7. `var dragitem = undefined;`
9. `function setdragitem(item, evt) {`
10. `dragitem=item;`
11. `// alert('item: '+item);`
12. `// item is an HTML DIV element.`
13. `// evt is an event.`
15. `// If the item should not be draggable, enable this next line.`
16. `// evt.preventDefault();`
18. `return true;`
19. `}`
20. `function cleardragitem() {`
21. `dragitem=undefined;`
22. `// alert('item: '+item);`
23. `}`
24. `function dodrag() {`
25. `// alert('item: '+dragitem);`
26. `}`
28. `// This is required---used to tell WebKit that the drag should`
29. `// be allowed.`
30. `function handledragenter(elt, evt) {`
31. `evt.preventDefault();`
32. `return true;`
33. `}`
34. `function handledragover(elt, evt) {`
35. `evt.preventDefault();`
36. `return true;`
37. `}`

40. `function handledragleave(elt, evt) {`
42. `}`
44. `function handledrop(elt, evt) {`
45. `// alert('drop');`
46. `dragitem.style.display="none";`
47. `var newid=dragitem.id + '_dest';`
48. `var dest = document.getElementById(newid);`
49. `dest.innerHTML = dragitem.innerHTML;`
50. `}`

53. `// --></script>`
55. `<style><!--`
57. `.wordbox { border: 1px solid black; text-align: center; width: 50px; float: left; -webkit-user-drag: element; -webkit-user-select: none; }`
58. `.spacer { clear: both; }`
59. `.target { margin-top: 30px; padding: 30px; width: 70px; border: 1px solid black; background: #c0c0ff; margin-bottom: 30px; -webkit-user-drop: element; }`
60. `.word { margin: 30px; min-height: 30px; border-bottom: 1px solid black; width: 50px; float: left; }`
62. `--></style>`
64. `</head>`
65. `<body>`
67. `<p>Drop words onto target area to put them in their places.</p>`
69. `<div class='wordbox' id='this' ondragstart='setdragitem(this, event);' ondrag='dodrag();' ondragend='cleardragitem();'>This</div>`
70. `<div class='wordbox' id='is' ondragstart='setdragitem(this, event);' ondrag='dodrag();' ondragend='cleardragitem();'>is</div>`
71. `<div class='wordbox' id='a' ondragstart='setdragitem(this, event);' ondrag='dodrag();' ondragend='cleardragitem();'>a</div>`
72. `<div class='wordbox' id='test' ondragstart='setdragitem(this, event);' ondrag='dodrag();' ondragend='cleardragitem();'>test</div>`
74. `<div class='spacer'></div>`
75. `<div class='target' ondragenter='handledragenter(this, event);' ondragover='handledragover(this, event);' ondragleave='handledragleave(this, event);' ondrop='handledrop(this, event);'>TARGET</div>`
77. `<div class='words'>`
78. `<div class='word' id='this_dest'></div>`
79. `<div class='word' id='is_dest'></div>`
80. `<div class='word' id='a_dest'></div>`
81. `<div class='word' id='test_dest'></div>`
82. `</div>`

85. `</body>`
86. `</html>`

[Cutting, Copying, and Pasting](CopyAndPaste.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgiztilkciffeosskifea)

[Responding to Force Touch Events](RespondingtoForceTouchEventsfromJavaScript.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dcnrsfvjvomi)
