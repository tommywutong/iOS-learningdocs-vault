---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Topics/ProgrammingTopics.c.html
archived_at: '2026-07-15T08:10:01.230261Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Programming Topics

[!](WebObjects%20Programming%20Topics.md) [!](Mixing%20Languages%20in%20an%20Application.md) [!](Handling%20International%20Character%20Sets%20with%20EOF.md)

#   Localizing a WebObjects Application

##  Synopsis

Describes the steps needed to localize your application for different languages.

##  Description

###  Resource Organization

WebObjects relies on a specific application directory structure to find localized resources. The resources are placed in
.lproj
subdirectories of the
Resources
and
WebServerResources
directories.

```

MyApp.woa/

  Resources/

    English.lproj/

      MyApplicationWide.strings

      Main.wo/

        Main.html

        Main.wod

        Main.woo

    French.lproj/

      MyApplicationWide.strings

      Main.wo/

        Main.html

        Main.wod

        Main.woo

  WebServerResources/

    English.lproj/

      Flag.gif

    French.lproj/

      Flag.gif
```


The
.lproj
subdirectories should contain everything that has localized content: string tables, sounds, images, and so on. The
Resources
directory contains resources that your WebObjects application uses, including
.wo
directories (containing components) and
.strings
files (containing localized strings). The
WebServerResources
directory contains resources that the web server needs, such as
.gif
and
.jpg
files. When WebObjects needs a resource, it searches the
.lproj
subdirectories before the top-level resource directory to ensure that if a localized resource is available, it is used. Thus, you need to be sure there are no files of the same name in localized locations when no localization is supposed to occur.

###  Project Builder Support

Project Builder maintains a Resources suitcase and a WebServerResources suitcase corresponding to the directories in the application, and creates the application directory structure from the contents of these suitcases. To add a localized resource file to your project, you first need to create a non-localized file, add it to the appropriate suitcase using Project->Add Files, and localize it using the following steps.

Select the file and open the inspector.

1. 

   Select File Attributes.
2. 

   Click Localized, and check the languages to support.
3. 

   Click Apply.

Project Builder creates copies of the resource in the appropriate
.lproj
folders and offers to remove the global (non-localized) version from the disk. Components can be localized in the same way.

###  Setting the Supported Languages

To tell WebObjects the languages your application supports, use WOSession's
setLanguages
method, as shown in the code below.

####  Java Code

```

public Session() {
    NSMutableArray languages = new NSMutableArray();
    languages.addObject("English");
    languages.addObject("French");
    this.setLanguages (languages);
}
```


The order of languages in the NSArray indicates the preferred order. The names of the languages are the names of the corresponding
.lproj
subdirectories.

###  Determining the User's Language Preferences

You can determine the language of the request sender by sending a
browserLanguages
message to the WORequest object. The
browserLanguages
method returns an array of language preferences from the user's browser converted to the same format that WOSession's
setLanguages
method understands. The following code shows how to determine the user's language preferences from a component.

####  Java Code

```

NSArray languages = this.context().request().browserLanguages();
```

###  Using Localized Strings

A
.strings
file contains a simple property list that maps common keys to words, phrases, or sentences in a particular language. For instance, a
MyApplicationWide.strings
file in
English.lproj
might have the following content:

```

{

  buttonTitle = "Submit your request";

}
```


The
MyApplicationWide.strings
file in
French.lproj
would have the following:

```

{

  buttonTitle = "Soumettez votre requete";

}
```


To access the
.strings
file use the WOResourceManager
stringForKey
method (
stringForKey:inTableNamed:withDefaultValue:inFramework:languages:
in Objective-C). For example, the following code implements an accessor method that can be bound to a button's value attribute.

####  Java Code

```

public String buttonValue() {
    NSArray languages = this.context().request().browserLanguages();
    WOResourceManager rm = this.application().resourceManager();
    return rm.stringForKey ("buttonTitle","MyApplicationWide",
        null,null,languages);
}
```

##  See Also

- 

  [Handling International Character Sets with EOF](Handling%20International%20Character%20Sets%20with%20EOF.md#apple-ge3tsnrx)
- 

  WXLocalizedString and WXLocalizedComponent component-based dynamic elements in the
  ComponentElements
  example framework.
- 

  LocalizedHelloWorld
  example.

##  Questions

- 

  How do I localize my application?
- 

  How do I include localized resources in my project?
- 

  How do I determine the user's language preferences?
- 

  How are my localized resources organized?

##  Keywords

- 

  Localization

##  Revision History

12 February, 1999. Clif Liu. First Draft.

```

```

---

© 1999 Apple Computer, Inc.

[!](WebObjects%20Programming%20Topics.md) [!](Mixing%20Languages%20in%20an%20Application.md) [!](Handling%20International%20Character%20Sets%20with%20EOF.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
