---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/Compiled/mainMethod.html
archived_at: '2026-07-15T07:48:31.471196Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](compiled.book.md) [!Previous Section](NewProject.md)

## The main method

The __Application.java__ file that WebObjects Builder creates contains the application's __main__ method:

```
import next.util.*;
import next.wo.*;

public class Application extends WebApplication {
    public static void main (String args[]) {
            ProcessInfo.setCommandLineArguments(args);
            Application application = new Application();
            application.run();
    }
}
```


The Application class is declared to be a subclass of WebApplication. The __main__ method instantiates the Application object and starts the request-response loop. Before doing so, it sends the application's NSProcessInfo object the command-line arguments so that WebObjects can properly initialize its defaults. (The command-line arguments contain the document root and the name of the WebObjects application under the document root.)

[!Table of Contents](compiled.book.md) [!Next Section](Frameworks.md)
