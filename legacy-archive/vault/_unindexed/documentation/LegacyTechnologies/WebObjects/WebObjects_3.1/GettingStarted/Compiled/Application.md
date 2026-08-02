---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/Compiled/Application.html
archived_at: '2026-07-15T07:48:10.476049Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](compiled.book.md) [!Previous Section](Person.md)

# Implement Application.java

In the previous section, you implemented a class named RegistrationManager, which maintains the list of registrants. You need to create an instance of RegistrationManager. Create the instance in __Application.java__.

- In WebObjects Builder, open the Registration application window.
- Click the Application tab.
- Choose Tools ! Script ! Scripts to open the Script window.
!

Instead of displaying a script, this window displays the __Application.java__ file. __Application.java__ defines an class named Application to be a subclass of WebApplication, and it shows the __main__ method that WebObjects Builder provided for you.

- Implement __Application.java__ as shown below. (Don't change the __main__ method.)

```
    import next.util.*;
    import next.wo.*;

    public class Application extends WebApplication {

        private protected RegistrationManager manager;

        public static void main (String args[]) {
            ProcessInfo.setCommandLineArguments(args);
            Application application = new Application();
            application.run();
        }

        public Application() {
            super();
            manager = new RegistrationManager();
        }

        public RegistrationManager manager() {
            return manager;
        }

    }
```


In addition to declaring the RegistrationManager instance variable and initializing it in a constructor, you also need to create an accessor method named __manager__. Components will use the __manager__ method to access the RegistrationManager object. Because you're writing a compiled application, you need to write the __manager__ method yourself. If you were using WebScript, __manager__ would be implicitly implemented when you declared the __manager__ instance variable.
You can edit the file __Application.java__ in Project Builder, but you must be careful if you do. WebObjects Builder does not detect if files have been edited externally. If you make a change in __Application.java__ using Project Builder and then edit it in WebObjects Builder, WebObjects Builder will overwrite the previous changes. If you want to edit files externally, make sure that you only have the file open in one application at a time, and always close the file as you move from one application to the next. To avoid the problem entirely, it's a good rule of thumb to edit custom objects in Project Builder and edit component logic in WebObjects Builder.

[!Table of Contents](compiled.book.md) [!Next Section](MainComponent.md)
