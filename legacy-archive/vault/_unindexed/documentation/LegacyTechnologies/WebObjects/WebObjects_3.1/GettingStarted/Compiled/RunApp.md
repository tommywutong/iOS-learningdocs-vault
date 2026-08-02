---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/Compiled/RunApp.html
archived_at: '2026-07-15T07:48:28.968297Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](compiled.book.md) [!Previous Section](Build.md)

# Run the application

After the project builds succesfully, you're ready to run it. The first time you run an application, you usually want to start it manually so that you can see any error messages that might appear.
Running a compiled WebObjects application is a little different from running a scripted WebObjects application. Scripted WebObjects applications have no executable file, so they use the default executable __WODefaultApp__. Compiled WebObjects applications do have an executable, so that's what you use to run the program. Your application's executable takes the same arguments as __WODefaultApp__.
The command you use to run the Registration application is:

```
Registration.exe -d DocumentRoot Registration
```


The two arguments to the executable specify the document root and the path to the application directory relative to the _<DocumentRoot>___/WebObjects__ directory. The example Registration application shown here was stored directly in _<DocumentRoot>___/WebObjects__. If you've created yours in a subdirectory, the final argument will be a relative path (for example, MyWebApps/Registration).
See "Run the application" in "Creating a Simple WebObjects Application" if you need additional help with this step.
When you start up Registration in your web browser, you'll see the Main page. Try typing in a few names to see how your application works. Be sure to try leaving out information to see the error messages that the Person class provides. Also, click Show All Registrants to see your list.
__Note:__  On Windows NT, if you want to be able to autostart the application from the web browser, you must make a copy of the file __Registration.exe__ named __Registration__. Both files must be in the same directory.

[!Table of Contents](compiled.book.md) [!Next Section](Deploy.md)
