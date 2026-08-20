---
title: Dashboard Programming Topics
apple_id: TP40002837
resource_type: Guide
platform: Safari|macOS
topic: Networking, Internet, & Web
technology: null
published: '2010-02-01'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashboard_ProgTopics/CopyAndPaste.html
archived_at: '2026-07-15T05:17:34.778467Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashboard Programming Topics](Introduction%20to%20Dashboard%20Programming%20Topics.md)


[Next](Dragging%20and%20Dropping.md)[Previous](Drawing%20Content.md)

# Cutting, Copying, and Pasting

Safari, Dashboard, and WebKit-based applications include support to let you handle cut, copy, and paste operations of your HTML content.

Support for clipboard operations is implemented in JavaScript and may be applied to any element of your HTML page. To handle these operations, you provide functions to handle any of six JavaScript events:

- `onbeforecut`
- `oncut`
- `onbeforecopy`
- `oncopy`
- `onbeforepaste`
- `onpaste`

You can provide handlers for the `oncut`, `oncopy`, and `onpaste` events if you want to define custom behavior for the corresponding operations. You can also provide handlers for the `onbeforecut`, `onbeforecopy`, and `onbeforepaste` events if you want to manipulate the target data before it is actually cut, copied, or pasted.

If your `oncut`, `oncopy`, and `onpaste` handlers do the actual work of cutting, copying, or pasting the data, your handler must call the `preventDefault` method of the event object. This method takes no parameters and notifies WebKit that your handler takes care of moving the data to or from the clipboard. If you do not call this method, WebKit takes responsibility for moving the data. You do not need to call `preventDefault` if you simply want to be notified when the events occur.

You can add handlers for clipboard events to any element in a webpage. When a clipboard operation begins, WebKit looks for the appropriate handler on the element that is the focus of the operation. If that element does not define a handler, WebKit walks up the list of parent elements until it finds one that does. (If no element defines a handler, WebKit applies the default behavior.) To demonstrate this process, suppose you have the following basic HTML in a webpage:

```
<body oncut="MyBodyCutFunction()"
        oncopy="MyBodyCopyFunction()"
        onpaste="MyBodyPasteFunction()">
    <span onpaste="MySpanPasteFunction()">Cut, copy, or paste here.</span>
</body>
```

If a user initiates a cut or copy operation on the text in the `span` tag, WebKit calls `MyBodyCutFunction` or `MyBodyCopyFunction` to handle the event. However, if the user tries to paste text into the span tag, WebKit calls the `MySpanPasteFunction` to handle the event. The `MyBodyPasteFunction` function would be called only if the paste operation occurred outside of the `span` tag.

When an event occurs, your handler uses the `clipboardData` object attached to the event to get and set the clipboard data. This object defines the `clearData`, `getData`, and `setData` methods to allow you to clear, get, and set the clipboard data.

WebKit’s clipboard implementation supports data types beyond those that are typically found in HTML documents. When you call either `getData` or `setData`, you specify the MIME type of the target data. For types it recognizes, including standard types found in HTML documents, WebKit maps the type to a known clipboard type. However, you can also specify MIME types that correspond to any custom data formats your application understands. For most clipboard operations, you will probably want to work with simple data types, such as plain text or a list of URIs.

WebKit also supports the ability to post the same data to the clipboard in multiple formats. To add another format, you simply call `setData` once for each format, specifying the format’s MIME type and a string of data that conforms to that type.

To get a list of types currently available on the clipboard, you can use the `types` property of the `clipboardData` object. This property contains an array of strings with the MIME types of the available data.

[Next](Dragging%20and%20Dropping.md)[Previous](Drawing%20Content.md)

