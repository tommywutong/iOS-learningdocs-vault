---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Debugging/DebuggingCompiled.html
archived_at: '2026-07-15T07:46:39.676352Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DevTasks.book.md) [!Previous Section](DebuggingScript.md)

# Debugging a Compiled Application

If you have an application that contains both compiled code and WebScript, do the following:

- Launch your debugger.
- Set breakpoints in the compiled code.
- Launch the application's executable in the debugger.

For example, if you are using __gdb__, you would type the following:

```
    (gdb) run -d /NextLibrary/WebServer/htdocs
        MyApplications/Registration
```

- In your browser, open the URL you'd normally use to launch your application. For example:

```
    http://localhost/cgi-bin/WebObjects/MyApplications/Registration
```


To debug the WebScript portion of the application, you still use __logWithFormat:__ and trace statements as described in "[Debugging WebScript](DebuggingScript.md#apple-gi4donq)." The output from these messages is displayed wherever your debugger displays standard error messages.

